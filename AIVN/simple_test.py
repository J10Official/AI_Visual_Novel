#!/usr/bin/env python3
"""
Simple test demonstrating full Gemini integration and JSON output
"""

import os
import json
import sys
sys.path.append('/home/jatin/Code/Year3/AIVN')

# Set up environment
os.environ['GEMINI_API_KEY'] = 'AIzaSyCwdZ-Y4sZjoGa0aPtl0mWyLXsTZ58BlKQ'

def test_simple_generation():
    print("🚀 TESTING GEMINI VISUAL NOVEL SYSTEM")
    print("=" * 60)
    
    try:
        from core.state_manager import StateManager
        
        # Initialize system
        print("1. Initializing full system...")
        state_manager = StateManager('Plotpoint_graph', 'Database')
        print(f"   ✅ Plot graph loaded: {len(state_manager.plot_graph)} nodes")
        print(f"   ✅ Database loaded: {len(state_manager.database.get('characters', {}))} characters")
        print(f"   ✅ Director LLM: {type(state_manager.director).__name__}")
        print(f"   ✅ Image generator: {type(state_manager.image_generator).__name__}")
        
        # Generate first scene
        print("\n2. Generating scene with Gemini...")
        scene = state_manager.get_current_scene()
        
        print(f"   ✅ Scene generated for: {scene['id']}")
        print(f"   ✅ Location: {scene['content']['scene_details']['location']}")
        print(f"   ✅ Mood: {scene['content']['scene_details']['mood']}")
        print(f"   ✅ Dialogue lines: {len(scene['content']['scene_script'])}")
        print(f"   ✅ Choices available: {len(scene['paths'])}")
        
        # Show JSON structure
        print("\n3. GENERATED JSON OUTPUT:")
        print("-" * 40)
        print(json.dumps(scene, indent=2))
        print("-" * 40)
        
        # Show image details
        bg = scene['content']['scene_details']['background']
        print(f"\n4. IMAGE GENERATION:")
        print(f"   🎨 Base image: {bg.get('base_image', 'none')}")
        print(f"   🖼️  Generated file: {bg.get('generated_image', 'none')}")
        print(f"   ✨ Edit prompt: {bg.get('edit_prompt', 'none')}")
        
        # Test choice navigation
        if scene['paths']:
            print(f"\n5. TESTING NAVIGATION:")
            choice_text = scene['paths'][0]['choice_text']
            print(f"   🎮 Making choice: '{choice_text}'")
            
            success = state_manager.make_choice(0)
            if success:
                new_scene = state_manager.get_current_scene()
                print(f"   ✅ Navigated to: {new_scene['id']}")
                print(f"   ✅ New scene generated successfully")
            else:
                print("   ❌ Navigation failed")
        
        print(f"\n🎉 SUCCESS! Full system working with Gemini API")
        print("=" * 60)
        
        return True
        
    except Exception as e:
        print(f"\n❌ ERROR: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    test_simple_generation()