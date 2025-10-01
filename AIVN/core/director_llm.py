"""
Director LLM Interface using Gemini API
Handles the generation of structured scene content from plot points
"""

import json
import os
from typing import Dict, Any, List, Optional
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

class DirectorLLM:
    def __init__(self):
        self.api_key = os.getenv('GEMINI_API_KEY')
        if not self.api_key:
            raise ValueError("GEMINI_API_KEY not found in environment variables")
        
        genai.configure(api_key=self.api_key)
        self.model = genai.GenerativeModel('gemini-2.0-flash')
    
    def generate_scene(self, 
                      plot_point: Dict[str, Any], 
                      database: Dict[str, Any], 
                      game_state: Dict[str, Any]) -> Dict[str, Any]:
        """
        Generate a complete scene based on a plot point, using the Director LLM
        """
        
        # Build the prompt for the Director LLM
        prompt = self._build_prompt(plot_point, database, game_state)
        
        try:
            # Generate content using Gemini
            print(f"🤖 GENERATING SCENE: {plot_point.get('id')} with Gemini")
            
            response = self.model.generate_content(prompt)
            
            print(f"   Gemini response length: {len(response.text)} characters")
            print(f"   Response preview: {response.text[:100]}...")
            
            # Parse the JSON response
            json_content = self._extract_json_from_response(response.text)
            
            # Validate and structure the response
            return self._validate_and_structure_response(json_content, plot_point)
            
        except Exception as e:
            print(f"Error generating scene: {e}")
            # Return a fallback scene
            return self._create_fallback_scene(plot_point)
    
    def _build_prompt(self, plot_point: Dict[str, Any], database: Dict[str, Any], game_state: Dict[str, Any]) -> str:
        """Build the comprehensive prompt for the Director LLM"""
        
        # Get character descriptions
        character_info = ""
        if 'characters' in plot_point:
            for char_id in plot_point['characters']:
                if char_id in database['characters']:
                    char_info = database['characters'][char_id]
                    character_info += f"- {char_id}: {char_info.get('description', 'No description')}\n"
        
        # Get location description
        location_info = ""
        if 'location' in plot_point and plot_point['location'] in database['locations']:
            location_info = database['locations'][plot_point['location']].get('description', '')
        
        # Get available background
        background_info = ""
        for bg in database['backgrounds']:
            if bg['location'] == plot_point.get('location'):
                background_info = f"Base image: {bg['image']}"
                break
        
        # Current game state flags
        current_flags = game_state.get('flags', {})
        flag_info = ", ".join([f"{k}={v}" for k, v in current_flags.items()])
        
        # Add randomization elements to ensure varied content
        import random
        import time
        random_seed = int(time.time() * 1000) % 10000
        variation_prompts = [
            "Focus on atmospheric details and environmental storytelling.",
            "Emphasize character emotions and internal thoughts.",
            "Highlight the cyberpunk technology and setting elements.",
            "Create tension through pacing and dramatic pauses.",
            "Add subtle world-building details and background information."
        ]
        variation_hint = random.choice(variation_prompts)
        
        prompt = f"""You are the Director LLM for a dynamic visual novel. Your job is to generate engaging, atmospheric scene content that bridges author-defined plot points.

**PLOT POINT INFORMATION:**
- Node ID: {plot_point.get('id', 'unknown')}
- Location: {plot_point.get('location', 'unknown')}
- Characters Present: {', '.join(plot_point.get('characters', []))}
- Author's Description: {plot_point.get('description', '')}

**CHARACTER INFORMATION:**
{character_info}

**LOCATION INFORMATION:**
{location_info}

**BACKGROUND ASSET:**
{background_info}

**CURRENT GAME STATE:**
Flags: {flag_info}

**CREATIVE DIRECTION:** {variation_hint}
**SESSION ID:** {random_seed}

**AVAILABLE EXPRESSIONS:** {', '.join(database.get('expressions', []))}
**AVAILABLE MOODS:** {', '.join(database.get('moods', []))}

**TASK:**
Generate a UNIQUE scene script that expands on the author's description while maintaining the core narrative intent. Create engaging dialogue and descriptions that feel natural and immersive. VARY your approach each time - use different dialogue styles, narrative perspectives, and descriptive focuses to keep content fresh.

**IMPORTANT: DO NOT GENERATE CHOICES OR PATHS** - The choice structure is already defined by the author and will be added automatically.

**OUTPUT FORMAT:**
Return ONLY a valid JSON object with this exact structure:

{{
  "id": "{plot_point.get('id', 'unknown')}",
  "content": {{
    "scene_script": [
      {{
        "character": "character_name_or_Narrator",
        "line": "The actual dialogue or narrative text",
        "expression": "expression_name_or_null"
      }}
    ],
    "scene_details": {{
      "mood": "mood_from_available_list",
      "location": "{plot_point.get('location', '')}",
      "characters_present": {json.dumps(plot_point.get('characters', []))},
      "background": {{
        "base_image": "{background_info.replace('Base image: ', '') if background_info else 'default_background.png'}",
        "edit_prompt": "description_of_any_needed_changes_or_null"
      }}
    }}
  }}
}}

**IMPORTANT GUIDELINES:**
- Focus ONLY on expanding the narrative content - dialogue and descriptions
- Keep dialogue natural and character-appropriate
- Maintain the sci-fi cyberpunk atmosphere of Aethelburg
- Each script entry should be substantial (2-4 sentences for dialogue, longer for narration)
- Choose expressions that match the emotional tone
- Select a mood that fits the scene's atmosphere
- The edit_prompt should describe visual changes to enhance the scene (lighting, weather, objects, etc.)
- DO NOT include any "paths" or choice information in your response

Generate the scene content now:"""

        return prompt
    
    def _extract_json_from_response(self, response_text: str) -> Dict[str, Any]:
        """Extract JSON from the model response"""
        # Find JSON block in the response
        response_text = response_text.strip()
        
        # Try to find JSON markers
        start_markers = ['{', '```json', '```']
        end_markers = ['}', '```']
        
        start_idx = -1
        for marker in start_markers:
            idx = response_text.find(marker)
            if idx != -1:
                if marker == '{':
                    start_idx = idx
                else:
                    start_idx = idx + len(marker)
                break
        
        if start_idx == -1:
            start_idx = 0
        
        # Find the end
        end_idx = len(response_text)
        for marker in end_markers:
            if marker == '}':
                # Find the last closing brace
                idx = response_text.rfind(marker)
                if idx != -1:
                    end_idx = idx + 1
                    break
            else:
                idx = response_text.rfind(marker)
                if idx != -1 and idx > start_idx:
                    end_idx = idx
                    break
        
        json_str = response_text[start_idx:end_idx].strip()
        
        # Clean up the JSON string
        if json_str.startswith('```json'):
            json_str = json_str[7:]
        if json_str.startswith('```'):
            json_str = json_str[3:]
        if json_str.endswith('```'):
            json_str = json_str[:-3]
        
        json_str = json_str.strip()
        
        try:
            return json.loads(json_str)
        except json.JSONDecodeError as e:
            print(f"Failed to parse JSON: {e}")
            print(f"JSON string: {json_str}")
            raise
    
    def _validate_and_structure_response(self, json_content: Dict[str, Any], plot_point: Dict[str, Any]) -> Dict[str, Any]:
        """Validate and ensure the response has the correct structure"""
        
        # Ensure required fields exist
        if 'content' not in json_content:
            json_content['content'] = {}
        
        if 'scene_script' not in json_content['content']:
            json_content['content']['scene_script'] = []
        
        if 'scene_details' not in json_content['content']:
            json_content['content']['scene_details'] = {}
        
        # CRITICAL FIX: Always use the exact choices from the plot point graph
        # The Director LLM should not modify the choice structure
        json_content['paths'] = []
        if 'choices' in plot_point:
            for choice in plot_point['choices']:
                json_content['paths'].append({
                    'choice_text': choice['text'],
                    'target_node': choice['target']
                })
        
        return json_content
    
    def _create_fallback_scene(self, plot_point: Dict[str, Any]) -> Dict[str, Any]:
        """Create a basic fallback scene if generation fails"""
        return {
            "id": plot_point.get('id', 'unknown'),
            "content": {
                "scene_script": [
                    {
                        "character": "Narrator",
                        "line": plot_point.get('description', 'The story continues...'),
                        "expression": None
                    }
                ],
                "scene_details": {
                    "mood": "calm",
                    "location": plot_point.get('location', 'unknown'),
                    "characters_present": plot_point.get('characters', []),
                    "background": {
                        "base_image": "default_background.png",
                        "edit_prompt": None
                    }
                }
            },
            "paths": [
                {
                    "choice_text": choice['text'],
                    "target_node": choice['target']
                } for choice in plot_point.get('choices', [])
            ]
        }