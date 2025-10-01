Parent notes: [[AI Visual Novel]]
Hashtags:

### 1\. Enforcing the Author's Narrative Outline

Instead of feeding the LLM a vague "outline" and hoping it follows, implement a **Plot Point Graph** system.

**Proposed Change:**

Your authoring tool won't be a single document but a graph (or a list) of mandatory "Plot Points." The LLM's job is not to decide the entire story, but to generate the **connective tissue** between these points.

**How It Works:**

1.  **Author defines the structure:**

      * `Plot Point 1`: Player arrives at the old mansion. Mood is `Eerie`.
      * `Plot Point 2`: Player finds a locked diary in the study. Mood is `Intriguing`.
      * `Plot Point 3`: The power suddenly goes out. Mood is `Tense`.
      * **`Choice Point A`**: Player hears a sound from the basement. The author flags this as a moment for player choice.

2.  **State-Aware Prompting:** The `Game State Manager` tracks which plot point was just completed. The prompt to the LLM becomes highly specific and constrained.

      * **Example Prompt:** "You are writing a scene for a horror visual novel. The player has just completed 'Plot Point 2: Found locked diary'. The next mandatory event is 'Plot Point 3: Power goes out'. Generate 3-5 lines of descriptive text and/or character inner monologue that builds suspense and bridges these two events. The scene should transition from an `Intriguing` mood to a `Tense` one. **Do not trigger the power outage yet.**"

**Why This Is Better:**

  * **Control:** This gives the author absolute control over the narrative spine. The story *will* hit the beats you design.
  * **Reliability:** It's a much simpler task for the LLM to write a short, constrained transition than an entire open-ended chapter, dramatically reducing the chance of it going off the rails.
  * **Cohesion:** You can explicitly dictate the mood and key elements for each segment, ensuring the generated content aligns with your vision.

