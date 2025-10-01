::SCENE::
LOCATION: Black
MOOD: Ominous
CHARACTERS: Narrator
BACKGROUND_IMAGE: black.png
BACKGROUND_EDIT: "Fade in from black"

::SCRIPT::
- CHARACTER: Narrator
  LINE: GET OUT
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Written by
  EXPRESSION: null
- CHARACTER: Barry Luc
  LINE: Barry Luc
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Based on, If Any
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Address (412) 312-3111
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: I appeal to you therefore, brothers, by the mercies of God, to present your bodies as a living sacrifice, holy and acceptable to God, which is your spiritual worship. Do not be conformed to this world, but be transformed by the renewal of your mind, that by testing you may discern what is the will of God, what is good and acceptable and perfect. -Romans 12:1-2
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue"
  TARGET: shaw_house_exterior
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: The Shaw's House - Front Lawn
MOOD: Peaceful
CHARACTERS: Narrator, Richard, Nancy, Joshua, May
BACKGROUND_IMAGE: shaw_house_exterior.png
BACKGROUND_EDIT: "Nighttime, a perfect suburban house with bay windows and a front lawn. The Shaw family eating dinner inside."

::SCRIPT::
- CHARACTER: Narrator
  LINE: A perfect suburban house with bay windows and a front lawn. The SHAW family. Caucasian and warm - RICHARD, 34; NANCY, 30; JOSHUA, 6; and MAY, 4 - eat dinner inside. Richard reads something on his tablet illuminating his face.
  EXPRESSION: null
- CHARACTER: Joshua
  LINE: Which one are we going to?
  EXPRESSION: Curious
- CHARACTER: Richard
  LINE: The one in Orlando.
  EXPRESSION: Casual
- CHARACTER: Nancy
  LINE: Disney World.
  EXPRESSION: Excited
- CHARACTER: Joshua
  LINE: Tony said that Mickey is not really Mickey; it’s someone else in there.
  EXPRESSION: Skeptical
- CHARACTER: Richard
  LINE: Mickey’s Mickey.
  EXPRESSION: Dismissive

::PATHS::
- CHOICE: "Continue"
  TARGET: suburban_street_night
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Suburban Street
MOOD: Normal
CHARACTERS: Narrator, Andre
BACKGROUND_IMAGE: suburban_street_night.png
BACKGROUND_EDIT: "Nighttime, an African-American man running down the sidewalk in sweats, listening to jazz on his phone."

::SCRIPT::
- CHARACTER: Narrator
  LINE: ANDRE, 29, an African-American man runs down the sidewalk in sweats. He listens to jazz on his phone. The music stops. He stops running and checks his phone.
  EXPRESSION: null
- CHARACTER: Andre
  LINE: Damn.
  EXPRESSION: Annoyed
- CHARACTER: Narrator
  LINE: He’s right in front of the Shaw’s house. He glances inside. The Shaw’s seem normal and content. Andre smiles.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: A motion detecting security light floods the lawn.
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue"
  TARGET: shaw_house_dining_room
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: The Shaw's House - Dining Room
MOOD: Observing
CHARACTERS: Narrator, Richard, Nancy, May, Joshua, Andre
BACKGROUND_IMAGE: shaw_house_dining_room.png
BACKGROUND_EDIT: "Continuous, Richard looks up from his table to see Andre standing there. The rest of the family doesn’t notice. Nancy tends to May, who squirms in her chair. Richard watches Andre protectively."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Richard looks up from his table to see Andre standing there. The rest of the family doesn’t notice. Nancy tends to May, who SQUIRMS in her chair. Richard watches Andre protectively.
  EXPRESSION: null
- CHARACTER: Joshua
  LINE: Also, Tony said he saw a chef Mickey and a normal Mickey.
  EXPRESSION: Curious
- CHARACTER: Nancy
  LINE: He must have changed his clothes for work.
  EXPRESSION: Explaining

::PATHS::
- CHOICE: "Continue"
  TARGET: suburban_street_continuous
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Suburban Street
MOOD: Uneasy
CHARACTERS: Narrator, Andre
BACKGROUND_IMAGE: suburban_street_continuous.png
BACKGROUND_EDIT: "Continuous, Andre walks on. It’s getting dark. He is suddenly very alone. A vintage creme-colored Porsche Boxter with tinted windows and a roof creeps up on the street behind Andre. It’s following him."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Andre walks on. It’s getting dark. He is suddenly very alone.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: A vintage creme-colored Porsche Boxter with tinted windows and a roof CREEPS up on the street behind Andre. It’s following him.
  EXPRESSION: Ominous

::PATHS::
- CHOICE: "Continue"
  TARGET: sports_car_interior
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Sports Car
MOOD: Mysterious
CHARACTERS: Narrator, Tutorial
BACKGROUND_IMAGE: sports_car_interior.png
BACKGROUND_EDIT: "Continuous, Driver’s POV watching Andre. His breath echoes deep and tinny as if it were into a coffee can. Through the car’s system we hear an English to French language tutorial recording."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Driver’s POV watching Andre. His BREATH ECHOES deep and tinny as if it were into a coffee can. Through the car’s system we hear an English to French language tutorial recording.
  EXPRESSION: null
- CHARACTER: Tutorial
  LINE: Pardon me. Where is the nearest restaurant? Pardonnez-moi. Ou est le restaurant le plus proche?
  EXPRESSION: Neutral
- CHARACTER: Narrator
  LINE: The driver doesn’t repeat.
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue"
  TARGET: suburban_street_continuous_2
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Suburban Street
MOOD: Suspicious
CHARACTERS: Narrator, Andre
BACKGROUND_IMAGE: suburban_street_continuous_2.png
BACKGROUND_EDIT: "Continuous, Andre, feeling followed, stops to tie his shoe. The car also stops. Andre waves at the unseen DRIVER. There is no response. The ENGINE PURRS. Andre begins walking again. The car begins slowly too. Andre stops again. The car does too. Andre peers through the windshield but can’t see through the tint."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Andre, feeling followed, stops to tie his shoe. The car also stops. Andre waves at the unseen DRIVER. There is no response. The ENGINE PURRS.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Andre begins walking again. The car begins slowly too. Andre stops again. The car does too. Andre peers through the windshield but can’t see through the tint.
  EXPRESSION: null
- CHARACTER: Andre
  LINE: Can I help you...?
  EXPRESSION: Inquisitive
- CHARACTER: Narrator
  LINE: No response.
  EXPRESSION: null
- CHARACTER: Andre
  LINE: I’m new to the area. I just moved here... Down on Evergreen...
  EXPRESSION: Explaining
- CHARACTER: Narrator
  LINE: Nothing. Did I do something wrong? ’Cause--
  EXPRESSION: Confused

::PATHS::
- CHOICE: "Continue"
  TARGET: sports_car_interior_2
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Sports Car
MOOD: Aloof
CHARACTERS: Narrator, Tutorial
BACKGROUND_IMAGE: sports_car_interior_2.png
BACKGROUND_EDIT: "Continuous, Driver’s POV. Andre continues to talk, but isn’t heard."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Driver’s POV. Andre continues to talk, but isn’t heard.
  EXPRESSION: null
- CHARACTER: Tutorial
  LINE: Can you show me the nearest bathroom? Pouvez-vous me montrer la salle de bain la plus prouche?
  EXPRESSION: Neutral

::PATHS::
- CHOICE: "Continue"
  TARGET: suburban_street_continuous_3
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Suburban Street
MOOD: Aggravated
CHARACTERS: Narrator, Andre
BACKGROUND_IMAGE: suburban_street_continuous_3.png
BACKGROUND_EDIT: "Continuous, Andre hears nothing from inside. Andre begins walking. The car creeps alongside him. After a few steps, Andre stops again. The car stops. Andre laughs. Wait a minute. I know you? You messing with me right?..Come on. No response. He realizes it’s not a friend. You know this could be considered stalking and harassment. Plus, you’re sitting in a deadly weapon so that’s some felony-type shit right there. No response. What?!? Say something then. No response. Andre can’t hide his anger anymore. He starts walking the other direction. The car backs up, following Andre in reverse. Calm down, Andre. Don’t do it. Don’t let him get to you. After a few more steps... Fuck."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Andre hears nothing from inside.
  EXPRESSION: null
- CHARACTER: Andre
  LINE: This is some shit right here.
  EXPRESSION: Angry
- CHARACTER: Narrator
  LINE: Andre begins walking. The car creeps alongside him. After a few steps, Andre stops again. The car stops. Andre laughs.
  EXPRESSION: null
- CHARACTER: Andre
  LINE: Wait a minute. I know you? You messing with me right?..Come on.
  EXPRESSION: Challenging
- CHARACTER: Narrator
  LINE: No response. He realizes it’s not a friend.
  EXPRESSION: null
- CHARACTER: Andre
  LINE: You know this could be considered stalking and harassment. Plus, you’re sitting in a deadly weapon so that’s some felony-type shit right there.
  EXPRESSION: Threatening
- CHARACTER: Narrator
  LINE: No response.
  EXPRESSION: null
- CHARACTER: Andre
  LINE: What?!? Say something then.
  EXPRESSION: Demanding
- CHARACTER: Narrator
  LINE: No response. Andre can’t hide his anger anymore. He starts walking the other direction. The car backs up, following Andre in reverse.
  EXPRESSION: null
- CHARACTER: Andre
  LINE: Calm down, Andre. Don’t do it. Don’t let him get to you.
  EXPRESSION: Self-restraining
- CHARACTER: Narrator
  LINE: After a few more steps...
  EXPRESSION: null
- CHARACTER: Andre
  LINE: Fuck.
  EXPRESSION: Frustrated

::PATHS::
- CHOICE: "Continue"
  TARGET: suburban_street_continuous_4
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Suburban Street
MOOD: Confrontational
CHARACTERS: Narrator, Andre
BACKGROUND_IMAGE: suburban_street_continuous_4.png
BACKGROUND_EDIT: "Continuous, Andre, fed up, stops. He approaches the passenger’s side window and bangs on it. I’m from Brooklyn, man. If you wanna do something, then let’s do something. I’m ready..! Hey, I’m talkin’ to you!!!"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Andre, fed up, stops. He approaches the passenger’s side window and bangs on it.
  EXPRESSION: null
- CHARACTER: Andre
  LINE: I’m from Brooklyn, man. If you wanna do something, then let’s do something. I’m ready..! Hey, I’m talkin’ to you!!!
  EXPRESSION: Aggressive

::PATHS::
- CHOICE: "Continue"
  TARGET: sports_car_interior_3
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Sports Car
MOOD: Shocking
CHARACTERS: Narrator
BACKGROUND_IMAGE: sports_car_interior_3.png
BACKGROUND_EDIT: "Continuous, Driver’s POV. Andre bangs on the window."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Driver’s POV. Andre bangs on the window.
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue"
  TARGET: suburban_street_continuous_5
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Suburban Street
MOOD: Terrifying
CHARACTERS: Narrator, Andre, Driver
BACKGROUND_IMAGE: suburban_street_continuous_5.png
BACKGROUND_EDIT: "Continuous, Andre bangs harder on the window three times. The car’s passenger-side window rolls down. Can you help me find a hotel? Pouvez-vous m’aider a trouver mon hotel? Andre’s expression goes from anger to terror. The driver wears a tubular metal medieval knight’s helmet with slanted rectangular eye holes. Shit. The driver raises a gun with a silencer on it. Andre turns to run but is shot in the back. Stunned, Andre stumbles towards the Shaw’s house."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Andre bangs harder on the window three times. The car’s passenger-side window rolls down.
  EXPRESSION: null
- CHARACTER: Tutorial
  LINE: Can you help me find a hotel? Pouvez-vous m’aider a trouver mon hotel?
  EXPRESSION: Neutral
- CHARACTER: Narrator
  LINE: Andre’s expression goes from anger to terror. The driver wears a tubular metal medieval knight’s helmet with slanted rectangular eye holes.
  EXPRESSION: null
- CHARACTER: Andre
  LINE: Shit.
  EXPRESSION: Terrified
- CHARACTER: Narrator
  LINE: The driver raises a gun with a silencer on it. Andre turns to run but is shot in the back. Stunned, Andre stumbles towards the Shaw’s house.
  EXPRESSION: Violent

::PATHS::
- CHOICE: "Continue"
  TARGET: shaw_house_front_lawn_continuous
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: The Shaw's House - Front Lawn
MOOD: Desperate
CHARACTERS: Narrator, Andre, Driver
BACKGROUND_IMAGE: shaw_house_front_lawn_continuous.png
BACKGROUND_EDIT: "Continuous, Andre falls in front of the Shaw’s lawn. A dart sticks out of his back. He reaches towards the Shaw family. The masked driver approaches calmly Andre drags himself toward the house as everything blurs around him. Help. Andre passes out as the security light floods the lawn again."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Andre falls in front of the Shaw’s lawn. A dart sticks out of his back. He reaches towards the Shaw family. The masked driver approaches calmly Andre drags himself toward the house as everything blurs around him.
  EXPRESSION: null
- CHARACTER: Andre
  LINE: Help
  EXPRESSION: Weak

::PATHS::
- CHOICE: "End Scene"
  TARGET: end
  STATE_CHANGE: Andre_shot = true
  CONDITION: null

::SCENE::
LOCATION: The Shaw's House - Dining Room
MOOD: Unsettling
CHARACTERS: Narrator, Richard, Joshua, Andre, Driver
BACKGROUND_IMAGE: shaw_house_dining_room.png
BACKGROUND_EDIT: "Continuous. The Shaw family eats. Andre is limp on the front lawn."

::SCRIPT::
- CHARACTER: Narrator
  LINE: The Shaw family eats while Andre lays on their front lawn.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: This time Richard, buried in his tablet, doesn’t notice. the driver lift Andre’s limp body and carries him to his car.
  EXPRESSION: null
- CHARACTER: Joshua
  LINE: Tony said Mickey’s face doesn’t move.
  EXPRESSION: null
- CHARACTER: Richard
  LINE: That’s right. Mickey’s always happy.
  EXPRESSION: null

::PATHS::
- CHOICE: "Observe the driver"
  TARGET: suburban_street
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Suburban Street
MOOD: Sinister
CHARACTERS: Narrator, Joshua, Richard, Driver, Andre
BACKGROUND_IMAGE: suburban_street.png
BACKGROUND_EDIT: "Continuous. The driver carries Andre to the car."

::SCRIPT::
- CHARACTER: Narrator
  LINE: The driver carries Andre to the car.
  EXPRESSION: null
- CHARACTER: Joshua
  LINE: Why?
  EXPRESSION: null
- CHARACTER: Richard
  LINE: Because he hasn’t aged in 100 years.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The driver plops Andre in the padded trunk. He gets in his car and drives off.
  EXPRESSION: null

::SCENE::
TITLE_CARD: "Get Out"

::SCENE::
LOCATION: Brooklyn Park Slope
MOOD: Peaceful
CHARACTERS: Narrator
BACKGROUND_IMAGE: park_slope_dawn.png
BACKGROUND_EDIT: "Dawn. The sun rises over the city. Autumn. Beautiful."

::SCRIPT::
- CHARACTER: Narrator
  LINE: The sun rises over the city. Autumn. Beautiful.
  EXPRESSION: null

::SCENE::
LOCATION: Brooklyn Loft - Living Room
MOOD: Calm
CHARACTERS: Narrator
BACKGROUND_IMAGE: brooklyn_loft_living_room.png
BACKGROUND_EDIT: "Morning. We move slowly through the small but clean apartment. The walls are decorated with fascinating urban photography."

::SCRIPT::
- CHARACTER: Narrator
  LINE: We move slowly through the small but clean apartment. The walls are decorated with fascinating urban photography.
  EXPRESSION: null

::SCENE::
LOCATION: Brooklyn Loft - Bathroom
MOOD: Reflective
CHARACTERS: Narrator, Chris Washington
BACKGROUND_IMAGE: brooklyn_loft_bathroom.png
BACKGROUND_EDIT: "Morning. Chris Washington, 26, a handsome African-American man shuts the medicine cabinet. He’s shirtless and naturally athletic. He scrutinizes his reflection with a touch of vanity."

::SCRIPT::
- CHARACTER: Narrator
  LINE: CHRIS WASHINGTON, 26, a handsome African-American man shuts the medicine cabinet. He’s shirtless and naturally athletic. He scrutinizes his reflection with a touch of vanity.
  EXPRESSION: null

::SCENE::
LOCATION: Starbucks Counter
MOOD: Pleasant
CHARACTERS: Narrator, Rose Armitage
BACKGROUND_IMAGE: starbucks_counter.png
BACKGROUND_EDIT: "Morning. Rose Armitage, 28 - Caucasian, brunette with freckles - cool and beautiful like an old Summer Camp crush. Rose looks at pastries through the glass. She can’t help but smile."

::SCRIPT::
- CHARACTER: Narrator
  LINE: ROSE ARMITAGE, 28 - Caucasian, brunette with freckles - cool and beautiful like an old Summer Camp crush. Rose looks at pastries through the glass. She can’t help but smile.
  EXPRESSION: null

::SCENE::
LOCATION: Brooklyn Loft - Bathroom
MOOD: Casual
CHARACTERS: Narrator, Chris Washington
BACKGROUND_IMAGE: brooklyn_loft_bathroom.png
BACKGROUND_EDIT: "Morning. Chris spreads shaving cream onto his face and shaves. He postures a little then nicks himself on the neck. He smirks; deserved that."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Chris spreads shaving cream onto his face and shaves. He postures a little then nicks himself on the neck. He smirks; deserved that.
  EXPRESSION: null

::SCENE::
LOCATION: Brooklyn Loft - Living Room
MOOD: Creative
CHARACTERS: Narrator, Chris, Sid
BACKGROUND_IMAGE: brooklyn_loft_living_room.png
BACKGROUND_EDIT: "Morning. Chris, clothed, looks out his window through a professional camera. He flips through some striking urban images on the digital display much like the ones framed around his apartment. He is a very talented photographer. Sid, a small black dog, watches him. The BUZZER RINGS."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Chris, clothed, looks out his window through a professional camera. He flips through some striking urban images on the digital display much like the ones framed around his apartment. He is a very talented photographer.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Sid, a small black dog, watches him. The BUZZER RINGS.
  EXPRESSION: null

::SCENE::
LOCATION: Brooklyn Building - Hallway
MOOD: Welcoming
CHARACTERS: Narrator, Chris, Rose
BACKGROUND_IMAGE: brooklyn_building_hallway.png
BACKGROUND_EDIT: "Morning. Chris opens the door. Rose stands outside the apartment with her hands full. She has two coffees and two bags of pastries. Chris smirks."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Chris opens the door. Rose stands outside the apartment with her hands full. She has two coffees and two bags of pastries. Chris smirks.
  EXPRESSION: null
- CHARACTER: Rose
  LINE: I couldn’t decide...
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: He takes the coffee tray and pulls her inside. They kiss.
  EXPRESSION: null

::SCENE::
LOCATION: Brooklyn Loft - Living Room
MOOD: Domestic Bliss
CHARACTERS: Narrator, Rose, Chris, Sid
BACKGROUND_IMAGE: brooklyn_loft_living_room.png
BACKGROUND_EDIT: "Morning. Rose and Chris have coffee and sweets by the window. The small mound of pastries sits on the coffee table. Sid lays on her lap. She strokes him. It’s a perfect morning."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Rose and Chris have coffee and sweets by the window. The small mound of pastries sits on the coffee table. SID lays on her lap. She strokes him. It’s a perfect morning.
  EXPRESSION: null
- CHARACTER: Rose
  LINE: Poor thing. Do you even pet him?
  EXPRESSION: null
- CHARACTER: Chris
  LINE: Are you kidding me? When you’re not here that dog gets the best fuckin’ pets of his life.
  EXPRESSION: null
- CHARACTER: Rose
  LINE: So, how come whenever I come over, he acts like he’s been totally neglected.
  EXPRESSION: null
- CHARACTER: Chris
  LINE: ‘Cause he know he’s got you wrapped around his little paw.
  EXPRESSION: null
- CHARACTER: Rose
  LINE: oh, really?
  EXPRESSION: null
- CHARACTER: Chris
  LINE: Yeah.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Chris picks up her foot sweetly and massages it. She melts.
  EXPRESSION: null

::SCENE::
LOCATION: Brooklyn Loft - Chris' Bedroom
MOOD: Anticipation
CHARACTERS: Narrator, Chris, Rose
BACKGROUND_IMAGE: brooklyn_loft_chris_bedroom.png
BACKGROUND_EDIT: "Day. Chris packs a small bag of luggage. Rose lays on the bed."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Chris packs a small bag of luggage. Rose lays on the bed.
  EXPRESSION: null
- CHARACTER: Rose
  LINE: Toothbrush... Deodorant...
  EXPRESSION: null
- CHARACTER: Chris
  LINE: Check... Check....
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Chris puts a cigarette in his mouth. Rose pops up and grabs the cigarette from his mouth and breaks it. Chris tries to feign incredulousness but is amused.
  EXPRESSION: null
- CHARACTER: Chris
  LINE: I’m not gonna have one the whole weekend.
  EXPRESSION: null
- CHARACTER: Rose
  LINE: You quit, remember?
  EXPRESSION: null
- CHARACTER: Chris
  LINE: I’m nervous.
  EXPRESSION: null
- CHARACTER: Rose
  LINE: Why? They’re going to love you.
  EXPRESSION: null
- CHARACTER: Chris
  LINE: Yeah? How do you know?
  EXPRESSION: null
- CHARACTER: Rose
  LINE: Let’s see, you’re smart, sweet, handsome, creative... You’re you.
  EXPRESSION: null
- CHARACTER: Chris
  LINE: Good answer.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Chris packs in silence for a moment.
  EXPRESSION: null
- CHARACTER: Chris
  LINE: Do they know I’m black?
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Rose is taken aback by the question.
  EXPRESSION: null
- CHARACTER: Rose
  LINE: I don’t think so. Why? Should they?
  EXPRESSION: null
- CHARACTER: Chris
  LINE: Seems like you might give them a heads up.
  EXPRESSION: null
- CHARACTER: Rose
  LINE: Really? Like “Mom, Dad, my black boyfriend is coming up for the weekend”?
  EXPRESSION: null
- CHARACTER: Chris
  LINE: You said, I’m the first black guy you’d ever dated.
  EXPRESSION: null
- CHARACTER: Rose
  LINE: Yeah...?
  EXPRESSION: null
- CHARACTER: Chris
  LINE: So this is uncharted territory for them.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Rose embraces him.
  EXPRESSION: null
- CHARACTER: Rose
  LINE: Baby, it’s fine. My dad would legit vote for Obama a third time he could. Yes, he will want to talk to you about it, and that will be embarrassing, but they’re gonna love you. I promise.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Chris nods. She kisses his neck and pulls him to the bed.
  EXPRESSION: null

::SCENE::
LOCATION: Brooklyn Loft - Living Room
MOOD: Departure
CHARACTERS: Narrator, Chris, Rose, Sid
BACKGROUND_IMAGE: brooklyn_loft_living_room.png
BACKGROUND_EDIT: "Day. Chris turns on the TV for Sid. He and Rose stand by the front door about to leave."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Chris turns on the TV for Sid. He and Rose stand by the front door about to leave.
  EXPRESSION: null
- CHARACTER: Chris
  LINE: Bye.
  EXPRESSION: null
- CHARACTER: Rose
  LINE: See you soon.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Rose blows Sid a kiss and they leave.
  EXPRESSION: null

::SCENE::
LOCATION: Brooklyn Neighborhood Street
MOOD: Excitement
CHARACTERS: Narrator, Chris, Rose
BACKGROUND_IMAGE: brooklyn_neighborhood_street.png
BACKGROUND_EDIT: "Day. Chris puts his luggage in the trunk and enters the passenger’s side of a shiny white BMW X5."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Chris puts his luggage in the trunk and enters the passenger’s side of a shiny white BMW X5.
  EXPRESSION: null

::SCENE::
LOCATION: Brooklyn Neighborhood Street - Parked Car
MOOD: Playful
CHARACTERS: Narrator, Rose, Chris
BACKGROUND_IMAGE: brooklyn_neighborhood_street_car.png
BACKGROUND_EDIT: "Continuous. Rose sits in the driver’s seat. Chris gets in the passenger’s seat. Her car is a mess."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Rose sits in the driver’s seat. Chris gets in the passenger seat. Her car is a mess.
  EXPRESSION: null
- CHARACTER: Chris
  LINE: How do they even let you in a hospital?
  EXPRESSION: null
- CHARACTER: Rose
  LINE: Shut up. I’m very sanitary at work.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: She moves some fast food wrappers to the back seat.
  EXPRESSION: null
- CHARACTER: Rose
  LINE: You ready?
  EXPRESSION: null
- CHARACTER: Chris
  LINE: Yeah. You?
  EXPRESSION: null
- CHARACTER: Rose
  LINE: Oh, wait.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: She raises her phone and takes a selfie of the two of them.
  EXPRESSION: null
- CHARACTER: Rose
  LINE: Ready.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Chris puts his hand on her leg, and they drive off.
  EXPRESSION: null

::SCENE::
LOCATION: New York - City
MOOD: Transition
CHARACTERS: Narrator
BACKGROUND_IMAGE: new_york_city.png
BACKGROUND_EDIT: "Continuous. The car leaves the city."

::SCRIPT::
- CHARACTER: Narrator
  LINE: The car leaves the city.
  EXPRESSION: null

::SCENE::
LOCATION: Rural Road - Bird's-Eye View
MOOD: Serene
CHARACTERS: Narrator
BACKGROUND_IMAGE: rural_road_birds_eye.png
BACKGROUND_EDIT: "Day. We soar over the car as it drives through the beautiful countryside; a road flanked by woods."

::SCRIPT::
- CHARACTER: Narrator
  LINE: We soar over the car as it drives through the beautiful countryside; a road flanked by woods.
  EXPRESSION: null

::SCENE::
LOCATION: Rose’s Car
MOOD: Relaxed
CHARACTERS: Narrator, Rose, Chris
BACKGROUND_IMAGE: roses_car.png
BACKGROUND_EDIT: "Day. Rose hums. Chris, in the passengers seat, looks through his camera at the passing trees. He snaps a test shot."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Rose hums. Chris, in the passengers seat, looks through his camera at the passing trees. He snaps a test shot.
  EXPRESSION: null
- CHARACTER: Chris
  LINE: How long has it been?
  EXPRESSION: null
- CHARACTER: Rose
  LINE: 10 months, so a year basically; longest I’ve ever been
  EXPRESSION: null

::SCENE::
LOCATION: Not specified (Implied Interior of a Car)
MOOD: Comedic Tension
CHARACTERS: Chris, Rose
BACKGROUND_IMAGE: car_interior.png
BACKGROUND_EDIT: "Dimly lit, possibly moving"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Away.
  EXPRESSION: null
- CHARACTER: Chris
  LINE: Chris takes out another cigarette. Rose promptly grabs it and opens the window.
  EXPRESSION: null
- CHARACTER: Chris
  LINE: Whoa... whoa!! Come on! I’m a grown man. If a man says he wants a cigarette, a man should be able to- -
  EXPRESSION: Exasperated
- CHARACTER: Narrator
  LINE: She throws it out the window.
  EXPRESSION: null
- CHARACTER: Chris
  LINE: Okay, so that’s like a dollar. You basically just throwin’ dollars out the window.
  EXPRESSION: Annoyed
- CHARACTER: Rose
  LINE: You shouldn’t have bought them.
  EXPRESSION: Firm
- CHARACTER: Chris
  LINE: I didn’t buy them. Rod... Shit.
  EXPRESSION: Realizing
- CHARACTER: Rose
  LINE: What?
  EXPRESSION: Curious
- CHARACTER: Chris
  LINE: I almost forgot Rod.
  EXPRESSION: Distracted

::PATHS::
- CHOICE: "Continue conversation"
  TARGET: none
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: LaGuardia Airport - Outside the Terminal
MOOD: Mundane, Urban
CHARACTERS: Rod Williams
BACKGROUND_IMAGE: airport_exterior.png
BACKGROUND_EDIT: "Daytime, bustling airport entrance"

::SCRIPT::
- CHARACTER: Narrator
  LINE: ROD WILLIAMS, 26, African American, a stocky TSA agent smokes a cigarette. His cell phone rings.
  EXPRESSION: null
- CHARACTER: Rod
  LINE: ‘Sup?
  EXPRESSION: Casual

