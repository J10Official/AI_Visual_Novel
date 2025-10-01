::SCENE::
LOCATION: Middle of the Night
MOOD: Disoriented
CHARACTERS: Amelia, Boy's Voice, Narrator
BACKGROUND_IMAGE: car_crash.png
BACKGROUND_EDIT: "Black screen, then close-up of a woman's face in a car crash, disoriented, spinning, then a bed in darkness"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Black screen. A rumbling sound. It intensifies.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: A woman’s face appears suddenly in close up, shocked, disoriented. It is AMELIA (late 30s.) She travels fast, pinned back to what could be a car seat. It’s not clear.
  EXPRESSION: Shocked
- CHARACTER: Narrator
  LINE: She is suddenly lifted up and around, her face tumbling as if in a dryer, 360 degrees.
  EXPRESSION: Shocked
- CHARACTER: Narrator
  LINE: The image slows down as she shuts her eyes. Bits of dirt and debris fly past her face. There’s no sound. The effect is strangely beautiful.
  EXPRESSION: null
- CHARACTER: Boy's Voice
  LINE: Mummy....
  EXPRESSION: Afraid
- CHARACTER: Narrator
  LINE: Amelia tries to open her eyes, she continues to spin.
  EXPRESSION: Struggling
- CHARACTER: Narrator
  LINE: Her face stops tumbling and comes to an upright position.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: A skidding sound builds in intensity. Her hand reaches above to brace herself for the impact. She turns to look beside her. Time is stretched.
  EXPRESSION: Tense
- CHARACTER: Narrator
  LINE: She sees a man staring ahead. He looks terrified. A light grows brighter. The skidding sound is almost deafening.
  EXPRESSION: Terrified
- CHARACTER: Narrator
  LINE: Amelia instinctively looks away from him, closing her eyes.
  EXPRESSION: Afraid
- CHARACTER: Narrator
  LINE: The terrible sound peaks, then slowly recedes.
  EXPRESSION: null
- CHARACTER: Boy's Voice
  LINE: MUM.
  EXPRESSION: Afraid
- CHARACTER: Narrator
  LINE: Amelia hears the boy’s voice for the first time. She opens her eyes as she ‘falls’ slowly back into space.
  EXPRESSION: Surprised
- CHARACTER: Narrator
  LINE: Finally, she ‘lands’. There is complete silence.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Amelia is lying on a pillow. She looks at the ceiling, dazed. Her breathing is erratic.
  EXPRESSION: Dazed
- CHARACTER: Boy's Voice
  LINE: MUMMY!
  EXPRESSION: Panicked
- CHARACTER: Narrator
  LINE: She sees her six year old son, SAMUEL, bedside. He’s small for his age, intense. A panicked look on his face.
  EXPRESSION: null
- CHARACTER: Samuel
  LINE: I had the dream again.
  EXPRESSION: Anxious
- CHARACTER: Narrator
  LINE: Amelia makes one mighty effort to get up. Her fluffy Maltese terrier, BUGSY, jumps off the bed with her. She scrambles to her feet, stumbling on the way to her son.
  EXPRESSION: Tired

::PATHS::
- CHOICE: "Check Samuel's room for monsters"
  TARGET: samuels_room_night
  STATE_CHANGE: fear = +1, tiredness = +1
  CONDITION: null

::SCENE::
LOCATION: Samuel's Room
MOOD: Anxious
CHARACTERS: Amelia, Samuel, Narrator
BACKGROUND_IMAGE: samuels_room.png
BACKGROUND_EDIT: "Nighttime, dark bedroom, POV under the bed, inside closet, then bedroom interior"

::SCRIPT::
- CHARACTER: Narrator
  LINE: POV under the bed. The doona is lifted. Amelia and Samuel peer underneath. The doona is dropped back into place.
  EXPRESSION: Searching
- CHARACTER: Narrator
  LINE: Black. Closet doors open, Amelia takes a quick look inside, Samuel checks everywhere. Amelia closes it.
  EXPRESSION: Searching
- CHARACTER: Narrator
  LINE: Amelia is dark haired and wiry. Pretty, but nervous looking.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Samuel’s little face is white with anxiety. He moves back and forth from one foot to the other.
  EXPRESSION: Anxious
- CHARACTER: Samuel
  LINE: Can we check under the bed?
  EXPRESSION: Anxious
- CHARACTER: Amelia
  LINE: What did it look like?
  EXPRESSION: Patient
- CHARACTER: Narrator
  LINE: Samuel shrugs his shoulders. He can’t remember.
  EXPRESSION: Confused
- CHARACTER: Amelia
  LINE: Remember what we said? If you can’t see it, then it mustn’t be real.
  EXPRESSION: Reassuring
- CHARACTER: Samuel
  LINE: It said it’s coming to kill us both.
  EXPRESSION: Afraid
- CHARACTER: Narrator
  LINE: His comment unnerves Amelia. She recovers quickly.
  EXPRESSION: Nervous
- CHARACTER: Amelia
  LINE: It’s just a silly dream.
  EXPRESSION: Gentle

::PATHS::
- CHOICE: "Read a story to comfort him"
  TARGET: samuels_room_bookshelf
  STATE_CHANGE: comfort = +1
  CONDITION: null

::SCENE::
LOCATION: Samuel's Room
MOOD: Comforting
CHARACTERS: Amelia, Samuel, Bugsy, Narrator
BACKGROUND_IMAGE: samuels_room_bookshelf.png
BACKGROUND_EDIT: "Nighttime, in a bedroom, near a bookshelf"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Amelia searches through the bookshelf. Samuel clings to her waist, not letting go. Bugsy follows them.
  EXPRESSION: Searching

::PATHS::
- CHOICE: "Pick a book"
  TARGET: amelias_bedroom_story
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Amelia's Bedroom
MOOD: Tired
CHARACTERS: Amelia, Samuel, Narrator
BACKGROUND_IMAGE: amelias_bedroom_night.png
BACKGROUND_EDIT: "Nighttime, in bed, warm lighting, Amelia reading to Samuel"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Amelia sits up in bed, Samuel in her lap, the doona surrounds them like a giant caterpillar. Amelia gives the book everything she’s got, fighting her tiredness.
  EXPRESSION: Tired
- CHARACTER: Amelia
  LINE: Well I’ll climb down your chimney you fat little pigs! And he climbed down that chimney, straight into the huge black pot. And that was the end of the big-bad-wolf!
  EXPRESSION: Animated
- CHARACTER: Narrator
  LINE: She closes the book. Samuel is still anxious.
  EXPRESSION: null
- CHARACTER: Samuel
  LINE: Did they really get the wolf?
  EXPRESSION: Anxious
- CHARACTER: Amelia
  LINE: I’m sure they did.
  EXPRESSION: Reassuring
- CHARACTER: Samuel
  LINE: I’m gonna kill the monster if it tries to hurt you Mum.
  EXPRESSION: Determined
- CHARACTER: Amelia
  LINE: Nothing’s going to hurt me Sam.
  EXPRESSION: Gentle
- CHARACTER: Samuel
  LINE: I’ll bash it to pieces when it comes.
  EXPRESSION: Determined
- CHARACTER: Amelia
  LINE: Time for bed now, OK? It’s very late.
  EXPRESSION: Tired
- CHARACTER: Narrator
  LINE: Samuel flips the pages straight back to the beginning.
  EXPRESSION: Resistant
- CHARACTER: Samuel
  LINE: Just one more time... Then I’ll sleep.
  EXPRESSION: Pleading
- CHARACTER: Narrator
  LINE: He won’t take no for an answer. She gives in to another read.
  EXPRESSION: Resigned
- CHARACTER: Narrator
  LINE: Samuel snuggles in close to her, wide awake.
  EXPRESSION: Anxious
- CHARACTER: Amelia
  LINE: A long time ago, just yesterday in fact, there were three little pigs and one nasty big wolf.
  EXPRESSION: Bright

::PATHS::
- CHOICE: "Continue reading"
  TARGET: amelias_bedroom_sleep
  STATE_CHANGE: tiredness = +1
  CONDITION: null

::SCENE::
LOCATION: Amelia's Bedroom
MOOD: Restless
CHARACTERS: Amelia, Samuel, Narrator
BACKGROUND_IMAGE: amelias_bedroom_sleep.png
BACKGROUND_EDIT: "Nighttime, in bed, dim lighting, Amelia uncomfortable, Samuel asleep"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Little legs wrapped tightly around Amelia’s waist.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Samuel’s face tucked in behind his mother’s. He’s fast asleep, she’s wide awake.
  EXPRESSION: Wide Awake
- CHARACTER: Narrator
  LINE: His mouth, chewing at nothing, grinding away. The sound goes right through Amelia. His breath irritates her neck.
  EXPRESSION: Annoyed
- CHARACTER: Narrator
  LINE: His hand plays with her ear in his sleep. She peels it away, puts it by his side.
  EXPRESSION: Annoyed
- CHARACTER: Narrator
  LINE: She unwraps his legs, making sure she doesn’t wake him.
  EXPRESSION: Careful
- CHARACTER: Narrator
  LINE: Amelia inches silently away from her son, her back to him.
  EXPRESSION: Relieved
- CHARACTER: Narrator
  LINE: Samuel doesn’t wake up. The gap between them widens.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Amelia curls up on the other side of the bed, her knees to her chest, alone.
  EXPRESSION: Lonely
- CHARACTER: Narrator
  LINE: TITLE - THE BABADOOK
  EXPRESSION: null

::PATHS::
- CHOICE: "Wake up in the morning"
  TARGET: house_morning_chaos
  STATE_CHANGE: frustration = +1, tiredness = +1
  CONDITION: null

::SCENE::
LOCATION: Amelia's House (Bedroom, Basement, Lounge, Kitchen)
MOOD: Chaotic
CHARACTERS: Amelia, Samuel, Narrator
BACKGROUND_IMAGE: house_morning.png
BACKGROUND_EDIT: "Morning, various rooms of a house, alarm blaring, child's workshop, messy"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Bedroom. A blaring alarm sounds. A lifeless arm pokes out from under the doona, hanging over the bed. It’s hard to believe someone could sleep through this noise.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Basement. Child’s hands grip a large hammer. The hammer is raised and comes down hard on a rusty nail.
  EXPRESSION: Determined
- CHARACTER: Narrator
  LINE: Little hands pushing down on a join in two pieces of wood, testing it for strength.
  EXPRESSION: Focused
- CHARACTER: Narrator
  LINE: Bedroom. The alarm keeps going. The arm has not moved.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Basement. A cricket ball is loaded into a large plastic cup, the cup is tied to a wooden plank.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: A metal contraption being fitted onto skinny shoulders.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Samuel grunts with the effort.
  EXPRESSION: Strained
- CHARACTER: Narrator
  LINE: Samuel’s serious face as he checks the apparatus.
  EXPRESSION: Serious
- CHARACTER: Narrator
  LINE: His legs running up the stairs.
  EXPRESSION: Energetic
- CHARACTER: Narrator
  LINE: Lounge room. Samuel’s head pokes out of the basement, checking to see if the coast is clear. It is.
  EXPRESSION: Cautious
- CHARACTER: Narrator
  LINE: He pushes a key into the basement door, locking it up.
  EXPRESSION: Focused
- CHARACTER: Narrator
  LINE: Kitchen. Samuel’s skinny legs standing on a chair, his top half obscured by an open cupboard door.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: His hand carefully placing the key back on a key rack.
  EXPRESSION: Careful
- CHARACTER: Narrator
  LINE: Samuel peers around the cupboard door, watching for his mother. He closes it quick and jumps down out of sight.
  EXPRESSION: Sneaky
- CHARACTER: Narrator
  LINE: Bedroom. The arm is still there. Alarm still blaring.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: A crashing sound downstairs. The arm retracts quickly, like a crab in a shell. Amelia pops out from under the covers, looking like shit. She slaps the alarm off, listening.
  EXPRESSION: Startled
- CHARACTER: Narrator
  LINE: Another crashing sound, a bigger one.
  EXPRESSION: Concerned
- CHARACTER: Narrator
  LINE: She leaps out of bed, racing out of the room.
  EXPRESSION: Alarmed

::PATHS::
- CHOICE: "Go to the lounge room"
  TARGET: lounge_room_morning
  STATE_CHANGE: frustration = +2, tiredness = -1
  CONDITION: null

::SCENE::
LOCATION: Lounge Room
MOOD: Frustrated
CHARACTERS: Amelia, Samuel, Bugsy, Narrator
BACKGROUND_IMAGE: lounge_room_messy.png
BACKGROUND_EDIT: "Morning, messy lounge room, toys everywhere, broken TV"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Amelia reaches the bottom stairs.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Sam’s catapult covers his body, comes up over his head. At the top sits a plastic cup with a cricket ball in it.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The lounge room is a mess, swords, toy soldiers and other ‘boy war paraphernalia’ everywhere. The big old tube TV has been knocked off its stand and lies on its side.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Bugsy is in the midst of it, barking, wagging his tail.
  EXPRESSION: Happy
- CHARACTER: Narrator
  LINE: Amelia struggles with all her might to hold her temper.
  EXPRESSION: Restraining Anger
- CHARACTER: Samuel
  LINE: It’s not broken! It just slipped.
  EXPRESSION: Defensive
- CHARACTER: Narrator
  LINE: She calmly walks to the TV, her movements controlled.
  EXPRESSION: Controlled
- CHARACTER: Amelia
  LINE: I don’t want you using the hammer and nails-
  EXPRESSION: Firm
- CHARACTER: Samuel
  LINE: Wait look at this! When the monster comes
  EXPRESSION: Eager

::PATHS::
- CHOICE: "End of excerpt"
  TARGET: end
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: The Room
MOOD: Tense
CHARACTERS: Amelia, Samuel, Narrator
BACKGROUND_IMAGE: room_interior.png
BACKGROUND_EDIT: "Interior of a room, possibly a child's bedroom or living space, in the morning"

::SCRIPT::
- CHARACTER: Amelia
  LINE: Not inside the house Samuel-
  EXPRESSION: Worried
- CHARACTER: Samuel
  LINE: I push down here-
  EXPRESSION: Determined
- CHARACTER: Narrator
  LINE: He pushes down hard, a lever rises and launches the ball.
  EXPRESSION: null
- CHARACTER: Amelia
  LINE: Don’t!
  EXPRESSION: Alarmed
- CHARACTER: Narrator
  LINE: It smashes a perfect hole in one of the windows.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Amelia stares at the hole, imploding. Samuel’s face crumples with anxiety.
  EXPRESSION: Shocked

::PATHS::
- CHOICE: "Continue"
  TARGET: samuels_room
  STATE_CHANGE: amelia_stress = +1, samuel_anxiety = +1
  CONDITION: null

::SCENE::
LOCATION: Samuel’s Room
MOOD: Mixed (Playful, Tense, Affectionate)
CHARACTERS: Samuel, Amelia, Bugsy, Narrator
BACKGROUND_IMAGE: samuels_room.png
BACKGROUND_EDIT: "A child's bedroom, morning light, school uniform, magician's hat"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Samuel waves his hands in the air. He has his school uniform on finished off by a sparkly magician’s hat.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Bugsy is jumping up and down and barking.
  EXPRESSION: null
- CHARACTER: Samuel
  LINE: Nothing in my hands. Nothing in my hands.
  EXPRESSION: Playful
- CHARACTER: Amelia
  LINE: Stand still please..
  EXPRESSION: Patient
- CHARACTER: Narrator
  LINE: He does. For three seconds.
  EXPRESSION: null
- CHARACTER: Amelia
  LINE: I don’t want you making weapons anymore.
  EXPRESSION: Firm
- CHARACTER: Samuel
  LINE: You have to look at me. Mum? It doesn’t work if you-
  EXPRESSION: Insistent
- CHARACTER: Narrator
  LINE: She pins him with her gaze.
  EXPRESSION: null
- CHARACTER: Amelia
  LINE: This monster thing has got to stop. Alright?
  EXPRESSION: Gentle
- CHARACTER: Narrator
  LINE: Samuel waves his arms about. Bugsy continues to bark.
  EXPRESSION: null
- CHARACTER: Samuel
  LINE: Nothing in my hands.
  EXPRESSION: Playful
- CHARACTER: Amelia
  LINE: Samuel?
  EXPRESSION: Firmer
- CHARACTER: Narrator
  LINE: POOF! A beautiful bunch of paper flowers pops into Samuel’s hands, seemingly out of nowhere.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Amelia smiles in spite of herself. She takes the paper bouquet. Sam touches her cheek very gently. She softens.
  EXPRESSION: null
- CHARACTER: Amelia
  LINE: That feels nice.
  EXPRESSION: Content
- CHARACTER: Narrator
  LINE: Sam hugs her, she hugs him back. He kisses her cheeks, grips her tighter and tighter. She hides her annoyance.
  EXPRESSION: null
- CHARACTER: Amelia
  LINE: That’s enough now..
  EXPRESSION: Restrained
- CHARACTER: Narrator
  LINE: Samuel won’t stop, he hugs her really tight. She recoils.
  EXPRESSION: null
- CHARACTER: Amelia
  LINE: Don’t do that!
  EXPRESSION: Snapping
- CHARACTER: Narrator
  LINE: Sam stops in his tracks. Amelia immediately looks guilty.
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue to car"
  TARGET: car_morning
  STATE_CHANGE: amelia_stress = +1, samuel_mood = upset
  CONDITION: null

::SCENE::
LOCATION: Car
MOOD: Tense
CHARACTERS: Amelia, Samuel, Narrator
BACKGROUND_IMAGE: car_interior.png
BACKGROUND_EDIT: "Messy car interior, morning traffic, focus on Amelia and Samuel"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The car is a junk heap, inside and out. Takeaway coffee cups, lolly wrappers, plastic containers, kid’s socks.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Amelia focuses on getting through the traffic. Samuel focuses on the back of his mum’s head.
  EXPRESSION: null
- CHARACTER: Samuel
  LINE: If I fired nails into its chest, would that kill it?
  EXPRESSION: Curious
- CHARACTER: Amelia
  LINE: Kill what?
  EXPRESSION: Distant
- CHARACTER: Samuel
  LINE: The monster in my dream.
  EXPRESSION: Annoyed
- CHARACTER: Amelia
  LINE: It certainly wouldn’t make it happy.
  EXPRESSION: Neutral
- CHARACTER: Samuel
  LINE: What about if I fired them into its head?
  EXPRESSION: Curious
- CHARACTER: Amelia
  LINE: That’d probably do it.
  EXPRESSION: Indifferent
- CHARACTER: Samuel
  LINE: If I fired them into its chest-
  EXPRESSION: Insistent
- CHARACTER: Amelia
  LINE: Let’s talk about something else, alright?
  EXPRESSION: Annoyed
- CHARACTER: Narrator
  LINE: Samuel looks out the window. Amelia keeps her eyes straight ahead. Silence.
  EXPRESSION: null
- CHARACTER: Samuel
  LINE: If I fired them into its eyes, I could run away because it’d be blinded.
  EXPRESSION: Quiet
- CHARACTER: Narrator
  LINE: Amelia stares straight ahead, choosing to ignore him.
  EXPRESSION: null
- CHARACTER: Samuel
  LINE: Mum?
  EXPRESSION: SeekingAttention

::PATHS::
- CHOICE: "Arrive at school"
  TARGET: school_entrance
  STATE_CHANGE: amelia_stress = +1
  CONDITION: null

::SCENE::
LOCATION: School Entrance (Car Interior)
MOOD: Rushed
CHARACTERS: Amelia, Samuel, Narrator
BACKGROUND_IMAGE: school_entrance.png
BACKGROUND_EDIT: "Morning, school entrance, expensive cars contrasting with Amelia's hatchback"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The decrepit hatchback rolls to a stop, standing out like a sore thumb amongst the Mercs and Audis.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Samuel climbs over the front seat, just to kiss his mum.
  EXPRESSION: null
- CHARACTER: Amelia
  LINE: Off you go. You’re late already.
  EXPRESSION: Rushed
- CHARACTER: Narrator
  LINE: He climbs back over, grabs his bag. It’s really heavy.
  EXPRESSION: null
- CHARACTER: Amelia
  LINE: What have you got in there?
  EXPRESSION: Curious
- CHARACTER: Samuel
  LINE: See you later alligator!
  EXPRESSION: Cheerful

::PATHS::
- CHOICE: "Samuel leaves, Amelia drives off"
  TARGET: car_amelia_alone
  STATE_CHANGE: samuel_at_school = true
  CONDITION: null

::SCENE::
LOCATION: Car
MOOD: Uplifting then Disgusted
CHARACTERS: Amelia, Narrator
BACKGROUND_IMAGE: car_interior.png
BACKGROUND_EDIT: "Amelia alone in her car, upbeat music playing"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Amelia has very upbeat music playing full blast in her car bubble. She sings along without inhibition, happy.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: She glances down, notices a small cockroach on her leg. She immediately stops singing, sweeps it away in disgust.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Then straight back into it, singing her heart out.
  EXPRESSION: null

::PATHS::
- CHOICE: "Drive to work"
  TARGET: nursing_home_morning
  STATE_CHANGE: amelia_mood = happy, amelia_job_focus = true
  CONDITION: null

::SCENE::
LOCATION: Nursing Home
MOOD: Somber, Patient
CHARACTERS: Amelia, Ron, Norma, Narrator
BACKGROUND_IMAGE: nursing_home.png
BACKGROUND_EDIT: "Interior of a nursing home, morning, elderly residents, cheerful music but somber atmosphere"

::SCRIPT::
- CHARACTER: Narrator
  LINE: An ancient woman’s sleeping face, her mouth hangs open.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Another very old lady, her head in her shaky hand.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Cheery music plays in the background. Despite this, the atmosphere is funereal.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: An elderly man without his teeth in. He watches Amelia as she arrives with a warm smile and two cups of tea.
  EXPRESSION: null
- CHARACTER: Amelia
  LINE: Here you go Ron. Nice cup of tea.
  EXPRESSION: Warm
- CHARACTER: Narrator
  LINE: He takes the tea offered, chewing on his gums absently.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Amelia moves to the ancient woman, staring into space.
  EXPRESSION: null
- CHARACTER: Amelia
  LINE: And one for you Norma, that’s got milk in it.
  EXPRESSION: Loving
- CHARACTER: Norma
  LINE: What?
  EXPRESSION: Confused
- CHARACTER: Amelia
  LINE: That’s got milk in it.
  EXPRESSION: Loving
- CHARACTER: Norma
  LINE: I don’t want milk.
  EXPRESSION: Confused
- CHARACTER: Amelia
  LINE: You said you wanted milk.
  EXPRESSION: Patient
- CHARACTER: Norma
  LINE: No, I don’t want that.
  EXPRESSION: Resigned
- CHARACTER: Amelia
  LINE: Not to worry, I’ll make you another one.
  EXPRESSION: Friendly
- CHARACTER: Narrator
  LINE: Amelia gives the befuddled Norma a friendly smile.
  EXPRESSION: null

::PATHS::
- CHOICE: "Go to the kitchen"
  TARGET: nursing_home_kitchen_day
  STATE_CHANGE: amelia_job_duty = +1
  CONDITION: null

::SCENE::
LOCATION: Nursing Home Kitchen
MOOD: Lighthearted
CHARACTERS: Amelia, Robbie, Narrator
BACKGROUND_IMAGE: nursing_home_kitchen.png
BACKGROUND_EDIT: "Brightly lit kitchen in a nursing home, daytime"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Amelia focuses on stacking the dishwasher, serious.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Robbie, a sweet, slightly chubby (male) nurse enters.
  EXPRESSION: null
- CHARACTER: Robbie
  LINE: Just where a woman should be, in the kitchen.
  EXPRESSION: Teasing
- CHARACTER: Narrator
  LINE: Amelia gets the joke, brightens up.
  EXPRESSION: null
- CHARACTER: Amelia
  LINE: Get to work, woman!
  EXPRESSION: Playful
- CHARACTER: Narrator
  LINE: They laugh. Robbie fills a mug with water and drinks it.
  EXPRESSION: null
- CHARACTER: Amelia
  LINE: Do you want a cuppa?
  EXPRESSION: Polite
- CHARACTER: Robbie
  LINE: Nah, I’m heading for the Dementia ward.
  EXPRESSION: Casual
- CHARACTER: Amelia
  LINE: You’ve got a few years before you end up there.
  EXPRESSION: Witty
- CHARACTER: Narrator
  LINE: He laughs. Amelia smiles.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Robbie hovers. Amelia stacks the dishwasher, shy.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Robbie eventually puts his cup in the dishwasher and leaves.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Amelia relaxes slightly when he’s gone.
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue with work duties"
  TARGET: nursing_home_afternoon
  STATE_CHANGE: amelia_mood = relaxed
  CONDITION: null

::SCENE::
LOCATION: Nursing Home (Games Table)
MOOD: Stressful, Patient
CHARACTERS: Amelia, Larry, Mrs. Winter, Narrator
BACKGROUND_IMAGE: nursing_home_games_table.png
BACKGROUND_EDIT: "Afternoon, nursing home common area, residents playing a game"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Amelia is playing ‘colour shape lotto’ at the games table.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: One of the old ladies places a card on the board.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Pause. Amelia waits very patiently.
  EXPRESSION: null
- CHARACTER: Amelia
  LINE: That’s it Larry, your go.
  EXPRESSION: Patient
- CHARACTER: Narrator
  LINE: Pause. He doesn’t put anything down. Pause.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The woman next to him, head in hand, emits a low wailing sound. Amelia politely ignores it.
  EXPRESSION: null
- CHARACTER: Amelia
  LINE: Same colour or same shape or both. I can help you if you like.
  EXPRESSION: Gentle
- CHARACTER: Narrator
  LINE: The woman’s wail rises in pitch and volume. The players become agitated. Amelia can’t ignore it any longer.
  EXPRESSION: null
- CHARACTER: Amelia
  LINE: It’s alright Mrs Winter, you don’t have to play. It’s OK.
  EXPRESSION: VeryPatient
- CHARACTER: Narrator
  LINE: The old woman wails like someone being murdered. Amelia rubs her back tenderly, hiding every ounce of stress.
  EXPRESSION: null

::PATHS::
- CHOICE: "Finish work for the day"
  TARGET: work_kitchen_afternoon
  STATE_CHANGE: amelia_stress = +1
  CONDITION: null

::SCENE::
LOCATION: Work Kitchen
MOOD: Worried
CHARACTERS: Amelia, Beverly, Narrator
BACKGROUND_IMAGE: work_kitchen_cupboard.png
BACKGROUND_EDIT: "Amelia scrubbing a cupboard in a work kitchen, afternoon"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Amelia is on her knees with her head inside an empty cupboard. She scrubs as if her life depended on it.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Amelia’s supervisor Beverly arrives, irritated.
  EXPRESSION: null
- CHARACTER: Beverly
  LINE: Amelia.
  EXPRESSION: Irritated
- CHARACTER: Narrator
  LINE: Amelia bumps her head as she backs out.
  EXPRESSION: null
- CHARACTER: Beverly
  LINE: Your son’s school is on the phone.
  EXPRESSION: Curt
- CHARACTER: Narrator
  LINE: Amelia looks worried.
  EXPRESSION: null

::PATHS::
- CHOICE: "Go to the principal's office"
  TARGET: principals_office
  STATE_CHANGE: amelia_stress = +2, amelia_worry = +1
  CONDITION: null

::SCENE::
LOCATION: Principal’s Office
MOOD: Grave, Ashamed
CHARACTERS: Amelia, Principal, Teacher, Narrator
BACKGROUND_IMAGE: principals_office.png
BACKGROUND_EDIT: "Afternoon, principal's office, serious atmosphere"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Amelia sits opposite the principal, a tired looking man in his 50s, and Sam’s teacher, a dour, middle aged woman. The principal is grave, the teacher looks traumatized.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The principal lays down a sinister contraption made from a belt, with some wood, screws and nails attached to it.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Amelia’s face falls. This is worse than she imagined.
  EXPRESSION: null
- CHARACTER: Principal
  LINE: This is the home made gun he demonstrated in class today. It fires off nails.
  EXPRESSION: Grave
- CHARACTER: Amelia
  LINE: Oh my God. Did he hurt anyone?
  EXPRESSION: Shocked
- CHARACTER: Teacher
  LINE: The nails could have gone right into a child’s eye. Or worse.
  EXPRESSION: Traumatized
- CHARACTER: Narrator
  LINE: Amelia studies the gun, parental shame creeping over her.
  EXPRESSION: null
- CHARACTER: Amelia
  LINE: I’m so sorry. I had no idea. I’m going to have a serious talk with him-
  EXPRESSION: Genuine
- CHARACTER: Principal
  LINE: Mrs Vanek, we’ve had the talks, we’ve had the sessions with the counsellor... Miss Bowen can’t have the boy in her class anymore without supervision, it’s just too dangerous. We’re going to have to employ a monitor for him.
  EXPRESSION: Serious
- CHARACTER: Amelia
  LINE: A mon
  EXPRESSION: Interrupted

::PATHS::
- CHOICE: "React to the news"
  TARGET: end
  STATE_CHANGE: amelia_stress = +3, amelia_shame = +1
  CONDITION: null

::SCENE::
LOCATION: Principal's Office
MOOD: Tense, Confrontational
CHARACTERS: Principal, Amelia, Teacher
BACKGROUND_IMAGE: principals_office.png
BACKGROUND_EDIT: "Daytime, formal office, serious atmosphere"

::SCRIPT::
- CHARACTER: Principal
  LINE: He’ll still be in the class, but he’ll be separated from the other children. The monitor will supervise him one on one.
  EXPRESSION: null
- CHARACTER: Amelia
  LINE: All the time?
  EXPRESSION: Worried
- CHARACTER: Principal
  LINE: Yes...
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Amelia searches both their faces, becoming desperate.
  EXPRESSION: Desperate
- CHARACTER: Amelia
  LINE: Please. Samuel won’t cope with this. He already feels so different.
  EXPRESSION: Desperate
- CHARACTER: Principal
  LINE: I understand your concern, but this is the only way we can keep him in school.
  EXPRESSION: Firm
- CHARACTER: Amelia
  LINE: I’ll have a talk to him-
  EXPRESSION: Desperate
- CHARACTER: Principal
  LINE: Mrs Vanek...
  EXPRESSION: Interrupting
- CHARACTER: Amelia
  LINE: I’ll have a serious talk and I know he’ll settle down.
  EXPRESSION: Desperate
- CHARACTER: Principal
  LINE: The boy has significant behavioural problems.
  EXPRESSION: Firm
- CHARACTER: Narrator
  LINE: Miss Bowen and myself realize you’ve had a rough trot so we’ve tried to be as lenient as we can...
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Amelia’s vulnerable demeanour shifts, her face tenses.
  EXPRESSION: Tense
- CHARACTER: Amelia
  LINE: Sorry?
  EXPRESSION: Confused
- CHARACTER: Narrator
  LINE: Uncomfortable moment. He treads very carefully.
  EXPRESSION: null
- CHARACTER: Principal
  LINE: Sometimes.. boys.. can be very hard to handle when there’s no father around.
  EXPRESSION: Cautious
- CHARACTER: Amelia
  LINE: Oh I see. I’m a single mother so I can’t look after my child, is that right?
  EXPRESSION: Angry
- CHARACTER: Principal
  LINE: No, no that’s not what I meant-
  EXPRESSION: Defensive
- CHARACTER: Amelia
  LINE: Samuel doesn’t need a full time monitor, he needs some understanding!
  EXPRESSION: Frustrated
- CHARACTER: Teacher
  LINE: Are you saying I’m not understanding?
  EXPRESSION: Defensive
