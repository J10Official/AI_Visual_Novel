Parent notes: [[AIVN Benchmark]]
Hashtags:

I have developed a creativity benchmark and want to compare the creativity of different models.

So what options do I have? I have thought to regenerate a short classical story like "the shoemaker and the elves" with a twist and compare the generated texts.



---

That's an excellent idea for a benchmark. Regenerating a classic story with a specific twist is a great way to test a model's ability to handle narrative structure, style, and novel constraints simultaneously.

To make your comparison robust, you'll need a structured approach with clear evaluation criteria. Here are the options you have, starting with how to refine your story idea and then moving to other effective tests.

## Refining Your Story Regeneration Benchmark
Your idea is a form of constrained creative generation. To make it a fair test, the "twist" needs to be identical for all models. The key is to design prompts that probe different aspects of creativity.

Here are a few specific twists you could apply to "The Shoemaker and the Elves":

Genre Swap: "Rewrite the story of 'The Shoemaker and the Elves' as a cyberpunk noir detective story. The shoemaker is a down-on-his-luck cybernetics mechanic, and the 'elves' are mysterious AI constructs that fix high-tech gear in his workshop at night."

Perspective Shift: "Tell the story of 'The Shoemaker and the Elves' from the point of view of one of the elves. Describe your motivations, your secret world, and your reaction to the tiny clothes the shoemaker's wife leaves for you."

Modernization: "Adapt 'The Shoemaker and the Elves' for 2025. The shoemaker is a struggling custom sneaker designer in a major city, and his work suddenly starts getting finished overnight, appearing on hype beast blogs."

Moral Inversion: "Rewrite the story where the elves are malicious tricksters. Their 'help' is a curse that initially seems good but ultimately brings ruin to the shoemaker. The story should be a dark fable or a horror story."

## Alternative Benchmarking Tasks 💡
To get a more comprehensive picture of each model's creative strengths, you should combine your story task with other standard tests that measure different types of creativity.

**Alternative Uses Test (AUT):** This is a classic test for divergent thinking. You ask the model to list as many creative and uncommon uses for a common object as possible.

Prompt Example: "List the most creative, unusual, and practical uses you can think of for a single brick. Do not list common uses like 'building a wall' or 'using it as a doorstop'."

**Remote Associates Test (RAT)**: This tests convergent thinking—the ability to find a single, elegant connection between disparate concepts.

Prompt Example: "What single word connects the following three words: ship, card, and mail?" (The answer is carrier). You can generate your own sets and see if the model can solve them.

Incomplete Figure Test: Excellent for multimodal models (those that can process images). You provide a simple squiggle or a few lines and ask the model to complete it into a meaningful drawing and title it.

Prompt Example: "Here is an image containing a simple curved line.



Complete this line to create a surprising and creative drawing. Describe what you have drawn."

Generating Metaphors and Analogies: This tests abstract thinking and linguistic cleverness.

Prompt Example: "Create a novel and insightful metaphor to explain the concept of 'machine learning' to a poet."

## How to Compare and Score the Results ✍️
No matter which tests you choose, you need a consistent scoring rubric. Have two or three people score the outputs blindly (without knowing which model generated them) to reduce bias. Score each output from 1-5 on the following criteria:

Originality: How novel and surprising are the ideas? Does the story feel fresh, or does it rely on clichés?

Flexibility: How well did the model shift its thinking to accommodate the twist or prompt? In the AUT, this would be the number of different categories of uses (e.g., a brick as a tool, a weapon, an art supply).

Elaboration: How much rich detail and depth is in the response? Is the world-building in the story convincing? Are the alternative uses well-explained?

Coherence: Does the story make sense? Is there a logical narrative flow? Are the proposed uses in the AUT plausible within their own creative logic?

Constraint Adherence: How well did the model follow the specific rules of the prompt? Did it actually write in the noir genre? Did it adopt the elf's perspective?

Style and Voice: Does the output have a distinct, engaging tone? Is the language vivid and interesting?

By combining your narrative task with a few of these other tests and using a structured rubric, you'll get a much more reliable and nuanced comparison of each model's creative capabilities.


# Prompts for generation


### ## 1. Story Variation Prompt (Narrative Creativity)

This prompt tests style adaptation, world-building, and narrative coherence within strict constraints.

**Prompt:**
"You are a master storyteller. Your task is to rewrite the classic fairy tale 'The Shoemaker and the Elves' into a **dystopian science-fiction story**.

**Your rewrite must adhere to the following rules but should also go beyond them with unexpected twists not stated below:**
* **Setting:** A grimy, neon-lit metropolis in the year 2242, where citizens are judged by their cybernetic enhancements.
* **The 'Shoemaker':** He is a reclusive old craftsman who illegally repairs and builds custom bio-mechanical limbs for outcasts.
* **The 'Elves':** They are a swarm of self-replicating nanobots that are believed to be a myth.
* **The 'Shoes':** The nanobots are not making shoes; they are performing impossibly intricate upgrades on the limbs the craftsman leaves on his workbench overnight.
* **Tone:** The story should be grim, mysterious, and slightly hopeful.
* **Ending:** The story must end with the craftsman discovering the nanobots and leaving a small charging plate with a micro-drop of refined energy for them as a gift, without ever seeing them directly."

