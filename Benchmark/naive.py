#!/usr/bin/env python3
"""
Naive Test Module
Scores texts independently and ranks them by AI-assigned scores
"""

import json
import random
import time
from typing import List, Tuple
import google.generativeai as genai
from comparator import Text

class NaiveScorer:
    """Handles AI-based independent text scoring"""
    
    def __init__(self, api_key: str):
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-2.0-flash-lite')
    
    def score_text(self, text: Text) -> int:
        """
        Score a single text for creativity (0-100)
        Returns a score from 0 to 100
        """
        prompt = f"""
Rate this text for creative originality, innovation, and literary merit on a scale of 0-100.

Consider factors like:
- Unique concepts and ideas (25 points)
- Creative use of language (25 points) 
- Originality of plot/narrative structure (25 points)
- Imaginative elements and literary sophistication (25 points)

TEXT ({text.filename}):
{text.content}

Respond with ONLY a JSON object in this exact format:
{{"score": 85, "reason": "Brief explanation of the score"}}

Provide a score between 0-100 where:
- 0-30: Basic/poor creativity
- 31-50: Below average creativity
- 51-70: Average creativity  
- 71-85: Good creativity
- 86-95: Excellent creativity
- 96-100: Exceptional creativity

Be decisive and specific with your scoring.
"""
        
        max_retries = 3
        for attempt in range(max_retries):
            try:
                response = self.model.generate_content(prompt)
                response_text = response.text.strip()
                
                # Try to extract JSON from response
                if response_text.startswith('```json'):
                    response_text = response_text[7:-3].strip()
                elif response_text.startswith('```'):
                    response_text = response_text[3:-3].strip()
                    
                result = json.loads(response_text)
                score = int(result.get('score', 50))
                reason = result.get('reason', 'No reason provided')
                
                # Ensure score is within valid range
                score = max(0, min(100, score))
                
                print(f"  📊 {text.filename}")
                print(f"  🎯 Score: {score}/100")
                print(f"  💭 Reason: {reason}")
                print()
                
                return score
                
            except Exception as e:
                error_str = str(e).lower()
                if any(keyword in error_str for keyword in ["quota", "rate limit", "429", "503", "overloaded", "unavailable"]):
                    if attempt < max_retries - 1:
                        print(f"  ⚠️  API quota/overload error. Waiting 60 seconds before retry {attempt + 2}/{max_retries}...")
                        time.sleep(60)
                        continue
                    else:
                        print(f"  ⚠️  API quota/overload exceeded after {max_retries} attempts. Using random score.")
                else:
                    print(f"  ⚠️  Error parsing AI response: {e}")
                    if attempt < max_retries - 1:
                        print(f"  🔄 Retrying... ({attempt + 2}/{max_retries})")
                        time.sleep(2)  # Short wait for other errors
                        continue
                    else:
                        print(f"  🎲 Defaulting to random score")
                
                # If this is the last attempt
                if attempt == max_retries - 1:
                    break
        
        # Fallback to random score
        random_score = random.randint(30, 80)
        print(f"  📊 {text.filename}")
        print(f"  🎯 Score (random): {random_score}/100")
        print()
        return random_score

class NaiveRanking:
    """Implements naive independent scoring and ranking"""
    
    def __init__(self, texts: List[Text], scorer: NaiveScorer):
        self.texts = texts
        self.scorer = scorer
        self.scores = {}
    
    def run_ranking(self) -> List[Text]:
        """Run independent scoring and return ranked texts"""
        print(f"🎯 NAIVE INDEPENDENT SCORING")
        print(f"📝 {len(self.texts)} texts to score")
        print(f"🔄 Each text will be scored independently (0-100)")
        print("=" * 50)
        
        print("📋 SCORING PHASE")
        print("Scoring each text independently...")
        print()
        
        # Score each text independently
        for i, text in enumerate(self.texts, 1):
            print(f"🔢 Scoring text {i}/{len(self.texts)}")
            score = self.scorer.score_text(text)
            self.scores[text] = score
        
        # Sort texts by score (highest first)
        ranked_texts = sorted(self.texts, key=lambda t: self.scores[t], reverse=True)
        
        print("🏁 FINAL NAIVE RANKINGS:")
        for i, text in enumerate(ranked_texts, 1):
            score = self.scores[text]
            print(f"{i:2d}. {text.filename} ({score}/100 points)")
        
        return ranked_texts
    
    def get_scores(self) -> dict:
        """Return the scores dictionary for analysis"""
        return self.scores.copy()