- CHARACTER: Amelia
  LINE: I’m just saying he needs more care at the moment, that’s all!
  EXPRESSION: Frustrated
- CHARACTER: Teacher
  LINE: I have 24 other 1st graders in that class! Would you like me to put them all at risk for your son?
  EXPRESSION: Angry
- CHARACTER: Principal
  LINE: Please, let’s just keep calm here -
  EXPRESSION: Calming
- CHARACTER: Teacher
  LINE: -I’m not a psychologist!
  EXPRESSION: Frustrated
- CHARACTER: Narrator
  LINE: Amelia stands, defensive.
  EXPRESSION: Defensive
- CHARACTER: Amelia
  LINE: You know what? I think it’s best I just look for another school.
  EXPRESSION: Determined
- CHARACTER: Principal
  LINE: Mrs Vanek, you can’t just take the boy out of school. We’ll have to inform Community Services.
  EXPRESSION: Exasperated
- CHARACTER: Amelia
  LINE: You do what you need to do, and I’ll find a school that sees my son as a human being, not a problem to be gotten rid of.
  EXPRESSION: Defiant
- CHARACTER: Principal
  LINE: That’s very unfair. We’re only trying to help the boy.
  EXPRESSION: Defensive
- CHARACTER: Amelia
  LINE: Please stop calling him ‘the boy.’ His name is Samuel.
  EXPRESSION: Angry

::PATHS::
- CHOICE: "Leave the office"
  TARGET: school_hallway
  STATE_CHANGE: amelia_angry = +1, samuel_status = "removed_from_school"
  CONDITION: null

::SCENE::
LOCATION: School Hallway
MOOD: Sadness, Helplessness
CHARACTERS: Amelia, Samuel
BACKGROUND_IMAGE: school_hallway.png
BACKGROUND_EDIT: "Afternoon, empty hallway, somber lighting"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Amelia spies Samuel sitting with a 7th grader on a bench at the end of the hall. She can see he’s been crying. His eyes are red and puffy. She approaches, bracing herself.
  EXPRESSION: null
- CHARACTER: Samuel
  LINE: I wasn’t going to hurt anyone...
  EXPRESSION: Sad
- CHARACTER: Narrator
  LINE: Amelia crouches down. She chooses her words carefully.
  EXPRESSION: null
- CHARACTER: Amelia
  LINE: We’re going to have a break from school for a little while.
  EXPRESSION: Gentle
- CHARACTER: Narrator
  LINE: Samuel’s face crumbles, his mouth opens wide in a silent scream. Then the wail starts up. It’s devastating.
  EXPRESSION: Devastated
- CHARACTER: Narrator
  LINE: Amelia takes his hand and slowly leads him down the hall. Her look of helplessness says it all.
  EXPRESSION: Helpless

::PATHS::
- CHOICE: "Go home"
  TARGET: car_interior
  STATE_CHANGE: samuel_distraught = +1, amelia_helpless = +1
  CONDITION: null

::SCENE::
LOCATION: Car Interior
MOOD: Melancholy, Attempted Comfort
CHARACTERS: Amelia, Samuel
BACKGROUND_IMAGE: car_interior.png
BACKGROUND_EDIT: "Afternoon, driving, quiet, introspective"

::SCRIPT::
- CHARACTER: Amelia
  LINE: I’m going to buy you a big tub of ice cream. What would you like?
  EXPRESSION: Comforting
- CHARACTER: Samuel
  LINE: Miss Bowen hates me.
  EXPRESSION: Sad
- CHARACTER: Amelia
  LINE: No she doesn’t. You just need a break.
  EXPRESSION: Reassuring
- CHARACTER: Narrator
  LINE: Samuel doesn’t respond, just stares out the window.
  EXPRESSION: Distant
- CHARACTER: Amelia
  LINE: We can see Ruby and Aunty Claire at the park today. Would you like that?
  EXPRESSION: Hopeful
- CHARACTER: Narrator
  LINE: Samuel looks out the window, not responding.
  EXPRESSION: Distant
- CHARACTER: Amelia
  LINE: You can play on that swing you like. For as long as you like. OK?
  EXPRESSION: Encouraging
- CHARACTER: Narrator
  LINE: He nods, warming up a little.
  EXPRESSION: Slightly improved
- CHARACTER: Amelia
  LINE: Don’t tell Aunty Claire what happened. I’ll tell her later...
  EXPRESSION: Concerned
- CHARACTER: Samuel
  LINE: Are you gonna stay at home with me all the time now Mum?
  EXPRESSION: Hopeful
- CHARACTER: Amelia
  LINE: We’ll sort something out.
  EXPRESSION: Smiling
- CHARACTER: Narrator
  LINE: Her smiles sticks, but her eyes look worried.
  EXPRESSION: Worried

::PATHS::
- CHOICE: "Head to the supermarket"
  TARGET: supermarket_checkout
  STATE_CHANGE: amelia_worried = +1, samuel_calmer = +1
  CONDITION: null

::SCENE::
LOCATION: Supermarket Checkout
MOOD: Embarrassment, Tension
CHARACTERS: Amelia, Samuel, Little Girl, Mother
BACKGROUND_IMAGE: supermarket_checkout.png
BACKGROUND_EDIT: "Afternoon, busy but with focus on characters, bright store lights"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Amelia has vagued out. The ‘beep beep’ of the register just white noise in the background.
  EXPRESSION: Distracted
- CHARACTER: Narrator
  LINE: She sees Samuel performing a magic trick for a little girl near the bubble gum dispenser.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: She pays as quick as she can keeping one eye on her son.
  EXPRESSION: Rushed
- CHARACTER: Narrator
  LINE: The little girl’s mother arrives, looking relieved. Amelia rushes to Samuel at the same time.
  EXPRESSION: null
- CHARACTER: Little Girl
  LINE: Watch this Mummy!
  EXPRESSION: Excited
- CHARACTER: Samuel
  LINE: I can do it again!
  EXPRESSION: Eager
- CHARACTER: Narrator
  LINE: The mother and Amelia register each other, smiling.
  EXPRESSION: Polite
- CHARACTER: Amelia
  LINE: No Samuel, don’t bother the lady.
  EXPRESSION: Apologetic
- CHARACTER: Mother
  LINE: We’ve got to get home and see Daddy, haven’t we?
  EXPRESSION: Polite
- CHARACTER: Narrator
  LINE: The mother smiles at Samuel.
  EXPRESSION: Polite
- CHARACTER: Samuel
  LINE: My Dad’s in the cemetery.
  EXPRESSION: Matter-of-fact
- CHARACTER: Narrator
  LINE: The woman’s face drops. Amelia tenses.
  EXPRESSION: null
- CHARACTER: Samuel
  LINE: He got killed driving Mum to the hospital to have me --
  EXPRESSION: Explaining
- CHARACTER: Amelia
  LINE: Samuel!
  EXPRESSION: Panicked
- CHARACTER: Amelia
  LINE: I’m sorry he just..
  EXPRESSION: Apologetic
- CHARACTER: Mother
  LINE: Oh, that’s.. I...
  EXPRESSION: Awkward
- CHARACTER: Mother
  LINE: Well, isn’t your Mum lucky to have you then!
  EXPRESSION: Forced
- CHARACTER: Narrator
  LINE: She practically runs off, clutching her child’s hand. Amelia watches them leave, embarrassed, sad.
  EXPRESSION: Embarrassed

::PATHS::
- CHOICE: "Go to the park"
  TARGET: park_outdoor
  STATE_CHANGE: amelia_embarrassed = +1, samuel_innocent = +1
  CONDITION: null

::SCENE::
LOCATION: Park
MOOD: Familial Tension, Worry
CHARACTERS: Amelia, Samuel, Claire, Ruby
BACKGROUND_IMAGE: park_outdoor.png
BACKGROUND_EDIT: "Afternoon, sunny, playground equipment, children playing"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Samuel climbs up onto the swing seat, looks to his mum.
  EXPRESSION: Anticipating
- CHARACTER: Narrator
  LINE: Amelia sits on a bench with her younger sister CLAIRE, a ‘young professional’, immaculately groomed. Claire’s 5 YO daughter RUBY plays close to her mum, a total princess.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Amelia watches Samuel, massaging her jaw, preoccupied.
  EXPRESSION: Preoccupied
- CHARACTER: Claire
  LINE: The artist was so drunk he vomited right in front of his own installation. We lost all these sales. Robert was beside himself...
  EXPRESSION: Annoyed
- CHARACTER: Claire
  LINE: You’re not listening.
  EXPRESSION: Irritated
- CHARACTER: Amelia
  LINE: No no I am listening, you lost all these sales. What happened then?
  EXPRESSION: Snapping to
- CHARACTER: Samuel
  LINE: MUM!
  EXPRESSION: Calling out
- CHARACTER: Narrator
  LINE: The women look up at Samuel.
  EXPRESSION: null
- CHARACTER: Samuel
  LINE: I’m gonna jump on the monster and break it in HALF! Watch...
  EXPRESSION: Enthusiastic
- CHARACTER: Narrator
  LINE: He leaps. Amelia feigns interest, massaging her jaw.
  EXPRESSION: Feigning interest
- CHARACTER: Claire
  LINE: Is that tooth still playing up?
  EXPRESSION: Concerned
- CHARACTER: Narrator
  LINE: Amelia immediately stops massaging.
  EXPRESSION: Self-conscious
- CHARACTER: Claire
  LINE: Go to the dentist.
  EXPRESSION: Irritated
- CHARACTER: Amelia
  LINE: Two thousand dollars later...
  EXPRESSION: Resigned
- CHARACTER: Claire
  LINE: Do you need to borrow some money?
  EXPRESSION: Offering
- CHARACTER: Amelia
  LINE: No, no it’s fine. I just need a good night’s sleep.
  EXPRESSION: Bright
- CHARACTER: Claire
  LINE: Ruby don’t play there sweetie it’s wet.
  EXPRESSION: Protective
- CHARACTER: Narrator
  LINE: Ruby stands up and smooths her skirt down perfectly.
  EXPRESSION: Meticulous
- CHARACTER: Amelia
  LINE: I was going to ask you for one favour.. I completely forgot there’s a pupil free day tomorrow. Would you be able to look after Samuel for the day?
  EXPRESSION: Tentative
- CHARACTER: Claire
  LINE: The whole day?
  EXPRESSION: Hesitant
- CHARACTER: Amelia
  LINE: I can’t get out of work.
  EXPRESSION: Explaining
- CHARACTER: Narrator
  LINE: Claire hesitates for more than a moment.
  EXPRESSION: Hesitant
- CHARACTER: Amelia
  LINE: That’s OK, I’ll ..... dag. I can just put on a DVD for him or something.
  EXPRESSION: Bright
- CHARACTER: Claire
  LINE: Don’t be stupid you organize something else.
  EXPRESSION: Dismissive
- CHARACTER: Samuel
  LINE: I can jump from here and smash its head!
  EXPRESSION: Boasting
- CHARACTER: Narrator
  LINE: He’s climbed up higher, jumps, does a forward roll, gets straight up to punch the air. Claire is unimpressed.
  EXPRESSION: null
- CHARACTER: Amelia
  LINE: Be careful.
  EXPRESSION: Worried
- CHARACTER: Amelia
  LINE: What would you like me to do for Wednesday? I can get their birthday cakes, that’s easy.
  EXPRESSION: Obliging
- CHARACTER: Claire
  LINE: Meels.... I’ve wanted to tell you. I was hoping Ruby would change her mind...
  EXPRESSION: Reluctant
- CHARACTER: Narrator
  LINE: Beat. Amelia waits for the bad news.
  EXPRESSION: Anxious
- CHARACTER: Claire
  LINE: She doesn’t want a joint party with Sam this year. It’s stupid I know, their birthdays are so close.
  EXPRESSION: Sheepish
- CHARACTER: Amelia
  LINE: Oh...
  EXPRESSION: Taken aback
- CHARACTER: Claire
  LINE: She wants her own birthday cake, her own party games. She wants a princess party.
  EXPRESSION: Explaining
- CHARACTER: Amelia
  LINE: That’s OK. We don’t have to come.
  EXPRESSION: Hurt
- CHARACTER: Claire
  LINE: You can still come, stupid. She just doesn
  EXPRESSION: Reassuring

::PATHS::
- CHOICE: "End of excerpt"
  TARGET: end
  STATE_CHANGE: amelia_hurt = +1, claire_guilty = +1
  CONDITION: null

::SCENE::
LOCATION: Park
MOOD: Tense
CHARACTERS: Claire, Amelia, Samuel, Narrator
BACKGROUND_IMAGE: park.png
BACKGROUND_EDIT: "Daytime, playground with swings"

::SCRIPT::
- CHARACTER: Claire
  LINE: ’t want to share the day with Sam anymore, that’s all...
  EXPRESSION: Annoyed
- CHARACTER: Amelia
  LINE: I understand. A little girl needs to feel special on her birthday..
  EXPRESSION: Understanding
- CHARACTER: Narrator
  LINE: Pause.
  EXPRESSION: null
- CHARACTER: Claire
  LINE: Now I feel bad.
  EXPRESSION: Guilty
- CHARACTER: Amelia
  LINE: You shouldn’t feel bad! I’m sure Sam will be OK with it-
  EXPRESSION: Reassuring
- CHARACTER: Samuel
  LINE: Mum, I can go really high!
  EXPRESSION: Excited
- CHARACTER: Narrator
  LINE: They clock him briefly. Samuel climbs higher than before.
  EXPRESSION: null
- CHARACTER: Claire
  LINE: Maybe you want to celebrate his birthday properly this year anyway. On the day. You’ve still got two weeks to plan it.
  EXPRESSION: Suggesting
- CHARACTER: Amelia
  LINE: We’ll think of something.
  EXPRESSION: Strained
- CHARACTER: Narrator
  LINE: Samuel climbs up to the very top. The women don’t notice.
  EXPRESSION: null
- CHARACTER: Claire
  LINE: You know Amelia, I just want you to be happy, then this birthday thing rolls around and I end up feeling awful.
  EXPRESSION: Annoyed
- CHARACTER: Narrator
  LINE: Samuel climbs higher and higher. They still don’t see.
  EXPRESSION: null
- CHARACTER: Amelia
  LINE: I don’t want you to feel awful Claire. We’ll be fine. We’ll be absolutely fine.
  EXPRESSION: Reassuring
- CHARACTER: Samuel
  LINE: MUM! LOOK AT ME!
  EXPRESSION: Seeking attention
- CHARACTER: Narrator
  LINE: The women finally look. Samuel is on the top of the swing with his arms outstretched. He must be 8 feet high.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Amelia springs to her feet, frightened.
  EXPRESSION: Frightened
- CHARACTER: Amelia
  LINE: SAMUEL!!
  EXPRESSION: Frightened

::PATHS::
- CHOICE: "Leave the park"
  TARGET: car_afternoon
  STATE_CHANGE: amelia_stress = +1, samuel_distress = +1
  CONDITION: null

::SCENE::
LOCATION: Car
MOOD: Tense
CHARACTERS: Amelia, Samuel, Narrator
BACKGROUND_IMAGE: car_interior.png
BACKGROUND_EDIT: "Afternoon, dim light, Amelia driving, Samuel crying in back"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Amelia grips the wheel. Samuel in the background, crying. Amelia makes a conscious effort to not react. Her jaw tightens as her son’s cries get louder and louder.
  EXPRESSION: Stressed

::PATHS::
- CHOICE: "Drive home"
  TARGET: amelia_front_yard
  STATE_CHANGE: amelia_stress = +1, samuel_distress = +1
  CONDITION: null

::SCENE::
LOCATION: Amelia’s Front Yard
MOOD: Downbeat
CHARACTERS: Amelia, Samuel, Mrs. Roach, Bugsy, Narrator
BACKGROUND_IMAGE: front_yard.png
BACKGROUND_EDIT: "Afternoon, crumbling terrace house, path"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Samuel trudges up the path to their crumbling, falling down old terrace. His face is tear stained.
  EXPRESSION: Sad
- CHARACTER: Narrator
  LINE: Amelia stops at the letter box. A bunch of bills, one has FINAL NOTICE written on the outside. She throws them in her bag without opening them.
  EXPRESSION: Worried
- CHARACTER: Narrator
  LINE: Mrs Roach, a sweet elderly neighbour, waters her azaleas. Her hands shake with Parkinsons disease.
  EXPRESSION: null
- CHARACTER: Mrs. Roach
  LINE: Who do we have here!
  EXPRESSION: Friendly
- CHARACTER: Samuel
  LINE: Hello Mrs Roach.
  EXPRESSION: Downbeat
- CHARACTER: Mrs. Roach
  LINE: You look tired little one, have you been in the wars today?
  EXPRESSION: Concerned
- CHARACTER: Samuel
  LINE: Yeah. Few wars.
  EXPRESSION: Resigned
- CHARACTER: Narrator
  LINE: He has the keys in hand, he unlocks and opens the door. Bugsy comes rushing out the door, jumping up on Samuel. Sam crouches down to hug the dog, then goes inside.
  EXPRESSION: null
- CHARACTER: Amelia
  LINE: He’s had a big day that’s all, he’s just exhausted.
  EXPRESSION: Cheerful
- CHARACTER: Mrs. Roach
  LINE: Poor little one...
  EXPRESSION: Sympathetic
- CHARACTER: Narrator
  LINE: Bugsy comes rushing up to Amelia, she picks him up, cuddles him affectionately.
  EXPRESSION: null
- CHARACTER: Mrs. Roach
  LINE: You look tired too love, are you OK?
  EXPRESSION: Concerned
- CHARACTER: Amelia
  LINE: Nothing that 5 years of sleep wouldn’t fix! No, I’m fine, work’s pretty busy.. I’ll take out the rubbish for you Gracie.
  EXPRESSION: Upbeat
- CHARACTER: Mrs. Roach
  LINE: You just got in pet. You have a break.
  EXPRESSION: Caring
- CHARACTER: Amelia
  LINE: No no, I’ll do it now and then it’s done.
  EXPRESSION: Insistent

::PATHS::
- CHOICE: "Help Mrs. Roach with bins"
  TARGET: mrs_roach_front_house
  STATE_CHANGE: amelia_stress = +0, amelia_social = +1
  CONDITION: null

::SCENE::
LOCATION: Front of Mrs. Roach’s House
MOOD: Masked
CHARACTERS: Amelia, Mrs. Roach, Narrator
BACKGROUND_IMAGE: mrs_roach_house_exterior.png
BACKGROUND_EDIT: "Afternoon, bins outside, neighbour's house"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Amelia drags out two very full and heavy OTTO bins.
  EXPRESSION: Exhausted
- CHARACTER: Narrator
  LINE: Mrs Roach watches, smiling, her hand shakes at her side.
  EXPRESSION: null
- CHARACTER: Mrs. Roach
  LINE: Oh! You’re an absolute angel.
  EXPRESSION: Grateful
- CHARACTER: Narrator
  LINE: Amelia smiles, completely masking the events of the day.
  EXPRESSION: Masking

::PATHS::
- CHOICE: "Go inside"
  TARGET: lounge_room_afternoon
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Lounge Room
MOOD: Suspenseful
CHARACTERS: Amelia, Bugsy, Narrator
BACKGROUND_IMAGE: lounge_room_interior.png
BACKGROUND_EDIT: "Afternoon, living space, basement door"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Amelia sees Bugsy scratching at the basement door. She freezes, watching him.
  EXPRESSION: Wary
- CHARACTER: Narrator
  LINE: Bugsy spots Amelia and scurries to her. She picks him up.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Amelia looks at the door, her face strained. Pause.
  EXPRESSION: Anxious
- CHARACTER: Narrator
  LINE: In a sudden move she strides over and checks the handle. It’s locked. Relieved, she wanders out snuggling Bugsy.
  EXPRESSION: Relieved

::PATHS::
- CHOICE: "Proceed with the evening"
  TARGET: kitchen_table_evening
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Kitchen Table
MOOD: Somber
CHARACTERS: Amelia, Samuel, Narrator
BACKGROUND_IMAGE: kitchen_table.png
BACKGROUND_EDIT: "Evening, dinner time, quiet atmosphere"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Dinner in silence. Amelia studies Sam.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: He shovels food in weakly, his face tired and sad. He looks up to his mum, manages a smile.
  EXPRESSION: Tired
- CHARACTER: Narrator
  LINE: She smiles back. It fades as soon as he looks away, replaced with worry.
  EXPRESSION: Worried

::PATHS::
- CHOICE: "Put Samuel to bed"
  TARGET: samuel_room_night_babadook
  STATE_CHANGE: amelia_worry = +1, samuel_sadness = +1
  CONDITION: null

::SCENE::
LOCATION: Samuel’s Room
MOOD: Unsettling
CHARACTERS: Amelia, Samuel, Narrator
BACKGROUND_IMAGE: samuel_room.png
BACKGROUND_EDIT: "Night, child's bedroom, dimly lit"

::SCRIPT::
- CHARACTER: Narrator
  LINE: POV under the bed. The doona comes up, Amelia and Samuel’s faces peering underneath.
  EXPRESSION: Playful
- CHARACTER: Narrator
  LINE: Black. Closet POV as the doors open. Amelia and Samuel do their nightly routine check for monsters.
  EXPRESSION: Playful
- CHARACTER: Amelia
  LINE: OK?
  EXPRESSION: Reassuring
- CHARACTER: Narrator
  LINE: Samuel nods, but looks nervous. He has his pyjamas on, his hair is washed and combed to the side. Very cute.
  EXPRESSION: Nervous
- CHARACTER: Amelia
  LINE: You can choose one tonight. Anything you like.
  EXPRESSION: Indulgent
- CHARACTER: Narrator
  LINE: He races to the bookshelf, searching through many books.
  EXPRESSION: Eager
- CHARACTER: Narrator
  LINE: One catches his eye. The spine reads MISTER BABADOOK in bold, black letters. He pulls it out, runs to mum.
  EXPRESSION: Intrigued
- CHARACTER: Narrator
  LINE: She takes a look at the cover: a black silhouette of a figure in a coat and top hat. It looks a little strange.
  EXPRESSION: Wary
- CHARACTER: Amelia
  LINE: Where’d you get this?
  EXPRESSION: Bemused
- CHARACTER: Samuel
  LINE: On the shelf.
  EXPRESSION: Casual
- CHARACTER: Narrator
  LINE: He jumps up, opens the book.
  EXPRESSION: Excited
- CHARACTER: Amelia
  LINE: 'If it’s in a word, or it’s in a look, you can’t get rid of The Babadook.’
  EXPRESSION: Reading aloud
- CHARACTER: Narrator
  LINE: It’s a pop up book. Looks like it could even be hand made.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Amelia turns the page.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: A pair of black eyes peep out from behind a door, a tall black top hat perched on top. It looks funny.
  EXPRESSION: null
- CHARACTER: Amelia
  LINE: ‘If you’re a really clever one, and you know what it is to see... Then you can make friends with a special one, a friend of you and me.’
  EXPRESSION: Reading aloud
- CHARACTER: Narrator
  LINE: Amelia pulls a lever, a black gloved hand pops out from behind the door, waving hello. Samuel’s face lights up.
  EXPRESSION: Delighted
- CHARACTER: Amelia
  LINE: ‘His name is Mister Babadook. And this is his book.’
  EXPRESSION: Reading aloud
- CHARACTER: Narrator
  LINE: The book is beautifully done, but somehow creepy.
  EXPRESSION: null
- CHARACTER: Amelia
  LINE: We might read another one tonight, hey?
  EXPRESSION: Uneasy
- CHARACTER: Samuel
  LINE: You said I could choose.
  EXPRESSION: Insistent
- CHARACTER: Narrator
  LINE: A little boy next to a big wardrobe, his hand to his ear. The words ‘RUMBLE RUMBLE RUMBLE’ are written around him.
  EXPRESSION: null
- CHARACTER: Amelia
  LINE: A rumbling sound, then 3 sharp knocks. ‘ba BA-ba DOOK! DOOK! DOOK!’ That’s when you’ll know that he’s around, you’ll see him if you look.
  EXPRESSION: Ominous
- CHARACTER: Narrator
  LINE: Amelia pulls a lever, the words Ba BA-ba DOOK! DOOK! DOOK! pop up. Samuel quickly turns the page.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Mr Babadook in his full form. A black top hat, a long black coat, pointy black gloves. The face is a mask, staring eyes, mouth smiling widely, more like a scream.
  EXPRESSION: Disturbing
- CHARACTER: Amelia
  LINE: This is what he wears on top. He’s funny, don’t you think?
  EXPRESSION: Wary
- CHARACTER: Narrator
  LINE: Creepy more like it. Amelia turns the page, very wary.
  EXPRESSION: Very wary
- CHARACTER: Amelia
  LINE: ‘See him in your room at night and you won’t sleep a wink.’
  EXPRESSION: Ominous
- CHARACTER: Narrator
  LINE: Mister Babadook falls from the ceiling towards the boy. The speech bubble reads ‘LET ME IN!’ The boy screams. The image is very disturbing. Samuel is instantly frightened.
  EXPRESSION: Frightened
- CHARACTER: Narrator
  LINE: Amelia hides the book from Sam, skimming it for herself, concerned. He struggles with her, trying to see it.
  EXPRESSION: Concerned
- CHARACTER: Samuel
  LINE: Does it hurt the boy? Mum??
  EXPRESSION: Scared
- CHARACTER: Narrator
  LINE: A black silhouette of the Babadook raising its arms like big insect wings. It looks freaky.
  EXPRESSION: Freaky
- CHARACTER: Samuel
  LINE: Where does it live?
  EXPRESSION: Scared
- CHARACTER: Amelia
  LINE: ‘I’ll soon take off my funny disguise (Take heed of what you’ve read...)
  EXPRESSION: Reading from book
- CHARACTER: Samuel (O.S.)
  LINE: Does it live under the bed?? Mum??
  EXPRESSION: Anxious
- CHARACTER: Amelia
  LINE: ‘And once you see what’s underneath..’
  EXPRESSION: Reading from book
- CHARACTER: Samuel
  LINE: Mummy.....
  EXPRESSION: Crying
- CHARACTER: Amelia
  LINE: ‘YOU’RE GOING TO WISH YOU WERE DEAD.’
  EXPRESSION: Chilling
- CHARACTER: Narrator
  LINE: She shuts the book quickly as Samuel’s cries escalate.
  EXPRESSION: Distressed

::PATHS::
- CHOICE: "Comfort Samuel"
  TARGET: samuel_room_night_after
  STATE_CHANGE: amelia_worry = +2, samuel_fear = +2
  CONDITION: null

::SCENE::
LOCATION: Samuel’s Room
MOOD: Distressed
CHARACTERS: Amelia, Samuel, Narrator
BACKGROUND_IMAGE: samuel_room.png
BACKGROUND_EDIT: "Night, child's bedroom, comforting but distressed atmosphere"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Amelia patiently reads another story to Samuel who has his arms wrapped around her waist, howling wi
  EXPRESSION: Patient

::PATHS::
- CHOICE: "Continue comforting Samuel"
  TARGET: end
  STATE_CHANGE: null
  CONDITION: null





::SCENE::
LOCATION: Outside Claire's House
MOOD: Tense
CHARACTERS: Narrator, Amelia, Claire, Samuel, Ruby
BACKGROUND_IMAGE: claire_house.png
BACKGROUND_EDIT: "Daytime, semi-mansion exterior, long driveway"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Amelia carts Samuel’s things up the long driveway. She spots Claire waiting out the front of her semi-mansion.
  EXPRESSION: null
- CHARACTER: Claire
  LINE: What have you been doing?
  EXPRESSION: Angry
- CHARACTER: Amelia
  LINE: Sorry.
  EXPRESSION: Afraid
- CHARACTER: Narrator
  LINE: Samuel runs up behind her.
  EXPRESSION: null
- CHARACTER: Claire
  LINE: Day off school hey?
  EXPRESSION: Surprised
- CHARACTER: Samuel
  LINE: I’m not allowed back at school anymore. My teacher can’t stand me.
  EXPRESSION: Sad
- CHARACTER: Amelia
  LINE: That’s not true!
  EXPRESSION: Angry
- CHARACTER: Samuel
  LINE: She told me! In front of the class!
  EXPRESSION: Angry
- CHARACTER: Narrator
  LINE: Claire looks to her sister who can’t look back.
  EXPRESSION: null
- CHARACTER: Claire
  LINE: Is there a pupil free day today?
  EXPRESSION: Surprised
- CHARACTER: Amelia
  LINE: I didn’t want to talk about it in front of the kids.
  EXPRESSION: Afraid
- CHARACTER: Claire
  LINE: So you lie to your sister. That’s nice.
  EXPRESSION: Angry
- CHARACTER: Amelia
  LINE: I just can’t deal with it this morning. Please, I never ask you to look after him-
  EXPRESSION: Sad
- CHARACTER: Narrator
  LINE: Samuel is showing Ruby some DVDs he has and is making explosion noises near her face. She flinches.
  EXPRESSION: null
- CHARACTER: Claire
  LINE: Be gentle, will you Samuel?
  EXPRESSION: Angry
- CHARACTER: Amelia
  LINE: Thanks so much for this. I’ll be back at three on the dot.
  EXPRESSION: Happy

::PATHS::
- CHOICE: "Leave Samuel with Claire"
  TARGET: nursing_home_common_room
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Nursing Home Common Room
MOOD: Frazzled
CHARACTERS: Narrator, Amelia, Elsie, Beverly
BACKGROUND_IMAGE: nursing_home_common_room.png
BACKGROUND_EDIT: "Daytime, old-fashioned common room, scattered old people"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Amelia has a microphone in one hand and a plastic bucket with bingo numbers in the other. She looks frazzled.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The oldies are scattered on various tables. Most aren’t listening, a few are asleep, some have their numbers out.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Upbeat musak plays in the background.
  EXPRESSION: null
- CHARACTER: Amelia
  LINE: Aaaannd, it’s number eleven! Who has number 11? Legs eleven?
  EXPRESSION: Happy
- CHARACTER: Narrator
  LINE: No one responds.
  EXPRESSION: null
- CHARACTER: Amelia
  LINE: OK, let’s try another one...
  EXPRESSION: Happy
- CHARACTER: Narrator
  LINE: She reaches in.
  EXPRESSION: null
- CHARACTER: Amelia
  LINE: 88? Number 88? Two fat ladies?
  EXPRESSION: Happy
- CHARACTER: Narrator
  LINE: After a long time one dedicated player holds up her hand.
  EXPRESSION: null
- CHARACTER: Amelia
  LINE: Good Elsie. Another few days and someone should be able to call ‘bingo.’
  EXPRESSION: Happy
- CHARACTER: Narrator
  LINE: No one gets the joke. She reaches for another number.
  EXPRESSION: null
- CHARACTER: Amelia
  LINE: Number 69? Not too much of that going on in here...
  EXPRESSION: Happy
- CHARACTER: Narrator
  LINE: No one claims the number. Amelia pulls out another one.
  EXPRESSION: null
- CHARACTER: Amelia
  LINE: The next number is 5 billion. Anyone got that? How about 75 gazillion, anyone got that one?
  EXPRESSION: Happy
- CHARACTER: Narrator
  LINE: Some of the sharper members of the crowd look confused.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Beverly pokes her head around the corner. She gives Amelia a disapproving look.
  EXPRESSION: Angry
- CHARACTER: Narrator
  LINE: Amelia shuts up immediately. The musak keeps going.
  EXPRESSION: Afraid

