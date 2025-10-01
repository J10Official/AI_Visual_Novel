"""
Flask Application for Generative Visual Novel Prototype
Main entry point for the web interface
"""

import os
from flask import Flask, render_template, jsonify, request, send_from_directory
from core.state_manager import StateManager

app = Flask(__name__)

# Initialize the state manager
try:
    state_manager = StateManager('Plotpoint_graph', 'Database')
    print("Game initialized successfully!")
    print(f"Available nodes: {list(state_manager.plot_graph.keys())}")
    print(f"Database loaded: {len(state_manager.database.get('characters', {}))} characters, {len(state_manager.database.get('locations', {}))} locations")
except Exception as e:
    print(f"Error initializing game: {e}")
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
        scene = state_manager.get_current_scene()
        return jsonify(scene)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/make_choice', methods=['POST'])
def make_choice():
    """Handle player choice"""
    if not state_manager:
        return jsonify({'error': 'Game not initialized'}), 500
    
    data = request.get_json()
    choice_index = data.get('choice_index')
    
    if choice_index is None:
        return jsonify({'error': 'No choice index provided'}), 400
    
    try:
        success = state_manager.make_choice(choice_index)
        if success:
            return jsonify({'success': True})
        else:
            return jsonify({'error': 'Invalid choice index'}), 400
    except Exception as e:
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

if __name__ == '__main__':
    if not state_manager:
        print("Error: Could not initialize state manager. Please check your Plotpoint_graph and Database files.")
        print("Make sure you have:")
        print("1. Created a .env file with GEMINI_API_KEY")
        print("2. Installed requirements: pip install -r requirements.txt")
        exit(1)
    
    print("\n=== Generative Visual Novel Prototype ===")
    print("Starting server...")
    print("Open your browser and navigate to: http://localhost:5000")
    print("Press Ctrl+C to stop the server")
    print("\nGame Features:")
    print("- Dynamic scene generation using Gemini API")
    print("- Procedural background generation")
    print("- Flag-based conditional choices")
    print("- Interactive web interface")
    print("\nMake sure you've set up your .env file with GEMINI_API_KEY!")
    
    app.run(debug=True, host='0.0.0.0', port=5000)