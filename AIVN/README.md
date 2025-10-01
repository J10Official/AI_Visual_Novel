# Generative Visual Novel Prototype

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Create a `.env` file with your Gemini API key:
```
GEMINI_API_KEY=your_api_key_here
```

3. Run the application:
```bash
python app.py
```

4. Open your browser and navigate to `http://localhost:5000`

## Project Structure

- `app.py` - Main Flask application
- `core/` - Core system components
  - `state_manager.py` - Manages game state and plot point navigation
  - `director_llm.py` - Interfaces with Gemini API for content generation
  - `asset_generator.py` - Handles background generation
  - `parser.py` - Parses plot point graphs and database files
- `templates/` - HTML templates
- `static/` - CSS, JS, and generated assets
- `Plotpoint_graph` - Example story structure
- `Database` - Character, location, and asset definitions

## Features Implemented

- Plot point graph parsing and navigation
- Gemini API integration for dynamic content generation
- Flag-based conditional choices
- Simple background generation
- Interactive web interface
- JSON-structured output from Director LLM

## Limitations (Prototype)

- No tiered memory system (as requested)
- Simple background generation instead of actual image editing
- No character sprites (would require pre-drawn assets)
- No audio system