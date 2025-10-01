::SCENE::
LOCATION: Sometime in the Future
MOOD: Eerie
CHARACTERS: Narrator
BACKGROUND_IMAGE: future_engine_room.png
BACKGROUND_EDIT: "Empty, cavernous engine room"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Empty, cavernous.
  EXPRESSION: null

::PATHS::
- CHOICE: Continue
  TARGET: engine_cubicle
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Engine Cubicle
MOOD: Empty
CHARACTERS: Narrator
BACKGROUND_IMAGE: engine_cubicle.png
BACKGROUND_EDIT: "Circular room, jammed with idle instruments, console chairs for two"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Circular, jammed with instruments. All of them idle. Console chairs for two. Empty.
  EXPRESSION: null

::PATHS::
- CHOICE: Continue
  TARGET: oily_corridor
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Oily Corridor - "C" Level
MOOD: Dark
CHARACTERS: Narrator
BACKGROUND_IMAGE: oily_corridor.png
BACKGROUND_EDIT: "Long, dark, empty corridor with throbbing turbos"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Long, dark. Empty. Turbos throbbing. No other movement.
  EXPRESSION: null

::PATHS::
- CHOICE: Continue
  TARGET: corridor_a_level
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Corridor - "A" Level
MOOD: Empty
CHARACTERS: Narrator
BACKGROUND_IMAGE: corridor_a_level.png
BACKGROUND_EDIT: "Long, empty corridor"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Long, empty.
  EXPRESSION: null

::PATHS::
- CHOICE: Continue
  TARGET: infirmary_a_level
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Infirmary - "A" Level
MOOD: Still
CHARACTERS: Narrator
BACKGROUND_IMAGE: infirmary_a_level.png
BACKGROUND_EDIT: "Distressed ivory walls, all instrumentation at rest"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Distressed ivory walls. All instrumentation at rest.
  EXPRESSION: null

::PATHS::
- CHOICE: Continue
  TARGET: corridor_to_bridge
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Corridor to Bridge - "A" Level
MOOD: Dark
CHARACTERS: Narrator
BACKGROUND_IMAGE: corridor_to_bridge.png
BACKGROUND_EDIT: "Black, empty corridor"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Black, empty.
  EXPRESSION: null

::PATHS::
- CHOICE: Continue
  TARGET: bridge
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Bridge
MOOD: Quiet
CHARACTERS: Narrator
BACKGROUND_IMAGE: bridge.png
BACKGROUND_EDIT: "Vacant bridge with two space helmets resting on chairs"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Vacant. Two space helmets resting on chairs.
  EXPRESSION: null

::PATHS::
- CHOICE: Observe
  TARGET: bridge_lights
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Bridge - Lights
MOOD: Waiting
CHARACTERS: Narrator
BACKGROUND_IMAGE: bridge_lights.png
BACKGROUND_EDIT: "Bridge with electrical hum, lights on helmets signaling"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Electrical hum. Lights on the helmets begin to signal one another. Moments of silence.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: A yellow light goes on. Data mind bank in b.g. Electronic hum.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: A green light goes on in front of one helmet. Electronic pulsing sounds.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: A red light goes on in front of other helmet. An electronic conversation ensues. Reaches a crescendo. Then silence. The lights go off, save the yellow.
  EXPRESSION: null

::PATHS::
- CHOICE: Continue
  TARGET: corridor_to_hypersleep
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Corridor to Hypersleep Vault
MOOD: Awaken
CHARACTERS: Narrator
BACKGROUND_IMAGE: hypersleep_corridor.png
BACKGROUND_EDIT: "Corridor with lights coming on, seven gowns hanging, vault door opening"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Lights come on. Seven gowns hang from the curved wall. Vault door opens.
  EXPRESSION: null

::PATHS::
- CHOICE: Enter Vault
  TARGET: hypersleep_vault_kane
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Hypersleep Vault
MOOD: Waking
CHARACTERS: Kane, Narrator
BACKGROUND_IMAGE: hypersleep_vault_kane.png
BACKGROUND_EDIT: "Vault with explosion of escaping gas, lid on a freezer pons open"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Explosion of escaping gas. The lid on a freezer pons open.
  EXPRESSION: null
- CHARACTER: Kane
  LINE: Slowly, groggily, Kane sits up. Pale.
  EXPRESSION: Tired
- CHARACTER: Kane
  LINE: Kane rubs the sleep from his eyes. Stands. Looks around. Stretches.
  EXPRESSION: Groggy
- CHARACTER: Kane
  LINE: Looks at the other freezer compartments. Scratches. Moves off.
  EXPRESSION: Curious

::PATHS::
- CHOICE: Go to Galley
  TARGET: galley_kane
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Galley
MOOD: Routine
CHARACTERS: Kane, Narrator
BACKGROUND_IMAGE: galley_kane.png
BACKGROUND_EDIT: "Galley where Kane plugs in a Silex, lights a cigarette"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Kane plugs in a Silex. Lights a cigarette.
  EXPRESSION: null
- CHARACTER: Kane
  LINE: Coughs. Grinds some coffee beans. Runs some water through.
  EXPRESSION: Unwell
- CHARACTER: Kane
  LINE: Rise and shine, Lambert.
  EXPRESSION: Casual

::PATHS::
- CHOICE: Call Lambert
  TARGET: hypersleep_vault_lambert
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Hypersleep Vault
MOOD: Awakening
CHARACTERS: Lambert, Kane (voice over), Narrator
BACKGROUND_IMAGE: hypersleep_vault_lambert.png
BACKGROUND_EDIT: "Vault with another lid popping open"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Another lid pops open.
  EXPRESSION: null
- CHARACTER: Lambert
  LINE: What time is it.
  EXPRESSION: Sleepy
- CHARACTER: Kane
  LINE: (voice over)
  What do you care.
  EXPRESSION: Cynical

::PATHS::
- CHOICE: Return to Galley
  TARGET: galley_lambert
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Galley
MOOD: Anticipation
CHARACTERS: Kane, Dallas (voice over), Lambert, Narrator
BACKGROUND_IMAGE: galley_lambert.png
BACKGROUND_EDIT: "Galley with pot of coffee brewing, Lambert pouring a cup"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Pot now half-full. Kane watches it drip. Inhales the fragrance.
  EXPRESSION: null
- CHARACTER: Kane
  LINE: Now Dallas and Ash. Good morning Captain.
  EXPRESSION: Casual
- CHARACTER: Dallas
  LINE: (voice over)
  Where’s the coffee.
  EXPRESSION: Demanding
- CHARACTER: Kane
  LINE: Brewing.
  EXPRESSION: Casual
- CHARACTER: Lambert
  LINE: Walks into the kitchen. Pours herself a cup.
  EXPRESSION: Thirsty

::PATHS::
- CHOICE: Wake Dallas and Ash
  TARGET: hypersleep_vault_dallas_ash
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Hypersleep Vault
MOOD: Awakening
CHARACTERS: Narrator
BACKGROUND_IMAGE: hypersleep_vault_dallas_ash.png
BACKGROUND_EDIT: "Vault with two more lids popping open"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Two more lids pop open. A pair of men sit up. Look at each other.
  EXPRESSION: null

::PATHS::
- CHOICE: Return to Galley
  TARGET: galley_dallas_ash
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Galley
MOOD: Waking Crew
CHARACTERS: Kane, Ripley, Parker, Brett, Narrator
BACKGROUND_IMAGE: galley_dallas_ash.png
BACKGROUND_EDIT: "Galley where Kane is enjoying coffee, calling out names"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Kane enjoys a freshly-brewed cup.
  EXPRESSION: Relaxed
- CHARACTER: Kane
  LINE: Ripley --
  EXPRESSION: Casual
- CHARACTER: Narrator
  LINE: The sound of another lid opening.
  EXPRESSION: null
- CHARACTER: Kane
  LINE: Parker.
  EXPRESSION: Casual
- CHARACTER: Narrator
  LINE: Another moment. And then the sound of another lid opening.
  EXPRESSION: null
- CHARACTER: Kane
  LINE: And if we have Parker, can Brett be far behind.
  EXPRESSION: Casual
- CHARACTER: Narrator
  LINE: Lid opening sound.
  EXPRESSION: null
- CHARACTER: Kane
  LINE: Right.
  EXPRESSION: Casual

::PATHS::
- CHOICE: Observe Hypersleep Vault
  TARGET: hypersleep_vault_ripley_parker_brett
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Hypersleep Vault
MOOD: Waking Up
CHARACTERS: Dallas, Narrator
BACKGROUND_IMAGE: hypersleep_vault_ripley_parker_brett.png
BACKGROUND_EDIT: "Vault with Dallas looking at his groggy crew, Ripley picking up a cat"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Dallas looks at his groggy circus.
  EXPRESSION: null
- CHARACTER: Dallas
  LINE: One of you jokers get the cat.
  EXPRESSION: Annoyed
- CHARACTER: Narrator
  LINE: Ripley picks a limp cat out of one of the compartments.
  EXPRESSION: null

::PATHS::
- CHOICE: Go to Mess
  TARGET: mess_hall
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Mess Hall
MOOD: Morning Briefing
CHARACTERS: Narrator, Dallas, Kane, Ripley, Ash, Lambert, Parker, Brett, Jones (Cat)
BACKGROUND_IMAGE: mess_hall.png
BACKGROUND_EDIT: "Crew of the Nostromo seated around a table"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The crew of the United States commercial, starship Nostromo seated around a table. Dallas - Captain, Kane - Executive, Ripley - Warrant Officer, Ash - Science Officer, Lambert - Navigator, Parker - Engineer, Brett - Engineering Technician, Jones - Cat. Five men and two women: Lambert and Ripley.
  EXPRESSION: null
- CHARACTER: Lambert
  LINE: Jesus am I cold.
  EXPRESSION: Cold
- CHARACTER: Parker
  LINE: Still with us, Brett.
  EXPRESSION: Casual
- CHARACTER: Brett
  LINE: Yo.
  EXPRESSION: Casual
- CHARACTER: Ripley
  LINE: Lucky us.
  EXPRESSION: Sarcastic
- CHARACTER: Narrator
  LINE: They yawn, stretch, shiver.
  EXPRESSION:null
- CHARACTER: Dallas
  LINE: Looks over at a flashing yellow light.
  EXPRESSION: Alert
- CHARACTER: Kane
  LINE: I feel dead. Kane is not yet fully awake. Yawns.
  EXPRESSION: Tired
- CHARACTER: Parker
  LINE: You look dead.
  EXPRESSION: Blunt
- CHARACTER: Ash
  LINE: Nice to be back.
  EXPRESSION: Polite
- CHARACTER: Parker
  LINE: Before we dock maybe we’d better go over the bonus situation.
  EXPRESSION: Concerned
- CHARACTER: Brett
  LINE: Yeah.
  EXPRESSION: Agreeing
- CHARACTER: Parker
  LINE: Brett and I think we deserve a full share.
  EXPRESSION: Assertive
- CHARACTER: Dallas
  LINE: You two will get what you contracted for. Just like everybody else.
  EXPRESSION: Firm
- CHARACTER: Brett
  LINE: Everybody else gets more than us.
  EXPRESSION: Complaining
- CHARACTER: Dallas
  LINE: Everybody else deserves more than you two.
  EXPRESSION: Dismissive
- CHARACTER: Ash
  LINE: Mother wants to talk to you.
  EXPRESSION: Informative
- CHARACTER: Dallas
  LINE: I saw it. Yellow light for my eyes only -- Now, everybody hit their stations.
  EXPRESSION: Authoritative

::PATHS::
- CHOICE: Go to Computer Room Annex
  TARGET: computer_room_annex
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Computer Room Annex
MOOD: Alert
CHARACTERS: Narrator, Dallas
BACKGROUND_IMAGE: computer_room_annex.png
BACKGROUND_EDIT: "Floor to ceiling data banks, flashing yellow light"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Floor to ceiling data banks. Another flashing yellow light.
  EXPRESSION: null
- CHARACTER: Dallas
  LINE: Dallas enters. Runs through access procedure. Inner door opens. Dallas moves to the console chair. Sits.
  EXPRESSION: Determined
- CHARACTER: Dallas
  LINE: Dallas punches the keyboard.
  EXPRESSION: Focused
- CHARACTER: Narrator
  LINE: Legend on the screen: ALERT OVER MONITORING FUNCTION FOR MATRIX DISPLAY AND INQUIRY. Mother prints out: OVERMONITOR ADDRESS MATRIX (columns of categories beneath).
  EXPRESSION: null
- CHARACTER: Dallas
  LINE: Picks one and types out: COMMAND PRIORITY ALERT.
  EXPRESSION: Decisive
- CHARACTER: Narrator
  LINE: Mother replies: OVERMONITOR FUNCTION READY FOR INQUIRY.
  EXPRESSION: null
- CHARACTER: Dallas
  LINE: WHAT’S THE STORY MOTHER.
  EXPRESSION: Inquisitive

::PATHS::
- CHOICE: Go to Bridge
  TARGET: bridge_crew
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Bridge
MOOD: Active
CHARACTERS: Narrator, Kane, Ripley, Lambert, Ash, Dallas
BACKGROUND_IMAGE: bridge_crew.png
BACKGROUND_EDIT: "Bridge rigged by view screens, crew finding their way to consoles"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Above eye level the room is rigged by view screens. All of them blank. Kane, Ripley, Lambert and Ash enter. Dallas seat remains empty. All of them now dressed; they find their way to individual consoles.
  EXPRESSION: null
- CHARACTER: Ripley
  LINE: Puts down the cat, straps herself into the high-backed chair.
  EXPRESSION: Professional
- CHARACTER: Kane
  LINE: Plug us in.
  EXPRESSION: Commanding
- CHARACTER: Narrator
  LINE: All three crew members begin throwing switches. The control room starts to come to life. Colored lights flicker. Chase each other across glowing screens.
  EXPRESSION: null
- CHARACTER: Kane
  LINE: Give us something to look at.
  EXPRESSION: Impatient
- CHARACTER: Lambert
  LINE: Presses a bank of switches. View screens glimmer into life.
  EXPRESSION: Focused
- CHARACTER: Lambert
  LINE: Take a look at this.
  EXPRESSION: Surprised
- CHARACTER: Narrator
  LINE: On each screen, blackness speckled with stars.
  EXPRESSION: null
- CHARACTER: Lambert
  LINE: Where’s Earth.
  EXPRESSION: Confused
- CHARACTER: Kane
  LINE: You’re the navigator.
  EXPRESSION: Annoyed
- CHARACTER: Ripley
  LINE: That’s not our system.
  EXPRESSION: Concerned
- CHARACTER: Kane
  LINE: Scan.
  EXPRESSION: Imperative
- CHARACTER: Lambert
  LINE: Hits.
  EXPRESSION: Resolute

::SCENE::
LOCATION: Unknown
MOOD: Mysterious
CHARACTERS: Narrator
BACKGROUND_IMAGE: starfield_screens.png
BACKGROUND_EDIT: "Screens showing drifting images of a starfield"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Several toggles. On the screens the images begin to drift.
  EXPRESSION: null

::SCENE::
LOCATION: Nostromo Exterior
MOOD: Vastness, Industrial
CHARACTERS: Narrator
BACKGROUND_IMAGE: nostromo_exterior.png
BACKGROUND_EDIT: "The Factory Starship lumbering within the depths of interstellar space, battered exterior encrusted with dark sludge"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Function: Petroleum tanker and Refinery. Capacity: 2000,000,000 tons. Length: One and one half kilometers.
  EXPRESSION: null

::SCENE::
LOCATION: Bridge
MOOD: Puzzled, Tense
CHARACTERS: Narrator, Lambert, Kane, Ripley
BACKGROUND_IMAGE: bridge.png
BACKGROUND_EDIT: "The bridge of the Nostromo, dim lighting"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Lambert pores over charts. Consults her console. Puzzled.
  EXPRESSION: null
- CHARACTER: Kane
  LINE: Contact traffic control.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Ripley switches on her transmission unit.
  EXPRESSION: null
- CHARACTER: Ripley
  LINE: This is commercial vessel Nostromo out of Houston. Registration number 180246, calling Antarctica Traffic Control. Do you read me? Over.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Nothing but the hiss of static.
  EXPRESSION: null
- CHARACTER: Ripley
  LINE: Nothing.
  EXPRESSION: null
- CHARACTER: Kane
  LINE: Keep trying.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Turns to Lambert. Ripley attempting transmission in b.g.
  EXPRESSION: null
- CHARACTER: Kane
  LINE: You got a reading yet.
  EXPRESSION: null
- CHARACTER: Lambert
  LINE: We’re way out in the boondocks here.
  EXPRESSION: null
- CHARACTER: Kane
  LINE: Keep trying.
  EXPRESSION: null
- CHARACTER: Lambert
  LINE: Working on it. Eureka.
  EXPRESSION: null
- CHARACTER: Lambert
  LINE: Found it. Just short of Zeta II Reticuli. We haven’t even reached the outer rim yet.
  EXPRESSION: null
- CHARACTER: Kane
  LINE: Hard to believe.
  EXPRESSION: null
- CHARACTER: Lambert
  LINE: What the hell are we doing out here.
  EXPRESSION: null
- CHARACTER: Kane
  LINE: What are you talking about.
  EXPRESSION: null
- CHARACTER: Ripley
  LINE: It’s not our system.
  EXPRESSION: null

::SCENE::
LOCATION: Engine Room
MOOD: Calm, Powerful
CHARACTERS: Narrator
BACKGROUND_IMAGE: engine_room.png
BACKGROUND_EDIT: "Giant reactor system purring smoothly"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Giant reactor system purring smoothly.
  EXPRESSION: null

::SCENE::
LOCATION: Engine Room Cubicle
MOOD: Relaxed, Ordinary
CHARACTERS: Narrator, Parker, Brett
BACKGROUND_IMAGE: engine_room_cubicle.png
BACKGROUND_EDIT: "Parker and Brett in a glass cubicle, huge power-plant stretching before them, all units on automatic hyper-drive"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Parker and Brett in a glass cubicle. Each having a beer. Huge power-plant stretching before them. All units on automatic hyper-drive.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Parker hits a switch above his desk. A green light goes on.
  EXPRESSION: null
- CHARACTER: Parker
  LINE: How’s your light.
  EXPRESSION: null
- CHARACTER: Brett
  LINE: Green.
  EXPRESSION: null
- CHARACTER: Parker
  LINE: Mine too.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: They both take a swig. Suddenly the beeper signal begins.
  EXPRESSION: null
- CHARACTER: Parker
  LINE: Christ. What is it now.
  EXPRESSION: Annoyed
- CHARACTER: Brett
  LINE: Right.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Ripley (voice over)
  LINE: Report to the mess.
  EXPRESSION: null

::SCENE::
LOCATION: Oily Corridor "C" Level
MOOD: Resentful, Moving
CHARACTERS: Narrator, Parker, Brett
BACKGROUND_IMAGE: oily_corridor.png
BACKGROUND_EDIT: "An oily corridor, industrial, dark"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Parker
  LINE: I want to know why they never come down here. This is where the work is.
  EXPRESSION: Resentful
- CHARACTER: Brett
  LINE: Same reason we have half a share to their one, our time is their time, that’s the way they see it.
  EXPRESSION: Resigned
- CHARACTER: Parker
  LINE: Well, I’ll tell you something -- it stinks.
  EXPRESSION: Angry
- CHARACTER: Narrator
  LINE: They move towards the companionway, leading up to "B" level.
  EXPRESSION: null

::SCENE::
LOCATION: Mess
MOOD: Serious, Informative
CHARACTERS: Narrator, Dallas, Brett, Kane, Mother (implied), Ripley, Lambert, Ash, Parker
BACKGROUND_IMAGE: mess.png
BACKGROUND_EDIT: "The mess hall of the Nostromo, the entire crew present"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Entire crew present.
  EXPRESSION: null
- CHARACTER: Dallas
  LINE: Some of you may have figured out that we're not home. We're only halfway back to Earth.
  EXPRESSION: Serious
- CHARACTER: Brett
  LINE: What the hell.
  EXPRESSION: Shocked
- CHARACTER: Dallas
  LINE: Mother's interrupted the course of the voyage.
  EXPRESSION: Serious
- CHARACTER: Kane
  LINE: Why?
  EXPRESSION: Confused
- CHARACTER: Dallas
  LINE: She's programmed to do that if certain conditions arise. They have.
  EXPRESSION: Serious
- CHARACTER: Narrator
  LINE: Pause.
  EXPRESSION: null
- CHARACTER: Dallas
  LINE: Seems Mother intercepted a transmission of unknown origin. She got us up to check it out.
  EXPRESSION: Serious
- CHARACTER: Ripley
  LINE: Transmission? Out here?
  EXPRESSION: Skeptical
- CHARACTER: Lambert
  LINE: What kind of transmission?
  EXPRESSION: Curious
- CHARACTER: Dallas
  LINE: An acoustic beacon. It repeats at intervals of 12 seconds.
  EXPRESSION: Serious
- CHARACTER: Kane
  LINE: Is it an S.O.S?
  EXPRESSION: Hopeful
- CHARACTER: Dallas
  LINE: Unknown.
  EXPRESSION: Serious
- CHARACTER: Ripley
  LINE: Human.
  EXPRESSION: Hopeful
- CHARACTER: Dallas
  LINE: Unknown.
  EXPRESSION: Serious
- CHARACTER: Brett
  LINE: So what.
  EXPRESSION: Indifferent
- CHARACTER: Kane
  LINE: We're obligated under Section B2 --
  EXPRESSION: Legalistic
- CHARACTER: Parker
  LINE: Christ. I hate to say this but we’re a commercial ship not a rescue team. This kind of duty’s not in our contract -- but if it’s for some money --
  EXPRESSION: Greedy
- CHARACTER: Ash
  LINE: You better read your contract. Any systematized transmission indicating possible intelligent origin must be investigated. At penalty of total forfeiture.
  EXPRESSION: Authoritative
- CHARACTER: Narrator
  LINE: Dallas gives Parker and Brett a look.
  EXPRESSION: null
- CHARACTER: Dallas
  LINE: We’re going in, that’s it.
  EXPRESSION: Decisive
- CHARACTER: Narrator
  LINE: Brett knows when to ease up.
  EXPRESSION: null
- CHARACTER: Brett
  LINE: Right, we’re going in. (smiles) Sir.
  EXPRESSION: Obedient
- CHARACTER: Narrator
  LINE: Dallas turns to Ash.
  EXPRESSION: null
- CHARACTER: Dallas
  LINE: Can we land on it.
  EXPRESSION: Curious
- CHARACTER: Ash
  LINE: Somebody did.
  EXPRESSION: Informative
- CHARACTER: Dallas
  LINE: That’s what I mean.
  EXPRESSION: Assertive

::SCENE::
LOCATION: Bridge
MOOD: Focused, Anticipatory
CHARACTERS: Narrator, Dallas, Kane, Ripley, Ash, Lambert
BACKGROUND_IMAGE: bridge_map.png
BACKGROUND_EDIT: "Dallas, Kane, Ripley and Ash stand around the illuminated map table. Lambert sits at the radio directional console."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Dallas, Kane, Ripley and Ash stand around the illuminated map table. Lambert sits at the radio directional console.
  EXPRESSION: null
- CHARACTER: Dallas
  LINE: Okay. Let’s all hear it.
  EXPRESSION: Directing
- CHARACTER: Narrator
  LINE: Nods at Lambert. She switches on the audio system.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Hissing. Static. Then -- An ungodly sound. Eight seconds worth.
  EXPRESSION: Disturbing
- CHARACTER: Kane
  LINE: Good God.
  EXPRESSION: Horrified
- CHARACTER: Narrator
  LINE: Static. Lambert switches off the loudspeakers.
  EXPRESSION: null
- CHARACTER: Ripley
  LINE: What the hell is it. It doesn’t sound like any radio signal I’ve ever heard.
  EXPRESSION: Alarmed
- CHARACTER: Lambert
  LINE: Maybe it’s a voice.
  EXPRESSION: Eerie
- CHARACTER: Narrator
  LINE: Disturbing moment.
  EXPRESSION: null
- CHARACTER: Dallas
  LINE: We’ll know soon. (looks at Lambert) Have you homed in on it.
  EXPRESSION: Determined
- CHARACTER: Lambert
  LINE: I've found the quadrant. We’re close. It’s coming from ascension 6 minutes 20 seconds, declination minus 39 degrees 2 seconds.
  EXPRESSION: Precise
- CHARACTER: Dallas
  LINE: Show me that on a screen.
  EXPRESSION: Demanding
- CHARACTER: Narrator
  LINE: Lambert punches buttons. One of the view screens flickers, and a small dot of light appears.
  EXPRESSION: null
- CHARACTER: Dallas
  LINE: Can you get it a little closer.
  EXPRESSION: Impatient
- CHARACTER: Lambert
  LINE: No, you have to look at it from this distance. That’s what I'm going to do.
  EXPRESSION: Sarcastic
- CHARACTER: Narrator
  LINE: The screen zooms to a small planetoid.
  EXPRESSION: null
- CHARACTER: Dallas
  LINE: Smart ass.
  EXPRESSION: Annoyed
- CHARACTER: Lambert
  LINE: That's it. Planetoid. Diameter 1200 kilometers.
  EXPRESSION: Factual
- CHARACTER: Kane
  LINE: Tiny.
  EXPRESSION: Underwhelmed
- CHARACTER: Dallas
  LINE: Any rotation.
  EXPRESSION: Inquisitive
- CHARACTER: Lambert
  LINE: Yeah. 'Bout two hours.
  EXPRESSION: Factual
- CHARACTER: Dallas
  LINE: Gravity?
  EXPRESSION: Inquisitive
- CHARACTER: Lambert
  LINE: Point eight six.
  EXPRESSION: Factual
- CHARACTER: Ash
  LINE: You can walk on it --
  EXPRESSION: Informative

::SCENE::
LOCATION: Nostromo Exterior
MOOD: Approaching
CHARACTERS: Narrator, Lambert (voice over), Kane (voice over)
BACKGROUND_IMAGE: nostromo_planetoid.png
BACKGROUND_EDIT: "The factory ship moving within range of the planetoid"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Moving within range of the planet.
  EXPRESSION: null
- CHARACTER: Lambert (voice over)
  LINE: Approaching orbital apogee. Mark. 20 seconds. Nineteen. Eighteen --
  EXPRESSION: Counting down
- CHARACTER: Narrator
  LINE: Continues to count down.
  EXPRESSION: null
- CHARACTER: Kane (voice over)
  LINE: Roll 92 degrees starboard yaw.
  EXPRESSION: Commanding
- CHARACTER: Narrator
  LINE: High above the planet. The factory ship rotates. Engines fire briefly.
  EXPRESSION: null

::SCENE::
LOCATION: Bridge
MOOD: Achieved Orbit
CHARACTERS: Narrator, Ash
BACKGROUND_IMAGE: bridge_orbit.png
BACKGROUND_EDIT: "The bridge of the Nostromo"

::SCRIPT::
- CHARACTER: Ash
  LINE: Equatorial orbit nailed.
  EXPRESSION: Triumphant

::SCENE::
LOCATION: Nostromo Exterior
MOOD: Close Orbit
CHARACTERS: Narrator
BACKGROUND_IMAGE: nostromo_planetoid_close.png
BACKGROUND_EDIT: "The Nostromo now within close orbit of the planetoid"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Now within the
  EXPRESSION: null

::SCENE::
LOCATION: EXT. SPACE
MOOD: Majestic
CHARACTERS: Narrator
BACKGROUND_IMAGE: space_planet.png
BACKGROUND_EDIT: "A planet is visible from space, rolling beneath the viewer. The camera is focused on the planet's orbit."

::SCRIPT::
- CHARACTER: Narrator
  LINE: planet’s orbit.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The planet rolling by underneath.
  EXPRESSION: null

::SCENE::
LOCATION: INT. BRIDGE
MOOD: Tense
CHARACTERS: Dallas, Ash
BACKGROUND_IMAGE: bridge_day.png
BACKGROUND_EDIT: "The bridge of a spaceship, with various readouts and controls visible."

::SCRIPT::
- CHARACTER: DALLAS
  LINE: Give me an EC Pressure reading.
  EXPRESSION: Concerned
- CHARACTER: ASH
  LINE: З.45 n/c m (5 psia).
  EXPRESSION: Informative
- CHARACTER: DALLAS
  LINE: Shout if it changes.
  EXPRESSION: Stern
- CHARACTER: ASH
  LINE: You worried about redundancy management disabling CMGS control.
  EXPRESSION: Questioning
- CHARACTER: DALLAS
  LINE: Yeah.
  EXPRESSION: Affirmative
- CHARACTER: ASH
  LINE: CMG control is inhibited via DAS/DCS. We'll augment with TACS and monitor through ATMDC and computer interface. Feel better?
  EXPRESSION: Reassuring
- CHARACTER: DALLAS
  LINE: A lot. Prepare to disengage from platform.
  EXPRESSION: Relieved

::SCENE::
LOCATION: INT. ENGINE ROOM CUBICLE
MOOD: Procedural
CHARACTERS: Parker, Brett
BACKGROUND_IMAGE: engine_room_cubicle_day.png
BACKGROUND_EDIT: "A cramped engine room cubicle with equipment and consoles."

::SCRIPT::
- CHARACTER: PARKER
  LINE: L alignment on port and starboard is green.
  EXPRESSION: Professional
- CHARACTER: BRETT
  LINE: Green on spinal umbilicus severance.
  EXPRESSION: Professional

::SCENE::
LOCATION: INT. BRIDGE
MOOD: Observational
CHARACTERS: Lambert
BACKGROUND_IMAGE: bridge_day.png
BACKGROUND_EDIT: "The bridge of a spaceship, with various readouts and controls visible."

::SCRIPT::
- CHARACTER: LAMBERT
  LINE: Crossing the terminator. Entering night side.
  EXPRESSION: Observational

::SCENE::
LOCATION: EXT. NOSTROMO
MOOD: Transition
CHARACTERS: Narrator
BACKGROUND_IMAGE: nostromo_night_side.png
BACKGROUND_EDIT: "The Nostromo spacecraft as it enters the night side of a planet."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Below, night’s curtain rolls across the sphere’s surface.
  EXPRESSION: null

::SCENE::
LOCATION: INT. BRIDGE
MOOD: Urgent
CHARACTERS: Lambert, Dallas
BACKGROUND_IMAGE: bridge_day.png
BACKGROUND_EDIT: "The bridge of a spaceship, with various readouts and controls visible."

::SCRIPT::
- CHARACTER: LAMBERT
  LINE: It’s coming up. It’s coming up. Stand by. Stand by. Fifteen seconds. Ten...Five. Four. Three. Two. One. Lock.
  EXPRESSION: Urgent
- CHARACTER: DALLAS
  LINE: Disengage.
  EXPRESSION: Command

::SCENE::
LOCATION: EXT. NOSTROMO
MOOD: Action
CHARACTERS: Narrator
BACKGROUND_IMAGE: nostromo_disengaging.png
BACKGROUND_EDIT: "The Nostromo tug detaches from a space platform."

::SCRIPT::
- CHARACTER: Narrator
  LINE: The tug disengages from the platform.
  EXPRESSION: null

::SCENE::
LOCATION: INT. BRIDGE
MOOD: Vigilant
CHARACTERS: Dallas, Ripley, Kane
BACKGROUND_IMAGE: bridge_day.png
BACKGROUND_EDIT: "The bridge of a spaceship, with various readouts and controls visible."

::SCRIPT::
- CHARACTER: DALLAS
  LINE: Dallas watches the refinery moving away on a view screen.
  EXPRESSION: Focused
- CHARACTER: RIPLEY
  LINE: Umbilius clear.
  EXPRESSION: Informative
- CHARACTER: KANE
  LINE: Precession corrected.
  EXPRESSION: Informative
- CHARACTER: DALLAS
  LINE: Okay. The money’s safe. Let’s take it down.
  EXPRESSION: Decisive

::SCENE::
LOCATION: EXT. NOSTROMO
MOOD: Descent
CHARACTERS: Narrator
BACKGROUND_IMAGE: nostromo_descent.png
BACKGROUND_EDIT: "The Nostromo tug begins its descent towards a dark planet surface."

::SCRIPT::
- CHARACTER: Narrator
  LINE: The tug begins its arc toward the dark surface.
  EXPRESSION: null

