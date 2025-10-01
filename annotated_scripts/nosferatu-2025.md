::SCENE::
LOCATION: Black
MOOD: Mysterious
CHARACTERS: Ellen (V.O.)
BACKGROUND_IMAGE: black.png
BACKGROUND_EDIT: "Pure black screen"

::SCRIPT::
- CHARACTER: Ellen (V.O.)
  LINE: (whispered) Once upon a time...
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Beat. A child’s desperate crying is heard, echoing in the night.
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue"
  TARGET: nursery
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Country Manor House. Nursery
MOOD: Dread
CHARACTERS: Narrator, Ellen
BACKGROUND_IMAGE: nursery.png
BACKGROUND_EDIT: "Dark, ornate child's bedroom at night"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The crying continues in the darkness of a child’s ornate bedroom.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The tears come from a pretty teenage girl. White skin, black hair, and enormous elfin eyes. Her name is Ellen. There is something supernatural and compelling about her...
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: She moves to the edge of her bed and clasps her hands together in fervent prayer.
  EXPRESSION: null
- CHARACTER: Ellen
  LINE: Come to me. Come to me: A guardian angel, a spirit of comfort – spirit of any celestial sphere – anything – hear my call.
  EXPRESSION: Pleading
- CHARACTER: Narrator
  LINE: Now she whispers silently, in her head, to the infinite:
  EXPRESSION: null
- CHARACTER: Ellen (V.O.)
  LINE: Come to me.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Pause. Ellen hears a silvery male voice whispering quietly in the wind. It grows louder. He speaks in an ancient, indecipherable language.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: She rises from bed like a phantom.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: A massive shadow emerges from her window.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: She walks to it, becoming shrouded in its darkness. It’s as if the shadow is embracing her. She merges with the apparition, inhaling its sweet scent. It is a powerful, unknown bliss. Her body trembles.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: She levitates, her toes inches above the floor.
  EXPRESSION: null
- CHARACTER: Shadow (V.O.)
  LINE: (whispered, subtitled) You are not for the living. You are not for human kind.
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue to the garden"
  TARGET: topiary_garden
  STATE_CHANGE: supernatural_connection = +1
  CONDITION: null

::SCENE::
LOCATION: Manor House. Topiary Garden
MOOD: Horror
CHARACTERS: Ellen, Shadow (V.O.)
BACKGROUND_IMAGE: topiary_garden.png
BACKGROUND_EDIT: "Manor house garden at night, dark shadows"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Ellen sleepwalks into the night.
  EXPRESSION: null
- CHARACTER: Shadow (V.O.)
  LINE: (whispered, subtitled) And shall you be one with me ever-eternally. Do you swear it?
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: CLOSE ON: Ellen, motionless in darkness.
  EXPRESSION: null
- CHARACTER: Ellen
  LINE: I swear.
  EXPRESSION: Resolute
- CHARACTER: Narrator
  LINE: SUDDENLY: Ellen is lying in the garden. The shadow presses on her... Harder... Harder... Her pleasure turns to pain. Out of nowhere, a dark hand grabs her throat, attacking her violently!
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: IMAGE (lasting under 12 frames): A horrible, naked, corpse-like demon lets out a diabolical growl, straddling Ellen!
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Ellen screams as if being stabbed in the heart!
  EXPRESSION: Terrified
- CHARACTER: Narrator
  LINE: THE NEXT MOMENT: Ellen is nearly buried in the garden dirt – violently seizing.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: AUDIO: Music builds to a horrific, blistering orchestral climax that would bring Beethoven to his knees in torment.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: TITLE: N O S F E R A T U
  EXPRESSION: null

::PATHS::
- CHOICE: "Transition to morning"
  TARGET: hutter_house_bedroom
  STATE_CHANGE: trauma = +1
  CONDITION: null

::SCENE::
LOCATION: Hutters House. Bedroom
MOOD: Unease
CHARACTERS: Narrator, Ellen, Thomas
BACKGROUND_IMAGE: hutter_house_bedroom.png
BACKGROUND_EDIT: "Early morning, cozy but slightly shabby middle-class bedroom"

::SCRIPT::
- CHARACTER: Narrator
  LINE: CLOSE ON: Ellen is now a young woman, early 20s. She opens her eyes from a nightmare. She gasps, frozen in bed. She takes a beat and realises she is awake. She rolls over, reaching to embrace her husband...
  EXPRESSION: null
- CHARACTER: Ellen
  LINE: Thomas.
  EXPRESSION: Worried
- CHARACTER: Narrator
  LINE: But he isn’t there.
  EXPRESSION: null
- CHARACTER: Ellen
  LINE: Thomas?
  EXPRESSION: Worried
- CHARACTER: Narrator
  LINE: She looks across the room: Thomas Hutter (mid 20s) is tying his cravat before a small mirror. He is very invested in tying it well. His back is to her. He’s handsome, if not pretty. Kind, determined eyes. He seems entirely unaware of the darkness in the world. Their middle-class bedroom is cute, with brand new, aspirational furnishing. These help to disguise its overall shabbiness.
  EXPRESSION: null
- CHARACTER: Thomas
  LINE: What’s that, my love?
  EXPRESSION: Kind
- CHARACTER: Narrator
  LINE: Thomas turns to her tightening his knot. Ellen is frightened.
  EXPRESSION: null
- CHARACTER: Thomas
  LINE: What is it?
  EXPRESSION: Concerned
- CHARACTER: Narrator
  LINE: Thomas goes to her, tenderly.
  EXPRESSION: null
- CHARACTER: Ellen
  LINE: Nothing. I... I dreamt... I –
  EXPRESSION: Frightened
- CHARACTER: Thomas
  LINE: Come here. There is nothing to be afraid of.
  EXPRESSION: Reassuring
- CHARACTER: Narrator
  LINE: Ellen wraps her arms around him tight, swooning.
  EXPRESSION: null
- CHARACTER: Ellen
  LINE: The honeymoon was yet too short!
  EXPRESSION: Playful
- CHARACTER: Narrator
  LINE: She tries to bring him into bed. Thomas falls onto her.
  EXPRESSION: null
- CHARACTER: Ellen
  LINE: Take off your shoes.
  EXPRESSION: Playful
- CHARACTER: Thomas
  LINE: I wish I could stay, my love.
  EXPRESSION: Affectionate
- CHARACTER: Narrator
  LINE: She covers him with kisses. He glows. Their love is pure.
  EXPRESSION: null
- CHARACTER: Thomas
  LINE: How should I have earned such a doting wife?
  EXPRESSION: Grateful
- CHARACTER: Narrator
  LINE: Greta the cat crawls into bed on top of them. Thomas laughs.
  EXPRESSION: null
- CHARACTER: Thomas
  LINE: (kind) Ellen, I have told you not to let her into bed. I cannot wear anything dark. I’m absolutely covered in it.
  EXPRESSION: Mildly Annoyed
- CHARACTER: Narrator
  LINE: He takes a few cat hairs off him while Ellen caresses the cat.
  EXPRESSION: null
- CHARACTER: Ellen
  LINE: But Greta loves it here. She wishes you to stay, too.
  EXPRESSION: Affectionate
- CHARACTER: Thomas
  LINE: Today is of the utmost importance for us.
  EXPRESSION: Serious
- CHARACTER: Ellen
  LINE: But one minute more.
  EXPRESSION: Pleading
- CHARACTER: Narrator
  LINE: Thomas kisses her. He looks at his watch. He’s later than he thought!
  EXPRESSION: null
- CHARACTER: Thomas
  LINE: I really must be off.
  EXPRESSION: Hurried
- CHARACTER: Narrator
  LINE: Ellen gets out of bed and they both brush the cat hair off of his frock coat. He pecks Ellen again, quickly.
  EXPRESSION: null
- CHARACTER: Thomas
  LINE: Goodbye.
  EXPRESSION: Affectionate
- CHARACTER: Narrator
  LINE: HOLD ON: Ellen, troubled by her dream, cuddling with Greta.
  EXPRESSION: null
- CHARACTER: Ellen
  LINE: (whispered) He has the position already. He’ll send him away.
  EXPRESSION: Troubled

::PATHS::
- CHOICE: "Follow Thomas to Wisburg"
  TARGET: wisburg_old_town
  STATE_CHANGE: apprehension = +1
  CONDITION: null

::SCENE::
LOCATION: Wisburg. Old Town
MOOD: Bustling
CHARACTERS: Narrator, Thomas
BACKGROUND_IMAGE: wisburg_old_town.png
BACKGROUND_EDIT: "Muddy, cramped cobblestone street in a Baltic port city, foggy morning"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Thomas jogs through a muddy and cramped cobblestone street of a bustling Baltic port city. The smell of horse dung, fish, and charcoal hangs in the foggy streets. He hops over a pile of steaming horse droppings.
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue to Market Street"
  TARGET: wisburg_market_street
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Wisburg Street. Market Street
MOOD: Busy
CHARACTERS: Narrator, Thomas
BACKGROUND_IMAGE: wisburg_market_street.png
BACKGROUND_EDIT: "Busy street with cattle, canals, warehouses, boats, steamboats, and harbor bells"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Thomas tries to pass through a large herd of cattle being led to the market square.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: He rushes past side street views of the busy canals full of boats, and lined with towering warehouses, funnelling toward the harbour. Workmen holler. Steamboats whistle. Harbour bells ring.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Thomas takes a shortcut through one of the old medieval passageways.
  EXPRESSION: null

::PATHS::
- CHOICE: "Enter the estate agency"
  TARGET: passage_knocks_estate_agency
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Passage/Knock’s Estate Agency
MOOD: Foreboding
CHARACTERS: Narrator, Thomas
BACKGROUND_IMAGE: passage_knocks_estate_agency.png
BACKGROUND_EDIT: "Dark passage leading to a crooked brick building with a stepped gable, sign reads 'Knock & Assoc. Estate Agents'"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Thomas emerges from the dark passage, running now.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Before him is a crooked brick building with a stepped gable. The sign, in German, reads “Knock & Assoc. Estate Agents”.
  EXPRESSION: null

::PATHS::
- CHOICE: "Enter the agency"
  TARGET: knocks_estate_agency_reception
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Knock’s Estate Agency. Reception
MOOD: Tense
CHARACTERS: Narrator, Thomas, Two Old Clerks
BACKGROUND_IMAGE: knocks_estate_agency_reception.png
BACKGROUND_EDIT: "Old, dark, dusty agency with two old clerks behind a counter"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Thomas stands out of breath in the old, dark, dusty agency. The shop bell is still ringing from his entrance.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Two old clerks look up at him through their thick spectacles.
  EXPRESSION: null
- CHARACTER: Clerk
  LINE: You have kept him a quarter hour.
  EXPRESSION: Stern
- CHARACTER: Narrator
  LINE: Thomas removes his hat, bowing slightly to the clerk. A strange laughter is heard from afar.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Thomas skulks down a dark corridor of profusely piled paperwork, anxiously fixing his hair. The menacing laughter getting louder. Thomas slowly opens the door, slightly ajar...
  EXPRESSION: null

::PATHS::
- CHOICE: "Enter Knock's Office"
  TARGET: knocks_estate_agency_office
  STATE_CHANGE: apprehension = +1
  CONDITION: null

::SCENE::
LOCATION: Knock’s Estate Agency. Knock’s Office
MOOD: Unsettling
CHARACTERS: Narrator, Thomas, Knock
BACKGROUND_IMAGE: knocks_estate_agency_office.png
BACKGROUND_EDIT: "Office of a wealthy man who appears to be near mental breakdown"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Knock is clearly a man of great status and wealth. Yet, he seems near a mental breakdown – or has it already begun?
  EXPRESSION: null
- CHARACTER: Thomas
  LINE: Pray, pardon me, Herr Knock, for my –
  EXPRESSION: Apologetic
- CHARACTER: Knock
  LINE: Your delay is providence, my boy, providence! Come in, come in. Still preparing the account.
  EXPRESSION: Enthusiastic
- CHARACTER: Narrator
  LINE: Thomas watches the goblin-like man scribble at his documents, letting out a freakish snicker, like a simmering tea-kettle. Thomas tries to ignore his tick.
  EXPRESSION: null
- CHARACTER: Knock
  LINE: You have been contracting with us for well over two years now, Herr Hutter?
  EXPRESSION: Inquisitive
- CHARACTER: Thomas
  LINE: And I thank you,
  EXPRESSION: Grateful

::PATHS::
- CHOICE: "Continue the conversation"
  TARGET: continue_meeting
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Knock's Office
MOOD: Professional with underlying unease
CHARACTERS: Narrator, Knock, Thomas
BACKGROUND_IMAGE: knocks_office.png
BACKGROUND_EDIT: "A well-appointed but slightly old-fashioned office."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Sir, for considering me.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: When tidings of your recent nuptials but reached my ears, I knew it was providence. A new husband requires new wages.
  EXPRESSION: null
- CHARACTER: Thomas
  LINE: You are too generous, sir.
  EXPRESSION: Grateful
- CHARACTER: Knock
  LINE: Do extend my tardy congratulations to your wife.
  EXPRESSION: Warm
- CHARACTER: Thomas
  LINE: Thank you, sir.
  EXPRESSION: Polite
- CHARACTER: Knock
  LINE: She is truly a... A nonpareil of beauty. Almost a sylph.
  EXPRESSION: Thoughtful
- CHARACTER: Narrator
  LINE: The comment makes Thomas uneasy. He changes the subject.
  EXPRESSION: Uneasy
- CHARACTER: Thomas
  LINE: Yes, thank you, sir... and I am most eager to proceed with whatever your request, that I might be fully engaged with the firm.
  EXPRESSION: Eager
- CHARACTER: Knock
  LINE: Indeed. Providence indeed.
  EXPRESSION: Amused
- CHARACTER: Narrator
  LINE: Knock blows the pounce off the documents.
  EXPRESSION: null
- CHARACTER: Knock
  LINE: I have been entertaining dealings with a foreign count. Very old line of nobility. Very old. Very... eccentric.
  EXPRESSION: Amused
- CHARACTER: Knock
  LINE: He, um, wishes to acquire a home in our Wisburg.
  EXPRESSION: Business-like
- CHARACTER: Thomas
  LINE: Oh yes?
  EXPRESSION: Curious
- CHARACTER: Knock
  LINE: To retire here. He has one foot in the grave, as they say.
  EXPRESSION: Amused
- CHARACTER: Thomas
  LINE: I should be pleased to escort the gentleman, and recommend him to our properties.
  EXPRESSION: Eager
- CHARACTER: Knock
  LINE: I have already selected: Grünewald Manor.
  EXPRESSION: Decisive
- CHARACTER: Narrator
  LINE: Thomas is taken aback.
  EXPRESSION: Surprised
- CHARACTER: Thomas
  LINE: Forgive me, but is it not, well, a ruin?
  EXPRESSION: Concerned
- CHARACTER: Knock
  LINE: He seeks an old home and will pay generously.
  EXPRESSION: Practical
- CHARACTER: Thomas
  LINE: I shall meet him tomorrow, then. Nine of the clock?
  EXPRESSION: Proactive
- CHARACTER: Knock
  LINE: That is the peculiarity... you see, he is yet to arrive. You needs must journey... to him. He lives in a small country, well east of Bohemia.
  EXPRESSION: Mysterious
- CHARACTER: Narrator
  LINE: Knock pulls out a large map. Thomas walks warily to his desk.
  EXPRESSION: Cautious
- CHARACTER: Thomas
  LINE: I see.
  EXPRESSION: Acknowledging
- CHARACTER: Knock
  LINE: Isolated within the Carpathian Alps. The land beyond the forest.
  EXPRESSION: Descriptive
- CHARACTER: Narrator
  LINE: Thomas examines the map to “TRANSILVANIA.” Just then, he notices many strange documents on Knock’s desk, all written in a mysterious, foreign alphabet and dripping in red wax seals. The seals have the same obscure sigil upon them. Knock notices Thomas' wandering eye and slides the documents away under a mass of paperwork. He hands the map to Thomas.
  EXPRESSION: Suspicious
- CHARACTER: Knock
  LINE: It will be a great adventure for you.
  EXPRESSION: Encouraging
- CHARACTER: Thomas
  LINE: Indeed. May not the count execute the deed here, when he arrives?
  EXPRESSION: Questioning
- CHARACTER: Knock
  LINE: He insists I offer him an agent – in the flesh. And he will pay handsomely, my dear boy. Handsomely! Secure this account and you shall have your official position in our firm!
  EXPRESSION: Motivating
- CHARACTER: Narrator
  LINE: Thomas looks at the map. Excited, and a bit concerned.
  EXPRESSION: Mixed emotions
- CHARACTER: Thomas
  LINE: Thank you sir. Thank you. I shan’t disappoint. And what was the count’s name?
  EXPRESSION: Determined
- CHARACTER: Knock
  LINE: Orlok.
  EXPRESSION: Sinister
- CHARACTER: Narrator
  LINE: Knock’s laughter becomes even more unsound. Rain begins to patter on the window.
  EXPRESSION: Ominous

::SCENE::
LOCATION: Wisburg. Old Town. Side Street
MOOD: Urgent and melancholic
CHARACTERS: Narrator, Thomas
BACKGROUND_IMAGE: wisburg_street.png
BACKGROUND_EDIT: "Dusk, pouring rain, narrow street with umbrellas."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Thomas runs through pouring rain, the narrow street constricted by pedestrians’ umbrellas. He guards a bouquet of lilacs with his top hat.
  EXPRESSION: Determined

::SCENE::
LOCATION: Hutter House. Parlour
MOOD: Somber and anxious
CHARACTERS: Narrator, Thomas, Ellen
BACKGROUND_IMAGE: hutter_parlour.png
BACKGROUND_EDIT: "Dimly lit parlour, wet Thomas kneeling."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Ellen looks despondently at the lilacs. A dripping wet Thomas is on his knee in the dim parlour light.
  EXPRESSION: Sad
- CHARACTER: Thomas
  LINE: ... and I shall set off tomorrow, as it is a six-week journey. Harding has generously agreed to keep you ‘til my return.
  EXPRESSION: Reassuring
- CHARACTER: Narrator
  LINE: Ellen is silent, still looking at the flowers.
  EXPRESSION: Silent
- CHARACTER: Thomas
  LINE: What?
  EXPRESSION: Questioning
- CHARACTER: Ellen
  LINE: --
  EXPRESSION: Subdued
- CHARACTER: Thomas
  LINE: I know, my love, yet I shall be home in but three fortnights. Time is swift.
  EXPRESSION: Hopeful
- CHARACTER: Narrator
  LINE: Ellen seems deeply sad.
  EXPRESSION: Deeply sad
- CHARACTER: Ellen
  LINE: Why have you killed these beautiful flowers?
  EXPRESSION: Accusatory
- CHARACTER: Thomas
  LINE: What?
  EXPRESSION: Confused
- CHARACTER: Ellen
  LINE: Nothing.
  EXPRESSION: Defeated
- CHARACTER: Thomas
  LINE: What are you talking about?
  EXPRESSION: Bewildered
- CHARACTER: Ellen
  LINE: Forgive me.
  EXPRESSION: Apologetic
- CHARACTER: Thomas
  LINE: Let us put them in water.
  EXPRESSION: Practical
- CHARACTER: Ellen
  LINE: They will only die in a few days. Throw them out.
  EXPRESSION: Desperate
- CHARACTER: Thomas
  LINE: What?
  EXPRESSION: Shocked
- CHARACTER: Ellen
  LINE: Throw them out!
  EXPRESSION: Insistent
- CHARACTER: Narrator
  LINE: Her reaction is extreme.
  EXPRESSION: Extreme
- CHARACTER: Thomas
  LINE: What is this?
  EXPRESSION: Alarmed
- CHARACTER: Ellen
  LINE: You cannot leave.
  EXPRESSION: Pleading
- CHARACTER: Thomas
  LINE: What are you –
  EXPRESSION: Stunned
- CHARACTER: Ellen
  LINE: I must tell you my dream.
  EXPRESSION: Urgent
- CHARACTER: Thomas
  LINE: Ellen, we have put all of these difficulties behind us.
  EXPRESSION: Dismissive
- CHARACTER: Ellen
  LINE: I must!
  EXPRESSION: Insistent
- CHARACTER: Thomas
  LINE: Please, no more of your childhood memories ... the doctors advised –
  EXPRESSION: Irritated
- CHARACTER: Ellen
  LINE: No... It was our wedding....
  EXPRESSION: Resigned
- CHARACTER: Narrator
  LINE: Thomas gives in.
  EXPRESSION: Resigned
- CHARACTER: Ellen
  LINE: Yet not in chapel walls. Above was an impenetrable thundercloud outstretched beyond the hills. The scent of the lilacs was strong in the rain... and when I reached the altar, you weren’t there. Standing before me, all in black... was... Death.
  EXPRESSION: Vividly recounting
- CHARACTER: Narrator
  LINE: Thomas shudders, though he doesn’t realise it. Ellen continues, the dream playing vividly in her eyes.
  EXPRESSION: Unaware
- CHARACTER: Ellen
  LINE: But I was so happy, so very happy. We exchanged vows, we embraced, and when we turned round, everyone was dead. Father... and... everyone. The stench of their bodies was horrible.
  EXPRESSION: Distraught
- CHARACTER: Ellen
  LINE: And – But I had never been so happy as that moment... as I held hands with Death.
  EXPRESSION: Ecstatic yet horrified
- CHARACTER: Narrator
  LINE: She cries in Thomas’s arms, both of them horrified from what she just said.
  EXPRESSION: Horrified
- CHARACTER: Thomas
  LINE: Never speak these things aloud. Never. It is a trifle. A foolish dream, just as your past fancies.
  EXPRESSION: Comforting
- CHARACTER: Narrator
  LINE: Thomas tries to soothe her.
  EXPRESSION: Soothing
- CHARACTER: Thomas
  LINE: Everything is well.
  EXPRESSION: Reassuring
- CHARACTER: Ellen
  LINE: It portends something awful for us.
  EXPRESSION: Foreboding
- CHARACTER: Thomas
  LINE: Ellen, we are already wed! What could be amiss? Look, when I return I will finally make something of myself –- I shall buy us a fine house of our own, with a maidservant --
  EXPRESSION: Optimistic
- CHARACTER: Ellen
  LINE: We needn’t any of that!
  EXPRESSION: Desperate
- CHARACTER: Thomas
  LINE: I wish you to have all you deserve of --
  EXPRESSION: Loving
- CHARACTER: Narrator
  LINE: She becomes desperate, wanting to protect her husband!
  EXPRESSION: Protective
- CHARACTER: Ellen
  LINE: You mustn’t leave, I love you too much!
  EXPRESSION: Desperate

::SCENE::
LOCATION: Coach
MOOD: Tense and silent
CHARACTERS: Narrator, Ellen, Thomas
BACKGROUND_IMAGE: coach_interior.png
BACKGROUND_EDIT: "Nighttime, interior of a coach."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Ellen and Thomas don’t look at each other. Their argument racing in their heads. Silence. Tension. Ellen pets Greta.
  EXPRESSION: Tense

::SCENE::
LOCATION: Harding House. Rear Drawing Room
MOOD: Jovial and convivial
CHARACTERS: Narrator, Friedrich Harding, Thomas
BACKGROUND_IMAGE: harding_drawing_room.png
BACKGROUND_EDIT: "Nighttime, a richly appointed drawing room with a roaring fire."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Friedrich Harding (late 20s) explodes with laughter!
  EXPRESSION: Boisterous
- CHARACTER: Harding
  LINE: Pray stop, stop! Never since our school days, Tom!
  EXPRESSION: Amused
- CHARACTER: Narrator
  LINE: Thomas laughs too, both near the mantel over a roaring fire. Harding pours yet another glass of brandy as he and Thomas smoke their cigars. The old friends lean on one another, a bit drunk and sweaty, in their evening attire. Harding is as stalwart and confident as Hutter is eager and anxious.
  EXPRESSION: Friendly
- CHARACTER: Harding
  LINE: From my grandfather. The best.
  EXPRESSION: Proud
- CHARACTER: Thomas
  LINE: Oh, I oughtn’t –
  EXPRESSION: Hesitant
- CHARACTER: Harding
  LINE: It’s worth celebrating your adventure! I envy you.
  EXPRESSION: Envious
- CHARACTER: Thomas
  LINE: I envy you. You’ve truly taken your father’s place now... it’s incredible.
  EXPRESSION: Admiring
- CHARACTER: Harding
  LINE: The bloody responsibility. It’s crushing, Thomas, crushing. Of course, It’s unseemly to complain with the earnings, but the demands of the market grow faster than the damnèd shipyard. And my two girls... two Tom... I... I love them more than the world... Yet I...
  EXPRESSION: Overwhelmed
- CHARACTER: Narrator
  LINE: They look through the doorway at Anna (20s), his lovely wife, who shares her husband’s affirming resilience. Her thoughtful eyes are full of warmth and zeal. She sits on a divan talking with
  EXPRESSION: Warm





::SCENE::
LOCATION: Outside the Transylvanian Inn
MOOD: Hostility, Fear
CHARACTERS: Thomas, Roma People, Innkeeper
BACKGROUND_IMAGE: inn_exterior_night.png
BACKGROUND_EDIT: "Night, Thomas is being mocked by Roma people, Innkeeper emerges to intervene."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Thomas doesn’t know what to do, or why he caused this. All the Roma, young and old, begin laughing at him.
  EXPRESSION: Confused, Scared
- CHARACTER: Narrator
  LINE: Just then, THE INNKEEPER comes to Thomas’ rescue and shoos the Roma away, shouting under his gigantic white moustache. The mocking laughter continues.
  EXPRESSION: Protective
- CHARACTER: Innkeeper
  LINE: (Romanian, subtitled) You bring trouble with you.
  EXPRESSION: Angry
- CHARACTER: Thomas
  LINE: Forgive me, I ... I only wish to stay one night. I have an audience at the castle. Castle Orlok, beyond the Árnyék Pass. I wish to hire a coach, or yet a guide to–
  EXPRESSION: Pleading
- CHARACTER: Narrator
  LINE: THE INNKEEPER grows more stern. Is he afraid?
  EXPRESSION: Fearful
- CHARACTER: Innkeeper
  LINE: Go.
  EXPRESSION: Stern
- CHARACTER: Handsome Roma Man
  LINE: (Romany, subtitled) Return to your country, Gadjo!
  EXPRESSION: Hostile
- CHARACTER: Narrator
  LINE: All the Roma shout and laugh. THE INNKEEPER shouts “Quiet” and curses them in Romanian.
  EXPRESSION: Loud, Angry
- CHARACTER: Thomas
  LINE: I am weary, I pray you.
  EXPRESSION: Exhausted, Pleading
- CHARACTER: Innkeeper
  LINE: (Romanian, subtitled) Leave here.
  EXPRESSION: Demanding
- CHARACTER: Narrator
  LINE: Thomas holds up his purse.
  EXPRESSION: Hopeful
- CHARACTER: Thomas
  LINE: I will pay double the board!
  EXPRESSION: Desperate

::PATHS::
- CHOICE: "Accept payment and let Thomas in"
  TARGET: inn_interior_tavern
  STATE_CHANGE: fear = +1
  CONDITION: null

::SCENE::
LOCATION: Transylvanian Inn - Tavern
MOOD: Smoky, Uneasy
CHARACTERS: Thomas, Innkeeper's Wife, Patrons
BACKGROUND_IMAGE: inn_tavern_night.png
BACKGROUND_EDIT: "Dark, smoky tavern, chickens, patrons in traditional garb, old women anointing windows with garlic."

::SCRIPT::
- CHARACTER: Narrator
  LINE: THE INNKEEPER’S WIFE, a tiny woman with a witch-like face, leads THOMAS through a dark tavern, thick with pipe smoke. Chickens mill about.
  EXPRESSION: Fearful
- CHARACTER: Narrator
  LINE: She leads him past the few patrons in their exotic garb of sheepskins, embroidery, and coin jewellery. They eye Thomas, suspiciously.
  EXPRESSION: Suspicious
- CHARACTER: Narrator
  LINE: She leads him past old women anointing the windows with garlic, praying...
  EXPRESSION: Superstitious
- CHARACTER: Narrator
  LINE: She leads him further into a dark corridor... Further into darkness... Her candlestick flickering as she mutters fearfully in Romanian...
  EXPRESSION: Fearful
- CHARACTER: Narrator
  LINE: Thomas grows uneasy...
  EXPRESSION: Uneasy

::PATHS::
- CHOICE: "Follow Innkeeper's Wife"
  TARGET: inn_room
  STATE_CHANGE: fear = +2
  CONDITION: null

::SCENE::
LOCATION: Inn Room
MOOD: Primitive, Foreboding
CHARACTERS: Thomas, Innkeeper's Wife
BACKGROUND_IMAGE: inn_room_primitive.png
BACKGROUND_EDIT: "Cramped room, unusually tall bed, flickering candlelight."

::SCRIPT::
- CHARACTER: Narrator
  LINE: THE INNKEEPER’S WIFE has led THOMAS into a primitive, cramped room with an unusually tall bed.
  EXPRESSION: Primitive
- CHARACTER: Narrator
  LINE: Speaking Romanian, she implores THOMAS not to go to Orlok’s castle, so it seems.
  EXPRESSION: Warning
- CHARACTER: Narrator
  LINE: She places a humble wooden CROSS pendant in his hand.
  EXPRESSION: Solemn
- CHARACTER: Innkeeper's Wife
  LINE: (Romanian, subtitled) Beware his shadow.
  EXPRESSION: Fearful
- CHARACTER: Narrator
  LINE: She passes her hand over his eyes. Slowly.
  EXPRESSION: Mystical
- CHARACTER: Innkeeper's Wife
  LINE: (Romanian, subtitled) The shadow covers you in nightmare. Awake, but a dream. There is no escape. Pray. Pray.
  EXPRESSION: Terrified
- CHARACTER: Narrator
  LINE: As she leaves, she crosses herself, and spits on the floor. She continues praying and mumbling, almost crying in her concern.
  EXPRESSION: Deeply Concerned
- CHARACTER: Narrator
  LINE: She’s made an impression. THOMAS grasps THE CROSS tightly ... No, it’s superstitious nonsense. He puts it on the candle stand.
  EXPRESSION: Skeptical

::PATHS::
- CHOICE: "Ignore the warning and go to sleep"
  TARGET: inn_room_night
  STATE_CHANGE: fear = +3, superstition = -2
  CONDITION: null

::SCENE::
LOCATION: Inn Room
MOOD: Interrupted Sleep, Confusion
CHARACTERS: Thomas
BACKGROUND_IMAGE: inn_room_night.png
BACKGROUND_EDIT: "Thomas is asleep in bed, sounds of animals and singing."

::SCRIPT::
- CHARACTER: Narrator
  LINE: THOMAS is awakened by a loud noise. Animals. Singing.
  EXPRESSION: Startled
- CHARACTER: Narrator
  LINE: He looks out the window: a procession of FLAMING TORCHES.
  EXPRESSION: Curious

::PATHS::
- CHOICE: "Investigate the torches"
  TARGET: outside_inn_night
  STATE_CHANGE: curiosity = +2
  CONDITION: null

::SCENE::
LOCATION: Outside the Inn
MOOD: Mysterious, Ritualistic
CHARACTERS: Thomas, Roma People
BACKGROUND_IMAGE: outside_inn_night.png
BACKGROUND_EDIT: "Night, Thomas watches a procession of Roma with torches entering a birch grove."

::SCRIPT::
- CHARACTER: Narrator
  LINE: THOMAS watches as a group of ROMA with torches walk into a grove of birch trees...
  EXPRESSION: Observant
- CHARACTER: Narrator
  LINE: He follows, staying in the shadows.
  EXPRESSION: Stealthy

::PATHS::
- CHOICE: "Follow the Roma into the grove"
  TARGET: birch_grove_night
  STATE_CHANGE: curiosity = +3, fear = +1
  CONDITION: null

::SCENE::
LOCATION: Birch Grove
MOOD: Pagan, Disturbing
CHARACTERS: Thomas, Roma People, Nude Teenage Girl, Old Roma Woman, Handsome Roma Man, Black Dog
BACKGROUND_IMAGE: birch_grove_night.png
BACKGROUND_EDIT: "Night, a nude teenage girl on a white horse, Roma people with torches, a black dog with two painted eyes."

::SCRIPT::
- CHARACTER: Narrator
  LINE: THOMAS watches as THE ROMA follow a NUDE TEENAGE GIRL RIDING ON A WHITE HORSE.
  EXPRESSION: Awe, Shock
- CHARACTER: Narrator
  LINE: THOMAS breathes heavily at the sight of her smooth, dark flesh, bouncing on horseback. He averts his eyes, embarrassed.
  EXPRESSION: Aroused, Embarrassed
- CHARACTER: Old Roma Woman
  LINE: (Romany, subtitled) Bless this virgin child. Bless her. Guide our stallion to the unclean spirit.
  EXPRESSION: Reverent
