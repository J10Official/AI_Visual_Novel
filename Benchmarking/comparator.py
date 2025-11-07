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
        # Gemini 2.5 Flash-Lite - lower RPM/TPM but higher RPD
        self.model = genai.GenerativeModel('gemini-2.5-flash-lite')
        self.request_count = 0
        self.requests_per_minute = 0
        self.last_minute_reset = time.time()
        
    def _check_rate_limits(self):
        """
        Check and enforce rate limits for Gemini 2.5 Flash-Lite
        Flash-Lite has lower RPM (15/min) but higher RPD (1500/day)
        """
        current_time = time.time()
        
        # Reset minute counter if a minute has passed
        if current_time - self.last_minute_reset >= 60:
            self.requests_per_minute = 0
            self.last_minute_reset = current_time
        
        # Check if we're approaching the per-minute limit (15 RPM for Flash-Lite)
        if self.requests_per_minute >= 14:  # Leave buffer of 1
            wait_time = 60 - (current_time - self.last_minute_reset)
            if wait_time > 0:
                print(f"  ⏱️  Rate limit approaching. Waiting {wait_time:.1f}s...")
                time.sleep(wait_time + 1)  # Add 1 second buffer
                self.requests_per_minute = 0
                self.last_minute_reset = time.time()
        
        self.requests_per_minute += 1
        self.request_count += 1
        
    def get_rate_limit_status(self):
        """Get current rate limiting status"""
        current_time = time.time()
        time_since_reset = current_time - self.last_minute_reset
        return {
            'total_requests': self.request_count,
            'requests_this_minute': self.requests_per_minute,
            'time_since_reset': time_since_reset,
            'requests_remaining_this_minute': max(0, 14 - self.requests_per_minute)
        }
        
    def compare_texts(self, text1: Text, text2: Text) -> Text:
        """
        Compare two texts for creativity and return the winner
        Returns consistent JSON response for reliable parsing
        """
        # SYNTAX PROMPT - COMMENTED OUT FOR NOW
        # prompt = f"""
        # Compare these two texts for adherence to the specified syntax format. The expected format is:
        # 
        # ::SCENE::
        # LOCATION: Short description of the location (e.g., 'Dark Forest', 'Kitchen')
        # MOOD: The dominant mood or tone of the scene (e.g., 'Tense', 'Calm')
        # CHARACTERS: Character_Name_1, Character_Name_2, Narrator
        # BACKGROUND_IMAGE: Reference to the visual background (e.g., 'forest.png')
        # BACKGROUND_EDIT: Change made to base background (e.g., 'during evening', 'add a clock to background')
        # 
        # ::SCRIPT::
        # CHARACTER: Name of character speaking (or 'Narrator')
        # LINE: The line of dialogue or action description for this moment.
        # EXPRESSION: The character's expression (e.g., 'Happy', 'Angry', 'null')
        # 
        # CHARACTER: Another_Character_Name
        # LINE: The next line of dialogue or action.
        # EXPRESSION: Another_Expression
        # 
        # ::PATHS::
        # CHOICE: The text presented to the user for this choice
        # TARGET: The_ID_of_the_next_scene_this_choice_leads_to
        # STATE_CHANGE: Any game state variables to change (e.g., 'score = +1', 'null')
        # CONDITION: The condition required for this choice to be visible (e.g., 'has_key == true', 'null')
        # 
        # Evaluate which text better follows this syntax structure. Consider:
        # - Correct use of section headers (::SCENE::, ::SCRIPT::, ::PATHS::)
        # - Proper field formatting (FIELD: value)
        # - Appropriate content in each section
        # - Overall structural adherence
        # - Completeness of required elements
        # 
        # TEXT A ({text1.filename}):
        # {text1.content}
        # 
        # TEXT B ({text2.filename}):
        # {text2.content}
        # 
        # Respond with ONLY a JSON object in this exact format:
        # {{"winner": "A", "reason": "Brief explanation of why this text better follows the syntax format"}}
        # 
        # Choose either "A" or "B" as the winner. Be decisive.
        # """
        
        # CREATIVITY PROMPT - NOW ACTIVE
        prompt = f"""
        Compare these two texts for creative originality, innovation, and literary merit. 
        
        IMPORTANT: These texts are clipped to 500 words for fair comparison. Do NOT consider completeness, story endings, or narrative conclusion as factors in your evaluation. Focus ONLY on the quality of the writing within the provided excerpt.
        
        Consider these factors:
        - Unique concepts and ideas
        - Creative use of language
        - Originality of plot/narrative structure
        - Imaginative elements
        - Literary sophistication
        - Quality of prose and descriptive writing
        - Character development within the excerpt
        - Atmospheric and world-building elements
        
        IGNORE these factors:
        - Whether the story feels complete or incomplete
        - Missing endings or conclusions
        - Abrupt cutoffs due to word limits
        - Overall narrative arc completion
        
        TEXT A ({text1.filename}):
        {text1.content}
        
        TEXT B ({text2.filename}):
        {text2.content}
        
        Respond with ONLY a JSON object in this exact format:
        {{"winner": "A", "reason": "Brief explanation of why this text excerpt is more creative"}}
        
        Choose either "A" or "B" as the winner. Be decisive.
        """
        
        max_retries = 10
        for attempt in range(max_retries):
            try:
                # Check rate limits before making request
                self._check_rate_limits()
                
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
                
                # Handle rate limiting errors specifically for Flash-Lite
                if any(keyword in error_str for keyword in ["quota", "rate limit", "429", "503", "overloaded", "unavailable"]):
                    if attempt < max_retries - 1:
                        # Reduced wait time to 20 seconds for faster retries
                        wait_time = 20
                        print(f"  ⚠️  Flash-Lite rate limit hit. Waiting {wait_time}s before retry {attempt + 2}/{max_retries}...")
                        time.sleep(wait_time)
                        # Reset rate limiting counters
                        self.requests_per_minute = 0
                        self.last_minute_reset = time.time()
                        continue
                    else:
                        print(f"  ⚠️  Flash-Lite quota/overload exceeded after {max_retries} attempts. Using random selection.")
                
                # Handle daily quota exceeded
                elif "resource_exhausted" in error_str or "daily quota" in error_str:
                    print(f"  🚫 Daily quota exhausted for Flash-Lite model. Switching to random selection.")
                    break
                
                # Handle other errors
                else:
                    print(f"  ⚠️  Error parsing AI response: {e}")
                    if attempt < max_retries - 1:
                        print(f"  🔄 Retrying... ({attempt + 2}/{max_retries})")
                        time.sleep(3)  # Slightly longer wait for parsing errors
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