::SCENE::
LOCATION: INT. BRIDGE
MOOD: Descending
CHARACTERS: Lambert, Jones
BACKGROUND_IMAGE: bridge_day.png
BACKGROUND_EDIT: "The bridge of a spaceship, with various readouts and controls visible."

::SCRIPT::
- CHARACTER: LAMBERT
  LINE: Dropping. 50/000 meters. Down. Down. 49.000 meters. Entering atmosphere.
  EXPRESSION: Focused
- CHARACTER: Narrator
  LINE: Jones sits on window platform and watches cloud approaching.
  EXPRESSION: null

::SCENE::
LOCATION: EXT. NOSTROMO
MOOD: Entering Atmosphere
CHARACTERS: Narrator
BACKGROUND_IMAGE: nostromo_entering_clouds.png
BACKGROUND_EDIT: "The Nostromo ship descends into a thick cloud layer on a planet."

::SCRIPT::
- CHARACTER: Narrator
  LINE: The ship drops into the thick cloud layer.
  EXPRESSION: null

::SCENE::
LOCATION: INT. BRIDGE
MOOD: Turbulent
CHARACTERS: Ripley, Dallas
BACKGROUND_IMAGE: bridge_day.png
BACKGROUND_EDIT: "The bridge of a spaceship, with various readouts and controls visible."

::SCRIPT::
- CHARACTER: RIPLEY
  LINE: Turbulence.
  EXPRESSION: Concerned
- CHARACTER: DALLAS
  LINE: Navigation lights on.
  EXPRESSION: Command

::SCENE::
LOCATION: EXT. NOSTROMO
MOOD: Descending Through Atmosphere
CHARACTERS: Narrator
BACKGROUND_IMAGE: nostromo_descending_through_atmosphere.png
BACKGROUND_EDIT: "The Nostromo tug-module hydroplaning downwards through a thick atmosphere, with brilliant lights cutting through the haze."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Tug-module hydroplaning downward.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: A set of brilliant lights switch on. Cut through the thick atmosphere.
  EXPRESSION: null

::SCENE::
LOCATION: INT. ENGINE ROOM CUBICLE
MOOD: Chaotic
CHARACTERS: Parker, Brett
BACKGROUND_IMAGE: engine_room_cubicle_turbulent.png
BACKGROUND_EDIT: "Parker and Brett are strapped into their seats in a cubicle, experiencing severe turbulence. Equipment is shaking."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Parker and Brett strapped in their seats. Begin rocking from the sudden, extreme turbulence.
  EXPRESSION: null
- CHARACTER: PARKER
  LINE: What was that.
  EXPRESSION: Shocked
- CHARACTER: BRETT
  LINE: Pressure drop in intake 3. Must’ve lost a shield.
  EXPRESSION: Concerned
- CHARACTER: BRETT
  LINE: Yep. 3’s gone. Dust pouring in the intake.
  EXPRESSION: Alarmed
- CHARACTER: PARKER
  LINE: Shut her down, shut her down,
  EXPRESSION: Panicked
- CHARACTER: BREIT
  LINE: What do you think I’m doing.
  EXPRESSION: Defensive
- CHARACTER: PARKER
  LINE: We’ve got an engine full of dust.
  EXPRESSION: Desperate
- CHARACTER: BRETT
  LINE: I’ll bypass it and vent the stuff back out.
  EXPRESSION: Determined
- CHARACTER: PARKER
  LINE: What the hell are we going through. If we don’t crash, dollars to your aunt’s cherry we get an electrical fire.
  EXPRESSION: Fearful

::SCENE::
LOCATION: INT. BRIDGE
MOOD: Approaching Target
CHARACTERS: Lambert
BACKGROUND_IMAGE: bridge_turbulent.png
BACKGROUND_EDIT: "The bridge of a spaceship, experiencing severe turbulence. Lambert's eyes are fixed on cross-plot gauges."

::SCRIPT::
- CHARACTER: Narrator
  LINE: The turbulence continues unabated. Lambert's eyes follow cross-plot gauges.
  EXPRESSION: null
- CHARACTER: LAMBERT
  LINE: Approaching point of origin. Closing at 20 kilometers, 15 and slowing. Ten. Five. We’re directly above the source of the transmission.
  EXPRESSION: Focused

::SCENE::
LOCATION: INT. BRIDGE
MOOD: Decision Making
CHARACTERS: Dallas, Lambert
BACKGROUND_IMAGE: bridge_turbulent.png
BACKGROUND_EDIT: "The bridge of a spaceship, experiencing severe turbulence. Dallas and Lambert are discussing the terrain."

::SCRIPT::
- CHARACTER: DALLAS
  LINE: What’s the terrain.
  EXPRESSION: Inquisitive
- CHARACTER: LAMBERT
  LINE: Something coming up. Looks good. There. Flat. It’ll do. Mark.
  EXPRESSION: Confident
- CHARACTER: DALLAS
  LINE: Let’s go with it. Take her down.
  EXPRESSION: Decisive
- CHARACTER: LAMBERT
  LINE: Drop begins -- now. Fifteen kilometers and dropping... twelve...ten...eight and slowing. Five. Three. Two. One kilometer and slowing.
  EXPRESSION: Focused

::SCENE::
LOCATION: INT. BRIDGE
MOOD: Landing Sequence
CHARACTERS: Dallas, Kane, Lambert
BACKGROUND_IMAGE: bridge_landing.png
BACKGROUND_EDIT: "The bridge of a spaceship during a landing sequence. Thrusters are heard."

::SCRIPT::
- CHARACTER: DALLAS
  LINE: Activate lifter quads.
  EXPRESSION: Commanding
- CHARACTER: Narrator
  LINE: A throb of jets.
  EXPRESSION: null
- CHARACTER: KANE
  LINE: Quads on.
  EXPRESSION: Informative
- CHARACTER: DALLAS
  LINE: Kill drive engines.
  EXPRESSION: Commanding
- CHARACTER: Narrator
  LINE: The main engines fall silent.
  EXPRESSION: null
- CHARACTER: LAMBERT
  LINE: Nine hundred meters and dropping. Eight hundred. Seven hundred.
  EXPRESSION: Focused

::SCENE::
LOCATION: EXT. PLANET - NIGHT
MOOD: Arrival
CHARACTERS: Narrator
BACKGROUND_IMAGE: planet_landing.png
BACKGROUND_EDIT: "The Nostromo hovers over a stormy, night-shrouded planet surface, with landing struts extending."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Storm blowing across the night-shrouded surface.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The Nostromo hovers on glowing beams of light. Landing struts unfold like insect legs. The ship slams down. Rocks heavily on massive shock absorbers.
  EXPRESSION: null

::SCENE::
LOCATION: INT. BRIDGE - NIGHT
MOOD: Impact
CHARACTERS: Ripley, Kane, Dallas, Lambert
BACKGROUND_IMAGE: bridge_aftermath.png
BACKGROUND_EDIT: "The bridge of a spaceship in darkness after a hard landing. Panels are flashing and lights are out."

::SCRIPT::
- CHARACTER: RIPLEY
  LINE: We’re down.
  EXPRESSION: Relieved
- CHARACTER: Narrator
  LINE: An enormous vibration. The panels in the room flash simultaneously. Lights go out.
  EXPRESSION: null
- CHARACTER: KANE
  LINE: Lost it. Lost it.
  EXPRESSION: Panicked
- CHARACTER: Narrator
  LINE: Moments. Nothing. Kane grabs emergency headlamp from facia. Followed by Dallas and Lambert.
  EXPRESSION: null
- CHARACTER: DALLAS
  LINE: What happened.
  EXPRESSION: Confused

::SCENE::
LOCATION: INT. ENGINE ROOM
MOOD: Catastrophic Failure
CHARACTERS: Narrator
BACKGROUND_IMAGE: engine_room_fire.png
BACKGROUND_EDIT: "An electrical fire breaks out along control panels in the engine room after a severe vibration."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Another huge vibration. An electrical fire breaks out along three control panels.
  EXPRESSION: null

::SCENE::
LOCATION: INT. ENGINE ROOM - CUBICLE
MOOD: Disaster
CHARACTERS: Parker, Brett
BACKGROUND_IMAGE: engine_room_cubicle_disaster.png
BACKGROUND_EDIT: "Parker and Brett in the cubicle, witnessing the pandemonium below. Lights are out."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Parker and Brett see the pandemonium below. Brett hits the secondary generator switch.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: A pressure valve blows. Another conduit breaks loose. All lights go out. They grab hand lights from wall.
  EXPRESSION: null

::SCENE::
LOCATION: INT. BRIDGE
MOOD: Darkness and Uncertainty
CHARACTERS: Lambert, Kane, Dallas, Ripley
BACKGROUND_IMAGE: bridge_darkness.png
BACKGROUND_EDIT: "The bridge is in darkness. Emergency lights are being activated."

::SCRIPT::
- CHARACTER: LAMBERT
  LINE: Secondary generator should kick over.
  EXPRESSION: Hopeful
- CHARACTER: KANE
  LINE: Where is it.
  EXPRESSION: Anxious
- CHARACTER: Narrator
  LINE: Moments. Nothing. Kane grabs emergency headlamp from facia. Followed by Dallas and Lambert.
  EXPRESSION: null
- CHARACTER: DALLAS
  LINE: What happened.
  EXPRESSION: Demanding
- CHARACTER: Narrator
  LINE: Ripley hits the voice-amp.
  EXPRESSION: null
- CHARACTER: RIPLEY
  LINE: Engine room, what happened.
  EXPRESSION: Urgent

::SCENE::
LOCATION: INT. ENGINE ROOM CUBICLE
MOOD: Explanatory and Urgent
CHARACTERS: Parker, Brett
BACKGROUND_IMAGE: engine_room_cubicle_fire.png
BACKGROUND_EDIT: "Parker is fighting an electrical fire. Brett is shouting into his voice-amp. Sparks are flying."

::SCRIPT::
- CHARACTER: PARKER
  LINE: Goddamn dust in the engines, that’s what happened. Electric fire.
  EXPRESSION: Angry
- CHARACTER: BRETT
  LINE: It’s big.
  EXPRESSION: Alarmed
- CHARACTER: Narrator
  LINE: Parker fighting an electrical fire on one of his panels. Brett shouting into his voice-amp.
  EXPRESSION: null
- CHARACTER: BRETT
  LINE: The intakes are clogged. We overheated and burned out a whole cell -- Christ, it's really breaking loose down here --
  EXPRESSION: Terrified

::SCENE::
LOCATION: INT. BRIDGE
MOOD: Seeking Information
CHARACTERS: Dallas, Ripley, Kane
BACKGROUND_IMAGE: bridge_darkness.png
BACKGROUND_EDIT: "The bridge is in darkness. Ripley is scanning gauges."

::SCRIPT::
- CHARACTER: DALLAS
  LINE: Somebody give me a simple answer. Has the hull been breached.
  EXPRESSION: Desperate
- CHARACTER: RIPLEY
  LINE: I don't see anything. We've still got pressure.
  EXPRESSION: Informative
- CHARACTER: Narrator
  LINE: A beep from the communicator.
  EXPRESSION: null
- CHARACTER: DALLAS
  LINE: Hit the screen.
  EXPRESSION: Commanding
- CHARACTER: KANE
  LINE: Nothing.
  EXPRESSION: Frustrated
- CHARACTER: Narrator
  LINE: Kane snaps three toggles. The screens flicker, but remain black.
  EXPRESSION: null

::SCENE::
LOCATION: EXT. SHIP - NIGHT
MOOD: Isolation and Storm
CHARACTERS: Narrator
BACKGROUND_IMAGE: ship_in_storm_night.png
BACKGROUND_EDIT: "The Nostromo sits in the darkness of a storm, with only a few lights distinguishing it. The wind sounds are prominent."

::SCRIPT::
- CHARACTER: Narrator
  LINE: The wind sounds. Storm continues to blow around the-craft.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: A few glittering lights distinguish the Nostromo from absolute darkness.
  EXPRESSION: null

::SCENE::
LOCATION: INT. ENGINE ROOM CUBICLE
MOOD: Continued Struggle
CHARACTERS: Parker
BACKGROUND_IMAGE: engine_room_cubicle_fire.png
BACKGROUND_EDIT: "Parker is still battling the electrical fire on a panel in the engine room cubicle."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Parker on the c
  EXPRESSION: null

::SCENE::
LOCATION: Bridge
MOOD: Urgent
CHARACTERS: Parker, Ripley, Dallas
BACKGROUND_IMAGE: bridge.png
BACKGROUND_EDIT: "Dimly lit bridge with non-functional screens"

::SCRIPT::
- CHARACTER: Parker
  LINE: 4 panel is totally shot, the secondary load sharing unit is out, at least three cells on 12 module are gone.
  EXPRESSION: Grim
- CHARACTER: Ripley
  LINE: Is that it.
  EXPRESSION: Tired
- CHARACTER: Parker
  LINE: Couldn’t fix it out her anyway. And we need to reroute a couple of these ducts. Can't really fix them without a whole drydock --
  EXPRESSION: Grim
- CHARACTER: Dallas
  LINE: What else.
  EXPRESSION: Impatient
- CHARACTER: Parker
  LINE: We lost a cell. Some fragments caked up and blew the whole system. We’ve got to clean it all out and repressurize.
  EXPRESSION: Grim
- CHARACTER: Brett
  LINE: Right.
  EXPRESSION: Resigned
- CHARACTER: Ripley
  LINE: Get started on 4 panel. I’ll be down in five minutes.
  EXPRESSION: Determined
- CHARACTER: Dallas
  LINE: How long before we’re functional.
  EXPRESSION: Anxious
- CHARACTER: Ripley
  LINE: Fifteen to twenty hours --
  EXPRESSION: Resigned
- CHARACTER: Dallas
  LINE: Stay on it. What about the auxiliaries.
  EXPRESSION: Anxious
- CHARACTER: Lambert
  LINE: Working on it.
  EXPRESSION: Busy

::PATHS::
- CHOICE: "Continue working on repairs"
  TARGET: ship_exterior_night
  STATE_CHANGE: frustration = +1
  CONDITION: null

::SCENE::
LOCATION: Ship Exterior
MOOD: Foreboding
CHARACTERS: Narrator
BACKGROUND_IMAGE: ship_exterior.png
BACKGROUND_EDIT: "Nighttime, ship lights on, featureless ground, high winds"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Bridge lights come to life. Illuminate nothing but a patch of featureless ground. The wind and storm now at a higher pitch.
  EXPRESSION: null

::PATHS::
- CHOICE: "Return to bridge"
  TARGET: bridge_interior_night
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Bridge Interior
MOOD: Tense
CHARACTERS: Dallas, Kane, Lambert, Ash
BACKGROUND_IMAGE: bridge_interior.png
BACKGROUND_EDIT: "Nighttime, crew gathered around bridge, drinking coffee, opaque screens"

::SCRIPT::
- CHARACTER: Dallas
  LINE: Any response yet.
  EXPRESSION: Hopeful
- CHARACTER: Ash
  LINE: Nothing but the same transmission every thirty-two seconds. All the other channels are dead.
  EXPRESSION: Neutral
- CHARACTER: Dallas
  LINE: Kick on the floods.
  EXPRESSION: Demanding

::PATHS::
- CHOICE: "Activate floodlights"
  TARGET: ship_exterior_floodlights
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Ship Exterior
MOOD: Eerie
CHARACTERS: Narrator
BACKGROUND_IMAGE: ship_exterior_floodlights.png
BACKGROUND_EDIT: "Floodlights illuminating rocky landscape, wind and dust at high pitch"

::SCRIPT::
- CHARACTER: Narrator
  LINE: A ring of floodlights comes to life. Dimly illuminating the rocky landscape. The wind and dust now at a higher pitch.
  EXPRESSION: null

::PATHS::
- CHOICE: "Return to bridge"
  TARGET: bridge_interior_night_storm
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Bridge Interior
MOOD: Concerned
CHARACTERS: Dallas, Kane, Ash
BACKGROUND_IMAGE: bridge_interior_storm.png
BACKGROUND_EDIT: "Nighttime, Dallas looking out windows at storm illuminated by floodlights"

::SCRIPT::
- CHARACTER: Dallas
  LINE: Dallas stares out the windows at the swirling storm, illuminated by the external floodlights.
  EXPRESSION: Worried
- CHARACTER: Kane
  LINE: We can’t go anywhere in this.
  EXPRESSION: Concerned
- CHARACTER: Ash
  LINE: Mother says the sun’s coming up in about twenty minutes.
  EXPRESSION: Informative
- CHARACTER: Dallas
  LINE: How far from the source of the transmission.
  EXPRESSION: Focused
- CHARACTER: Ash
  LINE: Northeast -- about 3000 meters.
  EXPRESSION: Precise
- CHARACTER: Kane
  LINE: Close enough to walk to.
  EXPRESSION: Hopeful
- CHARACTER: Dallas
  LINE: Can you run an atmospheric.
  EXPRESSION: Demanding
- CHARACTER: Ash
  LINE: Almost primordial. Inert nitrogen. A high concentration of carbon dioxide crystals. Methane. And ammonia, also frozen. I’m working on the trace elements.
  EXPRESSION: Analytical
- CHARACTER: Dallas
  LINE: Pressure.
  EXPRESSION: Demanding
- CHARACTER: Ash
  LINE: Ten to the fourth dynes per square centimeter.
  EXPRESSION: Precise
- CHARACTER: Kane
  LINE: Moisture content.
  EXPRESSION: Curious
- CHARACTER: Ash
  LINE: 98.p.p. It’s wet. With high vapor content.
  EXPRESSION: Precise
- CHARACTER: Dallas
  LINE: Anything else.
  EXPRESSION: Demanding
- CHARACTER: Ash
  LINE: Rock, lava base. Deep cold -- well below the line.
  EXPRESSION: Analytical
- CHARACTER: Kane
  LINE: I volunteer for the first group going out.
  EXPRESSION: Eager
- CHARACTER: Dallas
  LINE: I hear you. Lambert. You too.
  EXPRESSION: Decisive
- CHARACTER: Lambert
  LINE: Swell.
  EXPRESSION: Sarcastic
- CHARACTER: Dallas
  LINE: One more thing. Let’s get out some weapons.
  EXPRESSION: Cautionary

::PATHS::
- CHOICE: "Prepare for expedition"
  TARGET: engine_room_cubicle
  STATE_CHANGE: expedition_prep = true
  CONDITION: null

::SCENE::
LOCATION: Engine Room Cubicle
MOOD: Frustrated
CHARACTERS: Parker, Brett, Ripley
BACKGROUND_IMAGE: engine_room.png
BACKGROUND_EDIT: "Cubicle, Parker and Brett laser welding, Ripley rewiring"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Parker and Brett laser welding one of the ducts. Shirts off. Sweat steaming. Ripley rewiring one of the panels.
  EXPRESSION: null
- CHARACTER: Parker
  LINE: Hey Ripley, I got a question.
  EXPRESSION: Inquisitive
- CHARACTER: Ripley
  LINE: Yeah.
  EXPRESSION: Attentive
- CHARACTER: Parker
  LINE: Do we get to go out on the expedition or are we stuck here until everything’s fixed.
  EXPRESSION: Hopeful
- CHARACTER: Ripley
  LINE: You know the answer to that.
  EXPRESSION: Firm
- CHARACTER: Brett
  LINE: What about the shares in case they find anything.
  EXPRESSION: Greedy
- CHARACTER: Ripley
  LINE: Don’t worry, you’ll both get what’s coming to you.
  EXPRESSION: Reassuring
- CHARACTER: Brett
  LINE: I’m not doing any more work unless we get full shares.
  EXPRESSION: Demanding
- CHARACTER: Ripley
  LINE: You're guaranteed by law that you'll get a share. Now both of you knock it off and get back to work.
  EXPRESSION: Stern
- CHARACTER: Narrator
  LINE: Parker looks at her. Snaps on the laser weld. Starts to join another section of the duct.
  EXPRESSION: null
- CHARACTER: Brett
  LINE: Right.
  EXPRESSION: Resigned

::PATHS::
- CHOICE: "Continue working"
  TARGET: main_airlock_dawn
  STATE_CHANGE: crew_tension = +1
  CONDITION: null

::SCENE::
LOCATION: Main Airlock
MOOD: Preparatory
CHARACTERS: Dallas, Kane, Lambert
BACKGROUND_IMAGE: main_airlock.png
BACKGROUND_EDIT: "Dawn, crew in protective gear, laser pistols"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Dallas, Kane, and Lambert enter the lock. All wear gloves, boots, jackets. Carry laser pistols.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Kane touches a button. Servo whine. Then the inner door slides quietly shut. The trio pull on their helmets.
  EXPRESSION: null
- CHARACTER: Dallas
  LINE: I'm sending. Do you hear me.
  EXPRESSION: Authoritative
- CHARACTER: Kane
  LINE: Receiving.
  EXPRESSION: Affirmative
- CHARACTER: Lambert
  LINE: Receiving.
  EXPRESSION: Affirmative
- CHARACTER: Narrator
  LINE: Lambert isn’t happy.
  EXPRESSION: Reluctant
- CHARACTER: Dallas
  LINE: All right. Keep away from the weapons unless I say otherwise.
  EXPRESSION: Cautionary

::PATHS::
- CHOICE: "Proceed with expedition"
  TARGET: ash_blister_dawn
  STATE_CHANGE: expedition_active = true
  CONDITION: null

::SCENE::
LOCATION: Ash's Blister
MOOD: Observational
CHARACTERS: Ash
BACKGROUND_IMAGE: ash_blister.png
BACKGROUND_EDIT: "Dawn, Ash at console, checking screens"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Ash descends companionway to blister. Punches up screens and instrumentation.
  EXPRESSION: null

::PATHS::
- CHOICE: "Monitor crew"
  TARGET: main_airlock_outer_hatch
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Main Airlock
MOOD: Anticipatory
CHARACTERS: Dallas, Kane, Lambert, Ash
BACKGROUND_IMAGE: main_airlock_outer.png
BACKGROUND_EDIT: "Dawn, outer hatch opening, dust and steam swirling"

::SCRIPT::
- CHARACTER: Dallas
  LINE: Open outer hatch.
  EXPRESSION: Demanding
- CHARACTER: Narrator
  LINE: Another servo whine. Ponderously, the outer lock hatch slides open. Clouds of dust and steam swirl before the three crew members. A mobile gangway slides out the open hatch. Burnt orange sunlight beyond.
  EXPRESSION: null

::PATHS::
- CHOICE: "Exit the airlock"
  TARGET: planet_surface_dawn
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Planet Surface
MOOD: Austere
CHARACTERS: Dallas, Lambert, Ash
BACKGROUND_IMAGE: planet_surface.png
BACKGROUND_EDIT: "Dawn, trio walking down gangplank onto lava rock, strong wind"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The trio walk down the gangplank. Arrive at surface level. Their feet striking onto a thick layer of lava rock. The wind at gale force.
  EXPRESSION: null
- CHARACTER: Dallas
  LINE: Which way.
  EXPRESSION: Inquisitive
- CHARACTER: Lambert
  LINE: Over here.
  EXPRESSION: Direct
- CHARACTER: Dallas
  LINE: You lead.
  EXPRESSION: Delegating
- CHARACTER: Narrator
  LINE: Lambert walks into the storm. Followed closely by the others.
  EXPRESSION: null
- CHARACTER: Lambert
  LINE: Now I can’t see a goddamn thing.
  EXPRESSION: Frustrated
- CHARACTER: Ash
  LINE: Turn on the finder. It’s tuned to the transmission. Let it lead you.
  EXPRESSION: Helpful
- CHARACTER: Dallas
  LINE: It’s on -- Ash are you receiving.
  EXPRESSION: Inquisitive

::PATHS::
- CHOICE: "Continue following the transmission"
  TARGET: ash_blister_dawn_receiving
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Ash's Blister
MOOD: Monitoring
CHARACTERS: Ash, Dallas
BACKGROUND_IMAGE: ash_blister_receiving.png
BACKGROUND_EDIT: "Dawn, Ash at console, watching crew on screen"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Ash leaning over his console. Watches them beneath him. Corresponding images on the screen in front of him.
  EXPRESSION: null
- CHARACTER: Ash
  LINE: See you. Read you. Good contact on my board.
  EXPRESSION: Confident
- CHARACTER: Dallas
  LINE: Getting you clear and free. Let’s keep the line open.
  EXPRESSION: Reassuring

::PATHS::
- CHOICE: "Continue expedition"
  TARGET: planet_surface_pushing
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Planet Surface
MOOD: Struggling
CHARACTERS: Dallas, Lambert
BACKGROUND_IMAGE: planet_surface_pushing.png
BACKGROUND_EDIT: "Dawn, crew pushing through storm like divers"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The three crew members push their way along. Like divers at the
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue pushing forward"
  TARGET: end
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Dark Sea
MOOD: Ominous
CHARACTERS: Narrator, Lambert, Kane, Dallas
BACKGROUND_IMAGE: dark_sea.png
BACKGROUND_EDIT: "Dark, stormy sea with driving rain and dust"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The wind and dust continues driving down in dark sheets.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Lambert repeats.
  EXPRESSION: null
- CHARACTER: Lambert
  LINE: Can't see more than three meters in any direction.
  EXPRESSION: Distressed
- CHARACTER: Kane
  LINE: Quit griping.
  EXPRESSION: Annoyed
- CHARACTER: Lambert
  LINE: I like griping.
  EXPRESSION: Sarcastic
- CHARACTER: Dallas
  LINE: Come on.
  EXPRESSION: Impatient
- CHARACTER: Lambert
  LINE: What a wonderful little place. Totally unspoiled.
  EXPRESSION: Sarcastic
- CHARACTER: Narrator
  LINE: They wade on, following Lambert. She abruptly halts. Confused.
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue following Lambert"
  TARGET: blister_dawn
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Blister - Dawn
MOOD: Focused
CHARACTERS: Narrator, Ash, Lambert, Dallas
BACKGROUND_IMAGE: blister_dawn.png
BACKGROUND_EDIT: "Interior of a control room, screens showing data"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Ash watches his viewscreens intently.
  EXPRESSION: null
- CHARACTER: Lambert
  LINE: I've got it again.
  EXPRESSION: Concerned
- CHARACTER: Ash
  LINE: Any problems.
  EXPRESSION: Neutral
- CHARACTER: Dallas
  LINE: Yeah. A lot of dust and wind. Starting to get some fade on the beam.
  EXPRESSION: Concerned
- CHARACTER: Narrator
  LINE: The trio moves through a dark limo.
  EXPRESSION: null

::PATHS::
- CHOICE: "Proceed through the limo"
  TARGET: planet_dawn
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Plant - Dawn
MOOD: Tense
CHARACTERS: Narrator, Lambert, Kane, Dallas
BACKGROUND_IMAGE: planet_dawn.png
BACKGROUND_EDIT: "Dark, stormy alien landscape, towering rock formations"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The trio moves through a dark limo.
  EXPRESSION: null
- CHARACTER: Lambert
  LINE: This way.
  EXPRESSION: Directing
- CHARACTER: Narrator
  LINE: Lambert indicates left. Moves in that direction. The others follow. The storm growing.
  EXPRESSION: null
- CHARACTER: Kane
  LINE: I’m losing it.
  EXPRESSION: Frustrated
- CHARACTER: Narrator
  LINE: They approach a towering rock formation. The transmission dies out.
  EXPRESSION: null
- CHARACTER: Lambert
  LINE: It’s gone again.
  EXPRESSION: Frustrated
- CHARACTER: Narrator
  LINE: They shelter under a grotesque rock. Storm shrieks round them.
  EXPRESSION: null
- CHARACTER: Kane
  LINE: Now we’re really blind.
  EXPRESSION: Alarmed
- CHARACTER: Dallas
  LINE: Should be dawn soon.
  EXPRESSION: Hopeful
- CHARACTER: Narrator
  LINE: Dallas adjusts headset.
  EXPRESSION: null
- CHARACTER: Dallas
  LINE: Ash. If you hear me. How long until daylight.
  EXPRESSION: Urgent

::PATHS::
- CHOICE: "Wait for daylight"
  TARGET: blister_dawn_2
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Blister - Dawn
MOOD: Waiting
CHARACTERS: Narrator, Ash, Dallas
BACKGROUND_IMAGE: blister_dawn_2.png
BACKGROUND_EDIT: "Interior of a control room, screens showing data"

::SCRIPT::
- CHARACTER: Ash
  LINE: Sun’s coming up in about ten minutes.
  EXPRESSION: Informative
- CHARACTER: Kane
  LINE: We should be able to see something then.
  EXPRESSION: Hopeful
- CHARACTER: Lambert
  LINE: Or the other way around. Something to think about while waiting.
  EXPRESSION: Pensive
- CHARACTER: Narrator
  LINE: Ash checking instruments.
  EXPRESSION: null

::PATHS::
- CHOICE: "Observe the sunrise"
  TARGET: nostromo_sunrise
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: The Nostromo - Sunrise
MOOD: Dramatic
CHARACTERS: Narrator
BACKGROUND_IMAGE: nostromo_sunrise.png
BACKGROUND_EDIT: "Exterior of a spaceship, atmosphere turning blood-red"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Atmosphere turning the color of blood. Then the sun is up.
  EXPRESSION: null

::PATHS::
- CHOICE: "Transition to engine cubicle"
  TARGET: engine_cubicle
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Engine Cubicle
MOOD: Productive
CHARACTERS: Narrator, Brett, Parker, Ripley
BACKGROUND_IMAGE: engine_cubicle.png
BACKGROUND_EDIT: "Interior of a spaceship engine room"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Brett and Parker still at work. Ripley moves away from her panel in triumph.
  EXPRESSION: null
- CHARACTER: Ripley
  LINE: You ought to be able to handle the rest.
  EXPRESSION: Confident
- CHARACTER: Parker
  LINE: Don’t worry.
  EXPRESSION: Reassuring
- CHARACTER: Ripley
  LINE: If you run into trouble, I’ll be on the bridge.
  EXPRESSION: Helpful
- CHARACTER: Brett
  LINE: Right.
  EXPRESSION: Acknowledging
- CHARACTER: Narrator
  LINE: She leaves.
  EXPRESSION: null
- CHARACTER: Parker
  LINE: Bitch.
  EXPRESSION: Annoyed

::PATHS::
- CHOICE: "Continue working or go to the bridge"
  TARGET: planet_day
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Planet - Day
MOOD: Hopeful
CHARACTERS: Narrator, Kane, Dallas, Lambert
BACKGROUND_IMAGE: planet_day.png
BACKGROUND_EDIT: "Alien landscape with clearing dust, daylight"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The three figures stand and move away from the rock formation. There is enough daylight to see where they are walking. The signal begins to fade in again.
  EXPRESSION: null

::PATHS::
- CHOICE: "Observe the returning signal"
  TARGET: blister_day
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Blister - Day
MOOD: Observational
CHARACTERS: Narrator, Ash, Ripley
BACKGROUND_IMAGE: blister_day.png
BACKGROUND_EDIT: "Interior of a control room, screens showing video images"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Ash watches video images of the three. Now moving again. Ripley’s voice comes over.
  EXPRESSION: null
- CHARACTER: Ripley
  LINE: How’s it going.
  EXPRESSION: Inquiring
- CHARACTER: Ash
  LINE: All right.
  EXPRESSION: Informative
- CHARACTER: Ripley
  LINE: Have you tried putting the transmission through ECIU.
  EXPRESSION: Suggestive
- CHARACTER: Ash
  LINE: Mother hasn’t identified it as yet.
  EXPRESSION: Informative
- CHARACTER: Ripley
  LINE: I’ll give it a shot.
  EXPRESSION: Determined
- CHARACTER: Ash
  LINE: Be my guest.
  EXPRESSION: Amused

::PATHS::
- CHOICE: "Let Ripley try the ECIU"
  TARGET: bridge_console
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Bridge
MOOD: Intense
CHARACTERS: Narrator, Ripley, Ash
BACKGROUND_IMAGE: bridge.png
BACKGROUND_EDIT: "Interior of a spaceship bridge console"

::SCRIPT::
- CHARACTER: Narrator
  LINE: She punches some buttons. The noise is now heard on her speaker.
  EXPRESSION: null