::PATHS::
- CHOICE: "Continue working"
  TARGET: nursing_home_kitchen
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Nursing Home Kitchen
MOOD: Empathetic
CHARACTERS: Narrator, Amelia, Robbie
BACKGROUND_IMAGE: nursing_home_kitchen.png
BACKGROUND_EDIT: "Daytime, functional kitchen, slightly worn"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Amelia has her head in her hand, her eyes closed.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Robbie enters. She springs out of her contemplation.
  EXPRESSION: null
- CHARACTER: Robbie
  LINE: Beverly’s not impressed with you having a sense of humour. Are you alright?
  EXPRESSION: Happy
- CHARACTER: Amelia
  LINE: Yeah yeah, I’m fine. So how, how are you?
  EXPRESSION: Happy
- CHARACTER: Robbie
  LINE: You don’t have to be fine you know.
  EXPRESSION: Happy
- CHARACTER: Narrator
  LINE: Amelia smiles, caught out. She drops her guard a little.
  EXPRESSION: Happy
- CHARACTER: Amelia
  LINE: I am a bit stressed at the moment.
  EXPRESSION: Sad
- CHARACTER: Robbie
  LINE: Why don’t you go home? Old cranky bitch is going after lunch. I’ll cover for you.
  EXPRESSION: Happy
- CHARACTER: Amelia
  LINE: You’d do that? You can have my pay-
  EXPRESSION: Surprised
- CHARACTER: Robbie
  LINE: Don’t be ridiculous. You’ve got a sick kid. Life’s too short.
  EXPRESSION: Happy
- CHARACTER: Amelia
  LINE: You’re so sweet Robbie.
  EXPRESSION: Happy
- CHARACTER: Narrator
  LINE: He gives her a friendly touch on the shoulder, then drops his arm, but stays close. Amelia shifts in her seat.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Robbie touches her hand. Amelia pulls it away like she’s touched a burning stove. They’re both embarrassed.
  EXPRESSION: null
- CHARACTER: Amelia
  LINE: Sorry-
  EXPRESSION: Afraid
- CHARACTER: Robbie
  LINE: I’m an idiot.
  EXPRESSION: Sad
- CHARACTER: Amelia
  LINE: No, no, you’re not an idiot. Not at all..
  EXPRESSION: Afraid
- CHARACTER: Robbie
  LINE: We should do something sometime.
  EXPRESSION: Afraid
- CHARACTER: Amelia
  LINE: Yeah sure. I’ve got a bit on my plate at the moment, but we could have a cuppa sometime or-
  EXPRESSION: Tense
- CHARACTER: Robbie
  LINE: That’d be great. Maybe I can come round-
  EXPRESSION: Happy
- CHARACTER: Amelia
  LINE: Yeah. Or go out. Maybe later, sometime.
  EXPRESSION: Tense
- CHARACTER: Robbie
  LINE: Great!
  EXPRESSION: Happy
- CHARACTER: Narrator
  LINE: It’s almost too much for Amelia. Robbie senses it.
  EXPRESSION: null
- CHARACTER: Robbie
  LINE: You go... Say hello to Sam for me.
  EXPRESSION: Happy
- CHARACTER: Amelia
  LINE: I will...
  EXPRESSION: Happy

::PATHS::
- CHOICE: "Go home"
  TARGET: shopping_centre_montage
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Large Indoor Shopping Centre
MOOD: Reflective
CHARACTERS: Narrator, Amelia, Mum, Baby Girl
BACKGROUND_IMAGE: shopping_centre.png
BACKGROUND_EDIT: "Daytime, bustling indoor shopping centre"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Amelia wanders aimlessly looking at the life teeming around her. A comforting distraction.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Amelia sits on a bench eating an ice cream.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: She notices an adorable baby girl at the end of the bench sitting on her mum’s lap. The mum tickles the little girl’s tummy. She bursts into peals of laughter.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Amelia connects with the mother, they share a warm smile.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The mother focuses back on her child. Amelia’s smile drops slowly, sadness replacing it.
  EXPRESSION: null

::PATHS::
- CHOICE: "Leave the shopping centre"
  TARGET: undercover_car_park
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Undercover Car Park
MOOD: Yearning
CHARACTERS: Narrator, Amelia, Man, Woman, Claire
BACKGROUND_IMAGE: undercover_car_park.png
BACKGROUND_EDIT: "Daytime, dim, concrete car park"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Amelia gets into her car. She sees a man and a woman kissing in their car, opposite her. She doesn’t want to look, but the passion of their embrace draws her in.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The man whispers in the woman’s ear. She laughs, kissing him softly, then deeply, open mouthed.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Amelia watches, yearning, immeasurably sad.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The couple break apart. They happen to look her way.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Amelia looks down, not wanting to be seen. She rummages through her bag, happens to look at her mobile. 10 missed calls. She checks the sender. It’s her sister.
  EXPRESSION: null

::PATHS::
- CHOICE: "Check on Samuel"
  TARGET: outside_claire_house_afternoon
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Outside Claire’s House
MOOD: Chaotic
CHARACTERS: Narrator, Amelia, Claire, Ruby, Samuel
BACKGROUND_IMAGE: claire_house_afternoon.png
BACKGROUND_EDIT: "Afternoon, outside Claire's house, tense atmosphere"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Amelia arrives to a ‘scene’. Ruby is bawling, clinging to her mother. Samuel is curled up in a ball on the lawn, stressed and frightened. Claire’s face is a hard mask.
  EXPRESSION: null
- CHARACTER: Claire
  LINE: Where have you been! You weren’t at work, I’ve rung you a million times!
  EXPRESSION: Angry
- CHARACTER: Amelia
  LINE: What happened?
  EXPRESSION: Afraid
- CHARACTER: Claire
  LINE: He’s just scared the crap out of Ruby.
  EXPRESSION: Angry
- CHARACTER: Narrator
  LINE: The little girl cries, her mother gently shushes her.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Amelia looks at Samuel. He’s spooked.
  EXPRESSION: null
- CHARACTER: Claire
  LINE: He insisted on talking to this bloody Babadook thing, all day. Just talking to the air. It even freaked me out.
  EXPRESSION: Afraid
- CHARACTER: Amelia
  LINE: I’m so sorry.
  EXPRESSION: Sad
- CHARACTER: Claire
  LINE: You need to get him to see someone Amelia. It’s not normal.
  EXPRESSION: Angry
- CHARACTER: Amelia
  LINE: If you don’t want him here for Ruby’s party I understand.
  EXPRESSION: Sad
- CHARACTER: Claire
  LINE: Don’t be stupid. I just don’t want to have to deal with this monster crap-
  EXPRESSION: Angry
- CHARACTER: Samuel
  LINE: IT’S NOT CRAP, IT’S REAL!
  EXPRESSION: Angry
- CHARACTER: Amelia
  LINE: Don’t talk to Aunty Claire like that!
  EXPRESSION: Angry
- CHARACTER: Narrator
  LINE: She strides over. He puts his hands in his pockets, grabs something and throws it at the cement in front of her. It explodes with a bang. The women are stunned.
  EXPRESSION: null

::PATHS::
- CHOICE: "Take Samuel home"
  TARGET: car_afternoon
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Car
MOOD: Tense
CHARACTERS: Narrator, Amelia, Samuel
BACKGROUND_IMAGE: car_interior.png
BACKGROUND_EDIT: "Afternoon, car interior, tense driving"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Amelia grips the wheel, tense. Her eyes flick between traffic and son in the back seat.
  EXPRESSION: null
- CHARACTER: Amelia
  LINE: Where did you get those firecrackers?
  EXPRESSION: Angry
- CHARACTER: Samuel
  LINE: You got them for me on the Internet.
  EXPRESSION: Neutral
- CHARACTER: Amelia
  LINE: Well that’s the end of the Internet.
  EXPRESSION: Angry
- CHARACTER: Narrator
  LINE: Samuel sighs. Amelia tries a much gentler approach.
  EXPRESSION: null
- CHARACTER: Amelia
  LINE: If you keep talking to things that aren’t real, Aunty Claire won’t want you to come over anymore. Samuel?
  EXPRESSION: Sad
- CHARACTER: Narrator
  LINE: No answer. Just stubborn silence.
  EXPRESSION: null
- CHARACTER: Amelia
  LINE: If the Babadook was real, we’d see it right now, wouldn’t we?
  EXPRESSION: Sad
- CHARACTER: Samuel
  LINE: It wants to make us really scared first. Then you’ll see it.
  EXPRESSION: Afraid
- CHARACTER: Amelia
  LINE: Well I’m not scared.
  EXPRESSION: Angry
- CHARACTER: Samuel
  LINE: You will be when it creeps into your room at night.
  EXPRESSION: Afraid
- CHARACTER: Amelia
  LINE: That’s enough-
  EXPRESSION: Angry
- CHARACTER: Samuel
  LINE: You will be when it eats your insides.
  EXPRESSION: Afraid
- CHARACTER: Amelia
  LINE: I’ve decided you’re not having your birthday with Ruby this week. No cake, no games, that’s the end of it.
  EXPRESSION: Angry
- CHARACTER: Narrator
  LINE: Samuel is crushed. Amelia keeps her eyes on the road, grips th
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue driving"
  TARGET: end
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Kitchen / Basement
MOOD: Domestic, then unsettling, tense, determined
CHARACTERS: Amelia, Samuel, Mrs Roach, Bugsy, Oskar (photo)
BACKGROUND_IMAGE: kitchen_basement.png
BACKGROUND_EDIT: "Evening, intercut between a calm kitchen and a child's chaotic basement play"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Kitchen. A pot of soup boils away on the stove. Amelia stirs, focusing on the task. She looks up, and can just see Mrs Roach sitting in her lounge opposite, watching TV. The sight comforts her. She smiles, relaxes.
  EXPRESSION: Happy
- CHARACTER: Narrator
  LINE: Basement. Samuel’s sparkly gloves clapping together. Stuffed toys all lined up in a row. At the end of the line, a photo of Amelia with her husband, OSKAR. They have their arms around each other, smiling.
  EXPRESSION: null
- CHARACTER: Samuel
  LINE: Laayydees and gentlemehhhn! Mum and dad!
  EXPRESSION: Excited
- CHARACTER: Narrator
  LINE: Samuel has his magician outfit on, sparkly coat and hat.
  EXPRESSION: null
- CHARACTER: Samuel
  LINE: Life is not always as it seems. It can be a wonderrus thing..
  EXPRESSION: Confident
- CHARACTER: Narrator
  LINE: He does a quick magic trick. It’s good, he’s got a knack. Bugsy is close by, sniffing around.
  EXPRESSION: null
- CHARACTER: Samuel
  LINE: But it can also be very trecheruss...
  EXPRESSION: Serious
- CHARACTER: Narrator
  LINE: He throws two firecrackers onto the ground. They explode. Bugsy is spooked and hightails it up the stairs.
  EXPRESSION: Afraid
- CHARACTER: Samuel
  LINE: Don’t worry dad, I’m gonna save Mum. I’m gonna trap the Babadook like this..
  EXPRESSION: Determined
- CHARACTER: Narrator
  LINE: He runs to the stairs, and pulls on a rope. It tightens across the stairs like a trip wire.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Kitchen. Amelia sees Bugsy push open the basement door and run through it. She’s shocked to see that door open.
  EXPRESSION: Surprised
- CHARACTER: Narrator
  LINE: Basement.
  EXPRESSION: null
- CHARACTER: Samuel
  LINE: When he’s trapped I’m gonna KILL HIM!
  EXPRESSION: Angry
- CHARACTER: Narrator
  LINE: A newly made nail gun is strapped to his skinny leg. He fires it off. Nails fly through the air like tiny spears.
  EXPRESSION: null
- CHARACTER: Amelia
  LINE: SAMUEL.
  EXPRESSION: Angry
- CHARACTER: Narrator
  LINE: Samuel flinches. He rips off his weapons fast as he can, hides them and bolts upstairs. He’s in huge trouble.
  EXPRESSION: Afraid

::SCENE::
LOCATION: Loungeroom
MOOD: Tense, awkward, shameful, angry
CHARACTERS: Amelia, Samuel, Robbie
BACKGROUND_IMAGE: loungeroom.png
BACKGROUND_EDIT: "Afternoon, tense atmosphere"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Amelia’s face looks tight and strange.
  EXPRESSION: Angry
- CHARACTER: Narrator
  LINE: Samuel is nervous, he jigs around on the spot.
  EXPRESSION: Afraid
- CHARACTER: Narrator
  LINE: She searches his pocket, he pulls away from her. She tries the other one, pulls out a key. He’s very ashamed.
  EXPRESSION: Ashamed
- CHARACTER: Amelia
  LINE: How did you get this??
  EXPRESSION: Angry
- CHARACTER: Samuel
  LINE: I was just putting something back..
  EXPRESSION: Afraid
- CHARACTER: Amelia
  LINE: All your father’s things are down there.
  EXPRESSION: Angry
- CHARACTER: Samuel
  LINE: He’s MY father! YOU DON’T OWN HIM!
  EXPRESSION: Angry
- CHARACTER: Narrator
  LINE: A knock at the door. Amelia marches towards it, opens it.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: It’s Robbie, flowers in one hand, a present in the other.
  EXPRESSION: null
- CHARACTER: Robbie
  LINE: Just thought I’d see how you’re going. These are for you.
  EXPRESSION: Happy
- CHARACTER: Narrator
  LINE: She takes the flowers limply, not knowing what to say.
  EXPRESSION: Surprised
- CHARACTER: Robbie
  LINE: And this is for you matey. My mum always got me a model aeroplane when I was sick-
  EXPRESSION: Happy
- CHARACTER: Samuel
  LINE: I’m not sick.
  EXPRESSION: Angry
- CHARACTER: Narrator
  LINE: Uncomfortable pause. Amelia’s face burns. She’s caught out big time. A huge wave of shame builds up in her.
  EXPRESSION: Ashamed
- CHARACTER: Robbie
  LINE: Oh. I thought you were si-
  EXPRESSION: Surprised
- CHARACTER: Amelia
  LINE: No, he’s not actually. The truth is, he’s so disobedient he can’t go to school anymore.
  EXPRESSION: Angry
- CHARACTER: Samuel
  LINE: You said that’s not true!
  EXPRESSION: Angry
- CHARACTER: Amelia
  LINE: How many 6 year old boys do you know Robbie who still believe in monsters?
  EXPRESSION: Angry
- CHARACTER: Samuel
  LINE: I HATE YOU!
  EXPRESSION: Angry
- CHARACTER: Samuel
  LINE: She won’t let me have a birthday party and she WON’T let me have a DAD!
  EXPRESSION: Angry
- CHARACTER: Narrator
  LINE: Samuel bolts up the stairs. His door slams. A terribly awkward pause.
  EXPRESSION: null
- CHARACTER: Robbie
  LINE: I’m really sorry... If you want to talk about it-
  EXPRESSION: Sad
- CHARACTER: Amelia
  LINE: No, I don’t. Thanks anyway. Thanks for the presents.
  EXPRESSION: Angry
- CHARACTER: Narrator
  LINE: Robbie just stands there, looking at her, awkward.
  EXPRESSION: Sad
- CHARACTER: Amelia
  LINE: I wasn’t expecting anyone over. The house is a mess.
  EXPRESSION: Afraid
- CHARACTER: Robbie
  LINE: I don’t care-
  EXPRESSION: Sad
- CHARACTER: Amelia
  LINE: I care!
  EXPRESSION: Angry
- CHARACTER: Amelia
  LINE: Please, can you just go?
  EXPRESSION: Angry
- CHARACTER: Robbie
  LINE: I, I..
  EXPRESSION: Afraid
- CHARACTER: Amelia
  LINE: Please go!
  EXPRESSION: Angry
- CHARACTER: Narrator
  LINE: Robbie leaves, embarrassed. Amelia shuts the door, completely ashamed of herself.
  EXPRESSION: Ashamed
- CHARACTER: Narrator
  LINE: She looks up and sees the door to the basement wide open. She walks to it. Samuel has left the light on down there.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: After a time, she forces herself down those stairs.
  EXPRESSION: null

::SCENE::
LOCATION: Basement
MOOD: Chaos, remorse, fright
CHARACTERS: Amelia, Samuel (implied), Oskar (implied)
BACKGROUND_IMAGE: basement.png
BACKGROUND_EDIT: "Afternoon, chaotic, full of old items, dim lighting"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Amelia finds the crowded space in chaos. Samuel has pulled out all his father’s things, a desperate attempt to connect.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The sight of it all puts Amelia into a spin. She races around randomly stuffing things back in boxes.
  EXPRESSION: Angry
- CHARACTER: Narrator
  LINE: She clocks the photo of her and Oskar, walks over, picks it up, puts it in her pocket, unable to even look at it.
  EXPRESSION: Sad
- CHARACTER: Narrator
  LINE: She turns and what she sees makes her jump with fright.
  EXPRESSION: Surprised
- CHARACTER: Narrator
  LINE: Samuel has fixed a hat, shirt and trousers to the wall, using his father’s things to replicate a person. A pair of shoes rest under each trouser leg. Oskar’s violin is out of its case, propped up against the wall, as if the shirt arm were holding it.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Amelia’s fright subsides overtaken by a terrible remorse that hits her right in the guts. Tears well in her eyes.
  EXPRESSION: Sad

::SCENE::
LOCATION: Samuel’s Room
MOOD: Tentative, emotional, reconciliation
CHARACTERS: Amelia, Samuel
BACKGROUND_IMAGE: samuels_room.png
BACKGROUND_EDIT: "Afternoon, kid's room, quiet"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Amelia hears Samuel playing on a kid sized electric piano. It’s good, definitely music, not just noise.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: She enters the room, he stops playing immediately.
  EXPRESSION: null
- CHARACTER: Amelia
  LINE: That was really good.
  EXPRESSION: Happy
- CHARACTER: Narrator
  LINE: Samuel is mute. She walks to the bed, sits next to him.
  EXPRESSION: null
- CHARACTER: Amelia
  LINE: Your dad could play like that. He only had to hear something once.
  EXPRESSION: Sad
- CHARACTER: Samuel
  LINE: I know. You’ve told me.
  EXPRESSION: Annoyed
- CHARACTER: Amelia
  LINE: You can have your own birthday party this year if you want..
  EXPRESSION: Hopeful
- CHARACTER: Narrator
  LINE: Sam shrugs.
  EXPRESSION: Neutral
- CHARACTER: Amelia
  LINE: I’ve made some yummy soup. Real, not out of a can.
  EXPRESSION: Happy
- CHARACTER: Amelia
  LINE: And after dinner we can play Monopoly, OK?
  EXPRESSION: Happy
- CHARACTER: Narrator
  LINE: She smooths his hair gently. He doesn’t shrug her off.
  EXPRESSION: null
- CHARACTER: Amelia
  LINE: OK?
  EXPRESSION: Hopeful
- CHARACTER: Narrator
  LINE: He gives her the smallest of nods. Amelia breathes a tiny sigh of relief.
  EXPRESSION: Happy

::SCENE::
LOCATION: Kitchen
MOOD: Suspense, unnerving, fear
CHARACTERS: Amelia, Samuel
BACKGROUND_IMAGE: kitchen_night.png
BACKGROUND_EDIT: "Nighttime, dim, tense"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Sam watches his mum taste her soup. She bites down on something. It hurts. She takes it out of her mouth. It’s a shard of glass. Her tongue bleeds slightly.
  EXPRESSION: null
- CHARACTER: Amelia
  LINE: Don’t eat it.
  EXPRESSION: Surprised
- CHARACTER: Narrator
  LINE: Samuel stops. She sifts through her soup. Another shard.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: She tests his soup. No glass. She looks through hers and sees more pieces. Samuel looks panicked.
  EXPRESSION: Afraid
- CHARACTER: Amelia
  LINE: Did you put glass in my soup?
  EXPRESSION: Surprised
- CHARACTER: Samuel
  LINE: The Babadook did it mum...
  EXPRESSION: Afraid
- CHARACTER: Narrator
  LINE: He gets up. Amelia searches his face for the truth.
  EXPRESSION: null
- CHARACTER: Samuel
  LINE: The Babadook did it!
  EXPRESSION: Afraid
- CHARACTER: Amelia
  LINE: You go and watch a DVD, I’ll make something else.
  EXPRESSION: Unnerved
- CHARACTER: Narrator
  LINE: He looks like he’s about to jump out of his skin.
  EXPRESSION: Afraid
- CHARACTER: Amelia
  LINE: Just go watch a DVD Samuel.
  EXPRESSION: Angry

::SCENE::
LOCATION: Kitchen
MOOD: Suspicion, foreboding
CHARACTERS: Amelia, Samuel, Magician on TV
BACKGROUND_IMAGE: kitchen_night_tv.png
BACKGROUND_EDIT: "Nighttime, TV glowing, suspicious"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Amelia fries some sausages. The TV is loud. She goes in to have a look.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Samuel watches a magician DVD for kids, his back to her.
  EXPRESSION: null
- CHARACTER: Magician on TV
  LINE: Ladies and gentleman! Life is not always as it seems...
  EXPRESSION: Confident
- CHARACTER: Narrator
  LINE: Amelia looks at Sam’s little frame, so tiny sitting there.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Her mind is preoccupied, suspicious of her son.
  EXPRESSION: Angry

::SCENE::
LOCATION: Stairs / Amelia’s Room / Samuel’s Room
MOOD: Discovery, horror, dread
CHARACTERS: Amelia, Samuel (implied)
BACKGROUND_IMAGE: upstairs_night.png
BACKGROUND_EDIT: "Nighttime, dark stairs, bedroom, discovering something unsettling"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Stairs. Amelia trudges up the stairs. She sees the back of Samuel running into his room. He shuts the door behind him. Odd.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Amelia’s room. Amelia catches sight of something shoved under her wardrobe. She bends down to have a look.
  EXPRESSION: Surprised
- CHARACTER: Narrator
  LINE: It’s a hammer. There’s a broken glass next to it, shards of glass on the carpet. Her throat tightens.
  EXPRESSION: Afraid
- CHARACTER: Narrator
  LINE: She stands up,
  EXPRESSION: null

::SCENE::
LOCATION: Samuel's Room
MOOD: Tension, Fear, Anger
CHARACTERS: Narrator, Amelia, Samuel
BACKGROUND_IMAGE: samuels_room.png
BACKGROUND_EDIT: "Nighttime, messy room, covers pulled off bed"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Amelia notices the bed. All the covers have been pulled off and are lying on the floor. Amelia moves in, spotting a photo in the centre of the mattress.
  EXPRESSION: Concerned
- CHARACTER: Narrator
  LINE: It’s the one of her and Oskar. Oskar’s face has been scratched out with a pen. Her eyes have been drawn over with black holes, the mouth drawn into a silent scream. She strongly resembles the pictures of the Babadook.
  EXPRESSION: Horrified
- CHARACTER: Narrator
  LINE: Amelia storms in. She holds up the photo close to Samuel’s face, shaking with rage and fear.
  EXPRESSION: Furious
- CHARACTER: Amelia
  LINE: Do you think this is FUNNY!
  EXPRESSION: Angry
- CHARACTER: Narrator
  LINE: Samuel’s face drops. He runs straight for his catapult.
  EXPRESSION: Afraid
- CHARACTER: Narrator
  LINE: Amelia intercepts, trying to grab it from him. He wrenches it back off her, a genuine struggle.
  EXPRESSION: Resisting
- CHARACTER: Narrator
  LINE: She bends down to reason with him. He takes the chance to slap her hard across the face, then shoves her so forcefully she falls on her back.
  EXPRESSION: Shocked
- CHARACTER: Samuel
  LINE: DO YOU WANT TO DIE!?
  EXPRESSION: Violent
- CHARACTER: Narrator
  LINE: Amelia is speechless. She watches Sam load the catapult. For the first time, she’s genuinely scared of her son.
  EXPRESSION: Scared

::PATHS::
- CHOICE: "React to Samuel's violence"
  TARGET: kitchen_samuels_room_intercut
  STATE_CHANGE: fear = +3, anger = +2
  CONDITION: null

::SCENE::
LOCATION: Kitchen / Samuel's Room (Intercut)
MOOD: Anxiety, Dread, Apprehension
CHARACTERS: Narrator, Amelia, Bugsy, Samuel
BACKGROUND_IMAGE: kitchen_samuels_room_intercut.png
BACKGROUND_EDIT: "Night, alternating between anxious kitchen and shadowy bedroom"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Kitchen. Bugsy jumps up, trying to reach Amelia’s lap. She ignores him, scratching her head, staring into space. The lights dip in and out. It makes her anxious.
  EXPRESSION: Anxious
- CHARACTER: Narrator
  LINE: Suddenly that pain in her mouth again. She feels the offending molar, wincing as she pulls and tugs at it.
  EXPRESSION: Pain
- CHARACTER: Narrator
  LINE: Sam’s room. He sleeps sitting up with his catapult on, breathing too fast and shallow, dwarfed by his armour.
  EXPRESSION: Vigilant
- CHARACTER: Narrator
  LINE: Kitchen. Amelia scratches her scalp with her fingers, as if to relieve the pressure in her head and jaw. Bugsy tries to comfort her, but she’s in another world.
  EXPRESSION: Distressed
- CHARACTER: Narrator
  LINE: Sam’s room. He wakes suddenly. Shadows in every corner. It doesn’t feel safe. He looks at the wardrobe opposite. The doors are open.
  EXPRESSION: Afraid
- CHARACTER: Narrator
  LINE: Sam slips off the bed. Mustering all his courage, he takes small steps towards the wardrobe.
  EXPRESSION: Brave
- CHARACTER: Narrator
  LINE: Kitchen. Amelia’s fingers scrape against her scalp. The sound intensifies, the image so close it becomes surreal. Her face, her eyes in close up, full of anxiety. The sound of her scratching becomes deafening.
  EXPRESSION: Extremely Anxious
- CHARACTER: Narrator
  LINE: Samuel’s eyes and face, framed by the catapult. The dark closet yawns open, a deep terrifying hole.
  EXPRESSION: Terrified
- CHARACTER: Narrator
  LINE: He lifts his eyes and face slowly, following something we don’t see up the wall and across the ceiling.
  EXPRESSION: Terrified
- CHARACTER: Narrator
  LINE: Amelia hears a terrible crashing sound upstairs. Then Samuel screaming, as if he’s being murdered. She leaps to her feet and is up those stairs in an instant.
  EXPRESSION: Panicked

::PATHS::
- CHOICE: "Rush to Samuel"
  TARGET: samuels_room_after_crash
  STATE_CHANGE: panic = +5, concern = +3
  CONDITION: null

::SCENE::
LOCATION: Samuel’s Room
MOOD: Terror, Panic, Discovery
CHARACTERS: Narrator, Amelia, Samuel
BACKGROUND_IMAGE: samuels_room_ransacked.png
BACKGROUND_EDIT: "Moments later, room ransacked, wardrobe overturned, night"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Amelia finds the wardrobe, too heavy for Sam to pull over, lying face down on the floor. His clothes spill out underneath it. The room looks like it’s been ransacked.
  EXPRESSION: Shocked
- CHARACTER: Narrator
  LINE: Amelia can’t see Samuel. She runs to the open window, then to the bed in a panic, searches underneath.
  EXPRESSION: Panicked
- CHARACTER: Narrator
  LINE: Samuel is squashed right into a corner. He still has his catapult on. He won’t come out, clinging to the bed post. She has to really take hold and drag him out.
  EXPRESSION: Desperate
- CHARACTER: Narrator
  LINE: She’s never seen anything like it. His body is rigid in her arms, his face a picture of terror. It frightens her.
  EXPRESSION: Frightened
- CHARACTER: Samuel
  LINE: Don’t let it in! Don’t let it in! Don’t let it in!
  EXPRESSION: Terrified
- CHARACTER: Narrator
  LINE: He starts to hyperventilate. Amelia carries him to the bed and covers him with her body, trying to calm him.
  EXPRESSION: Comforting
- CHARACTER: Narrator
  LINE: Her eyes scan his pillows. Underneath one of them lies a book. She can see the spine of it. ‘MISTER BABADOOK.’
  EXPRESSION: Curious
- CHARACTER: Narrator
  LINE: Her blood runs cold.
  EXPRESSION: Terrified

::PATHS::
- CHOICE: "React to the book"
  TARGET: stairwell
  STATE_CHANGE: terror = +5, dread = +3
  CONDITION: null

::SCENE::
LOCATION: Stairwell
MOOD: Desperation, Fury
CHARACTERS: Narrator, Amelia
BACKGROUND_IMAGE: stairwell_night.png
BACKGROUND_EDIT: "Night, Amelia on the stairs"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Amelia throws the book down the stairs, pages flying.
  EXPRESSION: Furious

::PATHS::
- CHOICE: "Dispose of the book"
  TARGET: samuels_bedroom_calm
  STATE_CHANGE: frustration = +2, relief = +1
  CONDITION: null

::SCENE::
LOCATION: Samuel’s Bedroom
MOOD: Unease, Calm
CHARACTERS: Narrator, Samuel, Amelia
BACKGROUND_IMAGE: samuels_bedroom_night.png
BACKGROUND_EDIT: "Night, calm after the storm, dim lighting"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Samuel lies in a foetal position and sucks his thumb as Amelia pats his back, singing him a lullaby. Her voice trembles as she sings it. Samuel stares into space.
  EXPRESSION: Uneasy

::PATHS::
- CHOICE: "Tend to Samuel"
  TARGET: bathroom
  STATE_CHANGE: sadness = +1, exhaustion = +1
  CONDITION: null

::SCENE::
LOCATION: Bathroom
MOOD: Despair, Isolation
CHARACTERS: Narrator, Amelia
BACKGROUND_IMAGE: bathroom_night.png
BACKGROUND_EDIT: "Night, Amelia in bath, crying"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Amelia is in the bath, her knees up to her chest, crying her heart out. She takes a deep breath, trying to calm herself. It doesn’t work. She breaks out into fresh sobs, completely alone.
  EXPRESSION: Crying

::PATHS::
- CHOICE: "Confront the book again"
  TARGET: kitchen_front_yard_hallway_intercut
  STATE_CHANGE: despair = +3, determination = +1
  CONDITION: null

::SCENE::
LOCATION: Kitchen / Front Yard / Hallway (Intercut)
MOOD: Dread, Desperation, Futility
CHARACTERS: Narrator, Amelia, Samuel
BACKGROUND_IMAGE: kitchen_disposal_night.png
BACKGROUND_EDIT: "Night, Amelia destroying the book, then carrying Samuel"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Amelia takes the ‘MISTER BABADOOK’ to the table, opening it, becoming more agitated as she reads.
  EXPRESSION: Agitated
- CHARACTER: Narrator
  LINE: ‘If it’s in a word or it’s in a look, you can’t get rid of the Babadook.’ She turns the page.
  EXPRESSION: Reading
- CHARACTER: Narrator
  LINE: The image of the Babadook falling on the boy in bed. The speech bubble ‘let me in!’ from the creature’s mouth.
  EXPRESSION: Terrified
- CHARACTER: Narrator
  LINE: She slams the book shut, tries to rip it in half. It’s too thick. Determined, she rips out a page at a time, tearing each one to pieces.
  EXPRESSION: Determined
- CHARACTER: Narrator
  LINE: Amelia shoves the remnants in the Otto bin, shuts it.
  EXPRESSION: Determined
- CHARACTER: Narrator
  LINE: Amelia carries the sleeping Samuel into her room.
  EXPRESSION: Protective

::PATHS::
- CHOICE: "Try to sleep"
  TARGET: amelias_bedroom_night_day
  STATE_CHANGE: exhaustion = +2, anxiety = +1
  CONDITION: null

