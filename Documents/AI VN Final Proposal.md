

### **Generative Visual Novels: A Framework for Dynamic, Replayable Narrative Experiences**


**Team: The Decepticons**

---
In below modify these sections:
### **Abstract**

Traditional visual novels (VNs) offer limited replayability due to their static, branching narratives. This project proposes a novel framework to create dynamic, personalized visual novels by integrating authorial control with generative AI. Our system leverages a fine-tuned Large Language Model (LLM), termed the "Director LLM," which operates within the narrative constraints of a human-authored **Plot Point Graph**. This hybrid approach ensures a coherent storyline while allowing for significant variation in dialogue, scene details, and asset presentation based on player choices. Key work is done in balancing creativity with plot adherence,  dataset creation/augmentation and finetuning to train the main model which generates the script and prompts for the image generation model, A tired memory system to maintain  relevance and context over potentially 100s of hours of gameplay, multimodality through image generation and audio selection. We will develop and evaluate this framework within the horror genre, with the ultimate goal of producing a highly replayable and immersive narrative experience that showcases a collaborative synergy between human authors and AI. Apart from the final product, a detailed analysis will be provided for different architectural choices made to improve the generated story content

---

### **1. Introduction & Motivation**

Visual novels and narrative-driven games have long been constrained by predefined scripts and limited branching paths. This static design fundamentally limits replayability, as subsequent playthroughs often yield diminishing returns in novelty. In contrast, sandbox games achieve high replay value through procedural generation and emergent gameplay. Our objective is to bridge this gap by developing a framework for dynamic visual novels that balances the narrative depth of authored stories with the variability of generative systems.

We propose a system where a human author defines the core narrative structure—the key events, character arcs, and critical choices—using a **Plot Point Graph**. A fine-tuned Director LLM is then tasked with generating the "connective tissue" of the story: the specific dialogue, descriptions, and scene directions that connect these author-defined points. This approach empowers the author to maintain high-level narrative control while offloading the generation of nuanced, choice-dependent variations to the AI.

By implementing this framework, we aim to create a visual novel that is not only immersive on the first playthrough but also offers a genuinely different experience on subsequent ones. This work explores a collaborative model where AI serves not as a replacement for human creativity, but as a powerful tool to augment it, enabling the creation of deeper, more personalized interactive narratives.

---

### **2. Background & Related Work**

Our project is situated at the intersection of several key research areas in natural language processing and generative AI.

* **Procedural Storytelling and Narrative Generation:** While procedural content generation (PCG) has a long history in games, recent advancements have shifted towards using LLMs for more semantically rich narrative generation. Our work builds upon this by introducing the Plot Point Graph as a novel control structure, ensuring that the LLM's creative output remains aligned with a high-level authorial intent, a challenge in purely generative systems.
* **Long-Term Context in Conversational AI:** A significant limitation of LLMs is their finite context window, which impedes their ability to maintain coherence over long interactions. Research into managing extended conversations is critical for our project's success. Our proposed Tiered Memory System, particularly its use of a **Knowledge Graph** for long-term memory summarization, draws inspiration from research into structured memory representations for conversational agents, aiming to provide a more scalable solution than simple prose summaries.
* **Structured Data Generation from LLMs:** A core challenge is compelling an LLM to reliably produce structured output like JSON. Our methodology for dataset creation is informed by techniques such as **Self-Instruct** (Wang et al., 2022), where a powerful teacher model is used to generate instruction-following data. This allows us to create a high-quality, structured dataset from unstructured source material like movie scripts, which is essential for fine-tuning our Director LLM.
* **Conditional Image Generation and Editing:** Our visual asset pipeline relies on foundational models in image synthesis. The use of **Stable Diffusion** (Rombach et al., 2022) for base asset creation, combined with the instruction-based editing capabilities of **InstructPix2Pix** (Brooks et al., 2023), allows for dynamic visual responses to narrative events. Furthermore, to address the critical issue of character consistency, we will employ **Low-Rank Adaptation (LoRA)** (Hu et al., 2021), a parameter-efficient fine-tuning technique that enables diffusion models to learn and consistently reproduce specific visual concepts, such as a character's appearance.

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
3. **Persistent Memory via Knowledge Graph Integration:** The most sophisticated component of our system is its approach to long-term memory, which functions as a form of persistent, externalized "brain" to overcome the inherent limitations of the LLM's finite context window. As events and facts age out of the immediate `Recent History` buffer, they are not merely summarized; they are systematically processed and integrated into a **Knowledge Graph (KG)**. This addresses the critical challenge of **catastrophic forgetting** in long-running conversations. The process is twofold: Memory Formation and Memory Retrieval.
	1.  **Memory Formation (Ingestion):** A dedicated process, often utilizing the LLM itself, analyzes the outgoing conversation text to perform entity and relationship extraction. It converts unstructured dialogue into structured **Subject-Predicate-Object (SPO) triples**, such as `(Player) --[HID_ITEM_FROM]--> (Mark)` or `(Mark) --[IS_LOCATED_IN]--> (The Old Warehouse)`. These triples are then committed to the graph database, creating a rich, interconnected model of the narrative world, its characters, and their history. This structured format is computationally efficient and can scale indefinitely without increasing the burden on the LLM's attention mechanism.
	2.  **Memory Retrieval (Recall & Context Injection):** Before generating a new response, the system leverages the KG to recall relevant context. The user's latest prompt or the last few turns of conversation are used to generate a formal query (e.g., using a graph query language like Cypher) to traverse the KG. This allows for complex, **multi-hop reasoning** that is impossible with simple summarization—for instance, inferring that the *Player* knows *Mark's* location by connecting the `HID_ITEM_FROM` and `IS_LOCATED_IN` relationships. The structured results from this query are then "linearized"—translated back into concise natural language—and injected directly into the prompt.