::PATHS::
- CHOICE: "Answer call"
  TARGET: rose_car_phone
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Rose’s Car
MOOD: Conversational, Humorous
CHARACTERS: Chris, Rose, Rod (via phone)
BACKGROUND_IMAGE: car_interior_phone.png
BACKGROUND_EDIT: "Daytime, interior of a car, Chris on passenger seat"

::SCRIPT::
- CHARACTER: Chris
  LINE: Hey. You at work?
  EXPRESSION: Inquiring
- CHARACTER: Rod
  LINE: Yeah. How I’m gonna get in trouble for following standard procedure? Fuckin’ Gary out here thinkin’ just because a bitch old, she can’t hijack an airplane.
  EXPRESSION: Cynical
- CHARACTER: Narrator
  LINE: Chris laughs.
  EXPRESSION: Amused
- CHARACTER: Rod
  LINE: Like you can’t hide a bomb in a wheelchair? Watch, Chris, the next 9/11 is gonna be on some geriatric shit.
  EXPRESSION: Sarcastic
- CHARACTER: Chris
  LINE: Look, man, real quick. You good to watch Sid this weekend right?
  EXPRESSION: Anxious
- CHARACTER: Rod
  LINE: What? You think I forgot? Damn ‘C’, give your boy a little credit. I don’t forget shit; you do.
  EXPRESSION: Playfully offended
- CHARACTER: Chris
  LINE: You’re right. My bad.
  EXPRESSION: Apologetic
- CHARACTER: Rod
  LINE: Apology accepted. How’s ‘Lil Miss Rosie’?
  EXPRESSION: Playful
- CHARACTER: Chris
  LINE: She’s good.--
  EXPRESSION: Pleasant
- CHARACTER: Narrator
  LINE: Rose takes the phone.
  EXPRESSION: null
- CHARACTER: Rose
  LINE: Hi, Rod.
  EXPRESSION: Friendly
- CHARACTER: Rod
  LINE: Whattup babygirl? You better bring my boy back in one piece.
  EXPRESSION: Joking
- CHARACTER: Rose
  LINE: I don’t even know what that means but yes I promise.
  EXPRESSION: Playful
- CHARACTER: Rod
  LINE: You know you picked the wrong guy though right?
  EXPRESSION: Teasing
- CHARACTER: Narrator
  LINE: Rose takes the phone back.
  EXPRESSION: null
- CHARACTER: Rose
  LINE: It’s not too late for us is it?
  EXPRESSION: Hopeful
- CHARACTER: Chris
  LINE: Okay, get your own girl.
  EXPRESSION: Playful jealousy
- CHARACTER: Rod
  LINE: Damn, I never seen you like this. Meeting the family and everything? What does she do lick your ass?
  EXPRESSION: Shocked, teasing
- CHARACTER: Chris
  LINE: No! What the fuck is wrong with you?
  EXPRESSION: Outraged
- CHARACTER: Rod
  LINE: That’s it! First girl licks your ass and you done. Just...
  EXPRESSION: Exaggerated despair
- CHARACTER: Narrator
  LINE: Rod makes a WHIPPING SOUND.
  EXPRESSION: null
- CHARACTER: Chris
  LINE: You need help.
  EXPRESSION: Exasperated
- CHARACTER: Rod
  LINE: Yeah I do. I need your girl to introduce me to one of her freaky deaky boarding school friends.
  EXPRESSION: Mischievous
- CHARACTER: Chris
  LINE: I’ll see what I can do. Oh, and I’ll kick you some cash for watching Sid.
  EXPRESSION: Laughing, practical
- CHARACTER: Rod
  LINE: Come on, son! I don’t need your money. I got you!
  EXPRESSION: Generous
- CHARACTER: Chris
  LINE: Thanks, man.
  EXPRESSION: Grateful
- CHARACTER: Rod
  LINE: You better not come back all bougie on me tho--
  EXPRESSION: Warning
- CHARACTER: Narrator
  LINE: Chris hangs up. He gives Rose a look.
  EXPRESSION: null
- CHARACTER: Rose
  LINE: What..? Settle down. You know I’m yours.
  EXPRESSION: Reassuring

::PATHS::
- CHOICE: "Continue driving"
  TARGET: rural_road_incident
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Not specified (Implied Interior of a Car)
MOOD: Playful, then Sudden Shock
CHARACTERS: Chris, Rose
BACKGROUND_IMAGE: car_interior_shock.png
BACKGROUND_EDIT: "Moving car, then abrupt stop"

::SCRIPT::
- CHARACTER: Narrator
  LINE: After a beat he puts another cigarette in his mouth.
  EXPRESSION: null
- CHARACTER: Rose
  LINE: No!
  EXPRESSION: Protest
- CHARACTER: Chris
  LINE: Last one!
  EXPRESSION: Determined
- CHARACTER: Narrator
  LINE: She goes for it. He dodges playfully and tickles her causing her to cackle.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: A shadow darts across the road in front of the hood of the car. It’s hind legs SMACK the hood of the car with a loud THWAT-THWAT. It’s propelled into the woods at an awkward angle. The CAR SCREECHES to a halt.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Chris and Rose breathe hard for a few moments of shock.
  EXPRESSION: null
- CHARACTER: Rose
  LINE: Fuck!
  EXPRESSION: Shocked
- CHARACTER: Chris
  LINE: You okay?
  EXPRESSION: Concerned
- CHARACTER: Rose
  LINE: Yeah. You?
  EXPRESSION: Concerned
- CHARACTER: Chris
  LINE: Yeah. That scared the shit out of me.
  EXPRESSION: Shaken

::PATHS::
- CHOICE: "Inspect the damage"
  TARGET: rural_road_damage
  STATE_CHANGE: fear = +2
  CONDITION: null

::SCENE::
LOCATION: Rural Road
MOOD: Concern, Investigation
CHARACTERS: Rose, Chris
BACKGROUND_IMAGE: rural_road_damage.png
BACKGROUND_EDIT: "Daytime, car stopped, road, adjacent woods"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Rose gets out of her car and inspects the damage. Chris gets out as well. There’s a small bloody dent in the hood.
  EXPRESSION: null
- CHARACTER: Rose
  LINE: Fuck!!!
  EXPRESSION: Angry, distressed
- CHARACTER: Narrator
  LINE: Chris looks back in the direction of the collision.
  EXPRESSION: null
- CHARACTER: Chris
  LINE: Stay here.
  EXPRESSION: Decisive
- CHARACTER: Rose
  LINE: What are you doing?
  EXPRESSION: Questioning
- CHARACTER: Chris
  LINE: I don’t know... See if it’s okay?
  EXPRESSION: Hesitant
- CHARACTER: Narrator
  LINE: Chris walks a few more steps then stops. He rethinks.
  EXPRESSION: null
- CHARACTER: Chris
  LINE: Maybe it’s gone--
  EXPRESSION: Hopeful
- CHARACTER: Narrator
  LINE: A guttural, almost human, MOAN OF PAIN comes from in the woods behind them. They watch the woods in horror.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Chris walks back towards the haunting wail. It stops.
  EXPRESSION: null
- CHARACTER: Rose
  LINE: Chris...?
  EXPRESSION: Worried
- CHARACTER: Narrator
  LINE: Chris motions for Rose the stay. He keeps walking towards the thicket about 60 ft behind the car.
  EXPRESSION: null
- CHARACTER: Rose
  LINE: Be careful!
  EXPRESSION: Fearful
- CHARACTER: Narrator
  LINE: Chris gathers his courage and takes a step toward the thicket. The Moan starts again, but much loader and closer than Chris realized. He’s startled.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Chris peers through the bushes. The deer lays there gasping for breaths and watching him with a black wet eye. Chris is transfixed.
  EXPRESSION: null
- CHARACTER: Rose
  LINE: Do you see it?
  EXPRESSION: Anxious
- CHARACTER: Narrator
  LINE: Chris snaps to. He nods and takes out his phone.
  EXPRESSION: null

::PATHS::
- CHOICE: "Call for help"
  TARGET: upstate_new_york_road_cop
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Upstate New York Road
MOOD: Official, Tense
CHARACTERS: Officer Frostie, Officer Crowe, Rose, Chris
BACKGROUND_IMAGE: upstate_road_scene.png
BACKGROUND_EDIT: "Daytime, rural road, deer carcass, police car, Rose's car"

::SCRIPT::
- CHARACTER: Narrator
  LINE: A cop car is now pulled up to where the deer was hit. OFFICER FROSTIE - Caucasian - 33 stands near the deer. Another officer, OFFICER CROW - 40 - Caucasian with a patronizing smirk, stands by the driver’s side window of Rose’s car which Rose and Chris are both back in.
  EXPRESSION: null

::PATHS::
- CHOICE: "Interact with officers"
  TARGET: int_rose_car_crowe
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Rose’s Car (Interior)
MOOD: Interrogation, Defiance
CHARACTERS: Officer Crowe, Rose, Chris, Officer Frostie (O.C.)
BACKGROUND_IMAGE: car_interior_interrogation.png
BACKGROUND_EDIT: "Daytime, interior of Rose's car, officers outside"

::SCRIPT::
- CHARACTER: Officer Crowe
  LINE: So in the future the number to call is Animal Control Services.
  EXPRESSION: Patronizing
- CHARACTER: Narrator
  LINE: Rose doesn’t like the way he’s looking at them.
  EXPRESSION: null
- CHARACTER: Chris
  LINE: Right. That makes sense.
  EXPRESSION: Agreeable
- CHARACTER: Officer Crowe
  LINE: You two coming up from the city?
  EXPRESSION: Inquiring
- CHARACTER: Chris
  LINE: Yeah.
  EXPRESSION: Simple
- CHARACTER: Officer Crowe
  LINE: And what brings you up--
  EXPRESSION: Probing
- CHARACTER: Rose
  LINE: I’m from here. The Lake Pontaco area? We’re going home.
  EXPRESSION: Defensive
- CHARACTER: Officer Crowe
  LINE: You got a driver’s license?
  EXPRESSION: Demanding
- CHARACTER: Chris
  LINE: Oh... yeah.
  EXPRESSION: Hesitant
- CHARACTER: Narrator
  LINE: Chris gives Rose a “see?” Look as he gets his license.
  EXPRESSION: null
- CHARACTER: Chris
  LINE: I mean, I don’t have a driver’s license, I have a state I.D.
  EXPRESSION: Clarifying
- CHARACTER: Rose
  LINE: I was driving.
  EXPRESSION: Assertive
- CHARACTER: Officer Crowe
  LINE: I didn’t ask who was driving. I asked him for his I.D.
  EXPRESSION: Dismissive
- CHARACTER: Rose
  LINE: My boyfriend shouldn’t have to show you his I.D. because he hasn’t done anything wrong.
  EXPRESSION: Protective
- CHARACTER: Officer Crowe
  LINE: Ma’am, any time there is an incident--
  EXPRESSION: Patronizing
- CHARACTER: Rose
  LINE: No, fuck that!
  EXPRESSION: Angry
- CHARACTER: Chris
  LINE: Baby. It’s okay--
  EXPRESSION: Calming
- CHARACTER: Rose
  LINE: It’s bullshit, and you know it.
  EXPRESSION: Furious
- CHARACTER: Narrator
  LINE: There is a tense silence. Officer Crowe’s walkie chimes in.
  EXPRESSION: null
- CHARACTER: Officer Frostie (O.C.)
  LINE: Ever
  EXPRESSION: Incomplete sentence

::PATHS::
- CHOICE: "Continue to be defiant"
  TARGET: none
  STATE_CHANGE: null
  CONDITION: null
- CHOICE: "De-escalate"
  TARGET: none
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Rural Road
MOOD: Calm
CHARACTERS: Officer Crowe, Rose, Chris
BACKGROUND_IMAGE: rural_road.png
BACKGROUND_EDIT: "Daytime, road with a police car"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Everything alright up there Crowsie?
  EXPRESSION: null
- CHARACTER: Officer Crowe
  LINE: Yeah, I’m all good.
  EXPRESSION: null
- CHARACTER: Officer Crowe
  LINE: You guys be careful.
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue driving"
  TARGET: rose_car_interior
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Rose's Car - Interior
MOOD: Reflective
CHARACTERS: Rose, Chris
BACKGROUND_IMAGE: rose_car_interior.png
BACKGROUND_EDIT: "Afternoon, car interior, wooded road visible"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Chris sits in the passenger’s seat deep in thought. He watches Rose with a new awe. Rose notices. She shrugs.
  EXPRESSION: null
- CHARACTER: Rose
  LINE: What? I’m not gonna let anyone fuck with my man.
  EXPRESSION: Confident
- CHARACTER: Chris
  LINE: That was some ride or die shit, baby. I like that.
  EXPRESSION: Admiring
- CHARACTER: Rose
  LINE: We’re here.
  EXPRESSION: Happy

::PATHS::
- CHOICE: "Arrive at the estate"
  TARGET: armitage_estate_exterior
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Armitage Estate - Exterior
MOOD: Grandiose
CHARACTERS: Rose, Chris, Walter
BACKGROUND_IMAGE: armitage_estate_exterior.png
BACKGROUND_EDIT: "Afternoon, large mansion on expansive lawn by a lake"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The woods give way to an huge front lawn. A large mansion sits in the middle. Thick forest surrounds the estate except for one side which is the edge of a lake. The property feels expensive and isolated; no other houses in sight.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: As they drive through the large front lawn, Chris sees WALTER, African American 35 in the distance facing away. Walter wears a gardening hat and trims hedges. He works slowly and methodically.
  EXPRESSION: null
- CHARACTER: Rose
  LINE: That’s the grounds-keeper... I think his name is Walter.
  EXPRESSION: Informative
- CHARACTER: Narrator
  LINE: Rose parks in front of the house, and. He has a pleasant smile. Rose gets out of the car and waves.
  EXPRESSION: null
- CHARACTER: Rose
  LINE: Hi!
  EXPRESSION: Cheerful
- CHARACTER: Narrator
  LINE: Walter turns and waves back. Chris gets out and waves too.
  EXPRESSION: null
- CHARACTER: Chris
  LINE: Hey! What’s up?
  EXPRESSION: Friendly
- CHARACTER: Narrator
  LINE: Walter waves silently. Odd.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: As Chris gets the luggage from the trunk, Rose runs to the front door and RINGS the DOORBELL. FOOTSTEPS. The door swings open revealing...
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: DEAN ARMITAGE, 59, a tall, balding, barrel-chested, bear hug of a man. Though clearly smart, Dean has an endearing cockiness and a bad case of Dad humor. He is the kind of guy who pronounces garbage, Gar-bahge.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: And... MISSY ARMITAGE, 56, A beautiful beacon of intellectual patience. She is poised and warm; relaxed and in control. They stand in the shadows of the doorway smiling. Rose hugs her parents.
  EXPRESSION: null
- CHARACTER: Rose
  LINE: Hi!!!
  EXPRESSION: Affectionate
- CHARACTER: Dean
  LINE: There’s my girl! Hello sweetheart.
  EXPRESSION: Loving
- CHARACTER: Missy
  LINE: We miss you, Ro Ro.
  EXPRESSION: Loving
- CHARACTER: Rose
  LINE: I miss you guys.
  EXPRESSION: Affectionate
- CHARACTER: Narrator
  LINE: Chris approaches with the bags.
  EXPRESSION: null
- CHARACTER: Chris
  LINE: Hi.
  EXPRESSION: Polite
- CHARACTER: Rose
  LINE: Chris, these are my parents. Mom, Dad, this is Chris.
  EXPRESSION: Introducing
- CHARACTER: Chris
  LINE: Good to finally meet you...
  EXPRESSION: Polite
- CHARACTER: Dean
  LINE: Mr. Armitage will do.
  EXPRESSION: Playful
- CHARACTER: Chris
  LINE: Sure.
  EXPRESSION: Neutral
- CHARACTER: Dean
  LINE: I got him. Come here.
  EXPRESSION: Playful
- CHARACTER: Narrator
  LINE: Dean grabs Chris’ arm and pulls Chris in tight.
  EXPRESSION: null
- CHARACTER: Dean
  LINE: Call me Dean. We hug around here, Fella.
  EXPRESSION: Friendly
- CHARACTER: Chris
  LINE: Alright.
  EXPRESSION: Compliant
- CHARACTER: Dean
  LINE: My wife Missy.
  EXPRESSION: Proud
- CHARACTER: Chris
  LINE: I’ve heard so much about you guys.
  EXPRESSION: Eager
- CHARACTER: Narrator
  LINE: Missy holds Chris’ shoulders and examines his face and chest.
  EXPRESSION: null
- CHARACTER: Missy
  LINE: Yes, you’ll do just fine. So handsome.
  EXPRESSION: Appreciative
- CHARACTER: Rose
  LINE: Can we get inside before you guys start embarrassing me?
  EXPRESSION: Playful
- CHARACTER: Missy
  LINE: Of course, come inside, make yourself at home.
  EXPRESSION: Welcoming
- CHARACTER: Chris
  LINE: I’m fine with the embarrassing by the way; go ahead.
  EXPRESSION: Amused
- CHARACTER: Narrator
  LINE: Missy and Dean laugh. The four enter the house. Missy shuts the door behind them.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Outside, Walter watches as his smile fades away. He slowly turns and goes back to work.
  EXPRESSION: null

::PATHS::
- CHOICE: "Enter the house"
  TARGET: armitage_living_room
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Armitage Living Room - Interior
MOOD: Welcoming
CHARACTERS: Chris, Dean, Missy, Rose
BACKGROUND_IMAGE: armitage_living_room.png
BACKGROUND_EDIT: "Daytime, spacious living room with artwork and fireplace"

::SCRIPT::
- CHARACTER: Narrator
  LINE: A wonderful house looms ahead. The interior is worldly and interesting; clean and homey. Several paintings of castles and medieval battles accent the walls. Taxidermy. One wall is all bookshelf, and there is a fireplace.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Above the fireplace is a large hauntingly beautiful portrait an old man and woman.
  EXPRESSION: null
- CHARACTER: Chris
  LINE: Wow.
  EXPRESSION: Amazed
- CHARACTER: Dean
  LINE: “Wow” is good. We’ll take wow.
  EXPRESSION: Pleased
- CHARACTER: Chris
  LINE: I grew up in a one bedroom, so for me, this is ridiculous.
  EXPRESSION: Humble
- CHARACTER: Dean
  LINE: It ought to be. Lord knows we’ve done enough work on it through the years...
  EXPRESSION: Proud
- CHARACTER: Missy
  LINE: How was the ride in?
  EXPRESSION: Inquiring
- CHARACTER: Rose
  LINE: We hit a deer.
  EXPRESSION: Matter-of-fact
- CHARACTER: Dean
  LINE: Oh no! Where?
  EXPRESSION: Concerned
- CHARACTER: Missy
  LINE: Oh no! Where?
  EXPRESSION: Concerned
- CHARACTER: Rose
  LINE: I don’t know. Down around Lyons road?
  EXPRESSION: Uncertain
- CHARACTER: Chris
  LINE: It came out of nowhere.
  EXPRESSION: Startled
- CHARACTER: Missy
  LINE: Are you guys okay?
  EXPRESSION: Concerned
- CHARACTER: Chris
  LINE: Yeah.
  EXPRESSION: Reassured
- CHARACTER: Rose
  LINE: Yeah. It just fruck us out.
  EXPRESSION: Shaken
- CHARACTER: Missy
  LINE: I bet.
  EXPRESSION: Sympathetic
- CHARACTER: Dean
  LINE: You know what I say. One down... a few hundred thousand to go.
  EXPRESSION: Amused
- CHARACTER: Missy
  LINE: Dean. So awful!
  EXPRESSION: Exasperated
- CHARACTER: Rose
  LINE: Dad.
  EXPRESSION: Exasperated
- CHARACTER: Dean
  LINE: What?! Those things are everywhere up here, Chris; like rats. The damage they’ve done to the ecology alone... Anyway, are we ready for the grand tour?
  EXPRESSION: Opinionated
- CHARACTER: Missy
  LINE: Let them unload their bags first.
  EXPRESSION: Practical
- CHARACTER: Dean
  LINE: Leave ‘em. Walter will get ‘em.
  EXPRESSION: Dismissive
- CHARACTER: Rose
  LINE: I think we’ll manage, Dad.
  EXPRESSION: Firm

::PATHS::
- CHOICE: "Go upstairs with luggage"
  TARGET: armitage_upstairs_hallway
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Armitage Upstairs Hallway - Interior
MOOD: Casual
CHARACTERS: Rose, Chris
BACKGROUND_IMAGE: armitage_upstairs_hallway.png
BACKGROUND_EDIT: "Daytime, upstairs hallway"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Rose and Chris take their bags upstairs.
  EXPRESSION: null

::PATHS::
- CHOICE: "Go to Rose's room"
  TARGET: rose_bedroom
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Armitage House - Rose's Bedroom - Interior
MOOD: Nostalgic
CHARACTERS: Rose, Chris
BACKGROUND_IMAGE: rose_bedroom.png
BACKGROUND_EDIT: "Daytime, preserved teenage girl's bedroom"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Rose’s old room is preserved in the state of a young-minded teenage girl. Lots of pink and dated boy band posters, a stuffed lion. A window overlooks the front lawn.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Rose and Chris place their bags down.
  EXPRESSION: null
- CHARACTER: Rose
  LINE: You think they wish I was still a kid?
  EXPRESSION: Sarcastic
- CHARACTER: Chris
  LINE: I cannot believe they kept it the same.
  EXPRESSION: Amazed
- CHARACTER: Narrator
  LINE: Chris looks at some pictures posted on her dresser.
  EXPRESSION: null
- CHARACTER: Rose
  LINE: So...
  EXPRESSION: Hesitant
- CHARACTER: Chris
  LINE: They’re great.
  EXPRESSION: Reassured
- CHARACTER: Rose
  LINE: Yay.
  EXPRESSION: Pleased
- CHARACTER: Chris
  LINE: No, they’re totally sweet.
  EXPRESSION: Sincere
- CHARACTER: Narrator
  LINE: He sees a picture of Rose in high school on stage in a production of ‘The Crucible.'
  EXPRESSION: null
- CHARACTER: Chris
  LINE: What?! Is this you?
  EXPRESSION: Surprised
- CHARACTER: Rose
  LINE: “The Crucible.” I was Abigail.
  EXPRESSION: Proud
- CHARACTER: Chris
  LINE: I didn’t know you acted.
  EXPRESSION: Curious
- CHARACTER: Rose
  LINE: There’s a lot you don’t know about me.
  EXPRESSION: Mysterious
- CHARACTER: Narrator
  LINE: Rose grabs Chris by the belt and pulls him to the bed on top of her. They kiss. She goes for his fly.
  EXPRESSION: null
- CHARACTER: Chris
  LINE: Wait, what about the tour?
  EXPRESSION: Surprised
- CHARACTER: Rose
  LINE: “The tour?” Are you serious?
  EXPRESSION: Disbelieving
- CHARACTER: Chris
  LINE: We just got here. I don’t wanna
  EXPRESSION: Playful

::PATHS::
- CHOICE: "Continue kissing"
  TARGET: end
  STATE_CHANGE: relationship_stage = intimate
  CONDITION: null
- CHOICE: "Insist on the tour"
  TARGET: armitage_living_room_tour
  STATE_CHANGE: tension = +1
  CONDITION: null

::SCENE::
LOCATION: Armitage Downstairs Hallway
MOOD: Casual
CHARACTERS: Narrator, Dean, Chris, Rose, Missy
BACKGROUND_IMAGE: armitage_hallway.png
BACKGROUND_EDIT: "Daytime, walking through hallway, looking at pictures"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Dean and Chris walk and look at pictures on the wall. Rose and Missy catch up in the living room.
  EXPRESSION: null
- CHARACTER: Dean
  LINE: Frankenstein’s monster. Only pieces of the original structure remain; I like to think the soul is in tact though.
  EXPRESSION: Thoughtful
- CHARACTER: Dean
  LINE: There are seven bedrooms, ten bathrooms, three indoor dining areas, two study’s, two main kitchens. There’s an observatory wing on the top floor. And you’d be hard pressed to find a room that doesn’t serve as library.
  EXPRESSION: Informative
- CHARACTER: Narrator
  LINE: Chris zones in on a photograph taken in the 90’s in front of the Armitage house. Dean and Missy are younger, and Rose and her brother Jeremy are kids.
  EXPRESSION: null
- CHARACTER: Dean
  LINE: That’s Jeremy. Rose’s brother. He’s in Med school.
  EXPRESSION: Informative
- CHARACTER: Chris
  LINE: I’ve heard stories.
  EXPRESSION: Curious
- CHARACTER: Dean
  LINE: He went through a couple dark spots but came out the other side. You’ll meet him later.
  EXPRESSION: Reassuring
- CHARACTER: Chris
  LINE: Oh, cool.
  EXPRESSION: Casual
- CHARACTER: Narrator
  LINE: Dean points out the older couple in the picture, the same from the portrait in the living room; GRANDPA and GRANDMA.
  EXPRESSION: null
- CHARACTER: Dean
  LINE: Mother and Father lived here till the end. They died a few years ago now. Passed away within weeks of each other...
  EXPRESSION: Somber
- CHARACTER: Chris
  LINE: I hear that happens a lot.
  EXPRESSION: Neutral
- CHARACTER: Dean
  LINE: “Love” is a powerful thing.
  EXPRESSION: Romantic
- CHARACTER: Narrator
  LINE: They move down the hallway to a black and white framed picture of a 25 year old man posing in the starting position for a race.
  EXPRESSION: null
- CHARACTER: Dean
  LINE: My Dad was a runner. A good runner; great sprinter.
  EXPRESSION: Proud
- CHARACTER: Dean
  LINE: Oh, In fact, you might find this interesting, he was just beat out by Jessie Owens in the qualifying round for the ‘36 Olympics in Berlin. That’s the one where--
  EXPRESSION: Enthusiastic
- CHARACTER: Chris
  LINE: --Owens won in front of Hitler.
  EXPRESSION: Knowledgeable
- CHARACTER: Dean
  LINE: You know your history.
  EXPRESSION: Impressed
- CHARACTER: Chris
  LINE: Not really. That one always just stood out in my mind.
  EXPRESSION: Reflective
- CHARACTER: Dean
  LINE: Of course. One of those perfect moments. There’s Hitler on his high horse with his perfect Aryan race, and here comes this black guy to prove him wrong on the world’s stage. What a moment.
  EXPRESSION: Passionate
- CHARACTER: Chris
  LINE: Yeah, tough break for your father though.
  EXPRESSION: Empathetic
- CHARACTER: Dean
  LINE: He almost got over it.
  EXPRESSION: Amused
- CHARACTER: Narrator
  LINE: Dean winks.
  EXPRESSION: Amused

::SCENE::
LOCATION: Missy’s Office - Armitage House
MOOD: Informative
CHARACTERS: Narrator, Dean, Chris, Snowbell
BACKGROUND_IMAGE: missys_office.png
BACKGROUND_EDIT: "Daytime, Dean opens door to office, chairs, bookshelves, cat on desk"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Dean opens the door to the office. He and Chris stand outside the door as Dean reaches in to turn on the lights. In front of the desk two comfortable-looking chairs face each other. Books line the walls, and are stacked everywhere. Dean and Chris don’t enter. A white cat laying next to a teacup wakes up on the desk.
  EXPRESSION: null
- CHARACTER: Dean
  LINE: Okay Snowbell just looking. Missy’s office. This is where she takes appointments.
  EXPRESSION: Casual
- CHARACTER: Chris
  LINE: She’s a Therapist right?
  EXPRESSION: Curious
- CHARACTER: Dean
  LINE: Yeah. One of the best in the world. Not a tidy woman.
  EXPRESSION: Honest
- CHARACTER: Chris
  LINE: Like mother like daughter.
  EXPRESSION: Humorous
- CHARACTER: Narrator
  LINE: Dean Cackles.
  EXPRESSION: Amused

::SCENE::
LOCATION: Armitage House - Hallway
MOOD: Informative
CHARACTERS: Narrator, Chris, Dean
BACKGROUND_IMAGE: armitage_hallway.png
BACKGROUND_EDIT: "Daytime, passing a closed door"

::SCRIPT::
- CHARACTER: Chris
  LINE: And you’re a surgeon?
  EXPRESSION: Curious
- CHARACTER: Dean
  LINE: A neurosurgeon; was. I retired early. Now, I pretty much focus on the house and twiddle my thumbs.
  EXPRESSION: Content
- CHARACTER: Narrator
  LINE: Dean and Chris pass a closed door.
  EXPRESSION: null
