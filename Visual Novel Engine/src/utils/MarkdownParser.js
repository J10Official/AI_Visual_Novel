/**
 * Markdown to JSON Parser for Visual Novel Scripts
 * Converts structured markdown format to the JSON format expected by VNEngineNew
 */

export class MarkdownParser {
  constructor() {
    this.scenes = {};
    this.currentScene = null;
    this.parseMode = null; // 'SCENE', 'SCRIPT', 'PATHS'
  }

  /**
   * Main parsing function
   */
  parse(markdownContent) {
    const lines = markdownContent.split('\n');
    this.scenes = {};
    this.currentScene = null;
    this.parseMode = null;

    for (let i = 0; i < lines.length; i++) {
      const line = lines[i].trim();
      
      if (line === '') continue;
      
      if (line === '::SCENE::') {
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
      
      // Parse based on current mode
      if (this.parseMode === 'SCENE') {
        this.parseSceneProperty(line);
      } else if (this.parseMode === 'SCRIPT') {
        this.parseScriptLine(line);
      } else if (this.parseMode === 'PATHS') {
        this.parsePathLine(line);
      }
    }
    
    // Finalize the last scene
    this.finalizeCurrentScene();
    
    return this.scenes;
  }

  /**
   * Parse scene properties (location, mood, etc.)
   */
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

  /**
   * Parse script lines (character dialogue)
   */
  parseScriptLine(line) {
    if (!this.currentScene) return;
    
    const colonIndex = line.indexOf(':');
    if (colonIndex === -1) return;
    
    const key = line.substring(0, colonIndex).trim();
    const value = line.substring(colonIndex + 1).trim();
    
    // Find the current script entry being built
    let currentScriptEntry = this.currentScene.SCRIPT[this.currentScene.SCRIPT.length - 1];
    
    switch (key) {
      case 'CHARACTER':
        // Start a new script entry
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

  /**
   * Parse path lines (choices)
   */
  parsePathLine(line) {
    if (!this.currentScene) return;
    
    const colonIndex = line.indexOf(':');
    if (colonIndex === -1) return;
    
    const key = line.substring(0, colonIndex).trim();
    const value = line.substring(colonIndex + 1).trim();
    
    // Find the current path entry being built
    let currentPathEntry = this.currentScene.PATHS[this.currentScene.PATHS.length - 1];
    
    switch (key) {
      case 'CHOICE':
        // Start a new path entry
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

  /**
   * Finalize the current scene and add it to scenes collection
   */
  finalizeCurrentScene() {
    if (!this.currentScene) return;
    
    // Generate scene ID from location or use index
    const sceneId = this.currentScene.LOCATION
      ? this.currentScene.LOCATION.toLowerCase().replace(/\s+/g, '_').replace(/[^a-z0-9_]/g, '')
      : `scene_${Object.keys(this.scenes).length + 1}`;
    
    this.scenes[sceneId] = this.currentScene;
    this.currentScene = null;
  }

  /**
   * Validate the parsed JSON against the expected format
   */
  validate(parsedScenes) {
    const errors = [];
    
    for (const [sceneId, scene] of Object.entries(parsedScenes)) {
      // Check required scene properties
      if (!scene.LOCATION) {
        errors.push(`Scene ${sceneId}: Missing LOCATION`);
      }
      
      if (!scene.MOOD) {
        errors.push(`Scene ${sceneId}: Missing MOOD`);
      }
      
      if (!Array.isArray(scene.CHARACTERS) || scene.CHARACTERS.length === 0) {
        errors.push(`Scene ${sceneId}: Missing or invalid CHARACTERS array`);
      }
      
      // Check script entries
      if (!Array.isArray(scene.SCRIPT) || scene.SCRIPT.length === 0) {
        errors.push(`Scene ${sceneId}: Missing or empty SCRIPT array`);
      } else {
        scene.SCRIPT.forEach((entry, index) => {
          if (!entry.CHARACTER) {
            errors.push(`Scene ${sceneId}, Script ${index}: Missing CHARACTER`);
          }
          if (!entry.LINE) {
            errors.push(`Scene ${sceneId}, Script ${index}: Missing LINE`);
          }
          if (!entry.EXPRESSION) {
            errors.push(`Scene ${sceneId}, Script ${index}: Missing EXPRESSION`);
          }
        });
      }
      
      // Check paths (choices)
      if (Array.isArray(scene.PATHS)) {
        scene.PATHS.forEach((path, index) => {
          if (!path.CHOICE) {
            errors.push(`Scene ${sceneId}, Path ${index}: Missing CHOICE`);
          }
          if (!path.TARGET) {
            errors.push(`Scene ${sceneId}, Path ${index}: Missing TARGET`);
          }
        });
      }
    }
    
    return {
      isValid: errors.length === 0,
      errors: errors
    };
  }

  /**
   * Convert parsed scenes to the exact format expected by VNEngineNew
   */
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

  /**
   * Utility function to parse markdown file and return VN-ready JSON
   */
  static parseMarkdownToVN(markdownContent) {
    const parser = new MarkdownParser();
    const parsedScenes = parser.parse(markdownContent);
    const validation = parser.validate(parsedScenes);
    
    if (!validation.isValid) {
      console.warn('⚠️ Validation warnings:', validation.errors);
    }
    
    return parser.toVNEngineFormat(parsedScenes);
  }
}

// Export for use in other modules
export default MarkdownParser;