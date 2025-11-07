::SCENE::
LOCATION: Laboratory Entrance
MOOD: Mysterious
CHARACTERS: Kurisu, Player, Narrator
BACKGROUND_IMAGE: lab.jpg
BACKGROUND_EDIT: add mysterious blue lighting

::SCRIPT::
CHARACTER: Narrator
LINE: You stand at the entrance of a state-of-the-art laboratory. The air hums with the sound of advanced machinery.
EXPRESSION: null

CHARACTER: Kurisu
LINE: Welcome to Future Gadget Lab #8. I wasn't expecting visitors today.
EXPRESSION: neutral

CHARACTER: Player
LINE: I'm here about the time travel research. I heard you've made some breakthroughs.
EXPRESSION: null

CHARACTER: Kurisu
LINE: Time travel? That's... that's supposed to be classified. How did you find out about our work?
EXPRESSION: angry

CHARACTER: Narrator
LINE: Kurisu's eyes narrow with suspicion, her grip tightening on the lab reports she's carrying.
EXPRESSION: null

::PATHS::
CHOICE: Tell her the truth about being from the future
TARGET: laboratory_main_room
STATE_CHANGE: trust_kurisu = +1
CONDITION: null

CHOICE: Lie and say you're a government agent
TARGET: government_facility
STATE_CHANGE: deception = +1
CONDITION: null

CHOICE: Avoid the question and ask about her research instead
TARGET: research_laboratory
STATE_CHANGE: null
CONDITION: null

::SCENE::
LOCATION: Laboratory Main Room
MOOD: Tense
CHARACTERS: Kurisu, Player, Narrator
BACKGROUND_IMAGE: lab.jpg
BACKGROUND_EDIT: during evening with dramatic shadows

::SCRIPT::
CHARACTER: Player
LINE: I know this sounds impossible, but I'm from the year 2036. I came back to prevent a catastrophe.
EXPRESSION: null

CHARACTER: Kurisu
LINE: You're... you're serious, aren't you? The way you speak about our research, the details you know...
EXPRESSION: sad

CHARACTER: Narrator
LINE: Kurisu sets down her papers and studies you carefully, her scientific mind wrestling with the impossible.
EXPRESSION: null

CHARACTER: Kurisu
LINE: If what you're saying is true, then our experiments... they actually work? We succeed?
EXPRESSION: happy

CHARACTER: Player
LINE: Yes, but success comes with a terrible price. That's why I'm here - to change the timeline.
EXPRESSION: null

CHARACTER: Kurisu
LINE: Show me your proof. If you're really from the future, you'll know things about my research that no one else could.
EXPRESSION: angry

::PATHS::
CHOICE: Describe the PhoneWave experiment in detail
TARGET: secure_laboratory
STATE_CHANGE: kurisu_belief = +2
CONDITION: null

CHOICE: Warn her about the SERN conspiracy
TARGET: sern_facility
STATE_CHANGE: paranoia = +1
CONDITION: null

CHOICE: Tell her about her future Nobel Prize
TARGET: future_timeline
STATE_CHANGE: hope = +1
CONDITION: null

::SCENE::
LOCATION: Government Facility
MOOD: Dark
CHARACTERS: Agent_Smith, Kurisu, Player, Narrator
BACKGROUND_IMAGE: lab.jpg
BACKGROUND_EDIT: add government surveillance equipment

::SCRIPT::
CHARACTER: Player
LINE: Agent Johnson, Special Time Research Division. We've been monitoring your laboratory's activities.
EXPRESSION: null

CHARACTER: Kurisu
LINE: Government surveillance? I should have known... our research is too valuable to go unnoticed.
EXPRESSION: angry

CHARACTER: Narrator
LINE: An imposing figure in a black suit emerges from the shadows - Agent Smith, the division commander.
EXPRESSION: null

CHARACTER: Agent_Smith
LINE: Dr. Makise, your temporal research poses a threat to national security. We need full disclosure.
EXPRESSION: angry

CHARACTER: Kurisu
LINE: My research is purely theoretical! We haven't actually achieved time travel yet.
EXPRESSION: sad

CHARACTER: Agent_Smith
LINE: Yet? So you admit you're working toward that goal. This confirms our intelligence reports.
EXPRESSION: neutral

::PATHS::
CHOICE: Reveal you're actually from the future to protect Kurisu
TARGET: laboratory_main_room
STATE_CHANGE: heroic = +1
CONDITION: null

CHOICE: Continue the deception and demand to see their research
TARGET: research_laboratory
STATE_CHANGE: deception = +2
CONDITION: null

CHOICE: Try to escape with Kurisu
TARGET: future_timeline
STATE_CHANGE: trust_kurisu = +1
CONDITION: null

::SCENE::
LOCATION: Research Laboratory
MOOD: Focused
CHARACTERS: Kurisu, Player, Narrator
BACKGROUND_IMAGE: lab.jpg
BACKGROUND_EDIT: add complex equations on whiteboards

::SCRIPT::
CHARACTER: Player
LINE: Rather than dwelling on how I know, let's focus on your research. What have you discovered about temporal mechanics?
EXPRESSION: null

CHARACTER: Kurisu
LINE: Smart deflection... but fine. I'll humor you. We've been studying the properties of micro black holes.
EXPRESSION: neutral

CHARACTER: Narrator
LINE: Kurisu moves to a whiteboard covered in complex equations, her passion for science overriding her suspicion.
EXPRESSION: null

CHARACTER: Kurisu
LINE: The theory suggests that information can be transmitted backwards through time using quantum entanglement.
EXPRESSION: happy

CHARACTER: Player
LINE: The PhoneWave... you're talking about the PhoneWave experiment, aren't you?
EXPRESSION: null