- CHARACTER: Narrator
  LINE: THE HANDSOME ROMA MAN has a BLACK DOG on a leash. THE DOG has a SECOND SET OF EYES painted on its head in white. It barks ferociously, foaming at the mouth.
  EXPRESSION: Menacing
- CHARACTER: Narrator
  LINE: THE NUDE GIRL has led them to a GRAVE in the middle of the grove.
  EXPRESSION: Foreboding

::PATHS::
- CHOICE: "Continue watching the ritual"
  TARGET: birch_grove_later
  STATE_CHANGE: fear = +2
  CONDITION: null

::SCENE::
LOCATION: Birch Grove
MOOD: Necromantic, Horrific
CHARACTERS: Thomas, Roma People, Old Roma Woman
BACKGROUND_IMAGE: birch_grove_exhumation.png
BACKGROUND_EDIT: "Night, Roma people exhume a bloated, rotting corpse while chanting."

::SCRIPT::
- CHARACTER: Narrator
  LINE: THOMAS crouches behind a tree, watching the Roma EXHUME A BLOATED ROTTING RED-FACED CORPSE! The women chanting, praying, crying.
  EXPRESSION: Horrified
- CHARACTER: Old Roma Woman
  LINE: (Romany, subtitled) Find his tail! His cloven hooves!
  EXPRESSION: Intense, Possessed

::PATHS::
- CHOICE: "Witness the stake driving"
  TARGET: birch_grove_continuous
  STATE_CHANGE: fear = +4
  CONDITION: null

::SCENE::
LOCATION: Birch Grove
MOOD: Violent, Shocking
CHARACTERS: Thomas, Handsome Roma Man, Corpse
BACKGROUND_IMAGE: birch_grove_stake.png
BACKGROUND_EDIT: "Night, Handsome Roma Man stakes a corpse, which screams."

::SCRIPT::
- CHARACTER: Narrator
  LINE: THE HANDSOME ROMA MAN POUNDS AN IRON STAKE INTO THE CORPSE’S NAVEL! THE CORPSE SCREAMS IN PAIN! (Is it alive?)
  EXPRESSION: Brutal, Shocking
- CHARACTER: Thomas
  LINE: No, by the grace of God!
  EXPRESSION: Outraged, Terrified
- CHARACTER: Narrator
  LINE: THE ROMA MAN turns... He locks eyes with THOMAS... Suddenly...
  EXPRESSION: Confrontational

::PATHS::
- CHOICE: "React to the scene"
  TARGET: inn_room_morning
  STATE_CHANGE: fear = +5, shock = +3
  CONDITION: null

::SCENE::
LOCATION: Inn Room
MOOD: Nightmarish Awakening, Disbelief
CHARACTERS: Thomas
BACKGROUND_IMAGE: inn_room_morning_sweat.png
BACKGROUND_EDIT: "Thomas wakes up sweating, the cross pendant is around his neck, his boots are muddy."

::SCRIPT::
- CHARACTER: Narrator
  LINE: THOMAS wakes in a sweat. A rooster crows.
  EXPRESSION: Panicked
- CHARACTER: Narrator
  LINE: THE CROSS from Innkeeper’s wife is around his neck. He takes it off and throws it to the floor, in terror - he didn’t put it on.
  EXPRESSION: Terrified, Disgusted
- CHARACTER: Narrator
  LINE: Then he sees... he is wearing his boots, CAKED IN FRESH MUD.
  EXPRESSION: Confused, Alarmed

::PATHS::
- CHOICE: "Leave the inn"
  TARGET: inn_morning
  STATE_CHANGE: fear = +4, confusion = +2
  CONDITION: null

::SCENE::
LOCATION: Inn - Morning
MOOD: Deserted, Eerie
CHARACTERS: Thomas
BACKGROUND_IMAGE: inn_morning_deserted.png
BACKGROUND_EDIT: "Morning, the inn is empty, the gypsy camp is gone, Thomas' horse is missing."

::SCRIPT::
- CHARACTER: Narrator
  LINE: THOMAS walks outside. No one is there. Straw mattresses air out on the porch rail. The gypsy camp has gone. Extinguished fires smoulder. His horse is gone too.
  EXPRESSION: Astonished, Alarmed
- CHARACTER: Thomas
  LINE: Hello?
  EXPRESSION: Calling out
- CHARACTER: Narrator
  LINE: Pause. Nothing.
  EXPRESSION: Silent
- CHARACTER: Thomas
  LINE: My horse!?
  EXPRESSION: Panicked
- CHARACTER: Narrator
  LINE: His voice echoes.
  EXPRESSION: Empty

::PATHS::
- CHOICE: "Begin the journey to Castle Orlok"
  TARGET: mountains_day
  STATE_CHANGE: determination = +1, fear = +3
  CONDITION: null

::SCENE::
LOCATION: Mountains
MOOD: Oppressive, Gloomy
CHARACTERS: Thomas
BACKGROUND_IMAGE: mountains_oppressive.png
BACKGROUND_EDIT: "Brooding Carpathian landscape, misty, Thomas hiking with a stick, heavy atmosphere."

::SCRIPT::
- CHARACTER: Narrator
  LINE: A brooding Carpathian landscape of oppressive gloom.
  EXPRESSION: Gloomy
- CHARACTER: Narrator
  LINE: THOMAS hikes with a stick up a steep, misty mountain side. His saddle bag is slung over his shoulder. The dark and heavy atmosphere seems to drag THOMAS’ limbs down.
  EXPRESSION: Exhausted

::PATHS::
- CHOICE: "Continue on to Árnyék Pass"
  TARGET: arnyek_pass_dusk
  STATE_CHANGE: exhaustion = +2, fear = +2
  CONDITION: null

::SCENE::
LOCATION: Árnyék/Umbra Pass
MOOD: Perilous, Eerie
CHARACTERS: Thomas
BACKGROUND_IMAGE: arnyek_pass_dusk.png
BACKGROUND_EDIT: "Dusk, Thomas stumbles up a rugged peak to a wooden shrine at the edge of a bridge over a ravine. The shrine is adorned with crosses, garlic, and thorns."

::SCRIPT::
- CHARACTER: Narrator
  LINE: THE SUN sets as THOMAS stumbles up a rugged peak. In front of him are the remains of a WOODEN SHRINE at the edge of a bridge that crosses a perilous ravine. There is a freakish mess of weathered crosses, icons, garlic flowers, and thorned wreaths nailed all over THE SHRINE.
  EXPRESSION: Fearful
- CHARACTER: Narrator
  LINE: THOMAS is afraid to pass. But it calls to him. The wind howls. He closes his eyes and steps forward. His heart pounds. He crosses the bridge.
  EXPRESSION: Terrified, Determined

::PATHS::
- CHOICE: "Cross the bridge"
  TARGET: forest_crossroads_night
  STATE_CHANGE: fear = +4, courage = +1
  CONDITION: null

::SCENE::
LOCATION: Forest Crossroads
MOOD: Supernatural, Terrifying
CHARACTERS: Thomas, Ghostly Carriage, Black Horses
BACKGROUND_IMAGE: forest_crossroads_night.png
BACKGROUND_EDIT: "Night, snow is falling, wolves howl, a ghostly carriage drawn by four black horses approaches."

::SCRIPT::
- CHARACTER: Narrator
  LINE: THOMAS comes to a crossroads within a primeval forest. Snow is falling. Wolves howl in the distance.
  EXPRESSION: Ominous
- CHARACTER: Narrator
  LINE: Then, he hears something more grave. A horrible pounding of hellish hooves. An ethereal jingling. Through the tall pines, he sees something black, silhouetted by the moon. It is a CARRIAGE drawn by four black horses. Their long manes, plumes, bells and tassels float in the air weightlessly.
  EXPRESSION: Terrified
- CHARACTER: Narrator
  LINE: THOMAS recoils in terror as the ghostly CARRIAGE heads straight toward him. Closer... closer... it will trample him to death... He holds up his arms to guard himself from the imminent collision... the horses scream...
  EXPRESSION: Utter Terror
- CHARACTER: Narrator
  LINE: SUDDENLY: THE CARRIAGE has halted before him. Utterly still.
  EXPRESSION: Astonished
- CHARACTER: Narrator
  LINE: THOMAS looks on in wonder. He can’t see a driver. If there is one, he is still and silent as the ferryman of the river Styx. JUST THEN, THE ORNATE CARRIAGE DOORS OPEN, beckoning him. THOMAS enters as if lifted into it by an unseen force.
  EXPRESSION: Bewildered, Compelled

::PATHS::
- CHOICE: "Enter the carriage"
  TARGET: mountain_road_night
  STATE_CHANGE: fate = +1, fear = +5
  CONDITION: null

::SCENE::
LOCATION: Mountain Road
MOOD: Hecti, Supernatural Pursuit
CHARACTERS: Thomas, Carriage, Black Wolves, Castle Orlok
BACKGROUND_IMAGE: mountain_road_night.png
BACKGROUND_EDIT: "Night, the carriage speeds through falling snow, pursued by black wolves. Castle Orlok looms on a jagged mountain peak."

::SCRIPT::
- CHARACTER: Narrator
  LINE: The crack of a whip! THE CARRIAGE moves like a banshee through the falling snow.
  EXPRESSION: Fast, Supernatural
- CHARACTER: Narrator
  LINE: Huge, muscular BLACK WOLVES chase the carriage, growling and howling in excitement.
  EXPRESSION: Savage, Eager
- CHARACTER: Narrator
  LINE: THE CASTLE stands on the crest of a jagged mountain.
  EXPRESSION: Imposing

::PATHS::
- CHOICE: "Continue towards the castle"
  TARGET: castle_orlok_bridge
  STATE_CHANGE: anticipation = +2
  CONDITION: null

::SCENE::
LOCATION: Castle Orlok - Bridge
MOOD: Approaching Doom
CHARACTERS: Thomas, Carriage
BACKGROUND_IMAGE: castle_orlok_bridge.png
BACKGROUND_EDIT: "Night, the carriage rumbles across a crumbling drawbridge towards Castle Orlok."

::SCRIPT::
- CHARACTER: Narrator
  LINE: THE CARRIAGE rumbles across the crumbling drawbridge.
  EXPRESSION: Ominous

::PATHS::
- CHOICE: "Enter the castle"
  TARGET: ghost_carriage_interior
  STATE_CHANGE: doom = +1
  CONDITION: null

::SCENE::
LOCATION: INT/EXT. Ghost Carriage
MOOD: Claustrophobic, Delirious
CHARACTERS: Thomas
BACKGROUND_IMAGE: ghost_carriage_interior.png
BACKGROUND_EDIT: "Interior of a moldering, coffin-like carriage, Thomas is delirious."

::SCRIPT::
- CHARACTER: Narrator
  LINE: THOMAS suffocates inside the coach, as if it were a mouldering coffin. He closes his eyes in delirium.
  EXPRESSION: Suffocating, Delirious

::PATHS::
- CHOICE: "Succumb to delirium"
  TARGET: end
  STATE_CHANGE: madness = +1
  CONDITION: null

::SCENE::
LOCATION: Castle Orlok. Barbican Gate
MOOD: Eerie
CHARACTERS: Narrator, Thomas
BACKGROUND_IMAGE: castle_orlok_barbican_gate.png
BACKGROUND_EDIT: "Nighttime, imposing castle gate"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Thomas opens his eyes: He has exited the carriage. How? He cannot remember. It has vanished into the night with the wolves. He stands before two great wooden DOORS covered in grotesque ironwork.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Before Thomas can knock, the DOORS open, creaking and moaning. He walks into the dark ruins.
  EXPRESSION: null

::PATHS::
- CHOICE: "Enter the castle"
  TARGET: castle_courtyard
  STATE_CHANGE: fear = +2
  CONDITION: null

::SCENE::
LOCATION: Castle Orlok. Courtyard
MOOD: Foreboding
CHARACTERS: Narrator, Thomas, Count Orlok
BACKGROUND_IMAGE: castle_orlok_courtyard.png
BACKGROUND_EDIT: "Nighttime, dense fog, moonlight"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Thomas looks ahead... in the distance, within the dense fog, is A MAN standing in the moonlight. He is too far away for Thomas to make him out, but his presence is magnetic. He is deathly pale. His fierce eyes pierce through the darkness.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The figure walks slowly, as if hindered by rigour mortis. He is too tall, supernaturally thin, and dressed entirely in black. His clothing is rich, elegant, Eastern – the finery of a Hungarian nobleman. It is COUNT ORLOK. He stands many paces away from Thomas - utterly still, like a statue.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Thomas bows. Orlok looks at him. His eyes tear into Thomas.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Pause.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Orlok turns away slowly. He walks back into an abyss of darkness... into the castle. Thomas, stunned, exhausted, follows...
  EXPRESSION: null

::PATHS::
- CHOICE: "Follow Count Orlok"
  TARGET: castle_staircase
  STATE_CHANGE: exhaustion = +1
  CONDITION: null

::SCENE::
LOCATION: Castle Orlok. Staircase
MOOD: Ominous
CHARACTERS: Narrator, Thomas, Count Orlok
BACKGROUND_IMAGE: castle_orlok_staircase.png
BACKGROUND_EDIT: "Nighttime, steep winding staircase"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Thomas treads well behind Orlok, up the steep winding stairs.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Orlok speaks with an impossibly deep sepulchral voice, shrouded in the exotic accent of his mother tongue. In spite of its power, it seems every word he utters causes him great pain and effort to expel.
  EXPRESSION: null
- CHARACTER: Orlok
  LINE: You are late. The midnight hour is passed and my attendants have all retired.
  EXPRESSION: Angry
- CHARACTER: Thomas
  LINE: Forgive me, Count.
  EXPRESSION: Apologetic
- CHARACTER: Narrator
  LINE: The Count disappears. Thomas is startled, where did he go? He keeps walking... past a stone column he finds an open door...
  EXPRESSION: Surprised

::PATHS::
- CHOICE: "Enter the Great Hall"
  TARGET: great_hall
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Great Hall. Castle Orlok
MOOD: Bleak
CHARACTERS: Narrator, Thomas, Count Orlok
BACKGROUND_IMAGE: castle_orlok_great_hall.png
BACKGROUND_EDIT: "Nighttime, vast Gothic hall, flickering candles, cracked windows"

::SCRIPT::
- CHARACTER: Narrator
  LINE: A few candles flicker in the vast Gothic hall. Wind screeches through the cracked lead glass windows. It is frigid, mildewed, and bleak. A nightmare castle.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Thomas sees Orlok standing some distance away, motionless, almost entirely hidden in shadow. Thomas can only hear his breath. It is loud and asthmatic – pained, like his speech.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: In between them is a huge medieval TABLE, decked with a feast. For Thomas alone.
  EXPRESSION: null
- CHARACTER: Orlok
  LINE: Leave there your conveniences. Set out the deed. And sit.
  EXPRESSION: Imperious
- CHARACTER: Thomas
  LINE: Would you not wish to wait ‘til morning?
  EXPRESSION: Hesitant
- CHARACTER: Orlok
  LINE: I wish you to do as I request.
  EXPRESSION: Harsh
- CHARACTER: Thomas
  LINE: Yes, of course, sir.
  EXPRESSION: Submissive
- CHARACTER: Narrator
  LINE: Thomas goes to put his satchel down on the table.
  EXPRESSION: null
- CHARACTER: Orlok
  LINE: Lord.
  EXPRESSION: Demanding
- CHARACTER: Thomas
  LINE: Pardon me, sir?
  EXPRESSION: Confused
- CHARACTER: Orlok
  LINE: Your Lord. I will be addressed as the honour of my blood demands it.
  EXPRESSION: Arrogant
- CHARACTER: Thomas
  LINE: Yes, my lord. Forgive me, my lord.
  EXPRESSION: Embarrassed
- CHARACTER: Narrator
  LINE: Thomas is very embarrassed, he’s fouling up already, he’s so tired, disoriented. He puts his things down fearfully.
  EXPRESSION: null
- CHARACTER: Orlok
  LINE: Pray, sit.
  EXPRESSION: Command
- CHARACTER: Thomas
  LINE: Thank you, my lord.
  EXPRESSION: Nervous
- CHARACTER: Narrator
  LINE: With Thomas very far from him, Orlok takes the papers. Thomas watches the Count move in a strange and animal-like manner. His back is hunched, but in spite of his extremely lean profile, his chest is strong, masculine, even bull-like. His rich clothing is worm-eaten and filthy. Orlok continues to keep his face hidden from Thomas.
  EXPRESSION: null
- CHARACTER: Orlok
  LINE: I am most impatient to bring my eyes to your covenant papers and my correspondence with your proprietor, Herr Knock. I have long awaited them, and I hold matters I must attend to upon the morrow.
  EXPRESSION: Impatient
- CHARACTER: Thomas
  LINE: Yes, of course, my lord.
  EXPRESSION: Submissive
- CHARACTER: Narrator
  LINE: As Thomas reaches for some food, he realises the Count is right behind him! How did he get there?
  EXPRESSION: Surprised
- CHARACTER: Narrator
  LINE: The Count’s breath is fetid. Thomas recoils. He doesn’t see Orlok’s arthritic, mummy-like hand reaching for an ancient decanter. Orlok’s long fingernails crawl up the handle like a spider. He pours the wine into Thomas’ chalice.
  EXPRESSION: Disgusted
- CHARACTER: Orlok
  LINE: Drink.
  EXPRESSION: Command
- CHARACTER: Narrator
  LINE: By the time Thomas has turned to his cup, Orlok has disappeared again into the dark. Thomas hears him walking to the other side of the table, he can’t see him. Suddenly... Orlok is seated in an intimidating, throne of a chair.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: As Orlok pores over the documents, Thomas tries to make out his face in the dim light. His features are anorexic, severe, and bestial, and he wears the traditional moustache of the region. Yet, however cadaverous and feral – he is somehow quite handsome. Anything more than that, Thomas cannot see. Thomas tries to think of something to talk about. His host is most unsettling in his silence.
  EXPRESSION: null
- CHARACTER: Thomas
  LINE: I have... my lord, I have questions about the, um, unfamiliar customs of the peasantry and, um, errant wanderers...
  EXPRESSION: Nervous
- CHARACTER: Orlok
  LINE: (reading)
  EXPRESSION: Silent
- CHARACTER: Thomas
  LINE: Last night, I saw, or rather I believe I saw a band of gypsies... they ventured to a small birch grove, and –
  EXPRESSION: Hesitant
- CHARACTER: Orlok
  LINE: Yesternight was but the eve of their Szent András. Our common people say it is the darkest witching night when Devil’s magic bids the wolf to speak with tongues of men, and every nightmare freely treads upon this earth, ascendent from the torturous grave.
  EXPRESSION: Menacing
- CHARACTER: Narrator
  LINE: This does not comfort Thomas. Orlok lets out a Mephistophelian laugh.
  EXPRESSION: Fearful
- CHARACTER: Orlok
  LINE: I fear we yet keep close many superstitions here that may seem backward to a young man of your high learning.
  EXPRESSION: Condescending
- CHARACTER: Thomas
  LINE: These gypsies, they exhumed a corpse.
  EXPRESSION: Apprehensive
- CHARACTER: Orlok
  LINE: It is their filthy ritual.
  EXPRESSION: Disgusted
- CHARACTER: Thomas
  LINE: What manner of ritual –
  EXPRESSION: Curious
- CHARACTER: Orlok
  LINE: Speak not of it again!
  EXPRESSION: Enraged
- CHARACTER: Narrator
  LINE: His voice echoes through the high vaulted ceiling. Birds (or are they bats?) flutter in the silence. Orlok calms, he continues.
  EXPRESSION: null
- CHARACTER: Orlok
  LINE: How I look forward to retiring to your city of a modern mind, who knows nothing of... nor believes any such morbid... fairy tales.
  EXPRESSION: Sarcastic
- CHARACTER: Narrator
  LINE: The Count sits still in his chair, his eyes locked on Thomas. Hungry. Thomas sits still as well. Petrified.
  EXPRESSION: null
- CHARACTER: Orlok
  LINE: Eat.
  EXPRESSION: Command
- CHARACTER: Narrator
  LINE: Doing as he is told, he awkwardly begins to slice some bread. When can he leave the table and sleep!? Orlok keeps staring, still as death.
  EXPRESSION: null
- CHARACTER: Orlok
  LINE: You are married, Herr Hutter – ?
  EXPRESSION: Curious
- CHARACTER: Narrator
  LINE: Just as Thomas feels a chill from that question – the loud chime of a clock strikes “four” – he flinches from the sound! He cuts himself! Orlok’s eyes shift to Thomas’ hand: BLOOD!
  EXPRESSION: Shocked
- CHARACTER: Orlok
  LINE: Take heed what you do.
  EXPRESSION: Warning
- CHARACTER: Thomas
  LINE: It’s nothing.
  EXPRESSION: Dismissive
- CHARACTER: Narrator
  LINE: Orlok’s breathing grows louder... Louder...
  EXPRESSION: null
- CHARACTER: Orlok
  LINE: I might ease your wound.
  EXPRESSION: Sinister
- CHARACTER: Narrator
  LINE: Thomas senses Orlok’s animal instinct and guards his thumb – a reflex. He is immediately embarrassed by it, and lets go...
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Orlok stands slowly. His savage br
  EXPRESSION: null

::PATHS::
- CHOICE: "Observe Orlok's reaction"
  TARGET: orlok_reaction
  STATE_CHANGE: fear = +3
  CONDITION: null

::SCENE::
LOCATION: Castle Orlok. Great Hall - Night
MOOD: Dread, Gothic
CHARACTERS: Narrator, Orlok, Thomas
BACKGROUND_IMAGE: castle_orlok_great_hall_night.png
BACKGROUND_EDIT: "Dark, enormous fireplace casting little light, two armchairs."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Breathing growing... He walks toward THOMAS with dread intent... THOMAS is motionless, shaking with fear... what is happening?
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: BLOOD drips from his finger... ORLOK’S eyes sear into THOMAS... THOMAS breathes... ORLOK stops about six feet away, still obscured in darkness. He is consumed with bloodlust... But he must remain in control.
  EXPRESSION: null
- CHARACTER: Orlok
  LINE: Come by the fire. Your face shows you unwell.
  EXPRESSION: Calm, Menacing
- CHARACTER: Narrator
  LINE: ORLOK leads THOMAS to two armchairs by an enormous fireplace that somehow casts little light.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: THOMAS is sweaty, losing his grip on reality... He falls into the chair... THE COUNT stares at him hypnotically...
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: THOMAS is moving in and out of consciousness... THE TWO GARGOYLES SUPPORTING THE STONE MANTEL START TO MOVE... THEY LOOK AT THOMAS... THOMAS gasps...
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: IN DARKNESS, ORLOK APPROACHES HIM... HE BRINGS UP HIS ARMS...
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: THOMAS lets out a silent scream... ORLOK LUNGES AT HIM, ENVELOPING HIM IN DARKNESS!
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue"
  TARGET: harding_house_guest_room
  STATE_CHANGE: fear = +2
  CONDITION: null

::SCENE::
LOCATION: Harding House. Guest Room - Morning
MOOD: Melancholy, Love
CHARACTERS: Narrator, Ellen, Anna
BACKGROUND_IMAGE: harding_house_guest_room_morning.png
BACKGROUND_EDIT: "Sunlit room, trunk open, wedding dress."

::SCRIPT::
- CHARACTER: Narrator
  LINE: ELLEN takes her WEDDING DRESS out of a trunk. She holds it up with intense love and melancholy. She buries her face in it.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: She smells it, deeply. Hold.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: She smells it again.
  EXPRESSION: null
- CHARACTER: Anna
  LINE: Why ever did you bring that here?
  EXPRESSION: Concerned
- CHARACTER: Narrator
  LINE: ANNA has been standing in the doorway. She looks concerned.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: ELLEN is embarrassed. She fumbles with the dress.
  EXPRESSION: null
- CHARACTER: Anna
  LINE: Forgive me, I know you miss him. But, I daresay, you must put that away. Really, Leni.
  EXPRESSION: Sympathetic
- CHARACTER: Narrator
  LINE: ELLEN moves from embarrassment to shame. ANNA feels guilty.
  EXPRESSION: null
- CHARACTER: Anna
  LINE: Leni, what might we do for you?
  EXPRESSION: Caring
- CHARACTER: Ellen
  LINE: Tell me a letter from Thomas has arrived.
  EXPRESSION: Hopeful
- CHARACTER: Anna
  LINE: You received one within a fortnight.
  EXPRESSION: Matter-of-fact
- CHARACTER: Ellen
  LINE: That was yesterday.
  EXPRESSION: Impatient
- CHARACTER: Anna
  LINE: He doubtless just arrived himself.
  EXPRESSION: Reassuring
- CHARACTER: Ellen
  LINE: He said he’d write to me everyday.
  EXPRESSION: Overlapping, Sad
- CHARACTER: Anna
  LINE: The post would most surely be delayed from that strange part of the world.
  EXPRESSION: Explanatory
- CHARACTER: Narrator
  LINE: Pause.
  EXPRESSION: null
- CHARACTER: Anna
  LINE: What can cheer this poor humour, my love?
  EXPRESSION: Gentle
- CHARACTER: Ellen
  LINE: I should wish to go to the shore.
  EXPRESSION: Longing
- CHARACTER: Narrator
  LINE: This request strikes ANNA as strange.
  EXPRESSION: null
- CHARACTER: Anna
  LINE: Leni, it is now December.
  EXPRESSION: Surprised
- CHARACTER: Narrator
  LINE: ELLEN grows in excitement.
  EXPRESSION: null
- CHARACTER: Ellen
  LINE: It calms me to see the ships sail into port. Please? We must bring the children along! Please, my pet, it will be delicious fun!
  EXPRESSION: Excited, Pleading
- CHARACTER: Narrator
  LINE: ELLEN is beaming. Her excitement is almost discomforting.
  EXPRESSION: null

::PATHS::
- CHOICE: "Go to the shore"
  TARGET: castle_orlok_great_hall_morning
  STATE_CHANGE: hope = +2, unease = +1
  CONDITION: null

::SCENE::
LOCATION: Castle Orlok. Great Hall - Morning
MOOD: Disoriented, Ruined
CHARACTERS: Narrator, Thomas
BACKGROUND_IMAGE: castle_orlok_great_hall_morning.png
BACKGROUND_EDIT: "Cold stone floor, debris, rubble, dim light."

::SCRIPT::
- CHARACTER: Narrator
  LINE: THOMAS opens his eyes. He lies on his stomach, twisted up on the cold stone floor. He groans. As he gets up, he realizes his tie is undone.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: His collar flaps down to the side, his shirt is somewhat open. Flecks of blood on his linen tie... What the devil? He moves... He has a pain in his chest.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: He walks through the hall. It’s quite dark, even in daylight.
  EXPRESSION: null
- CHARACTER: Thomas
  LINE: Hello?
  EXPRESSION: Confused
- CHARACTER: Narrator
  LINE: The castle is in ruins. Covered in debris and rubble, as if no one had lived there in a hundred years.
  EXPRESSION: null
- CHARACTER: Thomas
  LINE: Count?!
  EXPRESSION: Calling Out
- CHARACTER: Narrator
  LINE: His voice echoes. Where are the servants? Where is everyone?
  EXPRESSION: null

::PATHS::
- CHOICE: "Search the castle"
  TARGET: castle_orlok_corridor_day
  STATE_CHANGE: confusion = +1, fear = +1
  CONDITION: null

::SCENE::
LOCATION: Castle Orlok. Corridor - Day
MOOD: Oppressive, Dream-like
CHARACTERS: Narrator, Thomas
BACKGROUND_IMAGE: castle_orlok_corridor_day.png
BACKGROUND_EDIT: "Dark stone corridors, locked doors."

::SCRIPT::
- CHARACTER: Narrator
  LINE: THOMAS wanders the castle trying to find someone, anyone. He fills with dread as he turns every deserted corner. The anxious atmosphere is dream-like.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: He continues through corridors of stone. Every door is LOCKED shut. The atmosphere becomes even more oppressive.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: At last: a room with a door ajar. Fearfully, he enters...
  EXPRESSION: null

::PATHS::
- CHOICE: "Enter the room"
  TARGET: castle_orlok_tower_chamber_continuous
  STATE_CHANGE: fear = +2
  CONDITION: null

::SCENE::
LOCATION: Castle Orlok. Tower Chamber - Continuous
MOOD: Gothic, Filthy
CHARACTERS: Narrator, Thomas
BACKGROUND_IMAGE: castle_orlok_tower_chamber.png
BACKGROUND_EDIT: "Filthy bedchamber, tenebrous mirror."

::SCRIPT::
- CHARACTER: Narrator
  LINE: It is a bedchamber. Gothic. Filthy. His overcoat and other belongings are all there. But he doesn’t see them.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: He walks in, opening up his shirt... headed to a tenebrous MIRROR on the wall... Impelled toward it... He hears the sound of one or two scuttling, screeching RATS.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: He looks at his murky reflection: There is a triangular BITE MARK ON HIS CHEST, OVER HIS HEART. Like a rat bite, only larger.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: A RAT runs past THOMAS’ feet. And another. He feels violated – horrified. Another RAT runs by... THOMAS drops the mirror! SUDDENLY...
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue"
  TARGET: castle_orlok_tower_chamber_bed_night_script_day
  STATE_CHANGE: horror = +3
  CONDITION: null

::SCENE::
LOCATION: Castle Orlok. Tower Chamber. Bed - Night/Script Day
MOOD: Disoriented, Horrified
CHARACTERS: Narrator, Thomas
BACKGROUND_IMAGE: castle_orlok_tower_chamber_bed.png
BACKGROUND_EDIT: "Dusty canopy bed, dim lighting."

::SCRIPT::
- CHARACTER: Narrator
  LINE: THOMAS wakes in a cold sweat! He is lying in the dusty canopy bed. Was it a dream? How did he get here? He looks down: THE BITE MARK IS STILL THERE.
  EXPRESSION: null

::PATHS::
- CHOICE: "Reflect"
  TARGET: estuary_day
  STATE_CHANGE: confusion = +2, horror = +1
  CONDITION: null

::SCENE::
LOCATION: Estuary - Day
MOOD: Somber, Romantic
CHARACTERS: Narrator, Anna, Ellen, Children, Head Nurse
BACKGROUND_IMAGE: estuary_day.png
BACKGROUND_EDIT: "Muddy bay shore, iron grave markers, sunset, children playing."

::SCRIPT::
- CHARACTER: Narrator
  LINE: ANNA and ELLEN walk arm in arm, among IRON GRAVE MARKERS near the shore of the muddy bay. They are in their warm shawls, bonnets, and parasols. A vast SUNSET behind them. THE CHILDREN play with their HEAD NURSE attending nearby.
  EXPRESSION: null
- CHARACTER: Anna
  LINE: Be careful now, children, keep from that filth!
  EXPRESSION: Calling Out
- CHARACTER: Narrator
  LINE: ELLEN is lost in thought watching the distant ships.
  EXPRESSION: null
- CHARACTER: Ellen
  LINE: Do you ever feel, at times, as if you were not – as if you were not a person?
  EXPRESSION: Questioning
- CHARACTER: Anna
  LINE: Well... I...
  EXPRESSION: Hesitant
- CHARACTER: Ellen
  LINE: What I wish to say is that you are not truly present nor alive, as if you were at the whim of another... like a doll, and someone or some thing had the power to breathe life into you, to move you?
  EXPRESSION: Explanatory
- CHARACTER: Narrator
  LINE: ANNA doesn’t understand. In fact, Ellen’s words frighten her a bit, but she wants to be supportive.
  EXPRESSION: null
- CHARACTER: Anna
  LINE: Well, of course I – we all feel out of sorts, set apart, at times. Small or... alone.
  EXPRESSION: Supportive, Hesitant
- CHARACTER: Ellen
  LINE: It’s not out of sorts.
  EXPRESSION: Insistent
- CHARACTER: Anna
  LINE: God.
  EXPRESSION: Startled
- CHARACTER: Narrator
  LINE: ANNA looks at her intensely. ELLEN smiles.
  EXPRESSION: null
- CHARACTER: Ellen
  LINE: No, my lovely Anna – I... Look at the sky!
  EXPRESSION: Passionate
- CHARACTER: Ellen
  LINE: Look at the sea! Does it never call to you? Urge you? Something is close at hand-
  EXPRESSION: Enthusiastic
- CHARACTER: Anna
  LINE: That is his power. A gentle breeze from Heaven–
  EXPRESSION: Gentle
- CHARACTER: Ellen
  LINE: Destiny!
  EXPRESSION: Overlapping, Passionate
- CHARACTER: Narrator
  LINE: She stares off into the horizon, the light igniting her eyes.
  EXPRESSION: null
- CHARACTER: Anna
  LINE: My sweet romantic.
  EXPRESSION: Affectionate
- CHARACTER: Narrator
  LINE: All of a sudden, ELLEN’S eyes fill with fear. Tears well up.
  EXPRESSION: null
- CHARACTER: Ellen
  LINE: I am not mad, Anna.
  EXPRESSION: Pleading