::SCENE::
LOCATION: Amelia’s Bedroom
MOOD: Unease, Exhaustion, Transition
CHARACTERS: Narrator, Amelia, Bugsy, Samuel
BACKGROUND_IMAGE: amelias_bedroom.png
BACKGROUND_EDIT: "Night to Day transition, messy room, lamp flickering"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Amelia watches Samuel as he sleeps. Bugsy is asleep in her arms, his front legs poking up near her face.
  EXPRESSION: Vigilant
- CHARACTER: Narrator
  LINE: The power surges, the lamp light flickers.
  EXPRESSION: Anxious
- CHARACTER: Narrator
  LINE: That sound again downstairs. Amelia’s face tightens. She listens for more, holding her breath.
  EXPRESSION: Anxious
- CHARACTER: Narrator
  LINE: Nothing. Just tight and tense silence.
  EXPRESSION: Relieved
- CHARACTER: Narrator
  LINE: Amelia moves in to Samuel, squashing Bugsy in between. She pulls the doona over her head. It covers the screen.
  EXPRESSION: Protective
- CHARACTER: Samuel
  LINE: Mum do we have to go to Ruby’s party?
  EXPRESSION: Tired
- CHARACTER: Narrator
  LINE: The doona is dragged down to reveal Amelia’s exhausted face. It’s suddenly morning. She stares at the ceiling, then makes a monumental effort to turn on her side.
  EXPRESSION: Exhausted
- CHARACTER: Narrator
  LINE: Her hand comes out from under the doona, reaches to the floor. She picks up a present amongst the clothes and books scattered there. The paper has angels all over it.
  EXPRESSION: Resigned

::PATHS::
- CHOICE: "Go to Ruby's party"
  TARGET: claires_kitchen
  STATE_CHANGE: exhaustion = +3, social_anxiety = +1
  CONDITION: null

::SCENE::
LOCATION: Claire’s Kitchen
MOOD: Awkward, Humiliation, Tension
CHARACTERS: Narrator, Amelia, Samuel, Ruby, Claire, Mother 3
BACKGROUND_IMAGE: claires_kitchen.png
BACKGROUND_EDIT: "Daytime, bright, clean kitchen, kids playing"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The present is passed to Ruby who’s waiting expectantly.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Amelia looks like she hasn’t slept in years, dark circles under her eyes. Sam sits on her lap, fragile, withdrawn. His arms around her neck. She suffers it in silence.
  EXPRESSION: Exhausted
- CHARACTER: Narrator
  LINE: The middle class mothers surround her, all perfect hair and white teeth. Beyond groomed. Kids running everywhere.
  EXPRESSION: null
- CHARACTER: Ruby
  LINE: I’ve already got this Barbie.
  EXPRESSION: Disappointed
- CHARACTER: Claire
  LINE: Well now she has a twin. They can go shopping together.
  EXPRESSION: Cheerful
- CHARACTER: Narrator
  LINE: Ruby flounces outside. The other kids follow her. Except for Samuel, who stays exactly where he is.
  EXPRESSION: Annoyed
- CHARACTER: Amelia
  LINE: Go on, off you go...
  EXPRESSION: Encouraging
- CHARACTER: Narrator
  LINE: Amelia’s aware she’s being watched by the mothers. Samuel won’t let go of her neck, burying his face in her chest.
  EXPRESSION: Embarrassed
- CHARACTER: Amelia
  LINE: He’s just tired..
  EXPRESSION: Nervously Laughing
- CHARACTER: Narrator
  LINE: She peels his arms away. Samuel frets, starting to cry. The mothers give each other surreptitious looks.
  EXPRESSION: Frustrated
- CHARACTER: Narrator
  LINE: Amelia pulls Samuel to her by both wrists.
  EXPRESSION: Determined
- CHARACTER: Amelia
  LINE: Go-and-play-right-now.
  EXPRESSION: Forceful
- CHARACTER: Narrator
  LINE: Sam leaves, half crying, half whining, looking at his mum all the way. She tries to pretend nothing’s happening.
  EXPRESSION: Upset
- CHARACTER: Narrator
  LINE: MOTHER 3 gives Claire a look. Claire rolls her eyes then looks to Amelia who is staring right at her. Claire looks away, caught out. Amelia is hurt and humiliated.
  EXPRESSION: Humiliated

::PATHS::
- CHOICE: "End of excerpt"
  TARGET: end
  STATE_CHANGE: social_anxiety = +2, humiliation = +1
  CONDITION: null

::SCENE::
LOCATION: Claire's House
MOOD: Awkward, Tense
CHARACTERS: Amelia, Claire, Mother 1, Mother 2, Mother 3, Narrator
BACKGROUND_IMAGE: claire_house_interior.png
BACKGROUND_EDIT: "Daytime, elegant living room, small social gathering"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Uncomfortable silence.
  EXPRESSION: null
- CHARACTER: Mother 1
  LINE: Claire tells me you’re a writer?
  EXPRESSION: null
- CHARACTER: Amelia
  LINE: Oh! Not so much anymore...
  EXPRESSION: Nervous
- CHARACTER: Mother 2
  LINE: What kind of writing do you do?
  EXPRESSION: null
- CHARACTER: Amelia
  LINE: I wrote articles for magazines. Some kids stuff but that was really just.. I’ve written a novel...
  EXPRESSION: Awkward
- CHARACTER: Mother 3
  LINE: Would we have read it?
  EXPRESSION: null
- CHARACTER: Amelia
  LINE: It hasn’t been published.
  EXPRESSION: Embarrassed
- CHARACTER: Mother 1
  LINE: Oh. Never mind...
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: An awkward pause. Amelia’s face flushes with humiliation.
  EXPRESSION: null
- CHARACTER: Claire
  LINE: She’s very talented, she just needs to get back into it, that’s all.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Amelia becomes very uncomfortable, the focus on her.
  EXPRESSION: null
- CHARACTER: Mother 1
  LINE: It must be very difficult. I do volunteer work with some disadvantaged women. A few of them have lost their husbands and they find it very hard.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Amelia looks at Mother 1, her face darkens.
  EXPRESSION: Angry
- CHARACTER: Claire
  LINE: How’s Richard’s merger going?
  EXPRESSION: Changing the subject
- CHARACTER: Mother 1
  LINE: Oh! Good but his workload’s ballooned.
  EXPRESSION: O.S.
- CHARACTER: Narrator
  LINE: Tight on Amelia, fighting a growing anger.
  EXPRESSION: null
- CHARACTER: Mother 1
  LINE: I’ve got the kids 24/7 it feels like.
  EXPRESSION: O.S.
- CHARACTER: Mother 2
  LINE: Tell me about it...
  EXPRESSION: O.S.
- CHARACTER: Mother 1
  LINE: I don’t even have time to go to the gym anymore, it’s ridiculous!
  EXPRESSION: O.S.
- CHARACTER: Amelia
  LINE: That’s a real tragedy.
  EXPRESSION: Blurting it out
- CHARACTER: Narrator
  LINE: The mothers all look at Amelia, taken aback. She stares at Mother 1, her contempt obvious.
  EXPRESSION: null
- CHARACTER: Amelia
  LINE: Not having time to go to the gym. How do you cope?
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Pause.
  EXPRESSION: null
- CHARACTER: Amelia
  LINE: You must have a lot to talk about with those poor disadvantaged women.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Horrible silence. Claire gives her sister a death stare. Amelia looks away, defiant, refusing to meet her gaze.
  EXPRESSION: null

::SCENE::
LOCATION: Claire's Backyard
MOOD: Playful, Tense, Confrontational, Chaotic
CHARACTERS: Amelia, Claire, Ruby, Samuel, Mother 1, Other Mothers, Kids, Narrator
BACKGROUND_IMAGE: claire_backyard_day.png
BACKGROUND_EDIT: "Daytime, large backyard, swings, tree house, clown entertaining children"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The large backyard is decked out with swings and a tree house. A clown entertains the kids with a lame trick.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Tree house. Ruby climbs up to find Sam hiding there.
  EXPRESSION: null
- CHARACTER: Ruby
  LINE: This is my tree house. I say who comes here.
  EXPRESSION: null
- CHARACTER: Samuel
  LINE: I’m not hurting anybody.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Backyard. Claire kisses the other mothers goodbye. Amelia fixes on the clown and kids.
  EXPRESSION: null
- CHARACTER: Mother 1
  LINE: You sure you don’t want us to stay?
  EXPRESSION: null
- CHARACTER: Claire
  LINE: No that’s fine. I’ll call you when they’re ready to be picked up.
  EXPRESSION: Cheek kissing
- CHARACTER: Narrator
  LINE: The women give Amelia a half hearted goodbye as they leave, she returns it, embarrassed.
  EXPRESSION: null
- CHARACTER: Amelia
  LINE: I can stay after and help you clean up.
  EXPRESSION: null
- CHARACTER: Claire
  LINE: I’ll be fine.
  EXPRESSION: Cold
- CHARACTER: Narrator
  LINE: Amelia doesn’t go. The tension builds as they sit there watching the children play in the enormous backyard.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Tree house.
  EXPRESSION: null
- CHARACTER: Samuel
  LINE: How would your Mum know if it’s real or not? She never comes to our house.
  EXPRESSION: null
- CHARACTER: Ruby
  LINE: Mum told Dad she doesn’t want to go to your house coz it’s too depressing.
  EXPRESSION: null
- CHARACTER: Samuel
  LINE: The Babadook would eat your Mum for breakfast! It’d rip her arms off!
  EXPRESSION: null
- CHARACTER: Ruby
  LINE: Shut up!
  EXPRESSION: Scared
- CHARACTER: Narrator
  LINE: Backyard. Amelia can’t stand it anymore.
  EXPRESSION: null
- CHARACTER: Amelia
  LINE: I never say anything bad to you or anyone. I say one thing and I’m an evil bitch.
  EXPRESSION: null
- CHARACTER: Claire
  LINE: You were bloody rude.
  EXPRESSION: null
- CHARACTER: Amelia
  LINE: She was so condescending! ‘I work with disadvantaged women’, give me a break!
  EXPRESSION: null
- CHARACTER: Claire
  LINE: Shereen is a huge supporter of the gallery, her husband is one of our major investors, and she’s my friend!
  EXPRESSION: null
- CHARACTER: Amelia
  LINE: Those women look down on me.
  EXPRESSION: null
- CHARACTER: Claire
  LINE: They feel for you in your situation!
  EXPRESSION: null
- CHARACTER: Amelia
  LINE: They feel sorry for me Claire! There’s a big difference!
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Tree house.
  EXPRESSION: null
- CHARACTER: Ruby
  LINE: I didn’t want you to come to my birthday party anyway. My mum made me do it.
  EXPRESSION: null
- CHARACTER: Samuel
  LINE: Well, I didn’t wanna come. It’s boring.
  EXPRESSION: null
- CHARACTER: Ruby
  LINE: No one likes you. You make up stories coz you don’t have any friends.
  EXPRESSION: null
- CHARACTER: Samuel
  LINE: I’m not making things up, you can’t see things coz you’re stupid.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Backyard.
  EXPRESSION: null
- CHARACTER: Claire
  LINE: I know what this is really all about.
  EXPRESSION: null
- CHARACTER: Amelia
  LINE: Oh? What?
  EXPRESSION: null
- CHARACTER: Claire
  LINE: As soon as anyone mentions Oskar, as soon as they even so much as hint at it, you can’t cope.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: This hits a raw nerve with Amelia, she covers it.
  EXPRESSION: null
- CHARACTER: Amelia
  LINE: That’s not true.
  EXPRESSION: null
- CHARACTER: Claire
  LINE: I know he was the love of your life. And it is God awful what happened to him. But it’ll be seven years Amelia, isn’t it time you moved on?
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Amelia struggles desperately to keep her feelings in.
  EXPRESSION: null
- CHARACTER: Amelia
  LINE: I have moved on! I don’t mention him, I don’t talk about him. What strain is it on you Claire? I listen... I listen to your life, day in day out and you don’t stop to ask me anything about mine!
  EXPRESSION: null
- CHARACTER: Claire
  LINE: I do ask! I want to know how you are!
  EXPRESSION: Defensive
- CHARACTER: Amelia
  LINE: Only if everything’s fine!
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Tree house.
  EXPRESSION: null
- CHARACTER: Ruby
  LINE: You’re not even good enough to have a dad. Everyone else has one and you don’t.
  EXPRESSION: null
- CHARACTER: Samuel
  LINE: I do have a dad.
  EXPRESSION: Getting upset
- CHARACTER: Ruby
  LINE: Your dad died so he didn’t have to be with you. And your mum doesn’t want you.
  EXPRESSION: null
- CHARACTER: Samuel
  LINE: That’s not true.
  EXPRESSION: Very close to tears
- CHARACTER: Ruby
  LINE: Is so.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Samuel stands up, his hurt turning to rage.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Backyard.
  EXPRESSION: null
- CHARACTER: Amelia
  LINE: You don’t come round to our house anymore.
  EXPRESSION: null
- CHARACTER: Claire
  LINE: And you know why that is.. I ask and you never come round-
  EXPRESSION: null
- CHARACTER: Claire
  LINE: Because I can’t stand being around your son!
  EXPRESSION: Snapping
- CHARACTER: Amelia
  LINE: I can’t believe you just said that.
  EXPRESSION: null
- CHARACTER: Claire
  LINE: You can’t stand being round him yourself!
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Tree house. Samuel lurches forward and pushes his cousin, hard.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Ruby is knocked off balance. She grabs at the air as she falls backwards right out the door.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Samuel face drops as he watches her fall.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Backyard. Claire sees her daughter fall, turn mid air and land straight on her face on the ground below. It looks awful. Both sisters rush over.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Ruby stands up, in shock, blood pouring from her mouth.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Slowly, surely, she starts to howl.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: All the kids stop playing and stare. Some get scared.
  EXPRESSION: null
- CHARACTER: Claire
  LINE: Let me have a look darling.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: She opens her mouth. A tooth has snapped off at the base.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Ruby is hysterical. Blood spurts out.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Amelia sees her son at the top of the tree house. He looks scared and guilty as he climbs down.
  EXPRESSION: null
- CHARACTER: Claire
  LINE: WHAT DID YOU DO!
  EXPRESSION: Lashing out at him
- CHARACTER: Samuel
  LINE: She said I didn’t have a dad! She kept saying it!
  EXPRESSION: Very upset, to Amelia
- CHARACTER: Ruby
  LINE: He.. He... said the Babadook was going to kill you Mummy...
  EXPRESSION: Through the sobs
- CHARACTER: Narrator
  LINE: She howls. Claire picks her up and moves swiftly into the house. Amelia follows, shame and anxiety on her face.
  EXPRESSION: null
- CHARACTER: Claire
  LINE: That bottom tooth is an adult tooth! She’s not going to get it back!
  EXPRESSION: To Amelia
- CHARACTER: Narrator
  LINE: Ruby squeals. Claire holds her tight and marches to the front door. Amelia follows her closely.
  EXPRESSION: null
- CHARACTER: Claire
  LINE: Stay here and look after the children! Do you want another one to get hurt?
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Claire’s voice upsets one of the girls, the girl cries, this sets another one off. The kids are scared.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: She charges out of the door with her squealing daughter.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Amelia turns to see a group of children in various states of distress. And in the middle is Samuel, completely lost. He rushes in to Amelia. She pushes him away. He runs to her again.
  EXPRESSION: null
- CHARACTER: Amelia
  LINE: GET AWAY FROM ME!
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Samuel stops in his tracks, shocked
  EXPRESSION: null

::SCENE::
LOCATION: Car
MOOD: Stress, Panic, Horrifying
CHARACTERS: Amelia, Samuel, Narrator
BACKGROUND_IMAGE: car_interior.png
BACKGROUND_EDIT: "Daytime, fast driving, messy car"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Amelia looks at the crying children in front of her. Her stress reaching boiling point.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Amelia drives fast, stuffing her emotions down.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: A large cockroach appears on her bare leg. She violently sweeps it away. It goes flying into the mess at her feet.
  EXPRESSION: Surprised
- CHARACTER: Samuel
  LINE: Mum.. I didn’t mean to hurt her. She wouldn’t believe me.. Mum-meee...
  EXPRESSION: Crying
- CHARACTER: Narrator
  LINE: He starts kicking the back of her seat to get her attention. Kicking over and over and over....
  EXPRESSION: Angry
- CHARACTER: Narrator
  LINE: Amelia swerves to the side of the road, screeches to a halt. She flips her seat belt off, turns around.
  EXPRESSION: Angry
- CHARACTER: Amelia
  LINE: There is no BABADOOK!
  EXPRESSION: Angry
- CHARACTER: Narrator
  LINE: Samuel’s anguish rising to fever pitch. He screams and cries, kicking the seat over and over.
  EXPRESSION: Angry
- CHARACTER: Amelia
  LINE: IT’S ALL MADE UP IN YOUR HEAD!
  EXPRESSION: Angry
- CHARACTER: Narrator
  LINE: Samuel suddenly goes quiet. He looks to his right, seeing something Amelia can’t see. He looks horrified.
  EXPRESSION: Surprised
- CHARACTER: Samuel
  LINE: Get out!
  EXPRESSION: Angry
- CHARACTER: Samuel
  LINE: Mummy..
  EXPRESSION: Scared
- CHARACTER: Amelia
  LINE: Samuel, stop it now...
  EXPRESSION: Frightened
- CHARACTER: Samuel
  LINE: GET-OUT!
  EXPRESSION: Terrified
- CHARACTER: Narrator
  LINE: He goes red in the face, as if he’s choking. Amelia watches, immobilized by shock.
  EXPRESSION: Surprised
- CHARACTER: Narrator
  LINE: A middle aged couple stop and stare, concerned.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Samuel kicks and punches, thrashing his body around. He screams out in pain. Amelia desperately tries to help.
  EXPRESSION: Pain
- CHARACTER: Narrator
  LINE: Samuel’s eyes roll back in his head, his body goes rigid, his fingers splayed. It looks absolutely horrifying.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Amelia panics. She opens her car door.
  EXPRESSION: Afraid
- CHARACTER: Amelia
  LINE: Please help! There’s something wrong with my child!
  EXPRESSION: Afraid

::PATHS::
- CHOICE: "Seek medical help"
  TARGET: doctors_surgery
  STATE_CHANGE: amelia_stress = +1, samuel_health = -1
  CONDITION: null

::SCENE::
LOCATION: Doctor’s Surgery
MOOD: Clinical, Concerned, Exhausted
CHARACTERS: Narrator, Doctor, Samuel, Amelia
BACKGROUND_IMAGE: doctors_surgery.png
BACKGROUND_EDIT: "Daytime, examination room, sterile equipment"

::SCRIPT::
- CHARACTER: Narrator
  LINE: An eye is checked by a sharp light. The pupil contracts.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: A tongue depressor is put into the child’s mouth.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: A stethoscope against Samuel’s bare chest.
  EXPRESSION: null
- CHARACTER: Doctor
  LINE: Cough now.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Samuel’s throat showing the reflex of a cough.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Samuel looks to the doctor, an overworked, middle-aged man.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Amelia sits on a chair nearby. She looks wrecked.
  EXPRESSION: Tired

::PATHS::
- CHOICE: "Discuss Samuel's condition"
  TARGET: doctors_reception
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Doctor’s Reception
MOOD: Stressed, Professional
CHARACTERS: Samuel, Receptionist, Doctor, Amelia, Narrator
BACKGROUND_IMAGE: doctors_reception.png
BACKGROUND_EDIT: "Daytime, waiting area, consultation desk"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Samuel waits on the bench, exhausted. The receptionist gives him a warm smile. He doesn’t smile back.
  EXPRESSION: null
- CHARACTER: Doctor
  LINE: I’d say it was a febrile convulsion. The brain gets overheated-
  EXPRESSION: null
- CHARACTER: Amelia
  LINE: Yes, I know what they are, I’m a nurse.
  EXPRESSION: Null
- CHARACTER: Doctor
  LINE: It always looks worse than it is.
  EXPRESSION: Null
- CHARACTER: Amelia
  LINE: I’ve never seen anything like that..
  EXPRESSION: Concerned
- CHARACTER: Doctor
  LINE: He’s obviously suffering from a high level of anxiety, very committed to the monster theory.
  EXPRESSION: Null
- CHARACTER: Amelia
  LINE: That’s an understatement..
  EXPRESSION: Null
- CHARACTER: Narrator
  LINE: The doctor stops to look at Amelia, slightly irritated.
  EXPRESSION: null
- CHARACTER: Doctor
  LINE: All children see monsters.
  EXPRESSION: Null
- CHARACTER: Amelia
  LINE: Not like this. And it’s getting worse.
  EXPRESSION: Concerned
- CHARACTER: Doctor
  LINE: He could see a psychiatrist. I have some numbers. Takes a few weeks to get in.
  EXPRESSION: Null
- CHARACTER: Amelia
  LINE: Of course he needs to see someone. But can I just get something now to make him sleep? Just until I get an appointment.
  EXPRESSION: Desperate
- CHARACTER: Narrator
  LINE: The doctor hesitates.
  EXPRESSION: null
- CHARACTER: Amelia
  LINE: Please. I haven’t slept in weeks. Neither has Samuel. When we go home tonight the whole nightmare will start up again and I’m-not-coping..
  EXPRESSION: Desperate
- CHARACTER: Narrator
  LINE: He seriously studies Amelia, sizing her up.
  EXPRESSION: null
- CHARACTER: Doctor
  LINE: I can prescribe a short course of Benzodiazepine, just till the tests come back. These are very strong for children. Most mothers aren’t too keen on them unless it’s really bad.
  EXPRESSION: Null
- CHARACTER: Amelia
  LINE: It’s really bad.
  EXPRESSION: Serious
- CHARACTER: Narrator
  LINE: He opens his pad and writes out the script.
  EXPRESSION: null
- CHARACTER: Doctor
  LINE: They can make children feel uncoordinated, foggy, maybe some temporary nausea. They’ll help him to sleep though, that’s for sure.
  EXPRESSION: Null
- CHARACTER: Narrator
  LINE: He rips out the prescription and hands it to her.
  EXPRESSION: null
- CHARACTER: Doctor
  LINE: That’s for one week. Half strength.
  EXPRESSION: Null
- CHARACTER: Narrator
  LINE: Amelia’s face relaxes a little. Problem solved for now.
  EXPRESSION: Relieved

::PATHS::
- CHOICE: "Take Samuel home with medication"
  TARGET: samuels_room_night
  STATE_CHANGE: amelia_stress = -1, samuel_anxiety = -1
  CONDITION: null

::SCENE::
LOCATION: Samuel’s Room
MOOD: Anxious, Tender, Melancholy
CHARACTERS: Amelia, Samuel, Narrator
BACKGROUND_IMAGE: samuels_room.png
BACKGROUND_EDIT: "Nighttime, child's bedroom, dim lighting"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Amelia has a glass of water and the pills at hand. Samuel sits up, worried, looking at the pills.
  EXPRESSION: null
- CHARACTER: Samuel
  LINE: Is there something wrong with me?
  EXPRESSION: Worried
- CHARACTER: Amelia
  LINE: I’m sure everything will be alright. These will help for now.
  EXPRESSION: Reassuring
- CHARACTER: Samuel
  LINE: Why don’t people like me?
  EXPRESSION: Sad
- CHARACTER: Amelia
  LINE: Why do you say that?
  EXPRESSION: Concerned
- CHARACTER: Samuel
  LINE: Ruby said people don’t like me coz I’m weird.
  EXPRESSION: Sad
- CHARACTER: Amelia
  LINE: Sometimes people say things that aren’t true.
  EXPRESSION: Reassuring
- CHARACTER: Narrator
  LINE: Samuel doesn’t look convinced.
  EXPRESSION: null
- CHARACTER: Amelia
  LINE: You just need to take your medicine, have a big sleep and not worry.
  EXPRESSION: Reassuring
- CHARACTER: Narrator
  LINE: Samuel is suddenly very anxious. He clings to Amelia. She tries not to tense up at his touch.
  EXPRESSION: Anxious
- CHARACTER: Samuel
  LINE: I don’t want you to die.
  EXPRESSION: Afraid
- CHARACTER: Amelia
  LINE: I’m not going to die for a long time yet.
  EXPRESSION: Reassuring
- CHARACTER: Samuel
  LINE: Did you think that about my dad before he died?
  EXPRESSION: Sad
- CHARACTER: Narrator
  LINE: The comment hits her. She slowly pulls him away from her.
  EXPRESSION: Sad
- CHARACTER: Amelia
  LINE: You need to take these pills so you can go to sleep.
  EXPRESSION: Firm
- CHARACTER: Amelia
  LINE: I’ve got the day off tomorrow. Maybe we can do something.
  EXPRESSION: Hopeful
- CHARACTER: Samuel
  LINE: Will these make the Babadook go away?
  EXPRESSION: Curious
- CHARACTER: Amelia
  LINE: I think so. But you have to promise you won’t mention it again.
  EXPRESSION: Firm
- CHARACTER: Narrator
  LINE: He takes the pills in hand, looks at her seriously.
  EXPRESSION: null
- CHARACTER: Samuel
  LINE: I promise to protect you if you promise to protect me. Then I won’t mention it.
  EXPRESSION: Serious
- CHARACTER: Amelia
  LINE: Of course I will.
  EXPRESSION: Reassuring
- CHARACTER: Samuel
  LINE: Sometimes people say things that aren’t true.
  EXPRESSION: Null
- CHARACTER: Narrator
  LINE: She looks him in the eyes, as sincerely as she can.
  EXPRESSION: null
- CHARACTER: Amelia
  LINE: I promise to protect you.
  EXPRESSION: Sincere
- CHARACTER: Amelia
  LINE: Come on.
  EXPRESSION: Null
- CHARACTER: Narrator
  LINE: He takes them, she gives him the water, he drinks it.
  EXPRESSION: null
- CHARACTER: Samuel
  LINE: Can you stay here with me?
  EXPRESSION: Anxious
- CHARACTER: Amelia
  LINE: Yes.
  EXPRESSION: Reassuring
- CHARACTER: Samuel
  LINE: I love you Mum.
  EXPRESSION: Loving
- CHARACTER: Amelia
  LINE: Me too.
  EXPRESSION: Tight
- CHARACTER: Narrator
  LINE: Samuel’s face drops with her response. Amelia tucks him into bed. He doesn’t look at her, infinitely sad.
  EXPRESSION: Sad
- CHARACTER: Narrator
  LINE: Amelia stands and looks at Samuel’s back, a guilty sadness crosses her face.
  EXPRESSION: Sad

::PATHS::
- CHOICE: "Go to bed"
  TARGET: amelias_room_night_morning
  STATE_CHANGE: samuel_asleep = true, amelia_guilt = +1
  CONDITION: null

::SCENE::
LOCATION: Amelia’s Room
MOOD: Exhaustion, Relief, Dreamy, Eerie
CHARACTERS: Amelia, Narrator
BACKGROUND_IMAGE: amelias_room.png
BACKGROUND_EDIT: "Night transitioning to morning, soft unearthly light"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Amelia sits on her bed, heavy with exhaustion.
  EXPRESSION: Tired
- CHARACTER: Narrator
  LINE: Her face seen from above as she falls onto the pillow in slow motion. The pillow seems miles away. A lullaby plays on violin. Her face relaxes, her eyes close.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Finally she lands on the pillow, surrendering to deep sleep.
  EXPRESSION: Peaceful
- CHARACTER: Narrator
  LINE: A soft, unearthly light plays on her face.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: After several blissful moments, the lullaby ends. Amelia opens her eyes and looks over at the clock. 11am.
  EXPRESSION: Null
- CHARACTER: Narrator
  LINE: She drifts up to sitting. It’s quiet and calm in the room and outside. She stands, her face is tranquil, dreamy.
  EXPRESSION: Tranquil

::PATHS::
- CHOICE: "Check on Samuel"
  TARGET: samuels_room_morning
  STATE_CHANGE: amelia_rested = true
  CONDITION: null

::SCENE::
LOCATION: Samuel’s Room
MOOD: Calm, Concerned
CHARACTERS: Amelia, Narrator
BACKGROUND_IMAGE: samuels_room.png
BACKGROUND_EDIT: "Morning, child's bedroom, bright but still"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Amelia sees Samuel lying on his bed with his back to her, completely still. She drifts towards him. His eyes are closed, his face perfect, like a doll’s.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: She leans in to check he’s breathing. He is.
  EXPRESSION: Concerned

::PATHS::
- CHOICE: "Proceed with the day"
  TARGET: hallway
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Hallway
MOOD: Content, Puzzled, Eerie, Rising Tension
CHARACTERS: Amelia, Narrator
BACKGROUND_IMAGE: house_hallway.png
BACKGROUND_EDIT: "Morning, quiet house, front door"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Amelia shuffles down the hallway, yawning, content.
  EXPRESSION: Content
- CHARACTER: Narrator
  LINE: Three knocks on the front door.
  EXPRESSION: Surprised
- CHARACTER: Narrator
  LINE: She covers over her dressing gown, smooths down her hair and moves to the door, opening it.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: There’s no one there. She peers out onto the street. Not a soul. It’s very quiet, strangely so. She stands there a moment, puzzled, then closes the door.
  EXPRESSION: Puzzled
- CHARACTER: Narrator
  LINE: Amelia’s almost at the end of the hall when it happens again.
  EXPRESSION: Surprised
- CHARACTER: Narrator
  LINE: Three loud, sharp knocks.
  EXPRESSION: Startled
- CHARACTER: Narrator
  LINE: She turns, strides to the front door, opens it.
  EXPRESSION: Determined
- CHARACTER: Narrator
  LINE: Sitting on the w
  EXPRESSION: null

::PATHS::
- CHOICE: "Investigate the knocking"
  TARGET: end
  STATE_CHANGE: amelia_fear = +1
  CONDITION: null

::SCENE::
LOCATION: Lounge Room
MOOD: Terrifying
CHARACTERS: Narrator, Amelia
BACKGROUND_IMAGE: lounge_room.png
BACKGROUND_EDIT: "Morning, Amelia's house, focusing on the mysterious book"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The blood drains from Amelia’s face. She bends down to pick it up. She looks on the street for any sign of life. Nothing.
  EXPRESSION: Afraid
- CHARACTER: Narrator
  LINE: Amelia runs inside with the book firmly in her grasp.
  EXPRESSION: Afraid
- CHARACTER: Narrator
  LINE: Amelia flips through the book, becoming more frightened as she goes. She finds a new page with large angry words.
  EXPRESSION: Afraid
- CHARACTER: Narrator
  LINE: ‘I’LL WAGER with YOU, I’LL MAKE you a BET. THE MORE you DENY, the STRONGER I GET.’
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: She flips the page.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The boy in the bed has been replaced by a screaming woman. She looks like Amelia. The Babadook drops down over her, the words ‘LET ME IN’ flying out of its mouth.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Amelia flips the page. The woman stands with arms outstretched. The Babadook’s shadow rises behind her.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: ‘You start to CHANGE when I get in, the BABADOOK growing right UNDER YOUR SKIN.’
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Amelia’s hands shake as she fumbles for the next page.
  EXPRESSION: Afraid
- CHARACTER: Narrator
  LINE: OH COME! COME SEE WHAT’S UNDER-NEATH!
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: She turns the page.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: A huge shadow envelops the woman as she snaps the neck of a little white dog. The dog looks exactly like Bugsy.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Amelia flips the page, not wanting but needing to see.
  EXPRESSION: Afraid