- CHARACTER: Dean
  LINE: Oh, downstairs is the wine cellar, the games room, some storage. Apparently a black mold issue down there. Almost everything needs to get thrown out; shame.
  EXPRESSION: Regretful

::SCENE::
LOCATION: Armitage Kitchen
MOOD: Observational
CHARACTERS: Narrator, Dean, Chris, Georgina
BACKGROUND_IMAGE: armitage_kitchen.png
BACKGROUND_EDIT: "Daytime, large and pristine kitchen, large windows overlooking backyard, Georgina cleaning"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Dean and Chris continue their walk-through. The kitchen is large, homey and pristine. Large windows overlook the backyard. GEORGINA, African American, 30 stands facing a wall. She is still.
  EXPRESSION: null
- CHARACTER: Dean
  LINE: My mother loved her kitchen.
  EXPRESSION: Nostalgic
- CHARACTER: Narrator
  LINE: Upon hearing them, Georgina comes alive. She resumes cleaning the kitchen.
  EXPRESSION: null
- CHARACTER: Chris
  LINE: That view.
  EXPRESSION: Appreciative
- CHARACTER: Dean
  LINE: Oh, Georgina, this is Chris; Rose’s boyfriend.
  EXPRESSION: Introducing
- CHARACTER: Narrator
  LINE: Georgina turns to them. She has the same eerie smile as Walter. Like she’s masking something.
  EXPRESSION: Uneasy
- CHARACTER: Chris
  LINE: Hi.
  EXPRESSION: Friendly
- CHARACTER: Georgina
  LINE: Hello.
  EXPRESSION: Polite

::SCENE::
LOCATION: Backyard
MOOD: Expansive
CHARACTERS: Narrator, Dean, Chris, Walter
BACKGROUND_IMAGE: backyard.png
BACKGROUND_EDIT: "Late afternoon, huge yard, ominous woods, wind rushing through trees, Dean leads Chris towards gazebo"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Dean opens the glass back door.
  EXPRESSION: null
- CHARACTER: Dean
  LINE: Ah ha! But now for the piece de resistance...
  EXPRESSION: Excited
- CHARACTER: Narrator
  LINE: The yard is huge and the woods beyond it ominous. The wind RUSHES through the trees. Dean leads Chris out through the yard towards a gazebo.
  EXPRESSION: null
- CHARACTER: Dean
  LINE: Badminton and bocce ball, croquet; we’re a family who loves games. Two other families have properties on lake Pontaco, and they’re way on the other side. Total privacy.
  EXPRESSION: Proud
- CHARACTER: Narrator
  LINE: Chris is distracted by Walter who prepares the lawn mower in the distance.
  EXPRESSION: null
- CHARACTER: Dean
  LINE: I know what you’re thinking.
  EXPRESSION: Perceptive
- CHARACTER: Chris
  LINE: Yeah?
  EXPRESSION: Curious
- CHARACTER: Dean
  LINE: Well-to-do white family; black servants...
  EXPRESSION: Direct
- CHARACTER: Chris
  LINE: I wasn’t gonna go there.
  EXPRESSION: Defensive
- CHARACTER: Dean
  LINE: You didn’t have to. We hired them a few years ago to help care for my parents; they became part of the family. Couldn’t bear to let them go. I hate the way it makes us look though...
  EXPRESSION: Concerned
- CHARACTER: Chris
  LINE: Hey. People need work.
  EXPRESSION: Pragmatic
- CHARACTER: Dean
  LINE: Yeah.
  EXPRESSION: Acknowledging
- CHARACTER: Narrator
  LINE: They arrive at an outdoor patio. Dean stops Chris from stepping on a dead sparrow.
  EXPRESSION: null
- CHARACTER: Dean
  LINE: Well, crap.
  EXPRESSION: Annoyed
- CHARACTER: Dean
  LINE: Walter!
  EXPRESSION: Calling
- CHARACTER: Narrator
  LINE: Walter turns to face them. He has that same eerily mild smile. Vacant in its sincerity.
  EXPRESSION: Uneasy
- CHARACTER: Dean
  LINE: Another dead bird! Damn things fly into the patio from time to time; break their necks.
  EXPRESSION: Resigned
- CHARACTER: Narrator
  LINE: Walter nods slowly. Dean gently kicks the bird’s carcass out of their way.
  EXPRESSION: null
- CHARACTER: Dean
  LINE: Iced tea?
  EXPRESSION: Hospitable

::SCENE::
LOCATION: Outdoor Patio
MOOD: Relaxed
CHARACTERS: Narrator, Dean, Missy, Chris, Rose
BACKGROUND_IMAGE: outdoor_patio.png
BACKGROUND_EDIT: "Daytime, sitting on patio with iced teas"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Dean, Missy, Chris and Rose sit with iced teas.
  EXPRESSION: null
- CHARACTER: Missy
  LINE: Rose tells us your parents aren’t with us.
  EXPRESSION: Empathetic
- CHARACTER: Chris
  LINE: My Dad was never really in the picture. My mom passed away when I was 11; She was hit by a car.
  EXPRESSION: Somber

::SCENE::
LOCATION: ARMITAGE HOUSE - DAY
MOOD: Warm, Familial
CHARACTERS: ISSY DEAN, CHRIS, ROSE, MISSY
BACKGROUND_IMAGE: armitage_house_day.png
BACKGROUND_EDIT: "Outdoor setting, sunny day, family gathered"

::SCRIPT::
- CHARACTER: ISSY DEAN
  LINE: Oh, that’s awful; so young. I’m so sorry to hear that.
  EXPRESSION: Sad
- CHARACTER: CHRIS
  LINE: Yeah. My aunt raised me, with my cousins. We didn’t have a lot of money or anything, but she’s a good person; kept me off the streets. She gave me my first camera.
  EXPRESSION: Reflective
- CHARACTER: Narrator
  LINE: Rose holds Chris’ hand.
  EXPRESSION: null
- CHARACTER: MISSY
  LINE: You two seem like you’ve been together for years. How long has it been now?
  EXPRESSION: Curious
- CHARACTER: CHRIS
  LINE: 4 months? 5 months.
  EXPRESSION: Uncertain
- CHARACTER: CHRIS
  LINE: 5? She’s right; I’m wrong.
  EXPRESSION: Corrective
- CHARACTER: DEAN
  LINE: ‘Atta boy Chris. Get used to saying that.
  EXPRESSION: Amused
- CHARACTER: MISSY
  LINE: Not a lot of time, anyway. So...? You guys in love or what?
  EXPRESSION: Direct
- CHARACTER: ROSE
  LINE: Mom.
  EXPRESSION: Chiding
- CHARACTER: CHRIS
  LINE: I mean, we’ve been trying to take it slow but...
  EXPRESSION: Hesitant
- CHARACTER: MISSY
  LINE: Yep. You’re in love. I can tell.
  EXPRESSION: Confident
- CHARACTER: DEAN
  LINE: Can’t resist the inevitable.
  EXPRESSION: Resigned
- CHARACTER: Narrator
  LINE: Walter mows past them in the distance.
  EXPRESSION: null
- CHARACTER: MISSY
  LINE: And how did you meet, again?
  EXPRESSION: Inquisitive
- CHARACTER: CHRIS
  LINE: At the blood drive.
  EXPRESSION: Factual
- CHARACTER: ROSE
  LINE: Remember when I volunteered at the community center?
  EXPRESSION: Reminder
- CHARACTER: DEAN
  LINE: Ah, yes.
  EXPRESSION: Acknowledging
- CHARACTER: MISSY
  LINE: And he really is so good looking, isn’t he? You’d have beautiful babies.
  EXPRESSION: Admiring
- CHARACTER: ROSE
  LINE: I know!
  EXPRESSION: Excited
- CHARACTER: DEAN
  LINE: Uh oh. Get out of here before it’s too late!
  EXPRESSION: Joking
- CHARACTER: ROSE
  LINE: Now, all you have to do is just quit smoking.
  EXPRESSION: Direct
- CHARACTER: DEAN
  LINE: Oh no! A smoker!?
  EXPRESSION: Mock Horror
- CHARACTER: MISSY
  LINE: And we were just beginning to like you.
  EXPRESSION: Teasing
- CHARACTER: CHRIS
  LINE: No. I’m quitting.
  EXPRESSION: Determined
- CHARACTER: DEAN
  LINE: You should have Missy take care of that for you.
  EXPRESSION: Suggestive
- CHARACTER: ROSE
  LINE: Oh God.
  EXPRESSION: Apprehensive
- CHARACTER: CHRIS
  LINE: How?
  EXPRESSION: Curious
- CHARACTER: DEAN
  LINE: Hypnosis. Works like a charm.
  EXPRESSION: Confident
- CHARACTER: Narrator
  LINE: Missy watches Chris’ reaction intently. He is uncomfortable.
  EXPRESSION: null
- CHARACTER: CHRIS
  LINE: Oh.
  EXPRESSION: Uncomfortable
- CHARACTER: DEAN
  LINE: I thought the whole thing was B.S. too. I smoked for 20 years. She puts me under once, now the sight of a cigarette makes me wanna vomit.
  EXPRESSION: Testimonial
- CHARACTER: MISSY
  LINE: Of course, I’d give you the service for free. You are family after all.
  EXPRESSION: Generous
- CHARACTER: CHRIS
  LINE: Wow. I don’t... Thank you. Um, I don’t know.
  EXPRESSION: Hesitant
- CHARACTER: Narrator
  LINE: Chris looks to Rose for help.
  EXPRESSION: null
- CHARACTER: ROSE
  LINE: You guys, normal people don’t want strangers fiddling around in their heads.
  EXPRESSION: Protective
- CHARACTER: MISSY
  LINE: If you change your mind... We’re just glad you could join us for the big get-together.
  EXPRESSION: Welcoming
- CHARACTER: Narrator
  LINE: Georgina brings the pitcher of iced tea around and refills everyone’s glass. Chris tries to thank her with a look. She smiles and avoids eye contact.
  EXPRESSION: null
- CHARACTER: CHRIS
  LINE: The get-together?
  EXPRESSION: Confused
- CHARACTER: ROSE
  LINE: The party tomorrow? I told you.
  EXPRESSION: Reminder
- CHARACTER: CHRIS
  LINE: I must have forgot.
  EXPRESSION: Apologetic
- CHARACTER: MISSY
  LINE: Oh, well we host a shindig once a year for our friends.
  EXPRESSION: Explanatory
- CHARACTER: DEAN
  LINE: A tradition. Some of my Dad’s old social club. Some old patients. Some just friends...
  EXPRESSION: Elaborating
- CHARACTER: MISSY
  LINE: Drinks, good food, good people...
  EXPRESSION: Enthusiastic
- CHARACTER: CHRIS
  LINE: Sounds fun.
  EXPRESSION: Pleased
- CHARACTER: Narrator
  LINE: Georgina has been pouring Chris’ drink too long and his glass has overflown.
  EXPRESSION: null
- CHARACTER: MISSY
  LINE: Georgina!
  EXPRESSION: Exasperated
- CHARACTER: Narrator
  LINE: Georgina snaps out of her daze. She realizes what she’s done and starts to clean.
  EXPRESSION: null
- CHARACTER: MISSY
  LINE: It’s fine George, I’ll get it. Maybe you need a nap.
  EXPRESSION: Dismissive
- CHARACTER: Narrator
  LINE: Georgina nods, smiles and walks away. Chris and Rose look at Dean. That was odd. Dean shrugs.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: A car horn honks in front of the house.
  EXPRESSION: null
- CHARACTER: DEAN
  LINE: Jeremy’s home.
  EXPRESSION: Informative
- CHARACTER: Narrator
  LINE: JEREMY, 29, rounds the house with open arms. He’s “Rich kid intense”; handsome and strong with an unpredictable wildness behind his eyes.
  EXPRESSION: null
- CHARACTER: JEREMY
  LINE: Who answers the door around here?!
  EXPRESSION: Boisterous

::SCENE::
LOCATION: ARMITAGE DINING ROOM - LATER/NIGHT
MOOD: Lively, Tipsy
CHARACTERS: DEAN, CHRIS, JEREMY, ROSE, MISSY
BACKGROUND_IMAGE: armitage_dining_room_night.png
BACKGROUND_EDIT: "Interior, dining room, evening, meal concluding"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Everyone laughs.
  EXPRESSION: null
- CHARACTER: DEAN
  LINE: Pours the remainder of a bottle of wine into Chris’ glass. Their meal is done and they are tipsy. Jeremy pops the cork on a new bottle of wine as he energetically holds court.
  EXPRESSION: null
- CHARACTER: JEREMY
  LINE: One more... So, let me set the scene. I’m a junior; Ro’s a freshman and she has a crush on this guy Connor--
  EXPRESSION: Storytelling
- CHARACTER: ROSE
  LINE: --No. Mom.
  EXPRESSION: Interrupting
- CHARACTER: MISSY
  LINE: Jeremy...
  EXPRESSION: Stern
- CHARACTER: CHRIS
  LINE: No, no... These are good. I wanna hear this.
  EXPRESSION: Eager
- CHARACTER: DEAN
  LINE: Manners, Rose. Give the guest what he wants.
  EXPRESSION: Scolding
- CHARACTER: JEREMY
  LINE: Yeah, Rose.
  EXPRESSION: Agreeing
- CHARACTER: ROSE
  LINE: I hate you.
  EXPRESSION: Affectionate
- CHARACTER: JEREMY
  LINE: Connor Garfield was on my lacrosse team. Huge guy, like 6’3”, and crazy, just like “Looney Tunes,” right? We had thrown a party--
  EXPRESSION: Storytelling
- CHARACTER: ROSE
  LINE: You did.
  EXPRESSION: Correcting
- CHARACTER: JEREMY
  LINE: I think my parents were in Greece or something. We had gotten into their liquor cabinet and we’re all shit-faced.
  EXPRESSION: Recounting
- CHARACTER: MISSY
  LINE: No you weren’t. Were you?
  EXPRESSION: Skeptical
- CHARACTER: JEREMY
  LINE: We put water in the bottles so you wouldn’t know. Let me finish. Okay, so I’m upstairs in my parents’ bathroom hooking up with Jenny Richardson. Hottest girl in our class.
  EXPRESSION: Boasting
- CHARACTER: MISSY
  LINE: Uch.
  EXPRESSION: Disgusted
- CHARACTER: ROSE
  LINE: You realize you’re coming off like a total douche right now, right?
  EXPRESSION: Blunt
- CHARACTER: JEREMY
  LINE: Thanks. All of a sudden Connor starts banging on the bathroom door, right? I open it, and he’s got blood gushing out of his mouth and he’s screaming “Your thith-ter bit my fuckin’ thongue off!!!!”
  EXPRESSION: Dramatic
- CHARACTER: CHRIS
  LINE: Whoa, what?
  EXPRESSION: Surprised
- CHARACTER: JEREMY
  LINE: Sure enough, there is a centimeter of tongue meat missing right here.
  EXPRESSION: Demonstrative
- CHARACTER: Narrator
  LINE: Jeremy demonstrates and Chris winces.
  EXPRESSION: null
- CHARACTER: CHRIS
  LINE: Ahhhh! You bit him?
  EXPRESSION: Shocked
- CHARACTER: ROSE
  LINE: He cornered me and shoved his tongue in my mouth, so yeah.
  EXPRESSION: Defiant
- CHARACTER: CHRIS
  LINE: Damn. That’s badass, Bae.
  EXPRESSION: Impressed
- CHARACTER: MISSY
  LINE: I’m going to see how dessert is coming along.
  EXPRESSION: Distracting
- CHARACTER: MISSY
  LINE: Maybe we can change the conversation to something a little lighter.
  EXPRESSION: Suggestive
- CHARACTER: ROSE
  LINE: Yeah, great story. Thanks for making it totally uncomfortable.
  EXPRESSION: Sarcastic
- CHARACTER: Narrator
  LINE: Missy walks out of the dining room into the kitchen. The door swings open and Chris gets another glimpse of Georgina who stands with a kitchen knife and wears an intense and wicked little smile. The door swings shut.
  EXPRESSION: null
- CHARACTER: DEAN
  LINE: Okay, new subject. Chris, Yanks or Mets?
  EXPRESSION: Diverting
- CHARACTER: CHRIS
  LINE: Ah, Orioles. My mom was from Baltimore so--
  EXPRESSION: Factual
- CHARACTER: JEREMY
  LINE: You an MMA fan?
  EXPRESSION: Inquisitive
- CHARACTER: ROSE
  LINE: Oh God.
  EXPRESSION: Exasperated
- CHARACTER: JEREMY
  LINE: What?
  EXPRESSION: Confused
- CHARACTER: DEAN
  LINE: She’s right. Let someone else talk for a bit.
  EXPRESSION: Restraining
- CHARACTER: JEREMY
  LINE: You’ve had your chance. He’s dating my sister. I can’t bond with t
  EXPRESSION: Defensive

::SCENE::
INT. DINING ROOM - NIGHT
CHARACTERS: CHRIS, DEAN, JEREMY, ROSE, MISSY
BACKGROUND_IMAGE: dining_room_night.png
BACKGROUND_EDIT: "A group of people are sitting around a dining table, some drinking wine."

::SCRIPT::
- CHARACTER: CHRIS
  LINE: he guy?
  EXPRESSION: null
- CHARACTER: DEAN
  LINE: Dean exhales.
  EXPRESSION: null
- CHARACTER: CHRIS
  LINE: You mean like UFC? Yeah, nah. Too brutal for me. I’m a lover, not a fighter.
  EXPRESSION: null
- CHARACTER: JEREMY
  LINE: You ever get into street fights as a kid?
  EXPRESSION: null
- CHARACTER: CHRIS
  LINE: Not really. I did take Judo for after-school in 1st grade.
  EXPRESSION: null
- CHARACTER: ROSE
  LINE: Awww.
  EXPRESSION: null
- CHARACTER: JEREMY
  LINE: Cause, with your frame, your genetic make-up? If you pushed your body, I mean really trained, you’d be a beast.
  EXPRESSION: null
- CHARACTER: CHRIS
  LINE: Cool... Thanks?
  EXPRESSION: null

::SCENE::
INT. DINING ROOM - NIGHT
CHARACTERS: CHRIS, DEAN, JEREMY, ROSE, MISSY
BACKGROUND_IMAGE: dining_room_night.png
BACKGROUND_EDIT: "Missy walks back in with a carrot cake. Georgina is gone."

::SCRIPT::
- CHARACTER: NARRATOR
  LINE: The kitchen door swings open again, and Missy walks back in with a perfect carrot cake. Georgina is gone.
  EXPRESSION: null
- CHARACTER: MISSY
  LINE: What’d I miss?
  EXPRESSION: null
- CHARACTER: ROSE
  LINE: More ramblings from King Awkward.
  EXPRESSION: null
- CHARACTER: JEREMY
  LINE: We’re talking about sports. Stand up. Let me show you something.
  EXPRESSION: null
- CHARACTER: MISSY
  LINE: No karate at the dinner table.
  EXPRESSION: null
- CHARACTER: JEREMY
  LINE: It’s not karate, it’s jiu-jitsu.
  EXPRESSION: null

::SCENE::
INT. DINING ROOM - NIGHT
CHARACTERS: CHRIS, DEAN, JEREMY, ROSE, MISSY
BACKGROUND_IMAGE: dining_room_night.png
BACKGROUND_EDIT: "Jeremy stumbles towards Chris and tries to put him in a headlock."

::SCRIPT::
- CHARACTER: NARRATOR
  LINE: He stumbles a little towards Chris and tries to put him in a headlock. Chris stands.
  EXPRESSION: null
- CHARACTER: CHRIS
  LINE: I’ve got a rule. I don’t play-fight with drunk dudes.
  EXPRESSION: null
- CHARACTER: JEREMY
  LINE: I’m just--
  EXPRESSION: null
- CHARACTER: DEAN
  LINE: --Alright, enough Jeremy!
  EXPRESSION: null
- CHARACTER: JEREMY
  LINE: I wasn’t going to hurt him.
  EXPRESSION: null

::SCENE::
INT. DINING ROOM - NIGHT
CHARACTERS: ROSE, JEREMY
BACKGROUND_IMAGE: dining_room_night.png
BACKGROUND_EDIT: "Dean is loud and stern. Jeremy looks drunk and embarrassed. He grabs a wine bottle and goes upstairs."

::SCRIPT::
- CHARACTER: NARRATOR
  LINE: Dean is loud and stern for the first time. Jeremy’s eyes flutter, DRUNK and embarrassed. He grabs a wine bottle and goes upstairs.
  EXPRESSION: null
- CHARACTER: ROSE
  LINE: And that’s my brother.
  EXPRESSION: null

::SCENE::
EXT. THE ESTATE - NIGHT
CHARACTERS: NARRATOR
BACKGROUND_IMAGE: estate_night.png
BACKGROUND_EDIT: "A full moon is visible. Crickets are chirping."

::SCRIPT::
- CHARACTER: NARRATOR
  LINE: Full moon. CRICKETS.
  EXPRESSION: null

::SCENE::
INT. ROSE'S BEDROOM - NIGHT
CHARACTERS: CHRIS, ROSE
BACKGROUND_IMAGE: rose_bedroom_night.png
BACKGROUND_EDIT: "Rose and Chris are making love in bed. A stuffed lion is on the bed."

::SCRIPT::
- CHARACTER: NARRATOR
  LINE: Rose and Chris make hushed love in her bed. A stuffed lion seems to watch Chris. He turns it away.
  EXPRESSION: null

::SCENE::
INT. ROSE'S BEDROOM - LATER
CHARACTERS: CHRIS, ROSE
BACKGROUND_IMAGE: rose_bedroom_night.png
BACKGROUND_EDIT: "Rose is asleep. Chris is awake. A soft howl of wind blows through the room. The closet door creaks open."

::SCRIPT::
- CHARACTER: NARRATOR
  LINE: Rose sleeps, but Chris is wide awake. There’s a buzz in his ear. He smacks his own head and sits up. A soft HOWL of WIND rushes through the room. The CLOSET DOOR CREEKS open.
  EXPRESSION: null
- CHARACTER: NARRATOR
  LINE: Chris’ eyes drift to the pack of cigarettes sticking out of his camera bag pocket draped on the desk chair.
  EXPRESSION: null

::SCENE::
INT. ARMITAGE HALLWAY - NIGHT
CHARACTERS: CHRIS
BACKGROUND_IMAGE: armitage_hallway_night.png
BACKGROUND_EDIT: "Chris leaves Rose's room and walks down a dark hallway. A floorboard creaks under his feet. He turns down the stairs."

::SCRIPT::
- CHARACTER: NARRATOR
  LINE: Chris leaves Rose’s room and walks down the dark hallway. A floorboard creaks under his feet. He turns down the stairs.
  EXPRESSION: null

::SCENE::
INT. ARMITAGE DOWNSTAIRS HALLWAY - CONTINUOUS
CHARACTERS: CHRIS
BACKGROUND_IMAGE: armitage_hallway_night.png
BACKGROUND_EDIT: "Chris reaches the bottom of the stairs. He hears a floorboard creak upstairs and turns, expecting someone to follow. Nothing. He continues down the hallway towards the kitchen. The basement door is open a crack. Chris peers into it. A figure stands at the end of the hallway behind him, unnoticed."

::SCRIPT::
- CHARACTER: NARRATOR
  LINE: Chris gets to the bottom of the stairs. He hears the floorboard creek upstairs. He stops and turns, expecting someone to follow him down. Nothing. Chris continues to walk down the hallway past the pictures towards the kitchen.
  EXPRESSION: null
- CHARACTER: NARRATOR
  LINE: The basement door is open a crack. Chris peers into it curiously. A stairwell leads down into pitch darkness. Chris shuts the door. A figure now stands at the end of the hallway behind him. He doesn’t notice. He just keeps going into...
  EXPRESSION: null

::SCENE::
INT. ARMITAGE KITCHEN - CONTINUOUS
CHARACTERS: CHRIS
BACKGROUND_IMAGE: armitage_kitchen_night.png
BACKGROUND_EDIT: "Chris walks through the kitchen, bumps into a bar chair, and continues out the sliding back door."

::SCRIPT::
- CHARACTER: NARRATOR
  LINE: Chris walks through the kitchen. He bumps into a bar chair moving it slightly. He keeps walking. He continues out the sliding back door of the house.
  EXPRESSION: null

::SCENE::
EXT. BACKYARD - CONTINUOUS
CHARACTERS: CHRIS
BACKGROUND_IMAGE: backyard_night.png
BACKGROUND_EDIT: "Chris steps out the back door and takes out a cigarette. He looks into the vast night. The crickets are deafening. Something darts fast across the yard. Chris peers into the darkness. The thing runs across the lawn again. A moment of terror comes over Chris. He makes out a shape. It’s now running towards him. Chris backs up in fear just as Walter, the grounds keeper, emerges from the shadows and passes Chris without noticing. The kitchen light turns on. Chris drops the cigarette and stomps it out. He turns back towards the house and finds himself face to face with Georgina, who glares through the window. He’s caught. Georgina doesn’t react. Chris is still. Georgina suddenly exposes her teeth in a frightening grimace. Chris backs away slowly."

::SCRIPT::
- CHARACTER: NARRATOR
  LINE: Chris steps out the back door and takes a cigarette out. Chris looks into the vast night around him. The CRICKETS are deafening.
  EXPRESSION: null
- CHARACTER: NARRATOR
  LINE: Suddenly, something DARTS FAST across the yard in the distance. Chris peers out into the darkness. The thing RUNS across the lawn again. A moment of terror comes over Chris. He makes out a shape. It’s now running towards him. Chris backs up in fear just as the figure emerges from the shadows and into the moonlight. It’s Walter, the grounds keeper. He passes Chris without noticing. Chris gathers his breath.
  EXPRESSION: null
- CHARACTER: NARRATOR
  LINE: The kitchen light turns on and floods the backyard. Chris drops the cigarette and stomps it out. He turns back towards the house and finds himself face to face with Georgina, who glares through the window dead in Chris’ eyes. He’s caught.
  EXPRESSION: null
- CHARACTER: NARRATOR
  LINE: Georgina doesn’t react. Chris it still. Georgina suddenly exposes her teeth in a frightening grimace. Chris backs away slowly.
  EXPRESSION: null

::SCENE::
INT. ARMITAGE KITCHEN - NIGHT
CHARACTERS: GEORGINA, CHRIS
BACKGROUND_IMAGE: armitage_kitchen_night.png
BACKGROUND_EDIT: "Georgina is looking at her teeth in the reflection in the window."

::SCRIPT::
- CHARACTER: NARRATOR
  LINE: Georgina sucks her teeth. She doesn’t actually see Chris at all. She’s looking at her teeth in the reflection in the window which, front lit, reflects her and the room around her. Outside is invisible.
  EXPRESSION: null

::SCENE::
EXT. BACKYARD - NIGHT
CHARACTERS: CHRIS, GEORGINA
BACKGROUND_IMAGE: backyard_night.png
BACKGROUND_EDIT: "Georgina notices the bar chair has been moved and moves it back. Chris quietly sneaks around the house."

::SCRIPT::
- CHARACTER: NARRATOR
  LINE: Chris realizes he’s not caught. Close call. Inside Georgina notices the bar chair has been moved. She moves it back into its original position, and begins cleaning the kitchen cabinets. Chris quietly sneaks around the house.
  EXPRESSION: null

::SCENE::
INT. ARMITAGE DINING ROOM - NIGHT
CHARACTERS: CHRIS
BACKGROUND_IMAGE: armitage_dining_room_night.png
BACKGROUND_EDIT: "Chris sneaks in through the door in the dark dining room."

::SCRIPT::
- CHARACTER: NARRATOR
  LINE: Chris sneaks in through the door in the dark dining room.
  EXPRESSION: null

::SCENE::
INT. ARMITAGE LIVING ROOM - NIGHT
CHARACTERS: CHRIS, MISSY
BACKGROUND_IMAGE: armitage_living_room_night.png
BACKGROUND_EDIT: "Chris moves through the living room towards the stairs. The lamp in the middle of the room turns on, startling Chris. Missy sits near him, cat in lap, almost seductively."

::SCRIPT::
- CHARACTER: NARRATOR
  LINE: Chris moves through the living room towards the stairs, the lamp in the middle of the room turns on startling Chris. Missy sits near him; cat in lap; almost seductively. He’s caught; for real this time.
  EXPRESSION: null
- CHARACTER: MISSY
  LINE: Quick fix?
  EXPRESSION: null
- CHARACTER: CHRIS
  LINE: Yeah. Nerves got me I guess.
  EXPRESSION: null
