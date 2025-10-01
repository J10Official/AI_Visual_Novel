#!/usr/bin/env python3
"""
Text Comparator Module
Handles AI-based text comparison using Gemini API
"""

import json
import random
import time
from typing import Optional
import google.generativeai as genai
from dataclasses import dataclass

@dataclass(frozen=True)
class Text:
    """Represents a text file with metadata"""
    id: str
    filename: str
    content: str
    
    def __str__(self):
        return f"{self.filename}"
    
    def __hash__(self):
        return hash((self.id, self.filename))

@dataclass
class Match:
    """Represents a match between two texts"""
    text1: Text
    text2: Text
    winner: Optional[Text] = None
    round_num: int = 0

class TextComparator:
    """Handles AI-based text comparison using Gemini API"""
    
    def __init__(self, api_key: str):
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-2.0-flash-lite')
        
    def compare_texts(self, text1: Text, text2: Text) -> Text:
        """
        Compare two texts for creativity and return the winner
        Returns consistent JSON response for reliable parsing
        """
        prompt = f"""
Compare these two texts for creative originality, innovation, and literary merit. 
Consider factors like:
- Unique concepts and ideas
- Creative use of language
- Originality of plot/narrative structure
- Imaginative elements
- Literary sophistication

TEXT A ({text1.filename}):
{text1.content}

TEXT B ({text2.filename}):
{text2.content}

Respond with ONLY a JSON object in this exact format:
{{"winner": "A", "reason": "Brief explanation of why this text is more creative"}}

Choose either "A" or "B" as the winner. Be decisive.
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
                winner_choice = result.get('winner', 'A').upper()
                reason = result.get('reason', 'No reason provided')
                
                winner = text1 if winner_choice == 'A' else text2
                loser = text2 if winner_choice == 'A' else text1
                
                print(f"  📊 {text1.filename} vs {text2.filename}")
                print(f"  🏆 Winner: {winner.filename}")
                print(f"  💭 Reason: {reason}")
                print()
                
                return winner
                
            except Exception as e:
                error_str = str(e).lower()
                if any(keyword in error_str for keyword in ["quota", "rate limit", "429", "503", "overloaded", "unavailable"]):
                    if attempt < max_retries - 1:
                        print(f"  ⚠️  API quota/overload error. Waiting 60 seconds before retry {attempt + 2}/{max_retries}...")
                        time.sleep(60)
                        continue
                    else:
                        print(f"  ⚠️  API quota/overload exceeded after {max_retries} attempts. Using random selection.")
                else:
                    print(f"  ⚠️  Error parsing AI response: {e}")
                    if attempt < max_retries - 1:
                        print(f"  🔄 Retrying... ({attempt + 2}/{max_retries})")
                        time.sleep(2)  # Short wait for other errors
                        continue
                    else:
                        print(f"  🎲 Defaulting to random choice")
                
                # If this is the last attempt or non-quota error
                if attempt == max_retries - 1:
                    break
        
        # Fallback to random selection
        winner = random.choice([text1, text2])
        print(f"  📊 {text1.filename} vs {text2.filename}")
        print(f"  🏆 Winner (random): {winner.filename}")
        print()
        return winner