- CHARACTER: Anna
  LINE: Leni!
  EXPRESSION: Concerned
- CHARACTER: Ellen
  LINE: Forgive me. Everything I say sounds so childish.
  EXPRESSION: Ashamed
- CHARACTER: Anna
  LINE: Leni, your words spring from your honest heart.
  EXPRESSION: Reassuring
- CHARACTER: Ellen
  LINE: My heart is lost without my Thomas.
  EXPRESSION: Heartbroken
- CHARACTER: Narrator
  LINE: HOLD ON: ELLEN pining... but not for God.
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue"
  TARGET: castle_orlok_library_night
  STATE_CHANGE: longing = +3, fear = +1
  CONDITION: null

::SCENE::
LOCATION: Castle Orlok. Library - Night
MOOD: Foreboding, Mysterious
CHARACTERS: Narrator, Orlok, Thomas
BACKGROUND_IMAGE: castle_orlok_library_night.png
BACKGROUND_EDIT: "Cavernous library, documents, lithograph, dim lighting."

::SCRIPT::
- CHARACTER: Narrator
  LINE: ORLOK signs a document written in “the mysterious symbols.” And another in German. A lithograph of Grünewald Manor, is also on the table. Even as an illustration it’s a looming vulture of a building.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: THOMAS has become pale, sickly. He looks almost like a child standing awkwardly in the cavernous library. He coughs.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: ORLOK, again, has his face hidden in shadow.
  EXPRESSION: null
- CHARACTER: Orlok
  LINE: And your signature, as solicitor.
  EXPRESSION: Authoritative
- CHARACTER: Thomas
  LINE: How careless of me, my Lord.
  EXPRESSION: Apologetic
- CHARACTER: Narrator
  LINE: THOMAS looks at the strange alphabet. He hesitates...
  EXPRESSION: null
- CHARACTER: Orlok
  LINE: The language of my forefathers.
  EXPRESSION: Ancient
- CHARACTER: Thomas
  LINE: Of course.
  EXPRESSION: Resigned
- CHARACTER: Narrator
  LINE: As he leans in to sign, his SILVER HEART-SHAPED LOCKET dangles from his watch-chain. It ca
  EXPRESSION: null

::PATHS::
- CHOICE: "Sign the document"
  TARGET: end
  STATE_CHANGE: servitude = +1, sickness = +1
  CONDITION: null

::SCENE::
LOCATION: Not specified
MOOD: Foreboding
CHARACTERS: Narrator, Orlok, Thomas
BACKGROUND_IMAGE: null
BACKGROUND_EDIT: "Candlelight, shadowy room"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Orlok catches the light. Like a predatory bird, Orlok sees it immediately.
  EXPRESSION: null
- CHARACTER: Orlok
  LINE: A maiden’s token, I see. Your bride?
  EXPRESSION: Sly
- CHARACTER: Thomas
  LINE: Oh, just so. It... yes.
  EXPRESSION: Hesitant
- CHARACTER: Narrator
  LINE: Thomas looks up and begins to tuck the locket away back into his waistcoat.
  EXPRESSION: null
- CHARACTER: Orlok
  LINE: May I?
  EXPRESSION: Demanding
- CHARACTER: Narrator
  LINE: Pause. Thomas feels this to be odd. Very odd. But Orlok keeps his hand extended.
  EXPRESSION: null
- CHARACTER: Thomas
  LINE: Of course.
  EXPRESSION: Anxious
- CHARACTER: Narrator
  LINE: Anxiously, Thomas unclips it, and hands it to Orlok.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Orlok breathes heavily, walking away from Thomas. He follows, afraid to get too close to the Count. He sees Orlok hold the open locket in his withered palm... the lock of Ellen’s hair within. Orlok is transfixed.
  EXPRESSION: null
- CHARACTER: Thomas
  LINE: We are newly married, of late. Incidentally, I have letters to her I would post – If I may?
  EXPRESSION: Anxious
- CHARACTER: Orlok
  LINE: Liliac.
  EXPRESSION: Whispering
- CHARACTER: Narrator
  LINE: Orlok smells the locket, remembering...
  EXPRESSION: null
- CHARACTER: Thomas
  LINE: What was that, my lord?
  EXPRESSION: Confused
- CHARACTER: Narrator
  LINE: Orlok’s breathing is carnal. Beat. He controls his emotions.
  EXPRESSION: null
- CHARACTER: Orlok
  LINE: You are fortunate in your love.
  EXPRESSION: Envious
- CHARACTER: Narrator
  LINE: Thomas is more uncomfortable.
  EXPRESSION: null
- CHARACTER: Thomas
  LINE: Providence, as Herr Knock would say.
  EXPRESSION: Nervous
- CHARACTER: Orlok
  LINE: Your signature....
  EXPRESSION: Threatening
- CHARACTER: Narrator
  LINE: Thomas is motionless, for there was an unmistakable threat to Orlok’s cadence. Orlok senses Thomas’ hesitation.
  EXPRESSION: null
- CHARACTER: Orlok
  LINE: I pray you will indulge my pardon.
  EXPRESSION: Mocking
- CHARACTER: Narrator
  LINE: Orlok takes out a bejewelled chest from the darkness. He opens it with a skeleton key, and withdraws something. He tosses a heavy velvet purse on his table, overfull with solid gold coins from antiquity. A few spill out, glittering.
  EXPRESSION: null
- CHARACTER: Orlok
  LINE: I durst not neglect your commission, Herr Hutter.
  EXPRESSION: Deceptive
- CHARACTER: Narrator
  LINE: Thomas marvels at the gold. Something inside him screams to him not to sign...
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: BUT HE SIGNS ALL THE SAME. He steps away.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Orlok folds the papers and seals them with a series of medieval formalities in blood red wax. The Orlok sigil glistens in the candlelight. Thomas feels his fate is somehow sealed within that sigil. He feels dirty. Guilty.
  EXPRESSION: null
- CHARACTER: Orlok
  LINE: Now are we neighbours.
  EXPRESSION: Sinister
- CHARACTER: Thomas
  LINE: It is my good fortune, my lord. Forgive my asking, my lord, but why such an... antique residence as Grünewald Manor?
  EXPRESSION: Curious
- CHARACTER: Orlok
  LINE: The covenant is signed.
  EXPRESSION: Victorious
- CHARACTER: Thomas
  LINE: Of course...
  EXPRESSION: Uneasy
- CHARACTER: Narrator
  LINE: Thomas coughs again. He puts the papers into his satchel.
  EXPRESSION: null
- CHARACTER: Thomas
  LINE: Well, I thank you and congratulate you on your new home.
  EXPRESSION: Forced
- CHARACTER: Orlok
  LINE: It is late. You must wish to retire?
  EXPRESSION: Feigned concern
- CHARACTER: Thomas
  LINE: If I may, my lord, if I may be slightly unsubtle in my approach... I wish to depart as soon as, well, as soon as agreeable, my services rendered. I am much... I have been enduring the most irregular dreams. I fear I am taken ill.
  EXPRESSION: Desperate
- CHARACTER: Narrator
  LINE: Orlok has disappeared into darkness.
  EXPRESSION: null
- CHARACTER: Thomas
  LINE: My lord? Count?
  EXPRESSION: Panicked
- CHARACTER: Narrator
  LINE: Orlok’s voice is somehow louder and more overwhelming, even as he himself is unseen:
  EXPRESSION: null
- CHARACTER: Orlok (O.S.)
  LINE: It is a black omen to journey in poor health. You will remain and well rest yourself, that your strength may soon return to you. Leave here your letters.
  EXPRESSION: Commanding
- CHARACTER: Thomas
  LINE: I must object, my lord.
  EXPRESSION: Defiant
- CHARACTER: Orlok
  LINE: You will obey this my council.
  EXPRESSION: Ruthless
- CHARACTER: Thomas
  LINE: But my lord...
  EXPRESSION: Pleading
- CHARACTER: Narrator
  LINE: Silence.
  EXPRESSION: null
- CHARACTER: Thomas
  LINE: Count?
  EXPRESSION: Desperate
- CHARACTER: Narrator
  LINE: Thomas takes a step further... He runs into the darkness... Orlok is nowhere to be found... Thomas stops:
  EXPRESSION: null
- CHARACTER: Thomas
  LINE: You have my locket...
  EXPRESSION: Terrified
- CHARACTER: Narrator
  LINE: He has never felt so vulnerable.
  EXPRESSION: null

::SCENE::
LOCATION: Harding House. Guest Room
MOOD: Eerie
CHARACTERS: Narrator, Ellen, Orlok (shadow)
BACKGROUND_IMAGE: null
BACKGROUND_EDIT: "Nighttime, moonlight, ships in harbor"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Ellen stands by the window. She watches the ships pass in the harbour. Her white skin is even whiter in the moonlight.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Slowly, a shadow drifts toward her, reaching... It is the shadow of Orlok’s hand... She hears the familiar whisper of his language... The claw grasps her tight... Ellen feels the shadow overwhelm her.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: She is seized with terror. Her breath quickens... she is under his spell...
  EXPRESSION: null

::SCENE::
LOCATION: Castle Orlok. Courtyard
MOOD: Desperate
CHARACTERS: Narrator, Thomas
BACKGROUND_IMAGE: null
BACKGROUND_EDIT: "Late afternoon, castle exterior"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Thomas tears through the castle. Every door is locked. He has grown more pale... weak. Panic sets in.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Thomas runs to the main gate. It is locked too. He pulls, he bangs. It is no use. He knows for certain that he is a prisoner.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Thomas scours the courtyard for a way out.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: He finds another door. It is locked too, but very weather-beaten. He can break in! Thomas picks up a stone... HE SMASHES THE DOOR...
  EXPRESSION: null

::SCENE::
LOCATION: Castle Orlok. Crypt
MOOD: Terrifying
CHARACTERS: Narrator, Thomas, Orlok
BACKGROUND_IMAGE: null
BACKGROUND_EDIT: "Continuous, dark, damp, dripping corridor"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Thomas walks slowly... his eyes adjusting to the darkness... He breathes heavily as he walks down a long, dank, dripping corridor. In front of him is a steep stairwell... He descends... His heart racing... Breathing...
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: As he reaches the bottom of the staircase, he fumbles, not seeing the last step...
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Thomas looks: the castle catacombs. The rank smell of death is thick in the musty air. It stings his eyes.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: He walks past coffins, skeletons in recessed tombs. At the far end of the vault is a large ancient sarcophagus. He is drawn to it.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: He passes a few dim beams of sunlight. Near the coffin, a pit has been dug in the dirt floor – soil removed – a shovel stuck in the ground.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: As he nears the sarcophagus he sees it is adorned with a magical heptagram. In the centre is Orlok’s sigil.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: It compels him onward... Closer... closer...
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: He holds his breath... he pushes the lid open... it lands with a dusty thud.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: WITHIN IS THE DEAD BODY OF ORLOK! In an instant Thomas sees: a horrible mangled creature, naked and half-buried in the rat-infested earth. His jaundiced, leathery flesh is bloated and bruised in the glands and stomach. Blood leaks from all of his orifices, especially his slightly open mouth, revealing sharp carnivorous teeth. His eyes wide open: dead, murky and colourless. He is a vampire.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Thomas trembles, nearly falling backward. He picks up the nearby shovel to strike him.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: He bravely lifts it high... he thrusts it into the coffin...
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: (Behind him the dim beams of sunlight fade into darkness...)
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Orlok’s eyes grow conscious... Just then, Orlok grabs the shovel... with incredible strength, he jerks it away from Thomas... Orlok rises from his coffin, the soil falling from his naked, emaciated body ... Thomas runs!
  EXPRESSION: null

::SCENE::
LOCATION: Castle Orlok. Corridor
MOOD: Panic
CHARACTERS: Narrator, Thomas
BACKGROUND_IMAGE: null
BACKGROUND_EDIT: "Nighttime, walls caving in"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Thomas is in a trance, running, heavy breathing, the castle walls caving in on him. His heartbeat pounding his brains to bits.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Black wolves chase him like phantoms, growling and barking.
  EXPRESSION: null

::SCENE::
LOCATION: Castle Orlok. Tower Chamber
MOOD: Trapped
CHARACTERS: Narrator, Thomas
BACKGROUND_IMAGE: null
BACKGROUND_EDIT: "Moments later, tower chamber"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Thomas slams the door and locks it’s massive bolt. Wolves jumping against the door! Their ferocity is relentless.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: He cries and laughs
  EXPRESSION: null

::SCENE::
LOCATION: Castle Orlok. Darkness
MOOD: Intense Supernatural Focus
CHARACTERS: Orlok
BACKGROUND_IMAGE: castle_orlok_darkness.png
BACKGROUND_EDIT: "Orlok alone in darkness, holding a locket"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Orlok is still. He holds the LOCKET. He buries his face within his hands. He smells her HAIR. Deeply. His eyes fill with desire, rolling back in his head, becoming WHITE.
  EXPRESSION: Intense Desire
- CHARACTER: Narrator
  LINE: Slowly, he raises his hand as a great magician... his claw is tense with unimaginable power... he whispers a dark incantation to ELLEN.
  EXPRESSION: Powerful, Menacing

::PATHS::
- CHOICE: "Continue incantation"
  TARGET: harding_house_hallway
  STATE_CHANGE: orlok_power = +1
  CONDITION: null

::SCENE::
LOCATION: Harding House. Upstairs Hallway
MOOD: Hypnotic, Erotic
CHARACTERS: Ellen
BACKGROUND_IMAGE: harding_house_hallway.png
BACKGROUND_EDIT: "Upstairs hallway at night, dimly lit"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Ellen sleepwalks, hypnotized – her eyes wide.
  EXPRESSION: Hypnotized
- CHARACTER: Narrator
  LINE: She moves calmly and sylph-like, through the cold house wearing nothing but a thin nightgown. She is perspiring heavily. Her chest heaves.
  EXPRESSION: Erotic, Troubled
- CHARACTER: Narrator
  LINE: Her mouth opens. She breathes sensually. Louder... Louder... She nears the stairs.
  EXPRESSION: Sensual

::PATHS::
- CHOICE: "Approach the stairs"
  TARGET: harding_house_bedchamber
  STATE_CHANGE: ellen_trance = +1
  CONDITION: null

::SCENE::
LOCATION: Harding House. Bed Chamber
MOOD: Intimate, Interrupted
CHARACTERS: Harding, Anna
BACKGROUND_IMAGE: harding_house_bedchamber.png
BACKGROUND_EDIT: "Bedroom at night, soft lighting, couple in bed"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Harding and Anna are making love in bed. They kiss sweetly, lovingly. Quietly.
  EXPRESSION: Loving
- CHARACTER: Narrator
  LINE: Suddenly... they hear FOOTSTEPS. Creaking floorboards.
  EXPRESSION: Startled
- CHARACTER: Anna
  LINE: (whispered) Stop.
  EXPRESSION: Uneasy
- CHARACTER: Narrator
  LINE: Harding doesn’t want to. He doesn’t.
  EXPRESSION: Reluctant
- CHARACTER: Anna
  LINE: (whispered) Stop my love. Do you hear that?
  EXPRESSION: Concerned
- CHARACTER: Narrator
  LINE: He stops. THE FOOTSTEPS GROW LOUDER. Anna calls out:
  EXPRESSION: Anxious
- CHARACTER: Anna
  LINE: Clara? Is that you?
  EXPRESSION: Curious, Uneasy

::PATHS::
- CHOICE: "Investigate footsteps"
  TARGET: castle_orlok_corridor
  STATE_CHANGE: tension = +1
  CONDITION: null

::SCENE::
LOCATION: Castle Orlok. Corridor
MOOD: Ominous Approach
CHARACTERS: Orlok
BACKGROUND_IMAGE: castle_orlok_corridor.png
BACKGROUND_EDIT: "Dark castle corridor, only Orlok visible"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Orlok walks slowly, steadily, in darkness. Each un-dead step echoing through the castle... Closer and closer to THOMAS...
  EXPRESSION: Relentless, Predatory

::PATHS::
- CHOICE: "Continue towards Thomas"
  TARGET: castle_orlok_tower_chamber_1
  STATE_CHANGE: orlok_proximity = +1
  CONDITION: null

::SCENE::
LOCATION: Castle Orlok. Tower Chamber
MOOD: Trance-like, Dread
CHARACTERS: Thomas, Orlok (shadow)
BACKGROUND_IMAGE: castle_orlok_tower_chamber.png
BACKGROUND_EDIT: "Tower chamber at night, Thomas in a trance"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Thomas’ emotions fade. He is in a trance, eyes wide open like Ellen’s. He hears Orlok’s footsteps approaching...
  EXPRESSION: Tranced, Fearful
- CHARACTER: Narrator
  LINE: THE SHADOW OF ORLOK looms over THOMAS trembling - but ORLOK is not in the room!
  EXPRESSION: Terrified
- CHARACTER: Narrator
  LINE: THOMAS steps away from the door... He stands back... The chamber door unlocks and slowly opens...
  EXPRESSION: Fearful, Hesitant
- CHARACTER: Narrator
  LINE: ORLOK stands in the distance surrounded by the WOLVES sitting tame at his feet. His eyes smoulder with bloodlust.
  EXPRESSION: Demonic, Bloodthirsty

::PATHS::
- CHOICE: "Face Orlok"
  TARGET: castle_orlok_tower_chamber_2
  STATE_CHANGE: fear = +2, orlok_power = +1
  CONDITION: null

::SCENE::
LOCATION: Harding House. Street
MOOD: Erotic, Dangerous
CHARACTERS: Ellen, Harding, Anna, Servant
BACKGROUND_IMAGE: harding_house_street.png
BACKGROUND_EDIT: "Street outside the house at night, near a canal"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Ellen walks barefoot into the street... Her erotic breathing growing...
  EXPRESSION: Erotic, Driven
- CHARACTER: Narrator
  LINE: She nears the edge of the quay, dangerously close to a canal...
  EXPRESSION: Reckless
- CHARACTER: Narrator
  LINE: HARDING, ANNA and a SERVANT rush out after her!
  EXPRESSION: Frantic
- CHARACTER: Harding & Anna
  LINE: Ellen! Ellen!
  EXPRESSION: Desperate

::PATHS::
- CHOICE: "Try to stop Ellen"
  TARGET: castle_orlok_tower_chamber_3
  STATE_CHANGE: danger = +1
  CONDITION: null

::SCENE::
LOCATION: Castle Orlok. Tower Chamber
MOOD: Climax of Supernatural Struggle
CHARACTERS: Orlok, Thomas
BACKGROUND_IMAGE: castle_orlok_tower_chamber_3.png
BACKGROUND_EDIT: "Tower chamber, Orlok towering over Thomas"

::SCRIPT::
- CHARACTER: Narrator
  LINE: ORLOK gets closer to THOMAS... Closer... THOMAS’ breath grows louder... louder... ORLOK RAISES HIS TALONS...
  EXPRESSION: Intense, Threatening
- CHARACTER: Narrator
  LINE: IMAGE: THOMAS POV: ELLEN STANDS ENTIRELY NAKED ABOVE THOMAS (in the same position that Orlok is in).
  EXPRESSION: Surreal, Disturbing
- CHARACTER: Narrator
  LINE: ORLOK ATTACKS THOMAS!
  EXPRESSION: Violent
- CHARACTER: Narrator
  LINE: IMAGE: ORLOK LIFTS UP THOMAS IN A SWIRL OF DARKNESS – THOMAS GIVES IN TO HIS POWER (does he like it?) – SUFFOCATING - HE CAN’T BREATHE. THEY SEEM TO LEVITATE IN ECSTASY.
  EXPRESSION: Ecstatic, Suffocating, Ambiguous
- CHARACTER: Narrator
  LINE: IMAGE: CU: ELLEN’S WHITE FACE IN THE MOONLIGHT, HER MOUTH DRIPPING RED BLOOD - HER EYES INSANE!
  EXPRESSION: Insane, Bloodthirsty

::PATHS::
- CHOICE: "Witness the attack"
  TARGET: harding_house_street_2
  STATE_CHANGE: orlok_victory = true, thomas_fate = unknown
  CONDITION: null

::SCENE::
LOCATION: Harding House. Street
MOOD: Catastrophe
CHARACTERS: Ellen
BACKGROUND_IMAGE: harding_house_street_2.png
BACKGROUND_EDIT: "Ellen collapsing on cobblestones"

::SCRIPT::
- CHARACTER: Narrator
  LINE: ELLEN’S eyes grow even more huge – she is orgasmic!
  EXPRESSION: Orgasmic, Overwhelmed
- CHARACTER: Narrator
  LINE: ELLEN FAINTS, COLLAPSING TO THE COBBLESTONES!
  EXPRESSION: Fainting, Overwhelmed

::PATHS::
- CHOICE: "Ellen faints"
  TARGET: castle_orlok_tower_chamber_4
  STATE_CHANGE: ellen_collapse = true
  CONDITION: null

::SCENE::
LOCATION: Castle Orlok. Tower Chamber
MOOD: Supernatural Consumption
CHARACTERS: Orlok, Thomas
BACKGROUND_IMAGE: castle_orlok_tower_chamber_4.png
BACKGROUND_EDIT: "Orlok's body on Thomas, pulsing"

::SCRIPT::
- CHARACTER: Narrator
  LINE: WIDE: ORLOK’S NAKED BODY LIES ON TOP OF THOMAS LIKE A NIGHTMARE – A SUPERNATURAL LEECH.
  EXPRESSION: Horrific, Draining
- CHARACTER: Narrator
  LINE: HIS UNCANNY STRENGTH DOMINATES THOMAS COMPLETELY, HIS HEAD AND HUNCHED BACK PULSING... DRINKING THOMAS’ BLOOD FROM HIS BREAST!
  EXPRESSION: Dominating, Consuming
- CHARACTER: Narrator
  LINE: BLACK.
  EXPRESSION: null

::PATHS::
- CHOICE: "Fade to black"
  TARGET: harding_house_guest_room
  STATE_CHANGE: thomas_drained = true
  CONDITION: null

::SCENE::
LOCATION: Harding House. Guest Room
MOOD: Concerned, Medical
CHARACTERS: Ellen, Doctor Sievers, Harding
BACKGROUND_IMAGE: harding_house_guest_room.png
BACKGROUND_EDIT: "Guest room at night, dimly lit, doctor with patient"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Several flickering lamps illuminate ELLEN’S room. A little porcelain-faced clock ticks balefully in the late hours of the night. A tall, kind-eyed gentleman, DOCTOR SIEVERS (40s/50s), is by ELLEN’S side packing up his bag. She moans a bit, asleep.
  EXPRESSION: Somber, Medical
- CHARACTER: Doctor Sievers
  LINE: In mild cases of somnambulism – sleepwalking – it is brought on by a congestion of the blood. Too much blood. Perhaps she was oppressed in a somewhat odd position beforehand.
  EXPRESSION: Professional, Explanatory
- CHARACTER: Harding
  LINE: Yet she has had these fits in the past. Troubled nerves and so on.
  EXPRESSION: Worried, Concerned
- CHARACTER: Doctor Sievers
  LINE: I see. If it continues, let me know of it, but for now, keep it from your worries, my dear fellow.
  EXPRESSION: Reassuring
- CHARACTER: Harding
  LINE: Yes. Of course.
  EXPRESSION: Resigned
- CHARACTER: Doctor Sievers
  LINE: I am disposed to recommend that she sleep in her corset. It encourages the correct posture, calms the womb, and revives circulation.
  EXPRESSION: Prescriptive, Slightly Unusual
- CHARACTER: Harding
  LINE: Yes, very well.
  EXPRESSION: Accepting
- CHARACTER: Doctor Sievers
  LINE: And if her stirring escalates, you can always tie her to the bed.
  EXPRESSION: Humorous (attempted)
- CHARACTER: Narrator
  LINE: SIEVERS tries to be humorous. HARDING laughs a little to be polite, though he finds the joke distasteful.
  EXPRESSION: Polite, Displeased
- CHARACTER: Narrator
  LINE: ELLEN starts to mumble. Yearning.
  EXPRESSION: Mumbling, Yearning
- CHARACTER: Ellen
  LINE: (whispered) He is coming to me. He is coming.
  EXPRESSION: Yearning, Erotic
- CHARACTER: Narrator
  LINE: HARDING looks concerned, uncomfortable, and somehow vulnerable from her overtly sexual tone. SIEVERS feels the same.
  EXPRESSION: Concerned, Uncomfortable, Vulnerable
- CHARACTER: Doctor Sievers
  LINE: I’ll increase the ether.
  EXPRESSION: Decisive
- CHARACTER: Narrator
  LINE: He douses a handkerchief in the sedative and covers her mouth and nose.
  EXPRESSION: Administering Sedative

::PATHS::
- CHOICE: "Administer ether"
  TARGET: castle_orlok_tower_chamber_5
  STATE_CHANGE: sedation = +1
  CONDITION: null

::SCENE::
LOCATION: Castle Orlok. Tower Chamber
MOOD: Survival, Escape
CHARACTERS: Thomas, Wolves
BACKGROUND_IMAGE: castle_orlok_tower_chamber_5.png
BACKGROUND_EDIT: "Tower chamber at dawn, Thomas injured, wolves present"

::SCRIPT::
- CHARACTER: Narrator
  LINE: THOMAS awakes in pain. Very little blood left in his body – half dead.
  EXPRESSION: Weak, In Pain
- CHARACTER: Narrator
  LINE: He looks around. His shirt and waistcoat are bloody and have been torn open... He must escape!
  EXPRESSION: Desperate
- CHARACTER: Narrator
  LINE: Just then, he hears a terrible growling! He turns around... His door is open and THE WOLVES standing there – stalking him!
  EXPRESSION: Terrified
- CHARACTER: Narrator
  LINE: They dart into the chamber... THOMAS climbs on the window ledge... WOLVES jump at him... He flees out the window just in time!
  EXPRESSION: Panicked, Escaping

::PATHS::
- CHOICE: "Flee through the window"
  TARGET: castle_orlok_tower
  STATE_CHANGE: escape = true
  CONDITION: null

::SCENE::
LOCATION: Castle Orlok. Tower
MOOD: Desperate Leap
CHARACTERS: Thomas, Wolves
BACKGROUND_IMAGE: castle_orlok_tower.png
BACKGROUND_EDIT: "Outside the tower, misty, icy water below"

::SCRIPT::
- CHARACTER: Narrator
  LINE: THOMAS teeters outside the window. THE WOLVES bark, growl and snarl into the morning air.
  EXPRESSION: Precarious, Threatened
- CHARACTER: Narrator
  LINE: HE LOOKS DOWN: Through the mist, ICY WATER rushes through the remains of a moat out to a river. The mountain wind blows relentlessly... He can barely keep his balance on the ledge...
  EXPRESSION: Fearful, Determined
- CHARACTER: Narrator
  LINE: He has no choice... He closes his eyes... He leaps, disappearing into the mist... The water swallows him.
  EXPRESSION: Resigned, Hopeful (of survival)

::PATHS::
- CHOICE: "Leap into the water"
  TARGET: estuary_sunset
  STATE_CHANGE: thomas_disappeared = true
  CONDITION: null

::SCENE::
LOCATION: Estuary. Sunset
MOOD: Anxious Waiting, Lingering Hope
CHARACTERS: Ellen, Harding, Anna
BACKGROUND_IMAGE: estuary_sunset.png
BACKGROUND_EDIT: "Estuary at sunset, Ellen wrapped in blankets, Ellen and Harding/Anna with her"

::SCRIPT::
- CHARACTER: Narrator
  LINE: ELLEN sits like a ghost wrapped in blankets in her wicker convalescent chair. She stares out at the sailing ships.
  EXPRESSION: Ghostly, Longing
- CHARACTER: Ellen
  LINE: Nothing of Thomas – nothing?
  EXPRESSION: Anxious, Hopeful
- CHARACTER: Narrator
  LINE: HARDING AND ANNA, in furs, are by her. The children are not with them. Sea birds screech (O.S.).
  EXPRESSION: Concerned, somber
- CHARACTER: Harding
  LINE: (overlapping) No. I mean, yes. I have received nothing of any kind.
  EXPRESSION: Evasive, Distressed
- CHARACTER: Ellen
  LINE: Not even to your... at the shipyard? And Herr Knock?
  EXPRESSION: Yearning, Anxious
- CHARACTER: Narrator
  LINE: Ellen looks yearningly at Harding and grasps his hand. He pulls away reflexively, and averts his eyes from her gaze.
  EXPRESSION: Yearning, Rebuffed
- CHARACTER: Harding
  LINE: Still no trace of him. The firm is in daily chaos.
  EXPRESSION: Frustrated, Distressed
- CHARACTER: Narrator
  LINE: HARDING looks at her now:
  EXPRESSION: Stern, Concerned
- CHARACTER: Harding
  LINE: I am most sensitive to your ardent nature, and shan’t reprove you further in this error of judgement. I will send someone daily until Herr Knock is found.
  EXPRESSION: Formal, Reassuring (with a hint of disapproval)
- CHARACTER: Narrator
  LINE: ELLEN looks
  EXPRESSION: Hopeful, Dejected

::PATHS::
- CHOICE: "Continue waiting"
  TARGET: end
  STATE_CHANGE: waiting_for_news = true
  CONDITION: null

::SCENE::
LOCATION: Estuary
MOOD: Melancholy
CHARACTERS: Narrator, Harding, Anna, Ellen
BACKGROUND_IMAGE: estuary.png
BACKGROUND_EDIT: "Late afternoon, calm water, Ellen staring out to sea"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Harding feels a bit guilty.
  EXPRESSION: null
- CHARACTER: Harding
  LINE: Thomas is well. I am certain of it.
  EXPRESSION: Reassuring
- CHARACTER: Anna
  LINE: Leni, it is near sundown, we really ought to be leaving.
  EXPRESSION: Concerned
- CHARACTER: Narrator
  LINE: Ellen keeps staring out. Lost. Her eyes fill with tears.
  EXPRESSION: Distressed
- CHARACTER: Anna
  LINE: Leni?
  EXPRESSION: Concerned
- CHARACTER: Ellen
  LINE: A moment longer... please.
  EXPRESSION: Longing

::PATHS::
- CHOICE: "Stay a moment longer"
  TARGET: estuary_later
  STATE_CHANGE: sadness = +1
  CONDITION: null
- CHOICE: "Leave now"
  TARGET: estuary_later
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Estuary
MOOD: Approaching Dread
CHARACTERS: Narrator, Harding, Anna, Ellen
BACKGROUND_IMAGE: estuary_later.png
BACKGROUND_EDIT: "Sunset, tide rising, Harding and Anna walking away from Ellen"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Harding and Anna walk away from Ellen. The sun quickly disappears behind them. Night approaches...
  EXPRESSION: null
- CHARACTER: Anna
  LINE: Clara asked me today if Aunty Ellen has become a ghost.
  EXPRESSION: Worried
- CHARACTER: Harding
  LINE: I thought it was agreed you were to keep the girls from her.
  EXPRESSION: Stern
- CHARACTER: Anna
  LINE: Friedrich, be not a churl, please –
  EXPRESSION: Pleading
- CHARACTER: Harding
  LINE: You mustn’t be swept up in her fairy ways. The entirety of the household centres upon her whims. I tire of discussing her.
  EXPRESSION: Impatient
- CHARACTER: Anna
  LINE: Think you there is no burden upon myself? I love her. She is blameless of her malady.
  EXPRESSION: Hurt
- CHARACTER: Harding
  LINE: Forgive me, my love. Dr. Sievers will pay another visit. Let us only please talk of something else. How is our little Friedrich?
  EXPRESSION: Apologetic
- CHARACTER: Narrator
  LINE: He touches her belly. She smiles a bit.
  EXPRESSION: Tender
- CHARACTER: Anna
  LINE: Well. Hungry as always ... Like his father.
  EXPRESSION: Smiling
- CHARACTER: Narrator
  LINE: Harding leans in and kisses her. Anna blushes.
  EXPRESSION: Affectionate
- CHARACTER: Anna
  LINE: Really, Friedrich, in public.
  EXPRESSION: Bashful
- CHARACTER: Harding
  LINE: I cannot resist you, my love.
  EXPRESSION: Passionate
- CHARACTER: Narrator
  LINE: Anna smiles, and then looks over her shoulder... She screams:
  EXPRESSION: Shocked
- CHARACTER: Anna
  LINE: Ellen! Leni!!
  EXPRESSION: Terrified
- CHARACTER: Narrator
  LINE: The sun has set. The tide has risen. Ellen has fallen, covered in slime and muck. Her skirts are up around her waist. One leg is bare, the other in just a stocking... her thighs exposed... her satin shoes lost in the bay. Her body convulsing erotically...
  EXPRESSION: Disturbed
- CHARACTER: Ellen
  LINE: He is coming! He is coming!
  EXPRESSION: Delirious

::PATHS::
- CHOICE: "Rush to Ellen's aid"
  TARGET: hospital_surgery
  STATE_CHANGE: fear = +2
  CONDITION: null

