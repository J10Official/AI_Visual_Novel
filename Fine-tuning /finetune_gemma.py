# ============================================
# CRITICAL PATCH: Must be FIRST - Prevent 404 errors
# ============================================
import sys
import os

# Set environment variable to suppress warnings
os.environ['TRANSFORMERS_VERBOSITY'] = 'error'

# Patch huggingface_hub BEFORE transformers imports it
import huggingface_hub.hf_api as hf_api

original_list_repo_tree = hf_api.HfApi.list_repo_tree

def patched_list_repo_tree(self, *args, **kwargs):
    """Wrapper that catches 404 errors when listing repo trees"""
    try:
        return original_list_repo_tree(self, *args, **kwargs)
    except Exception as e:
        if "404" in str(e) or "EntryNotFound" in str(e):
            # Return empty iterator for missing folders
            return iter([])
        raise

hf_api.HfApi.list_repo_tree = patched_list_repo_tree

# Also patch the transformers utils module
import transformers.utils.hub as hub_utils

def safe_list_repo_templates(*args, **kwargs):
    """Return empty list for missing chat templates"""
    return []

hub_utils.list_repo_templates = safe_list_repo_templates

print("✓ Applied patches to prevent 404 errors")

# ============================================
# Now import everything else
# ============================================
from huggingface_hub import login
login("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")

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
)
from peft import LoraConfig, get_peft_model, prepare_model_for_kbit_training
import gc


# ============================================
# PART 1: DATA PREPARATION (UPDATED FOR YOUR FORMAT)
# ============================================

def convert_screenplay_to_instructions(json_data):
    """Convert screenplay JSON to instruction-response pairs for your specific format"""
    instructions = []

    for scene in json_data:
        scene_info = scene.get('SCENE', {})
        script = scene.get('SCRIPT', [])
        paths = scene.get('PATHS', [])

        location = scene_info.get('LOCATION', 'Unknown Location')
        mood = scene_info.get('MOOD', 'Neutral')
        characters = scene_info.get('CHARACTERS', [])
        bg_image = scene_info.get('BACKGROUND_IMAGE', '')
        bg_edit = scene_info.get('BACKGROUND_EDIT', '')

        # Training Format 1: Generate complete scene with all elements
        instruction = {
            'input': f"Write a screenplay scene at {location} with {mood} mood. Characters: {', '.join(characters)}",
            'output': ''
        }

        output_parts = []
        
        # Add scene description
        output_parts.append(f"SCENE: {location}")
        output_parts.append(f"MOOD: {mood}")
        output_parts.append(f"CHARACTERS: {', '.join(characters)}")
        if bg_edit:
            output_parts.append(f"SETTING: {bg_edit}")
        output_parts.append("")  # Blank line
        
        # Add script lines
        for line in script:
            character = line.get('CHARACTER', 'Unknown')
            dialogue_text = line.get('LINE', '')
            expression = line.get('EXPRESSION', 'null')

            if character.lower() == 'narrator':
                # Narrator lines are descriptions
                if expression and expression.lower() != 'null':
                    output_parts.append(f"[NARRATION - {expression}] {dialogue_text}")
                else:
                    output_parts.append(f"[NARRATION] {dialogue_text}")
            else:
                # Character dialogue
                if expression and expression.lower() != 'null':
                    output_parts.append(f"{character} ({expression}): {dialogue_text}")
                else:
                    output_parts.append(f"{character}: {dialogue_text}")
        
        # Add paths if available
        if paths:
            output_parts.append("")
            output_parts.append("CHOICES:")
            for path in paths:
                choice = path.get('CHOICE', '')
                target = path.get('TARGET', '')
                output_parts.append(f"- {choice} → {target}")

        instruction['output'] = '\n'.join(output_parts).strip()
        instructions.append(instruction)

        # Training Format 2: Generate narration for a scene
        narrator_lines = [line for line in script if line.get('CHARACTER', '').lower() == 'narrator']
        if narrator_lines:
            instructions.append({
                'input': f"Write narrative descriptions for a {mood} scene at {location}",
                'output': '\n'.join([f"[NARRATION] {line.get('LINE', '')}" for line in narrator_lines])
            })

        # Training Format 3: Generate dialogue continuation
        dialogue_lines = [line for line in script if line.get('CHARACTER', '').lower() != 'narrator']
        if len(dialogue_lines) >= 2:
            # Split dialogue for continuation task
            mid = len(dialogue_lines) // 2
            context = dialogue_lines[:mid]
            continuation = dialogue_lines[mid:]

            context_text = '\n'.join([
                f"{l.get('CHARACTER','Unknown')}: {l.get('LINE','')}" 
                for l in context
            ])
            continuation_text = '\n'.join([
                f"{l.get('CHARACTER','Unknown')}: {l.get('LINE','')}" 
                for l in continuation
            ])

            instructions.append({
                'input': f"Continue this dialogue in a {mood} scene at {location}:\n{context_text}",
                'output': continuation_text
            })

        # Training Format 4: Generate scene with specific emotional expression
        for line in script:
            character = line.get('CHARACTER', 'Unknown')
            expression = line.get('EXPRESSION', 'null')
            if expression and expression.lower() not in ['null', 'none']:
                instructions.append({
                    'input': f"Write a line for {character} feeling {expression} in a {mood} scene at {location}",
                    'output': line.get('LINE', '')
                })

        # Training Format 5: Generate complete scene from minimal info
        if len(script) >= 3:  # Only if scene has enough content
            instructions.append({
                'input': f"Create a {mood} screenplay scene at {location} with characters {', '.join(characters)}. Include narration and dialogue.",
                'output': '\n'.join([
                    f"[NARRATION] {l.get('LINE', '')}" if l.get('CHARACTER', '').lower() == 'narrator'
                    else f"{l.get('CHARACTER', 'Unknown')}: {l.get('LINE', '')}"
                    for l in script
                ])
            })

        # Training Format 6: Generate scene paths/choices
        if paths and len(paths) > 0:
            instructions.append({
                'input': f"What choices could happen next in this {mood} scene at {location}?",
                'output': '\n'.join([f"Choice: {p.get('CHOICE', '')} leads to {p.get('TARGET', '')}" for p in paths])
            })

    return instructions