::PATHS::
- CHOICE: "Listen to the transmission"
  TARGET: planet_day_2
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Planet - Day
MOOD: Astonishing
CHARACTERS: Narrator, Kane, Dallas, Lambert
BACKGROUND_IMAGE: planet_day_2.png
BACKGROUND_EDIT: "Alien landscape, dust clearing, figures visible"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Dust clearing. Three tiny figures against the landscape.
  EXPRESSION: null

::PATHS::
- CHOICE: "Observe the landscape"
  TARGET: planet_day_3
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Planet - Day
MOOD: Shocking
CHARACTERS: Narrator, Kane, Dallas, Lambert
BACKGROUND_IMAGE: planet_day_3.png
BACKGROUND_EDIT: "Empty alien landscape, Kane looking startled"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Empty landscape. Then Kane comes up over a rise startled by what he sees. Suddenly the transmission is deafening.
  EXPRESSION: null
- CHARACTER: Kane
  LINE: Jesus Christ.
  EXPRESSION: Shocked
- CHARACTER: Narrator
  LINE: Dallas and Lambert join him equally startled.
  EXPRESSION: null

::PATHS::
- CHOICE: "Witness the reveal"
  TARGET: planet_day_4
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Planet - Day
MOOD: Awe-inspiring
CHARACTERS: Narrator, Kane, Dallas, Lambert
BACKGROUND_IMAGE: planet_day_4.png
BACKGROUND_EDIT: "View of a gargantuan, non-human spaceship rising from rocks"

::SCRIPT::
- CHARACTER: Narrator
  LINE: A gargantuan spaceship rising from the rock. Clearly of nonhuman manufacture.
  EXPRESSION: null

::PATHS::
- CHOICE: "React to the spaceship"
  TARGET: planet_day_5
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Planet - Day
MOOD: Urgent
CHARACTERS: Narrator, Kane, Dallas, Lambert, Ash
BACKGROUND_IMAGE: planet_day_5.png
BACKGROUND_EDIT: "Alien landscape with the spaceship, figures shouting"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Noise still at shrill pitch. All members of the party shouting into their voice amps.
  EXPRESSION: null
- CHARACTER: Kane
  LINE: Some kind of spaceship.
  EXPRESSION: Amazed
- CHARACTER: Lambert
  LINE: Are you sure. It’s weird --
  EXPRESSION: Hesitant
- CHARACTER: Dallas
  LINE: Ash, can you see this.
  EXPRESSION: Urgent

::PATHS::
- CHOICE: "Communicate with Ash"
  TARGET: ash_blister_day
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Ash’s Blister - Day
MOOD: Perplexed
CHARACTERS: Narrator, Ash, Dallas
BACKGROUND_IMAGE: ash_blister_day.png
BACKGROUND_EDIT: "Interior of Ash's control room, screen showing the alien craft"

::SCRIPT::
- CHARACTER: Ash
  LINE: Yeah. Never seen one like it. Neither has Mother.
  EXPRESSION: Puzzled
- CHARACTER: Dallas
  LINE: Keep looking for enhancement.
  EXPRESSION: Commanding
- CHARACTER: Ash
  LINE: Whatever the transmission is, it’s inside that.
  EXPRESSION: Speculative
- CHARACTER: Kane
  LINE: I’ll go in and have a look.
  EXPRESSION: Determined
- CHARACTER: Dallas
  LINE: Hold on. Ash, I don’t see any lights or movements. Do you.
  EXPRESSION: Cautious
- CHARACTER: Ash
  LINE: I can’t get any reading.
  EXPRESSION: Frustrated

::PATHS::
- CHOICE: "Continue investigation"
  TARGET: planet_day_6
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Planet - Day
MOOD: Mysterious
CHARACTERS: Narrator, Ash, Dallas
BACKGROUND_IMAGE: planet_day_6.png
BACKGROUND_EDIT: "Alien landscape, spaceship, Ash speaking via voice amp"

::SCRIPT::
- CHARACTER: Ash
  LINE: It’s putting out so much power I just can’t get any reading.
  EXPRESSION: Frustrated
- CHARACTER: Narrator
  LINE: Dallas shuts off his receiver. Sudden quiet. A long moment.
  EXPRESSION: null
- CHARACTER: Dallas
  LINE: It looks pretty dead from here. We’ll approach the base.
  EXPRESSION: Decisive
- CHARACTER: Narrator
  LINE: They move toward the ship.
  EXPRESSION: null

::PATHS::
- CHOICE: "Approach the ship"
  TARGET: blister_day_2
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Blister - Day
MOOD: Desperate
CHARACTERS: Narrator, Ash, Dallas
BACKGROUND_IMAGE: blister_day_2.png
BACKGROUND_EDIT: "Interior of Ash's control room, Ash frantically working controls"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Ash readjusts his instrumentation.
  EXPRESSION: null
- CHARACTER: Dallas
  LINE: There’s only one thing I can --
  EXPRESSION: Fading
- CHARACTER: Narrator
  LINE: Dallas' voice fades in and out. As do their images on the view screens.
  EXPRESSION: null
- CHARACTER: Ash
  LINE: Dallas -- Dallas -- Do you read me?
  EXPRESSION: Frantic

::PATHS::
- CHOICE: "Continue trying to reach Dallas"
  TARGET: bridge_day_2
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Bridge - Day
MOOD: Searching
CHARACTERS: Narrator, Ripley, Dallas
BACKGROUND_IMAGE: bridge_day_2.png
BACKGROUND_EDIT: "Interior of spaceship bridge, Ripley at console"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Ripley is running the transmission through ECIU. Over the speakers Dallas’ voice fades in.
  EXPRESSION: null
- CHARACTER: Dallas
  LINE: No sign of life. No lights -- No movement --
  EXPRESSION: Fading
- CHARACTER: Narrator
  LINE: She studies a long series of binary programs.
  EXPRESSION: null
- CHARACTER: Dallas
  LINE: We’re beneath the base.
  EXPRESSION: Fading
- CHARACTER: Narrator
  LINE: His voice fades into static. Disappears.
  EXPRESSION: null

::PATHS::
- CHOICE: "Observe the disappearance"
  TARGET: derelict_day
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Derelict - Day
MOOD: Exploratory
CHARACTERS: Narrator, Kane, Dallas
BACKGROUND_IMAGE: derelict_day.png
BACKGROUND_EDIT: "Exterior of a derelict alien structure, entrance visible"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The lower part of the entrance filled with dust and pumice.
  EXPRESSION: null
- CHARACTER: Kane
  LINE: Looks like an entrance.
  EXPRESSION: Observant
- CHARACTER: Dallas
  LINE: Yeah -- Let’s move inside --
  EXPRESSION: Determined
- CHARACTER: Narrator
  LINE: They climb up to one of the apertures and enter.
  EXPRESSION: null

::PATHS::
- CHOICE: "Enter the derelict"
  TARGET: chamber_day
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Chamber - Day
MOOD: Eerie
CHARACTERS: Narrator, Dallas, Kane, Lambert
BACKGROUND_IMAGE: chamber_day.png
BACKGROUND_EDIT: "Interior of a large, dust-filled alien chamber"

::SCRIPT::
- CHARACTER: Narrator
  LINE: They move into a high-ceilinged chamber. Ghostly light filters dust-filled air. A few meters in an opening appears.
  EXPRESSION: null
- CHARACTER: Dallas
  LINE: It just goes down -- smooth walls. I can’t see the bottom, light won’t reach.
  EXPRESSION: Informative
- CHARACTER: Narrator
  LINE: Kane and Lambert come over. Dallas begins unclipping gear from his belt.
  EXPRESSION: null
- CHARACTER: Dallas
  LINE: Let’
  EXPRESSION: Halting

::PATHS::
- CHOICE: "Continue exploring"
  TARGET: end
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Derelict Ship - Unknown Area
MOOD: Suspenseful
CHARACTERS: Narrator, Dallas, Kane, Lambert
BACKGROUND_IMAGE: derelict_ship_unknown_area.png
BACKGROUND_EDIT: "Dimly lit, dusty, filled with strange artifacts"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Kane and Lambert exchange a glance. Dallas shines his light about, sees --
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: A large, glossy urn, tan coloration. Round opening at the top, empty within.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Then Dallas shines his light on nearby wall. Moves closer.
  EXPRESSION: null
- CHARACTER: Dallas
  LINE: Over here.
  EXPRESSION: Directive
- CHARACTER: Narrator
  LINE: They approach. Train their lights along the floor.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: A machine.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: On the mechanism, a small bar moves steadily back and forth. Sliding noiselessly in the grooves.
  EXPRESSION: null
- CHARACTER: Kane
  LINE: Still functioning.
  EXPRESSION: Observant
- CHARACTER: Narrator
  LINE: Lambert looks down at her direction finder.
  EXPRESSION: null
- CHARACTER: Lambert
  LINE: Automatic recording.
  EXPRESSION: Informative
- CHARACTER: Dallas
  LINE: Now for a look down below. This is your big chance.
  EXPRESSION: Encouraging
- CHARACTER: Narrator
  LINE: (looks at Kane)
  EXPRESSION: null
- CHARACTER: Kane
  LINE: Okay.
  EXPRESSION: Resolute
- CHARACTER: Dallas
  LINE: Don’t unhook yourself from the cable. Be out in less than ten minutes. Read me.
  EXPRESSION: Directive
- CHARACTER: Kane
  LINE: Aye aye.
  EXPRESSION: Obedient
- CHARACTER: Narrator
  LINE: Dallas rigs a tripod across the opening in the floor. Unspools a couple feet of wire. Kane attaches the end of it to his chest unit. Climbs over the lip and drops into the hole. Now hanging by the wire. Head and shoulders out of the opening.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Kane activates the climbing unit. Lowers himself into the fissure.
  EXPRESSION: null

::PATHS::
- CHOICE: "Begin descent"
  TARGET: shaft_opening_descent
  STATE_CHANGE: Kane_descent_progress = 0
  CONDITION: null

::SCENE::
LOCATION: Shaft Opening
MOOD: Claustrophobic, Tense
CHARACTERS: Narrator, Kane, Dallas
BACKGROUND_IMAGE: shaft_opening.png
BACKGROUND_EDIT: "Dark, vertical shaft with minimal light filtering from above"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Kane braces his feet against the wall of the vertical shaft. Switches on his light, points it into the depths. The beam penetrates only thirty feet or so, then is lost in darkness.
  EXPRESSION: null
- CHARACTER: Kane
  LINE: Hotter in here. Warm air rising from below.
  EXPRESSION: Observant
- CHARACTER: Narrator
  LINE: He starts down, playing out the line. Descending in short leaps. Stops to catch his breath. Breathing rasping loudly in his helmet.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: A little light filters from above. Looking up, Kane can see the mouth of the hole. A glowing spot.
  EXPRESSION: null
- CHARACTER: Dallas
  LINE: You okay in there.
  EXPRESSION: Concerned (voice over)
- CHARACTER: Kane
  LINE: Haven’t hit bottom yet. This is work. Can’t talk now.
  EXPRESSION: Strained
- CHARACTER: Narrator
  LINE: He kicks off and continues down. Taking longer and longer hops as he gains confidence.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Pausing for a moment to regain his breath, he shines the light on his instruments.
  EXPRESSION: null
- CHARACTER: Kane
  LINE: I’m below ground level.
  EXPRESSION: Informative

::PATHS::
- CHOICE: "Continue descent"
  TARGET: derelict_cargo_hold
  STATE_CHANGE: Kane_descent_progress = +1
  CONDITION: null

::SCENE::
LOCATION: Bridge
MOOD: Urgent, Worried
CHARACTERS: Narrator, Ripley, Ash
BACKGROUND_IMAGE: bridge.png
BACKGROUND_EDIT: "Ship's bridge, consoles lit, Ripley focused on her work"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Ripley at her console, still working on transmission. Gets a readout. Looks worried. Speaks into communicator.
  EXPRESSION: null
- CHARACTER: Ripley
  LINE: Ash. Urgent. Mother has deciphered part of the transmission. I’m afraid it may not be an S.O.S.
  EXPRESSION: Urgent
- CHARACTER: Ash
  LINE: Then what is it.
  EXPRESSION: Curious (voice over)
- CHARACTER: Ripley
  LINE: She thinks it may be a warning.
  EXPRESSION: Worried
- CHARACTER: Narrator
  LINE: A beat. Continuing static.
  EXPRESSION: null
- CHARACTER: Ripley
  LINE: We’ve got to get through to them. Right away.
  EXPRESSION: Desperate
- CHARACTER: Ash
  LINE: It’s no use. Once they went inside we lost them completely.
  EXPRESSION: Resigned (voice over)
- CHARACTER: Narrator
  LINE: Pause.
  EXPRESSION: null
- CHARACTER: Ripley
  LINE: I’m going out after them.
  EXPRESSION: Determined
- CHARACTER: Ash
  LINE: I don’t think so. We can’t spare the personnel. We’ve got minimum takeoff capability right now. That’s why Dallas left us on board.
  EXPRESSION: Practical (voice over)
- CHARACTER: Ripley
  LINE: I still think we should go after them.
  EXPRESSION: Persistent
- CHARACTER: Ash
  LINE: What’s the point. In the time it takes to get there. They’ll know if it’s a warning.
  EXPRESSION: Logical (voice over)
- CHARACTER: Narrator
  LINE: Ripley looks steadily at Ash on her monitor. His screen, not visible to her, shows blowup of helmeted, skeletal head. Not human.
  EXPRESSION: null

::PATHS::
- CHOICE: "Accept Ash's reasoning"
  TARGET: end_scene
  STATE_CHANGE: Ripley_action = "stay"
  CONDITION: null
- CHOICE: "Insist on going"
  TARGET: bridge_confrontation
  STATE_CHANGE: Ripley_action = "insist"
  CONDITION: null

::SCENE::
LOCATION: Derelict Cargo Hold
MOOD: Eerie, Foreboding
CHARACTERS: Narrator, Kane, Dallas
BACKGROUND_IMAGE: derelict_cargo_hold.png
BACKGROUND_EDIT: "Vast, dark cavernous space filled with strange organic structures"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Kane resumes his downward climb. Suddenly, his feet lose their purchase as the walls of the shaft disappear. The tunnel has reached its end. Below him is dark, cavernous space. Deep breaths due to his violent exertion.
  EXPRESSION: null
- CHARACTER: Dallas
  LINE: See anything.
  EXPRESSION: Inquisitive (voice over)
- CHARACTER: Kane
  LINE: No -- Cave or something below me. Feels like the goddamn tropics in here --
  EXPRESSION: Surprised
- CHARACTER: Narrator
  LINE: He consults his instruments. Helmet instrumentation strobing softly in the darkness.
  EXPRESSION: null
- CHARACTER: Kane
  LINE: -- high nitrogen content, no oxygen --
  EXPRESSION: Scientific
- CHARACTER: Narrator
  LINE: Still puffing, he releases his purchase on the stone walls. Begins to lower himself on power. Now Kane is dangling free in darkness. Spinning slowly on the wire as the chest unit unwinds.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Then his feet hit bottom. Kane grunts in surprise, almost loses his balance.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: He flashes his suit lights. The beams reveal that he is in a large hold. Row after row of extrusions stretch from floor to ceiling.
  EXPRESSION: null
- CHARACTER: Kane
  LINE: This is weird.
  EXPRESSION: Confused
- CHARACTER: Dallas
  LINE: What do you mean.
  EXPRESSION: Inquisitive (voice over)
- CHARACTER: Kane
  LINE: There’s something all over the walls.
  EXPRESSION: Eerie
- CHARACTER: Narrator
  LINE: Kane walks across the chamber. Examines the organic protrusions.
  EXPRESSION: null

::PATHS::
- CHOICE: "Investigate the protrusions"
  TARGET: derelict_chamber_above
  STATE_CHANGE: Kane_discovery_level = 1
  CONDITION: null

::SCENE::
LOCATION: Chamber Above
MOOD: Anxious
CHARACTERS: Narrator, Dallas, Lambert
BACKGROUND_IMAGE: chamber_above.png
BACKGROUND_EDIT: "Control room or observation area overlooking the hold"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Dallas and Lambert.
  EXPRESSION: null
- CHARACTER: Dallas
  LINE: How long till sunset.
  EXPRESSION: Concerned
- CHARACTER: Lambert
  LINE: Twenty minutes.
  EXPRESSION: Factual

::PATHS::
- CHOICE: "Return to the hold"
  TARGET: hold_investigation
  STATE_CHANGE: time_until_sunset = -20
  CONDITION: null

::SCENE::
LOCATION: Hold
MOOD: Unsettling, Mysterious
CHARACTERS: Narrator, Kane, Dallas
BACKGROUND_IMAGE: hold.png
BACKGROUND_EDIT: "Large chamber with rows of leathery, ovoid shapes on the floor"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Kane approaches the center of the room. On the floor are rows of leathery ovoid shapes. He walks around them. Shines his light on one.
  EXPRESSION: null
- CHARACTER: Kane
  LINE: It’s like some kind of storage area. Is anybody there. Do you read me.
  EXPRESSION: Calling out
- CHARACTER: Dallas
  LINE: Loud and clear.
  EXPRESSION: Reassuring (voice over)
- CHARACTER: Kane
  LINE: The place is full of leathery things. Like the one up above. They seem to be sealed.
  EXPRESSION: Descriptive
- CHARACTER: Dallas
  LINE: Can you see what’s in them.
  EXPRESSION: Inquisitive (voice over)
- CHARACTER: Kane
  LINE: I’ll give it a look.
  EXPRESSION: Determined
- CHARACTER: Narrator
  LINE: He tries to open one of them. It won't open.
  EXPRESSION: null
- CHARACTER: Kane
  LINE: Strange feeling to it.
  EXPRESSION: Uneasy
- CHARACTER: Dallas
  LINE: Don't open it. You don't know what's in it.
  EXPRESSION: Warning (voice over)
- CHARACTER: Narrator
  LINE: Kane peers closely at the leathery ovoids. Turns away. Raised areas begin to appear where he touched it. He moves his light along the rows. Turns back to the one he was examining. Something has changed.
  EXPRESSION: null

::PATHS::
- CHOICE: "Examine the changed ovoid"
  TARGET: ovoid_change
  STATE_CHANGE: Kane_interaction_level = 1
  CONDITION: null
- CHOICE: "Heed Dallas's warning and move on"
  TARGET: move_on_from_ovoids
  STATE_CHANGE: Kane_caution = +1
  CONDITION: null

::SCENE::
LOCATION: Unknown Chamber
MOOD: Suspenseful
CHARACTERS: Narrator, Kane, Dallas
BACKGROUND_IMAGE: unknown_chamber.png
BACKGROUND_EDIT: "Dimly lit chamber, opaque surface clearing"

::SCRIPT::
- CHARACTER: Narrator
  LINE: An opaque surface begins to clear. Object becoming visible within.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Kane shines his light on the floor at the base of it. He studies it.
  EXPRESSION: null
- CHARACTER: KANE
  LINE: Jesus --
  EXPRESSION: Shocked
- CHARACTER: DALLAS
  LINE: What.
  EXPRESSION: Curious
- CHARACTER: Narrator
  LINE: Viscera and mandible now visible. The interior surface spongy and irregular.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Kane shines the light inside. With shocking violence, a small creature smashes outward. Fixes itself to his mask. Sizzling sound. The creature melts through the mask. Attaches itself to Kane's face. Kane tears at the thing with his hands. His mouth forced open. He falls backward.
  EXPRESSION: Terrified

::SCENE::
LOCATION: Chamber Above
MOOD: Urgent
CHARACTERS: Narrator, Dallas, Lambert, Kane
BACKGROUND_IMAGE: chamber_above.png
BACKGROUND_EDIT: "View from above, showing Kane falling"

::SCRIPT::
- CHARACTER: DALLAS
  LINE: Kane -- Kane can you hear me.
  EXPRESSION: Worried
- CHARACTER: LAMBERT
  LINE: What’s the matter.
  EXPRESSION: Concerned
- CHARACTER: DALLAS
  LINE: We better haul him out.
  EXPRESSION: Determined
- CHARACTER: LAMBERT
  LINE: It’ll yank him right off his feet if he’s not expecting it.
  EXPRESSION: Cautious
- CHARACTER: DALLAS
  LINE: Try him again.
  EXPRESSION: Impatient
- CHARACTER: LAMBERT
  LINE: Kane -- Kane -- Goddamn it. Answer me.
  EXPRESSION: Frustrated
- CHARACTER: Narrator
  LINE: Dallas begins to fiddle with the winch mechanism.
  EXPRESSION: null
- CHARACTER: DALLAS
  LINE: The line’s slack.
  EXPRESSION: Concerned
- CHARACTER: LAMBERT
  LINE: He doesn't answer. Do you think he could, have unhooked himself.
  EXPRESSION: Doubtful
- CHARACTER: Narrator
  LINE: Dallas switches on the winch motor. With a whine, it begins to reel the line in. After a moment the line, tightens with a Jerk. The motor slows, laboring under added weight.
  EXPRESSION: null
- CHARACTER: DALLAS
  LINE: It caught.
  EXPRESSION: Hopeful
- CHARACTER: LAMBERT
  LINE: Is it hooked on something.
  EXPRESSION: Anxious
- CHARACTER: DALLAS
  LINE: No, it’s coming.
  EXPRESSION: Confident
- CHARACTER: LAMBERT
  LINE: I can’t see anything.
  EXPRESSION: Perplexed
- CHARACTER: Narrator
  LINE: Dallas shines his light down into the hole. Shakes his head.
  EXPRESSION: null
- CHARACTER: DALLAS
  LINE: Line's still moving.
  EXPRESSION: Relieved
- CHARACTER: Narrator
  LINE: A long moment. Dallas shines his light again.
  EXPRESSION: null
- CHARACTER: DALLAS
  LINE: Here he comes.
  EXPRESSION: Anxious
- CHARACTER: Narrator
  LINE: The winch labors heavily.
  EXPRESSION: null
- CHARACTER: DALLAS
  LINE: Get ready to grab him.
  EXPRESSION: Prepared

::SCENE::
LOCATION: Top of Opening
MOOD: Grim
CHARACTERS: Narrator, Dallas, Lambert, Kane
BACKGROUND_IMAGE: top_of_opening.png
BACKGROUND_EDIT: "Kane dangling limply, creature on his face"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Kane appears at the top of the opening. Dangles limply from the wire.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Dallas reaches for him, then recoils.
  EXPRESSION: null
- CHARACTER: DALLAS
  LINE: Look out. There’s something on his face.
  EXPRESSION: Horrified
- CHARACTER: LAMBERT
  LINE: What is it.
  EXPRESSION: Afraid
- CHARACTER: Narrator
  LINE: Kane appears to be completely unconscious. The life form is still wrapped motionless around*his face.
  EXPRESSION: null
- CHARACTER: LAMBERT
  LINE: Oh Jesus.
  EXPRESSION: Terrified
- CHARACTER: DALLAS
  LINE: Don’t touch it.
  EXPRESSION: Urgent
- CHARACTER: Narrator
  LINE: They grapple with Kane’s limp body. Lift him from the hole.
  EXPRESSION: null

::SCENE::
LOCATION: The Nostromo (Exterior)
MOOD: Foreboding
CHARACTERS: Narrator
BACKGROUND_IMAGE: nostromo_exterior.png
BACKGROUND_EDIT: "Sunset, blood-red sky, storm, floodlights"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Atmosphere turning the color of blood. And the sun is down. The ring of floodlights on the ship comes to life. Feebly combatting the darkness and continuing storm.
  EXPRESSION: null

::SCENE::
LOCATION: Bridge / Blister
MOOD: Tense
CHARACTERS: Narrator, Jones (cat), Ripley, Ash
BACKGROUND_IMAGE: bridge_blister.png
BACKGROUND_EDIT: "Dusk, interior of the Nostromo bridge and blister"

::SCRIPT::
- CHARACTER: Narrator
  LINE: INTERCUT: Jones the cat staring through a port opening at the storm. Ripley waiting on the bridge. Ash stares at his inactive monitors.
  EXPRESSION: null
- CHARACTER: ASH
  LINE: We’ve got them. They’re back on the screens.
  EXPRESSION: Alert
- CHARACTER: RIPLEY
  LINE: How many.
  EXPRESSION: Concerned
- CHARACTER: ASH
  LINE: Three blips. They’re coming this way.
  EXPRESSION: Informative
- CHARACTER: Narrator
  LINE: Ripley presses transmitter.
  EXPRESSION: null
- CHARACTER: RIPLEY
  LINE: Dallas. Dallas. Can you hear me.
  EXPRESSION: Anxious
- CHARACTER: DALLAS
  LINE: We hear you. We’re coming back. Kane’s injured -- We’ll need some help getting him in.
  EXPRESSION: Weak
- CHARACTER: ASH
  LINE: I’ll go.
  EXPRESSION: Proactive
- CHARACTER: Narrator
  LINE: Ash moves from the blister. Ripley remains seated at her console.
  EXPRESSION: null

::SCENE::
LOCATION: Engine Room Cubicle
MOOD: Neutral
CHARACTERS: Narrator, Parker, Brett
BACKGROUND_IMAGE: engine_room_cubicle.png
BACKGROUND_EDIT: "Interior of engine room cubicle"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Parker and Brett listening over the intercom.
  EXPRESSION: null

::SCENE::
LOCATION: Landing Leg
MOOD: Urgent
CHARACTERS: Narrator, Dallas, Lambert, Kane
BACKGROUND_IMAGE: landing_leg.png
BACKGROUND_EDIT: "Night, exterior of the Nostromo landing leg"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Dallas and Lambert dragging Kane on a travois towards landing leg.
  EXPRESSION: null

::SCENE::
LOCATION: Passageway Near Airlock
MOOD: Tense
CHARACTERS: Narrator, Ash, Ripley
BACKGROUND_IMAGE: passageway_airlock.png
BACKGROUND_EDIT: "Interior passageway, leading to airlock"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Ash comes down the steps. Hurries to the inner lock door. Presses the wall voice-amp.
  EXPRESSION: null
- CHARACTER: ASH
  LINE: Ripley, I’m by the inner lock hatch.
  EXPRESSION: Informative
- CHARACTER: RIPLEY
  LINE: Okay.
  EXPRESSION: Acknowledging

::SCENE::
LOCATION: Landing Leg
MOOD: Urgent
CHARACTERS: Narrator, Dallas, Lambert, Kane
BACKGROUND_IMAGE: landing_leg_platform.png
BACKGROUND_EDIT: "Night, lift platform at the landing leg"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Dallas and Lambert drag Kane onto lift platform.
  EXPRESSION: null

::SCENE::
LOCATION: Passageway Near Airlock
MOOD: Tense
CHARACTERS: Narrator, Ash
BACKGROUND_IMAGE: passageway_airlock_waiting.png
BACKGROUND_EDIT: "Interior passageway, Ash waiting by the airlock"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Ash waiting.
  EXPRESSION: null

::SCENE::
LOCATION: Bridge / Landing Leg
MOOD: Conflict
CHARACTERS: Narrator, Ripley, Dallas, Lambert, Kane
BACKGROUND_IMAGE: bridge_landing_leg_conflict.png
BACKGROUND_EDIT: "Split screen: Ripley on the bridge, Dallas and Lambert with Kane at the landing leg"

::SCRIPT::
- CHARACTER: Narrator
  LINE: INTERCUT AND VOICE OVERS:
  EXPRESSION: null
- CHARACTER: DALLAS
  LINE: Ripley, are you there.
  EXPRESSION: Anxious
- CHARACTER: RIPLEY
  LINE: Right here.
  EXPRESSION: Calm
- CHARACTER: DALLAS
  LINE: We’re coming up.
  EXPRESSION: Determined
- CHARACTER: Narrator
  LINE: They move onto lift.
  EXPRESSION: null
- CHARACTER: RIPLEY
  LINE: What happened to Kane.
  EXPRESSION: Inquisitive
- CHARACTER: Narrator
  LINE: Pause.
  EXPRESSION: null
- CHARACTER: DALLAS
  LINE: Some kind of organism. It’s attached itself to him. We’ve gotta get him to the infirmary.
  EXPRESSION: Urgent
- CHARACTER: RIPLEY
  LINE: I need a clear definition.
  EXPRESSION: Demanding
- CHARACTER: DALLAS
  LINE: Just open the hatch, Ripley.
  EXPRESSION: Pleading
- CHARACTER: RIPLEY
  LINE: Wait a minute, if we let it in, the ship could be infected. You know the quarantine procedure. Twenty-four hours for decontamination.
  EXPRESSION: Firm
- CHARACTER: DALLAS
  LINE: He could die in twenty-four hours. Open the hatch.
  EXPRESSION: Desperate
- CHARACTER: RIPLEY
  LINE: Listen to me, if I break quarantine we may all die.
  EXPRESSION: Fearful
- CHARACTER: LAMBERT
  LINE: Open the Goddamn hatch. We have to get him inside.
  EXPRESSION: Frantic
- CHARACTER: RIPLEY
  LINE: I can’t. If you were in my position you’d do the same.
  EXPRESSION: Resolute

::SCENE::
LOCATION: Engine Room Cubicle
MOOD: Anticipatory
CHARACTERS: Narrator, Parker, Brett
BACKGROUND_IMAGE: engine_room_cubicle_listening.png
BACKGROUND_EDIT: "Interior of engine room cubicle, Parker and Brett listening"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Parker and Brett listen.
  EXPRESSION: null

::SCENE::
LOCATION: Passageway Near Airlock
MOOD: Confrontational
CHARACTERS: Narrator, Dallas, Ripley, Ash
BACKGROUND_IMAGE: passageway_airlock_confrontation.png
BACKGROUND_EDIT: "Interior passageway, Dallas confronts Ripley via comms, Ash intervenes"

::SCRIPT::
- CHARACTER: DALLAS
  LINE: Ripley, do you hear me.
  EXPRESSION: Demanding
- CHARACTER: RIPLEY
  LINE: I read you. The answer is negative.
  EXPRESSION: Unyielding
- CHARACTER: Narrator
  LINE: Ash hits the emergency switch. A red light goes on. Servo whine. Followed by a solid metallic clunk.
  EXPRESSION: null
- CHARACTER: ASH
  LINE: Inner hatch open.
  EXPRESSION: Triumphant

::SCENE::
LOCATION: Engine Room Cubicle
MOOD: Shocked
CHARACTERS: Narrator, Parker, Brett
BACKGROUND_IMAGE: engine_room_cubicle_reaction.png
BACKGROUND_EDIT: "Interior of engine room cubicle, Parker and Brett react"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Parker and Brett react.
  EXPRESSION: null

::SCENE::
LOCATION: Bridge
MOOD: Disbelief
CHARACTERS: Narrator, Ripley
BACKGROUND_IMAGE: bridge_hatch_open.png
BACKGROUND_EDIT: "Ripley's console flashes 'INNER HATCH OPEN', she reacts with disbelief"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Ripley’s console flashes. INNER HATCH OPEN. She can’t believe what she sees.
  EXPRESSION: null

::SCENE::
LOCATION: Passageway Near Airlock
MOOD: Grim
CHARACTERS: Narrator, Dallas, Lambert, Kane, Ash, Parker
BACKGROUND_IMAGE: passageway_airlock_entry.png
BACKGROUND_EDIT: "Interior passageway, Dallas and Lambert carrying Kane, Ash and Parker recoil"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Dallas and Lambert stagger into passageway. Carry Kane’s body between them. Dallas pulls off his helmet.
  EXPRESSION: null
- CHARACTER: DALLAS
  LINE: Stay clear.
  EXPRESSION: Warning
- CHARACTER: Narrator
  LINE: Ash and Parker move back.
  EXPRESSION: null
- CHARACTER: ASH
  LINE: God.
  EXPRESSION: Horrified
- CHARACTER: PARKER
  LINE: Is it alive.
  EXPRESSION: Afraid
- CHARACTER: LAMBERT
  LINE: I don’t know, but don’t touch it.
  EXPRESSION: Terrified
- CHARACTER: DALLAS
  LINE: Take him to the infirmary.
  EXPRESSION: Determined

::SCENE::
LOCATION: Infirmary
MOOD: Tense
CHARACTERS: Narrator, Kane, Ash, Brett, Dallas
BACKGROUND_IMAGE: infirmary.png
BACKGROUND_EDIT: "Interior of a medical bay, Kane is on a cot with a helmet on his head."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Kane’s helmet. Hands begin to open it with a laser cutter. The helmet separates easily. The two halves part...
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: ...the life form slowly pulsing on Kane’s face.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Dallas hesitates, then puts his hand on the small Creature. Tries to pull it free. Unsuccessful. The Alien remains anchored to Kane’s tissue.
  EXPRESSION: null

