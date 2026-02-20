#  AI Visual Novel Generation System
### Fine-tuned LLM + Custom Benchmark + Interactive Browser Engine

> A full-stack research system that fine-tunes a language model to generate structured, branching visual novel scripts — complete with a novel creativity benchmark, ablation study over decoding strategies, and a browser-based playable engine.

📽️ **[Watch the Demo Video](https://youtu.be/lmpHNBLLonk?si=e5UHNiFLiLSBZpN5)** &nbsp;|&nbsp; 📄 **[Read the Report](./Report.pdf)**

---

## What This Project Does

Traditional visual novels suffer from static, non-replayable story branches. Current AI story generators lack coherence and authorial control. This project bridges that gap with a **hybrid narrative system** combining human creative oversight with AI-driven dynamic content generation.

The pipeline takes a rough story outline as input and produces a fully playable, branching visual novel — complete with character expressions, mood-based music cues, and background editing prompts — rendered live in the browser.

```
Story Outline → Fine-tuned LLM → Structured JSON Script → Browser Visual Novel Engine
```

---

## Key Contributions

### 1. 🗂️ Dataset Creation Pipeline
- 27 horror movie screenplays (~650K tokens) annotated into a structured schema capturing scenes, dialogue, branching choices, character expressions, and background prompts
- Two-stage annotation: Markdown intermediate format → JSON, reducing LLM hallucination
- Iterated through Zero-Shot → Few-Shot → Constrained Few-Shot (Gemini 2.5 Flash), achieving near-perfect format and content quality
- Interactive validation tool with ~10% correction rate over automated outputs

### 2. 🤖 Fine-tuned Generation Model (Gemma 2-2B-IT + QLoRA)
- 4-bit quantized fine-tuning via QLoRA (NF4 + BitsAndBytes) — **75% memory reduction** (8GB → 2GB)
- LoRA adapters targeting all attention projections; only ~0.5% of parameters trained (~10M of 2B)
- Three instruction formats per scene for diversity: Complete Scene, Dialogue Continuation, Emotion-Conditioned Generation
- ~5,891 scenes, 600K+ tokens of training data

### 3. 🏆 Novel Creativity Benchmark (ELO Tournament System)
- Addresses the "no ground truth" problem for creative text evaluation
- Implements and compares four ranking methodologies: Naive Scoring, Knockout, Swiss Tournament, and **ELO Rating**
- ELO emerged as the clear winner — correct champion identification, 204-point spread, zero score compression vs. 87.5% compression for naive scoring
- Validated against 16 files with known creativity gradients

### 4. 🔬 Decoding Strategy Ablation Study
- Evaluated 74 configurations across 5 strategies (Greedy, Beam Search, Sampling, Top-K, Top-P) on both creative and syntax adherence tasks
- **Creative tasks**: Top-K (k=30, T=0.7) optimal — ELO 1646
- **Syntax tasks**: Top-P (p=0.98, T=0.9) optimal — ELO 1622
- Key finding: temperature is the single most critical hyperparameter, with a systematic +0.2 shift needed for syntax vs. creative tasks

### 5. 🎮 Browser-Based Visual Novel Engine
- Parses generated JSON scripts into an interactive, real-time visual novel
- Supports branching paths, character sprites with expressions, background art with edit prompts, and mood-based music

---

## Repository Structure

Each module is **self-contained** with its own README.

```
├── Dataset creation/       # Screenplay scraping, annotation pipeline, validation tool
├── Fine-tuning/             # QLoRA fine-tuning on Gemma 2-2B-IT (Kaggle T4/A100)
├── Ablation text generation/   # Text generation across 74 decoding configurations
├── Benchmarking/           # ELO/Swiss/Knockout tournament system + visualizations
└── Visual NOvel Engine/    # ⬅️ START HERE — browser-based playable engine
```

> **To run the final product**, go to the `visual_novel_engine/` directory and follow its README.

---

## Technical Stack

| Component | Technology |
|-----------|-----------|
| Base Model | Google Gemma 2-2B-IT |
| Fine-tuning | QLoRA (4-bit NF4), LoRA r=8, HuggingFace PEFT |
| Annotation LLM | Gemini 2.5 Flash (1M context window) |
| Local Inference | Ollama (Llama 3.2:1b) |
| Training Infra | Kaggle T4 GPU (16GB VRAM), ~16h / 3 epochs |
| Benchmark | Custom ELO tournament with Buchholz tie-breaking |
| Engine | Browser-based (JavaScript), JSON-driven |

---

## Results at a Glance

| Task | Best Strategy | Best Config | ELO Score |
|------|--------------|-------------|-----------|
| Creative Generation | Top-K | k=30, T=0.7 | 1646 |
| Syntax Adherence | Top-P | p=0.98, T=0.9 | 1622 |
| Benchmark Ranking | ELO System | — | Correctly ranks all 16 tiers |

---

## Authors

**Jatin Agrawal** (2023114014) . **Amisha** (2023114003) · **Aaryan Kashyap** (2023114006)