def load_all_screenplays(folder_path):
    """Load and combine all screenplay JSONs from a folder"""
    all_data = []
    json_files = glob.glob(f"{folder_path}/*.json")

    print(f"Found {len(json_files)} screenplay files")
    for file in json_files:
        with open(file, 'r') as f:
            data = json.load(f)
            # Handle both single scene and array of scenes
            if isinstance(data, list):
                all_data.extend(data)
            else:
                all_data.append(data)
    return all_data


print("Loading screenplay data from multiple files...")
folder_path = "/kaggle/input/annotated-json-gold"
screenplay_data = load_all_screenplays(folder_path)

print(f"Total scenes loaded: {len(screenplay_data)}")

# Convert to training format
print("Converting to training format...")
training_data = convert_screenplay_to_instructions(screenplay_data)

print(f"\n=== Training Data Sample ===")
print(f"Total training examples: {len(training_data)}")
print(f"\nExample 1:")
print(f"INPUT: {training_data[0]['input'][:200]}...")
print(f"OUTPUT: {training_data[0]['output'][:300]}...")

# Create dataset
dataset_dict = {
    'input': [item['input'] for item in training_data],
    'output': [item['output'] for item in training_data]
}
dataset = Dataset.from_dict(dataset_dict)

print(f"\nCreated dataset with {len(dataset)} examples")

# ============================================
# PART 2: MODEL SETUP (WITH AGGRESSIVE MEMORY CLEANUP)
# ============================================

print("\nClearing GPU memory...")
if torch.cuda.is_available():
    torch.cuda.empty_cache()
    torch.cuda.synchronize()
    gc.collect()
    
os.environ['PYTORCH_CUDA_ALLOC_CONF'] = 'expandable_segments:True'
os.environ.pop('CUDA_VISIBLE_DEVICES', None)

if torch.cuda.is_available():
    for i in range(torch.cuda.device_count()):
        with torch.cuda.device(i):
            torch.cuda.empty_cache()
    gc.collect()

print("Loading model with minimal memory footprint...")
model_id = "google/gemma-2-2b-it"

# Quantization config
bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=torch.bfloat16,
    bnb_4bit_use_double_quant=True
)

model = AutoModelForCausalLM.from_pretrained(
    model_id,
    quantization_config=bnb_config,
    device_map={'': torch.cuda.current_device()},
    trust_remote_code=True,
    torch_dtype=torch.bfloat16,
    attn_implementation='eager',
    use_cache=False,
    low_cpu_mem_usage=True,
)

