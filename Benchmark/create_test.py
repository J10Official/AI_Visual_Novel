#!/usr/bin/env python3
"""
Quick test with 4 texts to verify tournament logic
"""

import os
import shutil
from pathlib import Path

def create_test_texts():
    """Create a test directory with 4 texts"""
    test_dir = Path("test_texts")
    test_dir.mkdir(exist_ok=True)
    
    # Copy first 4 texts
    for i in range(1, 5):
        src = Path("texts") / f"file_{i:02d}.txt"
        dst = test_dir / f"file_{i:02d}.txt"
        if src.exists():
            shutil.copy2(src, dst)
    
    print(f"Created test directory with 4 texts")
    return str(test_dir)

if __name__ == "__main__":
    test_dir = create_test_texts()
    print(f"Test directory: {test_dir}")
    print("Run: python3 text_comparison.py --tournament knockout --directory test_texts")
    print("Or:  python3 text_comparison.py --tournament swiss --directory test_texts --rounds 2")