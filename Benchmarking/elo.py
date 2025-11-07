#!/usr/bin/env python3
"""
ELO Tournament Module
Implements ELO rating system for text comparison with Swiss-style pairing
"""

import math
import random
from typing import List, Optional, Tuple, Dict
from comparator import Text, TextComparator

class ELOText:
    """Extended Text class with ELO rating information"""
    
    def __init__(self, text: Text, initial_rating: int = 1500):
        self.text = text
        self.rating = initial_rating
        self.games_played = 0
        self.opponents = []
        self.wins = 0
        self.losses = 0
        self.buchholz_score = 0.0  # Sum of opponents' final scores
        
    @property
    def filename(self):
        return self.text.filename
    
    @property
    def content(self):
        return self.text.content
        
    @property
    def id(self):
        return self.text.id
    
    def get_k_factor(self) -> int:
        """Calculate adaptive K-factor based on experience"""
        if self.games_played < 10:
            return 32  # High volatility for new texts
        elif self.games_played < 20:
            return 24  # Medium volatility for developing texts
        else:
            return 16  # Low volatility for established texts
    
    def __str__(self):
        return f"{self.filename} (ELO: {self.rating:.0f}, Games: {self.games_played}, Buchholz: {self.buchholz_score:.1f})"

class ELOTournament:
    """Implements ELO rating system with Swiss-style pairing"""
    
    def __init__(self, texts: List[Text], comparator: TextComparator, rounds: Optional[int] = None):
        self.elo_texts = [ELOText(text) for text in texts]
        self.comparator = comparator
        self.rounds = rounds or max(1, math.ceil(math.log2(len(texts))))
        self.rating_floor = 800
        self.rating_ceiling = 2400
        
    def calculate_buchholz_scores(self):
        """Calculate Buchholz scores for all participants (sum of opponents' ratings)"""
        for elo_text in self.elo_texts:
            # Calculate sum of all opponents' final ratings
            elo_text.buchholz_score = sum(opponent.rating for opponent in elo_text.opponents)
    
    def calculate_expected_score(self, rating_a: float, rating_b: float) -> float:
        """Calculate expected score for player A against player B using ELO formula"""
        return 1.0 / (1.0 + math.pow(10, (rating_b - rating_a) / 400.0))
    
    def update_ratings(self, text_a: ELOText, text_b: ELOText, winner: Text):
        """Update ELO ratings based on match result"""
        # Determine actual scores (1 for win, 0 for loss)
        if winner.id == text_a.id:
            score_a, score_b = 1.0, 0.0
            text_a.wins += 1
            text_b.losses += 1
        else:
            score_a, score_b = 0.0, 1.0
            text_a.losses += 1
            text_b.wins += 1
        
        # Calculate expected scores
        expected_a = self.calculate_expected_score(text_a.rating, text_b.rating)
        expected_b = self.calculate_expected_score(text_b.rating, text_a.rating)
        
        # Get K-factors (adaptive based on experience)
        k_a = text_a.get_k_factor()
        k_b = text_b.get_k_factor()
        
        # Calculate rating changes
        rating_change_a = k_a * (score_a - expected_a)
        rating_change_b = k_b * (score_b - expected_b)
        
        # Update ratings with floor and ceiling constraints
        text_a.rating = max(self.rating_floor, 
                           min(self.rating_ceiling, 
                               text_a.rating + rating_change_a))
        text_b.rating = max(self.rating_floor, 
                           min(self.rating_ceiling, 
                               text_b.rating + rating_change_b))
        
        # Update game statistics
        text_a.games_played += 1
        text_b.games_played += 1
        text_a.opponents.append(text_b)
        text_b.opponents.append(text_a)
        
        # Debug output
        print(f"    📈 {text_a.filename}: {text_a.rating - rating_change_a:.0f} → {text_a.rating:.0f} ({rating_change_a:+.1f})")
        print(f"    📈 {text_b.filename}: {text_b.rating - rating_change_b:.0f} → {text_b.rating:.0f} ({rating_change_b:+.1f})")
    
    def find_best_pairing(self, available_texts: List[ELOText]) -> Optional[Tuple[ELOText, ELOText]]:
        """Find the best pairing based on ELO ratings and rematch avoidance"""
        if len(available_texts) < 2:
            return None
            
        # Sort by rating for better pairing
        available_texts.sort(key=lambda t: t.rating, reverse=True)
        
        best_pair = None
        best_score = float('inf')
        
        # Try to find the best pairing (closest ratings, no rematches)
        for i in range(len(available_texts)):
            for j in range(i + 1, len(available_texts)):
                text_a, text_b = available_texts[i], available_texts[j]
                
                # Check if they've played before
                rematch_penalty = 1000 if text_b in text_a.opponents else 0
                
                # Calculate rating difference (prefer similar ratings)
                rating_diff = abs(text_a.rating - text_b.rating)
                
                # Scoring: lower is better (prefer similar ratings, avoid rematches)
                pairing_score = rating_diff + rematch_penalty
                
                if pairing_score < best_score:
                    best_score = pairing_score
                    best_pair = (text_a, text_b)
        
        return best_pair
    
    def create_round_pairings(self) -> List[Tuple[ELOText, ELOText]]:
        """Create pairings for a round using ELO-based Swiss pairing"""
        available_texts = self.elo_texts.copy()
        pairings = []
        
        while len(available_texts) >= 2:
            pair = self.find_best_pairing(available_texts)
            if pair is None:
                break
                
            text_a, text_b = pair
            pairings.append((text_a, text_b))
            available_texts.remove(text_a)
            available_texts.remove(text_b)
        
        # Handle bye if odd number of texts
        if available_texts:
            bye_text = available_texts[0]
            print(f"🎫 {bye_text.filename} receives a bye (no rating change)")
        
        return pairings
    
    def run_tournament(self) -> List[Text]:
        """Run the complete ELO tournament"""
        print(f"⚖️  ELO RATING TOURNAMENT")
        print(f"📝 {len(self.elo_texts)} texts competing")
        print(f"🔄 Tournament will have {self.rounds} rounds")
        print(f"🎯 Initial rating: 1500, K-factor: Adaptive (32→24→16)")
        print("=" * 50)
        
        for round_num in range(1, self.rounds + 1):
            self._run_round(round_num)
            self._print_standings(round_num)
        
        # Calculate Buchholz scores before final rankings
        self.calculate_buchholz_scores()
        
        # Final rankings based on ELO ratings with Buchholz tie-breaking
        final_rankings = self._calculate_final_rankings()
        
        print("🏁 FINAL ELO RANKINGS:")
        for i, elo_text in enumerate(final_rankings, 1):
            win_rate = (elo_text.wins / elo_text.games_played * 100) if elo_text.games_played > 0 else 0
            print(f"{i:2d}. {elo_text.filename} (ELO: {elo_text.rating:.0f}, "
                  f"Record: {elo_text.wins}-{elo_text.losses}, Win Rate: {win_rate:.1f}%, "
                  f"Buchholz: {elo_text.buchholz_score:.0f})")
        
        return [elo_text.text for elo_text in final_rankings]
    
    def _run_round(self, round_num: int):
        """Run a single round of the ELO tournament"""
        print(f"🔄 ROUND {round_num}/{self.rounds}")
        
        # Create pairings based on ELO ratings
        pairings = self.create_round_pairings()
        
        if not pairings:
            print("  ⚠️  No valid pairings could be created")
            return
        
        # Run all matches
        for text_a, text_b in pairings:
            print(f"  ⚔️  {text_a.filename} (ELO: {text_a.rating:.0f}) vs "
                  f"{text_b.filename} (ELO: {text_b.rating:.0f})")
            
            winner = self.comparator.compare_texts(text_a.text, text_b.text)
            self.update_ratings(text_a, text_b, winner)
        
        print()
    
    def _print_standings(self, round_num: int):
        """Print current standings after a round"""
        print(f"📊 ELO STANDINGS AFTER ROUND {round_num}")
        
        # Calculate current Buchholz scores for interim standings
        for elo_text in self.elo_texts:
            elo_text.buchholz_score = sum(opponent.rating for opponent in elo_text.opponents)
        
        # Sort by ELO rating with Buchholz tie-breaking
        standings = sorted(self.elo_texts, 
                          key=lambda t: (t.rating, t.buchholz_score), 
                          reverse=True)
        
        for i, elo_text in enumerate(standings, 1):
            win_rate = (elo_text.wins / elo_text.games_played * 100) if elo_text.games_played > 0 else 0
            print(f"{i:2d}. {elo_text.filename} (ELO: {elo_text.rating:.0f}, "
                  f"{elo_text.wins}-{elo_text.losses}, {win_rate:.1f}%, "
                  f"Buchholz: {elo_text.buchholz_score:.0f})")
        print()
    
    def _calculate_final_rankings(self) -> List[ELOText]:
        """Calculate final rankings with Buchholz tie-breaking"""
        # Two-level sorting:
        # 1. ELO rating (primary)
        # 2. Buchholz score (secondary - strength of opponents)
        return sorted(self.elo_texts, 
                     key=lambda t: (t.rating, t.buchholz_score), 
                     reverse=True)
    
    def get_rating_distribution(self) -> Dict[str, float]:
        """Get statistics about rating distribution"""
        ratings = [t.rating for t in self.elo_texts]
        return {
            'mean': sum(ratings) / len(ratings),
            'min': min(ratings),
            'max': max(ratings),
            'std': math.sqrt(sum((r - sum(ratings)/len(ratings))**2 for r in ratings) / len(ratings))
        }