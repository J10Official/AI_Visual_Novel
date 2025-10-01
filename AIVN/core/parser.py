"""
Plot Point Graph and Database Parser
Handles parsing of the custom markup format for story structure and game data
"""

import re
from typing import Dict, List, Any, Optional
import yaml

class PlotPointParser:
    def __init__(self):
        self.nodes = {}
        self.start_node = None
    
    def parse_plot_point_graph(self, file_path: str) -> Dict[str, Any]:
        """Parse the plot point graph file"""
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Split content by node separators
        node_sections = re.split(r'^---\s*$', content, flags=re.MULTILINE)
        
        for section in node_sections:
            section = section.strip()
            if not section:
                continue
                
            node = self._parse_node_section(section)
            if node:
                self.nodes[node['id']] = node
                
        return self.nodes
    
    def _parse_node_section(self, section: str) -> Optional[Dict[str, Any]]:
        """Parse a single node section"""
        lines = section.split('\n')
        node = {}
        
        current_block = None
        description_lines = []
        
        for line in lines:
            line = line.strip()
            if not line:
                continue
                
            # Parse NODE_ID
            if line.startswith('NODE_ID:'):
                node['id'] = line.split(':', 1)[1].strip()
            
            # Parse LOCATION
            elif line.startswith('LOCATION:'):
                node['location'] = line.split(':', 1)[1].strip()
            
            # Parse CHARACTERS
            elif line.startswith('CHARACTERS:'):
                characters = line.split(':', 1)[1].strip()
                node['characters'] = [c.strip() for c in characters.split(',')]
            
            # Parse DESCRIPTION block
            elif line.startswith('DESCRIPTION:'):
                current_block = 'description'
                desc_start = line.find('"""')
                if desc_start != -1:
                    desc_content = line[desc_start + 3:]
                    if desc_content.endswith('"""'):
                        node['description'] = desc_content[:-3].strip()
                        current_block = None
                    else:
                        description_lines = [desc_content] if desc_content else []
            
            # Parse CHOICES block
            elif line.startswith('::CHOICES::'):
                current_block = 'choices'
            
            # Handle multi-line description
            elif current_block == 'description':
                if line.endswith('"""'):
                    description_lines.append(line[:-3])
                    node['description'] = '\n'.join(description_lines).strip()
                    current_block = None
                    description_lines = []
                else:
                    description_lines.append(line)
            
            # Handle choices
            elif current_block == 'choices' and line.startswith('- TEXT:'):
                # Parse all choices in this section
                remaining_lines = lines[lines.index(line):]
                choices = self._parse_choice_block(remaining_lines, 0)
                if choices:
                    node['choices'] = choices
                break  # We've processed all choices
            
        return node if 'id' in node else None
    
    def _parse_choice_block(self, lines: List[str], start_idx: int) -> List[Dict[str, Any]]:
        """Parse all choice blocks in the choices section"""
        choices = []
        current_choice = None
        
        for i, line in enumerate(lines):
            line = line.strip()
            
            if line.startswith('- TEXT:'):
                # Save previous choice if complete
                if current_choice and 'text' in current_choice and 'target' in current_choice:
                    choices.append(current_choice)
                
                # Start new choice
                current_choice = {}
                current_choice['text'] = line.split(':', 1)[1].strip().strip('"')
            
            elif current_choice is not None:
                if line.startswith('TARGET:'):
                    current_choice['target'] = line.split(':', 1)[1].strip()
                elif line.startswith('FLAG_CHECK:'):
                    flag_check = line.split(':', 1)[1].strip()
                    current_choice['flag_check'] = None if flag_check.lower() == 'null' else flag_check
                elif line.startswith('FLAG_SET:'):
                    flag_set = line.split(':', 1)[1].strip()
                    current_choice['flag_set'] = None if flag_set.lower() == 'null' else flag_set
        
        # Add the last choice
        if current_choice and 'text' in current_choice and 'target' in current_choice:
            choices.append(current_choice)
            
        return choices

class DatabaseParser:
    def __init__(self):
        self.database = {
            'expressions': [],
            'moods': [],
            'story_flags': {},
            'characters': {},
            'locations': {},
            'backgrounds': []
        }
    
    def parse_database(self, file_path: str) -> Dict[str, Any]:
        """Parse the database file"""
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        current_section = None
        current_item = {}
        
        for line in content.split('\n'):
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            
            # Section headers
            if line.startswith('::') and line.endswith('::'):
                current_section = line[2:-2].lower()
                continue
            
            # Handle different sections
            if current_section == 'expressions':
                if line.startswith('- '):
                    self.database['expressions'].append(line[2:])
            
            elif current_section == 'moods':
                if line.startswith('- '):
                    self.database['moods'].append(line[2:])
            
            elif current_section == 'story_flags':
                if ':' in line:
                    key, value = line.split(':', 1)
                    key = key.strip()
                    value = value.strip().lower()
                    self.database['story_flags'][key] = value == 'true'
            
            elif current_section == 'characters':
                if line.startswith('- ID:'):
                    if current_item and 'id' in current_item:
                        self.database['characters'][current_item['id']] = current_item
                    current_item = {'id': line.split(':', 1)[1].strip()}
                elif line.startswith('DESCRIPTION:'):
                    desc = line.split(':', 1)[1].strip().strip('"')
                    if current_item:
                        current_item['description'] = desc
            
            elif current_section == 'locations':
                if line.startswith('- ID:'):
                    if current_item and 'id' in current_item:
                        self.database['locations'][current_item['id']] = current_item
                    current_item = {'id': line.split(':', 1)[1].strip()}
                elif line.startswith('DESCRIPTION:'):
                    desc = line.split(':', 1)[1].strip().strip('"')
                    if current_item:
                        current_item['description'] = desc
            
            elif current_section == 'backgrounds':
                if line.startswith('- LOCATION:'):
                    if current_item and 'location' in current_item:
                        self.database['backgrounds'].append(current_item)
                    current_item = {'location': line.split(':', 1)[1].strip()}
                elif line.startswith('DESCRIPTOR:'):
                    desc = line.split(':', 1)[1].strip().strip('"')
                    if current_item:
                        current_item['descriptor'] = desc
                elif line.startswith('IMAGE:'):
                    image = line.split(':', 1)[1].strip().strip('"')
                    if current_item:
                        current_item['image'] = image
        
        # Add last item if exists
        if current_section == 'characters' and current_item and 'id' in current_item:
            self.database['characters'][current_item['id']] = current_item
        elif current_section == 'locations' and current_item and 'id' in current_item:
            self.database['locations'][current_item['id']] = current_item
        elif current_section == 'backgrounds' and current_item and 'location' in current_item:
            self.database['backgrounds'].append(current_item)
        
        return self.database