from huggingface_hub import login
login("hf_xxx")  # replace with your actual token

# ============================================
# IMPORTANT: Library Dependencies
# ============================================

# pip install --upgrade transformers bitsandbytes accelerate

# ============================================

import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig
from peft import PeftModel
import json

# ============================================
# LOAD MODELS
# ============================================

def load_base_model(base_model_id="google/gemma-2-2b-it"):
    """Load the original base model without LoRA"""
    
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
    print("✓ Original base model loaded successfully!")
    return base_model, tokenizer


def load_finetuned_model(lora_path, base_model_id="google/gemma-2-2b-it"):
    """Load the fine-tuned LoRA model"""
    
    print("\nLoading fine-tuned model with quantization...")
    
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
    
    print("Loading LoRA adapter...")
    finetuned_model = PeftModel.from_pretrained(base_model, lora_path)
    finetuned_model.eval()
    
    print("✓ Fine-tuned model loaded successfully!")
    return finetuned_model, tokenizer


# ============================================
# GENERATION FUNCTION (TOP-P STRATEGY)
# ============================================

def generate_screenplay(model, tokenizer, prompt, temperature=0.7, top_p=0.7, max_length=2048):
    """
    Generate screenplay using Top-P (Nucleus) sampling with temperature 0.7
    """
    
    # Format input in Gemma's chat template
    formatted_prompt = f"<start_of_turn>user\n{prompt}<end_of_turn>\n<start_of_turn>model\n"
    
    # Tokenize
    inputs = tokenizer(formatted_prompt, return_tensors="pt").to(model.device)
    
    # Generation parameters - Top-P with temperature 0.7
    gen_kwargs = {
        "max_length": max_length,
        "pad_token_id": tokenizer.eos_token_id,
        "eos_token_id": tokenizer.eos_token_id,
        "do_sample": True,
        "temperature": temperature,
        "top_p": top_p,
    }
    
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
# CREATE STRUCTURED PROMPT
# ============================================

def create_screenplay_prompt(location, mood, characters, background_image=None, 
                             background_edit=None, num_scenes=3):
    """
    Create a structured prompt for screenplay generation
    
    Args:
        location: Starting location (e.g., "Mystical Pond")
        mood: Overall mood (e.g., "Mysterious", "Eerie", "Dark")
        characters: List of characters (e.g., ["Woodcutter", "Pond Spirit"])
        background_image: Optional background image filename
        background_edit: Optional background description
        num_scenes: Number of scenes to generate
    """
    
    if isinstance(characters, list):
        characters_str = ", ".join(characters)
    else:
        characters_str = characters
    
    prompt = f"""Generate a screenplay with {num_scenes} connected scenes in the following format:

::SCENE::
LOCATION: {location}
MOOD: {mood}
CHARACTERS: {characters_str}"""
    
    if background_image:
        prompt += f"\nBACKGROUND_IMAGE: {background_image}"
    
    if background_edit:
        prompt += f'\nBACKGROUND_EDIT: "{background_edit}"'
    
    prompt += """

::SCRIPT::
- CHARACTER: [character name]
  LINE: [dialogue line]
  EXPRESSION: [expression or null]

::PATHS::
- CHOICE: [choice text]
  TARGET: [next scene id]
  STATE_CHANGE: null
  CONDITION: null

Create a complete, interconnected narrative with atmospheric descriptions and meaningful character interactions."""
    
    return prompt


# ============================================
# MAIN COMPARISON
# ============================================

