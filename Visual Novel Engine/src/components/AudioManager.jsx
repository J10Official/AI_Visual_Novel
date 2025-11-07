import React, { useEffect, useRef, useState } from 'react';

const AudioManager = ({ currentMusic, volume = 0.7, onError }) => {
  const audioRef = useRef(null);
  const [isLoaded, setIsLoaded] = useState(false);
  const [currentTrack, setCurrentTrack] = useState(null);
  const [userInteracted, setUserInteracted] = useState(false);
  const [audioError, setAudioError] = useState(null);
  const playPromiseRef = useRef(null);

  const log = (message, data = null, level = 'info') => {
    const timestamp = new Date().toLocaleTimeString();
    const prefix = `🎵 [${timestamp}] AudioManager:`;
    
    switch (level) {
      case 'error':
        console.error(`❌ ${prefix}`, message, data);
        break;
      case 'warn':
        console.warn(`⚠️ ${prefix}`, message, data);
        break;
      default:
        console.log(`ℹ️ ${prefix}`, message, data);
    }
  };

  useEffect(() => {
    if (!currentMusic) {
      log('No music specified');
      return;
    }

    // Don't reload the same track
    if (currentTrack === currentMusic && isLoaded) {
      log('Same track already playing', currentMusic);
      return;
    }

    const audio = audioRef.current;
    if (!audio) return;

    const loadMusic = async () => {
      try {
        log('Loading music', currentMusic);
        setAudioError(null);
        
        // Cancel any existing play promise
        if (playPromiseRef.current) {
          try {
            await playPromiseRef.current.catch(() => {
              // Ignore errors from cancelled promises
            });
          } catch (e) {
            // Ignore
          }
          playPromiseRef.current = null;
        }
        
        // Properly stop current music if playing
        if (!audio.paused) {
          audio.pause();
        }
        
        audio.currentTime = 0;
        
        // Set new source
        audio.src = `/Music/${currentMusic}`;
        audio.volume = volume;
        audio.loop = true;
        
        // Load the audio
        audio.load();
        
        // Try to play - handle autoplay restrictions
        try {
          const playPromise = audio.play();
          playPromiseRef.current = playPromise;
          
          if (playPromise !== undefined) {
            await playPromise;
            log('Music started playing', currentMusic);
            setIsLoaded(true);
            setCurrentTrack(currentMusic);
            playPromiseRef.current = null;
          }
        } catch (playError) {
          playPromiseRef.current = null;
          if (playError.name === 'NotAllowedError') {
            log('Autoplay blocked - waiting for user interaction', currentMusic, 'warn');
            setAudioError('autoplay-blocked');
            // Audio is loaded, just not playing yet
            setIsLoaded(true);
            setCurrentTrack(currentMusic);
          } else {
            throw playError;
          }
        }
        
      } catch (error) {
        log('Failed to load music', { music: currentMusic, error: error.message }, 'error');
        setAudioError(error.message);
        if (onError) onError(error);
        setIsLoaded(false);
      }
    };

    loadMusic();
  }, [currentMusic, onError, currentTrack, isLoaded, volume]);

  // Handle user interaction to enable audio
  useEffect(() => {
    const enableAudio = async () => {
      if (userInteracted || !audioRef.current || audioError !== 'autoplay-blocked') return;
      
      try {
        const audio = audioRef.current;
        if (audio.paused && audio.src) {
          log('User interacted - attempting to start audio');
          const playPromise = audio.play();
          playPromiseRef.current = playPromise;
          
          await playPromise;
          setUserInteracted(true);
          setAudioError(null);
          log('Audio enabled after user interaction');
          playPromiseRef.current = null;
        }
      } catch (error) {
        playPromiseRef.current = null;
        log('Still cannot play audio', error.message, 'warn');
      }
    };

    const handleInteraction = () => {
      if (!userInteracted) {
        setUserInteracted(true);
        enableAudio();
      }
    };

    // Listen for any user interaction
    document.addEventListener('click', handleInteraction);
    document.addEventListener('keydown', handleInteraction);
    document.addEventListener('touchstart', handleInteraction);

    return () => {
      document.removeEventListener('click', handleInteraction);
      document.removeEventListener('keydown', handleInteraction);
      document.removeEventListener('touchstart', handleInteraction);
    };
  }, [userInteracted, audioError]);

  // Update volume
  useEffect(() => {
    if (audioRef.current) {
      audioRef.current.volume = Math.max(0, Math.min(1, volume));
      log('Volume updated', volume);
    }
  }, [volume]);

  // Cleanup
  useEffect(() => {
    const audio = audioRef.current;
    return () => {
      if (audio) {
        // Cancel any pending play promise first
        if (playPromiseRef.current) {
          playPromiseRef.current.catch(() => {
            // Ignore errors from cancelled promises
          });
          playPromiseRef.current = null;
        }
        
        audio.pause();
        audio.currentTime = 0;
        log('Audio cleanup performed');
      }
    };
  }, []);

  return (
    <>
      <audio
        ref={audioRef}
        onError={(e) => {
          const errorMsg = e.target.error ? `Error ${e.target.error.code}: ${e.target.error.message}` : 'Unknown audio error';
          log('Audio element error', errorMsg, 'error');
          setAudioError(errorMsg);
          if (onError) onError(e.target.error);
        }}
        onLoadStart={() => log('Started loading audio')}
        onCanPlayThrough={() => log('Audio ready to play')}
        onPlay={() => log('Audio started playing')}
        onPause={() => log('Audio paused')}
        onEnded={() => log('Audio playback ended')}
        style={{ display: 'none' }}
      />
      
      {/* Audio status indicator */}
      {audioError === 'autoplay-blocked' && (
        <div className="fixed top-16 right-4 z-40 bg-yellow-600 text-white px-3 py-2 rounded text-sm">
          🔇 Click anywhere to enable audio
        </div>
      )}
      
      {audioError && 
       audioError !== 'autoplay-blocked' && 
       !audioError.includes('interrupted by a call to pause') && (
        <div className="fixed top-16 right-4 z-40 bg-red-600 text-white px-3 py-2 rounded text-sm">
          ❌ Audio error: {audioError}
        </div>
      )}
    </>
  );
};

export default AudioManager;