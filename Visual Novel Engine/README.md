# Visual Novel Engine - README

## Quick Start

1. **Install dependencies**
   ```bash
   npm install
   ```

2. **Write your story**
   - Edit `public/story_script.md` with your visual novel content
   - Follow the markdown template structure (see WORKFLOW.md)

3. **Parse markdown to JSON**
   ```bash
   node test_parser_simple.js
   ```

4. **Run the application**
   ```bash
   npm start
   ```

5. **Open browser** at `http://localhost:3000` and enjoy your interactive story!

## File Structure & Descriptions

### Core Application
- **`src/App.js`** - Main React app component, renders the VN engine
- **`src/components/VNEngineNew.jsx`** - Core visual novel engine with scene management, dialogue system, and choice handling
- **`src/components/AudioManager.jsx`** - Background music controller with mood-based track selection and autoplay handling
- **`src/components/CharacterDisplay.jsx`** - Character sprite renderer with expression animations
- **`src/components/TextBox.jsx`** - Dialogue text display with typing effects and character name display
- **`src/components/ChoiceMenu.jsx`** - Interactive choice buttons for player decisions

### Utilities & Services
- **`src/utils/MarkdownParser.js`** - Converts structured markdown to VN-compatible JSON format
- **`src/utils/GameConfig.js`** - Game configuration manager for settings and preferences
- **`src/utils/MoodMusicMapper.js`** - Maps scene moods to appropriate background music tracks

### Content & Assets
- **`public/story_script.md`** - Your story content in markdown format (edit this!)
- **`public/generated_story_script.json`** - Auto-generated JSON from markdown parser
- **`public/fixed_story_script.json`** - Previous story format (legacy)
- **`public/Kurisu/`** - Character sprite images with different expressions
- **`public/Music/`** - Background music files for different moods
- **`public/backgrounds/`** - Scene background images

### Development & Testing
- **`test_parser_simple.js`** - Standalone script to test markdown-to-JSON conversion
- **`WORKFLOW.md`** - Detailed documentation of the markdown format and system architecture
- **`package.json`** - Node.js dependencies and build scripts
- **`tailwind.config.js`** - Styling configuration for the visual novel interface

### Build Configuration
- **`postcss.config.js`** - CSS processing configuration
- **`src/index.js`** - React application entry point
- **`src/index.css`** - Global styles and CSS imports

## Development Workflow

1. **Story Creation**: Write/edit `public/story_script.md`
2. **Parse**: Run `node test_parser_simple.js` to generate JSON
3. **Test**: Use `npm start` to preview in browser
4. **Iterate**: Repeat steps 1-3 until satisfied
5. **Deploy**: Use `npm run build` for production

Perfect for rapid visual novel development and LLM-generated interactive stories!