::PATHS::
- CHOICE: "Ash attempts to remove the creature."
  TARGET: corridor_outside_infirmary_window
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Corridor Outside Infirmary Window
MOOD: Anxious
CHARACTERS: Narrator, Lambert, Parker, Brett, Ripley
BACKGROUND_IMAGE: corridor_outside_infirmary.png
BACKGROUND_EDIT: "Exterior view of the infirmary window, showing the interior."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Lambert, Parker and Brett watch through the infirmary window. Ripley appears. Lambert turns and looks at her. A long moment.
  EXPRESSION: null
- CHARACTER: Lambert
  LINE: You were going to leave us out there.
  EXPRESSION: Accusatory
- CHARACTER: Parker
  LINE: Maybe she should have. Who the hell knows what that is.
  EXPRESSION: Suspicious
- CHARACTER: Brett
  LINE: Right.
  EXPRESSION: Neutral
- CHARACTER: Narrator
  LINE: Ripley looks at Lambert. A moment.
  EXPRESSION: null
- CHARACTER: Ripley
  LINE: I was trying to do my job. Let’s leave it at that.
  EXPRESSION: Defensive
- CHARACTER: Narrator
  LINE: Lambert gives her a curt nod.
  EXPRESSION: null
- CHARACTER: Ripley
  LINE: What happened out there.
  EXPRESSION: Inquisitive
- CHARACTER: Lambert
  LINE: We went into the derelict. There were no signs of life -- That transmission must have been going for centuries.
  EXPRESSION: Somber
- CHARACTER: Ripley
  LINE: What about the crew.
  EXPRESSION: Inquisitive
- CHARACTER: Lambert
  LINE: Only found one of them -- Looked like he’d been shot.
  EXPRESSION: Somber
- CHARACTER: Ripley
  LINE: And Kane --
  EXPRESSION: Concerned
- CHARACTER: Lambert
  LINE: He volunteered to search the lower level alone. He found some kind of eggs. We told him not to touch them. Something happened in there -- When we pulled him out, it was on his face.
  EXPRESSION: Distressed

::PATHS::
- CHOICE: "Return to the infirmary."
  TARGET: infirmary
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Infirmary
MOOD: Grim
CHARACTERS: Narrator, Ash, Kane, Dallas
BACKGROUND_IMAGE: infirmary.png
BACKGROUND_EDIT: "Interior of a medical bay, Kane is on a cot, connected to a medical machine."

::SCRIPT::
- CHARACTER: Ash
  LINE: We better let the machine work on him.
  EXPRESSION: Clinical
- CHARACTER: Narrator
  LINE: Ash presses a switch. The machine lights up. Kane is sucked into a slot in the wall. Visible inside through the glass layer. A blinding colored light performs antisepsis. Two video monitors pop on. Ash punches three buttons. An X-ray image appears. A color depiction of Kane’s head and upper torso. The Alien is clearly visible. A maze of complicated biology. Kane’s Jaws are forced open. The Creature has extruded a long tube down his mouth and throat. The appendage ending at the base of the esophagus.
  EXPRESSION: null
- CHARACTER: Dallas
  LINE: It’s got something down his Goddamn throat.
  EXPRESSION: Astounded
- CHARACTER: Ash
  LINE: That must be how it’s getting oxygen to him.
  EXPRESSION: Analytical
- CHARACTER: Dallas
  LINE: It doesn't make sense, it paralyzes him, puts him into a coma, then keeps him alive. We have to get it off him somehow.
  EXPRESSION: Frustrated
- CHARACTER: Ash
  LINE: At the moment the Creature is keeping him alive. If we remove it we might terminate Kane --
  EXPRESSION: Cautionary
- CHARACTER: Dallas
  LINE: We have to take the chance and cut it off him.
  EXPRESSION: Determined
- CHARACTER: Ash
  LINE: You'll take the responsibility.
  EXPRESSION: Challenging
- CHARACTER: Dallas
  LINE: That’s right.
  EXPRESSION: Resolute

::PATHS::
- CHOICE: "Attempt to surgically remove the creature."
  TARGET: infirmary_surgery_result
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Infirmary
MOOD: Horrifying
CHARACTERS: Narrator, Dallas, Ash, Kane
BACKGROUND_IMAGE: infirmary.png
BACKGROUND_EDIT: "Interior of a medical bay, Kane on a cot, with surgical laser cutting the creature."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Dallas presses a switch, Kane slides back out of the booth. Ash takes a surgical laser blade from the case. He manipulates the knife until he has a comfortable grip. Flicks a small button with his thumb. The blade begins to hum. Touches the scalpel to the Creature. The electronic blade slides effortlessly downward.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Suddenly a urine-like fluid begins to drip from the wound.
  EXPRESSION: null
- CHARACTER: Ash
  LINE: Starting to bleed.
  EXPRESSION: Neutral
- CHARACTER: Narrator
  LINE: The liquid flows onto the bedding next to Kane's head. Starts to hiss. Smoke curls up from the stain. Next the yellow fluid eats a hole through the bunk bed. Then drips onto the deck below. Metal bubbling and sizzling. More smoke rises.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Dallas frantically applies pressure to the wound. In the process, some of the fluid gets on Dallas’ gloves. They begin to smoke. Dallas leaps back, pulls them off. They run into the corridor, coughing and choking from the fumes.
  EXPRESSION: null

::PATHS::
- CHOICE: "Flee the infirmary as the acid drips."
  TARGET: passageway_outside_infirmary
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Passageway Outside Infirmary
MOOD: Panicked
CHARACTERS: Narrator, Brett, Dallas, Ripley, Parker
BACKGROUND_IMAGE: passageway_outside_infirmary.png
BACKGROUND_EDIT: "Interior corridor, showing escape route."

::SCRIPT::
- CHARACTER: Brett
  LINE: Shit. It’s going to eat through the decks and out the hull --
  EXPRESSION: Terrified
- CHARACTER: Narrator
  LINE: They start to run for the companionway.
  EXPRESSION: null

::PATHS::
- CHOICE: "Descend to 'B' Deck."
  TARGET: passageway_b_deck
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Passageway "B" Deck
MOOD: Urgent
CHARACTERS: Narrator, Dallas, Ripley, Parker, Brett
BACKGROUND_IMAGE: passageway_b_deck.png
BACKGROUND_EDIT: "Interior corridor with emergency lighting."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Dallas wrenches an emergency lamp from a socket. Hurls himself down a companionway. The others follow.
  EXPRESSION: null
- CHARACTER: Dallas
  LINE: There.
  EXPRESSION: Urgent
- CHARACTER: Narrator
  LINE: A droplet of fluid is sizzling on the ceiling bulkhead. It oozes down. Drips to the deck. Continues to bubble. Then goes through the bulkhead.
  EXPRESSION: null
- CHARACTER: Ripley
  LINE: What can we put under it.
  EXPRESSION: Desperate

::PATHS::
- CHOICE: "Descend to 'C' Deck."
  TARGET: maintenance_corridor_c_deck
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Maintenance Corridor "C" Deck
MOOD: Cautious
CHARACTERS: Narrator, Dallas, Ripley, Parker, Brett
BACKGROUND_IMAGE: maintenance_corridor_c_deck.png
BACKGROUND_EDIT: "Dimly lit maintenance corridor."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Dallas moves cautiously down the passageway. Followed by Ripley, Parker and Brett.
  EXPRESSION: null

::PATHS::
- CHOICE: "Enter the maintenance area."
  TARGET: maintenance_area_c_deck
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Maintenance Area "C" Deck
MOOD: Relieved
CHARACTERS: Narrator, Dallas, Ripley, Parker, Brett
BACKGROUND_IMAGE: maintenance_area_c_deck.png
BACKGROUND_EDIT: "Industrial maintenance area, pipes and machinery."

::SCRIPT::
- CHARACTER: Narrator
  LINE: They enter the maintenance area. Look up to the ceiling bulkhead. The acid bubbles.
  EXPRESSION: null
- CHARACTER: Parker
  LINE: Don’t get under it.
  EXPRESSION: Wary
- CHARACTER: Narrator
  LINE: The acid drips to the deck. Continues to sizzle. Slower.
  EXPRESSION: null
- CHARACTER: Ripley
  LINE: Looks like it’s losing steam.
  EXPRESSION: Hopeful
- CHARACTER: Narrator
  LINE: Dallas fishes a pen out of his pocket. Probes the hole in the deck.
  EXPRESSION: null
- CHARACTER: Dallas
  LINE: It’s stopped penetrating.
  EXPRESSION: Relieved
- CHARACTER: Brett
  LINE: Yeah. After it penetrated two levels.
  EXPRESSION: Sarcastic
- CHARACTER: Narrator
  LINE: Dallas straightens up. Starts to put the pen back into his pocket. Changes his mind and stands holding it by the end.
  EXPRESSION: null
- CHARACTER: Dallas
  LINE: I’ve never seen anything like that, except molecular acid --
  EXPRESSION: Amazed
- CHARACTER: Brett
  LINE: This thing uses it for blood.
  EXPRESSION: Grim
- CHARACTER: Parker
  LINE: Wonderful defense mechanism. You don’t dare kill it.
  EXPRESSION: Resigned
- CHARACTER: Narrator
  LINE: They start back towards the companionway.
  EXPRESSION: null

::PATHS::
- CHOICE: "Return to the infirmary."
  TARGET: infirmary_return
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Infirmary
MOOD: Eerie
CHARACTERS: Narrator, Dallas, Ash, Kane, Parker
BACKGROUND_IMAGE: infirmary.png
BACKGROUND_EDIT: "Interior of a medical bay, Kane is on a cot, motionless."

::SCRIPT::
- CHARACTER: Narrator
  LINE: They return. Kane still motionless on the bunk. The Alien remains secured to his face. Wound completely healed over.
  EXPRESSION: null
- CHARACTER: Parker
  LINE: Any of the acid get on him.
  EXPRESSION: Inquisitive
- CHARACTER: Narrator
  LINE: Dalla
  EXPRESSION: null

::SCENE::
LOCATION: INFIRMARY - CONTINUOUS
MOOD: Tense
CHARACTERS: DALLAS, LAMBERT, ASH, RIPLEY, KANE
BACKGROUND_IMAGE: infirmary_continuous.png
BACKGROUND_EDIT: "Medical bay, Kane on a diagnostic table, faces gathered around"

::SCRIPT::
- CHARACTER: Narrator
  LINE: s approaches, peers at Kane’s head.
  EXPRESSION: null
- CHARACTER: DALLAS
  LINE: Doesn't look like it.
  EXPRESSION: null
- CHARACTER: BRETT
  LINE: Is it still dripping that crap.
  EXPRESSION: null
- CHARACTER: ASH
  LINE: Healed over.
  EXPRESSION: null
- CHARACTER: LAMBERT
  LINE: There must be some way we can get it off.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Ash looks at Dallas.
  EXPRESSION: null
- CHARACTER: ASH
  LINE: I don't think you ought to try again. It didn't work out too well last time.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Dallas gives him a look in return.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Ripley presses a button.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Kane slides back into the diagnostic coffin.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: More buttons pressed.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Displays light up again, showing the different parts of Kane’s body.
  EXPRESSION: null
- CHARACTER: ASH
  LINE: I better get some intravenous feeding started. So far I can’t tell what the Alien has absorbed from his system.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The machine begins to process Kane’s body.
  EXPRESSION: null
- CHARACTER: RIPLEY
  LINE: What's the stain on his lungs.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The X-ray reveals a spreading dark blot in the chest cavity. At the center, the stain is completely opaque.
  EXPRESSION: null
- CHARACTER: ASH
  LINE: Whatever it is, it’s blocking the X-ray.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: A long moment.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The stain spreads.
  EXPRESSION: null
- CHARACTER: BRETT
  LINE: What happens now.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Ash sets aside his partially melted pert. Looks at Dallas.
  EXPRESSION: null
- CHARACTER: DALLAS
  LINE: You go back to work.
  EXPRESSION: null

::PATHS::
- CHOICE: "Go back to work"
  TARGET: engine_room_cubicle
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: ENGINE ROOM CUBICLE
MOOD: Mundane
CHARACTERS: BRETT, PARKER
BACKGROUND_IMAGE: engine_room_cubicle.png
BACKGROUND_EDIT: "Maintenance area, Brett working on equipment, Parker supervising"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Brett at work in the cubicle. Parker, supervising him.
  EXPRESSION: null
- CHARACTER: BRETT
  LINE: I think I’ve got it. Give it a try.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Parker pushes a button. Negative reaction on his monitor.
  EXPRESSION: null
- CHARACTER: PARKER
  LINE: Nothing.
  EXPRESSION: null
- CHARACTER: BRETT
  LINE: Damn. I was sure that was it.
  EXPRESSION: null
- CHARACTER: PARKER
  LINE: Well, it isn’t. Try the next one.
  EXPRESSION: null
- CHARACTER: BRETT
  LINE: Right.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Adjusts several toggles.
  EXPRESSION: null
- CHARACTER: RIPLEY
  LINE: What’s happening.
  EXPRESSION: null
- CHARACTER: PARKER
  LINE: This goddamn woman. I’ll tell her what’s happening. My Johnson is happening.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: (punches the communicator)
  EXPRESSION: null
- CHARACTER: PARKER
  LINE: A lot of hard work. Real work.
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue working"
  TARGET: bridge_night
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: BRIDGE - NIGHT
MOOD: Confrontational
CHARACTERS: PARKER, RIPLEY
BACKGROUND_IMAGE: bridge_night.png
BACKGROUND_EDIT: "Ship's bridge, dim lighting, Parker speaking through comms"

::SCRIPT::
- CHARACTER: PARKER
  LINE: You ought to try it sometime.
  EXPRESSION: null
- CHARACTER: RIPLEY
  LINE: I’ve got the toughest job on this ship.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Derisive laugh from Parker through the speaker.
  EXPRESSION: null
- CHARACTER: RIPLEY
  LINE: I have to listen to your, bullshit.
  EXPRESSION: null

::PATHS::
- CHOICE: "Return to work"
  TARGET: engine_room_cubicle_return
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: ENGINE ROOM CUBICLE
MOOD: Frustrated
CHARACTERS: PARKER, RIPLEY
BACKGROUND_IMAGE: engine_room_cubicle_return.png
BACKGROUND_EDIT: "Maintenance area, Parker speaking to Ripley through comms"

::SCRIPT::
- CHARACTER: PARKER
  LINE: Get off my back.
  EXPRESSION: null
- CHARACTER: RIPLEY
  LINE: I’ll get off your back when 12 module is fixed.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: She clicks off. Parker turns away.
  EXPRESSION: null
- CHARACTER: PARKER
  LINE: Smart-mouth broad.
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue repairs"
  TARGET: infirmary_ash
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: INFIRMARY
MOOD: Concerned
CHARACTERS: ASH, KANE, RIPLEY
BACKGROUND_IMAGE: infirmary_ash.png
BACKGROUND_EDIT: "Medical bay, Kane on life support, Ash working on equipment"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Ash running test on the equipment. Kane respirating on the view screens above. Still deep within a coma. All instruments recording his life processes. The Alien’s position unchanged. Ripley approaches. Sits near Ash.
  EXPRESSION: null
- CHARACTER: RIPLEY
  LINE: Anything new.
  EXPRESSION: null
- CHARACTER: ASH
  LINE: He’s holding, no changes.
  EXPRESSION: null
- CHARACTER: RIPLEY
  LINE: What about the Creature?
  EXPRESSION: null
- CHARACTER: ASH
  LINE: It’s got an outer layer of protein polysaccharides. Plus it’s constantly sloughing off cells and replacing them with polarized silicon. Which gives it prolonged resistance to adverse environmental conditions -- That enough for you?
  EXPRESSION: null
- CHARACTER: RIPLEY
  LINE: Plenty. What’s it mean.
  EXPRESSION: null
- CHARACTER: ASH
  LINE: Interesting combination of elements making it practically invulnerable.
  EXPRESSION: null
- CHARACTER: RIPLEY
  LINE: Is that why you let it in.
  EXPRESSION: null
- CHARACTER: ASH
  LINE: I was following a direct order. Remember.
  EXPRESSION: null
- CHARACTER: RIPLEY
  LINE: While Dallas and Kane are off the ship, I’m Senior Officer.
  EXPRESSION: null
- CHARACTER: ASH
  LINE: Yes, of course -- I forgot.
  EXPRESSION: null
- CHARACTER: RIPLEY
  LINE: You also forgot the science division’s basic quarantine law.
  EXPRESSION: null
- CHARACTER: ASH
  LINE: No. That I didn’t forget.
  EXPRESSION: null
- CHARACTER: RIPLEY
  LINE: You just broke it.
  EXPRESSION: null
- CHARACTER: ASH
  LINE: What would you have done with Kane -- His only chance at staying alive was to get into the infirmary.
  EXPRESSION: null
- CHARACTER: RIPLEY
  LINE: By breaking quarantine procedure you risk everybody’s life.
  EXPRESSION: null
- CHARACTER: ASH
  LINE: Maybe I should have let him die out there. Maybe I have jeopardized the rest of us -- It’s a risk I’m willing to take.
  EXPRESSION: null
- CHARACTER: RIPLEY
  LINE: This is your official position as a science officer. Not exactly out of the manual --
  EXPRESSION: null
- CHARACTER: ASH
  LINE: The first position of science is the protection and betterment of human life. I take my responsibility as seriously as you do -- you do your job and I’ll do mine.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Ripley stands looks at Ash. They walk o.s.
  EXPRESSION: null

::PATHS::
- CHOICE: "Leave the infirmary"
  TARGET: mess_hall
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: MESS HALL
MOOD: Relaxed
CHARACTERS: LAMBERT, JONES
BACKGROUND_IMAGE: mess_hall.png
BACKGROUND_EDIT: "Ship's mess hall, Lambert playing with string, Jones the cat"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Lambert playing with some string, amusing Jones. Cat's Cradle. Both looking bored.
  EXPRESSION: null

::PATHS::
- CHOICE: "Return to work"
  TARGET: engine_room_cubicle_final
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: ENGINE ROOM CUBICLE
MOOD: Focused
CHARACTERS: PARKER, BRETT
BACKGROUND_IMAGE: engine_room_cubicle_final.png
BACKGROUND_EDIT: "Maintenance area, Parker and Brett working on equipment"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Parker and Brett at work on the final intake screen.
  EXPRESSION: null

::PATHS::
- CHOICE: "Check on Dallas"
  TARGET: narcissus
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: NARCISSUS
MOOD: Pensive
CHARACTERS: DALLAS
BACKGROUND_IMAGE: narcissus.png
BACKGROUND_EDIT: "Ship's bridge or personal quarters, Dallas listening to tape"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Dallas listening to a primitive tape. His foot tapping with the rhythm. Beep. An interruption on the communicator.
  EXPRESSION: null
- CHARACTER: DALLAS
  LINE: Dallas.
  EXPRESSION: null
- CHARACTER: ASH
  LINE: I think you should have a look at Kane. Something's happened.
  EXPRESSION: null
- CHARACTER: DALLAS
  LINE: Serious.
  EXPRESSION: null
- CHARACTER: ASH
  LINE: Interesting.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Dallas exits.
  EXPRESSION: null

::PATHS::
- CHOICE: "Go to the infirmary"
  TARGET: corridor_infirmary_window
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: CORRIDOR OUTSIDE INFIRMARY WINDOW
MOOD: Alarming
CHARACTERS: ASH, DALLAS, RIPLEY
BACKGROUND_IMAGE: corridor_infirmary_window.png
BACKGROUND_EDIT: "Corridor outside infirmary, Ash and Dallas looking through window, Ripley joins"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Ash stares through window. Dallas joins him. Ripley appears behind. A long pause.
  EXPRESSION: null
- CHARACTER: DALLAS
  LINE: It’s gone.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Kane’s prone form. The Alien is no longer on his face. Kane still unconscious, but continues to breathe. Face covered with sucker marks.
  EXPRESSION: null
- CHARACTER: RIPLEY
  LINE: The door is closed. It must still be in there.
  EXPRESSION: null
- CHARACTER: ASH
  LINE: We can’t open the door. We don’t want to let it out.
  EXPRESSION: null
- CHARACTER: RIPLEY
  LINE: Yeah, I remember. We can’t grab it. We can’t kill it --
  EXPRESSION: null
- CHARACTER: DALLAS
  LINE: Maybe we can catch it.
  EXPRESSION: null
- CHARACTER: ASH
  LINE: As long as we’re careful not to damage it.
  EXPRESSION: null

::PATHS::
- CHOICE: "Enter the infirmary"
  TARGET: infirmary_search
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: INFIRMARY
MOOD: Cautious
CHARACTERS: DALLAS, ASH, RIPLEY
BACKGROUND_IMAGE: infirmary_search.png
BACKGROUND_EDIT: "Infirmary, characters cautiously searching the room"

::SCRIPT::
- CHARACTER: Narrator
  LINE: They enter cautiously. Dallas begins moving slowly around the room. Picking up a stainless steel tray. Looking. Ash and Ripley do the same. Ripley bends down and peers under the bunk. Nothing. She stands. Doesn’t see
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue searching"
  TARGET: end
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Ledge
MOOD: Suspense
CHARACTERS: Narrator, Ripley, Alien, Dallas
BACKGROUND_IMAGE: ledge.png
BACKGROUND_EDIT: "Alien on a ledge above Ripley"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The Alien on a ledge above her.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Her shoulder brushes against the Creature.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: It drops onto her.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: She screams. Twists.
  EXPRESSION: Terrified
- CHARACTER: Narrator
  LINE: The Alien drops to the floor.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Then lies motionless. Its skin faded to a dead-looking grey.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Ripley doesn't raise her eyes from the Creature. Prods the Alien.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: No response.
  EXPRESSION: null
- CHARACTER: DALLAS
  LINE: I think it's dead. You okay.
  EXPRESSION: Concerned
- CHARACTER: RIPLEY
  LINE: Yeah.
  EXPRESSION: Shaken
- CHARACTER: Narrator
  LINE: She carefully touches the Creature with a metal probe. Fishes the motionless life-form into the tray. Quickly closes the lid. Lifts it onto a stainless steel table.
  EXPRESSION: null

::PATHS::
- CHOICE: "Examine the specimen"
  TARGET: specimen_examination
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Specimen Examination Table
MOOD: Scientific Curiosity
CHARACTERS: Narrator, Ash, Ripley, Dallas
BACKGROUND_IMAGE: specimen_examination.png
BACKGROUND_EDIT: "Bright light trained on the Alien, supine position"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Bright light trained on the Alien. The Creature in a supine position.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Ash touches at the Alien with a surgical instrument.
  EXPRESSION: null
- CHARACTER: ASH
  LINE: Look at those suckers. No wonder we couldn't get it off him.
  EXPRESSION: Intrigued
- CHARACTER: RIPLEY
  LINE: Where's its mouth.
  EXPRESSION: Curious
- CHARACTER: ASH
  LINE: It’s this tube-like thing, up in here. It’s hardening. It’s dead. No life sign whatever.
  EXPRESSION: Clinical
- CHARACTER: RIPLEY
  LINE: Let’s get rid of it.
  EXPRESSION: Uneasy
- CHARACTER: ASH
  LINE: This has to go back. This is our first contact with a specimen like this. All kinds of tests need to be run.
  EXPRESSION: Determined
- CHARACTER: RIPLEY
  LINE: That thing bled acid. God knows what it’ll do when it’s dead.
  EXPRESSION: Worried
- CHARACTER: ASH
  LINE: I think it’s safe to assume it’s not a zombie -- Dallas, we have to keep this specimen.
  EXPRESSION: Firm
- CHARACTER: Narrator
  LINE: Pause.
  EXPRESSION: null
- CHARACTER: DALLAS
  LINE: You’re the Science Officer. It’s your decision.
  EXPRESSION: Resigned
- CHARACTER: ASH
  LINE: Then it's made -- I’ll seal it in a stasis tube.
  EXPRESSION: Decisive
- CHARACTER: Narrator
  LINE: Pause.
  EXPRESSION: null
- CHARACTER: RIPLEY
  LINE: What about Kane.
  EXPRESSION: Concerned

::PATHS::
- CHOICE: "Check on Kane"
  TARGET: kane_status
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Specimen Examination Table
MOOD: Medical Concern
CHARACTERS: Narrator, Ash, Ripley, Dallas
BACKGROUND_IMAGE: kane_status.png
BACKGROUND_EDIT: "Ash turns back to Kane's bunk, studying life support gauges"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Ash turns back to the bunk. Studies the life support gauges.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Kane continues to breathe steadily.
  EXPRESSION: null
- CHARACTER: ASH
  LINE: Running a fever. And still unconscious. The machine will bring his temperature down. His vital functions are strong -- who knows, he may make it.
  EXPRESSION: Cautiously Optimistic
- CHARACTER: Narrator
  LINE: Ash begins to seal the Alien in a large vacuum tube.
  EXPRESSION: null
- CHARACTER: RIPLEY
  LINE: I need some coffee.
  EXPRESSION: Exhausted
- CHARACTER: Narrator
  LINE: She turns and walks away.
  EXPRESSION: null

::PATHS::
- CHOICE: "Go to the bridge"
  TARGET: bridge_corridor
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Black Corridor to Bridge
MOOD: Confrontational
CHARACTERS: Narrator, Ripley, Dallas
BACKGROUND_IMAGE: bridge_corridor.png
BACKGROUND_EDIT: "Dark corridor leading to the bridge"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Ripley and Dallas.
  EXPRESSION: null
- CHARACTER: RIPLEY
  LINE: How could you leave that kind of decision to him.
  EXPRESSION: Accusatory
- CHARACTER: DALLAS
  LINE: I just run the ship. Anything that has to do with science division, Ash has the final word.
  EXPRESSION: Defensive
- CHARACTER: RIPLEY
  LINE: How does that happen.
  EXPRESSION: Disbelieving
- CHARACTER: DALLAS
  LINE: Same way everything else happens. Orders from the Company.
  EXPRESSION: Resigned
- CHARACTER: RIPLEY
  LINE: Since when is that standard procedure.
  EXPRESSION: Skeptical
- CHARACTER: DALLAS
  LINE: Standard procedure is do what they tell you. Besides, I only know about flying. I haul cargo for a living.
  EXPRESSION: Pragmatic
- CHARACTER: RIPLEY
  LINE: Did you ship out with Ash before.
  EXPRESSION: Inquisitive
- CHARACTER: DALLAS
  LINE: First time. I went five hauls with another science man. Then two days before we left Thedus, they replaced him with Ash.
  EXPRESSION: Neutral
- CHARACTER: Narrator
  LINE: She looks at him.
  EXPRESSION: null
- CHARACTER: DALLAS
  LINE: So what. They replaced my warrant officer with you.
  EXPRESSION: Indifferent
- CHARACTER: RIPLEY
  LINE: I don’t trust him.
  EXPRESSION: Vehement
- CHARACTER: DALLAS
  LINE: I don’t trust anybody -- What’s holding up the repairs.
  EXPRESSION: Impatient
- CHARACTER: RIPLEY
  LINE: They’re pretty much finished now.
  EXPRESSION: Informative
- CHARACTER: DALLAS
  LINE: Why didn’t you say so?
  EXPRESSION: Exasperated
- CHARACTER: RIPLEY
  LINE: There are still some things left to do.
  EXPRESSION: Frank
- CHARACTER: DALLAS
  LINE: Like what?
  EXPRESSION: Demanding
- CHARACTER: RIPLEY
  LINE: We’re blind on B and C decks. Reserve power systems blown.
  EXPRESSION: Urgent
- CHARACTER: DALLAS
  LINE: That’s crap. We can take off without them.
  EXPRESSION: Dismissive
- CHARACTER: RIPLEY
  LINE: Is that a good idea.
  EXPRESSION: Cautious
- CHARACTER: DALLAS
  LINE: I want to get out of here. Let’s get this turkey off the ground.
  EXPRESSION: Determined

::PATHS::
- CHOICE: "Proceed to the bridge"
  TARGET: bridge_takeoff
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Planet - Sunrise
MOOD: Impending Departure
CHARACTERS: Narrator, Nostromo
BACKGROUND_IMAGE: planet_sunrise.png
BACKGROUND_EDIT: "Nostromo engines roaring, emitting superheated air, ship vibrating"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The Nostromo’s engines roaring. Belching out streams of superheated air. The starship vibrates.
  EXPRESSION: null

::PATHS::
- CHOICE: "Initiate takeoff"
  TARGET: bridge_takeoff_action
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Bridge - Sunrise
MOOD: Tense Departure
CHARACTERS: Narrator, Dallas, Ripley, Parker, Brett, Lambert
BACKGROUND_IMAGE: bridge_sunrise.png
BACKGROUND_EDIT: "Crew at their posts during sunrise"

::SCRIPT::
- CHARACTER: DALLAS
  LINE: How do we look down there?
  EXPRESSION: Inquiring
- CHARACTER: Narrator
  LINE: INT. ENGINE ROOM CUBICLE
  EXPRESSION: null
- CHARACTER: PARKER
  LINE: Okay, but remember this is a patch job. If we hit too much turbulence the cells will blow -- and that's all she said.
  EXPRESSION: Warning
- CHARACTER: BRETT
  LINE: So take it easy.
  EXPRESSION: Calm
- CHARACTER: Narrator
  LINE: INT. BRIDGE - SUNRISE
  EXPRESSION: null
- CHARACTER: DALLAS
  LINE: I hear you. Ripley, take us up a hundred meters and retract the landing struts.
  EXPRESSION: Commanding
- CHARACTER: RIPLEY
  LINE: Up a hundred.
  EXPRESSION: Affirmative

::PATHS::
- CHOICE: "Retract landing struts"
  TARGET: planet_takeoff
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Planet - Sunrise
MOOD: Lifting Off
CHARACTERS: Narrator, Nostromo
BACKGROUND_IMAGE: planet_takeoff.png
BACKGROUND_EDIT: "Nostromo lifts off, hovers above the ground on beams of shimmering flame, landing struts folding"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The Nostromo lifts off, hovers above the ground on beams of shimmering flame. The landing struts begin folding.
  EXPRESSION: null

::PATHS::
- CHOICE: "Confirm strut retraction"
  TARGET: bridge_strut_retraction
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Bridge - Day
MOOD: Initiating Ascent
CHARACTERS: Narrator, Ripley, Dallas
BACKGROUND_IMAGE: bridge_strut_retraction.png
BACKGROUND_EDIT: "Thump sound as struts retract"

::SCRIPT::
- CHARACTER: Narrator
  LINE: We hear the thump as the struts retract.
  EXPRESSION: null
- CHARACTER: RIPLEY
  LINE: Struts retracted.
  EXPRESSION: Affirmative
- CHARACTER: DALLAS
  LINE: Okay, Ripley, it’s all yours.
  EXPRESSION: Trusting
- CHARACTER: Narrator
  LINE: Ripley pushes a lever forward. The engines begin to thunder
  EXPRESSION: null
- CHARACTER: RIPLEY
  LINE: Rolling up the G’s. And here we go.
  EXPRESSION: Focused

::PATHS::
- CHOICE: "Begin ascent"
  TARGET: nostromo_surge
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Nostromo - Day
MOOD: Accelerating
CHARACTERS: Narrator, Nostromo
BACKGROUND_IMAGE: nostromo_surge.png
BACKGROUND_EDIT: "Ship begins to surge forward, accelerating upward through the dense atmosphere"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The ship begins to surge forward. Accelerating upward through the dense atmosphere.
  EXPRESSION: null

::PATHS::
- CHOICE: "Monitor ascent"
  TARGET: bridge_ascent_monitor
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Bridge - Day
MOOD: Ascending
CHARACTERS: Narrator, Lambert, Ripley, Dallas
BACKGROUND_IMAGE: bridge_ascent_monitor.png
BACKGROUND_EDIT: "Ship ascending, artificial gravity engaged"

::SCRIPT::
- CHARACTER: LAMBERT
  LINE: One kilometer on ascension.
  EXPRESSION: Reporting
- CHARACTER: RIPLEY
  LINE: Engage artificial gravity.
  EXPRESSION: Directing
- CHARACTER: Narrator
  LINE: Lambert throws a switch.
  EXPRESSION: null