- CHARACTER: Narrator
  LINE: The woman strangles a boy with her bare hands. The shadow holds her arms, forcing her to it. Amelia flips the page.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: An image of the woman, her mouth open in a terrible scream. She slits her throat, blood spurts everywhere.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Amelia turns to the final page. Just text that says ‘IF IT’S IN A WORD, OR IT’S IN A LOOK, YOU CAN’T GET RID OF THE BABADOOK.’
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue"
  TARGET: backyard_morning
  STATE_CHANGE: fear = +3
  CONDITION: null

::SCENE::
LOCATION: Backyard
MOOD: Desperate
CHARACTERS: Narrator, Amelia, Samuel
BACKGROUND_IMAGE: backyard.png
BACKGROUND_EDIT: "Morning, barbecue, burning book, Samuel at door"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Petrol splashes out of a can.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: A pair of hands throw a lit match into the barbecue where the ripped up book now lies. It ignites quickly.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Amelia stands back as the flames rise, watching it burn.
  EXPRESSION: Relieved
- CHARACTER: Narrator
  LINE: She sees Samuel at the back door, trying to wake up. She shoots him a tense smile. He looks concerned.
  EXPRESSION: Tense

::PATHS::
- CHOICE: "Continue"
  TARGET: amelia_hallway_morning
  STATE_CHANGE: babadook_book_destroyed = true
  CONDITION: null

::SCENE::
LOCATION: Amelia's Hallway (Claire's House)
MOOD: Anxious
CHARACTERS: Narrator, Amelia, Claire
BACKGROUND_IMAGE: amelia_hallway.png
BACKGROUND_EDIT: "Morning, Amelia on phone, tense atmosphere"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Amelia is on the phone to Claire.
  EXPRESSION: null
- CHARACTER: Claire
  LINE: She has to have a root canal and a crown.
  EXPRESSION: Neutral
- CHARACTER: Amelia
  LINE: I’ll pay for everything.
  EXPRESSION: Determined
- CHARACTER: Claire
  LINE: You can’t even pay for your own dental work, how are you going to do that?
  EXPRESSION: Skeptical
- CHARACTER: Narrator
  LINE: Amelia doesn’t know what to say.
  EXPRESSION: Embarrassed
- CHARACTER: Claire
  LINE: I really have to go now..
  EXPRESSION: Impatient
- CHARACTER: Amelia
  LINE: Claire, I think someone is stalking me and Samuel.
  EXPRESSION: Afraid
- CHARACTER: Claire
  LINE: What?
  EXPRESSION: Surprised
- CHARACTER: Amelia
  LINE: A book turned up at our house.
  EXPRESSION: Afraid
- CHARACTER: Claire
  LINE: What are you talking about?
  EXPRESSION: Confused
- CHARACTER: Amelia
  LINE: I threw it away. But someone glued it back together and put it on our doorstep.
  EXPRESSION: Afraid
- CHARACTER: Claire
  LINE: A book? Amelia I can’t help you now-
  EXPRESSION: Dismissive
- CHARACTER: Amelia
  LINE: I don’t expect you to help, I just-
  EXPRESSION: Frustrated
- CHARACTER: Claire
  LINE: If you’re worried you should go to the police. I’ve got to go.
  EXPRESSION: Dismissive
- CHARACTER: Narrator
  LINE: (Hangs up.)
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Amelia puts down the phone, crushed. She stares at her hands, black from the smoke. Silence.
  EXPRESSION: Sad
- CHARACTER: Narrator
  LINE: The phone rings sharply, giving her a fright.
  EXPRESSION: Startled
- CHARACTER: Amelia
  LINE: Claire?
  EXPRESSION: Hopeful
- CHARACTER: Narrator
  LINE: There is a silence on the other end.
  EXPRESSION: null
- CHARACTER: Amelia
  LINE: Hello?
  EXPRESSION: Tense
- CHARACTER: Narrator
  LINE: Finally, a noise on the other end, but not a human one.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: ‘Babababababa dook-dook-dook’
  EXPRESSION: Eerie
- CHARACTER: Narrator
  LINE: The sound rips through Amelia. She slams down the phone.
  EXPRESSION: Terrified

::PATHS::
- CHOICE: "Continue"
  TARGET: mrs_roach_house_day
  STATE_CHANGE: fear = +2, isolation = +1
  CONDITION: null

::SCENE::
LOCATION: Outside Mrs Roach's House
MOOD: Vulnerable
CHARACTERS: Narrator, Amelia, Samuel, Mrs Roach
BACKGROUND_IMAGE: mrs_roach_house.png
BACKGROUND_EDIT: "Daytime, house exterior, Amelia and Samuel on doorstep"

::SCRIPT::
- CHARACTER: Narrator
  LINE: A door opens. Amelia waits there, a vulnerable smile. Samuel is beside her, sitting on the doorstep.
  EXPRESSION: Vulnerable
- CHARACTER: Mrs Roach
  LINE: Hello love.
  EXPRESSION: Friendly
- CHARACTER: Amelia
  LINE: Hi Gracie.
  EXPRESSION: Friendly
- CHARACTER: Amelia
  LINE: Up you get Sam.
  EXPRESSION: Gentle
- CHARACTER: Mrs Roach
  LINE: Oh he’s alright. You tired little one?
  EXPRESSION: Concerned
- CHARACTER: Samuel
  LINE: I’m exhausted Mrs Roach. I’m on drugs.
  EXPRESSION: Frank
- CHARACTER: Amelia
  LINE: He had a fit yesterday. He’s alright, but we’ve had to medicate him.
  EXPRESSION: Explaining
- CHARACTER: Mrs Roach
  LINE: Oh, you poor little thing...
  EXPRESSION: Sympathetic
- CHARACTER: Amelia
  LINE: Gracie would I be able to leave Samuel with you for an hour or so? I’ve got to do something and he can’t come along.
  EXPRESSION: Asking
- CHARACTER: Mrs Roach
  LINE: Yes of course. Are you alright?
  EXPRESSION: Concerned
- CHARACTER: Amelia
  LINE: I’m fine. I normally wouldn’t ask you to look after him-
  EXPRESSION: Upbeat
- CHARACTER: Mrs Roach
  LINE: That’s no problem.
  EXPRESSION: Genuine
- CHARACTER: Narrator
  LINE: Mrs Roach reaches out taking Amelia’s hand.
  EXPRESSION: null
- CHARACTER: Mrs Roach
  LINE: It’s not a crime to ask for help love.
  EXPRESSION: Supportive
- CHARACTER: Narrator
  LINE: Amelia tries with all her might not to cry.
  EXPRESSION: Emotional

::PATHS::
- CHOICE: "Continue"
  TARGET: police_station_day
  STATE_CHANGE: samuel_safe = true
  CONDITION: null

::SCENE::
LOCATION: Police Station
MOOD: Frustrating
CHARACTERS: Narrator, Amelia, Sergeant, Teenage Cops
BACKGROUND_IMAGE: police_station.png
BACKGROUND_EDIT: "Daytime, police station interior, bored officers"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Amelia enters, intimidated by the surroundings.
  EXPRESSION: Intimidated
- CHARACTER: Narrator
  LINE: There are three policemen on duty, one older sergeant at the front desk, and two in the back who don’t look old enough to be working. They all look bored.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Amelia shuffles up to the counter.
  EXPRESSION: Hesitant
- CHARACTER: Amelia
  LINE: Hi. I want to report someone stalking me and my child.
  EXPRESSION: Serious
- CHARACTER: Sergeant
  LINE: When did the incident occur Madam?
  EXPRESSION: Professional
- CHARACTER: Amelia
  LINE: It started this week.
  EXPRESSION: Neutral
- CHARACTER: Sergeant
  LINE: Can you tell us what happened?
  EXPRESSION: Professional
- CHARACTER: Amelia
  LINE: Someone sent me a.. a children’s book.
  EXPRESSION: Hesitant
- CHARACTER: Narrator
  LINE: The teenage cops stifle a laugh. Amelia sees it. The Sergeant gives them a quick, stern look.
  EXPRESSION: null
- CHARACTER: Sergeant
  LINE: And?
  EXPRESSION: Impatient
- CHARACTER: Amelia
  LINE: And it contained violent and graphic images of my child and me being murdered.
  EXPRESSION: Angry
- CHARACTER: Narrator
  LINE: The two in the back instantly stop smiling.
  EXPRESSION: null
- CHARACTER: Sergeant
  LINE: Can we have a look at the book please?
  EXPRESSION: Professional
- CHARACTER: Amelia
  LINE: I burnt it.
  EXPRESSION: Sheepish
- CHARACTER: Sergeant
  LINE: You burnt it.
  EXPRESSION: Deflated
- CHARACTER: Amelia
  LINE: Yes.
  EXPRESSION: Defiant
- CHARACTER: Sergeant
  LINE: Well, unfortunately there’s nothing we can do about it.
  EXPRESSION: Dismissive
- CHARACTER: Amelia
  LINE: He’s making phone calls to me as well.
  EXPRESSION: Desperate
- CHARACTER: Sergeant
  LINE: What’s he saying?
  EXPRESSION: Neutral
- CHARACTER: Amelia
  LINE: Nothing, he’s just making noises.
  EXPRESSION: Frustrated
- CHARACTER: Sergeant
  LINE: How do you know it’s the same person?
  EXPRESSION: Skeptical
- CHARACTER: Amelia
  LINE: Because of what he wrote in the book!
  EXPRESSION: Frustrated
- CHARACTER: Sergeant
  LINE: The book you burnt.
  EXPRESSION: Sarcastic
- CHARACTER: Amelia
  LINE: Yes.....
  EXPRESSION: Defeated
- CHARACTER: Narrator
  LINE: She looks past the policemen in the back and sees a coat rack. On the rack hangs a long black coat. Perched right on top of the coat is an old fashioned black top hat. Just like the coat and hat in the book.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Amelia looks suddenly frightened. The Sergeant notes it. He looks at her hands on the counter, black from the fire.
  EXPRESSION: Terrified
- CHARACTER: Narrator
  LINE: Amelia retracts them, trying to remain composed.
  EXPRESSION: Composed
- CHARACTER: Narrator
  LINE: She straightens her hair, the hair she didn’t brush this morning. The Sergeant doesn’t take his eyes from her.
  EXPRESSION: Self-conscious
- CHARACTER: Sergeant
  LINE: Are you having a hard time at the moment, love?
  EXPRESSION: Concerned
- CHARACTER: Narrator
  LINE: She looks to the hat and coat, then back to the Sergeant, trying to concentrate.
  EXPRESSION: Distracted
- CHARACTER: Amelia
  LINE: OK, thanks, don’t worry about it.
  EXPRESSION: Dismissive
- CHARACTER: Narrator
  LINE: She almost runs out.
  EXPRESSION: Panicked

::PATHS::
- CHOICE: "Continue"
  TARGET: mrs_roach_house_afternoon
  STATE_CHANGE: fear = +3, frustration = +2
  CONDITION: null

::SCENE::
LOCATION: Outside Mrs Roach's House
MOOD: Tense
CHARACTERS: Narrator, Samuel, Mrs Roach, Amelia
BACKGROUND_IMAGE: mrs_roach_house.png
BACKGROUND_EDIT: "Afternoon, Samuel walking to Amelia, tense discussion"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Samuel trudges towards his mum coming down the path.
  EXPRESSION: Tired
- CHARACTER: Mrs Roach
  LINE: Did you get your things done?
  EXPRESSION: Neutral
- CHARACTER: Narrator
  LINE: Amelia nods, trying to appear relaxed.
  EXPRESSION: Tense
- CHARACTER: Samuel
  LINE: Mrs Roach has Parkingsuns, that’s why she shakes all the time like she’s dancing.
  EXPRESSION: Observant
- CHARACTER: Amelia
  LINE: Samuel-
  EXPRESSION: Interrupting
- CHARACTER: Samuel
  LINE: It might get worse but it won’t get better-
  EXPRESSION: Frank
- CHARACTER: Amelia
  LINE: You don’t have to say everything that comes into your head!
  EXPRESSION: Frustrated
- CHARACTER: Mrs Roach
  LINE: It’s alright love. He wanted to know, so we talked about it.
  EXPRESSION: Calm
- CHARACTER: Narrator
  LINE: Amelia checks herself. Samuel trudges back home, tired.
  EXPRESSION: Regretful
- CHARACTER: Mrs Roach
  LINE: He sees things as they are, that one. His dad was the same, always spoke his mind.
  EXPRESSION: Reflective
- CHARACTER: Amelia
  LINE: I’d rather not talk about his dad. It’s been seven years!
  EXPRESSION: Angry
- CHARACTER: Narrator
  LINE: She walks off without a
  EXPRESSION: Angry

::PATHS::
- CHOICE: "End scene"
  TARGET: end
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Lounge Room - Kitchen - Hallway
MOOD: Overwhelmed, Disgusted, Anxious, Suspicious
CHARACTERS: Amelia, Samuel, Bugsy, Welfare Man, Welfare Woman
BACKGROUND_IMAGE: lounge_kitchen_hallway_day.png
BACKGROUND_EDIT: "Daytime, messy house, cockroaches, later dishevelled Amelia, strangers at the door"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Amelia passes Samuel lying on the couch, already half asleep. Her tooth is giving her a massive migraine.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Bugsy is in the kitchen, barking nonstop. She tries to move closer to him, he runs straight past her outside.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: It looks like a bomb’s gone off. Food in the sink, mess everywhere. She pauses for a moment, overwhelmed.
  EXPRESSION: Overwhelmed
- CHARACTER: Narrator
  LINE: Something tickles her arm. It’s a cockroach. She jumps, flicking it off in disgust. It falls to the floor.
  EXPRESSION: Disgusted
- CHARACTER: Narrator
  LINE: She notices another one on the floor nearby. Then another. About six or seven of the bastards. They seem to be coming from behind the fridge.
  EXPRESSION: Concerned
- CHARACTER: Narrator
  LINE: Amelia pulls the fridge out from the wall. The wallpaper is torn in one place. A cockroach pops out of it. It disgusts her. She starts to peel back the paper.
  EXPRESSION: Disgusted
- CHARACTER: Narrator
  LINE: A hole in the wall. It’s filled with cockroaches. They crawl out, some dropping at her feet. She has to stop from vomiting as she runs for a broom.
  EXPRESSION: Disgusted
- CHARACTER: Narrator
  LINE: Samuel appears at the door.
  EXPRESSION: null
- CHARACTER: Amelia
  LINE: Don’t come in here!
  EXPRESSION: Angry
- CHARACTER: Narrator
  LINE: Later. The contents of the fridge have been turfed out onto the benches. It looks even messier than before.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Amelia has an old dress on and large rubber gloves. She looks completely dishevelled, manically cleaning.
  EXPRESSION: Maniacal
- CHARACTER: Narrator
  LINE: Suddenly, three knocks at the door. Amelia freezes.
  EXPRESSION: Surprised
- CHARACTER: Narrator
  LINE: A pause. The three knocks come again.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: She creeps past a sleeping Samuel on the couch, towards the front door, her broom as a weapon.
  EXPRESSION: Stealthy
- CHARACTER: Narrator
  LINE: Amelia looks through the peephole.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Two strangers at the door, a man and a woman.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Amelia opens the door.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The people look Amelia up and down. The old dress, the gloves, her dishevelled hair.
  EXPRESSION: Disapproving
- CHARACTER: Amelia
  LINE: I don’t want to buy anything.
  EXPRESSION: Terse
- CHARACTER: Welfare Man
  LINE: Are you Amelia Vanek?
  EXPRESSION: Inquisitive
- CHARACTER: Amelia
  LINE: Yes.
  EXPRESSION: Nervous
- CHARACTER: Welfare Man
  LINE: I’m Warren Newton and this is Prue Flannery from the Department of Community Services. The Babbage Bay Primary School has asked us to stop in and say hello.
  EXPRESSION: Formal
- CHARACTER: Amelia
  LINE: My son has only been away two days.
  EXPRESSION: Defensive
- CHARACTER: Welfare Man
  LINE: He’s not actually registered at Babbage Bay anymore. If I could just come in, meet Samuel and get you to look at these papers, that’d be terrific.
  EXPRESSION: Calm
- CHARACTER: Narrator
  LINE: Amelia manages to give them a feeble smile.
  EXPRESSION: Nervous
- CHARACTER: Narrator
  LINE: Lounge room. The welfare pair scrutinize their surrounds, both noticing the smashed window, now patched up with plastic and duct tape.
  EXPRESSION: Scrutinizing
- CHARACTER: Narrator
  LINE: Amelia is suddenly very self conscious.
  EXPRESSION: Self-conscious
- CHARACTER: Narrator
  LINE: Bugsy comes out, barking loudly. Samuel wakes up, groggy.
  EXPRESSION: null
- CHARACTER: Amelia
  LINE: Bugsy! Sshh! That’s enough.
  EXPRESSION: Frustrated
- CHARACTER: Narrator
  LINE: Bugsy runs away when Amelia tries to pick him up.
  EXPRESSION: null
- CHARACTER: Welfare Woman
  LINE: Hello Samuel. I’m Prue and this is Warren.
  EXPRESSION: Friendly
- CHARACTER: Narrator
  LINE: Samuel sits up. She puts out her hand, he shakes it.
  EXPRESSION: null
- CHARACTER: Samuel
  LINE: Hello.
  EXPRESSION: Neutral
- CHARACTER: Welfare Woman
  LINE: How are you?
  EXPRESSION: Concerned
- CHARACTER: Samuel
  LINE: I’m a bit tired from the drugs Mum gave me.
  EXPRESSION: Tired
- CHARACTER: Narrator
  LINE: They both look to Amelia with concern.
  EXPRESSION: Concerned
- CHARACTER: Amelia
  LINE: Not ‘drugs’, tranquillizers.
  EXPRESSION: Defensive
- CHARACTER: Narrator
  LINE: Their concern grows.
  EXPRESSION: Concerned
- CHARACTER: Amelia
  LINE: From the doctor. He had a fit yesterday.
  EXPRESSION: Quick, Defensive
- CHARACTER: Narrator
  LINE: Bugsy barks, Amelia tries to grab him, he runs outside.
  EXPRESSION: null
- CHARACTER: Samuel
  LINE: I feel really tired akshally.
  EXPRESSION: Tired
- CHARACTER: Welfare Woman
  LINE: That’s no good.
  EXPRESSION: Concerned
- CHARACTER: Narrator
  LINE: The welfare woman throws Amelia a disapproving glance. She looks into the kitchen chaos.
  EXPRESSION: Disapproving
- CHARACTER: Welfare Woman
  LINE: May I have a glass of water?
  EXPRESSION: Polite
- CHARACTER: Amelia
  LINE: Yes, of course. I’ll just get you one.
  EXPRESSION: Eager
- CHARACTER: Narrator
  LINE: Amelia darts into the kitchen. The welfare people follow.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: They notice a mound of wallpaper on the floor.
  EXPRESSION: Observant
- CHARACTER: Amelia
  LINE: It’s a real mess, I know. I’ve just found a cockroach infestation. I normally keep the house sprayed, I DID spray it already actually! There’s a big hole in the wall behind the fridge, that’s why I..
  EXPRESSION: Nervous, Explaining
- CHARACTER: Narrator
  LINE: Amelia shows them to the area behind the fridge.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: There’s no hole in the wall, just a mound of wallpaper at their feet. No cockroaches. Amelia is gob smacked.
  EXPRESSION: Shocked
- CHARACTER: Narrator
  LINE: The two welfare people sneak a look at each other.
  EXPRESSION: Skeptical
- CHARACTER: Amelia
  LINE: I didn’t mean a hole in the wall, there was a hole in the wall paper. They were laying their eggs in there, I think.
  EXPRESSION: Nervous, Explaining
- CHARACTER: Narrator
  LINE: She smiles, very nervous. They smile back, politely.
  EXPRESSION: Nervous
- CHARACTER: Welfare Man
  LINE: We’ve caught you at a bad time. I’ll leave some information for you to read over, we can come back in a week to talk through your options. Here’s my card.
  EXPRESSION: Polite, Firm
- CHARACTER: Samuel
  LINE: Mum.
  EXPRESSION: Distressed
- CHARACTER: Narrator
  LINE: All three adults look to Samuel.
  EXPRESSION: Concerned
- CHARACTER: Samuel
  LINE: I think I’m gonna vomit.
  EXPRESSION: Sick

::PATHS::
- CHOICE: "Continue to late afternoon"
  TARGET: outside_house_lounge_late_afternoon
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Outside House - Lounge Room
MOOD: Resigned, Weary
CHARACTERS: Amelia, Samuel
BACKGROUND_IMAGE: outside_house_lounge_late_afternoon.png
BACKGROUND_EDIT: "Late afternoon, outside house, lounge room getting dark"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Outside. Amelia stuffs all the wallpaper in the bin.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Lounge room, soon after. Samuel is once again fast asleep on the couch. It’s just starting to get dark.
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue to evening"
  TARGET: kitchen_lounge_evening
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Kitchen - Lounge Room
MOOD: Calm, then Eerie, Dread, Anxious
CHARACTERS: Amelia, Mrs Roach, Samuel, The Babadook
BACKGROUND_IMAGE: kitchen_lounge_evening.png
BACKGROUND_EDIT: "Evening, kitchen, lounge room, Babadook in shadows"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Amelia is washing dishes. She can see Mrs Roach watching TV in her lounge room. She smiles, comforted by the familiar sight. Time stretches.
  EXPRESSION: Comforted
- CHARACTER: Narrator
  LINE: She looks into the soapy water. The splashing sound, the warmth calms her. She pulls out a plate, looks up again.
  EXPRESSION: Calm
- CHARACTER: Narrator
  LINE: Standing in the shadows, behind Mrs Roach, is the half visible form of the Babadook. The black shadowy coat, the tall top hat, the long black gloves can just be seen.
  EXPRESSION: Eerie
- CHARACTER: Narrator
  LINE: It appears to be looking right at her.
  EXPRESSION: Threatening
- CHARACTER: Narrator
  LINE: Amelia drops the plate into the sink.
  EXPRESSION: Startled
- CHARACTER: Samuel
  LINE: Mum.
  EXPRESSION: Calling out
- CHARACTER: Narrator
  LINE: Amelia starts and looks at Samuel at the kitchen door.
  EXPRESSION: Startled
- CHARACTER: Samuel
  LINE: I’m gonna go to bed.
  EXPRESSION: Exhausted
- CHARACTER: Amelia
  LINE: Ah... It’s only 6 o'clock. Don’t you want to stay up with your Mum for a while?
  EXPRESSION: Persuading
- CHARACTER: Samuel
  LINE: No..
  EXPRESSION: Resigned
- CHARACTER: Narrator
  LINE: He turns and leaves. Amelia looks back out the window. No Babadook. Just Mrs Roach sitting with a cup of tea.
  EXPRESSION: Relieved
- CHARACTER: Narrator
  LINE: She turns and follows Sam into the lounge, on edge.
  EXPRESSION: Anxious
- CHARACTER: Amelia
  LINE: If you go to bed now, the pills won’t work properly. You have to stay up for a while sweetheart.
  EXPRESSION: Desperate
- CHARACTER: Narrator
  LINE: Samuel sighs. He drags himself onto the couch again.
  EXPRESSION: Resigned

::PATHS::
- CHOICE: "Continue to lounge room"
  TARGET: lounge_room_evening
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Lounge Room
MOOD: Frustration, Weariness
CHARACTERS: Amelia, Samuel
BACKGROUND_IMAGE: lounge_room_evening.png
BACKGROUND_EDIT: "Evening, Samuel doing magic, Amelia encouraging"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Samuel finishes off a magic trick, his heart’s not in it.
  EXPRESSION: null
- CHARACTER: Amelia
  LINE: What about another one?
  EXPRESSION: Encouraging
- CHARACTER: Samuel
  LINE: No Mum!
  EXPRESSION: Cranky

::PATHS::
- CHOICE: "Continue through the night"
  TARGET: lounge_bathroom_bedroom_night
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Lounge Room - Bathroom - Amelia’s Bedroom
MOOD: Weariness, Unease, Dread
CHARACTERS: Amelia, Samuel
BACKGROUND_IMAGE: various_rooms_night.png
BACKGROUND_EDIT: "Nighttime, Samuel asleep on couch, in bath, Amelia reading, lights flickering"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Samuel is on the couch half asleep, watching a video.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Amelia stares at the screen but doesn’t take it in.
  EXPRESSION: Distracted
- CHARACTER: Narrator
  LINE: She looks into the mess of the kitchen, fear on her face. She turns up the volume on the TV, Samuel stirs.
  EXPRESSION: Fearful
- CHARACTER: Narrator
  LINE: Bathroom. Samuel is almost asleep in the bath. Amelia washes his back vigorously.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Bedroom. Amelia reads. Sam barely has his eyes open.
  EXPRESSION: null
- CHARACTER: Amelia
  LINE: ...and lived happily in a beautiful palace for the rest of their days.’ THE END.
  EXPRESSION: Reading
- CHARACTER: Narrator
  LINE: Samuel is asleep. Amelia stares at the end of her bed, the light of the lamp bleeding into the darkness beyond.
  EXPRESSION: Anxious
- CHARACTER: Narrator
  LINE: The lights flicker. The bedside light buzzes softly, then gets louder. Amelia flicks her arm out and turns it off.
  EXPRESSION: Startled

::PATHS::
- CHOICE: "Continue to later in bedroom"
  TARGET: amelia_bedroom_later
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Amelia’s Bedroom
MOOD: Restless, Anxious
CHARACTERS: Amelia, Samuel
BACKGROUND_IMAGE: amelia_bedroom_night.png
BACKGROUND_EDIT: "Later night, Amelia wide awake, Samuel asleep"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Amelia lies wide awake in bed on her side. Samuel is out to it. She turns over, restless, staring at the ceiling.
  EXPRESSION: Restless

::PATHS::
- CHOICE: "End of excerpt"
  TARGET: end
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Amelia's Room
MOOD: Terrified
CHARACTERS: Amelia, Bugsy, Samuel
BACKGROUND_IMAGE: amelia_room_night.png
BACKGROUND_EDIT: "Dark bedroom, tense atmosphere, slightly open door"

::SCRIPT::
- CHARACTER: Narrator
  LINE: That sound downstairs again. Only this time, it comes up the stairs and stops outside her door.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Amelia freezes.
  EXPRESSION: Afraid
- CHARACTER: Narrator
  LINE: A slight scratching sound at the door. She starts to panic, the scratching gets louder.
  EXPRESSION: Afraid
- CHARACTER: Narrator
  LINE: She hears a whimpering. It’s the dog.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: She springs out of bed and opens the door, relieved.
  EXPRESSION: Happy
- CHARACTER: Narrator
  LINE: Bugsy runs in, jumps straight up on the bed, finds a spot near Samuel and settles. Amelia jumps under the covers.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Silence. Darkness. Amelia’s eyes flicking, nervous.
  EXPRESSION: Afraid
- CHARACTER: Narrator
  LINE: The scratching starts up again, only this time it can’t be the dog. Amelia stares at the door unable to move.
  EXPRESSION: Afraid
- CHARACTER: Narrator
  LINE: The door clicks and moves open by itself. Amelia watches, her heart in her throat. The rustling, scratching sound moves inside the room. Amelia slips the covers over her head, terrified. She can’t see anything now.
  EXPRESSION: Terrified
- CHARACTER: Narrator
  LINE: The sound appears to be moving closer.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: After an age, Amelia pulls down the duvet, unable to stand it anymore. She peers into the terrible darkness.
  EXPRESSION: Afraid
- CHARACTER: Narrator
  LINE: Something large and black lurks in one corner on the ceiling. She can’t make out what it is. Time stops.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The shadow scuttles quickly across the ceiling. It stops right above her head. Amelia is paralyzed by fear. She hears a rasping sound. The thing appears to be breathing.
  EXPRESSION: Terrified
- CHARACTER: Narrator
  LINE: Her hand reaches for the bedside lamp. Her eyes are fixed on the dreaded shadow right above her head.
  EXPRESSION: Afraid
- CHARACTER: Narrator
  LINE: Before she can get there, the thing drops down right on top of her. She sees its hideous, mask like face millimetres from her own; the black eyes, the mouth wrenched open in a permanent, silent scream. She takes a huge breath, as if breathing the thing in, terrorized.
  EXPRESSION: Terrified
- CHARACTER: Narrator
  LINE: Amelia switches on the lamp, springs out of bed and turns on the overhead light. Bugsy barks. Samuel wakes.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: There’s nothing there. Samuel sits up, trying to focus.
  EXPRESSION: Confused
- CHARACTER: Amelia
  LINE: We’re going downstairs.
  EXPRESSION: Afraid
- CHARACTER: Samuel
  LINE: Why?
  EXPRESSION: Confused
- CHARACTER: Amelia
  LINE: Because we are!
  EXPRESSION: Angry

::PATHS::
- CHOICE: "Go downstairs"
  TARGET: lounge_room_night
  STATE_CHANGE: fear = +1
  CONDITION: null

::SCENE::
LOCATION: Lounge Room
MOOD: Exhaustion
CHARACTERS: Amelia, Samuel, Bugsy
BACKGROUND_IMAGE: lounge_room_morning.png
BACKGROUND_EDIT: "Lounge room, all lights on, TV playing, transitioning from night to morning"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Amelia turns every lounge light on. She moves to the kitchen, turns the lights on there. Samuel watches, groggy. Bugsy follows Amelia, barking continuously.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Later. All the lights still on. The TV is up loud.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Amelia tries desperately to stay awake, absently hitting the remote. Commercials, nature program, soap opera.
  EXPRESSION: Tired
- CHARACTER: Narrator
  LINE: An old black and white George Méliès clip appears on the screen. Beautiful silent images, childlike but slightly disturbing. Just like the Babadook book. A weird tinkling lullaby accompanies them, seducing her to sleep.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: She fights it, her head nodding forward and back, a drowsy agitation, desperate to stay awake.
  EXPRESSION: Tired
- CHARACTER: Narrator
  LINE: The Méliès images stream in front of her. People dismembered, heads growing larger and smaller, old style cinema tricks. Strange and sinister.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Emotions pass over Amelia’s face as she watches, agitation, amusement, exhaustion, fear. Something is brewing. She jerks forward and back, her eyes heavy.
  EXPRESSION: Tired
- CHARACTER: Narrator
  LINE: Her face speeds up. It looks bizarre. The tinkly piano music continues to play. And still she doesn’t sleep.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Amelia’s face returns to normal speed, she looks around.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The sun is coming through the windows. It’s already morning.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: She leans over. Something doesn’t feel right.
  EXPRESSION: Confused
- CHARACTER: Narrator
  LINE: She looks to Samuel asleep on the couch, his back to her.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Bugsy peers over Samuel, studying Amelia with caution.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: She returns the dog’s stare, unblinking. There’s an eery silence in the room. She looks at the TV. It’s on mute.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Amelia suddenly lurches forward and manages to stand. She centres herself momentarily, then shuffles to the stairs.
  EXPRESSION: Tired

::PATHS::
- CHOICE: "Go to Amelia's room"
  TARGET: amelia_room_morning
  STATE_CHANGE: exhaustion = +1
  CONDITION: null

::SCENE::
LOCATION: Amelia's Room
MOOD: Anger
CHARACTERS: Amelia, Samuel (O.S.), Beverly (O.S.)
BACKGROUND_IMAGE: amelia_room_morning.png
BACKGROUND_EDIT: "Bedroom, morning light, unkempt bed, Amelia looking tired and agitated"

::SCRIPT::
- CHARACTER: Amelia
  LINE: Hi Beverly, it’s Amelia.
  EXPRESSION: Tired
- CHARACTER: Narrator
  LINE: Amelia looks exhausted and strange.
  EXPRESSION: Tired
