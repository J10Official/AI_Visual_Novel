#!/usr/bin/env python3
"""
Text Creativity Comparison System - Main Module
Orchestrates the tournament system using modular components
"""

import argparse
from pathlib import Path
from typing import List

# Import modular components
from comparator import Text, TextComparator
from knockout import KnockoutTournament
from swiss import SwissTournament
from naive import NaiveScorer, NaiveRanking

def load_texts_from_directory(directory: str) -> List[Text]:
    """Load all text files from the specified directory"""
    texts = []
    directory_path = Path(directory)
    
    if not directory_path.exists():
        raise FileNotFoundError(f"Directory not found: {directory}")
    
    for file_path in sorted(directory_path.glob("*.txt")):
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read().strip()
        
        text = Text(
            id=file_path.stem,
            filename=file_path.name,
            content=content
        )
        texts.append(text)
    
    return texts

def main():
    """Main function to run the text comparison system"""
    parser = argparse.ArgumentParser(description="Text Creativity Comparison System")
    parser.add_argument("--tournament", choices=["knockout", "swiss", "naive"], 
                       default="knockout", help="Tournament type")
    parser.add_argument("--directory", default="texts", 
                       help="Directory containing text files")
    parser.add_argument("--rounds", type=int, 
                       help="Number of rounds for Swiss tournament")
    parser.add_argument("--api-key", default="AIzaSyBnHRPjMzgtWh62VFEpVrI938CydbbgFAQ",
                       help="Gemini API key")
    
    args = parser.parse_args()
    
    print("🎯 TEXT CREATIVITY COMPARISON SYSTEM")
    print("=" * 50)
    
    try:
        # Load texts
        texts = load_texts_from_directory(args.directory)
        print(f"📚 Loaded {len(texts)} texts from {args.directory}/")
        
        if len(texts) < 2:
            print("❌ Need at least 2 texts to compare")
            return
        
        # Run tournament
        if args.tournament == "knockout":
            # Initialize comparator
            comparator = TextComparator(args.api_key)
            tournament = KnockoutTournament(texts, comparator)
            rankings = tournament.run_tournament()
        elif args.tournament == "swiss":
            # Initialize comparator
            comparator = TextComparator(args.api_key)
            tournament = SwissTournament(texts, comparator, args.rounds)
            rankings = tournament.run_tournament()
        else:  # naive
            # Initialize scorer
            scorer = NaiveScorer(args.api_key)
            ranking_system = NaiveRanking(texts, scorer)
            rankings = ranking_system.run_ranking()
        
        print("\n✅ Tournament completed successfully!")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return 1
    
    return 0

if __name__ == "__main__":
    exit(main())