::SCENE::
LOCATION: Wisburg Hospital. Surgery
MOOD: Chaotic
CHARACTERS: Narrator, Sievers, Orderly
BACKGROUND_IMAGE: hospital_surgery.png
BACKGROUND_EDIT: "Daytime, sterile operating room, distant screams"

::SCRIPT::
- CHARACTER: Narrator
  LINE: A hostile scream is heard in the distance.
  EXPRESSION: null
- CHARACTER: Sievers
  LINE: A new patient?
  EXPRESSION: Annoyed
- CHARACTER: Narrator
  LINE: Sievers turns from his fastidiously-ordered desk. His chair creaks. A uniformed Orderly (50s) mops the sweat from his brow. The screaming continues echoing in the halls.
  EXPRESSION: null
- CHARACTER: Orderly
  LINE: Yes sir, he’s... we stowed ‘em downstairs, sir.
  EXPRESSION: Nervous
- CHARACTER: Sievers
  LINE: I have strictly forbidden the use of the old cells!
  EXPRESSION: Angry
- CHARACTER: Orderly
  LINE: Beggin’ your pardon, Doctor, sir –
  EXPRESSION: Submissive
- CHARACTER: Sievers
  LINE: Out of the question. This a modern hospital, not a prison –
  EXPRESSION: Stern
- CHARACTER: Narrator
  LINE: The Orderly continues. He is in a mild state of shock.
  EXPRESSION: null
- CHARACTER: Orderly
  LINE: A little old soul he looks, but on my life... saw him screamin’ and a-groanin’... found him at the Luther Christmas market... killed three sheep with his bare hands – and he was eatin’ em raw-like. Raw!
  EXPRESSION: Horrified

::PATHS::
- CHOICE: "Investigate the basement"
  TARGET: hospital_basement_corridor
  STATE_CHANGE: curiosity = +1, fear = +1
  CONDITION: null

::SCENE::
LOCATION: Wisburg Hospital. Basement Corridor
MOOD: Foreboding
CHARACTERS: Narrator, Sievers, Orderly
BACKGROUND_IMAGE: hospital_basement_corridor.png
BACKGROUND_EDIT: "Daytime, dimly lit stone corridor, eerie weeping"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Sievers walks the Orderly to the old 18th century cells. The ones they don’t like to talk about. An eerie weeping is heard from inside...
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The Orderly opens a wooden door, nearly one foot thick... They enter...
  EXPRESSION: null

::PATHS::
- CHOICE: "Enter the cell"
  TARGET: knock_cell
  STATE_CHANGE: fear = +2
  CONDITION: null

::SCENE::
LOCATION: Wisburg Hospital. Knock's Cell
MOOD: Disturbing
CHARACTERS: Narrator, Sievers, Orderly, Knock
BACKGROUND_IMAGE: knock_cell.png
BACKGROUND_EDIT: "Continuous, dark and damp cell, hunched figure, mysterious symbols"

::SCRIPT::
- CHARACTER: Narrator
  LINE: It is dark. In the far corner of the cold, damp room is a hunched figure rocking back and forth, weeping. A murky shaft of light leaks through the small, barred window. The same “mysterious symbols” are scratched into the plaster walls.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Sievers slowly approaches. The Orderly stands close by.
  EXPRESSION: null
- CHARACTER: Sievers
  LINE: Hello. Good day, mein Herr. I am Dr. Sievers.
  EXPRESSION: Calm
- CHARACTER: Narrator
  LINE: The figure keeps weeping. Pigeons dart about.
  EXPRESSION: null
- CHARACTER: Sievers
  LINE: What, what seems to be the trouble?
  EXPRESSION: Inquisitive
- CHARACTER: Knock
  LINE: No trouble. Providence. Providence. He is coming to us.
  EXPRESSION: Delusional
- CHARACTER: Narrator
  LINE: His weeping turns into a laugh... a familiar laugh.
  EXPRESSION: null
- CHARACTER: Sievers
  LINE: I see. Can you tell me your name, Herr...?
  EXPRESSION: Patient
- CHARACTER: Knock
  LINE: No one. I am no one. His servant.
  EXPRESSION: Possessed
- CHARACTER: Sievers
  LINE: And um, what do you have there?
  EXPRESSION: Curious
- CHARACTER: Narrator
  LINE: The laughter continues. He turns around... It is Knock, dried blood upon his chin and expensive shirt front. His eyes are pitiful. Somehow missing the spark of human-ness. By his side is a collection of dead cockroaches, spiders, birds, etc.
  EXPRESSION: Horrified
- CHARACTER: Knock
  LINE: Lives. Gifts bestowed from his Lordship.
  EXPRESSION: Laughing
- CHARACTER: Narrator
  LINE: He eats one of the spiders. He laughs.
  EXPRESSION: Disgusted
- CHARACTER: Narrator
  LINE: Suddenly, Knock scuttles along the straw-strewn floor and catches one of the waddling pigeons. He pets it.
  EXPRESSION: null
- CHARACTER: Knock
  LINE: She is a pretty one. His Lordship loves the pretty ones best.
  EXPRESSION: Possessive
- CHARACTER: Narrator
  LINE: Knock presses the pigeon against his face.
  EXPRESSION: null
- CHARACTER: Sievers
  LINE: His Lordship?
  EXPRESSION: Inquiring
- CHARACTER: Narrator
  LINE: Knock becomes very excited.
  EXPRESSION: null
- CHARACTER: Knock
  LINE: He is Infinity... Eyes shining like a jewelled diadem. Putrescence. Asphyxience.
  EXPRESSION: Ecstatic
- CHARACTER: Narrator
  LINE: Knock puts the pigeon’s head in his mouth... He bites the head off the pigeon! He swallows it!
  EXPRESSION: Shocked
- CHARACTER: Knock
  LINE: Devourence.
  EXPRESSION: Guttural
- CHARACTER: Narrator
  LINE: Sievers stays calm.
  EXPRESSION: null
- CHARACTER: Sievers
  LINE: Now, my good fellow, why would you do that?
  EXPRESSION: Measured
- CHARACTER: Narrator
  LINE: Sievers walks toward him. The Orderly follows with his club ready.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Knock flinches, afraid.
  EXPRESSION: null
- CHARACTER: Sievers
  LINE: It’s alright. No one wants to hurt you, my dear friend.
  EXPRESSION: Soothing
- CHARACTER: Narrator
  LINE: Sievers walks closer.
  EXPRESSION: null
- CHARACTER: Knock
  LINE: He is coming.
  EXPRESSION: Terrified
- CHARACTER: Narrator
  LINE: Closer...
  EXPRESSION: null
- CHARACTER: Sievers
  LINE: Who, who is?
  EXPRESSION: Puzzled
- CHARACTER: Knock
  LINE: ‘Twas He that invoked me! ’Twas I that was chosen to serve Him for I know what He covets. And He shall cast upon you curses, confusion, affliction and rebuke, for you have forsaken me! And He shall reign over all your empty corpses! Devourence! Devourence!!
  EXPRESSION: Furious
- CHARACTER: Narrator
  LINE: Knock attacks Sievers! The Orderly blows his whistle and pulls them apart. Two more Attendants rush in, throwing pails of water on Knock and beat him with their clubs. He laughs and laughs, struggling, and bleeding on the floor. He seems to enjoy the beating.
  EXPRESSION: Violent
- CHARACTER: Knock
  LINE: He is coming!
  EXPRESSION: Manic
- CHARACTER: Narrator
  LINE: Whack! Whack!! Whack!!!
  EXPRESSION: Brutal

::PATHS::
- CHOICE: "Leave the cell"
  TARGET: harding_house_guest_room
  STATE_CHANGE: trauma = +2
  CONDITION: null

::SCENE::
LOCATION: Harding House. Guest Room
MOOD: Agitated
CHARACTERS: Narrator, Ellen, Dr. Sievers, Harding, Anna
BACKGROUND_IMAGE: harding_house_guest_room.png
BACKGROUND_EDIT: "Nighttime, dimly lit bedroom, Ellen struggling in bed"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Ellen, her eyes wide, tosses and turns violently in bed.
  EXPRESSION: null
- CHARACTER: Ellen
  LINE: (whispered) He is coming.
  EXPRESSION: Terrified
- CHARACTER: Narrator
  LINE: Dr. Sievers tightens the laces of her corset as Harding holds her down. They can barely contain her. Anna stands by in distress. Harding and Anna exchange a tense glance as Ellen moans, restrained by the men.
  EXPRESSION: null

::PATHS::
- CHOICE: "Proceed to the drawing room"
  TARGET: harding_house_drawing_room
  STATE_CHANGE: stress = +2
  CONDITION: null

::SCENE::
LOCATION: Harding House. Rear Drawing Room
MOOD: Tense
CHARACTERS: Narrator, Harding, Sievers
BACKGROUND_IMAGE: harding_house_drawing_room.png
BACKGROUND_EDIT: "Nighttime, dimly lit drawing room, Harding by billiard table"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Harding is crouched by his billiard table. He listlessly rolls the balls around, distracted. Tired. Very tired.
  EXPRESSION: null
- CHARACTER: Harding
  LINE: These hysterical spells come over her at nightfall, like clockwork. Cigar?
  EXPRESSION: Weary
- CHARACTER: Narrator
  LINE: He lights one to ease his stress.
  EXPRESSION: null
- CHARACTER: Sievers
  LINE: Thank you.
  EXPRESSION: Polite refusal
- CHARACTER: Narrator
  LINE: Sievers takes a pinch of snuff. His eyes teem with concern.
  EXPRESSION: null
- CHARACTER: Sievers
  LINE: I... I lament to tell you this... Hutter’s employer, Herr Knock, he... he was admitted to the hospital this morning.
  EXPRESSION: Grave
- CHARACTER: Narrator
  LINE: Harding looks up quickly.
  EXPRESSION: null
- CHARACTER: Harding
  LINE: What? Did you speak to him of Thomas?
  EXPRESSION: Anxious
- CHARACTER: Sievers
  LINE: He’s mad.
  EXPRESSION: Grim
- CHARACTER: Harding
  LINE: Mad?
  EXPRESSION: Disbelieving
- CHARACTER: Sievers
  LINE: Non compos mentis. And Friedrich, he... well, the wretched fellow – while inflamed with some sort of religious mania – he shares a similar motto to Frau Hutter: “He is coming.”
  EXPRESSION: Concerned
- CHARACTER: Harding
  LINE: What?
  EXPRESSION: Shocked
- CHARACTER: Sievers
  LINE: Whic
  EXPRESSION: Hesitant

::PATHS::
- CHOICE: "Inquire further about Knock's state"
  TARGET: end
  STATE_CHANGE: dread = +3
  CONDITION: null

::SCENE::
LOCATION: Bukovina River Bank
MOOD: Desperate
CHARACTERS: Narrator, Thomas, Novice
BACKGROUND_IMAGE: river_bank_dusk.png
BACKGROUND_EDIT: "Dusk, twisted body washed ashore"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Thomas is alive - barely. His body is washed up on shore in a twisted heap.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: An young Orthodox nun, a Novice, is collecting firewood, and has a large bundle of branches on her back. She takes a step. She gasps as she sees Thomas.
  EXPRESSION: null

::PATHS::
- CHOICE: "Observe the scene"
  TARGET: orthodox_monastery_night
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Orthodox Monastery
MOOD: Solemn, Pained
CHARACTERS: Narrator, Thomas, Orthodox Nuns, Priest
BACKGROUND_IMAGE: monastery_interior_night.png
BACKGROUND_EDIT: "Night, body carried by nuns, monastery walls covered in frescos, illuminated by candles"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Thomas' limp body is carried by dozens of Orthodox Nuns in their strange black habits. He shivers uncontrollably.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Women’s hands of all ages pass over his body. They walk him through monastery, every inch covered in frescos of saints, illuminated by hundreds of candles. The Nuns pray and pray. He breathes heavily, pained.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: They see his vampire bite. Their praying grows louder.
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue observing"
  TARGET: harding_house_drawing_room
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Harding House. Rear Drawing Room
MOOD: Urgent, Horrified
CHARACTERS: Narrator, Sievers, Harding
BACKGROUND_IMAGE: harding_house_drawing_room_night.png
BACKGROUND_EDIT: "Night, drawing room"

::SCRIPT::
- CHARACTER: Sievers
  LINE: A man by the name of Franz. Swiss.
  EXPRESSION: null
- CHARACTER: Harding
  LINE: Swiss?
  EXPRESSION: Horrified
- CHARACTER: Sievers
  LINE: Professor Albin Eberhart von Franz. He is the sole person who might be able to diagnose her. An eminent physician and scholar in Zürich, when I was at school. My finest teacher.
  EXPRESSION: null
- CHARACTER: Harding
  LINE: Send a message to Zürich then.
  EXPRESSION: null
- CHARACTER: Sievers
  LINE: No. He is here. In Wisburg.
  EXPRESSION: null
- CHARACTER: Harding
  LINE: Here? Here? Why haven’t you told me, man?
  EXPRESSION: Astonished
- CHARACTER: Sievers
  LINE: Well, you see, he... von Franz is the most learned in the field... his mind... staggering–
  EXPRESSION: null
- CHARACTER: Harding
  LINE: I’ll spare no expense.
  EXPRESSION: Determined
- CHARACTER: Sievers
  LINE: No, you misunderstand me, Friedrich. It falls hard on me to recommend him... He was tossed out of the university – laughed out of his home country.
  EXPRESSION: Reluctant
- CHARACTER: Harding
  LINE: What?
  EXPRESSION: Shocked
- CHARACTER: Sievers
  LINE: It grieves me to speak it, but he became obsessed with the work of Paracelsus, Agrippa, and the like.
  EXPRESSION: Sad
- CHARACTER: Harding
  LINE: I’m a ship-man, Sievers.
  EXPRESSION: Confused
- CHARACTER: Sievers
  LINE: Alchemy, mystic philosophy... the occult.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: This chills Harding.
  EXPRESSION: Chilled

::PATHS::
- CHOICE: "Continue the conversation"
  TARGET: orthodox_monastery_chapel
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Orthodox Monastery Chapel
MOOD: Agonizing, Spiritual
CHARACTERS: Narrator, Thomas, Nuns, Priest, Schema Abbess
BACKGROUND_IMAGE: monastery_chapel_later.png
BACKGROUND_EDIT: "Later, Thomas on a table, sweating, trembling, nuns praying, priest dousing with holy water"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Thomas lies on a table, shirtless and profusely sweating. He trembles in agony. Nuns pray. An aged Priest incants prayers and douses him with holy water.
  EXPRESSION: null

::SCENE::
LOCATION: Orthodox Monastery Chapel
MOOD: Exorcising, Terrifying
CHARACTERS: Narrator, Thomas, Nuns, Priest, Schema Abbess
BACKGROUND_IMAGE: monastery_chapel_later_icon.png
BACKGROUND_EDIT: "Later, icon placed on Thomas's chest, nuns praying, Schema Abbess clutching a cross"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Thomas has an icon placed on his chest. Nuns pray around him, with a tiny Schema Abbess(90s) clutching a cross in her wrinkled fist.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The Priest continues exorcizing the sickness away. He presses her hands firmly on his head: in Old Church Slavonic he prays with the might of Christ resurrecting Lazarus...
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Suddenly, Thomas inhales... his eyes open wide:
  EXPRESSION: null
- CHARACTER: Thomas
  LINE: No! Orlok! No!!
  EXPRESSION: Terrified
- CHARACTER: Narrator
  LINE: He rises from the bed, drenched in sweat, icon slipping. At the name “Orlok,” the Abbess is seized with terror.
  EXPRESSION: null

::PATHS::
- CHOICE: "Witness the reaction"
  TARGET: monastery_cell
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Monastery Cell
MOOD: Revealing, Determined
CHARACTERS: Narrator, Thomas, Old Schema Abbess, Novice
BACKGROUND_IMAGE: monastery_cell_later.png
BACKGROUND_EDIT: "Later, Thomas swaddled in blankets, listening intently, shaking. Old Schema Abbess speaking."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Thomas is swaddled in blankets, listening intently, still shaking. The Old Schema Abbess speaks to him in Romanian. A young Novice translates for her:
  EXPRESSION: null
- CHARACTER: Novice
  LINE: A black enchanter he was in life. Şolomanari. The Devil preserved his soul that his corpse may walk again in blaspheme.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The Abbess continues, she gesticulates with fervour.
  EXPRESSION: null
- CHARACTER: Novice
  LINE: You are lost in his shadow.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Thomas breaks down into tears. He shouts with determination:
  EXPRESSION: null
- CHARACTER: Thomas
  LINE: No!
  EXPRESSION: Determined
- CHARACTER: Novice
  LINE: Enchanters turn their spirit into shadow to infect your dreams.
  EXPRESSION: null
- CHARACTER: Thomas
  LINE: I must leave! I... I promised Ellen.
  EXPRESSION: Determined
- CHARACTER: Novice
  LINE: Remain here. His evil cannot enter this house of God.
  EXPRESSION: Reassuring
- CHARACTER: Thomas
  LINE: I promised I’d join the firm... I came here to sell the count a home in Wisburg.
  EXPRESSION: Determined
- CHARACTER: Novice
  LINE: Rest! Become well!
  EXPRESSION: Gentle
- CHARACTER: Thomas
  LINE: He is bound for Wisburg!
  EXPRESSION: Determined
- CHARACTER: Novice
  LINE: He cannot leave – he must return to the cursèd earth wherein he was buried.
  EXPRESSION: Firm
- CHARACTER: Thomas
  LINE: No! He seeks after Ellen. I know it!
  EXPRESSION: Determined

::PATHS::
- CHOICE: "Observe the conflict"
  TARGET: black_sea_dawn
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Black Sea
MOOD: Foreboding
CHARACTERS: Narrator
BACKGROUND_IMAGE: black_sea_dawn.png
BACKGROUND_EDIT: "Dawn, waves crashing against a schooner"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Waves crash against The Empusa, a small topsail schooner, its sails full of wind.
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue to the cargo hold"
  TARGET: empusa_cargo_hold_dawn
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Empusa. Cargo Hold
MOOD: Menacing
CHARACTERS: Narrator
BACKGROUND_IMAGE: empusa_cargo_hold_dawn.png
BACKGROUND_EDIT: "Dawn, coffin-shaped crate in the ship's bowels, sealed with a sigil"

::SCRIPT::
- CHARACTER: Narrator
  LINE: A large, coffin-shaped wooden crate sit menacingly in the creaking bowels of the ship. It is strapped with ropes and canvas and sealed with The Orlok Sigil.
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue to the hospital"
  TARGET: hospital_knocks_cell
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Hospital. Knock’s Cell
MOOD: Torturous, Obsessive
CHARACTERS: Narrator, Knock
BACKGROUND_IMAGE: hospital_knocks_cell_day.png
BACKGROUND_EDIT: "Day, Knock's hair shorn, strapped in a chair, vice on his head, chamber pot attached"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Knock’s hair has been crudely shorn. He is strapped into a chair that looks like a torture device. His trousers are removed. There is a chamber pot attached to the bottom of the seat. His head is held up vertically with a metal vice. He laughs. With every laugh he is caused great pain by the vice.
  EXPRESSION: null
- CHARACTER: Knock
  LINE: Your Lordship cometh! Sew thy pestilence within them, reap their blood, yet spare me! Bestow thy secret art upon me, and I shall serve by thy side! I have not failed your Lordship... thy promised gift awaits!
  EXPRESSION: Manic
- CHARACTER: Narrator
  LINE: He shakes. The straps and buckles pressing into his flesh – the metal vice fighting against his every movement.
  EXPRESSION: null
- CHARACTER: Knock
  LINE: Providence! Providence!
  EXPRESSION: Manic (Laughing)

::PATHS::
- CHOICE: "Move to the next scene"
  TARGET: harding_house_guest_room
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Harding House. Guest Room
MOOD: Eerie, Possessive
CHARACTERS: Narrator, Ellen, Orlok (V.O.)
BACKGROUND_IMAGE: harding_house_guest_room_night.png
BACKGROUND_EDIT: "Night, Ellen in the dark, hearing Orlok's whisper"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Ellen stands in the dark. She hears Orlok’s whisper.
  EXPRESSION: null
- CHARACTER: Orlok (V.O.)
  LINE: Soon I will be no more a shadow to you. Your spirit was never enough. Soon our flesh shall embrace and we shall be as one.
  EXPRESSION: Possessive (Subtitled)

::PATHS::
- CHOICE: "Enter the coffin"
  TARGET: empusa_cargo_hold_coffin
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Empusa. Cargo Hold. Coffin
MOOD: Incantatory, Powerful
CHARACTERS: Narrator, Orlok (V.O.)
BACKGROUND_IMAGE: empusa_cargo_hold_coffin.png
BACKGROUND_EDIT: "The next moment, camera pushes into Orlok incanting telepathically, buried within his earth-filled coffin"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Camera pushes into Orlok incanting telepathically, buried within his earth-filled coffin.
  EXPRESSION: null
- CHARACTER: Orlok (V.O.)
  LINE: Nature, I call unto thee, increase thy thunders...
  EXPRESSION: Incantatory (Subtitled)

AUDIO: The wind blows. Waves crash.

::PATHS::
- CHOICE: "Continue to the sea"
  TARGET: black_sea_night
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Black Sea
MOOD: Swift, Powerful
CHARACTERS: Narrator, Orlok (V.O.)
BACKGROUND_IMAGE: black_sea_night.png
BACKGROUND_EDIT: "Night, the sea rushes by camera at great speed"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Angle on: The sea rushes by camera at great speed.
  EXPRESSION: null
- CHARACTER: Orlok (V.O.)
  LINE: And hasten me upon the wings of thy barbarous winds.
  EXPRESSION: Powerful (Subtitled)

::PATHS::
- CHOICE: "Move to Wisburg"
  TARGET: wisburg_street_slums
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Wisburg Street. Slums
MOOD: Grimy, Skeptical
CHARACTERS: Narrator, Sievers, Harding, Drunkard
BACKGROUND_IMAGE: wisburg_street_slums_night.png
BACKGROUND_EDIT: "Night, frosty, dogs barking, vagrants, garbage"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Sievers and Harding walk in the frosty night. Dogs barking. Vagrants. Garbage.
  EXPRESSION: null
- CHARACTER: Sievers
  LINE: The scientific community is on a crusade to prove his work drove him to madness.
  EXPRESSION: null
- CHARACTER: Harding
  LINE: I am responsible for Thomas’s wife–
  EXPRESSION: Concerned
- CHARACTER: Narrator
  LINE: Harding bumps into a Drunkard urinating in the street, who curses him:
  EXPRESSION: null
- CHARACTER: Drunkard
  LINE: Bleedin’ dandy bum-boy!
  EXPRESSION: Aggressive
- CHARACTER: Sievers
  LINE: But it’s a sham. A sham. I assure you, Harding, he may be a bit... unconventional, but he will know the cause.
  EXPRESSION: Assured

::PATHS::
- CHOICE: "Omit"
  TARGET: omitted
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Boarding House Hallway
MOOD: Tense, Hesitant
CHARACTERS: Narrator, Sievers, Harding, Von Franz (O.S.)
BACKGROUND_IMAGE: boarding_house_hallway_night.png
BACKGROUND_EDIT: "Night, cramped hallway, attic door, sooty sconces"

::SCRIPT::
- CHARACTER: Narrator
  LINE: They stand cramped in front of an attic door. Sievers knocks with his walking stick.
  EXPRESSION: null
- CHARACTER: Sievers
  LINE: Professor von Franz?
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: No response. Sooty sconces drip wax down the buckling wall. Harding looks all the more unsure.
  EXPRESSION: null
- CHARACTER: Sievers
  LINE: Sievers knocks again. A weak, aged voice answers:
  EXPRESSION: null
- CHARACTER: Von Franz (O.S.)
  LINE: Leave me be.
  EXPRESSION: Weak
- CHARACTER: Sievers
  LINE: It is your former student–
  EXPRESSION: null
- CHARACTER: Von Franz (O.S.)
  LINE: Avaunt! Be gone I say!
  EXPRESSION: Booming
- CHARACTER: Narrator
  LINE: Sievers tries the handle. It’s unlocked. He opens it...
  EXPRESSION: null

::SCENE::
LOCATION: Von Franz’s Attic
MOOD: Chaotic, Astounding
CHARACTERS: Narrator, Sievers, Harding
BACKGROUND_IMAGE: von_franz_attic_continuous.png
BACKGROUND_EDIT: "Continuous, Von Franz's attic flat is an absolute catastrophe, piles of books everywhere"

::SCRIPT::
- CHARACTER: Sievers
  LINE: Please, Professor...
  EXPRESSION: Pleading
- CHARACTER: Narrator
  LINE: Harding and Sievers are aghast. Von Franz’s attic flat is an absolute catastrophe. Piles of books everywhere
  EXPRESSION: Aghast

::PATHS::
- CHOICE: "Enter the attic"
  TARGET: end
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Professor Von Franz's Study
MOOD: Chaotic, Eerie
CHARACTERS: Narrator, Von Franz, Sievers, Harding
BACKGROUND_IMAGE: von_franz_study.png
BACKGROUND_EDIT: "A cluttered study, filled with occult curiosities, dusty books, and china. Stray cats are present."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Holding up broken chairs, cabinets of occult curiosities, esoteric charts, and every surface is covered in old china, crumbs, and dust. Dust, dust, and more dust. Several stray cats prowl about, lapping up remnants from the china.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: A muttering is heard... it is VON FRANZ. He sits smoking his pipe. Several giant books on his lap. He wears an oriental robe and slippers. His disheveled hair is long. His white moustaches are upturned – yellowed from his incessant smoking. He holds his large signet ring like an amulet. He seems hypnotised, or mad. Or maybe just very old.
  EXPRESSION: null
- CHARACTER: Von Franz
  LINE: I had nearly unlocked the final key of the Mysteriorum Libri Quinque.
  EXPRESSION: Musing
- CHARACTER: Sievers
  LINE: I am sorry Professor, I...
  EXPRESSION: Apologetic
- CHARACTER: Von Franz
  LINE: No... No matter. I miscalculated the stars. Hermes will not render my black sulfur gold this evening.
  EXPRESSION: Resigned
- CHARACTER: Narrator
  LINE: He crosses himself and continues mumbling, rubbing his ring.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: HARDING is uncomfortable, he clearly thinks the old man is mad.
  EXPRESSION: Uneasy
- CHARACTER: Harding
  LINE: Yes, we shan’t trouble you further, we must take our leave.
  EXPRESSION: Polite
- CHARACTER: Narrator
  LINE: SIEVERS walks toward VON FRANZ.
  EXPRESSION: null
- CHARACTER: Sievers
  LINE: Good night, Professor.
  EXPRESSION: Respectful
- CHARACTER: Narrator
  LINE: SIEVERS puts his hand on VON FRANZ’s hand.
  EXPRESSION: null
- CHARACTER: Sievers
  LINE: Nolite dare sanctum canibus. (Subtitle: Do not reveal what is sacred to dogs)
  EXPRESSION: Solemn
- CHARACTER: Narrator
  LINE: Something clicks. VON FRANZ hears the doctor’s words. He holds up his quizzing-glass and sees SIEVERS through the lens. His eyes sparkle in the candlelight – nearly as intense as Orlok’s. He laughs heartily. He has come alive!
  EXPRESSION: null
- CHARACTER: Von Franz (O.S.)
  LINE: Neque mittatis margaritas vestra ante porcos! (Subtitle: Nor cast your pearls before swine)
  EXPRESSION: Joyful
- CHARACTER: Von Franz
  LINE: My dear young Sievers, or do my dying eyes deceive me? I should have known!
  EXPRESSION: Excited
- CHARACTER: Narrator
  LINE: VON FRANZ stands, laughing, his books falling to the floor.
  EXPRESSION: null
- CHARACTER: Von Franz
  LINE: Embrace me, my boy! I am so rejoiced to see you.
  EXPRESSION: Elated
- CHARACTER: Narrator
  LINE: As they hug, clouds of dust fly off of VON FRANZ’S clothing.
  EXPRESSION: null
- CHARACTER: Von Franz
  LINE: I sensed something... It took me to Wisburg all these years ago, and I had felt that now it was imminently approaching. I thought it ill, but it must have been you! Now, what is the matter?
  EXPRESSION: Enthusiastic
- CHARACTER: Narrator
  LINE: He looks at HARDING’S bewildered face.
  EXPRESSION: null
- CHARACTER: Von Franz
  LINE: Ah, I see, yes. Your friend’s dear wife: a morbid melancholic exhibiting acute hysteria manifested in protracted fits of somnambulism.
  EXPRESSION: Insightful
- CHARACTER: Narrator
  LINE: SIEVERS is triumphant. HARDING is in disbelief.
  EXPRESSION: null
- CHARACTER: Von Franz
  LINE: You look tired, young man.
  EXPRESSION: Observant
- CHARACTER: Narrator
  LINE: VON FRANZ dumps out a few china cups into a basin. He pulls out a bottle:
  EXPRESSION: null
- CHARACTER: Von Franz
  LINE: Schnapps?
  EXPRESSION: Hospitable

::SCENE::
LOCATION: Orthodox Monastery. Stables - Dawn
MOOD: Determined, Somber
CHARACTERS: Narrator, Thomas, The Old Abbess, Nuns
BACKGROUND_IMAGE: monastery_stables_dawn.png
BACKGROUND_EDIT: "Snowy landscape, dawn light, horses"

::SCRIPT::
- CHARACTER: Narrator
  LINE: THOMAS gallops away on a horse. He wears a borrowed shearling coat and looks like a shell of his former self. But his eyes shine with resolve.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: THE OLD ABBESS runs out of THE MONASTERY, several nuns behind her.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: THOMAS rides off into the snowy dawn.
  EXPRESSION: null

::SCENE::
LOCATION: Empusa. Cargo Hold - Morning
MOOD: Tense, Horrifying
CHARACTERS: Narrator, Captain Yusov, First Mate, Sailor, Cabin Boy, Deck Hands, Rats
BACKGROUND_IMAGE: empusa_cargo_hold.png
BACKGROUND_EDIT: "Dark ship cargo hold, morning light filtering in"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Several DECK HANDS are searching the dark hold for something.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: A rugged CAPTAIN descends from the hatch.
  EXPRESSION: null
- CHARACTER: Captain Yusov
  LINE: Back to the quarterdeck with you!
  EXPRESSION: Gruff
- CHARACTER: First Mate
  LINE: But Vasilyev’s still missing. And now Redenko.
  EXPRESSION: Worried
- CHARACTER: Narrator
  LINE: Suddenly they hear a thud – they dash toward the sound: A burly SAILOR is convulsing on the floor of the hold, entwined in rope. He has small red wounds all over his flesh. He coughs, vomiting up blood and bile – extreme haemorrhaging.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: THE CABIN BOY is dead by his side. The DECK HANDS back away from the sight as several rats scuttle from the bodies. The sailor screams, choking on his blood.
  EXPRESSION: null

::SCENE::
LOCATION: Harding House. Guest Room - Day
MOOD: Concerned, Hopeful
CHARACTERS: Narrator, Harding, Anna, Sievers, Von Franz, Ellen, Greta
BACKGROUND_IMAGE: harding_house_guest_room.png
BACKGROUND_EDIT: "A sickroom, sparse but for a bed and plants. Ellen is tied to the bed."

::SCRIPT::
- CHARACTER: Narrator
  LINE: HARDING and ANNA escort SIEVERS and VON FRANZ to Ellen’s room. Von Franz is shocked.
  EXPRESSION: null
- CHARACTER: Von Franz
  LINE: Untie this child at once!
  EXPRESSION: Authoritative
- CHARACTER: Narrator
  LINE: ELLEN IS TIED DOWN TO THE BED. She is pale, damp, exhausted. Her eyes are red. Her bedclothes saturated with perspiration. The chamber has been turned to a sickroom, all the luxuries gone. Only a bed, a chair, a chamber pot and pail, and a few plants in the window remain. GRETA, the cat, however, is with her.
  EXPRESSION: null
- CHARACTER: Harding
  LINE: It is all I could do to keep her from tearing the room to ribbons. She -
  EXPRESSION: Distressed
- CHARACTER: Von Franz
  LINE: Untie her!
  EXPRESSION: Urgent
- CHARACTER: Narrator
  LINE: SIEVERS unties her with VON FRANZ. HARDING assists, in shame.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: ELLEN sees VON FRANZ and looks at him with hope. She smiles, but her voice is very strained.
  EXPRESSION: null
- CHARACTER: Ellen
  LINE: You are the doctor our Sievers spoke of?
  EXPRESSION: Hopeful
- CHARACTER: Von Franz
  LINE: Drugged?
  EXPRESSION: Questioning
- CHARACTER: Sievers
  LINE: I have been administering an opiate. She must rest by day, for her body is in utter stress all the night.
  EXPRESSION: Explanatory
- CHARACTER: Von Franz
  LINE: She cannot be clouded. Step away. Step away!
  EXPRESSION: Firm
- CHARACTER: Narrator
  LINE: VON FRANZ sits beside the bed.
  EXPRESSION: null