- CHARACTER: Amelia
  LINE: I can’t come in today, I think I’ve caught what my son had... I don’t want to give it to anyone at work... Alright, give all my shifts to someone else, that’s just what I need... I can’t help it if I’m sick, what do you expect me to do?... You do that!
  EXPRESSION: Angry
- CHARACTER: Narrator
  LINE: She throws the phone on the bedside table, sits down heavily on the bed, her head in her hands.
  EXPRESSION: Angry
- CHARACTER: Narrator
  LINE: She lies on her side, pulls up the covers, stares at the wall, her eyes zombie like. They eventually close.
  EXPRESSION: Tired
- CHARACTER: Narrator
  LINE: Silence. And finally, sleep.
  EXPRESSION: null
- CHARACTER: Samuel
  LINE: Mum....
  EXPRESSION: Calling
- CHARACTER: Narrator
  LINE: Amelia’s eyes spring open. She doesn’t respond.
  EXPRESSION: Tired
- CHARACTER: Samuel
  LINE: I took my pills, but now I feel sick again. I need to eat something..
  EXPRESSION: Sick
- CHARACTER: Narrator
  LINE: Amelia’s eyes fill with resentment. She closes them.
  EXPRESSION: Angry
- CHARACTER: Samuel
  LINE: I couldn’t find any food in the fridge.
  EXPRESSION: Complaining
- CHARACTER: Narrator
  LINE: Her eyes snap open, staring, cold.
  EXPRESSION: Angry
- CHARACTER: Samuel
  LINE: You said to have them with food.
  EXPRESSION: Complaining
- CHARACTER: Narrator
  LINE: Amelia’s face hardens, a buried fury surfacing.
  EXPRESSION: Angry
- CHARACTER: Samuel
  LINE: I’m really hungry Mum.
  EXPRESSION: Complaining
- CHARACTER: Narrator
  LINE: She sits up suddenly, facing Samuel. She looks odd.
  EXPRESSION: Angry
- CHARACTER: Amelia
  LINE: Why do you have to talk-talk-talk all the time? Don’t you ever STOP TALKING?
  EXPRESSION: Angry
- CHARACTER: Narrator
  LINE: Samuel is taken aback by his mother’s tone.
  EXPRESSION: Surprised
- CHARACTER: Samuel
  LINE: I was just-
  EXPRESSION: Scared
- CHARACTER: Amelia
  LINE: I-NEED-TO-SLEEP.
  EXPRESSION: Angry
- CHARACTER: Narrator
  LINE: She looks fierce. Samuel is unnerved.
  EXPRESSION: null
- CHARACTER: Samuel
  LINE: I’m sorry Mummy, I was just hungry.
  EXPRESSION: Scared
- CHARACTER: Amelia
  LINE: If you’re that hungry, why don’t you go and EAT SHIT!
  EXPRESSION: Angry
- CHARACTER: Narrator
  LINE: Samuel backs away through the door, genuinely scared.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Amelia lies back down, pulling the sheets over her.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: After a moment, she realizes with absolute shame what she’s just done. It rattles her.
  EXPRESSION: Ashamed

::PATHS::
- CHOICE: "Go to Samuel's room"
  TARGET: samuel_room_morning
  STATE_CHANGE: guilt = +1
  CONDITION: null

::SCENE::
LOCATION: Samuel's Room
MOOD: Regret
CHARACTERS: Amelia, Samuel
BACKGROUND_IMAGE: samuel_room_morning.png
BACKGROUND_EDIT: "Samuel's bedroom, morning light, Samuel looking sad on his bed"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Amelia arrives at the door, sheepish. She sees Samuel on his bed, head down. He tries desperately not to cry. His body tenses as she comes near, he’s scared of her.
  EXPRESSION: null
- CHARACTER: Amelia
  LINE: I’m so sorry. I don’t know why I said that. That was terrible.
  EXPRESSION: Ashamed
- CHARACTER: Narrator
  LINE: Samuel doesn’t look at her. He starts to cry. It’s heart wrenching, Amelia feels it.
  EXPRESSION: null
- CHARACTER: Amelia
  LINE: It’s just... I’ve had absolutely no sleep... I didn’t know what I was saying.
  EXPRESSION: Ashamed
- CHARACTER: Narrator
  LINE: Samuel tries to stop crying, he can’t.
  EXPRESSION: null
- CHARACTER: Amelia
  LINE: I’ll cook you something. What would you like? You can have anything at all.
  EXPRESSION: Apologetic
- CHARACTER: Samuel
  LINE: I’m not hungry anymore.
  EXPRESSION: Sad
- CHARACTER: Narrator
  LINE: She puts her arm around him. He wriggles away from her.
  EXPRESSION: null
- CHARACTER: Amelia
  LINE: I can understand you being upset. I would be if I were you..
  EXPRESSION: Ashamed
- CHARACTER: Narrator
  LINE: Amelia searches for the right words to placate him.
  EXPRESSION: null
- CHARACTER: Amelia
  LINE: We need to get out of this house... Would you like to go to McDonalds?
  EXPRESSION: Apologetic
- CHARACTER: Samuel
  LINE: You said McDonalds is bad for you.
  EXPRESSION: Skeptical
- CHARACTER: Amelia
  LINE: Once in a while doesn’t hurt.
  EXPRESSION: Explaining
- CHARACTER: Narrator
  LINE: Samuel calms down a little.
  EXPRESSION: null
- CHARACTER: Amelia
  LINE: You can have whatever you want, alright? Even ice cream for breakfast if you want.
  EXPRESSION: Apologetic
- CHARACTER: Narrator
  LINE: A long pause as Samuel calms down, thinks about it.
  EXPRESSION: null

::PATHS::
- CHOICE: "Go to McDonalds"
  TARGET: mcdonalds_day
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: McDonalds
MOOD: Irritating
CHARACTERS: Amelia, Samuel
BACKGROUND_IMAGE: mcdonalds_day.png
BACKGROUND_EDIT: "Bright, noisy McDonalds interior, packed with children for a party"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Kid’s party. The place is packed with screaming children.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Amelia looks around at the tacky decor. The sounds and sights are irritating, loud and bright.
  EXPRESSION: Annoyed
- CHARACTER: Narrator
  LINE: Samuel sits in front of a large Happy Meal, dark circles under his eyes. He chomps away on his french fries.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Amelia gives him a wa
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue"
  TARGET: end
  STATE_CHANGE: null
  CONDITION: null

::SCRIPT::
- CHARACTER: Narrator
  LINE: He manages one back. Things are better, the power of junk food has worked.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: A stabbing pain in her jaw. Amelia winces. She reaches inside her mouth and feels her back molar. She massages her jaw, searching for relief.
  EXPRESSION: Pain

::SCENE::
LOCATION: Car
MOOD: Panicked
CHARACTERS: Samuel, Amelia, Guy
BACKGROUND_IMAGE: car_interior.png
BACKGROUND_EDIT: "Daytime, distressed interior, slight chaos"

::SCRIPT::
- CHARACTER: Samuel
  LINE: Where are we going?
  EXPRESSION: Tired
- CHARACTER: Amelia
  LINE: I just wanna drive for a while..
  EXPRESSION: Wired
- CHARACTER: Narrator
  LINE: Amelia feels an itch on her leg. She looks down. Her leg is covered in cockroaches. She recoils, desperately flicking them away. The car swerves, Samuel panics.
  EXPRESSION: Disgusted
- CHARACTER: Narrator
  LINE: Amelia looks in the rear vision mirror.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: A shadowy shape jumps onto the boot then the roof. She can hear it, pounding like mad, a terrible sound. She swerves all over the road, frightened.
  EXPRESSION: Frightened
- CHARACTER: Samuel
  LINE: screams.
  EXPRESSION: Scared
- CHARACTER: Narrator
  LINE: Amelia accidentally accelerates, heading straight towards another car. A screeching of tyres, a sickening sound.
  EXPRESSION: Scared
- CHARACTER: Narrator
  LINE: Amelia is frozen at the wheel, shell shocked. Samuel is crying. It’s a miracle they’re not hurt.
  EXPRESSION: Shocked
- CHARACTER: Narrator
  LINE: A young corporate guy gets out of the other car, a brand new Audi. He inspects the damage, then runs to Amelia.
  EXPRESSION: null
- CHARACTER: Guy
  LINE: You ran straight into me!
  EXPRESSION: Angry
- CHARACTER: Narrator
  LINE: Amelia looks at him with a blank expression, in shock.
  EXPRESSION: Shocked
- CHARACTER: Guy
  LINE: I just bought this bloody car! What were you doing?
  EXPRESSION: Angry
- CHARACTER: Narrator
  LINE: The guy looks into the back seat, sees Samuel cowering.
  EXPRESSION: null
- CHARACTER: Guy
  LINE: Oh! Driving on the wrong side of the road! With a kid in the back! You could have KILLED someone, you know that!?
  EXPRESSION: Angry
- CHARACTER: Narrator
  LINE: The man’s face looms large and terrible in the window.
  EXPRESSION: Scared
- CHARACTER: Narrator
  LINE: She reverses the car suddenly and screeches away as fast as she can, leaving the man bewildered in her wake.
  EXPRESSION: Panicked

::PATHS::
- CHOICE: "Drive home"
  TARGET: amelia_front_yard
  STATE_CHANGE: fear = +1, adrenaline = +1
  CONDITION: null

::SCENE::
LOCATION: Mrs Roache’s Front Yard / Amelia’s Front Yard
MOOD: Worried
CHARACTERS: Mrs Roach, Amelia, Sam
BACKGROUND_IMAGE: suburban_front_yard.png
BACKGROUND_EDIT: "Daytime, quiet suburban street, slightly overgrown"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Mrs Roach is collecting the mail. She sees Amelia and Sam getting out of their car, goes to say hello, but is stopped by the look on Amelia’s face. She looks terrible.
  EXPRESSION: Worried
- CHARACTER: Narrator
  LINE: Amelia checks the roof of the car. There’s nothing, not a dint, not a scratch. Her face pales. She stumbles to the house, Samuel drags along behind, focusing on his mum.
  EXPRESSION: Confused
- CHARACTER: Narrator
  LINE: Mrs Roach watches them as they disappear, worried.
  EXPRESSION: Worried

::PATHS::
- CHOICE: "Go inside"
  TARGET: bathroom
  STATE_CHANGE: confusion = +1, fear = +1
  CONDITION: null

::SCENE::
LOCATION: Bathroom
MOOD: Trembling
CHARACTERS: Amelia, Samuel
BACKGROUND_IMAGE: bathroom.png
BACKGROUND_EDIT: "Evening, warm bath running, worn and humble"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Amelia has a warm bath running and is sitting in it, fully clothed. She holds her knees to her chest, trembling, trying to calm herself down. She looks awful.
  EXPRESSION: Afraid
- CHARACTER: Narrator
  LINE: Samuel stands by, worried.
  EXPRESSION: Worried
- CHARACTER: Samuel
  LINE: Mum. Do you want me to call Aunty Claire?
  EXPRESSION: Worried
- CHARACTER: Narrator
  LINE: She doesn’t reply. Samuel edges closer.
  EXPRESSION: null
- CHARACTER: Samuel
  LINE: I can talk to her and tell her we had an accident and she can come over... Mum?
  EXPRESSION: Worried
- CHARACTER: Amelia
  LINE: Aunty Claire doesn’t want to talk to us anymore.
  EXPRESSION: Quiet
- CHARACTER: Narrator
  LINE: Beat. Amelia gets up and grabs hold of Samuel gently. She puts him into the bath, shirt, shorts, socks and all.
  EXPRESSION: Soothing
- CHARACTER: Amelia
  LINE: It’s nice and warm in here..
  EXPRESSION: Soothing
- CHARACTER: Narrator
  LINE: Samuel sits opposite his mum, very concerned. Long pause.
  EXPRESSION: Worried
- CHARACTER: Samuel
  LINE: I don’t want you to go away..
  EXPRESSION: Scared
- CHARACTER: Amelia
  LINE: I’m not going anywhere.
  EXPRESSION: Calm
- CHARACTER: Narrator
  LINE: They sit opposite each other, in silence.
  EXPRESSION: null

::PATHS::
- CHOICE: "Exit bathroom"
  TARGET: entrance_to_basement
  STATE_CHANGE: calm = -1, worry = +1
  CONDITION: null

::SCENE::
LOCATION: Entrance to Basement
MOOD: Shocked
CHARACTERS: Amelia, Samuel
BACKGROUND_IMAGE: basement_entrance.png
BACKGROUND_EDIT: "Evening, dark, cluttered hallway leading to a basement"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Amelia comes out of the basement, clutching the violin.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: She clocks Samuel in the lounge and walks right past him without acknowledgement. Sam is shocked.
  EXPRESSION: Shocked

::PATHS::
- CHOICE: "Follow Amelia"
  TARGET: amelia_room_first_part
  STATE_CHANGE: confusion = +1
  CONDITION: null

::SCENE::
LOCATION: Amelia’s Room
MOOD: Tense
CHARACTERS: Amelia, Samuel
BACKGROUND_IMAGE: amelia_room.png
BACKGROUND_EDIT: "Evening, slightly messy, intimate setting"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Amelia lies down, calmed by the violin tight in her arms.
  EXPRESSION: Calm
- CHARACTER: Narrator
  LINE: Sam follows, climbing on the bed to stroke her forehead. She relaxes and closes her eyes, letting him comfort her.
  EXPRESSION: Relaxed
- CHARACTER: Narrator
  LINE: A tender moment between them as Samuel smooths his mum’s hair, suddenly the parent.
  EXPRESSION: Tender
- CHARACTER: Samuel
  LINE: Mum... I don’t think we should stay here tonight. I can call Mrs Roach.
  EXPRESSION: Worried
- CHARACTER: Amelia
  LINE: We can’t trouble other people.
  EXPRESSION: Firm
- CHARACTER: Samuel
  LINE: She wouldn’t mind, I know she wouldn’t.
  EXPRESSION: Reassuring
- CHARACTER: Amelia
  LINE: I don’t want you to call anyone. I just need to sleep...
  EXPRESSION: Tired
- CHARACTER: Narrator
  LINE: Sam strokes Amelia’s cheek. She relaxes, letting him in.
  EXPRESSION: Relaxed
- CHARACTER: Narrator
  LINE: He accidentally knocks the violin with his knee.
  EXPRESSION: Accidental
- CHARACTER: Amelia
  LINE: Leave it!
  EXPRESSION: Vicious
- CHARACTER: Narrator
  LINE: Sam backs away, sitting on an easy chair in the corner.
  EXPRESSION: Scared
- CHARACTER: Narrator
  LINE: Amelia watches him there from the bed. Her eyelids open and close, she gives in to sleep, shutting out her son.
  EXPRESSION: Tired

::PATHS::
- CHOICE: "Wait for Amelia to sleep"
  TARGET: amelia_room_second_part
  STATE_CHANGE: fear = +1, tension = +1
  CONDITION: null

::SCENE::
LOCATION: Amelia’s Room
MOOD: Creepy
CHARACTERS: Amelia, (Whispers)
BACKGROUND_IMAGE: amelia_room_dark.png
BACKGROUND_EDIT: "Late evening, last rays of light dying, shadows forming"

::SCRIPT::
- CHARACTER: Narrator
  LINE: A short while later. The last rays of light are dying in the room, they play on the curtains, shadows form.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Creepy.
  EXPRESSION: Creepy
- CHARACTER: Narrator
  LINE: Amelia’s sleeping face. Whispering voices, barely audible, envelop her. They sound demonic. Her face contorts from a nightmare. The whispers intensify.
  EXPRESSION: Disturbed
- CHARACTER: Narrator
  LINE: Amelia’s eyes snap open. The whispers stop altogether.
  EXPRESSION: Startled
- CHARACTER: Narrator
  LINE: She sits up. Is she hearing things? She searches the near dark room.
  EXPRESSION: Confused
- CHARACTER: Narrator
  LINE: Eerie silence. Samuel is nowhere to be found.
  EXPRESSION: Eerie

::PATHS::
- CHOICE: "Search for Samuel"
  TARGET: upstairs_hallway
  STATE_CHANGE: fear = +2, confusion = +1
  CONDITION: null

::SCENE::
LOCATION: Upstairs Hallway
MOOD: Taunting
CHARACTERS: Amelia, (Whispers)
BACKGROUND_IMAGE: upstairs_hallway.png
BACKGROUND_EDIT: "Evening, fading light, dark and ominous"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Light is fading fast in the house. Amelia descends the stairs, straining to see.
  EXPRESSION: Strained
- CHARACTER: Narrator
  LINE: The whispers start up again, taunting her. She stops dead in her tracks and the sounds stop.
  EXPRESSION: Taunted
- CHARACTER: Narrator
  LINE: She stumbles on, her face dark and troubled.
  EXPRESSION: Troubled

::PATHS::
- CHOICE: "Continue downstairs"
  TARGET: lounge_room_kitchen
  STATE_CHANGE: fear = +1, anger = +1
  CONDITION: null

::SCENE::
LOCATION: Lounge Room - Kitchen
MOOD: Infuriated
CHARACTERS: Amelia, Samuel, Mrs Roach (O.S.)
BACKGROUND_IMAGE: lounge_kitchen.png
BACKGROUND_EDIT: "Evening, dark lounge transitioning to lit kitchen"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Amelia stands in the dark lounge room. The whispers return, only louder this time, more threatening. She can’t tell where they’re coming from. It infuriates her.
  EXPRESSION: Infuriated
- CHARACTER: Narrator
  LINE: She races into the kitchen, turns on the light, and rounds the bench.
  EXPRESSION: Rushing
- CHARACTER: Narrator
  LINE: She sees Samuel in his armour, whispering to someone on her mobile phone. He almost jumps out of his skin.
  EXPRESSION: Surprised
- CHARACTER: Narrator
  LINE: She rips the mobile out of his hand and looks at the screen, livid. Mrs Roach’s name flashes up.
  EXPRESSION: Furious
- CHARACTER: Narrator
  LINE: She tries to contain her fury as she prepares to talk.
  EXPRESSION: Containing Fury
- CHARACTER: Amelia
  LINE: Gracie. I am so sorry.
  EXPRESSION: Calm
- CHARACTER: Mrs Roach
  LINE: Has someone broken into the house? Sam said someone was trying to get in??
  EXPRESSION: Worried
- CHARACTER: Amelia
  LINE: No. We’re fine. Samuel’s just being very disobedient. Again.
  EXPRESSION: Dismissive
- CHARACTER: Mrs Roach
  LINE: Oh! I was so worried!
  EXPRESSION: Relieved
- CHARACTER: Amelia
  LINE: I’m really sorry. I told him not to bother anyone.
  EXPRESSION: Apologetic
- CHARACTER: Mrs Roach
  LINE: He asked if you could stay the night, that’s no problem at all-
  EXPRESSION: Welcoming
- CHARACTER: Amelia
  LINE: No, we’re fine. I have a small headache, that’s all. I’ve got to go now though. I’m sorry for troubling you.....Yes, talk soon.
  EXPRESSION: Polite
- CHARACTER: Narrator
  LINE: She hangs up, deadly silent, glaring at Sam.
  EXPRESSION: Furious
- CHARACTER: Narrator
  LINE: He looks white as a sheet.
  EXPRESSION: Scared
- CHARACTER: Amelia
  LINE: I told you not to call anyone and you deliberately disobeyed me.
  EXPRESSION: Tight
- CHARACTER: Narrator
  LINE: Samuel lowers his head, anxious and scared.
  EXPRESSION: Scared
- CHARACTER: Amelia
  LINE: Do you want to frighten Mrs Roach? An old lady who can hardly walk? Do you want to make her sick?
  EXPRESSION: Accusatory
- CHARACTER: Narrator
  LINE: Sam is too scared to talk. This inflames Amelia more.
  EXPRESSION: Angry
- CHARACTER: Amelia
  LINE: Take that bloody thing off!
  EXPRESSION: Exploding
- CHARACTER: Narrator
  LINE: He takes the catapult off quick smart.
  EXPRESSION: Quick
- CHARACTER: Narrator
  LINE: Amelia takes out her phone battery, chucks it in the bin, only half aware of what she’s doing.
  EXPRESSION: Distraught
- CHARACTER: Amelia
  LINE: Is this the only way I can trust you won’t embarrass me in front of the neighbours?
  EXPRESSION: Desperate
- CHARACTER: Narrator
  LINE: She grabs something from the kitchen: a large knife.
  EXPRESSION: Threatening
- CHARACTER: Narrator
  LINE: Samuel is freaked out by the sight.
  EXPRESSION: Terrified
- CHARACTER: Amelia
  LINE: Is this what I have to do?
  EXPRESSION: Desperate
- CHARACTER: Narrator
  LINE: She cuts the cord to the land line, shaking with anger.
  EXPRESSION: Enraged
- CHARACTER: Samuel
  LINE: I’m sorry Mummy. I was just scared because the B
  EXPRESSION: Scared

::PATHS::
- CHOICE: "End of excerpt"
  TARGET: end
  STATE_CHANGE: fear = +3, anger = +2
  CONDITION: null

::SCENE::
LOCATION: House
MOOD: Intense, Fear, Anger
CHARACTERS: Amelia, Samuel, Narrator
BACKGROUND_IMAGE: house_living_room.png
BACKGROUND_EDIT: "Nighttime, tense atmosphere, domestic setting"

::SCRIPT::
- CHARACTER: Narrator
  LINE: abadook made you crash the car and then-
  EXPRESSION: null
- CHARACTER: Amelia
  LINE: What did you say?
  EXPRESSION: Angry
- CHARACTER: Narrator
  LINE: Amelia’s energy darkens. Samuel’s fear increases.
  EXPRESSION: null
- CHARACTER: Samuel
  LINE: I just didn’t want you to LET IT IN!
  EXPRESSION: Afraid
- CHARACTER: Narrator
  LINE: Amelia snaps. She races to the cupboard. Keys jingling.
  EXPRESSION: null
- CHARACTER: Amelia
  LINE: I’ll make sure we don’t let anything in, alright Samuel? Nothing is coming in here tonight. NOTHING!
  EXPRESSION: Angry
- CHARACTER: Narrator
  LINE: She charges off to the front door, opens it, locks the security grill, slams the front door with a vengeance.
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue"
  TARGET: house_security_intercut
  STATE_CHANGE: amelia_rage = +2, samuel_fear = +1
  CONDITION: null

::SCENE::
LOCATION: House (Intercut)
MOOD: Panic, Paranoia, Desperation
CHARACTERS: Amelia, Samuel, Bugsy, Narrator
BACKGROUND_IMAGE: house_intercut.png
BACKGROUND_EDIT: "Night, various parts of a home, focus on locked doors/windows, then hidden items"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Amelia locks the doors and windows, her face a mixture of rage and fear. She can’t stop herself, slamming and locking every door, every window in the house.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Bugsy follows her, barking incessantly. She kicks him out of the way, completely agitated, driven.
  EXPRESSION: Angry
- CHARACTER: Narrator
  LINE: Samuel unlocks a case under his bed, pulling out hidden weapons. He listens to Amelia banging around downstairs.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Amelia has locked up the entire house. In one last impulsive move, she throws all her keys out a barred, backyard window. Her rage has worn itself out. Now, she just looks frightened.
  EXPRESSION: Afraid

::PATHS::
- CHOICE: "Continue"
  TARGET: samuels_bedroom_medication
  STATE_CHANGE: amelia_fear = +1, samuel_prepared = true
  CONDITION: null

::SCENE::
LOCATION: Samuel’s Bedroom
MOOD: Tense, Distrust, Manipulation
CHARACTERS: Amelia, Samuel, Narrator
BACKGROUND_IMAGE: samuels_bedroom.png
BACKGROUND_EDIT: "Night, dimly lit, cluttered kid's room, Amelia and Samuel on bed"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Amelia and Samuel sit on his bed.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Amelia tries her best to be nice. The intense pain in her jaw and head make it tough. She has the water and pills.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Sam is on edge, unwilling to take his medicine.
  EXPRESSION: null
- CHARACTER: Samuel
  LINE: I feel sick.
  EXPRESSION: Afraid
- CHARACTER: Amelia
  LINE: If you don’t take the pills you’ll feel worse.
  EXPRESSION: Neutral
- CHARACTER: Samuel
  LINE: Mum...
  EXPRESSION: Afraid
- CHARACTER: Amelia
  LINE: Come on Samuel.
  EXPRESSION: Neutral
- CHARACTER: Samuel
  LINE: I don’t think I need-
  EXPRESSION: Afraid
- CHARACTER: Amelia
  LINE: I am the parent and you are the child. So take-the-pills.
  EXPRESSION: Angry
- CHARACTER: Narrator
  LINE: Samuel takes the pills from her. He raises his arm.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The pills drop down discreetly into his shirt sleeve as he brings his hand to his mouth. A perfect sleight of hand that Amelia doesn’t see. He takes a swig of water.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: She opens his mouth, checks he’s taken them.
  EXPRESSION: null
- CHARACTER: Amelia
  LINE: Good boy.
  EXPRESSION: Neutral

::PATHS::
- CHOICE: "Continue"
  TARGET: loungeroom_hallucination
  STATE_CHANGE: samuel_outsmarted_amelia = true, amelia_pain = +1
  CONDITION: null

::SCENE::
LOCATION: Loungeroom
MOOD: Horror, Shock, Disorientation
CHARACTERS: Amelia, Samuel (O.S.), Narrator
BACKGROUND_IMAGE: loungeroom_evening.png
BACKGROUND_EDIT: "Evening, TV on, Amelia dozing, then a horrific hallucination"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Hysterical sound effects from a cartoon on the TV. Amelia is dozing. She jolts awake and looks over to the couch.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Samuel lies there on his back. His throat is cut. There are multiple stab wounds to his body. His dead eyes stare up at the ceiling, his face and body soaked in blood.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Amelia rushes over to him. She tries to scream, but nothing comes out, her face a horrible mask of fear.
  EXPRESSION: Afraid
- CHARACTER: Samuel (O.S.)
  LINE: Mum!
  EXPRESSION: Neutral
- CHARACTER: Narrator
  LINE: Amelia looks at her son.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: He is crouched on the sofa, ready to spring. He’s perfectly fine, but terrified by his mother’s behaviour.
  EXPRESSION: Afraid
- CHARACTER: Narrator
  LINE: Amelia slowly recovers, completely disoriented.
  EXPRESSION: Surprised
- CHARACTER: Narrator
  LINE: Samuel looks to her right hand, terrified.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Amelia looks to where he’s looking.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: There’s a large carving knife in her hand.
  EXPRESSION: Surprised

::PATHS::
- CHOICE: "Continue"
  TARGET: kitchen_knife
  STATE_CHANGE: amelia_fear = +2, amelia_disoriented = true
  CONDITION: null

::SCENE::
LOCATION: Kitchen
MOOD: Action, Self-preservation
CHARACTERS: Amelia, Narrator
BACKGROUND_IMAGE: kitchen_evening.png
BACKGROUND_EDIT: "Evening, kitchen interior, Amelia throwing a knife"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Amelia throws the knife in the drawer and slams it shut.
  EXPRESSION: Angry

::PATHS::
- CHOICE: "Continue"
  TARGET: amelias_room_bugsy
  STATE_CHANGE: amelia_denial = true
  CONDITION: null

::SCENE::
LOCATION: Amelia’s Room
MOOD: Sadness, Comfort, Sudden Shock
CHARACTERS: Amelia, Bugsy, Narrator
BACKGROUND_IMAGE: amelias_room.png
BACKGROUND_EDIT: "Night, Amelia's bedroom, soft lighting, then tension"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Amelia sits on her bed, tears roll down her face.
  EXPRESSION: Sad
- CHARACTER: Narrator
  LINE: Bugsy appears at the door. The sight of him comforts her.
  EXPRESSION: null
- CHARACTER: Amelia
  LINE: Come on sweetheart. Come here.
  EXPRESSION: Sad
- CHARACTER: Narrator
  LINE: He stays at the door.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Amelia goes to him very gently. He puts his ears back but lets himself be picked up. She strokes him tenderly, her fear dissipates. They stay there like that for a moment.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Bugsy suddenly bites her hand and jumps to the floor. Amelia watches him run away, in shock.
  EXPRESSION: Surprised

::PATHS::
- CHOICE: "Continue"
  TARGET: loungeroom_icecream
  STATE_CHANGE: amelia_shock = +1, bugsy_distrust = true
  CONDITION: null

::SCENE::
LOCATION: Lounge Room
MOOD: Forced Normalcy, Tension, Pain
CHARACTERS: Amelia, Samuel, Narrator
BACKGROUND_IMAGE: loungeroom_night.png
BACKGROUND_EDIT: "Night, TV on, Amelia and Samuel eating ice cream, forced cheerfulness"

::SCRIPT::
- CHARACTER: Narrator
  LINE: TV still on. Amelia brings two bowls loaded up with ice cream, marshmallows on top. She’s trying way too hard.
  EXPRESSION: null
- CHARACTER: Amelia
  LINE: Here we go!
  EXPRESSION: Happy
- CHARACTER: Narrator
  LINE: Samuel looks at the bowls, his face is worried and tense. She places it in front of him, forcing a smile.
  EXPRESSION: null
- CHARACTER: Amelia
  LINE: There’s more where that came from.
  EXPRESSION: Happy
- CHARACTER: Narrator
  LINE: Samuel takes a spoonful, tasting it gingerly.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Amelia watches him eat, tense as hell. A sudden, stabbing pain in her tooth, her hand flies up to her jaw. It’s getting worse. She massages, fear and pain in her eyes.
  EXPRESSION: Afraid

::PATHS::
- CHOICE: "Continue"
  TARGET: loungeroom_later_news
  STATE_CHANGE: amelia_pain = +1, samuel_worry = +1
  CONDITION: null

::SCENE::
LOCATION: Lounge Room (Later)
MOOD: Dread, Horror, Panic, Supernatural
CHARACTERS: Amelia, Samuel, Bugsy, News Reporter (V.O.), Narrator
BACKGROUND_IMAGE: loungeroom_late_night.png
BACKGROUND_EDIT: "Late night, TV news playing, unsettling images, then darkness and strange events"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Mother and son steal glances at each other. The TV blares over the top of their silence.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Samuel’s eyelids become heavy as he struggles with, then succumbs to sleep. Bugsy guards Samuel, watches Amelia.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Amelia channel surfs manically, not stopping to look at anything. She finally stops on the late night news.
  EXPRESSION: null
- CHARACTER: News Reporter (V.O.)
  LINE: ... in the kitchen where he beheaded his sister, reportedly a day after her birthday. She had just turned seven.
  EXPRESSION: Neutral
- CHARACTER: Narrator
  LINE: Amelia watches, horrified. Images of a normal suburban house, cordoned off, police on the scene.
  EXPRESSION: Afraid
- CHARACTER: News Reporter (V.O.)
  LINE: Her teenage brother remained inside where he was eventually shot dead by police.
  EXPRESSION: Neutral
- CHARACTER: Narrator
  LINE: Amelia sees police on the TV pass by a window of the house.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: What she sees next chills her to the bone.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: There is a clear image of Amelia herself looking out from the window of this suburban house, smiling a disturbing smile.
  EXPRESSION: Surprised
- CHARACTER: Narrator
  LINE: Amelia tries to comprehend what she sees.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Suddenly, all the lights snap off, plunging the house into darkness.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Amelia’s breathing hardens. Her eyes focus on the couch.
  EXPRESSION: Afraid
- CHARACTER: Narrator
  LINE: Samuel is no longer on it. Her panic increases.
  EXPRESSION: Afraid
- CHARACTER: Amelia
  LINE: Samuel...
  EXPRESSION: Afraid
