from huggingface_hub import login
login("hf_xxx")  # replace with your actual token

import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig
import os
from datetime import datetime

# ============================================
# IMPORTANT: Library Dependencies
# ============================================

# pip install --upgrade transformers bitsandbytes accelerate

# ============================================

# ============================================
# STORY PROMPT
# ============================================

STORY_PROMPT = """You are a master storyteller. Your task is to rewrite the classic fairy tale 'The Shoemaker and the Elves' into a **dystopian science-fiction story**.

**Your rewrite must adhere to the following rules but should also go beyond them with unexpected twists not stated below:**
* **Setting:** A grimy, neon-lit metropolis in the year 2242, where citizens are judged by their cybernetic enhancements.
* **The 'Shoemaker':** He is a reclusive old craftsman who illegally repairs and builds custom bio-mechanical limbs for outcasts.
* **The 'Elves':** They are a swarm of self-replicating nanobots that are believed to be a myth.
* **The 'Shoes':** The nanobots are not making shoes; they are performing impossibly intricate upgrades on the limbs the craftsman leaves on his workbench overnight.
* **Tone:** The story should be grim, mysterious, and slightly hopeful.
* **Ending:** The story must end with the craftsman discovering the nanobots and leaving a small charging plate with a micro-drop of refined energy for them as a gift, without ever seeing them directly."""

# ============================================
# MODEL LOADING FUNCTION
# ============================================

def load_base_model(base_model_id="google/gemma-2-2b-it"):
    """Load the original base model without fine-tuning"""
    
    print("Loading original base model with quantization...")
    
    bnb_config = BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_quant_type="nf4",
        bnb_4bit_compute_dtype=torch.bfloat16,
        bnb_4bit_use_double_quant=True
    )
    
    base_model = AutoModelForCausalLM.from_pretrained(
        base_model_id,
        quantization_config=bnb_config,
        device_map="auto",
        trust_remote_code=True,
        torch_dtype=torch.bfloat16,
    )
    
    tokenizer = AutoTokenizer.from_pretrained(base_model_id)
    tokenizer.pad_token = tokenizer.eos_token
    tokenizer.padding_side = "right"
    
    base_model.eval()
    print("✓ Original model loaded successfully!")
    return base_model, tokenizer

# ============================================
# GENERATION FUNCTION
# ============================================

def generate_story(model, tokenizer, prompt, strategy="greedy", temperature=1.0, 
                   top_k=50, top_p=0.9, max_length=1024):
    """Generate story with different decoding strategies"""
    
    # Format input in Gemma's chat template
    formatted_prompt = f"<start_of_turn>user\n{prompt}<end_of_turn>\n<start_of_turn>model\n"
    
    # Tokenize
    inputs = tokenizer(formatted_prompt, return_tensors="pt").to(model.device)
    
    # Generation parameters based on strategy
    gen_kwargs = {
        "max_length": max_length,
        "pad_token_id": tokenizer.eos_token_id,
        "eos_token_id": tokenizer.eos_token_id,
    }
    
    if strategy == "greedy":
        gen_kwargs.update({
            "do_sample": False,
            "num_beams": 1,
        })
        
    elif strategy == "sampling":
        gen_kwargs.update({
            "do_sample": True,
            "temperature": temperature,
        })
        
    elif strategy == "top_k":
        gen_kwargs.update({
            "do_sample": True,
            "temperature": temperature,
            "top_k": top_k,
        })
        
    elif strategy == "top_p":
        gen_kwargs.update({
            "do_sample": True,
            "temperature": temperature,
            "top_p": top_p,
        })
        
    elif strategy == "beam":
        gen_kwargs.update({
            "do_sample": False,
            "num_beams": 5,
            "early_stopping": True,
        })
    
    # Generate
    with torch.no_grad():
        outputs = model.generate(**inputs, **gen_kwargs)
    
    # Decode
    generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    
    # Extract only the model's response
    if "<start_of_turn>model" in generated_text:
        response = generated_text.split("<start_of_turn>model")[-1].strip()
    else:
        response = generated_text
    
    return response

# ============================================
# FILE SAVING FUNCTION
# ============================================

def save_story_to_file(filepath, story_text, prompt, strategy, temperature, model_type, top_k=None, top_p=None):
    """Save generated story to a text file with metadata"""
    
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        # f.write("="*80 + "\n")
        # f.write(f"GENERATED STORY - {model_type.upper()}\n")
        # f.write("="*80 + "\n\n")
        # f.write(f"Model Type: {model_type}\n")
        # f.write(f"Decoding Strategy: {strategy}\n")
        # if temperature is not None:
        #     f.write(f"Temperature: {temperature}\n")
        # if top_k is not None:
        #     f.write(f"Top-K: {top_k}\n")
        # if top_p is not None:
        #     f.write(f"Top-P: {top_p}\n")
        # f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        # f.write("\n" + "="*80 + "\n")
        # f.write("PROMPT:\n")
        # f.write("="*80 + "\n")
        # f.write(prompt + "\n")
        # f.write("\n" + "="*80 + "\n")
        # f.write("GENERATED STORY:\n")
        # f.write("="*80 + "\n\n")
        f.write(story_text)
        # f.write("\n\n" + "="*80 + "\n")