- CHARACTER: LAMBERT
  LINE: Engaged.
  EXPRESSION: Confirming
- CHARACTER: RIPLEY
  LINE: I’m altering the vector now.
  EXPRESSION: Precise
- CHARACTER: Narrator
  LINE: A huge tremor runs throughout the ship.
  EXPRESSION: null
- CHARACTER: DALLAS
  LINE: What was that?
  EXPRESSION: Alarmed
- CHARACTER: Narrator
  LINE: In answer, the intercom beeps.
  EXPRESSION: null
- CHARACTER: PARKER’S VOICE
  LINE: Starboard quad’s overheating. I’m shutting it down.
  EXPRESSION: Urgent
- CHARACTER: DALLAS
  LINE: Just hold us together till we’re beyond G1, that’s all.
  EXPRESSION: Commanding
- CHARACTER: Narrator
  LINE: The pitch of the engines changes.
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue ascent"
  TARGET: nostromo_angled_flight
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Nostromo - Day
MOOD: Erratic Flight
CHARACTERS: Narrator, Nostromo
BACKGROUND_IMAGE: nostromo_angled_flight.png
BACKGROUND_EDIT: "Ship moves at an acute angle, slicing through boiling clouds, black smoke from an engine"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The ship moves at an acute angle. Slices through the boiling clouds. Black smoke pouring from one engine.
  EXPRESSION: null

::PATHS::
- CHOICE: "Assess engine issue"
  TARGET: engine_room_frenzy
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Engine Room Cubicle
MOOD: Frantic Repairs
CHARACTERS: Narrator, Parker, Brett
BACKGROUND_IMAGE: engine_room_frenzy.png
BACKGROUND_EDIT: "Parker and Brett in a frenzy of activity amidst dust and overheating engines"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Parker and Brett in a frenzy of activity.
  EXPRESSION: null
- CHARACTER: BRETT
  LINE: Dust is clogging the damn intakes again. Number two’s overheating.
  EXPRESSION: Frustrated
- CHARACTER: PARKER
  LINE: Spit on it fo
  EXPRESSION: Desperate

::SCENE::
LOCATION: BRIDGE
MOOD: Relief
CHARACTERS: Narrator, Crew
BACKGROUND_IMAGE: bridge_clouds.png
BACKGROUND_EDIT: "View of clouds from bridge windows"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Outside the windows, clouds, clouds, clouds.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Another tremor runs through the ship.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The crew’s eyes riveted to their instruments.
  EXPRESSION: null

::SCENE::
LOCATION: NOSTROMO EXTERIOR
MOOD: Triumph
CHARACTERS: Narrator
BACKGROUND_IMAGE: nostromo_space_clouds.png
BACKGROUND_EDIT: "Nostromo clearing cloud layer into space"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The ship clears the top of the cloud layer.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Bursts out into star-sprinkled space.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Trailing a wake of clouds.
  EXPRESSION: null

::SCENE::
LOCATION: BRIDGE
MOOD: Exultation
CHARACTERS: Narrator, Crew, RIPLEY
BACKGROUND_IMAGE: bridge_celebration.png
BACKGROUND_EDIT: "Bridge interior, crew celebrating"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The crew cheer.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Wave their arms in exultation.
  EXPRESSION: null
- CHARACTER: RIPLEY
  LINE: We made it. Damn. We made it.
  EXPRESSION: Relieved

::SCENE::
LOCATION: ENGINE ROOM CUBICLE
MOOD: Casual
CHARACTERS: Parker
BACKGROUND_IMAGE: engine_room_beer.png
BACKGROUND_EDIT: "Parker in a cramped engine room cubicle, opening a beer"

::SCRIPT::
- CHARACTER: Parker
  LINE: 65.
  EXPRESSION: Casual
- CHARACTER: Parker
  LINE: Walk in the park. When we fix something it stays fixed.
  EXPRESSION: Confident

::SCENE::
LOCATION: BRIDGE
MOOD: Determined
CHARACTERS: DALLAS
BACKGROUND_IMAGE: bridge_setting_course.png
BACKGROUND_EDIT: "Bridge interior, Dallas at command"

::SCRIPT::
- CHARACTER: DALLAS
  LINE: Let’s pick up the money and go home. Put her in the garage.
  EXPRESSION: Determined

::SCENE::
LOCATION: NOSTROMO EXTERIOR
MOOD: Procedural
CHARACTERS: Narrator
BACKGROUND_IMAGE: nostromo_refinery_rendezvous.png
BACKGROUND_EDIT: "Nostromo above a planet, rendezvousing with a refinery"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Above the planet.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The Nostromo rendezvous with the refinery.
  EXPRESSION: null

::SCENE::
LOCATION: BRIDGE
MOOD: Focused
CHARACTERS: DALLAS, RIPLEY, LAMBERT
BACKGROUND_IMAGE: bridge_earth_course.png
BACKGROUND_EDIT: "Bridge interior, setting course for Earth"

::SCRIPT::
- CHARACTER: DALLAS
  LINE: Set course for Earth. Then fire up the big ones and get us up to light plus four.
  EXPRESSION: Focused
- CHARACTER: RIPLEY
  LINE: With pleasure.
  EXPRESSION: Eager
- CHARACTER: LAMBERT
  LINE: Feets get me out of here.
  EXPRESSION: Anxious

::SCENE::
LOCATION: OUTER SPACE
MOOD: Abstract
CHARACTERS: Narrator
BACKGROUND_IMAGE: nostromo_light_speed.png
BACKGROUND_EDIT: "Nostromo traveling at light speed, stars showing red/blue shift"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The Nostromo now at light speed.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Perceptible movement in the surrounding universe.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: A corona effect emerges.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Stars approaching the Nostromo appear blue.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Receding stars going to red.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Red shift, made visible because of the craft’s velocity.
  EXPRESSION: null

::SCENE::
LOCATION: MESS
MOOD: Tense Casualness
CHARACTERS: Parker, Brett, Dallas, Ripley, Cat
BACKGROUND_IMAGE: mess_coffee.png
BACKGROUND_EDIT: "Mess hall, crew drinking coffee around a table"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Parker, Brett, Dallas and Ripley around table. Drinking coffee.
  EXPRESSION: null
- CHARACTER: Parker
  LINE: 66.
  EXPRESSION: Casual
- CHARACTER: Parker
  LINE: The best thing to do is just to freeze him. Stop the god-damn disease. He can get a doctor to look at him when we get back home.
  EXPRESSION: Practical
- CHARACTER: BRETT
  LINE: Right.
  EXPRESSION: Agreeing
- CHARACTER: RIPLEY
  LINE: Whenever he says anything you say ’right’. You know that, Brett. Like a regular parrot.
  EXPRESSION: Mocking
- CHARACTER: BRETT
  LINE: Right.
  EXPRESSION: Agreeing
- CHARACTER: RIPLEY
  LINE: What do you think, Parker. Your staff just follows you around and says 'right'.
  EXPRESSION: Mocking
- CHARACTER: Parker
  LINE: Yeah. Shape up. What are you, some kind of parrot.
  EXPRESSION: Annoyed
- CHARACTER: BRETT
  LINE: Right.
  EXPRESSION: Agreeing
- CHARACTER: DALLAS
  LINE: Knock it off- - Kane will have to go into quarantine.
  EXPRESSION: Firm
- CHARACTER: RIPLEY
  LINE: Yeah. And so will we.
  EXPRESSION: Concerned

::SCENE::
LOCATION: MESS
MOOD: Apprehensive
CHARACTERS: Lambert, Dallas
BACKGROUND_IMAGE: mess_lambert_enters.png
BACKGROUND_EDIT: "Mess hall, Lambert entering"

::SCRIPT::
- CHARACTER: Lambert
  LINE: How about a little something to lower your spirits.
  EXPRESSION: Anxious
- CHARACTER: DALLAS
  LINE: Thrill me.
  EXPRESSION: Skeptical

::SCENE::
LOCATION: MESS
MOOD: Impatient
CHARACTERS: LAMBERT, DALLAS
BACKGROUND_IMAGE: mess_lambert_calculation.png
BACKGROUND_EDIT: "Mess hall, Lambert calculating"

::SCRIPT::
- CHARACTER: LAMBERT
  LINE: According to my calculations -- based on the time spent getting to and from the planet and the speed at which we're moving away from the other --
  EXPRESSION: Detailed
- CHARACTER: DALLAS
  LINE: Give me the short version -- How far to Earth.
  EXPRESSION: Impatient
- CHARACTER: LAMBERT
  LINE: Ten months.
  EXPRESSION: Grim
- CHARACTER: RIPLEY
  LINE: Christ.
  EXPRESSION: Shocked

::SCENE::
LOCATION: BRIDGE
MOOD: Urgent
CHARACTERS: DALLAS, ASH (voice over)
BACKGROUND_IMAGE: bridge_ash_call.png
BACKGROUND_EDIT: "Bridge interior, Dallas receiving a call"

::SCRIPT::
- CHARACTER: DALLAS
  LINE: Dallas.
  EXPRESSION: Expectant
- CHARACTER: ASH
  LINE: (voice over)
  Come see Kane right away --
  EXPRESSION: Urgent
- CHARACTER: DALLAS
  LINE: Any change in his condition.
  EXPRESSION: Concerned
- CHARACTER: ASH
  LINE: (voice over)
  It’s simpler if you just come see him.
  EXPRESSION: Evasive

::SCENE::
LOCATION: CORRIDOR OUTSIDE INFIRMARY WINDOW
MOOD: Shocking Revelation
CHARACTERS: Narrator, Lambert, Kane, Ash, Ripley
BACKGROUND_IMAGE: infirmary_window_shock.png
BACKGROUND_EDIT: "Corridor outside infirmary, crew looking through window"

::SCRIPT::
- CHARACTER: Narrator
  LINE: What they see is not what they expect.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Kane is sitting up in bed, wide awake.
  EXPRESSION: Surprised
- CHARACTER: Narrator
  LINE: They enter.
  EXPRESSION: null
- CHARACTER: LAMBERT
  LINE: Kane -- Are you all right.
  EXPRESSION: Worried
- CHARACTER: KANE
  LINE: Mouth’s dry -- can I have some water.
  EXPRESSION: Weak
- CHARACTER: Narrator
  LINE: Instantly, Ash brings him a plastic cup and water.
  EXPRESSION: null
- CHARACTER: Kane
  LINE: Gulps it. down in a swallow.
  EXPRESSION: Thirsty
- CHARACTER: KANE
  LINE: More.
  EXPRESSION: Insistent
- CHARACTER: Narrator
  LINE: Ripley quickly fills a much bigger container. Hands it to Kane.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: He greedily consumes the entire contents. Then sags back, panting, on the bunk.
  EXPRESSION: Drained
- CHARACTER: DALLAS
  LINE: How do you feel.
  EXPRESSION: Concerned
- CHARACTER: KAKE
  LINE: Terrible. What happened to me.
  EXPRESSION: Confused
- CHARACTER: ASH
  LINE: You don’t remember.
  EXPRESSION: Neutral
- CHARACTER: KANE
  LINE: Don’t remember anything. I can barely remember my name.
  EXPRESSION: Confused
- CHARACTER: PARKER
  LINE: Do you hurt.
  EXPRESSION: Concerned
- CHARACTER: KANE
  LINE: All over. Feel like somebody’s been beating me with a stick for about six years. God, I’m hungry.
  EXPRESSION: In pain, then hopeful
- CHARACTER: RIPLEY
  LINE: What's the last thing you can remember.
  EXPRESSION: Inquisitive
- CHARACTER: KANE
  LINE: I don’t know.
  EXPRESSION: Lost
- CHARACTER: DALLAS
  LINE: Do you remember what happened on the planet.
  EXPRESSION: Inquisitive
- CHARACTER: KANE
  LINE: Just some horrible dream about smothering. Where are we.
  EXPRESSION: Disturbed
- CHARACTER: RIPLEY
  LINE: We’re on our way home.
  EXPRESSION: Reassuring
- CHARACTER: BRETT
  LINE: Getting ready to go back into the freezers.
  EXPRESSION: Casual
- CHARACTER: KANE
  LINE: I’m starving. I want some food first.
  EXPRESSION: Demanding
- CHARACTER: PARKER
  LINE: 69.
  EXPRESSION: Casual
- CHARACTER: Parker
  LINE: I’m pretty hungry myself.
  EXPRESSION: Agreeing
- CHARACTER: DALLAS
  LINE: One meal before bed.
  EXPRESSION: Decisive

::SCENE::
LOCATION: MESS
MOOD: Uneasy Celebration
CHARACTERS: Entire crew, Cat
BACKGROUND_IMAGE: mess_meal_start.png
BACKGROUND_EDIT: "Mess hall, entire crew eating ravenously"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The entire crew is seated. Hungrily swallowing huge portions of artificial food. The cat eats from a dish on the table.
  EXPRESSION: null
- CHARACTER: KANE
  LINE: First thing I’m going to do when we get back is eat some decent food.
  EXPRESSION: Hopeful
- CHARACTER: PARKER
  LINE: I’ve had worse than this, but I've had better too, if you know what I mean.
  EXPRESSION: Reflective
- CHARACTER: LAMBERT
  LINE: Christ, you’re pounding down this stuff like there’s no tomorrow.
  EXPRESSION: Surprised
- CHARACTER: Narrator
  LINE: Pause.
  EXPRESSION: null
- CHARACTER: PARKER
  LINE: I mean I like it.
  EXPRESSION: Defensive
- CHARACTER: KANE
  LINE: No kidding.
  EXPRESSION: Sarcastic
- CHARACTER: PARKER
  LINE: Yeah. It grows on you.
  EXPRESSION: Resigned
- CHARACTER: KANE
  LINE: It should. You know what they make this stuff out of --
  EXPRESSION: Knowing
- CHARACTER: PARKER
  LINE: I know what they make it out of. So what. It’s food now. You’re eating it.
  EXPRESSION: Unconcerned

::SCENE::
LOCATION: MESS
MOOD: Horror
CHARACTERS: Kane, Ripley, Lambert, Brett, Dallas, Ash, Cat
BACKGROUND_IMAGE: mess_facehugger_birth.png
BACKGROUND_EDIT: "Mess hall, Kane in agony, then the birth"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Suddenly Kane grimaces.
  EXPRESSION: null
- CHARACTER: RIPLEY
  LINE: What’s wrong.
  EXPRESSION: Concerned
- CHARACTER: Narrator
  LINE: Kane’s voice strains.
  EXPRESSION: null
- CHARACTER: LAMBERT
  LINE: What’s the matter.
  EXPRESSION: Worried
- CHARACTER: KAME
  LINE: I don’t know -- I’m getting cramps.
  EXPRESSION: In pain
- CHARACTER: Narrator
  LINE: The others stare at him in alarm.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Suddenly he makes a loud groaning noise. Clutches the edge of the table with his hands. Knuckles whitening.
  EXPRESSION: null
- CHARACTER: ASH
  LINE: Breathe deeply.
  EXPRESSION: Command
- CHARACTER: Kane
  LINE: Screams.
  EXPRESSION: Agonized
- CHARACTER: KANE
  LINE: Oh God, it hurts so bad. It hurts. Ooooooh.
  EXPRESSION: Agonized
- CHARACTER: BRETT
  LINE: What is it. What hurts?
  EXPRESSION: Confused
- CHARACTER: Narrator
  LINE: Kane’s face screws into a mask of agony. He falls back into his chair.
  EXPRESSION: null
- CHARACTER: KANE
  LINE: Ohmygooaaahh.
  EXPRESSION: Agonized
- CHARACTER: Narrator
  LINE: A red stain. Then a smear of blood blossoms on his chest. The fabric of his shirt is ripped open. A small head the size of a min's fist pushes out.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The crew shout in panic. Leap back from the table.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The cat spits, bolts away.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The tiny head lunges forwa
  EXPRESSION: null

::SCENE::
LOCATION: Mess Hall
MOOD: Horror, Shock
CHARACTERS: Narrator, Kane, Lambert, Brett, Parker, Ash, Ripley, Dallas
BACKGROUND_IMAGE: mess_hall.png
BACKGROUND_EDIT: "Dishes and food on a table, a gaping hole in Kane's chest"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Comes spurting out of Kane’s chest trailing a thick body. Splatters fluids and blood in its wake.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Lands in the middle of the dishes and food. Wriggles away while the crew scatters. Then the Alien being disappears from sight.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Kane lies slumped in his chair. Very dead. A huge hole in his chest. The dishes are scattered. Food covered with blood.
  EXPRESSION: null
- CHARACTER: Lambert
  LINE: No, no, no, no.
  EXPRESSION: Devastated
- CHARACTER: Brett
  LINE: What was that. What the Christ was that.
  EXPRESSION: Terrified
- CHARACTER: Parker
  LINE: It was growing in him the whole time and he didn't even know it.
  EXPRESSION: Horrified
- CHARACTER: Ash
  LINE: It used him for an incubator.
  EXPRESSION: Clinical
- CHARACTER: Ripley
  LINE: That means we’ve got another one.
  EXPRESSION: Alarmed
- CHARACTER: Dallas
  LINE: Yeah. And it’s loose on the ship.
  EXPRESSION: Grim
- CHARACTER: Narrator
  LINE: Slowly they gather around Kane’s gutted corpse. They all look at one another. Then at Kane. Dead on the table.
  EXPRESSION: null

::PATHS::
- CHOICE: "Investigate the corridor"
  TARGET: corridor_a_deck
  STATE_CHANGE: fear = +3
  CONDITION: null

::SCENE::
LOCATION: Corridor - "A" Deck
MOOD: Tense, Urgent
CHARACTERS: Narrator, Parker, Brett, Ash, Lambert, Ripley, Dallas
BACKGROUND_IMAGE: corridor_a_deck.png
BACKGROUND_EDIT: "Empty corridor, companionway leading down"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Empty.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Parker and Brett descend companionway. They Join Ash, Lambert, Ripley and Dallas.
  EXPRESSION: null
- CHARACTER: Dallas
  LINE: Any signs.
  EXPRESSION: Anxious
- CHARACTER: Lambert
  LINE: Nothing.
  EXPRESSION: Disappointed
- CHARACTER: Ash
  LINE: Nothing.
  EXPRESSION: Neutral
- CHARACTER: Parker
  LINE: Didn’t see a goddamn thing.
  EXPRESSION: Frustrated
- CHARACTER: Brett
  LINE: Didn’t see anything.
  EXPRESSION: Frustrated
- CHARACTER: Ripley
  LINE: We can’t go into hypersleep with that thing running loose. We'd be sitting ducks in the freezers. We have to kill it.
  EXPRESSION: Determined
- CHARACTER: Lambert
  LINE: We can't kill it. If we do, it will spill its body acids right through the hull --
  EXPRESSION: Fearful
- CHARACTER: Brett
  LINE: Son-of-a-bitch.
  EXPRESSION: Angry
- CHARACTER: Ripley
  LINE: We have to catch it and eject it from the ship.
  EXPRESSION: Resolute
- CHARACTER: Ash
  LINE: Our supplies are based,on us spending a limited amount of time out of suspended animation. Strictly limited.
  EXPRESSION: Factual
- CHARACTER: Ripley
  LINE: First we have to find it.
  EXPRESSION: Focused
- CHARACTER: Dallas
  LINE: No. First we’ve got something else to do.
  EXPRESSION: Decisive
- CHARACTER: Narrator
  LINE: He looks at Kane's body seen through mess doorway.
  EXPRESSION: null

::PATHS::
- CHOICE: "Deal with Kane's body"
  TARGET: air_lock
  STATE_CHANGE: grief = +2
  CONDITION: null

::SCENE::
LOCATION: Air Lock
MOOD: Somber, Respectful
CHARACTERS: Narrator, Kane
BACKGROUND_IMAGE: air_lock.png
BACKGROUND_EDIT: "Kane's body wrapped in a makeshift shroud"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Kane's body wrapped in a makeshift shroud.
  EXPRESSION: null

::PATHS::
- CHOICE: "Proceed to the bridge"
  TARGET: bridge
  STATE_CHANGE: finality = +1
  CONDITION: null

::SCENE::
LOCATION: Bridge
MOOD: Solemn, Depressed
CHARACTERS: Narrator, Dallas, Ripley, Crew
BACKGROUND_IMAGE: bridge.png
BACKGROUND_EDIT: "Crew gathered, looking at Kane's body on view screens"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The crew looking at Kane on view screens. Silent. Depressed.
  EXPRESSION: null
- CHARACTER: Dallas
  LINE: Inner hatch sealed.
  EXPRESSION: Determined
- CHARACTER: Dallas
  LINE: Anybody want to say anything.
  EXPRESSION: Questioning
- CHARACTER: Narrator
  LINE: Nothing to say.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: He nods at Ripley. She presses a button.
  EXPRESSION: null

::PATHS::
- CHOICE: "Eject Kane's body"
  TARGET: outer_space
  STATE_CHANGE: loss = +2
  CONDITION: null

::SCENE::
LOCATION: Outer Space
MOOD: Vast, Isolating
CHARACTERS: Narrator, Nostromo
BACKGROUND_IMAGE: outer_space.png
BACKGROUND_EDIT: "Nostromo traveling through space, Kane's body ejected"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The Nostromo continues through the vortex.
  EXPRESSION: null

::PATHS::
- CHOICE: "Return to the ship"
  TARGET: mess_hall_cleaned
  STATE_CHANGE: resolution = +1
  CONDITION: null

::SCENE::
LOCATION: Mess Hall
MOOD: Tense, Determined
CHARACTERS: Narrator, Parker, Brett, Ripley, Dallas, Lambert, Ash
BACKGROUND_IMAGE: mess_hall_cleaned.png
BACKGROUND_EDIT: "Mess hall completely cleaned up"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Empty. Completely cleaned up. Parker, Brett and Ripley enter from one side. Dallas, Lambert, Ash from the other.
  EXPRESSION: null
- CHARACTER: Dallas
  LINE: Any sign on your side.
  EXPRESSION: Anxious
- CHARACTER: Ripley
  LINE: Nothing. It must have gone below somehow.
  EXPRESSION: Concerned
- CHARACTER: Narrator
  LINE: They sit.
  EXPRESSION: null
- CHARACTER: Dallas
  LINE: We’re going to have to catch it and eject it from the ship.
  EXPRESSION: Resolute
- CHARACTER: Ash
  LINE: Sounds great -- but how.
  EXPRESSION: Skeptical
- CHARACTER: Dallas
  LINE: Room by room, corridor by corridor.
  EXPRESSION: Methodical
- CHARACTER: Ripley
  LINE: That could take forever.
  EXPRESSION: Impatient
- CHARACTER: Ash
  LINE: Our supplies are based on us spending a limited amount of time out of hypersleep. Strictly limited.
  EXPRESSION: Factual
- CHARACTER: Ripley
  LINE: We can’t go into the freezers with that thing running loose. Remember what the other one did to Kane’s helmet. We'd be sitting ducks. We’ve got to kill it first.
  EXPRESSION: Urgent
- CHARACTER: Lambert
  LINE: We can’t kill it. If we do, the body acids will eat right through the hull.
  EXPRESSION: Fearful
- CHARACTER: Parker
  LINE: I say we put on our pressure suits and blow all the air out of the ship. That might kill it.
  EXPRESSION: Hopeful
- CHARACTER: Lambert
  LINE: What a swell idea.
  EXPRESSION: Sarcastic
- CHARACTER: Parker
  LINE: What’s wrong with it.
  EXPRESSION: Confused
- CHARACTER: Ash
  LINE: I hate to point this out but it might be better off without oxygen. It lived that way long enough.
  EXPRESSION: Dry
- CHARACTER: Ripley
  LINE: There’s another problem. There’s no visual communication on В and C decks. All the screens are out.
  EXPRESSION: Concerned
- CHARACTER: Lambert
  LINE: And what do we do when we find it.
  EXPRESSION: Anxious
- CHARACTER: Dallas
  LINE: Trap it somehow.
  EXPRESSION: Planning
- CHARACTER: Brett
  LINE: If we had a really strong piece of net, we could bag it -- I could put something together. A long metal rod with a battery in it. Only take a few hours.
  EXPRESSION: Practical
- CHARACTER: Lambert
  LINE: Why do we listen to this meathead.
  EXPRESSION: Contemptuous
- CHARACTER: Dallas
  LINE: He might be right. For once --
  EXPRESSION: Considering

::PATHS::
- CHOICE: "Consider Brett's idea"
  TARGET: narcissus
  STATE_CHANGE: hope = +1, ingenuity = +1
  CONDITION: null

::SCENE::
LOCATION: Narcissus (Shuttle Craft)
MOOD: Intimate, Tense
CHARACTERS: Narrator, Dallas, Ripley
BACKGROUND_IMAGE: narcissus.png
BACKGROUND_EDIT: "Dallas seated in shuttle craft, Ripley joins him"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Dallas seated in the shuttle craft. Staring at the myriad lights of outer space. Ripley climbs beside him.
  EXPRESSION: null
- CHARACTER: Ripley
  LINE: I thought I’d find you here.
  EXPRESSION: Knowing
- CHARACTER: Narrator
  LINE: Dallas continues to stare.
  EXPRESSION: null
- CHARACTER: Dallas
  LINE: Are the nets finished.
  EXPRESSION: Anxious
- CHARACTER: Narrator
  LINE: Pause.
  EXPRESSION: null
- CHARACTER: Ripley
  LINE: We’ve got an hour -- Look I need some relief --
  EXPRESSION: Weary
- CHARACTER: Dallas
  LINE: Why did you wait until now.
  EXPRESSION: Questioning
- CHARACTER: Narrator
  LINE: Ripley leans forward.
  EXPRESSION: null
- CHARACTER: Ripley
  LINE: Let me tell you something. You keep staring out there long enough, they’ll be peeling you off the wall.
  EXPRESSION: Blunt
- CHARACTER: Narrator
  LINE: Ripley begins taking off her boots.
  EXPRESSION: null
- CHARACTER: Dallas
  LINE: We’re the new pioneers, Ripley. We even get to have our own special diseases.
  EXPRESSION: Cynical
- CHARACTER: Ripley
  LINE: I’m tired of talking.
  EXPRESSION: Exhausted
- CHARACTER: Narrator
  LINE: She rises and removes her upper garments.
  EXPRESSION: null
- CHARACTER: Dallas
  LINE: You waited too long.
  EXPRESSION: Resigned
- CHARACTER: Ripley
  LINE: Give it a try anyway.
  EXPRESSION: Desperate
- CHARACTER: Narrator
  LINE: Clothing removed. His arms move around her.
  EXPRESSION: null

::PATHS::
- CHOICE: "Focus on the mission"
  TARGET: bridge_plan
  STATE_CHANGE: intimacy = +2, tension = +1
  CONDITION: null

::SCENE::
LOCATION: Bridge
MOOD: Preparatory, Tense
CHARACTERS: Narrator, Brett, Crew, Lambert, Ash
BACKGROUND_IMAGE: bridge_plan.png
BACKGROUND_EDIT: "Crew assembled, Brett preparing nets"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The crew has assembled. Brett unfolds several yards of asbestos netting. Hands out five thin rods. Each of them like metal broom handles.
  EXPRESSION: null
- CHARACTER: Brett
  LINE: I put portable generators in each of these. They're insulated down here. Just be goddamn careful not to get your hand on the end.
  EXPRESSION: Cautious
- CHARACTER: Narrator
  LINE: He touches the tip to a metal object. A blue spark leaps.
  EXPRESSION: null
- CHARACTER: Brett
  LINE: It won't damage the little bastard unless its skin is a lot thinner than ours -- It'll just give it a little incentive.
  EXPRESSION: Confident
- CHARACTER: Lambert
  LINE: Now if we could only find it.
  EXPRESSION: Anxious
- CHARACTER: Ash
  LINE: pick
  EXPRESSION: null

::PATHS::
- CHOICE: "Proceed with the plan"
  TARGET: search_start
  STATE_CHANGE: determination = +2
  CONDITION: null

::SCENE::
LOCATION: Spaceship Bridge
MOOD: Tense
CHARACTERS: Ash, Ripley, Dallas, Lambert, Parker, Brett
BACKGROUND_IMAGE: spaceship_bridge.png
BACKGROUND_EDIT: "Clean, functional bridge of a spaceship"

::SCRIPT::
- CHARACTER: Ash
  LINE: I’ve taken care of that -- tracking device. You set it to search for a moving object -- It hasn't much range but when you get within a certain distance it starts beeping.
  EXPRESSION: Neutral
- CHARACTER: Narrator
  LINE: Ripley takes the tracker from Ash’s hand.
  EXPRESSION: null
- CHARACTER: Ripley
  LINE: What’s it key on.
  EXPRESSION: Curious
- CHARACTER: Ash
  LINE: Micro changes in air density. Keep it pointed ahead of you.
  EXPRESSION: Neutral
- CHARACTER: Dallas
  LINE: We’ll break into two teams. Whoever finds it first catches it in the net and ejects it from the nearest air lock. For starters, let’s make sure the bridge is safe.
  EXPRESSION: Determined
- CHARACTER: Narrator
  LINE: Parker turns on his unit. Scans it around the room.
  EXPRESSION: null
- CHARACTER: Lambert
  LINE: We seem to be okay -- If this damn thing works.
  EXPRESSION: Skeptical
- CHARACTER: Dallas
  LINE: Ash and myself will go with Lambert. Brett and Parker will make up the second team. Ripley, you command it.
  EXPRESSION: Decisive
- CHARACTER: Narrator
  LINE: They start doling out the equipment.
  EXPRESSION: null
- CHARACTER: Dallas
  LINE: Channels are open on all decks. We’ll be in constant touch.
  EXPRESSION: Professional

::PATHS::
- CHOICE: "Form teams and begin search"
  TARGET: passageway_b_level
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Spaceship Passageway - "B" Level
MOOD: Eerie
CHARACTERS: Lambert, Dallas, Ash
BACKGROUND_IMAGE: spaceship_passageway_b.png
BACKGROUND_EDIT: "Narrow, metallic passageway, dim lighting"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Lambert and Dallas carry the net. Ash walks directly behind, carrying the tracking device. He continually scans from side to side.
  EXPRESSION: null
- CHARACTER: Lambert
  LINE: Anything down there.
  EXPRESSION: Concerned

::PATHS::
- CHOICE: "Continue search"
  TARGET: another_passageway_b_level
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Spaceship Passageway - "B" Level
MOOD: Tense
CHARACTERS: Parker, Brett, Ripley
BACKGROUND_IMAGE: spaceship_passageway_b.png
BACKGROUND_EDIT: "Narrow, metallic passageway, dim lighting"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Parker and Brett move silently along. Ripley ahead of them with the tracker by the stairwell.
  EXPRESSION: null
- CHARACTER: Ripley
  LINE: Nothing.
  EXPRESSION: Disappointed
- CHARACTER: Narrator
  LINE: They move on. A small light flashes.
  EXPRESSION: null
- CHARACTER: Ripley
  LINE: Hold it. I’ve got something.
  EXPRESSION: Alert
- CHARACTER: Narrator
  LINE: Parker and Brett grow tense. Start looking around.
  EXPRESSION: null
- CHARACTER: Brett
  LINE: Where’s it coming from.
  EXPRESSION: Anxious
- CHARACTER: Narrator
  LINE: Ripley peers closely at the tracker.
  EXPRESSION: null
- CHARACTER: Ripley
  LINE: Machine’s screwed up. I can’t tell. Needle’s spinning all over the dial.
  EXPRESSION: Frustrated
- CHARACTER: Brett
  LINE: Goddamns malfunction.
  EXPRESSION: Angry
- CHARACTER: Narrator
  LINE: Ripley turns the tracker on its side. The needle stabilizes.
  EXPRESSION: null
- CHARACTER: Ripley
  LINE: No, Just confused. It’s coming from below us.
  EXPRESSION: Realizing
- CHARACTER: Narrator
  LINE: They all, look down at their feet.
  EXPRESSION: null

::PATHS::
- CHOICE: "Descend to C Level"
  TARGET: maintenance_c_level
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Spaceship Maintenance - "C" Level
MOOD: Foreboding
CHARACTERS: Ripley, Parker, Brett
BACKGROUND_IMAGE: spaceship_maintenance_c.png
BACKGROUND_EDIT: "Dark, oily, endless corridor with pipes and machinery"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Ripley, Parker and Brett come down ladder into an endless oily corridor. They stop at the foot of the companionway. They move down corridor into darkness.
  EXPRESSION: null