if __name__ == "__main__":
    
    # Configuration
    LORA_PATH = "/kaggle/input/gemma-2-latest/transformers/default/1"
    BASE_MODEL_ID = "google/gemma-2-2b-it"
    
    # Load both models
    print("="*80)
    print("LOADING MODELS FOR COMPARISON")
    print("="*80)
    
    base_model, base_tokenizer = load_base_model(BASE_MODEL_ID)
    finetuned_model, finetuned_tokenizer = load_finetuned_model(LORA_PATH, BASE_MODEL_ID)
    
    # ============================================
    # TEST PROMPTS
    # ============================================
    
    test_prompts = [
        {
            "name": "Abandoned Space Station - Engine Room",
            "prompt": """Generate a screenplay scene in the following format:
::SCENE::
LOCATION: Abandoned Space Station - Engine Room
MOOD: Eerie, Desolate
CHARACTERS: Engineer Maya, Ship AI
BACKGROUND_IMAGE: dark_engine_room.png
BACKGROUND_EDIT: "Vast engine room with flickering emergency lights"
Create the complete scene with ::SCRIPT:: section containing character dialogue and ::PATHS:: section with choices."""
        },
        {
            "name": "Ancient Forest - Sacred Pond",
            "prompt": """Generate a screenplay scene in the following format:
::SCENE::
LOCATION: Ancient Forest - Sacred Pond
MOOD: Mysterious, Enchanted
CHARACTERS: Woodcutter, Pond Spirit
BACKGROUND_IMAGE: mystical_pond.png
BACKGROUND_EDIT: "Moonlit pond surrounded by ancient trees"
Create the complete scene with ::SCRIPT:: section containing character dialogue and ::PATHS:: section with choices."""
        },
        {
            "name": "Neo Tokyo - Rooftop Bar",
            "prompt": """Generate a screenplay scene in the following format:
::SCENE::
LOCATION: Neo Tokyo - Rooftop Bar
MOOD: Tense, Noir
CHARACTERS: Detective Chen, Informant
BACKGROUND_IMAGE: neon_rooftop.png
BACKGROUND_EDIT: "Rain-soaked rooftop with neon signs reflected in puddles"
Create the complete scene with ::SCRIPT:: section containing character dialogue and ::PATHS:: section with choices."""
        },
        {
            "name": "Victorian Mansion - Grand Hall",
            "prompt": """Generate a screenplay scene in the following format:
::SCENE::
LOCATION: Victorian Mansion - Grand Hall
MOOD: Haunting, Suspenseful
CHARACTERS: Investigator, Ghost
BACKGROUND_IMAGE: mansion_hall.png
BACKGROUND_EDIT: "Dust-covered grand hall with covered furniture"
Create the complete scene with ::SCRIPT:: section containing character dialogue and ::PATHS:: section with choices."""
        }
    ]
    
    # ============================================
    # RUN COMPARISONS
    # ============================================
    
    for i, test_case in enumerate(test_prompts, 1):
        print("\n\n" + "="*80)
        print(f"TEST CASE {i}: {test_case['name']}")
        print("="*80)
        
        print("\n" + "-"*80)
        print("PROMPT:")
        print("-"*80)
        print(test_case['prompt'])
        
        # Generate with ORIGINAL model
        print("\n\n" + "-"*80)
        print("ORIGINAL BASE MODEL OUTPUT (Top-P=0.7, T=0.7)")
        print("-"*80)
        base_output = generate_screenplay(
            base_model, 
            base_tokenizer, 
            test_case['prompt'],
            temperature=0.7,
            top_p=0.7
        )
        print(base_output)
        
        # Generate with FINE-TUNED model
        print("\n\n" + "-"*80)
        print("FINE-TUNED MODEL OUTPUT (Top-P=0.7, T=0.7)")
        print("-"*80)
        finetuned_output = generate_screenplay(
            finetuned_model, 
            finetuned_tokenizer, 
            test_case['prompt'],
            temperature=0.7,
            top_p=0.7
        )
        print(finetuned_output)
        
        print("\n" + "="*80)
        print(f"END OF TEST CASE {i}")
        print("="*80)
    
    print("\n\n" + "="*80)
    print("ALL COMPARISONS COMPLETE!")
    print("="*80)
    
    # ============================================
    # ANALYSIS SUMMARY
    # ============================================
    
    print("\n\n" + "="*80)
    print("COMPARISON ANALYSIS")
    print("="*80)
    print("""
Compare the outputs above to evaluate:

1. FORMAT ADHERENCE:
   - Does the fine-tuned model better follow the ::SCENE::, ::SCRIPT::, ::PATHS:: structure?
   - Are the required fields (LOCATION, MOOD, CHARACTERS, etc.) properly formatted?

2. CONTENT QUALITY:
   - Which model generates more coherent narrative flow?
   - Which produces more atmospheric and engaging descriptions?
   - Are character interactions more natural?

3. TECHNICAL ACCURACY:
   - Does the fine-tuned model correctly use EXPRESSION, STATE_CHANGE, CONDITION fields?
   - Are TARGET references logical for scene connections?

4. CREATIVITY VS STRUCTURE:
   - Does the fine-tuned model maintain creativity while following format?
   - Is the base model too free-form or the fine-tuned model too rigid?
    """)


# ============================================
# INTERACTIVE COMPARISON MODE (OPTIONAL)
# ============================================

def interactive_comparison(base_model, base_tokenizer, finetuned_model, finetuned_tokenizer):
    """Interactive mode to test custom prompts on both models"""
    
    print("\n" + "="*80)
    print("INTERACTIVE COMPARISON MODE")
    print("="*80)
    print("Enter screenplay parameters to compare both models")
    
    while True:
        print("\n" + "-"*80)
        choice = input("\n1. Use prompt builder\n2. Enter raw prompt\n3. Quit\n\nChoice: ")
        
        if choice == "3":
            break
        
        if choice == "1":
            location = input("Location: ")
            mood = input("Mood: ")
            characters = input("Characters (comma-separated): ")
            num_scenes = int(input("Number of scenes (default 3): ") or "3")
            
            prompt = create_screenplay_prompt(
                location=location,
                mood=mood,
                characters=characters.split(","),
                num_scenes=num_scenes
            )
        elif choice == "2":
            prompt = input("Enter your full prompt:\n")
        else:
            print("Invalid choice!")
            continue
        
        print("\n" + "="*80)
        print("GENERATING OUTPUTS...")
        print("="*80)
        
        # Base model
        print("\n--- ORIGINAL MODEL ---")
        base_out = generate_screenplay(base_model, base_tokenizer, prompt)
        print(base_out)
        
        # Fine-tuned model
        print("\n--- FINE-TUNED MODEL ---")
        ft_out = generate_screenplay(finetuned_model, finetuned_tokenizer, prompt)
        print(ft_out)

# Uncomment to run interactive comparison
# interactive_comparison(base_model, base_tokenizer, finetuned_model, finetuned_tokenizer)