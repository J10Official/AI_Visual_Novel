"""
Demo version of the Flask Application
Runs without requiring Gemini API for testing purposes
"""

import os
from flask import Flask, render_template, jsonify, request, send_from_directory

# Import demo version instead of real LLM
from core.state_manager import StateManager
from core.demo_director import DemoDirectorLLM

app = Flask(__name__)

class DemoStateManager(StateManager):
    """Modified state manager that uses demo content instead of real LLM"""
    
    def __init__(self, plot_graph_path: str, database_path: str):
        # Initialize parsers and asset generator
        from core.parser import PlotPointParser, DatabaseParser
        from core.asset_generator import AssetGenerator
        
        self.plot_parser = PlotPointParser()
        self.db_parser = DatabaseParser()
        self.director = DemoDirectorLLM()  # Use demo director instead
        self.asset_generator = AssetGenerator()
        
        # Load game data
        self.plot_graph = self.plot_parser.parse_plot_point_graph(plot_graph_path)
        self.database = self.db_parser.parse_database(database_path)
        
        # Initialize game state
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

# Initialize the demo state manager
try:
    state_manager = DemoStateManager('Plotpoint_graph', 'Database')
    print("Demo game initialized successfully!")
    print(f"Available nodes: {list(state_manager.plot_graph.keys())}")
    print(f"Database loaded: {len(state_manager.database.get('characters', {}))} characters, {len(state_manager.database.get('locations', {}))} locations")
except Exception as e:
    print(f"Error initializing demo game: {e}")
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
        print("Error: Could not initialize demo state manager.")
        exit(1)
    
    print("\n=== Generative Visual Novel DEMO ===")
    print("Starting demo server (no API key required)...")
    print("Open your browser and navigate to: http://localhost:5000")
    print("Press Ctrl+C to stop the server")
    print("\nDemo Features:")
    print("- Pre-written dynamic scenes for first 4 nodes")
    print("- Procedural background generation")
    print("- Flag-based conditional choices")
    print("- Interactive web interface")
    print("- No API key required!")
    print("\nNote: This demo uses pre-written content. For full AI generation,")
    print("use app.py with a valid Gemini API key.")
    
    app.run(debug=True, host='0.0.0.0', port=5000)