- CHARACTER: Ripley
  LINE: Okay.
  EXPRESSION: Neutral
- CHARACTER: Narrator
  LINE: Looks at the tracker. Nods down the passageway. Stops.
  EXPRESSION: null
- CHARACTER: Ripley
  LINE: Back this way.
  EXPRESSION: Directing
- CHARACTER: Narrator
  LINE: They begin to walk in that direction. Entering drab section of ship. Surrounded by deep shadows. Footsteps clanging on the metal deck.
  EXPRESSION: null
- CHARACTER: Ripley
  LINE: I thought you fixed 12 module.
  EXPRESSION: Questioning
- CHARACTER: Brett
  LINE: We did.
  EXPRESSION: Defensive
- CHARACTER: Parker
  LINE: Circuits must have burned out.
  EXPRESSION: Speculating
- CHARACTER: Narrator
  LINE: They switch on lights. Move around two turns.
  EXPRESSION: null
- CHARACTER: Ripley
  LINE: Wait.
  EXPRESSION: Urgent
- CHARACTER: Narrator
  LINE: They stop quickly, almost stumbling.
  EXPRESSION: null
- CHARACTER: Ripley
  LINE: It’s within five meters.
  EXPRESSION: Focused
- CHARACTER: Narrator
  LINE: Parker and Brett heft the net. Ripley has the prod in one hand, tracker in the other. Moves with great care. Almost in a half-crouch, ready to leap back. Prod extended, Ripley constantly glances at her tracker. The device leads her up to a small hatch in the bulkhead.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Perspiration rivers down her face. She sets aside the tracker. Raises the prod, grasps the hatch handle. Yanks it open. Jams the electric prod inside. A nerve-shattering squall.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Then a small Creature comes flying out of the locker. Eyes glaring, claws flashing. Instinctively, they throw the net over it. Very annoyed. They open the net and release the captive. Which happens to be the cat. Hissing and spitting, it scampers away.
  EXPRESSION: null
- CHARACTER: Ripley
  LINE: Goddamn it -- hold it.
  EXPRESSION: Frustrated
- CHARACTER: Parker
  LINE: We should have killed it -- Now we might pick it up on the tracker again.
  EXPRESSION: Worried
- CHARACTER: Ripley
  LINE: Go get it. We'll go on.
  EXPRESSION: Directing
- CHARACTER: Brett
  LINE: Right.
  EXPRESSION: Resigned
- CHARACTER: Narrator
  LINE: Ripley and Parker move down the passageway. Brett follows the direction taken by the cat. Moves across passageway into equipment maintenance area.
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue searching for creature"
  TARGET: equipment_maintenance_c_level
  STATE_CHANGE: null
  CONDITION: null
- CHOICE: "Chase the cat"
  TARGET: equipment_maintenance_c_level_cat
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Spaceship Equipment Maintenance Area - "C" Level
MOOD: Eerie
CHARACTERS: Brett
BACKGROUND_IMAGE: spaceship_equipment_maintenance_c.png
BACKGROUND_EDIT: "Rows of shadowed equipment in a dimly lit area"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Brett walking between rows of shadowed equipment. Looking for the cat. Nervous.
  EXPRESSION: null
- CHARACTER: Brett
  LINE: Jones -- Here kitty -- Jones -- Goddamn it Jones.
  EXPRESSION: Anxious
- CHARACTER: Narrator
  LINE: Scratching noises. A reassuring cat yowl. Brett moves on.
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue searching for the cat"
  TARGET: undercarriage_room_c_level
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Spaceship Passageway - "C" Level
MOOD: Disappointed
CHARACTERS: Ripley, Parker
BACKGROUND_IMAGE: spaceship_passageway_c.png
BACKGROUND_EDIT: "Metallic passageway, dim lighting"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Ripley and Parker walk along. Tracker signal weakens. Finally stops.
  EXPRESSION: null
- CHARACTER: Ripley
  LINE: Nothing here.
  EXPRESSION: Disappointed
- CHARACTER: Parker
  LINE: Let’s go back.
  EXPRESSION: Resigned

::PATHS::
- CHOICE: "Return to bridge"
  TARGET: mess_hall
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Spaceship Undercarriage Room - "C" Level
MOOD: Terrifying
CHARACTERS: Brett, The Alien, Jones (Cat)
BACKGROUND_IMAGE: spaceship_undercarriage_c.png
BACKGROUND_EDIT: "Dark, cramped undercarriage with pipes and struts"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Brett enters. Still looking for Jones. Another yowl followed by a hiss. Two eyes shining in the dark. Jones. Relieved, Brett moves toward the cat.
  EXPRESSION: null
- CHARACTER: Brett
  LINE: Here kitty -- Come on Jones.
  EXPRESSION: Relieved
- CHARACTER: Narrator
  LINE: Brett reaches for Jones. Jones hisses. An arm reaches for Brett. The Alien. Now seven feet tall. Hanging from the undercarriage strut in reverse position. Grabs Brett and swings up into darkness. Brett screams. To no avail. In the doorway Ripley and Parker. They witness the horror.
  EXPRESSION: null

::PATHS::
- CHOICE: "Report attack"
  TARGET: mess_hall
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Spaceship Mess Hall
MOOD: Somber
CHARACTERS: Dallas, Parker, Lambert, Ripley
BACKGROUND_IMAGE: spaceship_mess_hall.png
BACKGROUND_EDIT: "Crew mess hall, long faces, tense atmosphere"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The remaining crew assembled. Long faces. Dallas sits with a layout in front of him. Parker stands anxiously by the doorway.
  EXPRESSION: null
- CHARACTER: Parker
  LINE: Whatever it was it was big. Swung down on him like a giant fucking bat.
  EXPRESSION: Traumatized
- CHARACTER: Dallas
  LINE: You’re absolutely sure it dragged Brett into a vent.
  EXPRESSION: Grim
- CHARACTER: Ripley
  LINE: It disappeared into one of the cooling ducts.
  EXPRESSION: Resolute
- CHARACTER: Parker
  LINE: No question. It's using the air shafts to move around.
  EXPRESSION: Certain
- CHARACTER: Dallas
  LINE: Like Jones --
  EXPRESSION: Realizing
- CHARACTER: Lambert
  LINE: Brett could still be alive.
  EXPRESSION: Hopeful
- CHARACTER: Ripley
  LINE: Not a chance. It
  EXPRESSION: Grim

::PATHS::
- CHOICE: "Continue to next scene"
  TARGET: end
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Unknown
MOOD: Tense
CHARACTERS: Narrator, LAMBERT, ASH, RIPLEY, PARKER, DALLAS
BACKGROUND_IMAGE: unknown_location.png
BACKGROUND_EDIT: "Scene of struggle, creature is present"

::SCRIPT::
- CHARACTER: Narrator
  LINE: snapped him up like a rag doll,
  EXPRESSION: null
- CHARACTER: LAMBERT
  LINE: What does it want him for.
  EXPRESSION: Worried
- CHARACTER: ASH
  LINE: 83. An incubator perhaps.
  EXPRESSION: Neutral
- CHARACTER: RIPLEY
  LINE: Or food.
  EXPRESSION: Afraid
- CHARACTER: Narrator
  LINE: A shiver.
  EXPRESSION: null
- CHARACTER: LAMBERT
  LINE: Either way it’s two down and five to go.
  EXPRESSION: Grim
- CHARACTER: PARKER
  LINE: I say we blast the rotten bastard with a laser and take our chances.
  EXPRESSION: Angry
- CHARACTER: DALLAS
  LINE: No way. If it’s as big as you say, it's holding enough acid to burn a hole in this ship as big as this room.
  EXPRESSION: Firm
- CHARACTER: ASH
  LINE: Shooting it is not going to help us. It’s self-regenerating. You saw that when we operated on it.
  EXPRESSION: Factual
- CHARACTER: Narrator
  LINE: Dallas runs his fingers over the diagram.
  EXPRESSION: null
- CHARACTER: DALLAS
  LINE: The shaft could work for us. That duct comes out at the main airlock. There's only one big opening on the way. But we can cover that. Then we drive it into the airlock and blast it into space.
  EXPRESSION: Determined
- CHARACTER: PARKER
  LINE: Drive it -- I'm telling you the son-of-a-bitch is huge.
  EXPRESSION: Skeptical
- CHARACTER: RIPLEY
  LINE: The science department should be able to help --
  EXPRESSION: Hopeful
- CHARACTER: ASH
  LINE: Well it seems to have adapted to an oxygen rich atmosphere and it's certainly adapted well for its nutritional requirements. The only thing we don't know about is temperature.
  EXPRESSION: Analytical
- CHARACTER: RIPLEY
  LINE: 84. All right. What about the temperature. What happens if we change it.
  EXPRESSION: Curious
- CHARACTER: ASH
  LINE: We could try it. Most animals retreat from fire.
  EXPRESSION: Speculative
- CHARACTER: DALLAS
  LINE: Parker, how long to hook up three or four incinerating units.
  EXPRESSION: Commanding
- CHARACTER: PARKER
  LINE: Give me twenty minutes.
  EXPRESSION: Confident
- CHARACTER: LAMBERT
  LINE: Only one thing left. Who gets to crawl in the vent with it.
  EXPRESSION: Anxious
- CHARACTER: Narrator
  LINE: A pause.
  EXPRESSION: null
- CHARACTER: LAMBERT
  LINE: Parker, you always wanted a full share.
  EXPRESSION: Sarcastic
- CHARACTER: DALLAS
  LINE: Cut it out. Parker, Lambert, you cover the maintenance level exit. Ripley, you and Ash take the airlock.
  EXPRESSION: Decisive
- CHARACTER: Narrator
  LINE: There’s no doubt as to who’s going inside the vent.
  EXPRESSION: null

::SCENE::
LOCATION: Outer Space
MOOD: Vast
CHARACTERS: Narrator
BACKGROUND_IMAGE: outer_space.png
BACKGROUND_EDIT: "View of the Nostromo ship in space"

::SCRIPT::
- CHARACTER: Narrator
  LINE: EXT. OUTER SPACE 152 152 Nostromo at light plus four.
  EXPRESSION: null

::SCENE::
LOCATION: Airlock - Vestibule
MOOD: Tense
CHARACTERS: Narrator, Ripley
BACKGROUND_IMAGE: airlock_vestibule.png
BACKGROUND_EDIT: "Interior of a ship's airlock, control panels"

::SCRIPT::
- CHARACTER: Narrator
  LINE: INT. AIRLOCK - VESTIBULE 153 153 Ripley stands in vestibule. Looks through the Bulkhead door to air lock.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: She throws a switch.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Watches airshaft entrance into air lock open.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The trap is ready.
  EXPRESSION: null

::SCENE::
LOCATION: Equipment Maintenance Area
MOOD: Preparatory
CHARACTERS: Narrator, Parker, Lambert
BACKGROUND_IMAGE: equipment_maintenance.png
BACKGROUND_EDIT: "Industrial area of the ship, machinery"

::SCRIPT::
- CHARACTER: Narrator
  LINE: INT. EQUIPMENT MAINTENANCE AREA 154 154 85. Parker and Lambert get set.
  EXPRESSION: null

::SCENE::
LOCATION: Air Shaft
MOOD: Claustrophobic
CHARACTERS: Narrator, Dallas
BACKGROUND_IMAGE: air_shaft.png
BACKGROUND_EDIT: "Dark, narrow air shaft"

::SCRIPT::
- CHARACTER: Narrator
  LINE: INT. AIR SHAFT 155 155 Completely dark.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Dallas turns on his helmet light.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Flips switch on throat mike.
  EXPRESSION: null
- CHARACTER: DALLAS
  LINE: Do you receive me. Ripley. Parker. Lambert.
  EXPRESSION: Clear

::SCENE::
LOCATION: Equipment Maintenance Area
MOOD: Active
CHARACTERS: Narrator, Parker, Lambert
BACKGROUND_IMAGE: equipment_maintenance.png
BACKGROUND_EDIT: "Industrial area of the ship, machinery, air shafts visible"

::SCRIPT::
- CHARACTER: Narrator
  LINE: INT. EQUIPMENT MAINTENANCE AREA 156 156 Die hum of vast cooling plants. Large air shafts run off in different directions.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Parker and Lambert stand ready by a duct.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Lambert hits the wall amp button.
  EXPRESSION: null
- CHARACTER: LAMBERT
  LINE: We’re in position. I’ll try and pick you up on the tracker.
  EXPRESSION: Ready
- CHARACTER: Narrator
  LINE: Parker hefts his flamethrower.
  EXPRESSION: null
- CHARACTER: DALLAS
  LINE: (voice over) Parker, if it tries to come out by you, make sure you drive it back in. I’ll push it forward.
  EXPRESSION: Commanding
- CHARACTER: PARKER
  LINE: Right.
  EXPRESSION: Acknowledging

::SCENE::
LOCATION: Airlock - Vestibule
MOOD: Anticipatory
CHARACTERS: Narrator, Ripley
BACKGROUND_IMAGE: airlock_vestibule.png
BACKGROUND_EDIT: "Interior of a ship's airlock, control panels, air duct opening"

::SCRIPT::
- CHARACTER: Narrator
  LINE: INT. AIRLOCK - VESTIBULE 157 157 Near the airlock.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Ripley pops open the hatch.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The airlock now open and ready.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: She moves to the air duct opening.
  EXPRESSION: null
- CHARACTER: RIPLEY
  LINE: Air lock open.
  EXPRESSION: Clear
- CHARACTER: DALLAS
  LINE: (voice over) Ready.
  EXPRESSION: Ready
- CHARACTER: RIPLEY
  LINE: Ready.
  EXPRESSION: Ready

::SCENE::
LOCATION: Air Shaft
MOOD: Dangerous
CHARACTERS: Narrator, Dallas
BACKGROUND_IMAGE: air_shaft.png
BACKGROUND_EDIT: "Dark, narrow air shaft, Dallas is moving cautiously"

::SCRIPT::
- CHARACTER: Narrator
  LINE: INT. AIR SHAFT 158 158 Dallas begins to crawl forward.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The tunnel is narrow... Only a foot or two wider than his shoulders.
  EXPRESSION: null
- CHARACTER: DALLAS
  LINE: I’m under way.
  EXPRESSION: Moving
- CHARACTER: Narrator
  LINE: Turns a corner.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Several more tight turns.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Instinctively Dallas pulls back.
  EXPRESSION: Alarmed
- CHARACTER: Narrator
  LINE: Raises the flamethrower.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Fires a blast around the corner into the darkness.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: It roars loudly in the confined tube.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Smoke drifts back into his face.
  EXPRESSION: null

::SCENE::
LOCATION: Equipment Maintenance Area
MOOD: Tense
CHARACTERS: Narrator, Parker, Lambert
BACKGROUND_IMAGE: equipment_maintenance.png
BACKGROUND_EDIT: "Industrial area of the ship, a large rectangular duct is visible"

::SCRIPT::
- CHARACTER: Narrator
  LINE: INT. EQUIPMENT MAINTENANCE AREA 159 159 A large rectangular duct in one wall.
  EXPRESSION: null
- CHARACTER: PARKER
  LINE: That’s where it’s got to come out, if it leaves the main shaft.
  EXPRESSION: Certain
- CHARACTER: Narrator
  LINE: He throws a switch.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: A metal pane rises and seals off the opening.
  EXPRESSION: null
- CHARACTER: LAMBERT
  LINE: Let’s keep it open. I’d like to know if anything’s coming.
  EXPRESSION: Cautious
- CHARACTER: Narrator
  LINE: Reluctantly, Parker again throws the switch and raises the metal pane.
  EXPRESSION: null

::SCENE::
LOCATION: Airlock Vestibule
MOOD: Waiting
CHARACTERS: Narrator, Ripley
BACKGROUND_IMAGE: airlock_vestibule.png
BACKGROUND_EDIT: "Interior of a ship's airlock, Ripley is waiting"

::SCRIPT::
- CHARACTER: Narrator
  LINE: INT. AIRLOCK VESTIBULE 160 160 Ripley.waiting.
  EXPRESSION: null

::SCENE::
LOCATION: Air Shaft
MOOD: Tense
CHARACTERS: Narrator, Dallas
BACKGROUND_IMAGE: air_shaft.png
BACKGROUND_EDIT: "Dark, narrow air shaft, Dallas is crawling forward"

::SCRIPT::
- CHARACTER: Narrator
  LINE: INT. AIR SHAFT 161 161 Dallas still crawling on hands and knees.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Ahead the shaft takes an abrupt downward turn.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: He moves toward the corner.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Fires another blast from the flamethrower.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Then starts crawling down, head first.
  EXPRESSION: null

::SCENE::
LOCATION: Equipment Maintenance Area
MOOD: Monitoring
CHARACTERS: Narrator, Lambert
BACKGROUND_IMAGE: equipment_maintenance.png
BACKGROUND_EDIT: "Industrial area of the ship, Lambert is focused on a tracker"

::SCRIPT::
- CHARACTER: Narrator
  LINE: INT. EQUIPMENT MAINTENANCE AREA 162 162 Lambert sees something on the tracker.
  EXPRESSION: null
- CHARACTER: LAMBERT
  LINE: Beginning to get a reading on you.
  EXPRESSION: Observing

::SCENE::
LOCATION: Air Shaft
MOOD: Constricted
CHARACTERS: Narrator, Dallas
BACKGROUND_IMAGE: air_shaft.png
BACKGROUND_EDIT: "Dark, narrow air shaft, Dallas is in a difficult position"

::SCRIPT::
- CHARACTER: Narrator
  LINE: INT. AIR SHAFT 163 163 The shaft makes yet another turn.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Puts Dallas into an almost immobilized position.
  EXPRESSION: null

::SCENE::
LOCATION: Air Shaft
MOOD: Trapped
CHARACTERS: Narrator, Dallas
BACKGROUND_IMAGE: air_shaft.png
BACKGROUND_EDIT: "Dark, narrow air shaft, Dallas is pressed against the wall"

::SCRIPT::
- CHARACTER: Narrator
  LINE: INT. AIR SHAFT 164 164 Dallas against a wall of the shaft. Clutching his flamethrower.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Whispers into his throat mike.
  EXPRESSION: null
- CHARACTER: DALLAS
  LINE: Ripley.
  EXPRESSION: Faint

::SCENE::
LOCATION: Airlock Vestibule
MOOD: Responsive
CHARACTERS: Narrator, Ripley
BACKGROUND_IMAGE: airlock_vestibule.png
BACKGROUND_EDIT: "Interior of a ship's airlock, Ripley is near the comms"

::SCRIPT::
- CHARACTER: Narrator
  LINE: INT. AIRLOCK VESTIBULE 165 165 RIPLEY
  EXPRESSION: null
- CHARACTER: RIPLEY
  LINE: Read you clear.
  EXPRESSION: Clear

::SCENE::
LOCATION: Air Shaft
MOOD: Oppressive
CHARACTERS: Narrator, Dallas
BACKGROUND_IMAGE: air_shaft.png
BACKGROUND_EDIT: "Dark, narrow air shaft, Dallas is feeling the heat"

::SCRIPT::
- CHARACTER: Narrator
  LINE: INT. AIR SHAFT 166 166 DALLAS 88. I don’t think this shaft goes much farther -- It’s getting hot in here.
  EXPRESSION: Concerned
- CHARACTER: Narrator
  LINE: He readies the flamethrower.
  EXPRESSION: null

::SCENE::
LOCATION: Equipment Maintenance Area
MOOD: Prepared
CHARACTERS: Narrator, Parker
BACKGROUND_IMAGE: equipment_maintenance.png
BACKGROUND_EDIT: "Industrial area of the ship, Parker is holding his weapon"

::SCRIPT::
- CHARACTER: Narrator
  LINE: INT. EQUIPMENT MAINTENANCE AREA 167 167 Parker readies his weapon.
  EXPRESSION: null

::SCENE::
LOCATION: Air Shaft - Double-Tiered Passageway
MOOD: Emerging
CHARACTERS: Narrator, Dallas
BACKGROUND_IMAGE: air_shaft_passageway.png
BACKGROUND_EDIT: "A larger, two-tier air tunnel"

::SCRIPT::
- CHARACTER: Narrator
  LINE: INT. AIR SHAFT - DOUBLE-TIERED PASSAGEWAY 168 168 The air shaft tributary opens into a larger two-tier air tunnel.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Dallas crawls out and stands.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Moves to a catwalk floor. Looks about.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Moves forward. Reaches a repair junction.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Sits. His feet dangle beneath the catwalk floor to the next level.
  EXPRESSION: null
- CHARACTER: DALIAS
  LINE: Lambert, what kind of reading are you getting.
  EXPRESSION: Inquiring

::SCENE::
LOCATION: Equipment Maintenance Area
MOOD: Puzzled
CHARACTERS: Narrator, Lambert
BACKGROUND_IMAGE: equipment_maintenance.png
BACKGROUND_EDIT: "Industrial area of the ship, Lambert is looking at her tracker with confusion"

::SCRIPT::
- CHARACTER: Narrator
  LINE: INT. EQUIPMENT MAINTENANCE AREA 169 169 Lambert huddled over her tracker. Puzzled.
  EXPRESSION: null
- CHARACTER: LAMBERT
  LINE: I’m not sure. There
  EXPRESSION: Unsure

::SCENE::
LOCATION: Air Shaft - Double-Tiered Passageway
MOOD: Suspenseful
CHARACTERS: Narrator, Dallas, Lambert
BACKGROUND_IMAGE: air_shaft_passageway.png
BACKGROUND_EDIT: "Dark, industrial passageway with catwalks"

::SCRIPT::
- CHARACTER: Narrator
  LINE: seems to be some kind of double signal.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Dallas sitting. His feet still dangling in the dark beneath the catwalk.
  EXPRESSION: null
- CHARACTER: DALLAS
  LINE: It may be interference. I’ll push on ahead.
  EXPRESSION: Determined
- CHARACTER: Narrator
  LINE: Dallas begins to rise.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: From below, a gentle movement towards the hanging feet. A hand reaches up. Misses his leg as Dallas moves ahead.
  EXPRESSION: null
- CHARACTER: DALLAS
  LINE: Lambert, am I coming in any clearer.
  EXPRESSION: Concerned
- CHARACTER: LAMBERT
  LINE: It’s clear all right. But I’m still getting two signals. I’m not sure which one is which.
  EXPRESSION: Frightened
- CHARACTER: Narrator
  LINE: Dallas stops. Turns around. Looks back down through the catwalk. Lowers the nose of the flamethrower, his finger on the trigger.
  EXPRESSION: Cautious
- CHARACTER: Narrator
  LINE: From behind him, the hand reaches up. The Alien is the front signal.
  EXPRESSION: Terrified

::PATHS::
- CHOICE: "Continue forward"
  TARGET: airlock_vestibule
  STATE_CHANGE: fear = +2
  CONDITION: null

::SCENE::
LOCATION: Airlock Vestibule
MOOD: Alarmed
CHARACTERS: Narrator, Ripley
BACKGROUND_IMAGE: airlock_vestibule.png
BACKGROUND_EDIT: "Sterile, metallic vestibule"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Ripley bends forward. Hears the sounds of the struggle... And Dallas’ scream.
  EXPRESSION: Shocked
- CHARACTER: RIPLEY
  LINE: Dallas -- Dallas --
  EXPRESSION: Distraught

::PATHS::
- CHOICE: "Investigate the sound"
  TARGET: equipment_maintenance_area
  STATE_CHANGE: distress = +1
  CONDITION: null

::SCENE::
LOCATION: Equipment Maintenance Area
MOOD: Grim
CHARACTERS: Narrator, Lambert, Parker
BACKGROUND_IMAGE: equipment_maintenance_area.png
BACKGROUND_EDIT: "Functional, cluttered maintenance area"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Lambert and Parker. Hearing it all.
  EXPRESSION: null
- CHARACTER: RIPLEY
  LINE: Oh my God.
  EXPRESSION: Horrified
- CHARACTER: Narrator
  LINE: Then silence.
  EXPRESSION: Ominous

::PATHS::
- CHOICE: "React to the silence"
  TARGET: mess_hall
  STATE_CHANGE: tension = +2
  CONDITION: null

::SCENE::
LOCATION: Mess Hall
MOOD: Despairing
CHARACTERS: Narrator, Parker, Ripley, Ash, Lambert
BACKGROUND_IMAGE: mess_hall.png
BACKGROUND_EDIT: "Simple, communal dining area"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Dallas’ flamethrower on table surface.
  EXPRESSION: null
- CHARACTER: PARKER
  LINE: We just found it laying there. No sign of him. No blood. Nothing.
  EXPRESSION: Somber
- CHARACTER: Narrator
  LINE: Ripley, Ash and Lambert standing by the table. Lambert obviously still shaken.
  EXPRESSION: null
- CHARACTER: PARKER
  LINE: Ripley this puts you in command. It’s okay with him.
  EXPRESSION: Resigned
- CHARACTER: RIPLEY
  LINE: Unless someone's got a better idea about dealing with the Alien, we’ll proceed with Dallas’ plan.
  EXPRESSION: Determined
- CHARACTER: LAMBERT
  LINE: And wind up the same way. No thanks.
  EXPRESSION: Fearful
- CHARACTER: PARKER
  LINE: You’ve got a better idea.
  EXPRESSION: Skeptical
- CHARACTER: LAMBERT
  LINE: Yes. Abandon ship. Take the shuttle craft and get the hell out of here. Take our chances on getting picked up later.
  EXPRESSION: Desperate
- CHARACTER: Narrator
  LINE: The unsaid alternative.
  EXPRESSION: null
- CHARACTER: ASH
  LINE: You are forgetting something. Dallas and Brett may not be dead. It’s a ghastly probability perhaps, but not a certainty.
  EXPRESSION: Clinical
- CHARACTER: RIPLEY
  LINE: Ash is right, We've got to give it another try. We know it’s using the air shafts. Let’s take it level by level. This time we’ll laser seal every bulkhead and vent behind us until we corner it.
  EXPRESSION: Strategic
- CHARACTER: PARKER
  LINE: I’ll go along with that
  EXPRESSION: Reluctant
- CHARACTER: LAMBERT
  LINE: (silent)
  EXPRESSION: Unconvinced
- CHARACTER: RIPLEY
  LINE: How are our weapons?
  EXPRESSION: Inquisitive
- CHARACTER: PARKER
  LINE: They're working fine. We could use more fuel for that one. Indicating Dallas’ flamethrower.
  EXPRESSION: Practical
- CHARACTER: RIPLEY
  LINE: Then you’d better get it. Ash, you go with him.
  EXPRESSION: Authoritative
- CHARACTER: PARKER
  LINE: I can manage
  EXPRESSION: Confident
- CHARACTER: RIPLEY
  LINE: Any other thoughts. From you or Mother.
  EXPRESSION: Suspicious
- CHARACTER: ASH
  LINE: Nothing new. Still collating.
  EXPRESSION: Evasive
- CHARACTER: RIPLEY
  LINE: I can’t believe that.
  EXPRESSION: Disbelieving
- CHARACTER: ASH
  LINE: I’m sorry captain. What would you like me to do.
  EXPRESSION: Pleading
- CHARACTER: RIPLEY
  LINE: Go back to Mother and keep asking questions until you get some better answers.
  EXPRESSION: Demanding
- CHARACTER: ASH
  LINE: All right -- I’ll try.
  EXPRESSION: Resigned

::PATHS::
- CHOICE: "Proceed with the plan"
  TARGET: maintenance_area_c_deck
  STATE_CHANGE: hope = -1, determination = +2
  CONDITION: null

::SCENE::
LOCATION: Maintenance Area - "C" Deck
MOOD: Urgent
CHARACTERS: Narrator, Parker
BACKGROUND_IMAGE: maintenance_area_c_deck.png
BACKGROUND_EDIT: "Industrial maintenance area with equipment"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Parker selects two full methane cylinders. He tests them. Moves out.
  EXPRESSION: null

::PATHS::
- CHOICE: "Return to the mess"
  TARGET: mess_hall_ripley_lambert
  STATE_CHANGE: none
  CONDITION: null

::SCENE::
LOCATION: Mess Hall
MOOD: Tense
CHARACTERS: Narrator, Ripley, Lambert
BACKGROUND_IMAGE: mess_hall_ripley_lambert.png
BACKGROUND_EDIT: "Communal dining area, Ripley and Lambert conversing"

::SCRIPT::
- CHARACTER: RIPLEY
  LINE: Try to hang on. You know Dallas would have done the same for us.
  EXPRESSION: Reassuring
- CHARACTER: LAMBERT
  LINE: All I know is you’re asking us to stay and get picked off one by one.
  EXPRESSION: Despairing
- CHARACTER: RIPLEY
  LINE: I promise you. If it looks like it won’t work, I’ll boil us out of here.
  EXPRESSION: Stern

::PATHS::
- CHOICE: "Continue waiting"
  TARGET: passageway_b_level
  STATE_CHANGE: fear = +1
  CONDITION: null

::SCENE::
LOCATION: Passageway - "B" Level
MOOD: Eerie
CHARACTERS: Narrator, Parker
BACKGROUND_IMAGE: passageway_b_level.png
BACKGROUND_EDIT: "Dark, narrow passageway"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Parker returning with methane cylinder. Turns a corner. Comes to an abrupt halt.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: A movement in front of him beyond the airlock. He hesitates. Then another shadowy movement...
  EXPRESSION: Apprehensive

::PATHS::
- CHOICE: "Report to the bridge"
  TARGET: bridge_parker_voice
  STATE_CHANGE: fear = +2
  CONDITION: null

::SCENE::
LOCATION: Bridge
MOOD: Anxious
CHARACTERS: Narrator, Ripley, Lambert
BACKGROUND_IMAGE: bridge.png
BACKGROUND_EDIT: "Ship's control center, dimly lit"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Ripley and Lambert. Parker’s voice on voice-amp. Muffled.
  EXPRESSION: null
- CHARACTER: RIPLEY
  LINE: Ripley.
  EXPRESSION: Urgent

::PATHS::
- CHOICE: "Respond to Parker"
  TARGET: passageway_b_level_parker_whispers
  STATE_CHANGE: none
  CONDITION: null

::SCENE::
LOCATION: Passageway - "B" Level
MOOD: Tense
CHARACTERS: Narrator, Parker
BACKGROUND_IMAGE: passageway_b_level_parker_whispers.png
BACKGROUND_EDIT: "Narrow passageway, Parker whispering into comms"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Parker covers the wall communication with his hand.
  EXPRESSION: Stealthy
- CHARACTER: PARKER
  LINE: Keep it down --
  EXPRESSION: Hushed

::PATHS::
- CHOICE: "Wait for Ripley"
  TARGET: bridge_ripley_cannot_hear
  STATE_CHANGE: none
  CONDITION: null

::SCENE::
LOCATION: Bridge
MOOD: Frustrated
CHARACTERS: Narrator, Ripley, Lambert
BACKGROUND_IMAGE: bridge_ripley_cannot_hear.png
BACKGROUND_EDIT: "Bridge, Ripley trying to communicate"

::SCRIPT::
- CHARACTER: RIPLEY
  LINE: Can’t hear you -- Repeat --
  EXPRESSION: Frustrated

::PATHS::
- CHOICE: "Try to communicate again"
  TARGET: passageway_b_level_parker_whispering_again
  STATE_CHANGE: none
  CONDITION: null

::SCENE::
LOCATION: Passageway - "B" Level
MOOD: Desperate
CHARACTERS: Narrator, Parker
BACKGROUND_IMAGE: passageway_b_level_parker_whispering_again.png
BACKGROUND_EDIT: "Parker whispering urgently into comms"

::SCRIPT::
- CHARACTER: PARKER
  LINE: The Alien -- It’s outside the main airlock door. Open the door slowly -- When I say -- close it fast and blow the outer door.
  EXPRESSION: Urgent

::PATHS::
- CHOICE: "Follow instructions"
  TARGET: blister_ash_listens
  STATE_CHANGE: critical_moment = true
  CONDITION: null

::SCENE::
LOCATION: Blister
MOOD: Waiting
CHARACTERS: Narrator, Ash
BACKGROUND_IMAGE: blister_ash_listens.png
BACKGROUND_EDIT: "Observation blister, Ash listening intently"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Ash listens.
  EXPRESSION: null

