"""
Full Gemini-Powered Visual Novel Application
Uses Gemini API for both content generation and image creation
"""

import os
from flask import Flask, render_template, jsonify, request, send_from_directory
from core.state_manager import StateManager

app = Flask(__name__)

# Initialize the full state manager with Gemini capabilities
try:
    state_manager = StateManager('Plotpoint_graph', 'Database')
    print("Full Gemini-powered game initialized successfully!")
    print(f"Available nodes: {list(state_manager.plot_graph.keys())}")
    print(f"Database loaded: {len(state_manager.database.get('characters', {}))} characters, {len(state_manager.database.get('locations', {}))} locations")
    print(f"Image generator: {type(state_manager.image_generator).__name__}")
    print(f"Director LLM: {type(state_manager.director).__name__}")
except Exception as e:
    print(f"Error initializing full game: {e}")
    print("Make sure you have:")
    print("1. Set GEMINI_API_KEY in .env file")
    print("2. Installed google-generativeai: pip install google-generativeai")
    state_manager = None

@app.route('/')
def index():
    """Main game interface"""
    return render_template('index.html')

@app.route('/api/current_scene')
def get_current_scene():
    """Get the current scene data"""
    if not state_manager:
        return jsonify({'error': 'Game not initialized'}), 500
    
    try:
        print(f"🎬 SCENE REQUEST: Current node = {state_manager.game_state['current_node']}")
        scene = state_manager.get_current_scene()
        print(f"   Scene generated with {len(scene.get('paths', []))} choices")
        return jsonify(scene)
    except Exception as e:
        print(f"Error getting current scene: {e}")
        return jsonify({'error': str(e)}), 500

@app.route('/api/scene_json')
def get_scene_json():
    """Get the raw JSON structure for debugging"""
    if not state_manager:
        return jsonify({'error': 'Game not initialized'}), 500
    
    try:
        scene = state_manager.get_current_scene()
        # Return formatted JSON for inspection
        return jsonify({
            'scene_data': scene,
            'current_node': state_manager.game_state['current_node'],
            'flags': state_manager.game_state['flags'],
            'director_type': type(state_manager.director).__name__,
            'image_generator_type': type(state_manager.image_generator).__name__
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/make_choice', methods=['POST'])
def make_choice():
    """Handle player choice"""
    if not state_manager:
        return jsonify({'error': 'Game not initialized'}), 500
    
    data = request.get_json()
    choice_index = data.get('choice_index')
    
    print(f"🎮 CHOICE MADE: Index {choice_index}")
    print(f"   Current node before: {state_manager.game_state['current_node']}")
    
    if choice_index is None:
        return jsonify({'error': 'No choice index provided'}), 400
    
    try:
        success = state_manager.make_choice(choice_index)
        print(f"   Choice success: {success}")
        print(f"   Current node after: {state_manager.game_state['current_node']}")
        
        if success:
            return jsonify({'success': True})
        else:
            return jsonify({'error': 'Invalid choice index'}), 400
    except Exception as e:
        print(f"Error making choice: {e}")
        return jsonify({'error': str(e)}), 500

@app.route('/api/reset_game', methods=['POST'])
def reset_game():
    """Reset the game to initial state"""
    if not state_manager:
        return jsonify({'error': 'Game not initialized'}), 500
    
    try:
        state_manager.reset_game()
        return jsonify({'success': True})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/game_state')
def get_game_state():
    """Get current game state summary"""
    if not state_manager:
        return jsonify({'error': 'Game not initialized'}), 500
    
    try:
        state = state_manager.get_game_state_summary()
        return jsonify(state)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/static/generated_assets/<path:filename>')
def generated_assets(filename):
    """Serve generated assets"""
    return send_from_directory('static/generated_assets', filename)

@app.route('/static/placeholder_bg.png')
def placeholder_background():
    """Serve a placeholder background if needed"""
    # Create a simple placeholder if it doesn't exist
    placeholder_path = 'static/placeholder_bg.png'
    if not os.path.exists(placeholder_path):
        from PIL import Image, ImageDraw
        img = Image.new('RGB', (800, 600), (30, 30, 50))
        draw = ImageDraw.Draw(img)
        draw.text((350, 290), "Background Loading...", fill=(100, 100, 100))
        os.makedirs('static', exist_ok=True)
        img.save(placeholder_path)
    
    return send_from_directory('static', 'placeholder_bg.png')

@app.route('/debug')
def debug_info():
    """Debug page showing system information"""
    if not state_manager:
        return "Game not initialized"
    
    debug_data = {
        'plot_graph_nodes': list(state_manager.plot_graph.keys()),
        'current_node': state_manager.game_state['current_node'],
        'flags': state_manager.game_state['flags'],
        'history_length': len(state_manager.game_state['history']),
        'director_type': type(state_manager.director).__name__,
        'image_generator_type': type(state_manager.image_generator).__name__,
        'database_summary': {
            'characters': len(state_manager.database.get('characters', {})),
            'locations': len(state_manager.database.get('locations', {})),
            'expressions': len(state_manager.database.get('expressions', [])),
            'moods': len(state_manager.database.get('moods', [])),
        }
    }
    
    return f"<pre>{jsonify(debug_data).get_data(as_text=True)}</pre>"

if __name__ == '__main__':
    if not state_manager:
        print("\n❌ STARTUP FAILED")
        print("Could not initialize the full Gemini-powered application.")
        print("\nPlease ensure:")
        print("1. ✅ .env file exists with valid GEMINI_API_KEY")
        print("2. ✅ All packages installed: pip install google-generativeai requests pillow flask python-dotenv")
        print("3. ✅ Plotpoint_graph and Database files are present")
        exit(1)
    
    print("\n🚀 GENERATIVE VISUAL NOVEL - FULL VERSION")
    print("=" * 50)
    print("🤖 AI-Powered Content Generation: ✅ ACTIVE")
    print("🎨 Gemini Image Generation: ✅ ACTIVE") 
    print("📖 Dynamic Story Generation: ✅ ACTIVE")
    print("🎮 Interactive Interface: ✅ READY")
    print("=" * 50)
    print("\n🌐 Server starting at: http://localhost:5000")
    print("🔍 Debug info available at: http://localhost:5000/debug")
    print("📋 Raw JSON endpoint: http://localhost:5000/api/scene_json")
    print("\n💡 Features:")
    print("   • Gemini-generated narrative content")
    print("   • AI-enhanced background images")
    print("   • Dynamic scene descriptions")
    print("   • Conditional choice branching")
    print("   • Real-time content generation")
    print("\n⚡ Ready to generate your story!")
    print("Press Ctrl+C to stop")
    
    app.run(debug=True, host='0.0.0.0', port=5000)