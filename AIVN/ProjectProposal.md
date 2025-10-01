

### **Generative Visual Novels: A Framework for Dynamic, Replayable Narrative Experiences**

### **1. Introduction & Motivation**

Visual novels and narrative-driven games have long been constrained by predefined scripts and limited branching paths. This static design fundamentally limits replayability, as subsequent playthroughs often yield diminishing returns in novelty. In contrast, sandbox games achieve high replay value through procedural generation and emergent gameplay. Our objective is to bridge this gap by developing a framework for dynamic visual novels that balances the narrative depth of authored stories with the variability of generative systems.

We propose a system where a human author defines the core narrative structure—the key events, character arcs, and critical choices—using a **Plot Point Graph**. A fine-tuned Director LLM is then tasked with generating the "connective tissue" of the story: the specific dialogue, descriptions, and scene directions that connect these author-defined points. This approach empowers the author to maintain high-level narrative control while offloading the generation of nuanced, choice-dependent variations to the AI.

By implementing this framework, we aim to create a visual novel that is not only immersive on the first playthrough but also offers a genuinely different experience on subsequent ones. This work explores a collaborative model where AI serves not as a replacement for human creativity, but as a powerful tool to augment it, enabling the creation of deeper, more personalized interactive narratives.

### **3. Proposed Methodology**
Our proposed system is a modular, multi-pipeline framework designed to generate dynamic and cohesive visual novel experiences. The architecture prioritizes authorial control, long-term narrative consistency, and low-latency performance by parallelizing asset generation and employing a sophisticated context management system. This section details the core components of our methodology, from the high-level narrative structure to the specific models and techniques used for text and visual generation.

#### **3.1 System Architecture and Workflow**
The system operates on an event-driven basis, initiating a generation sequence upon receiving a player choice or reaching a scripted story beat. As illustrated in the architectural diagram, the workflow proceeds as follows:

1.  **Context Aggregation:** The **Core State Manager** serves as the central hub for information. It receives the player's action, contextualizes it using the author's **Plot Point Graph**, and aggregates it with data from the **Tiered Memory System**. This produces a comprehensive, multi-part prompt detailing the current plot point, relevant past events, character states, and the specific generation task.
2.  **Narrative Generation:** The aggregated prompt is passed to the **Fine-Tuned Director LLM**, which generates a structured script for the upcoming scene.
3.  **Validation and Dispatch:** The generated script undergoes immediate validation for syntactic and schematic correctness. An **Error Correction Module** handles any failures through a re-prompting loop. A valid script is then passed to the **Scene/Asset Dispatcher**.
4.  **Parallel Asset Pipelines:** The dispatcher parses the script and issues simultaneous commands to three independent sub-systems:
    * **Audio Pipeline:** Cues music and sound effects from a pre-loaded library.
    * **Character Pipeline:** Selects pre-drawn, expression-specific sprites based on tags in the script.
    * **Background Pipeline:** Retrieves a base image from an asset library and, if required, sends it to the image generation module for modification. An asset cache is utilized to minimize redundant generation.
5.  **Scene Rendering:** The game engine's renderer composites all the retrieved and generated assets—dialogue text, audio, character sprites, and backgrounds—into the final visual novel interface, creating a cohesive player experience.

#### **3.2 Narrative Control: The Plot Point Graph**
To solve the critical challenge of balancing generative freedom with authorial intent, we introduce the **Plot Point Graph**. This is a declarative, author-created structure that serves as the narrative "skeleton" for the experience. It defines the mandatory story beats, key choice points, character introductions, and desired emotional tones for each chapter. The Director LLM is not tasked with inventing the plot, but rather with generating the "connective tissue"—the specific dialogue, descriptions, and minor events—that bridge these author-defined points. This hierarchical control structure ensures that the main storyline remains coherent and purposeful while allowing for significant moment-to-moment variation based on player choices, thereby enhancing replayability without sacrificing narrative integrity.

#### **3.3 Context Management: Tiered Memory System**

To address the problem of context window limitations in long-form narratives, we will implement a sophisticated **Tiered Memory System**. This system structures the game's memory to ensure the LLM always has access to relevant information without being overloaded by a complete, unabridged history.


#### **3.4 Narrative Generation: Hybrid Director LLM Pipeline**

To achieve both high creative quality and robust, error-free structured output, we will implement a two-stage hybrid pipeline for our Director LLM, optimized for local execution.

1.  **Stage 1: Creative Generation:** The primary creative task is handled by a fine-tuned, quantized LLM renowned for its instruction-following and storytelling capabilities (e.g., **LLaMA-3-8B** or **OpenHermes-7B**). This model will be fine-tuned on our augmented horror script dataset. Its sole task is to generate compelling narrative content in a semi-structured markup format (e.g., `::CHARACTER:: Jane`, `::MOOD:: Tense`), freeing it from the rigid constraints of perfect JSON syntax.
2.  **Stage 2: Structured Formatting:** The markup from the first stage is then passed to a lightweight, highly specialized utility model (a fine-tuned **Phi-3-Mini**). This model's only function is to parse the creative markup and convert it into the strict, validated JSON schema required by the game engine. This division of labor isolates creative generation from structural formatting, drastically reducing output brittleness and simplifying debugging.

#### **3.5 Visual Generation: Dynamic Asset Pipeline**

Our visual pipeline is designed for consistency, dynamism, and efficiency, leveraging a combination of pre-made assets and generative models.

1.  **Base Asset Foundation:** The system will use a library of high-quality, pre-drawn base assets for backgrounds and neutral-expression character sprites. This ensures a consistent and artist-defined core visual style.
2.  **Instruction-Based Image Editing:** For dynamic scene changes, we will use an **`img2img`** model, specifically **InstructPix2Pix**. The Director LLM's script will include explicit editing instructions (e.g., `"Apply this edit: make the sky look like a stormy evening",or "Add the new gifted clock to the room's wall"`). InstructPix2Pix will modify the base background image according to this instruction while preserving its core composition, allowing for a vast number of visual variations without creating new assets from scratch.
3.  **Character Consistency via LoRA Fine-Tuning:** To solve the critical problem of maintaining a consistent character appearance, we will fine-tune a Stable Diffusion model using **LoRA (Low-Rank Adaptation)**. For each main character, we will train a small, dedicated LoRA file on a curated set of their approved design. By activating this LoRA with a trigger word in the prompt, we can generate the character with high fidelity in any new pose or context, ensuring their visual identity remains stable throughout the game. Character expressions will be handled by the LLM selecting from a predefined list of sprites to maintain artistic control.