- CHARACTER: Von Franz
  LINE: My dear creature, yes, I am he, and I am hither come to help you.
  EXPRESSION: Reassuring
- CHARACTER: Narrator
  LINE: ELLEN, now unrestrained, holds GRETA tight.
  EXPRESSION: null
- CHARACTER: Von Franz
  LINE: Is she yours?
  EXPRESSION: Curious
- CHARACTER: Ellen
  LINE: Greta? She has no master nor mistress.
  EXPRESSION: Amused
- CHARACTER: Von Franz
  LINE: Quite so.
  EXPRESSION: Understanding
- CHARACTER: Narrator
  LINE: He pets GRETA, and takes something from his pocket to feed her.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: VON FRANZ looks at ELLEN in the eye.
  EXPRESSION: null
- CHARACTER: Von Franz
  LINE: I entreat you to excuse me, but I should like to begin my consultation presently. You see, I have a curiosity about you – Dr. Sievers tells me you have had these spells since childhood?
  EXPRESSION: Inquisitive
- CHARACTER: Narrator
  LINE: ELLEN nods yes.
  EXPRESSION: null
- CHARACTER: Von Franz
  LINE: Would you describe them to me?
  EXPRESSION: Gentle
- CHARACTER: Ellen
  LINE: I cannot always remember them. As if my spirit wanders off.
  EXPRESSION: Hesitant
- CHARACTER: Von Franz
  LINE: Tell me what you can. From the beginning.
  EXPRESSION: Encouraging
- CHARACTER: Narrator
  LINE: While her voice is weak, she speaks with ease, without shame.
  EXPRESSION: null
- CHARACTER: Ellen
  LINE: Sometimes it was... it is like a dream. And I know things. I always knew the contents of my Christmas gifts. I knew when... that my mother would pass. Father... he would find me in our fields... within the forest... as if – I was his little changeling girl.
  EXPRESSION: Reflective
- CHARACTER: Von Franz
  LINE: I see.
  EXPRESSION: Attentive
- CHARACTER: Narrator
  LINE: ELLEN grows uneasy.
  EXPRESSION: null
- CHARACTER: Ellen
  LINE: But as I became older it worsened... Father dispraised me for it... I frightened him. My touch. I was so very alone, you see and... I wished for comfort... then a presence... and the nightmares, the epilepsies... I...
  EXPRESSION: Vulnerable
- CHARACTER: Von Franz
  LINE: Pray, continue.
  EXPRESSION: Patient
- CHARACTER: Narrator
  LINE: ELLEN sees the story vividly. Reexperiencing the emotions.
  EXPRESSION: null
- CHARACTER: Ellen
  LINE: At last Papa found me once laying... unclothed, I was... my body... my flesh... my...
  EXPRESSION: Distressed
- CHARACTER: Narrator
  LINE: Intense sexual implications are clear in her tone. Everyone is embarrassed, except for VON FRANZ.
  EXPRESSION: null
- CHARACTER: Ellen
  LINE: Sin, sin, he said... He would have sent me to someplace... I shan’t go... I –
  EXPRESSION: Desperate
- CHARACTER: Von Franz
  LINE: No, no.
  EXPRESSION: Soothing
- CHARACTER: Ellen
  LINE: It all ended when first I met my Thomas.
  EXPRESSION: Relieved
- CHARACTER: Von Franz
  LINE: Your husband?
  EXPRESSION: Inquiring
- CHARACTER: Ellen
  LINE: From our love, I became as normal.
  EXPRESSION: Serene

::PATHS::
- CHOICE: "Continue consultation"
  TARGET: ellen_consultation_2
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Unknown
MOOD: Questioning, Fear
CHARACTERS: Narrator, Ellen, Von Franz
BACKGROUND_IMAGE: null
BACKGROUND_EDIT: "Dark, intimate setting"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Yet these visions and night wanderings have returned to you?
  EXPRESSION: null
- CHARACTER: Ellen
  LINE: He left on a fool’s errand. I fear for him so.
  EXPRESSION: Worried
- CHARACTER: Narrator
  LINE: Ellen leans closer to Von Franz with intensity.
  EXPRESSION: null
- CHARACTER: Ellen
  LINE: Professor... My dreams grow darker, they sicken me. Does evil come from within us or from beyond?
  EXPRESSION: Intense, Sickened

::SCENE::
LOCATION: EMPUSA. DECK
MOOD: Violent, Grim
CHARACTERS: Narrator, The First Mate, Captain Yusov, Deck Hand 2
BACKGROUND_IMAGE: empusa_deck.png
BACKGROUND_EDIT: "Night, violent gale, freezing rain, sleet"

::SCRIPT::
- CHARACTER: Narrator
  LINE: A violent gale has begun. Freezing rain. Sleet.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: A corpse in a canvas body bag is dropped into the sea. Waves crash.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The First Mate, Captain Yusov, and Deck Hand 2 stand by, shivering in their icy oilskins. They cross themselves.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The First Mate fills with rage. He whispers to himself:
  EXPRESSION: null
- CHARACTER: First Mate
  LINE: (Russian, Subtitled) I will end this plague. This devil.
  EXPRESSION: Furious
- CHARACTER: Narrator
  LINE: He looks out at the hellish moonrise and lifts a boarding axe with determination!
  EXPRESSION: null

::SCENE::
LOCATION: HARDING HOUSE. GUEST ROOM
MOOD: Tense, Medical, Supernatural
CHARACTERS: Narrator, Von Franz, Sievers, Ellen
BACKGROUND_IMAGE: harding_house_guest_room.png
BACKGROUND_EDIT: "Night, room is quite dark"

::SCRIPT::
- CHARACTER: Von Franz
  LINE: Her trance state is begun.
  EXPRESSION: Observant
- CHARACTER: Narrator
  LINE: It has. A quick breath parts her lips. Von Franz presses on her body very hard... Her wrists, her neck...
  EXPRESSION: null
- CHARACTER: Von Franz
  LINE: You have bled her to decrease the congestion.
  EXPRESSION: Professional
- CHARACTER: Sievers
  LINE: Of course.
  EXPRESSION: Affirmative
- CHARACTER: Narrator
  LINE: He lifts up her chemise and presses on her womb...
  EXPRESSION: null
- CHARACTER: Von Franz
  LINE: And her menstruations are also?
  EXPRESSION: Inquisitive
- CHARACTER: Sievers
  LINE: Liberal.
  EXPRESSION: Factual
- CHARACTER: Narrator
  LINE: Ellen’s breathing increases...
  EXPRESSION: null
- CHARACTER: Von Franz
  LINE: Too much blood. Too much. (to Sievers) A taper, please.
  EXPRESSION: Concerned
- CHARACTER: Narrator
  LINE: Sievers lights a candle.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Von Franz holds it near Ellen’s eyes, peering through his quizzing-glass.
  EXPRESSION: null
- CHARACTER: Von Franz
  LINE: The pupil is expanded. It does not contract naturally to light.
  EXPRESSION: Astonished
- CHARACTER: Sievers
  LINE: Impossible.
  EXPRESSION: Disbelieving
- CHARACTER: Von Franz
  LINE: A second sight. She is no longer here. My bag...
  EXPRESSION: Certain
- CHARACTER: Narrator
  LINE: Von Franz takes out a long needle.
  EXPRESSION: null
- CHARACTER: Von Franz
  LINE: Forgive the grotesque tediousness of this demonstration, however, I must impress upon you that this child is not with us.
  EXPRESSION: Serious
- CHARACTER: Narrator
  LINE: Von Franz draws the needle through the flame, then inserts it into Ellen’s delicate wrist – through her flesh and out the other side. Ellen does not react at all.
  EXPRESSION: null
- CHARACTER: Von Franz
  LINE: Restrain your protestations, for she feels nothing. She communes now with another realm.
  EXPRESSION: Authoritative
- CHARACTER: Narrator
  LINE: He removes the needle.
  EXPRESSION: null
- CHARACTER: Von Franz
  LINE: Sievers, bind the wound.
  EXPRESSION: Directive
- CHARACTER: Narrator
  LINE: Von Franz places his palm on Ellen’s forehead.
  EXPRESSION: null
- CHARACTER: Von Franz
  LINE: (to Ellen) Now, do you hear me my child?
  EXPRESSION: Commanding
- CHARACTER: Narrator
  LINE: She shakes her head “yes.”
  EXPRESSION: null
- CHARACTER: Von Franz
  LINE: What then do you see?
  EXPRESSION: Demanding
- CHARACTER: Ellen
  LINE: I... I...
  EXPRESSION: Hesitant
- CHARACTER: Von Franz
  LINE: I charge you, speak now what you see.
  EXPRESSION: Forceful
- CHARACTER: Ellen
  LINE: Enduring night... a spectre of death... He... he... spreads his shadow... and... and... he is coming–
  EXPRESSION: Terrified
- CHARACTER: Von Franz
  LINE: Who, who is coming to you my child?
  EXPRESSION: Impatient
- CHARACTER: Ellen
  LINE: ...
  EXPRESSION: Mute
- CHARACTER: Von Franz
  LINE: Who?!
  EXPRESSION: Demanding
- CHARACTER: Narrator
  LINE: Her muscles tense... Her breathing becomes rapid.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Von Franz removes his ring and places it on her forehead. He holds it there and presses on it.
  EXPRESSION: null
- CHARACTER: Von Franz
  LINE: Who, damn you!? Speak!!
  EXPRESSION: Enraged
- CHARACTER: Anna
  LINE: (overlapping) Please, Professor!
  EXPRESSION: Pleading
- CHARACTER: Von Franz
  LINE: I will not harm her!
  EXPRESSION: Defensive
- CHARACTER: Narrator
  LINE: Her fit builds. Her body contorts... her voice stifled...
  EXPRESSION: null
- CHARACTER: Von Franz
  LINE: I command you, hearken to my voice. By the protection of Chamuel, Haniel, and Zadkiel, impart your speech unto me. In the name of Eligos, Orabas, and Asmoday, impart your speech unto me!
  EXPRESSION: Incantatory
- CHARACTER: Narrator
  LINE: She speaks as if her voice were trying to free itself from hell:
  EXPRESSION: null
- CHARACTER: Ellen
  LINE: I shall persist to join you every night, first in sleep, then in your arms. Everything will be mixed with abomination, and you'll be knee-deep in blood. Everyone will cry. There will be none to bury the dead.
  EXPRESSION: Tormented
- CHARACTER: Narrator
  LINE: Von Franz grabs her shoulders... Her fit worsens...
  EXPRESSION: null
- CHARACTER: Ellen
  LINE: You... are... promised... to... me.
  EXPRESSION: Possessive
- CHARACTER: Von Franz
  LINE: Promised? Promised?!
  EXPRESSION: Shocked
- CHARACTER: Anna
  LINE: (overlapping) She means her husband!
  EXPRESSION: Clarifying
- CHARACTER: Narrator
  LINE: Ellen tries to break from her fit, screaming:
  EXPRESSION: null
- CHARACTER: Ellen
  LINE: Help me! Help me!
  EXPRESSION: Desperate
- CHARACTER: Narrator
  LINE: She holds Von Franz’s lapels, tight... She clenches her fists harder... harder... tearing the buttons off of his jacket... screaming...
  EXPRESSION: null
- CHARACTER: Ellen
  LINE: HELP ME!!!!
  EXPRESSION: Screaming

::SCENE::
LOCATION: HARDING HOUSE. FRONT DRAWING ROOM
MOOD: Horrified, Ominous
CHARACTERS: Narrator, Von Franz, Harding, Anna, Sievers, Ellen
BACKGROUND_IMAGE: harding_house_drawing_room.png
BACKGROUND_EDIT: "Later, dimly lit room with a Christmas tree"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Von Franz indiscreetly lights his pipe on one of the many candles perched on the Christmas tree’s branches.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Everyone else stands or sits, horrified from the last scene.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Ellen’s screaming is heard from upstairs.
  EXPRESSION: null
- CHARACTER: Von Franz
  LINE: As I feared.
  EXPRESSION: Grim
- CHARACTER: Narrator
  LINE: Long pause.
  EXPRESSION: null
- CHARACTER: Harding
  LINE: Well?
  EXPRESSION: Impatient
- CHARACTER: Von Franz
  LINE: Well what, my boy? Cannot you see?
  EXPRESSION: Sarcastic
- CHARACTER: Harding
  LINE: See what?
  EXPRESSION: Confused
- CHARACTER: Von Franz
  LINE: See that she is cursed.
  EXPRESSION: Certain
- CHARACTER: Harding
  LINE: Cursed?
  EXPRESSION: Astonished
- CHARACTER: Von Franz
  LINE: Yes, cursed. The dear young creature is obsessed of some spirit... perhaps some daemon.
  EXPRESSION: Serious
- CHARACTER: Harding
  LINE: I beg your pardon?
  EXPRESSION: Disbelieving
- CHARACTER: Sievers
  LINE: I assure you, Harding, the good professor means this as hyperbole.
  EXPRESSION: Reassuring
- CHARACTER: Von Franz
  LINE: No, I mean a daemon.
  EXPRESSION: Adamant
- CHARACTER: Harding
  LINE: You jest–
  EXPRESSION: Skeptical
- CHARACTER: Sievers
  LINE: What of your discovery of macabre hallucination pathologies –
  EXPRESSION: Suggestive
- CHARACTER: Von Franz
  LINE: This is not one!
  EXPRESSION: Forceful
- CHARACTER: Harding
  LINE: You scarcely looked at her!
  EXPRESSION: Accusatory
- CHARACTER: Anna
  LINE: How should this happen to Ellen?
  EXPRESSION: Worried
- CHARACTER: Von Franz
  LINE: Daemonic spirits more easily obsess those whose lower animal functions dominate - Daemons like them, they seek them out.
  EXPRESSION: Explanatory
- CHARACTER: Anna
  LINE: How mean you?
  EXPRESSION: Confused
- CHARACTER: Von Franz
  LINE: They can discover their victims from across mountains, great oceans...
  EXPRESSION: Mysterious
- CHARACTER: Sievers
  LINE: Those with lower animal funct- ?
  EXPRESSION: Inquisitive
- CHARACTER: Von Franz
  LINE: Yes. Hysterics, children, lunatics... which reminds me - Sievers, you must introduce me to your mad man tomorrow.
  EXPRESSION: Directive
- CHARACTER: Sievers
  LINE: Yes of course, but Professor I -
  EXPRESSION: Hesitant
- CHARACTER: Von Franz
  LINE: Somnambulists afflicted with these perversions oft possess a gift: a second sight into the borderland.
  EXPRESSION: Informative
- CHARACTER: Sievers
  LINE: I do not wish to dispute you, yet, I have myself seen women of nervous constitutions invent any manor of delusion.
  EXPRESSION: Cautious
- CHARACTER: Von Franz
  LINE: This is no delusion. I believe she has always been highly conductive to these cosmic forces, uniquely so. The lunatic... perhaps.
  EXPRESSION: Certain
- CHARACTER: Narrator
  LINE: This terrifies Harding.
  EXPRESSION: null
- CHARACTER: Sievers
  LINE: Do you then acknowledge a connection between these cases?
  EXPRESSION: Questioning
- CHARACTER: Von Franz
  LINE: That is the question.
  EXPRESSION: Pensive
- CHARACTER: Von Franz
  LINE: No. This evil, what it is, how it has been summoned – unleashed – I know not. But this remarkable child it has chained itself to is in grave peril.
  EXPRESSION: Grave
- CHARACTER: Narrator
  LINE: Von Franz puts on his coat to leave.
  EXPRESSION: null
- CHARACTER: Von Franz
  LINE: I must to my studies. Frau Harding, sit with her, observe her, report her behaviour. Sievers, no more ether.
  EXPRESSION: Firm
- CHARACTER: Sievers
  LINE: She will rave all the night.
  EXPRESSION: Resigned
- CHARACTER: Von Franz
  LINE: Then rave she must! There is a dread storm rising!
  EXPRESSION: Foreboding
- CHARACTER: Narrator
  LINE: Ellen’s screaming from upstairs grows louder! Thunder claps!
  EXPRESSION: null

::SCENE::
LOCATION: EMPUSA. CARGO HOLD
MOOD: Dark, Oppressive
CHARACTERS: Narrator, The First Mate
BACKGROUND_IMAGE: empusa_cargo_hold.png
BACKGROUND_EDIT: "Continuous, dark hold, rain and sleet pouring in through open hatch"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The First Mate descends down into the dark hold...
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Rain and sleet pour in through the open hatch above ...
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The First Mate’s breathing grows louder... It grows darker with every step down the ladder ... Darker...
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: It is very hard to see. Water drips. The ship rocks, the timbers creak. He
  EXPRESSION: null

::SCENE::
LOCATION: Unknown
MOOD: Suspense
CHARACTERS: First Mate, Narrator, Rats, Tall Thin Figure, Orlok
BACKGROUND_IMAGE: unknown_location.png
BACKGROUND_EDIT: "Dimly lit space, focus on a crate, rats present"

::SCRIPT::
- CHARACTER: Narrator
  LINE: breathes, afraid, but fierce. His breath turns to steam in the lamp light. He holds his AXE firm...
  EXPRESSION: Afraid but determined
- CHARACTER: Narrator
  LINE: He slowly approaches THE CRATE... Rats scurry... his single sailor’s earring shakes with fear.
  EXPRESSION: Nervous
- CHARACTER: Narrator
  LINE: He walks closer... Closer... Breathing... Breathing...
  EXPRESSION: Tense
- CHARACTER: Narrator
  LINE: He hacks at it! The wood splinters... RATS spew out of the crate... THE FIRST MATE doesn’t see, but in the shadows behind him, A TALL, THIN FIGURE APPROACHES...
  EXPRESSION: Startled
- CHARACTER: Narrator
  LINE: He hacks at the crate again! THE FIGURE comes closer... THE FIRST MATE has torn a large hole in the crate....
  EXPRESSION: Focused
- CHARACTER: Narrator
  LINE: He gasps to discover that INSIDE IS A COFFIN... THE FIGURE is even closer...
  EXPRESSION: Shocked
- CHARACTER: Narrator
  LINE: THE FIRST MATE leans forward toward the sarcophagus, and wedges it open with his axe... He reaches his hand inside... Only soil. He frantically searches for something... but nothing is there! He turns around in defeat...
  EXPRESSION: Desperate, then defeated
- CHARACTER: Narrator
  LINE: SUDDENLY, ORLOK STANDS BEFORE HIM, A NAKED, ROTTEN CORPSE! HE TAKES THE FIRST MATE IN HIS ENORMOUS CLAWS, AND SINKS HIS TEETH INTO HIS BREAST! THE FIRST MATE TRIES TO SCREAM... ORLOK WRAPS AROUND HIM, SMOTHERING HIM, SUFFOCATING HIM... HE STRUGGLES TO BREAK FREE, BUT ORLOK DRAGS HIM INTO SHADOW!!
  EXPRESSION: Terrified, then consumed

::SCENE::
LOCATION: Harding House. Guest Room
MOOD: Distress
CHARACTERS: Ellen, Anna
BACKGROUND_IMAGE: harding_house_guest_room.png
BACKGROUND_EDIT: "Nighttime, Ellen in bed, distressed, Anna comforting her"

::SCRIPT::
- CHARACTER: Ellen
  LINE: Anna please... Please...
  EXPRESSION: Pleading
- CHARACTER: Narrator
  LINE: Conflicted, ANNA lets her go.
  EXPRESSION: Hesitant
- CHARACTER: Narrator
  LINE: ELLEN rises slowly, drenched in sweat... She goes to the window, her desire is intense, but she stands utterly still, looking out.
  EXPRESSION: Tormented, then still
- CHARACTER: Narrator
  LINE: ANNA follows with trepidation...
  EXPRESSION: Anxious
- CHARACTER: Narrator
  LINE: THEY STAND next to each other. They watch THE STORM RAGE. ELLEN breathes with want, fogging the warped glass of the window.
  EXPRESSION: Longing, then breathless

::SCENE::
LOCATION: Wisburg Harbour
MOOD: Ominous
CHARACTERS: Narrator, Orlok, Empusa
BACKGROUND_IMAGE: wisburg_harbour.png
BACKGROUND_EDIT: "Nighttime, city silhouetted, storm raging, sails like ghosts"

::SCRIPT::
- CHARACTER: Narrator
  LINE: WISBURG, silhouetted by the moon, lays asleep. The whole city is shut in from the storm. ORLOK’S MAGICAL INCANTATIONS ECHO IN THE WIND.
  EXPRESSION: Foreboding
- CHARACTER: Narrator
  LINE: THE EMPUSA is hurled along by the tempest toward the town. Sails billow like ghosts’ funeral shrouds. A terrible crash is imminent...
  EXPRESSION: Dire

::SCENE::
LOCATION: Hospital. Knock's Cell
MOOD: Frenzied
CHARACTERS: Knock, Night Orderly
BACKGROUND_IMAGE: hospital_cell.png
BACKGROUND_EDIT: "Nighttime, cell with restraints, rain and sleet"

::SCRIPT::
- CHARACTER: Knock
  LINE: His Lordship! He is come!
  EXPRESSION: Manic laughter
- CHARACTER: Narrator
  LINE: His screaming becomes so horrific, the NIGHT ORDERLY runs into the cell. KNOCK is completely crazed, he begins seizing... thick spittle and blood ooze from his clenched teeth.
  EXPRESSION: Hysterical, then violent
- CHARACTER: Narrator
  LINE: In a panic, THE ORDERLY blows his whistle, rapidly unbuckling KNOCK’S bonds... Just as he lets loose of the final strap, KNOCK’S eyes change... his convulsing stops. It was all an act...
  EXPRESSION: Panicked, then cunning
- CHARACTER: Narrator
  LINE: HE ATTACKS THE ORDERLY LIKE AN ANIMAL, BITING INTO HIS THROAT, BLOOD SPURTING ACROSS THE ROOM! He falls dead to the floor. KNOCK laps up the blood.
  EXPRESSION: Savage, then primal
- CHARACTER: Knock
  LINE: The blood is the life!
  EXPRESSION: Ecstatic

::SCENE::
LOCATION: Wisburg Street. Colonnade
MOOD: Demonic
CHARACTERS: Knock
BACKGROUND_IMAGE: wisburg_street.png
BACKGROUND_EDIT: "Nighttime, street, colonnade, Knock running pant-less"

::SCRIPT::
- CHARACTER: Narrator
  LINE: KNOCK runs off pant-less into the night, like a demonic ape.
  EXPRESSION: Demonic
- CHARACTER: Knock
  LINE: The blood is the life!!
  EXPRESSION: Obsessed

::SCENE::
LOCATION: Harding House. Guest Room
MOOD: Hopeful
CHARACTERS: Ellen, Anna
BACKGROUND_IMAGE: harding_house_guest_room.png
BACKGROUND_EDIT: "Nighttime, Ellen blinking, eyes filling with hope"

::SCRIPT::
- CHARACTER: Narrator
  LINE: ELLEN blinks. She breaks out of her trance. Her eyes fill with hope! She seems herself again!
  EXPRESSION: Awakened, hopeful
- CHARACTER: Narrator
  LINE: She runs out of the bedroom.
  EXPRESSION: Urgent
- CHARACTER: Anna
  LINE: Ellen!
  EXPRESSION: Surprised
- CHARACTER: Ellen
  LINE: He is here!
  EXPRESSION: Certain

::SCENE::
LOCATION: Harding House
MOOD: Dramatic Arrival
CHARACTERS: Ellen, Anna, Thomas
BACKGROUND_IMAGE: harding_house_exterior.png
BACKGROUND_EDIT: "Nighttime, icy rain, Ellen bursting outside"

::SCRIPT::
- CHARACTER: Narrator
  LINE: ELLEN bursts outside into the street, the icy rain still descending.
  EXPRESSION: Determined
- CHARACTER: Narrator
  LINE: THOMAS RIDES A HORSE THROUGH THE STORM! HE IS HERE! He is nearly horizontal. He tumbles off the saddle, dressed in strange eastern garb. He looks like hell.
  EXPRESSION: Exhausted, desperate
- CHARACTER: Thomas
  LINE: Ellen!
  EXPRESSION: Urgent plea
- CHARACTER: Narrator
  LINE: ELLEN picks him up off the street. She holds his head and kisses him all over his face. The horse continues to rear, frantically whinnying.
  EXPRESSION: Relieved, loving

::SCENE::
LOCATION: Harding House. Front Drawing Room
MOOD: Fragile Intimacy
CHARACTERS: Thomas, Ellen, Harding, Anna
BACKGROUND_IMAGE: harding_house_drawing_room.png
BACKGROUND_EDIT: "Nighttime, Thomas and Ellen on divan, wet and shivering"

::SCRIPT::
- CHARACTER: Narrator
  LINE: THOMAS AND ELLEN sit on the divan, wet and shivering. He touches ELLEN’S cheek, his voice weak, his eyes wild.
  EXPRESSION: Weak, relieved
- CHARACTER: Thomas
  LINE: He hasn’t found you. I... I feared I’d never see you again.
  EXPRESSION: Weak, relieved
- CHARACTER: Narrator
  LINE: He coughs repeatedly. ELLEN holds him – she seems herself again.
  EXPRESSION: Concerned, solid
- CHARACTER: Ellen
  LINE: My love.
  EXPRESSION: Affectionate
- CHARACTER: Narrator
  LINE: THOMAS crumbles in her arms, delirious...
  EXPRESSION: Fading
- CHARACTER: Thomas
  LINE: You were right. You were... It... he... has your locket.
  EXPRESSION: Weak, delirious
- CHARACTER: Narrator
  LINE: THOMAS loses consciousness. ELLEN shakes him.
  EXPRESSION: Desperate
- CHARACTER: Ellen
  LINE: Thomas!
  EXPRESSION: Desperate plea
- CHARACTER: Narrator
  LINE: HARDING and ANNA go to help... SUDDENLY, A KNOCK AT THE DOOR.
  EXPRESSION: Alarmed
- CHARACTER: Harding
  LINE: What the hell is it now? Hartmann, the door.
  EXPRESSION: Irritated
- CHARACTER: Servant (O.S.)
  LINE: Very good, sir.
  EXPRESSION: Obedient
- CHARACTER: Narrator
  LINE: ANOTHER KNOCK.
  EXPRESSION: Insistent
- CHARACTER: Clara (O.S.)
  LINE: Mama! Papa! Is the monster here?
  EXPRESSION: Frightened
- CHARACTER: Narrator
  LINE: HARDING blazes down the hall and he steps in front of Hartmann, his SERVANT... THE KNOCKING is even more insistent.
  EXPRESSION: Angry, protective

::SCENE::
LOCATION: Harding House. Foyer
MOOD: Confrontational
CHARACTERS: Harding, Policeman, Dockhands, Hartmann
BACKGROUND_IMAGE: harding_house_foyer.png
BACKGROUND_EDIT: "Nighttime, foyer, Harding throws open the door"

::SCRIPT::
- CHARACTER: Narrator
  LINE: HARDING THROWS OPEN THE DOOR.
  EXPRESSION: Angry
- CHARACTER: Harding
  LINE: What the devil is this? It is past three o’clock in the morning!
  EXPRESSION: Furious
- CHARACTER: Narrator
  LINE: In front of him is a POLICEMAN and several DOCKHANDS with troubled faces.
  EXPRESSION: Concerned

::SCENE::
LOCATION: Wisburg Harbour. Dockside
MOOD: Disastrous
CHARACTERS: Harding, Dockhand, Rats
BACKGROUND_IMAGE: wisburg_harbour_dockside.png
BACKGROUND_EDIT: "Nighttime, storm over, wrecked ship, commotion"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The storm is over. HARDING stands looking at the disastrous wreck and the commotion of workers untangling the rigging. His face shows his alarm.
  EXPRESSION: Alarmed
- CHARACTER: Harding
  LINE: My God.
  EXPRESSION: Horrified
- CHARACTER: Narrator
  LINE: One by one, RATS run out of the giant hole in the hull of the ship across the quay.
  EXPRESSION: Foreboding
- CHARACTER: Dockhand
  LINE: Plague! It’s a plague ship!
  EXPRESSION: Terrified

::SCENE::
LOCATION: Wisburg Canal/Grünewald Manor
MOOD: Menacing
CHARACTERS: Knock, Orlok
BACKGROUND_IMAGE: wisburg_canal_grunewald_manor.png
BACKGROUND_EDIT: "Nighttime, dark canal, skiff approaching monstrous manor"

::SCRIPT::
- CHARACTER: Narrator
  LINE: A long SKIFF drifts across black nighttime waters toward the monstrous ruin of GRÜNEWALD MANOR, through its iron gates.
  EXPRESSION: Ominous
- CHARACTER: Narrator
  LINE: KNOCK is within the boat, escorting Orlok’s COFFIN.
  EXPRESSION: Sinister
- CHARACTER: Narrator
  LINE: In the highest floor of the manor stands ORLOK. His unblinking gaze looms over the city, bringing with it misery and death.
  EXPRESSION: Threatening

::SCENE::
LOCATION: Harding House. Guest Room
MOOD: Desperate Plea
CHARACTERS: Thomas, Ellen
BACKGROUND_IMAGE: harding_house_guest_room.png
BACKGROUND_EDIT: "Nighttime, Thomas in sickbed, Ellen holding his face"

::SCRIPT::
- CHARACTER: Narrator
  LINE: THOMAS lies in pain in Ellen’s sickbed. She holds his face and implores him with an intense whisper.
  EXPRESSION: Pained, pleading
- CHARACTER: Ellen
  LINE: Please, wake, Thomas.
  EXPRESSION: Desperate plea
- CHARACTER: Narrator
  LINE: He cannot.
  EXPRESSION: Hopeless
- CHARACTER: Ellen
  LINE: Your presence has already saved me.
  EXPRESSION: Resigned, grateful
- CHARACTER: Narrator
  LINE: He twists in agony as if having a terrible nightmare.
  EXPRESSION: Agonized

::SCENE::
LOCATION: Grünewald Manor
MOOD: Menacing Revelation
CHARACTERS: Orlok, Knock
BACKGROUND_IMAGE: grunewald_manor.png
BACKGROUND_EDIT: "Dilapidated room, Orlok unseen, Knock kneeling"

::SCRIPT::
- CHARACTER: Narrator
  LINE: CLOSE ON: ORLOK’S EYES. HE feels Thomas’ presence.
  EXPRESSION: Aware, predatory
- CHARACTER: Orlok
  LINE: The broker lives. I had cast aside his carrion body for my hellhounds to feed on.
  EXPRESSION: Cold, surprised
- CHARACTER: Narrator
  LINE: WIDE: KNOCK kneels before ORLOK on the floor of the entirely dilapidated and abandoned room (ORLOK is unseen).
  EXPRESSION: Subservient
- CHARACTER: Knock
  LINE: I shall then stifle out the bridegroom, your Lordship.
  EXPRESSION: Determined
- CHARACTER: Orlok (O.S.)
  LINE: I have use in him.
  EXPRESSION: Possessive
- CHARACTER: Narrator
  LINE: CLOSE ON: KNOCK (ORLOK remains unseen).
  EXPRESSION: Focused
- CHARACTER: Knock
  LINE: Pray then, instruct me, my Lord. Charge me. Use me. Shall I fetch unto thee thy pretty belonging?
  EXPRESSION: Eager, subservient
- CHARACTER: Orlok (O.S.)
  LINE: The compact commands she must willingly re-pledge her vow. She cannot be stolen.
  EXPRESSION: Authoritative
- CHARACTER: Narrator
  LINE: KNOCK rises to touch the hem of Orlok’s coat.
  EXPRESSION: Pleading
- CHARACTER: Knock
  LINE: Yet my Lord, I beg thee.
  EXPRESSION: Desperate
- CHARACTER: Orlok (O.S.)
  LINE: Silence, dog!
  EXPRESSION: Furious
- CHARACTER: Narrator
  LINE: ORLOK ROARS (still O.S.), st
  EXPRESSION: Enraged

::SCENE::
LOCATION: Orlok's Lair (Implied)
MOOD: Menacing
CHARACTERS: Orlok, Knock
BACKGROUND_IMAGE: orlok_lair.png
BACKGROUND_EDIT: "Dark, oppressive interior"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Striking KNOCK from within the darkness.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: KNOCK falls, smashing his face to the floor.
  EXPRESSION: null
- CHARACTER: Orlok
  LINE: Your entreaties grow insolent. You shall crave of me nothing.
  EXPRESSION: Cold
- CHARACTER: Narrator
  LINE: Knock nurses his bloody nose, barely able to speak.
  EXPRESSION: pained
- CHARACTER: Knock
  LINE: My Lord.
  EXPRESSION: weak
- CHARACTER: Orlok (O.S.)
  LINE: Away!
  EXPRESSION: dismissive
- CHARACTER: Narrator
  LINE: CLOSE ON: ORLOK profile.
  EXPRESSION: null
- CHARACTER: Orlok
  LINE: Daybreak draws near. Anon the bells of dawn shall toll in despair of my coming.
  EXPRESSION: ominous
