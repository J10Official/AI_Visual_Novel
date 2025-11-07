/**
 * Test script for Markdown Parser
 * This script will parse the markdown story and compare it with the expected JSON format
 */

import MarkdownParser from '../src/utils/MarkdownParser.js';
import fs from 'fs';
import path from 'path';

// Function to run the parser test
async function testMarkdownParser() {
  console.log('🚀 Starting Markdown Parser Test');
  console.log('================================\n');

  try {
    // Read the markdown file
    const markdownPath = './public/story_script.md';
    console.log(`📖 Reading markdown file: ${markdownPath}`);
    
    const markdownContent = fs.readFileSync(markdownPath, 'utf8');
    console.log(`✅ Loaded ${markdownContent.split('\n').length} lines of markdown\n`);

    // Parse the markdown
    console.log('🔄 Parsing markdown to JSON...');
    const parser = new MarkdownParser();
    const parsedScenes = parser.parse(markdownContent);
    
    console.log(`✅ Parsed ${Object.keys(parsedScenes).length} scenes\n`);

    // Validate the parsed content
    console.log('🔍 Validating parsed content...');
    const validation = parser.validate(parsedScenes);
    
    if (validation.isValid) {
      console.log('✅ Validation passed - no errors found\n');
    } else {
      console.log('⚠️ Validation warnings:');
      validation.errors.forEach(error => console.log(`  - ${error}`));
      console.log('');
    }

    // Convert to VN Engine format
    console.log('🎮 Converting to VN Engine format...');
    const vnFormat = parser.toVNEngineFormat(parsedScenes);
    
    // Save the result
    const outputPath = './public/generated_story_script.json';
    fs.writeFileSync(outputPath, JSON.stringify(vnFormat, null, 2));
    console.log(`💾 Saved parsed JSON to: ${outputPath}\n`);

    // Display summary
    console.log('📊 Parsing Summary:');
    console.log('==================');
    
    for (const [sceneId, scene] of Object.entries(vnFormat)) {
      console.log(`\n🎬 Scene: ${sceneId}`);
      console.log(`   Location: ${scene.LOCATION}`);
      console.log(`   Mood: ${scene.MOOD}`);
      console.log(`   Characters: ${scene.CHARACTERS.join(', ')}`);
      console.log(`   Script entries: ${scene.SCRIPT.length}`);
      console.log(`   Choices: ${scene.PATHS.length}`);
    }

    // Compare with original format
    console.log('\n🔍 Format Comparison:');
    console.log('====================');
    
    // Load the original fixed_story_script.json for comparison
    try {
      const originalContent = fs.readFileSync('./public/fixed_story_script.json', 'utf8');
      const originalScenes = JSON.parse(originalContent);
      
      console.log(`Original script scenes: ${Object.keys(originalScenes).length}`);
      console.log(`Generated script scenes: ${Object.keys(vnFormat).length}`);
      
      // Check if structure matches
      const originalStructure = getSceneStructure(originalScenes);
      const generatedStructure = getSceneStructure(vnFormat);
      
      console.log('\n📋 Structure Comparison:');
      console.log(`Original has required fields: ${originalStructure.hasRequiredFields}`);
      console.log(`Generated has required fields: ${generatedStructure.hasRequiredFields}`);
      console.log(`Format compatibility: ${compareStructures(originalStructure, generatedStructure) ? '✅ Compatible' : '❌ Incompatible'}`);
      
    } catch (error) {
      console.log('⚠️ Could not load original script for comparison');
    }

    console.log('\n🎉 Parser test completed successfully!');
    console.log('\n💡 Next steps:');
    console.log('1. Review the generated JSON in public/generated_story_script.json');
    console.log('2. Test the generated script in your VN engine');
    console.log('3. Adjust the markdown format if needed');
    
    return {
      success: true,
      sceneCount: Object.keys(vnFormat).length,
      validationErrors: validation.errors,
      outputFile: outputPath
    };

  } catch (error) {
    console.error('❌ Parser test failed:', error);
    return {
      success: false,
      error: error.message
    };
  }
}

// Helper function to analyze scene structure
function getSceneStructure(scenes) {
  const sampleScene = Object.values(scenes)[0];
  if (!sampleScene) return { hasRequiredFields: false };
  
  const requiredFields = ['LOCATION', 'MOOD', 'CHARACTERS', 'SCRIPT', 'PATHS'];
  const hasRequiredFields = requiredFields.every(field => field in sampleScene);
  
  return {
    hasRequiredFields,
    fields: Object.keys(sampleScene),
    scriptStructure: sampleScene.SCRIPT?.[0] ? Object.keys(sampleScene.SCRIPT[0]) : [],
    pathStructure: sampleScene.PATHS?.[0] ? Object.keys(sampleScene.PATHS[0]) : []
  };
}

// Helper function to compare structures
function compareStructures(original, generated) {
  return original.hasRequiredFields && 
         generated.hasRequiredFields &&
         original.fields.length > 0 &&
         generated.fields.length > 0;
}

// Run the test if this file is executed directly
if (import.meta.url === `file://${process.argv[1]}`) {
  testMarkdownParser().then(result => {
    process.exit(result.success ? 0 : 1);
  });
}

export default testMarkdownParser;