# ============================================
# MAIN GENERATION FUNCTION
# ============================================

def generate_all_stories(base_model, tokenizer, output_dir="story_output"):
    """Generate stories organized by decoding strategy with temperature variations"""
    
    print("\n" + "="*80)
    print("GENERATING STORIES WITH THE BASE MODEL")
    print("="*80 + "\n")
    
    # Define configuration for each decoding strategy
    strategies_config = [
        {
            "name": "greedy",
            "temperatures": [None],  # Greedy doesn't use temperature
            "extra_params": {}
        },
        {
            "name": "sampling",
            "temperatures": [0.3, 0.5, 0.7, 0.9],
            "extra_params": {}
        },
        {
            "name": "top_k",
            "temperatures": [0.3, 0.5, 0.7, 0.9],
            "extra_params": {"top_k": 50}
        },
        {
            "name": "top_p",
            "temperatures": [0.3, 0.5, 0.7, 0.9],
            "extra_params": {"top_p": 0.9}
        },
        {
            "name": "beam",
            "temperatures": [None],  # Beam search doesn't use temperature
            "extra_params": {}
        }
    ]
    
    total_files = sum(len(config["temperatures"]) for config in strategies_config)
    current_file = 0
    
    # Generate stories for each strategy
    for config in strategies_config:
        strategy_name = config["name"]
        temperatures = config["temperatures"]
        extra_params = config["extra_params"]
        
        print(f"\n{'='*80}")
        print(f"DECODING STRATEGY: {strategy_name.upper()}")
        print(f"{'='*80}")
        
        # Create strategy folder
        strategy_dir = os.path.join(output_dir, strategy_name)
        
        # Generate for each temperature
        for temp in temperatures:
            temp_str = "default" if temp is None else f"{temp:.1f}"
            
            print(f"\n  Temperature: {temp_str}")
            
            # Prepare generation kwargs
            gen_kwargs = {"strategy": strategy_name, **extra_params}
            if temp is not None:
                gen_kwargs["temperature"] = temp
            
            # ========================================
            # Generate with BASE model
            # ========================================
            current_file += 1
            print(f"    [{current_file}/{total_files}] Generating with BASE model...")
            
            base_story = generate_story(base_model, tokenizer, STORY_PROMPT, **gen_kwargs)
            
            # Create filename
            filename = f"base_{strategy_name}_{temp_str}.txt"
            filepath = os.path.join(strategy_dir, filename)
            
            # Save file
            save_story_to_file(
                filepath, 
                base_story, 
                STORY_PROMPT, 
                strategy_name, 
                temp,
                "BASE MODEL",
                top_k=extra_params.get("top_k"),
                top_p=extra_params.get("top_p")
            )
            print(f"        ✓ Saved: {filename}")
    
    return total_files

# ============================================
# MAIN EXECUTION
# ============================================

if __name__ == "__main__":
    
    # Configuration
    BASE_MODEL_ID = "google/gemma-2-2b-it"
    OUTPUT_DIR = "story_generation_output"
    
    print("\n" + "="*80)
    print("STORY GENERATION SCRIPT")
    print("="*80)
    print(f"\nBase Model: {BASE_MODEL_ID}")
    print(f"Output Directory: {OUTPUT_DIR}")
    print("\n" + "="*80)
    
    # Load model
    print("\nStep 1: Loading model...")
    print("-" * 80)
    base_model, tokenizer = load_base_model(BASE_MODEL_ID)
    
    # Generate all stories
    print("\nStep 2: Generating stories...")
    print("-" * 80)
    total_files = generate_all_stories(base_model, tokenizer, OUTPUT_DIR)
    
    # Summary
    print("\n" + "="*80)
    print("GENERATION COMPLETE!")
    print("="*80)
    print(f"\nTotal files generated: {total_files}")
    print(f"Output location: {OUTPUT_DIR}/")
    print("\nFolder structure:")
    print(f"  {OUTPUT_DIR}/")
    print(f"  ├── greedy/")
    print(f"  │   └── base_greedy_default.txt")
    print(f"  ├── sampling/")
    print(f"  │   ├── base_sampling_0.3.txt")
    print(f"  │   ├── base_sampling_0.5.txt")
    print(f"  │   └── ...")
    print(f"  ├── top_k/")
    print(f"  │   └── ...")
    print(f"  ├── top_p/")
    print(f"  │   └── ...")
    print(f"  └── beam/")
    print(f"      └── ...")
    print("\nEach file contains:")
    print("  • Model type")
    print("  • Generation parameters")
    print("  • The full prompt")
    print("  • The generated story text")
    print("\n" + "="*80)