- CHARACTER: Narrator
  LINE: He smells Ellen’s hair deeply within the locket. His eyes glimmer with cruel passion.
  EXPRESSION: lustful
- CHARACTER: Orlok
  LINE: And I shall taste of you.
  EXPRESSION: predatory

::PATHS::
- CHOICE: "Orlok contemplates his next move."
  TARGET: wisburg_streets
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Wisburg Streets
MOOD: Ominous
CHARACTERS: Narrator
BACKGROUND_IMAGE: wisburg_streets.png
BACKGROUND_EDIT: "Morning, streets overrun with rats"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Hundreds of RATS run through the streets and gutters.
  EXPRESSION: unsettling

::PATHS::
- CHOICE: "Investigate the Harding House."
  TARGET: harding_house_guest_room
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Harding House. Guest Room
MOOD: Concerned
CHARACTERS: Narrator, Ellen, Thomas, Anna
BACKGROUND_IMAGE: harding_house_guest_room.png
BACKGROUND_EDIT: "Afternoon, Thomas is ill in bed"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Ellen sits by Thomas’ side as he struggles in bed. Anna stands by her.
  EXPRESSION: worried
- CHARACTER: Anna
  LINE: How is he faring?
  EXPRESSION: concerned
- CHARACTER: Ellen
  LINE: I fear no better than everyone tells me I have suffered. Pray, forgive me for the troubles I have caused you.
  EXPRESSION: regretful
- CHARACTER: Anna
  LINE: I am only glad that you have become yourself again. It seems a miracle. Perhaps Professor Franz was wrong. Perhaps it was only your wish to see Thomas safely returned, and your... your -
  EXPRESSION: hopeful
- CHARACTER: Ellen
  LINE: My melancholy?
  EXPRESSION: thoughtful
- CHARACTER: Narrator
  LINE: Pause.
  EXPRESSION: null
- CHARACTER: Ellen
  LINE: Thomas has seen something awful. If only I could speak to the professor –
  EXPRESSION: troubled
- CHARACTER: Anna
  LINE: Hush. His thoughts are so queer, so sordid, I dare not repeat them.
  EXPRESSION: hesitant
- CHARACTER: Ellen
  LINE: Professor Franz said a demon!
  EXPRESSION: fearful
- CHARACTER: Anna
  LINE: Leni, please. For the sake of the children – Christmastide is upon us. Why must you remain so exasperatingly contrary?!
  EXPRESSION: frustrated
- CHARACTER: Ellen
  LINE: Because I am in the right!
  EXPRESSION: defiant

::PATHS::
- CHOICE: "Go to the hospital morgue."
  TARGET: wisburg_hospital_morgue
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Wisburg Hospital. Morgue
MOOD: Grim
CHARACTERS: Narrator, Sievers, Von Franz, Attendant
BACKGROUND_IMAGE: wisburg_hospital_morgue.png
BACKGROUND_EDIT: "Afternoon, sterile, unpleasant atmosphere"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Sievers uncovers the corpse of CAPTAIN YUSOV on a wooden slab. The air is thick with the stench of dripping carbolic acid. An Attendant assists Sievers.
  EXPRESSION: null
- CHARACTER: Von Franz
  LINE: Sievers, I requested conference with your maniac, not a dead man.
  EXPRESSION: impatient
- CHARACTER: Sievers
  LINE: I beg your patience, Professor. This is what vexes me: He exhibits all the signs of a blood plague: sepsis, ophthalmic discharge – even flagrant rodent bites, here and here. I fear this ship has brought the plague to Wisburg.
  EXPRESSION: concerned
- CHARACTER: Narrator
  LINE: Von Franz crosses himself.
  EXPRESSION: fearful
- CHARACTER: Sievers
  LINE: What’s more, his body is entirely absent of blood.
  EXPRESSION: shocked
- CHARACTER: Sievers
  LINE: And look at this curious mark here...
  EXPRESSION: curious
- CHARACTER: Narrator
  LINE: Von Franz looks at the chest. A VAMPIRE BITE.
  EXPRESSION: horrified
- CHARACTER: Sievers
  LINE: I have seen some leviathan-like pests in our canals, but tell me, Professor, what rat has jaws of such size?
  EXPRESSION: questioning
- CHARACTER: Von Franz
  LINE: Angels and Daemons protect us. Where is your lunatic? You must take me to him presently!
  EXPRESSION: alarmed
- CHARACTER: Attendant
  LINE: Ain’t you heard it, Doctor, sir?
  EXPRESSION: matter-of-fact
- CHARACTER: Sievers
  LINE: No...
  EXPRESSION: unaware
- CHARACTER: Attendant
  LINE: Herr Knock, he’s gone and escaped –
  EXPRESSION: surprised
- CHARACTER: Von Franz
  LINE: That man must be found!
  EXPRESSION: urgent
- CHARACTER: Narrator
  LINE: He puts on his hat and heads to the door in haste.
  EXPRESSION: null
- CHARACTER: Von Franz
  LINE: Sirrah, show me out. Sievers, meet me at my residence tonight. I must to my studies!
  EXPRESSION: determined

::PATHS::
- CHOICE: "Follow Von Franz to his residence."
  TARGET: von_franzs_attic
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Von Franz’s Attic
MOOD: Scientific Obsession
CHARACTERS: Narrator, Harding, Sievers, Von Franz
BACKGROUND_IMAGE: von_franzs_attic.png
BACKGROUND_EDIT: "Night, cluttered attic with scientific equipment"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Harding and Sievers stand awkwardly, leaning forward in unison, peering into a magnifying glass on a stand.
  EXPRESSION: null
- CHARACTER: Von Franz
  LINE: Gnathobdela. The common leech.
  EXPRESSION: clinical
- CHARACTER: Narrator
  LINE: IN THE GLASS: A LEECH on Von Franz’s hand, sucking his blood. It twitches vulgarly. Von Franz’s vein pulses.
  EXPRESSION: repulsive
- CHARACTER: Von Franz
  LINE: Its sole impulse is to feed on what even Mephistopheles calls “the most especial nectar.” Look at her drink. (laughs)
  EXPRESSION: disturbed
- CHARACTER: Harding
  LINE: Please Professor, what is all this?
  EXPRESSION: confused
- CHARACTER: Von Franz
  LINE: Quickly now, Sievers ...
  EXPRESSION: urgent
- CHARACTER: Narrator
  LINE: Von Franz removes the leech with some tweezers and sucks his wound. He spits on the floor and puts the leech in a jar.
  EXPRESSION: null
- CHARACTER: Von Franz
  LINE: ... the plague is present in its most rapidly fatal form, Pestis siderans.
  EXPRESSION: grave
- CHARACTER: Sievers
  LINE: A savage infection of the blood.
  EXPRESSION: grim
- CHARACTER: Von Franz
  LINE: You have read Glaser’s treatise on the pestilent revenants of the eastern frontiers of the Hapsburg Empire?
  EXPRESSION: expectant
- CHARACTER: Narrator
  LINE: Sievers is completely shocked.
  EXPRESSION: stunned
- CHARACTER: Sievers
  LINE: That has been long proven to be a degrading peasant superstition.
  EXPRESSION: dismissive
- CHARACTER: Von Franz
  LINE: Is our leech a superstition?
  EXPRESSION: challenging
- CHARACTER: Narrator
  LINE: Sievers laughs.
  EXPRESSION: skeptical
- CHARACTER: Sievers
  LINE: No, but leeches do not rise from the grave, my dear professor.
  EXPRESSION: amused
- CHARACTER: Von Franz
  LINE: Please, Sievers, please, explain Glaser’s account.
  EXPRESSION: pleading
- CHARACTER: Narrator
  LINE: Sievers begins, reluctantly.
  EXPRESSION: null
- CHARACTER: Sievers
  LINE: A... a plague ravaged the countryside. The alleged cause ... a... a walking corpse that maintained a semblance of life by feeding on the heart blood of the living. Every victim succumbed to death.
  EXPRESSION: reluctant

::PATHS::
- CHOICE: "Return to the Harding House for the night."
  TARGET: harding_house_guest_room_night
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Grünewald Manor
MOOD: Powerful Evil
CHARACTERS: Narrator, Orlok
BACKGROUND_IMAGE: grunewald_manor.png
BACKGROUND_EDIT: "Night, vast, empty room with an open window"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Orlok stands in a huge, dark, furniture-less room. His stance is broad and powerful. He looks out a massive open window at all of Wisburg. His hypnotic eyes gleam...
  EXPRESSION: menacing
- CHARACTER: Narrator
  LINE: He begins his incantations... He raises his hand... he opens his palms...
  EXPRESSION: ritualistic

::PATHS::
- CHOICE: "Orlok casts his spell."
  TARGET: harding_house_guest_room_night_simultaneous
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Harding House. Guest Room
MOOD: Traumatic
CHARACTERS: Narrator, Ellen, Thomas, Orlok (shadow)
BACKGROUND_IMAGE: harding_house_guest_room_night.png
BACKGROUND_EDIT: "Night, Ellen and Thomas in bed"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Ellen and Thomas lie in bed together. She holds him close.
  EXPRESSION: intimate
- CHARACTER: Orlok (V.O.)
  LINE: Your bond shall not survive me.
  EXPRESSION: whispered, subtitled
- CHARACTER: Narrator
  LINE: Orlok’s shadow spreads over Thomas. Ellen doesn’t see it.
  EXPRESSION: ominous
- CHARACTER: Narrator
  LINE: Thomas struggles in bed. Ellen touches him gently...
  EXPRESSION: concerned
- CHARACTER: Narrator
  LINE: IMAGE: ORLOK attacks THOMAS!
  EXPRESSION: violent
- CHARACTER: Narrator
  LINE: Thomas wakes from his nightmare vision... he pulls away from Ellen. In his delirium, he barks at her fiercely:
  EXPRESSION: panicked
- CHARACTER: Thomas
  LINE: Get off me. Give me room. I can’t breathe!
  EXPRESSION: desperate
- CHARACTER: Narrator
  LINE: She is stunned. She tries to comfort him:
  EXPRESSION: null
- CHARACTER: Ellen
  LINE: It’s me.
  EXPRESSION: soothing
- CHARACTER: Thomas
  LINE: I can’t breathe... Get off!!!
  EXPRESSION: frantic
- CHARACTER: Narrator
  LINE: He throws her off of him violently, accidentally striking her... She nearly falls off the bed...
  EXPRESSION: violent
- CHARACTER: Narrator
  LINE: HOLD ON: Ellen’s face, afraid, and hurt. She doesn’t want to feel rejected, BUT SHE DOES.
  EXPRESSION: pained

::PATHS::
- CHOICE: "Ellen seeks comfort in the nursery."
  TARGET: harding_house_hallway_nursery
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Harding House. Upstairs Hallway/Nursery
MOOD: Fearful but Protective
CHARACTERS: Narrator, Anna, Clara, Louise, Ellen
BACKGROUND_IMAGE: harding_house_hallway_nursery.png
BACKGROUND_EDIT: "Moments later, dimly lit hallway"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Anna tucks Clara and Louise into their beds, then takes a large LAMP.
  EXPRESSION: null
- CHARACTER: Clara
  LINE: Please you, don’t leave us, mama.
  EXPRESSION: scared
- CHARACTER: Anna
  LINE: I promise, I shan’t let anything harm you. No monsters – nothing. Now, kiss me good night and say your prayers.
  EXPRESSION: reassuring
- CHARACTER: Narrator
  LINE: Anna kisses them. She hesitates, then closes the door.
  EXPRESSION: null
- CHARACTER: Clara (O.S.)
  LINE: Now I lay me down to sleep, I pray the Lord my soul to keep...
  EXPRESSION: praying
- CHARACTER: Narrator
  LINE: Anna walks with her LAMP...
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: She sees something move in the shadows. Her blood runs cold. She hears footsteps. She is gripped with fear.
  EXPRESSION: terrified
- CHARACTER: Narrator
  LINE: Suddenly, something emerges from the dark...
  EXPRESSION: startled
- CHARACTER: Narrator
  LINE: She gasps, almost dropping the lamp.
  EXPRESSION: shocked
- CHARACTER: Narrator
  LINE: She looks: it’s only Ellen.
  EXPRESSION: relieved
- CHARACTER: Anna
  LINE: You frightened me.
  EXPRESSION: startled
- CHARACTER: Ellen
  LINE: Forgive me.
  EXPRESSION: apologetic
- CHARACTER: Narrator
  LINE: Ellen is beginning to look haunted again.
  EXPRESSION: troubled
- CHARACTER: Ellen
  LINE: Has Friedrich returned?
  EXPRESSION: anxious
- CHARACTER: Anna
  LINE: No.
  EXPRESSION: calm
- CHARACTER: Narrator
  LINE: Anna senses Ellen’s sadness.
  EXPRESSION: empathetic
- CHARACTER: Anna
  LINE: What is it my lovely?
  EXPRESSION: gentle
- CHARACTER: Narrator
  LINE: Ellen looks at her longingly...
  EXPRESSION: wistful
- CHARACTER: Ellen
  LINE: May I stay with you tonight?
  EXPRESSION: pleading

::PATHS::
- CHOICE: "Ellen stays with Anna."
  TARGET: harding_house_master_bedchamber
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: OMITTED

::SCRIPT::
- CHARACTER: Narrator
  LINE: OMITTED
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue to the master bedchamber."
  TARGET: harding_house_master_bedchamber_later
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Harding House. Master Bedchamber
MOOD: Comforting
CHARACTERS: Narrator, Ellen, Anna
BACKGROUND_IMAGE: harding_house_master_bedchamber.png
BACKGROUND_EDIT: "Later, cozy bedchamber"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Ellen cuddles in with Anna in bed, playing with the cross around Anna’s neck like a kitten. Anna’s...
  EXPRESSION: affectionate

::PATHS::
- CHOICE: "The scene fades."
  TARGET: end
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: INT. VON FRANZ ATTIC
MOOD: Somber, Desperate
CHARACTERS: Anna, Ellen
BACKGROUND_IMAGE: von_franz_attic_day.png
BACKGROUND_EDIT: "Dusty attic, dimly lit"

::SCRIPT::
- CHARACTER: Narrator
  LINE: eyes droop.
  EXPRESSION: Tired
- CHARACTER: Anna
  LINE: If I speak yet more words of comfort, you must not hear them as feeble or petty. Our friendship is a precious balm to my heart. Forgive my chiding you.
  EXPRESSION: Gentle
- CHARACTER: Ellen
  LINE: Thank you for loving me.
  EXPRESSION: Grateful
- CHARACTER: Narrator
  LINE: ANNA is not quite sure what to say.
  EXPRESSION: Uncertain
- CHARACTER: Anna
  LINE: You may take it if you wish.
  EXPRESSION: Offering
- CHARACTER: Narrator
  LINE: ELLEN takes THE CROSS off of her and plays with it.
  EXPRESSION: Distracted
- CHARACTER: Anna
  LINE: God is with us, Leni.
  EXPRESSION: Reassuring
- CHARACTER: Ellen
  LINE: Don’t close your eyes first. Please.
  EXPRESSION: Pleading
- CHARACTER: Anna
  LINE: I shan’t.
  EXPRESSION: Determined
- CHARACTER: Ellen
  LINE: Let me watch you.
  EXPRESSION: Yearning
- CHARACTER: Narrator
  LINE: ELLEN watches her, yearning. She holds THE CROSS.
  EXPRESSION: Yearning

::SCENE::
LOCATION: INT. VON FRANZ ATTIC – MOMENTS LATER
MOOD: Intense, Terrified
CHARACTERS: Harding, Von Franz
BACKGROUND_IMAGE: von_franz_attic_later.png
BACKGROUND_EDIT: "Stove in the background, tension in the air"

::SCRIPT::
- CHARACTER: Harding
  LINE: I cannot yield to being haunted by some ghost!
  EXPRESSION: Exasperated
- CHARACTER: Von Franz
  LINE: No, no, no, please, no. It is no mere ghost, for it can manifest physically, and with the most foul intent.
  EXPRESSION: Urgent
- CHARACTER: Harding
  LINE: And what, pray, is that?
  EXPRESSION: Skeptical
- CHARACTER: Von Franz
  LINE: Like every plague, its only desire is to consume all life on earth. It is a force more powerful than evil. It is death itself.
  EXPRESSION: Grim
- CHARACTER: Narrator
  LINE: HARDING boils.
  EXPRESSION: Enraged
- CHARACTER: Harding
  LINE: I have not slept in days, my house is become a bedlam, and here I have been re-summoned to this God-forsaken habitation for this? Do not tell me you believe in such medieval devilry?!
  EXPRESSION: Outraged
- CHARACTER: Narrator
  LINE: VON FRANZ looks HARDING in the eye with the profundity of Moses reading the commandments:
  EXPRESSION: Serious
- CHARACTER: Von Franz
  LINE: I do not believe. I know.
  EXPRESSION: Certain
- CHARACTER: Von Franz
  LINE: I have seen things in this world that would have made Isaac Newton crawl back into his mother’s womb. We have not become so much enlightened as we have been blinded by the gaseous light of science. I have wrestled with the Devil as Jacob wrestled the angel in Peniel and I tell you, if we are to tame darkness, we must first face that it exists. Meine Herren, we are here encountering the un-dead plague carrier... the Vampyr... Nosferatu!
  EXPRESSION: Solemn

::SCENE::
LOCATION: INT. HARDING HOUSE. MASTER BEDCHAMBER – THE NEXT MOMENT
MOOD: Eerie, Foreboding
CHARACTERS: Ellen, Anna, Orlok (manifestation)
BACKGROUND_IMAGE: harding_bedchamber_night.png
BACKGROUND_EDIT: "Dimly lit bedroom, shadows forming"

::SCRIPT::
- CHARACTER: Narrator
  LINE: ELLEN and ANNA lie asleep. All is silent. Too silent.
  EXPRESSION: Suspenseful
- CHARACTER: Narrator
  LINE: Slowly, a dark SHADOW forms around the large windows. Just as slowly, ELLEN opens her eyes.
  EXPRESSION: Unsettling
- CHARACTER: Narrator
  LINE: She rises from bed, her limbs weightless... her heart throbbing... her body growing hot... her breath accelerating...
  EXPRESSION: Transformed
- CHARACTER: Narrator
  LINE: She nears the window... she opens it.
  EXPRESSION: Drawn
- CHARACTER: Narrator
  LINE: She is surrounded by the MIST, almost suspended by it...
  EXPRESSION: Ethereal
- CHARACTER: Narrator
  LINE: SUDDENLY, A HORRIFIC FACE WITH PENETRATING EYES APPEARS TO HER... she gasps in fear... IT IS ORLOK, and for the first time, she faces him in THE FLESH.
  EXPRESSION: Terrified
- CHARACTER: Narrator
  LINE: She is drawn to him – so drawn to his presence – aflame with desire... but she holds herself still.
  EXPRESSION: Conflicted
- CHARACTER: Ellen
  LINE: I have felt you like a serpent crawling in my body.
  EXPRESSION: Revulsed yet Drawn
- CHARACTER: Orlok
  LINE: It is not me. It is your nature.
  EXPRESSION: Manipulative
- CHARACTER: Ellen
  LINE: No! I love Thomas.
  EXPRESSION: Defiant
- CHARACTER: Orlok
  LINE: Love is inferior to you. I told you, you are not of human kind.
  EXPRESSION: Condescending
- CHARACTER: Ellen
  LINE: You are a villain to speak so.
  EXPRESSION: Indignant
- CHARACTER: Orlok
  LINE: I am an appetite. Nothing more.
  EXPRESSION: Cold
- CHARACTER: Narrator
  LINE: He takes a pained breath. The faintest glimmer of something human flashes within his eyes.
  EXPRESSION: Fleeting Humanity
- CHARACTER: Orlok
  LINE: O’er centuries, a loathsome beast I lay within the darkest pit ‘til you did wake me, enchantress, and stirred me from my grave. You are my affliction.
  EXPRESSION: Possessive
- CHARACTER: Ellen
  LINE: I care nothing of your afflictions.
  EXPRESSION: Dismissive
- CHARACTER: Orlok
  LINE: Yet even now we are fated.
  EXPRESSION: Gloating
- CHARACTER: Narrator
  LINE: He smiles mockingly. Gloating.
  EXPRESSION: Mocking
- CHARACTER: Orlok
  LINE: Your husband has signed his name, and covenanted you to my person for but a sack of gold.
  EXPRESSION: Cruel
- CHARACTER: Narrator
  LINE: This strikes at ELLEN’S heart. But she doesn’t believe it.
  EXPRESSION: Shocked
- CHARACTER: Ellen
  LINE: Lies.
  EXPRESSION: Disbelieving
- CHARACTER: Orlok
  LINE: For gold he did absolve his nuptial bond.
  EXPRESSION: Mocking
- CHARACTER: Ellen
  LINE: You know nothing of him.
  EXPRESSION: Insistent
- CHARACTER: Orlok
  LINE: And the resignation must be completed by you, freely of thine own will.
  EXPRESSION: Demanding
- CHARACTER: Ellen
  LINE: You are a deceiver!
  EXPRESSION: Accusatory
- CHARACTER: Orlok
  LINE: You deceive yourself.
  EXPRESSION: Taunting
- CHARACTER: Ellen
  LINE: I was but an innocent child –
  EXPRESSION: Pleading
- CHARACTER: Orlok
  LINE: And thought you I would not return? Thought you I would not? Your passion is bound to me.
  EXPRESSION: Threatening
- CHARACTER: Narrator
  LINE: He reaches his long, leathery fingers toward her... his nails grabbing her hair... his fist tightens... drawing her close.
  EXPRESSION: Violently
- CHARACTER: Ellen
  LINE: You cannot love.
  EXPRESSION: Desperate
- CHARACTER: Orlok
  LINE: I cannot. Yet, I cannot be sated without you.
  EXPRESSION: Lustful
- CHARACTER: Narrator
  LINE: His breath is lustful. So is hers. She disgusts herself by how drawn she is to him. ORLOK grips her more tightly.
  EXPRESSION: Desperate and Disgusted
- CHARACTER: Orlok
  LINE: Remember how once we were? A moment. Remember?
  EXPRESSION: Tempting
- CHARACTER: Narrator
  LINE: ELLEN whispers to his hideous and alluring face.
  EXPRESSION: Whispering
- CHARACTER: Ellen
  LINE: I abhor you.
  EXPRESSION: Revulsed
- CHARACTER: Narrator
  LINE: Pause. This sends Orlok into a rage.
  EXPRESSION: Furious
- CHARACTER: Orlok
  LINE: You are false!
  EXPRESSION: Enraged
- CHARACTER: Orlok
  LINE: So you wish me to prove my enmity as well? I will leave you three nights. Tonight was the first. Tonight you denied yourself, and thereby you suffer me to vanish up the lives of those you love.
  EXPRESSION: Vengeful
- CHARACTER: Ellen
  LINE: Denied myself?! You revel in my torture!
  EXPRESSION: Anguished
- CHARACTER: Orlok
  LINE: Dry your cheek. Upon the third night you will submit, or he you call your husband shall perish by my hand.
  EXPRESSION: Threatening
- CHARACTER: Ellen
  LINE: No!
  EXPRESSION: Desperate
- CHARACTER: Orlok
  LINE: You will press thy lips to my cold mouth and I will drink upon thy soul. ‘Til you bid me come, shall you watch the world become as naught.
  EXPRESSION: Terrifying
- CHARACTER: Ellen
  LINE: NO!!!
  EXPRESSION: Screaming
- CHARACTER: Narrator
  LINE: IMAGE: ORLOK’S hideous face growls like a virile, predatory animal! His claws splayed!
  EXPRESSION: Monstrous
- CHARACTER: Narrator
  LINE: ELLEN SEES IT! HIS GROWL BREAKS HER TRANCE... SHE SCREAMS!
  EXPRESSION: Shattered
- CHARACTER: Narrator
  LINE: She is no longer at the window... she is back in bed... and to her side, ANNA is not there... only her golden cross. ELLEN looks across the room...
  EXPRESSION: Disoriented
- CHARACTER: Narrator
  LINE: ANNA LIES ON THE FLOOR... her nightgown ripped, exposing her body... SHE WRITHES EROTICALLY, AS RATS CRAWL ALL OVER HER, SCURRYING AWAY.
  EXPRESSION: Horrifying and Disturbing

::SCENE::
LOCATION: EXT. HARDING HOUSE. WINDOW - THAT SAME MOMENT
MOOD: Horrifying
CHARACTERS: Orlok, Ellen (implied)
BACKGROUND_IMAGE: orlok_window_night.png
BACKGROUND_EDIT: "Close on Orlok's face, bloodied"

::SCRIPT::
- CHARACTER: Narrator
  LINE: CLOSE ON: ORLOK, his mouth covered in ANNA’S BLOOD. He whispers to ELLEN.
  EXPRESSION: Savage
- CHARACTER: Orlok
  LINE: (subtitled) Two more nights.
  EXPRESSION: Menacing

::SCENE::
LOCATION: INT. WISBURG HOSPITAL. CORRIDOR – DAY
MOOD: Chaotic, Desperate
CHARACTERS: Sievers, Hospital Nurse, Citizens
BACKGROUND_IMAGE: wisburg_hospital_corridor_day.png
BACKGROUND_EDIT: "Hospital corridor, signs of riot and illness"

::SCRIPT::
- CHARACTER: Narrator
  LINE: SEEN THROUGH A WINDOW: Citizens shout, and riot, beating their fists upon the doors of the hospital. Some fall down dead. The Wisburg MILITARY POLICE hold their rifles, beating people back.
  EXPRESSION: Chaotic
- CHARACTER: Narrator
  LINE: SIEVERS walks at a feverish pace. A HOSPITAL NURSE by his side.
  EXPRESSION: Urgent
- CHARACTER: Narrator
  LINE: Patients are rushed through the hospital on stretchers, the besotted marks of sepsis on their skin.
  EXPRESSION: Grim
- CHARACTER: Narrator
  LINE: The screaming and pounding echoes through the building. The stress, the anxiety is becoming too much.
  EXPRESSION: Overwhelming
- CHARACTER: Hospital Nurse
  LINE: I ain’t never seen the like. It’s a-spreadin’ faster than wildfire since yester-morn.
  EXPRESSION: Worried
- CHARACTER: Sievers
  LINE: We simply cannot admit any more. The rate of contraction is too high, the deaths so rapid – it’s a most desperate hazard. I’ve entreated the burgomaster for a quarantine. The city must be shut up.
  EXPRESSION: Resolute
- CHARACTER: Hospital Nurse
  LINE: It is not Christian, sir! The day of judgment is a-coming, sir. Pity them, sir. Take pity!
  EXPRESSION: Desperate
- CHARACTER: Narrator
  LINE: The O.S. rioting, reaches a fever pitch.
  EXPRESSION: Escalating
- CHARACTER: Sievers
  LINE: We must r
  EXPRESSION: Interrupted

::SCENE::
LOCATION: Harding House. Master Bedchamber
MOOD: Tragic, Disturbing
CHARACTERS: Anna, Harding, Ellen
BACKGROUND_IMAGE: harding_house_master_bedchamber.png
BACKGROUND_EDIT: "Daytime. Anna is in bed, pale and weak. Harding holds her hand, looking distraught. Ellen stands nearby, observing."

::SCRIPT::
- CHARACTER: Anna
  LINE: Such nightmares... a shadow pressing... my body sinking... sinking... The smell of rancid meat... Suffocating... I... feel so weak... I...
  EXPRESSION: Weak, Frightened
- CHARACTER: Harding
  LINE: (Sees THE VAMPIRE BITE on her chest. Does he believe?)
  EXPRESSION: Troubled
- CHARACTER: Anna
  LINE: I fear little Friedrich is so strong and hungry, he’s eating me weary.
  EXPRESSION: Weak, Distraught
- CHARACTER: Anna
  LINE: (Puts his hand on her womb. They both hold back tears.)
  EXPRESSION: Sad
- CHARACTER: Harding
  LINE: Yes...
  EXPRESSION: Sad
- CHARACTER: Anna
  LINE: (Tries to be strong, but she can see the horror in her husband’s face.) May I see the girls?
  EXPRESSION: Sad
- CHARACTER: Harding
  LINE: (Can’t say yes.)
  EXPRESSION: Distraught
- CHARACTER: Anna
  LINE: I must assure them...
  EXPRESSION: Desperate
- CHARACTER: Anna
  LINE: (Suddenly begins to laugh more intensely.)
  EXPRESSION: Unsettled
- CHARACTER: Harding
  LINE: Everything shall be well my darling. Everything shall be just fine.
  EXPRESSION: Reassuring, but strained
- CHARACTER: Anna
  LINE: (Keeps laughing and crying at the same time.) I don’t know myself... I... Ellen, tell me, what is this insufferable darkness?
  EXPRESSION: Distraught, Crying
- CHARACTER: Narrator
  LINE: (ELLEN AND ANNA LOCK EYES... SHE CONTINUES TO LAUGH, NOW WRITHING SENSUALLY, AS ELLEN HAS DONE.)
  EXPRESSION: Unsettling

::SCENE::
LOCATION: Harding House. Upstairs Hall
MOOD: Tense, Urgent
CHARACTERS: Ellen, Harding
BACKGROUND_IMAGE: harding_house_upstairs_hall.png
BACKGROUND_EDIT: "Moments later. Ellen and Harding stand outside Anna's door."

::SCRIPT::
- CHARACTER: Ellen
  LINE: Herr Harding, you must hear me, there is something... the shadow... an infernal creature...
  EXPRESSION: Urgent, Fearful
- CHARACTER: Harding
  LINE: (Can’t look at her.) Ellen–
  EXPRESSION: Avoidant
- CHARACTER: Ellen
  LINE: Please, these are no troubled nerves – it is as Professor Franz described... a demon!
  EXPRESSION: Pleading, Fearful
- CHARACTER: Harding
  LINE: (Overlapping) Frau Hutter, forgive me, but you and Thomas must... I need you both to return home.
  EXPRESSION: Dismissive, Strained
- CHARACTER: Ellen
  LINE: What?
  EXPRESSION: Shocked
- CHARACTER: Harding
  LINE: It is for your own sake.
  EXPRESSION: Firm, but pained
- CHARACTER: Narrator
  LINE: (He keeps his demeanour dignified, but his emotions are brimming. He could explode at any moment.)
  EXPRESSION: Tense
- CHARACTER: Ellen
  LINE: Please, have pity, Thomas is very poorly and...
  EXPRESSION: Pleading, Worried
- CHARACTER: Harding
  LINE: I know not what to... I shall pray for Tom. You know I love you both.
  EXPRESSION: Distant, Evasive
- CHARACTER: Ellen
  LINE: What of Anna? Did you not see–
  EXPRESSION: Desperate
- CHARACTER: Harding
  LINE: None of your concern.
  EXPRESSION: Harsh, Final
- CHARACTER: Ellen
  LINE: Friedrich, you must listen to me, we are all in the most grave danger – I throw myself at your feet.
  EXPRESSION: Desperate, Begging
- CHARACTER: Narrator
  LINE: (As ELLEN goes almost to kiss his hand ...)
  EXPRESSION: Humiliating
- CHARACTER: Harding
  LINE: Frau Hutter! Please!
  EXPRESSION: Shocked, Repulsed
- CHARACTER: Ellen
  LINE: (Is hurt. She looks him square in the eye.) Why do you hate me?
  EXPRESSION: Hurt, Accusatory
- CHARACTER: Narrator
  LINE: (Pause. HARDING is shocked by her candour.)
  EXPRESSION: Surprised
- CHARACTER: Harding
  LINE: How dare you speak to me in that marked manner?
  EXPRESSION: Indignant
- CHARACTER: Ellen
  LINE: (Overlapping) You have never liked me. Never.
  EXPRESSION: Resentful
- CHARACTER: Harding
  LINE: Know your place, madam.
  EXPRESSION: Authoritative, Cold
- CHARACTER: Ellen
  LINE: I will not stand by and pretend at your superiority. Why can you not hear me?
  EXPRESSION: Defiant, Frustrated
- CHARACTER: Harding
  LINE: I refuse to exchange reproaches with you.
  EXPRESSION: Dismissive
- CHARACTER: Ellen
  LINE: Tied me up?
  EXPRESSION: Accusatory
- CHARACTER: Harding
  LINE: ...find the dignity to display the respect to your caretaker –
  EXPRESSION: Patronizing
- CHARACTER: Ellen
  LINE: How can you be so stupid and cruel?
  EXPRESSION: Outraged
- CHARACTER: Narrator
  LINE: (HARDING IS ENRAGED. HE WANTS TO SCREAM. Instead, he says:)
  EXPRESSION: Furious
- CHARACTER: Harding
  LINE: Hartmann will call you a coach, at my expense – of course.
  EXPRESSION: Cold, Final

::SCENE::
LOCATION: Wisburg Hospital. Knock's Cell
MOOD: Mysterious, Foreboding
CHARACTERS: Von Franz, Sievers
BACKGROUND_IMAGE: wisburg_hospital_knocks_cell.png
BACKGROUND_EDIT: "Daytime. Von Franz studies esoteric writing on a blood-stained wall. Sievers is present."

