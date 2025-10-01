#!/usr/bin/env python3
"""
Test script to verify the core functionality without requiring API keys
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from core.parser import PlotPointParser, DatabaseParser
from core.asset_generator import AssetGenerator

def test_parsing():
    print("=== Testing Plot Point Graph Parser ===")
    
    # Test plot point parsing
    plot_parser = PlotPointParser()
    try:
        plot_graph = plot_parser.parse_plot_point_graph('Plotpoint_graph')
        print(f"✓ Successfully parsed {len(plot_graph)} plot points")
        for node_id, node in plot_graph.items():
            print(f"  - {node_id}: {node.get('location', 'unknown location')}")
        print()
    except Exception as e:
        print(f"✗ Error parsing plot graph: {e}")
        return False
    
    # Test database parsing
    print("=== Testing Database Parser ===")
    db_parser = DatabaseParser()
    try:
        database = db_parser.parse_database('Database')
        print(f"✓ Successfully parsed database")
        print(f"  - Characters: {len(database.get('characters', {}))}")
        print(f"  - Locations: {len(database.get('locations', {}))}")
        print(f"  - Backgrounds: {len(database.get('backgrounds', []))}")
        print(f"  - Story flags: {len(database.get('story_flags', {}))}")
        print()
    except Exception as e:
        print(f"✗ Error parsing database: {e}")
        return False
    
    # Test asset generation
    print("=== Testing Asset Generator ===")
    try:
        asset_gen = AssetGenerator()
        test_scene = {
            'location': 'kaelens_hab',
            'mood': 'rising_tension',
            'background': {
                'edit_prompt': 'Make it look stormy and dark'
            }
        }
        filename = asset_gen.generate_background(test_scene)
        print(f"✓ Generated test background: {filename}")
        print()
    except Exception as e:
        print(f"✗ Error generating assets: {e}")
        return False
    
    print("=== All Tests Passed! ===")
    print("The core system is working properly.")
    print("To run the full application, you'll need to:")
    print("1. Set up your Gemini API key in .env file")
    print("2. Run: python app.py")
    return True

if __name__ == "__main__":
    test_parsing()