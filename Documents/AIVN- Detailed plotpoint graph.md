Parent notes: [[AI Visual Novel]]
Hashtags:

Of course. Here is an example of a Plot Point Graph for the beginning of a horror story.

This graph acts as the "narrative skeleton" that you, the author, would create. The game engine would then use this structure to generate specific, constrained prompts for the Director LLM.

---

### **Example Plot Point Graph**

**Title:** *Echoes of Polaris*
**Genre:** Sci-Fi Horror
**Setting:** A remote, abandoned arctic research station.

---

### **Chapter 1: The Silent Station**

**`ID: PP_1.1`**
* **Title:** Arrival
* **Location:** Station Exterior -> Airlock
* **Mood:** `Eerie`, `Isolated`, `Anticipatory`
* **Description:** The protagonist, Dr. Aris Thorne, arrives via snow-cat at the Polaris Research Station to find it completely silent. The main power is on, but there are no signs of the previous crew.


**`ID: PP_1.2`**
* **Title:** First Anomaly
* **Location:** Main Hub
* **Mood:** `Tense`, `Intriguing`
* **Description:** As Aris restores secondary systems, a bank of monitors flickers to life, displaying a strange, fractal-like symbol for a moment before shorting out with a loud crackle.


**`ID: PP_1.3`**
* **Title:** The Captain's Log
* **Location:** Captain's Quarters
* **Mood:** `Foreboding`, `Mysterious`
* **Description:** Aris finds the station captain's personal datapad. The last entry is corrupted, but readable fragments mention "a sound from the ice," "don't trust the signal," and a final, chilling sign-off: "It hears us now."


**`ID: CP_1.A` (Choice Point)**
* **Title:** The Signal and the Storm
* **Location:** Main Hub
* **Mood:** `Urgent`, `Conflicted`
* **Description:** An automated alert sounds. A massive blizzard is 90 minutes out, requiring a station lockdown. Simultaneously, a faint, repeating SOS signal appears on the comms panel, originating from the damaged relay tower half a kilometer away. The captain's log warned against trusting a signal.

* **Player Choices:**
    * **Path A:** "Investigate the relay tower. I can't ignore an SOS."
    * **Path B:** "Heed the warning. Lockdown the station now."

---

### **Branching Paths**

**(If player chose Path A)**
**`ID: PP_1.A.1`**
* **Title:** The Treacherous Path
* **Location:** Exterior - Path to Tower
* **Mood:** `Exposed`, `Harsh`
* **Description:** Aris dons an EV suit and ventures into the worsening weather. The wind is howling, and visibility is low.

* **Followed by `PP_1.A.2`**

**(If player chose Path B)**
**`ID: PP_1.B.1`**
* **Title:** Securing Engineering
* **Location:** Engineering Deck
* **Mood:** `Cautious`, `Tense`
* **Description:** Aris follows lockdown procedure, starting with reinforcing the power conduits in the engineering bay. The station groans under the wind's force.

* **Followed by `PP_1.B.2`**

---

**`ID: PP_1.A.2` (Result of Path A)**
* **Title:** The Lure
* **Location:** Relay Tower
* **Mood:** `Dread`, `Revelation`
* **Description:** Aris reaches the tower to find the SOS beacon is automated. A diagnostic check reveals its true purpose: it's not transmitting an SOS, but broadcasting a high-frequency signal *down* into the ice below the station. It was designed to attract something.
* **Key Info Gained:** `signal_is_a_lure = true`


**`ID: PP_1.B.2` (Result of Path B)**
* **Title:** The Hidden Schematic
* **Location:** Engineering Deck
* **Mood:** `Alarm`, `Discovery`
* **Description:** While sealing a service panel, Aris finds a scorched datachip hidden inside. It contains a partial schematic of the station's deep-ice sensors, showing a massive, unidentified energy source directly beneath the station—an energy source that seems to be *responding* to the relay tower's frequency.
* **Key Info Gained:** `energy_source_below = true`
* **LLM Task:** Generate the scene of finding the hidden chip and the alarming realization of what the schematics imply.

---

### **`ID: CP_1.C` (Convergence Point)**

* **Title:** The Blackout
* **Location:** Relay Tower (Path A) / Engineering (Path B)
* **Mood:** `Crisis`, `Trapped`
* **Description:** Regardless of the path taken, the blizzard hits with full force, causing a catastrophic power failure across the entire station. Emergency lights flicker on, casting deep, moving shadows. Aris is plunged into near darkness, armed with the terrifying knowledge she just uncovered.
* **LLM Task:** Describe the sudden, violent power outage. The narration should be slightly different depending on the player's location but the outcome is the same. The LLM should incorporate the `Key Info Gained` into Aris's internal monologue (e.g., Path A: "The blackout... did the signal finally call something up?"; Path B: "The blackout... did that energy source just wake up?").

---

### How This Graph Solves Problems:

* **Narrative Control:** The author has absolute control over the main story beats. The blackout *will* happen, but the context is shaped by the player.
* **Meaningful Agency:** The player's choice provides them with different information (`Key Info`). A player who went to the tower understands the *intent* behind the signal, while a player who stayed behind understands the *target* of the signal. This makes their knowledge unique and their choices feel impactful, even when the major plot points converge.
* **Constrained Generation:** The LLM is never asked to "write the story." It's given small, specific tasks like "describe the blackout" or "write a log entry," which dramatically increases reliability and cohesion.
