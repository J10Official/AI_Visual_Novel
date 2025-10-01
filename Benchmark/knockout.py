#!/usr/bin/env python3
"""
Knockout Tournament Module
Implements knockout tournament with recursive ranking
"""

import math
import random
from typing import List
from comparator import Text, TextComparator, Match

class KnockoutTournament:
    """Implements knockout tournament with recursive ranking"""
    
    def __init__(self, texts: List[Text], comparator: TextComparator):
        self.texts = texts
        self.comparator = comparator
        self.matches_played = []
        self.rankings = []
        
    def run_tournament(self) -> List[Text]:
        """Run the complete knockout tournament with recursive ranking"""
        print(f"🥊 KNOCKOUT TOURNAMENT")
        print(f"📝 {len(self.texts)} texts competing")
        
        # Calculate total rounds for main tournament
        total_main_rounds = math.ceil(math.log2(len(self.texts)))
        print(f"📊 Main tournament will have {total_main_rounds} rounds")
        print("=" * 50)
        
        # Phase 1: Main tournament
        champion = self._run_main_tournament()
        self.rankings.append(champion)
        print(f"🏆 CHAMPION: {champion.filename}")
        print()
        
        # Phase 2: Recursive ranking for remaining positions
        self._run_recursive_ranking()
        
        print("🏁 FINAL KNOCKOUT RANKINGS:")
        for i, text in enumerate(self.rankings, 1):
            print(f"{i:2d}. {text.filename}")
        
        return self.rankings
    
    def _run_main_tournament(self) -> Text:
        """Run the main elimination tournament"""
        current_texts = self.texts.copy()
        round_num = 1
        
        while len(current_texts) > 1:
            print(f"🔄 ROUND {round_num}")
            print(f"📊 {len(current_texts)} texts remaining")
            
            # Handle byes if odd number of texts
            if len(current_texts) % 2 == 1:
                bye_text = random.choice(current_texts)
                current_texts.remove(bye_text)
                print(f"🎫 {bye_text.filename} receives a bye")
                
            # Create pairs and run matches
            winners = []
            random.shuffle(current_texts)
            
            for i in range(0, len(current_texts), 2):
                text1, text2 = current_texts[i], current_texts[i+1]
                match = Match(text1, text2, round_num=round_num)
                winner = self.comparator.compare_texts(text1, text2)
                match.winner = winner
                self.matches_played.append(match)
                winners.append(winner)
            
            # Add bye text back if there was one
            if 'bye_text' in locals():
                winners.append(bye_text)
                del bye_text  # Clean up for next round
            
            current_texts = winners
            round_num += 1
            print()
        
        return current_texts[0]
    
    def _run_recursive_ranking(self):
        """Recursively rank the remaining texts"""
        print("🔄 RECURSIVE RANKING PHASE")
        
        remaining_texts = [t for t in self.texts if t not in self.rankings]
        
        for rank_position in range(2, len(self.texts) + 1):
            if not remaining_texts:
                break
                
            print(f"🎯 Finding rank #{rank_position}")
            
            # Find all texts that lost to any currently ranked text
            playoff_pool = set()
            for match in self.matches_played:
                if match.winner in self.rankings:
                    loser = match.text1 if match.winner == match.text2 else match.text2
                    if loser in remaining_texts:
                        playoff_pool.add(loser)
            
            playoff_texts = list(playoff_pool)
            
            if not playoff_texts:
                # If no playoff pool, take remaining texts
                playoff_texts = remaining_texts.copy()
            
            if len(playoff_texts) == 1:
                # Only one candidate, they get this rank
                next_ranked = playoff_texts[0]
            else:
                # Run mini tournament
                print(f"  🏟️  Playoff with {len(playoff_texts)} texts")
                mini_tournament = KnockoutTournament(playoff_texts, self.comparator)
                mini_result = mini_tournament._run_main_tournament()
                next_ranked = mini_result
            
            self.rankings.append(next_ranked)
            remaining_texts.remove(next_ranked)
            print(f"  🏆 Rank #{rank_position}: {next_ranked.filename}")
            print()