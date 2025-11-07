/**
 * Simple test runner for the Markdown Parser
 * This tests the parser by converting the markdown story to JSON
 */

const fs = require('fs');

// Inline the MarkdownParser class for testing
class MarkdownParser {
  constructor() {
    this.scenes = {};
    this.currentScene = null;
    this.parseMode = null;
  }

  parse(markdownContent) {
    const lines = markdownContent.split('\n');
    this.scenes = {};
    this.currentScene = null;
    this.parseMode = null;

    for (let i = 0; i < lines.length; i++) {
      const line = lines[i].trim();
      
      if (line === '') continue;
      
      if (line === '::SCENE::') {
        this.finalizeCurrentScene();
        this.parseMode = 'SCENE';
        this.currentScene = {
          LOCATION: '',
          MOOD: '',
          CHARACTERS: [],
          BACKGROUND_IMAGE: '',
          BACKGROUND_EDIT: '',
          SCRIPT: [],
          PATHS: []
        };
        continue;
      }
      
      if (line === '::SCRIPT::') {
        this.parseMode = 'SCRIPT';
        continue;
      }
      
      if (line === '::PATHS::') {
        this.parseMode = 'PATHS';
        continue;
      }
      
      if (this.parseMode === 'SCENE') {
        this.parseSceneProperty(line);
      } else if (this.parseMode === 'SCRIPT') {
        this.parseScriptLine(line);
      } else if (this.parseMode === 'PATHS') {
        this.parsePathLine(line);
      }
    }
    
    this.finalizeCurrentScene();
    return this.scenes;
  }

  parseSceneProperty(line) {
    if (!this.currentScene) return;
    
    const colonIndex = line.indexOf(':');
    if (colonIndex === -1) return;
    
    const key = line.substring(0, colonIndex).trim();
    const value = line.substring(colonIndex + 1).trim();
    
    switch (key) {
      case 'LOCATION':
        this.currentScene.LOCATION = value;
        break;
      case 'MOOD':
        this.currentScene.MOOD = value;
        break;
      case 'CHARACTERS':
        this.currentScene.CHARACTERS = value.split(',').map(c => c.trim());
        break;
      case 'BACKGROUND_IMAGE':
        this.currentScene.BACKGROUND_IMAGE = value;
        break;
      case 'BACKGROUND_EDIT':
        this.currentScene.BACKGROUND_EDIT = value === 'null' ? '' : value;
        break;
    }
  }

  parseScriptLine(line) {
    if (!this.currentScene) return;
    
    const colonIndex = line.indexOf(':');
    if (colonIndex === -1) return;
    
    const key = line.substring(0, colonIndex).trim();
    const value = line.substring(colonIndex + 1).trim();
    
    let currentScriptEntry = this.currentScene.SCRIPT[this.currentScene.SCRIPT.length - 1];
    
    switch (key) {
      case 'CHARACTER':
        currentScriptEntry = {
          CHARACTER: value,
          LINE: '',
          EXPRESSION: 'neutral'
        };
        this.currentScene.SCRIPT.push(currentScriptEntry);
        break;
      case 'LINE':
        if (currentScriptEntry) {
          currentScriptEntry.LINE = value;
        }
        break;
      case 'EXPRESSION':
        if (currentScriptEntry) {
          currentScriptEntry.EXPRESSION = value === 'null' ? 'neutral' : value.toLowerCase();
        }
        break;
    }
  }

  parsePathLine(line) {
    if (!this.currentScene) return;
    
    const colonIndex = line.indexOf(':');
    if (colonIndex === -1) return;
    
    const key = line.substring(0, colonIndex).trim();
    const value = line.substring(colonIndex + 1).trim();
    
    let currentPathEntry = this.currentScene.PATHS[this.currentScene.PATHS.length - 1];
    
    switch (key) {
      case 'CHOICE':
        currentPathEntry = {
          CHOICE: value,
          TARGET: '',
          STATE_CHANGE: null,
          CONDITION: null
        };
        this.currentScene.PATHS.push(currentPathEntry);
        break;
      case 'TARGET':
        if (currentPathEntry) {
          currentPathEntry.TARGET = value;
        }
        break;
      case 'STATE_CHANGE':
        if (currentPathEntry) {
          currentPathEntry.STATE_CHANGE = value === 'null' ? null : value;
        }
        break;
      case 'CONDITION':
        if (currentPathEntry) {
          currentPathEntry.CONDITION = value === 'null' ? null : value;
        }
        break;
    }
  }

  finalizeCurrentScene() {
    if (!this.currentScene) return;
    
    const sceneId = this.currentScene.LOCATION
      ? this.currentScene.LOCATION.toLowerCase().replace(/\s+/g, '_').replace(/[^a-z0-9_]/g, '')
      : `scene_${Object.keys(this.scenes).length + 1}`;
    
    this.scenes[sceneId] = this.currentScene;
    this.currentScene = null;
  }

  toVNEngineFormat(parsedScenes) {
    const result = [];
    
    for (const [sceneId, scene] of Object.entries(parsedScenes)) {
      result.push({
        id: sceneId,
        SCENE: {
          LOCATION: scene.LOCATION,
          MOOD: scene.MOOD,
          CHARACTERS: scene.CHARACTERS,
          BACKGROUND_IMAGE: scene.BACKGROUND_IMAGE || 'lab.jpg',
          BACKGROUND_EDIT: scene.BACKGROUND_EDIT || null
        },
        SCRIPT: scene.SCRIPT,
        PATHS: scene.PATHS
      });
    }
    
    return result;
  }
}

// Main test function
function testParser() {
  console.log('🚀 Testing Markdown Parser');
  console.log('===========================\n');

  try {
    // Read markdown file
    console.log('📖 Reading story_script.md...');
    const markdownContent = fs.readFileSync('./public/story_script.md', 'utf8');
    console.log(`✅ Loaded ${markdownContent.split('\n').length} lines\n`);

    // Parse markdown
    console.log('🔄 Parsing markdown...');
    const parser = new MarkdownParser();
    const scenes = parser.parse(markdownContent);
    console.log(`✅ Parsed ${Object.keys(scenes).length} scenes\n`);

    // Convert to VN format
    console.log('🎮 Converting to VN Engine format...');
    const vnFormat = parser.toVNEngineFormat(scenes);

    // Save result
    const outputPath = './public/generated_story_script.json';
    fs.writeFileSync(outputPath, JSON.stringify(vnFormat, null, 2));
    console.log(`💾 Saved to ${outputPath}\n`);

    // Show summary
    console.log('📊 Generated Scenes:');
    console.log('===================');
    vnFormat.forEach(sceneObj => {
      console.log(`🎬 ${sceneObj.id}: ${sceneObj.SCENE.LOCATION} (${sceneObj.SCRIPT.length} lines, ${sceneObj.PATHS.length} choices)`);
    });

    console.log('\n✅ Parser test completed successfully!');
    return true;

  } catch (error) {
    console.error('❌ Test failed:', error.message);
    return false;
  }
}

// Run the test
const success = testParser();
process.exit(success ? 0 : 1);