![](file:///C:/Users/Jatin/AppData/Local/Microsoft/Windows/Clipboard/HistoryData/%7BD36EB9D5-E44A-45A6-8104-D005F19EB124%7D/%7BFFBFA1DF-C394-4C26-973D-87F2A2D42A9A%7D/ResourceMap/%7B7E01BAF8-7048-4118-B83F-34E6B2542C85%7D)

The pipeline executes a dynamic visual novel scene through a structured, parallel-processing framework. The sequence is initiated by a player choice or a scripted event, which is contextualized by the author's predefined **Plot Point Graph**. A **Core State Manager** aggregates this input with the recent event history and character memory to construct a comprehensive prompt for the **Director LLM**. The LLM then generates a structured script that is immediately validated for syntactic correctness and passed to a central dispatcher. This dispatcher parses the script and issues commands simultaneously to three independent sub-systems: an audio pipeline to cue music and sound effects, a character pipeline to select and render the appropriate sprite, and a background pipeline to retrieve a cached or pre-drawn image or generate a new one. Finally, these disparate assets—dialogue, audio, character, and background—are integrated and rendered in the visual novel interface to deliver a cohesive and dynamic player experience. The core NLP related components are expanded below:


## **Proposed Methodologies and Systems**

### **1. Tiered Memory System and Context Management**

To address the critical research problem of maintaining long-term narrative coherence in extended interactions with LLMs, this project will implement a sophisticated **Tiered Memory System**. Standard LLM interactions suffer from context window limitations, leading to memory decay and logical inconsistencies over long sessions—a fatal flaw for a visual novel intended for hundreds of hours of gameplay. Our proposed system mitigates this by structuring memory into three distinct, dynamically managed tiers, ensuring that the context provided to the Director LLM is always concise, relevant, and computationally efficient.

---

#### **Implementation Strategy**

The three tiers—**Core State, Recent History, and Summarized Memory**—work in concert to provide a holistic view of the game state.

1.  **Core State:** A compact, persistent JSON object representing the "ground truth" of the game world. It tracks essential, slowly changing variables such as character relationships, critical inventory items, major plot flags (`power_is_out: true`), and character statuses (`Dr_Evans: deceased`). This tier is immutable except through direct game events and ensures the LLM adheres to fundamental narrative rules.

2.  **Recent History:** A rolling buffer containing the full, structured JSON outputs of the last 3-5 narrative beats. This provides the LLM with immediate, high-fidelity conversational context, allowing it to track the flow of recent dialogue and actions accurately.

3.  **Summarized Memory (Knowledge Graph Representation):** The most innovative component of our system is the move beyond simple text summarization. As events fall out of the `Recent History` buffer, they are not merely condensed into prose but are processed into a **Knowledge Graph**. This approach, inspired by advancements in structured information extraction and graph-based memory systems, represents a more robust solution to long-term memory.
    * **Mechanism:** After each chapter or major plot arc, a dedicated process will parse the event history and extract key entities (characters, items, locations) and their relationships. For instance, the sequence of events "Player chose to hide the diary from Mark" would be encoded as nodes and edges in the graph: `(Player) --[HID_ITEM_FROM]--> (Mark)` and `(Diary) --[IS_SUBJECT_OF]--> (HID_ITEM_FROM)`.
    * **Advantages:** This graph structure allows for efficient querying of past events without bloating the context window. Before generating a new scene involving Mark and the diary, the system can query the graph for all relationships between them and inject a concise summary into the prompt (e.g., `"MEMORY: Player previously hid the diary from Mark, causing distrust"`). This method, supported by research in graph-based memory for conversational AI, provides a structured, relational memory that is more scalable and less prone to information loss than prose summarization. 

By adopting this tiered, graph-based memory system, our project directly addresses the challenge of growing context in long-running LLM conversations, ensuring narrative consistency and logical integrity throughout the player's extensive journey.

***

### **2. Fine-Tuned Director LLM Pipeline**

The core of our narrative generation engine is a **Fine-Tuned Director LLM**, which is responsible for creating coherent, emotionally resonant, and structurally sound scene scripts. This project will employ a two-stage pipeline, leveraging the complementary strengths of different local open-weight models to separate the creative task of writing from the rigid task of formatting. This hybrid approach, detailed below, is designed for robustness, scalability, and local execution on consumer-grade hardware.

---

#### **Implementation Strategy**

1.  **Stage 1: Creative Generation:** A local, quantized LLM with strong instruction-following and storytelling capabilities (e.g., **LLaMA-3-8B** or **OpenHermes-7B**) will serve as the creative engine. This model will be fine-tuned on an augmented dataset derived from horror movie scripts and Creepypastas. Its sole task is to generate a narratively compelling scene in a semi-structured markup format (e.g., `::CHARACTER:: Jane`, `::MOOD:: Tense`), freeing it from the constraints of perfect JSON syntax. This focus on creative output ensures higher-quality prose and dialogue.

2.  **Stage 2: Structured Formatting:** A lightweight, highly specialized local model (e.g., **Phi-3-Mini** or **Qwen-2.5-1.5B**) will act as a utility formatter. This model will be fine-tuned on a paired dataset of the semi-structured markup and the final, strict JSON schema. Its only function is to parse the creative output from Stage 1 and convert it into the machine-readable JSON format required by the game engine. This division of labor makes the pipeline resilient to formatting errors and allows for independent optimization of both the creative and structural components.

The training data for these models will be synthetically generated using techniques from seminal works like *Self-Instruct* (Wang et al., 2022), ensuring a robust and diverse dataset for fine-tuning.

***

### **3. Image-to-Image (img2img) Generation System**

To ensure visual consistency and narrative cohesion, this project will implement an advanced **Image-to-Image Generation System** based on the **InstructPix2Pix** model, complemented by **LoRA (Low-Rank Adaptation)** fine-tuning for character fidelity. This system is designed to modify a set of pre-defined base assets (backgrounds, character sprites) in response to dynamic narrative events, ensuring that the visuals always reflect the current state of the story.

---

#### **Implementation Strategy**

1.  **Base Asset Modification:** The Director LLM's JSON output will contain specific, instruction-based prompts for the image pipeline. For example, if the player is gifted a clock, the JSON will include a prompt like `"Apply this edit: Add an antique grandfather clock to the left of the fireplace."`
2.  **Instruction-Based Editing:** The **InstructPix2Pix** model will take a pre-drawn base image of the room and the text instruction as input. As demonstrated by Brooks et al. (2023), this model excels at performing targeted edits while preserving the overall style and composition of the base image. This allows for dynamic changes—such as altering the time of day, adding or removing key items, or showing weather effects—without requiring a vast library of pre-rendered assets.
3.  **Character Consistency with LoRA:** To maintain character identity across different scenes and expressions, we will fine-tune a Stable Diffusion model using **LoRA**. By training a small LoRA file on a curated dataset of a specific character's approved design, we can invoke that character with high fidelity using a trigger word. This parameter-efficient fine-tuning method, adapted from the work of Hu et al. (2021), ensures that "Jane" always looks like Jane, whether she is happy, sad, or terrified, solving one of the most significant challenges in generative visual storytelling.

***

### **4. Performance Metrics and Evaluation Framework**

The success of this project will be evaluated through a comprehensive framework that assesses technical performance, qualitative output, and the overall user experience. This multi-faceted approach ensures a rigorous and holistic measure of the system's capabilities.

---

#### **Evaluation Criteria**

1.  **Technical Performance:**
    * **Latency:** We will measure **Time-to-Text** (player input to first word on screen) and **Time-to-Visuals** (input to final rendered image). The primary target is to keep perceived latency for text under 2 seconds.
    * **Validity Rate:** We will track the percentage of LLM outputs that are syntactically valid JSON and adhere to the required schema, targeting a >98% success rate after the self-correction loop.
    * **Resource Utilization:** For local execution, we will benchmark peak VRAM and CPU usage to ensure the application runs smoothly on consumer-grade hardware.

2.  **Qualitative Analysis:**
    * Using an automated VLM-based evaluator, we will score generated scenes (on a 1-10 scale) across several dimensions:
        * **Narrative Coherence:** Logical consistency and memory of past events.
        * **Character Consistency:** Adherence to defined personality traits.
        * **Plot Adherence:** Faithfulness to the author's Plot Point Graph.
        * **Text-Image Cohesion:** The degree to which the generated visuals match the text's mood and content.

3.  **User Experience (UX) Testing:**
    * **Player Surveys:** Post-session questionnaires will use Likert scales to gauge player perception of story engagement, character believability, and the meaningfulness of their choices.
    * **Replayability Study:** The project's core hypothesis of dynamic storytelling will be tested by having users play through a chapter multiple times with different choices. A successful evaluation will see players reporting genuinely distinct narrative paths and outcomes, confirming the system's ability to create unique, replayable experiences. 

----
----

---

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

1.  **Core State:** A compact, persistent JSON object representing the "ground truth" of the game world. It tracks essential variables like character relationships, major plot flags (`power_is_out: true`), and character statuses (`Dr_Evans: deceased`), acting as an immutable rulebook for the LLM.
2.  **Recent History:** A rolling FIFO (First-In, First-Out) buffer containing the full JSON outputs of the last 3-5 narrative beats. This provides high-fidelity, short-term context for maintaining immediate conversational flow.
3.  **Summarized Memory (Knowledge Graph Representation):** The most novel component of our system is its approach to long-term memory. As events age out of the `Recent History` buffer, they are processed into a **Knowledge Graph**. A dedicated NLP process will extract entities (characters, items, locations) and their relationships (e.g., `(Player) --[HID_ITEM_FROM]--> (Mark)`). This structured, graph-based representation allows for efficient querying of past events. Before a new generation, the system can traverse the graph to find relevant historical relationships and inject them as a concise summary into the prompt. This method provides a more scalable and accurate memory model than simple prose summarization, ensuring long-term narrative consistency.

#### **3.4 Narrative Generation: Hybrid Director LLM Pipeline**

To achieve both high creative quality and robust, error-free structured output, we will implement a two-stage hybrid pipeline for our Director LLM, optimized for local execution.

1.  **Stage 1: Creative Generation:** The primary creative task is handled by a fine-tuned, quantized LLM renowned for its instruction-following and storytelling capabilities (e.g., **LLaMA-3-8B** or **OpenHermes-7B**). This model will be fine-tuned on our augmented horror script dataset. Its sole task is to generate compelling narrative content in a semi-structured markup format (e.g., `::CHARACTER:: Jane`, `::MOOD:: Tense`), freeing it from the rigid constraints of perfect JSON syntax.
2.  **Stage 2: Structured Formatting:** The markup from the first stage is then passed to a lightweight, highly specialized utility model (e.g., a fine-tuned **Phi-3-Mini**). This model's only function is to parse the creative markup and convert it into the strict, validated JSON schema required by the game engine. This division of labor isolates creative generation from structural formatting, drastically reducing output brittleness and simplifying debugging.

#### **3.5 Visual Generation: Dynamic Asset Pipeline**

Our visual pipeline is designed for consistency, dynamism, and efficiency, leveraging a combination of pre-made assets and generative models.

1.  **Base Asset Foundation:** The system will use a library of high-quality, pre-drawn base assets for backgrounds and neutral-expression character sprites. This ensures a consistent and artist-defined core visual style.
2.  **Instruction-Based Image Editing:** For dynamic scene changes, we will use an **`img2img`** model, specifically **InstructPix2Pix**. The Director LLM's script will include explicit editing instructions (e.g., `"Apply this edit: make the sky look like a stormy evening"`). InstructPix2Pix will modify the base background image according to this instruction while preserving its core composition, allowing for a vast number of visual variations without creating new assets from scratch.
3.  **Character Consistency via LoRA Fine-Tuning:** To solve the critical problem of maintaining a consistent character appearance, we will fine-tune a Stable Diffusion model using **LoRA (Low-Rank Adaptation)**. For each main character, we will train a small, dedicated LoRA file on a curated set of their approved design. By activating this LoRA with a trigger word in the prompt, we can generate the character with high fidelity in any new pose or context, ensuring their visual identity remains stable throughout the game. Character expressions will be handled by the LLM selecting from a predefined list of sprites to maintain artistic control.