print("Loading tokenizer (404 errors suppressed)...")
tokenizer = AutoTokenizer.from_pretrained(model_id)
tokenizer.pad_token = tokenizer.eos_token
tokenizer.padding_side = "right"

print("✓ Tokenizer loaded successfully")

# Prepare model for training
model = prepare_model_for_kbit_training(model)
model.config.use_cache = False

# LoRA configuration - INCREASED rank for better quality
lora_config = LoraConfig(
    r=16,  # Increased from 8
    lora_alpha=32,  # Increased proportionally
    target_modules=["q_proj", "k_proj", "v_proj", "o_proj"],
    lora_dropout=0.05,
    bias="none",
    task_type="CAUSAL_LM"
)

model = get_peft_model(model, lora_config)
trainable, total = model.get_nb_trainable_parameters()
print(f"Trainable parameters: {trainable:,} / {total:,} ({100*trainable/total:.2f}%)")

torch.cuda.empty_cache()
gc.collect()
print(f"GPU Memory after model load: {torch.cuda.memory_allocated(0)/1024**3:.2f} GB")

# ============================================
# PART 3: TOKENIZE DATASET WITH PROPER MASKING (CRITICAL FIX)
# ============================================

print("\nTokenizing dataset with proper label masking...")

def tokenize_and_mask(examples):
    """
    Tokenize and create labels that only compute loss on the model's response.
    This is CRITICAL to prevent the model from learning to predict the instruction.
    """
    model_inputs = {"input_ids": [], "attention_mask": [], "labels": []}
    
    for inp, out in zip(examples["input"], examples["output"]):
        # Format with proper EOS token (CRITICAL FIX)
        full_text = f"<start_of_turn>user\n{inp}<end_of_turn>\n<start_of_turn>model\n{out}<end_of_turn>{tokenizer.eos_token}"
        
        # Tokenize the full sequence
        tokenized_full = tokenizer(
            full_text,
            truncation=True,
            max_length=768,  # Increased for screenplay format (scenes can be long)
            padding=False,
        )
        
        # Tokenize just the instruction part to find where response starts
        instruction_text = f"<start_of_turn>user\n{inp}<end_of_turn>\n<start_of_turn>model\n"
        tokenized_instruction = tokenizer(
            instruction_text,
            truncation=False,
            padding=False,
        )
        
        # Create labels: -100 for instruction tokens (ignored in loss), actual token ids for response
        labels = [-100] * len(tokenized_instruction["input_ids"]) + \
                 tokenized_full["input_ids"][len(tokenized_instruction["input_ids"]):]
        
        # Ensure labels match input_ids length
        labels = labels[:len(tokenized_full["input_ids"])]
        
        model_inputs["input_ids"].append(tokenized_full["input_ids"])
        model_inputs["attention_mask"].append(tokenized_full["attention_mask"])
        model_inputs["labels"].append(labels)
    
    return model_inputs

# Tokenize with proper masking
tokenized_dataset = dataset.map(
    tokenize_and_mask,
    batched=True,
    remove_columns=dataset.column_names,
    desc="Tokenizing with label masking",
)

print(f"Tokenized dataset: {len(tokenized_dataset)} examples")

# Verify one example
sample = tokenized_dataset[0]
print("\n=== Sample Check ===")
print(f"Input length: {len(sample['input_ids'])}")
print(f"Labels (first 20): {sample['labels'][:20]}")
print(f"Number of -100 (masked): {sum(1 for x in sample['labels'] if x == -100)}")
print(f"Number of trainable tokens: {sum(1 for x in sample['labels'] if x != -100)}")

# Decode to verify
decoded_input = tokenizer.decode(sample['input_ids'][:100])
print(f"\nDecoded sample (first 100 tokens):\n{decoded_input}")

# ============================================
# PART 4: CUSTOM DATA COLLATOR (NO AUTOMATIC LABEL CREATION)
# ============================================

from dataclasses import dataclass
from typing import Any, Dict, List

