# Text Creativity Comparison & Tournament Suite

This repository provides a modular system to compare, score, and rank short texts using AI-assisted comparisons and several tournament formats (knockout, Swiss, ELO, and a naive independent scorer). It also includes a visualization utility to create comprehensive analysis and visual outputs.

## Quick start — run a tournament

Prerequisites
- Python 3.8+ (Linux)
- pip
- An API key for the Gemini / Google Generative AI client (passed via the `--api-key` flag)

Install minimal dependencies

It's recommended to use a virtual environment. From the project root:

```bash
# create and activate a virtual environment (optional but recommended)
python -m venv .venv
source .venv/bin/activate

# install required packages from the requirements file
pip install -r requirements.txt
```

Place your text files (UTF-8, `.txt`) in a directory, e.g. `texts/`. Each file will be treated as one entry in the tournament. Filenames (without the `.txt`) are used as IDs.

Run the main orchestration script `text_comparison_modular.py`:

```bash
# Knockout (default)
python text_comparison_modular.py --tournament knockout --directory texts --api-key YOUR_API_KEY

# Swiss
python text_comparison_modular.py --tournament swiss --directory texts --rounds 5 --api-key YOUR_API_KEY

# ELO
python text_comparison_modular.py --tournament elo --directory texts --rounds 6 --api-key YOUR_API_KEY

# Naive independent scoring
python text_comparison_modular.py --tournament naive --directory texts --api-key YOUR_API_KEY
```

Notes
- The scripts call the Gemini model via the Google Generative AI Python client (`google.generativeai as genai`). Make sure your API key has access.
- The comparator modules include rate-limiting and retry/fallback behavior. If API requests fail, some modules fall back to randomized choices/scores.

## Files overview (brief)

- `comparator.py`
  - Core AI-based text comparator. Wraps the Gemini model, enforces per-minute rate limits, and implements `compare_texts(textA, textB)` returning the more creative excerpt. Handles JSON parsing of AI responses, retry/backoff, and falls back to random selection when necessary.

- `text_comparison_modular.py`
  - Main CLI orchestrator. Loads texts from a directory and runs the selected tournament (`knockout`, `swiss`, `elo`, or `naive`). Sets up logging and timing, and exposes `--tournament`, `--directory`, `--rounds`, and `--api-key` flags.

- `knockout.py`
  - Implements a single-elimination (knockout) tournament. Handles byes, runs rounds until one champion is left, and then runs recursive mini-tournaments to produce a full ranking of all entries.

- `swiss.py`
  - Implements a Swiss-system tournament. Maintains a scoreboard, avoids rematches when possible, gives byes, and uses Buchholz tiebreakers for final rankings.

- `elo.py`
  - Implements an ELO-based tournament with adaptive K-factors and Swiss-style pairings. Tracks games played, opponents, wins/losses, and computes Buchholz scores for tie-breaking.

- `naive.py`
  - Independent scoring flow: each text is sent to the model and receives a numeric score (0–100). The final ranking is simply the descending sort by score. Contains a `NaiveScorer` with retries and a random fallback.

- `create_comprehensive_analysis.py`
  - Generates visualizations and textual analysis from tournament outputs. Produces heatmaps, line graphs, parameter vs ELO graphs, beam-width analysis, and writes detailed `.txt` analysis into the `Comprehensive_Analysis/` folder.

- `Comprehensive_Analysis/`
  - Output directory produced by `create_comprehensive_analysis.py`. Contains subfolders and generated plots/analysis (`heatmaps/`, `line_graphs/`, `parameter_graphs/`, `beam_analysis/`, `text_analysis/`, etc.).


## Tips & troubleshooting

- If you get rate-limit errors from the AI API, the `comparator` and `naive` modules include retries and wait logic. You can lower the request rate by spacing runs or batching offline.
- For large numbers of texts, consider running the `naive` scorer (independent scoring) first to narrow candidates before running tournament comparisons.
- If plotting fails, ensure `matplotlib` is installed and that the environment can write files to the working directory.

## Suggested improvements (small list)

- Add a `requirements.txt` with pinned package versions.
- Add an environment-variable option for the API key (so it doesn't appear on the CLI history).
- Add unit tests for the tournament pairing logic and for JSON parsing of comparator responses.

## License

Include your license of choice here (e.g., MIT) or remove this section if using in a private project.

---

README created at project root. Run the main CLI (`text_comparison_modular.py`) to start experiments and produce logs and analysis.
