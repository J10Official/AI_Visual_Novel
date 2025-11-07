import React, { useState, useEffect, useCallback } from 'react';
import { FaVolumeUp, FaVolumeMute, FaCog } from 'react-icons/fa';
import AudioManager from './AudioManager';
import CharacterDisplay from './CharacterDisplay';
import TextBox from './TextBox';
import ChoiceMenu from './ChoiceMenu';
import Background from './Background';
import { MoodMusicMapper } from '../utils/MoodMusicMapper';

const VNEngineNew = () => {
  const [gameState, setGameState] = useState({
    currentSceneId: null,
    currentScriptIndex: 0,
    isLoading: true,
    script: null, // Array of scenes in new format
    scenesById: {}, // Map for quick scene lookup by id
    choices: null,
    showChoices: false,
    isTextComplete: false,
    isGameComplete: false,
  });

  const [settings, setSettings] = useState({
    textSpeed: 50,
    musicVolume: 0.7,
    soundEffectsVolume: 0.8,
    isMuted: false,
  });

  const [debugMode, setDebugMode] = useState(true);

  // Enhanced logging function
  const log = useCallback((message, data = null, level = 'info') => {
    if (!debugMode) return;
    
    const timestamp = new Date().toLocaleTimeString();
    const prefix = `🎮 [${timestamp}] VNEngineNew:`;
    
    switch (level) {
      case 'error':
        console.error(`❌ ${prefix}`, message, data);
        break;
      case 'warn':
        console.warn(`⚠️ ${prefix}`, message, data);
        break;
      case 'debug':
        console.debug(`🔍 ${prefix}`, message, data);
        break;
      default:
        console.log(`ℹ️ ${prefix}`, message, data);
    }
  }, [debugMode]);

  // Convert old format to new format
  const convertOldFormatToNew = useCallback((oldScript) => {
    log('Converting old format to new format...');
    
    if (!oldScript.script || !Array.isArray(oldScript.script)) {
      return [];
    }

    return oldScript.script.map((scene, index) => {
      const sceneId = `scene_${index}`;
      
      // Convert interactions to new SCRIPT format
      const scriptEntries = [];
      const paths = [];
      
      scene.interactions?.forEach((interaction, interactionIndex) => {
        if (interaction.character_name === 'Player' && 
            (Array.isArray(interaction.dialogue) || 
             (typeof interaction.dialogue === 'object' && interaction.dialogue.choices))) {
          // This is a choice point - add choices to PATHS
          let choices = [];
          if (Array.isArray(interaction.dialogue)) {
            choices = interaction.dialogue.map(choice => ({ text: choice, outcome: 'next' }));
          } else if (interaction.dialogue.choices) {
            choices = interaction.dialogue.choices;
          }
          
          choices.forEach((choice, choiceIndex) => {
            paths.push({
              CHOICE: choice.text,
              TARGET: index < oldScript.script.length - 1 ? `scene_${index + 1}` : null,
              STATE_CHANGE: null,
              CONDITION: null
            });
          });
        } else {
          // Regular dialogue
          scriptEntries.push({
            CHARACTER: interaction.character_name,
            LINE: typeof interaction.dialogue === 'string' ? interaction.dialogue : JSON.stringify(interaction.dialogue),
            EXPRESSION: interaction.character_expression || 'neutral'
          });
        }
      });

      return {
        id: sceneId,
        SCENE: {
          LOCATION: scene.scene_name || `Scene ${index + 1}`,
          MOOD: 'Neutral',
          CHARACTERS: [...new Set(scriptEntries.map(s => s.CHARACTER))],
          BACKGROUND_IMAGE: 'lab.jpg',
          BACKGROUND_EDIT: null
        },
        SCRIPT: scriptEntries,
        PATHS: paths
      };
    });
  }, [log]);

  // Load script data
  useEffect(() => {
    const loadScript = async () => {
      try {
        log('Loading game configuration...');
        
        // Try to load the fixed story script first
        let scriptPath = '/generated_story_script.json';
        
        log(`Loading script from: ${scriptPath}`);
        
        const response = await fetch(scriptPath);
        
        if (!response.ok) {
          throw new Error(`Failed to load script: ${response.status} ${response.statusText}`);
        }
        
        const scriptData = await response.json();
        
        // Validate new format
        if (!Array.isArray(scriptData)) {
          throw new Error('Script must be an array of scenes');
        }

        // Create scenes by ID map for quick lookup
        const scenesById = {};
        scriptData.forEach(scene => {
          if (!scene.id) {
            log('Warning: Scene without ID found', scene, 'warn');
            return;
          }
          scenesById[scene.id] = scene;
        });

        log('Script loaded successfully', {
          totalScenes: scriptData.length,
          firstSceneId: scriptData[0]?.id,
          scenesWithIds: Object.keys(scenesById).length
        });
        
        // Initialize with first scene
        const firstSceneId = scriptData[0]?.id;
        if (!firstSceneId) {
          throw new Error('No valid first scene found');
        }
        
        setGameState(prev => ({
          ...prev,
          script: scriptData,
          scenesById: scenesById,
          currentSceneId: firstSceneId,
          currentScriptIndex: 0,
          isLoading: false,
        }));

        log('Game state initialized', {
          totalScenes: scriptData.length,
          firstScene: firstSceneId,
          currentScriptIndex: 0,
        });
        
      } catch (error) {
        log('Failed to load new format script', error, 'error');
        setGameState(prev => ({ ...prev, isLoading: false }));
        
        // Fallback to original script.json
        try {
          log('Attempting fallback to /script.json...');
          const fallbackResponse = await fetch('/script.json');
          if (fallbackResponse.ok) {
            const fallbackData = await fallbackResponse.json();
            // Convert old format to new format on the fly
            const convertedScript = convertOldFormatToNew(fallbackData);
            
            const scenesById = {};
            convertedScript.forEach(scene => {
              scenesById[scene.id] = scene;
            });
            
            setGameState(prev => ({
              ...prev,
              script: convertedScript,
              scenesById: scenesById,
              currentSceneId: convertedScript[0]?.id,
              currentScriptIndex: 0,
              isLoading: false,
            }));
            log('Fallback script loaded and converted successfully');
          }
        } catch (fallbackError) {
          log('Fallback loading also failed', fallbackError, 'error');
        }
      }
    };

    loadScript();
  }, [log, convertOldFormatToNew]);

  const getCurrentScene = useCallback(() => {
    if (!gameState.currentSceneId || !gameState.scenesById) return null;
    return gameState.scenesById[gameState.currentSceneId];
  }, [gameState.currentSceneId, gameState.scenesById]);

  const getCurrentScriptEntry = useCallback(() => {
    const scene = getCurrentScene();
    if (!scene?.SCRIPT) return null;
    return scene.SCRIPT[gameState.currentScriptIndex];
  }, [getCurrentScene, gameState.currentScriptIndex]);

  const getCurrentMusic = useCallback(() => {
    const scene = getCurrentScene();
    if (!scene?.SCENE?.MOOD) return 'ChillLofiR.mp3';
    return MoodMusicMapper.getMusicForMood(scene.SCENE.MOOD);
  }, [getCurrentScene]);

  const advanceScript = useCallback(() => {
    const scene = getCurrentScene();
    if (!scene) {
      log('Cannot advance: No current scene', null, 'warn');
      return;
    }

    const currentEntry = getCurrentScriptEntry();
    if (!currentEntry) {
      log('Cannot advance: No current script entry', null, 'warn');
      return;
    }

    log('Advancing script', {
      currentScene: gameState.currentSceneId,
      currentScriptIndex: gameState.currentScriptIndex,
      character: currentEntry.CHARACTER,
    });

    // Check if we're at the end of the current scene's script
    if (gameState.currentScriptIndex >= scene.SCRIPT.length - 1) {
      // End of scene - show choices if available
      if (scene.PATHS && scene.PATHS.length > 0) {
        log('End of scene script, showing choices', scene.PATHS);
        setGameState(prev => ({
          ...prev,
          choices: scene.PATHS,
          showChoices: true,
          isTextComplete: true,
        }));
        return;
      } else {
        // No choices available - game complete
        log('No more script entries and no choices - game complete');
        setGameState(prev => ({
          ...prev,
          isGameComplete: true,
        }));
        return;
      }
    }

    // Advance to next script entry
    setGameState(prev => ({
      ...prev,
      currentScriptIndex: prev.currentScriptIndex + 1,
      isTextComplete: false,
    }));
  }, [gameState, getCurrentScene, getCurrentScriptEntry, log]);

  const handleChoice = useCallback((choiceIndex) => {
    const choices = gameState.choices;
    log('handleChoice called', { choiceIndex, choicesLength: choices?.length, choices });
    
    if (!choices || choiceIndex >= choices.length) {
      log('Invalid choice selection', { choiceIndex, availableChoices: choices }, 'error');
      return;
    }

    const selectedChoice = choices[choiceIndex];
    
    log('Player chose option', {
      choiceIndex,
      choice: selectedChoice.CHOICE,
      target: selectedChoice.TARGET,
      selectedChoice
    });

    // Hide choices
    setGameState(prev => ({
      ...prev,
      showChoices: false,
      choices: null,
    }));

    // Navigate to target scene
    setTimeout(() => {
      if (!selectedChoice.TARGET) {
        log('Choice has no target - game complete');
        setGameState(prev => ({
          ...prev,
          isGameComplete: true,
        }));
        return;
      }

      if (!gameState.scenesById[selectedChoice.TARGET]) {
        log('Target scene not found', { target: selectedChoice.TARGET }, 'error');
        setGameState(prev => ({
          ...prev,
          isGameComplete: true,
        }));
        return;
      }

      log('Navigating to target scene', { target: selectedChoice.TARGET });
      setGameState(prev => ({
        ...prev,
        currentSceneId: selectedChoice.TARGET,
        currentScriptIndex: 0,
        isTextComplete: false,
      }));
    }, 300);
  }, [gameState.choices, gameState.scenesById, log]);

  const handleTextComplete = useCallback(() => {
    log('Text animation completed');
    setGameState(prev => ({
      ...prev,
      isTextComplete: true,
    }));
  }, [log]);

  const handleAdvance = useCallback(() => {
    if (!gameState.isTextComplete) return;
    
    if (gameState.showChoices) {
      log('Choices are showing, cannot advance');
      return;
    }

    advanceScript();
  }, [gameState.isTextComplete, gameState.showChoices, advanceScript, log]);

  // Auto-play logic
  useEffect(() => {
    if (settings.autoPlay && gameState.isTextComplete && !gameState.showChoices && !gameState.isGameComplete) {
      const timer = setTimeout(() => {
        handleAdvance();
      }, 3000);
      
      return () => clearTimeout(timer);
    }
  }, [settings.autoPlay, gameState.isTextComplete, gameState.showChoices, gameState.isGameComplete, handleAdvance]);

  // Loading state
  if (gameState.isLoading) {
    return (
      <div className="min-h-screen bg-gradient-to-br from-purple-900 via-blue-900 to-indigo-900 flex items-center justify-center">
        <div className="text-white text-2xl animate-pulse">
          🎮 Loading Visual Novel...
        </div>
      </div>
    );
  }

  // Game complete state
  if (gameState.isGameComplete) {
    return (
      <div className="min-h-screen bg-gradient-to-br from-purple-900 via-blue-900 to-indigo-900 flex items-center justify-center">
        <div className="text-center text-white">
          <div className="text-4xl mb-4">🎉</div>
          <div className="text-2xl mb-2">Story Complete!</div>
          <div className="text-lg">Thank you for playing</div>
          <button 
            onClick={() => window.location.reload()} 
            className="mt-4 px-6 py-2 bg-blue-600 text-white rounded hover:bg-blue-700 transition-colors"
          >
            Play Again
          </button>
        </div>
      </div>
    );
  }

  const scene = getCurrentScene();
  const currentEntry = getCurrentScriptEntry();
  const currentMusic = getCurrentMusic();

  if (!scene || !currentEntry) {
    return (
      <div className="min-h-screen bg-gradient-to-br from-purple-900 via-blue-900 to-indigo-900 flex items-center justify-center">
        <div className="text-white text-xl">
          ❌ Error: No scene or script entry available
        </div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-purple-900 via-blue-900 to-indigo-900 relative overflow-hidden">
      {/* Audio Manager */}
      <AudioManager
        currentMusic={currentMusic}
        volume={settings.isMuted ? 0 : settings.musicVolume}
      />

      {/* Background */}
      <Background
        imagePath={scene.SCENE.BACKGROUND_IMAGE}
        location={scene.SCENE.LOCATION}
      />

      {/* Character Display */}
      <CharacterDisplay
        character={currentEntry.CHARACTER}
        expression={currentEntry.EXPRESSION}
        characters={scene.SCENE.CHARACTERS}
      />

      {/* Text Box */}
      <TextBox
        character={currentEntry.CHARACTER}
        dialogue={currentEntry.LINE}
        onTextComplete={handleTextComplete}
        onAdvance={handleAdvance}
        canAdvance={gameState.isTextComplete && !gameState.showChoices}
        textSpeed={settings.textSpeed}
      />

      {/* Choice Menu */}
      {gameState.showChoices && gameState.choices && (
        <ChoiceMenu
          choices={gameState.choices}
          onChoice={handleChoice}
        />
      )}

      {/* Settings Panel */}
      <div className="absolute top-4 right-4 z-30 flex space-x-2">
        <button
          onClick={() => setSettings(prev => ({ ...prev, isMuted: !prev.isMuted }))}
          className="p-2 bg-black bg-opacity-50 text-white rounded hover:bg-opacity-70 transition-opacity"
          title={settings.isMuted ? "Unmute" : "Mute"}
        >
          {settings.isMuted ? <FaVolumeMute /> : <FaVolumeUp />}
        </button>
        
        <button
          onClick={() => setDebugMode(prev => !prev)}
          className="p-2 bg-black bg-opacity-50 text-white rounded hover:bg-opacity-70 transition-opacity"
          title="Toggle Debug Mode"
        >
          <FaCog />
        </button>
      </div>

      {/* Debug Info */}
      {debugMode && (
        <div className="absolute top-4 left-4 z-30 bg-black bg-opacity-75 text-white p-3 rounded text-sm max-w-md">
          <div><strong>Current Scene:</strong> {gameState.currentSceneId}</div>
          <div><strong>Script Index:</strong> {gameState.currentScriptIndex}/{scene.SCRIPT.length - 1}</div>
          <div><strong>Character:</strong> {currentEntry.CHARACTER}</div>
          <div><strong>Mood:</strong> {scene.SCENE.MOOD}</div>
          <div><strong>Music:</strong> {currentMusic}</div>
          <div><strong>Music Path:</strong> /Music/{currentMusic}</div>
          <div><strong>Volume:</strong> {settings.isMuted ? 'MUTED' : settings.musicVolume}</div>
          <div><strong>Location:</strong> {scene.SCENE.LOCATION}</div>
          <div><strong>Choices Available:</strong> {scene.PATHS?.length || 0}</div>
        </div>
      )}
    </div>
  );
};

export default VNEngineNew;