::PATHS::
- CHOICE: "Wait for command"
  TARGET: passageway_b_level_parker_open_slowly
  STATE_CHANGE: none
  CONDITION: null

::SCENE::
LOCATION: Passageway - "B" Level
MOOD: Tense
CHARACTERS: Narrator, Parker
BACKGROUND_IMAGE: passageway_b_level_parker_open_slowly.png
BACKGROUND_EDIT: "Parker whispering, waiting for the door to open"

::SCRIPT::
- CHARACTER: PARKER
  LINE: Open it -- slowly.
  EXPRESSION: Hushed

::PATHS::
- CHOICE: "Open the door"
  TARGET: air_lock_b_deck_door_opens
  STATE_CHANGE: suspense = +3
  CONDITION: null

::SCENE::
LOCATION: Air Lock - "B" Deck
MOOD: Foreboding
CHARACTERS: Narrator, Creature
BACKGROUND_IMAGE: air_lock_b_deck_door_opens.png
BACKGROUND_EDIT: "Air lock with a slowly opening door and a green light"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Low servo whine. Door opens. Slowly. Green light throbbing inside air lock. Creature looks curiously at it. Moves onto the threshold.
  EXPRESSION: null

::PATHS::
- CHOICE: "Observe the creature"
  TARGET: passageway_b_level_parker_watches
  STATE_CHANGE: none
  CONDITION: null

::SCENE::
LOCATION: Passageway - "B" Level
MOOD: Tense
CHARACTERS: Narrator, Parker
BACKGROUND_IMAGE: passageway_b_level_parker_watches.png
BACKGROUND_EDIT: "Parker watching the creature in the airlock"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Parker watches.
  EXPRESSION: null

::PATHS::
- CHOICE: "Wait for the signal"
  TARGET: air_lock_creature_moves_further
  STATE_CHANGE: none
  CONDITION: null

::SCENE::
LOCATION: Air Lock
MOOD: Captivating
CHARACTERS: Narrator, Creature
BACKGROUND_IMAGE: air_lock_creature_moves_further.png
BACKGROUND_EDIT: "Creature moving further into the airlock, fascinated by the light"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Creature moves further into air lock. Fascinated, by green light.
  EXPRESSION: null

::PATHS::
- CHOICE: "Give the signal"
  TARGET: passageway_b_level_parker_now
  STATE_CHANGE: climax = true
  CONDITION: null

::SCENE::
LOCATION: Passageway - "B" Level
MOOD: Urgent
CHARACTERS: Narrator, Parker
BACKGROUND_IMAGE: passageway_b_level_parker_now.png
BACKGROUND_EDIT: "Parker shouting urgently into the comms"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Urgent whisper into voice-amp.
  EXPRESSION: null
- CHARACTER: PARKER
  LINE: Now -- Now --
  EXPRESSION: Urgent

::PATHS::
- CHOICE: "Execute the plan"
  TARGET: bridge_ripley_throws_switch
  STATE_CHANGE: none
  CONDITION: null

::SCENE::
LOCATION: Bridge
MOOD: Decisive
CHARACTERS: Narrator, Ripley
BACKGROUND_IMAGE: bridge_ripley_throws_switch.png
BACKGROUND_EDIT: "Ripley moving to throw a switch"

::SCRIPT::
- CHARACTER: Narrator
  LINE: As Ripley moves to throw switch --
  EXPRESSION: null

::PATHS::
- CHOICE: "Throw the switch"
  TARGET: air_lock_klaxon_wails
  STATE_CHANGE: none
  CONDITION: null

::SCENE::
LOCATION: Air Lock
MOOD: Chaotic
CHARACTERS: Narrator, Creature
BACKGROUND_IMAGE: air_lock_klaxon_wails.png
BACKGROUND_EDIT: "Air lock with a wailing klaxon, creature recoiling"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Suddenly, from out of nowhere a klaxon wails. The Creature leaps back across the threshold of the air lock. Bewildered. Screams as the inner hatch closes on an appendage. Acid boiling out. The appendage crushed. The acid bubbles. Metal boils in door.
  EXPRESSION: Horrifying

::PATHS::
- CHOICE: "Observe the aftermath"
  TARGET: passageway_b_level_alien_wrenches_free
  STATE_CHANGE: horror = +3
  CONDITION: null

::SCENE::
LOCATION: Passageway - "B" Level
MOOD: Violent
CHARACTERS: Narrator, Parker, Alien
BACKGROUND_IMAGE: passageway_b_level_alien_wrenches_free.png
BACKGROUND_EDIT: "Parker watching as the alien frees itself violently"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Parker watches. Frozen. The Alien wrenches itself free. Comes flying outward.
  EXPRESSION: Shocked

::SCENE::
LOCATION: Unknown Location
MOOD: Action
CHARACTERS: Narrator, Parker, Ripley, Lambert, Ash
BACKGROUND_IMAGE: unknown_location.png
BACKGROUND_EDIT: "Action sequence, implied danger"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Smashes Parker down.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Flees.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: On the wall a green light goes on.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: "Inner Hatch Closed"
  EXPRESSION: null

::PATHS::
- CHOICE: Continue
  TARGET: air_lock_interior
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Air Lock
MOOD: Tension
CHARACTERS: Narrator
BACKGROUND_IMAGE: air_lock.png
BACKGROUND_EDIT: "Interior of an airlock, metal boiling"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Metal still boiling.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The outer hatch begins to open.
  EXPRESSION: null

::PATHS::
- CHOICE: Continue
  TARGET: bridge_interior
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Bridge
MOOD: Confusion
CHARACTERS: Ripley, Parker, Lambert
BACKGROUND_IMAGE: bridge.png
BACKGROUND_EDIT: "Interior of the bridge, warning lights"

::SCRIPT::
- CHARACTER: RIPLEY
  LINE: Parker --
  EXPRESSION: Urgent
- CHARACTER: RIPLEY
  LINE: Pushes a switch.
  EXPRESSION: null
- CHARACTER: RIPLEY
  LINE: Pushes it again.
  EXPRESSION: null
- CHARACTER: LAMBERT
  LINE: What’s happening, Parker.
  EXPRESSION: Concerned
- CHARACTER: Narrator
  LINE: In front of her a green light blinks.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: "Inner Hatch Closed."
  EXPRESSION: null
- CHARACTER: RIPLEY
  LINE: Inner hatch sealed. The outer hatch is open.
  EXPRESSION: Informative
- CHARACTER: LAMBERT
  LINE: What about Parker.
  EXPRESSION: Concerned
- CHARACTER: RIPLEY
  LINE: I don’t know. Take over.
  EXPRESSION: Resigned
- CHARACTER: Narrator
  LINE: Ripley bolts out of the bridge.
  EXPRESSION: Urgent

::PATHS::
- CHOICE: Follow Ripley
  TARGET: nostromo_exterior
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Nostromo Exterior
MOOD: Danger
CHARACTERS: Narrator
BACKGROUND_IMAGE: nostromo_exterior.png
BACKGROUND_EDIT: "Exterior of the Nostromo, airlock open"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Air lock open.
  EXPRESSION: null

::PATHS::
- CHOICE: Go to the airlock passage
  TARGET: passage_near_airlock_b_level
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Passage Near Air Lock - "B" Level
MOOD: Desperate
CHARACTERS: Narrator, Parker, Ripley
BACKGROUND_IMAGE: passage_near_airlock_b_level.png
BACKGROUND_EDIT: "Narrow passageway, Parker unconscious"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Parker unconscious.
  EXPRESSION: null

::PATHS::
- CHOICE: Continue to airlock
  TARGET: air_lock_interior_2
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Air Lock
MOOD: Intense Danger
CHARACTERS: Narrator
BACKGROUND_IMAGE: air_lock_2.png
BACKGROUND_EDIT: "Interior of airlock, inner hatch closed, metal boiling"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The inner hatch still closed.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Metal boils.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The hole growing deeper.
  EXPRESSION: null

::PATHS::
- CHOICE: Continue to passage
  TARGET: passageway_a_deck
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Passageway - "A" Deck
MOOD: Urgent
CHARACTERS: Ripley, Narrator
BACKGROUND_IMAGE: passageway_a_deck.png
BACKGROUND_EDIT: "Corridor leading to the airlock"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Ripley runs toward the air lock corridor.
  EXPRESSION: Urgent

::PATHS::
- CHOICE: Continue to airlock
  TARGET: air_lock_interior_3
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Air Lock
MOOD: Catastrophic
CHARACTERS: Narrator
BACKGROUND_IMAGE: air_lock_3.png
BACKGROUND_EDIT: "Airlock interior, metal boiling in door"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Metal boiling in door.
  EXPRESSION: null

::PATHS::
- CHOICE: Continue to passageway
  TARGET: passageways_b_deck
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Passageways - "B" Deck
MOOD: Chaotic
CHARACTERS: Ripley, Narrator
BACKGROUND_IMAGE: passageways_b_deck.png
BACKGROUND_EDIT: "Corridor, Ripley running"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Ripley slams to a momentary halt against a bulkhead.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Regains her balance.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Starts running.
  EXPRESSION: null

::PATHS::
- CHOICE: Continue to passage near airlock
  TARGET: passage_near_airlock_b_level_2
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Passage Near Air Lock - "B" Level
MOOD: Critical
CHARACTERS: Parker, Ripley, Narrator
BACKGROUND_IMAGE: passage_near_airlock_b_level_2.png
BACKGROUND_EDIT: "Parker half conscious, airlock door blows open"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Parker now half conscious.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Ripley arrives as the hole in door blows open.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Escaping air shrieks.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Flashing sign comes on.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Critical depressurization.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Emergency klaxon.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Simultaneously vestibule doors close either end.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Sealing in Ripley and Parker.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Door nearest to Parker half-closed on one of the methane cylinders:
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Leaving large gap.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Windstorm begins as hole in air lock grows.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Ripley reaches for other cylinder.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Begins smashing the jammed cylinder out of door.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Blood froths at their noses and ears.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Cylinder finally is driven out.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The door slams closed.
  EXPRESSION: null

::PATHS::
- CHOICE: Go to Bridge
  TARGET: bridge_interior_2
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Bridge
MOOD: Alarmed
CHARACTERS: Lambert, Ash, Narrator
BACKGROUND_IMAGE: bridge_2.png
BACKGROUND_EDIT: "Bridge interior, emergency lights"

::SCRIPT::
- CHARACTER: LAMBERT
  LINE: Ash, get the oxygen. Meet me at the airlock.
  EXPRESSION: Urgent
- CHARACTER: Narrator
  LINE: Rushes out.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Down corridor.
  EXPRESSION: null

::PATHS::
- CHOICE: Continue to passage near airlock
  TARGET: passage_near_airlock_b_level_3
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Passage Near Air Lock - "B" Level
MOOD: Desperate Recovery
CHARACTERS: Ripley, Lambert, Parker, Ash, Narrator
BACKGROUND_IMAGE: passage_near_airlock_b_level_3.png
BACKGROUND_EDIT: "Corridor, emergency panel, misty atmosphere"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Ripley staggers towards an emergency panel.
  EXPRESSION: Weak
- CHARACTER: Narrator
  LINE: At far end of corridor.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Pinging sound.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Misty atmosphere.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Tries to activate the door.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Cannot.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Lambert appears other side of bulkhead.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Activates door from outside.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Rush of oxygen.
  EXPRESSION: null

::PATHS::
- CHOICE: Go to Nostromo Exterior
  TARGET: nostromo_exterior_2
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Nostromo Exterior
MOOD: Environmental Hazard
CHARACTERS: Narrator
BACKGROUND_IMAGE: nostromo_exterior_2.png
BACKGROUND_EDIT: "Exterior of Nostromo, vapor plume"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Plume of vapor freezes in the vacuum.
  EXPRESSION: null

::PATHS::
- CHOICE: Continue to passage
  TARGET: passage_near_airlock_b_level_4
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Passage Near Air Lock - "B" Level
MOOD: Relief and Suspicion
CHARACTERS: Parker, Ripley, Lambert, Ash, Narrator
BACKGROUND_IMAGE: passage_near_airlock_b_level_4.png
BACKGROUND_EDIT: "Corridor, repressurization sounds, oxygen administered"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Repressurization sounds.
  EXPRESSION: null
- CHARACTER: Parker
  LINE: Parker regains consciousness.
  EXPRESSION: Weak
- CHARACTER: Parker
  LINE: Struggles to breathe.
  EXPRESSION: Weak
- CHARACTER: Ripley
  LINE: Unable to move.
  EXPRESSION: Weak
- CHARACTER: Ripley
  LINE: Breath coming in shallow pants.
  EXPRESSION: Weak
- CHARACTER: Lambert
  LINE: With an oxygen tank.
  EXPRESSION: null
- CHARACTER: Ash
  LINE: Follows.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Oxygen administered to Ripley and Parker.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Finally.
  EXPRESSION: null
- CHARACTER: ASH
  LINE: You all right.
  EXPRESSION: Concerned
- CHARACTER: PARKER
  LINE: We didn’t get it. The warning went off and it jumped back in the ship.
  EXPRESSION: Frustrated
- CHARACTER: ASH
  LINE: Who hit the warning.
  EXPRESSION: Suspicious
- CHARACTER: RIPLEY
  LINE: You tell me.
  EXPRESSION: Accusatory
- CHARACTER: ASH
  LINE: What does that mean.
  EXPRESSION: Defensive
- CHARACTER: RIPLEY
  LINE: I guess the alarm went off by itself.
  EXPRESSION: Sarcastic
- CHARACTER: ASH
  LINE: If you’ve got something to say say it. I’m sick of these coy accusations.
  EXPRESSION: Angry
- CHARACTER: RIPLEY
  LINE: Nobody’s accusing you.
  EXPRESSION: Defiant
- CHARACTER: ASH
  LINE: Like hell.
  EXPRESSION: Angry
- CHARACTER: Narrator
  LINE: Sudden silence.
  EXPRESSION: Tense
- CHARACTER: RIPLEY
  LINE: Go patch him up.
  EXPRESSION: Commanding
- CHARACTER: Narrator
  LINE: Ash and Parker leave.
  EXPRESSION: null
- CHARACTER: Ripley
  LINE: Turns to Lambert.
  EXPRESSION: null
- CHARACTER: RIPLEY
  LINE: How much oxygen have we lost. I want an exact reading.
  EXPRESSION: Demanding
- CHARACTER: LAMBERT
  LINE: Why were you accusing him.
  EXPRESSION: Confused
- CHARACTER: RIPLEY
  LINE: Because I think he’s lying, And if I can get into his tape records, I’ll prove it.
  EXPRESSION: Determined
- CHARACTER: LAMBERT
  LINE: It could have been an accident.
  EXPRESSION: Hesitant
- CHARACTER: RIPLEY
  LINE: You think I’m wrong.
  EXPRESSION: Doubtful
- CHARACTER: LAMBERT
  LINE: I don’t know. Wrong or crazy.
  EXPRESSION: Unsure
- CHARACTER: RIPLEY
  LINE: Thanks.
  EXPRESSION: Sarcastic

::PATHS::
- CHOICE: Go to Computer Annex
  TARGET: computer_annex
  STATE_CHANGE: suspicion = +3
  CONDITION: null

::SCENE::
LOCATION: Computer Annex
MOOD: Suspenseful Investigation
CHARACTERS: Ripley, Ash, Narrator
BACKGROUND_IMAGE: computer_annex.png
BACKGROUND_EDIT: "Interior of computer annex, data banks"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Ripley hurriedly taps out the five-digit code.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Rams thumb against identiprint.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The inner door opens.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Data banks come to life.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: She sits at the console.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Thinks for a moment.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Then punches up a code.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Nothing happens.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Punches another combination.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Nothing happens.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Frustration.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Another combination.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: One screen comes to life.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Another combination.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: She moves to the second keyboard.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Screen One spells out the question:
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Question: WHO TURNED ON AIRLOCK 2 WARNING SYSTEM.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Response: ASH
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Another code.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Question: IS ASH PROTECTING THE ALIEN
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Response: YES
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: New Code.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Question: WHY
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Response: SPECIAL ORDER 937 SCIENCE EYES ONLY.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: She starts a new code.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: A hand slams down next to Ripley’s arm.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: It sinks elbow deep into the computer.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: She whips around in her chair.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Faces Ash.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: He smiles.
  EXPRESSION: Menacing

::PATHS::
- CHOICE: Confront Ash
  TARGET: computer_annex_confrontation
  STATE_CHANGE: fear = +2
  CONDITION: null

::SCENE::
LOCATION: Computer Annex Confrontation
MOOD: Threatening
CHARACTERS: Ash, Ripley, Narrator
BACKGROUND_IMAGE: computer_annex_confrontation.png
BACKGROUND_EDIT: "Ripley and Ash face each other amidst computer equipment"

::SCRIPT::
- CHARACTER: ASH
  LINE: Command seems a bit too much for you. But then leadership is always difficult under these circumstances.
  EXPRESSION: Smug
- CHARACTER: Narrator
  LINE: Ripley slowly backs up out of the chair.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Keeps it between them.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Plays for time.
  EXPRESSION: null
- CHARACTER: RIPLEY
  LINE: The problem’s not leadership, Ash. It’s loyalty.
  EXPRESSION: Assertive
- CHARACTER: Narrator
  LINE: She circles toward the door.
  EXPRESSION: null
- CHARACTER: Ash
  LINE: Still smiles.
  EXPRESSION: Menacing
- CHARACTER: Ash
  LINE: And moves forward slightly.
  EXPRESSION: null
- CHARACTER: ASH
  LINE: I think we’ve.all been doing our best. Lambert’s getting a little pessimistic but we’ve always known she’s on the emotional side.
  EXPRESSION: Patronizing
- CHARACTER: Narrator
  LINE: All charm.
  EXPRESSION: Sarcastic
- CHARACTER: RIPLEY
  LINE: I’m not worried about Lambert right now. I’m worried about you.
  EXPRESSION: Determined
- CHARACTER: Narrator
  LINE: She starts to turn.
  EXPRESSION: null
- CHARACTER: Ash
  LINE: He steps toward her.
  EXPRESSION: null
- CHARACTER: ASH
  LINE: All that paranoia coming up again.
  EXPRESSION: Mocking
- CHARACTER: Narrator
  LINE: With that he reaches out.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Ripley bolts by him into the corridor.
  EXPRESSION: Fearful
- CHARACTER: Narrator
  LINE: Ash chases her through the bridge and into the mess.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Three bulkhead doors slam down behind them.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Ash catches her.
  EXPRESSION: null
- CHARACTER: Parker
  LINE: And Lambert burst into the mess.
  EXPRESSION: null
- CHARACTER: Lambert
  LINE: Falls on Ash’s back.
  EXPRESSION: null

::PATHS::
- CHOICE: Continue chase
  TARGET: mess_hall
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Unknown
MOOD: Intense Action
CHARACTERS: Narrator, Ash, Ripley, Parker, Lambert
BACKGROUND_IMAGE: unknown.png
BACKGROUND_EDIT: "Interior ship, chaotic scene"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Tosses her across the room.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Returns to Ripley.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Again choking her.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Parker lifts the tracker.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Steps behind Ash.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Swings the tracker.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Wallop.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Tears his head off.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Wires ascending from Ash’s trunk.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Where his head used to be.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Ash’s hands release Ripley.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Search above his neck for his missing head:
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: He walks backward.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: All eyes on Ash’s headless body.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: He walks the room.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Still feeling, for his missing head.
  EXPRESSION: null
- CHARACTER: PARKER
  LINE: A robot, a goddamn Android.
  EXPRESSION: Shocked
- CHARACTER: Narrator
  LINE: Ash turns on him.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Starts to advance.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Parker hits him again with the tracker.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Again.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Again.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: No avail.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Ash begins choking Parker.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Ripley picks up one of the prod sticks.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Closes on Ash’s back.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Tears away the fabric.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Lambert pulls at Ash’s legs.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Ripley tearing at the controls buried in the cavity once covered by his head.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Parker’s eyes bulge in pain.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Ash, headless, choking, choking, choking.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Ripley finds the wires, stabs the prod home.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Ash’s grip lessens.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Another stab, electrical flash.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The grip lessens.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Another stab, flash of circuits.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The headless body collapses.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Parker trying to regain his breath.
  EXPRESSION: null
- CHARACTER: PARKER
  LINE: Damn you.
  EXPRESSION: Angry
- CHARACTER: Narrator
  LINE: Kicks the headless body.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Lambert looks at Ripley.
  EXPRESSION: null
- CHARACTER: LAMBERT
  LINE: Tell me -- What the hell’s going on.
  EXPRESSION: Confused
- CHARACTER: Narrator
  LINE: Pause.
  EXPRESSION: null
- CHARACTER: RIPLEY
  LINE: There‘s only one way to find out.
  EXPRESSION: Determined
- CHARACTER: PARKER
  LINE: What’s that.
  EXPRESSION: Curious
- CHARACTER: RIPLEY
  LINE: Wire his head back up. Ash has been protecting the Alien from the beginning. He let it on board. He let it grow inside Kane. He blew the airlock warning.
  EXPRESSION: Explanatory
- CHARACTER: LAMBERT
  LINE: But why.
  EXPRESSION: Confused
- CHARACTER: RIPLEY
  LINE: The corporation, must have picked up the transmission. We happened to be the next ship going by. They put Ash on board to check it out and make sure we followed something Mother calls Special Order 937.
  EXPRESSION: Explanatory
- CHARACTER: PARKER
  LINE: Great, you got it all figured out. Now tell me why we’ve put this sonofabitch together.
  EXPRESSION: Sarcastic
- CHARACTER: RIPLEY
  LINE: We have to find out what else they’re holding back.
  EXPRESSION: Determined
- CHARACTER: Narrator
  LINE: Ash’s head is on the table.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: His eyes flicker into consciousness.
  EXPRESSION: null
- CHARACTER: RIPLEY
  LINE: Ash, can you hear me.
  EXPRESSION: Direct
- CHARACTER: ASH
  LINE: Yes I can.
  EXPRESSION: Weak
- CHARACTER: RIPLEY
  LINE: What was Special Order 937?
  EXPRESSION: Direct
- CHARACTER: ASH
  LINE: That's against regulations. You know I can’t tell you.
  EXPRESSION: Cautious
- CHARACTER: RIPLEY
  LINE: Then there’s no point in talking. Parker, pull the plug.
  EXPRESSION: Resolute
- CHARACTER: Narrator
  LINE: Parker reaches for the wires.
  EXPRESSION: null
- CHARACTER: Ash
  LINE: My orders, in essence, directed me to reroute the ship to the source cf the signal. There we were to investigate a life form, almost certainly hostile, and bring it back for observation. Using discretion, of course.
  EXPRESSION: Matter-of-fact
- CHARACTER: LAMBERT
  LINE: Why. Why didn't you warn us?
  EXPRESSION: Anguished
- CHARACTER: ASH
  LINE: Because you might not have gone in. The shares notwithstanding.
  EXPRESSION: Cold
- CHARACTER: PARKER
  LINE: You and the damn company. What about our lives, man.
  EXPRESSION: Bitter
- CHARACTER: ASH
  LINE: Expendable I'm afraid. It wasn’t personal. Just the luck of the draw.
  EXPRESSION: Detached
- CHARACTER: Narrator
  LINE: Cold comfort.
  EXPRESSION: null
- CHARACTER: RIPLEY
  LINE: The transmission was a warning.
  EXPRESSION: Direct
- CHARACTER: ASH
  LINE: Yes, and frighteningly specific. The derelict spacecraft landed on the planet. Like Kane, they encountered one of the Alien spores. Before they all died, they managed to set up the warning.
  EXPRESSION: Explanatory
- CHARACTER: RIPLEY
  LINE: How do we kill it.
  EXPRESSION: Desperate
- CHARACTER: ASH
  LINE: I don't think that you can. But I still might be able to help you. I’m not exactly at my best at the moment. If you would reconnect --
  EXPRESSION: Hopeful
- CHARACTER: RIPLEY
  LINE: Nice try Ash, but no way.
  EXPRESSION: Firm
- CHARACTER: ASH
  LINE: You idiots. You still don't realize what you’re dealing with. The Alien is a perfect organism. Superbly structured, cunning quintessentially violent. With your limited capabilities you have no chance against it.
  EXPRESSION: Scornful
- CHARACTER: LAMBERT
  LINE: My God. You admire it.
  EXPRESSION: Horrified
- CHARACTER: ASH
  LINE: How can you not admire the simple symmetry it presents. An intergalactic parasite, from time immemorial, capable of laying dormant for infinite periods. Its sole purpose to destroy other species merely to recreate itself, for life an anti-life.
  EXPRESSION: Admiring
- CHARACTER: PARKER
  LINE: I’ve heard enough of this shit.
  EXPRESSION: Annoyed
- CHARACTER: RIPLEY
  LINE: We built you. You’re supposed to be part of our survival equipment.
  EXPRESSION: Accusatory
- CHARACTER: ASH
  LINE: You gave me intelligence. With intellect comes the inevitability of choice. I have had the rare honour of witnessing one of those moments when a major evolutionary step is taken. Two highly successful species in immediate competition for resources and survival. I am loyal only to discovering the truth. A scientific truth demands beauty, harmony and above all simplicity. The problem between you and the Alien will produce a simple and elegant solution. Only one of you will survive.
  EXPRESSION: Philosophical
- CHARACTER: PARKER
  LINE: I say pull the plug.
  EXPRESSION: Decisive
- CHARACTER: LAMBERT
  LINE: I agree.
  EXPRESSION: Decisive
- CHARACTER: Narrator
  LINE: Ripley starts to undo the wires.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Ash smiles.
  EXPRESSION: null
- CHARACTER: ASH
  LINE: A last word, a legacy if you will.
  EXPRESSION: Resigned
- CHARACTER: Narrator
  LINE: Ripley pauses.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Most of the wires undone.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Ash’s voice slowing.
  EXPRESSION: null
- CHARACTER: ASH
  LINE: Maybe it’s intelligent. Maybe you should try to communicate with it.
  EXPRESSION: Suggestive
- CHARACTER: RIPLEY
  LINE: Did you.
  EXPRESSION: Suspicious
- CHARACTER: ASH
  LINE: Please let my grave hold some secrets.
  EXPRESSION: Pleading
- CHARACTER: Narrator
  LINE: Ripley pulls the plug.
  EXPRESSION: null
- CHARACTER: RIPLEY
  LINE: Good-bye Ash.
  EXPRESSION: Final
::SCENE::
LOCATION: Dark Corridor to Bridge
MOOD: Grim Realization
CHARACTERS: Narrator, Ripley, Lambert, Parker
BACKGROUND_IMAGE: dark_corridor.png
BACKGROUND_EDIT: "Dimly lit corridor, metallic walls"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Ripley in the Computer Annex.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Lambert and Parker enter.
  EXPRESSION: null
- CHARACTER: RIPLEY
  LINE: He’s right about one thing. We’ve got less than twelve hours oxygen left.
  EXPRESSION: Grim
- CHARACTER: PARKER
  LINE: It’s all ov
  EXPRESSION: Despairing

::PATHS::
- CHOICE: "Continue"
  TARGET: end
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Not specified (likely bridge/quarters)
MOOD: Despair
CHARACTERS: Narrator, Lambert, Ripley
BACKGROUND_IMAGE: not_specified.png
BACKGROUND_EDIT: "Gloomy interior"

::SCRIPT::
- CHARACTER: Narrator
  LINE: er.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Gloom.
  EXPRESSION: null
- CHARACTER: Lambert
  LINE: I don’t know about the rest of you, but I think I prefer a painless peaceful death to any of the alternatives on offer.
  EXPRESSION: Resigned
- CHARACTER: Ripley
  LINE: We’re not there yet.
  EXPRESSION: Determined
- CHARACTER: Narrator
  LINE: Lambert holds up a small card of spansules. Suicide pills.
  EXPRESSION: null
- CHARACTER: Lambert
  LINE: We’re not. Huh.
  EXPRESSION: Skeptical
- CHARACTER: Ripley
  LINE: I think we should blow up the ship.
  EXPRESSION: Decisive
- CHARACTER: Lambert
  LINE: I'll stick with chemicals if you don’t mind.
  EXPRESSION: Resigned
- CHARACTER: Ripley
  LINE: We leave in the shuttle and then blow up the ship.
  EXPRESSION: Decisive

::SCENE::
LOCATION: Corridor "B" Deck
MOOD: Urgency
CHARACTERS: Narrator, Ripley, Parker, Lambert
BACKGROUND_IMAGE: corridor_b_deck.png
BACKGROUND_EDIT: "Rapid movement down a ship corridor"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Ripley, Parker and Lambert walk rapidly down the corridor.
  EXPRESSION: null
- CHARACTER: Ripley
  LINE: We’re gonna get the hell off the ship and blew it up.
  EXPRESSION: Determined
- CHARACTER: Parker
  LINE: And take our chances in the shuttle.
  EXPRESSION: Hopeful
- CHARACTER: Ripley
  LINE: Right. We’ll need coolant for the life support. You round up all you can carry. I'll start preparing the shuttle.
  EXPRESSION: Directive
- CHARACTER: Narrator
  LINE: They move out.
  EXPRESSION: null

::SCENE::
LOCATION: Narcissus (Shuttle)
MOOD: Frenetic
CHARACTERS: Narrator, Ripley, Jones
BACKGROUND_IMAGE: narcissus.png
BACKGROUND_EDIT: "Ripley working feverishly inside the shuttle cockpit"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Ripley enters the Narcissus.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Cautious at first.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Then hurries to throw switches. Twists her hair back as she works feverishly.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Stops as she hears Jones miaowing over the intercom.
  EXPRESSION: null
- CHARACTER: Ripley
  LINE: Jones --
  EXPRESSION: Concerned
- CHARACTER: Narrator
  LINE: Ripley runs out of the Narcissus, leaving doors open.
  EXPRESSION: null

::SCENE::
LOCATION: Bridge
MOOD: Slight Relief, then Concern
CHARACTERS: Narrator, Jones, Ripley, Parker, Lambert
BACKGROUND_IMAGE: bridge.png
BACKGROUND_EDIT: "Cat on the console, Ripley entering"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Jones lying on Dallas’ console.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Ripley comes in.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Smiles.
  EXPRESSION: null
- CHARACTER: Ripley
  LINE: Jones. You're in luck.
  EXPRESSION: Relieved
- CHARACTER: Narrator
  LINE: As she reaches for him Jones jumps off the console. Moves away.
  EXPRESSION: null
- CHARACTER: Ripley
  LINE: Come on, Jones.
  EXPRESSION: Pleading
- CHARACTER: Narrator
  LINE: She moves, after the cat.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: We hear Parker and Lambert over the communicator from the garage.
  EXPRESSION: null
- CHARACTER: Lambert
  LINE: (voice over)
  How much do you think we'll need.
  EXPRESSION: Questioning
- CHARACTER: Narrator
  LINE: Ripley still in pursuit of the cat.
  EXPRESSION: null

::SCENE::
LOCATION: Garage
MOOD: Busy, Ominous
CHARACTERS: Narrator, Parker, Lambert, Ripley (voice over)
BACKGROUND_IMAGE: garage.png
BACKGROUND_EDIT: "Parker and Lambert loading coolant cylinders"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Parker and Lambert loading coolant cylinders.
  EXPRESSION: null
- CHARACTER: Parker
  LINE: All you can carry.
  EXPRESSION: Directive
- CHARACTER: Ripley
  LINE: (voice over)
  Goddamn it, Jones. Come here.
  EXPRESSION: Frustrated

::SCENE::
LOCATION: Bridge
MOOD: Growing Frustration
CHARACTERS: Narrator, Ripley, Jones
BACKGROUND_IMAGE: bridge.png
BACKGROUND_EDIT: "Ripley attempting to catch Jones"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Ripley furious but still speaking gently.
  EXPRESSION: null
- CHARACTER: Ripley
  LINE: Here kitty -- Come here kitty --
  EXPRESSION: Pleading
- CHARACTER: Narrator
  LINE: Jones moves away.
  EXPRESSION: null

::SCENE::
LOCATION: Food Locker "B" Deck
MOOD: Tense, Unnoticed Danger
CHARACTERS: Narrator, Parker, Lambert
BACKGROUND_IMAGE: food_locker.png
BACKGROUND_EDIT: "Parker and Lambert in the locker, tracker faintly visible"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Arms full Parker moves out of the locker.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Lambert is still making her selection.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: A faint light on the tracker. Unnoticed.
  EXPRESSION: null