- CHARACTER: MISSY
  LINE: Come. Let’s nip this in the bud.
  EXPRESSION: null

::SCENE::
INT. MISSY'S OFFICE - NIGHT
CHARACTERS: CHRIS, MISSY
BACKGROUND_IMAGE: missy_office_night.png
BACKGROUND_EDIT: "Missy sits in a chair and directs Chris to sit across from her. She pours them both some tea."

::SCRIPT::
- CHARACTER: NARRATOR
  LINE: Missy sits in a chair and directs Chris to sit across from her. She pours them both some tea. Chris sits.
  EXPRESSION: null
- CHARACTER: CHRIS
  LINE: I still don’t know if this is right for me.
  EXPRESSION: null
- CHARACTER: MISSY
  LINE: There really is no need to be nervous.
  EXPRESSION: null
- CHARACTER: CHRIS
  LINE: I’m good. The dude was running out there. Scared me.
  EXPRESSION: null
- CHARACTER: MISSY
  LINE: Walter starts early every day. He’s borderline obsessive compulsive. Tea?
  EXPRESSION: null
- CHARACTER: CHRIS
  LINE: Nah, I’m good. It’ll keep me up.
  EXPRESSION: null
- CHARACTER: NARRATOR
  LINE: Missy puts two sugar cubes in her cup. She begins to stir slowly, CLINKING the SPOON softly and rhythmically against the sides of the cup. TING TING. TING TING.
  EXPRESSION: null
- CHARACTER: MISSY
  LINE: How’s the bed. Good?
  EXPRESSION: null
- CHARACTER: CHRIS
  LINE: Yeah.
  EXPRESSION: null
- CHARACTER: MISSY
  LINE: Comfortable enough?
  EXPRESSION: null
- CHARACTER: CHRIS
  LINE: It’s perfect, thanks.
  EXPRESSION: null
- CHARACTER: MISSY
  LINE: Enough sheets?
  EXPRESSION: null
- CHARACTER: CHRIS
  LINE: Yep.
  EXPRESSION: null
- CHARACTER: CHRIS
  LINE: So, how does this work? Are you going to sw
  EXPRESSION: null

::SCENE::
LOCATION: Unknown
MOOD: Calm
CHARACTERS: Narrator, Missy, Chris
BACKGROUND_IMAGE: unknown.png
BACKGROUND_EDIT: "Close up on a pocket watch"

::SCRIPT::
- CHARACTER: Narrator
  LINE: ing a pocket watch in
front of my face?
  EXPRESSION: null
- CHARACTER: Missy
  LINE: You watch a lot of Television. Now,
you are feeling very sleepy...
  EXPRESSION: Calm
- CHARACTER: Narrator
  LINE: They share a smile.
  EXPRESSION: null
- CHARACTER: Missy
  LINE: We do use focal points sometimes,
but just about any object or simple
motion can guide someone to a state
of heightened suggestibility.
  EXPRESSION: Calm
- CHARACTER: Chris
  LINE: Heightened suggestibility. Okay,
where do we start?
  EXPRESSION: Curious
- CHARACTER: Missy
  LINE: Your childhood.
  EXPRESSION: Calm
- CHARACTER: Chris
  LINE: Yeah, my memory sucks.
  EXPRESSION: Frustrated

::SOUND::
- SOUND: TING TING. TING TING.
  DURATION: short
- SOUND: TING TING. TING TING.
  DURATION: short

::SCRIPT::
- CHARACTER: Missy
  LINE: Wounds get locked in your heart and
they fester and grow into ugly
little things like depression and
addiction. But, they are all in
there somewhere. All we need to do
is find the key.
  EXPRESSION: Empathetic
- CHARACTER: Narrator
  LINE: The world around Chris slowly goes out of focus.
  EXPRESSION: null
- CHARACTER: Chris
  LINE: I guess if it makes me quit...
Wait... Has it started--?
  EXPRESSION: Hesitant
- CHARACTER: Missy
  LINE: --we’re going to go back to a place
that might be uncomfortable for
you. Your Mother’s death to be
specific. Were you there when she
was hit?
  EXPRESSION: Calm
- CHARACTER: Chris
  LINE: I was home. I was watching TV.
  EXPRESSION: Resigned
- CHARACTER: Missy
  LINE: Let’s go back there. Hear this
place. Let the vibrations rush run
through your body and ears. Hear
it... Find it... Tell me when you
find it.
  EXPRESSION: Calm
- SOUND: RAIN AGAINST a WINDOW slowly fades up along with the MUFFLED sound of a SITCOM ON TELEVISION.
  DURATION: continuous

::SCRIPT::
- CHARACTER: Chris
  LINE: Okay... Yeah, I found it.
  EXPRESSION: Determined
- SOUND: TING TING. TING TING.
  DURATION: short

::SCRIPT::
- CHARACTER: Missy
  LINE: Good. How did you find out she
died?
  EXPRESSION: Calm
- CHARACTER: Chris
  LINE: I knew it. She was never late after
work. When she didn’t come home, I
just knew something was wrong.
  EXPRESSION: Sad
- CHARACTER: Missy
  LINE: Good. Now touch. Feel your
surroundings. Feel every part of
your body and what you touched.
Feel it. Find it... Tell me when
you find it...
  EXPRESSION: Calm

::SCENE::
LOCATION: Small Apartment
MOOD: Anxious
CHARACTERS: Narrator, Missy (V.O.), Chris
BACKGROUND_IMAGE: small_apartment.png
BACKGROUND_EDIT: "Close up on 11-year-old Chris' hands scratching a bed post nervously."

::SCRIPT::
- CHARACTER: Missy (V.O.)
  LINE: Tell me when you find it.
  EXPRESSION: Calm
- CHARACTER: Chris (V.O.)
  LINE: I found it.
  EXPRESSION: Determined
- CHARACTER: Narrator
  LINE: His toes brush the carpet as his dangling legs swing off the
side of his bed.
  EXPRESSION: null

::SOUND::
- SOUND: TING TING. TING TING.
  DURATION: short

::SCENE::
LOCATION: Missy’s Office
MOOD: Tense
CHARACTERS: Narrator, Missy, Chris
BACKGROUND_IMAGE: missys_office.png
BACKGROUND_EDIT: "Chris' feet try to swing but are too long. He scratches the arm of the chair in Missy’s office."

::SCRIPT::
- CHARACTER: Missy
  LINE: You said ‘you knew something was
wrong.’ What did you do?
  EXPRESSION: Calm
- CHARACTER: Chris
  LINE: Nothing.
  EXPRESSION: Resigned
- CHARACTER: Missy
  LINE: Nothing?
  EXPRESSION: Skeptical
- CHARACTER: Chris
  LINE: I just sat there. Watching TV.
  EXPRESSION: Resigned
- CHARACTER: Missy
  LINE: You didn’t call someone? Your Aunt
or the police?
  EXPRESSION: Calm
- CHARACTER: Chris
  LINE: No.
  EXPRESSION: Resigned
- CHARACTER: Missy
  LINE: Why not?
  EXPRESSION: Curious
- CHARACTER: Chris
  LINE: I don’t know. I thought if I did,
it would make it real.
  EXPRESSION: Fearful
- CHARACTER: Missy
  LINE: Next is smell and taste. Breathe in
and let the scent fill your nose.
Smell that place. Taste it. Find
it.
  EXPRESSION: Calm
- CHARACTER: Narrator
  LINE: Chris is getting emotional. He breathes deep through his
nose.
  EXPRESSION: null

::SCENE::
LOCATION: Small Apartment Kitchen
MOOD: Emotional
CHARACTERS: Narrator, Missy (V.O.), Young Chris
BACKGROUND_IMAGE: small_apartment_kitchen.png
BACKGROUND_EDIT: "Young Chris finishes inhaling. The rain hits the window sill."

::SCRIPT::
- CHARACTER: Missy (V.O.)
  LINE: Tell me. Tell me when you find it.
  EXPRESSION: Calm
- CHARACTER: Narrator
  LINE: Young Chris takes sip of a juice box.
  EXPRESSION: null

::SCENE::
LOCATION: Missy’s Office
MOOD: Intense
CHARACTERS: Narrator, Chris, Missy
BACKGROUND_IMAGE: missys_office.png
BACKGROUND_EDIT: "26-year-old Chris sips from an invisible straw."

::SCRIPT::
- CHARACTER: Chris
  LINE: I found it.
  EXPRESSION: Determined

::SOUND::
- SOUND: TING TING. TING TING.
  DURATION: short

::SCRIPT::
- CHARACTER: Missy
  LINE: Good. Now lastly, you must see it.
Let the light flood into your eyes.
Every color, every detail. See it.
See it. Find it.
  EXPRESSION: Calm
- CHARACTER: Narrator
  LINE: Chris’ eyelids flutter. He continues to scratch the armchair.
  EXPRESSION: null

::SOUND::
- SOUND: TING TING. TING TING.
  DURATION: short

::SCENE::
LOCATION: Small Apartment
MOOD: Disturbed
CHARACTERS: Narrator, Missy (V.O.), 11-year-old Chris
BACKGROUND_IMAGE: small_apartment.png
BACKGROUND_EDIT: "11-year-old Chris scratches through the wood on his bed, splintering the wood. He watches TV from his bed next to some action figures."

::SCRIPT::
- CHARACTER: Missy (V.O.)
  LINE: Tell me when--
  EXPRESSION: Calm
- CHARACTER: Narrator
  LINE: 11-year-old Chris nods.
  EXPRESSION: null

::SOUND::
- SOUND: TING TING. TING TING.
  DURATION: short

::SCENE::
LOCATION: Missy’s Office
MOOD: Emotional
CHARACTERS: Narrator, Chris, Missy
BACKGROUND_IMAGE: missys_office.png
BACKGROUND_EDIT: "Chris nods and cries."

::SCRIPT::
- CHARACTER: Chris
  LINE: --Found it.
  EXPRESSION: Emotional
- CHARACTER: Missy
  LINE: You think it was your fault.
  EXPRESSION: Realizing
- CHARACTER: Narrator
  LINE: Chris nods.
  EXPRESSION: null

::SOUND::
- SOUND: TING TING. TING TING.
  DURATION: short

::SCRIPT::
- CHARACTER: Missy
  LINE: I want you to feel that fear again,
Chris.
  EXPRESSION: Commanding
- CHARACTER: Chris
  LINE: I don't want to.
  EXPRESSION: Fearful
- CHARACTER: Missy
  LINE: It's okay. I'm here.
  EXPRESSION: Reassuring
- CHARACTER: Narrator
  LINE: Chris trembles anxiously.
  EXPRESSION: null
- CHARACTER: Missy
  LINE: Are you afraid now? Paralyzed like
that day?
  EXPRESSION: Commanding
- CHARACTER: Narrator
  LINE: He nods. Her empathetic expression turns into a sick smile.
  EXPRESSION: null
- CHARACTER: Missy
  LINE: Good. Now sink into the floor.
  EXPRESSION: Commanding
- CHARACTER: Chris
  LINE: Wait--
  EXPRESSION: Startled
- CHARACTER: Missy
  LINE: Sink! Now!
  EXPRESSION: Commanding

::SOUND::
- SOUND: TING TING...
  DURATION: short

::SCRIPT::
- CHARACTER: Narrator
  LINE: Chris’ hand has compulsively scratched open the arm of the
chair. His hand stops. His mouth drops and eyes open, frozen.
  EXPRESSION: null

::SCENE::
LOCATION: Small Apartment
MOOD: Terrifying
CHARACTERS: Narrator, 11-year-old Chris
BACKGROUND_IMAGE: small_apartment.png
BACKGROUND_EDIT: "Suddenly, 11-year-old Chris falls through the bed and floor."

::SCRIPT::
- CHARACTER: Narrator
  LINE: END FLASHBACK.
  EXPRESSION: null

::SCENE::
LOCATION: Darkness
MOOD: Terror
CHARACTERS: Narrator, Chris (26)
BACKGROUND_IMAGE: darkness.png
BACKGROUND_EDIT: "Chris, 26 again, breathes fast but falls in slow motion though darkness as if through water."

::SOUND::
- SOUND: TING TING. TING TING.
  DURATION: continuous

::SCRIPT::
- CHARACTER: Narrator
  LINE: He flails towards a pitch black abyss. He’s illuminated by
the fading blue flicker of a large downward facing TV-like
screen. On it Missy sits Speaking to him and clinking her
teacup.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Missy’s voice is everywhere.
  EXPRESSION: null
- CHARACTER: Missy
  LINE: Good. Good. Sink. Sink.
  EXPRESSION: Echoing

::SCENE::
LOCATION: Missy’s Office
MOOD: Helpless
CHARACTERS: Narrator, Chris, Missy
BACKGROUND_IMAGE: missys_office.png
BACKGROUND_EDIT: "Chris’ body sits in his chair motionless. He can’t move. His eyes are wide open, staring strait at Missy."

::SCENE::
LOCATION: Darkness
MOOD: Desperate
CHARACTERS: Narrator, Chris, Missy
BACKGROUND_IMAGE: darkness.png
BACKGROUND_EDIT: "Chris continues to slowly fall backwards. Missy approaches on the screen above him. It shows what his eyes are seeing."

::SCRIPT::
- CHARACTER: Chris
  LINE: No! NO!!! I’m done! Bring me back!
Please!!!!
  EXPRESSION: Panicked
- CHARACTER: Narrator
  LINE: There is no response. Chris cries. Eventually he slows down
and comes to a stop. He lands feet first on a soft ground.
This place sounds like it’s crawling with insects. He looks
up. He can still see the screen above but it is far away,
like the mouth of a deep and expansive well.
  EXPRESSION: null
- CHARACTER: Chris
  LINE: Mrs. Armitage!!!
  EXPRESSION: Pleading
- CHARACTER: Narrator
  LINE: On the screen, Missy stands. She walks towards Chris’ body
and looks down at him through his own eyes.
  EXPRESSION: null
- CHARACTER: Missy
  LINE: Now you are in the Sunken Place.
  EXPRESSION: Malevolent
- CHARACTER: Narrator
  LINE: Missy reaches towards the s
  EXPRESSION: null

::SCENE::
LOCATION: Darkness
MOOD: Terror
CHARACTERS: Chris, Narrator
BACKGROUND_IMAGE: darkness.png
BACKGROUND_EDIT: "Screen goes black, then dimly lit abyss"

::SCRIPT::
- CHARACTER: Narrator
  LINE: and shuts his eyelids. The abyss goes almost completely dark. Now he’s alone in the dark. He cries in terror.
  EXPRESSION: Terrified
- CHARACTER: Narrator
  LINE: Chris hears a DEEP HULKING BREATHING in the darkness.
  EXPRESSION: Fearful
- CHARACTER: Chris
  LINE: Something’s down here...
  EXPRESSION: Terrified
- CHARACTER: Narrator
  LINE: No response.
  EXPRESSION: null
- CHARACTER: Chris
  LINE: Bring me back. Bring me back. Bring me back. Bring me back...
  EXPRESSION: Desperate
- CHARACTER: Narrator
  LINE: In the darkness, the SOUND OF HOOVES CRUNCHING ON SOFT GROUND approaches.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: THUNK THUNK. THUNK THUNK.
  EXPRESSION: null
- CHARACTER: Chris
  LINE: Bring me back. Bring me back. Bring me back.
  EXPRESSION: Desperate
- CHARACTER: Narrator
  LINE: The sounds get louder and louder.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: THUNK THUNK. THUNK THUNK.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: An antlered thing emerges from the shadow. It’s head is that of a deer, but with the flesh stripped off and with mostly its skull exposed.
  EXPRESSION: Horrified
- CHARACTER: Chris
  LINE: No!
  EXPRESSION: Terrified
- CHARACTER: Narrator
  LINE: Its eyes glow and flicker faint blue in its sockets. It MOANS A WRONG SOUNDING MOAN; in hateful anguish. It charges Chris...
  EXPRESSION: Menacing
- CHARACTER: Narrator
  LINE: THUNK THUNK. THUNK THUNK. THUNK THUNK.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The bloody deer impales Chris on its antlers. They both MOAN.
  EXPRESSION: Horrifying

::PATHS::
- CHOICE: "Wake up"
  TARGET: rose_bedroom_dawn
  STATE_CHANGE: fear = +5
  CONDITION: null

::SCENE::
LOCATION: Rose's Bedroom
MOOD: Disoriented
CHARACTERS: Chris, Narrator, Rose
BACKGROUND_IMAGE: rose_bedroom.png
BACKGROUND_EDIT: "Dawn, messy bed, Rose's bathroom"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Chris wakes up with a start in Rose’s bed sweaty and heaving. He’s alone and confused. Bad dream? Headache.
  EXPRESSION: Confused
- CHARACTER: Narrator
  LINE: The SHOWER RUNS inside Rose’s bathroom. SHE HUMS.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: DING DING
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: He’s gotten a message. It’s a picture of Rod pretending to pour beer in Sid’s mouth. Chris smiles. The batteries are low. He plugs his phone in and puts it on the dresser.
  EXPRESSION: Amused

::PATHS::
- CHOICE: "Go outside"
  TARGET: backyard_dawn
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Backyard
MOOD: Peaceful transitioning to unease
CHARACTERS: Chris, Narrator, Georgina, Walter
BACKGROUND_IMAGE: backyard.png
BACKGROUND_EDIT: "Golden hour, edge of forest, house in distance"

::SCRIPT::
- CHARACTER: Narrator
  LINE: It’s Golden hour. Beautiful. Chris walks through the yard to the edge of the forest with his camera.
  EXPRESSION: Calm
- CHARACTER: Narrator
  LINE: Chris keeps walking. He looks through a long-zoom lens into the wilderness. He sees a bird and snaps a picture.
  EXPRESSION: Focused
- CHARACTER: Narrator
  LINE: He turns to the house. Georgina can be seen through an upstairs window knitting. He raises his camera. She’s beautiful. She stands and begins to remove her wig. Then as if aware she’s being watched, she turns towards him. Chris turns away, taking a picture in another direction. He glances back at the window. Georgina is gone.
  EXPRESSION: Surprised
- CHARACTER: Narrator
  LINE: BANG. A sparrow slams against the gazebo and falls to the ground. Startling Chris.
  EXPRESSION: Startled
- CHARACTER: Chris
  LINE: Damn.
  EXPRESSION: Annoyed
- CHARACTER: Narrator
  LINE: He turns away and is startled even more by Walter smiling serenely at him about 50 feet away in the yard. Embarrassed, Chris gathers himself. He walks towards Walter.
  EXPRESSION: Startled
- CHARACTER: Chris
  LINE: What’s up?
  EXPRESSION: Casual
- CHARACTER: Narrator
  LINE: No response.
  EXPRESSION: null
- CHARACTER: Chris
  LINE: They working you good out here, huh?
  EXPRESSION: Casual
- CHARACTER: Narrator
  LINE: Walter’s voice is soft and methodical. His eyes remain distant as though he his looking through Chris. Chilling. There is a hidden anger behind his pleasantness.
  EXPRESSION: Chilling
- CHARACTER: Walter
  LINE: Nothing I don’t want to be doing.
  EXPRESSION: Calm
- CHARACTER: Chris
  LINE: Ha!
  EXPRESSION: Skeptical
- CHARACTER: Narrator
  LINE: Walter isn’t joking.
  EXPRESSION: null
- CHARACTER: Chris
  LINE: Yeah... yeah. No, I can tell. I never really got to meet you actually, up close. I’m Chris.
  EXPRESSION: Awkward
- CHARACTER: Walter
  LINE: I know who you are. You’re Rose’s friend.
  EXPRESSION: Calm
- CHARACTER: Narrator
  LINE: Chris stops walking about 15 feet from Walter. Something doesn’t feel right.
  EXPRESSION: Uneasy
- CHARACTER: Chris
  LINE: Yeah. That’s one way to put it. So, where you from originally?
  EXPRESSION: Inquisitive
- CHARACTER: Walter
  LINE: She is lovely isn’t she?
  EXPRESSION: Fond
- CHARACTER: Chris
  LINE: Rose? Yeah, she is...
  EXPRESSION: Agreeing
- CHARACTER: Walter
  LINE: One of a kind; a real doggone keeper.
  EXPRESSION: Admiring
- CHARACTER: Narrator
  LINE: Chris is weirded out.
  EXPRESSION: Weirded out
- CHARACTER: Walter
  LINE: Sorry if I scared you last night.
  EXPRESSION: Apologetic
- CHARACTER: Chris
  LINE: Oh, yeah. Actually, I guess I was pretty drunk. I don’t remember much.
  EXPRESSION: Hazy
- CHARACTER: Walter
  LINE: And the hypnosis? Did it work?
  EXPRESSION: Curious
- CHARACTER: Chris
  LINE: Hypnosis? No, I didn’t...
  EXPRESSION: Recalling
- CHARACTER: Narrator
  LINE: Chris remembers.
  EXPRESSION: null
- CHARACTER: Walter
  LINE: Well, I should get back to work.
  EXPRESSION: Resolute
- CHARACTER: Narrator
  LINE: Chris raises his hand in a timid ‘black power fist.’ Walter raises his hand in an open wave.
  EXPRESSION: null
- CHARACTER: Chris
  LINE: There’s another bird...
  EXPRESSION: Distracted
- CHARACTER: Walter
  LINE: nods.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Chris turns and walks to the house. Chris makes pops a cigarette into his mouth. He is repulsed by the taste of it. He looks at it. More of last night seems to come back to him.
  EXPRESSION: Troubled

::PATHS::
- CHOICE: "Enter the house"
  TARGET: rose_bedroom_day
  STATE_CHANGE: unease = +2
  CONDITION: null

::SCENE::
LOCATION: Rose's Bedroom
MOOD: Concerned
CHARACTERS: Chris, Narrator, Rose
BACKGROUND_IMAGE: rose_bedroom_day.png
BACKGROUND_EDIT: "Daytime, Rose blow drying hair"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Chris enters as Rose finishes blow drying her hair. He’s worked up.
  EXPRESSION: Agitated
- CHARACTER: Rose
  LINE: Hi. Where have you been?
  EXPRESSION: Curious
- CHARACTER: Chris
  LINE: Out. Taking pictures. Hey, so I think your mom hypnotised me last night.
  EXPRESSION: Hazy
- CHARACTER: Rose
  LINE: Wait, what?
  EXPRESSION: Surprised
- CHARACTER: Chris
  LINE: I think I snuck out for a smoke, and she caught me and offered? I don’t know. I must have agreed to it ‘cause the thing just made me nauseous.
  EXPRESSION: Hazy
- CHARACTER: Rose
  LINE: Okay. Well then that’s good, right?
  EXPRESSION: Reassuring
- CHARACTER: Chris
  LINE: No, not good. I can barely remember any of it even happening; I don’t like that. Plus I had these fucked up dreams.
  EXPRESSION: Upset
- CHARACTER: Rose
  LINE: That happened to me too.
  EXPRESSION: Sympathetic
- CHARACTER: Chris
  LINE: What did?
  EXPRESSION: Inquisitive
- CHARACTER: Rose
  LINE: The nightmares. When I was a kid. She hypnotized me once for stage fright, and I had the craziest nightmares, but it worked...
  EXPRESSION: Reflective
- CHARACTER: Narrator
  LINE: She wraps herself up in Chris’ arms. Chris thinks.
  EXPRESSION: null
- CHARACTER: Chris
  LINE: And, what’s the deal with the help?
  EXPRESSION: Suspicious
- CHARACTER: Rose
  LINE: Like... The iced tea thing? Yeah that was weird.
  EXPRESSION: Puzzled
- CHARACTER: Chris
  LINE: That, but also the lawn-mower guy creepin’ me the fuck out too.
  EXPRESSION: Uneasy
- CHARACTER: Rose
  LINE: Why? Did he say something?
  EXPRESSION: Concerned
- CHARACTER: Chris
  LINE: It’s not what he says, it’s how he says it. You know?
  EXPRESSION: Uneasy
- CHARACTER: Rose
  LINE: Yeah, something about them seems... different.
  EXPRESSION: Concerned
- CHARACTER: Narrator
  LINE: Out the window, A CAR DRIVES onto the front yard. Rose hears and looks.
  EXPRESSION: null
- CHARACTER: Rose
  LINE: They’re here.
  EXPRESSION: Expectant
- CHARACTER: Narrator
  LINE: Chris looks as well. A car parks on the front lawn. A Chauffer gets out and opens the backseat passenger door. A well-trained Husky service dog exits the car followed by JIM HUDSON, 57. Jim is blind and has slicked back grey hair.
  EXPRESSION: null

::PATHS::
- CHOICE: "Observe the arrival"
  TARGET: front_yard_noon
  STATE_CHANGE: anticipation = +1
  CONDITION: null

::SCENE::
LOCATION: Front Yard
MOOD: Grand Entrance
CHARACTERS: Narrator, Walter, Jim Hudson, Guests
BACKGROUND_IMAGE: front_yard.png
BACKGROUND_EDIT: "Noon, cars on lawn, guests arriving"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Bird's-eye view. Walter helps direct 12 expensive cars onto a makeshift parking lot on the front lawn. Wealthy guests emerge from each one.
  EXPRESSION: Grand

::PATHS::
- CHOICE: "Move to the party"
  TARGET: backyard_noon
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Backyard
MOOD: Festive
CHARACTERS: Narrator
BACKGROUND_IMAGE: backyard_party.png
BACKGROUND_EDIT: "Noon, outdoor party in full swing"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The party
  EXPRESSION: Festive

::SCENE::
LOCATION: PARTY
MOOD: Lively, Social
CHARACTERS: Narrator, Georgina, Rose, Chris, Missy, Gordon Greene, Emily Greene
BACKGROUND_IMAGE: party_interior.png
BACKGROUND_EDIT: "A bustling party, guests mingling, food being prepared in the background"

::SCRIPT::
- CHARACTER: Narrator
  LINE: is in full swing. The 30 or so guests mingle excitedly. They are all white except for one Japanese man.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Through the kitchen window, Georgina fixes food and helps occupy four white children by helping them make Hors d’oeuvres.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Rose and Chris get a drink at the bar. They walk through the party. Missy mingles with some guests. She makes eye contact with Chris and winks. He looks away.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Chris and Rose are stopped by GORDON GREENE, 68, and his wife EMILY GREENE, 67. Gordon is a cute man with a cane and impish excitement. Emily is pretty and birdlike. They watch Chris intently and smile from ear to ear. Gordon shakes Chris’ hand thoroughly.
  EXPRESSION: null
- CHARACTER: GORDON
  LINE: Nice to meet you, Chris. Nice to meet you indeed.
  EXPRESSION: Friendly
- CHARACTER: GORDON
  LINE: Good grip.
  EXPRESSION: Appreciative
- CHARACTER: CHRIS
  LINE: Thanks. You too.
  EXPRESSION: Polite
- CHARACTER: GORDON
  LINE: You ever play golf?
  EXPRESSION: Inquisitive
- CHARACTER: CHRIS
  LINE: Once, actually; a few years ago. I wasn’t very good.
  EXPRESSION: Modest
- CHARACTER: EMILY
  LINE: Gordon was a professional golfer for years.
  EXPRESSION: Proud
- CHARACTER: CHRIS
  LINE: Oh? No kidding.
  EXPRESSION: Surprised
- CHARACTER: GORDON
  LINE: Can’t quite swing the hips like I used to though. You know, I met Tiger.
  EXPRESSION: Nostalgic
- CHARACTER: Narrator
  LINE: Rose and Chris share a subtle smirk.
  EXPRESSION: Amused
- CHARACTER: ROSE
  LINE: Wow, that’s great. Cool.
  EXPRESSION: Sarcastic
- CHARACTER: CHRIS
  LINE: Wow, that’s great. Cool.
  EXPRESSION: Sarcastic
- CHARACTER: EMILY
  LINE: Gordon loves Tiger.
  EXPRESSION: Affectionate
- CHARACTER: GORDON
  LINE: Best I’ve ever seen. Ever, hands down. Let’s see your form.
  EXPRESSION: Enthusiastic
- CHARACTER: CHRIS
  LINE: Me? I could barely hit the thing.
  EXPRESSION: Hesitant
- CHARACTER: GORDON
  LINE: Show me...
  EXPRESSION: Encouraging
- CHARACTER: Narrator
  LINE: Chris does.
  EXPRESSION: null
- CHARACTER: GORDON
  LINE: If I knew what I know now at your age? Now then I could really play.
  EXPRESSION: Regretful