CHARACTER: Kurisu
LINE: How could you possibly know about that? We haven't published anything about the PhoneWave prototype!
EXPRESSION: angry

::PATHS::
CHOICE: Admit you've seen the experiment work in the future
TARGET: laboratory_main_room
STATE_CHANGE: trust_kurisu = +1
CONDITION: null

CHOICE: Claim you deduced it from the equations
TARGET: secure_laboratory
STATE_CHANGE: intelligence = +1
CONDITION: null

CHOICE: Ask her to demonstrate the PhoneWave
TARGET: secure_laboratory
STATE_CHANGE: curiosity = +1
CONDITION: null

::SCENE::
LOCATION: Secure Laboratory
MOOD: Scientific
CHARACTERS: Kurisu, Player, Narrator
BACKGROUND_IMAGE: lab.jpg
BACKGROUND_EDIT: focus on the PhoneWave device with blue energy

::SCRIPT::
CHARACTER: Kurisu
LINE: The PhoneWave operates by creating a controlled singularity that affects local space-time.
EXPRESSION: happy

CHARACTER: Player
LINE: I know exactly how it works. You use a microwave to generate Kerr black holes, then modulate the message using the phone as a transmitter.
EXPRESSION: null

CHARACTER: Kurisu
LINE: That's... that's exactly right. But those specifications are classified. No one outside our lab should know this!
EXPRESSION: angry

CHARACTER: Narrator
LINE: The PhoneWave device hums to life, its display showing temporal displacement readings.
EXPRESSION: null

CHARACTER: Kurisu
LINE: You've proven you know our research, but knowledge and time travel are very different things. Show me real proof.
EXPRESSION: neutral

CHARACTER: Player
LINE: Send a message to yourself one hour in the past. Tell past-Kurisu to check her lab coat pocket.
EXPRESSION: null

::PATHS::
CHOICE: Put a coin in her pocket before she sends the message
TARGET: future_timeline
STATE_CHANGE: time_proof = +2
CONDITION: null

CHOICE: Have her send lottery numbers from tomorrow's drawing
TARGET: sern_facility
STATE_CHANGE: temporal_knowledge = +1
CONDITION: null

CHOICE: Warn past-Kurisu about a "random" accident you'll cause
TARGET: laboratory_main_room
STATE_CHANGE: demonstration = +1
CONDITION: null

::SCENE::
LOCATION: SERN Facility
MOOD: Ominous
CHARACTERS: Kurisu, SERN_Director, Player, Narrator
BACKGROUND_IMAGE: lab.jpg
BACKGROUND_EDIT: add SERN logos and surveillance cameras

::SCRIPT::
CHARACTER: Player
LINE: Kurisu, we need to talk about SERN. They're not the research organization they claim to be.
EXPRESSION: null

CHARACTER: Kurisu
LINE: SERN? The European research council? They've been funding some of our theoretical work...
EXPRESSION: neutral

CHARACTER: Narrator
LINE: Suddenly, the laboratory doors burst open. Armed personnel in SERN uniforms flood in.
EXPRESSION: null

CHARACTER: SERN_Director
LINE: Dr. Makise, you've been developing unauthorized time travel technology. This research now belongs to SERN.
EXPRESSION: angry

CHARACTER: Kurisu
LINE: What? This is impossible! Our funding came with no strings attached!
EXPRESSION: sad

CHARACTER: SERN_Director
LINE: Naive scientist. SERN has been manipulating timeline research for decades. Your work is just another piece of the puzzle.
EXPRESSION: neutral

::PATHS::
CHOICE: Fight back against SERN with Kurisu
TARGET: future_timeline
STATE_CHANGE: rebellion = +1
CONDITION: null

CHOICE: Try to negotiate with the SERN Director
TARGET: research_laboratory
STATE_CHANGE: diplomacy = +1
CONDITION: null

CHOICE: Use the PhoneWave to send a warning to the past
TARGET: laboratory_entrance
STATE_CHANGE: temporal_mastery = +1
CONDITION: null

::SCENE::
LOCATION: Future Timeline
MOOD: Hopeful
CHARACTERS: Kurisu, Player, Narrator
BACKGROUND_IMAGE: lab.jpg
BACKGROUND_EDIT: add futuristic technology and Nobel Prize certificate

::SCRIPT::
CHARACTER: Player
LINE: In the future, your research revolutionizes physics. You win the Nobel Prize in 2029.
EXPRESSION: null

CHARACTER: Kurisu
LINE: Nobel Prize? Me? That's... that's been my dream since I was a child studying physics.
EXPRESSION: happy

CHARACTER: Narrator
LINE: Kurisu's eyes light up with wonder and ambition, seeing a glimpse of her potential future.
EXPRESSION: null

CHARACTER: Kurisu
LINE: But if you're here to change the timeline, does that mean my future achievements are in danger?
EXPRESSION: sad

CHARACTER: Player
LINE: Not in danger - they're why I came back. Your discoveries are crucial for preventing the catastrophe.
EXPRESSION: null

CHARACTER: Kurisu
LINE: Then we need to work together. Show me exactly what timeline changes are necessary.
EXPRESSION: neutral

::PATHS::
CHOICE: Explain the dystopian future timeline
TARGET: sern_facility
STATE_CHANGE: knowledge_burden = +1
CONDITION: null

CHOICE: Focus on preserving her Nobel Prize work
TARGET: secure_laboratory
STATE_CHANGE: motivation = +1
CONDITION: null

CHOICE: Propose working together to create a better future
TARGET: laboratory_entrance
STATE_CHANGE: partnership = +2
CONDITION: null