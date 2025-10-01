Parent notes:
Hashtags:


# Director LLM JSON

```json
{
  "story_title": "String",
  "start_node": "String (ID of the first node)",
  "nodes": {
    "node_id_1": { "Node Object" },
    "node_id_2": { "Node Object" },
    "...": "..."
  }
}
```


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
      "target_node": "String (ID of the destination node)",
      "state_changes": { 
        "key": "value" 
      },
      "condition": { 
        "key": "value" 
      }
    }
  ]
}
```



# JSON Description

### **Root Object**

```json
{
  "story_title": "String",
  "start_node": "String",  // ID of the first node to load.
  "nodes": {               // Contains all story nodes.
    "node_id_1": { "Node Object" },
    "...": "..."
  }
}
```

### **Node Object**

This is the core blueprint for a single node, with concise comments on the essential fields.

```json
{
  "id": "String",

  "content": { // All visual and narrative content for the scene.
    "scene_script": [ // An ordered sequence of dialogue and narration.
      {
        "character": "String", // Speaker. Use "Narrator" for descriptions.
        "line": "String",
        "expression": "String or null" // Character sprite expression (e.g., "Happy").
      }
    ],
    "scene_details": { // Atmospheric details for the scene.
      "mood": "String",
      "location": "String",
      "characters_present": [ "String" ], // Characters visible in the scene.
      "background": { // Scene background image.
        "base_image": "String",
        "edit_prompt": "String or null" // Optional img2img prompt; null uses base image as-is.
      }
    }
  },

  "paths": [ // Defines all exits. 1 path = linear, 2+ paths = choice.
    {
      "choice_text": "String", // Text for the player option.
      "target_node": "String",
      "state_changes": {       // State changes applied when this path is taken. Can be null.
        "key": "value"
      },
      "condition": {           // Required game state for this path to be available. Can be null.
        "key": "value"
      }
    }
  ]
}
```

# Markup

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
  STATE_CHANGE: [key = value, key += value, or null]
  CONDITION: [key = value, key != value, or null]
# (Add more path items for multiple choices, or just one for a linear path)

---

NODE_ID: [ID for the next node]
# ( ... content for the next node follows the same structure ... )
```


# Example


**Markup Input:**

```
STORY_TITLE: My Visual Novel
START_NODE: intro

---

NODE_ID: intro
::SCENE::
LOCATION: Classroom
MOOD: Tense
CHARACTERS: Alice, Bob
BACKGROUND_IMAGE: classroom.png
BACKGROUND_EDIT: "Evening lighting"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The classroom felt unusually quiet.
  EXPRESSION: null
- CHARACTER: Alice
  LINE: Did you hear that?
  EXPRESSION: worried

::PATHS::
- CHOICE: "Look around"
  TARGET: investigate
  STATE_CHANGE: suspicion = 1
  CONDITION: null
```

**JSON Output:**

```json
{
  "story_title": "My Visual Novel",
  "start_node": "intro",
  "nodes": {
    "intro": {
      "id": "intro",
      "content": {
        "scene_script": [
          {
            "character": "Narrator",
            "line": "The classroom felt unusually quiet.",
            "expression": null
          },
          {
            "character": "Alice",
            "line": "Did you hear that?",
            "expression": "worried"
          }
        ],
        "scene_details": {
          "mood": "Tense",
          "location": "Classroom",
          "characters_present": ["Alice", "Bob"],
          "background": {
            "base_image": "classroom.png",
            "edit_prompt": "Evening lighting"
          }
        }
      },
      "paths": [
        {
          "choice_text": "Look around",
          "target_node": "investigate",
          "state_changes": {
            "suspicion": 1
          },
          "condition": null
        }
      ]
    }
  }
}
```

# Database

Expressions={Happy, angry, sad, afraid, surprised}
Mood={calm, rising tension, peak action, humorous, romantic, dread}
location (description of location)
background (pngs of location (location, descriptor like in evening, image))
story_flags(has light etc.)

# Game state 

```json
{
  "current_location_id": "hospital_entrance",
  "player_name": "Maya",
  "story_flags": {
    "power_is_on": false,
    "knows_door_is_locked": true,
    "discovered_subject_zero": false,
    "has_basement_key": false,
    "has_fathers_locket": true
  },
  "seen_nodes": [
    "entry_hall",
    "main_door_check"
  ]
}
```


# Simplified JSON

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