- CHARACTER: CHRIS
  LINE: It’d be kind of a waste of time travel though.
  EXPRESSION: Witty
- CHARACTER: Narrator
  LINE: They laugh.
  EXPRESSION: Amused

::SCENE::
LOCATION: Backyard
MOOD: Uncomfortable, Predatory
CHARACTERS: Narrator, Chris, Rose, Nelson Deets, Lisa Deets
BACKGROUND_IMAGE: backyard_later.png
BACKGROUND_EDIT: "Later, in the backyard, Chris and Rose are speaking with an elderly couple"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Chris and Rose speak to NELSON DEETS, 82, who’s smiles in a wheelchair with his jaw hanging, and LISA DEETS, 54, a loose-lipped trophy wife smiles at Chris in a predatory manner. They have Dutch accents.
  EXPRESSION: null
- CHARACTER: LISA
  LINE: (To Rose) How handsome is he?
  EXPRESSION: Bold
- CHARACTER: ROSE
  LINE: Extremely.
  EXPRESSION: Assertive
- CHARACTER: Narrator
  LINE: Lisa squeezes Chris’ bicep. A bit too familiar.
  EXPRESSION: null
- CHARACTER: LISA
  LINE: Not bad huh, Nelson?
  EXPRESSION: Provocative
- CHARACTER: NELSON
  LINE: Eh?
  EXPRESSION: Confused
- CHARACTER: LISA
  LINE: (to Rose) So, is it true? The love making. Is it better?
  EXPRESSION: Blunt
- CHARACTER: Narrator
  LINE: Rose cackles at the bluntness of the question. Chris almost chokes on his drink. Lisa continues to size Chris up.
  EXPRESSION: null
- CHARACTER: CHRIS
  LINE: Wow. Um..
  EXPRESSION: Flustered
- CHARACTER: LISA
  LINE: (to Rose) I’m being too forward?
  EXPRESSION: Playful
- CHARACTER: ROSE
  LINE: We’ll talk later.
  EXPRESSION: Amused
- CHARACTER: CHRIS
  LINE: Oh, will you now?
  EXPRESSION: Sarcastic

::SCENE::
LOCATION: Backyard
MOOD: Annoyed, Intellectualizing Race
CHARACTERS: Narrator, Chris, Rose, Parker Dray, April Dray
BACKGROUND_IMAGE: backyard_later_2.png
BACKGROUND_EDIT: "Later, in the backyard, Chris and Rose are speaking with another couple"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Chris and Rose talk to PARKER DRAY, 60, and APRIL DRAY, 57. They are an overweight, rose-cheeked tipsy wasp couple. Chris and Rose try to mask boredom and annoyance.
  EXPRESSION: null
- CHARACTER: APRIL
  LINE: Who even cares about skin color? My God.
  EXPRESSION: Dismissive
- CHARACTER: CHRIS
  LINE: Right. I mean--
  EXPRESSION: Agreeing
- CHARACTER: PARKER
  LINE: The world cares, April. But it’s not a question of physical superiority, it’s “What skin color is more culturally advantageous?”
  EXPRESSION: Dogmatic
- CHARACTER: Narrator
  LINE: As Parker drones on Chris looks around the party. Dean schmoozes animatedly with two couples. He quickly scans the party, finds Chris and points him out. The two couples wave and smile giddily. They had all just been talking about him. Chris pretends to not see this.
  EXPRESSION: null
- CHARACTER: ROSE
  LINE: “Advantageous?”
  EXPRESSION: Questioning
- CHARACTER: Narrator
  LINE: Suddenly, Chris sees another black guy walking through the crowd. Relief. It is Andre, the jogger from the first scene, but he’s very different than before. He seems glazed-over with the same frozen smile as Walter and Georgina, and wears a particularly square ascot and golfing hat.
  EXPRESSION: null
- CHARACTER: PARKER
  LINE: Fairer skin is has been in favor’ the last couple of thousands of years, but the pendulum has swung back again hasn't it..?
  EXPRESSION: Philosophical
- CHARACTER: CHRIS
  LINE: I’m sorry. I’m going to get another drink.
  EXPRESSION: Evasive
- CHARACTER: Narrator
  LINE: Chris walks away.
  EXPRESSION: null
- CHARACTER: PARKER
  LINE: I didn’t mean to offend him.
  EXPRESSION: Insecure
- CHARACTER: ROSE
  LINE: Really? ‘Cause you have yet to say anything that’s not a blanket statement about race.
  EXPRESSION: Confrontational
- CHARACTER: PARKER
  LINE: Now, Rose.--
  EXPRESSION: Appeasing

::SCENE::
LOCATION: Backyard Bar
MOOD: Eerie, Disconnected
CHARACTERS: Narrator, Chris, Andre/Logan, Phil
BACKGROUND_IMAGE: backyard_bar.png
BACKGROUND_EDIT: "Momenst later, Chris approaches Andre by the bar"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Andre stands by the bar and makes himself a Martini. Chris approaches him.
  EXPRESSION: null
- CHARACTER: CHRIS
  LINE: It’s good to see another brother around here.
  EXPRESSION: Hopeful
- CHARACTER: Narrator
  LINE: Andre turns to face Chris neatly. Andre’s voice is completely different from the first scene. There is no longer any trace of an urban dialect. He speaks in a lower pitch and slow, enunciating his words precisely.
  EXPRESSION: null
- CHARACTER: ANDRE
  LINE: Yes, of course it is.
  EXPRESSION: Monotone
- CHARACTER: Narrator
  LINE: Chris expects Andre to engage more. He doesn’t. He just stares at him smiling.
  EXPRESSION: null
- CHARACTER: CHRIS
  LINE: Who do you know?
  EXPRESSION: Inquiring
- CHARACTER: ANDRE
  LINE: Why, the Armitage’s of course. We’re friends of the family.
  EXPRESSION: Distant
- CHARACTER: Narrator
  LINE: PHIL, 65, a craggy effeminate man with manicured eyebrows, cuts between them.
  EXPRESSION: null
- CHARACTER: PHIL
  LINE: (to Andre) There you are. Here, put this somewhere.
  EXPRESSION: Possessive
- CHARACTER: Narrator
  LINE: Phil hands his napkin to Andre who pockets it obediently. Phil places his hand on Andre’s back possessively.
  EXPRESSION: null
- CHARACTER: PHIL
  LINE: (to Chris) Oh, hello. I’m Phil... and you are...?
  EXPRESSION: Condescending
- CHARACTER: CHRIS
  LINE: Chris. Rose’s boyfriend.
  EXPRESSION: Guarded
- CHARACTER: PHIL
  LINE: Fantastic. Logan and I know Rose very well.
  EXPRESSION: Superior
- CHARACTER: ANDRE
  LINE: I’m sorry, where are my manners. Logan, Logan King. (To Phil) Chris was just telling me that he felt more comfortable with my being here.
  EXPRESSION: Evasive
- CHARACTER: Narrator
  LINE: Chris is let down. Andre isn’t what he had hoped.
  EXPRESSION: null
- CHARACTER: PHIL
  LINE: That’s nice. Logan, I hate to tear you away, dear, but the Wincott’s were asking about you.
  EXPRESSION: Dismissive
- CHARACTER: ANDRE/LOGAN
  LINE: Ah, well it was nice meeting you Chris.
  EXPRESSION: Perfunctory
- CHARACTER: CHRIS
  LINE: Sure.
  EXPRESSION: Disappointed
- CHARACTER: Narrator
  LINE: Chris holds out his fist for Andre/Logan to bump. Andre/Logan shakes Chris’ fist and then, realizing his error fist bumps him like it’s the first time.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Andre/Logan and Phil laugh and walk away. They join a small group of people who applaud Andre’s arrival. Andre does a little spin showing off his clothes.
  EXPRESSION: null

::SCENE::
LOCATION: Backyard
MOOD: Agitated, Creeped Out
CHARACTERS: Narrator, Chris, Rose
BACKGROUND_IMAGE: backyard_later_3.png
BACKGROUND_EDIT: "Moments later, Chris returns to Rose"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Chris comes back to Rose. He is more creeped out and agitated.
  EXPRESSION: null
- CHARACTER: ROSE
  LINE: Where’s your drink?
  EXPRESSION: Concerned

::SCENE::
LOCATION: (Unspecified)
MOOD: Excitement
CHARACTERS: Dean, Crowd
BACKGROUND_IMAGE: crowd.png
BACKGROUND_EDIT: "Large gathering of people"

::SCRIPT::
- CHARACTER: Narrator
  LINE: What? Oh, I forgot.
  EXPRESSION: null
- CHARACTER: Dean
  LINE: Hello!
  EXPRESSION: Cheerful
- CHARACTER: Narrator
  LINE: Everyone applauds and gives Dean their attention.
  EXPRESSION: null
- CHARACTER: Dean
  LINE: Achem! Once again, I want to thank you all for coming. Words cannot express how much it means to us that after all these years we can all still get together and share. I’m reminded of stories of how the knights of old would gather in honor of a new crusade...
  EXPRESSION: Sincere

::SCENE::
LOCATION: Gazebo
MOOD: Secrecy
CHARACTERS: Chris, Jim, Seeing Eye Dog
BACKGROUND_IMAGE: gazebo.png
BACKGROUND_EDIT: "Daytime, outdoor gazebo"

::SCRIPT::
- CHARACTER: Narrator
  LINE: During Dean’s speech, Chris wanders away from the group.
  EXPRESSION: null
- CHARACTER: Jim
  LINE: Ignorant shit...
  EXPRESSION: Angry
- CHARACTER: Narrator
  LINE: Chris hadn’t seen Jim Hudson, the blind man, who sits in the gazebo with his seeing eye dog. He is close to Chris, but far enough away from the group that no one else hears them.
  EXPRESSION: null
- CHARACTER: Chris
  LINE: Who?
  EXPRESSION: Confused
- CHARACTER: Jim
  LINE: All of them. Ignorant assholes. They have no idea what real people go through.
  EXPRESSION: Bitter
- CHARACTER: Chris
  LINE: I guess people only see what’s in front of them.
  EXPRESSION: Thoughtful
- CHARACTER: Narrator
  LINE: Chris notices his faux pas.
  EXPRESSION: null
- CHARACTER: Chris
  LINE: I mean...
  EXPRESSION: Embarrassed
- CHARACTER: Jim
  LINE: Heh. No, you’re right. And usually not even that much. That’s people.
  EXPRESSION: Cynical
- CHARACTER: Narrator
  LINE: Jim holds a glass up. Chris fist bumps the glass.
  EXPRESSION: null
- CHARACTER: Jim
  LINE: Jim Hudson.
  EXPRESSION: Casual
- CHARACTER: Chris
  LINE: Chris-
  EXPRESSION: Hesitant
- CHARACTER: Jim
  LINE: I know who you are. I’m an admirer of your work; you have a great eye...
  EXPRESSION: Appreciative
- CHARACTER: Chris
  LINE: Wait. Jim Hudson... of Hudson Galleries?
  EXPRESSION: Surprised
- CHARACTER: Jim
  LINE: The irony of being a blind art dealer isn’t lost on me.
  EXPRESSION: Amused
- CHARACTER: Chris
  LINE: How do you do it?
  EXPRESSION: Curious
- CHARACTER: Jim
  LINE: I have an assistant describe work to me. You’ve got something... The images you capture... so brutally melancholic. Powerful stuff.
  EXPRESSION: Serious
- CHARACTER: Chris
  LINE: Thank you. Yeah, I just like finding the beauty in abandoned things.
  EXPRESSION: Humble
- CHARACTER: Jim
  LINE: I used to dabble myself. Wilderness mostly. I submitted to Nat Geo 14 times before realizing I didn’t have “the eye” for it; Began dealing. And then, of course, my vision went to shit.
  EXPRESSION: Resigned
- CHARACTER: Chris
  LINE: Damn.
  EXPRESSION: Sympathetic
- CHARACTER: Jim
  LINE: I know. Life can be a sick joke. One day you're working in a dark room, and the next day - BAM. You wake up in the dark. Genetic disease.
  EXPRESSION: Bitter
- CHARACTER: Chris
  LINE: Shit ain’t fair, man.
  EXPRESSION: Frustrated
- CHARACTER: Jim
  LINE: Yeah.
  EXPRESSION: Resigned
- CHARACTER: Narrator
  LINE: Jeremy comes over with his preppy friend, Derrick, 29.
  EXPRESSION: null
- CHARACTER: Jeremy
  LINE: Chris, we need you...
  EXPRESSION: Urgent
- CHARACTER: Chris
  LINE: Yeah, sure. Nice to meet you.
  EXPRESSION: Polite
- CHARACTER: Jim
  LINE: Stop by the gallery some time. Bout time you had a solo show.
  EXPRESSION: Encouraging
- CHARACTER: Chris
  LINE: Really? Wow, okay. Thank you. That would be a game changer.
  EXPRESSION: Excited
- CHARACTER: Jim
  LINE: I think we could do wonderful things together.
  EXPRESSION: Confident

::SCENE::
LOCATION: Backyard
MOOD: Playful Competition
CHARACTERS: Chris, Rose, Jeremy, Derrick, Party Guests
BACKGROUND_IMAGE: backyard.png
BACKGROUND_EDIT: "Daytime, outdoor backyard party"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Chris and Rose play badminton against Jeremy and Derrick. A gaggle of party guests watch, entertained. Chris is actually having fun. He swings big but misses the shuttlecock.
  EXPRESSION: null
- CHARACTER: Jeremy
  LINE: HA! Come on. You can do better than that!
  EXPRESSION: Teasing
- CHARACTER: Chris
  LINE: Not my game, what can I say.
  EXPRESSION: Shrugging
- CHARACTER: Jeremy
  LINE: Yeah, I see that.
  EXPRESSION: Sarcastic
- CHARACTER: Rose
  LINE: Shut up Jeremy.
  EXPRESSION: Protective
- CHARACTER: Jeremy
  LINE: I’m just saying, if your boy isn’t gonna bring his ‘A’ game, we might as well bring Mom up here.
  EXPRESSION: Provocative
- CHARACTER: Chris
  LINE: Whoa, whoa, okay. Now we talkin’ smack huh?
  EXPRESSION: Challenging
- CHARACTER: Narrator
  LINE: Chris serves the shuttlecock hard. The following rally is long, captivating the crowd. Chris ends it with an impressive diving swat. Derrick misses the return and the crowd goes wild. Chris throws his arms up in celebration.
  EXPRESSION: null
- CHARACTER: Chris
  LINE: Boom!
  EXPRESSION: Victorious
- CHARACTER: Rose
  LINE: Yay, baby!
  EXPRESSION: Excited
- CHARACTER: Jeremy
  LINE: See, that’s what I’m talking about!!! Okay, again!
  EXPRESSION: Enthusiastic
- CHARACTER: Narrator
  LINE: Chris is about to serve. He scans the crowd of beaming faces. Everyone is rooting for Chris. They love him. Chris scans the crowd. It’s too much.
  EXPRESSION: null
- CHARACTER: Chris
  LINE: Hold up. Here.
  EXPRESSION: Distracted
- CHARACTER: Rose
  LINE: Where are you--
  EXPRESSION: Confused
- CHARACTER: Chris
  LINE: I’m gonna go to the bathroom.
  EXPRESSION: Evasive
- CHARACTER: Narrator
  LINE: Chris gives his racket to Gordon Greene.
  EXPRESSION: null

::SCENE::
LOCATION: Armitage House - Kitchen
MOOD: Transition
CHARACTERS: Chris
BACKGROUND_IMAGE: kitchen.png
BACKGROUND_EDIT: "Daytime interior of a house kitchen"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Chris walks through the kitchen.
  EXPRESSION: null

::SCENE::
LOCATION: Armitage Living Room
MOOD: Suspense
CHARACTERS: Chris, Guests
BACKGROUND_IMAGE: living_room.png
BACKGROUND_EDIT: "Daytime interior of a house living room"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Chris slips past several small groups of guests mingling. He goes up the stairs to the second floor.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: As soon as he are out of sight and earshot, the mingling guests stop in mid-conversation. Everyone in the room waits and listens to CHRIS’ FOOTSTEPS above.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: It is now clear that their conversations have been fake. They are all hanging on Chris’ actions.
  EXPRESSION: null

::SCENE::
LOCATION: Armitage Upstairs Hallway
MOOD: Exploration
CHARACTERS: Chris
BACKGROUND_IMAGE: upstairs_hallway.png
BACKGROUND_EDIT: "Daytime interior of a house upstairs hallway"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Chris walks to Rose’ room.
  EXPRESSION: null

::SCENE::
LOCATION: Rose's Bedroom
MOOD: Unease
CHARACTERS: Chris
BACKGROUND_IMAGE: rose_bedroom.png
BACKGROUND_EDIT: "Daytime interior of a bedroom"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Chris exits the bathroom in Rose’s room. The bed is made. He picks his phone up from the dresser. It’s unplugged and out of batteries. That’s odd. He plugs it in again as he hears a CREAK down the hall.
  EXPRESSION: null

::SCENE::
LOCATION: Armitage Upstairs Hallway
MOOD: Suspicion
CHARACTERS: Chris, Georgina
BACKGROUND_IMAGE: upstairs_hallway.png
BACKGROUND_EDIT: "Daytime interior of a house upstairs hallway"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Chris leaves Rose’s room. A door at the end of the hallway is a crack open. Chris slowly walks down the hall, and peers inside. A couple lacrosse trophies and one for ju-jitsu. Jeremy’s room. Movement inside. It’s Georgina making the bed. The door creaks alerting her of his presence, she turns slowly. Before she sees him he walks quickly back to Rose’s room just as she comes upstairs.
  EXPRESSION: null

::SCENE::
LOCATION: Rose's Bedroom
MOOD: Confrontation
CHARACTERS: Chris, Rose
BACKGROUND_IMAGE: rose_bedroom.png
BACKGROUND_EDIT: "Daytime interior of a bedroom"

::SCRIPT::
- CHARACTER: Rose
  LINE: Hey! You okay?
  EXPRESSION: Concerned
- CHARACTER: Narrator
  LINE: Chris waves for her to join him back in her room.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Chris speaks quietly and frantically to Rose.
  EXPRESSION: null
- CHARACTER: Chris
  LINE: The housekeeper unplugged my phone.
  EXPRESSION: Frantic
- CHARACTER: Rose
  LINE: Sighs. “Not this again.”
  EXPRESSION: Exasperated
- CHARACTER: Chris
  LINE: I’m trying to check in with Rod, and I got no juice.
  EXPRESSION: Worried
- CHARACTER: Rose
  LINE: I’m sure it was an honest mistake.
  EXPRESSION: Reassuring
- CHARACTER: Chris
  LINE: Yeah, or maybe not. Maybe she doesn’t like the fact that I’m with you.
  EXPRESSION: Suspicious
- CHARACTER: Rose
  LINE: Chris...
  EXPRESSION: Doubtful
- CHARACTER: Chris
  LINE: What? It’s a thing.
  EXPRESSION: Insistent
- CHARACTER: Rose
  LINE: You think my family’s housekeeper gives a shit who you’re with? That’s crazy bae.
  EXPRESSION: Dismissive
- CHARACTER: Chris
  LINE: Forget it. Nevermind.
  EXPRESSION: Defeated
- CHARACTER: Rose
  LINE: Look, I get it. This whole thing is stres
  EXPRESSION: Empathetic

::SCENE::
LOCATION: Chris' Apartment
MOOD: Tense
CHARACTERS: Narrator, Rose, Chris
BACKGROUND_IMAGE: chris_apartment_interior.png
BACKGROUND_EDIT: "Interior of Chris' apartment, daytime. Rose is speaking to Chris."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Sful. I mean, they’re circling you like hyenas down there. I just don’t get why you’re taking it out on George and Walter.
  EXPRESSION: null
- CHARACTER: Chris
  LINE: You’re right. I’m being paranoid. I just need a minute and I’ll be down.
  EXPRESSION: passive aggressive
- CHARACTER: Narrator
  LINE: Rose leaves a little annoyed.
  EXPRESSION: null

::PATHS::
- CHOICE: "Rose leaves"
  TARGET: chris_apartment_rod_call
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Chris' Apartment
MOOD: Casual
CHARACTERS: Narrator, Rod, Sid
BACKGROUND_IMAGE: chris_apartment_couch.png
BACKGROUND_EDIT: "Interior of Chris' apartment, daytime. Rod is on the couch eating a cheeseburger and watching TV with a dog."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Rod eats a cheeseburger and watches a true crime show on Chris’ couch with Sid the dog. His PHONE RINGS.
  EXPRESSION: null
- CHARACTER: Rod
  LINE: Hey.
  EXPRESSION: null

::PATHS::
- CHOICE: "Answer phone"
  TARGET: rose_room_intercut
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Rose's Room
MOOD: Uneasy
CHARACTERS: Narrator, Chris, Rod
BACKGROUND_IMAGE: rose_room_interior.png
BACKGROUND_EDIT: "Interior of Rose's room, daytime. Chris is looking out the window."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Chris is alone in Rose’s room. He peers out the window.
  EXPRESSION: null
- CHARACTER: Chris
  LINE: Bruh. What’s up?
  EXPRESSION: null
- CHARACTER: Rod
  LINE: Not much. Sid’s chillin’. We eatin’ burgers. What’s up with you?
  EXPRESSION: null
- CHARACTER: Chris
  LINE: Yeah...
  EXPRESSION: null
- CHARACTER: Rod
  LINE: Uh oh. That doesn’t sound good.
  EXPRESSION: null
- CHARACTER: Chris
  LINE: They just got me over here meeting all the family friends. It’s like they never met a black dude that doesn’t work for them or some shit.
  EXPRESSION: null
- CHARACTER: Rod
  LINE: Oh, they got you on display?
  EXPRESSION: null
- CHARACTER: Chris
  LINE: Exactly. Also, I got hypnotised last night...
  EXPRESSION: null
- CHARACTER: Rod
  LINE: Nigga, what the fuck? Oh, Hell no!
  EXPRESSION: Shocked
- CHARACTER: Chris
  LINE: Yeah, to quit smoking. Rose’s mom is a hypnotherapist--
  EXPRESSION: null
- CHARACTER: Rod
  LINE: --Nope. I don’t give a fuck if she’s Dr. Drew up in this bitch. You ain’t getting in my head.
  EXPRESSION: Angry
- CHARACTER: Chris
  LINE: Right.
  EXPRESSION: null
- CHARACTER: Rod
  LINE: Who knows what they’ll make you do. You know white people into some crazy sex slave shit.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Chris laughs.
  EXPRESSION: null
- CHARACTER: Chris
  LINE: Yeah, I’m like 99% sure they’re not a kinky sex family, but-
  EXPRESSION: null
- CHARACTER: Rod
  LINE: Why not? Jeffery Dahmer ate niggas’ heads, but that was after he fucked the heads. You think they saw that shit coming? Hell no. One second they think they just gonna suck some dick, next second they sucking dick but their head isn’t on their body Chris.
  EXPRESSION: null
- CHARACTER: Chris
  LINE: And thanks for that image, right there.
  EXPRESSION: null
- CHARACTER: Rod
  LINE: I saw that on A&E, so that’s real life.
  EXPRESSION: null
- CHARACTER: Chris
  LINE: It’s the black people out here that are the weirdest. The help. It’s like they’re possessed or...
  EXPRESSION: null
- CHARACTER: Rod
  LINE: Hypnotised.
  EXPRESSION: null
- CHARACTER: Chris
  LINE: Ha ha--
  EXPRESSION: dry
- CHARACTER: Rod
  LINE: I’m just connecting the dots you presenting me with. The mom puttin’ trances on niggas and fuckin’ them. It’s clear as day and that’s fucked up. She hot?
  EXPRESSION: null
- CHARACTER: Chris
  LINE: What’s fucked up is: You’re the first line of defense against terrorism.
  EXPRESSION: null
- CHARACTER: Rod
  LINE: This is good shit tho.
  EXPRESSION: null
- CHARACTER: Chris
  LINE: Oh, and the one other black guest is like the whitest-most dude at the party.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Rod laughs.
  EXPRESSION: null
- CHARACTER: Chris
  LINE: I mean Rod, if you could see what this dude is wearing.
  EXPRESSION: null
- CHARACTER: Rod
  LINE: Send me a picture. You are a photographer. You should be documentin’ this shit.
  EXPRESSION: null
- CHARACTER: Chris
  LINE: Aiight. I’ll try.
  EXPRESSION: amused
- CHARACTER: Rod
  LINE: And yo, don’t say I didn’t warn you ‘cause my ass sure as Hell ain’t coming up to the country to save you from no fuckin’ witch coven... Unless the mom’s hot. She hot?
  EXPRESSION: null
- CHARACTER: Chris
  LINE: Thanks Rod, bye.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Chris hangs up and brings his phone with him. He opens the door. Georgina stands right outside it, eerie smile and all. Chris is startled.
  EXPRESSION: null

::PATHS::
- CHOICE: "Hang up phone"
  TARGET: georgina_encounter
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Hallway outside Chris' Room
MOOD: Eerie
CHARACTERS: Narrator, Chris, Georgina
BACKGROUND_IMAGE: hallway_outside_chris_room.png
BACKGROUND_EDIT: "Hallway outside Chris' room. Georgina is standing by the door."

::SCRIPT::
- CHARACTER: Georgina
  LINE: Hello.
  EXPRESSION: null
- CHARACTER: Chris
  LINE: Hi.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Georgina’s voice is shaky and careful.
  EXPRESSION: null
- CHARACTER: Georgina
  LINE: I owe you an apology. I shouldn’t be touching things that don’t belong to me.
  EXPRESSION: null
- CHARACTER: Chris
  LINE: Oh, no. It’s cool. I was just confused.
  EXPRESSION: null
- CHARACTER: Georgina
  LINE: I lifted your cellular phone this morning to wipe down the dresser and it accidentally came undone, see?
  EXPRESSION: null
- CHARACTER: Chris
  LINE: Yeah, I--
  EXPRESSION: null
- CHARACTER: Georgina
  LINE: Rather than meddle with it further, I left it that way.
  EXPRESSION: null
- CHARACTER: Chris
  LINE: Really, it’s okay. I didn’t mean to rat you out.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Georgina eyes get lost for a moment. There’s a pain behind her smile.
  EXPRESSION: null
- CHARACTER: Chris
  LINE: ...get you in trouble.
  EXPRESSION: null
- CHARACTER: Georgina
  LINE: Oh no, no, no, no, no, no... Aren’t you the sweetest thing? Not at all. The Armitages are so good to us; They treat us like family.
  EXPRESSION: null

::PATHS::
- CHOICE: "Enter the backyard"
  TARGET: backyard_afternoon
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Backyard
MOOD: Awkward Interrogation
CHARACTERS: Narrator, Chris, Dean, David, Marcia, Ronald, Celia, Hiroki, Fredrich, Jessika
BACKGROUND_IMAGE: backyard_afternoon.png
BACKGROUND_EDIT: "Backyard, afternoon. Chris is being introduced to a group of people."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Chris walks back into the back yard where Dean entertains seven people Chris hasn’t met. They turn as Chris approaches smiling eagerly. They all seem to share a private joke.
  EXPRESSION: null
- CHARACTER: Dean
  LINE: Chris! There you are. I wanted to introduce you to some old friends. We’ll do it quickly. Down the line: David and Marcia Wincott, Ronald and Celia Jeffries, Hiroki Tanaka, and Fredrich and Jessika Walden.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Each couple - DAVID and MARCIA, RONALD and CELIA, HIROKI, FREDRICH and JESSIKA - waves as they are named.
  EXPRESSION: null
- CHARACTER: Chris
  LINE: Too many names to remember but...
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The couples all laugh nervously.
  EXPRESSION: null
- CHARACTER: Hiroki
  LINE: Can we ask him questions?
  EXPRESSION: null
- CHARACTER: Dean
  LINE: Of course.
  EXPRESSION: null
- CHARACTER: Hiroki
  LINE: Do you find that being African American has more advantages or disadvantages in the modern world?
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Chris pans the crowd who all give him their undivided attention. The silence is long. Chris sighs. He looks for Rose. She is off talking to someone.
  EXPRESSION: null
- CHARACTER: Chris
  LINE: Yeah, I don’t know, man.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: They all smile like hungry vampires. Chris is very uncomfortable with this unprovoked group interrogation. Andre/ Logan and Phil approach.
  EXPRESSION: null
- CHARACTER: Chris
  LINE: That’s actually a great question. Logan! They were asking me about the African American experience. Maybe you could take this one.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Andre/Logan is a little caught off guard but dives in.
  EXPRESSION: null
