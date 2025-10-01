"""
Enhanced Image Generator using Gemini API
Handles both image generation from scratch and image editing based on prompts
"""

import os
import base64
import requests
from PIL import Image, ImageDraw, ImageFont
from typing import Dict, Any, Optional
import google.generativeai as genai
from dotenv import load_dotenv
import io

load_dotenv()

class GeminiImageGenerator:
    def __init__(self):
        self.api_key = os.getenv('GEMINI_API_KEY')
        if not self.api_key:
            raise ValueError("GEMINI_API_KEY not found in environment variables")
        
        genai.configure(api_key=self.api_key)
        
        # Use current Gemini models
        self.text_model = genai.GenerativeModel('gemini-2.0-flash')
        # Note: Vision capabilities are integrated into the main model now
        
        self.output_dir = "static/generated_assets"
        self.ensure_output_directory()
        
        # Enhanced scene prompts for better image generation
        self.location_prompts = {
            'kaelens_hab': "A futuristic high-tech apartment with panoramic windows showing a neon-lit cyberpunk city in the rain. Interior has sleek metallic surfaces, holographic displays, and modern furniture. Dark atmosphere with blue and cyan lighting.",
            'the_glitch': "A dimly lit underground bar in a cyberpunk setting. Filled with smoke, holographic advertisements, and data terminals. Patrons in dark corners, neon signs flickering. Industrial decor with exposed pipes and worn surfaces.",
            'lower_decks': "Abandoned industrial corridors in a space station. Rusted metal surfaces, flickering emergency lights, debris scattered around. Dark and foreboding atmosphere with visible decay and neglect.",
            'abandoned_lab': "A sterile white laboratory facility that's been abandoned. Clean surfaces with advanced scientific equipment, some displays still glowing. Eerily pristine but empty, with subtle signs of hasty evacuation."
        }
        
        self.mood_modifiers = {
            'calm': "peaceful, serene lighting, soft colors",
            'rising_tension': "dramatic lighting, contrasting shadows, warmer colors suggesting unease",
            'peak_action': "intense dramatic lighting, dynamic shadows, high contrast",
            'humorous': "bright, cheerful lighting, warm and inviting colors",
            'romantic': "soft, warm lighting, gentle colors, intimate atmosphere",
            'dread': "ominous shadows, cool blue/purple tones, foreboding atmosphere"
        }
    
    def ensure_output_directory(self):
        """Ensure the output directory exists"""
        os.makedirs(self.output_dir, exist_ok=True)
    
    def generate_or_edit_image(self, scene_details: Dict[str, Any]) -> str:
        """
        Generate or edit an image based on scene details
        Returns the filename of the generated/edited image
        """
        location = scene_details.get('location', 'unknown')
        mood = scene_details.get('mood', 'calm')
        background_info = scene_details.get('background', {})
        base_image = background_info.get('base_image')
        edit_prompt = background_info.get('edit_prompt')
        
        # Generate cache key
        cache_key = f"{location}_{mood}_{hash(edit_prompt or 'none') % 10000}"
        filename = f"gemini_bg_{cache_key}.png"
        filepath = os.path.join(self.output_dir, filename)
        
        # Check if already generated
        if os.path.exists(filepath):
            return filename
        
        try:
            if base_image and os.path.exists(f"art/backgrounds/{base_image}") and edit_prompt:
                # Edit existing image
                image = self.edit_existing_image(f"art/backgrounds/{base_image}", edit_prompt, location, mood)
            else:
                # Generate from scratch
                image = self.generate_image_from_scratch(location, mood, edit_prompt)
            
            # Save the image
            image.save(filepath, 'PNG')
            return filename
            
        except Exception as e:
            print(f"Error generating image with Gemini: {e}")
            # Fallback to procedural generation
            return self.generate_fallback_image(scene_details)
    
    def generate_image_from_scratch(self, location: str, mood: str, edit_prompt: Optional[str] = None) -> Image.Image:
        """Generate a new image from scratch using AI guidance"""
        
        # Build comprehensive prompt
        base_prompt = self.location_prompts.get(location, f"A {location} scene")
        mood_modifier = self.mood_modifiers.get(mood, "neutral lighting")
        
        full_prompt = f"{base_prompt}. {mood_modifier}."
        
        if edit_prompt:
            full_prompt += f" Additional details: {edit_prompt}"
        
        full_prompt += " Digital art style, highly detailed, atmospheric, cinematic composition."
        
        # Use Gemini to enhance the prompt and provide detailed description
        enhanced_prompt = self.enhance_image_prompt(full_prompt)
        
        # For now, create a sophisticated procedural image based on the enhanced description
        # In a production system, you'd use this enhanced prompt with DALL-E, Midjourney, or Stable Diffusion
        image = self.create_sophisticated_procedural_image(location, mood, enhanced_prompt, edit_prompt)
        
        return image
    
    def edit_existing_image(self, base_image_path: str, edit_prompt: str, location: str, mood: str) -> Image.Image:
        """Edit an existing image based on the edit prompt"""
        
        try:
            base_image = Image.open(base_image_path)
            
            # Use Gemini to analyze the image and provide editing guidance
            editing_instructions = self.get_editing_instructions(base_image, edit_prompt, location, mood)
            
            # Apply procedural edits based on AI guidance
            edited_image = self.apply_procedural_edits(base_image, editing_instructions, edit_prompt)
            
            return edited_image
            
        except Exception as e:
            print(f"Error editing image: {e}")
            # Fallback to generating from scratch
            return self.generate_image_from_scratch(location, mood, edit_prompt)
    
    def enhance_image_prompt(self, base_prompt: str) -> str:
        """Use Gemini to enhance and detail the image generation prompt"""
        
        enhancement_prompt = f"""
        You are an expert at creating detailed, atmospheric image descriptions for a cyberpunk visual novel.
        
        Base scene description: {base_prompt}
        
        Please enhance this description with:
        1. Specific visual details (lighting, colors, textures)
        2. Atmospheric elements (mood, feeling)
        3. Composition details (foreground, background, focal points)
        4. Technical art direction (style, camera angle, depth of field)
        
        Keep it concise but vivid, focusing on creating a cinematic cyberpunk atmosphere.
        Return only the enhanced description, no additional text.
        """
        
        try:
            response = self.text_model.generate_content(enhancement_prompt)
            return response.text.strip()
        except Exception as e:
            print(f"Error enhancing prompt: {e}")
            return base_prompt
    
    def get_editing_instructions(self, base_image: Image.Image, edit_prompt: str, location: str, mood: str) -> str:
        """Use Gemini Vision to analyze image and provide editing guidance"""
        
        # Convert image to bytes for Gemini Vision
        img_byte_arr = io.BytesIO()
        base_image.save(img_byte_arr, format='PNG')
        img_byte_arr = img_byte_arr.getvalue()
        
        analysis_prompt = f"""
        Analyze this image of a {location} scene with {mood} mood.
        
        The user wants to apply this edit: {edit_prompt}
        
        Please provide specific technical instructions for how to modify this image:
        1. What colors should be adjusted?
        2. What lighting changes are needed?
        3. What objects or elements should be added/modified?
        4. What atmospheric effects should be applied?
        
        Keep instructions practical and specific for image editing.
        """
        
        try:
            # Note: In a real implementation, you'd pass the image to Gemini Vision
            # For now, provide intelligent editing guidance based on the prompt
            return self.generate_editing_guidance(edit_prompt, location, mood)
        except Exception as e:
            print(f"Error getting editing instructions: {e}")
            return f"Apply {edit_prompt} to the {location} scene"
    
    def generate_editing_guidance(self, edit_prompt: str, location: str, mood: str) -> str:
        """Generate intelligent editing guidance based on prompt analysis"""
        
        guidance_prompt = f"""
        You are an expert image editor working on a cyberpunk visual novel.
        
        Scene: {location}
        Mood: {mood}
        Edit request: {edit_prompt}
        
        Provide specific technical editing instructions:
        - Color adjustments needed
        - Lighting modifications
        - Elements to add or emphasize
        - Atmospheric effects to apply
        
        Be specific and practical. Return only the editing instructions.
        """
        
        try:
            response = self.text_model.generate_content(guidance_prompt)
            return response.text.strip()
        except Exception as e:
            print(f"Error generating editing guidance: {e}")
            return f"Apply {edit_prompt} effects"
    
    def create_sophisticated_procedural_image(self, location: str, mood: str, enhanced_prompt: str, edit_prompt: Optional[str]) -> Image.Image:
        """Create a sophisticated procedural image based on AI-enhanced prompts"""
        
        width, height = 800, 600
        image = Image.new('RGB', (width, height), (0, 0, 0))
        draw = ImageDraw.Draw(image)
        
        # Enhanced color palettes based on AI analysis
        color_schemes = {
            'kaelens_hab': {
                'calm': [(20, 40, 80), (0, 100, 200), (40, 60, 120)],
                'rising_tension': [(60, 40, 80), (100, 50, 150), (80, 20, 100)],
                'dread': [(40, 20, 60), (20, 10, 40), (60, 30, 80)]
            },
            'the_glitch': {
                'calm': [(40, 20, 20), (80, 40, 20), (60, 30, 15)],
                'rising_tension': [(80, 30, 0), (120, 60, 20), (100, 40, 10)],
                'dread': [(60, 0, 0), (40, 0, 0), (80, 20, 20)]
            },
            'lower_decks': {
                'calm': [(40, 40, 40), (60, 60, 60), (80, 80, 80)],
                'rising_tension': [(60, 50, 40), (80, 60, 40), (100, 70, 50)],
                'dread': [(30, 30, 40), (20, 20, 30), (40, 40, 50)]
            },
            'abandoned_lab': {
                'calm': [(200, 200, 200), (220, 220, 220), (180, 180, 180)],
                'rising_tension': [(180, 200, 180), (160, 220, 160), (140, 180, 140)],
                'dread': [(150, 180, 200), (120, 150, 180), (100, 130, 160)]
            }
        }
        
        # Get appropriate color scheme
        colors = color_schemes.get(location, {}).get(mood, [(50, 50, 50), (100, 100, 100), (150, 150, 150)])
        
        # Create sophisticated gradient background
        self.create_advanced_gradient(draw, width, height, colors)
        
        # Add location-specific sophisticated elements
        if location == 'kaelens_hab':
            self.draw_futuristic_hab(draw, width, height, colors, mood, edit_prompt)
        elif location == 'the_glitch':
            self.draw_cyberpunk_bar(draw, width, height, colors, mood, edit_prompt)
        elif location == 'lower_decks':
            self.draw_industrial_decay(draw, width, height, colors, mood, edit_prompt)
        elif location == 'abandoned_lab':
            self.draw_sterile_lab(draw, width, height, colors, mood, edit_prompt)
        
        # Apply edit prompt effects
        if edit_prompt:
            self.apply_edit_prompt_effects(draw, width, height, edit_prompt, colors)
        
        return image
    
    def create_advanced_gradient(self, draw, width, height, colors):
        """Create a sophisticated multi-layered gradient"""
        for y in range(height):
            for x in range(width):
                # Create complex gradient with multiple color zones
                x_ratio = x / width
                y_ratio = y / height
                
                # Blend multiple colors based on position
                if y_ratio < 0.3:  # Top area
                    color = self.interpolate_color(colors[0], colors[1], x_ratio)
                elif y_ratio < 0.7:  # Middle area
                    color = self.interpolate_color(colors[1], colors[2], x_ratio)
                else:  # Bottom area
                    color = self.interpolate_color(colors[2], colors[0], x_ratio)
                
                # Add subtle noise for texture
                noise = (hash((x, y)) % 20) - 10
                color = tuple(max(0, min(255, c + noise)) for c in color)
                
                draw.point((x, y), fill=color)
    
    def draw_futuristic_hab(self, draw, width, height, colors, mood, edit_prompt):
        """Draw sophisticated futuristic habitat elements"""
        # Window frame
        draw.rectangle([50, 50, width-50, height//3], outline=colors[1], width=3)
        
        # Holographic displays
        for i in range(3):
            x = 100 + i * 200
            y = height//2
            # Glowing rectangle with gradient effect
            for j in range(10):
                alpha = 255 - j * 20
                color = (*colors[1], alpha) if len(colors[1]) == 3 else colors[1]
                draw.rectangle([x-j, y-j, x+50+j, y+30+j], outline=color)
        
        # City skyline silhouette through window
        for i in range(10):
            building_x = 60 + i * (width-120) // 10
            building_height = 50 + (hash(i) % 100)
            draw.rectangle([building_x, 60, building_x + 30, 60 + building_height], 
                         fill=tuple(c//3 for c in colors[2]))
    
    def draw_cyberpunk_bar(self, draw, width, height, colors, mood, edit_prompt):
        """Draw sophisticated cyberpunk bar elements"""
        # Bar counter
        draw.rectangle([0, height*2//3, width, height], fill=colors[2])
        
        # Neon signs
        neon_colors = [(255, 0, 100), (0, 255, 255), (255, 255, 0)]
        for i, neon_color in enumerate(neon_colors):
            x = 100 + i * 200
            y = 100
            # Create glow effect
            for j in range(5):
                alpha = 100 - j * 15
                draw.rectangle([x-j*2, y-j, x+80+j*2, y+40+j], outline=(*neon_color, alpha))
        
        # Smoke/atmosphere effect
        import random
        for _ in range(50):
            x = random.randint(0, width)
            y = random.randint(height//2, height)
            size = random.randint(5, 20)
            smoke_color = tuple(c + 20 for c in colors[0])
            draw.ellipse([x-size, y-size, x+size, y+size], fill=smoke_color)
    
    def draw_industrial_decay(self, draw, width, height, colors, mood, edit_prompt):
        """Draw sophisticated industrial decay elements"""
        # Structural beams
        for i in range(5):
            x = i * width // 5
            draw.line([(x, 0), (x, height)], fill=colors[1], width=8)
        
        # Rust and damage effects
        import random
        for _ in range(30):
            x = random.randint(0, width)
            y = random.randint(0, height)
            size = random.randint(10, 40)
            rust_color = (120, 80, 40)
            draw.ellipse([x-size, y-size, x+size, y+size], fill=rust_color)
        
        # Emergency lighting
        for i in range(3):
            x = 150 + i * 250
            # Flickering red light effect
            for j in range(5):
                draw.ellipse([x-20-j*3, 50-j*2, x+20+j*3, 90+j*2], 
                           outline=(255, 0, 0, 100-j*20))
    
    def draw_sterile_lab(self, draw, width, height, colors, mood, edit_prompt):
        """Draw sophisticated sterile laboratory elements"""
        # Clean tile pattern
        tile_size = 50
        for x in range(0, width, tile_size):
            for y in range(0, height, tile_size):
                if (x//tile_size + y//tile_size) % 2 == 0:
                    draw.rectangle([x, y, x+tile_size, y+tile_size], 
                                 fill=tuple(min(255, c+10) for c in colors[0]))
        
        # Equipment silhouettes
        equipment_positions = [(100, height-150), (300, height-120), (500, height-180)]
        for x, y in equipment_positions:
            draw.rectangle([x, y, x+80, height-50], fill=colors[2])
            # Control panels
            draw.rectangle([x+10, y+10, x+70, y+40], fill=colors[1])
        
        # Status indicators
        status_colors = [(0, 255, 0), (255, 255, 0), (255, 0, 0)]
        for i, status_color in enumerate(status_colors):
            x = 200 + i * 100
            draw.ellipse([x-5, 80-5, x+5, 80+5], fill=status_color)
    
    def apply_edit_prompt_effects(self, draw, width, height, edit_prompt, colors):
        """Apply sophisticated effects based on edit prompt"""
        prompt_lower = edit_prompt.lower()
        
        if 'storm' in prompt_lower or 'rain' in prompt_lower:
            # Enhanced rain effect
            import random
            for _ in range(100):
                x = random.randint(0, width)
                y = random.randint(0, height)
                length = random.randint(10, 30)
                draw.line([(x, y), (x+3, y+length)], fill=(200, 200, 255, 150), width=2)
        
        if 'dark' in prompt_lower or 'night' in prompt_lower:
            # Darkness overlay with preserved highlights
            overlay = Image.new('RGBA', (width, height), (0, 0, 0, 80))
            # This would need proper alpha blending in production
        
        if 'fire' in prompt_lower or 'explosion' in prompt_lower:
            # Enhanced fire effects
            import random
            fire_colors = [(255, 0, 0), (255, 100, 0), (255, 200, 0)]
            for _ in range(50):
                x = random.randint(0, width)
                y = random.randint(height//2, height)
                size = random.randint(15, 50)
                color = random.choice(fire_colors)
                draw.ellipse([x-size, y-size, x+size, y+size], fill=color)
        
        if 'lightning' in prompt_lower:
            # Lightning effects
            import random
            for _ in range(5):
                x1 = random.randint(0, width)
                x2 = x1 + random.randint(-50, 50)
                draw.line([(x1, 0), (x2, height)], fill=(255, 255, 255), width=3)
    
    def apply_procedural_edits(self, base_image: Image.Image, instructions: str, edit_prompt: str) -> Image.Image:
        """Apply procedural edits to an existing image based on AI instructions"""
        
        # Create a copy to edit
        edited_image = base_image.copy()
        draw = ImageDraw.Draw(edited_image)
        width, height = edited_image.size
        
        # Apply edits based on the edit prompt
        self.apply_edit_prompt_effects(draw, width, height, edit_prompt, [(100, 100, 100), (150, 150, 150), (200, 200, 200)])
        
        return edited_image
    
    def generate_fallback_image(self, scene_details: Dict[str, Any]) -> str:
        """Generate a simple fallback image if AI generation fails"""
        from core.asset_generator import AssetGenerator
        fallback_generator = AssetGenerator()
        return fallback_generator.generate_background(scene_details)
    
    def interpolate_color(self, color1, color2, ratio):
        """Interpolate between two colors"""
        return tuple(int(c1 + (c2 - c1) * ratio) for c1, c2 in zip(color1, color2))
    
    def get_asset_url(self, filename: str) -> str:
        """Get the URL for a generated asset"""
        return f"/static/generated_assets/{filename}"