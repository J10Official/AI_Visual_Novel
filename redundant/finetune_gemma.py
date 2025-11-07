from huggingface_hub import login
login("hf_xxx")  # replace with your actual token

# ============================================
# IMPORTANT: Library Dependencies
# ============================================

# %pip install bitsandbytes

# ============================================

import json
import torch
import glob
from datasets import Dataset
from transformers import (
    AutoTokenizer,
    AutoModelForCausalLM,
    BitsAndBytesConfig,
    TrainingArguments,
    Trainer,
    DataCollatorForLanguageModeling
)
from peft import LoraConfig, get_peft_model, prepare_model_for_kbit_training

# ============================================
# PART 1: DATA PREPARATION
# ============================================

def convert_screenplay_to_instructions(json_data):
    """Convert screenplay JSON to instruction-response pairs"""
    instructions = []

    for scene in json_data:
        scene_info = scene.get('SCENE', {})
        script = scene.get('SCRIPT', [])

        location = scene_info.get('LOCATION', 'Unknown Location')
        mood = scene_info.get('MOOD', 'Neutral')
        characters = scene_info.get('CHARACTERS', [])

        # Format 1: Generate complete scene
        instruction = {
            'input': f"Create a scene at {location} with mood: {mood}. Characters: {', '.join(characters)}",
            'output': ''
        }

        output_parts = []
        for line in script:
            character = line.get('CHARACTER', 'Unknown')
            dialogue_text = line.get('LINE', '')
            expression = line.get('EXPRESSION', None)

            if character.lower() == 'narrator':
                output_parts.append(f"[NARRATION] {dialogue_text}")
            else:
                expr = f" ({expression})" if expression and expression.lower() != 'null' else ""
                output_parts.append(f"{character}{expr}: {dialogue_text}")

        instruction['output'] = '\n'.join(output_parts).strip()
        instructions.append(instruction)

        # Format 2: Dialogue continuation
        if len(script) > 2:
            mid = len(script) // 2
            context = script[:mid]
            continuation = script[mid:]

            context_text = '\n'.join([f"{l.get('CHARACTER','Unknown')}: {l.get('LINE','')}" for l in context])
            continuation_text = '\n'.join([f"{l.get('CHARACTER','Unknown')}: {l.get('LINE','')}" for l in continuation])

            instructions.append({
                'input': f"Continue this scene:\n{context_text}",
                'output': continuation_text
            })

        # Format 3: Emotional dialogue
        for line in script:
            character = line.get('CHARACTER', 'Unknown')
            expression = line.get('EXPRESSION', None)
            if character.lower() != 'narrator' and expression and expression.lower() != 'null':
                instructions.append({
                    'input': f"Write dialogue for {character} feeling {expression} at {location}",
                    'output': line.get('LINE', '')
                })

    return instructions


def format_for_gemma(example):
    """Format in Gemma's chat template"""
    return {
        'text': f"<start_of_turn>user\n{example['input']}<end_of_turn>\n<start_of_turn>model\n{example['output']}<end_of_turn>"
    }


def load_all_screenplays(folder_path):
    """Load and combine all screenplay JSONs from a folder"""
    all_data = []
    json_files = glob.glob(f"{folder_path}/*.json")

    print(f"Found {len(json_files)} screenplay files")
    for file in json_files:
        with open(file, 'r') as f:
            data = json.load(f)
            all_data.extend(data)
    return all_data


print("Loading screenplay data from multiple files...")
folder_path = "/kaggle/input/annotated-json"
screenplay_data = load_all_screenplays(folder_path)

print(f"Total scenes loaded: {len(screenplay_data)}")

# Convert to training format
print("Converting to training format...")
training_data = convert_screenplay_to_instructions(screenplay_data)

# Create dataset
dataset_dict = {
    'input': [item['input'] for item in training_data],
    'output': [item['output'] for item in training_data]
}
dataset = Dataset.from_dict(dataset_dict)
formatted_dataset = dataset.map(format_for_gemma)

print(f"Created dataset with {len(formatted_dataset)} examples")

# ============================================
# PART 2: MODEL SETUP (WITH AGGRESSIVE MEMORY CLEANUP)
# ============================================
import os
import gc

# CRITICAL: Clear all GPU memory first
print("Clearing GPU memory...")
if torch.cuda.is_available():
    torch.cuda.empty_cache()
    torch.cuda.synchronize()
    gc.collect()
    
# Try to set memory fragmentation settings
os.environ['PYTORCH_CUDA_ALLOC_CONF'] = 'expandable_segments:True'
os.environ.pop('CUDA_VISIBLE_DEVICES', None)

# Clear any existing GPU memory again
if torch.cuda.is_available():
    for i in range(torch.cuda.device_count()):
        with torch.cuda.device(i):
            torch.cuda.empty_cache()
    gc.collect()

print("Loading model with minimal memory footprint...")
model_id = "google/gemma-2-2b-it"
device = "cuda:0" if torch.cuda.is_available() else "cpu"

# Quantization config for maximum memory efficiency
bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=torch.bfloat16,
    bnb_4bit_use_double_quant=True
)