- CHARACTER: Andre/Logan
  LINE: My life as an African American has been, for the most part, very good. It’s hard to be too specific as I haven’t much desired to leave the house in a while.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The crowd chuckles. Chris takes out his phone.
  EXPRESSION: null
- CHARACTER: Phil
  LINE: We’ve become homebodies...
  EXPRESSION: null
- CHARACTER: Andre/Logan
  LINE: But recently, even when you go to the city, I’ve just had no interest.
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue conversation"
  TARGET: continuation
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Backyard
MOOD: Tension
CHARACTERS: Narrator, Chris, Andre/Logan, Phil, Jeremy, Missy, Dean
BACKGROUND_IMAGE: backyard_party.png
BACKGROUND_EDIT: "Afternoon, lively party, people gathered"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The chores are my sanctu--
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: With the attention on Andre/Logan, Chris subtly backs away from the conversation. He raises his phone toward Andre/Logan and the group and snaps a picture. The FLASH POPS.
  EXPRESSION: null
- CHARACTER: Chris
  LINE: Shit.
  EXPRESSION: Startled
- CHARACTER: Narrator
  LINE: Everyone turns to Chris. Andre/Logan steps forward and looks at Chris oddly; His head cocks a little and his peaceful expression drifts slowly to maddened horror. Some of the party guests gasp.
  EXPRESSION: null
- CHARACTER: Phil
  LINE: Logan?
  EXPRESSION: Concerned
- CHARACTER: Narrator
  LINE: Andre/Logan drops his glass and stumbles towards Chris. Chris backs up, but Andre is already up in his space.
  EXPRESSION: null
- CHARACTER: Andre
  LINE: Get out.
  EXPRESSION: Angry
- CHARACTER: Narrator
  LINE: Andre/Logan’s voice is higher and scratchy, like it was in the first scene.
  EXPRESSION: null
- CHARACTER: Chris
  LINE: Hey, man, I’m sorry, I--
  EXPRESSION: Apologetic
- CHARACTER: Andre
  LINE: Get the fuck out of here!!!!
  EXPRESSION: Furious
- CHARACTER: Narrator
  LINE: Andre/Logan grabs Chris by the shoulders and screams shrilly. Blood trickles out of his nose.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Phil and Jeremy grab Andre. They have to pry Andre/Logan’s grip off of Chris. When they do Andre/Logan screams bloodcurdlingly. It takes all their strength to bring him into the house. Missy and Dean follow.
  EXPRESSION: null

::PATHS::
- CHOICE: "Follow them inside"
  TARGET: living_room_afternoon
  STATE_CHANGE: fear = +2, confusion = +1
  CONDITION: null

::SCENE::
LOCATION: Living Room
MOOD: Shocked, Concerned
CHARACTERS: Narrator, Rose, Chris, Dean, Andre/Logan, Missy, Phil
BACKGROUND_IMAGE: living_room_afternoon.png
BACKGROUND_EDIT: "Afternoon, Rose is crying on the couch, other guests present"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Rose sits on the couch. She’s been crying. Chris comforts her but is clearly traumatised. A few other concerned guests mill around. Dean enters everyone gives him their attention.
  EXPRESSION: null
- CHARACTER: Rose
  LINE: What the Hell was that?
  EXPRESSION: Distraught
- CHARACTER: Dean
  LINE: It was a seizure.
  EXPRESSION: Calm
- CHARACTER: Rose
  LINE: A seizure?
  EXPRESSION: Disbelieving
- CHARACTER: Dean
  LINE: Yes. Logan’s okay. Missy’s with him now. Are you okay Chris?
  EXPRESSION: Reassuring
- CHARACTER: Chris
  LINE: Yeah. Why did he come at me like that?
  EXPRESSION: Confused
- CHARACTER: Rose
  LINE: Yeah seizures don’t make people attack people, I’m sorry.
  EXPRESSION: Skeptical
- CHARACTER: Dean
  LINE: It was an abnormal manifestation but yes, actually, sometimes they do. The flash on your phone must have triggered it.
  EXPRESSION: Explanatory
- CHARACTER: Narrator
  LINE: Andre/Logan enters with stands with Missy and Phil to a smattering of concerned applause. He addresses a group in his lower pitched “Logan” voice.
  EXPRESSION: null
- CHARACTER: Andre/Logan
  LINE: Well, I do believe I owe you all an apology.
  EXPRESSION: Apologetic
- CHARACTER: Narrator
  LINE: The group grumbles.
  EXPRESSION: null
- CHARACTER: Missy
  LINE: We’re just glad you’re feeling yourself again.
  EXPRESSION: Relieved
- CHARACTER: Andre/Logan
  LINE: Well yes I am. It’s quite like being trapped in a dark room and watching my experiences through a window. Thank God you and Dean were here to calm me down.
  EXPRESSION: Grateful
- CHARACTER: Dean
  LINE: It’s a simple glitch of the brain. Nothing to be afraid of.
  EXPRESSION: Reassuring
- CHARACTER: Andre/Logan
  LINE: I know I scared you all quite a bit.. especially you Chris.
  EXPRESSION: Apologetic
- CHARACTER: Chris
  LINE: No, I’m sorry about the flash. I didn’t know.
  EXPRESSION: Remorseful
- CHARACTER: Andre/Logan
  LINE: Of course. How could you have?
  EXPRESSION: Understanding
- CHARACTER: Phil
  LINE: You shouldn’t have been drinking either.
  EXPRESSION: Joking
- CHARACTER: Narrator
  LINE: The group chuckles.
  EXPRESSION: null
- CHARACTER: Andre/Logan
  LINE: As I said I’m feeling much better now, but you’ll all have to proceed without the aid of my marvellous wit; the whole thing has left me a quite a bit exhausted.
  EXPRESSION: Tired
- CHARACTER: Dean
  LINE: Of course.
  EXPRESSION: Understanding
- CHARACTER: Andre/Logan
  LINE: It was nice meeting you.
  EXPRESSION: Polite
- CHARACTER: Chris
  LINE: Yeah, you too.
  EXPRESSION: Skeptical
- CHARACTER: Narrator
  LINE: Chris is skeptical. Missy shows Phil and Logan out. Andre and Phil leave.
  EXPRESSION: null
- CHARACTER: Dean
  LINE: Let’s do sparklers shall we? Brighten the mood?
  EXPRESSION: Enthusiastic
- CHARACTER: Narrator
  LINE: He gives Chris and Rose sparklers and to other people who light them.
  EXPRESSION: null
- CHARACTER: Rose
  LINE: Let’s go.
  EXPRESSION: Determined
- CHARACTER: Narrator
  LINE: Rose takes Chris’ hand.
  EXPRESSION: null
- CHARACTER: Missy
  LINE: Anybody need a drink?
  EXPRESSION: Sociable
- CHARACTER: Rose
  LINE: We’re going on a walk.
  EXPRESSION: Firm
- CHARACTER: Narrator
  LINE: Rose grabs Chris’ hand and leads him out the front door. The party guests in the living room, Dean and Missy included, go silent. As their sparklers burn they approach the window, watching Rose and Chris leave the front yard.
  EXPRESSION: null

::PATHS::
- CHOICE: "Follow Rose and Chris"
  TARGET: lakeside_afternoon
  STATE_CHANGE: curiosity = +1, suspicion = +1
  CONDITION: null

::SCENE::
LOCATION: Lakeside
MOOD: Reflective, Uneasy
CHARACTERS: Narrator, Rose, Chris
BACKGROUND_IMAGE: lakeside_afternoon.png
BACKGROUND_EDIT: "Afternoon, walking by a lake, sparklers fizzling out"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Rose and Chris walk by the lake. Their sparklers fizzle.
  EXPRESSION: null
- CHARACTER: Chris
  LINE: My cousin is epileptic. That wasn’t a seizure.
  EXPRESSION: Certain
- CHARACTER: Rose
  LINE: Honestly? That was one of the strangest things I’ve ever seen in my life.
  EXPRESSION: Astounded
- CHARACTER: Chris
  LINE: Also, this is gonna sound weird, but when he got up in my face like that, I got the feeling like I knew that guy.
  EXPRESSION: Puzzled

::PATHS::
- CHOICE: "Discuss the situation further"
  TARGET: lakeside_same_time_continued
  STATE_CHANGE: trust = +1, unease = +1
  CONDITION: null

::SCENE::
LOCATION: Back Yard
MOOD: Mysterious, Commercial
CHARACTERS: Narrator, Dean, Party Guests, The Waldens, Gordon Greene
BACKGROUND_IMAGE: backyard_auction.png
BACKGROUND_EDIT: "Afternoon, party guests gathered in the back yard facing Dean"

::SCRIPT::
- CHARACTER: Narrator
  LINE: With Chris and Rose away, the party guests have all gathered in the back yard facing Dean who stands by a large picture of Chris on an easel. Everyone is silent.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Dean raises his hand and makes numbers with his fingers: “Three and three.” Several party guests raise their hands. Dean points to the Waldens.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: This is an auction.
  EXPRESSION: null

::PATHS::
- CHOICE: "Observe the auction"
  TARGET: backyard_same_time_auction
  STATE_CHANGE: intrigue = +2, suspicion = +2
  CONDITION: null

::SCENE::
LOCATION: Lakeside
MOOD: Frustrated, Uncertain
CHARACTERS: Narrator, Rose, Chris
BACKGROUND_IMAGE: lakeside_same_time.png
BACKGROUND_EDIT: "Afternoon, continuing walk by the lake"

::SCRIPT::
- CHARACTER: Chris
  LINE: Let’s go back home tonight.
  EXPRESSION: Urgent
- CHARACTER: Rose
  LINE: What? Wait, no.
  EXPRESSION: Surprised
- CHARACTER: Chris
  LINE: I’m just... Something doesn’t feel right.
  EXPRESSION: Uneasy
- CHARACTER: Rose
  LINE: You mean with us?
  EXPRESSION: Questioning
- CHARACTER: Chris
  LINE: No. With this whole situation! I just... I can’t explain but I need you to trust me. Let’s just go. It doesn’t even have to be a big deal.
  EXPRESSION: Pleading
- CHARACTER: Rose
  LINE: It is a big deal. It’s my family. I wouldn’t even know what to tell them.
  EXPRESSION: Resolute

::PATHS::
- CHOICE: "Persist in leaving"
  TARGET: lakeside_same_time_continued_persistence
  STATE_CHANGE: frustration = +1, confusion = +1
  CONDITION: null
- CHOICE: "Stay with Rose"
  TARGET: lakeside_same_time_continued_stay
  STATE_CHANGE: compromise = +1, suspicion = +1
  CONDITION: null

::SCENE::
LOCATION: Backyard
MOOD: Commercial, Transactional
CHARACTERS: Narrator, Dean, Gordon Greene
BACKGROUND_IMAGE: backyard_auction_update.png
BACKGROUND_EDIT: "Afternoon, Dean continues the auction"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Dean raises his hand again making more numbers with his fingers: “4, 5.” Gordon Greene raises his hand. Dean points to him accepting his bid.
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue observing"
  TARGET: lakeside_same_time_continued_auction
  STATE_CHANGE: intrigue = +1, suspicion = +1
  CONDITION: null

::SCENE::
LOCATION: Lakeside
MOOD: Emotional, Conflicted
CHARACTERS: Narrator, Rose, Chris
BACKGROUND_IMAGE: lakeside_emotional.png
BACKGROUND_EDIT: "Afternoon, continuing to walk by the lake"

::SCRIPT::
- CHARACTER: Rose
  LINE: Yes, it’s weird. There are a lot of ways I wish this was going different. I wish my brother wasn’t a cock. I wish my parents friends were chill; but just because it’s tough, it doesn’t mean you run away...
  EXPRESSION: Emotional
- CHARACTER: Narrator
  LINE: Rose cries.
  EXPRESSION: null
- CHARACTER: Chris
  LINE: Baby, I--
  EXPRESSION: Tender
- CHARACTER: Rose
  LINE: ...I’m late.
  EXPRESSION: Hesitant
- CHARACTER: Chris
  LINE: Late?
  EXPRESSION: Confused
- CHARACTER: Rose
  LINE: I should’ve got my period like last week.
  EXPRESSION: Uncertain
- CHARACTER: Chris
  LINE: Oh.
  EXPRESSION: Surprised
- CHARACTER: Rose
  LINE: I mean, I did change my birth control, so it could just be that, but...
  EXPRESSION: Tentative
- CHARACTER: Narrator
  LINE: Chris thinks silently.
  EXPRESSION: null
- CHARACTER: Rose
  LINE: So...?
  EXPRESSION: Expectant
- CHARACTER: Chris
  LINE: I don’t know what to say.
  EXPRESSION: Speechless
- CHARACTER: Rose
  LINE: Okay... Try any emotional response whatsoever.
  EXPRESSION: Frustrated
- CHARACTER: Narrator
  LINE: He’s silent. Rose wipes her tears.
  EXPRESSION: null
- CHARACTER: Rose
  LINE: If you wanna go then go. I’m not going to force you to stay but I’m not leaving.
  EXPRESSION: Resigned

::PATHS::
- CHOICE: "Respond to Rose"
  TARGET: response_to_rose
  STATE_CHANGE: relationship_status = uncertain, decision_pending = true
  CONDITION: null

::SCENE::
LOCATION: Inside Auction Tent
TIME: Day
CHARACTERS: Dean, Mr. Greene, Mrs. Deets, Jim Hudson, Jim's Chauffeur, Guests
BACKGROUND_IMAGE: auction_tent_day.png
BACKGROUND_EDIT: "Bustling auction tent, focus on the auctioneer"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The auction is flying now. Dean’s hand signals are going fast. It’s down to three couples.
  EXPRESSION: null
- CHARACTER: Dean
  LINE: “5, 6.”
  EXPRESSION: null
- CHARACTER: Mr. Greene
  LINE: (Raises hand)
  EXPRESSION: null
- CHARACTER: Dean
  LINE: “5, 8.”
  EXPRESSION: null
- CHARACTER: Mrs. Deets
  LINE: (Raises hand)
  EXPRESSION: null
- CHARACTER: Dean
  LINE: “6.”
  EXPRESSION: null
- CHARACTER: Jim Hudson
  LINE: (Raises both hands, signals “10.”)
  EXPRESSION: null
- CHARACTER: Jim's Chauffeur
  LINE: (Whispering in his ear)
  EXPRESSION: null
- CHARACTER: Dean
  LINE: “10, 2?” “10, 2?”
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The crowd looks around. No one is challenging. Dean smiles.
  EXPRESSION: null
- CHARACTER: Dean
  LINE: (Bangs his fist onto his open palm and points to Jim Hudson.)
  EXPRESSION: null
- CHARACTER: Jim's Chauffeur
  LINE: (Whispering in his ear)
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The guests clap in a mixture of delight and disappointment.
  EXPRESSION: null

::PATHS::
- CHOICE: "Exit auction tent"
  TARGET: lakeside_dusk
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Lakeside
TIME: Dusk
CHARACTERS: Chris, Rose, Guests (distant)
BACKGROUND_IMAGE: lakeside_dusk.png
BACKGROUND_EDIT: "Serene lake at sunset, faint sounds of distant applause"

::SCRIPT::
- CHARACTER: Chris
  LINE: I told you about the night my mom died. How I didn’t call 911; didn’t go out looking for her.
  EXPRESSION: Sad
- CHARACTER: Rose
  LINE: Baby--
  EXPRESSION: Concerned
- CHARACTER: Chris
  LINE: One hour went by, then two, three... I just sat there... I just watched TV.
  EXPRESSION: Guilt-ridden
- CHARACTER: Rose
  LINE: It wasn’t your fault--
  EXPRESSION: Comforting
- CHARACTER: Chris
  LINE: I found out later she had survived the initial hit. She laid there bleeding by the side of the road all night, cold and alone. And that’s how she died in the early morning... Cold and alone. And I was watching TV.
  EXPRESSION: Devastated
- CHARACTER: Chris
  LINE: There was time. If someone was looking for her, there was time. But no one was looking.
  EXPRESSION: Despairing
- CHARACTER: Narrator
  LINE: Chris cries. Rose embraces him.
  EXPRESSION: null
- CHARACTER: Rose
  LINE: You were just a kid.
  EXPRESSION: Soothing
- CHARACTER: Chris
  LINE: Yeah... yeah. So, I’m not gonna leave here without you. I‘m not going to abandon you. Never.
  EXPRESSION: Determined
- CHARACTER: Narrator
  LINE: They share a moment of pure love.
  EXPRESSION: null
- CHARACTER: Rose
  LINE: Fuck it. Come on. Let’s go back home.
  EXPRESSION: Resolute
- CHARACTER: Chris
  LINE: Yeah?
  EXPRESSION: Hopeful
- CHARACTER: Rose
  LINE: Yeah. I mean, you’re right. This sucks. I’ll go back with you. I’ll make something up.
  EXPRESSION: Loyal
- CHARACTER: Chris
  LINE: I love you.
  EXPRESSION: Loving
- CHARACTER: Rose
  LINE: I love you too.
  EXPRESSION: Loving
- CHARACTER: Narrator
  LINE: The two get up and walk back toward the house.
  EXPRESSION: null

::PATHS::
- CHOICE: "Return to the house"
  TARGET: front_lawn_dusk
  STATE_CHANGE: commitment_to_rose = +1
  CONDITION: null

::SCENE::
LOCATION: Front Lawn
TIME: Dusk
CHARACTERS: Chris, Rose, Dean, Missy, Lisa Deets, Nelson, Walter, Guests
BACKGROUND_IMAGE: front_lawn_dusk.png
BACKGROUND_EDIT: "Front lawn at dusk, fireflies appearing, guests departing"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Chris and Rose approach the house as the last of the guests get into their cars and drive off. The fireflies are out.
  EXPRESSION: null
- CHARACTER: Chris
  LINE: That was fast.
  EXPRESSION: Observant
- CHARACTER: Rose
  LINE: Yeah.
  EXPRESSION: Agreeing
- CHARACTER: Narrator
  LINE: The guests wave to Dean and Missy, who stand at the front door, and then to Chris and Rose. Lisa Deets, the trophy wife, is tipsy. Nelson is in their car.
  EXPRESSION: null
- CHARACTER: Lisa Deets
  LINE: Bye Chris! It was a pleasure meeting you. I hope you--
  EXPRESSION: Tipsy
- CHARACTER: Narrator
  LINE: Chris and Rose wave.
  EXPRESSION: null
- CHARACTER: Nelson
  LINE: Come on, Lisa. Before you say something stupid.
  EXPRESSION: Impatient
- CHARACTER: Narrator
  LINE: Chris laughs. Walter shuts the car door behind Lisa. Walter stands pleasantly watching the cars leave. He turns to Chris with the same ‘ol smile. Chris and Rose enter the house.
  EXPRESSION: null

::PATHS::
- CHOICE: "Enter the house"
  TARGET: armitage_bathroom_dusk
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Armitage Bathroom
TIME: Dusk
CHARACTERS: Chris, Rod (via text)
BACKGROUND_IMAGE: armitage_bathroom_dusk.png
BACKGROUND_EDIT: "Bathroom with running sink, mirror"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Sink running. Chris washes his hands and looks in the mirror.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: His phone signals a text message from Rod. It’s a picture from the internet of witches in a circle around a man being sacrificed followed by the text message. “You dead yet?”
  EXPRESSION: null
- CHARACTER: Chris
  LINE: Bruh, you have no idea.
  EXPRESSION: Sarcastic
- CHARACTER: Narrator
  LINE: He finds the picture he took of Logan/Andre on his phone and sends it.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Moments later, his phone vibrates.
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue communication with Rod"
  TARGET: chris_apartment_dusk
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Chris' Apartment
TIME: Dusk
CHARACTERS: Rod, Chris (via phone)
BACKGROUND_IMAGE: chris_apartment_dusk.png
BACKGROUND_EDIT: "Chris' apartment, Rod on the phone"

::SCRIPT::
- CHARACTER: Rod
  LINE: That’s Dre.
  EXPRESSION: Informative
- CHARACTER: Chris
  LINE: Dre?
  EXPRESSION: Puzzled
- CHARACTER: Rod
  LINE: Andre um... Hayworth! Yeah! He used to kick it with Veronica.
  EXPRESSION: Reminiscent
- CHARACTER: Chris
  LINE: Veronica from...
  EXPRESSION: Questioning
- CHARACTER: Rod
  LINE: ...Teresa’s sister! Worked at the movie theatre on 8th; got us into the movie a couple of times; Rush hour 2 and, um Usual Suspect.
  EXPRESSION: Nostalgic
- CHARACTER: Chris
  LINE: Yeah. That is him. But...
  EXPRESSION: Shocked
- CHARACTER: Rod
  LINE: ...But what?
  EXPRESSION: Inquisitive
- CHARACTER: Chris
  LINE: This is so fuckin’ crazy. He’s different now.
  EXPRESSION: Astounded
- CHARACTER: Rod
  LINE: Different? How?
  EXPRESSION: Curious
- CHARACTER: Chris
  LINE: Different. Slower... I mean he was street; now he’s all like... white-seeming. Oh, plus he’s gay!
  EXPRESSION: Bewildered
- CHARACTER: Rod
  LINE: No, he ain’t.
  EXPRESSION: Disbelieving
- CHARACTER: Chris
  LINE: I’m telling you: He’s gay, I met his man. He’s--
  EXPRESSION: Insistent
- CHARACTER: Rod
  LINE: Chris, you in a fucked up Eyes Wide Shut situation. You need to--.
  EXPRESSION: Urgent
- CHARACTER: Narrator
  LINE: The phone goes dead. No batteries.
  EXPRESSION: null

::PATHS::
- CHOICE: "Go to Rose's room"
  TARGET: rose_bedroom_night
  STATE_CHANGE: suspicion_of_rod = +1
  CONDITION: null

::SCENE::
LOCATION: Rose's Bedroom
TIME: Night
CHARACTERS: Chris, Jim Hudson's Driver, Missy
BACKGROUND_IMAGE: rose_bedroom_night.png
BACKGROUND_EDIT: "Rose's bedroom, Chris packing, looking out window"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Chris’ phone lays on the dresser plugged in. He’s in a hurry now. He packs his small bag and looks out the window.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: One car remains parked in the designated parking area. It’s the first to have arrived for the party: Jim Hudson’s. The driver brings the dog to the back seat. He gets a green envelope from the glove compartment and brings it to Missy at the front door. She accepts it silently.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The driver drives away without Jim.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Chris goes to leave Rose’s room. Her closet creaks open. Chris sees a framed picture of Rose inside. Not quite knowing what he’s looking for, he goes to the closet. The picture is a frightening one. Rose is one of the witches in a high school production of Macbeth. It’s on top of a red shoebox that has the drama/comedy masks drawn on top of it.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: He takes it off of the shelf. Inside is a pile of pictures. On top is one of Rose dressed as Juliet in a high school play.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The next one is of Rose at 13 playing Ms. Hannigan in Annie. Chris flips through a few more pictures of Rose at different ages in different class plays.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Finally Chris comes upon a photo printed from a computer. It’s a selfie of her and some other black guy. The picture is almost identical to the one she took with Chris before the ride up. Under the image are written the words. “X-mas 2014”
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Stunned, Chris flips to the next picture. It’s another romantic selfie, this time with a different black guy. Underneath,
  EXPRESSION: null

::PATHS::
- CHOICE: "Examine the next photo"
  TARGET: rose_closet_continued
  STATE_CHANGE: suspicion_of_rose = +1
  CONDITION: null

::SCENE::
LOCATION: Unknown
MOOD: Suspenseful
CHARACTERS: Narrator, Rose, Chris
BACKGROUND_IMAGE: unknown_room.png
BACKGROUND_EDIT: "Dimly lit room, Chris looking at photos"

::SCRIPT::
- CHARACTER: Narrator
  LINE: the caption “Memorial Day 2013”
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: He continues flipping through the stack of pictures of Rose with 8 different black guys. The last one is a picture of Rose with Walter. In it she kisses Walter’s cheek intimately. “Thanksgiving 2009” Walter looks different in the picture. He isn’t smiling vaguely; he’s got swagger.
  EXPRESSION: null
- CHARACTER: Rose
  LINE: What are you doing?
  EXPRESSION: Emotionless
- CHARACTER: Narrator
  LINE: Rose stands there in the doorway behind him. Chris subtly drops the pictures back in the shoebox.
  EXPRESSION: null
- CHARACTER: Chris
  LINE: Um... Looking for my camera.
  EXPRESSION: Nervous
- CHARACTER: Narrator
  LINE: Rose points to her desk. He grabs his bag and the camera.
  EXPRESSION: null
- CHARACTER: Chris
  LINE: Where are the keys..? I gotta put our bags in the trunk.
  EXPRESSION: Nervous
- CHARACTER: Rose
  LINE: Walter can do that.
  EXPRESSION: Distant
- CHARACTER: Chris
  LINE: Nah, I’ll do it.
  EXPRESSION: Resolute
- CHARACTER: Narrator
  LINE: Rose is truly distant for the first time. A different person. She is methodical and emotionless. The jig is up, and now she is now phoning it in.
  EXPRESSION: null

::PATHS::
- CHOICE: "Leave the room"
  TARGET: foyer_living_room
  STATE_CHANGE: suspicion = +1
  CONDITION: null

::SCENE::
LOCATION: Foyer/Living Room
MOOD: Tense
CHARACTERS: Narrator, Rose, Chris, Jeremy, Dean, Missy
BACKGROUND_IMAGE: foyer_living_room.png
BACKGROUND_EDIT: "Nighttime interior, grand staircase and living room"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Rose follows Chris down the stairs.
  EXPRESSION: null
- CHARACTER: Rose
  LINE: Chris... What’s wrong?
  EXPRESSION: Concerned
- CHARACTER: Chris
  LINE: Nothing.
  EXPRESSION: Evasive
- CHARACTER: Narrator
  LINE: Jeremy stands near the front door twirling his lacrosse stick. Dean and Missy sit in the living room.
  EXPRESSION: null
- CHARACTER: Jeremy
  LINE: Where are you going? The party’s just getting started.
  EXPRESSION: Casual
- CHARACTER: Chris
  LINE: I’m going to the car; see if we left the keys in there.
  EXPRESSION: Evasive
- CHARACTER: Missy
  LINE: I just made tea.
  EXPRESSION: Inviting
- CHARACTER: Chris
  LINE: I’m good.
  EXPRESSION: Resolute
- CHARACTER: Narrator
  LINE: The family is silent. Missy’s glare pierces Chris. He avoids eye contact.
  EXPRESSION: null
- CHARACTER: Rose
  LINE: Oh, I know where they are. In my bag. Duh.
  EXPRESSION: Feigned Casualness
- CHARACTER: Missy
  LINE: You’re leaving us.
  EXPRESSION: Accusatory
- CHARACTER: Chris
  LINE: Yeah.
  EXPRESSION: Resolute
- CHARACTER: Missy
  LINE: Is something wrong?
  EXPRESSION: Suspicious
- CHARACTER: Chris
  LINE: No. Well, yeah... Um.
  EXPRESSION: Hesitant
- CHARACTER: Rose
  LINE: His dog is not well. He needs to go to the vet first thing in the morn-
  EXPRESSION: Blank
- CHARACTER: Narrator
  LINE: Dean hits play on the sound system. Darkly valiant classical music begins. He standing in front of the fireplace.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Lost in the fire, Dean begins conducting the music.
  EXPRESSION: null
- CHARACTER: Dean
  LINE: What is your purpose, Chris?
  EXPRESSION: Philosophical
- CHARACTER: Chris
  LINE: What?
  EXPRESSION: Confused
- CHARACTER: Dean
  LINE: In life? What is your purpose..?
  EXPRESSION: Philosophical
- CHARACTER: Chris
  LINE: Right now, it’s finding the keys.
  EXPRESSION: Dismissive
- CHARACTER: Dean
  LINE: We’ve been looking for our purpose for such a long time. Fire has mesmerized man since the Stone Age. It is a reflection of our impermanence in the world. Fire is born, it breathes and then it dies.
  EXPRESSION: Philosophical
- CHARACTER: Chris
  LINE: Rose...
  EXPRESSION: Pleading
- CHARACTER: Rose
  LINE: I’m looking.
  EXPRESSION: Feigned Diligence
- CHARACTER: Chris
  LINE: Rose, what is this shit?!
  EXPRESSION: Angry
