Parent notes:
 

# Algorithm

- Load all the entries to be compared lets say (61)
- Create a knockout style tournament board with seeding (32 matchups)
- Ask gemini to compare the two in terms of creativity (write a good prompt, creativity is too vague) and then decide on a winner.
- By backtracking who all lost against the winner figure out who was the second place(Since second place would have lost against the winner somewhere, this is a popular DSA algorithm)
- This way you have a ranked list of top creative texts

- **Principle:** AI models are better at comparison rather than assigning scores


# Refined algorithm



### Algorithm 1: Knockout with Recursive Ranking

This algorithm produces a complete ranking by running a main elimination tournament and then a series of subsequent "consolation" tournaments to rank the losers.



---

## 1. Initial Setup and Bracket Creation

1.  **Load Texts:** Begin with your list of N texts.
2.  **Handle N:**
    * **If N is a power of two** (e.g., 32, 64): Proceed directly to creating a standard knockout bracket.
    * **If N is not a power of two** (e.g., 61): You must create **byes** (free passes to the next round).
        * Find the next highest power of two, **P** (for N=61, P=64).
        * Calculate the number of byes: `Byes = P - N` (so, `64 - 61 = 3`).
        * Randomly select **3** texts to receive a bye. They advance directly to Round 2.
        * The remaining **58** texts will play in Round 1.
3.  **Build Bracket:** Randomly pair the texts playing in Round 1. Place the "bye" texts into the Round 2 slots.

## 2. Phase 1: Run the Main Tournament

1.  **Compare Texts:** For each matchup in the bracket, send the two texts to an AI with a clear and consistent prompt (e.g., "*Between Text A and Text B, which demonstrates greater creative originality? State only the winner.*").
2.  **Record and Advance:** Log the winner and who it defeated for every match. The winner advances to the next round.
3.  **Crown a Champion:** Continue until only one text remains. This text is **Rank #1**.

## 3. Phase 2: Run the Recursive Ranking Playoffs

1.  **To Find Rank #2:**
    * Create a new pool of all texts that were defeated *directly by the #1 ranked text*.
    * Run a new, separate knockout tournament on this pool.
    * The winner of this playoff is **Rank #2**.
2.  **To Find Rank #3:**
    * Create a new pool of all texts that were defeated *directly by either the #1 or #2 ranked text*.
    * Remove any texts that have already been ranked (i.e., #1 and #2).
    * Run a new knockout tournament on this pool. The winner is **Rank #3**.
3.  **To Find Rank #k:**
    * Continue this pattern. To find the k-th rank, create a pool of all texts that lost to any of the top (k-1) ranked texts, remove those already ranked, and run a playoff.
4.  **Final Output:** A complete list of texts ranked from 1 to N.

***

### Algorithm 2: The Swiss System

This non-eliminating algorithm ranks texts based on performance over a fixed number of rounds, where players are continually matched against opponents with a similar record.



---

## 1. Initial Setup

1.  **Load Texts:** Begin with your list of N texts.
2.  **Set Rounds:** Determine the number of rounds, **R**. A good standard is `log₂(N)`, rounded up (e.g., for 61 texts, you'd run 6 rounds).
3.  **Create Scoreboard:** Initialize a scoreboard where every text has **0 points** and an empty list to track its past opponents.

## 2. Execute the Rounds

1.  **Round 1:**
    * Randomly pair all texts into N/2 matchups.
    * For each pair, use the AI to determine a winner.
    * Update the scoreboard: winners get 1 point, losers get 0. Record the opponent for each text.
2.  **Rounds 2 through R:**
    * Sort all texts by their current point score, from highest to lowest.
    * Pair texts that have the same score. For example, pair the top text in the "2 points" group with the second text in that group, and so on.
    * **No Rematches:** Before finalizing a pair, check if they've played before. If so, pair the first text with the next available opponent in the same score bracket.
    * Run all matchups for the round and update the scoreboard and opponent lists.
3.  **Repeat:** Continue this process for all R rounds.

## 3. Determine Final Ranking

1.  **Primary Rank:** After the final round, sort the texts by their total points. This is the main ranking.
2.  **Tie-Breaking:** If multiple texts have the same final score, you must break the tie. The best method is the **Buchholz Score**.
    * For each tied text, calculate its Buchholz score by summing the final scores of **all its past opponents**.
    * The text with the higher Buchholz score wins the tie, as it indicates they played against a stronger overall schedule.
3.  **Final Output:** A complete list of texts ranked from 1 to N, based on overall performance and strength of schedule.


### Improvements

- ELO based system
- Ensemble of judges
- Instead of win/loss maybe use relative difference (con: even relative difference may be inconsistent so use different judges)
- Test: Rank Gemini generated stories, since Gemini has generated them it should tend to rate them as it rated them while generating. 
- The comparison function is configurable and can be according to your specific values. Maybe you can give some examples using fewshot (Experimenting with comparison function)
- Create a gold standard dataset, the position of the "creative text" within that dataset will help determine the "score"
## Observations

- Above a certain threshold the ai model over-rates each text making ranking difficult
- [[AIVN Benchmark- Terminal output]]
- [[AIVN Benchmark Tests]]