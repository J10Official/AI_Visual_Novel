"""
Demo Director LLM Interface - No API Required
Provides pre-written examples for testing without requiring API access
"""

import json
from typing import Dict, Any

class DemoDirectorLLM:
    def __init__(self):
        # Pre-written scenes for demonstration
        self.demo_scenes = {
            'start_mission': {
                "id": "start_mission",
                "content": {
                    "scene_script": [
                        {
                            "character": "Narrator",
                            "line": "The neon-soaked rain cascades down your hab-unit's panoramic window, creating a kaleidoscope of bleeding colors against the darkness. The eternal storm of Aethelburg never truly stops, only pauses to gather strength.",
                            "expression": None
                        },
                        {
                            "character": "Anya",
                            "line": "Kaelen, I need you to listen carefully. This isn't your typical ghost signal—the energy patterns are unlike anything in our databases. Something in Sector Gamma-7 is calling out, and frankly, that terrifies me more than any conventional threat.",
                            "expression": "Afraid"
                        },
                        {
                            "character": "Narrator", 
                            "line": "Anya's holographic form flickers slightly, betraying the urgency behind her composed exterior. The blue glow of her projection casts strange shadows across your sparse living space.",
                            "expression": None
                        }
                    ],
                    "scene_details": {
                        "mood": "rising_tension",
                        "location": "kaelens_hab",
                        "characters_present": ["Narrator", "Anya"],
                        "background": {
                            "base_image": "art/backgrounds/hab_unit_night_rain.png",
                            "edit_prompt": "Add more dramatic lightning flashes in the stormy sky, enhance the neon reflections"
                        }
                    }
                }
            },
            
            'anya_intel_briefing': {
                "id": "anya_intel_briefing",
                "content": {
                    "scene_script": [
                        {
                            "character": "Anya",
                            "line": "The Med-Tech quarter was abandoned after the synth-plague outbreak fifteen years ago. Official reports claim complete sterilization, but our sensors are detecting active energy signatures that predate any known human technology.",
                            "expression": "Afraid"
                        },
                        {
                            "character": "Narrator",
                            "line": "The holographic schematic rotates slowly, revealing the labyrinthine structure of Gamma-7. Red warning indicators pulse at multiple breach points, like digital wounds in the station's hull.",
                            "expression": None
                        },
                        {
                            "character": "Anya",
                            "line": "I'm sending you the access codes now. Remember—this is reconnaissance only. If you encounter anything beyond our threat parameters, retreat immediately and report back.",
                            "expression": "Angry"
                        }
                    ],
                    "scene_details": {
                        "mood": "dread",
                        "location": "kaelens_hab", 
                        "characters_present": ["Anya"],
                        "background": {
                            "base_image": "art/backgrounds/hab_unit_night_rain.png",
                            "edit_prompt": "Display holographic schematics floating in the air, blue technical diagrams overlaying the scene"
                        }
                    }
                }
            },
            
            'contact_silas': {
                "id": "contact_silas",
                "content": {
                    "scene_script": [
                        {
                            "character": "Narrator",
                            "line": "The encrypted channel crackles with interference before Silas's paranoid whisper cuts through the static. Years of hiding in the digital underground have made him perpetually suspicious of every shadow.",
                            "expression": None
                        },
                        {
                            "character": "Silas",
                            "line": "Kaelen? Christ, I thought you were dead. Listen to me very carefully—Gamma-7 isn't just abandoned, it's quarantined for reasons the Bureau will never tell you. They buried something down there that should have stayed buried.",
                            "expression": "Afraid"
                        },
                        {
                            "character": "Silas", 
                            "line": "Meet me at The Glitch in one hour. Come alone, sweep for surveillance, and for the love of everything digital, don't let the Bureau know you contacted me. Some secrets are worth more than careers, Kaelen.",
                            "expression": "Angry"
                        }
                    ],
                    "scene_details": {
                        "mood": "dread",
                        "location": "kaelens_hab",
                        "characters_present": ["Narrator", "Silas"],
                        "background": {
                            "base_image": "art/backgrounds/hab_unit_night_rain.png", 
                            "edit_prompt": "Add static interference effects and dark, ominous shadows in the corners"
                        }
                    }
                }
            },
            
            'the_glitch_bar': {
                "id": "the_glitch_bar",
                "content": {
                    "scene_script": [
                        {
                            "character": "Narrator",
                            "line": "The Glitch reeks of synthetic alcohol and ozone. Holographic advertisements flicker erratically overhead while data-runners conduct their business in whispered code. Silas sits hunched in the darkest corner, a ghost of his former self.",
                            "expression": None
                        },
                        {
                            "character": "Silas",
                            "line": "You look surprised to see me alive. Smart. I've been dead to the Bureau for three years now, ever since I stumbled onto Project Chimera. This nullifier will let you see what's really down there—not the shadows they want you to see.",
                            "expression": "Afraid"
                        },
                        {
                            "character": "Narrator",
                            "line": "The chroniton nullifier gleams under the bar's sickly lighting. It's smaller than you expected, but you can feel the latent energy humming within its crystalline core.",
                            "expression": None
                        },
                        {
                            "character": "Silas",
                            "line": "Whatever you find down there, don't trust the Bureau with it. They've been hunting for this technology for decades, and they'll burn anyone who gets in their way. Even you.",
                            "expression": "Angry"
                        }
                    ],
                    "scene_details": {
                        "mood": "dread",
                        "location": "the_glitch",
                        "characters_present": ["Narrator", "Silas"],
                        "background": {
                            "base_image": "art/backgrounds/glitch_bar_interior.png",
                            "edit_prompt": "Emphasize the shadowy corners and flickering holo-ads, add smoke and mysterious figures"
                        }
                    }
                }
            }
        }
    
    def generate_scene(self, plot_point: Dict[str, Any], database: Dict[str, Any], game_state: Dict[str, Any]) -> Dict[str, Any]:
        """Generate a scene using pre-written demo content"""
        
        node_id = plot_point.get('id', 'unknown')
        
        if node_id in self.demo_scenes:
            scene = self.demo_scenes[node_id].copy()
            
            # Add paths from plot point
            scene['paths'] = []
            if 'choices' in plot_point:
                for choice in plot_point['choices']:
                    scene['paths'].append({
                        'choice_text': choice['text'],
                        'target_node': choice['target']
                    })
            
            return scene
        else:
            # Fallback to basic scene for nodes without demo content
            return self._create_basic_scene(plot_point)
    
    def _create_basic_scene(self, plot_point: Dict[str, Any]) -> Dict[str, Any]:
        """Create a basic scene for nodes without demo content"""
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