- CHARACTER: Dean
  LINE: There’s a reason we worship the Sun, Chris. He who lights the way through the darkness of life. He in all his glory was around long before us and will be here long after we are gone, but he too will die some day! That’s right even the Sun God will die. It is no less mortal than we, but it inspires us to defy it! So what do we do?--
  EXPRESSION: Manic
- CHARACTER: Chris
  LINE: --Rose.--
  EXPRESSION: Pleading
- CHARACTER: Dean
  LINE: --What do we do?! We baptize ourselves in the firewater! We bathe in his reflection, for one chance to emerge having defied death! You’d take that baptism wouldn’t you, Chris? The baptism of immortality?
  EXPRESSION: Manic
- CHARACTER: Chris
  LINE: I was raised Episcopalian.
  EXPRESSION: Sarcastic
- CHARACTER: Narrator
  LINE: Chris starts toward the door, but his path is blocked by Jeremy swinging at air.
  EXPRESSION: null
- CHARACTER: Jeremy
  LINE: Whoa! Be careful, bro.
  EXPRESSION: Playful
- CHARACTER: Missy
  LINE: Don’t hurt him, Jeremy.
  EXPRESSION: Concerned
- CHARACTER: Jeremy
  LINE: What? I’m not doing anything.
  EXPRESSION: Innocent
- CHARACTER: Dean
  LINE: Listen, Chris--
  EXPRESSION: Urgent
- CHARACTER: Chris
  LINE: --I don’t know what you’re saying!
  EXPRESSION: Frustrated
- CHARACTER: Dean
  LINE: I’m saying that we’ve found OUR PURPOSE!!! There must be a sacrifice! Sacrifice is essential for the righteous to achieve our true potential. A vessel must be comprised. A host must be born!!!
  EXPRESSION: Ecstatic
- CHARACTER: Chris
  LINE: Rose! The keys!!!
  EXPRESSION: Desperate
- CHARACTER: Rose
  LINE: Oh baby... You know I can’t give you the keys.
  EXPRESSION: Resigned
- CHARACTER: Narrator
  LINE: Chris makes a run for the door. Missy CLINKS the cup with her SPOON.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: TING TING. TING TING. The world instantly blurs around Chris. He begins to fall. He sees a flash.
  EXPRESSION: null

::PATHS::
- CHOICE: "Fall"
  TARGET: darkness
  STATE_CHANGE: consciousness = -1
  CONDITION: null

::SCENE::
LOCATION: Darkness
MOOD: Disoriented
CHARACTERS: Narrator, Chris, Jeremy, Missy, Dean, Rose
BACKGROUND_IMAGE: darkness.png
BACKGROUND_EDIT: "Abyssal void, Chris's POV falling"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Chris falls through the abyss towards ‘The Sunken Place’ again just like when he was hypnotized. The blue screen above him shows what his open eyes see. It’s his own perspective falling to the floor. CRASH! The screen now shows the living room ceiling. Jeremy leans over him.
  EXPRESSION: null
- CHARACTER: Jeremy
  LINE: Oh shit!
  EXPRESSION: Shocked
- CHARACTER: Missy
  LINE: Is he hurt?
  EXPRESSION: Concerned
- CHARACTER: Chris
  LINE: What the fuck?
  EXPRESSION: Confused
- CHARACTER: Jeremy
  LINE: Did you see him drop?
  EXPRESSION: Curious
- CHARACTER: Dean
  LINE: He hit his head pretty good.
  EXPRESSION: Matter-of-fact
- CHARACTER: Rose
  LINE: It’s just a bump. He’s fine.
  EXPRESSION: Dismissive
- CHARACTER: Chris
  LINE: Rose!!!
  EXPRESSION: Desperate
- CHARACTER: Missy
  LINE: Why do you push them, Dean?
  EXPRESSION: Accusatory
- CHARACTER: Dean
  LINE: It’s important to me that they acknowledge the purpose.
  EXPRESSION: Intense
- CHARACTER: Missy
  LINE: Why do you think he ran?
  EXPRESSION: Perplexed
- CHARACTER: Jeremy
  LINE: Rose gave it away.
  EXPRESSION: Observing
- CHARACTER: Rose
  LINE: He already knew.
  EXPRESSION: Resigned
- CHARACTER: Missy
  LINE: Take him to the games room. Jeremy, get the legs. Dean, help him.
  EXPRESSION: Directive
- CHARACTER: Jeremy
  LINE: I can take him alone.
  EXPRESSION: Confident
- CHARACTER: Missy
  LINE: No. We’ve already damaged him enough. Dean, please.
  EXPRESSION: Pleading
- CHARACTER: Narrator
  LINE: Chris continues to fall slowly further from the screen above which continues to show his body’s POV as it is being lifted by Dean and Jeremy and carried out of the room.
  EXPRESSION: null
- CHARACTER: Chris
  LINE: Rose!? No, no, no, no. Shit, shit...
  EXPRESSION: Panicked
- CHARACTER: Dean
  LINE: You’re going to drop him.
  EXPRESSION: Cautionary
- CHARACTER: Jeremy
  LINE: No I’m not.
  EXPRESSION: Reassuring
- CHARACTER: Missy
  LINE: Be careful what you say, everyone. He can hear every word.
  EXPRESSION: Warning
- CHARACTER: Chris
  LINE: Rose!!!!
  EXPRESSION: Desperate
- CHARACTER: Rose
  LINE: It doesn’t matter any more does it?
  EXPRESSION: Melancholy
- CHARACTER: Narrator
  LINE: A DOOR CREAKS open. Chris’ body is taken downstairs into the darkness. The screen in the abyss goes dark.
  EXPRESSION: null
- CHARACTER: Chris
  LINE: No!! Help!!! Help!!!!! Help!!!!!!
  EXPRESSION: Screaming
- CHARACTER: Narrator
  LINE: Chris sinks, his screams are enveloped by the pitch back.
  EXPRESSION: null

::PATHS::
- CHOICE: "Sink into darkness"
  TARGET: airport_security
  STATE_CHANGE: consciousness = -1
  CONDITION: null

::SCENE::
LOCATION: Airport Security Check
MOOD: Neutral
CHARACTERS: Narrator
BACKGROUND_IMAGE: airport_security.png
BACKGROUND_EDIT: "Daytime, airport security checkpoint"

::SCRIPT::
- CHARACTER: Narrator
  LINE: 102
  EXPRESSION: null

::PATHS::
- CHOICE: "Proceed through security"
  TARGET: end
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Airport - Bag X-Ray Area
MOOD: Distracted
CHARACTERS: Rod, Gary
BACKGROUND_IMAGE: airport_bag_xray.png
BACKGROUND_EDIT: "Rod sitting by a bag x-ray machine, staring into space"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Rod sits by the bag x-ray but stares into space distracted by thought.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: GARY (40) a condescending supervisor snaps his fingers in Rod’s face.
  EXPRESSION: null
- CHARACTER: Gary
  LINE: Hey... two strikes. Go take 10; get it together.
  EXPRESSION: Annoyed

::PATHS::
- CHOICE: "Take a break"
  TARGET: airport_departures
  STATE_CHANGE: frustration = +1
  CONDITION: null

::SCENE::
LOCATION: Airport - Departures Terminal
MOOD: Anxious
CHARACTERS: Rod, Chris (V.O.)
BACKGROUND_IMAGE: airport_departures.png
BACKGROUND_EDIT: "Rod standing outside the departures terminal, smoking a cigarette"

::SCRIPT::
- CHARACTER: Rod
  LINE: Sup? Making sure you good. I thought you were coming back yesterday, so hopefully you home already and just sleeping or some shit. Aiight. Let me know.
  EXPRESSION: Worried
- CHARACTER: Chris (V.O.)
  LINE: It’s Chris. I’m away from my phone or I just don’t want to talk to you.
  EXPRESSION: Indifferent

::PATHS::
- CHOICE: "Go to Chris's place"
  TARGET: chris_living_room_night
  STATE_CHANGE: worry = +1
  CONDITION: null

::SCENE::
LOCATION: Chris' Living Room
MOOD: Welcoming
CHARACTERS: Rod, Sid
BACKGROUND_IMAGE: chris_living_room_night.png
BACKGROUND_EDIT: "Rod opening the door to Chris's living room, dog wagging tail"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Rod opens the door. Sid wags his tail hungrily.
  EXPRESSION: null

::PATHS::
- CHOICE: "Check on Chris"
  TARGET: chris_kitchen_later
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Chris' Kitchen
MOOD: Concerned
CHARACTERS: Rod, Chris (V.O.), Sid
BACKGROUND_IMAGE: chris_kitchen_later.png
BACKGROUND_EDIT: "Rod opening dog food while on the phone with Chris"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Rod opens dog food while he calls Chris.
  EXPRESSION: null
- CHARACTER: Chris (V.O.)
  LINE: Hey, it’s Chris. I’m away from my phone or I just don’t want to talk to--
  EXPRESSION: Indifferent
- CHARACTER: Narrator
  LINE: Rod hangs up. He places Sid’s bowl down. Sid doesn’t eat. Instead Sid looks back up at Rod and WHINES.
  EXPRESSION: null
- CHARACTER: Rod
  LINE: Yeah... me too.
  EXPRESSION: Sad

::PATHS::
- CHOICE: "Search for Chris online"
  TARGET: chris_living_room_later
  STATE_CHANGE: concern = +2
  CONDITION: null

::SCENE::
LOCATION: Chris' Living Room
MOOD: Shocked
CHARACTERS: Rod, Sid
BACKGROUND_IMAGE: chris_living_room_later.png
BACKGROUND_EDIT: "Rod sitting at Chris's desk, Sid on his lap, searching online"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Rod sits at Chris’ desk in front of his laptop. Sid sits on Rod’s lap.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Rod types “Andre Hayworth” into the search engine. Images of Andre come up.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Rod finds an article entitled: “What Happened to Andre Hayworth?” under in bold “Brooklyn Native Goes Missing In Evergreen Hallow.”
  EXPRESSION: null
- CHARACTER: Rod
  LINE: Oh shit.
  EXPRESSION: Shocked

::PATHS::
- CHOICE: "Investigate Evergreen Hallow"
  TARGET: games_room
  STATE_CHANGE: fear = +3, intrigue = +2
  CONDITION: null

::SCENE::
LOCATION: Games Room
MOOD: Terrified
CHARACTERS: Chris, Rose
BACKGROUND_IMAGE: games_room.png
BACKGROUND_EDIT: "Chris tied to a chair in a dark room, animal heads mounted on walls"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Chris wakes up with a bump on his head. In front of Chris, a deer’s head is mounted above an old-school floor-standing television. Behind him, a goat’s head is mounted under a taxidermy owl, wings spread.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: His arms and legs fastened to a leather upholstered chair in the middle of a small dark room full of board games.
  EXPRESSION: null
- CHARACTER: Chris
  LINE: Hey. Hey!!!! Rose!!!!
  EXPRESSION: Panicked
- CHARACTER: Narrator
  LINE: Chris tries to gnaw at the harnesses, but they are too thick.
  EXPRESSION: null
- CHARACTER: Chris
  LINE: Oh shit. Oh shit. Oh fuck. Oh shit. The fuck?!?!! Y’all are psycho!? Is that it? Let me out of this chair.
  EXPRESSION: Panicked
- CHARACTER: Narrator
  LINE: Chris looks around.
  EXPRESSION: null
- CHARACTER: Chris
  LINE: People know I’m here. I told a bunch of people where I was going! You don’t know me!!! You don’t know me!!!! Hey! Hey!! Hey!!!!!
  EXPRESSION: Desperate
- CHARACTER: Narrator
  LINE: The television screen turns on. Chris watches intently. The image of deer walking through woods comes on. The words “YOU’VE GOT A FRIEND by James Taylor” comes up as the song starts to PLAY. It’s a forest-themed karaoke video.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Chris is confused. He tries to slip out of the binds again drawing blood on his wrists.
  EXPRESSION: null

::PATHS::
- CHOICE: "Keep struggling"
  TARGET: police_station
  STATE_CHANGE: pain = +1, fear = +2
  CONDITION: null

::SCENE::
LOCATION: Chris' Living Room
MOOD: Peaceful
CHARACTERS: Rod, Sid
BACKGROUND_IMAGE: chris_living_room_dawn.png
BACKGROUND_EDIT: "Rod sleeping on the sofa, Sid waking him up"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Sid wakes Rod up with a lick to the face. He’s on the sofa.
  EXPRESSION: null

::PATHS::
- CHOICE: "Go to the police station"
  TARGET: police_station
  STATE_CHANGE: determination = +1
  CONDITION: null

::SCENE::
LOCATION: Police Station
MOOD: Frustrated
CHARACTERS: Rod, Sid, Detective Latoya
BACKGROUND_IMAGE: police_station.png
BACKGROUND_EDIT: "Rod sitting at a desk with Sid on his lap, talking to Detective Latoya"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Rod sits at a desk with Sid on his lap.. DETECTIVE LATOYA 50, African American enters. She looks like she’s been doing this way too long. She speaks to someone outside her office.
  EXPRESSION: null
- CHARACTER: Detective Latoya
  LINE: ...Then he should’ve gone back up there and made sure everything was accounted for. ‘Cause hey, look; how about this? If you record the evidence, you’re responsible for it.
  EXPRESSION: Gruff
- CHARACTER: Narrator
  LINE: Latoya shuts the door and sits at her desk. She begins opening and eating a bag of cashews.
  EXPRESSION: null
- CHARACTER: Detective Latoya
  LINE: Hello Mr...
  EXPRESSION: Professional
- CHARACTER: Rod
  LINE: Williams... Rod Williams...
  EXPRESSION: Nervous
- CHARACTER: Detective Latoya
  LINE: From the TSA?
  EXPRESSION: Skeptical
- CHARACTER: Rod
  LINE: Yes Ma’am.
  EXPRESSION: Anxious
- CHARACTER: Detective Latoya
  LINE: You know that TSA issues should be brought to your authorizing officer, right?
  EXPRESSION: Challenging
- CHARACTER: Rod
  LINE: It’s not TSA business, ma’am.
  EXPRESSION: Assertive
- CHARACTER: Detective Latoya
  LINE: Please don’t call me “ma’am,” or we’re not gonna get along. How can I help you, Rod Williams from the TSA?
  EXPRESSION: Stern
- CHARACTER: Rod
  LINE: Here it is: My boy Chris has been missing for two days.
  EXPRESSION: Urgent
- CHARACTER: Detective Latoya
  LINE: Your son is missing?
  EXPRESSION: Surprised
- CHARACTER: Rod
  LINE: No, sorry, not my son, my boy. He’s my friend. He’s 26. His name is Chris... Washington...
  EXPRESSION: Correcting
- CHARACTER: Narrator
  LINE: He gives her time to write the name which she doesn’t do. She just stares at him.
  EXPRESSION: null
- CHARACTER: Rod
  LINE: He left town on Friday with his girlfriend Rose... Armitage... She’s white.
  EXPRESSION: Informative
- CHARACTER: Detective Latoya
  LINE: That’s four days ago.
  EXPRESSION: Fact-checking
- CHARACTER: Rod
  LINE: Yeah, I mean he’s only been MISSING for two days. He was supposed--
  EXPRESSION: Clarifying
- CHARACTER: Detective Latoya
  LINE: --I’m gonna stop you right there. Now you know the minimum amount of time without contact before you can file a missing persons report is--
  EXPRESSION: Interrogating
- CHARACTER: Rod
  LINE: --Three days I know, but I have reason to believe he’s been abducted.
  EXPRESSION: Pleading
- CHARACTER: Detective Latoya
  LINE: Go on.
  EXPRESSION: Encouraging
- CHARACTER: Rod
  LINE: Chris was set to come back home on Sunday. I was watching his dog Sid.
  EXPRESSION: Explaining
- CHARACTER: Detective Latoya
  LINE: That’s Sid.
  EXPRESSION: Acknowledging
- CHARACTER: Rod
  LINE: Yup. Cute right? Now look...
  EXPRESSION: Proud
- CHARACTER: Narrator
  LINE: Rod takes out his phone and scrolls to a photo of Andre.
  EXPRESSION: null
- CHARACTER: Rod
  LINE: Chris sent me this which he took at the girlfriend's parents house. That’s Andre Hayworth, a guy we knew from back in the day. Come to find out he went missing 6 months ago in an affluent suburb upstate.
  EXPRESSION: Informative
- CHARACTER: Detective Latoya
  LINE: Don’t look too missing to me.
  EXPRESSION: Dismissive
- CHARACTER: Rod
  LINE: Well that’s the thing. We found him and now, according to Chris, he’s gay with a different personality.
  EXPRESSION: Confused
- CHARACTER: Detective Latoya
  LINE: Gay?
  EXPRESSION: Disbelieving
- CHARACTER: Rod
  LINE: But he didn’t used to be.
  EXPRESSION: Insistent
- CHARACTER: Detective Latoya
  LINE: I think he might just argue with you on that one.
  EXPRESSION: Sarcastic
- CHARACTER: Rod
  LINE: I know what I’m about to say is gonna sound crazy.
  EXPRESSION: Hesitant
- CHARACTER: Detective Latoya
  LINE: Try me.
  EXPRESSION: Ready
- CHARACTER: Rod
  LINE: You ready for this...? I think this family is abducting black people and brainwashing them to work for them as sex slaves and shit... Sorry.
  EXPRESSION: Distraught
- CHARACTER: Detective Latoya
  LINE: ...Brainwashing?
  EXPRESSION: Shocked

::PATHS::
- CHOICE: "Continue the investigation"
  TARGET: end
  STATE_CHANGE: police_involvement = +1, conspiracy = +3
  CONDITION: null

::SCENE::
LOCATION: Police Station
MOOD: Serious
CHARACTERS: Rod, Detective Latoya, Garcia, Frostie
BACKGROUND_IMAGE: police_station_interrogation.png
BACKGROUND_EDIT: "Moments later, two detectives join Latoya"

::SCRIPT::
- CHARACTER: Rod
  LINE: Yeah.
  EXPRESSION: null
- CHARACTER: Detective Latoya
  LINE: Hold on one second.
  EXPRESSION: null
- CHARACTER: Detective Latoya
  LINE: Garcia, Frostie, get in here a second.
  EXPRESSION: null
- CHARACTER: Detective Latoya
  LINE: I want you to tell these officers exactly what you just told me.
  EXPRESSION: null

::PATHS::
- CHOICE: "Tell the officers what happened"
  TARGET: police_station_officers
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Police Station - Officers Present
MOOD: Dismissive
CHARACTERS: Rod, Detective Latoya, Garcia, Frostie, Drake
BACKGROUND_IMAGE: police_station_interrogation.png
BACKGROUND_EDIT: "Two detectives, Garcia and Drake, stand behind Latoya"

::SCRIPT::
- CHARACTER: Rod
  LINE: 83. ...See, I don’t know if the hypnosis makes you a slave or if it just turns you gay or what, but they already got two brothers that we know of, and who knows how many more there could be.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The officers are all riveted... Then... All three detectives laugh. Rod is not being taken the slightest bit seriously.
  EXPRESSION: null
- CHARACTER: Detective Latoya
  LINE: So, I don’t want none of you sayin’ I don’t do nothin’ for you... White girls’ll get ya every time!
  EXPRESSION: Humorous
- CHARACTER: Narrator
  LINE: They laugh even harder.
  EXPRESSION: null

::PATHS::
- CHOICE: "Leave the police station"
  TARGET: games_room
  STATE_CHANGE: frustration = +2
  CONDITION: null

::SCENE::
LOCATION: Games Room
MOOD: Torturous
CHARACTERS: Chris
BACKGROUND_IMAGE: games_room.png
BACKGROUND_EDIT: "Song plays over and over"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The SONG PLAYS Over and over. Chris is too weak to struggle.
  EXPRESSION: null
- CHARACTER: Chris
  LINE: Is this the only song you got?
  EXPRESSION: Weak

::PATHS::
- CHOICE: "Continue to endure"
  TARGET: games_room_repeat
  STATE_CHANGE: exhaustion = +1
  CONDITION: null

::SCENE::
LOCATION: Games Room
MOOD: Desperate
CHARACTERS: Chris
BACKGROUND_IMAGE: games_room.png
BACKGROUND_EDIT: "Song ends and begins again"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The SONG ends. It BEGINS again.
  EXPRESSION: null
- CHARACTER: Chris
  LINE: Okay. Okay! What do you want? You tryin’ to break me? I won’t say shit!! I’ll just... I’ll do what you say, just answer me!
  EXPRESSION: Desperate

::PATHS::
- CHOICE: "Agree to do as they say"
  TARGET: chris_loft
  STATE_CHANGE: broken = true
  CONDITION: null

::SCENE::
LOCATION: Chris' Loft
MOOD: Contemplative
CHARACTERS: Rod, Sid, Rose
BACKGROUND_IMAGE: chris_loft.png
BACKGROUND_EDIT: "Rod sits by the window looking out over rooftops, holding his phone"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Rod sits by the window with Sid. He looks out over rooftops and thinks. He picks up his phone and calls Chris again. He knows Chris won’t answer. Then--
  EXPRESSION: null
- CHARACTER: Rose
  LINE: Hello?
  EXPRESSION: Surprised
- CHARACTER: Narrator
  LINE: Rod is taken off guard. He almost drops his phone.
  EXPRESSION: Shocked
- CHARACTER: Rose
  LINE: Chris?
  EXPRESSION: Confused
- CHARACTER: Rod
  LINE: Yo. Um, Rose? It’s Rod.
  EXPRESSION: Nervous
- CHARACTER: Rose
  LINE: Hi.
  EXPRESSION: null
- CHARACTER: Rod
  LINE: Where’s Chris?
  EXPRESSION: Worried

::PATHS::
- CHOICE: "Intercut with Rose's location"
  TARGET: armitage_house_dining_room
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Armitage House. Dining Room
MOOD: Upset
CHARACTERS: Rose, Rod
BACKGROUND_IMAGE: armitage_house_dining_room.png
BACKGROUND_EDIT: "Rose stands by the dining table on Chris' phone, starting to cry"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Rose stands by the dining table on Chris’ phone. Rose starts to cry.
  EXPRESSION: null
- CHARACTER: Rose
  LINE: He left like two days ago.
  EXPRESSION: Crying
- CHARACTER: Rod
  LINE: He left?
  EXPRESSION: Disbelieving
- CHARACTER: Rose
  LINE: We got in a fight. He got all paranoid and flipped out; He took a cab home. He forgot his phone. Wait... You haven’t seen him?
  EXPRESSION: Confused
- CHARACTER: Rod
  LINE: No. He never made it back here.
  EXPRESSION: Worried
- CHARACTER: Rose
  LINE: Oh my God.
  EXPRESSION: Horrified
- CHARACTER: Rod
  LINE: I’ve been calling. I went to the police and everything.
  EXPRESSION: Desperate
- CHARACTER: Narrator
  LINE: Rose is silent.
  EXPRESSION: null
- CHARACTER: Rod
  LINE: Hello?
  EXPRESSION: Anxious
- CHARACTER: Rose
  LINE: What did you say?
  EXPRESSION: Suspicious
- CHARACTER: Rod
  LINE: I told them he was missing.
  EXPRESSION: null
- CHARACTER: Rose
  LINE: Uh huh...
  EXPRESSION: null
- CHARACTER: Rod
  LINE: So... What cab company did he use?
  EXPRESSION: Determined
- CHARACTER: Rose
  LINE: I don’t know. A local one I’m guessing. Maybe uber? Wait, I’m so confused...
  EXPRESSION: Confused
- CHARACTER: Rod
  LINE: Hold on a second.
  EXPRESSION: Suspicious

::PATHS::
- CHOICE: "Confront Rose about her involvement"
  TARGET: garage_band_recording
  STATE_CHANGE: suspicion = +3
  CONDITION: null

::SCENE::
LOCATION: Chris' Loft (Garage Band)
MOOD: Suspicious
CHARACTERS: Rod, Rose
BACKGROUND_IMAGE: chris_loft_computer.png
BACKGROUND_EDIT: "Rod opens 'Garage Band' on Chris' computer and puts the phone on speaker, recording her."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Rod knows she had something to do with it. He opens ‘Garage Band’ on Chris’ computer and puts the phone on speaker, recording her.
  EXPRESSION: null
- CHARACTER: Rod
  LINE: So, last time Chris and I talked, he told me your mom hypnotized him?
  EXPRESSION: Accusatory
- CHARACTER: Rose
  LINE: Rod, just stop.
  EXPRESSION: Annoyed
- CHARACTER: Rod
  LINE: Huh?
  EXPRESSION: Confused
- CHARACTER: Rose
  LINE: I know why you’re calling.
  EXPRESSION: Knowing
- CHARACTER: Rod
  LINE: Why is that?
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: We now see Rose’s family standing in the living room behind her. They watch her operate.
  EXPRESSION: null
- CHARACTER: Rose
  LINE: Come on. I mean, it’s kind of obvious.
  EXPRESSION: Flirtatious
- CHARACTER: Rod
  LINE: What?
  EXPRESSION: null
- CHARACTER: Rose
  LINE: That there’s something between us.
  EXPRESSION: Flirtatious
- CHARACTER: Rod
  LINE: No. I’m calling about Chris.
  EXPRESSION: Firm
- CHARACTER: Rose
  LINE: We’d all go out drinking... I remember you looking at me.
  EXPRESSION: Flirtatious
- CHARACTER: Narrator
  LINE: Rod is put on the spot. He becomes extremely uncomfortable.
  EXPRESSION: Uncomfortable
- CHARACTER: Rod
  LINE: That’s my best friend. If you did something--
  EXPRESSION: Panicked
- CHARACTER: Rose
  LINE: I know you think about fucking me, Rod.
  EXPRESSION: Provocative
- CHARACTER: Rod
  LINE: --No. You crazy... No.
  EXPRESSION: Terrified

::PATHS::
- CHOICE: "Hang up in panic"
  TARGET: rose_reaction
  STATE_CHANGE: panic = true
  CONDITION: null