@dataclass
class CustomDataCollator:
    """
    Custom data collator that uses our pre-computed labels.
    Does NOT overwrite labels like DataCollatorForLanguageModeling does.
    """
    tokenizer: Any
    
    def __call__(self, features: List[Dict[str, Any]]) -> Dict[str, torch.Tensor]:
        # Find max length in batch
        max_length = max(len(f["input_ids"]) for f in features)
        
        # Pad sequences
        input_ids = []
        attention_mask = []
        labels = []
        
        for f in features:
            # Padding
            padding_length = max_length - len(f["input_ids"])
            
            input_ids.append(f["input_ids"] + [self.tokenizer.pad_token_id] * padding_length)
            attention_mask.append(f["attention_mask"] + [0] * padding_length)
            labels.append(f["labels"] + [-100] * padding_length)
        
        return {
            "input_ids": torch.tensor(input_ids, dtype=torch.long),
            "attention_mask": torch.tensor(attention_mask, dtype=torch.long),
            "labels": torch.tensor(labels, dtype=torch.long),
        }

data_collator = CustomDataCollator(tokenizer=tokenizer)

# ============================================
# PART 5: TRAINING WITH IMPROVED PARAMETERS
# ============================================

training_args = TrainingArguments(
    output_dir="./gemma2-screenplay-checkpoints",
    num_train_epochs=3,
    per_device_train_batch_size=1,
    gradient_accumulation_steps=16,
    gradient_checkpointing=True,
    gradient_checkpointing_kwargs={"use_reentrant": False},
    learning_rate=2e-4,
    fp16=True,
    logging_steps=10,
    save_steps=100,
    save_total_limit=2,  # Keep 2 checkpoints for comparison
    save_strategy="steps",
    load_best_model_at_end=False,
    warmup_ratio=0.1,
    lr_scheduler_type="cosine",
    optim="paged_adamw_8bit",
    max_grad_norm=0.3,
    weight_decay=0.001,
    remove_unused_columns=False,
    report_to="tensorboard",
    ddp_find_unused_parameters=False,
    eval_strategy="no",
    save_safetensors=True,
    dataloader_pin_memory=False,
    save_only_model=True,
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_dataset,
    data_collator=data_collator,  # Use our custom collator
)

torch.cuda.empty_cache()
gc.collect()

print("\nStarting training with fixed configuration...")
print(f"GPU Memory before training: {torch.cuda.memory_allocated(0)/1024**3:.2f} GB")
trainer.train()

# ============================================
# PART 6: SAVE MODEL
# ============================================

print("\n" + "="*50)
print("Saving fine-tuned model...")
print("="*50 + "\n")

final_model_path = "./gemma2-screenplay-lora"
model.save_pretrained(final_model_path)
tokenizer.save_pretrained(final_model_path)

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
    },
    "training_notes": "Fixed version with proper EOS tokens and label masking for screenplay format",
    "format": "Screenplay with SCENE, NARRATION, DIALOGUE, and PATHS"
}

with open(f"{final_model_path}/training_config.json", 'w') as f:
    json.dump(config_info, f, indent=2)

print(f"✓ Model saved to: {final_model_path}")
print("\nTraining complete!")

# ============================================
# PART 7: INFERENCE EXAMPLE
# ============================================

print("\n" + "="*50)
print("INFERENCE EXAMPLE:")
print("="*50)
print("""
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
from peft import PeftModel
import torch

# Load base model
base_model = AutoModelForCausalLM.from_pretrained(
    "google/gemma-2-2b-it",
    device_map="auto",
    torch_dtype=torch.bfloat16
)

# Load LoRA adapter
model = PeftModel.from_pretrained(base_model, "./gemma2-screenplay-lora")
tokenizer = AutoTokenizer.from_pretrained("./gemma2-screenplay-lora")

# Create pipeline
pipe = pipeline("text-generation", model=model, tokenizer=tokenizer)

# Generate
prompt = "Create a Weary screenplay scene at Crappy Car Interior with characters Narrator, MIKE ENSLIN. Include narration and dialogue."

output = pipe(
    f"<start_of_turn>user\\n{prompt}<end_of_turn>\\n<start_of_turn>model\\n",
    max_new_tokens=400,
    do_sample=True,
    temperature=0.7,
    top_p=0.9,
    top_k=50,
    repetition_penalty=1.2,      # CRITICAL for preventing repetition
    no_repeat_ngram_size=3,      # Don't repeat 3-word sequences
    pad_token_id=tokenizer.eos_token_id,
    eos_token_id=tokenizer.eos_token_id,
)

print(output[0]['generated_text'])
""")