# Plot point graph structure


# Director LLM output:
```json
{
  "id": "String (Unique node ID)",
  "content": {
    "scene_script": [
      {
        "character": "String",
        "line": "String",
        "expression": "String or null"
      }
    ],
    "scene_details": {
      "mood": "String",
      "location": "String",
      "characters_present": [ "String (Character ID)", "..." ],
      "background": {
        "base_image": "String",
        "edit_prompt": "String or null"
      }
    }
  },
  "paths": [
    {
      "choice_text": "String (e.g., 'Go left', or 'Continue...')",
      "target_node": "String (ID of the destination node)"
    }
  ]
}
```

# Simplified Markup


```c

STORY_TITLE: [Title of the Visual Novel]
START_NODE: [ID of the first node]

---

NODE_ID: [Unique ID for this node]
::SCENE::
LOCATION: [Name of the scene's location]
MOOD: [Mood of the scene]
CHARACTERS: [Comma-separated list of character IDs present]
BACKGROUND_IMAGE: [Filename of the base background image]
BACKGROUND_EDIT: [Instruction for image model, e.g., "Make it nighttime", or null]

::SCRIPT::


  LINE: [The line of dialogue or narration]
  EXPRESSION: [Sprite expression, e.g., happy, sad, or null]
# (Add more script items for more dialogue/narration)

::PATHS::
- CHOICE: "[Text displayed to the player for this choice]"
  TARGET: [Node ID to go to if this choice is selected]
# (Add more path items for multiple choices, or just one for a linear path)

---

NODE_ID: [ID for the next node]
# ( ... content for the next node follows the same structure ... )
```

# Author defined plot point graph

```c


---

NODE_ID: [Unique ID for this node, e.g., "start_scene"]
LOCATION: [The setting for the scene, e.g., "Old Town Square"]
CHARACTERS: [Characters speaking or "Narrator"]
DESCRIPTION: """
[Enter your descriptive text or dialogue here. This block can span multiple lines. For example: The town square is bustling with activity. A merchant calls out to you from a nearby stall, while a guard eyes you suspiciously from the gate.]
"""

::CHOICES::  //optional not for all 
- TEXT: "[The first choice for the player, e.g., 'Approach the merchant.']"
  TARGET: [The NODE_ID to go to next, e.g., "merchant_talk"]
  FLAG_CHECK: [A condition to show this choice, e.g., "gold > 10", or null]
  FLAG_SET: [A state change to apply, e.g., "approached_merchant = true", or null]

- TEXT: "[The second choice for the player, e.g., 'Walk towards the gate.']"
  TARGET: [The NODE_ID to go to next, e.g., "gate_scene"]
  FLAG_CHECK: [A condition, e.g., "has_pass == true", or null]
  FLAG_SET: [A state change, e.g., null]
  
---
```

# Database format

```c
::EXPRESSIONS::
- Happy
- Angry
- Sad
- Afraid
- Surprised

::MOODS::
- calm
- rising_tension
- peak_action
- humorous
- romantic
- dread

::STORY_FLAGS::
# FORMAT: flag_name: initial_value
[flag_name_1]: [initial_value]
[flag_name_2]: [initial_value]

::CHARACTERS::
- ID: [unique_character_id]
  DESCRIPTION: "[A brief text description of the character.]"
- ID: [another_unique_character_id]
  DESCRIPTION: "[Description for the second character.]"

::LOCATIONS::
- ID: [unique_location_id]
  DESCRIPTION: "[A brief text description of what this location is like.]"
- ID: [another_unique_location_id]
  DESCRIPTION: "[Description for the second location.]"

::BACKGROUNDS::
# FORMAT: A list of Location, Descriptor, and Image links.
- LOCATION: [location_id_from_above]
  DESCRIPTOR: [e.g., "Day", "Evening", "Night", "Stormy"]
  IMAGE: "[path/to/background_image.png]"
- LOCATION: [location_id_from_above]
  DESCRIPTOR: [e.g., "Ruined", "Winter"]
  IMAGE: "[path/to/another_background.png]"
```
