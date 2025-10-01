#!/usr/bin/env python3
"""
Usage Examples for Text Creativity Comparison System
Demonstrates all three tournament types: knockout, swiss, and naive
"""

import subprocess
import sys
import os

def run_command(command, description):
    """Run a command and display its output"""
    print(f"\n{'='*60}")
    print(f"🚀 {description}")
    print(f"{'='*60}")
    print(f"💻 Command: {command}")
    print(f"{'='*60}")
    
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True, cwd="/home/jatin/Code/Year3/benchmark")
        print(result.stdout)
        if result.stderr and "WARNING" not in result.stderr:
            print("STDERR:", result.stderr)
        return result.returncode == 0
    except Exception as e:
        print(f"❌ Error running command: {e}")
        return False

def main():
    """Demonstrate all tournament types"""
    print("🎯 TEXT CREATIVITY COMPARISON SYSTEM - USAGE EXAMPLES")
    print("This script demonstrates all three tournament types available.")
    
    # Check if we're in the right directory
    if not os.path.exists("/home/jatin/Code/Year3/benchmark/text_comparison_modular.py"):
        print("❌ Please run this script from the benchmark directory")
        return 1
    
    examples = [
        {
            "command": "python3 text_comparison_modular.py --tournament naive --directory test_texts",
            "description": "NAIVE SCORING - Independent AI scoring (0-100) of each text"
        },
        {
            "command": "python3 text_comparison_modular.py --tournament knockout --directory test_texts", 
            "description": "KNOCKOUT TOURNAMENT - Single elimination with recursive ranking"
        },
        {
            "command": "python3 text_comparison_modular.py --tournament swiss --directory test_texts --rounds 3",
            "description": "SWISS TOURNAMENT - Round-robin style with Buchholz scoring"
        }
    ]
    
    print(f"\n📋 Available Tournament Types:")
    print(f"1. 🎯 NAIVE - Independent scoring (fastest, most direct)")
    print(f"2. 🥊 KNOCKOUT - Head-to-head elimination (exciting, dramatic)")
    print(f"3. 🇨🇭 SWISS - Multiple rounds, fair pairing (comprehensive, balanced)")
    print(f"\n🔄 Running examples with test_texts directory...")
    
    for i, example in enumerate(examples, 1):
        success = run_command(example["command"], f"Example {i}: {example['description']}")
        if not success:
            print(f"⚠️  Example {i} had issues, but continuing...")
        
        if i < len(examples):
            print(f"\n⏭️  Moving to next example...")
    
    print(f"\n✅ All examples completed!")
    print(f"\n📚 Usage Summary:")
    print(f"• Naive:    python3 text_comparison_modular.py --tournament naive --directory [DIR]")
    print(f"• Knockout: python3 text_comparison_modular.py --tournament knockout --directory [DIR]") 
    print(f"• Swiss:    python3 text_comparison_modular.py --tournament swiss --directory [DIR] --rounds [N]")
    
    return 0

if __name__ == "__main__":
    exit(main())