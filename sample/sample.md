::SCENE::
LOCATION: Highway
MOOD: Calm
CHARACTERS: Narrator, Mike
BACKGROUND_IMAGE: highway.png
BACKGROUND_EDIT: "Daytime, empty dull road"

::SCRIPT::
- CHARACTER: Narrator
  LINE: A dull highway. A crappy sedan roars by.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: At the wheel, driving this piece of shit, is MIKE ENSLIN, 35, a grizzled, weary soul. He stares glassily at the road, a cigarette behind his ear, a styrofoam cup of Exxon coffee at his mouth.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: A sign drifts by: "Woodfin, Rte 251 N - Asheville, Interstate 240 E, Hwy 40, Next Right, Thru Traffic Merge”.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Mike frowns.
  EXPRESSION: Angry

::PATHS::
- CHOICE: "Continue driving"
  TARGET: country_road
  STATE_CHANGE: frustration = +1
  CONDITION: null

::SCENE::
LOCATION: Country Road
MOOD: Rising Tension
CHARACTERS: Narrator, Mike
BACKGROUND_IMAGE: country_road.png
BACKGROUND_EDIT: "Unpaved muddy road, dusk, heavy rain"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Rain pours down on an unpaved country intersection.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Mike stands outside his car, soaked, checking a wet map. He’s confused and annoyed. There are no road markings at all. He checks his watch.
  EXPRESSION: Angry

::PATHS::
- CHOICE: "Keep searching for the inn"
  TARGET: country_inn
  STATE_CHANGE: frustration = +1
  CONDITION: null

::SCENE::
LOCATION: Country Inn
MOOD: Dread
CHARACTERS: Narrator, Mike
BACKGROUND_IMAGE: country_inn.png
BACKGROUND_EDIT: "Nighttime, porch lanterns glowing, deep shadows"

::SCRIPT::
- CHARACTER: Narrator
  LINE: A quaint rural inn, dark of night. The ambiance is picturesque, but off-putting. Porch lanterns glow. Shadows are deep. An ancient elm tree frames the banging weathered-sign: "The Camden Inn".
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Finally — headlights. Mike’s car pulls up in the mud.
  EXPRESSION: null

::PATHS::
- CHOICE: "Enter the inn"
  TARGET: inn_lobby
  STATE_CHANGE: fear = +1
  CONDITION: null

::SCENE::
LOCATION: Inn Lobby
MOOD: Rising Tension
CHARACTERS: Narrator, Mike, Mr. Innkeeper, Mrs. Innkeeper
BACKGROUND_IMAGE: inn_lobby.png
BACKGROUND_EDIT: "Nighttime interior, cozy but old-fashioned"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Mike trudges into the homey, worn lobby.
  EXPRESSION: null
- CHARACTER: Mike
  LINE: Hi. Mike Enslin, checking in —
  EXPRESSION: Angry
- CHARACTER: Mr. Innkeeper
  LINE: Oh, Mr. Enslin! We were so worried you weren’t gonna show!
  EXPRESSION: Happy
- CHARACTER: Mrs. Innkeeper
  LINE: It's such an honor to have you here.
  EXPRESSION: Happy
- CHARACTER: Mike
  LINE: Yeah. Great. Uh, if I could just get my key —
  EXPRESSION: Angry
- CHARACTER: Mr. Innkeeper
  LINE: You probably want to hear all about our haunted history! Well, that rear staircase is where the maid reputedly hung herself in 1870.
  EXPRESSION: Happy
- CHARACTER: Mrs. Innkeeper
  LINE: There’s a picture —
  EXPRESSION: Happy
- CHARACTER: Mike
  LINE: Can we do this in the morning?
  EXPRESSION: Angry
- CHARACTER: Mrs. Innkeeper
  LINE: Wait! It's printed in our brochure!
  EXPRESSION: Happy
- CHARACTER: Narrator
  LINE: She thrusts out a brochure that says "HAUNTED!" There’s a PHOTO of the lobby, and a faint white shape in a window.
  EXPRESSION: null
- CHARACTER: Mrs. Innkeeper
  LINE: Do you SEE her?
  EXPRESSION: Happy
- CHARACTER: Mike
  LINE: Uh —
  EXPRESSION: Surprised
- CHARACTER: Mrs. Innkeeper
  LINE: A guest took that photo in 1986. You can sort of see Sylvia's "ethereal apparition" reflected in the window.
  EXPRESSION: Happy
- CHARACTER: Narrator
  LINE: Mike stares, unimpressed.
  EXPRESSION: Angry
- CHARACTER: Mr. Innkeeper
  LINE: At least, Sylvia is what we call her.
  EXPRESSION: Happy
- CHARACTER: Mike
  LINE: Terrifying. I’m ready to hit the sack. In your letter, you mentioned the scariest rooms were in the old attic?
  EXPRESSION: Angry
- CHARACTER: Mrs. Innkeeper
  LINE: That's right. The third floor is the former servant's quarters. People say all Sylvia's children died up there of tuberculosis. Right up there. Right above where you and I are standing, right now...
  EXPRESSION: Afraid
- CHARACTER: Mr. Innkeeper
  LINE: Guests have reported strange sounds. At the stroke of midnight, there’s been weird noises. Creaks. Moans. Our best advice... is to lock your door from the inside.
  EXPRESSION: Afraid

::PATHS::
- CHOICE: "Go to room"
  TARGET: inn_room
  STATE_CHANGE: fear = +2, frustration = -1
  CONDITION: null

::SCENE::
LOCATION: Mike’s Inn Room
MOOD: Dread
CHARACTERS: Narrator, Mike
BACKGROUND_IMAGE: inn_room.png
BACKGROUND_EDIT: "Late night, antique furniture, dim lighting"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Mike lies on the antique bed, on a quilt, drinking mini-bar booze. He has an army of tiny Scotches, Gins, Vodkas. He's bored out of his mind.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Later, the boozes are empty. Somewhere, a grandfather clock chimes midnight. DONG, DONG, DONG! Mike groggily glances at a bedside clock, waiting. Listening. Alert to anything...
  EXPRESSION: Afraid
- CHARACTER: Narrator
  LINE: Suddenly a loud crash! Mike jerks, startled. He jumps up, concerned... then realizes it's only thunder. Oh.
  EXPRESSION: Surprised
- CHARACTER: Narrator
  LINE: Later, Mike is snoring, drooling, passed out.
  EXPRESSION: null

::PATHS::
- CHOICE: "Fall asleep"
  TARGET: end
  STATE_CHANGE: drunk = true, fear = +1
  CONDITION: null