::SCRIPT::
- CHARACTER: Von Franz
  LINE: Why did you not tell me of this before?
  EXPRESSION: Inquisitive, Stern
- CHARACTER: Sievers
  LINE: I am a fool. His obsessive consumption of living creatures – of course it is Herr Knock!
  EXPRESSION: Guilt-ridden, Realizing
- CHARACTER: Von Franz
  LINE: He is not Nosferatu - yet he must be found for he has made compact with this shadow.
  EXPRESSION: Determined
- CHARACTER: Sievers
  LINE: Then you can decipher it?
  EXPRESSION: Hopeful
- CHARACTER: Von Franz
  LINE: “His thunder roars from clouds of carcasses, I feedeth on my shroud, and death avails me not. For I am his.”
  EXPRESSION: Cryptic
  STATE_CHANGE: current_script_line = "His thunder roars from clouds of carcasses, I feedeth on my shroud, and death avails me not. For I am his."

::SCENE::
LOCATION: Knock’s Estate Agency
MOOD: Desperate, Chaotic
CHARACTERS: Von Franz, Sievers
BACKGROUND_IMAGE: knocks_estate_agency.png
BACKGROUND_EDIT: "Daytime. Von Franz and Sievers rush to the boarded-up facade of Knock’s agency. The street is shrouded in a fog of chlorine gas. Quarantine notices line the windows. They break in."

::SCRIPT::
- CHARACTER: Narrator
  LINE: VON FRANZ and SIEVERS rush to the BOARDED UP facade of KNOCK’S AGENCY. The street is shrouded in a fog of chlorine gas. Wheat-pasted quarantine notices line boarded-up storefronts. Using an iron bar, VON FRANZ and SIEVERS break in to the agency with a bang!
  EXPRESSION: Urgent

::SCENE::
LOCATION: Knock's Office
MOOD: Intense, Revealing
CHARACTERS: Von Franz, Sievers
BACKGROUND_IMAGE: knocks_office.png
BACKGROUND_EDIT: "Continuous action. Von Franz and Sievers search the office."

::SCRIPT::
- CHARACTER: Von Franz
  LINE: Search everything.
  EXPRESSION: Demanding
- CHARACTER: Narrator
  LINE: MOMENTS LATER: His eyes widen. He has found many notes and papers in “the secret language.”
  EXPRESSION: Astonished
- CHARACTER: Narrator
  LINE: MOMENTS LATER: He finds a massive medieval BOOK with THE EVIL EYE on the cover. He takes it. He stands and studies the room. Beat.
  EXPRESSION: Significant
- CHARACTER: Von Franz
  LINE: Pull up the rug.
  EXPRESSION: Commanding
- CHARACTER: Narrator
  LINE: He and SIEVERS move KNOCK’S large desk up against a wall. They pull back a large, well-worn oriental RUG to reveal... KNOCK’S MAGICAL HEPTAGRAM.
  EXPRESSION: Revealing
- CHARACTER: Von Franz
  LINE: Şolomanari.
  EXPRESSION: Knowing

::SCENE::
LOCATION: Wisburg. Old Town
MOOD: Grim, Desperate
CHARACTERS: Ellen, Thomas, Greta (in cage)
BACKGROUND_IMAGE: wisburg_old_town.png
BACKGROUND_EDIT: "Afternoon. Ellen and Thomas exit a coach, covering their mouths. Ellen carries Greta in a cage. Thomas limps and is struggling to stay conscious."

::SCRIPT::
- CHARACTER: Narrator
  LINE: ELLEN and THOMAS exit the coach, covering their mouths from the chlorine gas and billowing smoke from the open fires.
  EXPRESSION: Suffering
- CHARACTER: Narrator
  LINE: ELLEN carries GRETA in a little wicker cage. THOMAS limps on a cane, having difficulty staying conscious.
  EXPRESSION: Frail
- CHARACTER: Narrator
  LINE: As they walk, he begins to faint.
  EXPRESSION: Weakening
- CHARACTER: Ellen
  LINE: Keep with me, my love.
  EXPRESSION: Supportive, Worried
- CHARACTER: Narrator
  LINE: She collects her husband.
  EXPRESSION: Caring
- CHARACTER: Ellen
  LINE: We are nearly home.
  EXPRESSION: Hopeful, Tired
- CHARACTER: Narrator
  LINE: ELLEN is horrified as she sees TOWN OFFICIALS walking down her own street marking a “cross” in chalk upon the doors of the afflicted houses.
  EXPRESSION: Horrified
- CHARACTER: Narrator
  LINE: A raving maniac shouts broken phrases from Revelation. Mothers, fathers, brothers and sisters cry and howl, as their dead loved ones are loaded onto carts. ELLEN fills with tears. She knows it is the work of Orlok.
  EXPRESSION: Devastated

::SCENE::
LOCATION: Harding House. Rear Drawing Room
MOOD: Despair, Confusion
CHARACTERS: Harding, Sievers, Von Franz
BACKGROUND_IMAGE: harding_house_rear_drawing_room.png
BACKGROUND_EDIT: "Afternoon. Harding looks broken. Sievers and Von Franz are with him. The Christmas tree is unlit."

::SCRIPT::
- CHARACTER: Sievers
  LINE: I could not bring myself to tell Anna the source of her illness.
  EXPRESSION: Reluctant, Guilty
- CHARACTER: Harding
  LINE: This is madness!
  EXPRESSION: Agitated
- CHARACTER: Sievers
  LINE: And Friedrich, it seems Herr Knock is in league with the creature.
  EXPRESSION: Informative, Troubled
- CHARACTER: Von Franz
  LINE: Our Nosferatu is of an especial malignancy. He is an arch-enchanter, Şolomonari, Satan’s own learnèd disciple.
  EXPRESSION: Explanatory, Grave
- CHARACTER: Harding
  LINE: What say you?
  EXPRESSION: Desperate
- CHARACTER: Von Franz
  LINE: Further elucidation leads only to insanity. Hence the misfortune of Herr Knock’s decent. Our somnambulist and her husband are in incomparable danger!
  EXPRESSION: Grave, Warning
- CHARACTER: Harding
  LINE: I sent them home.
  EXPRESSION: Resigned, Regretful
- CHARACTER: Von Franz
  LINE: I must see them.
  EXPRESSION: Determined
- CHARACTER: Harding
  LINE: (Is about to burst, he is desperate:) How can this perversion be killed?
  EXPRESSION: Desperate, Anguished
- CHARACTER: Von Franz
  LINE: I don’t know. You sent them home?
  EXPRESSION: Uncertain, Questioning
- CHARACTER: Harding
  LINE: (Overlapping) What?
  EXPRESSION: Confused
- CHARACTER: Von Franz
  LINE: You sent them home?
  EXPRESSION: Repeating, Questioning
- CHARACTER: Harding
  LINE: (Overlapping) Not that – Yes, I did – You don’t know?
  EXPRESSION: Frustrated, Desperate
- CHARACTER: Von Franz
  LINE: Precisely. Correct. I do not know. I have never encountered Nosferatu first hand.
  EXPRESSION: Honest, Unsure
- CHARACTER: Narrator
  LINE: (Pause. Everyone is dismayed.)
  EXPRESSION: Dismayed
- CHARACTER: Harding
  LINE: He doesn’t know.
  EXPRESSION: Devastated
- CHARACTER: Von Franz
  LINE: (Overlapping, ignoring) Their efficacy is plainly unknown. Boiling wine, a spike of cold iron transpiercing the navel, decapitation, incineration... Yet there is one i
  EXPRESSION: Thoughtful, Pondering

::SCENE::
LOCATION: Study
MOOD: Intense Discussion
CHARACTERS: Narrator, Sievers, Von Franz
BACKGROUND_IMAGE: von_franz_study.png
BACKGROUND_EDIT: "Night, cluttered study with books"

::SCRIPT::
- CHARACTER: Narrator
  LINE: ...variable fact that interests me most...
  EXPRESSION: null
- CHARACTER: Sievers
  LINE: Go on.
  EXPRESSION: null
- CHARACTER: Von Franz
  LINE: In every account, the Nosferatu must return to the earth wherein it was buried, by the first crow of cock.
  EXPRESSION: null
- CHARACTER: Sievers
  LINE: It must sleep in its grave by day. What happens if it does not?
  EXPRESSION: Thoughtful
- CHARACTER: Von Franz
  LINE: That, my dear Sievers, is the question.
  EXPRESSION: Mysterious

::PATHS::
- CHOICE: "Continue discussion"
  TARGET: harding_reaction
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Study
MOOD: Escalating Panic
CHARACTERS: Narrator, Harding, Sievers, Von Franz
BACKGROUND_IMAGE: harding_panic.png
BACKGROUND_EDIT: "Night, tense atmosphere"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Harding begins to laugh. They turn to him. He keeps laughing.
  EXPRESSION: Unhinged
- CHARACTER: Harding
  LINE: Oh, my God. My God! I am shattering – I’m breaking apart. Get out. Take your leave at once.
  EXPRESSION: Hysterical
- CHARACTER: Sievers
  LINE: Harding?
  EXPRESSION: Concerned
- CHARACTER: Harding
  LINE: Both of you, go!
  EXPRESSION: Enraged
- CHARACTER: Sievers
  LINE: Friedrich, please, we don’t wish to –
  EXPRESSION: Pleading
- CHARACTER: Harding
  LINE: Can’t you see there is a bloody real plague, gentlemen? A real epidemic that is really killing real people? Jesus Christ in heaven! This isn’t a Satanic magician, or any other humiliating fantasy. It’s no wonder you’re a laughing stock. Out!
  EXPRESSION: Desperate
- CHARACTER: Sievers
  LINE: Damn you, Friedrich!
  EXPRESSION: Angry
- CHARACTER: Harding
  LINE: My Anna was bitten by vermin. Rats. No more. Tomorrow we are leaving Wisburg –
  EXPRESSION: Determined
- CHARACTER: Sievers
  LINE: But the quarantine... Tomorrow we close off the city.
  EXPRESSION: Shocked
- CHARACTER: Harding
  LINE: I’m not going to let your vain-madness kill my wife!
  EXPRESSION: Fierce
- CHARACTER: Von Franz
  LINE: The night-daemon has supped of your good wife’s blood and shall return for the rest!
  EXPRESSION: Ominous
- CHARACTER: Harding
  LINE: Leave!
  EXPRESSION: Commanding
- CHARACTER: Von Franz
  LINE: The Nosferatu will never cease unless it is destroyed!
  EXPRESSION: Grave

::PATHS::
- CHOICE: "Leave the study"
  TARGET: harding_house_nursery
  STATE_CHANGE: alarm = +2
  CONDITION: null

::SCENE::
LOCATION: Harding House. Nursery
MOOD: Heartbreaking
CHARACTERS: Narrator, Harding
BACKGROUND_IMAGE: harding_nursery.png
BACKGROUND_EDIT: "Moments later, nursery with toys strewn about"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Harding embraces his children tightly, sitting on the floor of the nursery, trying to stay strong. Toys lay strewn about around them, looking somehow mournful.
  EXPRESSION: Grief-stricken

::PATHS::
- CHOICE: "Tend to the sick"
  TARGET: hutter_house_parlour
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Hutter House. Parlour
MOOD: Desperate Love
CHARACTERS: Narrator, Ellen, Thomas
BACKGROUND_IMAGE: hutter_parlour.png
BACKGROUND_EDIT: "Night, sickbed on a sofa"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Ellen sits on the floor attending Thomas. She has made a sickbed on the sofa for him.
  EXPRESSION: Devoted
- CHARACTER: Narrator
  LINE: He opens his eyes...
  EXPRESSION: Hopeful
- CHARACTER: Ellen
  LINE: Thomas...
  EXPRESSION: Relieved
- CHARACTER: Narrator
  LINE: Ellen embraces him. He must save them. He struggles to speak. His mind races.
  EXPRESSION: Hopeful
- CHARACTER: Thomas
  LINE: Ellen, my love. We must go. We must flee the city. You’re in danger. You knew–
  EXPRESSION: Urgent
- CHARACTER: Ellen
  LINE: We cannot run.
  EXPRESSION: Resigned
- CHARACTER: Thomas
  LINE: We must –
  EXPRESSION: Pleading
- CHARACTER: Ellen
  LINE: There is something I must tell you. Something so loathsome, so base –
  EXPRESSION: Ashamed
- CHARACTER: Thomas
  LINE: Nothing you can say will shake me – for there is a devil in this world, and I have met him. And he... I cannot speak it – he is come to Wisburg... for you.
  EXPRESSION: Terrified
- CHARACTER: Ellen
  LINE: I know.
  EXPRESSION: Knowing
- CHARACTER: Thomas
  LINE: What?
  EXPRESSION: Confused
- CHARACTER: Ellen
  LINE: I know him.
  EXPRESSION: Certain
- CHARACTER: Thomas
  LINE: Know him?
  EXPRESSION: Disbelieving
- CHARACTER: Ellen
  LINE: I have brought this evil upon us.
  EXPRESSION: Guilty
- CHARACTER: Narrator
  LINE: Thomas is shocked.
  EXPRESSION: Shocked
- CHARACTER: Ellen
  LINE: I have never shared my secret with any soul. I sought company, I sought tenderness, and I called out...
  EXPRESSION: Confessional
- CHARACTER: Thomas
  LINE: Ellen –
  EXPRESSION: Concerned
- CHARACTER: Ellen
  LINE: But Thomas, it was you that gave me the courage to be free of my shame – you!
  EXPRESSION: Grateful
- CHARACTER: Thomas
  LINE: What are you telling me?
  EXPRESSION: Bewildered
- CHARACTER: Ellen
  LINE: Don’t you understand?
  EXPRESSION: Impatient
- CHARACTER: Thomas
  LINE: You cannot understand?
  EXPRESSION: Desperate
- CHARACTER: Ellen
  LINE: No!
  EXPRESSION: Frustrated
- CHARACTER: Thomas
  LINE: He is my shame! He is my melancholy! He took me as his lover then, and now he has come back. He has discovered our marriage and has come back!
  EXPRESSION: Agitated
- CHARACTER: Ellen
  LINE: Impossible.
  EXPRESSION: Disbelieving
- CHARACTER: Narrator
  LINE: Thomas goes to her. She avoids him as if she were poison.
  EXPRESSION: Repulsed
- CHARACTER: Ellen
  LINE: Don’t touch me. I am not to be touched.
  EXPRESSION: Revulsed
- CHARACTER: Narrator
  LINE: Slowly, a shadow passes through the room, Orlok’s breath is heard.
  EXPRESSION: Eerie
- CHARACTER: Narrator
  LINE: The Shadow passes over Ellen. Her eyes change. Her tone becomes leaden.
  EXPRESSION: Transformed
- CHARACTER: Ellen
  LINE: You stopped your letters to me.
  EXPRESSION: Accusatory
- CHARACTER: Thomas
  LINE: What?
  EXPRESSION: Confused
- CHARACTER: Ellen
  LINE: You promised to write to me every day. Did not you think of me in that castle?
  EXPRESSION: Bitter
- CHARACTER: Thomas
  LINE: I did, I–
  EXPRESSION: Defensive
- CHARACTER: Ellen
  LINE: Lies.
  EXPRESSION: Scathing
- CHARACTER: Thomas
  LINE: After what you have just confessed, how can you –
  EXPRESSION: Indignant
- CHARACTER: Ellen
  LINE: He told me about you. He told me how foolish you were. How fearful. How like a child. How you fell into his arms as a swooning lily of a woman.
  EXPRESSION: Mocking
- CHARACTER: Thomas
  LINE: Ellen!
  EXPRESSION: Anguished
- CHARACTER: Ellen
  LINE: He told me how you sold me to him for gold.
  EXPRESSION: Bitterly
- CHARACTER: Thomas
  LINE: I–
  EXPRESSION: Speechless
- CHARACTER: Narrator
  LINE: Ellen rises from the sofa.
  EXPRESSION: Confrontational
- CHARACTER: Ellen
  LINE: Well where is it? Your money? Your promotion? Your house? Where is that which is so precious to you? Have you paid back kind Harding your debt? Have you repaid him with this plague that infects his wife?
  EXPRESSION: Furious
- CHARACTER: Thomas
  LINE: I left for us, for our future...
  EXPRESSION: Pleading
- CHARACTER: Ellen
  LINE: For what? For what? For these... things?!
  EXPRESSION: Disgusted
- CHARACTER: Narrator
  LINE: Ellen gestures to the furnishing of the house.
  EXPRESSION: Contemptuous
- CHARACTER: Thomas
  LINE: For you!
  EXPRESSION: Desperate
- CHARACTER: Narrator
  LINE: Ellen shrieks:
  EXPRESSION: Unhinged
- CHARACTER: Ellen
  LINE: It doesn’t matter! It doesn’t matter!!
  EXPRESSION: Hysterical
- CHARACTER: Narrator
  LINE: Ellen is possessed by anger. She throws china off the shelves... Tearing the room to pieces... totally unhinged!
  EXPRESSION: Manic
- CHARACTER: Ellen
  LINE: Can’t you see?! It doesn’t matter! We should never have married! We are already dead!
  EXPRESSION: Screaming
- CHARACTER: Narrator
  LINE: She screams uncontrollably on the floor! Flailing her arms. The veins in her head look like they will explode, her eyes crossing. Her hands shake. IT IS UNCANNY. DEMONIC. More extreme than she has ever been before. ELLEN BEGINS RIPPING HER CLOTHES APART... TEARING AT HER BODICE...
  EXPRESSION: Demonic
- CHARACTER: Thomas
  LINE: I shall send for Doctor Sievers.
  EXPRESSION: Determined
- CHARACTER: Narrator
  LINE: She quickly changes her tone.
  EXPRESSION: Shifting
- CHARACTER: Ellen
  LINE: No! No!!
  EXPRESSION: Desperate
- CHARACTER: Narrator
  LINE: She is desperate, crying, she crawls to her husband... She grabs his legs to hold him back..
  EXPRESSION: Pleading
- CHARACTER: Ellen
  LINE: Please. I’ll be good, I’ll be good.
  EXPRESSION: Submissive
- CHARACTER: Narrator
  LINE: She places her cheek against his thigh, slowly looking up at him... she whispers in the most sensual and taunting tone:
  EXPRESSION: Seductive
- CHARACTER: Ellen
  LINE: You could never please me as he could.
  EXPRESSION: Taunting
- CHARACTER: Narrator
  LINE: Thomas becomes enraged with insane jealousy! He throws her to the sickbed... she unbuttons his trousers... he lifts her skirts... and they begin making love.
  EXPRESSION: Frenzied
- CHARACTER: Ellen
  LINE: Kiss me.
  EXPRESSION: Demanding
- CHARACTER: Narrator
  LINE: He does.
  EXPRESSION: Obedient
- CHARACTER: Ellen
  LINE: Again.
  EXPRESSION: Insistent
- CHARACTER: Narrator
  LINE: He does.
  EXPRESSION: Obedient
- CHARACTER: Ellen
  LINE: Again. Kiss me here. Kiss my heart.
  EXPRESSION: Demanding
- CHARACTER: Narrator
  LINE: He does. ELLEN becomes more aggressive.
  EXPRESSION: Aggressive
- CHARACTER: Ellen
  LINE: Let him see. Let him see our love!
  EXPRESSION: Provocative
- CHARACTER: Narrator
  LINE: She pushes his head into her heart. Her moaning is animal-like. She opens his shirt... she sees THE VAMPIRE BITE. She kisses and licks it... he pulls her from his chest, afraid... She is beyond human passion...
  EXPRESSION: Wild
- CHARACTER: Narrator
  LINE: IMAGE: ELLEN, NAKED – HER WHITE FACE – HER MOUTH DRIPPING WITH RED BLOOD – HER EYES INSANE!!
  EXPRESSION: Monstrous
- CHARACTER: Narrator
  LINE: Thomas recoils, terrified by the fleeting image he saw!
  EXPRESSION: Terrified
- CHARACTER: Thomas
  LINE: Ellen!
  EXPRESSION: Horrified
- CHARACTER: Narrator
  LINE: She looks him in the eye and laughs in a frightening manner, trying to pull him back in to her...
  EXPRESSION: Frightening
- CHARACTER: Ellen
  LINE: You have unloosed a demon!
  EXPRESSION: Triumphant
- CHARACTER: Thomas
  LINE: Ellen, wake from this. I love you! I love you.
  EXPRESSION: Pleading
- CHARACTER: Narrator
  LINE: Something changes. ELLEN’S laughter turns to shame, to tears. She sobs in horror. THOMAS embraces her.
  EXPRESSION: Despairing
- CHARACTER: Thomas
  LINE: Forgive me, please.
  EXPRESSION: Remorseful
- CHARACTER: Ellen
  LINE: Keep away from me – I am unclean!
  EXPRESSION: Horrified
- CHARACTER: Thomas
  LINE: Never!
  EXPRESSION: Determined
- CHARACTER: Ellen
  LINE: He will murder you if I do not go to him. We will be torn apart and all will be despair.
  EXPRESSION: Fearful
- CHARACTER: Narrator
  LINE: Thomas holds her tight, his eyes blaze mercilessly.
  EXPRESSION: Vengeful
- CHARACTER: Thomas
  LINE: I’ll kill him! He shall never harm you again. Never!
  EXPRESSION: Fierce
- CHARACTER: Narrator
  LINE: ELLEN fears it is impossible.
  EXPRESSION: Hopeless

::PATHS::
- CHOICE: "Confront the enemy"
  TARGET: von_franz_study_night
  STATE_CHANGE: resolve = +1
  CONDITION: null

::SCENE::
LOCATION: Von Franz’s Study
MOOD: Scholarly Investigation
CHARACTERS: Narrator, Von Franz
BACKGROUND_IMAGE: von_franz_study_night.png
BACKGROUND_EDIT: "Night, desk with books, an open book"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Von Franz sits at his desk surrounded with books. He opens up Knock’s book with THE E
  EXPRESSION: null

::PATHS::
- CHOICE: "Examine the book"
  TARGET: end
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Unknown
MOOD: Mysterious
CHARACTERS: Narrator, Von Franz
BACKGROUND_IMAGE: unknown_location.png
BACKGROUND_EDIT: "Close up on a book cover"

::SCRIPT::
- CHARACTER: Narrator
  LINE: VIL EYE on the cover. It is written in the language of the ŞOLOMONARI.
  EXPRESSION: null
- CHARACTER: Von Franz
  LINE: And so the maiden fair did offer up, Her love unto the beast, and with him lay, In close embrace until the first cock crow.
  EXPRESSION: Reading
- CHARACTER: Narrator
  LINE: He turns to an ILLUSTRATION... IT IS A MEDIEVAL WOODCUT OF A YOUNG WOMAN EMBRACING A NOSFERATU-LIKE CORPSE IN BED.
  EXPRESSION: null
- CHARACTER: Von Franz
  LINE: Her willing sacrifice thus broke the curse, And freed them from the plague of Nosferatu.
  EXPRESSION: Reading
- CHARACTER: Narrator
  LINE: VON FRANZ’ eyes turn inspired. Prophetic.
  EXPRESSION: null
- CHARACTER: Von Franz
  LINE: She is the way.
  EXPRESSION: Inspired

::SCENE::
LOCATION: Hutter House. Parlour
MOOD: Ominous
CHARACTERS: Narrator, Thomas, Ellen, Orlok
BACKGROUND_IMAGE: hutter_house_parlour.png
BACKGROUND_EDIT: "Nighttime interior, Thomas holding Ellen, Orlok's shadow looming"

::SCRIPT::
- CHARACTER: Narrator
  LINE: As THOMAS holds ELLEN in his arms, ORLOK’S SHADOW passes over, taking her into his dark dreamworld. He whispers to her:
  EXPRESSION: null
- CHARACTER: Orlok (V.O.)
  LINE: More blood shall stain thy hands, another night has passed. Tomorrow night, the third, shall be his last.
  EXPRESSION: Subtitled

::SCENE::
LOCATION: Harding House. Master Bedchamber
MOOD: Desperate
CHARACTERS: Narrator, Anna, Harding, Orlok
BACKGROUND_IMAGE: harding_house_master_bedchamber.png
BACKGROUND_EDIT: "Nighttime interior, Anna near death in bed, Harding asleep beside her"

::SCRIPT::
- CHARACTER: Narrator
  LINE: ANNA is in bed. She is near death. She hears her children crying in the nursery... strange and muffled...
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: She turns to HARDING asleep by her side, fully clothed. One hand on hers, the other on a pistol. There is a ghostly SHADOW above him.
  EXPRESSION: null
- CHARACTER: Orlok (V.O.)
  LINE: Wake not.
  EXPRESSION: Subtitled
- CHARACTER: Narrator
  LINE: ORLOK’S SHADOW quickly ascends away from him like a viper.
  EXPRESSION: null
- CHARACTER: Clara And Louise (O.S.)
  LINE: The Monster! The Monster!!
  EXPRESSION: Fearful
- CHARACTER: Narrator
  LINE: ANNA tries to rouse HARDING, shaking him, shaking him with all her might – but he will not wake.
  EXPRESSION: null
- CHARACTER: Anna
  LINE: Friedrich!
  EXPRESSION: Desperate
- CHARACTER: Narrator
  LINE: A spell is over him. She rushes out of bed...
  EXPRESSION: null

::SCENE::
LOCATION: Harding House. Upstairs Hallway
MOOD: Terrifying
CHARACTERS: Narrator, Anna
BACKGROUND_IMAGE: harding_house_upstairs_hallway.png
BACKGROUND_EDIT: "Nighttime interior, Anna running down hallway"

::SCRIPT::
- CHARACTER: Narrator
  LINE: ANNA RUNS TO SAVE HER CHILDREN. THEY SCREAM LIKE MUTILATED ANIMALS.
  EXPRESSION: null

::SCENE::
LOCATION: Harding House. Nursery
MOOD: Horrific
CHARACTERS: Narrator, Anna, Orlok
BACKGROUND_IMAGE: harding_house_nursery.png
BACKGROUND_EDIT: "Nighttime interior, nursery, Orlok dropping children's bodies"

::SCRIPT::
- CHARACTER: Narrator
  LINE: She bursts into the nursery... She looks... Silhouetted by the window, ORLOK DROPS THE LIFELESS BODIES OF HER CHILDREN FROM HIS CLAWS... they thump upon the floor.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: ANNA is emotionally obliterated – paralysed with fear. She tries to go to her children... she can’t move. Her eyes well up with tears. She can’t scream. She chokes. She begins to shake with insanity, tears flowing from her eyes...
  EXPRESSION: Devastated
- CHARACTER: Narrator
  LINE: ORLOK approaches... He leaps upon her, engulfing her.
  EXPRESSION: null

::SCENE::
LOCATION: Wisburg Cemetery
MOOD: Somber
CHARACTERS: Narrator, Harding, Servants, Ellen, Thomas, Sievers, Von Franz
BACKGROUND_IMAGE: wisburg_cemetery.png
BACKGROUND_EDIT: "Daytime, overcast, a funeral procession"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Never was a day more leaden with sorrow. HARDING and two of his SERVANTS carry ANNA’S BLACK CASKET out of the hearse, into the cemetery gates. PALLBEARERS follow with TWO WHITE CHILDREN’S CASKETS. The tall, leafless linden trees that grow between headstones seem to mourn the dead.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: ELLEN, THOMAS, and SIEVERS have also gathered, unknown to HARDING. They watch from afar.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: ELLEN looks through her black veil as the pallbearers take the caskets into the HARDING FAMILY TOMB – a stately mausoleum.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: HARDING tries to stay composed as the tomb is closed, but he is a broken man. He is deathly pale, his eyes red. Is he, too, infected?
  EXPRESSION: null
- CHARACTER: Sievers
  LINE: We must speak to him.
  EXPRESSION: Determined
  TO: Thomas
- CHARACTER: Thomas
  LINE: A moment longer. His grief is too great.
  EXPRESSION: Empathetic
- CHARACTER: Narrator
  LINE: Through the fog and snow emerges VON FRANZ, covering his face with a handkerchief. ELLEN can feel his approach.
  EXPRESSION: null
- CHARACTER: Von Franz
  LINE: More will be taken.
  EXPRESSION: Grave
- CHARACTER: Ellen
  LINE: I know. She was with child.
  EXPRESSION: Sad
- CHARACTER: Von Franz
  LINE: Cover your face, dear creature. The grim reaper wields his heavy scythe with every change of wind.
  EXPRESSION: Warning
- CHARACTER: Ellen
  LINE: Professor, I must speak with you.
  EXPRESSION: Urgent
- CHARACTER: Narrator
  LINE: ELLEN takes VON FRANZ’ hand.
  EXPRESSION: null
- CHARACTER: Von Franz
  LINE: And I would speak with you.
  EXPRESSION: Eager
- CHARACTER: Narrator
  LINE: SUDDENLY...
  EXPRESSION: null
- CHARACTER: Harding
  LINE: Take that blackguard from this place!
  EXPRESSION: Angry
  TO: Von Franz
- CHARACTER: Narrator
  LINE: Harding starts for VON FRANZ!
  EXPRESSION: null
- CHARACTER: Harding
  LINE: Your diseasèd mind has brought all of this outrage -
  EXPRESSION: Enraged
  TO: Von Franz
- CHARACTER: Sievers
  LINE: Stop this!
  EXPRESSION: Commanding
- CHARACTER: Thomas
  LINE: Friedrich! Stop!
  EXPRESSION: Pleading
- CHARACTER: Narrator
  LINE: THOMAS runs limping on his cane, and embraces HARDING. THOMAS is a man possessed!
  EXPRESSION: null
- CHARACTER: Thomas
  LINE: Please, it is my fault! Forgive me my dear, sweet friend!
  EXPRESSION: Hysterical
  TO: Harding
- CHARACTER: Narrator
  LINE: THOMAS holds HARDING BACK.
  EXPRESSION: null
- CHARACTER: Harding
  LINE: This moment doesn’t concern you, Thomas!
  EXPRESSION: Dismissive
  TO: Thomas
- CHARACTER: Thomas
  LINE: Friedrich! These nightmares do exist! They exist!
  EXPRESSION: Hysterical
  TO: Harding
- CHARACTER: Narrator
  LINE: In hysterics, THOMAS tears open his shirt and shows him HIS VAMPIRE BITE!
  EXPRESSION: null

::SCENE::
LOCATION: Coach. Wisburg Street
MOOD: Tense
CHARACTERS: Narrator, Ellen, Thomas, Von Franz, Sievers, Harding
BACKGROUND_IMAGE: coach_interior.png
BACKGROUND_EDIT: "Daytime interior of a cramped coach, windows sealed"

::SCRIPT::
- CHARACTER: Narrator
  LINE: They are all crammed in a stuffy coach. Windows sealed. ELLEN is next to THOMAS.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: VON FRANZ looks at ELLEN through her veil.
  EXPRESSION: null
- CHARACTER: Sievers
  LINE: And he shows no sign of the blood plague.
  EXPRESSION: Observant
  TO: Von Franz
- CHARACTER: Thomas
  LINE: The good sisters sought to nurse me back to health with their prayer ... Yet I fear I am not free of his spell–
  EXPRESSION: Troubled
- CHARACTER: Von Franz
  LINE: Trust in God and your strength. The monster left you to the wolves, and yet you prevailed.
  EXPRESSION: Encouraging
- CHARACTER: Sievers
  LINE: Harding!
  EXPRESSION: Concerned
  TO: Harding
- CHARACTER: Narrator
  LINE: HARDING has passed out! SIEVERS shakes him awake. He is white as a ghost. He looks as if he has a brain fever, his eyes darting about – aflame at one moment, nearly lustreless the next. He struggles to speak.
  EXPRESSION: null
- CHARACTER: Harding
  LINE: Forgive me. I am not myself. I... Please, forgive me, all of you. My reason could not accept... accept...
  EXPRESSION: Weak
- CHARACTER: Sievers
  LINE: Strength, man. Strength.
  EXPRESSION: Encouraging
- CHARACTER: Von Franz
  LINE: Orlok has kept his coffin within Grünewald Manor?
  EXPRESSION: Questioning
- CHARACTER: Thomas
  LINE: Assuredly.
  EXPRESSION: Certain
- CHARACTER: Von Franz
  LINE: Under our very noses. Tonight we destroy the beast!
  EXPRESSION: Determined
- CHARACTER: Ellen
  LINE: Let me come with you.
  EXPRESSION: Determined
- CHARACTER: Thomas
  LINE: Of course not, Ellen. You must be kept safe away.
  EXPRESSION: Protective
- CHARACTER: Von Franz
  LINE: We shall meet at Harding’s and depart to Grünewald Manor.
  EXPRESSION: Decisive
- CHARACTER: Harding
  LINE: Please. The readiness is all.
  EXPRESSION: Resigned
- CHARACTER: Narrator
  LINE: Harding says vehemently, yet his thoughts seem far away.
  EXPRESSION: null
