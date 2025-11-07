#!/usr/bin/env python3
"""
Text Creativity Comparison System - Main Module
Orchestrates the tournament system using modular components
"""

import argparse
import logging
import sys
from datetime import datetime
from pathlib import Path
from typing import List

# Import modular components
from comparator import Text, TextComparator
from knockout import KnockoutTournament
from swiss import SwissTournament
from naive import NaiveScorer, NaiveRanking
from elo import ELOTournament

def setup_logging(tournament_type: str, directory: str, rounds: int = None) -> str:
    """Setup logging with unique timestamped filename"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    directory_name = Path(directory).name
    
    if rounds:
        log_filename = f"tournament_log_{tournament_type}_{directory_name}_r{rounds}_{timestamp}.txt"
    else:
        log_filename = f"tournament_log_{tournament_type}_{directory_name}_{timestamp}.txt"
    
    # Create logs directory if it doesn't exist
    log_dir = Path("tournament_logs")
    log_dir.mkdir(exist_ok=True)
    log_path = log_dir / log_filename
    
    # Setup logging configuration
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_path, mode='w', encoding='utf-8'),
            logging.StreamHandler(sys.stdout)
        ]
    )
    
    return str(log_path)

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
    parser.add_argument("--tournament", choices=["knockout", "swiss", "naive", "elo"], 
                       default="knockout", help="Tournament type")
    parser.add_argument("--directory", default="texts", 
                       help="Directory containing text files")
    parser.add_argument("--rounds", type=int, 
                       help="Number of rounds for Swiss/ELO tournament")
    parser.add_argument("--api-key", default="AIzaSyCS5ZQvL-_-sXUIuXh6VK9pkxDeeBLIf_Q",
                       help="Gemini API key")
    
    args = parser.parse_args()
    
    # Setup logging with unique filename
    log_path = setup_logging(args.tournament, args.directory, args.rounds)
    
    logging.info("🎯 TEXT CREATIVITY COMPARISON SYSTEM")
    logging.info("=" * 50)
    logging.info(f"📝 Log file: {log_path}")
    logging.info(f"🏆 Tournament type: {args.tournament}")
    logging.info(f"📁 Directory: {args.directory}")
    if args.rounds:
        logging.info(f"🔄 Rounds: {args.rounds}")
    
    try:
        # Load texts
        texts = load_texts_from_directory(args.directory)
        logging.info(f"📚 Loaded {len(texts)} texts from {args.directory}/")
        
        if len(texts) < 2:
            logging.error("❌ Need at least 2 texts to compare")
            return
        
        # Log text files found
        logging.info("📋 Text files:")
        for i, text in enumerate(texts, 1):
            logging.info(f"  {i:2d}. {text.filename}")
        
        start_time = datetime.now()
        logging.info(f"⏰ Tournament started at: {start_time.strftime('%Y-%m-%d %H:%M:%S')}")
        
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
        elif args.tournament == "elo":
            # Initialize comparator
            comparator = TextComparator(args.api_key)
            tournament = ELOTournament(texts, comparator, args.rounds)
            rankings = tournament.run_tournament()
        else:  # naive
            # Initialize scorer
            scorer = NaiveScorer(args.api_key)
            ranking_system = NaiveRanking(texts, scorer)
            rankings = ranking_system.run_ranking()
        
        end_time = datetime.now()
        duration = end_time - start_time
        
        logging.info(f"⏰ Tournament completed at: {end_time.strftime('%Y-%m-%d %H:%M:%S')}")
        logging.info(f"⏱️  Total duration: {duration}")
        logging.info("✅ Tournament completed successfully!")
        logging.info("=" * 50)
        
    except Exception as e:
        logging.error(f"❌ Error: {e}")
        return 1
    
    return 0

if __name__ == "__main__":
    exit(main())