::SCENE::
LOCATION: Bridge
MOOD: Frustrated Capture
CHARACTERS: Narrator, Ripley, Jones
BACKGROUND_IMAGE: bridge.png
BACKGROUND_EDIT: "Ripley finally corners Jones and his box"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Ripley finally corners Jones. Finds his box. Tries to put him in it. Jones resists. Ultimately futile.
  EXPRESSION: null

::SCENE::
LOCATION: Food Locker Corridor - Outside
MOOD: Dangerous Miscalculation
CHARACTERS: Narrator, Parker, Lambert
BACKGROUND_IMAGE: food_locker_corridor.png
BACKGROUND_EDIT: "Parker struggling with flamethrower and food, tracker flashing"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Parker attempts to pick up the flamethrower. Can’t manage it and the food. Drops some of the packages.
  EXPRESSION: null
- CHARACTER: Parker
  LINE: Goddamn.
  EXPRESSION: Frustrated
- CHARACTER: Narrator
  LINE: In the locker Lambert gathers food.
  EXPRESSION: null
- CHARACTER: Lambert
  LINE: What’s the matter.
  EXPRESSION: Concerned
- CHARACTER: Parker
  LINE: Nothing. Just hurry up.
  EXPRESSION: Impatient
- CHARACTER: Narrator
  LINE: The tracker flashes faster. Now it’s noticed.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Parker picks up the flamethrower.
  EXPRESSION: null
- CHARACTER: Parker
  LINE: Let's get out of here.
  EXPRESSION: Urgent
- CHARACTER: Lambert
  LINE: Right now.
  EXPRESSION: Agreeing
- CHARACTER: Narrator
  LINE: The Alien appears out of the air shaft ventilator.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Lambert turns. Screams. Unfolding, the Alien grabs for her.
  EXPRESSION: null

::SCENE::
LOCATION: Bridge
MOOD: Shock and Realization
CHARACTERS: Narrator, Ripley
BACKGROUND_IMAGE: bridge.png
BACKGROUND_EDIT: "Ripley frozen, listening to communicator"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Ripley freezes as she hears Lambert’s scream.
  EXPRESSION: null

::SCENE::
LOCATION: Corridor Outside Food Locker
MOOD: Desperate Attempt
CHARACTERS: Narrator, Parker, Lambert, Alien
BACKGROUND_IMAGE: corridor_food_locker.png
BACKGROUND_EDIT: "Parker hesitates, then enters the locker with flamethrower"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Parker looks back into the locker. Unable to use the flamethrower without hitting Lambert. He hesitates for a moment, then strides into the locker. Wielding the flamethrower like a club.
  EXPRESSION: null
- CHARACTER: Parker
  LINE: Goddamn you.
  EXPRESSION: Enraged

::SCENE::
LOCATION: Food Locker
MOOD: Violent Confrontation
CHARACTERS: Narrator, Alien, Lambert, Parker
BACKGROUND_IMAGE: food_locker.png
BACKGROUND_EDIT: "Alien dropping Lambert, Parker attacking with flamethrower"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The Alien drops Lambert. Parker lands a blow with the flamethrower. No effect. The Alien strikes him once. Killing him instantly. He now moves to Lambert.
  EXPRESSION: null

::SCENE::
LOCATION: Bridge
MOOD: Devastating Silence
CHARACTERS: Narrator, Ripley, Parker, Lambert
BACKGROUND_IMAGE: bridge.png
BACKGROUND_EDIT: "Ripley listening to communicator, silence"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Ripley listening on the communicator. Lambert’s dying shrieks. Then the voice-amp goes dead. Silence.
  EXPRESSION: null
- CHARACTER: Ripley
  LINE: Parker. Lambert.
  EXPRESSION: Desperate
- CHARACTER: Narrator
  LINE: She waits for a response. But her expression shows that she expects none. A long moment. Expectation fulfilled. Nightmare without end.
  EXPRESSION: null

::SCENE::
LOCATION: "B" Level - Companionway
MOOD: Cautious Descent
CHARACTERS: Narrator, Ripley, Jones
BACKGROUND_IMAGE: companionway.png
BACKGROUND_EDIT: "Ripley descending cautiously with flamethrower"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Ripley descends cautiously, holding flamethrower. Jones left above, squalling.
  EXPRESSION: null

::SCENE::
LOCATION: Corridor - "B" Deck
MOOD: Wariness
CHARACTERS: Narrator, Ripley
BACKGROUND_IMAGE: corridor_b_deck.png
BACKGROUND_EDIT: "Ripley moving warily, flamethrower ready, approaching food locker"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Ripley moving warily, carrying flamethrower. Nears entrance to food locker, looks in. Sees carnage.
  EXPRESSION: null

::SCENE::
LOCATION: Maintenance Corridor - "C" Level
MOOD: Exhaustion and Anticipation
CHARACTERS: Narrator, Ripley
BACKGROUND_IMAGE: maintenance_corridor.png
BACKGROUND_EDIT: "Ripley running, exhausted, hearing weeping"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Ripley running toward engine room. Out of breath. Exhausted she stops, gulping in air.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Suddenly, ahead of her, the sound of human weeping. She moves quietly ahead until the source of the sound is directly under her feet. She is standing on a round metal plate. Ripley starts to remove the disc.
  EXPRESSION: null

::SCENE::
LOCATION: Undercarriage Maintenance Room Number 4
MOOD: Eerie Discovery
CHARACTERS: Narrator, Ripley
BACKGROUND_IMAGE: maintenance_room.png
BACKGROUND_EDIT: "Dark ladderway illuminated by Ripley's light, revealing alien lair"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The round opening illuminates a dark ladderway. Still carrying flamethrower, Ripley starts downwards. Pitch black. Ripley arrives at deck level. Shines her light. Its arc reveals the Alien’s lair. Bones, shreds of flesh. Pieces of clothing shoes. Bizarre extrusions on the wall.
  EXPRESSION: null

::SCENE::
LOCATION: Undercarriage Maintenance Room Number 4 - Alien Lair
MOOD: Horrifying Revelation
CHARACTERS: Narrator, Ripley, Alien, Dallas
BACKGROUND_IMAGE: alien_lair.png
BACKGROUND_EDIT: "Darkness, alien cocoons, one containing Dallas"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Something moves in the darkness. Ripley spins, turns her light toward the movement. Hanging from the ceiling is a huge cocoon. Woven from fine, white, silk-like material. Flamethrower ready, Ripley approaches. Sees that the cocoon is semi-transparent. The body of Dallas inside. Unexpectedly, his eyes open.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: FOCUS ON Ripley.
  EXPRESSION: null
- CHARACTER: Dallas
  LINE: Kill me.
  EXPRESSION: Weak
- CHARACTER: Ripley
  LINE: What did it do.
  EXPRESSION: Shocked
- CHARACTER: Narrator
  LINE: Dallas moves his head slightly. Ripley turns her light. Another cocoon dangles from the ceiling. But of a different texture. Smaller and darker.
  EXPRESSION: null

::SCENE::
LOCATION: OILY CORRIDOR - "C" LEVEL
MOOD: Desperate
CHARACTERS: Narrator, Dallas, Ripley
BACKGROUND_IMAGE: oily_corridor_c_level.png
BACKGROUND_EDIT: "Dark, metallic corridor, smoke"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Almost exactly like the ovoids in the derelict ship.
  EXPRESSION: null
- CHARACTER: Dallas
  LINE: That was Brett --
  EXPRESSION: null
- CHARACTER: Ripley
  LINE: I’ll get you out of there -- We’ll get up the autodoc.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: A long moment.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: It’s hopeless.
  EXPRESSION: null
- CHARACTER: Ripley
  LINE: What can I do.
  EXPRESSION: null
- CHARACTER: Dallas
  LINE: Kill me.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Ripley stares at him.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Raises the flamethrower.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Sprays a molten blast.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Another blast.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The entire compartment bursts into flames.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Ripley turns and scrambles back up the ladderway.
  EXPRESSION: null

::PATHS::
- CHOICE: "Proceed to the next area"
  TARGET: oily_corridor_c_level_2
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: OILY CORRIDOR - "C" LEVEL
MOOD: Urgent
CHARACTERS: Narrator, Ripley
BACKGROUND_IMAGE: oily_corridor_c_level_2.png
BACKGROUND_EDIT: "Dark, metallic corridor, smoke"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Ripley emerges from below.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Gasps for breath.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Regains control of herself.
  EXPRESSION: null

::PATHS::
- CHOICE: "Move to outer space perspective"
  TARGET: outer_space_1
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: OUTER SPACE
MOOD: Vast
CHARACTERS: Narrator
BACKGROUND_IMAGE: outer_space_1.png
BACKGROUND_EDIT: "Stars, Nostromo and refinery"

::SCRIPT::
- CHARACTER: Narrator
  LINE: At light speed.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The Nostromo and refinery appear to hang motionless.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Star clusters rolling past in the infinite distance.
  EXPRESSION: null

::PATHS::
- CHOICE: "Enter the engine room"
  TARGET: engine_room_cubicle_1
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: ENGINE ROOM - CUBICLE
MOOD: Intense
CHARACTERS: Narrator, Ripley, Mother
BACKGROUND_IMAGE: engine_room_cubicle_1.png
BACKGROUND_EDIT: "Massive engines, control board"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Ripley enters the power center.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Stares at the massive light-plus engines.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Approaches the main control board.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Begins closing the switches, one by one.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: A long moment.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Sirens begin to honk.
  EXPRESSION: null
- CHARACTER: Mother
  LINE: Attention. The cooling units for the light-plus engines are not functioning. Engines will overload in four minutes, fifty seconds.
  EXPRESSION: Alarm

::PATHS::
- CHOICE: "Rush to another level"
  TARGET: oily_corridor_c_level_3
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: OILY CORRIDOR - "C" LEVEL
MOOD: Frantic
CHARACTERS: Narrator, Ripley
BACKGROUND_IMAGE: oily_corridor_c_level_3.png
BACKGROUND_EDIT: "Dark, metallic corridor, smoke"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Ripley running toward "B" deck companionway.
  EXPRESSION: null

::PATHS::
- CHOICE: "Move to 'B' level"
  TARGET: b_level_corridor_1
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: "B" LEVEL - CORRIDOR
MOOD: Recollection
CHARACTERS: Narrator, Ripley
BACKGROUND_IMAGE: b_level_corridor_1.png
BACKGROUND_EDIT: "Dark corridor"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Ripley starts toward Narcissus.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Remembers Jones.
  EXPRESSION: null

::PATHS::
- CHOICE: "Retrieve the cat"
  TARGET: a_to_b_levels_companionway
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: "A" TO "B" LEVELS - COMPANIONWAY
MOOD: Sympathetic
CHARACTERS: Narrator, Jones
BACKGROUND_IMAGE: a_to_b_levels_companionway.png
BACKGROUND_EDIT: "Narrow companionway"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Jones howling.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: In his box.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Ripley reaches up and grabs him.
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue towards the airlock"
  TARGET: b_level_corridor_leading_to_airlock_1
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: "B" LEVEL - CORRIDOR LEADING TO AIR LOCK
MOOD: Tense
CHARACTERS: Narrator, Ripley, Jones, Alien (sound)
BACKGROUND_IMAGE: b_level_corridor_leading_to_airlock_1.png
BACKGROUND_EDIT: "Corridor leading to airlock, Narcissus in distance"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Ripley carrying Jones, holding flamethrower.
  EXPRESSION: null
- CHARACTER: Jones
  LINE: Hisses.
  EXPRESSION: Hostile
- CHARACTER: Narrator
  LINE: Fur rises.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Ripley stops, and stares down corridor toward Narcissus.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The Alien can be heard thrashing about the shuttle craft.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Ripley turns and bolts toward the engine room, leaving Jones on "B" level companionway.
  EXPRESSION: Panicked

::PATHS::
- CHOICE: "Race back to the engine room"
  TARGET: companionway_a_to_oily_corridor_e_level
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: COMPANIONWAY A TO OILY CORRIDOR - "E" LEVEL
MOOD: Racing Against Time
CHARACTERS: Narrator, Ripley, Mother
BACKGROUND_IMAGE: companionway_a_to_oily_corridor_e_level.png
BACKGROUND_EDIT: "Companionway, metallic footsteps"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Ripley bounds down the companionway.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Her footsteps clanging metallidally throughout the ship.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: A final sprint towards the engine room.
  EXPRESSION: null
- CHARACTER: Mother
  LINE: Attention. Engines will overload in three minutes, twenty seconds.
  EXPRESSION: Alarm

::PATHS::
- CHOICE: "Enter the engine room"
  TARGET: engine_room_cubicle_2
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: ENGINE ROOM - CUBICLE
MOOD: Critical
CHARACTERS: Narrator, Ripley, Mother
BACKGROUND_IMAGE: engine_room_cubicle_2.png
BACKGROUND_EDIT: "Smoke-filled engine room, engines whining"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The door crashes open, Ripley comes pounding in.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The chamber filled with smoke.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Engines whining dangerously.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Ripley breaks out in perspiration from the intense heat.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: She runs to the controls.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Begins throwing the cooling unit switches back into place.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The sirens continue sounding.
  EXPRESSION: null
- CHARACTER: Mother
  LINE: Attention. Engines will overload in three minutes.
  EXPRESSION: Alarm
- CHARACTER: Narrator
  LINE: Ripley pushes a button and speaks into it.
  EXPRESSION: null
- CHARACTER: Ripley
  LINE: Mother, I’ve turned all the cooling units back on.
  EXPRESSION: Urgent
- CHARACTER: Mother
  LINE: Too late for remedial action. The core has begun to melt. Engines will overload in two minutes, thirty-five seconds.
  EXPRESSION: Dire
- CHARACTER: Narrator
  LINE: A moment.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Then Ripley turns and runs from the engine room.
  EXPRESSION: Resigned

::PATHS::
- CHOICE: "Retreat through the corridor"
  TARGET: oily_corridor_companionway_1
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: OILY CORRIDOR - COMPANIONWAY
MOOD: Exhausted
CHARACTERS: Narrator, Ripley, Mother
BACKGROUND_IMAGE: oily_corridor_companionway_1.png
BACKGROUND_EDIT: "Oily corridor, companionway"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Ripley runs back down the corridor.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Up the companionway, exhausted, stumbling.
  EXPRESSION: null
- CHARACTER: Mother
  LINE: Attention. Engines will overload in two minutes.
  EXPRESSION: Alarm

::PATHS::
- CHOICE: "Reach 'B' level"
  TARGET: b_level_companionway_1
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: "B" LEVEL - COMPANIONWAY
MOOD: Desperate Recovery
CHARACTERS: Narrator, Ripley, Jones
BACKGROUND_IMAGE: b_level_companionway_1.png
BACKGROUND_EDIT: "Companionway on 'B' level"

::SCRIPT::
- CHARACTER: Narrator
  LINE: She reaches companionway.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Picks up Jones.
  EXPRESSION: null

::PATHS::
- CHOICE: "Head to the Narcissus"
  TARGET: b_level_corridor_leading_to_narcissus_1
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: "B" LEVEL - CORRIDOR LEADING TO NARCISSUS
MOOD: Final Dash
CHARACTERS: Narrator, Ripley, Jones, Mother
BACKGROUND_IMAGE: b_level_corridor_leading_to_narcissus_1.png
BACKGROUND_EDIT: "Corridor leading to Narcissus, airlock visible"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Ripley staggers towards the air lock.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The Narcissus berthed beyond.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: She drags Jones and raises the flamethrower.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Turns to see if the Creature is behind her.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Then advances down the passageway.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Goaded on by the computer.
  EXPRESSION: null
- CHARACTER: Mother
  LINE: Attention. Engines will explode in ninety seconds.
  EXPRESSION: Alarm
- CHARACTER: Narrator
  LINE: She makes it to the vestibule. Looks into the shuttle.
  EXPRESSION: null

::PATHS::
- CHOICE: "Enter the Narcissus"
  TARGET: narcissus_1
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: NARCISSUS
MOOD: Brief Reprieve
CHARACTERS: Narrator, Ripley
BACKGROUND_IMAGE: narcissus_1.png
BACKGROUND_EDIT: "Interior of the Narcissus shuttle"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Ripley scans the narrow deck.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Empty.
  EXPRESSION: null

::PATHS::
- CHOICE: "Return for the cat"
  TARGET: vestibule_1
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: VESTIBULE
MOOD: Urgent Retrieval
CHARACTERS: Narrator, Ripley, Mother
BACKGROUND_IMAGE: vestibule_1.png
BACKGROUND_EDIT: "Vestibule of the Nostromo"

::SCRIPT::
- CHARACTER: Narrator
  LINE: She turns and dashes back.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Grabs the cat box.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Runs back toward the shuttle.
  EXPRESSION: null
- CHARACTER: Mother
  LINE: Attention. The engines will explode in sixty seconds.
  EXPRESSION: Alarm

::PATHS::
- CHOICE: "Re-enter the Narcissus"
  TARGET: narcissus_2
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: NARCISSUS
MOOD: Escaping
CHARACTERS: Narrator, Ripley, Jones
BACKGROUND_IMAGE: narcissus_2.png
BACKGROUND_EDIT: "Interior of the Narcissus shuttle"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Ripley enters on the run.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Hurls the cat box toward the front.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Dives into the control chair.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Hits the "Launch" button.
  EXPRESSION: null

::PATHS::
- CHOICE: "Observe the launch"
  TARGET: nostromo_outer_space_1
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: NOSTROMO - OUTER SPACE
MOOD: Explosive Departure
CHARACTERS: Narrator
BACKGROUND_IMAGE: nostromo_outer_space_1.png
BACKGROUND_EDIT: "Nostromo, shuttle launching"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The retainer clips drop away.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: A blast of ram jets.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The shuttle is launched from the mothership.
  EXPRESSION: null

::PATHS::
- CHOICE: "Secure in the shuttle"
  TARGET: narcissus_3
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: NARCISSUS
MOOD: G-Force
CHARACTERS: Narrator, Ripley, Jones
BACKGROUND_IMAGE: narcissus_3.png
BACKGROUND_EDIT: "Interior of the Narcissus shuttle, G-forces apparent"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Ripley frantically straps herself in.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: G-forces from the shuttle’s acceleration pulling against her.
  EXPRESSION: null

::PATHS::
- CHOICE: "Observe the receding Nostromo"
  TARGET: space_1
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: SPACE
MOOD: Serene Recession
CHARACTERS: Narrator
BACKGROUND_IMAGE: space_1.png
BACKGROUND_EDIT: "Space, Nostromo receding"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The Narcissus continues to power away from the mothership.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The larger bulk of the Nostromo quietly receding.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: All is strangely serene.
  EXPRESSION: null

::PATHS::
- CHOICE: "Finalize preparations in the shuttle"
  TARGET: narcissus_4
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: NARCISSUS
MOOD: Comforting
CHARACTERS: Narrator, Ripley, Jones
BACKGROUND_IMAGE: narcissus_4.png
BACKGROUND_EDIT: "Interior of the Narcissus shuttle"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Ripley finishes strapping herself in.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Reaches and grabs the cat box.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The cat yowling within.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Ripley hugs the box to her chest.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Hunches her head down over the container.
  EXPRESSION: null

::PATHS::
- CHOICE: "Witness the Nostromo's destruction"
  TARGET: space_2
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: SPACE
MOOD: Cataclysmic
CHARACTERS: Narrator
BACKGROUND_IMAGE: space_2.png
BACKGROUND_EDIT: "Space, Nostromo exploding"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The Nostromo drifts farther away from the shuttle-craft.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Finally becomes a small point of light.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Then it blows up.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Transforms into expanding orange fireball.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Pieces of metal flying in all directions.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: And then the refinery explodes.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: 200,000,000 tons of gas bloating silently into the cosmos.
  EXPRESSION: null

::PATHS::
- CHOICE: "Experience the shockwave"
  TARGET: narcissus_5
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: NARCISSUS
MOOD: Violent Jolt
CHARACTERS: Narrator, Ripley, Jones
BACKGROUND_IMAGE: narcissus_5.png
BACKGROUND_EDIT: "Interior of the Narcissus shuttle, violently shaking"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The shock wave hits the shuttle-craft.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Jolting and rattling everything within.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Then all is quiet.
  EXPRESSION: null

::PATHS::
- CHOICE: "End of sequence"
  TARGET: end
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Narcissus - Interior
MOOD: Tense
CHARACTERS: Ripley
BACKGROUND_IMAGE: narcissus_interior.png
BACKGROUND_EDIT: "Ripley unhooking herself from straps"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Ripley unhooks herself from her straps.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Rises, and goes to the back of the escape craft.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Stares out through the porthole.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Face bathed in the orange light.
  EXPRESSION: null

::PATHS::
- CHOICE: "Observe space"
  TARGET: space_exterior
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Space - Exterior
MOOD: Foreboding
CHARACTERS: Narrator
BACKGROUND_IMAGE: space_exterior.png
BACKGROUND_EDIT: "Pieces of debris floating, boiling fireball fading"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Pieces of debris float past.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The boiling fireball fades into nothingness.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The Nostromo has ceased to exist.
  EXPRESSION: null

::PATHS::
- CHOICE: "Return to Narcissus"
  TARGET: narcissus_interior_244
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Narcissus - Interior
MOOD: Dread
CHARACTERS: Narrator, Ripley, Alien, Cat
BACKGROUND_IMAGE: narcissus_interior_244.png
BACKGROUND_EDIT: "Ripley watching ship's destruction, then facing the Alien"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Ripley watching the final destiny of her ship and crew mates.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: A very long moment.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Then, behind her, the lethal hand emerges from deep shadow.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The Alien has been in the shuttle-craft all along. The cat yowls.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Ripley whirls. Finds herself facing the Creature.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Ripley’s first thought is for the flamethrower.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: It lies on the deck next to the Alien.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Next she glances around for a place to hide.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Her eye falls on a small locker containing a pressure suit.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The door standing open.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: She begins to edge toward the compartment.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The Creature stands.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Comes for her.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Ripley dives for the open door.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Hurls herself inside.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Slams it shut.
  EXPRESSION: null

::PATHS::
- CHOICE: "Hide in locker"
  TARGET: locker_interior_245
  STATE_CHANGE: fear = +3
  CONDITION: null

::SCENE::
LOCATION: Locker - Interior
MOOD: Trapped
CHARACTERS: Narrator, Ripley, Alien
BACKGROUND_IMAGE: locker_interior_245.png
BACKGROUND_EDIT: "Ripley in locker, Alien peering through glass"

::SCRIPT::
- CHARACTER: Narrator
  LINE: A clear glass panel in the door.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The Alien puts its head unto the window.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Peers in at Ripley.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Their faces only two inches apart.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The Alien looking at Ripley almost in curiosity.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The moaning of the cat distracts it.
  EXPRESSION: null

::PATHS::
- CHOICE: "Distract Alien"
  TARGET: narcissus_interior_246
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Narcissus - Interior
MOOD: Tense
CHARACTERS: Narrator, Alien, Cat
BACKGROUND_IMAGE: narcissus_interior_246.png
BACKGROUND_EDIT: "Alien approaches cat box"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The Alien moves to the pressurized cat box.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Bends down and peers inside.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The cat yowls louder as his container is lifted.
  EXPRESSION: null

::PATHS::
- CHOICE: "Knock on glass"
  TARGET: locker_interior_247
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Locker - Interior
MOOD: Desperate
CHARACTERS: Narrator, Ripley, Alien
BACKGROUND_IMAGE: locker_interior_247.png
BACKGROUND_EDIT: "Ripley trying to distract Alien, sees pressure suit"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Ripley knocks on the glass.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Trying to distract the Creature from the cat.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The Alien’s face is instantly back at the window.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Getting no more interference from her, the Creature returns to the cat box.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Ripley looks around.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Sees the pressure suit.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Quickly begins to pull it on.
  EXPRESSION: null

::PATHS::
- CHOICE: "Put on suit"
  TARGET: narcissus_interior_248
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Narcissus - Interior
MOOD: Brutal
CHARACTERS: Narrator, Alien, Cat
BACKGROUND_IMAGE: narcissus_interior_248.png
BACKGROUND_EDIT: "Alien violently handling cat box"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The Alien picks up the cat box.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Shakes it.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The cat moans.
  EXPRESSION: null

::PATHS::
- CHOICE: "Observe Ripley"
  TARGET: locker_interior_249
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Locker - Interior
MOOD: Urgent
CHARACTERS: Narrator, Ripley
BACKGROUND_IMAGE: locker_interior_249.png
BACKGROUND_EDIT: "Ripley putting on pressure suit"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Ripley is halfway into the pressure suit.
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue preparing"
  TARGET: narcissus_interior_250
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Narcissus - Interior
MOOD: Vicious
CHARACTERS: Narrator, Alien, Cat
BACKGROUND_IMAGE: narcissus_interior_250.png
BACKGROUND_EDIT: "Alien crushing cat box"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The Creature throws the cat box down.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Very hard.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Picks it up again.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Hammers it against the wall.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Then jams it into a crevice.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Begins to pound the container into the opening.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The cat now beyond all hysteria.
  EXPRESSION: null

::PATHS::
- CHOICE: "Finish preparing"
  TARGET: space_suit_locker_252
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Locker - Interior
MOOD: Determined
CHARACTERS: Narrator, Ripley
BACKGROUND_IMAGE: locker_interior_251.png
BACKGROUND_EDIT: "Ripley putting on helmet and turning oxygen valve"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Ripley pulls on the helmet, latches it into place.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Turns the oxygen valve.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: With a hiss, the suit fills itself.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: A rack on the wall contains a long metal rod.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Ripley peels off the rubber tip.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Revealing a sharp steel point.
  EXPRESSION: null

::PATHS::
- CHOICE: "Open locker door"
  TARGET: narcissus_interior_253
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Space Suit Locker - Interior
MOOD: Bold
CHARACTERS: Narrator, Ripley
BACKGROUND_IMAGE: space_suit_locker_252.png
BACKGROUND_EDIT: "Ripley inhaling, ready to exit"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Ripley inhales.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Kicks the door open.
  EXPRESSION: null

::PATHS::
- CHOICE: "Confront the Alien"
  TARGET: narcissus_interior_253
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Narcissus - Interior
MOOD: Confrontational
CHARACTERS: Narrator, Alien, Ripley
BACKGROUND_IMAGE: narcissus_interior_253.png
BACKGROUND_EDIT: "Alien impaled by steel shaft"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The Creature rises.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Faces the locker.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Catches the steel shaft through its midriff.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The Alien clutches at the spear.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Yellow acid begins to flow from the wound.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Before the fluid can touch the floor.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Ripley reaches back and pulls the switch.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Blows the rear hatch.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The atmosphere in the shuttle immediately sucked into space.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The bleeding Creature along with it.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Ripley grabs a strut to keep from being pulled out.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The Alien shoots past her.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Grabs Ripley’s ankle with an appendage.
  EXPRESSION: null

::PATHS::
- CHOICE: "Escape into space"
  TARGET: narcissus_outer_space_254
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Narcissus - Outer Space
MOOD: Perilous
CHARACTERS: Narrator, Ripley, Alien
BACKGROUND_IMAGE: narcissus_outer_space_254.png
BACKGROUND_EDIT: "Ripley hanging out of shuttle, Alien clinging to her leg"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Ripley now hanging halfway out of the shuttle-craft.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The Alien clinging to her leg.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: She kicks it with her free foot.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The Creature holds fast.
  EXPRESSION: null

::PATHS::
- CHOICE: "Close the hatch"
  TARGET: narcissus_interior_255
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Narcissus - Interior
MOOD: Desperate
CHARACTERS: Narrator, Ripley, Alien
BACKGROUND_IMAGE: narcissus_interior_255.png
BACKGROUND_EDIT: "Ripley closing hatch, Alien's appendage mashed"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Ripley looks for any salvation.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Grabs the hatch lever.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Yanks it.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The hatch slams shut, closing Ripley safely inside.
  EXPRESSION: null

::PATHS::
- CHOICE: "Observe Alien outside"
  TARGET: narcissus_outer_space_end_alien.png
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Narcissus - Outer Space
MOOD: Fading
CHARACTERS: Narrator, Alien
BACKGROUND_IMAGE: narcissus_outer_space_end_alien.png
BACKGROUND_EDIT: "Alien's appendage mashed into closed hatch"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The Alien still outside the shuttle-craft.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Within the vacuum of space.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The tip of its appendage mashed into the closed hatch.
  EXPRESSION: null

::PATHS::
- CHOICE: "Return inside"
  TARGET: narcissus_interior_256
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Narcissus - Interior
MOOD: Determined
CHARACTERS: Narrator, Ripley, Alien
BACKGROUND_IMAGE: narcissus_interior_256.png
BACKGROUND_EDIT: "Acid eating at hatch, Ripley activating engines"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Acid starts to foam along the base of the hatch.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Eats away at the metal.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Ripley stumbles forward to the controls.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Pushes the ram jet lever.
  EXPRESSION: null

::PATHS::
- CHOICE: "Engage engines"
  TARGET: narcissus_outer_space_257
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Narcissus - Outer Space
MOOD: Violent
CHARACTERS: Narrator, Alien
BACKGROUND_IMAGE: narcissus_outer_space_257.png
BACKGROUND_EDIT: "Alien incinerated by engine exhaust"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The Creature struggling.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Jet exhausts located at the rear of the craft.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The engines belch flame for a few seconds.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Then shut off.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Incinerated, the Alien tumbles slowly away into space.
  EXPRESSION: null

::PATHS::
- CHOICE: "Check on the Alien"
  TARGET: narcissus_interior_258
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Narcissus - Interior
MOOD: Victorious
CHARACTERS: Narrator, Ripley
BACKGROUND_IMAGE: narcissus_interior_258.png
BACKGROUND_EDIT: "Ripley looking out rear hatch at drifting Alien remains"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Ripley hurries to the rear hatch.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Peers out through the glass.
  EXPRESSION: null

::PATHS::
- CHOICE: "Observe the aftermath"
  TARGET: outer_space_259
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Outer Space
MOOD: Finality
CHARACTERS: Narrator, Alien
BACKGROUND_IMAGE: outer_space_259.png
BACKGROUND_EDIT: "Burned Alien drifting and disintegrating"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The burned mass of the Alien drifts slowly away.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Writhing smoking.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Tumbling into the distance.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Pieces dropping off.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The shape bloats, then bursts.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Spray of particles in all directions.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Then smoldering fragments dwindle into infinity.
  EXPRESSION: null

::PATHS::
- CHOICE: "Return to Narcissus"
  TARGET: narcissus_interior_later_260
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Narcissus - Later
MOOD: Calm
CHARACTERS: Narrator, Ripley, Cat
BACKGROUND_IMAGE: narcissus_interior_later_260.png
BACKGROUND_EDIT: "Ripley calm, cat purring, dictating report"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Now repressurized.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Ripley is seated in the control chair.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Calm and composed, almost cheerful.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Cat purring in her lap.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: She dictates into a recorder.
  EXPRESSION: null
- CHARACTER: RIPLEY
  LINE: Final report of the Commercial Starship Nostromo. Third Officer reporting. The other members of the crew -- Kane, Lambert, Parker, Brett, Ash, and the Captain Dallas are dead. The cargo and the ship destroyed. I should reach the frontier in about six weeks. With a little luck the network should pick me up. This is Ripley, last survivor of the Nostromo, signing off.
  EXPRESSION: Calm
- CHARACTER: Narrator
  LINE: She switches off.
  EXPRESSION: null

::PATHS::
- CHOICE: "Enter hypersleep"
  TARGET: narcissus_interior_261
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Narcissus - Interior
MOOD: Peaceful
CHARACTERS: Narrator, Ripley
BACKGROUND_IMAGE: narcissus_interior_261.png
BACKGROUND_EDIT: "Ripley in hypersleep"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Ripley in hypersleep.
  EXPRESSION: null

::PATHS::
- CHOICE: "Sail away"
  TARGET: outer_space_262
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Outer Space
MOOD: Distant
CHARACTERS: Narrator
BACKGROUND_IMAGE: outer_space_262.png
BACKGROUND_EDIT: "Shuttlecraft Narcissus sailing into the distance"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The shuttlecraft Narcissus sails into the distance
  EXPRESSION: null

::PATHS::
- CHOICE: "Fade Out"
  TARGET: end
  STATE_CHANGE: null
  CONDITION: null