model = AutoModelForCausalLM.from_pretrained(
    model_id,
    quantization_config=bnb_config,
    device_map={'': torch.cuda.current_device()},  # CRITICAL: Use current_device() for quantized models
    trust_remote_code=True,
    torch_dtype=torch.bfloat16,
    attn_implementation='eager',
    use_cache=False,  # Disable KV cache for training - saves memory
    low_cpu_mem_usage=True,  # Use less CPU memory during loading
)

tokenizer = AutoTokenizer.from_pretrained(model_id)
tokenizer.pad_token = tokenizer.eos_token
tokenizer.padding_side = "right"

# Prepare model for training
model = prepare_model_for_kbit_training(model)
model.config.use_cache = False  # Ensure cache is disabled

# LoRA configuration - keep it small for memory efficiency
lora_config = LoraConfig(
    r=8,
    lora_alpha=16,
    target_modules=["q_proj", "k_proj", "v_proj", "o_proj"],
    lora_dropout=0.05,
    bias="none",
    task_type="CAUSAL_LM"
)

# Apply LoRA adapter
model = get_peft_model(model, lora_config)
trainable, total = model.get_nb_trainable_parameters()
print(f"Trainable parameters: {trainable:,} / {total:,} ({100*trainable/total:.2f}%)")

# Clear memory after model loading
torch.cuda.empty_cache()
gc.collect()
print(f"GPU Memory after model load: {torch.cuda.memory_allocated(0)/1024**3:.2f} GB")

# ============================================
# PART 3: TOKENIZE DATASET
# ============================================

print("Tokenizing dataset...")

def tokenize_function(examples):
    """Tokenize the text field - labels will be created by data collator"""
    return tokenizer(
        examples["text"],
        truncation=True,
        max_length=384,  # Reduced from 512 to save memory
        padding=False,
    )

# Tokenize the dataset
tokenized_dataset = formatted_dataset.map(
    tokenize_function,
    batched=True,
    remove_columns=formatted_dataset.column_names,
    desc="Tokenizing dataset",
)

print(f"Tokenized dataset: {len(tokenized_dataset)} examples")

# ============================================
# PART 4: TRAINING WITH STANDARD TRAINER (MEMORY OPTIMIZED)
# ============================================

training_args = TrainingArguments(
    output_dir="./gemma2-screenplay-checkpoints",
    num_train_epochs=3,
    per_device_train_batch_size=1,  # Reduced to 1 for memory
    gradient_accumulation_steps=16,  # Increased to maintain effective batch size
    gradient_checkpointing=True,
    gradient_checkpointing_kwargs={"use_reentrant": False},  # More memory efficient
    learning_rate=2e-4,
    fp16=True,
    logging_steps=10,
    save_steps=100,
    save_total_limit=1,  # Only keep 1 checkpoint to save space
    save_strategy="steps",  # Save based on steps
    load_best_model_at_end=False,  # Don't load best model (saves memory)
    warmup_ratio=0.1,
    lr_scheduler_type="cosine",
    optim="paged_adamw_8bit",
    max_grad_norm=0.3,
    weight_decay=0.001,
    remove_unused_columns=False,
    report_to="tensorboard",
    ddp_find_unused_parameters=False,  # Memory optimization
    # Additional memory optimizations
    eval_strategy="no",  # Disable evaluation to save memory
    save_safetensors=True,
    dataloader_pin_memory=False,  # Reduce memory overhead
    save_only_model=True,  # Only save model, not optimizer states (saves space)
)

# Data collator - this will automatically create labels from input_ids
data_collator = DataCollatorForLanguageModeling(
    tokenizer=tokenizer,
    mlm=False,  # Causal LM, not masked LM
    pad_to_multiple_of=8,  # For efficiency with tensor cores
)

# Create trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_dataset,
    data_collator=data_collator,
)

# Clear cache before training
import gc
torch.cuda.empty_cache()
gc.collect()

print("Starting training with optimized memory settings...")
print(f"GPU Memory before training: {torch.cuda.memory_allocated(0)/1024**3:.2f} GB")
trainer.train()

# ============================================
# PART 5: SAVE MODEL PROPERLY
# ============================================

print("\n" + "="*50)
print("Saving fine-tuned model...")
print("="*50 + "\n")

# Save the LoRA adapter weights
final_model_path = "./gemma2-screenplay-lora"
model.save_pretrained(final_model_path)
tokenizer.save_pretrained(final_model_path)

# Save configuration for easy reloading
config_info = {
    "base_model": model_id,
    "lora_config": {
        "r": lora_config.r,
        "lora_alpha": lora_config.lora_alpha,
        "target_modules": lora_config.target_modules,
        "lora_dropout": lora_config.lora_dropout,
        "bias": lora_config.bias,
        "task_type": lora_config.task_type
    },
    "quantization_config": {
        "load_in_4bit": True,
        "bnb_4bit_quant_type": "nf4",
        "bnb_4bit_compute_dtype": "bfloat16",
        "bnb_4bit_use_double_quant": True
    }
}

with open(f"{final_model_path}/training_config.json", 'w') as f:
    json.dump(config_info, f, indent=2)

print(f"✓ Model saved to: {final_model_path}")
print(f"✓ Saved files: adapter_config.json, adapter_model.safetensors, tokenizer files, training_config.json")
print(f"\nYou can now load this model later for inference with different parameters!")

print("\nTraining complete!")