- CHARACTER: Narrator
  LINE: Samuel is suddenly beside her. It frightens her.
  EXPRESSION: Surprised
- CHARACTER: Samuel
  LINE: Wake up Mummy.
  EXPRESSION: Neutral
- CHARACTER: Narrator
  LINE: She can see his eyes are closed.
  EXPRESSION: null
- CHARACTER: Amelia
  LINE: Darling, you’re the one who’s asleep.
  EXPRESSION: Confused
- CHARACTER: Narrator
  LINE: He stands there for some time, then drifts towards the basement door, eyes still closed.
  EXPRESSION: null
- CHARACTER: Amelia
  LINE: Don’t go down there..
  EXPRESSION: Afraid
- CHARACTER: Narrator
  LINE: He opens the door. A light comes on down there. Samuel disappears down the stairs.
  EXPRESSION: null
- CHARACTER: Amelia
  LINE: It’s not safe!
  EXPRESSION: Afraid
- CHARACTER: Narrator
  LINE: She stands at the top of the basement stairs watching Sam descend. She’s confused by the light being on down there. It draws her down, into the bowels of the house.
  EXPRESSION: Confused

::PATHS::
- CHOICE: "Follow Samuel"
  TARGET: basement_reunion
  STATE_CHANGE: amelia_fear = +2, amelia_curiosity = +1
  CONDITION: null

::SCENE::
LOCATION: Basement
MOOD: Ethereal, Reunion, Sudden Dread
CHARACTERS: Amelia, Oskar, Narrator
BACKGROUND_IMAGE: basement_night.png
BACKGROUND_EDIT: "Night, basement transformed by ethereal light, then deep shadows"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Amelia arrives to a basement completely clear of clutter. The most beautiful, ethereal light transforms it.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Samuel is nowhere to be found. Amelia steps into the light and is calmed by it.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Out of the shadows steps the man from the photo. Amelia’s husband, Oskar, a handsome man in his forties.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Amelia’s face drops when she sees him. Her eyes spontaneously fill with tears. She races in to him.
  EXPRESSION: Sad
- CHARACTER: Narrator
  LINE: They stay like that for a long time, holding each other.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Amelia cries in disbelief, her emotions overwhelming her.
  EXPRESSION: Sad
- CHARACTER: Narrator
  LINE: He kisses her, he’s real. She melts into him, letting go into one exquisite moment.
  EXPRESSION: null
- CHARACTER: Amelia
  LINE: I thought you were dead..
  EXPRESSION: Sad
- CHARACTER: Oskar
  LINE: We can be together sweetheart...
  EXPRESSION: Happy
- CHARACTER: Narrator
  LINE: She hugs him tighter, in complete disbelief. Long pause.
  EXPRESSION: null
- CHARACTER: Oskar
  LINE: You just need to bring me the boy.
  EXPRESSION: Neutral
- CHARACTER: Narrator
  LINE: Amelia feels a sudden chill run over her and pulls back from her husband. It suddenly doesn’t feel right.
  EXPRESSION: Afraid
- CHARACTER: Narrator
  LINE: The beautiful light has disappeared. Deep shadows fall across Oskar’s face. He looks strange.
  EXPRESSION: null
- CHARACTER: Amelia
  LINE: You mean Samuel..
  EXPRESSION: Surprised
- CHARACTER: Oskar
  LINE: You can bring me th
  EXPRESSION: Angry

::PATHS::
- CHOICE: "Confront Oskar"
  TARGET: end
  STATE_CHANGE: amelia_fear = +3, oskar_revealed = true
  CONDITION: null

::SCENE::
LOCATION: Living Room - Downstairs
MOOD: Terrifying, Confrontational
CHARACTERS: Amelia, Oskar, The Babadook
BACKGROUND_IMAGE: living_room_downstairs.png
BACKGROUND_EDIT: "Nighttime, dimly lit, unsettling atmosphere"

::SCRIPT::
- CHARACTER: The Babadook (Through Oskar)
  LINE: The boy... You can bring me the boy...
  EXPRESSION: Distorted
- CHARACTER: Amelia
  LINE: Stop calling him the boy.
  EXPRESSION: Angry
- CHARACTER: Narrator
  LINE: Amelia looks down to Oskar’s hands. There’s nothing at the end of his sleeves. She tries to comprehend it. A rumbling sound starts up.
  EXPRESSION: Surprised
- CHARACTER: Oskar
  LINE: I think it’s going to rain.
  EXPRESSION: Distorted
- CHARACTER: Narrator
  LINE: She looks up.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: A razor thin line of blood forms a diagonal line from one ear across to his jaw on the other side.
  EXPRESSION: null
- CHARACTER: Amelia
  LINE: No....
  EXPRESSION: Terrified
- CHARACTER: Narrator
  LINE: Amelia bolts up those stairs as fast as she can.
  EXPRESSION: Terrified

::PATHS::
- CHOICE: "Flee upstairs to the lounge room"
  TARGET: lounge_room_kitchen
  STATE_CHANGE: fear = +3
  CONDITION: null

::SCENE::
LOCATION: Lounge Room - Kitchen
MOOD: Extreme Terror, Dread
CHARACTERS: Amelia, The Babadook
BACKGROUND_IMAGE: lounge_room_kitchen.png
BACKGROUND_EDIT: "Nighttime, flickering lights, dark kitchen corner, eerie"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Amelia enters the lounge room. The lights have returned, flickering on and off. The TV is on static.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Amelia watches the overhead light flare up. The bulb smashes.
  EXPRESSION: Surprised
- CHARACTER: Narrator
  LINE: Complete darkness. A hideous silence.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Amelia senses something behind her in the kitchen. She turns slowly and is met with her worst nightmare.
  EXPRESSION: Afraid
- CHARACTER: Narrator
  LINE: At the far corner of the kitchen, about 15 metres away, is a hideous silhouette in the darkness. A large black coat, pointy black gloves and a tall black hat.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Then she hears it. A terrifying, insect like noise as the thing glides straight towards her. It stops, towering over her. She can’t make out any details, but she can feel it looking at her, suspended in terror.
  EXPRESSION: Afraid
- CHARACTER: Narrator
  LINE: She suddenly tears up those stairs, taking two at a time, racing into the first open door she can find. The sound of the thing screeching after her.
  EXPRESSION: Terrified

::PATHS::
- CHOICE: "Escape into Samuel's room"
  TARGET: samuels_room
  STATE_CHANGE: fear = +3
  CONDITION: null

::SCENE::
LOCATION: Samuel’s Room
MOOD: Absolute Terror, Possession
CHARACTERS: Amelia, The Babadook
BACKGROUND_IMAGE: samuels_room.png
BACKGROUND_EDIT: "Nighttime, dark, oppressive atmosphere, fireplace"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Amelia grabs a chair and pushes it under the doorknob, stumbling backwards towards the fireplace.
  EXPRESSION: Terrified
- CHARACTER: Narrator
  LINE: An awful silence, just the sound of Amelia’s breath.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Something falls down the chimney and lands in the hearth right next to her. A black top hat.
  EXPRESSION: Surprised
- CHARACTER: Narrator
  LINE: Amelia goes into a panic attack. She crawls back towards the door, but her movements are slow and tortured.
  EXPRESSION: Terrified
- CHARACTER: Narrator
  LINE: She can hear something huge and hideous travelling up the wall behind her, then onto the ceiling overhead. An insect-like sound fills the room. Amelia can’t bear to look up, lying on her stomach, frozen with terror.
  EXPRESSION: Terrified
- CHARACTER: Narrator
  LINE: Something drops down nearby. A black coat. Amelia starts to hyperventilate.
  EXPRESSION: Terrified
- CHARACTER: Narrator
  LINE: A terrible noise, flesh ripping from flesh. Something drops inches from her face. The ripped off ‘face’ of the Babadook, nothing but a hardened mask. Black sticky blood oozes from its edges, from the holes where the eyes should be, the mouth open in a permanent scream.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: In spite of her terror, Amelia forces herself to look up to the ceiling for a split second, in disbelief.
  EXPRESSION: Surprised
- CHARACTER: Narrator
  LINE: An huge shadow fills half of the ceiling, a hideous shape with outstretched ‘wings’, like an enormous bat.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Amelia immediately looks away. She holds her breath, tensing up, belly to the ground, beyond terror.
  EXPRESSION: Terrified
- CHARACTER: Amelia
  LINE: It isn’t real it isn’t real it isn’t real it isn’t real..
  EXPRESSION: Terrified
- CHARACTER: Narrator
  LINE: There is an unbearable screeching sound.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: POV from high on the ceiling. Something rushes straight down towards Amelia’s back at lightning pace.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Amelia’s eye in extreme close up. A huge bang, a terrible scraping, ripping sound. Her pupil ‘bleeds’ outwards till the whole eye is completely black.
  EXPRESSION: Terrified

::PATHS::
- CHOICE: "Amelia is possessed"
  TARGET: black_screen
  STATE_CHANGE: amelia_possessed = true, fear = +5
  CONDITION: null

::SCENE::
LOCATION: Black Screen
MOOD: Disorienting, Jarring
CHARACTERS: Narrator
BACKGROUND_IMAGE: black_screen.png
BACKGROUND_EDIT: "Pure black, only sound"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The sound of a TV up as loud as it will go. An informercial.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Terrible, deafening, meaningless sounds.
  EXPRESSION: null

::PATHS::
- CHOICE: "Transition to next scene"
  TARGET: amelias_bedroom_sam
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Amelia’s Bedroom
MOOD: Terrified, Suspense
CHARACTERS: Sam, Bugsy
BACKGROUND_IMAGE: amelias_bedroom.png
BACKGROUND_EDIT: "Nighttime, dimly lit, locked door"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Sam hides behind a locked door clutching Bugsy. The TV is deafening even from upstairs. He’s terrified. He unlocks and opens the door a sliver but doesn’t venture out.
  EXPRESSION: Terrified

::PATHS::
- CHOICE: "Stay hidden"
  TARGET: lounge_room_possessed_amelia
  STATE_CHANGE: sam_hiding = true, fear = +1
  CONDITION: null

::SCENE::
LOCATION: Lounge Room
MOOD: Disturbing, Unsettling, Eerie
CHARACTERS: Amelia, Judge 1 (O.S.), Judge 4 (O.S.), Model Host (O.S.), Judge 3 (O.S.)
BACKGROUND_IMAGE: lounge_room.png
BACKGROUND_EDIT: "Nighttime, TV static, possessed Amelia, unsettling"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The back of Amelia watching an informercial. Something’s not right with her. She breathes very fast and heavy.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Her face is revealed. Her eyes have a dead stare, the pupils like pin pricks. Her limbs are slightly distorted, rigid. She looks human, but there’s something about her that just-isn’t-right.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: She sits as if resting for a moment in her new skin, her casual stare at odds with her bizarre appearance. She changes channels to ‘Australia’s Next Top Model.’
  EXPRESSION: null
- CHARACTER: Judge 1
  LINE: She’s a great girl, but she’s too fat.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Amelia watches the program with a dead cool calm.
  EXPRESSION: null
- CHARACTER: Judge 4
  LINE: I agree unfortunately.
  EXPRESSION: null
- CHARACTER: Model Host
  LINE: What about Cindy?
  EXPRESSION: null
- CHARACTER: Judge 3
  LINE: Cindy is great! She can do soft, she can do bold, she can do sexy..
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Amelia cricks her neck, suddenly agitated. She stands and in a few jerky moves is up on top of the old TV.
  EXPRESSION: Angry
- CHARACTER: Judge 3
  LINE: I think she has a lot of extremes...
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: A stream of piss comes from between Amelia’s legs. It runs over the TV screen.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Amelia’s face as she relieves herself. She opens her mouth wide, clicking her jaw. She looks terrible.
  EXPRESSION: Terrified

::PATHS::
- CHOICE: "Continue watching possessed Amelia"
  TARGET: upstairs_landing_kitchen_lounge
  STATE_CHANGE: amelia_degraded = true, sanity = -2
  CONDITION: null

::SCENE::
LOCATION: Upstairs Landing - Lounge Room - Kitchen
MOOD: Horrific, Violent, Deeply Disturbing
CHARACTERS: Samuel, Bugsy, Amelia
BACKGROUND_IMAGE: house_interior.png
BACKGROUND_EDIT: "Nighttime, various rooms, chaotic, violent"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Landing. Samuel opens the door a sliver. Bugsy jumps from his arms and races down the stairs. Sam is beside himself, trying to call the dog back.
  EXPRESSION: Terrified
- CHARACTER: Narrator
  LINE: Bugsy arrives in the loungeroom, bravely facing his opponent. He barks ferociously.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Amelia, still on top of the TV, regards the dog with casual indifference, her eyes dead.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: She jumps down to the floor, squaring off at Bugsy.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: A moment of stillness.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Bugsy is spooked and makes a run for it.
  EXPRESSION: Afraid
- CHARACTER: Narrator
  LINE: Kitchen. Amelia chases Bugsy. The poor thing doesn’t have a chance as she grabs it by the neck. He struggles, trying to bite her. It’s awful.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Amelia’s terrible face, the dead eyes, fixated on the task.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The sound of Bugsy squealing in pain.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Bugsy’s little legs kick in spasms. A ghastly snapping sound.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The squealing stops dead, the legs go limp.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Amelia looks at the dog’s corpse, emotionless. Her face suddenly scrunches up in pain, she looks broken. It’s her molar. She yells dropping Bugsy’s corpse on the floor.
  EXPRESSION: Angry
- CHARACTER: Narrator
  LINE: She reaches into her mouth with her fingers, grabs hold in the back, wrenches the tooth from side to side, groaning horribly. She pulls and tugs, screaming in pain.
  EXPRESSION: Angry
- CHARACTER: Narrator
  LINE: After an age it wrenches free. She looks at the bloodied molar in morbid fascination, blood pooling in her mouth.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Suddenly bored with it, she throws the tooth away.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Lounge. Amelia stalks into the room. She instinctively whips her head up and looks straight at her son, his face peering over the bannister. He disappears, a door slams.
  EXPRESSION: Angry
- CHARACTER: Narrator
  LINE: Amelia’s jagged limbs move quickly, like a spider. She bolts straight up those stairs to her son.
  EXPRESSION: Angry

::PATHS::
- CHOICE: "Amelia pursues Samuel"
  TARGET: amelias_bedroom_outside
  STATE_CHANGE: bugsy_dead = true, sam_in_danger = true, fear = +4
  CONDITION: null

::SCENE::
LOCATION: Amelia’s Bedroom / Outside Amelia’s Bedroom
MOOD: Suspense, Dread, Psychological Horror
CHARACTERS: Samuel, Amelia
BACKGROUND_IMAGE: amelias_bedroom_door.png
BACKGROUND_EDIT: "Nighttime, locked door, tense atmosphere"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Samuel sits with his back against the locked door, key in hand. He hears Amelia’s footsteps right outside. He freezes as she tries the door.
  EXPRESSION: Terrified
- CHARACTER: Amelia
  LINE: Samuel.
  EXPRESSION: Distorted
- CHARACTER: Narrator
  LINE: He tenses, sits up to listen.
  EXPRESSION: Afraid
- CHARACTER: Narrator
  LINE: Amelia on the other side. She clears her throat, tries to ‘normalize.’ The pupils in her eyes contract slightly.
  EXPRESSION: null
- CHARACTER: Amelia
  LINE: Samuel. Let me in.
  EXPRESSION: Neutral
- CHARACTER: Narrator
  LINE: No response.
  EXPRESSION: null
- CHARACTER: Amelia
  LINE: Bugsy’s hurt. We need to go get help..
  EXPRESSION: Neutral

::PATHS::
- CHOICE: "Samuel faces Amelia"
  TARGET: end_sequence
  STATE_CHANGE: sam_confrontation = true
  CONDITION: null

::SCENE::
LOCATION: Samuel's Room
MOOD: Intense, Terrifying, Violent
CHARACTERS: Amelia, Samuel, Narrator
BACKGROUND_IMAGE: samuels_room.png
BACKGROUND_EDIT: "Nighttime, messy child's room, door broken, shadows, unsettling"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Her voice sounds normal but her face is terrifying.
  EXPRESSION: null
- CHARACTER: Amelia
  LINE: Samuel. Do you want Bugsy to die??
  EXPRESSION: Threatening
- CHARACTER: Narrator
  LINE: Samuel silently disappears out of frame.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Back to Amelia on the other side. Her mouth contorts with rage, her eyes devil’s eyes. She pounds on the door, growing violent.
  EXPRESSION: Angry
- CHARACTER: Amelia
  LINE: Samuel! Let-me-in!
  EXPRESSION: Angry
- CHARACTER: Narrator
  LINE: (No response)
  EXPRESSION: null
- CHARACTER: Amelia
  LINE: I’ll huff and I’ll puff and I’ll BLOW YOUR FUCKING DOOR IN!!
  EXPRESSION: Furious
- CHARACTER: Narrator
  LINE: She grabs the door frame with both hands, lifts herself up and slams the door with both feet. Then again, and again, over and over, till the door is kicked off its hinges and falls to the floor.
  EXPRESSION: Violent
- CHARACTER: Narrator
  LINE: Amelia enters, looks around. No sign of Samuel. This infuriates her.
  EXPRESSION: Furious
- CHARACTER: Narrator
  LINE: She moves in a jerky, powerful way, as if she has rods in her limbs. She looks under the bed, behind the curtains.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: She hears a tiny noise, swivels around in time to see her son sliding down from the top of the wardrobe. His little frame running towards the door.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Amelia lets out a screeching sound, just like the Babadook.
  EXPRESSION: Screeching
- CHARACTER: Narrator
  LINE: Samuel stops and turns to look, terrified.
  EXPRESSION: Afraid
- CHARACTER: Narrator
  LINE: His mother glides straight towards him, a spectral sight.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Samuel instantly wets his pants.
  EXPRESSION: Afraid
- CHARACTER: Amelia
  LINE: You little pig. 6 years old and you’re still wetting yourself.
  EXPRESSION: Cruel
- CHARACTER: Narrator
  LINE: He can’t look at her, puts his hands in his pockets.
  EXPRESSION: Ashamed
- CHARACTER: Amelia
  LINE: You don’t know how many times I’ve wished it was you not him that died.
  EXPRESSION: Cruel
- CHARACTER: Samuel
  LINE: I just want you to be happy.
  EXPRESSION: Sad
- CHARACTER: Amelia
  LINE: I just want you to be happee! You know, sometimes I just want to smash your head against the wall until your fucking brains pop out.
  EXPRESSION: Maniacal
- CHARACTER: Narrator
  LINE: Samuel backs away from her, his fists clenched.
  EXPRESSION: Defiant
- CHARACTER: Samuel
  LINE: You’re not my mother.
  EXPRESSION: Low
- CHARACTER: Amelia
  LINE: What did you say?
  EXPRESSION: Challenging
- CHARACTER: Narrator
  LINE: Looking her bravely in the eyes. Those terrible eyes.
  EXPRESSION: Brave
- CHARACTER: Samuel
  LINE: I said you’re not my mother!
  EXPRESSION: Defiant
- CHARACTER: Narrator
  LINE: She bends down to Samuel, her face evil, horrifying.
  EXPRESSION: Evil
- CHARACTER: Amelia
  LINE: I-AM-YOUR-MOTHER!!
  EXPRESSION: Shrieking
- CHARACTER: Narrator
  LINE: Samuel throws a firecracker on the floorboards, then another. They stun her long enough so he can escape.
  EXPRESSION: Action
- CHARACTER: Narrator
  LINE: Amelia finds fresh rage. She bolts out after him.
  EXPRESSION: Furious

::SCENE::
LOCATION: Upstairs Hallway / Samuel's Room
MOOD: Terrifying Chase, Violent Struggle, Desperation
CHARACTERS: Samuel, Amelia, Narrator
BACKGROUND_IMAGE: upstairs_hallway_samuels_room.png
BACKGROUND_EDIT: "Nighttime, dark hallway, a child's room visible, signs of struggle"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Samuel pelts down the hallway. His mother tears after him, screaming, her limbs disjointed and ‘broken’, moving fast like a spider.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Sam’s room. Samuel’s hands shake as he puts on his weapons. His eyes are wide with terror.
  EXPRESSION: Afraid
- CHARACTER: Narrator
  LINE: Amelia appears in the doorway, huge and terrifying. She looks at him with a cruel fascination.
  EXPRESSION: Terrifying
- CHARACTER: Samuel
  LINE: GET AWAY!!
  EXPRESSION: Desperate
- CHARACTER: Narrator
  LINE: She laughs a hideous laugh, closing in on the boy.
  EXPRESSION: Laughing
- CHARACTER: Narrator
  LINE: He launches the cricket ball, it hits her in the face. She bends over, covers her face with her hands, groaning.
  EXPRESSION: Pain
- CHARACTER: Narrator
  LINE: Samuel looks at his mum, very worried.
  EXPRESSION: Worried
- CHARACTER: Narrator
  LINE: Amelia stands up, takes her hands from her face. She laughs, mocking him. She’s not hurt at all.
  EXPRESSION: Mocking
- CHARACTER: Narrator
  LINE: Samuel fires his nail gun off in desperation, two large rusty nails land in his mother’s shoulder. She yells out in pain. This time she’s not pretending.
  EXPRESSION: Pain
- CHARACTER: Narrator
  LINE: Samuel makes a quick getaway.
  EXPRESSION: null

::SCENE::
LOCATION: Hallway
MOOD: Suspenseful, Dangerous, Relentless
CHARACTERS: Amelia, Samuel, Narrator
BACKGROUND_IMAGE: hallway.png
BACKGROUND_EDIT: "Nighttime, dark hallway, cabinets, suspenseful lighting"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Amelia comes out raging. She pulls the nails out of her shoulder, looks downstairs, then up to the top rooms, which way did he go?
  EXPRESSION: Raging
- CHARACTER: Narrator
  LINE: Samuel is behind her, hiding in front of a cabinet in the hall. All she has to do is turn around and he’s dead. He stares at his mother’s back, holding his breath.
  EXPRESSION: Afraid
- CHARACTER: Narrator
  LINE: There is a loud knock on the front door. Amelia pauses. Then she’s down those stairs, hardly touching the ground.
  EXPRESSION: null

::SCENE::
LOCATION: Lounge Room / Front Door / Kitchen
MOOD: Tense, Horrifying, Sudden Shift
CHARACTERS: Amelia, Samuel, Mrs. Roach, Narrator
BACKGROUND_IMAGE: lounge_kitchen_front_door.png
BACKGROUND_EDIT: "Nighttime, cluttered lounge room, front door visible, kitchen entrance, disturbing atmosphere"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Amelia lurches towards the front door, her face looks casually insane, and wholly evil.
  EXPRESSION: Evil
- CHARACTER: Narrator
  LINE: A silent, swift blur of movement can be seen in the background. It’s Samuel escaping to the kitchen.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Amelia’s deranged profile looking through the peep hole.
  EXPRESSION: Deranged
- CHARACTER: Narrator
  LINE: Amelia’s POV. Mrs Roach is waiting outside.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Amelia’s fingers clutch the doorknob. She’s ready to rip that door off its hinges.
  EXPRESSION: Violent
- CHARACTER: Narrator
  LINE: Samuel is horrified to see Bugsy’s remains on the floor in the kitchen. He tries the back door. It’s locked.
  EXPRESSION: Horrified
- CHARACTER: Narrator
  LINE: Through the peephole: Mrs Roach waits patiently in her dressing gown, shaky on her feet. She hesitates to knock again. Her kindly face looks worried.
  EXPRESSION: Worried
- CHARACTER: Narrator
  LINE: Something changes in Amelia. Her terrible expression softens. She lowers her head, her breathing slows down.
  EXPRESSION: Softening

::SCENE::
LOCATION: Hallway / Front Porch
MOOD: Melancholy, Vulnerable, Brief Respite
CHARACTERS: Amelia, Mrs. Roach, Narrator
BACKGROUND_IMAGE: hallway_front_porch.png
BACKGROUND_EDIT: "Nighttime, doorway with security grille, shadows, Mrs. Roach outside"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The door opens, Amelia stands behind the locked security grille. Her face is half in the shadows.
  EXPRESSION: null
- CHARACTER: Mrs. Roach
  LINE: Sorry love, I know it’s late. I just wanted to make sure you’re OK...
  EXPRESSION: Concerned
- CHARACTER: Amelia
  LINE: I’m OK.
  EXPRESSION: Clearing throat
- CHARACTER: Mrs. Roach
  LINE: I know this time of year is terribly hard for you. And I know you don’t want me to go on about it, so I won’t..
  EXPRESSION: Sympathetic
- CHARACTER: Narrator
  LINE: Amelia’s face behind the screen. She starts to normalize with Mrs Roach’s words, her eyes full of pain.
  EXPRESSION: Pained
- CHARACTER: Mrs. Roach
  LINE: I just want you to know I’d do anything for you and Sam. I love you both. You can always talk to me love. Always.
  EXPRESSION: Loving
- CHARACTER: Narrator
  LINE: Amelia’s face softens and saddens with every word. Her eye glints in the shadows, tears forming.
  EXPRESSION: Sad

::SCENE::
LOCATION: Kitchen
MOOD: Deceptive Calm, Mounting Tension, Betrayal, Shock, Madness
CHARACTERS: Amelia, Samuel, Narrator
BACKGROUND_IMAGE: kitchen.png
BACKGROUND_EDIT: "Nighttime, domestic kitchen, tense lighting, potential for violence"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Samuel has just closed a kitchen drawer.
  EXPRESSION: null
- CHARACTER: Amelia
  LINE: Samuel.
  EXPRESSION: Normal voice
- CHARACTER: Narrator
  LINE: Sam jumps. He turns sharply to see his mother at the other end of the kitchen. She looks completely normal.
  EXPRESSION: Surprised
- CHARACTER: Narrator
  LINE: Samuel watches her, caught between love and terror.
  EXPRESSION: Conflicted
- CHARACTER: Amelia
  LINE: I’m sorry. I said some terrible things. But I didn’t mean any of them...
  EXPRESSION: Genuine
- CHARACTER: Narrator
  LINE: She takes a step further into the kitchen. Samuel tenses.
  EXPRESSION: Tense
- CHARACTER: Amelia
  LINE: I understand you’re scared.
  EXPRESSION: Understanding
- CHARACTER: Narrator
  LINE: Samuel watches her, very wary, but drawn in by her.
  EXPRESSION: Wary
- CHARACTER: Amelia
  LINE: I haven’t been good since your Dad died. I haven’t been good at all.. I’m sick Sam, I need help.
  EXPRESSION: Remorseful
- CHARACTER: Narrator
  LINE: Samuel’s face softens. He listens intently.
  EXPRESSION: Softening
- CHARACTER: Amelia
  LINE: I just spoke to Mrs Roach. We’re going to stay there for the night.
  EXPRESSION: Normal
- CHARACTER: Narrator
  LINE: Amelia comes closer. She kneels in front of her son. Her face is soft and terribly sad.
  EXPRESSION: Sad
- CHARACTER: Amelia
  LINE: Do you want to do that?
  EXPRESSION: Gentle
- CHARACTER: Narrator
  LINE: Amelia puts one hand gently on his shoulder. Samuel nods.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Amelia’s hand behind her back is twisted and clenched.
  EXPRESSION: Tense
- CHARACTER: Amelia
  LINE: I want to make it up to you Sam. I want you to meet your Dad.
  EXPRESSION: Deceptive
- CHARACTER: Narrator
  LINE: She slips her other hand around the back of his neck, soothing him with her touch. He tenses.
  EXPRESSION: Tense
- CHARACTER: Amelia
  LINE: It’s beautiful. You’ll be happy there..
  EXPRESSION: Eerie
- CHARACTER: Narrator
  LINE: Samuel can see his mother’s pupils don’t look normal.
  EXPRESSION: Disturbed
- CHARACTER: Narrator
  LINE: Without warning, he quickly raises a carving knife behind his back and sinks it deep into his mother’s leg.
  EXPRESSION: Violent
- CHARACTER: Narrator
  LINE: She looks to him, then to the knife, absolutely stunned.
  EXPRESSION: Stunned
- CHARACTER: Samuel
  LINE: Sorry Mummy.
  EXPRESSION: Apologetic
- CHARACTER: Narrator
  LINE: He’s out of there.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Amelia stumbles onto her arse, looking in shock at the big knife sticking out of her thigh.
  EXPRESSION: Shocked
- CHARACTER: Narrator
  LINE: She reverts to something much more primitive than before. Her face distorts, a picture of madness. She rips the knife out in one go, yelling as she d
  EXPRESSION: Maddened

::SCENE::
LOCATION: Basement
MOOD: Frantic, Violent
CHARACTERS: Samuel, Amelia
BACKGROUND_IMAGE: basement.png
BACKGROUND_EDIT: "Dark, dingy basement, night"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Samuel races to the basement door. He takes a look back.
  EXPRESSION: Rushing
- CHARACTER: Narrator
  LINE: Amelia lets out a blood curdling sound as she rises.
  EXPRESSION: Terrifying
- CHARACTER: Narrator
  LINE: Samuel disappears into the basement.
  EXPRESSION: Scared
- CHARACTER: Narrator
  LINE: Amelia pauses at the top of the stairs, then descends at full speed, screaming like a banshee.
  EXPRESSION: Charging
- CHARACTER: Narrator
  LINE: A little hand pulls a rope, a trip wire forms.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Amelia’s feet connect with it. She tumbles forward, hitting her head on the ceiling beam, hard.
  EXPRESSION: Injured
- CHARACTER: Narrator
  LINE: She stumbles around, concussed. The room spins before her, she sees a brief glimpse of Samuel watching in horror, then the ceiling, the floor, out of control.
  EXPRESSION: Concussed
- CHARACTER: Narrator
  LINE: It looks terrible as she swerves and stumbles.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Sam has a baseball bat in both hands. He runs to Amelia and strikes her as hard as he can in the of the knees. She buckles and hits her head first on the wall, then hard on the concrete floor. The blows knock her out.
  EXPRESSION: Violent

::PATHS::
- CHOICE: "Continue"
  TARGET: basement_later
  STATE_CHANGE: amelia_unconscious = true, samuel_fear = +2
  CONDITION: null

::SCENE::
LOCATION: Basement
MOOD: Tense, Horrifying, Emotional
CHARACTERS: Amelia, Samuel
BACKGROUND_IMAGE: basement.png
BACKGROUND_EDIT: "Dingy basement, later, Amelia tied up"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Black screen.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The sound of very fast, shallow breathing. The ceiling comes into focus, one dingy light overhead.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Amelia in profile breathing super fast. Her pupils are now large and black as coals. She tries to lift herself up but despite her considerable power, she can’t.
  EXPRESSION: Distressed
- CHARACTER: Narrator
  LINE: She looks down. Every part of her, neck to toe, is tied and bound with rope, belts, anything Samuel could get his hands on. She looks like Gulliver in Lilliput. She makes a terrible shrieking sound, struggling to free herself.
  EXPRESSION: Struggling
- CHARACTER: Narrator
  LINE: Samuel slinks out of the shadows with his magician’s cape on, holding the baseball bat, trembling with fear.
  EXPRESSION: Scared
- CHARACTER: Samuel
  LINE: Mum...
  EXPRESSION: Trembling
- CHARACTER: Narrator
  LINE: Amelia sees him. She snarls, threatening him.
  EXPRESSION: Snarling
- CHARACTER: Samuel
  LINE: I’m not leaving you...
  EXPRESSION: Resolute
- CHARACTER: Narrator
  LINE: Amelia groans horribly, trying to free herself.
  EXPRESSION: Struggling
