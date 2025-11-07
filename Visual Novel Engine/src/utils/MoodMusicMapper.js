/**
 * Mood to Music Mapping Utility
 * Maps scene moods to appropriate background music files
 */

export const MoodMusicMapper = {
  // Default mood to music mappings
  moodMusicMap: {
    'Analytical': 'ChillLofiR.mp3',
    'Contemplative': 'ChillLofiR.mp3',
    'Dramatic': 'ChillLofiR.mp3',
    'Exciting': 'ChillLofiR.mp3',
    'Focused': 'ChillLofiR.mp3',
    'Hopeful': 'ChillLofiR.mp3',
    'Mysterious': 'ChillLofiR.mp3',
    'Relieved': 'ChillLofiR.mp3',
    'Tense': 'ChillLofiR.mp3',
    'Urgent': 'ChillLofiR.mp3',
    // Additional common moods
    'Curious': 'ChillLofiR.mp3',
    'Playful': 'ChillLofiR.mp3',
    'Reflective': 'ChillLofiR.mp3',
    'Calm': 'ChillLofiR.mp3',
    'Excited': 'ChillLofiR.mp3',
    'Sad': 'ChillLofiR.mp3',
    'Happy': 'ChillLofiR.mp3',
    'Serious': 'ChillLofiR.mp3',
    'Romantic': 'ChillLofiR.mp3',
    'Action': 'ChillLofiR.mp3'
  },

  /**
   * Get music file for a given mood
   * @param {string} mood - The scene mood
   * @returns {string} - The music file path
   */
  getMusicForMood(mood) {
    if (!mood) {
      console.warn('⚠️ No mood specified, using default music');
      return 'ChillLofiR.mp3';
    }

    const music = this.moodMusicMap[mood];
    if (!music) {
      console.warn(`⚠️ No music mapping found for mood '${mood}', using default`);
      return 'ChillLofiR.mp3';
    }

    console.log(`🎵 Mood '${mood}' mapped to music: ${music}`);
    return music;
  },

  /**
   * Update the music mapping for a specific mood
   * @param {string} mood - The mood to update
   * @param {string} musicFile - The music file to map to
   */
  setMoodMusic(mood, musicFile) {
    this.moodMusicMap[mood] = musicFile;
    console.log(`🔧 Updated mood mapping: ${mood} → ${musicFile}`);
  },

  /**
   * Get all available moods
   * @returns {string[]} - Array of available mood keys
   */
  getAvailableMoods() {
    return Object.keys(this.moodMusicMap);
  },

  /**
   * Load custom mood mapping from a configuration object
   * @param {Object} customMapping - Custom mood to music mapping
   */
  loadCustomMapping(customMapping) {
    if (typeof customMapping === 'object' && customMapping !== null) {
      this.moodMusicMap = { ...this.moodMusicMap, ...customMapping };
      console.log('🔧 Loaded custom mood mapping', customMapping);
    } else {
      console.warn('⚠️ Invalid custom mapping provided, keeping defaults');
    }
  }
};

export default MoodMusicMapper;