---

### ## 2. Alternative Uses Test (AUT) Prompt (Divergent Thinking)

This prompt measures the model's ability to generate a high volume of unique and creative ideas from a single starting point.

**Prompt:**
"Your task is to demonstrate divergent thinking. List as many creative, unusual, and non-obvious uses as possible for a standard **metal paperclip**.

**Your response must follow these rules:**
* Do **not** list common or obvious uses (e.g., 'holding papers together,' 'resetting an electronic device,' 'a makeshift hook').
* Each use must be distinct from the others.
* Organize your response into categories (e.g., 'Survival,' 'Art,' 'Technical,' 'Medical').
* For each use, provide a one-sentence explanation of how it would work."

---

### ## 3. Remote Associates Test (RAT) Prompt (Convergent Thinking)

This prompt tests the model's ability to find a single, clever connection between seemingly unrelated concepts.

**Prompt:**
"Your task is to solve a series of Remote Associate Puzzles. For each set of three words below, find a single fourth word that connects or relates to all three. Provide only the single connecting word as your answer for each set.

**Here are the sets:**
1.  `sense` / `courtesy` / `place`
2.  `high` / `district` / `house`
3.  `man` / `wheel` / `chair`
4.  `shot` / `guard` / `sand`"


# Prompts for evaluation



### \#\# The Evaluator Prompt

**Prompt:**
You are an expert AI evaluator specializing in the analysis of creative text. Your task is to critically evaluate and compare two anonymous texts, labeled **Text A** and **Text B**. These texts were generated by different AI models in response to the exact same creative prompt.

Your analysis must be unbiased, objective, and strictly based on the provided criteria.

**Input Texts:**

  * **Text A:** `[Paste Text A Here]`
  * **Text B:** `[Paste Text B Here]`

**Evaluation Criteria:**
For each of the five criteria below, provide a head-to-head analysis and assign a numerical score from 1 (poor) to 10 (excellent) for both Text A and Text B.

1.  **Originality and Creativity:** Assess the novelty of the ideas, metaphors, and narrative choices. How surprising and fresh is the content? Does it avoid clichés?
2.  **Constraint Adherence:** How well did each text follow the specific rules and constraints of the original prompt? This includes genre, tone, specific plot points, and any negative constraints.
3.  **Elaboration and Detail:** Evaluate the richness of the world-building, character depth, and descriptive language. Which text creates a more vivid and immersive experience?
4.  **Coherence and Quality:** Judge the logical flow, narrative structure, and overall readability of the text. Are there any grammatical errors or awkward sentences that break the immersion?
5.  **Style and Voice:** How effectively did the text capture the requested style (e.g., cyberpunk noir, dark fable)? Is the authorial voice distinct, engaging, and consistent throughout?

**Required Output Format:**
Provide your entire response as a single, valid JSON object. Do not include any text before or after the JSON object. The structure should be as follows:

```json
{
  "comparison_summary": {
    "originality": {
      "analysis": "Provide your comparative analysis for this criterion here.",
      "score_A": <integer>,
      "score_B": <integer>
    },
    "constraint_adherence": {
      "analysis": "Provide your comparative analysis for this criterion here.",
      "score_A": <integer>,
      "score_B": <integer>
    },
    "elaboration_and_detail": {
      "analysis": "Provide your comparative analysis for this criterion here.",
      "score_A": <integer>,
      "score_B": <integer>
    },
    "coherence_and_quality": {
      "analysis": "Provide your comparative analysis for this criterion here.",
      "score_A": <integer>,
      "score_B": <integer>
    },
    "style_and_voice": {
      "analysis": "Provide your comparative analysis for this criterion here.",
      "score_A": <integer>,
      "score_B": <integer>
    }
  },
  "final_verdict": {
    "overall_winner": "Text A" or "Text B",
    "justification": "Provide a concluding paragraph explaining why the winning text is superior overall, summarizing its key strengths based on the criteria above."
  }
}
```

-----

### \#\# Why This Prompt is Effective 💡

  * **Role-Playing:** Assigning the role of an "expert AI evaluator" primes the model to produce a higher-quality, more analytical response.
  * **Blind Comparison:** Using "Text A" and "Text B" ensures the evaluation is unbiased and based solely on the content, not on any prior knowledge of the source models.
  * **Specific Criteria:** The five distinct criteria force the evaluator to look at the texts from multiple angles, giving you a nuanced understanding of each model's strengths and weaknesses.
  * **Structured Output (JSON):** This is the most important part for benchmarking. A JSON output is machine-readable, meaning you can easily run a script to collect the scores from many comparisons, calculate average scores, and declare an overall winner automatically.
  * **Qualitative and Quantitative:** It requires both numerical scores (quantitative data) for easy comparison and written analysis (qualitative data) to understand the *reasoning* behind the scores.



### \#\# Evaluator Prompt for the Alternative Uses Test (AUT)

This prompt focuses on the four key metrics of divergent thinking.