- CHARACTER: Narrator
  LINE: Samuel comes in a touch closer. The monstrous Amelia looks at him, as if trying to register who it is.
  EXPRESSION: Cautious
- CHARACTER: Narrator
  LINE: Samuel inches in closer, Amelia stops struggling.
  EXPRESSION: Cautious
- CHARACTER: Narrator
  LINE: He pulls out the bunch of paper flowers. She stares at them, becoming more herself, calming. Sam leans in.
  EXPRESSION: Offering
- CHARACTER: Narrator
  LINE: Amelia suddenly yells even louder than before. Samuel runs to the far corner of the basement, scared stiff. She laughs at his terror, a monstrous, agonized laugh.
  EXPRESSION: Furious
- CHARACTER: Samuel
  LINE: We said we’d protect each other...
  EXPRESSION: Reminding
- CHARACTER: Narrator
  LINE: Some of her ties have come undone. A few of the others are starting to come loose.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Samuel doesn’t notice as he sneaks back towards her, trying his hardest to be brave.
  EXPRESSION: Brave
- CHARACTER: Samuel
  LINE: I know you don’t love me. The Babadook won’t let you. But I love you mummy, ever since I was born and I always will...
  EXPRESSION: Emotional
- CHARACTER: Narrator
  LINE: The words get in somehow. Amelia’s face screws up in pain, fighting this thing that has taken her over.
  EXPRESSION: Pained
- CHARACTER: Narrator
  LINE: Another tie works itself loose, she wriggles and moves.
  EXPRESSION: Struggling
- CHARACTER: Samuel
  LINE: My dad died because he died. Not because of me.. It’s not my fault.
  EXPRESSION: Confessing
- CHARACTER: Narrator
  LINE: Amelia’s face contorts, affected by his words. She gasps for breath, trying to come out of it. A black tear wells up in the corner of her eye. She starts to shake.
  EXPRESSION: Affected
- CHARACTER: Samuel
  LINE: You let it in, you have to get it out!
  EXPRESSION: Desperate
- CHARACTER: Narrator
  LINE: The tear rolls down her face. A black substance seeps from one nostril. She looks terrible, shaking, trying to come back from the brink.
  EXPRESSION: Suffering
- CHARACTER: Narrator
  LINE: Samuel starts to cry at the sight, suddenly losing all his strength. The baseball bat goes limp in his arms.
  EXPRESSION: Crying
- CHARACTER: Samuel
  LINE: I don’t want you to go away...
  EXPRESSION: Bawling
- CHARACTER: Narrator
  LINE: Amelia’s arm suddenly comes free. Amelia rips the bat out of Sam’s hands and throws it across the room. He tries to get away. But before he can escape she’s grabbed him.
  EXPRESSION: Violent
- CHARACTER: Samuel
  LINE: NO!... NO, NO!! MUMMY!
  EXPRESSION: Terrified
- CHARACTER: Narrator
  LINE: Her other hand comes free. Samuel tries to punch and kick her, she tightens the grip on the back of his neck.
  EXPRESSION: Violent
- CHARACTER: Narrator
  LINE: She takes both hands and places them round Samuel’s neck. She struggles with what she is about to do but loses out.
  EXPRESSION: Choking
- CHARACTER: Narrator
  LINE: Slowly but surely, she chokes him.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: His little hands pull at her hands around his neck. But she’s too strong. Sam’s face turns red, he can’t breathe.
  EXPRESSION: Struggling
- CHARACTER: Narrator
  LINE: A look of terrible recognition passes across Amelia’s monstrous face as she realizes what she’s doing, but still she can’t stop. She cries out, trying to summon up strength from the depths. It doesn’t come.
  EXPRESSION: Horrified
- CHARACTER: Narrator
  LINE: Samuel eyes bulge. He takes both hands and with great effort places them on his mother’s cheeks. He strokes his mother’s face, full of love, trying to get her to stop.
  EXPRESSION: Loving
- CHARACTER: Narrator
  LINE: It’s heart wrenching. Something snaps in Amelia. Her body shakes violently. Black tears rolling down her face.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: She throws Samuel away from her, screaming out as she sends him sliding halfway across the room.
  EXPRESSION: Releasing
- CHARACTER: Narrator
  LINE: Amelia gets up on all fours, shaking her head from side to side. The movement becomes so quick, so surreal, that her head becomes a violent, screaming blur.
  EXPRESSION: Agitated
- CHARACTER: Narrator
  LINE: Samuel calls out to his mother, desperate and frightened.
  EXPRESSION: Frightened
- CHARACTER: Narrator
  LINE: After a time, Amelia’s head movements slow down. Then finally, they stop. A long pause.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Amelia suddenly and forcefully vomits up a black substance.
  EXPRESSION: Expelling
- CHARACTER: Narrator
  LINE: It hits the floor urgently. Samuel watches on, speechless.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: It’s horrible, disturbing.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Just as soon as it started, it stops. Amelia falls face forward and lies dead still, her eyes open and staring.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Samuel runs to her. Desperate, he grabs her shirt, pulling her up, her head falls back. He hits her hard on the chest, as hard as he possibly can, over and over.
  EXPRESSION: Desperate
- CHARACTER: Narrator
  LINE: Amelia inhales like a drowning person coming up for air. She lets out a cry, a human cry this time, full of pain.
  EXPRESSION: Pained
- CHARACTER: Narrator
  LINE: Samuel wipes her face and kisses her cheek, grateful she’s alive.
  EXPRESSION: Relieved
- CHARACTER: Narrator
  LINE: Amelia looks around completely disoriented.
  EXPRESSION: Disoriented

::PATHS::
- CHOICE: "Exit basement"
  TARGET: lounge_room
  STATE_CHANGE: amelia_recovering = true, samuel_traumatized = true
  CONDITION: null

::SCENE::
LOCATION: Lounge Room
MOOD: Uneasy, Ominous
CHARACTERS: Amelia, Samuel
BACKGROUND_IMAGE: lounge_room.png
BACKGROUND_EDIT: "Dimly lit lounge room, night, silent"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Amelia limps through the basement door holding her son’s hand, slowly coming out of her trance like state. They stand there shell shocked. The house is silent.
  EXPRESSION: Recovering
- CHARACTER: Narrator
  LINE: A low rumbling starts up. Samuel looks all around him, then to his mum. She looks at him, unnerved.
  EXPRESSION: null
- CHARACTER: Samuel
  LINE: ‘If it’s in a word, or it’s in a look, you can’t get rid of the Babadook.’
  EXPRESSION: Reciting
- CHARACTER: Narrator
  LINE: Without warning Samuel’s body is suddenly ripped from her arms. An unseen force drags him up the stairs, his body bouncing as he hollers for his life.
  EXPRESSION: Terrified
- CHARACTER: Narrator
  LINE: Amelia screams as she watches him disappear out of sight.
  EXPRESSION: Screaming

::PATHS::
- CHOICE: "Follow Samuel"
  TARGET: amelia_s_room
  STATE_CHANGE: amelia_desperate = true, samuel_in_danger = true
  CONDITION: null

::SCENE::
LOCATION: Stairwell / Amelia's Room
MOOD: Frantic, Violent, Desperate
CHARACTERS: Amelia, Samuel
BACKGROUND_IMAGE: amelia_s_room.png
BACKGROUND_EDIT: "Dark stairwell leading to Amelia's room, night, violent struggle"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Amelia races up the stairs as fast as she can.
  EXPRESSION: Frantic
- CHARACTER: Narrator
  LINE: She arrives at the door.
  EXPRESSION: Frantic
- CHARACTER: Narrator
  LINE: Sam is standing by her bed, his arms rigid. He is picked up and flung against the wall. A sickening thud, he looks like a broken doll. Amelia screams.
  EXPRESSION: Frightened
- CHARACTER: Narrator
  LINE: She races to Sam, grabs hold of his arms. They’re ripped out of her grasp. Sam hits the wall again and again. It’s brutal, he starts to lose consciousness.
  EXPRESSION: Desperate
- CHARACTER: Narrator
  LINE: Amelia grabs Sam’s leg, then locks her arms round his waist.
  EXPRESSION: Protecting
- CHARACTER: Narrator
  LINE: She uses all her strength to push him onto the bed, covering him with her body, gripping the edges so she doesn’t fly up against the wall.
  EXPRESSION: Protecting

::PATHS::
- CHOICE: "Protect Samuel"
  TARGET: end_of_excerpt
  STATE_CHANGE: amelia_fighting_babadook = true, samuel_protected = true
  CONDITION: null

::SCENE::
LOCATION: Amelia's Bedroom
MOOD: Terror, Confrontation, Grief, Rage
CHARACTERS: Amelia, Samuel, Oskar, Babadook (shadow/figure)
BACKGROUND_IMAGE: bedroom_night.png
BACKGROUND_EDIT: "Dark, chaotic, shaking room with intense supernatural activity"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The bed starts to shake violently. A rumbling sound throughout the room.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Amelia stares off into the shadows, acknowledging this thing as real for the very first time.
  EXPRESSION: Afraid
- CHARACTER: Amelia
  LINE: What do you want!
  EXPRESSION: Desperate
- CHARACTER: Narrator
  LINE: The bed lifts up then slams down violently with them on it.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Amelia holds on tighter, Samuel clings to her.
  EXPRESSION: Afraid
- CHARACTER: Amelia
  LINE: TELL ME WHAT YOU WANT!!
  EXPRESSION: Desperate
- CHARACTER: Narrator
  LINE: The bed drops to the floor. The sound stops, replaced by an eerie calm. Sam hides his face in the mattress.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The door creaks open. A figure steps into the light, Amelia stands up on the bed to see who it is. Sam grabs her waist, hides his face in her skirt.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: It’s Oskar. A look of dread passes over Amelia’s face.
  EXPRESSION: Afraid
- CHARACTER: Amelia
  LINE: NO...
  EXPRESSION: Afraid
- CHARACTER: Oskar
  LINE: Keep breathing..
  EXPRESSION: Calm
- CHARACTER: Narrator
  LINE: A very faint rumble starts up again. Amelia can’t take her eyes from her husband, her panic becomes visible.
  EXPRESSION: Afraid
- CHARACTER: Oskar
  LINE: Put your seat back sweetheart. Ten more minutes and we’re there.
  EXPRESSION: Calm
- CHARACTER: Amelia
  LINE: NO...
  EXPRESSION: Afraid
- CHARACTER: Narrator
  LINE: Amelia shakes, tears forming. The rumbling intensifies.
  EXPRESSION: Afraid
- CHARACTER: Oskar
  LINE: I think it’s going to rain.
  EXPRESSION: Calm
- CHARACTER: Narrator
  LINE: Oskar is oblivious to the noise building around him.
  EXPRESSION: null
- CHARACTER: Amelia
  LINE: STOP!!
  EXPRESSION: Desperate
- CHARACTER: Narrator
  LINE: Truck tyres skid, brakes screech, horns blaring.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: A hot, white light shines in Oskar’s face, blinding him. The screeching sound becomes deafening.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Amelia watches as the top half of her husband’s head is severed, from the ear on one side to the jaw on the other.
  EXPRESSION: Terrified
- CHARACTER: Narrator
  LINE: His corpse quickly drops to the floor.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Amelia stares at it, her body shakes uncontrollably, tears run down her face. She cries out as if she’s being murdered, an unimaginable grief.
  EXPRESSION: Grieving
- CHARACTER: Narrator
  LINE: A sound starts up, taunting her. ‘Babababababa dook-dook-dook.’
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Amelia watches the corpse suddenly pulled back, swallowed up by the shadows as if it was never there. She searches the dark but can only see a formless shape lurking there.
  EXPRESSION: Afraid
- CHARACTER: Narrator
  LINE: Her grief and pain transforms into anger. She spits the words out, trembling, hardly able to breathe.
  EXPRESSION: Angry
- CHARACTER: Amelia
  LINE: You....are....nothing.
  EXPRESSION: Angry
- CHARACTER: Narrator
  LINE: The hideous growling grows more threatening with her words.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Her energy rises visibly. A pure, white hot rage.
  EXPRESSION: Angry
- CHARACTER: Amelia
  LINE: YOU’RE NOTHING!
  EXPRESSION: Angry
- CHARACTER: Narrator
  LINE: The hideous shadow grows larger, rising up to the ceiling, terrorizing her. The floors and walls shake.
  EXPRESSION: null
- CHARACTER: Amelia
  LINE: This is MY HOUSE! You are trespassing in MY HOUSE!
  EXPRESSION: Angry
- CHARACTER: Narrator
  LINE: Its growls turn to a deafening roar as the shadow touches the ceiling, a huge mass of black terror.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Amelia fights a sickening, gut wrenching fear as she finally faces up to this thing.
  EXPRESSION: Afraid
- CHARACTER: Amelia
  LINE: If you touch my son again, I’ll fucking KILL YOU!
  EXPRESSION: Angry
- CHARACTER: Narrator
  LINE: Bits of the ceiling fall to the floor. The walls crack.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Sam’s body is flipped up and pulled violently towards the shadows. He yells.
  EXPRESSION: Afraid
- CHARACTER: Narrator
  LINE: Amelia grabs him by the hands and yanks him to her, there’s no way she’s letting go this time. Sam wraps around her waist, she holds him tight.
  EXPRESSION: Determined
- CHARACTER: Narrator
  LINE: The sound of the Babadook is deafening. Its presence takes over the room.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Amelia jumps up on the bed end, her son in her arms, and lets out a scream so strong, so piercing, it smashes every window in the room. She looks utterly fierce. A mother enraged, protecting her son.
  EXPRESSION: Angry
- CHARACTER: Narrator
  LINE: Her scream dies away, but her eyes are full of life. She searches the darkness.
  EXPRESSION: Determined
- CHARACTER: Narrator
  LINE: The huge shadow shrinks down from the ceiling, its growls reduce to a hideous moan. The shadow is slowly and completely lost to the darkness.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The noise of the Babadook stops altogether.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Amelia stands tall on the bed end, searching the shadows, holding her breath.
  EXPRESSION: Determined
- CHARACTER: Narrator
  LINE: An unbearable silence.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The outward figure of the Babadook, just like the one in the picture book only life size, rolls in to the edge of the shadows. It looks absurd, creepy, its black arms stretched out like a scarecrow. Amelia holds her breath, waiting for something to happen. The ‘figure’ suddenly drops to the ground like a sack. Amelia starts. It collapses into a shapeless mound of hat and coat with nothing underneath. Amelia slides down to the floor, staring at it, dumbfounded. Sam jumps on the mattress, face down. A moaning sound starts up under the coat. Hellish, but somehow sad. Amelia inches in to look, her face softens.
  EXPRESSION: Afraid
- CHARACTER: Samuel
  LINE: Mum, don’t...
  EXPRESSION: Scared
- CHARACTER: Narrator
  LINE: Amelia comes in really close now, reaching out to touch the coat, checking if it’s real. The Babadook POV. It rises from under the coat up to the ceiling, towering over Amelia, then screeches right down to her face. We don’t see it but she does. It blows the skin back on her face, her eyes widen, her mouth is forced open in a grimace. Just like mask of the Babadook. And as quick as it appeared, that thing is out of there.
  EXPRESSION: Terrified
- CHARACTER: Narrator
  LINE: The Babadook’s POV flying out the door, Amelia and Sam are left behind.
  EXPRESSION: null

::PATHS::
- CHOICE: "Follow the Babadook downstairs"
  TARGET: lounge_room_night
  STATE_CHANGE: fear = -5, anger = -5, determination = +5
  CONDITION: null

::SCENE::
LOCATION: Lounge Room
MOOD: Relief, Trauma, Love
CHARACTERS: Amelia, Samuel
BACKGROUND_IMAGE: lounge_room_night.png
BACKGROUND_EDIT: "Nighttime, dark and disheveled lounge room, basement door visible"

::SCRIPT::
- CHARACTER: Narrator
  LINE: By the time Amelia makes it downstairs, the Babadook has disappeared into the basement, door slamming. She runs over to it, locks the door, takes the key.
  EXPRESSION: Relieved
- CHARACTER: Narrator
  LINE: Amelia turns. Sam stands opposite her. He cries, then howls, completely overwhelmed, his body shaking.
  EXPRESSION: Afraid
- CHARACTER: Narrator
  LINE: Amelia races to him, scoops him up. Samuel clings to her for dear life. She strokes his head, kisses his face, holding him as tight as she can.
  EXPRESSION: Loving
- CHARACTER: Narrator
  LINE: She takes him to the couch, cradles him in her arms and soothes him with her words. Full of a mother’s love.
  EXPRESSION: Loving
- CHARACTER: Narrator
  LINE: They stay there like that for a long time together.
  EXPRESSION: null

::PATHS::
- CHOICE: "Rest and recover with Samuel"
  TARGET: mrs_roach_front_yard_day
  STATE_CHANGE: healing = +10, bond_amelia_samuel = +10
  CONDITION: null

::SCENE::
LOCATION: Mrs. Roach's Front Yard
MOOD: Hopeful, Calm
CHARACTERS: Amelia, Samuel, Mrs. Roach
BACKGROUND_IMAGE: suburban_yard_day.png
BACKGROUND_EDIT: "Daytime, sunny, tidy front yard with house steps"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Sam looks through a window. He has his best clothes on, looking adorable. He sees something, his face lights up.
  EXPRESSION: Happy
- CHARACTER: Narrator
  LINE: The front door opens. Sam guides Mrs Roach down the steps, then lets go of her hand and runs to mum.
  EXPRESSION: Happy
- CHARACTER: Narrator
  LINE: Amelia scoops Sam up in her arms. She looks different. Stronger. Her eyes more relaxed and alive.
  EXPRESSION: Calm
- CHARACTER: Mrs. Roach
  LINE: Watch your mum’s leg little one.
  EXPRESSION: Concerned
- CHARACTER: Amelia
  LINE: He’s fine. I’ve had the stitches out.
  EXPRESSION: Calm
- CHARACTER: Mrs. Roach
  LINE: You’ll have to be more careful around the home. It can be a death trap.
  EXPRESSION: Concerned
- CHARACTER: Amelia
  LINE: I know.
  EXPRESSION: Calm
- CHARACTER: Mrs. Roach
  LINE: What time’s the party?
  EXPRESSION: Curious
- CHARACTER: Amelia
  LINE: Anytime after 3 is fine. Just going to have a bit of real food first, before the sugar onslaught starts.
  EXPRESSION: Calm
- CHARACTER: Narrator
  LINE: Samuel snuggles into her. She hugs him back.
  EXPRESSION: Loving
- CHARACTER: Mrs. Roach
  LINE: See you in a few hours then.
  EXPRESSION: Friendly
- CHARACTER: Narrator
  LINE: Mrs Roach gives them a sweet nana wave. They wave back.
  EXPRESSION: Friendly

::PATHS::
- CHOICE: "Prepare for the party inside"
  TARGET: lounge_room_day
  STATE_CHANGE: party_preparation = true
  CONDITION: null

::SCENE::
LOCATION: Lounge Room
MOOD: Reflective, Cautiously Optimistic
CHARACTERS: Amelia, Samuel, Prue, Warren
BACKGROUND_IMAGE: lounge_room_day.png
BACKGROUND_EDIT: "Daytime, tidy but run-down lounge, birthday decorations"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The lounge room is still run down, but tidy and clean. There are homemade birthday decorations strung up.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Amelia and Samuel sit on the couch, side by side.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The couple from Social Services sit opposite, cups of tea in hand. Amelia is much more grounded in their presence.
  EXPRESSION: Calm
- CHARACTER: Prue
  LINE: That school’s a good choice.
  EXPRESSION: Approving
- CHARACTER: Amelia
  LINE: I’ve done a lot of reading about it so.. I think Sam’ll be happy there.
  EXPRESSION: Calm
- CHARACTER: Warren
  LINE: He’s been away from school over two weeks now. Time to get
  EXPRESSION: Stiff

::PATHS::
- CHOICE: "Continue the discussion"
  TARGET: end
  STATE_CHANGE: social_services_meeting = complete
  CONDITION: null

::SCENE::
LOCATION: Living Room
MOOD: Tense
CHARACTERS: Amelia, Samuel, Prue, Welfare Man
BACKGROUND_IMAGE: living_room.png
BACKGROUND_EDIT: "Daytime, domestic setting, a sense of underlying tension."

::SCRIPT::
- CHARACTER: Amelia
  LINE: We needed time to sort things out.
  EXPRESSION: Strong
- CHARACTER: Narrator
  LINE: Samuel nestles into his mum. Prue smiles tightly.
  EXPRESSION: null
- CHARACTER: Prue
  LINE: Are you having a party?
  EXPRESSION: Neutral
- CHARACTER: Amelia
  LINE: It’s Sam’s birthday today. We’re having a small thing, just a few friends.
  EXPRESSION: Neutral
- CHARACTER: Samuel
  LINE: The first birthday I’ve ever celebrated.
  EXPRESSION: Happy
- CHARACTER: Narrator
  LINE: The visitors look a little shocked.
  EXPRESSION: Surprised
- CHARACTER: Amelia
  LINE: That’s not true!
  EXPRESSION: Defensive
- CHARACTER: Samuel
  LINE: Yes it is mum. My first party on the day.
  EXPRESSION: Matter-of-fact
- CHARACTER: Prue
  LINE: That’s unusual.
  EXPRESSION: Pointed
- CHARACTER: Narrator
  LINE: Amelia can see the judgement in the woman’s eyes. She decides not to let it go.
  EXPRESSION: null
- CHARACTER: Amelia
  LINE: My husband died the day that Sam was born.
  EXPRESSION: Calm
- CHARACTER: Narrator
  LINE: The DOCs couple don’t know how to respond.
  EXPRESSION: null
- CHARACTER: Samuel
  LINE: He got killed driving mum to the hospital to have me.
  EXPRESSION: Matter-of-fact
- CHARACTER: Narrator
  LINE: Amelia doesn’t rush in to rescue them. The woman mouths the word ‘oh’. The man is completely out of his depth, just staring blankly at them.
  EXPRESSION: null
- CHARACTER: Amelia
  LINE: Sam’s just like his dad was, always speaks his mind.
  EXPRESSION: Neutral
- CHARACTER: Narrator
  LINE: Sam is snuggled right in to his mum, protected.
  EXPRESSION: null
- CHARACTER: Welfare Woman
  LINE: Birthday parties are always fun, especially when they’re yours.
  EXPRESSION: Polite
- CHARACTER: Samuel
  LINE: My cousin was going to come but she’s scared of me because I knocked her front tooth out.
  EXPRESSION: Casual
- CHARACTER: Narrator
  LINE: Amelia looks to DOCs, a half smile plays on her lips. She looks beautiful. Prue looks awkward, her cup slipping on the saucer.
  EXPRESSION: null
- CHARACTER: Amelia
  LINE: I’ll take that for you.
  EXPRESSION: Courteous

::PATHS::
- CHOICE: "End the conversation"
  TARGET: garden_bugsy
  STATE_CHANGE: judgment = +1, Amelia_resilience = +1
  CONDITION: null

::SCENE::
LOCATION: Garden
MOOD: Macabre
CHARACTERS: Narrator, Amelia, Samuel, Bugsy (corpse)
BACKGROUND_IMAGE: garden.png
BACKGROUND_EDIT: "Daytime, lush garden, rose bush, target painted on fence."

::SCRIPT::
- CHARACTER: Narrator
  LINE: A cross section of soil. Bugsy’s corpse buried there. The flesh begins to rot. Worms and bugs crawl through it.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Travelling up to the roots of a plant bursting out of the earth. A rose bush. Amelia’s tends to the soil around it.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: She admires a single black rose in full bloom.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Samuel is nearby, opposite the fence. There’s a target painted on it. He has two home made ‘nail guns’ on either leg. He aims then fires them off in quick succession.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Amelia looks up. The nails hit their mark.
  EXPRESSION: null
- CHARACTER: Amelia
  LINE: Good shot!
  EXPRESSION: Praising
- CHARACTER: Narrator
  LINE: Samuel looks pleased. He runs over to her.
  EXPRESSION: null
- CHARACTER: Samuel
  LINE: I’m protecting you mum.
  EXPRESSION: Determined
- CHARACTER: Amelia
  LINE: You’re doing such a good job.
  EXPRESSION: Genuine
- CHARACTER: Narrator
  LINE: He runs back to his target, full of beans, firing up again.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Amelia picks up another worm and adds it to a bowl full of them. She takes off her gloves and gets up.
  EXPRESSION: null

::PATHS::
- CHOICE: "Go to the basement door"
  TARGET: basement_door
  STATE_CHANGE: samuel_proud = true, amelia_focused = true
  CONDITION: null

::SCENE::
LOCATION: Basement Door
MOOD: Tense
CHARACTERS: Narrator, Amelia, Samuel
BACKGROUND_IMAGE: basement_door.png
BACKGROUND_EDIT: "Daytime, interior, a heavily bolted basement door."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Amelia is at the door which now has many bolts on it. She undoes them all as Samuel watches. She goes over to where she’s put down the bowl of sludge and worms, picks it up.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Sam keeps one eye on her as he tentatively sneaks one foot into the basement. She turns around and sees him.
  EXPRESSION: null
- CHARACTER: Amelia
  LINE: UH UH UH! NO!
  EXPRESSION: Fierce
- CHARACTER: Narrator
  LINE: He stops in his tracks.
  EXPRESSION: null
- CHARACTER: Amelia
  LINE: It’s not a game, Sam.
  EXPRESSION: Serious
- CHARACTER: Narrator
  LINE: Amelia crouches down to Sam’s level, patient and loving.
  EXPRESSION: null
- CHARACTER: Amelia
  LINE: One day, when you’re a bit bigger. You keep working on your weapons...
  EXPRESSION: Gentle
- CHARACTER: Narrator
  LINE: Samuel silently accepts what she’s offering. For now.
  EXPRESSION: null
- CHARACTER: Amelia
  LINE: Go right out into the yard and stay there till I call you, alright?
  EXPRESSION: Firm
- CHARACTER: Narrator
  LINE: He nods and runs outside.
  EXPRESSION: null

::PATHS::
- CHOICE: "Enter the basement"
  TARGET: basement_confrontation
  STATE_CHANGE: samuel_safe = true, amelia_resolved = true
  CONDITION: null

::SCENE::
LOCATION: Basement
MOOD: Terrifying
CHARACTERS: Narrator, Amelia, The Babadook (unseen)
BACKGROUND_IMAGE: basement.png
BACKGROUND_EDIT: "Daytime, dark and rumbling basement, Oskar's things neatly stacked."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Amelia descends the stairs. It’s dark and hard to see. A very faint rumbling starts up.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The room is clearer than before. Oskar’s things are still there, but now very neatly stacked in one corner.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Amelia places the bowl of slop in the centre of the room. She steps back and waits, peering into the darkness. She’s frightened, but does her best to conceal it.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The rumbling increases. She can see a familiar shadow in the corner, moving ever so slightly. A low insect like noise. She braces herself, peering in to try and see it.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: A sound behind her. The back of Amelia’s head as she turns around, her eyes widening.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Amelia is knocked off balance then twisted and bent backwards. Her arms grab at the air to try and right herself.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: She grunts and groans, her face is forced to one side. The sounds around her are horrible, threatening.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Amelia seen from above. She is bent right back as she forces her head to look up. She lets out a low guttural warning sound, then a shout, full of power..
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Her back releases slightly, she is able to right herself, standing eye to eye with something we don’t see. Her face is tense, her pupils dilate. She looks afraid but something else is there now. Something soft and sad.
  EXPRESSION: null
- CHARACTER: Amelia
  LINE: Ssh.. Ssh... It’s alright, it’s alright.. Ssh.....
  EXPRESSION: Tender
- CHARACTER: Narrator
  LINE: She stays there awhile. Her breathing is laboured, her pupils now huge and black. A tortured moan off screen. She continues to soothe and reassure it, undeterred.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Time stretches. A moment of peace.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Amelia’s eyes return to normal. The POV falls away from her, dropping to the floor. Amelia stands over it.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The bowl of slop there on the floor untouched. Nothing else can be seen in the room.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: In one quick move the bowl is sucked into the darkness.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Amelia walks backwards to the stairs. She turns and climbs them as quick as she can without running.
  EXPRESSION: null

::PATHS::
- CHOICE: "Exit the basement"
  TARGET: garden_birthday
  STATE_CHANGE: babadook_contained = true, amelia_bravery = +1
  CONDITION: null

::SCENE::
LOCATION: Garden
MOOD: Loving
CHARACTERS: Narrator, Amelia, Samuel
BACKGROUND_IMAGE: garden.png
BACKGROUND_EDIT: "Daytime, serene garden setting, Amelia and Samuel together."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Amelia carries a tray filled with sandwiches. She sets it down in front of Samuel. He has his magician’s outfit on.
  EXPRESSION: null
- CHARACTER: Samuel
  LINE: How was the Babadook?
  EXPRESSION: Curious
- CHARACTER: Amelia
  LINE: Pretty quiet today.
  EXPRESSION: Calm
- CHARACTER: Narrator
  LINE: Amelia reaches up and undoes his top collar, inspecting the bruises on his neck. She can’t hide her shame.
  EXPRESSION: null
- CHARACTER: Samuel
  LINE: It’s much better mummy..
  EXPRESSION: Gentle
- CHARACTER: Narrator
  LINE: She brings her hand up to stroke his cheek, looking at him with love. She puts a sandwich on Sam’s plate.
  EXPRESSION: null
- CHARACTER: Samuel
  LINE: Wait! I’ve got a new trick..
  EXPRESSION: Excited
- CHARACTER: Narrator
  LINE: He runs to get a silver dome off the ground, races back and plonks it on the table.
  EXPRESSION: null
- CHARACTER: Samuel
  LINE: Life is not always as it seems! Nothing in my hands, nothing in my hands.
  EXPRESSION: Playful
- CHARACTER: Narrator
  LINE: He makes something appear in his palm, it’s a coin.
  EXPRESSION: null
- CHARACTER: Amelia
  LINE: Very good!
  EXPRESSION: Impressed
- CHARACTER: Samuel
  LINE: Wait! I haven’t finished..
  EXPRESSION: Eager
- CHARACTER: Narrator
  LINE: Amelia watches on, intrigued.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Samuel places the dome over the coin. He grabs a spoon and taps it on the top for special effect. He whips the lid off and underneath is a bird. A real, live bird.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Amelia laughs with surprise.
  EXPRESSION: null
- CHARACTER: Amelia
  LINE: How did you do that!
  EXPRESSION: Shocked
- CHARACTER: Narrator
  LINE: The bird flaps around on the table. Samuel does an impromptu jig around his mum, very pleased with himself.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: She laughs, enjoying his dance. She tries to grab hold of his arm. He wriggles free, happy, laughing.
  EXPRESSION: null
- CHARACTER: Amelia
  LINE: Come here...
  EXPRESSION: Affectionate
- CHARACTER: Narrator
  LINE: Amelia finally catches his arm, drawing him to her. She hugs him and puts him on her lap. He stops wriggling around and settles in, relishing his mother’s love.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: A quiet beautiful moment, neither of them say a thing. Amelia rubs her son’s back, he snuggles into her.
  EXPRESSION: null
- CHARACTER: Amelia
  LINE: Happy birthday sweetheart.
  EXPRESSION: Quiet
- CHARACTER: Narrator
  LINE: Sam breaks into a smile. He closes his eyes and leans into his mother, his face beaming.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: THE END
  EXPRESSION: null

::PATHS::
- CHOICE: "The story concludes"
  TARGET: end
  STATE_CHANGE: peace = true, love = true, resolution = true
  CONDITION: null

