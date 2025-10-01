"""
Asset Generator for backgrounds and visual elements
Handles background generation and modification
"""

import os
from PIL import Image, ImageDraw, ImageFont
from typing import Dict, Any, Optional
import colorsys
import random

class AssetGenerator:
    def __init__(self):
        self.output_dir = "static/generated_assets"
        self.ensure_output_directory()
        
        # Color palettes for different moods and locations
        self.mood_palettes = {
            'calm': [(135, 206, 235), (144, 238, 144), (255, 250, 205)],  # Sky blue, light green, light yellow
            'rising_tension': [(255, 165, 0), (255, 69, 0), (139, 0, 0)],  # Orange, red-orange, dark red
            'peak_action': [(255, 0, 0), (128, 0, 0), (64, 0, 0)],  # Red variations
            'humorous': [(255, 192, 203), (255, 255, 0), (0, 255, 255)],  # Pink, yellow, cyan
            'romantic': [(255, 182, 193), (255, 105, 180), (186, 85, 211)],  # Light pink, hot pink, medium orchid
            'dread': [(25, 25, 112), (72, 61, 139), (106, 90, 205)]  # Midnight blue, dark slate blue, slate blue
        }
        
        self.location_themes = {
            'kaelens_hab': {'base_color': (20, 30, 50), 'accent': (0, 150, 255), 'style': 'tech'},
            'the_glitch': {'base_color': (40, 20, 20), 'accent': (255, 100, 0), 'style': 'bar'},
            'lower_decks': {'base_color': (30, 30, 30), 'accent': (100, 100, 100), 'style': 'industrial'},
            'abandoned_lab': {'base_color': (240, 240, 240), 'accent': (0, 255, 100), 'style': 'clinical'}
        }
    
    def ensure_output_directory(self):
        """Ensure the output directory exists"""
        os.makedirs(self.output_dir, exist_ok=True)
    
    def generate_background(self, scene_details: Dict[str, Any]) -> str:
        """Generate a background image based on scene details"""
        
        location = scene_details.get('location', 'unknown')
        mood = scene_details.get('mood', 'calm')
        edit_prompt = scene_details.get('background', {}).get('edit_prompt')
        
        # Create image
        width, height = 800, 600
        image = Image.new('RGB', (width, height), (0, 0, 0))
        draw = ImageDraw.Draw(image)
        
        # Get base theme
        theme = self.location_themes.get(location, {
            'base_color': (50, 50, 50),
            'accent': (100, 100, 100),
            'style': 'default'
        })
        
        # Generate base background
        if theme['style'] == 'tech':
            self._draw_tech_background(draw, width, height, theme, mood)
        elif theme['style'] == 'bar':
            self._draw_bar_background(draw, width, height, theme, mood)
        elif theme['style'] == 'industrial':
            self._draw_industrial_background(draw, width, height, theme, mood)
        elif theme['style'] == 'clinical':
            self._draw_clinical_background(draw, width, height, theme, mood)
        else:
            self._draw_default_background(draw, width, height, theme, mood)
        
        # Apply edit prompt modifications
        if edit_prompt:
            self._apply_edit_prompt(draw, width, height, edit_prompt)
        
        # Save the image
        filename = f"bg_{location}_{mood}_{hash(edit_prompt or 'none') % 10000}.png"
        filepath = os.path.join(self.output_dir, filename)
        image.save(filepath)
        
        return filename
    
    def _draw_tech_background(self, draw, width, height, theme, mood):
        """Draw a tech/futuristic background"""
        base_color = self._adjust_color_for_mood(theme['base_color'], mood)
        accent_color = self._adjust_color_for_mood(theme['accent'], mood)
        
        # Gradient background
        for y in range(height):
            ratio = y / height
            color = self._interpolate_color(base_color, (10, 10, 30), ratio)
            draw.line([(0, y), (width, y)], fill=color)
        
        # Tech grid pattern
        for x in range(0, width, 50):
            draw.line([(x, 0), (x, height)], fill=accent_color + (30,))
        for y in range(0, height, 50):
            draw.line([(0, y), (width, y)], fill=accent_color + (30,))
        
        # Neon window effect
        draw.rectangle([50, 50, width-50, 200], outline=accent_color, width=2)
        draw.rectangle([60, 60, width-60, 190], fill=base_color + (100,))
    
    def _draw_bar_background(self, draw, width, height, theme, mood):
        """Draw a bar/dive background"""
        base_color = self._adjust_color_for_mood(theme['base_color'], mood)
        accent_color = self._adjust_color_for_mood(theme['accent'], mood)
        
        # Dark gradient
        for y in range(height):
            ratio = y / height
            color = self._interpolate_color(base_color, (10, 5, 5), ratio)
            draw.line([(0, y), (width, y)], fill=color)
        
        # Bar lighting effects
        for i in range(3):
            x = 100 + i * 200
            draw.ellipse([x-20, 100-10, x+20, 100+10], fill=accent_color + (80,))
    
    def _draw_industrial_background(self, draw, width, height, theme, mood):
        """Draw an industrial/decay background"""
        base_color = self._adjust_color_for_mood(theme['base_color'], mood)
        accent_color = self._adjust_color_for_mood(theme['accent'], mood)
        
        # Gradient with industrial feel
        for y in range(height):
            ratio = y / height
            color = self._interpolate_color(base_color, (15, 15, 15), ratio)
            draw.line([(0, y), (width, y)], fill=color)
        
        # Pipe/structure lines
        for i in range(5):
            x = i * (width // 5)
            draw.line([(x, 0), (x, height)], fill=accent_color, width=3)
        
        # Rust/decay spots
        for _ in range(10):
            x = random.randint(0, width)
            y = random.randint(0, height)
            draw.ellipse([x-15, y-15, x+15, y+15], fill=(100, 50, 30, 50))
    
    def _draw_clinical_background(self, draw, width, height, theme, mood):
        """Draw a clinical/lab background"""
        base_color = self._adjust_color_for_mood(theme['base_color'], mood)
        accent_color = self._adjust_color_for_mood(theme['accent'], mood)
        
        # Clean white/gray gradient
        for y in range(height):
            ratio = y / height
            color = self._interpolate_color(base_color, (220, 220, 220), ratio)
            draw.line([(0, y), (width, y)], fill=color)
        
        # Lab equipment outlines
        draw.rectangle([50, height-150, 150, height-50], outline=accent_color, width=2)
        draw.rectangle([width-150, height-100, width-50, height-50], outline=accent_color, width=2)
        
        # Status lights
        for i in range(3):
            x = 200 + i * 50
            draw.ellipse([x-5, 50-5, x+5, 50+5], fill=accent_color)
    
    def _draw_default_background(self, draw, width, height, theme, mood):
        """Draw a default background"""
        base_color = self._adjust_color_for_mood(theme['base_color'], mood)
        
        # Simple gradient
        for y in range(height):
            ratio = y / height
            color = self._interpolate_color(base_color, (base_color[0]//2, base_color[1]//2, base_color[2]//2), ratio)
            draw.line([(0, y), (width, y)], fill=color)
    
    def _apply_edit_prompt(self, draw, width, height, edit_prompt: str):
        """Apply visual modifications based on edit prompt"""
        edit_prompt = edit_prompt.lower()
        
        if 'storm' in edit_prompt or 'rain' in edit_prompt:
            # Add rain effect
            for _ in range(50):
                x = random.randint(0, width)
                y = random.randint(0, height)
                draw.line([(x, y), (x+2, y+10)], fill=(200, 200, 255), width=1)
        
        if 'night' in edit_prompt or 'dark' in edit_prompt:
            # Add dark overlay
            overlay = Image.new('RGBA', (width, height), (0, 0, 0, 100))
            # This would need to be composited properly in a real implementation
        
        if 'fire' in edit_prompt or 'explosion' in edit_prompt:
            # Add fire/explosion effect
            for _ in range(20):
                x = random.randint(0, width)
                y = random.randint(height//2, height)
                size = random.randint(10, 30)
                draw.ellipse([x-size, y-size, x+size, y+size], fill=(255, random.randint(50, 200), 0, 150))
    
    def _adjust_color_for_mood(self, color, mood):
        """Adjust a color based on the scene mood"""
        if mood in self.mood_palettes:
            mood_color = random.choice(self.mood_palettes[mood])
            # Blend the base color with mood color
            return tuple(int((c + m) / 2) for c, m in zip(color, mood_color))
        return color
    
    def _interpolate_color(self, color1, color2, ratio):
        """Interpolate between two colors"""
        return tuple(int(c1 + (c2 - c1) * ratio) for c1, c2 in zip(color1, color2))
    
    def get_asset_url(self, filename: str) -> str:
        """Get the URL for a generated asset"""
        return f"/static/generated_assets/{filename}"