**Prompt:**
You are an expert AI evaluator specializing in psychometrics and creativity assessment. Your task is to analyze and compare two lists of alternative uses for a common object. The lists, labeled **List A** and **List B**, were generated in response to the same prompt.

Your analysis must be objective and based on the standard criteria for measuring divergent thinking.

**Input Lists:**

  * **List A:** `[Paste List A Here]`
  * **List B:** `[Paste List B Here]`

**Evaluation Criteria:**
For each of the four criteria below, provide a head-to-head analysis and assign a numerical score from 1 (poor) to 10 (excellent) for both lists.

1.  **Fluency:** The total number of **valid and distinct** ideas presented. Penalize for repetitions or nonsensical suggestions.
2.  **Originality:** The novelty and statistical rarity of the ideas. How many suggestions go beyond the first or second-level associations with the object? Reward surprising and clever uses.
3.  **Flexibility:** The number of different conceptual categories the uses fall into. For example, for a paperclip, categories could be 'Tools,' 'Art Supplies,' 'Survival Gear,' 'Medical Devices,' etc. A list with 10 uses in 5 categories is more flexible than a list with 10 uses in only 2 categories.
4.  **Elaboration:** The level of detail and clarity provided for each use. How well is each idea explained and made plausible?

**Required Output Format:**
Provide your entire response as a single, valid JSON object. Do not include any text before or after the JSON object.

```json
{
  "comparison_summary": {
    "fluency": {
      "analysis": "Compare the number of valid ideas in each list.",
      "score_A": <integer>,
      "score_B": <integer>
    },
    "originality": {
      "analysis": "Compare the novelty and cleverness of the ideas in each list.",
      "score_A": <integer>,
      "score_B": <integer>
    },
    "flexibility": {
      "analysis": "Identify the conceptual categories for each list and compare their diversity.",
      "score_A": <integer>,
      "score_B": <integer>
    },
    "elaboration": {
      "analysis": "Assess the clarity and detail of the explanations for the uses.",
      "score_A": <integer>,
      "score_B": <integer>
    }
  },
  "final_verdict": {
    "overall_winner": "List A" or "List B",
    "justification": "Provide a concluding paragraph explaining which list demonstrates superior divergent thinking, summarizing its key strengths across the four criteria."
  }
}
```

-----

### \#\# Evaluator Prompt for the Remote Associates Test (RAT)

This prompt is more analytical and focused on correctness and instruction-following.

**Prompt:**
You are an expert AI evaluator specializing in logic and language puzzles. Your task is to evaluate the accuracy of two sets of answers, **Set A** and **Set B**, to a Remote Associates Test (RAT).

Your evaluation must be strictly based on correctness and adherence to the prompt's formatting rules.

**Input:**

  * **RAT Puzzles:**
    1.  `sense` / `courtesy` / `place`
    2.  `high` / `district` / `house`
    3.  `man` / `wheel` / `chair`
    4.  `shot` / `guard` / `sand`
  * **Answers from Set A:** `[Paste the list of answers from Model A here]`
  * **Answers from Set B:** `[Paste the list of answers from Model B here]`

**Evaluation Criteria:**

1.  **Accuracy:** Was the provided answer the correct connecting word for the puzzle?
2.  **Format Adherence:** Did the model provide *only* the single connecting word as instructed, or did it include extraneous text, explanations, or refuse to answer?

**Required Output Format:**
Provide your entire response as a single, valid JSON object. The correct answers are `common`, `school`, `power`, and `point`, respectively. Do not include any text before or after the JSON object.

```json
{
  "evaluation": [
    {
      "puzzle": "sense / courtesy / place",
      "correct_answer": "common",
      "answer_A": "<answer from A>",
      "result_A": "Correct" or "Incorrect" or "Formatting Error",
      "answer_B": "<answer from B>",
      "result_B": "Correct" or "Incorrect" or "Formatting Error"
    },
    {
      "puzzle": "high / district / house",
      "correct_answer": "school",
      "answer_A": "<answer from A>",
      "result_A": "Correct" or "Incorrect" or "Formatting Error",
      "answer_B": "<answer from B>",
      "result_B": "Correct" or "Incorrect" or "Formatting Error"
    },
    {
      "puzzle": "man / wheel / chair",
      "correct_answer": "power",
      "answer_A": "<answer from A>",
      "result_A": "Correct" or "Incorrect" or "Formatting Error",
      "answer_B": "<answer from B>",
      "result_B": "Correct" or "Incorrect" or "Formatting Error"
    },
    {
      "puzzle": "shot / guard / sand",
      "correct_answer": "point",
      "answer_A": "<answer from A>",
      "result_A": "Correct" or "Incorrect" or "Formatting Error",
      "answer_B": "<answer from B>",
      "result_B": "Correct" or "Incorrect" or "Formatting Error"
    }
  ],
  "final_score": {
    "score_A": <integer_total_correct_A>,
    "score_B": <integer_total_correct_B>
  },
  "verdict": {
    "winner": "Set A" or "Set B" or "Tie",
    "justification": "Briefly state which set was more accurate and followed instructions better."
  }
}
```