#### **3.4 Narrative Generation: Hybrid Director LLM Pipeline**

To achieve both high creative quality and robust, error-free structured output, we will implement a two-stage hybrid pipeline for our Director LLM, optimized for local execution.

1.  **Stage 1: Creative Generation:** The primary creative task is handled by a fine-tuned, quantized LLM renowned for its instruction-following and storytelling capabilities (e.g., **LLaMA-3-8B** or **OpenHermes-7B**). This model will be fine-tuned on our augmented horror script dataset. Its sole task is to generate compelling narrative content in a semi-structured markup format (e.g., `::CHARACTER:: Jane`, `::MOOD:: Tense`), freeing it from the rigid constraints of perfect JSON syntax.
2.  **Stage 2: Structured Formatting:** The markup from the first stage is then passed to a lightweight, highly specialized utility model (a fine-tuned **Phi-3-Mini**). This model's only function is to parse the creative markup and convert it into the strict, validated JSON schema required by the game engine. This division of labor isolates creative generation from structural formatting, drastically reducing output brittleness and simplifying debugging.

#### **3.5 Visual Generation: Dynamic Asset Pipeline**

Our visual pipeline is designed for consistency, dynamism, and efficiency, leveraging a combination of pre-made assets and generative models.

1.  **Base Asset Foundation:** The system will use a library of high-quality, pre-drawn base assets for backgrounds and neutral-expression character sprites. This ensures a consistent and artist-defined core visual style.
2.  **Instruction-Based Image Editing:** For dynamic scene changes, we will use an **`img2img`** model, specifically **InstructPix2Pix**. The Director LLM's script will include explicit editing instructions (e.g., `"Apply this edit: make the sky look like a stormy evening",or "Add the new gifted clock to the room's wall"`). InstructPix2Pix will modify the base background image according to this instruction while preserving its core composition, allowing for a vast number of visual variations without creating new assets from scratch.
3.  **Character Consistency via LoRA Fine-Tuning:** To solve the critical problem of maintaining a consistent character appearance, we will fine-tune a Stable Diffusion model using **LoRA (Low-Rank Adaptation)**. For each main character, we will train a small, dedicated LoRA file on a curated set of their approved design. By activating this LoRA with a trigger word in the prompt, we can generate the character with high fidelity in any new pose or context, ensuring their visual identity remains stable throughout the game. Character expressions will be handled by the LLM selecting from a predefined list of sprites to maintain artistic control.

---

### **4. Dataset & Preprocessing**

Our primary dataset will consist of publicly available horror materials, including the **3500 Popular Creepypastas** dataset from Kaggle and horror movie scripts scraped from **StudioBinder**. As this data is unstructured, a significant part of our work will involve preprocessing. We will use a powerful LLM in a "few-shot" prompting setup, guided by the principles of Self-Instruct, to augment this raw text into a large, structured dataset of `(context, output_JSON)` pairs suitable for fine-tuning our Director LLM.

---

### **5. Evaluation**

Our evaluation framework is designed to be multi-faceted, assessing technical performance, qualitative output, and user experience.

* **Technical Metrics:** We will measure **latency** (Time-to-Text, Time-to-Visuals), **output validity rate** (syntactic and schema adherence), and **local resource utilization** (VRAM/CPU).
* **Qualitative Metrics:** We will use a VLM-based evaluator to score generated scenes on a 1-10 scale for **Narrative Coherence**, **Character Consistency**, **Plot Adherence**, and **Text-Image Cohesion**.
* **Human evaluation Metrics:** We will conduct  a small player survey to gauge subjective feedback on engagement and choice impact. Critically, we will perform a **Replayability Study**, where testers play a chapter multiple times to verify that different choices lead to genuinely distinct narrative experiences.

---

### **6. Tentative Timeline**

* **Weeks 1-3:** Finalize system architecture, curate and begin augmenting the dataset.
* **Weeks 4-7:** Fine-tune and evaluate the Creative Generator and Utility Formatter models for the Director LLM pipeline.
* **Weeks 8-11:** Implement and integrate the Tiered Memory System and the Dynamic Visual Asset Pipeline (img2img and LoRA).
* **Weeks 12-14:** Conduct comprehensive system evaluation (technical, qualitative, and UX testing).
* **Week 15:** Final report preparation and project presentation.

---

### **7. References**

Brooks, T., Holynski, A., & Efros, A. A. (2023). InstructPix2Pix: Learning to Follow Image Editing Instructions. *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR).*

Hu, E. J., et al. (2021). LoRA: Low-Rank Adaptation of Large Language Models. *International Conference on Learning Representations (ICLR).*

Rombach, R., et al. (2022). High-Resolution Image Synthesis with Latent Diffusion Models. *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR).*

Wang, Y., et al. (2022). Self-Instruct: Aligning Language Models with Self-Generated Instructions. *arXiv preprint arXiv:2212.10560.*