::SCENE::
LOCATION: Armitage House. Dining Room (Rose's Reaction)
MOOD: Cold
CHARACTERS: Rose, Rose's family
BACKGROUND_IMAGE: armitage_house_dining_room.png
BACKGROUND_EDIT: "Rose places the phone on the dining room table and looks back at her family."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Rod hangs up in panic. He looks at Sid helplessly. Rose’s flirtacious smile goes blank. She places the phone on the dining room table and looks back at her family. They watch in approval.
  EXPRESSION: null

::PATHS::
- CHOICE: "Return to Games Room"
  TARGET: games_room_final
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Games Room
MOOD: Resigned
CHARACTERS: Chris
BACKGROUND_IMAGE: games_room.png
BACKGROUND_EDIT: "Chris, still strapped to the chair, hangs his head in resignation."

::SCRIPT::
- CHARACTER: Narrator
  LINE: “You’ve Got A Friend” plays. Chris, still strapped to the chair, hangs his head in resignation. Eyes shut, he sings along.
  EXPRESSION: null
- CHARACTER: Chris
  LINE: ...Winter, Spring, Summer and Fall, all you need to do is call. And I’ll be there. You got a friend. Ain’t it good to know you’ve got a friend. Ain’t it good to know you’ve got a friend. Oh, yeah, yeah, you’ve got a friend.
  EXPRESSION: Resigned
- CHARACTER: Narrator
  LINE: The song is over. After a moment. Chris begins to sing the opening guitar lick. He gets a couple notes before realizing he’s singing alone.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The television in front of Chris flickers off and then back on to the image of a tea cup comes into focus on the screen. A spoon comes into the shot and clinks the side of the cup. “TING TING, TING TING”
  EXPRESSION: null
- CHARACTER: Chris
  LINE: No-
  EXPRESSION: Startled
- CHARACTER: Narrator
  LINE: Before he can react, Chris falls asleep. Later... Chris wakes up bald. Static snow clicks fills the TV lighting the room. The image clicks to that of...
  EXPRESSION: null

::PATHS::
- CHOICE: "Wake up bald and see Jim Hudson on TV"
  TARGET: hospital_room_tv
  STATE_CHANGE: bald = true, sleep = true
  CONDITION: null

::SCENE::
LOCATION: Hospital Room - Day (Television)
MOOD: Interrogative
CHARACTERS: Jim Hudson, Chris
BACKGROUND_IMAGE: hospital_room_tv.png
BACKGROUND_EDIT: "Jim Hudson, also shaven, sits on a hospital bed and faces Chris through the television."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Jim Hudson, also shaven, sits on a hospital bed. And faces Chris through the television.
  EXPRESSION: null
- CHARACTER: Jim
  LINE: Hello Chris. How’s it going...? You can answer. There’s an intercom in the room; I can hear you.
  EXPRESSION: Calm
- CHARACTER: Chris
  LINE: I need water.
  EXPRESSION: Weak
- CHARACTER: Jim
  LINE: Yeah, sorry about that. If it makes you feel any better, I’m thirsty too.
  EXPRESSION: Apologetic
- CHARACTER: Chris
  LINE: I need to get outta here.
  EXPRESSION: Desperate
- CHARACTER: Jim
  LINE: Right. So, the reason I am talking to you now is so you can understand what is happening to you. I guess your ‘understanding’ it raises the success rate of this whole thing. Not even sure I ‘understand’ it.
  EXPRESSION: Explanatory
- CHARACTER: Chris
  LINE: Where’s Rose?
  EXPRESSION: Anxious
- CHARACTER: Jim
  LINE: Hot isn’t she? Hot voice anyway, you dirty dog. You’re one of the lucky one’s. The son Jeremy’s wrangling method sounds way less pleasant.
  EXPRESSION: Smug
- CHARACTER: Chris
  LINE: Is this some kind of a game to you?
  EXPRESSION: Angry
- CHARACTER: Jim
  LINE: They asked me for my favorite song, which was hard; I like all types of music. Turns out they really just needed one I knew all the words to: I went with James Taylor’s “You Got a Friend.” I hope it hasn’t been too torturous; that wasn’t the point. The point is that you learn it, and for us to have that knowledge in common.
  EXPRESSION: Explanatory
- CHARACTER: Chris
  LINE: Who the fuck are you people?
  EXPRESSION: Furious
- CHARACTER: Jim
  LINE: Oh right
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue to question Jim"
  TARGET: end
  STATE_CHANGE: anger = +2
  CONDITION: null

::SCENE::
LOCATION: Unknown
MOOD: Ominous
CHARACTERS: Narrator, Jim, Chris
BACKGROUND_IMAGE: unknown.png
BACKGROUND_EDIT: "Dark, sterile room"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Okay, let me back up and give you the cliff notes. The Armitages and I are a part of a society. A pretty extraordinary society actually.
  EXPRESSION: null
- CHARACTER: Jim
  LINE: One whose sole purpose for many years has been a search for a very powerful object. Armitage lineage redefined the nature of that search. They proved that the power didn’t just exist in that object; You see, with science the Armitage’s created a miracle.
  EXPRESSION: null
- CHARACTER: Chris
  LINE: You hypnotize me? Break my will..? Make me a slave like the others? This is some crazy racist shit.
  EXPRESSION: Angry
- CHARACTER: Jim
  LINE: No. Not racist, Chris. We don’t hate you. We want to be you... You are not going to be a slave. You’re going to be a vessel.
  EXPRESSION: null
- CHARACTER: Chris
  LINE: Wait, what?
  EXPRESSION: Confused
- CHARACTER: Jim
  LINE: Missy’s hypnosis was merely to sedate you. Oh, that and to prepare you psychologically...
  EXPRESSION: null
- CHARACTER: Chris
  LINE: For what?
  EXPRESSION: Confused
- CHARACTER: Jim
  LINE: For the procedure.
  EXPRESSION: Smiling
- CHARACTER: Chris
  LINE: What’s the procedure?
  EXPRESSION: Confused
- CHARACTER: Jim
  LINE: Are you ready...? Drum roll please. Brain transplantation. Some say it could never be done;
  EXPRESSION:null
- CHARACTER: Jim
  LINE: They experimented for centuries, but it turned out re-linking the brain to a foreign central nervous system was impossible. The nerve connections are far too intricate and delicate.
  EXPRESSION: null
- CHARACTER: Chris
  LINE: What the fuck?
  EXPRESSION: Shocked
- CHARACTER: Jim
  LINE: Dean’s the only guy who really gets the science. He’s the one who discovered that full brain transplantation isn’t actually necessary to transfer the soul, and that partial brain transplantation solves the little nerve ending problem.
  EXPRESSION: null
- CHARACTER: Chris
  LINE: No.
  EXPRESSION: Disbelieving
- CHARACTER: Narrator
  LINE: Jim holds up a Color coded diagram of the human Brain. There is a big red part that takes up 80% of the image. The other 20% is blue and located near the lower back of his skull.
  EXPRESSION: null
- CHARACTER: Jim
  LINE: Okay so... You see the blue part? That’s the piece of your brain that’s all rooted in the nervous system. So that stays; keeping those tricky little connections intact. The rest is discarded. Then they’ll remove the red part of my brain from my skull and put in yours. Your “blue” and my “red” basically absorb each other. And apparently the brain heals surprisingly fast, so assuming everything goes as planned, we should be up and functioning in a couple weeks.
  EXPRESSION: null
- CHARACTER: Chris
  LINE: And my brain?
  EXPRESSION: Anxious
- CHARACTER: Jim
  LINE: Your red part? It’ll be discarded, but don’t worry. You wont be gone. Well not completely. You’ll still be in there somewhere; limited consciousness of course; you’ll still be able to see and hear but your existence will be as a passenger... an audience. You will live in...
  EXPRESSION: null
- CHARACTER: Chris
  LINE: ...The Sunken Place.
  EXPRESSION: Defeated
- CHARACTER: Jim
  LINE: Yes. That’s what she calls it. Good! So you understand, I’ll control the motor functions, the will of our body, effectively making me--
  EXPRESSION: null
- CHARACTER: Chris
  LINE: Me... You will be me.
  EXPRESSION: Resigned
- CHARACTER: Jim
  LINE: As far as the world is concerned. It’s still a pretty new operation. Some kinks. We’re supposed to stay away from flashes of light for example. They can trigger a “momentary lapse in control of motor functions...”
  EXPRESSION: null
- CHARACTER: Chris
  LINE: Why black people?
  EXPRESSION: Angry
- CHARACTER: Jim
  LINE: Well, because you get the highest bids. For the last decade or so anyway. I wish it was less simple than that, but it’s not. You’re in fashion, baby!
  EXPRESSION: Disappointed
- CHARACTER: Narrator
  LINE: Final hope sinks from. Chris shoulders.
  EXPRESSION: null
- CHARACTER: Jim
  LINE: Honestly though, personally..? I couldn’t give two shits about race. I don’t care if you’re black, brown, green, purple... whatever. What I want is so much deeper: Your eye, man. I want those things you see through.
  EXPRESSION: null
- CHARACTER: Chris
  LINE: That’s crazy.
  EXPRESSION: Disgusted
- CHARACTER: Jim
  LINE: Take it as a compliment.
  EXPRESSION: null
- CHARACTER: Chris
  LINE: You’re not going to get away with this.
  EXPRESSION: Defiant
- CHARACTER: Jim
  LINE: We have and we will. We’ll be together soon, brother.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The television turns off. Chris clenches his body trying to pry free from his restraints, before his shoulders collapse with exhaustion. He lifts his head to a rip in the leather arm of the chair revealing its cotton stuffing. He looks at the cotton. We see Chris make a difficult decision.
  EXPRESSION: null

::SCENE::
LOCATION: Unknown
MOOD: Tense
CHARACTERS: Narrator, Chris
BACKGROUND_IMAGE: unknown.png
BACKGROUND_EDIT: "Dark, sterile room, later"

::SCRIPT::
- CHARACTER: Narrator
  LINE: We hear nothing except a heartbeat. Chris' head hangs, asleep. His lips are dry. Chris wakes up.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The Television turns on. On the screen, a woman’s hand holds a tea cup. With a spoon, she clinks it. We don’t hear it though. We still hear nothing but the HEART BEAT.
  EXPRESSION: null
- CHARACTER: Chris
  LINE: No, No--
  EXPRESSION: Panicked
- CHARACTER: Narrator
  LINE: Before Chris can finish screaming, his eyes widen. He goes limp -- unconscious again.
  EXPRESSION: null

::SCENE::
LOCATION: Unknown
MOOD: Violent
CHARACTERS: Narrator, Rose, Chris
BACKGROUND_IMAGE: unknown.png
BACKGROUND_EDIT: "Dark, sterile room, medical equipment"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Rose enters wearing a white and black nurse’s outfit with a red cross on the chest. She rolls a medical table into the room. She draws a dotted line across his forehead and around to the back of his scalp. Then she unstraps his arm and prepares it for an IV. She inserts the needle.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: She goes to put earbuds connected to an ipod in his ears but sees the arm of his chair has been stripped open. She looks at Chris. Cotton makeshift earplugs have been stuffed in his ears! He’s not really hypnotized!
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Rose tries to scream but Chris grabs her throat with his free hand and squeezes. The HEARTBEAT quickens. Rose pleads, but we don’t hear her.
  EXPRESSION: null
- CHARACTER: Rose
  LINE: Wait. Wait. Chris!.... Chri-
  EXPRESSION: Inaudible
- CHARACTER: Narrator
  LINE: Chris chokes her. Tears stream down his face.
  EXPRESSION: null
- CHARACTER: Chris
  LINE: Shhhh.
  EXPRESSION: Calm
- CHARACTER: Narrator
  LINE: Rose convulses. She scratches his hand and cheeks. He’s too strong. She stares at Chris’ eyes as her consciousness fades. Then, through the agony, her face curls into a twisted smile. She’s having fun. Psycho. Rose goes
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue the struggle"
  TARGET: end_of_scene
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Operating Room
MOOD: Intense
CHARACTERS: Narrator, Chris, Jim Hudson, Dean, Jeremy
BACKGROUND_IMAGE: operating_room.png
BACKGROUND_EDIT: "Bright medical light, two operating beds"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Chris takes the cotton out of his ears. We can hear again.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: “You’ve got a Friend” plays on the earbuds of the iPod.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Earbuds also rest in Jim Hudson’s ears playing the same song. He lies unconscious on one of two operating beds in the center of the room connected to an IV and heart monitors.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: A bright medical light shines on Jim’s shaved head which also has a dotted line around it. The other bed is empty and has a light shining on it as well. This bed is for Chris.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Dean stands in a black and white robe with a red cross in the middle, his palms upwards in silent prayer near some ceremonial candles. Jeremy watches his father. They are unaware of what’s happening in the Medical room down the hall.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Dean finishes his prayer.
  EXPRESSION: null
- CHARACTER: Dean
  LINE: Saw...
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Jeremy hands Dean a circular surgical saw.
  EXPRESSION: null
- CHARACTER: Dean
  LINE: The vessel.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Jeremy leaves as Dean begins to saw into Jim’s cranium.
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue observing"
  TARGET: dark_hallway
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Dark Hallway
MOOD: Suspenseful
CHARACTERS: Narrator, Chris, Jeremy, Rose
BACKGROUND_IMAGE: dark_hallway.png
BACKGROUND_EDIT: "Dimly lit hallway, games room door"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Chris finds an old badminton set.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Jeremy exits the room briskly and walks down a dark hallway. He turns into the games room and finds Rose’s body.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Jeremy’s eyes go wild. He turns as Chris emerges lunging from the darkness with a badminton racket. Before Jeremy can scream, Chris slams him in the face with the metal side of the racket. He pulls Jeremy inside and shuts the door cutting off the sound from outside.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Jeremy wilts in pain.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Chris whips him over and over warping the racket to a crumpled bloody mess.
  EXPRESSION: null

::PATHS::
- CHOICE: "Return to operating room"
  TARGET: operating_room_2
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Operating Room
MOOD: Violent
CHARACTERS: Narrator, Dean, Chris, Deer
BACKGROUND_IMAGE: operating_room.png
BACKGROUND_EDIT: "Operating room, disarray"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Dean finishes sawing the top of Jim’s skull off. He removes the cranium preciously exposing Jim’s brain.
  EXPRESSION: null
- CHARACTER: Dean
  LINE: Jeremy...?
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Dean walks to the doorway. Dean scans the dark hallway. It’s quiet.
  EXPRESSION: null
- CHARACTER: Dean
  LINE: Ro Ro...?
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Chris emerges charging from the darkness with Deer’s head in his arms. He punctures Dean through his neck and shoulder with the antlers.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Dean and stumbles back into the operating room, deer’s head attached.
  EXPRESSION: null
- CHARACTER: Dean
  LINE: Miss--
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: His call to Missy devolves into gargles. Dean falls knocking the unused bed over along with some candles. The bed has caught fire. The fire grows fast.
  EXPRESSION: null

::PATHS::
- CHOICE: "Proceed to kitchen"
  TARGET: kitchen
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Kitchen
MOOD: Ominous
CHARACTERS: Narrator, Missy, Georgina, Walter, Chris
BACKGROUND_IMAGE: kitchen.png
BACKGROUND_EDIT: "Nighttime kitchen, window reflection"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Missy takes a whistling tea pot off the stove and pours herself a cup. Georgina sits nearby knitting. The window, like before reflects the room around them.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: She sniffs the air. She is suddenly afraid. She turns off the light illuminating the back yard. Walter runs back and forth in the distance. She turns the light back on again.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Chris’ reflection is now behind hers. He looks savage; covered in blood.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Georgina screams and runs out the back door.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Chris heads to the door, but sees his phone on the dining room table. He goes for it.
  EXPRESSION: null

::PATHS::
- CHOICE: "Go to dining room"
  TARGET: dining_room
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Dining Room
MOOD: Violent Confrontation
CHARACTERS: Narrator, Chris, Missy
BACKGROUND_IMAGE: dining_room.png
BACKGROUND_EDIT: "Dining room, Chris's phone on table"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Chris runs through the dining room and finds his cell phone on the dining room table.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Chris picks up his phone and presses the power button. The loading screen comes up.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Chris grunts with frustration as he hears a creak behind him. It’s Missy, now in the kitchen doorway behind him holding her teacup and spoon. She begins clinking her tea cup...
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: TING...
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Chris knocks the cup out of her hand spraying hot water on her chest and face. She screams.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The cat bounds off the dining room table at Chris’ face.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Chris punches it out of the air. This has given Missy enough time to grab a knife. She lunges at Chris screaming psychotically.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Chris can’t pin her down. She slices his hands. Chris grabs the tea pot and cracks her in the head with it. She falls. He hits her one more time. Done.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The cat slinks out an open window.
  EXPRESSION: null

::PATHS::
- CHOICE: "Go to foyer"
  TARGET: foyer
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Foyer
MOOD: Chaotic
CHARACTERS: Narrator, Chris, Jeremy
BACKGROUND_IMAGE: foyer.png
BACKGROUND_EDIT: "Foyer, entryway to front door"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Chris runs towards the front door. Before he can open it, he hears a footsteps running upstairs from the basement followed bloodcurdling scream from back in the kitchen:
  EXPRESSION: null
- CHARACTER: Jeremy (O.S.)
  LINE: Ahhhhhhhh!!!!!!!!!
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Jeremy bursts though the dining room and pounces on Chris’ back. The two roll around.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Chris throws his elbow back at Jeremy who blocks it and uses it to put Chris in a choke hold from behind.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Chris slams the back of his head into Jeremy’s face. He does it again, and again, and again. Jeremy squeezes tighter.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Chris, about to pass out, reaches into Jeremy’s pocket and pulls out his keys. He scrapes them deep into Jeremy’s eye.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Jeremy screams in pain and Chris wriggles out of his grasp tripping him with an improvised Judo throw.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Jeremy lunges at Chris again but slips on his own blood banging the back of his head on the coffee table. He’s out.
  EXPRESSION: null

::PATHS::
- CHOICE: "Exit to front yard"
  TARGET: front_yard
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Front Yard
MOOD: Escape
CHARACTERS: Narrator, Chris, Jeremy
BACKGROUND_IMAGE: front_yard.png
BACKGROUND_EDIT: "Front yard, car visible"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Chris begins to run but then sees the beige sports car we recognize from the opening scene. He looks at Jeremy downed in the doorway and then at the keys in his hand.
  EXPRESSION: null

::PATHS::
- CHOICE: "Get in the car"
  TARGET: sports_car
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Sports Car
MOOD: Urgent Escape
CHARACTERS: Narrator, Chris, 911 Operator
BACKGROUND_IMAGE: sports_car.png
BACKGROUND_EDIT: "Interior of sports car at night"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Chris is in the driver’s seat. The tubular metal helmet sits next to him in the passengers seat. His phone finally turns on. There is a very small amount of batteries.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: He turns the ignition. The English to French tutorial comes on.
  EXPRESSION: null
- CHARACTER: Tutorial
  LINE: I seem to have misplaced my passport. Je crois avoi egare mon passeport.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Chris peels off, driving fast through the field into the night. He dials 911.
  EXPRESSION: null
- CHARACTER: 911 Operator
  LINE: 911 emergency, I’m at the home of Dean and Missy Armitage--
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue driving"
  TARGET: end
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Exterior - Road at night
MOOD: Chaotic, Violent
CHARACTERS: Chris, Georgina, Tutorial
BACKGROUND_IMAGE: road_night.png
BACKGROUND_EDIT: "Dark road, house in background"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Chris looks in the rearview mirror as the house gets smaller behind him. All of a sudden, BAM! The car slams into and over Georgina, who, in the night, seems to come out of nowhere. The phone falls.
  EXPRESSION: Shocked
- CHARACTER: Chris
  LINE: Ahhhh!
  EXPRESSION: Terrified
- CHARACTER: Tutorial
  LINE: Can you direct me to the nearest hospital? Pouvez-vous me diriger vers l’hopital le plus proche?
  EXPRESSION: Neutral
- CHARACTER: Narrator
  LINE: He drives on a few more seconds on a flat tire but then stops the car. Chris breathes heavy.
  EXPRESSION: Panicked

::PATHS::
- CHOICE: "Continue driving"
  TARGET: road_stop
  STATE_CHANGE: None
  CONDITION: None

::SCENE::
LOCATION: Exterior - Road (stopped car)
MOOD: Desperate, Conflicted
CHARACTERS: Chris
BACKGROUND_IMAGE: road_stop.png
BACKGROUND_EDIT: "Car stopped on the side of the road, flat tire"

::SCRIPT::
- CHARACTER: Chris
  LINE: No... no... Don’t do it... Just get the fuck outta here... Just go! Just... Fuck!
  EXPRESSION: Agitated
- CHARACTER: Narrator
  LINE: Chris puts the car in reverse and drives backwards beside the motionless bloody heap that is Georgina.
  EXPRESSION: Determined
- CHARACTER: Tutorial
  LINE: Where is the nearest train? EST LA GARE LA PLUS PROCHE?
  EXPRESSION: Neutral
- CHARACTER: Narrator
  LINE: He looks back at the house which is now filling with smoke.
  EXPRESSION: Concerned
- CHARACTER: Narrator
  LINE: Chris quickly gets out of the car and lifts what’s left of Georgina’s mangled unconscious body into the passenger’s seat of the car. He shuts the door and gets in the driver’s seat. He floors it.
  EXPRESSION: Desperate

::PATHS::
- CHOICE: "Drive away quickly"
  TARGET: car_interior_driving
  STATE_CHANGE: None
  CONDITION: None

::SCENE::
LOCATION: Interior - Car during pursuit
MOOD: Eerie, Violent
CHARACTERS: Chris, Georgina, Tutorial
BACKGROUND_IMAGE: car_interior_driving.png
BACKGROUND_EDIT: "Driving at night, Georgina in passenger seat"

::SCRIPT::
- CHARACTER: Narrator
  LINE: After a moment of driving, Georgina’s eyes open and she rises. The wig slides off her head revealing an old surgical scar around the top of her head. Chris hasn’t noticed her yet. He reaches for his phone.
  EXPRESSION: Surprised
- CHARACTER: Tutorial
  LINE: Can you please call the police? Pouvez-vous s’il vous plait appelez la police?
  EXPRESSION: Neutral
- CHARACTER: Narrator
  LINE: Annoyed, Chris turns off the sound system just before Georgina grabs his face and scratches it.
  EXPRESSION: Annoyed
- CHARACTER: Georgina
  LINE: Ahhhhh!!
  EXPRESSION: In pain
- CHARACTER: Chris
  LINE: Ahhhhhhhh!!
  EXPRESSION: Terrified
- CHARACTER: Narrator
  LINE: Chris veers the car into a tree. Georgina‘s head hits the windshield hard and bursts open. She’s dead. So is the car.
  EXPRESSION: Violent

::PATHS::
- CHOICE: "React to the crash"
  TARGET: exterior_crash_scene
  STATE_CHANGE: None
  CONDITION: None

::SCENE::
LOCATION: Exterior - Crash Scene
MOOD: Shocking, Violent
CHARACTERS: Chris, Jeremy, Georgina, Walter/Grandpa
BACKGROUND_IMAGE: exterior_crash_scene.png
BACKGROUND_EDIT: "Car crashed into a tree, smoking house in background"

::SCRIPT::
- CHARACTER: Narrator
  LINE: A bullet hits the rear view mirror. Jeremy stands in front of the smoking house with a hunting rifle. He’s soaked in blood.
  EXPRESSION: Shocked
- CHARACTER: Jeremy
  LINE: Grandma!!!!
  EXPRESSION: Grief
- CHARACTER: Narrator
  LINE: Chris looks at Georgina’s body. Georgina was Grandma.
  EXPRESSION: Realization
- CHARACTER: Jeremy
  LINE: Grampa!
  EXPRESSION: Grief
- CHARACTER: Narrator
  LINE: Walter, the grounds keeper, rounds the house at top speed. Walter is grandpa and he’s so fast.
  EXPRESSION: Astonished
- CHARACTER: Jeremy
  LINE: Get him!!!
  EXPRESSION: Angry
- CHARACTER: Narrator
  LINE: Chris crawls out of the car as Walter/Grandpa sprints across the front lawn straight at him. Walter’s hat flies off revealing the surgical scar around his head like the others.
  EXPRESSION: Frightened
- CHARACTER: Narrator
  LINE: Jeremy shoots again, and it grazes Chris’ side. Chris runs through the trees. Walter/grandpa closes the gap quickly. Another shot hits a tree. As Chris reaches the road, Walter/Grandpa pounces like a jaguar and rolls him over on his back. He pushes his thumbs into Chris’ eyes.
  EXPRESSION: Painful
- CHARACTER: Grandpa
  LINE: Damn you to Hell!!!
  EXPRESSION: Vengeful
- CHARACTER: Narrator
  LINE: Jeremy arrives behind them crying.
  EXPRESSION: Grief
- CHARACTER: Jeremy
  LINE: Kill him, Grandpa.
  EXPRESSION: Desperate
- CHARACTER: Grandpa
  LINE: The gun, Jeremy.
  EXPRESSION: Commanding
- CHARACTER: Narrator
  LINE: Jeremy tosses the rifle. Grandpa catches it and holds it up to Chris’ head.
  EXPRESSION: Tense
- CHARACTER: Grandpa
  LINE: You ruined everything!!!
  EXPRESSION: Furious
- CHARACTER: Narrator
  LINE: Chris, blinded, raises his phone to Walter/Grandpa’s face. He takes a picture, flashing straight into Walter/Grandpa’s eyes. Walter/Grandpa doesn’t shoot. Instead he looks up. Jeremy is confused as to why Walter/Grandpa has stopped.
  EXPRESSION: Strategic
- CHARACTER: Jeremy
  LINE: What...? Grandpa--?
  EXPRESSION: Confused
- CHARACTER: Narrator
  LINE: Walter/Grandpa spins and gathers his bearing. His eye is cocked and blood trickles out of his nose. He lets out a pained moan reminiscent of the deer’s.
  EXPRESSION: Injured
- CHARACTER: Walter/Grandpa
  LINE: Ahhhhhhh!
  EXPRESSION: Pain
- CHARACTER: Narrator
  LINE: Walter/Grandpa shoots Jeremy in the chest. He falls. Chris, on his back, pushes himself away. Walter/Grandpa sees Chris’ scurry. He turns looking mad.
  EXPRESSION: Shocked
- CHARACTER: Chris
  LINE: Wait.
  EXPRESSION: Pleading
- CHARACTER: Narrator
  LINE: Walter/Grandpa raises the gun under his own chin and shoots himself through the head. He falls. Approaching sirens blare in the distance.
  EXPRESSION: Tragic
- CHARACTER: Narrator
  LINE: Chris lays in shock. It’s over. Just then a hand grabs Chris’ face! Jeremy’s still alive! Blood pours from his mouth.
  EXPRESSION: Renewed Fear
- CHARACTER: Jeremy
  LINE: Ahhhhhh!
  EXPRESSION: Agonized
- CHARACTER: Narrator
  LINE: They both go for the gun, grabbing it at the same time. They roll around in the grass. Chris ends up on top. He bludgeons Jeremy over and over with the butt of the gun into the ground. Chris is lost in violence.
  EXPRESSION: Brutal
- CHARACTER: Narrator
  LINE: 2 police cars pull up. He drops the gun.
  EXPRESSION: Tense
- CHARACTER: Cops
  LINE: Hands! Hands! Get away from the weapon/ Show me your hands!/ Hands! Hands!! Get on your Knees!/ Hands! Hands!/ Goddamn Hands!!!
  EXPRESSION: Authoritative
- CHARACTER: Narrator
  LINE: Chris, covered in blood, raises his sliced hands.
  EXPRESSION: Defeated
- CHARACTER: Chris
  LINE: Look in the basement!
  EXPRESSION: Urgent
- CHARACTER: Narrator
  LINE: He is violently swarmed by officers. The house burns.
  EXPRESSION: Chaos

::PATHS::
- CHOICE: "Surrender to police"
  TARGET: prison_visiting_room
  STATE_CHANGE: None
  CONDITION: None

::SCENE::
LOCATION: INT. MAXIMUM SECURITY PRISON. VISITING ROOM - NIGHT
MOOD: Weary, Frustrated
CHARACTERS: Rod, Chris
BACKGROUND_IMAGE: prison_visiting_room.png
BACKGROUND_EDIT: "Dimly lit prison visiting room"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Rod sits down opposite Chris who wears a prison jumpsuit and smokes a cigarette. Both of them look like shit. Rod is gaunt with circles under his eyes. Chris’ hair and beard have grown in.
  EXPRESSION: Tired
- CHARACTER: Narrator
  LINE: There’s a long silence.
  EXPRESSION: Heavy
- CHARACTER: Rod
  LINE: I really need to...
  EXPRESSION: Pleading
- CHARACTER: Chris
  LINE: ...I don’t remember...
  EXPRESSION: Amnesiac
- CHARACTER: Rod
  LINE: ...impress on you the importance of remembering some of those names. The fire didn’t leave enough--
  EXPRESSION: Frustrated
- CHARACTER: Narrator
  LINE: They’ve clearly had this conversation many times before.
  EXPRESSION: Repetitive
- CHARACTER: Chris
  LINE: I don’t remember.
  EXPRESSION: Resigned
- CHARACTER: Rod
  LINE: You gotta help me out, Chris. Secret societies doesn’t get you very far on Google. I’m over here feeling like I’m playing connect the dots on a fucking football field. One name...
  EXPRESSION: Desperate
- CHARACTER: Chris
  LINE: I don’t remember.
  EXPRESSION: Unwavering
- CHARACTER: Rod
  LINE: Well, try again please.
  EXPRESSION: Hopeful
- CHARACTER: Chris
  LINE: Rod.
  EXPRESSION: Neutral
- CHARACTER: Rod
  LINE: Let’s start at the beginning; walk me through it again.
  EXPRESSION: Patient
- CHARACTER: Chris
  LINE: Rod.
  EXPRESSION: Resigned
- CHARACTER: Narrator
  LINE: Rod knows he’s been defeated.
  EXPRESSION: Defeated
- CHARACTER: Chris
  LINE: I’m good, man. I stopped it. You know? I stopped it.
  EXPRESSION: Peaceful
- CHARACTER: Narrator
  LINE: Chris is at peace. He takes a long good drag of his cigarette then gets up and leaves.
  EXPRESSION: Serene

::PATHS::
- CHOICE: "Leave the visiting room"
  TARGET: prison_hallway
  STATE_CHANGE: None
  CONDITION: None

::SCENE::
LOCATION: INT. MAXIMUM SECURITY PRISON. HALLWAY - NIGHT
MOOD: Finality, Resignation
CHARACTERS: Two Guards, Chris
BACKGROUND_IMAGE: prison_hallway.png
BACKGROUND_EDIT: "Prison hallway with guards escorting Chris"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Two Guards escort Chris back to his cell. He whistles “You Got A Friend.”
  EXPRESSION: Calm
- CHARACTER: Narrator
  LINE: The End
  EXPRESSION: Final

::PATHS::
- CHOICE: "End of story"
  TARGET: end
  STATE_CHANGE: None
  CONDITION: None

