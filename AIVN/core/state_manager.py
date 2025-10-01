"""
Core State Manager
Handles game state, plot point navigation, and flag management
"""

from typing import Dict, Any, List, Optional
from core.parser import PlotPointParser, DatabaseParser
try:
    from core.director_llm import DirectorLLM
except ImportError:
    # Fallback for demo mode
    DirectorLLM = None
try:
    from core.gemini_image_generator import GeminiImageGenerator
    from core.asset_generator import AssetGenerator
except ImportError:
    # Fallback to basic asset generator
    from core.asset_generator import AssetGenerator
    GeminiImageGenerator = None

class StateManager:
    def __init__(self, plot_graph_path: str, database_path: str):
        self.plot_parser = PlotPointParser()
        self.db_parser = DatabaseParser()
        if DirectorLLM:
            self.director = DirectorLLM()
        else:
            # This will be overridden in demo mode
            self.director = None
        
        # Use Gemini image generator if available, otherwise fallback
        if GeminiImageGenerator:
            try:
                self.image_generator = GeminiImageGenerator()
            except Exception as e:
                print(f"Failed to initialize Gemini image generator: {e}")
                self.image_generator = AssetGenerator()
        else:
            self.image_generator = AssetGenerator()
        
        # Load game data
        self.plot_graph = self.plot_parser.parse_plot_point_graph(plot_graph_path)
        self.database = self.db_parser.parse_database(database_path)
        
        # Initialize game state
        self.game_state = {
            'current_node': 'start_mission',  # Starting node from plot graph
            'flags': self.database.get('story_flags', {}).copy(),
            'history': [],
            'scene_cache': {}
        }
        
        # Find starting node
        if 'start_mission' not in self.plot_graph:
            # Find first node if start_mission doesn't exist
            first_node = next(iter(self.plot_graph.keys())) if self.plot_graph else None
            self.game_state['current_node'] = first_node
    
    def get_current_scene(self) -> Dict[str, Any]:
        """Get the current scene, generating it if necessary"""
        current_node_id = self.game_state['current_node']
        
        if not current_node_id or current_node_id not in self.plot_graph:
            return self._create_error_scene("Invalid node")
        
        # Check cache first
        cache_key = f"{current_node_id}_{hash(str(self.game_state['flags']))}"
        if cache_key in self.game_state['scene_cache']:
            return self.game_state['scene_cache'][cache_key]
        
        # Get plot point
        plot_point = self.plot_graph[current_node_id]
        
        # Filter choices based on flags
        filtered_choices = self._filter_choices_by_flags(plot_point.get('choices', []))
        plot_point_with_filtered_choices = plot_point.copy()
        plot_point_with_filtered_choices['choices'] = filtered_choices
        
        # Generate scene using Director LLM
        try:
            scene = self.director.generate_scene(
                plot_point_with_filtered_choices, 
                self.database, 
                self.game_state
            )
            
            # Generate background using Gemini image generator
            if scene.get('content', {}).get('scene_details'):
                if hasattr(self, 'image_generator') and hasattr(self.image_generator, 'generate_or_edit_image'):
                    # Use Gemini image generator
                    bg_filename = self.image_generator.generate_or_edit_image(
                        scene['content']['scene_details']
                    )
                else:
                    # Fallback to basic asset generator
                    bg_filename = self.asset_generator.generate_background(
                        scene['content']['scene_details']
                    )
                scene['content']['scene_details']['background']['generated_image'] = bg_filename
            
            # Cache the scene
            self.game_state['scene_cache'][cache_key] = scene
            
            return scene
            
        except Exception as e:
            print(f"Error generating scene: {e}")
            return self._create_fallback_scene(plot_point)
    
    def make_choice(self, choice_index: int) -> bool:
        """Make a player choice and advance the story"""
        current_scene = self.get_current_scene()
        
        if 'paths' not in current_scene or choice_index >= len(current_scene['paths']):
            return False
        
        chosen_path = current_scene['paths'][choice_index]
        target_node = chosen_path['target_node']
        
        # Record choice in history
        self.game_state['history'].append({
            'from_node': self.game_state['current_node'],
            'choice_text': chosen_path['choice_text'],
            'to_node': target_node
        })
        
        # Apply flag changes if any
        current_node = self.plot_graph.get(self.game_state['current_node'])
        if current_node and 'choices' in current_node:
            for choice in current_node['choices']:
                if choice['text'] == chosen_path['choice_text']:
                    if choice.get('flag_set'):
                        self._apply_flag_change(choice['flag_set'])
                    break
        
        # Move to target node
        self.game_state['current_node'] = target_node
        
        return True
    
    def _filter_choices_by_flags(self, choices: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Filter choices based on current flag states"""
        filtered = []
        
        for choice in choices:
            flag_check = choice.get('flag_check')
            
            if not flag_check:
                # No flag requirement, include choice
                filtered.append(choice)
            else:
                # Check flag condition
                if self._evaluate_flag_condition(flag_check):
                    filtered.append(choice)
        
        return filtered
    
    def _evaluate_flag_condition(self, condition: str) -> bool:
        """Evaluate a flag condition (simple implementation)"""
        try:
            # Handle simple conditions like "has_nullifier == true"
            if '==' in condition:
                flag_name, value = condition.split('==')
                flag_name = flag_name.strip()
                value = value.strip().lower()
                
                current_value = self.game_state['flags'].get(flag_name, False)
                expected_value = value == 'true'
                
                return current_value == expected_value
            
            # Handle simple flag existence checks
            flag_name = condition.strip()
            return self.game_state['flags'].get(flag_name, False)
            
        except Exception:
            return False
    
    def _apply_flag_change(self, flag_change: str):
        """Apply a flag change like 'has_nullifier = true'"""
        try:
            if '=' in flag_change:
                flag_name, value = flag_change.split('=')
                flag_name = flag_name.strip()
                value = value.strip().lower()
                
                self.game_state['flags'][flag_name] = (value == 'true')
        except Exception as e:
            print(f"Error applying flag change: {e}")
    
    def _create_error_scene(self, error_msg: str) -> Dict[str, Any]:
        """Create an error scene"""
        return {
            "id": "error",
            "content": {
                "scene_script": [
                    {
                        "character": "System",
                        "line": f"Error: {error_msg}",
                        "expression": None
                    }
                ],
                "scene_details": {
                    "mood": "dread",
                    "location": "unknown",
                    "characters_present": [],
                    "background": {
                        "base_image": "error.png",
                        "edit_prompt": None
                    }
                }
            },
            "paths": []
        }
    
    def _create_fallback_scene(self, plot_point: Dict[str, Any]) -> Dict[str, Any]:
        """Create a fallback scene when generation fails"""
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
                        "base_image": "default.png",
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
    
    def get_game_state_summary(self) -> Dict[str, Any]:
        """Get a summary of the current game state"""
        return {
            'current_node': self.game_state['current_node'],
            'flags': self.game_state['flags'],
            'history_length': len(self.game_state['history']),
            'available_nodes': list(self.plot_graph.keys())
        }
    
    def reset_game(self):
        """Reset the game to initial state"""
        self.game_state = {
            'current_node': 'start_mission',
            'flags': self.database.get('story_flags', {}).copy(),
            'history': [],
            'scene_cache': {}
        }
        
        # Find starting node
        if 'start_mission' not in self.plot_graph:
            first_node = next(iter(self.plot_graph.keys())) if self.plot_graph else None
            self.game_state['current_node'] = first_node