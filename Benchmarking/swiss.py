#!/usr/bin/env python3
"""
Swiss Tournament Module
Implements Swiss tournament system
"""

import math
import random
from typing import List, Optional, Tuple
from comparator import Text, TextComparator

class SwissTournament:
    """Implements Swiss tournament system"""
    
    def __init__(self, texts: List[Text], comparator: TextComparator, rounds: Optional[int] = None):
        self.texts = texts
        self.comparator = comparator
        self.rounds = rounds or max(1, math.ceil(math.log2(len(texts))))
        self.scoreboard = {text: {'points': 0, 'opponents': [], 'buchholz': 0} for text in texts}
        
    def run_tournament(self) -> List[Text]:
        """Run the complete Swiss tournament"""
        print(f"🇨🇭 SWISS TOURNAMENT")
        print(f"📝 {len(self.texts)} texts competing")
        print(f"🔄 Tournament will have {self.rounds} rounds")
        print("=" * 50)
        
        for round_num in range(1, self.rounds + 1):
            self._run_round(round_num)
            self._print_standings(round_num)
        
        # Calculate final rankings with tiebreakers
        final_rankings = self._calculate_final_rankings()
        
        print("🏁 FINAL SWISS RANKINGS:")
        for i, (text, score) in enumerate(final_rankings, 1):
            buchholz = self.scoreboard[text]['buchholz']
            print(f"{i:2d}. {text.filename} ({score} pts, Buchholz: {buchholz:.1f})")
        
        return [text for text, _ in final_rankings]
    
    def _run_round(self, round_num: int):
        """Run a single round of the Swiss tournament"""
        print(f"🔄 ROUND {round_num}/{self.rounds}")
        
        # Group texts by score
        score_groups = {}
        for text in self.texts:
            score = self.scoreboard[text]['points']
            if score not in score_groups:
                score_groups[score] = []
            score_groups[score].append(text)
        
        # Create pairings
        pairs = []
        unpaired = []
        
        for score in sorted(score_groups.keys(), reverse=True):
            group = score_groups[score]
            random.shuffle(group)
            
            # Add any unpaired text from previous score group
            if unpaired:
                group = unpaired + group
                unpaired = []
            
            # Pair within the group, avoiding rematches when possible
            for i in range(0, len(group) - 1, 2):
                text1, text2 = group[i], group[i + 1]
                
                # Check for previous matchup
                if text2 in self.scoreboard[text1]['opponents']:
                    # Try to find alternative pairing
                    found_alternative = False
                    for j in range(i + 2, len(group)):
                        if group[j] not in self.scoreboard[text1]['opponents']:
                            group[i + 1], group[j] = group[j], group[i + 1]
                            text2 = group[i + 1]
                            found_alternative = True
                            break
                    
                    if not found_alternative:
                        print(f"  ⚠️  Forced rematch: {text1.filename} vs {text2.filename}")
                
                pairs.append((text1, text2))
            
            # Handle odd number in group
            if len(group) % 2 == 1:
                unpaired.append(group[-1])
        
        # Handle final unpaired text (gets a bye)
        if unpaired:
            bye_text = unpaired[0]
            print(f"🎫 {bye_text.filename} receives a bye (+1 point)")
            self.scoreboard[bye_text]['points'] += 1
        
        # Run all matches
        for text1, text2 in pairs:
            winner = self.comparator.compare_texts(text1, text2)
            loser = text2 if winner == text1 else text1
            
            # Update scores and opponent lists
            self.scoreboard[winner]['points'] += 1
            self.scoreboard[text1]['opponents'].append(text2)
            self.scoreboard[text2]['opponents'].append(text1)
        
        print()
    
    def _print_standings(self, round_num: int):
        """Print current standings after a round"""
        print(f"📊 STANDINGS AFTER ROUND {round_num}")
        
        # Sort by points
        standings = sorted(self.texts, 
                         key=lambda t: self.scoreboard[t]['points'], 
                         reverse=True)
        
        for i, text in enumerate(standings, 1):
            points = self.scoreboard[text]['points']
            print(f"{i:2d}. {text.filename} ({points} pts)")
        print()
    
    def _calculate_final_rankings(self) -> List[Tuple[Text, int]]:
        """Calculate final rankings with Buchholz tiebreaker"""
        # Calculate Buchholz scores
        for text in self.texts:
            buchholz_score = 0
            for opponent in self.scoreboard[text]['opponents']:
                buchholz_score += self.scoreboard[opponent]['points']
            self.scoreboard[text]['buchholz'] = buchholz_score
        
        # Sort by points first, then by Buchholz score
        final_standings = sorted(self.texts, 
                               key=lambda t: (self.scoreboard[t]['points'], 
                                            self.scoreboard[t]['buchholz']), 
                               reverse=True)
        
        return [(text, self.scoreboard[text]['points']) for text in final_standings]