- CHARACTER: Von Franz
  LINE: We shall sanctify the earth wherein he was buried, and destroy the sarcophagus, then he can have no sanctuary at cock crow.
  EXPRESSION: Strategic
- CHARACTER: Narrator
  LINE: ELLEN looks at VON FRANZ.
  EXPRESSION: null
- CHARACTER: Sievers
  LINE: And when we uncover his body?
  EXPRESSION: Inquisitive
- CHARACTER: Thomas
  LINE: I will drive a spike of cold iron through him!
  EXPRESSION: Vengeful
- CHARACTER: Narrator
  LINE: VON FRANZ looks at ELLEN.
  EXPRESSION: null
- CHARACTER: Ellen
  LINE: What if it does not work?
  EXPRESSION: Anxious
- CHARACTER: Narrator
  LINE: ELLEN keeps staring at VON FRANZ. Determination in her eyes.
  EXPRESSION: null
- CHARACTER: Thomas
  LINE: It must.
  EXPRESSION: Hopeful
- CHARACTER: Narrator
  LINE: The carriage stops.
  EXPRESSION: null
- CHARACTER: Ellen
  LINE: Professor, allow me to walk you to your door?
  EXPRESSION: Polite

::SCENE::
LOCATION: Slums. Von Franz’s Boarding House
MOOD: Secretive
CHARACTERS: Narrator, Ellen, Von Franz, Husband
BACKGROUND_IMAGE: von_franz_boarding_house.png
BACKGROUND_EDIT: "Daytime, exterior of a boarding house, Ellen and Von Franz walking arm-in-arm"

::SCRIPT::
- CHARACTER: Narrator
  LINE: ELLEN walks arm in arm with VON FRANZ. She is stiff, her head forward, trying not to give away her secret conversation, as her husband is watching from the carriage.
  EXPRESSION: null
- CHARACTER: Ellen
  LINE: I must know... why me, professor?
  EXPRESSION: Pleading
  TO: Von Franz
- CHARACTER: Von Franz
  LINE: I am but an able tourist in this occult world, you were born to it. You tell me why.
  EXPRESSION: Cryptic
  TO: Ellen
- CHARACTER: Ellen
  LINE: His pull on me is so terrible, so powerful – yet my spirit cannot be evil as his.
  EXPRESSION: Conflicted
- CHARACTER: Von Franz
  LINE: We must know evil to be able to destroy it, we must discover it within ourselves. And when we have, we must crucify the evil within us, or there is no salvation.
  EXPRESSION: Philosophical
  TO: Ellen
- CHARACTER: Ellen
  LINE: I need no salvation. My entire life I have done no ill but heed my nature.
  EXPRESSION: Resolute
- CHARACTER: Von Franz
  LINE: Then harken to it. I fear Nosfe
  EXPRESSION: Concerned

::SCENE::
LOCATION: Hutters House. Parlour
MOOD: Desperate, Foreboding
CHARACTERS: Narrator, Thomas, Von Franz, Ellen
BACKGROUND_IMAGE: hutter_house_parlour.png
BACKGROUND_EDIT: "Afternoon, parlour with a window covered in garlic and whitethorn wreaths. Makeshift undertakers carry coffins down an abandoned street outside. Fires burn, rats feed on dead horses and dogs."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Ratu is impervious to any of our iron stakes. I believe only you have the faculty to redeem us.
  EXPRESSION: null
- CHARACTER: Thomas (O.S.)
  LINE: Ellen! Let us make haste.
  EXPRESSION: Urgent
- CHARACTER: Von Franz
  LINE: In heathen times you might have been a great priestess of Isis. Yet, in this strange and modern world your purpose is of greater worth.
  EXPRESSION: Admiring
- CHARACTER: Narrator
  LINE: Ellen looks at Von Franz with an eternal calm. She smiles. She has always known what is destined.
  EXPRESSION: Calm
- CHARACTER: Ellen
  LINE: Thank you.
  EXPRESSION: Grateful
- CHARACTER: Narrator
  LINE: She kisses his hand.
  EXPRESSION: Affectionate
- CHARACTER: Von Franz
  LINE: I will keep your husband at bay tonight. Go now. Go home. Attend him that he is sturdy for this false hunt.
  EXPRESSION: Protective

::SCENE::
LOCATION: Hutters House. Parlour
MOOD: Somber, Determined
CHARACTERS: Narrator, Ellen, Thomas
BACKGROUND_IMAGE: hutter_house_parlour_afternoon.png
BACKGROUND_EDIT: "Afternoon. Ellen sits by a window covered in wreaths of garlic and whitethorn. Through the wavy glass, makeshift undertakers carry coffins down an abandoned street. Fires burn. Rats feed on dead horses and dogs. The city is a morgue. She knows what she must do. No more shall die from this."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Ellen sits by a window covered in wreaths of garlic and whitethorn. She looks through the wavy glass: makeshift undertakers carry coffins down an abandoned street. Fires burn. Rats feed on dead horses and dogs. The city is a morgue. SHE KNOWS WHAT SHE MUST DO. NO MORE SHALL DIE FROM THIS.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Thomas kisses her head, wearing his coat, ready to leave.
  EXPRESSION: Affectionate
- CHARACTER: Ellen
  LINE: You will put an end to all of this?
  EXPRESSION: Hopeful
- CHARACTER: Narrator
  LINE: She has to be sure that she will be left alone this night. This is a loving deceit, a vital deceit.
  EXPRESSION: null
- CHARACTER: Ellen
  LINE: You promise you shan't return to me ‘til he is no more? Promise you won’t return-
  EXPRESSION: Pleading
- CHARACTER: Thomas
  LINE: I promise.
  EXPRESSION: Assuring
- CHARACTER: Ellen
  LINE: He does not have power over you, Thomas.
  EXPRESSION: Reassuring
- CHARACTER: Narrator
  LINE: They embrace. Tears fall from her eyes. She knows this moment is their last together.
  EXPRESSION: Heartbroken
- CHARACTER: Ellen
  LINE: I place my utter faith in you. I love you.
  EXPRESSION: Devoted
- CHARACTER: Thomas
  LINE: Cry not.
  EXPRESSION: Comforting
- CHARACTER: Narrator
  LINE: Their final kiss. Thomas leaves, ever empowered by his wife.
  EXPRESSION: Melancholy
- CHARACTER: Narrator
  LINE: HOLD ON: ELLEN, feeling her imminent destiny stir within her.
  EXPRESSION: null
- CHARACTER: Ellen
  LINE: Goodbye.
  EXPRESSION: Resigned

::SCENE::
LOCATION: Harding House. Drawing Room
MOOD: Tense, Determined
CHARACTERS: Narrator, Thomas, Sievers, Von Franz, Hartman
BACKGROUND_IMAGE: harding_house_drawing_room.png
BACKGROUND_EDIT: "Daytime. Thomas, Sievers, and Von Franz stand with weapons ready, as vampire hunters."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Thomas, Sievers, and Von Franz stand with weapons ready, as vampire hunters.
  EXPRESSION: null
- CHARACTER: Sievers
  LINE: He is not here?
  EXPRESSION: Anxious
- CHARACTER: Hartman
  LINE: No, Herr Harding has departed, sir.
  EXPRESSION: Respectful
- CHARACTER: Thomas
  LINE: Where could he have gone?
  EXPRESSION: Concerned
- CHARACTER: Von Franz
  LINE: He has a heavy grief. We shall wait for him. There is time yet ‘til sundown.
  EXPRESSION: Calm
- CHARACTER: Narrator
  LINE: Von Franz casually lights his pipe.
  EXPRESSION: Relaxed
- CHARACTER: Thomas
  LINE: No. We must find him.
  EXPRESSION: Urgent

::SCENE::
LOCATION: Wisburg Cemetery
MOOD: Eerie, Tragic
CHARACTERS: Narrator, Harding
BACKGROUND_IMAGE: wisburg_cemetery_dusk.png
BACKGROUND_EDIT: "Dusk. Snow falls. Harding wanders in the blue twilight. He approaches his family tomb. The red marks of sepsis are on his haunted face, discharge in his eyes. He has the plague."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Harding wanders in the blue twilight. Snow falls. He approaches his FAMILY TOMB. The red marks of sepsis are on his haunted face, discharge in his eyes. HE HAS THE PLAGUE.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: As he unlocks the vault, without noticing, he lets his huge fur coat fall off of his shoulders into the snow.
  EXPRESSION: Careless

::SCENE::
LOCATION: Harding Family Tomb
MOOD: Sorrowful, Delirious
CHARACTERS: Narrator, Harding
BACKGROUND_IMAGE: harding_family_tomb_interior.png
BACKGROUND_EDIT: "Moments later. Harding seems in a trance, his eyes full of tears."

::SCRIPT::
- CHARACTER: Narrator
  LINE: He seems in a trance, his eyes full of tears.
  EXPRESSION: null
- CHARACTER: Harding
  LINE: Clara. Louise. My girls.
  EXPRESSION: Grief-stricken
- CHARACTER: Narrator
  LINE: He gently touches their coffins as he walks by them, with a melancholy smile, as if stroking his daughters’ cheeks.
  EXPRESSION: Tender

::SCENE::
LOCATION: Wisburg Street
MOOD: Urgent, Panicked
CHARACTERS: Narrator, Harding, The Vampire Hunters, Thomas, Sievers, Von Franz
BACKGROUND_IMAGE: wisburg_street_dusk.png
BACKGROUND_EDIT: "Dusk. The vampire hunters call for Harding. Thomas limps on his cane."

::SCRIPT::
- CHARACTER: Narrator
  LINE: THE VAMPIRE HUNTERS call for HARDING. THOMAS limps on his cane.
  EXPRESSION: null

::SCENE::
LOCATION: Harding Family Tomb
MOOD: Desperate, Heartbreaking
CHARACTERS: Narrator, Harding, Anna
BACKGROUND_IMAGE: harding_family_tomb_interior_dusk.png
BACKGROUND_EDIT: "Dusk. Harding sees Anna's coffin on a stone bier."

::SCRIPT::
- CHARACTER: Narrator
  LINE: HARDING sees ANNA’S COFFIN on a stone bier.
  EXPRESSION: null
- CHARACTER: Harding
  LINE: Anna. Your bed is so dark, so small.
  EXPRESSION: Heartbroken
- CHARACTER: Narrator
  LINE: He hugs and caresses the lid.
  EXPRESSION: Affectionate
- CHARACTER: Harding
  LINE: Anna, my love. Our son ... our little son ... forgive me. I shall never sleep again. Never.
  EXPRESSION: Devastated
- CHARACTER: Narrator
  LINE: He breathes with desire, slowly opening the coffin. He takes her limp head passionately in his arms. Suddenly... he is seized with an internal haemorrhage... the plague ripping at him. Blood trickles from his mouth. But his love for his wife is enough to withstand the pain.
  EXPRESSION: Passionate
- CHARACTER: Harding
  LINE: Let this your tender embrace keep me now in bliss, away from everlasting sleep.
  EXPRESSION: Ecstatic
- CHARACTER: Narrator
  LINE: Quivering with passion, and in his death throes, he brings his wife’s cold lips to his.
  EXPRESSION: Tragic

::SCENE::
LOCATION: Harbour
MOOD: Frantic, Urgent
CHARACTERS: Narrator, The Vampire Hunters, Thomas, Sievers, Von Franz
BACKGROUND_IMAGE: harbour_dusk.png
BACKGROUND_EDIT: "Dusk. The vampire hunters run through the abandoned harbour."

::SCRIPT::
- CHARACTER: Narrator
  LINE: THE VAMPIRE HUNTERS run through the abandoned harbour.
  EXPRESSION: null
- CHARACTER: Sievers and Von Franz
  LINE: Harding! Harding!
  EXPRESSION: Shouting
- CHARACTER: Thomas
  LINE: I know where he has gone!
  EXPRESSION: Determined

::SCENE::
LOCATION: Cemetery
MOOD: Urgent, Foreboding
CHARACTERS: Narrator, The Vampire Hunters, Thomas, Sievers, Von Franz
BACKGROUND_IMAGE: cemetery_night.png
BACKGROUND_EDIT: "Night. The vampire hunters run through the cemetery."

::SCRIPT::
- CHARACTER: Narrator
  LINE: THE VAMPIRE HUNTERS run through the cemetery.
  EXPRESSION: null

::SCENE::
LOCATION: Harding Family Tomb
MOOD: Shocking, Tragic
CHARACTERS: Narrator, Thomas, Von Franz, Anna, Harding
BACKGROUND_IMAGE: harding_family_tomb_interior_night.png
BACKGROUND_EDIT: "Night. They dash in... stunned... Thomas lowers his torch."

::SCRIPT::
- CHARACTER: Narrator
  LINE: They dash in... stunned... THOMAS lowers his torch: ANNA’S CASKET IS TUMBLED OVER. SHE LIES HALF INSIDE, HALF ON THE FLOOR... HARDING IS DEAD, TOO. HE HOLDS HER IN HIS ARMS, SKIRTS FLOWING AROUND HER HUSBAND. HER LEG WRAPPED AROUND HIM. HE COULD NOT RESIST HER. THE PLAGUE HAS TAKEN THEM BOTH.
  EXPRESSION: Shocked
- CHARACTER: Thomas
  LINE: I cannot bear anymore!
  EXPRESSION: Devastated
- CHARACTER: Von Franz
  LINE: Set fire to their infected bodies. They must be sanctified.
  EXPRESSION: Grim
- CHARACTER: Thomas
  LINE: Please, we must onward.
  EXPRESSION: Desperate
- CHARACTER: Sievers
  LINE: But Orlok... Will he not have already risen? Should we not return to our homes?
  EXPRESSION: Fearful
- CHARACTER: Thomas
  LINE: No. I will not wait ‘til morning! We must stop him now.
  EXPRESSION: Determined
- CHARACTER: Von Franz
  LINE: Very wise, young Thomas.
  EXPRESSION: Cunning
- CHARACTER: Narrator
  LINE: Von Franz seems somehow suspicious to Thomas. Sievers notices Thomas trembling.
  EXPRESSION: Suspicious
- CHARACTER: Thomas
  LINE: I feel his hold upon me this night.
  EXPRESSION: Terrified
- CHARACTER: Sievers
  LINE: Make haste, Professor!
  EXPRESSION: Urgent
- CHARACTER: Narrator
  LINE: Von Franz prays and nods to Sievers who remorsefully douses the bodies in coal oil. THE MEN slowly lower their torches to cremate their friends.
  EXPRESSION: Somber

::SCENE::
LOCATION: Canal
MOOD: Ominous, Determined
CHARACTERS: Narrator, The Vampire Hunters
BACKGROUND_IMAGE: canal_night.png
BACKGROUND_EDIT: "Night. The vampire hunters drift down the canal in a small boat, torches burning high, toward Grünewald Manor."

::SCRIPT::
- CHARACTER: Narrator
  LINE: THE VAMPIRE HUNTERS drift down the canal in a small boat, torches burning high, toward Grünewald Manor.
  EXPRESSION: null

::SCENE::
LOCATION: Grünewald Manor
MOOD: Menacing
CHARACTERS: Narrator, Orlok
BACKGROUND_IMAGE: grunewald_manor_night_window.png
BACKGROUND_EDIT: "Night. Orlok stands looking out his window. Eyes blazing."

::SCRIPT::
- CHARACTER: Narrator
  LINE: ORLOK stands looking out his window. Eyes blazing.
  EXPRESSION: null

::SCENE::
LOCATION: Hutters House. Bedroom
MOOD: Resolute, Apprehensive
CHARACTERS: Narrator, Ellen
BACKGROUND_IMAGE: hutter_house_bedroom_night.png
BACKGROUND_EDIT: "Night. Ellen sits at her dressing table and lets down her long hair. She looks at herself. She breathes. She is afraid but ready."

::SCRIPT::
- CHARACTER: Narrator
  LINE: ELLEN sits at her dressing table and lets down her long hair. She looks at herself. She breathes. She is afraid but ready.
  EXPRESSION: null

::SCENE::
LOCATION: Grünewald Manor
MOOD: Forceful
CHARACTERS: Narrator, Thomas
BACKGROUND_IMAGE: grunewald_manor_gate_night.png
BACKGROUND_EDIT: "Night. Thomas forces open the old iron gate."

::SCRIPT::
- CHARACTER: Narrator
  LINE: THOMAS forces open the old iron gate.
  EXPRESSION: null
- CHARACTER: Thomas
  LINE: There is a chapel in the rear.
  EXPRESSION: Directing

::SCENE::
LOCATION: Hutters House. Bedroom
MOOD: Mystical, Inviting
CHARACTERS: Narrator, Ellen, Orlok
BACKGROUND_IMAGE: hutter_house_bedroom_night_open_window.png
BACKGROUND_EDIT: "Night. Ellen takes down the garlic and whitethorn. She flings the window open; wind blows. She slowly raises her arms, beckoning, like a sorceress... radiant..."

::SCRIPT::
- CHARACTER: Narrator
  LINE: ELLEN TAKES DOWN THE GARLIC AND WHITETHORN... She flings the window open... wind blows. She slowly raises her arms, beckoning, like a sorceress... radiant...
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: SHE SPEAKS TO ORLOK WITHOUT OPENING HER MOUTH. TELEPATHICALLY.
  EXPRESSION: null
- CHARACTER: Ellen (V.O.)
  LINE: I am ready. I bid you, come to me.
  EXPRESSION: Whispered

::SCENE::
LOCATION: Grünewald Manor. Chapel
MOOD: Eerie, Escalating Danger
CHARACTERS: Narrator, Orlok, Rats
BACKGROUND_IMAGE: grunewald_manor_chapel_night.png
BACKGROUND_EDIT: "Same moment. Orlok walks through the chapel, into the shadows. The high-pitched screeching of rats grows louder and louder."

::SCRIPT::
- CHARACTER: Narrator
  LINE: ORLOK walks through the chapel, into the shadows. The high-pitched screeching of RATS grows louder and louder...
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: ORLOK STOPS WALKING. HE TURNS HIS HEAD. HE HEARS ELLEN.
  EXPRESSION: null
- CHARACTER: Orlok (V.O.)
  LINE: Behold the third night.
  EXPRESSION: Menacing

::SCENE::
LOCATION: Grünewald Manor. Chapel
MOOD: Shocking, Terrifying
CHARACTERS: Narrator, The Vampire Hunters, Thomas, Sievers, Von Franz, Pigeons, Rats
BACKGROUND_IMAGE: grunewald_manor_chapel_night_rats.png
BACKGROUND_EDIT: "Moments later. The vampire hunters burst open the doors of the chapel. Pigeons fly. They see it, in the distance: Orlok’s sarcophagus! They gasp! There are rats everywhere. Thousands piled up, frantically crawling. They are ankle deep in rats!"

::SCRIPT::
- CHARACTER: Narrator
  LINE: THE VAMPIRE HUNTERS burst open the doors of the chapel. Pigeons fly. THEY SEE IT, in the distance: ORLOK’S SARCOPHAGUS!
  EXPRESSION: null
- CHARACTER: Thomas
  LINE: There it is!
  EXPRESSION: Triumphant
- CHARACTER: Narrator
  LINE: THEN, THEY GASP! THERE ARE RATS EVERYWHERE. THOUSANDS PILED UP, FRANTICALLY CRAWLING.
  EXPRESSION: Horrified
- CHARACTER: Sievers
  LINE: Oh god.
  EXPRESSION: Terrified
- CHARACTER: Narrator
  LINE: THEY ARE ANKLE DEEP IN RATS!
  EXPRESSION: null
- CHARACTER: Von Franz
  LINE: The fire will keep them at bay.
  EXPRESSION: Determined
- CHARACTER: Narrator
  LINE: It works... They lower their torches, keeping the rats away... walking in fear.
  EXPRESSION: Fearful
- CHARACTER: Von Franz
  LINE: Go forward Thomas. Set free the daemon’s body!
  EXPRESSION: Commanding

::SCENE::
LOCATION: Somewhere
MOOD: Intense Action
CHARACTERS: Narrator, Vers, Thomas, Sievers, Knock
BACKGROUND_IMAGE: null
BACKGROUND_EDIT: "Furious action at a coffin"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Vers throws open the coffin lid with ferocity.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Thomas without so much as looking... thrusts in his iron spike and hammers it! But Sievers sees into the box before Thomas:
  EXPRESSION: null
- CHARACTER: Sievers
  LINE: No, Thomas!!
  EXPRESSION: Shocked
- CHARACTER: Narrator
  LINE: An old, thin, pale arm juts out of the box in agony! Blood!! An old man’s scream!
  EXPRESSION: Painful
- CHARACTER: Narrator
  LINE: Thomas looks: it is no vampire – it is Knock, naked in Orlok’s dirt! The stake deep in his gut.
  EXPRESSION: Realization
- CHARACTER: Sievers
  LINE: Herr Knock!
  EXPRESSION: Horrified
- CHARACTER: Knock
  LINE: I relinquished him my soul...
  EXPRESSION: Resigned
- CHARACTER: Narrator
  LINE: Knock holds the stake, blood pouring from his mouth.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Knock pushes the stake deeper into his body. His eyes look kind.
  EXPRESSION: Serene
- CHARACTER: Knock
  LINE: I should have been the Prince of Rats – immortal... but he broke our covenant... for he cares only for his pretty bride.
  EXPRESSION: Bitter
- CHARACTER: Thomas
  LINE: Ellen!
  EXPRESSION: Shocked
- CHARACTER: Knock
  LINE: She is his!
  EXPRESSION: Sad
- CHARACTER: Narrator
  LINE: Thomas realizes what he has just said... and that he has left Ellen at home... as prey!
  EXPRESSION: Horrified
- CHARACTER: Thomas
  LINE: Monstrous!
  EXPRESSION: Horrified
- CHARACTER: Knock
  LINE: Strike again. I am blasphemy!
  EXPRESSION: Defiant
- CHARACTER: Narrator
  LINE: Von Franz takes a mallet from Thomas...
  EXPRESSION: null
- CHARACTER: Thomas
  LINE: No!
  EXPRESSION: Pleading
- CHARACTER: Von Franz
  LINE: Die you accursed mis-birth of Hell!
  EXPRESSION: Vengeful
- CHARACTER: Knock
  LINE: Deliverance...
  EXPRESSION: Peaceful
- CHARACTER: Narrator
  LINE: Knock dies.
  EXPRESSION: null
- CHARACTER: Von Franz
  LINE: Set fire to it all!
  EXPRESSION: Fanatical
- CHARACTER: Narrator
  LINE: Von Franz incants prayers, dousing the earth and Knock’s body with coal oil.
  EXPRESSION: null
- CHARACTER: Thomas
  LINE: Dammit man, he has gone to my wife!
  EXPRESSION: Desperate
- CHARACTER: Von Franz
  LINE: We must burn it! We must destroy all of his habitation. No sanctuary.
  EXPRESSION: Fanatical
- CHARACTER: Narrator
  LINE: He pours the oil everywhere lighting everything on fire.
  EXPRESSION: null
- CHARACTER: Thomas
  LINE: There is not time to be lost, he pursues Ellen!
  EXPRESSION: Urgent
- CHARACTER: Narrator
  LINE: Von Franz pays no attention to Thomas. The flames grow.
  EXPRESSION: null
- CHARACTER: Von Franz
  LINE: By holy Paul, there is no remission without her blood!! (laughs)
  EXPRESSION: Maniacal
- CHARACTER: Narrator
  LINE: Thomas and Sievers realize that Von Franz knew it all along!
  EXPRESSION: Shocked
- CHARACTER: Sievers
  LINE: You are a mad man!
  EXPRESSION: Accusatory
- CHARACTER: Thomas
  LINE: You knew Orlok would not be here! You knew it this afternoon!
  EXPRESSION: Accusatory
- CHARACTER: Von Franz
  LINE: Your wife wills it!!
  EXPRESSION: Fanatical
- CHARACTER: Thomas
  LINE: This is not moral!!
  EXPRESSION: Disgusted
- CHARACTER: Von Franz
  LINE: God is beyond our morals.
  EXPRESSION: Unwavering
- CHARACTER: Narrator
  LINE: Thomas runs savagely at Von Franz. Sievers holds him back. Von Franz laughs in a religious fervour!
  EXPRESSION:null
- CHARACTER: Von Franz
  LINE: In vain! In vain! (laughs)
  EXPRESSION: Triumphant
- CHARACTER: Narrator
  LINE: Thomas fills with tears of rage. He turns away, running to Ellen. Sievers follows. The flames growing wild. Rats scream!
  EXPRESSION:null
- CHARACTER: Von Franz
  LINE: You run in vain! You cannot out-run your destiny! (laughs) Her dark bond with the beast shall redeem us all. For when Jove’s pure light shall break upon the dawn: Redemption. (laughs) The plague shall be lifted! (laughs)
  EXPRESSION: Maniacal

::SCENE::
LOCATION: Hutter House. Bedroom
MOOD: Foreboding
CHARACTERS: Narrator, Ellen
BACKGROUND_IMAGE: bedroom.png
BACKGROUND_EDIT: "Nighttime, ready for fate, distant flames"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Ellen stands by the window, ready for her fate. The flames of Grünewald Manor flicker miles away.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: She hears heavy footsteps...
  EXPRESSION:null

::SCENE::
LOCATION: Hutter House. Stairwell
MOOD: Ominous
CHARACTERS: Narrator, Orlok
BACKGROUND_IMAGE: stairwell.png
BACKGROUND_EDIT: "Nighttime, Orlok ascending stairs"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Orlok is in her house... ascending the stairs...
  EXPRESSION:null
- CHARACTER: Narrator
  LINE: His breathing growing louder...
  EXPRESSION:null
- CHARACTER: Narrator
  LINE: His approach growing closer...
  EXPRESSION:null
- CHARACTER: Narrator
  LINE: Closer...
  EXPRESSION:null

::SCENE::
LOCATION: Hutter House. Hall
MOOD: Threatening
CHARACTERS: Narrator, Orlok
BACKGROUND_IMAGE: hall.png
BACKGROUND_EDIT: "Nighttime, Orlok's shadow approaching a door"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The shadow of Orlok’s claw reaches the door of the bedroom.
  EXPRESSION:null
- CHARACTER: Narrator
  LINE: His breathing is louder still.
  EXPRESSION:null

::SCENE::
LOCATION: Hutter House. Bedroom
MOOD: Apprehensive
CHARACTERS: Narrator, Ellen, Orlok
BACKGROUND_IMAGE: bedroom.png
BACKGROUND_EDIT: "Nighttime, Ellen in wedding dress, prepared"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Ellen turns to the door, trembling. She wears her wedding dress. Dried lilacs from her wedding adorn her hair, like a crown. She is prepared to be wed to death, as her dream foretold...
  EXPRESSION:null
- CHARACTER: Narrator
  LINE: Orlok enters the room.
  EXPRESSION:null
- CHARACTER: Orlok
  LINE: You accept this, of your own will?
  EXPRESSION: Ancient Dacian, subtitled
- CHARACTER: Narrator
  LINE: Their eyes of infinite depth meet each other.
  EXPRESSION:null
- CHARACTER: Ellen
  LINE: I do.
  EXPRESSION: Resolute
- CHARACTER: Orlok
  LINE: Then the covenant is fulfilled. Your oath re-pledged.
  EXPRESSION: Subtitled
- CHARACTER: Ellen
  LINE: Yes.
  EXPRESSION: Affirmative
- CHARACTER: Orlok
  LINE: As our spirits are one, so too shall be our flesh. You are mine.
  EXPRESSION: Subtitled
- CHARACTER: Narrator
  LINE: He breathes with obsession.
  EXPRESSION:null
- CHARACTER: Narrator
  LINE: A tear falls from her eye.
  EXPRESSION:null
- CHARACTER: Narrator
  LINE: They embrace. His grasp is overwhelming. Violent. Frightening.
  EXPRESSION:null
- CHARACTER: Narrator
  LINE: She pulls away in fear. He pulls tighter. His shrunken corpse mouth is bloody. He kisses her. Deeply. It is ecstasy for both of them.
  EXPRESSION:null
- CHARACTER: Narrator
  LINE: She leads him to the bed...
  EXPRESSION:null
- CHARACTER: Narrator
  LINE: She undresses...
  EXPRESSION:null
- CHARACTER: Narrator
  LINE: He caresses her body with his claws... She draws him to her heart, where she had wished Thomas would kiss her...
  EXPRESSION:null
- CHARACTER: Narrator
  LINE: He opens his rat-like jaws, lifts up his head and sinks his teeth into her breast, penetrating her flesh!
  EXPRESSION:null
- CHARACTER: Narrator
  LINE: She shudders. She moans. She holds his cold skull close as he drinks her blood. Her whole body throbs as the blood rushes out of her veins... She holds him tighter... Her breathing bursts with rapture.
  EXPRESSION:null

::SCENE::
LOCATION: Wisburg
MOOD: Hopeful, yet somber
CHARACTERS: Narrator
BACKGROUND_IMAGE: wisburg_dawn.png
BACKGROUND_EDIT: "Dawn over a plague-ridden city"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Wide: Wisburg, the plague-ridden city, awaits redemption. The first golden rays of dawn grow in the horizon behind the city skyline. In the distance, a rooster crows.
  EXPRESSION:null

::SCENE::
LOCATION: Wisburg Street
MOOD: Urgent
CHARACTERS: Narrator, Thomas, Sievers
BACKGROUND_IMAGE: wisburg_street_dawn.png
BACKGROUND_EDIT: "Dawn, Thomas and Sievers running"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Thomas and Sievers run.
  EXPRESSION:null
- CHARACTER: Narrator
  LINE: Thomas sees the amber sky and sunlight breaking upon the steeple of the church. He quickens his pace, running himself to death – he will save Ellen!
  EXPRESSION: Driven

::SCENE::
LOCATION: Hutter House. Bedroom
MOOD: Climax
CHARACTERS: Narrator, Orlok, Ellen, Thomas, Sievers
BACKGROUND_IMAGE: bedroom_climax.png
BACKGROUND_EDIT: "Dawn sunlight entering the room, Orlok feeding"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Orlok’s jaws are still latched to Ellen’s breast, though he is engorged.
  EXPRESSION:null
- CHARACTER: Narrator
  LINE: He senses the dawn and begins to rise, but Ellen lovingly guides him back to her. She whispers almost inaudibly:
  EXPRESSION:null
- CHARACTER: Ellen
  LINE: More. More.
  EXPRESSION: Weakly
- CHARACTER: Narrator
  LINE: He cannot resist. He drinks. She holds him close.
  EXPRESSION:null
- CHARACTER: Narrator
  LINE: As he drinks, the first rays of the sun ascending into the room. He feels the warmth - afraid.
  EXPRESSION:null
- CHARACTER: Narrator
  LINE: Ellen looks at him. He sees a fiery reckoning in her eyes. She has won.
  EXPRESSION:null
- CHARACTER: Narrator
  LINE: He slowly rises... The sunlight rakes over him... He puts up his hands to shield himself...
  EXPRESSION:null
- CHARACTER: Narrator
  LINE: The light is obliterating Nosferatu!
  EXPRESSION:null
- CHARACTER: Narrator
  LINE: In agony, he contorts himself into a twisted position... Ellen’s blood oozes from all of his orifices. He screams... his lungs shredded by the cry.
  EXPRESSION: Agonized
- CHARACTER: Narrator
  LINE: Just then, Thomas and Sievers rush in, gasping at what they see!
  EXPRESSION:null
- CHARACTER: Thomas
  LINE: Ellen!
  EXPRESSION: Desperate
- CHARACTER: Narrator
  LINE: Orlok falls onto Ellen, both of them building epiletically writhing in an anguished and putrid ballet. Climaxing.
  EXPRESSION:null
- CHARACTER: Narrator
  LINE: Thomas springs to the bed... but it is too late. Thomas falls to his knees in despair.
  EXPRESSION:null
- CHARACTER: Narrator
  LINE: Ellen gently touches Thomas. Ellen and Thomas exchange one final look of love, as she and Orlok die.
  EXPRESSION:null
- CHARACTER: Narrator
  LINE: Thomas holds his wife’s lifeless hand tightly. Beautiful, pure, golden light shines through the windows behind him.
  EXPRESSION:null
- CHARACTER: Narrator
  LINE: Von Franz walks into the bedroom, solemnly removing his hat. He puts his hand on Thomas’ shoulder. Thomas doesn’t feel it.
  EXPRESSION:null
- CHARACTER: Narrator
  LINE: Von Franz holds a bouquet of lilacs which he scatters upon the remains of Ellen and Orlok. Just as he crosses himself, Greta crawls by and leaps up into his arms. He pets her and smiles as she nestles up to him.
  EXPRESSION:null
- CHARACTER: Narrator
  LINE: Ellen and Orlok lay dead together, their limbs entwined in carnage and the fragrant lilacs. Orlok is now an empty shell. Ellen’s face is calm, beatific. Finally at peace.
  EXPRESSION:null
- CHARACTER: Narrator
  LINE: Hold.
  EXPRESSION:null
- CHARACTER: Narrator
  LINE: The End.
  EXPRESSION:null

