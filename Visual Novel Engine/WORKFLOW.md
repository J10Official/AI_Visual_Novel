# Visual Novel Markdown-to-JSON Pipeline

## How It Works

This system transforms simple markdown stories into interactive visual novels. The finetuned model generates structured markdown files that define scenes, dialogue, and player choices. The parser automatically converts these into complex JSON configurations that power a React-based visual novel engine. The engine handles character sprite rendering, background music selection based on mood, facial expression animations, and branching narrative paths. This workflow enables rapid story development - especially useful for LLM-generated content where markdown is more reliable than JSON output.

The pipeline consists of markdown authoring, automatic parsing, and real-time browser playback with full visual novel features including character interactions, atmospheric backgrounds, mood-driven audio, and choice-based storytelling.

## Markdown Template Structure

```markdown
::SCENE::
LOCATION: [Scene name - becomes the scene ID]
MOOD: [Emotional tone - controls background music selection]
CHARACTERS: [Character1, Character2, Narrator - defines who appears]
BACKGROUND_IMAGE: [image.jpg - sets visual backdrop]
BACKGROUND_EDIT: [Visual modifications like lighting/props, or 'null']

::SCRIPT::
CHARACTER: [Speaker name - must match CHARACTERS list]
LINE: [What the character says or narrative description]
EXPRESSION: [happy/angry/sad/neutral/null - controls facial animation]

CHARACTER: [Next speaker]
LINE: [Their dialogue]
EXPRESSION: [Their expression]

::PATHS::
CHOICE: [Player choice text displayed as button]
TARGET: [target_scene_id - which scene this choice leads to]
STATE_CHANGE: [variable = value to track player decisions, or 'null']
CONDITION: [requirement for choice to appear, or 'null']

CHOICE: [Second choice option]
TARGET: [different_scene_id]
STATE_CHANGE: [null or state modification]
CONDITION: [null or visibility requirement]
```

## Key Files
- `story_script.md` - put your generated story here
- `test_parser_simple.js` - Converts markdown to JSON
- `generated_story_script.json` - Engine-ready output
- `src/utils/MarkdownParser.js` - Parser library