::SCENE::
LOCATION: Title Screen
MOOD: Ominous
CHARACTERS: Narrator
BACKGROUND_IMAGE: title_screen.png
BACKGROUND_EDIT: "Title: ROSEMARY'S BABY, Written by Roman Polanski, based on the novel by Ira Levin"

::SCRIPT::
- CHARACTER: Narrator
  LINE: ROSEMARY'S BABY
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Written by
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Roman Polanski
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: based on the novel by Ira Levin
  EXPRESSION: null

::PATHS::
- CHOICE: "Start Game"
  TARGET: bramford_exterior
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Bramford Exterior
MOOD: Grandeur and Foreboding
CHARACTERS: Narrator, Guy Woodhouse, Rosemary Woodhouse
BACKGROUND_IMAGE: bramford_exterior.png
BACKGROUND_EDIT: "Panoramic view of New York City, focusing on the Bramford building."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Panoramic of New York from a high building, finishing on the Bramford.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: GUY and ROSEMARY WOODHOUSE enter the main gate of the Bramford.
  EXPRESSION: null

::PATHS::
- CHOICE: "Enter the Bramford"
  TARGET: bramford_entrance_hall
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Bramford Entrance Hall
MOOD: Eccentric and Welcoming
CHARACTERS: Narrator, Mr. Nicklas, Guy Woodhouse, Rosemary Woodhouse
BACKGROUND_IMAGE: bramford_entrance_hall.png
BACKGROUND_EDIT: "Interior of the Bramford's entrance hall. Mr. Nicklas, a dapper man with missing fingers, is present."

::SCRIPT::
- CHARACTER: Narrator
  LINE: MR. NICKLAS is a small and dapper man; his fingers missing from both hands.
  EXPRESSION: null
- CHARACTER: Mr. Nicklas
  LINE: Oh, an actor. We’re very popular with actors. Have I seen you in anything?
  EXPRESSION: Friendly
  STAGE_DIRECTION: Ringing for the elevator with his middle finger
- CHARACTER: Guy Woodhouse
  LINE: Let’s see. I did Hamlet a while back, didn’t I, Liz? And then we made The Sandpiper...
  EXPRESSION: Playful
- CHARACTER: Rosemary Woodhouse
  LINE: He’s joking, he was in "Luther" and "Nobody Loves an Albatross” and a lot of television plays and commercials.
  EXPRESSION: Affectionate
- CHARACTER: Narrator
  LINE: The elevator doors slide open. They enter.
  EXPRESSION: null
- CHARACTER: Mr. Nicklas
  LINE: That’s where the money is, isn’t it? The commercials.
  EXPRESSION: Inquisitive
- CHARACTER: Rosemary Woodhouse
  LINE: Yes.
  EXPRESSION: Neutral
- CHARACTER: Guy Woodhouse
  LINE: And the artistic thrill, too.
  EXPRESSION: Witty
  STAGE_DIRECTION: Rosemary gives him a pleading look? he gives back one of stunned innocence and then makes a leering vampire face at the top of Mr. Nicklas’ head.

::PATHS::
- CHOICE: "Proceed to the apartment"
  TARGET: elevator
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Elevator Interior
MOOD: Informative and slightly unsettling
CHARACTERS: Narrator, Mr. Nicklas, Guy Woodhouse, Rosemary Woodhouse, Diego (elevator boy)
BACKGROUND_IMAGE: elevator.png
BACKGROUND_EDIT: "Interior of an oak-paneled elevator with a brass handrail. Diego, a uniformed Negro boy with a locked-in smile, operates it."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Oak-paneled with a shining brass handrail - is run by a uniformed Negro boy, DIEGO, with a locked-in- place smile.
  EXPRESSION: null
- CHARACTER: Mr. Nicklas
  LINE: Seven. Originally the smallest apartment was a nine - they've been broken up into fours, fives, and sixes. Seven E is a four that was originally the back part of a ten. It has the original master bedroom for its living room, another bedroom for its bedroom, and two servants’ rooms thrown together for its dining room or second bedroom. Do you have children?
  EXPRESSION: Informative
- CHARACTER: Rosemary Woodhouse
  LINE: We plan to.
  EXPRESSION: Hopeful
- CHARACTER: Narrator
  LINE: The elevator stops and DIEGO, smiling, chivvies it down, up and down again for a closer alignment.
  EXPRESSION: null

::PATHS::
- CHOICE: "Exit elevator"
  TARGET: hallway
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Hallway
MOOD: Dark and Worn
CHARACTERS: Narrator, Mr. Nicklas, Guy Woodhouse, Rosemary Woodhouse, Workman
BACKGROUND_IMAGE: hallway.png
BACKGROUND_EDIT: "Dimly lighted hallway, walled and carpeted in dark green. A workman is fitting a periscope into a sculpted green door."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Dimly lighted, walled and carpeted in dark green. They pass a sculptured green door marked Seven B. A WORKMAN is fitting a periscope into it. He looks at them and turns back to the cut-out hole.
  EXPRESSION: null
- CHARACTER: Mr. Nicklas
  LINE: The previous tenant, Mrs. Gardenia, passed away only a few days ago and nothing has been moved yet. Her son asked me to say that some of the furniture can be had practically for the asking.
  EXPRESSION: Matter-of-fact
- CHARACTER: Narrator
  LINE: Mr. Nicklas leads the way to the right and then to the left, through short branches of dark greenhallway. The wallpaper is rubbed away and curling inward in places. One of the bulbs in a cut-glass sconce is dead. The dark green carpet is patched with light green tape. Guy looks at Rosemary and lifts his eyebrows in mock outrage. She looks away and smiles brightly with an I-love-it-everything's-lovely expression.
  EXPRESSION: null
- CHARACTER: Rosemary Woodhouse
  LINE: Did she die in the apartment? Not that it -
  EXPRESSION: Concerned
- CHARACTER: Mr. Nicklas
  LINE: Oh, no, in a hospital.
  EXPRESSION: Reassuring
  STAGE_DIRECTION: Mr. Nicklas presses the pearl bell-button (the name L. Gardenia is mounted above it on black plastic)
- CHARACTER: Mr. Nicklas
  LINE: She’d been in a coma for weeks.
  EXPRESSION: Somber
  STAGE_DIRECTION: Mr. Nicklas turns a key in the lock. Despite lost fingers he works the knob and throws the door smartly.
- CHARACTER: Mr. Nicklas
  LINE: After you, please. She was very old and passed away without ever waking.
  EXPRESSION: Polite

::PATHS::
- CHOICE: "Enter the apartment"
  TARGET: apartment_interior
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: The Apartment Interior
MOOD: Vast and Dated
CHARACTERS: Narrator, Mr. Nicklas, Guy Woodhouse, Rosemary Woodhouse
BACKGROUND_IMAGE: apartment_interior.png
BACKGROUND_EDIT: "Interior of the apartment, showing the kitchen, study/greenhouse, and hallway. Roped bales of magazines are visible."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Four rooms divided two and two on either side of a narrow central hallway that extends in a straight line from the front door. The first room on the right is the kitchen. It has a six-burner gas stove with two ovens, a mammoth refrigerator, a monumental sink, dozens of cabinets, a high ceiling and a window on Seventh Avenue. On a chrome table, roped bales of "Fortune" and "Musical America." Opposite the kitchen, another room with windows facing onto a narrow courtyard, which has apparently been used as a combination study and greenhouse. Hundreds of small plants, dying and dead, stand on jerry-built shelves under spirals of unlighted fluorescent tubing; in their midst a roll-top desk spilled over with books and papers.
  EXPRESSION: null
- CHARACTER: Mr. Nicklas
  LINE: I’ll be grateful to go that way myself when the time comes. She was chipper right to the end... She’d been one of the first women lawyers in New York State.
  EXPRESSION: Reflective
- CHARACTER: Narrator
  LINE: Rosemary nudges Guy and indicates the desk. She leaves Guy and Mr. Nicklas and goes to it, stepping over a shelf of withered brown fronds. She touches the old wood. It is a handsome desk, broad and gleaming with age. On mauve paper, graceful blue penmanship "...than merely the intriguing pastime I believed it to be. I can no longer associate myself...” Rosemary catches herself snooping and looks up at Mr. Nicklas.
  EXPRESSION: null
- CHARACTER: Rosemary Woodhouse
  LINE: Is this for sale?
  EXPRESSION: Inquisitive
- CHARACTER: Mr. Nicklas
  LINE: I don’t know. I could find out for you.
  EXPRESSION: Neutral
- CHARACTER: Guy Woodhouse
  LINE: It’s a beauty.
  EXPRESSION: Appreciative
- CHARACTER: Rosemary Woodhouse
  LINE: Isn’t it?
  EXPRESSION: Delighted
  STAGE_DIRECTION: She looks about smiling.
- CHARACTER: Mr. Nicklas
  LINE: It would make an ideal nursery.
  EXPRESSION: Suggestive
- CHARACTER: Rosemary Woodhouse
  LINE: White and yellow wallpaper would brighten it tremendously.
  EXPRESSION: Visionary
  STAGE_DIRECTION: She looks at the closet filled with potted seedlings.
- CHARACTER: Guy Woodhouse
  LINE: What are all these?
  EXPRESSION: Curious
- CHARACTER: Rosemary Woodhouse
  LINE: Herbs, mostly. Mint. Basil.
  EXPRESSION: Knowledgeable
- CHARACTER: Narrator
  LINE: Further along the hall is a guest closet on the left and, on the right, a wide archway opening into the Living Room. Two large bay windows, small fireplace and high oak bookshelves.
  EXPRESSION: null
- CHARACTER: Rosemary Woodhouse
  LINE: Oh, Guy!
  EXPRESSION: Ecstatic
  STAGE_DIRECTION: She finds Guy’s hand and squeezes it.
- CHARACTER: Guy Woodhouse
  LINE: Mmm.
  EXPRESSION: Noncommittal
  STAGE_DIRECTION: Squeezing back her hand.
- CHARACTER: Mr. Nicklas
  LINE: The fireplace works, of course.
  EXPRESSION: Informative
  STAGE_DIRECTION: Mr. Nicklas, standing behind them, turns to the bedroom opposite. Its windows are facing on to the same narrow courtyard as those of the study. The bathroom is beyond the living room; big and full of bulbous white brass-knobbed fixtures.
- CHARACTER: Rosemary Woodhouse
  LINE: It's a marvelous apartment! I love it
  EXPRESSION: Thrilled
- CHARACTER: Guy Woodhouse
  LINE: What she's trying to do is get you to lower the rent.
  EXPRESSION: Playful
- CHARACTER: Mr. Nicklas
  LINE: We would raise it if we were allowed. Apartments with this kind of charm -
  EXPRESSION: Enthusiastic
  STAGE_DIRECTION: Mr. Nicklas stops short and looks at a mahogany secretary at the head of the central hallway.
- CHARACTER: Mr. Nicklas
  LINE: That's odd. There's a closet behind that secretary. I'm sure there is.
  EXPRESSION: Puzzled
  STAGE_DIRECTION: Mr. Nicklas goes closer to the secretary. Guy stands on tiptoe.
- CHARACTER: Guy Woodhouse
  LINE: You're right.
  EXPRESSION: Confirmatory
- CHARACTER: Rosemary Woodhouse
  LINE: She moved it. It used to be there.
  EXPRESSION: Observant
  STAGE_DIRECTION: She points to a peaked silhouette left ghost-like on the wall near the bedroom door, and the deep prints of four ball feet in the burgundy carpet. Faint scuff-trails curve and cross from the four prints to the secretary's feet where they stand now against the narrow adjacent wall.
- CHARACTER: Mr. Nicklas
  LINE: Give me a hand, will you?
  EXPRESSION: Requesting
  STAGE_DIRECTION: Guy and Mr. Nicklas, between them, work the secretary bit by bit back toward its original place.
- CHARACTER: Guy Woodhouse
  LINE: I see why she went into a coma.
  EXPRESSION: Joking
- CHARACTER: Mr. Nicklas
  LINE: She couldn't have moved this by herself. She was eighty-nine.
  EXPRESSION: Disbelieving
- CHARACTER: Narrator
  LINE: Rosemary looks doubtfully at the closet door they have uncovered.
  EXPRESSION: null
- CHARACTER: Rosemary Woodhouse
  LINE: Should we open it? Maybe her son should.
  EXPRESSION: Cautious
- CHARACTER: Mr. Nicklas
  LINE: I'm authorized to show the apartment.
  EXPRESSION: Authoritative
  STAGE_DIRECTION: He goes to the door and opens it. The closet is nearly empty; a vacuum cleaner at one side and four wood boards at the other. The overhead shelf is stacked with blue and green bath towels.
- CHARACTER: Guy Woodhouse
  LINE: Whoever she locked in got out.
  EXPRESSION: Sarcastic
- CHARACTER: Mr. Nicklas
  LINE: She probably didn't need five closets.
  EXPRESSION: Shrugging
- CHARACTER: Rosemary Woodhouse
  LINE: Why would she cover up her vacuum cleaner and her towels?
  EXPRESSION: Puzzled
- CHARACTER: Mr. Nicklas
  LINE: I don't suppose we'll ever know. She may have been getting senile after all.
  EXPRESSION: Resigned
  STAGE_DIRECTION: Smiles.
- CHARACTER: Mr. Nicklas
  LINE: Is there anything else?
  EXPRESSION: Inquiring
- CHARACTER: Rosemary Woodhouse
  LINE: Yes. What about the laundry facilities?
  EXPRESSION: Practical

::PATHS::
- CHOICE: "Continue the tour"
  TARGET: seventh_avenue_exterior
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Seventh Avenue Exterior
MOOD: Contemplative
CHARACTERS: Narrator, Rosemary Woodhouse, Guy Woodhouse
BACKGROUND_IMAGE: seventh_avenue_exterior.png
BACKGROUND_EDIT: "Rosemary and Guy walking along Seventh Avenue."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Rosemary and Guy walk along.
  EXPRESSION: null
- CHARACTER: Rosemary Woodhouse
  LINE: It's cheaper than the other.
  EXPRESSION: Pragmatic
- CHARACTER: Guy Woodhouse
  LINE: It's one room less, honey.
  EXPRESSION: Gentle
  STAGE_DIRECTION: They walk in silence for a moment.
- CHARACTER: Rosemary Woodhouse
  LINE: It’s better located.
  EXPRESSION: Assertive
- CHARACTER: Guy Woodhouse
  LINE: God, yes. I could walk to all the theatres.
  EXPRESSION: Excited
- CHARACTER: Rosemary Woodhouse
  LINE: Oh, Guy. Let’s take it! Please! That living room could be - oh please, let’s take it, all right?
  EXPRESSION: Eager
- CHARACTER: Guy Woodhouse
  LINE: Well, sure. If we can get out of the other lease.
  EXPRESSION: Agreeable

::PATHS::
- CHOICE: "Decide to take the apartment"
  TARGET: new_york_cafe
  STATE_CHANGE: apartment_taken = true
  CONDITION: null

::SCENE::
LOCATION: New York Cafe
MOOD: Anxious Anticipation
CHARACTERS: Narrator, Rosemary Woodhouse, Guy Woodhouse, Pregnant Woman, Mother, Joan Jellico, Man
BACKGROUND_IMAGE: new_york_cafe.png
BACKGROUND_EDIT: "Interior of a New York cafe. Rosemary is at a table, anxiously watching a telephone booth. Guy is inside the booth."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Rosemary sitting at a table. There are two Bloody Mary’s in front of her. She is looking anxiously at the telephone booth at the end of the room. Guy is inside the booth talking on the phone. Rosemary at the table. She keeps her fingers crossed.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: A PREGNANT WOMAN passes in a navy blue dress, followed by her MOTHER, carrying packages. Rosemary watches them.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: JOAN JELLICO, a red-haired girl, waves to Rosemary from a table opposite. Rosemary waves back. Joan Jellico mimes I’ll-come-to-see-you. A starved-looking, waxen-faced MAN facing Joan Jellico turns to look at Rosemary.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Rosemary looks toward the telephone booth again. Guy is on his way back, biting back a grin.
  EXPRESSION: null
- CHARACTER: Rosemary Woodhouse
  LINE: Yes?
  EXPRESSION: Hopeful
- CHARACTER: Guy Woodhouse
  LINE: The lease is void. We’ll get back the deposit.
  EXPRESSION: Triumphant
- CHARACTER: Rosemary Woodhouse
  LINE: What did you tell them?
  EXPRESSION: Curious
  STAGE_DIRECTION: Guy sits down. A WAITRESS brings sandwiches.
- CHARACTER: Guy Woodhouse
  LINE: I’m leaving for Vietnam on a U.S.O. tour and you’re going to Omaha to stay with your folks.
  EXPRESSION: Deceptive
- CHARACTER: Rosemary Woodhouse
  LINE: Is that all?
  EXPRESSION: Suspicious
- CHARACTER: Guy Woodhouse
  LINE: No. When I’m in Saigon I’m to keep an eye open for Lieutenant Hartman of the Marine Corps.
  EXPRESSION: Further Deception
- CHARACTER: Narrator
  LINE: Joan Jellico reaches the table and bends over it.
  EXPRESSION: null
- CHARACTER: Joan Jellico
  LINE: Hi!
  EXPRESSION: Friendly
  STAGE_DIRECTION: Guy turns to see who it is.
- CHARACTER: Guy Woodhouse
  LINE: Joan!
  EXPRESSION: Surprised
- CHARACTER: Joan Jellico
  LINE: Where have you been hiding?
  EXPRESSION: Inquisitive
- CHARACTER: Rosemary Woodhouse
  LINE: How’s Dick?
  EXPRESSION: Inquiring
- CHARACTER: Joan Jellico
  LINE: Okay.
  EXPRESSION: Casual
- CHARACTER: Guy Woodhouse
  LINE: Sit down.
  EXPRESSION: Welcoming
- CHARACTER: Joan Jellico
  LINE: (Indicates over shou
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue conversation with Joan"
  TARGET: cafe_conversation
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: HUTCH’S APARTMENT - KITCHEN
MOOD: Casual, Amused
CHARACTERS: Narrator, Rosemary, Joan, Guy, Hutch
BACKGROUND_IMAGE: hutch_apartment_kitchen.png
BACKGROUND_EDIT: "Small, well-equipped, slightly old-fashioned kitchen at night."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Guy is leaning against a tall refrigerator, glass of wine in his hand. Rosemary is sitting on a stool, also with wine. Hutch, wearing an apron and one oven glove, is bent double, looking in the oven. He is English, has a broad shiny face and a few strands of wetted-down hair combed crossways over his skull.
  EXPRESSION: null
- CHARACTER: Hutch
  LINE: I was tempted to write the management that you were drug addicts and litterbugs.
  EXPRESSION: Amused
- CHARACTER: Narrator
  LINE: Rosemary and Guy laugh.
  EXPRESSION: null
- CHARACTER: Hutch
  LINE: Instead, I lied and said that you’d be wonderful tenants.
  EXPRESSION: Teasing
- CHARACTER: Rosemary
  LINE: You're great, Hutch.
  EXPRESSION: Grateful
- CHARACTER: Hutch
  LINE: I hope though, that I can talk you out of it.
  EXPRESSION: Concerned
- CHARACTER: Guy
  LINE: He's pulling your leg.
  EXPRESSION: Skeptical
- CHARACTER: Hutch
  LINE: I'm not indeed.
  EXPRESSION: Serious

::PATHS::
- CHOICE: "Continue the conversation"
  TARGET: hutch_apartment_dining_room
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: HUTCH’S APARTMENT - DINING ROOM
MOOD: Informative, Slightly Foreboding
CHARACTERS: Narrator, Hutch, Rosemary, Guy
BACKGROUND_IMAGE: hutch_apartment_dining_room.png
BACKGROUND_EDIT: "Small, dark, neat room with an inscribed photo of Winston Churchill, a period sofa, two bridge tables with typewriters, and a side table laid for dinner."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Hutch straightens up, red-faced, perspiring, holding a large joint of lamb.
  EXPRESSION: null
- CHARACTER: Guy
  LINE: Gee, that looks great.
  EXPRESSION: Appreciative
- CHARACTER: Narrator
  LINE: Hutch, holding the joint out in front of him, leads the way into the other room.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: This is small, dark and neat. There is an inscribed photo of Winston Churchill and a period sofa. Two bridge tables, each with its typewriter and piles of paper. There is another table at the side, laid for dinner and looking out of place. Hutch goes to this table and puts down the joint.
  EXPRESSION: null
- CHARACTER: Hutch
  LINE: Are you aware that the Bramford had rather an unpleasant reputation early in the century?
  EXPRESSION: Curious
- CHARACTER: Narrator
  LINE: Hutch looks at them; Rosemary sits down and Guy is pouring more wine into the glasses. Hutch starts carving.
  EXPRESSION: null
- CHARACTER: Hutch
  LINE: It's where the Trench sisters performed their little dietary experiments, and Keith Kennedy held his parties. Adrian Marcato lived there too; so did Pearl Ames.
  EXPRESSION: Informative
- CHARACTER: Guy
  LINE: Who were the Trench sisters?
  EXPRESSION: Inquisitive
- CHARACTER: Rosemary
  LINE: Who was Adrian Marcato?
  EXPRESSION: Inquisitive
- CHARACTER: Hutch
  LINE: The Trench sisters were two proper Victorian ladies. They cooked and ate several young children, including a niece.
  EXPRESSION: Matter-of-fact
- CHARACTER: Guy
  LINE: Lovely.
  EXPRESSION: Sarcastic
- CHARACTER: Hutch
  LINE: Adrian Marcato practiced witchcraft. He made quite a splash in the nineties, announcing he had conjured up the living Satan. Apparently people believed him; so they attacked and nearly killed him in the Bramford lobby.
  EXPRESSION: Informative
- CHARACTER: Rosemary
  LINE: You're joking.
  EXPRESSION: Disbelieving
- CHARACTER: Hutch
  LINE: Later the Keith Kennedy business began, and by the twenties the house was half empty.
  EXPRESSION: Informative
- CHARACTER: Guy
  LINE: I knew about Keith Kennedy, I didn't know Marcato lived there.
  EXPRESSION: Surprised
- CHARACTER: Rosemary
  LINE: And those sisters!
  EXPRESSION: Horrified
- CHARACTER: Narrator
  LINE: Hutch sits down and they start eating.
  EXPRESSION: null
- CHARACTER: Hutch
  LINE: World War Two filled the place up again.
  EXPRESSION: Informative
- CHARACTER: Rosemary
  LINE: Mmm. Terrific.
  EXPRESSION: Enjoying food
- CHARACTER: Guy
  LINE: The house?
  EXPRESSION: Inquisitive
- CHARACTER: Rosemary
  LINE: The lamb.
  EXPRESSION: Enjoying food
- CHARACTER: Hutch
  LINE: It was called Black Branford.
  EXPRESSION: Informative
- CHARACTER: Rosemary
  LINE: But - awful things happen in every apartment house.
  EXPRESSION: Rationalizing
- CHARACTER: Hutch
  LINE: The house happens to have a high incidence of unpleasant happenings. Why deliberately enter a danger zone?
  EXPRESSION: Concerned
- CHARACTER: Guy
  LINE: Danger zone! Sounds like something out of your boys’ stories. You must be kidding.
  EXPRESSION: Skeptical
- CHARACTER: Hutch
  LINE: I am honestly trying to talk you out of it.
  EXPRESSION: Sincere
- CHARACTER: Guy
  LINE: Well, Jesus, Hutch --
  EXPRESSION: Frustrated
- CHARACTER: Hutch
  LINE: Go to the Wyoming or the Osborne if you’re dead set on nineteenth century splendor.
  EXPRESSION: Suggestive
- CHARACTER: Rosemary
  LINE: The Wyoming is co-op. The Osborne is going to be torn down.
  EXPRESSION: Practical
- CHARACTER: Narrator
  LINE: They eat for a moment in silence.
  EXPRESSION: null
- CHARACTER: Hutch
  LINE: In ’59 a dead infant was found wrapped in newspaper in the basement.
  EXPRESSION: Grim
- CHARACTER: Guy
  LINE: You really rouse my appetite!
  EXPRESSION: Sarcastic
- CHARACTER: Hutch
  LINE: Have some more wine.
  EXPRESSION: Reassuring
- CHARACTER: Narrator
  LINE: Hutch refills the glasses.
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue discussion about the Bramford"
  TARGET: street_carpet_store
  STATE_CHANGE: fear = +2
  CONDITION: null

::SCENE::
LOCATION: STREET IN FRONT OF CARPET STORE
MOOD: Mundane
CHARACTERS: Narrator, Rosemary, Joan Jellico
BACKGROUND_IMAGE: street_carpet_store.png
BACKGROUND_EDIT: "Daytime, street in front of a carpet store."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Rosemary and Joan Jellico stand looking in the window. They have parcels and magazines in their hands.
  EXPRESSION: null

::PATHS::
- CHOICE: "Enter the store"
  TARGET: store_fabric_department
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: STORE - FABRIC DEPARTMENT
MOOD: Bustling, Shopping
CHARACTERS: Narrator, Rosemary, Joan Jellico
BACKGROUND_IMAGE: store_fabric_department.png
BACKGROUND_EDIT: "Daytime, Rosemary and Joan Jellico are looking through curtain fabrics hung like flags."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Rosemary and Joan Jellico are ploughing their way through curtain fabrics, hung like flags side by side.
  EXPRESSION: null

::PATHS::
- CHOICE: "Go to the escalator"
  TARGET: store_escalator
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: STORE - ESCALATOR
MOOD: Busy, Ascending
CHARACTERS: Narrator, Rosemary, Joan Jellico, Elise Dunstan
BACKGROUND_IMAGE: store_escalator.png
BACKGROUND_EDIT: "Daytime, Rosemary and Joan Jellico are going up on an escalator, arms full of packages. They wave to Elise Dunstan going down."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Rosemary and Joan Jellico standing, on the escalator, going up, their arms piled high with packages and bags.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: They wave to ELISE DUNSTAN going down on the other escalator.
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue to bedding department"
  TARGET: store_bedding_department
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: STORE - BEDDING DEPARTMENT
MOOD: Humorous, Decisive
CHARACTERS: Narrator, Rosemary, Joan Jellico, Salesman, Elise Dunstan
BACKGROUND_IMAGE: store_bedding_department.png
BACKGROUND_EDIT: "Daytime, Rosemary is bouncing on a large bed, being watched by Elise Dunstan, Joan Jellico, and a Salesman."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Rosemary lies, bouncing up and down, on a huge bed.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Elise Dunstan, Joan Jellico and a SALESMAN stand watching her.
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: This is too big.
  EXPRESSION: Decisive
- CHARACTER: Narrator
  LINE: She looks at the Salesman and points to a bed opposite
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: What about this one?
  EXPRESSION: Inquisitive
- CHARACTER: Joan
  LINE: Oh no. You want a king-size bed.
  EXPRESSION: Assertive
- CHARACTER: Salesman
  LINE: If your husband is not a heavy person, this is quite comfortable for two people.
  EXPRESSION: Professional
- CHARACTER: Joan
  LINE: What happens if there are three?
  EXPRESSION: Playful
- CHARACTER: Narrator
  LINE: What do you mean? The baby?
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The girls burst into laughter.
  EXPRESSION: null

::PATHS::
- CHOICE: "Purchase the bed"
  TARGET: guy_rosemary_apartment_entry
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: GUY AND ROSEMARY’S APARTMENT - ENTRY
MOOD: Quiet, Anticipatory
CHARACTERS: Narrator, Guy, Rosemary
BACKGROUND_IMAGE: guy_rosemary_apartment_entry.png
BACKGROUND_EDIT: "Dusk, the apartment is empty and dark, with faint blue light coming through the windows. Some furniture from Mrs. Gardenia's son is present."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Guy and Rosemary enter. He is carrying a lamp and a shopping bag. Rosemary pulls the key out of the door and follows Guy along the hallway. The apartment is empty, except for a few pieces of furniture in the den, from Mrs. Gardenia's son. The rooms are dark and full of shadows. Faint blue light comes through the windows.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Guy turns into the living room, Rosemary to the bedroom; there are many packages spread on the floor (results of the shopping) and a solitary vanity.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Rosemary kneels, opens a wooden crate, and pulls out three plates from the shavings. Guy comes in; she hands him the plates and starts putting back the shavings.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: We hear a woman’s voice from behind the wall.
  EXPRESSION: null
- CHARACTER: MRS. CASTEVET (O.S.)
  LINE: Roman? Bring me in some root beer when you come!
  EXPRESSION: Demanding
- CHARACTER: Narrator
  LINE: Guy and Rosemary look at each other.
  EXPRESSION: null
- CHARACTER: Guy
  LINE: I didn't know they were still making Ma and Pa Kettle movies.
  EXPRESSION: Amused
- CHARACTER: Narrator
  LINE: He goes back to the living room. Rosemary follows him. On her way, she stops and looks toward the closet at the end of the hallway. She goes to it and opens it slowly. She takes out one of the four boards leaning against the side, turns it and looks at it.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Guy has plugged the lamp in the living room and a light comes through the archway.
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: Hey, these are shelves!
  EXPRESSION: Surprised
- CHARACTER: Narrator
  LINE: Rosemary brings the shelf into the Living Room, puts it on the floor; they picnic on it - tuna sandwiches and beer - sitting on the rug.
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: Let's make love!
  EXPRESSION: Passionate
- CHARACTER: Narrator
  LINE: They unplug the lamp, strip and start making love.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Wide-eyed with fear, Guy hisses.
  EXPRESSION: null
- CHARACTER: GUY
  LINE: Shh! I hear - the Trench sisters chewing!
  EXPRESSION: Terrified
- CHARACTER: Narrator
  LINE: Rosemary hits him on the head, hard.
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue the evening"
  TARGET: guy_rosemary_apartment_day
  STATE_CHANGE: fear = +3, intimacy = +1
  CONDITION: null

::SCENE::
LOCATION: GUY AND ROSEMARY’S APARTMENT
MOOD: Chaotic, Busy
CHARACTERS: Narrator, Rosemary, Painters, Carpet Layer, Workmen, Paperhanger
BACKGROUND_IMAGE: guy_rosemary_apartment_day.png
BACKGROUND_EDIT: "Daytime, the apartment is being renovated with painters, carpet layers, workmen, and a paperhanger."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Big splash, of paint on the wall; the PAINTERS are working in the living room. The CARPET LAYER unrolls carpet on the floor in the bedroom. THREE WORKMEN carrying an enormous bed and chairs in the hallway. A PAPERHANGER, grumbling, hangs wallpaper in the bedroom.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Rosemary, standing on a table, hangs curtains in the den. We hear the sound of a television commercial.
  EXPRESSION: null
- CHARACTER: COMMERCIAL ANNOUNCER (O.S.)
  LINE: Discover the swinging world of Yamaha...
  EXPRESSION: Promotional
- CHARACTER: Narrator
  LINE: Rosemary drops everything, jumps down from the table, and hunkers down in front of the television set. She waits for Guy to appear. When the commercial is finished, she switches off.
  EXPRESSION: null

::PATHS::
- CHOICE: "Wait for Guy"
  TARGET: kitchen_dusk
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: KITCHEN
MOOD: Domestic, Welcoming
CHARACTERS: Narrator, Rosemary, Guy, Joan, Dick Jellico, Alan (agent)
BACKGROUND_IMAGE: kitchen_dusk.png
BACKGROUND_EDIT: "Dusk, a completely furnished and equipped kitchen. Rosemary is washing salad. Preparations for dinner are on the table. A large potted plant stands on the fridge and a smaller one on the floor."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Completely furnished and equipped. Rosemary is washing salad. There are preparations for dinner on the table. A large potted plant stands on the fridge and a smaller one on the floor.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Guy comes in. Rosemary, holding her dripping hands away, kisses him. She points to the large plant.
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: From Joan and Dick Jellico.
  EXPRESSION: Smiling
- CHARACTER: Rosemary
  LINE: From your agent.
  EXPRESSION: Smiling
- CHARACTER: GUY
  LINE: Alan? Stingy bastard.
  EXPRESSION: Teasing
- CHARACTER: Narrator
  LINE: Rosemary turns and picks up a telegram, holding it carefully by the corner with her wet hand. She hands it to Guy.
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: From Hutch.
  EXPRESSION: Neutral
- CHARACTER: Narrator
  LINE: Guy looks at it.
  EXPRESSION: null
- CHARACTER: Guy
  LINE: "The Bramford will change from a bad house to a good house when one of its doors is marked R. and G. Woodhouse."
  EXPRESSION: Amused
- CHARACTER: Narrator
  LINE: They both collapse in laughter.
  EXPRESSION: null

::PATHS::
- CHOICE: "Read the telegram"
  TARGET: seventh_floor_hallway
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: SEVENTH FLOOR HALLWAY
MOOD: Curious, Observational
CHARACTERS: Narrator, Rosemary, Mr. Gould, Mrs. Gould, Mrs. Castevet (O.S.), Mr. R. Castevet
BACKGROUND_IMAGE: seventh_floor_hallway.png
BACKGROUND_EDIT: "Daytime, Rosemary exits the elevator carrying a roll of gingham contact paper. The Goulds are coming out of their apartment."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Rosemary steps out of the elevator, carrying a large roll, of gingham contact paper. On the left, the GOULDS, a middle-aged couple, are coming out of an apartment door.
  EXPRESSION: null
- CHARACTER: MR. GOULD
  LINE: Hold it, hold it, pleased
  EXPRESSION: Friendly
- CHARACTER: Narrator
  LINE: They run towards the elevator, smiling at Rosemary. Rosemary smiles back at them. When the rolling gate closes, Rosemary goes to see their names on the door of their apartment. It says 3 MR. and MRS. GOULD. Rosemary turns back in her own direction and passing the door opposite the elevator, Seven A, looks for the name around the doorbell. There is no sign of any. Rosemary bends down and looks at the pile of mail on the doorstep. There are six to eight letters, with stamps of different countries. The name reads; MR. R. CASTEVET. A VOICE behind the door can be HEARD.
  EXPRESSION: null
- CHARACTER: MRS. CASTEVET (O.S.)
  LINE: Terry? Where's Terry?
  EXPRESSION: Calling
- CHARACTER: Narrator
  LINE: Rosemary straightens up and moves on and looks at the door of Seven B. There is a little golden plate; MESSRS. DUBIN and DeVORE.
  EXPRESSION: null

::PATHS::
- CHOICE: "Examine apartment 7A further"
  TARGET: guy_rosemary_apartment_closet
  STATE_CHANGE: curiosity = +1
  CONDITION: null

::SCENE::
LOCATION: GUY AND ROSEMARY'S APARTMENT - CLOSET
MOOD: Domestic, Productive
CHARACTERS: Narrator, Rosemary, Guy
BACKGROUND_IMAGE: guy_rosemary_apartment_closet.png
BACKGROUND_EDIT: "Dusk, Rosemary is in the closet at the end of the hallway, sticking gingham contact paper on the top shelf. The shelves below are already finished."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Rosemary is in the closet at the end of the hallway. She is sticking the gingham contact paper on the top shelf. The shelves below are already finished.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Guy comes in. Rosemary shows him the shelves.
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: Look!
  EXPRESSION: Proud
- CHARACTER: GUY
  LINE: Great.
  EXPRESSION: Appreciative
- CHARACTER: Narrator
  LINE: They kiss.
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue domestic tasks"
  TARGET: kitchen_night
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: KITCHEN
MOOD: Domestic, Relaxed
CHARACTERS: Narrator, Rosemary, Guy
BACKGROUND_IMAGE: kitchen_night.png
BACKGROUND_EDIT: "Night, Rosemary and Guy are in the kitchen. Guy is eating a sandwich."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Rosemary and Guy. He's eating a sandwich.
  EXPRESSION: null

::PATHS::
- CHOICE: "End Scene"
  TARGET: end
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Guy and Rosemary's Apartment - Living Room
MOOD: Domestic
CHARACTERS: Narrator, Guy, Rosemary
BACKGROUND_IMAGE: apartment_living_room.png
BACKGROUND_EDIT: "Daytime, newspaper, can of beer"

::SCRIPT::
- CHARACTER: Narrator
  LINE: wich, with a newspaper open at the theatrical page, and a can of beer in front of him.
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: I’ve seen those people Goulds.
  EXPRESSION: null
- CHARACTER: Guy
  LINE: Mmm.
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: And Ma and Pa Kettle’s name is Castevet. They get a lot of mail. Who were Ma and Pa Kettle anyway?
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Guy, reading, doesn’t answer. Rosemary waits for a moment.
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: Guy?
  EXPRESSION: null
- CHARACTER: Guy
  LINE: Yes, honey.
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: Oh, never mind!
  EXPRESSION: null

::SCENE::
LOCATION: Basement Laundry Room - Day - September 10, 1965
MOOD: Prison-like, Steamy
CHARACTERS: Narrator, Rosemary, Terry
BACKGROUND_IMAGE: basement_laundry_room.png
BACKGROUND_EDIT: "Steamy brick walls, bulbs in cages, deep double sinks in iron-mesh cubicles"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Prison-like with steamy brick walls, bulbs in cages, and scores of deep double sinks in iron-mesh cubicles.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Rosemary is sitting reading the ’New Yorker’ next to an operating machine. TERRY, a girl Rosemary’s age, enters. She is dark-haired and looks like Anna Maria Alberghetti. Terry carries a yellow plastic laundry basket. She nods at Rosemary and then, not looking at her, goes to one of the machines and begins feeding dirty clothes into it.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Rosemary stares at the girl. Terry finishes putting in the clothes, closes the door, starts the machine; the water begins to fill up. Terry turns and catches Rosemary’s look and smiles questioningly.
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: I’m sorry. I thought you were Ama Maria Alberghetti. I’m sorry.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Terry blushes and looks at the floor.
  EXPRESSION: null
- CHARACTER: Terry
  LINE: It’s all right. Lot of people think I’m Anna Maria. I don’t see any resemblance.
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: Do you know her?
  EXPRESSION: null
- CHARACTER: Terry
  LINE: No.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Terry wipes her hand on her shorts and steps forward, holding it out.
  EXPRESSION: null
- CHARACTER: Terry
  LINE: I’m Terry Gionoffrio.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Rosemary smiles and shakes hands.
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: I’m Rosemary Woodhouse. We're new tenants here.
  EXPRESSION: null
- CHARACTER: Terry
  LINE: I’m staying with Mr. and Mrs. Castevet. Seventh floor. I'm their guest, sort of, since June.
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: Oh, our apartment used to be the back part of yours.
  EXPRESSION: null
- CHARACTER: Terry
  LINE: Oh, for goodness' sake. You took the old lady's apartments Mrs. -
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: Gardenia.
  EXPRESSION: null
- CHARACTER: Terry
  LINE: Gardenia. She was a good friend of the Castevets. She used to grow herbs and things and bring them in for Mrs. Castevet to cook with.
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: I've seen those plants.
  EXPRESSION: null
- CHARACTER: Terry
  LINE: Now Mrs. Castevet grows her own things.
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: Excuse me, I have to put softener in.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Rosemary gets up and takes a bottle from the laundry bag on the washer. She pours a capful of softener. Terry opens the washer door.
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: Thank you.
  EXPRESSION: null
- CHARACTER: Terry
  LINE: What does your husband do?
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Capping the bottle Rosemary nods complacently.
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: He is an actor.
  EXPRESSION: null
- CHARACTER: Terry
  LINE: No kidding? What’s his name?
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: Guy Woodhouse. He was in "Luther” and "Nobody Loves an Albatross” and he does a lot of television.
  EXPRESSION: null
- CHARACTER: Terry
  LINE: Gee, I watch TV all day long. I’ll bet I’ve seen him.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Glass crashes somewhere in the basement.
  EXPRESSION: null
- CHARACTER: Terry
  LINE: Yow.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Rosemary hunches her shoulders and looks uneasily toward the laundry room’s doorway.
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: I hate this basement.
  EXPRESSION: null
- CHARACTER: Terry
  LINE: Listen, we could come down together regular.
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: That would be great.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Terry laughs happily, seems to seek words and then, still laughing:
  EXPRESSION: null
- CHARACTER: Terry
  LINE: I’ve got a good luck charm that'll maybe do for both of us!
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: She pulls away the collar of her blouse, draws out a silver neck chain and shows Rosemary on the end of it a silver filigree ball a little less than an inch in diameter.
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: Oh, that’s beautiful.
  EXPRESSION: null
- CHARACTER: Terry
  LINE: Isn't it? Mrs. Castevet gave it to me. It's good luck, or anyway it's supposed to be. There's some stuff inside it.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Rosemary looks more closely at the charm Terry holds out between thumb and fingertips. It is filled with a greenish-brown spongy substance which presses out against the silver openwork.
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: Rosemary draws back, wrinkling her nose.
  EXPRESSION: null
- CHARACTER: Terry
  LINE: I'm not mad about the smell either. I hope it works.
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: It's a beautiful charm. I’ve never seen anything like it.
  EXPRESSION: null
- CHARACTER: Terry
  LINE: European.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: She leans a hip against the washer and admires the ball, turning it one way and another.
  EXPRESSION: null
- CHARACTER: Terry
  LINE: The Castevets are the most wonderful people in the world, bar none. They picked me up off the sidewalk - literally.
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: You were sick?
  EXPRESSION: null
- CHARACTER: Terry
  LINE: I was starving and on dope and doing a lot of other things. They’re childless. I'm like the daughter they never had, you know?
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Rosemary nods.
  EXPRESSION: null
- CHARACTER: Terry
  LINE: I thought at first they had some kind of sex thing they would want me to do, but they've really been like real grandparents.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Terry drops the filigree ball back into her blouse.
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: It’s nice to know there are people like that, when you hear so much about apathy and people who are afraid of getting involved.
  EXPRESSION: null
- CHARACTER: Terry
  LINE: I would be dead now if it wasn’t for them. That’s an absolute fact. Dead or in jail.
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: You don’t have any family that could have helped you?
  EXPRESSION: null
- CHARACTER: Terry
  LINE: A brother in the Navy.
  EXPRESSION: null

::SCENE::
LOCATION: Guy and Rosemary’s Apartment - Dusk - September 10, 1965
MOOD: Domestic, Slightly Awkward
CHARACTERS: Narrator, Guy, Rosemary, Terry
BACKGROUND_IMAGE: apartment_living_room.png
BACKGROUND_EDIT: "Dusk, Fritos bag on coffee table"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Guy is sitting in front of the TV set eating a bag of Fritos. Rosemary enters with Terry.
  EXPRESSION: null
- CHARACTER: Guy
  LINE: Them sure must be clean clothes.
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: This is Terry. This is Guy.
  EXPRESSION: null
- CHARACTER: Terry
  LINE: Hello, Guy.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: They shake hands. Terry blushes and turns to Rosemary, flustered.
  EXPRESSION: null
- CHARACTER: Terry
  LINE: Of course I remember him. He was in - how was it called?
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: Terry is staying with the Castevets. Seven A, you know.
  EXPRESSION: null
- CHARACTER: Terry
  LINE: 'Another World' wasn’t it?
  EXPRESSION: null
- CHARACTER: Guy
  LINE: Are you sure it wasn’t Donald Baumbart?
  EXPRESSION: null
- CHARACTER: Terry
  LINE: Oh, I thought it was you.
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: Of course it was Guy. He’s teasing you. Guy and Donald are reading for the same part.
  EXPRESSION: null
- CHARACTER: Terry
  LINE: Oh, I’m sure you’ll get it. It’s a lovely apartment.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Looks round the apartment.
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: It will be. Have you seen it before?
  EXPRESSION: null
- CHARACTER: Terry
  LINE: No.
  EXPRESSION: null
- CHARACTER: Guy
  LINE: You know, you remind me of somebody.
  EXPRESSION: null
- CHARACTER: Terry
  LINE: I’ve got to go now. The Castevets eat at six.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Rosemary opens the door.
  EXPRESSION: null

::SCENE::
LOCATION: Hallway - Dusk
MOOD: Transition
CHARACTERS: Narrator, Rosemary, Terry, Lisa
BACKGROUND_IMAGE: hallway.png
BACKGROUND_EDIT: "Dusk, hallway leading to apartments"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Rosemary walks Terry towards Castevets’ apartment. The door of Seven D is open and LISA, a two-year-old girl, stands on the threshold.
  EXPRESSION: null
- CHARACTER: Lisa
  LINE: What’s your name?
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Rosemary bends down, smiling. Terry goes on.
  EXPRESSION: null
- CHARACTER: Terry
  LINE: See you, Rosemary.
  EXPRESSION: null
- CHARACTER: Lisa
  LINE: I’m Lisa.
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: Hello, Lisa.
  EXPRESSION: null
- CHARACTER: Lisa
  LINE: Did you eat your Captain Crunch?
  EXPRESSION: null

::SCENE::
LOCATION: Guy and Rosemary’s Apartment - Day - September 15, 1965
MOOD: Domestic, Unpacking
CHARACTERS: Narrator, Rosemary, Hutch
BACKGROUND_IMAGE: apartment_living_room.png
BACKGROUND_EDIT: "Daytime, partially furnished living room, unpacked ice bucket"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Rosemary is unwrapping a tall teak wood ice bucket with a bright orange lining, on the table in the living room. Hutch is walking around admiring the half-furnished room. Rosemary goes to Hutch and kisses him.
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: Oh, Hutch! I'm so ashamed, we haven't had you over for dinner yet.
  EXPRESSION: null
- CHARACTER: Hutch
  LINE: For God’s sake don’t even think about entertaining. Tell me, how is everything?
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: Guy's still auditioning. Nothing really exciting except for commercials, which is not too bad - money-wise.
  EXPRESSION: null
- CHARACTER: Hutch
  LINE: It costs a fortune to furnish a place nowadays.
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: Ah, and the time... The chairs are four weeks late.
  EXPRESSION: null
- CHARACTER: Hutch
  LINE: Typical.
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: The neighbors certainly don’t seem abnormal. Except normal abnormal like homosexuals. They breed Persian cats. We can have one any time we want,
  EXPRESSION: null
- CHARACTER: Hutch
  LINE: They shed.
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: And there’s a couple who took in this girl who was hooked on drugs, and they completely cured her.
  EXPRESSION: null
- CHARACTER: Hutch
  LINE: It sounds as if you've moved into Sunnybrook Farm, I'm delighted.
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: The basement is kind of creepy, I curse you every time I go down there.
  EXPRESSION: null

::SCENE::
LOCATION: Bedroom - Night
MOOD: Eavesdropping, Uneasy
CHARACTERS: Narrator, Guy, Rosemary, Mrs. Castevet (O.S.)
BACKGROUND_IMAGE: bedroom.png
BACKGROUND_EDIT: "Night, bed, vanity mirror"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Guy in bed reading, Rosemary in front of her vanity mirror, brushing her hair. We hear a WOMAN’S voice behind the wall,
  EXPRESSION: null
- CHARACTER: Mrs. Castevet
  LINE: But it's impossible to be a hundred percent sure! if you want my opinion, we shouldn't tell her at all; that's my opinion!
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The voice fades away. Guy lifts his head from his book; Rosemary turns round; they both look at the wall.
  EXPRESSION: null
- CHARACTER: Guy
  LINE: Jesus!
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: That must be the partition.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Guy pulls his pajama sleeves over his hands, leaving only one finger showing on each hand; imitating Mr. Nicklas’ voices:
  EXPRESSION: null
- CHARACTER: Guy
  LINE: This is the back part of the original 'ten', with its master bedroom...
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Rosemary, laughing, jumps into the bed and claps her hand over his mouth. Guy switches the lamp off. They kiss for a moment, then lift their heads in surprise; there is a sound of a party, flat unmusical singing and a flute or a clarinet piping along beside it.
  EXPRESSION: null

::SCENE::
LOCATION: Street - Night - September 17, 1965
MOOD: Shocking, Tragic
CHARACTERS: Narrator, Rosemary, Guy, Onlooker, 2nd Onlooker, Policeman, Toby (Night Doorman)
BACKGROUND_IMAGE: street_accident.png
BACKGROUND_EDIT: "Night, mild and balmy, Bramford building, parked car, police cars with spinning lights, crumpled Volkswagen"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Rosemary and Guy walk along approaching the Bramford. The night is mild and balmy. As they get nearer they see a group of about TWENTY PEOPLE gathered in a semicircle at the side of a parked car. Two police cars are double-parked, roof lights spinning red. Rosemary and Guy walk faster, hand in hand, straining to get a better view, Cars on the street slow questioningly; windows scrape open in the Bramford and heads look out beside gargoyle’s heads, The NIGHT DOORMAN, TOBY, comes from the house with a tan blanket, A POLICEMAN turns to take it from him. The roof of a Volkswagen is crumpled to the sides the windshield is crazed with a million fractures.
  EXPRESSION: null
- CHARACTER: Onlooker
  LINE: Dead,
  EXPRESSION: null
- CHARACTER: 2nd Onlooker
  LINE: Gee, did you hear that crash. Wow.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Rosemary and Guy stand on tiptoes, craning over peoples’ shoulders.
  EXPRESSION: null
- CHARACTER: Policeman
  LINE: Get back now, will you?
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The shoulders separate, a SPORT-SHIRTED BACK moves away. On the sidewalk lies Terry, watching the sky with one eye, half of her face gone to red pulp. The blanket flips over her, settles, and red blotches soak through in one place and then another. Rosemary wheels, eye
  EXPRESSION: null

::SCENE::
LOCATION: Street outside Apartment Building
MOOD: Somber, Confused
CHARACTERS: Narrator, Guy, Policeman, Second Policeman, Third Policeman, Mr. Nicklas, Rosemary
BACKGROUND_IMAGE: street_outside_apartment.png
BACKGROUND_EDIT: "Night, police presence, body covered with a sheet."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Her right hand making an automatic cross. Her mouth is tightly closed.
  EXPRESSION: null
- CHARACTER: Guy
  LINE: Oh, Jesus. Oh my God.
  EXPRESSION: Distraught
- CHARACTER: Policeman
  LINE: Get back, will you?
  EXPRESSION: Authoritative
- CHARACTER: Guy
  LINE: We know her.
  EXPRESSION: Anxious
- CHARACTER: Narrator
  LINE: A SECOND POLICEMAN turns towards them. He is forty or so and sweating. His eyes are blue and beautiful, with thick, black lashes.
  EXPRESSION: null
- CHARACTER: Second Policeman
  LINE: What’s her name?
  EXPRESSION: Inquisitive
- CHARACTER: Guy
  LINE: Terry.
  EXPRESSION: Anxious
- CHARACTER: Second Policeman
  LINE: Terry what?
  EXPRESSION: Inquisitive
- CHARACTER: Guy
  LINE: 25. Ro? What was her name? Terry what?
  EXPRESSION: Confused
- CHARACTER: Rosemary
  LINE: I don’t remember. An Italian name,
  EXPRESSION: Faint
- CHARACTER: Guy
  LINE: She was staying with people named Castevet, in Seven A.
  EXPRESSION: Informative
- CHARACTER: Second Policeman
  LINE: We’ve got that already.
  EXPRESSION: Dismissive
- CHARACTER: Narrator
  LINE: A THIRD POLICEMAN comes up holding a sheet of yellow notepaper, Mr. Nicklas is behind him, tight-mouthed, in a raincoat over striped pajamas.
  EXPRESSION: null
- CHARACTER: Third Policeman
  LINE: Short and sweet.
  EXPRESSION: Resigned
- CHARACTER: Narrator
  LINE: Handing over notepaper. She stuck it to the window sill with a band-aid.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The Third Policeman and Mr. Nicklas shake their heads.
  EXPRESSION: Disappointed
- CHARACTER: Narrator
  LINE: The Second Policeman reads the sheet of paper, sucking thoughtfully at his front teeth.
  EXPRESSION: Contemplative
- CHARACTER: Second Policeman
  LINE: Theresa Gionoffrio.
  EXPRESSION: Thoughtful (with an Italian accent)
- CHARACTER: Mr. Nicklas
  LINE: Did you know her?
  EXPRESSION: Direct
- CHARACTER: Rosemary
  LINE: Only slightly.
  EXPRESSION: Hesitant
- CHARACTER: Narrator
  LINE: The Second Policeman opens his pad holder and puts the paper inside it. He closes the holder with a width of yellow sticking out.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Guy puts his hand on Rosemary’s back.
  EXPRESSION: Comforting
- CHARACTER: Guy
  LINE: Come on, hon.
  EXPRESSION: Gentle
- CHARACTER: Narrator
  LINE: Rosemary and Guy nod to the 2nd Policeman and Mr. Nicklas and start towards the house.
  EXPRESSION: null
- CHARACTER: Mr. Nicklas
  LINE: Here they come now.
  EXPRESSION: Informative

::SCENE::
LOCATION: Street outside Apartment Building
MOOD: Anticipation, Foreboding
CHARACTERS: Narrator, Rosemary, Guy, Mrs. Castevet, Mr. Castevet, Second Policeman
BACKGROUND_IMAGE: street_outside_apartment_castevets.png
BACKGROUND_EDIT: "Night, street, an elderly couple approaching."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Rosemary and Guy stop and turn. An old couple is coming along the street.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: MRS. CASTEVET is wrapped in light blue, with snow-white dabs of gloves, purse, shoes and hat. Nurselike she supports her husband’s forearm. He is dazzling, in an every-color seersucker jacket, red slacks, a pink bow tie, and a grey fedora with a pink band. He is seventy-five or older; she is sixty-eight or nine. They come closer with expressions of young alertness, with friendly quizzical smiles.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The 2nd Policeman steps forward to meet them and their smiles falter and fall away. Mrs. Castevet says something worryingly; Mr. Castevet frowns and shakes his head. His wide thin-lipped mouth is rosy-pink, as if lipsticked; his cheeks are chalky, his eyes small and bright in deep sockets. She is big-nosed, with a sullen fleshy underlap. She wears pink-rimmed eyeglasses on a neck chain that dips down from behind plain pearly earrings.
  EXPRESSION: null
- CHARACTER: Second Policeman
  LINE: Are you folks the Caste vets on the seventh floor?
  EXPRESSION: Formal
- CHARACTER: Mr. Castevet
  LINE: We are.
  EXPRESSION: Dry (voice that has to be listened for)
- CHARACTER: Second Policeman
  LINE: You have a young woman named Theresa Gionoffrio living with you?
  EXPRESSION: Formal
- CHARACTER: Mr. Castevet
  LINE: We do. What’s wrong? Has there been an accident?
  EXPRESSION: Concerned
- CHARACTER: Second Policeman
  LINE: You’d better brace yourselves for some bad news. She’s dead. She killed herself. Jumped out of the window.
  EXPRESSION: Grave
- CHARACTER: Narrator
  LINE: Mr. and Mrs. Castevet look at the 2nd Policeman with no change of expression at all, as if he hasn’t spoken yet; then Mrs. Castevet leans sideways, glancing beyond him at the red-stained blanket. She stands straight again and looks him in the eyes.
  EXPRESSION: null
- CHARACTER: Mrs. Castevet
  LINE: That’s not possible. It’s a mistake.
  EXPRESSION: Disbelieving (Loud midwestern accent)
- CHARACTER: Second Policeman
  LINE: Artie, would you let these people take a look, please?
  EXPRESSION: Pleading (Without turning from her)
- CHARACTER: Narrator
  LINE: Mrs. Castevet marches past him, her jaw set. Mr. Castevet stays where he is.
  EXPRESSION: null
- CHARACTER: Mr. Castevet
  LINE: I knew this would happen. She got deeply depressed every three weeks or so. I told my wife but she pooh-poohed me.
  EXPRESSION: Resigned
- CHARACTER: Mrs. Castevet
  LINE: That doesn’t mean that she killed herself. She was a very happy girl with no reason for self-destruction. She must have been cleaning the windows or something.
  EXPRESSION: Defensive
- CHARACTER: Mr. Castevet
  LINE: She wasn’t cleaning windows at midnight.
  EXPRESSION: Assertive
- CHARACTER: Mrs. Castevet
  LINE: Why not? Maybe she was!
  EXPRESSION: Assertive
- CHARACTER: Narrator
  LINE: The 2nd Policeman takes the yellow paper from his holder and holds it out. Mrs. Castevet hesitates, then takes it and turns it round to read it. Mr. Castevet tips his head in over her arm and reads it too, his thin vivid lips moving.
  EXPRESSION: null
- CHARACTER: Second Policeman
  LINE: Is that her handwriting?
  EXPRESSION: Inquisitive
- CHARACTER: Mrs. Castevet
  LINE: Definitely. Absolutely.
  EXPRESSION: Affirmative
- CHARACTER: Narrator
  LINE: The 2nd Policeman holds out his hand and Mrs. Castevet gives him the paper.
  EXPRESSION: null
- CHARACTER: Second Policeman
  LINE: Thank you. I’ll see you get it back when we’re done with it.
  EXPRESSION: Polite
- CHARACTER: Narrator
  LINE: Mrs. Castevet takes off her glasses, dropping them on their neck-chain and covering both her eyes with white-gloved fingertips.
  EXPRESSION: null
- CHARACTER: Mrs. Castevet
  LINE: I don’t believe it. I just don’t believe it. She was so happy.
  EXPRESSION: Distraught
- CHARACTER: Narrator
  LINE: Mr. Castevet puts his hand on her shoulder, looks at the ground and shakes his head.
  EXPRESSION: null
- CHARACTER: Second Policeman
  LINE: Who is the next-of-kin?
  EXPRESSION: Direct
- CHARACTER: Mrs. Castevet
  LINE: She was all alone. She didn’t have anyone, only us.
  EXPRESSION: Sad
- CHARACTER: Rosemary
  LINE: Didn't she have a brother?
  EXPRESSION: Questioning
- CHARACTER: Narrator
  LINE: Mrs. Castevet puts on her glasses and looks at her. Mr. Castevet looks up from the ground, his deep-socketed eyes glinting under his hat brim.
  EXPRESSION: null
- CHARACTER: Second Policeman
  LINE: Did she?
  EXPRESSION: Inquisitive
- CHARACTER: Rosemary
  LINE: She said she did. In the Navy.
  EXPRESSION: Uncertain
- CHARACTER: Narrator
  LINE: The 2nd Policeman looks to the Castevets.
  EXPRESSION: null
- CHARACTER: Mrs. Castevet
  LINE: It’s news to me.
  EXPRESSION: Surprised
- CHARACTER: Second Policeman
  LINE: Do you know where he’s stationed?
  EXPRESSION: Inquisitive
- CHARACTER: Rosemary
  LINE: No, I don't. She mentioned him to me in the laundry room. I'm Rosemary Woodhouse.
  EXPRESSION: Factual
- CHARACTER: Guy
  LINE: We're in Seven E.
  EXPRESSION: Factual
- CHARACTER: Rosemary
  LINE: I feel just the way you do, Mrs. Castevet. She seemed so happy and full of - of - she said wonderful things about you and your husband; how grateful she was.
  EXPRESSION: Sympathetic
- CHARACTER: Mrs. Castevet
  LINE: Thank you.
  EXPRESSION: Appreciative
- CHARACTER: Second Policeman
  LINE: You know anything about this brother except he’s in the Navy?
  EXPRESSION: Inquisitive
- CHARACTER: Rosemary
  LINE: No.
  EXPRESSION: Negative
- CHARACTER: Mr. Castevet
  LINE: It should be easy to find him.
  EXPRESSION: Confident
- CHARACTER: Narrator
  LINE: Guy puts his hand on Rosemary's back and they begin to withdraw towards the house.
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: I’m so stunned and so sorry.
  EXPRESSION: Grieved
- CHARACTER: Guy
  LINE: It’s such a pity. It’s -
  EXPRESSION: Sad
- CHARACTER: Mrs. Castevet
  LINE: Thank you.
  EXPRESSION: Polite

::SCENE::
LOCATION: Guy's and Rosemary's Apartment - Bedroom
MOOD: Disturbed, Anxious
CHARACTERS: Narrator, Rosemary, Guy, Sister Agnes (voice), Mrs. Castevet (O.S.)
BACKGROUND_IMAGE: bedroom_night.png
BACKGROUND_EDIT: "Night, couple in bed, Rosemary awake."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Guy is asleep but Rosemary lies awake beside him, she sees: Terry’s pulped face and her one eye watching the sky. (This is the first shot leading to the dream sequence.) Sister Agnes is shaking her fist at Rosemary.
  EXPRESSION: null
- CHARACTER: Sister Agnes (voice)
  LINE: Sometimes I wonder how come you’re the leader of anything?
  EXPRESSION: Scolding (Mrs. Castevet’s voice)
- CHARACTER: Narrator
  LINE: A bump on the other side of the wall wakes Rosemary.
  EXPRESSION: null
- CHARACTER: Mrs. Castevet (O.S.)
  LINE: And please don’t tell me what Laura-Louise said because I’m not interested?
  EXPRESSION: Irritated
- CHARACTER: Narrator
  LINE: Rosemary turns over and burrows into her pillow.
  EXPRESSION: null

::SCENE::
LOCATION: Dream Sequence (?)
MOOD: Chaotic, Fragmented
CHARACTERS: Narrator, Masons, Sister Agnes, Uncle Mike, Other Sisters, Girls, Sister Veronica, Rosemary
BACKGROUND_IMAGE: dream_sequence.png
BACKGROUND_EDIT: "Composite of school, body shop, cinema candy counter."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Set in a composite of Our Lady’s School, Uncle Mike’s Body Shop and the candy counter in the Orpheum Cinema.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: MASONS are bricking up the windows. Sister Agnes is furious. She squeezes her piggy-eyes and shouts.
  EXPRESSION: null
- CHARACTER: Sister Agnes
  LINE: If you’d listened to me, we wouldn’t have had to do this! We’d have been all set to go now instead of starting all over from scratch!
  EXPRESSION: Furious
- CHARACTER: Narrator
  LINE: She points to the window.
  EXPRESSION: null
- CHARACTER: Uncle Mike
  LINE: I told you not to tell her anything in advance.
  EXPRESSION: Stern
- CHARACTER: Narrator
  LINE: Other SISTERS and GIRLS are standing a little apart listening to the argument.
  EXPRESSION: null
- CHARACTER: Sister Agnes
  LINE: I told you she wouldn’t be open-minded.
  EXPRESSION: Accusatory
- CHARACTER: Narrator
  LINE: She points at SISTER VERONICA who stands with her head lowered.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Uncle Mike looks questioningly at Rosemary. Rosemary starts to explain to him in a hushed voice.
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: I told Sister Veronica about the windows and she withdrew the school from the competition. Otherwise we would have won.
  EXPRESSION: Explanatory (hushed)
- CHARACTER: Narrator
  LINE: Uncle Mike looks at Sister Veronica questioningly who spreads her hands out wide in a helpless gesture. By this time we are already in Uncle Mike's body shop.
  EXPRESSION: null
- CHARACTER: Sister Agnes
  LINE: Anybody! Anybody! All she has to be is young, healthy, and not a virgin. She doesn’t have to be a no-good-drug-addict whore out of the gutter.
  EXPRESSION: Shouting
- CHARACTER: Narrator
  LINE: Uncle Mike is shocked. Rosemary turns and she is at the candy counter with the other children.
  EXPRESSION: null

::SCENE::
LOCATION: Kitchen
MOOD: Mundane, then Ominous
CHARACTERS: Narrator, Rosemary, Mrs. Gastevet (Mrs. Castevet)
BACKGROUND_IMAGE: kitchen_daytime.png
BACKGROUND_EDIT: "Daytime, kitchen interior, Rosemary washing vegetables."

::SCRIPT::
- CHARACTER: Narrator
  LINE: SEPTEMBER 20, 1965. Rosemary is washing the vegetables. The bell rings. She goes to the door and looks through the peephole.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Mrs. Gastevet, white hair in curlers under a blue-and-white kerchief, looks solemnly straight ahead as if posing for a photograph. Rosemary opens the door.
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: Hello. How are you?
  EXPRESSION: Polite
- CHARACTER: Mrs. Gastevet
  LINE: Fine.
  EXPRESSION: Bleak
- CHARACTER: Narrator
  LINE: She smiles bleakly. May I come in for a minute?
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: Yes, of course; please do.
  EXPRESSION: Welcoming
- CHARACTER: Narrator
  LINE: Rosemary holds the door wide open. Mrs. Gastevet comes in. She wears toreador pants; her hips and thighs are massive, slabbed with wide bands of fat. The pants are lime-green under a blue blouse; the blade of a screwdriver pokes from her hip pocket.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: They stop between the doorways of the den and the kitchen, Mrs. Gastevet puts on her neck chained glasses and smiles at Rosemary.
  EXPRESSION: null
- CHARACTER: Mrs. Castevet
  LINE: I just came over to thank you for saying those nice things to us the other night.
  EXPRESSION: Grateful
- CHARACTER: Rosemary
  LINE: Please, there’s no reason —
  EXPRESSION: Modest
- CHARACTER: Mrs. Castevet
  LINE: Poor Terry. We thought maybe we had failed her in some way, although her note made it crystal clear we hadn’t. You’ll never know how helpful it was, in such a shock moment. So I do thank you. Roman does too. Roman is my hubby.
  EXPRESSION: Sincere
- CHARACTER: Narrator
  LINE: Rosemary ducks her head in concession.
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: You're welcome. I’m glad I helped.
  EXPRESSION: Humble
- CHARACTER: Mrs. Castevet
  LINE: She was cremated yesterday. Now we have to forget and go on. It won’t be easy. We don’t have children of our own. Do yo
  EXPRESSION: Resigned

::SCENE::
LOCATION: Rosemary and Guy's Apartment - Kitchen
MOOD: Conversational
CHARACTERS: Mrs. Castevet, Rosemary
BACKGROUND_IMAGE: kitchen_day.png
BACKGROUND_EDIT: "Rosemary's apartment kitchen, daytime. Pans hanging on the wall, a table is set."

::SCRIPT::
- CHARACTER: Mrs. Castevet
  LINE: Oh, that’s nice. And look how you put the table, isn’t that interesting.
  EXPRESSION: Appraising
- CHARACTER: Rosemary
  LINE: It was in a magazine.
  EXPRESSION: Casual
- CHARACTER: Mrs. Castevet
  LINE: Nice paint job.
  EXPRESSION: Appreciative
- CHARACTER: Mrs. Castevet
  LINE: Oh, that’s nice. A T.V. room.
  EXPRESSION: Appreciative
- CHARACTER: Rosemary
  LINE: It's only temporary. It's going to be a nursery.
  EXPRESSION: Hopeful
- CHARACTER: Mrs. Castevet
  LINE: Are you pregnant?
  EXPRESSION: Direct
- CHARACTER: Rosemary
  LINE: Not yet, but I hope to be, as soon as we’re settled.
  EXPRESSION: Hopeful
- CHARACTER: Mrs. Castevet
  LINE: That’s wonderful. You’re young and healthy; you ought to have lots of children.
  EXPRESSION: Enthusiastic
- CHARACTER: Rosemary
  LINE: We plan to have three.
  EXPRESSION: Determined
- CHARACTER: Mrs. Castevet
  LINE: I’m dying to see what you’ve done to this apartment. The woman who had it before was a dear friend of mine.
  EXPRESSION: Eager
- CHARACTER: Rosemary
  LINE: I know. Terry told me.
  EXPRESSION: Informative
- CHARACTER: Mrs. Castevet
  LINE: Oh, did she? You two had some long talks together in the laundry room.
  EXPRESSION: Suspicious
- CHARACTER: Rosemary
  LINE: Only one.
  EXPRESSION: Firm
- CHARACTER: Mrs. Castevet
  LINE: My goodness! It looks so much brighter. What did you pay for a chair like that?
  EXPRESSION: Startled
- CHARACTER: Rosemary
  LINE: I’m not sure. I think it was about two hundred dollars.
  EXPRESSION: Unsure
- CHARACTER: Mrs. Castevet
  LINE: You don’t mind my asking do you? That’s how I got a big nose, by being nosy.
  EXPRESSION: Playful

::SCENE::
LOCATION: Rosemary and Guy's Apartment - Kitchen
MOOD: Friendly, Slightly Nosy
CHARACTERS: Rosemary, Mrs. Castevet
BACKGROUND_IMAGE: kitchen_day.png
BACKGROUND_EDIT: "Rosemary's apartment kitchen, daytime. Rosemary and Mrs. Castevet are seated at a table with coffee and cake."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Rosemary and Mrs. Castevet are sitting having coffee and cake.
  EXPRESSION: null
- CHARACTER: Mrs. Castevet
  LINE: I knew it! I said it to Roman yesterday. He’s so good-looking! What movies was he in?
  EXPRESSION: Excited
- CHARACTER: Rosemary
  LINE: No movies. He was in two plays called ’Luther' and ’Nobody Loves An Albatross’ and he does a lot of television and radio.
  EXPRESSION: Informative
- CHARACTER: Mrs. Castevet
  LINE: Listen, Rosemary, I’ve got a two inch thick sirloin steak sitting defrosting right this minute. Why don’t you and Guy come over and have supper with us tonight, what do you say?
  EXPRESSION: Inviting
- CHARACTER: Rosemary
  LINE: Oh, no. We couldn’t.
  EXPRESSION: Hesitant
- CHARACTER: Mrs. Castevet
  LINE: Why not?
  EXPRESSION: Puzzled
- CHARACTER: Rosemary
  LINE: This is very kind but really —
  EXPRESSION: Polite refusal
- CHARACTER: Mrs. Castevet
  LINE: It would be a big help to us.
  EXPRESSION: Pleading
- CHARACTER: Mrs. Castevet
  LINE: This’ll be the first night we’ll be alone since -
  EXPRESSION: Vulnerable
- CHARACTER: Rosemary
  LINE: If you’re sure it won’t be trouble for you.
  EXPRESSION: Concerned
- CHARACTER: Mrs. Castevet
  LINE: Honey, if it was trouble I wouldn’t ask you.
  EXPRESSION: Reassuring
- CHARACTER: Rosemary
  LINE: I’ll have to check with Guy, but you go ahead and count on us.
  EXPRESSION: Agreeable
- CHARACTER: Mrs. Castevet
  LINE: Listen! You tell him I won't take no for an answer!
  EXPRESSION: Determined
- CHARACTER: Mrs. Castevet
  LINE: Oh, here’s your mail, dear. Ads.
  EXPRESSION: Trivial
::PATHS::
- CHOICE: "Leave"
  TARGET: guy_rosemary_apartment
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Guy and Rosemary's Apartment - Living Room
MOOD: Domestic, Slightly Tense
CHARACTERS: Guy, Rosemary
BACKGROUND_IMAGE: apartment_living_room_day.png
BACKGROUND_EDIT: "Rosemary's apartment living room, daytime. New furniture, a bay window."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Guy come in, kisses Rosemary and goes straight into the living room. Rosemary goes into the kitchen. Guy calls out from the living room.
  EXPRESSION: null
- CHARACTER: Guy
  LINE: Donald Baumgart got that part.
  EXPRESSION: Excited
- CHARACTER: Rosemary
  LINE: It’s a bad play anyway.
  EXPRESSION: Dismissive
- CHARACTER: Guy
  LINE: Even if it folds out of town, it’s the kind of part that gets noticed.
  EXPRESSION: Determined
- CHARACTER: Narrator
  LINE: Guy opens the corner of his sandwich, looks in bitterly, closes it, and starts eating.
  EXPRESSION: Bitter
- CHARACTER: Rosemary
  LINE: Mrs. Castevet was here. To thank me for what I said about Terry. She’s the nosiest person I’ve ever seen. She actually asked the prices of things.
  EXPRESSION: Annoyed
- CHARACTER: Guy
  LINE: No kidding.
  EXPRESSION: Skeptical
- CHARACTER: Narrator
  LINE: Rosemary kneels on the floor between the bay windows, drawing a line on brown paper with crayon and a yardstick and then measuring the depth of the window seats.
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: She invited us to have dinner with them. I told her I’d have to check with you, but that it would probably be okay.
  EXPRESSION: Hesitant
- CHARACTER: Guy
  LINE: Ah, Jesus, Ro, we don't want to do that, do we?
  EXPRESSION: Resigned
- CHARACTER: Rosemary
  LINE: I think they’re lonely.
  EXPRESSION: Empathetic
- CHARACTER: Guy
  LINE: Honey, if we get friendly with an old couple like that we’re never going to get them off our necks, they’re right across the wall!
  EXPRESSION: Exasperated
- CHARACTER: Rosemary
  LINE: I told her she could count on us.
  EXPRESSION: Resolute
- CHARACTER: Guy
  LINE: I thought you told her you had to check first.
  EXPRESSION: Questioning
- CHARACTER: Rosemary
  LINE: I did, but I told her she could count on us too.
  EXPRESSION: Defensive
- CHARACTER: Guy
  LINE: Well, it’s not my night for being kind to Ma and Pa Kettle. I’m sorry, honey.
  EXPRESSION: Grudging
- CHARACTER: Rosemary
  LINE: All right, I'll tell her.
  EXPRESSION: Resigned
- CHARACTER: Narrator
  LINE: Rosemary draws another line with the crayon and the yardstick. Guy finishes his sandwich.
  EXPRESSION: null
- CHARACTER: Guy
  LINE: You don’t have to sulk about it.
  EXPRESSION: Impatient
- CHARACTER: Rosemary
  LINE: I’m not sulking. I see exactly what you mean.
  EXPRESSION: Understanding
- CHARACTER: Guy
  LINE: Oh, hell. We’ll go.
  EXPRESSION: Capitulating
- CHARACTER: Rosemary
  LINE: No, no, what for?
  EXPRESSION: Hesitant
- CHARACTER: Guy
  LINE: We’ll go.
  EXPRESSION: Decisive
- CHARACTER: Rosemary
  LINE: We don’t have to if you don’t want to. That sounds so phony but I really mean it, really I do.
  EXPRESSION: Sincere
- CHARACTER: Guy
  LINE: It’ll be my good deed for the day.
  EXPRESSION: Sarcastic
- CHARACTER: Rosemary
  LINE: Only if you want- to. And we ’ll make it clear that it’s only this one time and not the beginning of any­ thing. Right?
  EXPRESSION: Negotiating
- CHARACTER: Guy
  LINE: Right.
  EXPRESSION: Agreeable
::PATHS::
- CHOICE: "Go to Castevet's for dinner"
  TARGET: castevet_hallway
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Hallway - Outside Castevet's Apartment
MOOD: Apprehensive
CHARACTERS: Guy, Rosemary, Mr. DeVore
BACKGROUND_IMAGE: hallway_dusk.png
BACKGROUND_EDIT: "Apartment building hallway, dusk. Guy and Rosemary are at the Castevet's door. An elevator opens."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Guy and Rosemary at the Castevet's door. Guy rings the bell. The elevator behind them clangs open and Mr. DeVore comes out carrying a suit swathed in cleaner’s plastic. He smiles and unlocks the door of Seven B next to them.
  EXPRESSION: null
- CHARACTER: Mr. DeVore
  LINE: You’re in the wrong place, aren’t you?
  EXPRESSION: Amused
- CHARACTER: Narrator
  LINE: Rosemary and Guy make friendly laughs.
  EXPRESSION: null
- CHARACTER: Mr. DeVore
  LINE: Me!
  EXPRESSION: Calling out
- CHARACTER: Narrator
  LINE: As the door is ajar we get a glimpse of a black sideboard and red and gold wallpaper.
  EXPRESSION: null
::PATHS::
- CHOICE: "Enter Castevet's apartment"
  TARGET: castevet_apartment_foyer
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Castevet's Apartment - Foyer
MOOD: Unsettling, Oddly Furnished
CHARACTERS: Mrs. Castevet, Guy, Rosemary, Mr. Castevet
BACKGROUND_IMAGE: castevet_apartment_foyer.png
BACKGROUND_EDIT: "Castevet's apartment foyer, dusk. A dining table is set for four. The room has contrasting styles of furniture."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Mrs. Castevet opens the door. She is powdered and rouged and smiling broadly. She is wearing light green silk with a frilled pink apron.
  EXPRESSION: null
- CHARACTER: Mrs. Castevet
  LINE: Perfect timing! Come on in! Roman’s making Vodka Blushes. My, I’m glad you could come, Guy! I’m fixing to tell people I knew you when!
  EXPRESSION: Overly enthusiastic
- CHARACTER: Narrator
  LINE: Guy and Rosemary laugh and exchange glances. They enter.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: A large foyer with a rectangular table set for four. It has an embroidered white cloth, plates that don’t all match, and bright ranks of ornate silver. The room is oddly furnished? at the fireplace end. there is a settee, a lamp table and a few chairs. At the opposite end an office-like clutter of file cabinets, bridge tables piled with newspapers, overfilled book­shelves and a typewriter on a metal stand. There are clean squares on the walls as if pictures had been removed.
  EXPRESSION: null
- CHARACTER: Mrs. Castevet
  LINE: Please, sit down. Mrs. Woodhouse?
  EXPRESSION: Welcoming
- CHARACTER: Narrator
  LINE: Rosemary takes the glass, thanks him and sits. Mrs. Castevet quickly puts a paper cocktail napkin in her lap.
  EXPRESSION: null
- CHARACTER: Mr. Castevet
  LINE: Mr. Woodhouse? A Vodka Blush. Have you ever tasted one?
  EXPRESSION: Inquiring
- CHARACTER: Guy
  LINE: No.
  EXPRESSION: Simple
- CHARACTER: Mrs. Castevet
  LINE: Minnie.
  EXPRESSION: Informative
- CHARACTER: Rosemary
  LINE: It looks delicious.
  EXPRESSION: Polite
- CHARACTER: Narrator
  LINE: Rosemary smiles vividly as she wipes the base of her glass.
  EXPRESSION: null
- CHARACTER: Mr. Castevet
  LINE: They’re very popular in Australia.
  EXPRESSION: Informative
- CHARACTER: Mr. Castevet
  LINE: To our guests. Welcome to our home.
  EXPRESSION: Welcoming
- CHARACTER: Narrator
  LINE: Mr. Castevet drinks, cocking his head critically, one eye partway closed, the tray at his side dripping on the carpet.
  EXPRESSION: null
- CHARACTER: Mrs. Castevet
  LINE: The carpet!
  EXPRESSION: Alarmed
- CHARACTER: Narrator
  LINE: Mrs. Castevet chokes and points at the carpet. Mr. Castevet looks down, then holds the tray up un­certainly.
  EXPRESSION: null
- CHARACTER: Mr. Castevet
  LINE: Oh, dear.
  EXPRESSION: Apologetic
- CHARACTER: Narrator
  LINE: Mrs. Castevet thrusts aside her drink, hurries to her knees and lays a paper napkin carefully over the wetness.
  EXPRESSION: null
- CHARACTER: Mrs. Castevet
  LINE: Brand-new carpet. This man is so clumsy.
  EXPRESSION: Annoyed
- CHARACTER: Rosemary
  LINE: Do you come from Australia?
  EXPRESSION: Curious
- CHARACTER: Mr. Castevet
  LINE: Oh no. I’m from right here in New York City. I've been there though. I've been everywhere. Literally. You name a place and I've been there. Go ahead. Name a place.
  EXPRESSION: Boastful
- CHARACTER: Guy
  LINE: Fairbanks, Alaska.
  EXPRESSION: Challenging
- CHARACTER: Mr. Castevet
  LINE: I've been there. I've been all over Alaska? Fairbanks, Juneau, Anchorage, Nome, Seward? I spent four months there in '38.
  EXPRESSION: Proud
- CHARACTER: Mrs. Castevet
  LINE: Where are you folks from?
  EXPRESSION: Inquiring
- CHARACTER: Rosemary
  LINE: I'm from Omaha. Guy is from Baltimore.
  EXPRESSION: Informative
- CHARACTER: Mr. Castevet
  LINE: Omaha is a good city, Baltimore is too.
  EXPRESSION: Agreeable
- CHARACTER: Rosemary
  LINE: Do you travel for business?
  EXPRESSION: Curious
- CHARACTER: Mr. Castevet
  LINE: Business and pleasure both, I’m seventy-nine and I've been going one place or another since I was ten. You name it, I've been there.
  EXPRESSION: Vain
- CHARACTER: Narrator
  LINE: A bell pings in the kitchen.
  EXPRESSION: null
- CHARACTER: Mrs. Castevet
  LINE: Steak's ready. Don't rush your drinks now; Roman, take your pill.
  EXPRESSION: Directing
::PATHS::
- CHOICE: "Move to dining room"
  TARGET: castevet_dining_room
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Castevet's Apartment - Dining Room
MOOD: Domestic, Uneasy
CHARACTERS: Guy, Rosemary, Mr. Castevet, Mrs. Castevet
BACKGROUND_IMAGE: castevet_apartment_dining_room.png
BACKGROUND_EDIT: "Castevet's apartment dining room, dusk. The four are seated at the table, eating."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Guy, Rosemary, Mr. and Mrs. Castevet are sitting at the table, eating.
  EXPRESSION: null
- CHARACTER: Mr. Castevet
  LINE: No Pope ever visits a
  EXPRESSION: Mid-sentence
::PATHS::
- CHOICE: "Continue eating"
  TARGET: end
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: KITCHEN
MOOD: Awkward
CHARACTERS: Narrator, Mrs. Castevet, Guy, Rosemary, Mr. Castevet
BACKGROUND_IMAGE: kitchen.png
BACKGROUND_EDIT: "Nighttime, Newspaper strike implied by conversation"

::SCRIPT::
- CHARACTER: Narrator
  LINE: city where the newspapers are on strike.
  EXPRESSION: null
- CHARACTER: Mrs. Castevet
  LINE: I heard he's going to postpone and wait till it’s over.
  EXPRESSION: null
- CHARACTER: Guy
  LINE: Well, that's showbiz.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Mr. and Mrs. Castevet laugh, Guy along with them.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Rosemary smiles and cuts her steak. It is difficult to cut, and flanked by peas and mashed potatoes. From her expression we can gather it doesn't taste good either.
  EXPRESSION: null

::SCENE::
LOCATION: KITCHEN
MOOD: Tense
CHARACTERS: Narrator, Mr. Castevet, Mrs. Castevet, Rosemary, Guy
BACKGROUND_IMAGE: kitchen.png
BACKGROUND_EDIT: "Nighttime, table setting with food"

::SCRIPT::
- CHARACTER: Mr. Castevet
  LINE: That's just what it is. The costumes, the rituals.
  EXPRESSION: Laughing
- CHARACTER: Mrs. Castevet
  LINE: I think we're offending Rosemary.
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: No, no, not at all.
  EXPRESSION: null
- CHARACTER: Mr. Castevet
  LINE: You aren't religious, my dear, are you?
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: I was brought up a Catholic, now I don’t know.
  EXPRESSION: null
- CHARACTER: Mrs. Castevet
  LINE: You looked uncomfortable.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Mrs. Castevet stands up and starts to collect the empty plates.
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: Well, he is the Pope.
  EXPRESSION: null
- CHARACTER: Mr. Castevet
  LINE: You don't need to have respect for him because he pretends he is holy.
  EXPRESSION: null
- CHARACTER: Guy
  LINE: Good point.
  EXPRESSION: null
- CHARACTER: Mrs. Castevet
  LINE: When I think what they spend on robes and jewels.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Mrs. Castevet serves the dessert; Boston cream pie.
  EXPRESSION: null
- CHARACTER: Mr. Castevet
  LINE: A good picture of the hypocrisy behind organized religion was given. I thought in ’Luther'. Did you ever get to play the leading parts. Guy?
  EXPRESSION: null
- CHARACTER: Guy
  LINE: Me? No.
  EXPRESSION: null
- CHARACTER: Mr. Castevet
  LINE: Weren’t you Albert Finney’s understudy?
  EXPRESSION: null
- CHARACTER: Guy
  LINE: No.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: We can see from Rosemary's expression that the Boston cream pie isn’t too good. She looks at Guy but he is eating away avidly.
  EXPRESSION: null
- CHARACTER: Mr. Castevet
  LINE: That’s strange. I remember being struck by a gesture you made and checking in the program to see who you were.
  EXPRESSION: null
- CHARACTER: Guy
  LINE: What gesture do you mean?
  EXPRESSION: null
- CHARACTER: Mr. Castevet
  LINE: I'm not sure now^ a movement of your -
  EXPRESSION: null
- CHARACTER: Guy
  LINE: I used to do a thing with my arms when Luther had the fit; a sort of involuntary reaching -
  EXPRESSION: null
- CHARACTER: Mr. Castevet
  LINE: That’s it! It had a wonderful authenticity to it.
  EXPRESSION: null
- CHARACTER: Guy
  LINE: Oh, come on now.
  EXPRESSION: null
- CHARACTER: Mr. Castevet
  LINE: Oh no, I mean it.
  EXPRESSION: null
- CHARACTER: Guy
  LINE: That makes two of us.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Guy laughs but he is pleased. He casts a bright-eyed glance at Rosemary. She smiles back.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Mrs. Castevet holds out the Boston cream pie towards Guy.
  EXPRESSION: null
- CHARACTER: Mrs. Castevet
  LINE: Guy?
  EXPRESSION: null
- CHARACTER: Guy
  LINE: Oh yes, please.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Rosemary looks in surprise at Guy who is helping himself to the dessert.
  EXPRESSION: null

::SCENE::
LOCATION: KITCHEN
MOOD: Supportive/Observational
CHARACTERS: Narrator, Mr. Castevet, Guy, Rosemary, Mrs. Castevet
BACKGROUND_IMAGE: kitchen.png
BACKGROUND_EDIT: "Nighttime, miniature greenhouse on table"

::SCRIPT::
- CHARACTER: Mr. Castevet
  LINE: My father was a theatrical producer. My early years were spent in the company of such people as Mrs. Fiske, Forbes-Robertson, Modjeska. You have a most interesting inner quality, Guy. It appears in your television work too, and it should carry you very far indeed, provided, of course, that you get those initial ’breaks'. Are you preparing for a show now?
  EXPRESSION: null
- CHARACTER: Guy
  LINE: I'm up for a couple of parts.
  EXPRESSION: null
- CHARACTER: Mr. Castevet
  LINE: I can’t believe that you won’t get them.
  EXPRESSION: null
- CHARACTER: Guy
  LINE: I can.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: It opens off the foyer. It’s small and it has the miniature greenhouse, which stands on a large white table near the one window. Goosenecked lamps with bright bulbs lean over it with a blinding white light, reflecting in the glass. In the remaining space the sink, stove and refrigerator stand close together with cabinets jutting out on all sides above them.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Mrs. Castevet stands at the sink washing up. Rosemary stands beside her drying. The pile of clean dishes beside her indicate that they have been in the kitchen for some time. While drying a dish, Rosemary turns and looks at the greenhouse.
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: I’d like to have a spice garden some day, I’m a country girl at heart.
  EXPRESSION: null
- CHARACTER: Mrs. Castevet
  LINE: Do you come from a big family?
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: Three brothers and two sisters,
  EXPRESSION: null
- CHARACTER: Mrs. Castevet
  LINE: Are your sisters married?
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: Yes, they are,
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Mrs. Castevet pushes a soapy sponge up and down inside a dinner glass. She is a slow and thorough washer. Rosemary has to wait each time, towel in hand, for the next piece.
  EXPRESSION: null
- CHARACTER: Mrs. Castevet
  LINE: Do they have children?
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: One has two and the other has four.
  EXPRESSION: null
- CHARACTER: Mrs. Castevet
  LINE: Well, there’s a chance you will have lots of children too.
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: Oh, we’re fertile, all right. I’ve got twenty nieces and nephews.
  EXPRESSION: null
- CHARACTER: Mrs. Castevet
  LINE: My goodness!
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: Would you like me to wash and you wipe for a while?
  EXPRESSION: null
- CHARACTER: Mrs. Castevet
  LINE: No, this is fine, dear.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Rosemary looks outside the door. She can see only the end of the living room that has bridge tables and file cabinets. Mr. Castevet and Guy are out of sight. A plane of blue cigarette smoke lies motionless in the air.
  EXPRESSION: null
- CHARACTER: Mrs. Castevet
  LINE: Rosemary?
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Rosemary turns. Mrs. Castevet, smiling, holds out a wet plate in a green rubber-gloved hand.
  EXPRESSION: null

::SCENE::
LOCATION: LIVING ROOM
MOOD: Conversational/Intriguing
CHARACTERS: Narrator, Mr. Castevet, Guy, Rosemary, Mrs. Castevet
BACKGROUND_IMAGE: living_room.png
BACKGROUND_EDIT: "Nighttime, settee, doorway"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Mr. Castevet and Guy are sitting facing each other on the settee. Guy is looking at Mr. Castevet, fascinated. They smoke for the moment in silence. Rosemary appears in the doorway.
  EXPRESSION: null
- CHARACTER: Mr. Castevet
  LINE: Take Kennedy for example. Do you think it could have been a plot of some kind?
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Mrs. Castevet comes past Rosemary into the room.
  EXPRESSION: null
- CHARACTER: Mrs. Castevet
  LINE: Now Roman, you stop bending Guy’s ear with your Modjeska stories. He’s only listening 'cause he's polite.
  EXPRESSION: null
- CHARACTER: Guy
  LINE: No, it’s interesting, Mrs. Castevet.
  EXPRESSION: null
- CHARACTER: Mr. Castevet
  LINE: You see?
  EXPRESSION: null
- CHARACTER: Mrs. Castevet
  LINE: Minnie, I’m Minnie and he's Roman, okay?
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Looking mock-defiantly at Rosemary
  EXPRESSION: null
- CHARACTER: Mrs. Castevet
  LINE: Okay?
  EXPRESSION: null
- CHARACTER: Guy
  LINE: Okay, Minnie.
  EXPRESSION: null

::SCENE::
LOCATION: HALLWAY OUTSIDE THE CASTEVET'S APARTMENT
MOOD: Relief/Playful
CHARACTERS: Narrator, Rosemary, Guy
BACKGROUND_IMAGE: hallway.png
BACKGROUND_EDIT: "Nighttime, apartment door"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Rosemary and Guy go along the hallway and the door closes behind them. They both give relieved sighs, look at each other and laugh.
  EXPRESSION: null
- CHARACTER: Guy
  LINE: Naow Roman, yew stop bendin’ Guy's ee-yurs with them thar Mojestky sto-rees!
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Laughing, Rosemary hushes him. They run hand in hand on ultra-quiet tiptoes to their own door.
  EXPRESSION: null

::SCENE::
LOCATION: GUY'S AND ROSEMARY'S APARTMENT
MOOD: Humorous/Exaggerated Relief
CHARACTERS: Narrator, Guy, Rosemary
BACKGROUND_IMAGE: apartment.png
BACKGROUND_EDIT: "Nighttime, interior of apartment"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Rosemary and Guy slam, lock, bolt and chain the door; Guy nails it over with imaginary beams, pushes up three imaginary boulders, hoists an imaginary drawbridge, mops his brow and pants while Rosemary bends over double and laughs into both hands.
  EXPRESSION: null
- CHARACTER: Guy
  LINE: About that steak.
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: Oh my God! The pie! How did you eat two pieces? It was weird!
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Guy pretends that he is going to vomit and runs to the bedroom.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Rosemary works her feet against the floor to unshoe them.
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: Only three dinner plates that match..
  EXPRESSION: null
- CHARACTER: Guy
  LINE: Shhh —
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: ...and all that beautiful, beautiful silver.
  EXPRESSION: null
- CHARACTER: Guy
  LINE: Let’s be nice; maybe they'll will it to us.
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: Guess what they’ve got in the bathroom.
  EXPRESSION: null
- CHARACTER: Guy
  LINE: A bidet.
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: 'Jokes for the John'.
  EXPRESSION: null
- CHARACTER: Guy
  LINE: No.
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: A book on a hook. Right next to the toilet.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Guy smiles and shakes his head. He begins taking out his cufflinks, standing beside the armoire.
  EXPRESSION: null
- CHARACTER: Guy
  LINE: Roman's stories were pretty damn interesting, actually. I’d never even heard of Forbes-Robertson before.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Working at the second link, having trouble with it
  EXPRESSION: null
- CHARACTER: Guy
  LINE: I’m going to go over there again tomorrow night and hear some more.
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: You are?
  EXPRESSION: Disconcerted
- CHARACTER: Guy
  LINE: He asked me.
  EXPRESSION: null
- CHARACTER: Guy
  LINE: Can you get this off for me?
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Rosemary goes to him and works at the link, feeling suddenly lost and uncertain.
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: I thought we were going to do something with Dick and Joan Jellico.
  EXPRESSION: null
- CHARACTER: Guy
  LINE: Was that definite?
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: It wasn't definite.
  EXPRESSION: null
- CHARACTER: Guy
  LINE: We’ll see them next week.
  EXPRESSION: Shrugging
- CHARACTER: Narrator
  LINE: Rosemary gets the link out and holds it in her palm. Guy takes it.
  EXPRESSION: null
- CHARACTER: Guy
  LINE: Thanks. You don’t have to come along if you don’t want to; you can stay here.
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: I think I will. Stay here.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Rosemary goes to the bed and sits down.
  EXPRESSION: null
- CHARACTER: Guy
  LINE: He knew Henry Irving too. Really interesting.
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: Why did they take down the pictures.
  EXPRESSION: null
- CHARACTER: Guy
  LINE: What do you mean?
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: Their pictures; they took them down. There are hooks in the wall and clean places. And the one picture that is there doesn’t fit.
  EXPRESSION: null
- CHARACTER: Guy
  LINE: I didn’t notice.
  EXPRESSION: null

::SCENE::
LOCATION: GUY AND ROSEMARY’S APARTMENT
MOOD: Quiet/Domestic
CHARACTERS: Narrator, Rosemary, Mrs. Castevet, Laura-Louise McBurney
BACKGROUND_IMAGE: apartment_dusk.png
BACKGROUND_EDIT: "Dusk, new couch, record player"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Rosemary puts a record on, picks up a hook, sits on the new couch, puts up her feet and opens the book.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The doorbell rings. She remains motionless for a moment. Then, closes the book, gets up and goes to the door.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: It’s Mrs. Castevet and another woman, short, plump and smiling, with a Buckley-for-Mayor button on the shoulder of her green dress.
  EXPRESSION: null
- CHARACTER: Mrs. Castevet
  LINE: Hi, dear, we’re not bothering you, are we? This is my dear friend Laura-Louise McBurney, who lives up on twelve. Laura-Louise, this is Guy’s wife Rosemary.
  EXPRESSION: null
- CHARACTER: Laura-Louise
  LINE: Hello, Rosemary, welcome to the Bram!
  EXPRESSION: null
- CHARACTER: Mrs. Castevet
  LINE: Laura-Louise just met Guy and she wanted to meet you too. Can we come in?
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: With resigned good grace Rosemary shows them into the living room. Mrs. Castevet indicates a new couch.
  EXPRESSION: null
- CHARACTER: Mrs. Castevet
  LINE: Oh, isn’t it beautiful!
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: It came this morning.
  EXPRESSION: null
- CHARACTER: Mrs. Castevet
  LINE: Are you all right, dear. You look worn.
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: I’m fine.
  EXPRESSION: Smiling
- CHARACTER: Rosemary
  LINE: It’s the first day of my period.
  EXPRESSION: null
- CHARACTER: Laura-Louise
  LINE: And you’re up and around?
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Sitting
  EXPRESSION: null
- CHARACTER: Laura-Louise
  LINE: On my first day I experienced such pain that I couldn’t move or eat or anything. Dan had to give me gin through a straw to kill the pain.
  EXPRESSION: null
- CHARACTER: Mrs. Castevet
  LINE: Girls today take things more in their stride.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Sitting
  EXPRESSION: null
- CHARACTER: Mrs. Castevet
  LINE: They’re healthier than we were, thanks to vitamins and better medical care.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Both women have identical green sewing bags and, to Rosemary’s surprise, they open them now.
  EXPRESSION: null

::SCENE::
LOCATION: Castevet's Apartment - Living Room
MOOD: Tense
CHARACTERS: Narrator, Mrs. Castevet, Laura-Louise, Rosemary
BACKGROUND_IMAGE: castevet_apartment_living_room_day.png
BACKGROUND_EDIT: "Afternoon, women are engaged in needlework"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Mrs. Castevet takes out darning and Laura-Louise takes out crocheting.
  EXPRESSION: null
- CHARACTER: Mrs. Castevet
  LINE: What’s that over there? Seat covers?
  EXPRESSION: Curious
- CHARACTER: Rosemary
  LINE: Cushions for the window seats.
  EXPRESSION: Neutral
- CHARACTER: Narrator
  LINE: Rosemary stands for a moment undecidedly. She sits uneasily, trying to find a comfortable position.
  EXPRESSION: Uneasy
- CHARACTER: Mrs. Castevet
  LINE: Oh, before I forget. This is for you. From Roman and me.
  EXPRESSION: Kindly
- CHARACTER: Narrator
  LINE: Mrs. Castevet hands Rosemary a small packet of pink tissue paper.
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: For me?
  EXPRESSION: Surprised
- CHARACTER: Mrs. Castevet
  LINE: It’s just a little present is all. For moving in.
  EXPRESSION: Dismissive
- CHARACTER: Rosemary
  LINE: But there's no reason...
  EXPRESSION: Hesitant
- CHARACTER: Narrator
  LINE: Rosemary unfolds the leaves of used-before tissue paper. Within the pink is Terry’s silver filigree ball-charm and its clustered-together neck chain. She pulls her head away.
  EXPRESSION: Disturbed
- CHARACTER: Mrs. Castevet
  LINE: It's real old. Over three hundred years.
  EXPRESSION: Proud
- CHARACTER: Narrator
  LINE: Rosemary holds the ball between her thumb and fingertips like Terry did. She stares at it for a moment.
  EXPRESSION: Pensive
- CHARACTER: Rosemary
  LINE: It's lovely.
  EXPRESSION: Polite
- CHARACTER: Mrs. Castevet
  LINE: The green inside is called tannis root. It's good luck.
  EXPRESSION: Matter-of-fact
- CHARACTER: Rosemary
  LINE: It's lovely, but I can't accept such a -
  EXPRESSION: Reluctant
- CHARACTER: Mrs. Castevet
  LINE: You already have.
  EXPRESSION: Firm
- CHARACTER: Narrator
  LINE: Mrs. Castevet darns a brown sock not looking at Rosemary.
  EXPRESSION: Uncaring
- CHARACTER: Mrs. Castevet
  LINE: Put it on.
  EXPRESSION: Commanding
- CHARACTER: Laura-Louise
  LINE: You’ll get used to the smell before you know it.
  EXPRESSION: Encouraging
- CHARACTER: Mrs. Castevet
  LINE: Go on.
  EXPRESSION: Insistent
- CHARACTER: Rosemary
  LINE: Well, thank you.
  EXPRESSION: Resigned
- CHARACTER: Narrator
  LINE: Rosemary uncertainly puts the chain over her head and tucks the ball into the collar of her dress.
  EXPRESSION: Apprehensive

::SCENE::
LOCATION: Guy and Rosemary's Apartment - Living Room
MOOD: Domestic
CHARACTERS: Narrator, Guy, Rosemary, Mrs. Castevet, Laura-Louise
BACKGROUND_IMAGE: guy_rosemary_apartment_living_room_night.png
BACKGROUND_EDIT: "Night, women are in similar positions, tray with coffee"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Guy opens the door of the apartment, comes in and goes into the living room.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The women are seated in different positions as before. Rosemary is sewing the cushion covers and there's a tray with coffee pot and cups on the table. Guy says hello to the women and, by Rosemary’s chair, bends and kisses her cheek. He is quiet and a little self-contained.
  EXPRESSION: Quiet
- CHARACTER: Mrs. Castevet
  LINE: Eleven? My land! Come on, Laura-Louise.
  EXPRESSION: Surprised
- CHARACTER: Laura-Louise
  LINE: Come and visit me any time, you want, Rosemary; I’m in twelve F.
  EXPRESSION: Friendly
- CHARACTER: Narrator
  LINE: The two women close their sewing bags and leave quickly.
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: Were his stories as interesting as last night?
  EXPRESSION: Inquisitive
- CHARACTER: Guy
  LINE: Yes. Did you have a nice time?
  EXPRESSION: Neutral
- CHARACTER: Rosemary
  LINE: All right. I got a present.
  EXPRESSION: Neutral
- CHARACTER: Narrator
  LINE: She shows him the charm.
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: It was Terry’s.
  EXPRESSION: Neutral
- CHARACTER: Guy
  LINE: No kidding! It's pretty though.
  EXPRESSION: Interested
- CHARACTER: Narrator
  LINE: Rosemary lifts the chain off over her head and holds it out between two fingers, the ball dangling at the end of the chain.
  EXPRESSION: null
- CHARACTER: Guy
  LINE: Aren't you going to wear it?
  EXPRESSION: Curious
- CHARACTER: Rosemary
  LINE: It smells. There's stuff in it called tennis root. From her green­house.
  EXPRESSION: Disgusted
- CHARACTER: Guy
  LINE: It's not bad.
  EXPRESSION: Shrugging
- CHARACTER: Narrator
  LINE: Rosemary goes into the bedroom and as she opens a drawer in the vanity, she catches her reflection in the mirror. She leans towards it and calls?
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: Tannis, anyone?
  EXPRESSION: Sarcastic
- CHARACTER: Guy
  LINE: If you took it, you ought to wear it.
  EXPRESSION: Suggestive
- CHARACTER: Narrator
  LINE: Rosemary turns? Guy is leaning against the door frame. Instead of answering Rosemary opens a tin Louis Sherry box in the drawer, puts the charm in the box, closes it and closes the drawer.
  EXPRESSION: Determined

::SCENE::
LOCATION: Guy and Rosemary's Apartment - Bedroom
MOOD: Intimate
CHARACTERS: Narrator, Rosemary, Guy
BACKGROUND_IMAGE: guy_rosemary_apartment_bedroom_night.png
BACKGROUND_EDIT: "Night, Rosemary wakes to find Guy smoking"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Rosemary wakes up and finds Guy beside her smoking in the dark.
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: What’s the matter?
  EXPRESSION: Concerned
- CHARACTER: Guy
  LINE: Nothing.
  EXPRESSION: Vague
- CHARACTER: Narrator
  LINE: A moment of silence, then she touches his arm.
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: Don’t worry.
  EXPRESSION: Reassuring
- CHARACTER: Guy
  LINE: About what?
  EXPRESSION: Doubtful
- CHARACTER: Rosemary
  LINE: About anything.
  EXPRESSION: Reassuring
- CHARACTER: Guy
  LINE: All right. I won’t.
  EXPRESSION: Resigned
- CHARACTER: Rosemary
  LINE: You’re the greatest. You know? And it's going to come out right.
  EXPRESSION: Affectionate
- CHARACTER: Narrator
  LINE: Guy smiles in the glow of his cigarette.
  EXPRESSION: Fond
- CHARACTER: Rosemary
  LINE: Any day now. Something big. Something worthy of you.
  EXPRESSION: Hopeful
- CHARACTER: Guy
  LINE: I know. Go to sleep, honey.
  EXPRESSION: Gentle
- CHARACTER: Rosemary
  LINE: Okay. Watch the cigarette.
  EXPRESSION: Affectionate
- CHARACTER: Guy
  LINE: I will.
  EXPRESSION: Loving
- CHARACTER: Rosemary
  LINE: I love you.
  EXPRESSION: Loving
- CHARACTER: Guy
  LINE: I love you, Ro.
  EXPRESSION: Loving

::SCENE::
LOCATION: Guy and Rosemary's Apartment - Living Room
MOOD: Expectant
CHARACTERS: Narrator, Guy, Rosemary
BACKGROUND_IMAGE: guy_rosemary_apartment_living_room_day_sept25.png
BACKGROUND_EDIT: "Daytime, September 25, 1965, Guy offers tickets"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Guy holds out a pair of theatre tickets to Rosemary.
  EXPRESSION: null
- CHARACTER: Guy
  LINE: Here, these are for the 'Fanta­sticks”. Alan Stone gave them to me so why don't you call Hutch or somebody and go and see it.
  EXPRESSION: Casual
- CHARACTER: Rosemary
  LINE: Aren’t you going to see it with me?
  EXPRESSION: Disappointed
- CHARACTER: Guy
  LINE: I saw it ages ago.
  EXPRESSION: Dismissive

::SCENE::
LOCATION: Taxi - Avenue
MOOD: Conversational
CHARACTERS: Narrator, Elise Dunstan, Rosemary, Driver
BACKGROUND_IMAGE: taxi_avenue_night.png
BACKGROUND_EDIT: "Night, driving along an avenue, taxi interior"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Elise Dunstan and Rosemary, dressed for the theatre in her summer silk coat, sitting in the back. There is a fat, old DRIVER listening to their conversation.
  EXPRESSION: null
- CHARACTER: Elise Dunstan
  LINE: This is a break for me to get away from my three monsters.
  EXPRESSION: Relieved
- CHARACTER: Rosemary
  LINE: That's what we’re going to have. Three, two years apart.
  EXPRESSION: Excited
- CHARACTER: Elise Dunstan
  LINE: You’re not pregnant, are you?
  EXPRESSION: Incredulous
- CHARACTER: Rosemary
  LINE: I wish I was, Elise, Guy is "not ready yet”.
  EXPRESSION: Frustrated
- CHARACTER: Elise Dunstan
  LINE: Well -
  EXPRESSION: Understanding
- CHARACTER: Rosemary
  LINE: I'm afraid he’ll never be ready, until he’s like Marlon Brando and Richard Burton put together.
  EXPRESSION: Humorous
- CHARACTER: Narrator
  LINE: They giggle.
  EXPRESSION: null
- CHARACTER: Elise Dunstan
  LINE: All men feel the same way. You have plenty of time.
  EXPRESSION: Reassuring
- CHARACTER: Rosemary
  LINE: I have my little plan. I’m going to get pregnant by accident.
  EXPRESSION: Determined
- CHARACTER: Elise Dunstan
  LINE: Are you taking pills?
  EXPRESSION: Curious
- CHARACTER: Narrator
  LINE: Rosemary shakes her head.
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: I told Guy they give me a head­ache, and the rubber gadgets are repulsive. So he studies the calendar like mad. But I’ll get him anyway.
  EXPRESSION: Mischievous
- CHARACTER: Narrator
  LINE: They laugh.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The Driver looks in the mirror and grins.
  EXPRESSION: Amused
- CHARACTER: Elise Dunstan
  LINE: You mustn’t do that, Rosie, it’s a terrible thing to do to a man.
  EXPRESSION: Concerned
- CHARACTER: Rosemary
  LINE: It’s a contest between us.
  EXPRESSION: Playful
- CHARACTER: Elise Dunstan
  LINE: Contest? He doesn’t know he's engaged in it.
  EXPRESSION: Amused

::SCENE::
LOCATION: Theatre
MOOD: Anticipatory
CHARACTERS: Narrator, Elise Dunstan, Rosemary, Driver
BACKGROUND_IMAGE: theatre_exterior_night.png
BACKGROUND_EDIT: "Night, exterior of a theatre, illuminated sign"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The taxi stops in front of a theatre. There is a big illuminated sign with "The Fantasticks” and the names of artists.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Elise Dunstan and Rosemary get out of the cab and turn to pay the fare.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The Driver has a good look at Rosemary.
  EXPRESSION: null
- CHARACTER: Driver
  LINE: Lot’sa luck, lady.
  EXPRESSION: Friendly
- CHARACTER: Narrator
  LINE: Rosemary and Elise Dunstan go into the theatre.
  EXPRESSION: null

::SCENE::
LOCATION: Guy and Rosemary's Apartment - Living Room/Bathroom/Kitchen
MOOD: Intimate/Domestic
CHARACTERS: Narrator, Rosemary, Guy
BACKGROUND_IMAGE: guy_rosemary_apartment_night_post_theatre.png
BACKGROUND_EDIT: "Night, Rosemary and Guy in their apartment after the theatre"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Rosemary, taking off her silk coat, goes into the Bathroom. Guy is getting out of the shower, wrapping himself in a towel. He kisses Rosemary vivaciously.
  EXPRESSION: null
- CHARACTER: Guy
  LINE: How was it?
  EXPRESSION: Eager
- CHARACTER: Rosemary
  LINE: Wonderful, wonderful. You worked on your scene?
  EXPRESSION: Enthusiastic
- CHARACTER: Guy
  LINE: Yes. I’ve got it down cold.
  EXPRESSION: Confident
- CHARACTER: Narrator
  LINE: Rosemary sniffs.
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: Damn that tannis root. It’s even in here.
  EXPRESSION: Annoyed
- CHARACTER: Narrator
  LINE: Rosemary goes to the Kitchen (tossing her coat on the way into the Bedroom).
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: Elise says that Joan and Dick Jellico are separating.
  EXPRESSION: Gossipy
- CHARACTER: Guy
  LINE: No kidding.
  EXPRESSION: Surprised
- CHARACTER: Narrator
  LINE: Rosemary comes back with some aluminum foil, and a deodorant bomb.
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: Lucky they didn’t have children,
  EXPRESSION: Matter-of-fact
- CHARACTER: Narrator
  LINE: She takes the charm out of the Louis Sherry box, winds it in a tight triple wrapping and twists the ends to seal it. Guy, comes Into the Bedroom, drying his hair with a towel.
  EXPRESSION: null
- CHARACTER: Guy
  LINE: It’ll probably lose its strength in a few days.
  EXPRESSION: Speculative
- CHARACTER: Rosemary
  LINE: It better. If not, I’ll throw it away,
  EXPRESSION: Threatening
- CHARACTER: Narrator
  LINE: As Rosemary puts the wrapped charm back in the box, standing behind her, Guy unzips her dress and pulls it off her shoulders; he starts kissing her neck. We HEAR a party in progress behind the wall; flat unmusical CHANTING, with a flute or clarinet underneath it.
  EXPRESSION: null

::SCENE::
LOCATION: Guy and Rosemary's Apartment - Hallway
MOOD: Industrious
CHARACTERS: Narrator, Guy
BACKGROUND_IMAGE: guy_rosemary_apartment_hallway_day_sept28.png
BACKGROUND_EDIT: "Daytime, September 28, 1965, Guy painting a closet red"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Guy is painting the inside of the guest closet red.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: There are several brushes, cans of paint and paint remover.
  EXPRESSION: null

::SCENE::
LOCATION: Guy and Rosemary's Apartment - Living Room
MOOD: Anxious
CHARACTERS: Narrator, Rosemary, Guy
BACKGROUND_IMAGE: guy_rosemary_apartment_living_room_day.png
BACKGROUND_EDIT: "Daytime, Rosemary arranging chairs, telephone rings"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Rosemary trying different arrangements with chairs.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The telephone RINGS in the Bedroom. Rosemary makes an involuntary move to answer it. Through the arch-way she sees Guy, can of paint remover in his hand, running to get to the phone.
  EXPRESSION: null
- CHARACTER: Guy
  LINE: Yes? This is he. Oh, God, no. Oh, the poor guy.
  EXPRESSION: Shocked
- CHARACTER: Narrator
  LINE: Rosemary goes to the Bedroom door; Guy is sitting on the bed, the phone in one hand and a can of Red Devil paint remover in the other. He doesn’t look at Rosemary.
  EXPRESSION: Distraught
- CHARACTER: Guy
  LINE: And they don’t have any idea what’s causing it? My God, that’s awful, just awful.
  EXPRESSION: Horrified
- CHARACTER: Guy
  LINE: Yes I am. Yes I would. I'd hate to get it this way, but I - Well, you’d have to speak to my agent about that end of it. Alan Stone, but I’m sure there won’t be any problem, Mr. Weiss, not as far as we’re concerned.
  EXPRESSION: Negotiating
- CHARACTER: Narrator
  LINE: Rosemary, standing in the doorway, holds her breath, waiting.
  EXPRESSION: Tense
- CHARACTER: Guy
  LINE: Thank you, Mr. Weiss.
  EXPRESSION: Resigned
- CHARACTER: Narrator
  LINE: Guy hangs up and shuts his eyes. He sits motionless, his hand staying on the phone. He is pale and dummy-like, a Pop Art wax statue with real clothes and props, real phone, real can of paint remover.
  EXPRESSION: Petrified
- CHARACTER: Rosemary
  LINE: Guy?
  EXPRESSION: Concerned
- CHARACTER: Narrator
  LINE: He opens his eyes and looks at her.
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: What is it?
  EXPRESSION: Anxious
- CHARACTER: Narrator
  LINE: Guy blinks and comes alive.
  EXPRESSION: null
- CHARACTER: Guy
  LINE: Donald Baumgart. He’s gone blind. He woke up yesterday and - he can’t see.
  EXPRESSION: Grim
- CHARACTER: Narrator
  LINE: They look painfully at each other.
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: Oh no.
  EXPRESSION: Horrified
- CHARACTER: Guy
  LINE: I’ve got the part. It’s hell of a way to get it.
  EXPRESSION: Bitter
- CHARACTER: Narrator
  LINE: Guy looks at the paint remover in his hand and puts it on the night table.
  EXPRESSION: null
- CHARACTER: Guy
  LINE: Listen, I’ve got to get out and walk around.
  EXPRESSION: Agitated
- CHARACTER: Rosemary
  LINE: I understand. Go ahead.
  EXPRESSION: Understanding
- CHARACTER: Narrator
  LINE: Rosemary stands back from the doorway. Guy goes out, down the hall, out the door, closing it behind him. Rosemary goes into the Living Room and sits down. She leans with arms folded on her knees, thinking. She remains motionless for a moment, then pronounces slowly, tasting the name.
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: Baumgart. Donald Baum ...
  EXPRESSION: Pensive
- CHARACTER: Narrator
  LINE: She looks at the window, stands up and goes quickly to it. She opens the window and looks down at the quiet street.
  EXPRESSION: null

::SCENE::
LOCATION: Guy and Rosemary's Apartment - Living Room
MOOD: Somber
CHARACTERS: Narrator, Guy, Rosemary
BACKGROUND_IMAGE: guy_rosemary_apartment_living_room_day_sept30.png
BACKGROUND_EDIT: "Daytime, September 30, 1965, Guy watches Rosemary vacuum"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Guy Is sitting in an easy chair, cigarette between his fingers. He is motionless but his eyes follow Rosemary as she vacuum cleans the room. She works thoroughly, gradually moving toward the door. After she has disappeared into the hall, the SOUND of the vacuum cleaner fades.
  EXPRESSION: null

::SCENE::
LOCATION: Unknown
MOOD: Melancholy
CHARACTERS: Narrator, Guy, Rosemary
BACKGROUND_IMAGE: null
BACKGROUND_EDIT: "Guy is smoking, Rosemary approaches."

::SCRIPT::
- CHARACTER: Narrator
  LINE: cleaner stops. Guy, still in the same position, slowly lifts the cigarette to his mouth. Rosemary comes back without the cleaner. She walks slowly towards Guy and stands silently in front of him. They look at each other.
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: What’s wrong?
  EXPRESSION: Concerned
- CHARACTER: Guy
  LINE: Nothing. Don’t you have your sculpture class today?
  EXPRESSION: Distant
- CHARACTER: Rosemary
  LINE: I haven’t gone in two months.
  EXPRESSION: Resigned
- CHARACTER: Guy
  LINE: Why don’t you go?
  EXPRESSION: Distant

::PATHS::
- CHOICE: "Continue conversation"
  TARGET: kitchen_day
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Kitchen
MOOD: Hopeful
CHARACTERS: Narrator, Rosemary, Guy
BACKGROUND_IMAGE: kitchen_interior.png
BACKGROUND_EDIT: "Daytime, October 2, 1965. Roses on the table."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Rosemary comes in, her coat still on and carrying a shopping bag. There are roses in a vase on the table.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Rosemary puts down the shopping bag and goes in surprise to examine them. She inhales their scent.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Taking off her coat, she goes into the Living Room.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: There are roses there also. Guy comes in from the Bedroom, one rose in his hand, and kisses her.
  EXPRESSION: null
- CHARACTER: Guy
  LINE: I’ve been a creep. It’s from worrying Baumgart would regain his sight, rat that I am.
  EXPRESSION: Remorseful
- CHARACTER: Rosemary
  LINE: That's natural. You're bound to feel two ways about -
  EXPRESSION: Understanding

::PATHS::
- CHOICE: "Continue the conversation"
  TARGET: kitchen_follow_guy
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Kitchen
MOOD: Hopeful
CHARACTERS: Narrator, Guy, Rosemary
BACKGROUND_IMAGE: kitchen_interior.png
BACKGROUND_EDIT: "Guy offering a rose, leading Rosemary into the kitchen."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Guy lifts the rose to her nose. Then he turns and walks toward the Kitchen. Rosemary follows him.
  EXPRESSION: null
- CHARACTER: Guy
  LINE: Listen, even if I’m Mister Yamaha for the rest of my days, I'm going to stop giving you the short end of the stick.
  EXPRESSION: Determined
- CHARACTER: Rosemary
  LINE: You haven’t -
  EXPRESSION: Denying
- CHARACTER: Guy
  LINE: Yes, I have. I’ve been too busy tearing my hair out over my career. Let's have a baby, okay? Let’s have three, one at a time.
  EXPRESSION: Eager
- CHARACTER: Narrator
  LINE: Rosemary looks at him.
  EXPRESSION: Contemplative
- CHARACTER: Guy
  LINE: A baby. You know, Goo, goo? Diapers? Waa, waa?
  EXPRESSION: Playful
- CHARACTER: Rosemary
  LINE: Do you mean it?
  EXPRESSION: Hopeful
- CHARACTER: Guy
  LINE: Sure I mean it; I even figured out the right time to start. Look!
  EXPRESSION: Excited
- CHARACTER: Narrator
  LINE: Guy turns towards the calendar hanging on the wall. There are two days encircled with a red pencil. He taps them with his finger.
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: You really mean it, Guy?
  EXPRESSION: Emotional
- CHARACTER: Guy
  LINE: No, I'm kidding. Sure I mean it. Look, Rosemary, for God’s sake don’t cry, all right? Please.
  EXPRESSION: Reassuring

::PATHS::
- CHOICE: "Accept the proposal"
  TARGET: kitchen_day_oct4
  STATE_CHANGE: commitment = +1
  CONDITION: null

::SCENE::
LOCATION: Kitchen
MOOD: Domestic
CHARACTERS: Narrator, Rosemary
BACKGROUND_IMAGE: kitchen_interior.png
BACKGROUND_EDIT: "Daytime, October 4, 1965. Rosemary washing salad, TV on."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Rosemary is washing salad. There are other things on the table ready to be cooked. The TV set has been moved so that she can see it while working. She is watching the Pope's visit in New York, and listening to the newscaster.
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue with evening plans"
  TARGET: bedroom_night
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Bedroom
MOOD: Anticipatory
CHARACTERS: Narrator, Rosemary, Guy
BACKGROUND_IMAGE: bedroom_interior.png
BACKGROUND_EDIT: "Night. Rosemary getting ready at her vanity."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Rosemary is sitting at her vanity, dressed in burgundy silk lounging pajamas. She makes up her eyes, powders her face and perfumes herself. She hears the front door open off-screen and goes out into the hallway.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Guy has just come into the apartment. Rosemary meets him and they kiss.
  EXPRESSION: null
- CHARACTER: Guy
  LINE: Mmm, you look good enough to eat. Damn!
  EXPRESSION: Admiring
- CHARACTER: Rosemary
  LINE: What?
  EXPRESSION: Curious
- CHARACTER: Guy
  LINE: I forgot the pie.
  EXPRESSION: Annoyed
- CHARACTER: Rosemary
  LINE: It's all right.
  EXPRESSION: Understanding
- CHARACTER: Guy
  LINE: I passed two of those damn retail stores; not one but two.
  EXPRESSION: Frustrated
- CHARACTER: Rosemary
  LINE: We can have fruit and cheese. That's the best dessert anyway, really.
  EXPRESSION: Practical
- CHARACTER: Guy
  LINE: It is not; Horn and Hardart pumpkin pie is.
  EXPRESSION: Stubborn
- CHARACTER: Narrator
  LINE: Guy starts to undress; going into the Bathroom.
  EXPRESSION: null

::PATHS::
- CHOICE: "Proceed to dinner"
  TARGET: living_room_night_dinner
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Living Room
MOOD: Cozy, then interrupted
CHARACTERS: Narrator, Guy, Rosemary, Mrs. Castevet (off-screen)
BACKGROUND_IMAGE: living_room_interior.png
BACKGROUND_EDIT: "Night. Table set for dinner, fireplace ready."

::SCRIPT::
- CHARACTER: Narrator
  LINE: The table is set for dinner. Rosemary and Guy are drinking cocktails and eating stuffed mushrooms. Guy puts crumpled newspaper and sticks of kindling on the fireplace grate, and two big chunks of cannel coal.
  EXPRESSION: null
- CHARACTER: Guy
  LINE: Here goes nothing.
  EXPRESSION: Determined
- CHARACTER: Narrator
  LINE: He strikes a match and lights the paper. It flames high and catches the kindling. Dark smoke begins spilling out over the front of the mantel and up toward the ceiling. Guy gropes inside the fireplace.
  EXPRESSION: null
- CHARACTER: Guy
  LINE: Good grief!
  EXPRESSION: Surprised
- CHARACTER: Rosemary
  LINE: The paint, the paint!
  EXPRESSION: Alarmed
- CHARACTER: Narrator
  LINE: Guy gets the flue opened; and the air conditioner draws out the smoke.
  EXPRESSION: null
- CHARACTER: Guy
  LINE: Nobody, but nobody has a fire tonight.
  EXPRESSION: Smug
- CHARACTER: Narrator
  LINE: Rosemary kneels, with her drink, and stares into the spitting flame-wrapped coals.
  EXPRESSION: Mesmerized
- CHARACTER: Rosemary
  LINE: Isn’t it gorgeous? I hope we have the coldest winter ever.
  EXPRESSION: Enchanted
- CHARACTER: Narrator
  LINE: Guy puts on a record.
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue dinner"
  TARGET: living_room_night_doorbell
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Living Room
MOOD: Interrupted, then relieved
CHARACTERS: Narrator, Guy, Rosemary, Mrs. Castevet (off-screen)
BACKGROUND_IMAGE: living_room_interior.png
BACKGROUND_EDIT: "Night. Rosemary and Guy at the dining table."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Rosemary and Guy are at the dining table eating swordfish. The doorbell rings.
  EXPRESSION: null
- CHARACTER: Guy
  LINE: Oh! No!
  EXPRESSION: Exasperated
- CHARACTER: Narrator
  LINE: He gets up, tosses down his napkin, goes out. Rosemary cocks her head and listens. We hear the door open off screen and Mrs. Castevet’s voice saying 'hi Guy'. The rest is unintelligible.
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: Oh, no! Don’t let her in.... not tonight.
  EXPRESSION: Desperate
- CHARACTER: Narrator
  LINE: Off screen dialogue continues. Now Guy speaks; then Mrs. Castevet again. Only a few words are intelligible "... extra. We don’t need them". Guy again and Mrs. Castevet again. Rosemary holds in her breath. We hear the door being closed and chained.
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: Good!
  EXPRESSION: Relieved
- CHARACTER: Narrator
  LINE: We hear the bolt drawn.
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: Good!
  EXPRESSION: Relieved
- CHARACTER: Narrator
  LINE: Guy appears in the archway, smiling smugly, with both hands behind his back.
  EXPRESSION: null
- CHARACTER: Guy
  LINE: Who says there’s nothing to ESP?
  EXPRESSION: Confident
- CHARACTER: Narrator
  LINE: He comes towards the table and brings forth his hands with two white custard cups sitting one on each palm.
  EXPRESSION: null
- CHARACTER: Guy
  LINE: Madame and Monsieur shall have ze dessairt after all.
  EXPRESSION: Showy
- CHARACTER: Narrator
  LINE: He puts one cup by Rosemary's wine glass and the other by his own. The cups are filled with peaked swirls of chocolate. One topped with a sprinkling of chopped nuts. The other with a half walnut.
  EXPRESSION: null
- CHARACTER: Guy
  LINE: Mousse au chocolat or ’chocolate mouse’, as Minnie calls it.
  EXPRESSION: Proud
- CHARACTER: Rosemary
  LINE:
  EXPRESSION: Happy
- CHARACTER: Narrator
  LINE: Guy replaces his napkin and pours more wine.
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: I was afraid she’d stay all evening.
  EXPRESSION: Relieved
- CHARACTER: Guy
  LINE: No, she just wanted us to try it, seein’ as how it’s one of her speci-al-ities.
  EXPRESSION: Explaining
- CHARACTER: Rosemary
  LINE: It’s sweet of her, really. Shouldn't make fun of her.
  EXPRESSION: Kind
- CHARACTER: Guy
  LINE: You’re right. You’re right.
  EXPRESSION: Agreeing
- CHARACTER: Narrator
  LINE: Guy and Rosemary start eating the chocolate mousse.
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: It’s good.
  EXPRESSION: Satisfied
- CHARACTER: Narrator
  LINE: At the second spoonful, she pauses and looks at Guy but he is busy eating.
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: It has an undertaste.
  EXPRESSION: Puzzled
- CHARACTER: Narrator
  LINE: Guy looks up at Rosemary.
  EXPRESSION: null
- CHARACTER: Guy
  LINE: Mmm?
  EXPRESSION: Inquiring
- CHARACTER: Rosemary
  LINE: A chalky undertaste.
  EXPRESSION: Certain
- CHARACTER: Narrator
  LINE: Guy rolls the mousse on his palate, cocking his head.
  EXPRESSION: null
- CHARACTER: Guy
  LINE: I don't get it.
  EXPRESSION: Dismissive
- CHARACTER: Narrator
  LINE: After a few swallows, Rosemary puts down her spoon.
  EXPRESSION: null
- CHARACTER: Guy
  LINE: That's silly, honey, there's no 'undertaste'.
  EXPRESSION: Dismissive
- CHARACTER: Rosemary
  LINE: There is.
  EXPRESSION: Insistent
- CHARACTER: Guy
  LINE: Come on, the old bat slaved all day; eat it.
  EXPRESSION: Impatient
- CHARACTER: Rosemary
  LINE: But I don't like it.
  EXPRESSION: Rebellious
- CHARACTER: Guy
  LINE: It's delicious.
  EXPRESSION: Insistent
- CHARACTER: Rosemary
  LINE: You can have mine.
  EXPRESSION: Offering
- CHARACTER: Guy
  LINE: All right, don't eat it. There's always something wrong.
  EXPRESSION: Annoyed
- CHARACTER: Rosemary
  LINE: Oh - if it's going to turn into a big scene -
  EXPRESSION: Resigned
- CHARACTER: Narrator
  LINE: She takes a full spoonful of mousse and thrusts it into her mouth.
  EXPRESSION: null
- CHARACTER: Guy
  LINE: Look, if you really can’t stand it, don't eat it.
  EXPRESSION: Resigned
- CHARACTER: Rosemary
  LINE: Delicious. No undertaste at all. Turn the records over.
  EXPRESSION: Forced
- CHARACTER: Narrator
  LINE: Guy gets up and goes to the record player. Rosemary doubles her napkin in her lap and plops a few spoonfuls of the mousse into it. She folds the napkin closed and then showily scrapes clean the inside of the cup and swallows down the scrappings as Guy comes back to the table.
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: There, Daddy. Do I get a gold star?
  EXPRESSION: Sarcastic
- CHARACTER: Guy
  LINE: Two of them. I’m sorry if I was stuffy.
  EXPRESSION: Apologetic
- CHARACTER: Rosemary
  LINE: You were.
  EXPRESSION: Stating
- CHARACTER: Guy
  LINE: I’m sorry.
  EXPRESSION: Apologetic
- CHARACTER: Narrator
  LINE: He smiles and kisses her.
  EXPRESSION: null

::PATHS::
- CHOICE: "Clean up dinner"
  TARGET: kitchen_night_cleaning
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Kitchen
MOOD: Uneasy
CHARACTERS: Narrator, Rosemary
BACKGROUND_IMAGE: kitchen_interior.png
BACKGROUND_EDIT: "Night. Rosemary cleaning up after dinner, TV sounds from den."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Rosemary scrapes the uneaten mousse from her napkin into the waste bin. The water is running into the sink. We hear the sound of television from the other room. A sudden wave of dizziness makes her sway for a moment, then blink and frown.
  EXPRESSION: null
- CHARACTER: Guy (O.S.)
  LINE: The Pope at Yankee Stadium. Christ, what a mob I
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: Good.
  EXPRESSION: Distracted
- CHARACTER: Narrator
  LINE: She shakes her head to clear the dizziness, then rolls the napkins up inside the tablecloth and puts the bundle aside. She turns the water off and loads the dirty dishes into the full sink. She dries her hands on the kitchen towel and as she hangs it up, another wave of dizziness makes her swivel and hang on to the edge of the sink. This time it lasts longer.
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: Oh boy!
  EXPRESSION: Worried
- CHARACTER: Narrator
  LINE: She straightens up and makes it to the doorway of the Den. She keeps her footing with difficulty by holding on to the knob with one hand and the jamb with the other.
  EXPRESSION: null
- CHARACTER: Guy
  LINE: What is it?
  EXPRESSION: Anxious
- CHARACTER: Rosemary
  LINE: Dizzy.
  EXPRESSION: Weak
- CHARACTER: Narrator
  LINE: Guy snaps off the TV, comes to her, takes her arm and holds her surely around the waist.
  EXPRESSION: null
- CHARACTER: Guy
  LINE: No wonder, all that booze. You probably had an empty stomach, too.
  EXPRESSION: Dismissive
- CHARACTER: Narrator
  LINE: He helps her towards the bedroom but her legs buckle.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: He catches her up and carries her. He puts her down on the bed and sits beside her, taking her hand and stroking her forehead sympathetically. Rosemary closes her eyes.
  EXPRESSION: null

::PATHS::
- CHOICE: "Fall asleep"
  TARGET: dream_sequence_raft
  STATE_CHANGE: health = -1
  CONDITION: null

::SCENE::
LOCATION: Dream Sequence - Raft
MOOD: Peaceful
CHARACTERS: Narrator, Rosemary, Guy (O.S.)
BACKGROUND_IMAGE: dream_raft.png
BACKGROUND_EDIT: "Daytime. Bed is a raft on gentle water."

::SCRIPT::
- CHARACTER: Narrator
  LINE: The bed is a raft floating on gentle ripples.
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: Nice.
  EXPRESSION: Content
- CHARACTER: Guy (O.S.)
  LINE: Sleep is what you need.
  EXPRESSION: Reassuring

::PATHS::
- CHOICE: "Continue sleeping"
  TARGET: bedroom_night_sleeping
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Bedroom
MOOD: Caring
CHARACTERS: Narrator, Guy, Rosemary
BACKGROUND_IMAGE: bedroom_interior.png
BACKGROUND_EDIT: "Night. Guy beside Rosemary, stroking her forehead."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Guy is sitting beside Rosemary stroking her forehead.
  EXPRESSION: null
- CHARACTER: Guy
  LINE: A good night’s sleep.
  EXPRESSION: Gentle
- CHARACTER: Rosemary
  LINE: We have to make a baby.
  EXPRESSION: Urgent
- CHARACTER: Guy
  LINE: We will. Tomorrow. There's plenty of time.
  EXPRESSION: Calming
- CHARACTER: Rosemary
  LINE: Just a nap.
  EXPRESSION: Drowsy

::PATHS::
- CHOICE: "Fall deeper asleep"
  TARGET: dream_sequence_yacht
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Dream Sequence - Yacht
MOOD: Serene, then unsettling
CHARACTERS: Narrator, Rosemary, Hutch, Elevator Operator
BACKGROUND_IMAGE: dream_yacht.png
BACKGROUND_EDIT: "Daytime. Rosemary on a yacht, sunny and breezy. Skipper (Hutch) plots course."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Large Yacht. Rosemary is sitting with a drink in her hand. It is sunny and breezy. The Skipper is unrolling a large map to plot the course. He is Hutch now and is giving terse and knowing instructions to a Negro Mate (Elevator Operator).
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Guy’s hands take off the top of Rosemary's pajamas.
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue the dream"
  TARGET: bedroom_night_pajamas_top
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Bedroom
MOOD: Intimate, then unsettling
CHARACTERS: Narrator, Guy, Rosemary
BACKGROUND_IMAGE: bedroom_interior.png
BACKGROUND_EDIT: "Night. Guy undressing Rosemary."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Guy is taking off the top of Rosemary’s pajamas.
  EXPRESSION: null
- CHARACTER: Guy
  LINE: To make you more comfortable.
  EXPRESSION: Gentle
- CHARACTER: Rosemary
  LINE: I am comfortable.
  EXPRESSION: Mildly protesting
- CHARACTER: Guy
  LINE: Sleep. Ro.
  EXPRESSION: Soothing
- CHARACTER: Narrator
  LINE: Guy undoes the snaps at the side and slowly draws off the bottom of Rosemary’s pajamas.
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue the dream"
  TARGET: dream_sequence_yacht_pants
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Dream Sequence / Interior (?)
MOOD: Unsettling, exposed
CHARACTERS: Narrator, Guy, Rosemary
BACKGROUND_IMAGE: dream_yacht_interior.png
BACKGROUND_EDIT: "On the yacht. Guy pulling off Rosemary's pajamas. Other ladies in bikinis."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Back on the yacht. Guy is holding the legs of Rosemary’s pajamas and pulling them away from her.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Rosemary tries to hide her nudity? she looks around and sees other ladies on the yacht. They are wearing bikinis - so is Ro
  EXPRESSION: null





::SCENE::
LOCATION: Hutch's Apartment - Interior (implied)
MOOD: Sadness
CHARACTERS: Narrator, Rosemary, Hutch
BACKGROUND_IMAGE: null
BACKGROUND_EDIT: null

::SCRIPT::
- CHARACTER: Narrator
  LINE: bit self-centered. I bet Laurence Olivier is vain and self-centered —
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Rosemary's voice cracks; determined not to cry, she continues:
  EXPRESSION: null
- CHARACTER: ROSEMARY
  LINE: It's a difficult part. He’s got to work with crutches and naturally he’s preoccupied and — and, well, preoccupied.
  EXPRESSION: Sad
- CHARACTER: Narrator
  LINE: Rosemary breaks down. Hutch comes over and comforts her.
  EXPRESSION: null

::PATHS::
- CHOICE: null
  TARGET: null
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Hutch's Apartment - Interior (implied)
MOOD: Comforting
CHARACTERS: Narrator, Hutch
BACKGROUND_IMAGE: null
BACKGROUND_EDIT: null

::SCRIPT::
- CHARACTER: Narrator
  LINE: 75.
  EXPRESSION: null
- CHARACTER: HUTCH
  LINE: I've a lot of good advice for you, but I’m going to shut up.
  EXPRESSION: Caring

::PATHS::
- CHOICE: null
  TARGET: null
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Street Outside Hutch's Apartment
MOOD: Conversational
CHARACTERS: Narrator, Rosemary, Hutch
BACKGROUND_IMAGE: street_hutch_apt.png
BACKGROUND_EDIT: "Daytime street scene outside an apartment building"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Rosemary and Hutch walking along the street.
  EXPRESSION: null
- CHARACTER: HUTCH
  LINE: I meant to ask you. You had another suicide up there at Happy House?
  EXPRESSION: Curious
- CHARACTER: ROSEMARY
  LINE: Oh, didn't I tell you?
  EXPRESSION: Distracted
- CHARACTER: HUTCH
  LINE: No, you didn't.
  EXPRESSION: Neutral
- CHARACTER: ROSEMARY
  LINE: It was that girl I told you about; the drug addict who was rehabilitated by this old couple. I’m sure I told you that.
  EXPRESSION: Forgetful
- CHARACTER: HUTCH
  LINE: They didn’t rehabilitate her very successfully, it would seem.
  EXPRESSION: Sarcastic
- CHARACTER: ROSEMARY
  LINE: We’ve gotten to know them well, since. Mr. Castevet’s father was a theatrical producer in the old days.
  EXPRESSION: Informative
- CHARACTER: HUTCH
  LINE: Castevet. That’s an odd name. French, I suppose?
  EXPRESSION: Curious

::PATHS::
- CHOICE: null
  TARGET: null
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Kitchen - Guy and Rosemary's Apartment
MOOD: Domestic
CHARACTERS: Narrator, Guy, Rosemary
BACKGROUND_IMAGE: kitchen_day.png
BACKGROUND_EDIT: "October 22, 1965. Morning. Kitchen with a calendar on the wall."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Guy is sitting at the table reading the theatre section of the Sunday Times. Rosemary is preparing breakfast. As she puts the Chemex on the table, her eyes fall on the calendar; she stares at it.
  EXPRESSION: null
- CHARACTER: GUY
  LINE: It was due on Friday.
  EXPRESSION: Neutral
- CHARACTER: ROSEMARY
  LINE: It was?
  EXPRESSION: Surprised
- CHARACTER: Narrator
  LINE: Guy nods.
  EXPRESSION: null
- CHARACTER: ROSEMARY
  LINE: It’ll probably come tonight. Or tomorrow.
  EXPRESSION: Hopeful
- CHARACTER: GUY
  LINE: You want to bet?
  EXPRESSION: Challenging
- CHARACTER: ROSEMARY
  LINE: Okay.
  EXPRESSION: Determined
- CHARACTER: GUY
  LINE: You’re going to lose, Ro,
  EXPRESSION: Confident
- CHARACTER: ROSEMARY
  LINE: Shut up, You’re getting me all jumpy. It’s only two days.
  EXPRESSION: Annoyed

::PATHS::
- CHOICE: null
  TARGET: null
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Dr. Hill’s Office
MOOD: Anxious
CHARACTERS: Narrator, Rosemary, Dr. Hill
BACKGROUND_IMAGE: dr_hill_office.png
BACKGROUND_EDIT: "October 28, 1965. Day. Doctor's office."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Rosemary sitting while Dr. Hill is measuring her blood pressure. He is very young, medium height, and handsome. He speaks slowly and tries to appear older by his serious behavior.
  EXPRESSION: null
- CHARACTER: ROSEMARY
  LINE: When will I know?
  EXPRESSION: Anxious
- CHARACTER: Narrator
  LINE: Dr. Hill takes the instrument off Rosemary’s arm, and puts it back into the box.
  EXPRESSION: null
- CHARACTER: DR. HILL
  LINE: I will call you as soon as I have the results. I like to do a general checkup just to know something more.
  EXPRESSION: Professional
- CHARACTER: ROSEMARY
  LINE: It was Elise Dunstan who recommended you to me, Dr. Hill.
  EXPRESSION: Informative
- CHARACTER: DR. HILL
  LINE: Oh, yes, yes. How is she?
  EXPRESSION: Polite
- CHARACTER: ROSEMARY
  LINE: Fine. And the boys are great. Did you deliver all of them?
  EXPRESSION: Inquisitive
- CHARACTER: DR. HILL
  LINE: No. Only the last.
  EXPRESSION: Neutral
- CHARACTER: Narrator
  LINE: The Nurse comes with a syringe and two little bottles.
  EXPRESSION: null
- CHARACTER: DR. HILL
  LINE: Universal and haemoglobin.
  EXPRESSION: Clinical
- CHARACTER: NURSE
  LINE: Yes.
  EXPRESSION: Responsive
- CHARACTER: Narrator
  LINE: She goes to Rosemary, applies a tourniquet and draws blood from her arm.
  EXPRESSION: null
- CHARACTER: ROSEMARY
  LINE: We went to see "The Fantasticks” —
  EXPRESSION: Casual
- CHARACTER: DR. HILL
  LINE: Oh, did you?
  EXPRESSION: Interested

::PATHS::
- CHOICE: null
  TARGET: null
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Guy and Rosemary’s Apartment - Interior
MOOD: Hopeful / Anxious
CHARACTERS: Narrator, Rosemary, Dr. Hill (O.S.)
BACKGROUND_IMAGE: apartment_day.png
BACKGROUND_EDIT: "October 30, 1965. Day. Apartment bedroom with telephone."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Telephone rings. Rosemary picks it up.
  EXPRESSION: null
- CHARACTER: DR. HILL (O.S.)
  LINE: Mrs. Woodhouse?
  EXPRESSION: Professional
- CHARACTER: ROSEMARY
  LINE: Dr. Hill?
  EXPRESSION: Hopeful
- CHARACTER: DR. HILL (O.S.)
  LINE: Congratulations.
  EXPRESSION: Joyful
- CHARACTER: ROSEMARY
  LINE: Really?
  EXPRESSION: Elated
- CHARACTER: DR. HILL (O.S.)
  LINE: Really.
  EXPRESSION: Affirmative
- CHARACTER: Narrator
  LINE: Smiling, Rosemary sits down on the side of the bed.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Pause.
  EXPRESSION: null
- CHARACTER: DR. HILL (O.S.)
  LINE: Are you there?
  EXPRESSION: Inquiring
- CHARACTER: ROSEMARY
  LINE: What happens now?
  EXPRESSION: Eager
- CHARACTER: DR. HILL (O.S.)
  LINE: Very little. You come and see me next month. And you get those Ntaln pills. One a day. I’ll mail you forms - for the hospital.
  EXPRESSION: Informative
- CHARACTER: ROSEMARY
  LINE: When will it be?
  EXPRESSION: Inquisitive
- CHARACTER: DR. HILL (O.S.)
  LINE: Works out to June twenty-eighth.
  EXPRESSION: Specific
- CHARACTER: ROSEMARY
  LINE: That sounds so far away,
  EXPRESSION: Pensive
- CHARACTER: DR. HILL (O.S.)
  LINE: It is. Oh, one more thing, Mrs. Woodhouse. We would like another blood sample.
  EXPRESSION: Casual
- CHARACTER: ROSEMARY
  LINE: Yes, of course.
  EXPRESSION: Agreeable
- CHARACTER: Narrator
  LINE: (A beat)
  EXPRESSION: null
- CHARACTER: ROSEMARY
  LINE: What for?
  EXPRESSION: Concerned
- CHARACTER: DR. HILL (O.S.)
  LINE: Nurse didn't take enough. So would you drop by and see her?
  EXPRESSION: Reassuring
- CHARACTER: ROSEMARY
  LINE: But - I’m pregnant, aren't I?
  EXPRESSION: Confused
- CHARACTER: DR. HILL (O.S.)
  LINE: Oh yes. It’s just for blood sugar and so forth. Nothing to be concerned about. You’re pregnant, don’t worry.
  EXPRESSION: Reassuring
- CHARACTER: ROSEMARY
  LINE: All right. I’ll come tomorrow.
  EXPRESSION: Resigned
- CHARACTER: DR. HILL (O.S.)
  LINE: Good. Don’t forget the pills. Goodbye.
  EXPRESSION: Polite
- CHARACTER: ROSEMARY
  LINE: Goodbye, Dr. Hill.
  EXPRESSION: Polite
- CHARACTER: Narrator
  LINE: She puts down the telephone slowly and looks at it for a long moment, hand still on the receiver.
  EXPRESSION: null
- CHARACTER: ROSEMARY
  LINE: Blood sugar?
  EXPRESSION: Suspicious
- CHARACTER: Narrator
  LINE: She stands up briskly and walks out.
  EXPRESSION: null

::PATHS::
- CHOICE: null
  TARGET: null
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Kitchen - Guy and Rosemary's Apartment
MOOD: Pensive
CHARACTERS: Narrator, Rosemary
BACKGROUND_IMAGE: kitchen_day_calendar.png
BACKGROUND_EDIT: "Daytime. Close-up on a wall calendar. Rosemary marks 'Blood'."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Rosemary marks on the wall calendar: "Blood".
  EXPRESSION: null

::PATHS::
- CHOICE: null
  TARGET: null
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Hallway - Guy and Rosemary's Apartment
MOOD: Celebratory / Reconciliatory
CHARACTERS: Narrator, Rosemary, Guy
BACKGROUND_IMAGE: hallway_dusk.png
BACKGROUND_EDIT: "Dusk. Hallway outside Guy and Rosemary's apartment."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Rosemary holds out a quarter in her palm. Guy, who has just come in, looks at Rosemary’s outstretched hand, closing the door behind him.
  EXPRESSION: null
- CHARACTER: GUY
  LINE: What’s this for?
  EXPRESSION: Confused
- CHARACTER: Narrator
  LINE: He catches on, takes Rosemary by the shoulders and kisses her.
  EXPRESSION: null
- CHARACTER: GUY
  LINE: Oh, that's great, honey! Just great.
  EXPRESSION: Elated
- CHARACTER: ROSEMARY
  LINE: Father.
  EXPRESSION: Proud
- CHARACTER: GUY
  LINE: Mother.
  EXPRESSION: Proud
- CHARACTER: Narrator
  LINE: Rosemary looks up at him, suddenly serious.
  EXPRESSION: null
- CHARACTER: ROSEMARY
  LINE: Guy, listen. Let’s make this a new beginning, okay? A new openness and talking-to-each-other. Because we haven't been open.
  EXPRESSION: Earnest
- CHARACTER: Narrator
  LINE: Guy puts his hands on her shoulders, his eyes meeting hers earnestly.
  EXPRESSION: null
- CHARACTER: GUY
  LINE: It’s true. I’m so God-damned self-centered, Ro, That's what the whole trouble is. You know I love you though, don't you? I do, Ro. I swear to God. I’ll be as open as -
  EXPRESSION: Remorseful
- CHARACTER: ROSEMARY
  LINE: It's my fault as much as -
  EXPRESSION: Humble
- CHARACTER: GUY
  LINE: Bull. It's mine. Bear with me, will you, Ro? I'll try to do better.
  EXPRESSION: Sincere
- CHARACTER: ROSEMARY
  LINE: Oh, Guy.
  EXPRESSION: Moved
- CHARACTER: Narrator
  LINE: Deeply moved, she falls into his arms. They kiss fervently.
  EXPRESSION: null
- CHARACTER: GUY
  LINE: Fine way for parents to be carrying on.
  EXPRESSION: Playful
- CHARACTER: Narrator
  LINE: Rosemary laughs, wet-eyed.
  EXPRESSION: null
- CHARACTER: GUY
  LINE: Gee, honey. Do you know what I'd love to do?
  EXPRESSION: Excited
- CHARACTER: ROSEMARY
  LINE: What?
  EXPRESSION: Eager
- CHARACTER: GUY
  LINE: Tell Minnie and Roman. I know, I know, it’s supposed to be a deep dark secret. But I told them we were trying. They were so pleased -
  EXPRESSION: Eager
- CHARACTER: ROSEMARY
  LINE: Tell them.
  EXPRESSION: Loving
- CHARACTER: Narrator
  LINE: Guy kisses her nose.
  EXPRESSION: null
- CHARACTER: GUY
  LINE: Back in two minutes.
  EXPRESSION: Hurried
- CHARACTER: Narrator
  LINE: (He hurries out the door)
  EXPRESSION: null

::PATHS::
- CHOICE: null
  TARGET: null
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Bathroom - Guy and Rosemary's Apartment
MOOD: Reflective / Anxious
CHARACTERS: Narrator, Rosemary
BACKGROUND_IMAGE: bathroom_night.png
BACKGROUND_EDIT: "Night. Bathroom. Rosemary looks at her reflection."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Rosemary fixes her eyes in front of the mirror. She looks at herself.
  EXPRESSION: null
- CHARACTER: ROSEMARY
  LINE: You're pregnant.
  EXPRESSION: Awed
- CHARACTER: Narrator
  LINE: (Pause)
  EXPRESSION: null
- CHARACTER: ROSEMARY
  LINE: Another blood sample?
  EXPRESSION: Suspicious
- CHARACTER: Narrator
  LINE: Through the front door comes Mrs. Castevet in a housedress, Mr. Castevet carrying a bottle of wine, and Guy behind them flushed and smiling.
  EXPRESSION: null

::PATHS::
- CHOICE: null
  TARGET: null
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Guy and Rosemary's Apartment - Living Room / Kitchen
MOOD: Celebratory
CHARACTERS: Narrator, Mrs. Castevet, Mr. Castevet, Guy, Rosemary
BACKGROUND_IMAGE: apartment_living_kitchen.png
BACKGROUND_EDIT: "Night. Apartment interior. Mrs. and Mr. Castevet arrive with wine."

::SCRIPT::
- CHARACTER: MRS. CASTEVET
  LINE: Now that's what I call good news! Congrat-u-la-tions!
  EXPRESSION: Joyful
- CHARACTER: Narrator
  LINE: She bears down on Rosemary, takes her by the shoulders and kisses her cheek hard and loud. Mr. Castevet kisses Rosemary’s other cheek.
  EXPRESSION: null
- CHARACTER: MR. CASTEVET
  LINE: Our best wishes to you, Rosemary. We’re more pleased than we can say. We have no champagne on hand, but this will do just as nicely.
  EXPRESSION: Gracious
- CHARACTER: Narrator
  LINE: He shows the bottle of St. Julien. Guy goes into the kitchen.
  EXPRESSION: null
- CHARACTER: MRS. CASTEVET
  LINE: When are you due, dear?
  EXPRESSION: Inquisitive
- CHARACTER: ROSEMARY
  LINE: June twenty-eighth.
  EXPRESSION: Calm
- CHARACTER: MRS. CASTEVET
  LINE: It’s going to be so exciting.
  EXPRESSION: Enthusiastic
- CHARACTER: Narrator
  LINE: Guy comes back with glasses and a corkscrew. Mr. Castevet turns with him to the opening of the wine.
  EXPRESSION: null
- CHARACTER: Mrs. Castevet
  LINE: Listen, dear. Do you have a good doctor?
  EXPRESSION: Concerned
- CHARACTER: ROSEMARY
  LINE: A very good one.
  EXPRESSION: Confident
- CHARACTER: MRS. CASTEVET
  LINE: One of the top obstetricians is a dear friend of ours. Abe Sapirstein. He delivers all the Society babies.
  EXPRESSION: Recommending
- CHARACTER: Narrator
  LINE: Mr. Castevet and Guy are at the other end of the room, busy with the wine.
  EXPRESSION: null
- CHARACTER: MR. CASTEVET
  LINE: Abe Sapirstein? One of the finest obstetricians in the country.
  EXPRESSION: Endorsing
- CHARACTER: GUY
  LINE: Wasn’t he on 'Open End' a couple of years ago?
  EXPRESSION: Recalling
- CHARACTER: MR. CASTEVET
  LINE: That’s right.
  EXPRESSION: Affirmative
- CHARACTER: GUY
  LINE: Ro?
  EXPRESSION: Inquiring
- CHARACTER: ROSEMARY
  LINE: What about Dr. Hill?
  EXPRESSION: Anxious
- CHARACTER: GUY
  LINE: Don’t worry, I’ll tell him something. You know me,
  EXPRESSION: Confident
- CHARACTER: MRS. CASTEVET
  LINE: I’m not going to let you go to no Dr. Hill that nobody heard of! The best is what you’re going to have, young lady, where’s the phone?
  EXPRESSION: Insistent
- CHARACTER: GUY
  LINE: In the bedroom.
  EXPRESSION: Informative
- CHARACTER: Narrator
  LINE: Mrs. Castevet goes into the Bedroom. Mr. Castevet pours glasses of wine.
  EXPRESSION: null
- CHARACTER: MR. CASTEVET
  LINE: He’s a brilliant man. Very sensitive.
  EXPRESSION: Praising
- CHARACTER: Narrator
  LINE: He gives glasses to Rosemary and Guy,
  EXPRESSION: null
- CHARACTER: ROSEMARY
  LINE: Let’s wait for Minnie.
  EXPRESSION: Patient
- CHARACTER: Narrator
  LINE: They stand motionless, each holding a glass, Mr. Castevet holding two.
  EXPRESSION: null
- CHARACTER: GUY
  LINE: Sit down, honey.
  EXPRESSION: Gentle
- CHARACTER: Narrator
  LINE: Rosemary shakes her head. Through the open doors of the Living Room and Bedroom, we see Mrs. Castevet sitting on the bed, holding the phone.
  EXPRESSION: null
- CHARACTER: MRS. CASTEVET
  LINE: Abe? Minnie. Fine. Listen, a dear friend of ours just found out today that she’s pregnant. Yes, isn't it? I’m in her apartment now. We told her you’d be glad to take care of her and that you wouldn't charge none of your fancy Society prices neither.
  EXPRESSION: Busybody
- CHARACTER: Narrator
  LINE: (Silence)
  EXPRESSION: null
- CHARACTER: MRS. CASTEVET
  LINE: Wait a minute. Rosemary? Tomorrow morning at eleven?
  EXPRESSION: Loud
- CHARACTER: ROSEMARY
  LINE: Fine.
  EXPRESSION: Agreeable
- CHARACTER: MR. CASTEVET
  LINE: You see?
  EXPRESSION: Satisfied
- CHARACTER: MRS. CASTEVET
  LINE: Eleven's fine, Abe. Yes. You too. No, not at all. Let's hope so. Good-bye.
  EXPRESSION: Efficient
- CHARACTER: Narrator
  LINE: Mrs. Castevet comes back into the Living Room.
  EXPRESSION: null
- CHARACTER: MRS. CASTEVET
  LINE: There you are.
  EXPRESSION: Triumphant
- CHARACTER: GUY
  LINE: Thanks a million, Minnie.
  EXPRESSION: Grateful
- CHARACTER: ROSEMARY
  LINE: I don't know how to thank you. Both of you.
  EXPRESSION: Grateful
- CHARACTER: Narrator
  LINE: Mrs. Castevet takes the glass of wine from Mr. Castevet.
  EXPRESSION: null
- CHARACTER: MRS. CASTEVET
  LINE: Just have a fine healthy baby; that’s all. Oh, my, I can't wait to tell Laura-Louise.
  EXPRESSION: Enthusiastic
- CHARACTER: ROSEMARY
  LINE: Oh, please. Don't tell anyone else. Not yet.
  EXPRESSION: Pleading
- CHARACTER: MR. CASTEVET
  LINE: She’s right, there'll be plenty of time.
  EXPRESSION: Agreeable
- CHARACTER: Narrator
  LINE: (Raising his glass)
  EXPRESSION: null
- CHARACTER: MR. CASTEVET
  LINE: To a fine healthy baby.
  EXPRESSION: Hopeful
- CHARACTER: GUY
  LINE: Hear, hear.
  EXPRESSION: Agreeable
- CHARACTER: Narrator
  LINE: They all drink.
  EXPRESSION: null

::PATHS::
- CHOICE: null
  TARGET: null
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Bedroom - Guy and Rosemary's Apartment
MOOD: Introspective / Uneasy
CHARACTERS: Narrator, Rosemary, Guy, Castevets (implied)
BACKGROUND_IMAGE: bedroom_night.png
BACKGROUND_EDIT: "Night. Bedroom. Rosemary is awake in bed while Guy sleeps."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Guy and Rosemary are in bed. Guy is asleep on his side, but Rosemary's eyes are wide open. She lies on her back with her hands folded across her stomach.
  EXPRESSION: null
- CHARACTER: ROSEMARY
  LINE: Andrew - Andy?
  EXPRESSION: Whispering
- CHARACTER: Narrator
  LINE: (Silence)
  EXPRESSION: null
- CHARACTER: ROSEMARY
  LINE: Or Susan.
  EXPRESSION: Whispering
- CHARACTER: ROSEMARY
  LINE: Susan!
  EXPRESSION: Calling
- CHARACTER: Narrator
  LINE: She looks quickly at Guy but he doesn’t stir. Behind the wall, the Castevets bed creaks. A fire engine screams by. Guy shifts and mumbles. Suddenly Rosemary slips out of bed, tiptoes to the vanity, takes the good luck charm from the Louis Sherry box, frees it from its aluminum-foil wrapping and puts the chain over her head.
  EXPRESSION: null

::PATHS::
- CHOICE: null
  TARGET: null
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Dr. Sapirstein’s Office
MOOD: Professional / Cautious
CHARACTERS: Narrator, Rosemary, Dr. Sapirstein
BACKGROUND_IMAGE: dr_sapirstein_office.png
BACKGROUND_EDIT: "October 31, 1965. Day. Dr. Sapirstein's office. Rosemary is listening to him."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Rosemary listens carefully to Dr. Sapirstein, sitting on the other side of a de
  EXPRESSION: null

::PATHS::
- CHOICE: null
  TARGET: null
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Not specified
MOOD: Informative
CHARACTERS: Narrator, Dr. Sapirstein, Rosemary
BACKGROUND_IMAGE: null
BACKGROUND_EDIT: "Description of Dr. Sapirstein: tall, sunburned, white hair, reassuringly old-fashioned and direct."

::SCRIPT::
- CHARACTER: Narrator
  LINE: He is a tall sunburned man with white hair, reassuringly old-fashioned and direct.
  EXPRESSION: null
- CHARACTER: DR. SAPIRSTEIN
  LINE: Please don’t read books. No pregnancy was ever exactly like the ones described in the books. And don’t listen to your friends either. No two pregnancies are ever alike.
  EXPRESSION: Concerned
- CHARACTER: ROSEMARY
  LINE: Dr. Hill prescribed vitamin pills.
  EXPRESSION: Inquisitive
- CHARACTER: DR. SAPIRSTEIN
  LINE: No, no pills. Minnie Castevet has a herbarium. I’m going to have her make a daily drink-for you that will be fresher, safer and more vitamin-rich than any pill on the market. Any questions you have, call me night or day. Call me, not your Aunt Fanny. That’s what I’m here for.
  EXPRESSION: Reassuring

::PATHS::
- CHOICE: Continue
  TARGET: apartment_kitchen
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Guy and Rosemary’s Apartment - Kitchen
MOOD: Domestic, Slightly Odd
CHARACTERS: Narrator, Mrs. Castevet, Rosemary
BACKGROUND_IMAGE: apartment_kitchen.png
BACKGROUND_EDIT: "Daytime, November 1, 1965. Rosemary is holding a glass of pistachio milkshake."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Mrs. Castevet holds out to Rosemary a large glass of watery pistachio milkshake.
  EXPRESSION: null
- CHARACTER: MRS. CASTEVET
  LINE: Here!
  EXPRESSION: Encouraging
- CHARACTER: Narrator
  LINE: Rosemary happily takes the glass and looks at it,
  EXPRESSION: null
- CHARACTER: ROSEMARY
  LINE: What's in it?
  EXPRESSION: Curious
- CHARACTER: MRS. CASTEVET
  LINE: Snips and snails and puppy-dogs’ tails.
  EXPRESSION: Playful
- CHARACTER: ROSEMARY
  LINE: That’s fine, but what if we want a girl?
  EXPRESSION: Playful
- CHARACTER: Narrator
  LINE: She lifts the glass and starts drinking.
  EXPRESSION: null
- CHARACTER: MRS. CASTEVET
  LINE: Do you?
  EXPRESSION: Inquisitive
- CHARACTER: ROSEMARY
  LINE: Would be nice if the first one were a boy.
  EXPRESSION: Hopeful
- CHARACTER: MRS. CASTEVET
  LINE: Well, there you are.
  EXPRESSION: Matter-of-fact
- CHARACTER: ROSEMARY
  LINE: No, really, what’s in it?
  EXPRESSION: Insistent
- CHARACTER: MRS. CASTEVET
  LINE: A raw egg, gelatin, herbs...
  EXPRESSION: Informative
- CHARACTER: ROSEMARY
  LINE: Tennis root?
  EXPRESSION: Questioning
- CHARACTER: MRS. CASTEVET
  LINE: Some of that, some of some other things.
  EXPRESSION: Vague

::PATHS::
- CHOICE: Continue
  TARGET: living_room_night
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Living Room
MOOD: Domestic, Slightly Concerned
CHARACTERS: Narrator, Guy, Rosemary
BACKGROUND_IMAGE: living_room_night.png
BACKGROUND_EDIT: "Nighttime, November 21, 1965. Guy is practicing with crutches, repeating lines from a script. Rosemary has a new haircut."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Guy is practicing with crutches, repeating his lines from the script. Rosemary comes in. She has a new haircut. Guy looks at her.
  EXPRESSION: null
- CHARACTER: GUY
  LINE: What’s this?
  EXPRESSION: Surprised
- CHARACTER: ROSEMARY
  LINE: I’ve been to Vidal Sassoon,
  EXPRESSION: Proud
- CHARACTER: GUY
  LINE: You didn’t pay them for that, did you?
  EXPRESSION: Skeptical
- CHARACTER: ROSEMARY
  LINE: I have a - pain.
  EXPRESSION: Pained
- CHARACTER: GUY
  LINE: Where?
  EXPRESSION: Concerned
- CHARACTER: ROSEMARY
  LINE: Here.
  EXPRESSION: Pained
- CHARACTER: GUY
  LINE: Just how?
  EXPRESSION: Concerned
- CHARACTER: ROSEMARY
  LINE: Since Monday. A sharp pain.
  EXPRESSION: Pained
- CHARACTER: GUY
  LINE: Did you see Dr. Sapirstein?
  EXPRESSION: Urgent
- CHARACTER: ROSEMARY
  LINE: I’m seeing him Wednesday.
  EXPRESSION: Calm
- CHARACTER: GUY
  LINE: But this is ridiculous! Why didn’t you say anything? Why didn’t you see Dr. Sapirstein?
  EXPRESSION: Frustrated
- CHARACTER: ROSEMARY
  LINE: I see him Wednesday regular.
  EXPRESSION: Calm

::PATHS::
- CHOICE: Continue
  TARGET: dr_sapirstein_office
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Dr. Sapirstein’s Office
MOOD: Clinical, Reassuring
CHARACTERS: Narrator, Dr. Sapirstein, Rosemary
BACKGROUND_IMAGE: dr_sapirstein_office.png
BACKGROUND_EDIT: "Daytime, November 24, 1965. Dr. Sapirstein and Rosemary are across the desk."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Dr. Sapirstein and Rosemary across the desk.
  EXPRESSION: null
- CHARACTER: DR. SAPIRSTEIN
  LINE: An entirely natural expansion of the pelvis. You can fight it with ordinary aspirin.
  EXPRESSION: Reassuring
- CHARACTER: ROSEMARY
  LINE: I was afraid it might be an ectopic pregnancy.
  EXPRESSION: Anxious
- CHARACTER: DR. SAPIRSTEIN
  LINE: Ectopic? I thought you weren’t going to read books, Rosemary,
  EXPRESSION: Skeptical
- CHARACTER: ROSEMARY
  LINE: It was staring at me in the drug store.
  EXPRESSION: Embarrassed
- CHARACTER: DR. SAPIRSTEIN
  LINE: And all it did was worry you. Will you go home and throw it away, please.
  EXPRESSION: Firm
- CHARACTER: ROSEMARY
  LINE: I will. Promise.
  EXPRESSION: Sincere
- CHARACTER: DR. SAPIRSTEIN
  LINE: The pains will be gone in two days. Ectopic pregnancy.
  EXPRESSION: Dismissive

::PATHS::
- CHOICE: Continue
  TARGET: living_room_dusk
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Living Room
MOOD: Domestic, Strained
CHARACTERS: Narrator, Guy, Rosemary
BACKGROUND_IMAGE: living_room_dusk.png
BACKGROUND_EDIT: "Dusk, December 1, 1965. Guy and Rosemary are playing Scrabble on the floor. Rosemary gets up in pain."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Guy and Rosemary sitting on the floor playing Scrabble. Rosemary gets up and goes to the Bathroom. She sits on the edge of the bathtub, and doubles over in pain. Guy making up a word on the board. Rosemary comes back and stands in the archway.
  EXPRESSION: null
- CHARACTER: ROSEMARY
  LINE: I look awful.
  EXPRESSION: Self-deprecating
- CHARACTER: GUY
  LINE: What are you talking about? You look great. It’s that haircut that looks, awful, if you want the truth, honey. That's the biggest mistake you ever made.
  EXPRESSION: Blunt

::PATHS::
- CHOICE: Continue
  TARGET: den_day
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Den
MOOD: Gloomy, Unwell
CHARACTERS: Narrator, Rosemary
BACKGROUND_IMAGE: den_day.png
BACKGROUND_EDIT: "Daytime, December 5, 1965. The television is on but no sound. Rosemary is sitting in front of it, sick and frozen with pain."

::SCRIPT::
- CHARACTER: Narrator
  LINE: The television is on but no sound. Rosemary is sitting in front of it sick frozen with pain.
  EXPRESSION: null

::PATHS::
- CHOICE: Continue
  TARGET: hallway_day
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Hallway
MOOD: Awkward, Concerned
CHARACTERS: Narrator, Hutch, Rosemary
BACKGROUND_IMAGE: hallway_day.png
BACKGROUND_EDIT: "Daytime, December 9, 1965. Hutch stands on the threshold, staring at Rosemary."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Hutch stands on the threshold, staring at Rosemary.
  EXPRESSION: null
- CHARACTER: HUTCH
  LINE: My God!
  EXPRESSION: Shocked
- CHARACTER: ROSEMARY
  LINE: It’s Vidal Sassoon and it’s very in.
  EXPRESSION: Defensive
- CHARACTER: Narrator
  LINE: She pats her hair. Hutch steps inside and Rosemary closes the door.
  EXPRESSION: null
- CHARACTER: HUTCH
  LINE: What’s wrong with you?
  EXPRESSION: Worried
- CHARACTER: ROSEMARY
  LINE: Do I look that bad?
  EXPRESSION: Anxious
- CHARACTER: Narrator
  LINE: With a fixed, bright smile, she takes his coat and hat and hangs them away.
  EXPRESSION: null
- CHARACTER: HUTCH
  LINE: Terrible. You aren't on one of those 'Zen diets' are you?
  EXPRESSION: Concerned
- CHARACTER: ROSEMARY
  LINE: No.
  EXPRESSION: Resigned
- CHARACTER: HUTCH
  LINE: Then what is it? Have you seen a doctor?
  EXPRESSION: Inquisitive
- CHARACTER: ROSEMARY
  LINE: Oh, I might as well tell you. I'm pregnant.
  EXPRESSION: Resigned
- CHARACTER: HUTCH
  LINE: That's ridiculous. Pregnant women gain weight, they don't lose it.
  EXPRESSION: Skeptical
- CHARACTER: ROSEMARY
  LINE: I don't sleep well. I have stiff joints or something, so I have pains. Nothing serious.
  EXPRESSION: Downplaying
- CHARACTER: Narrator
  LINE: They enter the Living Room. Hutch sits in the easy chair.
  EXPRESSION: null
- CHARACTER: HUTCH
  LINE: Well, congratulations. You must be very happy.
  EXPRESSION: Polite
- CHARACTER: ROSEMARY
  LINE: I am. We both are.
  EXPRESSION: Sincere
- CHARACTER: HUTCH
  LINE: Who's your obstetrician?
  EXPRESSION: Curious
- CHARACTER: ROSEMARY
  LINE: Abraham Sapirstein. He's -
  EXPRESSION: Proud
- CHARACTER: HUTCH
  LINE: He delivered two of my daughter's babies.
  EXPRESSION: Impressed
- CHARACTER: ROSEMARY
  LINE: He's one of the best in the city.
  EXPRESSION: Confident
- CHARACTER: HUTCH
  LINE: When did you see him last?
  EXPRESSION: Inquisitive
- CHARACTER: ROSEMARY
  LINE: Yesterday.
  EXPRESSION: Casual
- CHARACTER: HUTCH
  LINE: And?
  EXPRESSION: Expectant
- CHARACTER: ROSEMARY
  LINE: He says it’s fairly common.
  EXPRESSION: Reassuring
- CHARACTER: HUTCH
  LINE: How much weight have you lost?
  EXPRESSION: Direct
- CHARACTER: ROSEMARY
  LINE: Three pounds.
  EXPRESSION: Casual
- CHARACTER: HUTCH
  LINE: Nonsense! You've lost far more than that!
  EXPRESSION: Disbelieving
- CHARACTER: ROSEMARY
  LINE: It's perfectly normal to lose a little at first. Later on I'll be gaining.
  EXPRESSION: Smiling
- CHARACTER: Narrator
  LINE: Rosemary smiles. Hutch leans back and smiles, too.
  EXPRESSION: null
- CHARACTER: HUTCH
  LINE: Well, we'll assume Dr. Sapirstein knows whereof he speaks. He should; he charges enough.
  EXPRESSION: Cynical
- CHARACTER: ROSEMARY
  LINE: We’re getting bargain rates; our neighbors are close friends of his.
  EXPRESSION: Matter-of-fact
- CHARACTER: Narrator
  LINE: The DOOR BELL RINGS.
  EXPRESSION: null
- CHARACTER: HUTCH
  LINE: I'll go.
  EXPRESSION: Willing
- CHARACTER: ROSEMARY
  LINE: Hurts less when I move around.
  EXPRESSION: Resigned
- CHARACTER: Narrator
  LINE: She goes out of the room to the front door and opens it. Mr. Castevet is standing there, looking slightly winded. Rosemary smiles.
  EXPRESSION: null
- CHARACTER: ROSEMARY
  LINE: I was just talking about you.
  EXPRESSION: Friendly
- CHARACTER: MR. CASTEVET
  LINE: Favorably I hope. Do you need anything from outside?
  EXPRESSION: Inquisitive
- CHARACTER: ROSEMARY
  LINE: No, nothing. Thanks so much for asking.
  EXPRESSION: Grateful
- CHARACTER: Narrator
  LINE: Mr. Castevet glances beyond her for a moment, and then smiles.
  EXPRESSION: null
- CHARACTER: MR. CASTEVET
  LINE: Is Guy home already?
  EXPRESSION: Inquisitive
- CHARACTER: ROSEMARY
  LINE: No, he won’t be home till six.
  EXPRESSION: Informative
- CHARACTER: Narrator
  LINE: Mr. Castevet stays, waiting with a questioning smile.
  EXPRESSION: null
- CHARACTER: ROSEMARY
  LINE: A friend of ours is here.
  EXPRESSION: Informative
- CHARACTER: Narrator
  LINE: The questioning smile stays.
  EXPRESSION: null
- CHARACTER: ROSEMARY
  LINE: Would you like to meet him?
  EXPRESSION: Welcoming
- CHARACTER: MR. CASTEVET
  LINE: If I won’t be intruding.
  EXPRESSION: Polite
- CHARACTER: Narrator
  LINE: She shows Mr. Castevet in. He passes close to her and she notices that his ear is pierced. She follows him to the living room archway. Hutch rises and smiles.
  EXPRESSION: null
- CHARACTER: ROSEMARY
  LINE: This is Edward Hutchins. This is Roman Castevet. I was just telling Hutch that it was you and Minnie who sent me to Dr. Sapirstein.
  EXPRESSION: Introducing
- CHARACTER: Narrator
  LINE: The two men shake hands and greet each other. The men seat themselves and Rosemary sits by Hutch.
  EXPRESSION: null
- CHARACTER: MR. CASTEVET
  LINE: So Rosemary has told you the good news, has she?
  EXPRESSION: Inquisitive
- CHARACTER: HUTCH
  LINE: Yes, she has. Taking better care of Rosemary than her own parents would.
  EXPRESSION: Appreciative
- CHARACTER: MR. CASTEVET
  LINE: We’re very fond of her, and of Guy, too.
  EXPRESSION: Affectionate
- CHARACTER: Narrator
  LINE: He pushes against the arms of his chair and raises himself to his feet.
  EXPRESSION: null
- CHARACTER: MR. CASTEVET
  LINE: If you’ll excuse me, I have to go now. My wife is waiting for me.
  EXPRESSION: Polite
- CHARACTER: HUTCH
  LINE: It’s a pleasure to have met you.
  EXPRESSION: Polite
- CHARACTER: MR. CASTEVET
  LINE: We’ll meet again, I’m sure. Don’t bother, Rosemary.
  EXPRESSION: Confident

::PATHS::
- CHOICE: Continue
  TARGET: kitchen_day
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Kitchen
MOOD: Casual Conversation
CHARACTERS: Narrator, Rosemary, Hutch, Guy
BACKGROUND_IMAGE: kitchen_day.png
BACKGROUND_EDIT: "Daytime, December 5, 1965. Rosemary and Hutch are sitting drinking coffee. Guy enters."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Rosemary and Hutch are sitting drinking coffee.
  EXPRESSION: null
- CHARACTER: ROSEMARY
  LINE: He’s been everywhere in the world. Really everywhere.
  EXPRESSION: Amazed
- CHARACTER: HUTCH
  LINE: Nonsense; nobody has.
  EXPRESSION: Dismissive
- CHARACTER: ROSEMARY
  LINE: I’ve just noticed he has pierced ears.
  EXPRESSION: Curious
- CHARACTER: HUTCH
  LINE: Pierced ears and piercing eyes. What’s she like?
  EXPRESSION: Inquisitive
- CHARACTER: ROSEMARY
  LINE: Nosey. Funny. Guy’s gotten very close to them. I think they’ve become sort of parent-figures for him.
  EXPRESSION: Reflective
- CHARACTER: HUTCH
  LINE: And you?
  EXPRESSION: Inquisitive
- CHARACTER: ROSEMARY
  LINE: I’m not sure. Sometimes they’re too friendly and helpful.
  EXPRESSION: Hesitant
- CHARACTER: Narrator
  LINE: We hear the front door open; Guy hurries in. He still has his make-up on; his face is orange, his eyes black-lashed and large.
  EXPRESSION: null
- CHARACTER: GUY
  LINE: Hey, what a surprise.
  EXPRESSION: Enthusiastic
- CHARACTER: Narrator
  LINE: He comes over and grabs Hutch’s hand before he can rise.
  EXPRESSION: null
- CHARACTER: GUY
  LINE: How are you, Hutch? Good to see you.
  EXPRESSION: Warm
- CHARACTER: Narrator
  LINE: He clasps Rosemary’s head in his other hand and bends and kisses her cheek and lips.
  EXPRESSION: null
- CHARACTER: ROSEMARY
  LINE: You’re the surprise. What happened?
  EXPRESSION: Surprised
- CHARACTER: GUY
  LINE: Ah, they stopped for a rewrite, the dumb bastards. Stay where you are, nobody move.
  EXPRESSION: Annoyed
- CHARACTER: Narrator
  LINE: He goes out to the closet.
  EXPRESSION: null
- CHARACTER: ROSEMARY
  LINE: Would you like some coffee?
  EXPRESSION: Offering
- CHARACTER: GUY (O.S.)
  LINE: Love some!
  EXPRESSION: Eager
- CHARACTER: Narrator
  LINE: Rosemary gets up, pours a cup and refills Hutch's cup and her own. Hutch sucks at his pipe, looking thoughtfully before him. Guy comes back in with his hands full of packs of Pall Mall. He dumps them on the table.
  EXPRESSION: null
- CHARACTER: GUY
  LINE: Loot.
  EXPRESSION: Triumphant
- CHARACTER: Narrator
  LINE: Guy tears a pack open, jams cigarettes up, and pulls one out. He winks at Rosemary as she sits down again.
  EXPRESSION: null
- CHARACTER: HUTCH
  LINE: It seems congratulations are in order.
  EXPRESSION: Congratulatory
- CHARACTER: GUY
  LINE: It’s wonderful, isn’t it?
  EXPRESSION: Happy
- CHARACTER: HUTCH
  LINE: When is the baby due?
  EXPRESSION: Inquisitive
- CHARACTER: ROSEMARY
  LINE: June twenty-eighth. Do you know that Dr. Sapirstein delivered two of Hutch’s grand children?
  EXPRESSION: Informative
- CHARACTER: GUY
  LINE: Really?
  EXPRESSION: Surprised
- CHARACTER: HUTCH
  LINE: I met your neighbor, Roman Castevet.
  EXPRESSION: Casual
- CHARACTER: GUY
  LINE: Oh, did you? Funny old duck, isn’t he?
  EXPRESSION: Amused
- CHARACTER: ROSEMARY
  LINE: Did you ever notice that his ears are pierced?
  EXPRESSION: Questioning
- CHARACTER: GUY
  LINE: You’re kidding?
  EXPRESSION: Surprised
- CHARACTER: ROSEMARY
  LINE: No I’m not; I saw.
  EXPRESSION: Certain
- CHARACTER: Narrator
  LINE: They drink their coffee.
  EXPRESSION: null
- CHARACTER: GUY
  LINE: It’s a shame we haven’t seen more of you lately. With me so busy and Ro being the way she is, we really haven’t seen anyone.
  EXPRESSION: Regretful
- CHARACTER: HUTCH
  LINE: Perhaps we can have dinner together soon.
  EXPRESSION: Suggestive
- CHARACTER: GUY
  LINE: Sure.
  EXPRESSION: Agreeable
- CHARACTER: Narrator
  LINE: Hutch rises. Guy goes to get his coat.
  EXPRESSION: null
- CHARACTER: HUTCH
  LINE: Thank you for the coffee, my dear.
  EXPRESSION: Grateful
- CHARACTER: Narrator
  LINE: In the hallway, they meet Guy who is holding out Hutch’s coat.
  EXPRESSION: null
- CHARACTER: GUY
  LINE: It's not mine, it must be yours.
  EXPRESSION: Confused
- CHARACTER: HUTCH
  LINE: Right you are.
  EXPRESSION: Understanding
- CHARACTER: Narrator
  LINE: He turns around and puts his arms into the sleeves, Guy holding it for him. Hutch feels in his pockets.
  EXPRESSION: null
- CHARACTER: HUTCH
  LINE: Have you thought about names yet? Or is it too soon?
  EXPRESSION: Inquisitive
- CHARACTER: ROSEMARY
  LINE: Andrew or Douglas if it’s a boy. Melinda or Sarah if it’s a girl.
  EXPRESSION: Thoughtful
- CHARACTER: GUY
  LINE: Sarah? What happened to Susan?
  EXPRESSION: Questioning
- CHARACTER: Narrator
  LINE: Guy gives Hutch his hat. Hutch shows them a fur-lined glove and feels in his pockets again.
  EXPRESSION: null
- CHARACTER: HUTCH
  LINE: Is there another one of these around?
  EXPRESSION: Inquisitive
- CHARACTER: Narrator
  LINE: Rosemary looks round the fl
  EXPRESSION: null

::PATHS::
- CHOICE: End Scene
  TARGET: end
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: HALLWAY - (NIGHT)
MOOD: Neutral
CHARACTERS: Narrator, Guy, Hutch, Rosemary
BACKGROUND_IMAGE: hallway_night.png
BACKGROUND_EDIT: "Interior hallway, night time"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Guy goes to the closet to look down on the floor and up on the shelf.
  EXPRESSION: null
- CHARACTER: Guy
  LINE: I don’t see it, Hutch.
  EXPRESSION: Frustrated
- CHARACTER: Hutch
  LINE: Nuisance. I probably left it at City Centre. I’ll stop back there. Let’s really have that dinner, shall we?
  EXPRESSION: Annoyed
- CHARACTER: Guy
  LINE: Definitely.
  EXPRESSION: Agreeable
- CHARACTER: Narrator
  LINE: Next week.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: They watch him go round the first turn of the hallway.
  EXPRESSION: null
- CHARACTER: Guy
  LINE: (To Rosemary) That was a nice surprise.
  EXPRESSION: Happy
- CHARACTER: Rosemary
  LINE: Guess what he said.
  EXPRESSION: Curious
- CHARACTER: Guy
  LINE: What?
  EXPRESSION: Curious
- CHARACTER: Rosemary
  LINE: I look terrible.
  EXPRESSION: Amused
- CHARACTER: Guy
  LINE: Good old Hutch.
  EXPRESSION: Amused
- CHARACTER: Narrator
  LINE: He picks up his coat from the closet and puts it on.
  EXPRESSION: null
- CHARACTER: Guy
  LINE: Spreading cheer wherever he goes.
  EXPRESSION: Sarcastic
- CHARACTER: Narrator
  LINE: Rosemary looks at him questioningly. Guy moves to the front door.
  EXPRESSION: null
- CHARACTER: Guy
  LINE: Going to get a paper.
  EXPRESSION: Casual
- CHARACTER: Narrator
  LINE: He turns back to look at Rosemary, over his shoulder.
  EXPRESSION: null
- CHARACTER: Guy
  LINE: (Opening the door) He is a professional crape-hanger, honey.
  EXPRESSION: Sarcastic
- CHARACTER: Rosemary
  LINE: He isn’t a professional crape-hanger.
  EXPRESSION: Skeptical
- CHARACTER: Guy
  LINE: (Going out) Then he sure is one of the top-ranking amateurs.
  EXPRESSION: Sarcastic

::SCENE::
LOCATION: INT. DEN - (NIGHT)
MOOD: Relaxed
CHARACTERS: Narrator, Guy
BACKGROUND_IMAGE: den_night.png
BACKGROUND_EDIT: "Interior den, night time, television on"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Guy watches television.
  EXPRESSION: null

::SCENE::
LOCATION: INT. BEDROOM - (NIGHT)
MOOD: Calm then Tense
CHARACTERS: Narrator, Rosemary, Guy, Hutch
BACKGROUND_IMAGE: bedroom_night.png
BACKGROUND_EDIT: "Interior bedroom, night time, Rosemary reading in bed"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Rosemary in bed reading. The telephone rings in the other room. We hear Guy answering it and after a moment, he appears in the doorway, phone in hand.
  EXPRESSION: null
- CHARACTER: Guy
  LINE: Hutch wants to speak to you.
  EXPRESSION: Neutral
- CHARACTER: Narrator
  LINE: He puts the phone on the bed and plugs it in.
  EXPRESSION: null
- CHARACTER: Guy
  LINE: I told him you were resting. He said it couldn’t wait.
  EXPRESSION: Neutral
- CHARACTER: Narrator
  LINE: Rosemary picks up the receiver. The television is still playing in the other room and we can hardly hear Hutch’s voice.
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: Hutch?
  EXPRESSION: Curious
- CHARACTER: Hutch (O.S.)
  LINE: Tell me, dear, do you go out at all?
  EXPRESSION: Inquisitive
- CHARACTER: Rosemary
  LINE: Well, I haven’t been going out. Why?
  EXPRESSION: Cautious
- CHARACTER: Narrator
  LINE: She looks at Guy who looks back at her, frowning, listening.
  EXPRESSION: null
- CHARACTER: Hutch (O.S.)
  LINE: Can you meet me tomorrow morning at eleven in front of the Time-Life Building?
  EXPRESSION: Direct
- CHARACTER: Rosemary
  LINE: Yes, if you want me to. What is it? Can’t you tell me now?
  EXPRESSION: Inquisitive
- CHARACTER: Hutch (O.S.)
  LINE: I’d rather not. We can have an early lunch if you’d like.
  EXPRESSION: Private
- CHARACTER: Rosemary
  LINE: That would be nice.
  EXPRESSION: Pleased
- CHARACTER: Hutch (O.S.)
  LINE: Good. Eleven o’clock then.
  EXPRESSION: Decisive
- CHARACTER: Rosemary
  LINE: Right. Did you get your glove?
  EXPRESSION: Curious
- CHARACTER: Hutch (O.S.)
  LINE: No, they didn’t have it. Good night. Rosemary. Sleep well.
  EXPRESSION: Resigned
- CHARACTER: Rosemary
  LINE: You too. Good night.
  EXPRESSION: Polite
- CHARACTER: Narrator
  LINE: She hangs up.
  EXPRESSION: null
- CHARACTER: Guy
  LINE: What was that?
  EXPRESSION: Curious
- CHARACTER: Rosemary
  LINE: He wants to talk to me.
  EXPRESSION: Neutral
- CHARACTER: Guy
  LINE: What about?
  EXPRESSION: Curious
- CHARACTER: Rosemary
  LINE: He didn’t say.
  EXPRESSION: Neutral
- CHARACTER: Narrator
  LINE: Guy shakes his head, smiling.
  EXPRESSION: Amused
- CHARACTER: Guy
  LINE: I think those boys’ adventure stories are going to his head. Where are you meeting him?
  EXPRESSION: Amused
- CHARACTER: Rosemary
  LINE: In front of the Time-Life Building at eleven o’clock.
  EXPRESSION: Informative
- CHARACTER: Narrator
  LINE: Guy unplugs the phone and goes out with it to the den; almost immediately the Television sound stops, and Guy comes back.
  EXPRESSION: null
- CHARACTER: Guy
  LINE: Isn’t it funny? You’re pregnant and I’ve got the yens.
  EXPRESSION: Playful
- CHARACTER: Narrator
  LINE: He plugs the phone back in again and puts it on the night table.
  EXPRESSION: null
- CHARACTER: Guy
  LINE: I’m going to get an ice cream cone. Do you want one?
  EXPRESSION: Caring
- CHARACTER: Rosemary
  LINE: Okay.
  EXPRESSION: Agreeable
- CHARACTER: Guy
  LINE: Vanilla?
  EXPRESSION: Inquiring
- CHARACTER: Rosemary
  LINE: Fine.
  EXPRESSION: Agreeable
- CHARACTER: Narrator
  LINE: Guy goes out. Rosemary leans back against the pillows, looking ahead at nothing with her book forgotten in her lap. Far away we hear a short ring on a doorbell.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Rosemary tries to listen but she has to fold with a sudden pain.
  EXPRESSION: Painful

::SCENE::
LOCATION: INT. HALLWAY - (DAY) - DECEMBER 10, 1965
MOOD: Cold, then Painful
CHARACTERS: Narrator, Rosemary, Mrs. Castevet
BACKGROUND_IMAGE: hallway_day_dec10_1965.png
BACKGROUND_EDIT: "Interior hallway, day time, December 10, 1965"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Rosemary rings the Castevets doorbell. Mrs. Castevet opens the door. She is wearing a housecoat with her hair in curlers.
  EXPRESSION: null
- CHARACTER: Mrs. Castevet
  LINE: Hi.
  EXPRESSION: Casual
- CHARACTER: Rosemary
  LINE: Hi, Minnie. I’m going out this morning, so I won’t have the drink at eleven.
  EXPRESSION: Polite
- CHARACTER: Mrs. Castevet
  LINE: Why, that’s fine, dear. You can take it later. Buzz me when you get back.
  EXPRESSION: Understanding

::SCENE::
LOCATION: EXT. PARK AVENUE - (DAY)
MOOD: Cold, then Painful, Festive
CHARACTERS: Narrator, Rosemary
BACKGROUND_IMAGE: park_avenue_day.png
BACKGROUND_EDIT: "Exterior Park Avenue, day time, festive Christmas decorations"

::SCRIPT::
- CHARACTER: Narrator
  LINE: - with its centre line of Christmas trees - Sunny, clear cold day. Rosemary walks slowly, carrying her pain inside her. Her coat is slightly snug over her stomach.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Rosemary passes Salvation Army Santa Clauses, shaking their bells, stores with their Christmas windows. She reaches the Time-Life Building and walks around looking for Hutch. It’s five-to-eleven on her wristwatch. She sits down on the low wall at the side of the forecourt.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: She lifts her face to the sun, and listens to the noises of the busy street. With her eyes closed, she speaks to herself.
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: Pain, begone! I will have no more of thee!
  EXPRESSION: Determined
- CHARACTER: Narrator
  LINE: She laughs ruefully. We hear a racketing noise. She opens her eyes and looks up. A helicopter passes over the building.
  EXPRESSION: null

::SCENE::
LOCATION: EXT. THE GLASS DOORS OF THE TIME-LIFE BUILDING - (DAY)
MOOD: Disappointment, Frustration
CHARACTERS: Narrator, Rosemary
BACKGROUND_IMAGE: time_life_building_glass_doors_day.png
BACKGROUND_EDIT: "Exterior glass doors of Time-Life Building, day time"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Rosemary is standing at the edge of the heavy flow of traffic. She looks at the out-coming faces, stretching how and then on tiptoes. She sees a man looking like Hutch, goes towards him, and realizes her mistake. It is a quarter past eleven on the clock.
  EXPRESSION: null

::SCENE::
LOCATION: INT. THE TIME-LIFE BUILDING - (DAY)
MOOD: Confusion, Concern
CHARACTERS: Narrator, Rosemary
BACKGROUND_IMAGE: time_life_building_lobby_day.png
BACKGROUND_EDIT: "Interior lobby of Time-Life Building, day time"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Rosemary walks in the lobby. She looks vaguely at the Directory on the wall.
  EXPRESSION: null

::SCENE::
LOCATION: INT. TIME-LIFE - (DAY)
MOOD: Shock, Concern
CHARACTERS: Narrator, Rosemary, Negro Girl, Grace Cardiff
BACKGROUND_IMAGE: time_life_phone_booth_day.png
BACKGROUND_EDIT: "Interior Time-Life Building, stainless steel phone booth, day time"

::SCRIPT::
- CHARACTER: Narrator
  LINE: A stainless steel phone booth. A Negro Girl is in it. She finishes soon and comes out with a friendly smile. Rosemary slips in and dials. On the first ring, a woman’s voice answers.
  EXPRESSION: null
- CHARACTER: Grace Cardiff (O.S.)
  LINE: Yes?
  EXPRESSION: Questioning
- CHARACTER: Rosemary
  LINE: Is this Edward Hutchins’ apartment?
  EXPRESSION: Inquiring
- CHARACTER: Grace Cardiff (O.S.)
  LINE: Yes. Who is this, please.
  EXPRESSION: Guarded
- CHARACTER: Rosemary
  LINE: My name is Rosemary Woodhouse, I had an appointment with Mr. Hutchins — is he there?
  EXPRESSION: Formal
- CHARACTER: Narrator
  LINE: (Silence)
  EXPRESSION: null
- CHARACTER: Grace Cardiff (O.S.)
  LINE: He was taken ill this morning.
  EXPRESSION: Grave
- CHARACTER: Rosemary
  LINE: Taken ill?
  EXPRESSION: Shocked
- CHARACTER: Grace Cardiff (O.S.)
  LINE: Yes. He’s in a deep coma at St. Vincent’s Hospital.
  EXPRESSION: Grave
- CHARACTER: Rosemary
  LINE: Oh, that’s awful. I spoke to him last night about ten-thirty.
  EXPRESSION: Distressed
- CHARACTER: Grace Cardiff (O.S.)
  LINE: I spoke to him at eleven.
  EXPRESSION: Matter-of-fact
- CHARACTER: Rosemary
  LINE: Who is this?
  EXPRESSION: Suspicious
- CHARACTER: Grace Cardiff (O.S.)
  LINE: You don’t know me, Rosemary, I am Grace Cardiff, Hutch’s friend.
  EXPRESSION: Informative
- CHARACTER: Rosemary
  LINE: What's causing it?
  EXPRESSION: Concerned
- CHARACTER: Grace Cardiff (O.S.)
  LINE: They don't know yet. At the moment he's totally unresponsive.
  EXPRESSION: Worried
- CHARACTER: Rosemary
  LINE: How awful.
  EXPRESSION: Sympathetic
- CHARACTER: Grace Cardiff (O.S.)
  LINE: I’m going to the hospital now.
  EXPRESSION: Determined
- CHARACTER: Rosemary
  LINE: Is there anything I can do?
  EXPRESSION: Helpful
- CHARACTER: Grace Cardiff (O.S.)
  LINE: Not really.
  EXPRESSION: Resigned

::SCENE::
LOCATION: EXT. MADISON AVENUE - (DAY)
MOOD: Melancholy, Reflective, Coincidental
CHARACTERS: Narrator, Rosemary, Mrs. Castevet
BACKGROUND_IMAGE: madison_avenue_day.png
BACKGROUND_EDIT: "Exterior Madison Avenue, day time, shop windows visible"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Rosemary walks slowly, looking down at the pavement.
  EXPRESSION: Sad
- CHARACTER: Narrator
  LINE: She crosses the street. Involuntarily she stops in front of a shop window in which a small creche is spotlighted. Rosemary smiles tenderly at the scene. She sees suddenly her own smiling reflection in the window glass. Her black-circled eyes look deeper and her cheeks more skeletal. The smile fades on her face.
  EXPRESSION: Melancholy
- CHARACTER: Mrs. Castevet (O.S.)
  LINE: Well, this is what I call the long arm of coincidence!
  EXPRESSION: Exclamatory
- CHARACTER: Narrator
  LINE: Rosemary turns and sees Mrs. Castevet, smiling, coming towards her.
  EXPRESSION: null
- CHARACTER: Mrs. Castevet
  LINE: I said to myself, ’As long as Rosemary’s out, I might as well go out for a little bit of Christmas shopping’, and here you are and here I am! Isn’t that something? Why, what’s the matter, dear?
  EXPRESSION: Enthusiastic
- CHARACTER: Narrator
  LINE: She looks at Rosemary, who is frozen with pain.
  EXPRESSION: null
- CHARACTER: Mrs. Castevet
  LINE: Do you feel all right?
  EXPRESSION: Concerned
- CHARACTER: Narrator
  LINE: Rosemary nods, pale, biting her lips.
  EXPRESSION: Painful
- CHARACTER: Mrs. Castevet
  LINE: You poor thing. You know what I think? I think we ought to be going home now. What do you say?
  EXPRESSION: Caring
- CHARACTER: Rosemary
  LINE: (Fast) No, no you have to do your shopping.
  EXPRESSION: Panicked
- CHARACTER: Mrs. Castevet
  LINE: Oh shoot, there’s two more weeks.
  EXPRESSION: Dismissive
- CHARACTER: Narrator
  LINE: She puts her wrist to her mouth and blows a whistle on her gold-chain bracelet. A taxi veers towards them. They get in.
  EXPRESSION: null

::SCENE::
LOCATION: INT. GUY AND ROSEMARY’S APARTMENT - KITCHEN - (DAY) - DECEMBER 20, 1965
MOOD: Domestic, Somber
CHARACTERS: Narrator, Rosemary
BACKGROUND_IMAGE: apartment_kitchen_day_dec20_1965.png
BACKGROUND_EDIT: "Interior kitchen of Guy and Rosemary's apartment, day time, December 20, 1965"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Rosemary opens fridge, takes out a little piece of meat, goes to the stove, puts it on a frying pan for two seconds each side, then puts it on a plate, sits down at the table and starts cutting the practically raw meat. There are many Christmas cards piled on the table. Rosemary, while eating, writes names on the cards.
  EXPRESSION: null

::SCENE::
LOCATION: INT. MR. & MRS. CASTEVETS’ APARTMENT LIVING ROOM - (NIGHT) - DECEMBER 31, 1965
MOOD: Festive, Tense
CHARACTERS: Narrator, Laura-Louise, Mr. Fountain, Mrs. Fountain, Mr. Gilmore, Mrs. Gilmore, Mr. Wees, Mrs. Wees, Mrs. Sabatini, Dr. Sapirstein, Rosemary, Guy, Mr. Castevet, Mrs. Castevet
BACKGROUND_IMAGE: castevets_apartment_living_room_night_dec31_1965.png
BACKGROUND_EDIT: "Interior living room of Mr. and Mrs. Castevets' apartment, night time, New Year's Eve party, December 31, 1965"

::SCRIPT::
- CHARACTER: Narrator
  LINE: New Year’s Eve party. All elderly people talking quietly, drinks in their hands. Laura-Louise, Mr. & Mrs. Fountain, Mr. & Mrs. Gilmore, Mr. & Mrs. Wees, Mrs. Sabatini and her cat. In two armchairs sit Dr. Sapirstein and Rosemary. Guy is at her side, resting on the arm of her chair.
  EXPRESSION: null
- CHARACTER: Dr. Sapirstein
  LINE: It’ll stop any day now.
  EXPRESSION: Reassuring
- CHARACTER: Rosemary
  LINE: It’s like a wire inside me getting tighter and tighter.
  EXPRESSION: Agonized
- CHARACTER: Dr. Sapirstein
  LINE: Usually older women, with less flexible joints have this sort of trouble.
  EXPRESSION: Clinical
- CHARACTER: Rosemary
  LINE: I’m not going out any more.
  EXPRESSION: Resigned
- CHARACTER: Dr. Sapirstein
  LINE: You don’t have to —
  EXPRESSION: Gentle
- CHARACTER: Narrator
  LINE: Mrs. Castevet brings Dr. Shand towards them.
  EXPRESSION: null
- CHARACTER: Mrs. Castevet
  LINE: Rosemary, I’d like you to meet Dr. Shand. He used to be a famous dentist? and he made the chain for your charm.
  EXPRESSION: Introduces
- CHARACTER: Rosemary
  LINE: Nice to meet you.
  EXPRESSION: Polite
- CHARACTER: Mr. Castevet
  LINE: One minute to go!
  EXPRESSION: Excited
- CHARACTER: Narrator
  LINE: Guy looks at his watch, stands up and goes toward Mr. Castevet. Mr. Castevet opens the champagne. He is an attentive and energetic host. Mrs. Castevet and Guy help with glasses. The champagne is passed around.
  EXPRESSION: null
- CHARACTER: Mr. Castevet
  LINE: To 1966, The Year One!
  EXPRESSION: Toasts

::SCENE::
LOCATION: INT. KITCHEN - (EARLY MORNING) - JANUARY 12, 1966
MOOD: Disturbing, Nauseating
CHARACTERS: Narrator, Rosemary
BACKGROUND_IMAGE: kitchen_early_morning_jan12_1966.png
BACKGROUND_EDIT: "Interior kitchen, early morning, January 12, 1966"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Rosemary in front of the open fridge chewing a raw and dripping chicken heart. She catches her reflection in the side of the toaster, looks at herself, her hand and the part of the heart not yet eaten held in red-dripping fingers. She goes over and puts the heart in the garbage, then turns on the water and rinses her hand. With the water still running, she bends over the sink and begins to vomit. She drinks some water, washes her face and hands, turns off the water and dries herself. She stands for a while, thinking; she gets a memo pad and pencil from a drawer, sits at the table and starts to write.
  EXPRESSION: Disturbing

::SCENE::
LOCATION: INT. HALLWAY - KITCHEN - (DAY)
MOOD: Neutral
CHARACTERS: Narrator
BACKGROUND_IMAGE: hallway_kitchen_day.png
BACKGROUND_EDIT: "Interior hallway leading to kitchen, day time"

::SCRIPT::
- CHARACTER: Narrator
  LINE:
  EXPRESSION: null

::SCENE::
LOCATION: Kitchen
MOOD: Domesticity, underlying tension
CHARACTERS: Guy, Rosemary
BACKGROUND_IMAGE: kitchen_planning.png
BACKGROUND_EDIT: "Early morning, kitchen table with cookbooks and slips of paper"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Guy, in his pajamas, goes across the hallway. He enters the kitchen.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Rosemary his the Life Cookbook open on the table and is copying a recipe from it.
  EXPRESSION: null
- CHARACTER: Guy
  LINE: What the hell are you doing?
  EXPRESSION: Confused
- CHARACTER: Rosemary
  LINE: Planning the menu. We’re giving a party on January twenty-second. A week from next Saturday.
  EXPRESSION: Determined
- CHARACTER: Narrator
  LINE: She looks among several slips of paper on the table and picks one up.
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: For our old friends. I mean our young friends. Minnie and Roman are not invited. Neither is Laura-Louise. Neither is Dr. Sapirstein and Dr. Shand. This is a very special party. You have to be under sixty to get in.
  EXPRESSION: Calculating
- CHARACTER: Guy
  LINE: Whew! For a minute there I didn’t think I was going to make it.
  EXPRESSION: Sarcastic
- CHARACTER: Rosemary
  LINE: Oh, you make it. You’re the bartender.
  EXPRESSION: Amused
- CHARACTER: Guy
  LINE: Swell. Do you really think this is such a great idea?
  EXPRESSION: Skeptical
- CHARACTER: Rosemary
  LINE: I think it’s the best idea I’ve had in months.
  EXPRESSION: Confident
- CHARACTER: Guy
  LINE: Don’t you think you ought to check with Sapirstein first?
  EXPRESSION: Concerned
- CHARACTER: Rosemary
  LINE: Why? I’m just going to give a party? I’m not going to swim the English Channel.
  EXPRESSION: Dismissive
- CHARACTER: Narrator
  LINE: Guy goes to the sink, turns on the water and holds a glass under it. He turns off the water, raises the glass and drinks.
  EXPRESSION: null
- CHARACTER: Guy
  LINE: What about the pain?
  EXPRESSION: Worried
- CHARACTER: Rosemary
  LINE: Haven’t you heard? It’ll go in a day or two.
  EXPRESSION: Dryly amused

::SCENE::
LOCATION: Kitchen
MOOD: Domestic preparation, subtle unease
CHARACTERS: Rosemary, Mrs. Castevet
BACKGROUND_IMAGE: kitchen_preparations.png
BACKGROUND_EDIT: "Daytime, kitchen counter with food ingredients and drinks"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Mrs. Castevet is standing beside Rosemary in the doorway. Rosemary is wearing an apron and holding the glass with the drink in her hand. On the table, there is crab-meat and pieces of lobster and other food ready to be cooked. Mrs. Castevet looks at the preparations.
  EXPRESSION: null
- CHARACTER: Mrs. Castevet
  LINE: That looks interesting. What is it?
  EXPRESSION: Curious
- CHARACTER: Rosemary
  LINE: We’re having some people over, on Saturday.
  EXPRESSION: Casual
- CHARACTER: Mrs. Castevet
  LINE: Oh, you feel up to entertaining?
  EXPRESSION: Concerned
- CHARACTER: Rosemary
  LINE: Yes, I do. These are old friends whom we haven’t seen in a long time. They don’t even know yet that I’m pregnant.
  EXPRESSION: Proud
- CHARACTER: Mrs. Castevet
  LINE: I’d be glad to give you a hand if you’d like. I could help you dish things out.
  EXPRESSION: Helpful
- CHARACTER: Rosemary
  LINE: That’s sweet of you, but I can manage. It’s going to be a buffet and we are getting a bartender.
  EXPRESSION: Gracious
- CHARACTER: Mrs. Castevet
  LINE: I could help you take the coats.
  EXPRESSION: Eager
- CHARACTER: Rosemary
  LINE: No, really, Minnie, you do enough for me as it is. Really.
  EXPRESSION: Firm
- CHARACTER: Mrs. Castevet
  LINE: Well, let me know if you change your mind. Drink your drink now.
  EXPRESSION: Persuasive
- CHARACTER: Narrator
  LINE: Rosemary looks at the glass in her hand.
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: I’d rather not. Not this minute. I’ll drink it in a little while.
  EXPRESSION: Hesitant
- CHARACTER: Mrs. Castevet
  LINE: It doesn’t do to let it stand.
  EXPRESSION: Insistent
- CHARACTER: Rosemary
  LINE: I won’t wait long. Go on, You go back and I’ll bring the glass to you later on.
  EXPRESSION: Evasive
- CHARACTER: Mrs. Castevet
  LINE: I’ll wait and save you the walk.
  EXPRESSION: Stubborn
- CHARACTER: Rosemary
  LINE: You’ll do no such thing. I get very nervous if anyone watches me while I’m cooking. Scoot now, go on. You’re too nice to me, really you are.
  EXPRESSION: Forceful
- CHARACTER: Narrator
  LINE: Mrs. Castevet backs away.
  EXPRESSION: null
- CHARACTER: Mrs. Castevet
  LINE: Don’t wait too long. It’s going to lose its vitamins.
  EXPRESSION: Warning
- CHARACTER: Narrator
  LINE: Mrs. Castevet goes. Rosemary watches the door close.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: She goes into the kitchen and stands a moment with the glass in her hand, then goes to the sink and tips out the pale green drink straight down into the drain.
  EXPRESSION: Deceptive

::SCENE::
LOCATION: Guy and Rosemary's Apartment - Party
MOOD: Festive, celebratory with underlying tension
CHARACTERS: Renato, Ted, Carole Wendell, Joan Jelico, Elise Dunstan, Hugh Dunstan, Rain Morgan, Jimmy, Tiger, Lou Comfort, Claudia Comfort, Scott, Rosemary
BACKGROUND_IMAGE: party_living_room.png
BACKGROUND_EDIT: "Night, lively party with guests mingling, fire in the hearth"

::SCRIPT::
- CHARACTER: Narrator
  LINE: There is a fire going and an Italian bartender, RENATO, mixes drinks quickly. People already there are: TED and CAROLE WENDELL, JOAN JELICO, ELISE and HUGH (limping) DUNSTAN, RAIN MORGAN (a beautiful Negro model), JIMMY and TIGER, LOU and CLAUDIA COMFORT and SCOTT (Claudia’s brother).
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: JOAN is giving Rosemary a hug and a kiss.
  EXPRESSION: null
- CHARACTER: Joan
  LINE: You dirty stinking secret-keeper!
  EXPRESSION: Playful
- CHARACTER: Rain Morgan (O.S.)
  LINE: Who's pregnant?
  EXPRESSION: Inquisitive
- CHARACTER: Elise (O.S.)
  LINE: Rosemary is.
  EXPRESSION: Excited
- CHARACTER: Narrator
  LINE: People gather to congratulate Rosemary. Telephone RINGS in the bedroom.
  EXPRESSION: null
- CHARACTER: Claudia (O.S.)
  LINE: Rosie! Bob and Lee are stuck at another party. They’ll be right over.
  EXPRESSION: Excited
- CHARACTER: Rain Morgan
  LINE: Congratulations.
  EXPRESSION: Sincere
- CHARACTER: Lou and Claudia
  LINE: Come from the bedroom.
  EXPRESSION: null
- CHARACTER: Claudia
  LINE: You’re so lucky. What a great house?
  EXPRESSION: Admiring
- CHARACTER: Hugh Dunstan
  LINE: Adrian Marcato lived here
  EXPRESSION: Spooky
- CHARACTER: Guy
  LINE: And the Trench sisters.
  EXPRESSION: Informative
- CHARACTER: Narrator
  LINE: The DOORBELL RINGS; Rosemary goes out.
  EXPRESSION: null
- CHARACTER: Jimmy
  LINE: The Trent sisters?
  EXPRESSION: Curious
- CHARACTER: Hugh Dunstan
  LINE: Trench. They ate little children.
  EXPRESSION: Ominous
- CHARACTER: Ted
  LINE: And he doesn’t mean just ate them. He means ate them?
  EXPRESSION: Grim
- CHARACTER: Narrator
  LINE: Rosemary opens the door. Mike and Pedro stand there with bouquets of bright red roses. They kiss, Pedro, with his cheek against Rosemary, murmurs?
  EXPRESSION: null
- CHARACTER: Pedro
  LINE: Make him feed you, baby; you look like a bottle of iodine,
  EXPRESSION: Affectionate, concerned
- CHARACTER: Narrator
  LINE: Rosemary takes the roses into the kitchen, Elise Dunstan comes in after her, with a drink in her hand.
  EXPRESSION: null
- CHARACTER: Elise Dunstan
  LINE: Will you look at this kitchen? Are you all right, Rosie? You look a little tired.
  EXPRESSION: Concerned
- CHARACTER: Rosemary
  LINE: Thanks for the understatement,
  EXPRESSION: Sarcastic
- CHARACTER: Elise
  LINE: How do you like C. C. Hill? Isn't he a dreamboy?
  EXPRESSION: Inquisitive
- CHARACTER: Rosemary
  LINE: Yes, but I’m not using him.
  EXPRESSION: Firm
- CHARACTER: Elise
  LINE: No!
  EXPRESSION: Surprised
- CHARACTER: Rosemary
  LINE: I’ve got a doctor named Sapirstein, an older man.
  EXPRESSION: Informative
- CHARACTER: Narrator
  LINE: Guy looks in.
  EXPRESSION: null
- CHARACTER: Elise
  LINE: Well congratulations, Dad.
  EXPRESSION: Playful
- CHARACTER: Guy
  LINE: Thanks. Weren’t nothin’ to it. Do you want me to bring in the dip, Ro?
  EXPRESSION: Humorous
- CHARACTER: Rosemary
  LINE: Oh, yes, would you? Look at these roses!
  EXPRESSION: Enthusiastic
- CHARACTER: Narrator
  LINE: Guy takes a tray of crackers and a bowl of pale pink dip from the table.
  EXPRESSION: null
- CHARACTER: Guy
  LINE: Would you get the other one?
  EXPRESSION: Helpful
- CHARACTER: Elise
  LINE: Sure.
  EXPRESSION: Agreeable
- CHARACTER: Narrator
  LINE: Elise takes the second bowl and follows Guy out.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: PORTIA HAYNES and DEE BERTILLON arrive. They leave their coats in the bedroom.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: In the living room, Guy puts dip on table.
  EXPRESSION: null
- CHARACTER: Tiger
  LINE: Hey, what ever happened to the other guy? Is he still blind?
  EXPRESSION: Curious
- CHARACTER: Guy
  LINE: I don’t know.
  EXPRESSION: Indifferent
- CHARACTER: Narrator
  LINE: Rosemary enters with roses. Mike wig-wags over heads and mouths "Congratulations." Rosemary smiles and mouths "Thanks."
  EXPRESSION: null
- CHARACTER: Carol
  LINE: Donald Baumgart? You know who he is, Tiger, he’s the boy Zoe Piper lives with.
  EXPRESSION: Informative
- CHARACTER: Tiger
  LINE: Oh, is he the one?
  EXPRESSION: Realizing
- CHARACTER: Narrator
  LINE: Renato gives Rosemary a scotch with a lot of water.
  EXPRESSION: null
- CHARACTER: Renato
  LINE: I make the first ones strong, to get them happy. Then I go light and conserve.
  EXPRESSION: Pragmatic
- CHARACTER: Carol
  LINE: He’s writing a great play.
  EXPRESSION: Admiring
- CHARACTER: Rosemary
  LINE: Is he still blind?
  EXPRESSION: Concerned
- CHARACTER: Carol
  LINE: Oh, yes. He’s going through hell trying to make the adjustment. But this great play is coming out of it. He dictates and Zoe writes.
  EXPRESSION: Empathetic
- CHARACTER: Narrator
  LINE: Rosemary shuts her eyes and holds her breath with pain.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: She puts her drink aside.
  EXPRESSION: null
- CHARACTER: Claudia
  LINE: Are you all right?
  EXPRESSION: Concerned
- CHARACTER: Rosemary
  LINE: Smiling
  EXPRESSION: Forced smile
- CHARACTER: Rosemary
  LINE: Yes, fine. I had a cramp for a moment.
  EXPRESSION: Reassuring (false)

::SCENE::
LOCATION: Kitchen
MOOD: Anxious, concerned, secretive
CHARACTERS: Tiger, Joan, Elise, Rosemary
BACKGROUND_IMAGE: kitchen_salad.png
BACKGROUND_EDIT: "Night, kitchen area, salad bowl on table"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Tiger watches Rosemary tossing the salad. Joan and Elise come in and close the door behind them.
  EXPRESSION: null
- CHARACTER: Joan
  LINE: Is the doctor satisfied with your condition?
  EXPRESSION: Direct
- CHARACTER: Narrator
  LINE: Rosemary nods.
  EXPRESSION: null
- CHARACTER: Joan
  LINE: Claudia said you had a cramp.
  EXPRESSION: Skeptical
- CHARACTER: Rosemary
  LINE: I have a pain. But it's going to stop soon.
  EXPRESSION: Resigned
- CHARACTER: Tiger
  LINE: What kind of a pain?
  EXPRESSION: Inquisitive
- CHARACTER: Rosemary
  LINE: A - a pain. A sharp pain, that’s all. It’s because my pelvis is expanding.
  EXPRESSION: Deflecting
- CHARACTER: Elise
  LINE: Rosie, I’ve had that - two times. It’s a bit like a Charley horse, that's all.
  EXPRESSION: Reassuring
- CHARACTER: Rosemary
  LINE: Well, everyone is different. Every pregnancy is different.
  EXPRESSION: Defensive
- CHARACTER: Joan
  LINE: Not that different. You look like Miss Concentration Camp ’66. Are you sure this doctor knows what he’s doing?
  EXPRESSION: Accusatory
- CHARACTER: Narrator
  LINE: Rosemary begins to sob quietly and defeatedly, holding the wooden spoon in the salad. Tears run down her cheeks.
  EXPRESSION: Devastated
- CHARACTER: Joan
  LINE: Oh, God.
  EXPRESSION: Upset
- CHARACTER: Narrator
  LINE: She looks for help to Tiger who touches Rosemary’s shoulder.
  EXPRESSION: null
- CHARACTER: Tiger
  LINE: Shh, ah, shh, don’t cry, Rosemary.
  EXPRESSION: Comforting
- CHARACTER: Elise
  LINE: It's good. It's the best thing. Let her.
  EXPRESSION: Encouraging
- CHARACTER: Narrator
  LINE: Rosemary weeps, black streaks smearing down her cheeks. Elise puts her into a chair; Tiger takes the spoons from her hands and moves the salad bowl to the far side of the table.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The door starts to open and Joan runs to it and stops and blocks it. It’s Guy.
  EXPRESSION: null
- CHARACTER: Guy (O.S.)
  LINE: Hey, let me in.
  EXPRESSION: Demanding
- CHARACTER: Joan
  LINE: Sorry. Girls only.
  EXPRESSION: Firm
- CHARACTER: Guy (O.S.)
  LINE: Let me speak to Rosemary.
  EXPRESSION: Insistent
- CHARACTER: Joan
  LINE: Can't; she's busy.
  EXPRESSION: Evasive
- CHARACTER: Guy (O.S.)
  LINE: Look, I've got to wash glasses.
  EXPRESSION: Annoyed
- CHARACTER: Joan
  LINE: Use the bathroom.
  EXPRESSION: Dismissive
- CHARACTER: Narrator
  LINE: She shoulders the door; it closes with a click and she leans against it.
  EXPRESSION: null
- CHARACTER: Guy (O.S.)
  LINE: Damn it, open the door.
  EXPRESSION: Frustrated
- CHARACTER: Narrator
  LINE: Rosemary goes on crying, her head bowed, her shoulders heaving, her hands limp in her lap. Elise crouches, wiping at her cheeks with the end of a towel; Tiger smooths her hair and tries to still her shoulders.
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: It hurts so much.
  EXPRESSION: Pained
- CHARACTER: Narrator
  LINE: She raises her face to them.
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: I’m so afraid the baby is going to die.
  EXPRESSION: Terrified
- CHARACTER: Elise
  LINE: What is he doing to help you?
  EXPRESSION: Direct
- CHARACTER: Rosemary
  LINE: Nothing, nothing.
  EXPRESSION: Hopeless
- CHARACTER: Tiger
  LINE: When did it start?
  EXPRESSION: Concerned
- CHARACTER: Narrator
  LINE: Rosemary SOBS.
  EXPRESSION: null
- CHARACTER: Elise
  LINE: When did the pain start, Rosie?
  EXPRESSION: Gentle
- CHARACTER: Rosemary
  LINE: In November.
  EXPRESSION: Weak
- CHARACTER: Elise
  LINE: In November?
  EXPRESSION: Shocked
- CHARACTER: Joan (From the door)
  LINE: What?
  EXPRESSION: Shocked
- CHARACTER: Tiger
  LINE: You've been in pain since November, and he isn't doing anything for you?
  EXPRESSION: Outraged
- CHARACTER: Rosemary
  LINE: He says it'll stop.
  EXPRESSION: Resigned
- CHARACTER: Joan
  LINE: Why don’t you see another doctor?
  EXPRESSION: Insistent
- CHARACTER: Narrator
  LINE: Rosemary shakes her head.
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: He’s very good. He was on "Open End."
  EXPRESSION: Defending
- CHARACTER: Tiger
  LINE: He sounds like a sadistic nut.
  EXPRESSION: Disgusted
- CHARACTER: Elise
  LINE: Pain like that is a warning that something’s not right. Go see Dr. Hill, Rosie. See somebody besides that -
  EXPRESSION: Urgent
- CHARACTER: Tiger
  LINE: That nut.
  EXPRESSION: Disgusted
- CHARACTER: Elise
  LINE: You can’t go on suffering like this.
  EXPRESSION: Pleading
- CHARACTER: Rosemary
  LINE: I won’t have an abortion.
  EXPRESSION: Adamant
- CHARACTER: Narrator
  LINE: Joan leans from the door whispering.
  EXPRESSION: null
- CHARACTER: Joan
  LINE: Nobody’s telling you to have an abortion! Just go see another doctor, that’s all.
  EXPRESSION: Frustrated
- CHARACTER: Narrator
  LINE: Rosemary takes the towel and presses it to each eye in turn. She smiles at Elise, and at Tiger and Joan.
  EXPRESSION: null

::SCENE::
LOCATION: Living Room
MOOD: Socializing, consumption
CHARACTERS: Various Guests, Renato, Claudia's Brother
BACKGROUND_IMAGE: party_guests_eating.png
BACKGROUND_EDIT: "Night, living room with guests eating and drinking"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The guests are sitting round in various places with napkins and plates on their knees, eating chute and salad. Renato is serving wine.
  EXPRESSION: null
- CHARACTER: Claudia’s Brother
  LINE: His name is Altizer and he’s down in - Atlanta, I think; he says that the death of God is a specific historic event that hap
  EXPRESSION: Philosophical

::SCENE::
LOCATION: Not specified
MOOD: Surreal
CHARACTERS: Narrator, Jimmy
BACKGROUND_IMAGE: not_specified_day.png
BACKGROUND_EDIT: "Abstract, possibly cosmic background"

::SCRIPT::
- CHARACTER: Narrator
  LINE: pened right now, in our time. That God literally died.
  EXPRESSION: null
- CHARACTER: Jimmy
  LINE: Hey, snow!
  EXPRESSION: Excited

::PATHS::
- CHOICE: "Watch the snow"
  TARGET: living_room_night
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Not specified
MOOD: Cozy, Watchful
CHARACTERS: Narrator, Rosemary
BACKGROUND_IMAGE: not_specified_day.png
BACKGROUND_EDIT: "Abstract, possibly cosmic background"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Guests crowd the windows; fat wet snowflakes shear down, now then striking one of the panes, sliding and melting.
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: This is why I wanted this apartment; to sit here and watch the snow with the fire going.
  EXPRESSION: Content

::PATHS::
- CHOICE: "Continue watching snow"
  TARGET: living_room_night
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Living Room
MOOD: Tense, Discontent
CHARACTERS: Narrator, Rosemary, Guy
BACKGROUND_IMAGE: living_room_night.png
BACKGROUND_EDIT: "Nighttime, cluttered with dirty glasses, used napkins, and overflowing ashtrays. Rosemary is sitting, Guy is standing."

::SCRIPT::
- CHARACTER: Narrator
  LINE: There are dirty glasses, used napkins and spilling-over ashtrays all round. Rosemary is sitting. Guy is standing with his hands on his hips; looking round the room.
  EXPRESSION: null
- CHARACTER: Guy
  LINE: The thing to do now is move.
  EXPRESSION: Determined
- CHARACTER: Rosemary
  LINE: Guy.
  EXPRESSION: Pleading
- CHARACTER: Guy
  LINE: Yes?
  EXPRESSION: Attentive
- CHARACTER: Rosemary
  LINE: I’m going to Dr. Hill. Monday morning.
  EXPRESSION: Resolute
- CHARACTER: Narrator
  LINE: Guy says nothing, looking at Rosemary.
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: Dr. Sapirstein is either lying or else he’s - I don’t know, out of his mind. Pain like this is a warning that something is wrong.
  EXPRESSION: Frustrated
- CHARACTER: Guy
  LINE: Rosemary.
  EXPRESSION: Concerned
- CHARACTER: Rosemary
  LINE: And I’m not drinking Minnie’s drink any more. I want vitamins in pills, like everybody else. I haven’t drunk it for three days now. I’ve thrown it away.
  EXPRESSION: Determined
- CHARACTER: Guy
  LINE: You’ve -
  EXPRESSION: Shocked
- CHARACTER: Rosemary
  LINE: I’ve made my own drink instead.
  EXPRESSION: Defiant
- CHARACTER: Narrator
  LINE: Guy draws together all his surprise and anger and points back over his shoulder toward the kitchen, crying at her.
  EXPRESSION: null
- CHARACTER: Guy
  LINE: Is that what those bitches were giving you in there? Is that their hint for today?
  EXPRESSION: Enraged
- CHARACTER: Rosemary
  LINE: They’re my friends. Don't call them, bitches.
  EXPRESSION: Angry
- CHARACTER: Guy
  LINE: They're a bunch of not-very-bright bitches who ought to mind their own God-damned business.
  EXPRESSION: Enraged
- CHARACTER: Rosemary
  LINE: All they said was get a second opinion.
  EXPRESSION: Calm
- CHARACTER: Guy
  LINE: You've got the best doctor in New York, Rosemary. Do you know what Dr. Hill is? Charley Nobody, that's what he is.
  EXPRESSION: Scornful
- CHARACTER: Rosemary
  LINE: I'm tired of hearing how great Dr. Sapirstein is.
  EXPRESSION: Upset
- CHARACTER: Narrator
  LINE: (She starts to cry)
  EXPRESSION: null
- CHARACTER: Guy
  LINE: We'll have to pay Sapirstein and pay Hill too. It's out of the question.
  EXPRESSION: Agitated
- CHARACTER: Rosemary
  LINE: I'm not going to change, I'm just going to let Hill examine me and give his opinion.
  EXPRESSION: Determined
- CHARACTER: Guy
  LINE: I won't let you. It's - it's not fair to Sapirstein.
  EXPRESSION: Angry
- CHARACTER: Narrator
  LINE: Rosemary rises.
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: Not fair to - What are you talking about? What about what's fair to me?
  EXPRESSION: Disbelieving
- CHARACTER: Guy
  LINE: You want another opinion? All right. Tell Sapirstein; let him decide who gives it. At least have that much courtesy to the top man in his field.
  EXPRESSION: Condescending
- CHARACTER: Rosemary
  LINE: I want Dr. Hill. If you won't pay I'll
  EXPRESSION: Defiant
- CHARACTER: Narrator
  LINE: She stops short and stands motionless, paralyzed, no part of her moving. A tear slides down her cheek.
  EXPRESSION: null
- CHARACTER: Guy
  LINE: Ro?
  EXPRESSION: Worried
- CHARACTER: Narrator
  LINE: Rosemary catches her breath.
  EXPRESSION: null
- CHARACTER: Guy
  LINE: Ro?
  EXPRESSION: Worried
- CHARACTER: Narrator
  LINE: He takes a step forward, worried.
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: It stopped.
  EXPRESSION: Breathless
- CHARACTER: Guy
  LINE: What?
  EXPRESSION: Confused
- CHARACTER: Rosemary
  LINE: The pain.
  EXPRESSION: Calm
- CHARACTER: Guy
  LINE: Stopped?
  EXPRESSION: Disbelieving
- CHARACTER: Rosemary
  LINE: Just now.
  EXPRESSION: Calm
- CHARACTER: Narrator
  LINE: She manages to smile at him.
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: It stopped. Just like that.
  EXPRESSION: Relieved
- CHARACTER: Narrator
  LINE: She closes her eyes and takes a deep breath; then another one, deeper still. She opens her eyes. Guy is still looking at her, worried.
  EXPRESSION: null
- CHARACTER: Guy
  LINE: What was in the drink you made?
  EXPRESSION: Concerned
- CHARACTER: Narrator
  LINE: Consternation. Rosemary doesn't answer immediately.
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: An egg. Milk. Sugar.
  EXPRESSION: Calm
- CHARACTER: Guy
  LINE: What else?
  EXPRESSION: Demanding
- CHARACTER: Narrator
  LINE: Rosemary puts her hands on her stomach, concentrating.
  EXPRESSION: null
- CHARACTER: Guy
  LINE: What else?
  EXPRESSION: Demanding
- CHARACTER: Rosemary
  LINE: It's alive.
  EXPRESSION: Giggling
- CHARACTER: Narrator
  LINE: (She giggles again)
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: It’s moving. It's all right. It's moving.
  EXPRESSION: Joyful
- CHARACTER: Narrator
  LINE: She looks down at her stomach and presses it lightly. She reaches for Guy, not looking at him; snaps her fingers quickly for his hand. He comes closer and gives it. She puts it to the side of her stomach and holds it.
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: You feel it?
  EXPRESSION: Eager
- CHARACTER: Narrator
  LINE: (She looks at him) There.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Guy jerks his hand away, pale.
  EXPRESSION: null
- CHARACTER: Guy
  LINE: Yes. Yes, I felt it.
  EXPRESSION: Terrified
- CHARACTER: Rosemary
  LINE: It's nothing to be afraid of. It won't bite you
  EXPRESSION: Laughing
- CHARACTER: Narrator
  LINE: It's wonderful.
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: It's alive. It’s kicking.
  EXPRESSION: Ecstatic
- CHARACTER: Narrator
  LINE: Rosemary laughs and cries too, holding her stomach with both hands.
  EXPRESSION: null
- CHARACTER: Guy
  LINE: I’ll clean up some of this mess.
  EXPRESSION: Nervous
- CHARACTER: Narrator
  LINE: He picks up an ashtray and a glass and another glass.
  EXPRESSION: null

::PATHS::
- CHOICE: "Clean up"
  TARGET: den_day
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Den
MOOD: Domesticity, Anticipation
CHARACTERS: Narrator, Mrs. Castevet, Rosemary, Guy, Two Workers
BACKGROUND_IMAGE: den_day.png
BACKGROUND_EDIT: "Daytime, wallpaper being hung. Mrs. Castevet is present. Rosemary is visibly pregnant. Baby items are being brought in."

::SCRIPT::
- CHARACTER: Narrator
  LINE: The grumbling PAPERHANGER sticks yellow and white paper on the wall. Mrs. Castevet hands Rosemary the drink and a white cake.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: TWO WORKERS come with a bureau, Guy with a bathinette, and Rosemary with a crib. She is much bigger than before. She looks healthier and prettier.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Rosemary puts baby clothes into the bureau; receiving blankets, waterproof pants and shirts. She holds up a tiny shirt to show Guy. They both laugh.
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue preparing for the baby"
  TARGET: apartment_bedroom_dusk
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Guy and Rosemary's Apartment Bedroom
MOOD: Preparatory, Slightly Anxious
CHARACTERS: Narrator, Rosemary, Guy
BACKGROUND_IMAGE: apartment_bedroom_dusk.png
BACKGROUND_EDIT: "Dusk, a suitcase is open on the bed. Rosemary is in her ninth month of pregnancy."

::SCRIPT::
- CHARACTER: Narrator
  LINE: An open suitcase lying on the bed. Rosemary in her ninth month is putting things into it (nightgowns, nursing brassieres, a quilted housecoat, etc.). She closes the suitcase, goes to the Hallway and leaves it next to the Bedroom door.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: In the Living Room, Guy is sitting in an armchair with an open newspaper. He watches Rosemary as she places the suitcase.
  EXPRESSION: null
- CHARACTER: Guy
  LINE: What’s that for?
  EXPRESSION: Curious
- CHARACTER: Rosemary
  LINE: My hospital suitcase.
  EXPRESSION: Casual
- CHARACTER: Guy
  LINE: Honey, you have three weeks to —
  EXPRESSION: Concerned
- CHARACTER: Narrator
  LINE: The telephone rings. Rosemary goes to answer it. Guy strains to listen.
  EXPRESSION: null
- CHARACTER: Rosemary (O.S.)
  LINE: Yes. Hello, Mrs. Cardiff. No! Oh my God! Yes I will.
  EXPRESSION: Shocked
- CHARACTER: Narrator
  LINE: Guy stands up and goes toward the Bedroom. As he is under the archway, Rosemary appears in the Bedroom door. They look at each other for a moment.
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: Hutch is dead.
  EXPRESSION: Somber
- CHARACTER: Narrator
  LINE: Guy turns white. There is a long silence.
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: I feel awful. All this time I didn’t even think of him.
  EXPRESSION: Guilty

::PATHS::
- CHOICE: "React to the news"
  TARGET: cemetery_gate
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Cemetery Gate
MOOD: Somber, Late
CHARACTERS: Narrator, Rosemary, Doris, Husband, Edna, Grace Cardiff
BACKGROUND_IMAGE: cemetery_gate.png
BACKGROUND_EDIT: "June 8, 1966. Rosemary arrives late. Funeral guests are leaving."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Rosemary gets out of a taxi. She is late; the funeral guests are leaving the cemetery and getting into cars.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Rosemary meets DORIS and her HUSBAND.
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: I’m Mrs. Woodhouse. I knew your father.
  EXPRESSION: Polite
- CHARACTER: Doris
  LINE: Oh, you’re Rosemary?
  EXPRESSION: Recognizing
- CHARACTER: Narrator
  LINE: They shake hands.
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: Yes. I know how you feel, both of you.
  EXPRESSION: Empathetic
- CHARACTER: Narrator
  LINE: Doris indicates EDNA, who looks like Doris, but a little younger.
  EXPRESSION: null
- CHARACTER: Doris
  LINE: This is my sister, Edna.
  EXPRESSION: Introducing
- CHARACTER: Rosemary
  LINE: Nice to meet you. I’m so sorry to be late.
  EXPRESSION: Apologetic
- CHARACTER: Narrator
  LINE: GRACE CARDIFF, a smartly dressed woman in her early fifties, touches Rosemary’s arm.
  EXPRESSION: null
- CHARACTER: Grace Cardiff
  LINE: Excuse me.
  EXPRESSION: Polite
- CHARACTER: Rosemary
  LINE: Yes?
  EXPRESSION: Attentive
- CHARACTER: Grace Cardiff
  LINE: I’m Grace Cardiff.
  EXPRESSION: Introducing
- CHARACTER: Rosemary
  LINE: Oh! I’m glad I met you. Thank you so much for calling me.
  EXPRESSION: Grateful
- CHARACTER: Narrator
  LINE: Grace Cardiff is holding a book-size brown-paper package.
  EXPRESSION: null
- CHARACTER: Grace Cardiff
  LINE: I was going to mail this. Then I thought you’d be here.
  EXPRESSION: Explaining
- CHARACTER: Narrator
  LINE: She gives Rosemary the package. Rosemary looks at it; her name and address are printed on it, and Grace Cardiff’s return address.
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: What is it
  EXPRESSION: Curious
- CHARACTER: Grace Cardiff
  LINE: Hatch regained consciousness at the end and ho thought it was the next morning. You know - when you had the appointment.
  EXPRESSION: Informative
- CHARACTER: Rosemary
  LINE: Yes.
  EXPRESSION: Acknowledging
- CHARACTER: Grace Cardiff
  LINE: I wasn’t there, but he told the doctor to make sure that you got the book that was on his desk.
  EXPRESSION: Informative
- CHARACTER: Narrator
  LINE: Grace gets into car. The car begins to leave.
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: Thank you.
  EXPRESSION: Grateful
- CHARACTER: Grace Cardiff
  LINE: Oh, and I’m to tell you, the name is an anagram.
  EXPRESSION: Informative
- CHARACTER: Narrator
  LINE: (Through window)
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: The name of the book?
  EXPRESSION: Inquiring
- CHARACTER: Grace Cardiff
  LINE: Apparently. He was delirious - so it’s hard to be sure.
  EXPRESSION: Uncertain

::PATHS::
- CHOICE: "Examine the book"
  TARGET: apartment_bedroom_day
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Guy and Rosemary's Apartment Bedroom
MOOD: Introspective, Mysterious
CHARACTERS: Narrator, Rosemary, Mrs. Castevet
BACKGROUND_IMAGE: apartment_bedroom_day.png
BACKGROUND_EDIT: "Daytime. Rosemary is back from the cemetery, unwrapping a book. Mrs. Castevet arrives with a drink and cake."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Rosemary slips out of her shoes, takes off her gloves and pushes her feet into slippers. At the same time, she picks up her handbag, opens it and takes out the wrapped book. The doorbell rings. Still carrying the book, Rosemary goes to open the door. Mrs. Castevet stands there with the drink and a little white cake.
  EXPRESSION: null
- CHARACTER: Mrs. Castevet
  LINE: I heard you come in. It certainly wasn’t very long.
  EXPRESSION: Observant
- CHARACTER: Rosemary
  LINE: I was late. Couldn’t get a taxi.
  EXPRESSION: Stating fact
- CHARACTER: Narrator
  LINE: She takes the glass and drinks the pale green liquid.
  EXPRESSION: null
- CHARACTER: Mrs. Castevet
  LINE: Oh! What a shame! You got mail already?
  EXPRESSION: Feigning surprise
- CHARACTER: Rosemary
  LINE: No, someone gave it to me.
  EXPRESSION: Truthful
- CHARACTER: Mrs. Castevet
  LINE: Here, I’ll hold it.
  EXPRESSION: Helpful
- CHARACTER: Narrator
  LINE: Mrs. Castevet takes the package and hands Rosemary the white cake. Rosemary starts to eat it.
  EXPRESSION: null
- CHARACTER: Mrs. Castevet
  LINE: A book?
  EXPRESSION: Inquisitive
- CHARACTER: Narrator
  LINE: (Weighing the package)
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: Mm-hmm.
  EXPRESSION: Affirmative
- CHARACTER: Mrs. Castevet
  LINE: Oh, I know that house. The Gilmores used to live there.
  EXPRESSION: Nostalgic
- CHARACTER: Narrator
  LINE: (Reading the return address)
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: Oh?
  EXPRESSION: Curious
- CHARACTER: Mrs. Castevet
  LINE: I’ve been there lots of times. ’Grace'. That’s one of my favorite names.
  EXPRESSION: Fond
- CHARACTER: Rosemary
  LINE: Yes?
  EXPRESSION: Polite
- CHARACTER: Narrator
  LINE: She finishes the cake and the drink and takes the package from Mrs. Castevet; giving her the glass.
  EXPRESSION: null
- CHARACTER: Mrs. Castevet
  LINE: You need anything?
  EXPRESSION: Inquiring
- CHARACTER: Rosemary
  LINE: No, thanks.
  EXPRESSION: Polite
- CHARACTER: Mrs. Castevet
  LINE: Take a nap, why don’t you?
  EXPRESSION: Suggestive
- CHARACTER: Rosemary
  LINE: I’m going to. ’By.
  EXPRESSION: Agreeable
- CHARACTER: Narrator
  LINE: With a paring knife Rosemary cuts the string of the package and undoes the brown paper. It is a black book, not new; the gold lettering, all worn away, says: "All Of Them Witches by J.R. Hanslet.” On the flyleaf is HUTCH’S signature, with the inscription: "Torquay, 1934.” Rosemary goes into the living room, riffling its pages. There are occasional photographs of respectable-looking Victorians, several underlining's and marginal checkmarks. One underlined phrase is: "the fungus they call 'Devil's Pepper’." Rosemary sits in one of the window bays and looks at the table of contents. The name: "Adrian Marcato" is the title of Chapter Four. Other chapter titles: "Prudence Duvernoy: Stanley Rolfe; Aleister Crowley; Margaret Wick; Witch Practices; Witchcraft and Satanism."
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: Rosemary turns back to the chapter: Adrian Marcato. "Born in Glasgow in 18^6, he was brought soon after to New York (underlined)...he was attacked by a mob out­ side the Bramford...." Outside. Not in the lobby.
  EXPRESSION: Reading, then clarifying
- CHARACTER: Narrator
  LINE: There is a standing portrait of Marcato, a hypnotic­ eyed black-bearded man. Rosema
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue reading"
  TARGET: end
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Guy and Rosemary’s Apartment - Interior
MOOD: Intense, Investigative
CHARACTERS: Narrator, Rosemary
BACKGROUND_IMAGE: rosemarys_apartment.png
BACKGROUND_EDIT: "Dimly lit room, book open on lap, Scrabble set on the floor"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Rosemary turns the page.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: There is a less formal photograph of him sitting at a Paris café. The caption reads: "Paris, 1899. Adrian Marcato, his wife and son, Steven." The name "Steven" is underlined.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Rosemary flips through the book; pauses for other underlining. A few pages later: "the universally-held belief in the power of fresh blood."
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: But there are no witches. Not really.
  EXPRESSION: Thoughtful
- CHARACTER: Narrator
  LINE: She closes the book, looks at the title.
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: The name is an anagram.
  EXPRESSION: Realization
- CHARACTER: Narrator
  LINE: Holding the book on her lap, she looks at the ceiling; then at the book again. Suddenly, she stands up and goes to get the Scrabble Set. She puts the book, an open board and the box on the floor. Kneeling in front of them, she picks up the letters to spell: "All Of Them Witches". She jumbles the letters, mixes them round and starts building a new sentence; it comes out: "Comes with the fall". Then: "How is hell fact me". She looks at the one letter left in her hand for a moment. Then, mixes the letters again and forms: "Elf shot lame witch" and "Tell me which fatso".
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: That really makes sense.
  EXPRESSION: Sarcastic
- CHARACTER: Narrator
  LINE: She puts the letters back in the box, the box on the board, the book on top of the box, and everything on the window seat. She steps back and looks at them.
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: Poor Hutch.
  EXPRESSION: Sad
- CHARACTER: Narrator
  LINE: A new idea comes. Slowly, she picks up the book, looks at the edge, finds the place where the corner of a page had been folded. She bends the corner again as it was, then straightens it. Once more, she looks at the Paris photograph and the name "Steven" underlined. Suddenly, she grabs the box and empties it on the floor. Very fast, she forms the name "Steven Marcato" with the wooden squares; Index finger, "R” out, then "O". With two fingers "M" and "A". With index, "N": "ROMAN". With her whole hand, she moves "STEVE" to the right, after "ROMAN". Again her index finger pulls down "T" at the end of it and "GA" in front: "ROMAN CASTEVET".
  EXPRESSION: Determined

::SCENE::
LOCATION: Guy and Rosemary’s Apartment - Kitchen (Dusk)
MOOD: Suspenseful, Domestic
CHARACTERS: Narrator, Rosemary, Guy
BACKGROUND_IMAGE: rosemarys_apartment_kitchen.png
BACKGROUND_EDIT: "Dusk, kitchen interior, Rosemary eating tuna fish"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The front door unlocks and pushes against the chain. Rosemary is sitting in the kitchen eating tuna fish; the open book in front of her. She lifts her head, listening. The doorbell rings and Rosemary goes to see who it is. It’s Guy. She lets him in. He has a bunch of daisies and a box from Bronzini.
  EXPRESSION: null
- CHARACTER: Guy
  LINE: What’s with the chain?
  EXPRESSION: Puzzled
- CHARACTER: Narrator
  LINE: Rosemary closes the door and rechains it.
  EXPRESSION: null
- CHARACTER: Guy
  LINE: What’s the matter?
  EXPRESSION: Concerned
- CHARACTER: Narrator
  LINE: He kisses her and gives her the daisies.
  EXPRESSION: null
- CHARACTER: Guy
  LINE: Are you all right?
  EXPRESSION: Concerned
- CHARACTER: Rosemary
  LINE: Yes.
  EXPRESSION: Vague
- CHARACTER: Narrator
  LINE: She goes into the kitchen.
  EXPRESSION: null
- CHARACTER: Guy
  LINE: How was the funeral?
  EXPRESSION: Casual
- CHARACTER: Rosemary
  LINE: O.K.
  EXPRESSION: Dismissive
- CHARACTER: Narrator
  LINE: Rosemary puts the daisies into a blue pitcher. Guy calls out from the Bedroom.
  EXPRESSION: null
- CHARACTER: Guy (O.S.)
  LINE: I got the shirt that was in "The New Yorker”.
  EXPRESSION: Proud
- CHARACTER: Narrator
  LINE: Rosemary takes the flowers into the living room. Guy comes in and shows her the shirt.
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: That's nice. Do you know who Roman really is?
  EXPRESSION: Direct
- CHARACTER: Narrator
  LINE: Guy looks at her, blinks and frowns.
  EXPRESSION: Confused
- CHARACTER: Guy
  LINE: What do you mean, honey?
  EXPRESSION: Confused
- CHARACTER: Rosemary
  LINE: He's Adrian Marcato's son.
  EXPRESSION: Assertive
- CHARACTER: Guy
  LINE: What?
  EXPRESSION: Shocked
- CHARACTER: Rosemary
  LINE: I'll show you something. 'Roman Castevet' is 'Steven Marcato' rearranged.
  EXPRESSION: Explanatory
- CHARACTER: Narrator
  LINE: They enter the kitchen. Rosemary picks up the book and gives it to Guy.
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: It's from Hutch.
  EXPRESSION: Resigned
- CHARACTER: Narrator
  LINE: Guy looks at the book, then puts his shirt aside, and starts leafing through it. Rosemary puts her finger on the Parisian photograph.
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: Here he is when he was thirteen. See the eyes?
  EXPRESSION: Pointing
- CHARACTER: Guy
  LINE: A coincidence.
  EXPRESSION: Dismissive
- CHARACTER: Narrator
  LINE: She turns the page and searches for a second, Guy still holding the book.
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: Soon after that, in August 1886, his son Steven was born. 1886. Got it? Makes him seventy-nine now. No coincidence.
  EXPRESSION: Emphatic
- CHARACTER: Guy
  LINE: No, I guess not. He’s Steven Marcato, all right. Poor old geezer. With a crazy father like that no wonder he switched his name around.
  EXPRESSION: Accepting
- CHARACTER: Narrator
  LINE: Rosemary looks at Guy uncertainly.
  EXPRESSION: Uncertain
- CHARACTER: Rosemary
  LINE: You don’t think he’s - the same?
  EXPRESSION: Hesitant
- CHARACTER: Guy
  LINE: What do you mean? A witch?
  EXPRESSION: Amused
- CHARACTER: Narrator
  LINE: Rosemary nods.
  EXPRESSION: null
- CHARACTER: Guy
  LINE: Ro, are you kidding?
  EXPRESSION: Laughing
- CHARACTER: Narrator
  LINE: He laughs and gives the book back to her.
  EXPRESSION: null
- CHARACTER: Guy
  LINE: Ah Ro, honey.
  EXPRESSION: Patronizing
- CHARACTER: Narrator
  LINE: He picks up his shirt and goes to the Living Room.
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: His father was a martyr to it. Do you know how he died?
  EXPRESSION: Insistent
- CHARACTER: Guy
  LINE: Honey, it’s 1966.
  EXPRESSION: Exasperated
- CHARACTER: Narrator
  LINE: Rosemary holds out the book towards him.
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: This was published in 1933; there were covens in Europe - that’s what they’re called, the the - congregation; covens - in Europe, in America, in Australia. They’ve got one right here — all that bunch; those parties with the flute and the chanting, those are sabbaths or esbats or whatever-they-are!
  EXPRESSION: Agitated
- CHARACTER: Guy
  LINE: Honey, don’t get excited! Let's -
  EXPRESSION: Calming
- CHARACTER: Rosemary
  LINE: Read what they do, Guy.
  EXPRESSION: Demanding
- CHARACTER: Narrator
  LINE: She opens the book at him and jabs a page with her forefinger.
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: They use blood in their rituals, and the blood that has the most power is a baby’s blood. And they use more than the blood, they use the flesh too.
  EXPRESSION: Horrified
- CHARACTER: Guy
  LINE: For God's sake, Rosemary!
  EXPRESSION: Shocked
- CHARACTER: Rosemary
  LINE: They’re not setting foot in this apartment ever again. And they’re not coming within fifty feet of the baby.
  EXPRESSION: Determined
- CHARACTER: Guy
  LINE: Honey, they’re old people and they have a bunch of old friends, and Dr. Shand happens to play the recorder.
  EXPRESSION: Defeated
- CHARACTER: Narrator
  LINE: She goes to the window where the Scrabble set lay, holding the book in both hands, trembling.
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: I’m not going to take any chances with the baby's safety. We're going to sub-let and move out.
  EXPRESSION: Resolute
- CHARACTER: Guy
  LINE: We are not.
  EXPRESSION: Firm
- CHARACTER: Narrator
  LINE: Turning to him
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: Oh yes we are.
  EXPRESSION: Adamant
- CHARACTER: Narrator
  LINE: Guy picks up his new shirt and goes out and into the Bedroom.
  EXPRESSION: null
- CHARACTER: Guy
  LINE: We’ll talk about it later.
  EXPRESSION: Postponing
- CHARACTER: Narrator
  LINE: Rosemary sits down next to the Scrabble set. She closes it and, after a moment, opens the book and begins to read the final chapter; "Witchcraft and Satanism". Guy comes back in without the shirt.
  EXPRESSION: null
- CHARACTER: Guy
  LINE: I don’t think you ought to read any more of that.
  EXPRESSION: Concerned
- CHARACTER: Rosemary
  LINE: Just this last chapter.
  EXPRESSION: Stubborn
- CHARACTER: Guy
  LINE: Not today, honey.
  EXPRESSION: Gentle
- CHARACTER: Narrator
  LINE: He puts his hand out and waits for her to give him the book.
  EXPRESSION: null
- CHARACTER: Guy
  LINE: You’re shaking. Come on, give it to me. You’ll read it tomorrow.
  EXPRESSION: Firm
- CHARACTER: Rosemary
  LINE: Guy -
  EXPRESSION: Pleading
- CHARACTER: Guy
  LINE: No, I mean it. Come on, give it to me.
  EXPRESSION: Insistent
- CHARACTER: Narrator
  LINE: Ohh.
  EXPRESSION: Resigned
- CHARACTER: Narrator
  LINE: She gives it to him. He goes over to the bookshelves, stretches up, and puts it as high as he can reach, across the tops of the two Kinsey Reports.
  EXPRESSION: null

::SCENE::
LOCATION: Dr. Sapirstein’s Office - Interior (Day) - June 9, 1966
MOOD: Clinical, Revealing
CHARACTERS: Narrator, Rosemary, Dr. Sapirstein
BACKGROUND_IMAGE: dr_sapirsteins_office.png
BACKGROUND_EDIT: "Daytime, doctor's office interior"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Rosemary is sitting in front of Dr. Sapirstein.
  EXPRESSION: null
- CHARACTER: Dr. Sapirstein
  LINE: Fantastic, Absolutely fantastic. What did you say the name was, 'Machado'?
  EXPRESSION: Amazed
- CHARACTER: Rosemary
  LINE: Marcato.
  EXPRESSION: Correcting
- CHARACTER: Dr. Sapirstein
  LINE: Fantastic. I think he told me once that his father was a coffee importer.
  EXPRESSION: Thoughtful
- CHARACTER: Rosemary
  LINE: He told Guy that he was a producer.
  EXPRESSION: Neutral
- CHARACTER: Dr. Sapirstein
  LINE: I understand how disturbed you must be to have him for a close neighbor.
  EXPRESSION: Empathetic
- CHARACTER: Rosemary
  LINE: I don’t want anything more to do with him or Minnie. I don’t want to take even the slightest chance where the baby’s safety is concerned.
  EXPRESSION: Determined
- CHARACTER: Dr. Sapirstein
  LINE: Absolutely. Any mother would feel the same way.
  EXPRESSION: Affirming
- CHARACTER: Narrator
  LINE: Leaning forward
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: Is there any chance at all that Minnie put something harmful in the drink or in those little cakes?
  EXPRESSION: Anxious
- CHARACTER: Dr. Sapirstein
  LINE: No, Rosemary. I would have seen evidence of it long ago.
  EXPRESSION: Reassuring
- CHARACTER: Rosemary
  LINE: I won’t take anything else from her.
  EXPRESSION: Firm
- CHARACTER: Dr. Sapirstein
  LINE: You won’t have to. I can give you some pills that will be adequate in these last few weeks. In a way this may be the answer to Minnie and Roman’s problem too.
  EXPRESSION: Professional
- CHARACTER: Rosemary
  LINE: What do you mean?
  EXPRESSION: Curious
- CHARACTER: Dr. Sapirstein
  LINE: Roman is very ill. In fact - confidentially - he has no more than a month or two left to him.
  EXPRESSION: Confidential
- CHARACTER: Rosemary
  LINE: I had no idea--
  EXPRESSION: Surprised
- CHARACTER: Dr. Sapirstein
  LINE: He wanted to pay a last visit to a few of his favorite cities, but they didn’t want to offend you by leaving before the baby's birth.
  EXPRESSION: Explanatory
- CHARACTER: Rosemary
  LINE: I’m sorry to hear that Roman isn’t well.
  EXPRESSION: Sympathetic
- CHARACTER: Dr. Sapirstein
  LINE: He would be extremely embarrassed if he knew what you found out. Suppose we do this: I’ll tell them to leave on Sunday. I’ll say I spoke to you, and you understand.
  EXPRESSION: Strategic
- CHARACTER: Rosemary
  LINE: Are you sure they’ll leave on Sunday?
  EXPRESSION: Skeptical
- CHARACTER: Dr. Sapirstein
  LINE: I’ll see to it.
  EXPRESSION: Assured
- CHARACTER: Rosemary
  LINE: All right. I’ll go along, but only until Sunday.
  EXPRESSION: Conditional

::SCENE::
LOCATION: Sidewalk Outside Bramford - Exterior (Day) - June 12, 1966
MOOD: Bittersweet, Formal
CHARACTERS: Narrator, Mrs. Castevet, Mr. Castevet, Rosemary, Guy
BACKGROUND_IMAGE: sidewalk_bramford.png
BACKGROUND_EDIT: "Daytime, sidewalk in front of an apartment building, suitcases present"

::SCRIPT::
- CHARACTER: Narrator
  LINE: At the edge of the curb, the Doorman blows his whistle at the oncoming cars. A little behind him stands Mr. Castevet with the transistor radio over his shoulder, Mrs. Castevet in white dress and gloves, with a camera and a hatbox, Rosemary in her peppermint-striped smock, and Guy in blue jeans and a T-shirt. Two big suitcases are beside them on the sidewalk.
  EXPRESSION: null
- CHARACTER: Mrs. Castevet
  LINE: No matter where we are, our thoughts are going to be with you every minute, darling, till you’re all happy and thin again with your sweet little boy or girl lying safe in your arms.
  EXPRESSION: Affectionate
- CHARACTER: Narrator
  LINE: Rosemary kisses her cheek.
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: Thank you. Thank you for everything.
  EXPRESSION: Grateful
- CHARACTER: Mrs. Castevet
  LINE: You make Guy send us lots of pictures, you hear?
  EXPRESSION: Playful
- CHARACTER: Rosemary
  LINE: I will. I will.
  EXPRESSION: Affirming
- CHARACTER: Narrator
  LINE: Mrs. Castevet turns to Guy and Mr. Castevet takes Rosemary's hand.
  EXPRESSION: null
- CHARACTER: Mr. Castevet
  LINE: I won’t wish you luck, because you won't need it. You're going to have a happy, happy life.
  EXPRESSION: Optimistic
- CHARACTER: Narrator
  LINE: Rosemary kisses him.
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: Have a wonderful trip, and come back safely.
  EXPRESSION: Sincere
- CHARACTER: Mr. Castevet
  LINE: Smiling
  EXPRESSION: Gracious

::SCENE::
LOCATION: Airport / Street
MOOD: Sadness / Departure
CHARACTERS: Narrator, Rosemary, Guy, Mr. Castevet, Mrs. Castevet, Driver, Doorman
BACKGROUND_IMAGE: airport_departure.png
BACKGROUND_EDIT: "Taxi pulling away from an airport area"

::SCRIPT::
- CHARACTER: Narrator
  LINE: But I may stay on in Dubrovnik, or Pescara or maybe Mallorca. We shall see, we shall see...
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: Come back.
  EXPRESSION: Sincere
- CHARACTER: Narrator
  LINE: She kisses him again. A taxi comes. Guy and the Doorman stow the suitcases beside the Driver. Mrs. Castevet shoulders and grunts her way in, sweating under the arms of her white dress, Mr. Castevet folds himself in beside her.
  EXPRESSION: null
- CHARACTER: Mr. Castevet
  LINE: Kennedy Airport. TWA building.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: As the taxi pulls away there are more ’Goodbyes' through the open window. Rosemary and Guy stand waving at the taxi speeding away with hands ungloved and white-gloved waving from either side of it.
  EXPRESSION: null

::PATHS::
- CHOICE: "Go home"
  TARGET: apartment_living_room
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Guy and Rosemary's Apartment - Living Room
MOOD: Domestic / Busy
CHARACTERS: Narrator, Rosemary, Guy
BACKGROUND_IMAGE: apartment_living_room.png
BACKGROUND_EDIT: "Daytime, cluttered living room with books"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Rosemary is standing on a chair, looking over the Kinsey Reports, for Hutch's book. She takes the two thick volumes away and looks behind. With the books still in her hands, she glances around the room and calls toward the Bedroom.
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: Guy?
  EXPRESSION: Calling
- CHARACTER: Guy (O.S.)
  LINE: Yes.
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: Where is the book?
  EXPRESSION: Inquiring
- CHARACTER: Narrator
  LINE: Guy appears in the archway.
  EXPRESSION: null
- CHARACTER: Guy
  LINE: What was that, honey?
  EXPRESSION: Concerned
- CHARACTER: Rosemary
  LINE: I’m looking for my book.
  EXPRESSION: Annoyed
- CHARACTER: Narrator
  LINE: 130.
  EXPRESSION: null
- CHARACTER: Guy
  LINE: Oh, I put it in the garbage.
  EXPRESSION: Resigned
- CHARACTER: Rosemary
  LINE: What?
  EXPRESSION: Shocked
- CHARACTER: Guy
  LINE: I’m sorry, Ro. I didn't want you upsetting yourself any more.
  EXPRESSION: Apologetic
- CHARACTER: Rosemary
  LINE: Guy, Hutch gave me that book. He left it to me.
  EXPRESSION: Upset
- CHARACTER: Guy
  LINE: I didn't think about that part of it. I’m sorry.
  EXPRESSION: Apologetic
- CHARACTER: Rosemary
  LINE: That's a terrible thing to do.
  EXPRESSION: Angry
- CHARACTER: Guy
  LINE: I’m sorry. I wasn't thinking about Hutch.
  EXPRESSION: Remorseful

::PATHS::
- CHOICE: "Accept apology and move on"
  TARGET: stationery_counter_tiffany's
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Stationery Counter in Tiffany's
MOOD: Businesslike / Slight Unease
CHARACTERS: Narrator, Rosemary, Salesman, Alan Stone
BACKGROUND_IMAGE: tiffanys_stationery.png
BACKGROUND_EDIT: "Daytime, elegant stationery counter"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Rosemary stands holding a sample card of a birth announcement in her hand. There are other samples, more decorative and fancy, lying on the counter. The Salesman is writing on a pad.
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: Andrew John or Jennifer Melinda.
  EXPRESSION: Decisive
- CHARACTER: Salesman
  LINE: Well, the name is usually phoned later.
  EXPRESSION: Professional
- CHARACTER: Rosemary
  LINE: Oh yes, of course. With the date.
  EXPRESSION: Understanding
- CHARACTER: Salesman
  LINE: Envelopes?
  EXPRESSION: Professional
- CHARACTER: Rosemary
  LINE: Yes. Fifty.
  EXPRESSION: Decisive
- CHARACTER: Narrator
  LINE: Alan Stone leans over Rosemary’s shoulder,
  EXPRESSION: null
- CHARACTER: Alan
  LINE: When is my new client due?
  EXPRESSION: Playful
- CHARACTER: Rosemary
  LINE: Alan! How are you?
  EXPRESSION: Surprised
- CHARACTER: Alan
  LINE: Haven’t seen you for ages. Has Guy been hiding you?
  EXPRESSION: Inquisitive

::PATHS::
- CHOICE: "Continue with announcements"
  TARGET: ext_tiffanys
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Tiffany's - Exterior
MOOD: Bustling / Brief Encounter
CHARACTERS: Narrator, Alan, Rosemary
BACKGROUND_IMAGE: ext_tiffanys.png
BACKGROUND_EDIT: "Daytime, elegant facade of Tiffany's"

::SCRIPT::
- CHARACTER: Alan
  LINE: Tell Guy I’ll call him tonight. We’ve got an offer from Paramount.
  EXPRESSION: Excited
- CHARACTER: Rosemary
  LINE: Really? That’s wonderful!
  EXPRESSION: Delighted
- CHARACTER: Narrator
  LINE: He kisses her on the cheek, starts to leave.
  EXPRESSION: null
- CHARACTER: Alan
  LINE: Why don’t you drop in with Guy to see our new office?
  EXPRESSION: Friendly
- CHARACTER: Rosemary
  LINE: I will. I’ve never thanked you for the tickets to "The Fantasticks." I just loved it.
  EXPRESSION: Grateful
- CHARACTER: Alan
  LINE: "The Fantasticks"?
  EXPRESSION: Confused
- CHARACTER: Rosemary
  LINE: You gave Guy a pair of tickets. Oh, long ago.
  EXPRESSION: Certain
- CHARACTER: Alan
  LINE: I never had any tickets to "The Fantasticks"; you’re mistaken.
  EXPRESSION: Firm
- CHARACTER: Rosemary
  LINE: Last fall.
  EXPRESSION: Insistent
- CHARACTER: Alan
  LINE: I’ve got to rush. You’ll tell Guy I’ll call him, yes?
  EXPRESSION: Rushed

::PATHS::
- CHOICE: "Return to the apartment"
  TARGET: fifth_avenue
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Fifth Avenue
MOOD: Distracted / Foreboding
CHARACTERS: Narrator, Rosemary, Driver
BACKGROUND_IMAGE: fifth_avenue.png
BACKGROUND_EDIT: "Daytime, busy Fifth Avenue street"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Rosemary absent-mindedly walks along the Avenue. She crosses the street. A CAR HONKS and swerves to avoid her.
  EXPRESSION: null
- CHARACTER: Driver
  LINE: For God’s sake, lady!
  EXPRESSION: Irritated
- CHARACTER: Narrator
  LINE: Rosemary pulls the charm out from under her dress, undoes the chain and drops it in the sewer grating.
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: So much for tannis root.
  EXPRESSION: Determined

::PATHS::
- CHOICE: "Enter a bookshop"
  TARGET: bookshop
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Bookshop
MOOD: Discovery / Intrigue
CHARACTERS: Narrator, Rosemary, Bookseller
BACKGROUND_IMAGE: bookshop_interior.png
BACKGROUND_EDIT: "Daytime, interior of a bookshop"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Through the window we can see Rosemary talking to a Bookseller. He nods, turns, goes towards the shelves and with his finger, indicates a large section of it. Rosemary looks at him with surprise and also lifts her hand in a gesture which means "All of this"?
  EXPRESSION: null

::PATHS::
- CHOICE: "Leave with books"
  TARGET: taxi_interior
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Taxi - Interior
MOOD: Focused / Concerned
CHARACTERS: Narrator, Rosemary
BACKGROUND_IMAGE: taxi_interior.png
BACKGROUND_EDIT: "Daytime, inside of a taxi"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Rosemary has two books. She examines the covers and spine of each. She puts the small book on her lap, opens the big one: "United mental force of the whole coven, could blind, deafen, paralyze and ultimately kill the chosen victim."
  EXPRESSION: null

::PATHS::
- CHOICE: "Return to the apartment"
  TARGET: apartment_living_room_later
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Guy and Rosemary's Apartment - Living Room
MOOD: Studying / Quiet Intensity
CHARACTERS: Narrator, Rosemary
BACKGROUND_IMAGE: apartment_living_room_later.png
BACKGROUND_EDIT: "Daytime, living room, Rosemary reading"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Rosemary sitting in the Living Room reading the smaller book: "Spells can’t be cast without one of the victim’s belongings."
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: She stands up and starts walking around the room. She lifts the front of her dress and sniffs it.
  EXPRESSION: null

::PATHS::
- CHOICE: "Go to the bedroom"
  TARGET: bedroom
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Bedroom
MOOD: Preparation / Urgency
CHARACTERS: Narrator, Rosemary
BACKGROUND_IMAGE: bedroom.png
BACKGROUND_EDIT: "Daytime, bedroom"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Rosemary changes her dress, splashes herself all over with cologne.
  EXPRESSION: null

::PATHS::
- CHOICE: "Make a phone call"
  TARGET: phone_call_baumgart
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Phone Call - Donald Baumgart
MOOD: Tense / Deceptive
CHARACTERS: Narrator, Rosemary, Donald Baumgart (O.S.)
BACKGROUND_IMAGE: phone_call.png
BACKGROUND_EDIT: "Visual representation of a phone call"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The ringing tone before someone answers.
  EXPRESSION: null
- CHARACTER: Donald Baumgart (O.S.)
  LINE: Yeh?
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: Is this Donald Baumgart?
  EXPRESSION: Formal
- CHARACTER: Baumgart (O.S.)
  LINE: That’s right.
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: This is Rosemary Woodhouse. Guy Woodhouse’s wife.
  EXPRESSION: Polite
- CHARACTER: Baumgart (O.S.)
  LINE: Oh?
  EXPRESSION: Casual
- CHARACTER: Rosemary
  LINE: I wanted -
  EXPRESSION: Hesitant
- CHARACTER: Baumgart (O.S.)
  LINE: My God, you must be a happy little lady these days! Living in the Bram. Rows of uniformed lackeys -
  EXPRESSION: Sarcastic
- CHARACTER: Rosemary
  LINE: I wanted to know now you are; if there’s been any improvement.
  EXPRESSION: Concerned
- CHARACTER: Baumgart (O.S.)
  LINE: Why bless your heart, Guy Woodhouse’s wife. I’m splendid! I only broke six glasses today.
  EXPRESSION: Mocking
- CHARACTER: Rosemary
  LINE: Guy and I are both very unhappy that he got his break because of your misfortune.
  EXPRESSION: Sympathetic
- CHARACTER: Narrator
  LINE: Silence for a moment.
  EXPRESSION: null
- CHARACTER: Baumgart (O.S.)
  LINE: Oh, what the hell. That’s the way it goes.
  EXPRESSION: Indifferent
- CHARACTER: Rosemary
  LINE: I’m sorry I didn’t come along that day he came to visit you.
  EXPRESSION: Apologetic
- CHARACTER: Donald Baumgart (O.S.)
  LINE: Visit me? You mean the day we met for drinks?
  EXPRESSION: Clarifying
- CHARACTER: Rosemary
  LINE: Yes. That’s what I meant. By the way, he has something of yours, you know.
  EXPRESSION: Suspicious
- CHARACTER: Donald Baumgart (O.S.)
  LINE: What do you mean?
  EXPRESSION: Confused
- CHARACTER: Rosemary
  LINE: Don't you know?
  EXPRESSION: Challenging
- CHARACTER: Donald Baumgart (O.S.)
  LINE: No.
  EXPRESSION: Ignorant
- CHARACTER: Rosemary
  LINE: Didn’t you miss anything that day?
  EXPRESSION: Pointed
- CHARACTER: Donald Baumgart (O.S.)
  LINE: You don’t mean my tie, do you?
  EXPRESSION: Doubtful
- CHARACTER: Rosemary
  LINE: Yes.
  EXPRESSION: Certain
- CHARACTER: Donald Baumgart (O.S.)
  LINE: Well he’s got mine and I’ve got his. He can have it back; it doesn’t matter to me how what color tie I’m wearing.
  EXPRESSION: Dismissive
- CHARACTER: Rosemary
  LINE: I didn’t understand. I thought he had only borrowed it.
  EXPRESSION: Confused
- CHARACTER: Donald Baumgart (O.S.)
  LINE: No, it was a trade. Did you think he stole it?
  EXPRESSION: Amused
- CHARACTER: Rosemary
  LINE: I have to hang up now. I just wanted to know if there was any improvement.
  EXPRESSION: Abrupt
- CHARACTER: Donald Baumgart (O.S.)
  LINE: No, there isn't. It was nice of you to call.
  EXPRESSION: Polite
- CHARACTER: Rosemary
  LINE: 'By.
  EXPRESSION: Resigned
- CHARACTER: Narrator
  LINE: She hangs up; looks at the time (nine after four).
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: She takes a fold of bills from underneath Guy’s underwear in the drawer, puts them in her handbag. She puts in also the bottle of vitamin capsules and her address book. She takes the suitcase standing by the bedroom door and goes out. Halfway down the hallway, she turns and doubles back. She rides down in the service elevator with TWO DELIVERY BOYS.
  EXPRESSION: null

::PATHS::
- CHOICE: "Go to Dr. Sapirstein's"
  TARGET: dr_sapirstein_outer_office
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Dr. Sapirstein's Outer Office
MOOD: Anxious / Waiting
CHARACTERS: Narrator, Rosemary, Receptionist, Mrs. Byron, Pregnant Woman
BACKGROUND_IMAGE: dr_sapirstein_outer_office.png
BACKGROUND_EDIT: "Daytime, sterile waiting room"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Rosemary is standing with her suitcase in front of the Receptionist’s desk. Another woman (Mrs. Byron) sits reading. The Receptionist looks at the suitcase and smiles.
  EXPRESSION: null
- CHARACTER: Receptionist
  LINE: You aren’t in labor, are you?
  EXPRESSION: Inquiring
- CHARACTER: Rosemary
  LINE: No, but I have to see the doctor. It’s very important.
  EXPRESSION: Urgent
- CHARACTER: Narrator
  LINE: The Receptionist glances at her watch.
  EXPRESSION: null
- CHARACTER: Receptionist
  LINE: He has to leave at five and there’s Mrs. Byron... She looks across at Mrs. Byron and then smiles at Rosemary. I’m sure he’ll see you. Sit down.
  EXPRESSION: Reassuring
- CHARACTER: Rosemary
  LINE: Thank you.
  EXPRESSION: Grateful
- CHARACTER: Narrator
  LINE: Rosemary puts her suitcase by the nearest chair and sits down. She opens her handbag, takes out a tissue and wipes her pains and then her upper lip and temples. Her hands are shaking.
  EXPRESSION: null
- CHARACTER: Receptionist
  LINE: How is it out there?
  EXPRESSION: Casual
- CHARACTER: Rosemary
  LINE: Terrible. Ninety-four.
  EXPRESSION: Strained
- CHARACTER: Narrator
  LINE: The Receptionist makes a pained sound. A PREGNANT WOMAN (5-6 months) comes out from Dr. Sapirstein's office and nods at Rosemary. The Receptionist goes in to Dr. Sapirstein.
  EXPRESSION: null
- CHARACTER: Pregnant Woman
  LINE: You’re due any day now, aren’t you?
  EXPRESSION: Friendly
- CHARACTER: Rosemary
  LINE: Tuesday.
  EXPRESSION: Nervous
- CHARACTER: Pregnant Woman
  LINE: You’re smart to get it over with before August.
  EXPRESSION: Encouraging
- CHARACTER: Narrator
  LINE: The Receptionist comes out again.
  EXPRESSION: null
- CHARACTER: Receptionist
  LINE: Mrs. Byron? He’ll see you right after.
  EXPRESSION: Professional
- CHARACTER: Rosemary
  LINE: Thank you.
  EXPRESSION: Grateful
- CHARACTER: Narrator
  LINE: Mrs. Byron goes in to Dr. Sapirstein and closes the door. The Pregnant Woman by the desk confers with the Receptionist.
  EXPRESSION: null
- CHARACTER: Receptionist
  LINE: July 10th?
  EXPRESSION: Inquiring
- CHARACTER: Pregnant Woman
  LINE: What time?
  EXPRESSION: Questioning
- CHARACTER: Receptionist
  LINE: Four o’clock?
  EXPRESSION: Suggesting
- CHARACTER: Pregnant Woman
  LINE: O.K. Good-by. She turns and goes out, passing Rosemary, she smiles.
  EXPRESSION: null
- CHARACTER: Pregnant Woman
  LINE: Good luck.
  EXPRESSION: Warm
- CHARACTER: Narrator
  LINE: The Receptionist writes. Rosemary takes up a copy of "Time”, in red letters on a black background, it says: "Is God dead?"
  EXPRESSION: null
- CHARACTER: Receptionist
  LINE: That smells nice. What is it?
  EXPRESSION: Curious
- CHARACTER: Rosemary
  LINE: It’s called ’Detchema'.
  EXPRESSION: Proud
- CHARACTER: Receptionist
  LINE: It’s a big improvement on your regular, if you don’t mind my saying.
  EXPRESSION: Candid
- CHARACTER: Rosemary
  LINE: That wasn’t a cologne, it was a good luck charm. I threw it away.
  EXPRESSION: Defiant
- CHARACTER: Receptionist
  LINE: Good. Maybe the doctor will follow your example.
  EXPRESSION: Sarcastic
- CHARACTER: Narrator
  LINE: (After a silence)
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: Dr. Sapirstein?
  EXPRESSION: Anxious
- CHARACTER: Receptionist
  LINE: He has the after-shave. But it isn’t is it? I don’t think he has a good luck charm. Anyway, he has the same smell once in a while, whatever it is, and when he does - oh boy! Haven’t you ever noticed?
  EXPRESSION: Gossipy
- CHARACTER: Rosemary
  LINE: No.
  EXPRESSION: Distracted
- CHARACTER: Narrator
  LINE: Rosemary is standing up with her suitcase in her hand.
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: My husband is outside. I have to tell him something. I’ll be back in a minute.
  EXPRESSION: Determined
- CHARACTER: Narrator
  LINE: The Receptionist looks surprised as Rosemary backs and runs out.
  EXPRESSION: null

::PATHS::
- CHOICE: "Run outside"
  TARGET: ext_street
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Street
MOOD: Rushed / Determined
CHARACTERS: Narrator, Rosemary
BACKGROUND_IMAGE: street.png
BACKGROUND_EDIT: "Daytime, busy street"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Rosemary, suitcase in hand, walks fast.
  EXPRESSION: null

::PATHS::
- CHOICE: "Find a phone booth"
  TARGET: phone_booth
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Phone Booth
MOOD: Desperate / Sweating
CHARACTERS: Narrator, Rosemary, Woman's Voice (O.S.)
BACKGROUND_IMAGE: phone_booth.png
BACKGROUND_EDIT: "Daytime, interior of a phone booth"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Rosemary enters a glass phone booth, puts the suitcase on the floor, takes the address book out of her handbag, finds a number and, repeating it to herself, searches in her purse for a coin. She finds one, puts it in the slot and starts to dial. She is sweating.
  EXPRESSION: null
- CHARACTER: Woman's Voice (O.S.)
  LINE: Dr. Hill’s office.
  EXPRESSION: Professional
- CHARACTER: Rosemary
  LINE: Dr. Hill, please.
  EXPRESSION: Pleading
- CHARACTER: Narrator
  LINE: 138.
  EXPRESSION: null
- CHARACTER: Woman's Voice (O.S.)
  LINE: Thi
  EXPRESSION: null

::SCENE::
LOCATION: Unknown Location (Phone Booth)
MOOD: Anxious, Desperate
CHARACTERS: Narrator, Rosemary, Woman's Voice
BACKGROUND_IMAGE: phone_booth.png
BACKGROUND_EDIT: "Interior of a phone booth, day, Rosemary looks stressed"

::SCRIPT::
- CHARACTER: Narrator
  LINE: 's his answering service. Would you like to leave a message?
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: My name is Rosemary Woodhouse. Please ask him to call me back right away, 475-2498. It’s an emergency. I’m in a phone booth.
  EXPRESSION: Urgent
- CHARACTER: Woman's Voice
  LINE: All right.
  EXPRESSION: Neutral
- CHARACTER: Narrator
  LINE: With her foot, she cracks the door open for air. Rosemary replaces the receiver. Wiping her forehead, she speaks to herself.
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: Quickly, please, Dr. Hill. Call me.
  EXPRESSION: Pleading
- CHARACTER: Narrator
  LINE: She notices a Woman coming towards the telephone booth. She steps back, letting the door close and picks up the receiver, keeping a hidden finger on the hook. The Woman stands outside and waits.
  EXPRESSION: Cautious
- CHARACTER: Rosemary
  LINE: Oh, I didn't know that. Really? What else did he say? That’s wonderful. Did he say anything else?
  EXPRESSION: Deceptive
- CHARACTER: Narrator
  LINE: The TELEPHONE RINGS. Rosemary jumps and lets her finger off the hook. Sweat is pouring down her face.
  EXPRESSION: Startled, Panicked
- CHARACTER: Rosemary
  LINE: Dr. Hill?
  EXPRESSION: Hopeful
- CHARACTER: Woman's Voice (O.S.)
  LINE: Did I get the name right? Is it ’Rosemary Woodhouse’?
  EXPRESSION: Suspicious
- CHARACTER: Narrator
  LINE: The Woman outside the booth is walking away.
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: Yes!
  EXPRESSION: Eager
- CHARACTER: Woman's Voice (O.S.)
  LINE: Are you Dr. Hill’s patient?
  EXPRESSION: Questioning
- CHARACTER: Rosemary
  LINE: 139. No. Yes. I mean - I’ve seen him once. Please, please, he has to speak to me! It’s important! It’s - Please tell him to call me.
  EXPRESSION: Desperate
- CHARACTER: Woman's Voice (O.S.)
  LINE: All right.
  EXPRESSION: Indifferent
- CHARACTER: Narrator
  LINE: Rosemary looks around; nobody is waiting; she doesn’t replace the receiver though, but puts her finger on the hook. She opens the door again and with the hand holding the receiver, wipes the sweat from her forehead.
  EXPRESSION: Nervous
- CHARACTER: Rosemary
  LINE: All of them. All of them. All in it together. "All of them Witches”. Don’t you worry, Andy-or-Jenny, I’ll kill them before I let them touch you!
  EXPRESSION: Furious, Determined
- CHARACTER: Narrator
  LINE: The TELEPHONE RINGS. She jumps her finger from the hook, stopping the ring in the middle. She steps forward and the door closes.
  EXPRESSION: Startled, Urgent
- CHARACTER: Rosemary
  LINE: Yes?
  EXPRESSION: Anxious
- CHARACTER: Dr. Hill (O.S.)
  LINE: Mrs. Woodhouse?
  EXPRESSION: Questioning
- CHARACTER: Rosemary
  LINE: Thank you. Thank you for calling me.
  EXPRESSION: Relieved
- CHARACTER: Dr. Hill (O.S.)
  LINE: I thought you were in California.
  EXPRESSION: Confused
- CHARACTER: Rosemary
  LINE: No. I went to another doctor, and he isn't good, Dr. Hill; he's been lying to me and giving me unusual kinds of - drinks and capsules. The baby is due on Tuesday - remember, you told me, June twenty-eight? - and I want you to deliver it.
  EXPRESSION: Urgent, Desperate
- CHARACTER: Dr. Hill (O.S.)
  LINE: Mrs. Woodhouse -
  EXPRESSION: Hesitant
- CHARACTER: Rosemary
  LINE: Please, let me talk to you. Let me come and explain what’s been going on. I can’t stay too long here. They will be looking for me. There is a plot. I know that sounds crazy, Doctor, and you’re probably thinking, 'My God, this poor girl has completely flipped,' but I haven’t flipped, Doctor, I swear by all the saints I haven't. There are plots against people, aren't there?
  EXPRESSION: Pleading, Frantic
- CHARACTER: Dr. Hill (O.S.)
  LINE: Yes, I suppose there are.
  EXPRESSION: Neutral
- CHARACTER: Rosemary
  LINE: There's one against me and my baby.
  EXPRESSION: Terrified
- CHARACTER: Dr. Hill (O.S.)
  LINE: Come to my office tomorrow after -
  EXPRESSION: Firm
- CHARACTER: Rosemary
  LINE: Now. Right now.
  EXPRESSION: Demanding
- CHARACTER: Dr. Hill (O.S.)
  LINE: Mrs. Woodhouse, I’m not at my office now, I’m home. I’ve been up since yesterday morning and -
  EXPRESSION: Exhausted
- CHARACTER: Rosemary
  LINE: I beg you, I beg you.
  EXPRESSION: Pleading
- CHARACTER: Narrator
  LINE: (Silence) I can’t stay here.
  EXPRESSION: Desperate
- CHARACTER: Dr. Hill (O.S.)
  LINE: My office at eight o'clock.
  EXPRESSION: Resigned
- CHARACTER: Rosemary
  LINE: Yes. Thank you.
  EXPRESSION: Relieved
- CHARACTER: Dr. Hill (O.S.)
  LINE: All right.
  EXPRESSION: Neutral
- CHARACTER: Rosemary
  LINE: Dr. Hill?
  EXPRESSION: Concerned
- CHARACTER: Dr. Hill (O.S.)
  LINE: Yes?
  EXPRESSION: Questioning
- CHARACTER: Rosemary
  LINE: My husband may call you and ask -
  EXPRESSION: Anxious
- CHARACTER: Dr. Hill (O.S.)
  LINE: I'm not going to speak to anyone. I'm going to take a nap.
  EXPRESSION: Firm
- CHARACTER: Rosemary
  LINE: Thank you, Dr. Hill.
  EXPRESSION: Grateful
- CHARACTER: Narrator
  LINE: She replaces the receiver, breathing deeply in relief. She notices that somebody is standing outside, back against the door. It is a MAN looking like Dr. Saperstein. Rosemary, who has been bending to pick up her suitcase, is unable to move. She remains in this position for several seconds until the MAN turns and looks at her. She straightens up, opens the door, and suitcase in hand goes quickly away.
  EXPRESSION: Relieved, then Shocked, then Panicked

::PATHS::
- CHOICE: "Leave the phone booth"
  TARGET: taxi
  STATE_CHANGE: fear = +1
  CONDITION: null

::SCENE::
LOCATION: Taxi
MOOD: Anxious
CHARACTERS: Narrator, Rosemary, Driver
BACKGROUND_IMAGE: taxi_interior.png
BACKGROUND_EDIT: "Interior of a taxi, day, Rosemary with her suitcase"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Rosemary is sitting with her suitcase on her knees. The taxi stops somewhere on West Seventy-second. The driver stops the meter and Rosemary gives him money. She looks anxiously around.
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: Driver, could you wait please, and watch until I’m inside the door?
  EXPRESSION: Anxious
- CHARACTER: Narrator
  LINE: The Driver, a little surprised, hands Rosemary the change.
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: Keep it, please.
  EXPRESSION: Generous, Stressed

::PATHS::
- CHOICE: "Exit the taxi and go to the office"
  TARGET: office_doorway
  STATE_CHANGE: fear = +1
  CONDITION: null

::SCENE::
LOCATION: The Doorway of Dr. Hill’s Office
MOOD: Apprehensive
CHARACTERS: Narrator, Rosemary, Dr. Hill
BACKGROUND_IMAGE: dr_hills_office_exterior.png
BACKGROUND_EDIT: "Exterior of Dr. Hill's office, day"

::SCRIPT::
- CHARACTER: Narrator
  LINE: She gets out, shrinks, trying to be as small as possible, and hurries to the door. Dr. Hill opens it. He wears a blue and yellow plaid sport shirt. He had grown a moustache, blond and hardly noticeable. He shows Rosemary inside.
  EXPRESSION: null

::PATHS::
- CHOICE: "Enter Dr. Hill's office"
  TARGET: dr_hills_office_consulting_room
  STATE_CHANGE: hope = +1
  CONDITION: null

::SCENE::
LOCATION: Dr. Hill’s Office - Consulting Room
MOOD: Intense, Paranoia
CHARACTERS: Narrator, Rosemary, Dr. Hill
BACKGROUND_IMAGE: dr_hills_office_interior.png
BACKGROUND_EDIT: "Interior of Dr. Hill's office, consulting room, day"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Rosemary sits in an armchair. Dr. Hill sits beside the desk.
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: You see, he lied to you. He said we were going to Hollywood. The worst thing of all, he is involved with them as well. He sleeps in pajamas now. He never used to before. He’s probably hiding a mark. You know, they give you a mark when you join. All sorts of rituals. They hold Sabbaths there. You could hear them singing through the wall. Guy, my husband, said it was Dr. Shand, one of these people, playing a recorder. Now, how did he know it was Dr. Shand unless he was there with them? They’re very clever. They planned everything from the beginning. I suppose they made some sort of a deal with Guy. They gave him success and he promised them a baby. To use in their rituals. I know, this sounds crazy, but I’ve got hooks here. I’ll show them to you.
  EXPRESSION: Agitated, Confident
- CHARACTER: Narrator
  LINE: Rosemary opens her suitcase, takes the two books out of it, finds a place in the large one and hands it to Dr. Hill.
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: There was another actor like him, Donald Baumgart, and they cast a spell on him to make him blind, so Guy could get his part. Look. Here!
  EXPRESSION: Earnest
- CHARACTER: Narrator
  LINE: Dr. Hill looks at the place. He puts the book on the desk and holding his hand on the page, reads it. While Rosemary is speaking, Dr. Hill examines the cover and starts flicking through the leaves.
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: I had a friend, Edward Hutchins. Maybe you heard of him? A writer. He wrote for boys. Anyway, he was a friend of mine since I first came to New York.
  EXPRESSION: Nostalgic, then Anxious
- CHARACTER: Dr. Hill
  LINE: May I keep it?
  EXPRESSION: Polite
- CHARACTER: Rosemary
  LINE: Yes, please.
  EXPRESSION: Willing
- CHARACTER: Narrator
  LINE: Rosemary gives him the smaller book also. Dr. Hill puts it on top of the larger one at the side of his desk.
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: Once, Mr. Hutchins came to visit me. It was the time I had this pain. I was suffering so much, Doctor, you can't imagine how much I was suffering. And they wouldn't help me. Nobody would. They were giving me a drink, with tannis root. Also a witch stuff. Tannis root. So, Hutch came and immediately saw something was wrong. He knew about witches, you see. Suddenly Guy rushed in with his make-up still on, which he never did. They must have called him to get home and steal one of Hutch's belongings. So he did. Took his glove, and they cast a spell on him too. Put him in a coma. Three months later he died. Maybe all this is coincidence but one thing is certain. They have a coven and they want my baby.
  EXPRESSION: Emotional, Terrified
- CHARACTER: Dr. Hill
  LINE: It certainly seems that way.
  EXPRESSION: Neutral, possibly humoring
- CHARACTER: Narrator
  LINE: Rosemary shuts her eyes and almost cries from happiness, that Dr. Hill believes her. She opens her eyes and looks at him, calm and composed. Dr. Hill had moved behind the desk and is writing. Rosemary, who was clutching the chair arms, relaxes her hands and dries her palm on her dress.
  EXPRESSION: Hopeful, Relieved
- CHARACTER: Rosemary
  LINE: I was afraid you wouldn’t believe me.
  EXPRESSION: Vulnerable
- CHARACTER: Dr. Hill
  LINE: I don’t believe in witchcraft but there are plenty of maniacs and crazy people in this city. The doctor’s name is Shand, you say.
  EXPRESSION: Pragmatic, Skeptical
- CHARACTER: Rosemary
  LINE: No, Dr. Shand is one of the group. The doctor is Dr. Sapirstein.
  EXPRESSION: Correcting, Uneasy
- CHARACTER: Dr. Hill
  LINE: Abraham Sapirstein?
  EXPRESSION: Questioning
- CHARACTER: Rosemary
  LINE: Yes. Do you know him?
  EXPRESSION: Worried
- CHARACTER: Dr. Hill
  LINE: I met him once or twice.
  EXPRESSION: Nonchalant
- CHARACTER: Rosemary
  LINE: Looking at him, you would never think he -
  EXPRESSION: Skeptical
- CHARACTER: Dr. Hill
  LINE: Never in a million years.
  EXPRESSION: Agreement
- CHARACTER: Narrator
  LINE: (Putting down his pen) Would you like to go into Mount Sinai right now, this evening?
  EXPRESSION: Offering
- CHARACTER: Rosemary
  LINE: I would love to. Is it possible?
  EXPRESSION: Joyful, Hopeful
- CHARACTER: Dr. Hill
  LINE: Difficult but we’ll try. I want you to lie down and get some rest.
  EXPRESSION: Reassuring
- CHARACTER: Narrator
  LINE: He rises and goes to the open door of his examining room, reaches inside and switches on an ice-blue fluorescent light.
  EXPRESSION: null
- CHARACTER: Dr. Hill
  LINE: I’ll see what I can do, then I’ll check you over.
  EXPRESSION: Professional
- CHARACTER: Narrator
  LINE: Rosemary hefts herself up and goes, clutching her handbag, into the examining room.
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: Anything you’ve got. Even a broom closet.
  EXPRESSION: Desperate
- CHARACTER: Dr. Hill
  LINE: I hope we can do better than that.
  EXPRESSION: Confident
- CHARACTER: Narrator
  LINE: He comes into the examining room after her. There is a day bed at the far end of the room covered in blue, and a chair. There are blue curtains on the window. Dr. Hill switches on the air conditioner in the window. It is a noisy one.
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: Shall I undress?
  EXPRESSION: Shy
- CHARACTER: Dr. Hill
  LINE: No, not yet. It'll take some half-hour on the telephone. Just lie down and rest.
  EXPRESSION: Direct
- CHARACTER: Narrator
  LINE: He switches off the light, goes out and closes the door. There is a nice glow of evening light from behind the curtains. Rosemary puts her handbag on a chair, and sits down heavily on the day bed.
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: God bless Dr. Hill.
  EXPRESSION: Grateful
- CHARACTER: Narrator
  LINE: She shakes off her sandals and lies back gratefully.
  EXPRESSION: Relaxed
- CHARACTER: Rosemary
  LINE: Everything's okay now, Andy-or-Jenny. We’re going to be in a nice clean bed with no Visitors and -
  EXPRESSION: Content
- CHARACTER: Narrator
  LINE: She sits up suddenly, opens her handbag, takes out the fold of bills and counts them. There is some more money in her purse. She takes it out and adds it to the fold of bills. She takes the capsules out
  EXPRESSION: Alert, Preoccupied

::PATHS::
- CHOICE: "Count money and prepare for examination"
  TARGET: end_of_excerpt
  STATE_CHANGE: fear = -1, hope = +1
  CONDITION: null

::SCENE::
LOCATION: Examining Room
MOOD: Despair
CHARACTERS: Rosemary, Dr. Hill, Guy, Dr. Sapirstein
BACKGROUND_IMAGE: examining_room.png
BACKGROUND_EDIT: "Dusk, dimly lit examining room"

::SCRIPT::
- CHARACTER: Narrator
  LINE: of her handbag, puts the money back in, closes it and puts it on the chair. She looks at the bottle of capsules in her hand.
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: Monsters!
  EXPRESSION: Angry
- CHARACTER: Rosemary
  LINE: She puts the bottle on the chair beside the handbag, lies back again on the day bed.
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: Unspeakable. Unspeakable.
  EXPRESSION: Distraught

::SCENE::
LOCATION: Dream Sequence - Beverly Hills House Exterior
MOOD: Eerie Calm
CHARACTERS: Rosemary, Man, Elise Dunstan, Family, Friends
BACKGROUND_IMAGE: dream_sequence_beverly_hills.png
BACKGROUND_EDIT: "Daytime, contemporary house in Beverly Hills"

::SCRIPT::
- CHARACTER: Narrator
  LINE: In front of a large contemporary house in Beverly Hills, Rosemary rocks a bassinet. There are ten to twelve persons around her family and some of her friends.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Looking over shoulders, each one tries to see into the bassinet. Rosemary picks up the baby.
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: He’ll be four months in two days.
  EXPRESSION: Affectionate
- CHARACTER: Man
  LINE: Already talking?
  EXPRESSION: Curious
- CHARACTER: Narrator
  LINE: Rosemary cradles the baby in her arms. Elise Dunstan bends over it, making cooing noises.
  EXPRESSION: null
- CHARACTER: Elise Dunstan
  LINE: Andy, Andy!
  EXPRESSION: Cooing

::SCENE::
LOCATION: Examining Room
MOOD: Manipulation and Control
CHARACTERS: Rosemary, Dr. Hill, Guy, Dr. Sapirstein
BACKGROUND_IMAGE: examining_room_dusk.png
BACKGROUND_EDIT: "Dusk, examining room with fluorescent light"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The door opens. Dr. Hill looks in. Rosemary, lying on the day bed, looks at him.
  EXPRESSION: null
- CHARACTER: Dr. Hill
  LINE: Dr. Hill switches on the fluorescent light. Rosemary shields her eyes with her hand and smiles at him.
  EXPRESSION: Neutral
- CHARACTER: Rosemary
  LINE: I’ve been sleeping.
  EXPRESSION: Sleepy
- CHARACTER: Narrator
  LINE: Dr. Hill withdraws, pushing the door wide open. Guy and Dr. Sapirstein come in. Rosemary sits up, lowering her hand from her eyes. They come and stand close to her. Guy's face is stony and blank. He looks at the walls, not at her.
  EXPRESSION: null
- CHARACTER: Dr. Sapirstein
  LINE: Come with us quietly, Rosemary. Don’t argue or make a scene, because if you say anything more about witches or witchcraft we’re going to be forced to take you to a mental hospital. You don’t want that, do you? So put your shoes on.
  EXPRESSION: Threatening
- CHARACTER: Narrator
  LINE: Guy finally looks at her.
  EXPRESSION: null
- CHARACTER: Guy
  LINE: We’re just going to take you home. No one’s going to hurt you.
  EXPRESSION: Reassuring
- CHARACTER: Dr. Sapirstein
  LINE: Or the baby. Put your shoes on.
  EXPRESSION: Assertive
- CHARACTER: Narrator
  LINE: He picks up the bottle of capsules, looks at it, and puts it in his pocket. Rosemary puts her sandals on and Dr. Sapirstein gives her the handbag. They go out, Dr. Sapirstein holding her arm, Guy touching her other elbow. Dr. Hill gives Rosemary’s suitcase to Guy.
  EXPRESSION: null
- CHARACTER: Dr. Sapirstein
  LINE: She’s fine now. We’re going to go home and rest.
  EXPRESSION: Dismissive
- CHARACTER: Narrator
  LINE: Dr. Hill smiles at Rosemary.
  EXPRESSION: null
- CHARACTER: Dr. Hill
  LINE: That’s all it takes.
  EXPRESSION: Condescending
- CHARACTER: Narrator
  LINE: Rosemary looks at Dr. Hill and says nothing.
  EXPRESSION: null
- CHARACTER: Dr. Sapirstein
  LINE: Thank you for your trouble, Doctor.
  EXPRESSION: Polite
- CHARACTER: Guy
  LINE: It’s a shame you had to come in here and -
  EXPRESSION: Apologetic
- CHARACTER: Dr. Hill
  LINE: I’m glad I could be of help, sir.
  EXPRESSION: Subservient

::SCENE::
LOCATION: Street Outside Dr. Hill’s Office
MOOD: Foreboding Silence
CHARACTERS: Rosemary, Guy, Dr. Sapirstein, Mr. Gilmore
BACKGROUND_IMAGE: street_dusk.png
BACKGROUND_EDIT: "Dusk, street outside a medical office"

::SCRIPT::
- CHARACTER: Narrator
  LINE: There is a car waiting with Mr. Gilmore at the wheel. Rosemary sits in the back between Guy and Dr. Sapirstein. The suitcase is put on the front seat.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Nobody says anything; they drive in silence.
  EXPRESSION: null

::SCENE::
LOCATION: Bramford Lobby
MOOD: Deception and Escape Attempt
CHARACTERS: Guy, Rosemary, Dr. Sapirstein, Diego
BACKGROUND_IMAGE: bramford_lobby_night.png
BACKGROUND_EDIT: "Night, interior of a building lobby"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Guy, Rosemary and Dr. Sapirstein walk across the lobby towards the elevator. Diego smiles at Rosemary from the open door of the elevator.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: As they walk Rosemary sneaks open her handbag at her side, hooks a finger through the key ring and holding onto the keys, spills the handbag onto the floor near the elevator.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: There are coins, rolling lipstick, bills fluttering all over the floor. Rosemary looks down stupidly.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Guy and Dr. Sapirstein start to pick the contents up. Diego comes out to help them, making tongue-teeth sounds of concern.
  EXPRESSION: null

::SCENE::
LOCATION: Elevator
MOOD: Desperate Escape
CHARACTERS: Rosemary, Diego (O.S.), Guy, Dr. Sapirstein
BACKGROUND_IMAGE: elevator_night.png
BACKGROUND_EDIT: "Night, interior of an elevator"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Rosemary backs into the elevator to get out of the way. Watching them, she toes the big round floor-button. The rolling door rolls. She pulls closed the inner gate.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Diego grabs for the door but saves his fingers; smacks the outside.
  EXPRESSION: null
- CHARACTER: Diego (O.S.)
  LINE: Hey, Mrs. Woodhouse!
  EXPRESSION: Surprised
- CHARACTER: Narrator
  LINE: Rosemary pushes the handle and the car lurches upward. She overruns the elevator car to the ninth floor, then back to between six and seven, eventually just above seven. She opens the gates and steps down.
  EXPRESSION: null

::SCENE::
LOCATION: Hallway
MOOD: Panic and Pursuit
CHARACTERS: Rosemary, Guy, Dr. Sapirstein
BACKGROUND_IMAGE: hallway_night.png
BACKGROUND_EDIT: "Night, interior hallway"

::SCRIPT::
- CHARACTER: Narrator
  LINE: She runs through the turns of hallway as quickly as she can. As she reaches the landing near the apartment door, she stops, holding her middle, leaning against the wall, breathing shallowly.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: She sees the service elevator indicator, light blink for the fourth then fifth floor. Rosemary dashes for the door; the key won't go in.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The service elevator door opens; Guy and Dr. Sapirstein come out, rushing towards Rosemary.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The apartment door opens; Rosemary stumbles in. She slams the door behind her, chains it and bolts it, leans against it, breathing.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: We hear a key being put into the lock; immediately the door opens against the chain. We can see Guy's face and the tips of his fingers through the crack.
  EXPRESSION: null
- CHARACTER: Guy
  LINE: Open up, Ro.
  EXPRESSION: Pleading
- CHARACTER: Rosemary
  LINE: Go to hell.
  EXPRESSION: Defiant
- CHARACTER: Guy
  LINE: I’m not going to hurt you, honey.
  EXPRESSION: Deceptive
- CHARACTER: Rosemary
  LINE: You promised them the baby. Get away.
  EXPRESSION: Accusatory
- CHARACTER: Guy
  LINE: I didn't promise them anything. What are you talking about? Promised who?
  EXPRESSION: Feigning ignorance
- CHARACTER: Dr. Sapirstein (O.S.)
  LINE: Rosemary.
  EXPRESSION: Calm
- CHARACTER: Rosemary
  LINE: You too. Get away.
  EXPRESSION: Furious
- CHARACTER: Narrator
  LINE: She pushes the door shut and bolts it. She backs away watching it. It stays bolted. Rosemary goes to the Bedroom. The time is nine-thirty. She picks up the phone and dials. Still holding the phone, Rosemary steps towards the door and looks down the hallway towards the front door. There is quiet, the door is still closed. She steps back and sits on the bed.
  EXPRESSION: null
- CHARACTER: Baby Sitter (O.S.)
  LINE: Hello.
  EXPRESSION: Neutral
- CHARACTER: Rosemary
  LINE: Elise?
  EXPRESSION: Hopeful
- CHARACTER: Baby Sitter (O.S.)
  LINE: Mrs. Dunstan is out.
  EXPRESSION: Informative
- CHARACTER: Rosemary
  LINE: Who is this?
  EXPRESSION: Confused
- CHARACTER: Baby Sitter (O.S.)
  LINE: The baby sitter.
  EXPRESSION: Neutral
- CHARACTER: Rosemary
  LINE: Do you know where she is?
  EXPRESSION: Anxious
- CHARACTER: Baby Sitter (O.S.)
  LINE: They went to the movies.
  EXPRESSION: Informative
- CHARACTER: Rosemary
  LINE: This is Rosemary. Please tell Mrs. Dunstan to call Rosemary the second she gets back. It’s terribly urgent. Please don’t forget.
  EXPRESSION: Urgent
- CHARACTER: Baby Sitter (O.S.)
  LINE: Don’t worry.
  EXPRESSION: Reassuring
- CHARACTER: Narrator
  LINE: She hangs up, and stares at the telephone. We can hear whispers and footsteps.
  EXPRESSION: null
- CHARACTER: Guy
  LINE: Honey, we’re not going to hurt you.
  EXPRESSION: Soothing
- CHARACTER: Narrator
  LINE: Rosemary stands up. Guy is in the doorway with Mr. Fountain. Behind them, Dr. Sapirstein with a loaded hypodermic, the needle up and dripping his thumb at the plunger. Other people appear behind them: Mrs. Gilmore, Mrs. Fountain, Dr. Shand.
  EXPRESSION: null
- CHARACTER: Mrs. Gilmore
  LINE: We’re your friends.
  EXPRESSION: Friendly
- CHARACTER: Mrs. Fountain
  LINE: There’s nothing to be afraid of, Rosemary; honest and truly there isn’t.
  EXPRESSION: Reassuring
- CHARACTER: Dr. Sapirstein
  LINE: This is nothing but a mild sedative to calm you down.
  EXPRESSION: Clinical
- CHARACTER: Narrator
  LINE: Rosemary is between the bed and the wall. They come toward her.
  EXPRESSION: null
- CHARACTER: Guy
  LINE: You know I wouldn’t let anyone hurt you, Ro?
  EXPRESSION: Protective
- CHARACTER: Narrator
  LINE: Rosemary picks up the phone and strikes with the receiver at Guy’s head. He catches her wrist. Mr. Fountain catches her other arm and the phone falls as he pulls her around with startling strength.
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: Help me, somebody!
  EXPRESSION: Screaming
- CHARACTER: Narrator
  LINE: A handkerchief is jammed into her mouth and held there by a small strong hand. They drag her away from the bed so Dr. Sapirstein can come in front of her with the hypodermic and a dab of cotton.
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: (Moaning through handkerchief)
  EXPRESSION: Pained
- CHARACTER: Narrator
  LINE: A contraction; she clenches shut her eyes, holds her breath, then sucks air in through her nostrils in quick little pulls. A hand feels her belly deftly.
  EXPRESSION: null
- CHARACTER: Dr. Sapirstein
  LINE: Wait a minute, wait a minute now; we happen to be in labor here.
  EXPRESSION: Observant
- CHARACTER: Narrator
  LINE: Silence. Whispers outside the room.
  EXPRESSION: null
- CHARACTER: Voice (O.S.)
  LINE: She’s in labor.
  EXPRESSION: Informative
- CHARACTER: Narrator
  LINE: Rosemary opens her eyes and stares at Dr. Sapirstein, dragging air in through her nostrils. He nods at her, takes her arm that Mr. Fountain is holding, touches it with cotton and jabs the needle into it.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Rosemary takes the injection without moving. Dr. Sapirstein withdraws the needle and rubs the spot with his thumb, then with the cotton. The women are turning down the bed.
  EXPRESSION: null
- CHARACTER: Mrs. Gilmore
  LINE: Here?
  EXPRESSION: Questioning
- CHARACTER: Dr. Sapirstein
  LINE: Here.
  EXPRESSION: Affirmative
- CHARACTER: Narrator
  LINE: Rosemary struggles. In the confusion of this scene we hear Rosemary’s voice, without knowing if she is saying the words-or if they are her thoughts. At the same time, Guy is speaking into Rosemary's ear.
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: It was supposed to be Doctors Hospital! Doctors Hospital, with nurses and everything clean and sterile!
  EXPRESSION: Desperate
- CHARACTER: Guy
  LINE: You’ll be all right, honey, I swear to God you will! Don't go on fighting like this, Ro, please don't! I give you my absolute word of honor you're going to be perfectly all right!
  EXPRESSION: Pleading
- CHARACTER: Narrator
  LINE: Another contraction. Dr. Sapirstein gives Rosemary another injection. Mrs. Gilmore wipes Rosemary's forehead. The telephone rings.
  EXPRESSION: null
- CHARACTER: Guy
  LINE: She isn’t here Elise, I’ll have her call you back.
  EXPRESSION: Lying
- CHARACTER: Narrator
  LINE: Another contraction. Darkness. We hear Rosemary's voice.
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: Oh, Andy, Andy-or-Jenny! I’m sorry, my little darling. Forgive me!
  EXPRESSION: Apologetic

::SCENE::
LOCATION: Bedroom
MOOD: Fragile Peace
CHARACTERS: Rosemary, Guy
BACKGROUND_IMAGE: bedroom_day.png
BACKGROUND_EDIT: "Daytime, bedroom"

::SCRIPT::
- CHARACTER: Narrator
  LINE: After a long moment of darkness - light. The ceiling. Guy sitting beside the bed watching Rosemary with an anxious, uncertain smile.
  EXPRESSION: null
- CHARACTER: Guy
  LINE: Hi.
  EXPRESSION: Tentative
- CHARACTER: Rosemary
  LINE: Hi.
  EXPRESSION: Weak
- CHARACTER: Narrator
  LINE: (Long pause)
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: Is it all right?
  EXPRESSION: Anxious
- CHARACTER: Guy
  LINE: Yes, fine.
  EXPRESSION: Reassuring
- CHARACTER: Rosemary
  LINE: What is it?
  EXPRESSION: Curious
- CHARACTER: Guy
  LINE: A boy.
  EXPRESSION: Calm
- CHARACTER: Rosemary
  LINE: Really? A boy?
  EXPRESSION: Amazed
- CHARACTER: Guy
  LINE: Guy nods.
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: And it’s all right?
  EXPRESSION: Relieved
- CHARACTER: Guy
  LINE: Yes.
  EXPRESSION: Affirmative
- CHARACTER: Narrator
  LINE: Rosemary lets her eyes close, then manages to open them again.
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: Did you call Tiffany's?
  EXPRESSION: Hopeful
- CHARACTER: Guy
  LINE: Yes.
  EXPRESSION: Affirmative
- CHARACTER: Narrator
  LINE: Rosemary lets her eyes close and sleeps.
  EXPRESSION: null

::SCENE::
LOCATION: Bedroom
MOOD: Unease
CHARACTERS: Rosemary, Laura-Louise
BACKGROUND_IMAGE: bedroom_night_ll.png
BACKGROUND_EDIT: "Night, bedroom"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Next to the bed in which Rosemary is sleeping, Laura-Louise sits reading the "Reader’s Digest” with a magnifying glass.
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: Where is it?
  EXPRESSION: Groggily
- CHARACTER: Narrator
  LINE: Laura-Louise jumps, drops the book and presses the magnifying glass to her bosom.
  EXPRESSION: null
- CHARACTER: Laura-Louise
  LINE: My goodness, dear, what a start you gave me. My goodness!
  EXPRESSION: Startled
- CHARACTER: Narrator
  LINE: She closes her eyes and breathes deeply.
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: The baby: where is it?
  EXPRESSION: Demanding
- CHARACTER: Laura-Louise
  LINE: You
  EXPRESSION: Hesitant

::SCENE::
INT. BEDROOM - (DAY) - JUNE 26, 1966
MOOD: Somber
CHARACTERS: Narrator, Rosemary, Laura-Louise, Guy, Dr. Sapirstein
BACKGROUND_IMAGE: bedroom_day.png
BACKGROUND_EDIT: "June 26, 1966, bedroom, daytime"

::SCRIPT::
- CHARACTER: Narrator
  LINE: She gets up, retrieves the "Reader’s Digest", and goes toward the door.
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: Where’s the baby?
  EXPRESSION: Anxious
- CHARACTER: Laura-Louise (O.S.)
  LINE: I’ll get Doctor Abe. Just wait.
  EXPRESSION: Calm
- CHARACTER: Narrator
  LINE: Rosemary tries to get up but falls back, her arms boneless. She looks at the clock. It’s half past six. Guy and Dr. Sapirstein come in looking grave and resolute.
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: Where’s the baby?
  EXPRESSION: Anxious
- CHARACTER: Narrator
  LINE: Guy comes around to the side of the bed, crouches down and takes her hand.
  EXPRESSION: null
- CHARACTER: Guy
  LINE: Honey.
  EXPRESSION: Gentle
- CHARACTER: Rosemary
  LINE: Where is it?
  EXPRESSION: Anxious
- CHARACTER: Guy
  LINE: Honey... He tries to say more but can’t. He looks across the bed for help. Dr. Sapirstein stands looking down at Rosemary.
  EXPRESSION: Distressed
- CHARACTER: Dr. Sapirstein
  LINE: There were complications, Rosemary, but nothing; that till effect future births.
  EXPRESSION: Grave
- CHARACTER: Rosemary
  LINE: It’s -
  EXPRESSION: Distraught
- CHARACTER: Dr. Sapirstein
  LINE: Dead.
  EXPRESSION: Grave
- CHARACTER: Narrator
  LINE: Rosemary stares at Dr. Sapirstein. He nods. She turns to Guy. He nods too.
  EXPRESSION: null
- CHARACTER: Dr. Sapirstein
  LINE: It was in the wrong position, In the; hospital I might have been able to do something, but you wouldn’t listen -
  EXPRESSION: Resigned
- CHARACTER: Guy
  LINE: We can have others, honey, just as soon as you’re better, I promise you.
  EXPRESSION: Reassuring
- CHARACTER: Dr. Sapirstein
  LINE: Absolutely. You can start on another in a very few months.
  EXPRESSION: Professional
- CHARACTER: Narrator
  LINE: Guy squeezes Rosemary’s hand and smiles encouragingly at her.
  EXPRESSION: null
- CHARACTER: Guy
  LINE: As soon as you’re better.
  EXPRESSION: Reassuring
- CHARACTER: Narrator
  LINE: Rosemary looks at them.
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: You’re lying. I don’t believe you. You're both lying.
  EXPRESSION: Accusatory
- CHARACTER: Guy
  LINE: Honey.
  EXPRESSION: Gentle
- CHARACTER: Rosemary
  LINE: It didn’t die. You took it. You’re lying. You're witches. You’re - lying! You’re lying! You’re lying! You’re lying! You’re lying! You’re lying!
  EXPRESSION: Manic
- CHARACTER: Narrator
  LINE: Guy holds her shoulders to the bed and Dr. Sapirstein gives her an injection.
  EXPRESSION: null

::SCENE::
INT. BEDROOM - (DAY) - JUNE 26, 1966
MOOD: Unsettling Calm
CHARACTERS: Narrator, Rosemary, Guy
BACKGROUND_IMAGE: bedroom_day_soup.png
BACKGROUND_EDIT: "June 26, 1966, bedroom, daytime, Rosemary with soup tray"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Rosemary in bed with a tray of soup and buttered white bread on her lap. Guy, standing, hands her a glass of water and a small white pill. Rosemary takes it.
  EXPRESSION: null
- CHARACTER: Guy
  LINE: Abe says it’s called Prepartum I-don't-know, some kind of hysteria. You were really kapow out of your mind.
  EXPRESSION: Concerned
- CHARACTER: Narrator
  LINE: Rosemary says nothing; she takes a spoonful of soup. Guy sits on the edge of the bed, and starts nibbling at one of the bread triangles.
  EXPRESSION: null
- CHARACTER: Guy
  LINE: Listen, I know how you got the idea Minnie and Roman were witches, but what made you think Abe and I had joined the party?
  EXPRESSION: Casual
- CHARACTER: Narrator
  LINE: Rosemary says nothing. Guy takes another of the bread triangles and bites off first one point and then another.
  EXPRESSION: null
- CHARACTER: Guy
  LINE: Let's face it, darling, you had the prepartum crazies. Now you’re going to rest and get over them. I know this is the worst thing that ever happened to you, but from now on everything’s going to be roses. Paramount is within an inch of where we want them, and suddenly Universal is interested too. We’re going to blow this town and be in the beautiful hills of Beverly, with the pool and the spice garden and the whole schmeer. And the kids, too, Ro. Scout's honor. You heard what Abe said.
  EXPRESSION: Persuasive
- CHARACTER: Narrator
  LINE: He kisses her hand.
  EXPRESSION: null
- CHARACTER: Guy
  LINE: Got to run now and get ’famous.
  EXPRESSION: Eager
- CHARACTER: Narrator
  LINE: He gets up and starts for the door.
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: Let me see your shoulder.
  EXPRESSION: Suspicious
- CHARACTER: Narrator
  LINE: Guy stops and turns.
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: Let me see your shoulder.
  EXPRESSION: Demanding
- CHARACTER: Guy
  LINE: Are you kidding?
  EXPRESSION: Surprised
- CHARACTER: Rosemary
  LINE: Left shoulder.
  EXPRESSION: Firm
- CHARACTER: Narrator
  LINE: Guy looks at her.
  EXPRESSION: null
- CHARACTER: Guy
  LINE: All right, whatever you say, honey.
  EXPRESSION: Compliant
- CHARACTER: Narrator
  LINE: He undoes the collar of his short-sleeved blue knit shirt and peels it up over his head. Underneath is a white T shirt.
  EXPRESSION: null
- CHARACTER: Guy
  LINE: I generally prefer doing this to music.
  EXPRESSION: Playful
- CHARACTER: Narrator
  LINE: He takes off the T shirt; goes close to the bed, leans and shows Rosemary his left shoulder. It is unmarked. There is only a faint scar of a boil or pimple. Guy shows his other shoulder, his chest and back.
  EXPRESSION: null
- CHARACTER: Guy
  LINE: This is as far as I go without a blue light.
  EXPRESSION: Playful

::SCENE::
INT. BEDROOM - (NIGHT) - JUNE 28, 1966
MOOD: Tense
CHARACTERS: Narrator, Rosemary, Florence Gilmore
BACKGROUND_IMAGE: bedroom_night_tv.png
BACKGROUND_EDIT: "June 28, 1966, bedroom, nighttime, Rosemary watching TV"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Rosemary is lying in bed watching television. We hear the faint sound of a baby crying. Rosemary rays off the television and listens. She slips out of bed and turns off the air conditioner. FLORENCE GILMORE comes in with a pump and cup, glass of water and small white pill on a tray.
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: Do you hear a baby crying?
  EXPRESSION: Hopeful
- CHARACTER: Narrator
  LINE: They both listen. We hear a baby cry.
  EXPRESSION: null
- CHARACTER: Mrs. Gilmore
  LINE: No, dear, I don’t. Get back into bed now. Take your pill.
  EXPRESSION: Dismissive
- CHARACTER: Narrator
  LINE: She hands Rosemary the tray and switches on the air conditioner. Rosemary puts the pill under the mattress.
  EXPRESSION: null
- CHARACTER: Mrs. Gilmore
  LINE: Did you turn it off? You mustn’t do that. People are actually dying, it’s so hot.
  EXPRESSION: Stern
- CHARACTER: Narrator
  LINE: Mrs. Gilmore looks out the window.
  EXPRESSION: null

::SCENE::
INT. BEDROOM - (DAY) - JUNE 29, 1966
MOOD: Suspicious
CHARACTERS: Narrator, Rosemary, Laura-Louise, Guy
BACKGROUND_IMAGE: bedroom_day_tray.png
BACKGROUND_EDIT: "June 29, 1966, bedroom, daytime, Rosemary with tray"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Rosemary lying in bed. Laura-Louise sitting beside, holding the tray, with the pump and cup, glass of water and small white pill on a tray.
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: What do you do with it? (Indicating the milk)
  EXPRESSION: Curious
- CHARACTER: Laura-Louise
  LINE: Why, throw it away.
  EXPRESSION: Casual
- CHARACTER: Narrator
  LINE: Guy comes in. He puts his head around the doo
  EXPRESSION: null
- CHARACTER: Guy
  LINE: Hello, girls, Phew! Ninety-five outside.
  EXPRESSION: Energetic
- CHARACTER: Laura-Louise
  LINE: Your pill, Rosemary.
  EXPRESSION: Matter-of-fact
- CHARACTER: Narrator
  LINE: Rosemary takes the pill, lifts it to her mouth and fakes swallowing it, She takes the glass of water and drinks it. Simultaneously, with her other hand, she slips the pill under the mattress. Eight or ten other pills are already there. Guy calls from the other room.
  EXPRESSION: null
- CHARACTER: Guy (O.S)
  LINE: Some new people moved in. Up on eight.
  EXPRESSION: Distant
- CHARACTER: Rosemary
  LINE: Do they have a baby?
  EXPRESSION: Hopeful
- CHARACTER: Narrator
  LINE: Guy’s head appears once again in the doorway,
  EXPRESSION: null
- CHARACTER: Guy
  LINE: How did you know?
  EXPRESSION: Surprised
- CHARACTER: Rosemary
  LINE: I heard it crying.
  EXPRESSION: Assertive
- CHARACTER: Narrator
  LINE: There is a cup and saucer on the bedside with remains of coffee and a dirty spoon beside it, Rosemary takes the cup and puts it on the tray. She lifts the dirty spoon and starts putting it into the Pyrex cup of milk, Laura-Louise grabs her hand.
  EXPRESSION: null
- CHARACTER: Laura-Louise
  LINE: Don’t do that!
  EXPRESSION: Alarmed
- CHARACTER: Rosemary
  LINE: What difference does it make?
  EXPRESSION: Defiant
- CHARACTER: Laura-Louise
  LINE: Just messy, that’s all.
  EXPRESSION: Irritated

::SCENE::
INT. BEDROOM - (DUSK)
MOOD: Determined
CHARACTERS: Narrator, Rosemary
BACKGROUND_IMAGE: bedroom_dusk.png
BACKGROUND_EDIT: "Dusk, bedroom, Rosemary getting out of bed"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Rosemary gets out of bed, slides her feet into slippers, the puts on her housecoat. Going quietly out of the bedroom, she walks to the linen closet and opens it. The shelves look neat and orderly piled with bath towels, hand towels and winter blankets.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Rosemary takes everything out of the closet except what is on the fixed top shelf. She puts towels and linens on the floor, then lifts out the four gingham-covered shelves. The back of the closet, below the top shelf, is a single large white-painted panel framed with narrow white molding. Standing close and leaning aside for better light, Rosemary can see that where the panel and the molding meet, the paint is broken in a continuous line. She presses at one side of the panel and then at the others presses harder, and it swings inward on scraping hinges. Within is darkness a second closet with a wire hanger glinting on the floor, and one bright spot of light, a keyhole. Pushing the panel all the way open, Rosemary steps into the second closet and ducks down.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Through the keyhole, Rosemary sees at a distance a small curio cabinet that stands at a job in the hallway of Mr. and Mrs. Castevetfs apartment, Rosemary tries the door. It opens. She closes it and backs out through her own closet and goes to the kitchen.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: From her knife-rack, Rosemary takes the longest sharpest carving knife. As she is leaving the kitchen, we hear a key working in the lock of the front door, Rosemary rushes into the nursery, brushing against the new bassinet, and presses herself against the wall.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Guy enters and goes into the kitchen, opens the fridge and takes out ice cubes.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Rosemary sees that the bassinet is swinging. She stops it with the point of the long knife.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Guy comes out of the kitchen with Hutch’s ice bucket in his hand. He opens the entrance door and goes out.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Rosemary listens for a moment, then moves out to the front door and chains it. Holding the knife point-down at her side, she goes down the hallway to the linen closet door. She opens it, goes through again into the second closet (quick glance at the under-neath of the fixed top shelf like in the dream), looks through the keyhole and cracks open the door into the Castevet’s apartment. Holding the knife point forward, Rosemary pushes the door wide open and steps through. The hallway is empty. There are distant voices from the living room. The bathroom is on Rosemary’s righty its door open, dark; the Castevet’s bedroom on the left, with a bedside lamp burn­ing. She goes cautiously down the hallway and tries a door on the right; it is locked. Another, on the left, is a linen closet. Over the curio cabinet hangs a vivid oil painting of a church in flames.
  EXPRESSION: null
- CHARACTER: Rosemary
  LINE: - got her too high.
  EXPRESSION: Whispered
- CHARACTER: Narrator
  LINE: Knife high, she follows the jog to the left and the right. Other doors are locked. There is another painting; nude men and women dancing in a circle. Ahead are the foyer, the front door and the archway on the right to the living room. The voices are louder.
  EXPRESSION: null
- CHARACTER: Mr. Fountain (O.S)
  LINE: Not if he’s still waiting for a plane, he isn’t!
  EXPRESSION: Distant
- CHARACTER: Narrator
  LINE: There is laughter and then hushing.
  EXPRESSION: null
- CHARACTER: Mrs. Castevet (O.S.)
  LINE: Oh hell now, Hayato, you’re just making fun of me! ’Pulling my leg’ is what we say over here.
  EXPRESSION: Distant
- CHARACTER: Narrator
  LINE: Rosemary is at the archway now. She can see the coven is at the other end, laughing, talking softly. Ice cubes clink. She betters her grip on the knife and moves a step forward. She stops, staring. Across the room, in the one large window bay; stands a black bassinet, skirted wit
  EXPRESSION: null

::SCENE::
LOCATION: Castevet's Apartment - Living Room
MOOD: Ominous / Surreal
CHARACTERS: Narrator, Rosemary, Mr. Castevet, Mrs. Castevet, Guy, Mr. Fountain, The Weeses, Laura-Louise, Japanese Guest
BACKGROUND_IMAGE: castevet_living_room.png
BACKGROUND_EDIT: "A lavishly decorated room, guests in party attire, Adrian Marcato portrait above mantelpiece."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Black taffeta, hooded and flounced with black organza. A silver ornament turns on a black ribbon pinned to its black hood.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The stiff organza trembles. The silver ornament quivers and we can see that it is a crucifix hanging upside down, with the black ribbon wound and knotted around Jesus’ ankles.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Rosemary wipes her hands on her housecoat, throws back her hair, finds a fresh grip on the knife’s thick handle, and steps out where they can see-her.
  EXPRESSION: Determined
- CHARACTER: Narrator
  LINE: Insanely, they don’t. They go right on talking, listening, sipping, pleasantly partying; Mr. and Mrs. Castevet, Guy, Mr. Fountain, the Weeses, Laura-Louise and a studious-looking young Japanese with eye-glasses. All gathered under an over-the-mantel portrait of Adrian Marcato (the same as in the book).
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Mr. Castevet sees Rosemary first, puts down his drink and touches Mrs. Castevet’s arm. The voices fade. Those who sit with their back to Rosemary turn around questioningly. Guy starts to rise but sits down again. Laura-Louise claps both hands to her mouth and starts squealing.
  EXPRESSION: null
- CHARACTER: MRS. GILMORE
  LINE: Get back in bed, Rosemary; you know you aren’t supposed to be up and around.
  EXPRESSION: Concerned
- CHARACTER: JAPANESE
  LINE: Is the mother?
  EXPRESSION: Curious
- CHARACTER: Narrator
  LINE: Mr. Castevet nods and the Japanese looks at Rosemary with interest.
  EXPRESSION: null
- CHARACTER: JAPANESE
  LINE: Ah, sssssssssssss.
  EXPRESSION: Intrigue
- CHARACTER: Narrator
  LINE: Watching them, Rosemary starts across the room toward the bassinet.
  EXPRESSION: null
- CHARACTER: MR. CASTEVET
  LINE: Rosemary.
  EXPRESSION: Warning
- CHARACTER: ROSEMARY
  LINE: Shut up.
  EXPRESSION: Defiant
- CHARACTER: MR. CASTEVET
  LINE: Before you look at -
  EXPRESSION: Warning
- CHARACTER: ROSEMARY
  LINE: Shut up. You’re in Dubrovnik. I don’t hear you.
  EXPRESSION: Defiant
- CHARACTER: Narrator
  LINE: Rosemary watched them until she is by the bassinet, which is angled in their direction. With her free hand, she catches the black-covered handle and swings the bassinet slowly, gently, around to face her.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Taffeta rustles, the black wheels squeal. She looks in. Smiling gently, she slowly reaches her left arm to take the baby. The smile fades on her face and changes into an expression of horror. She backs slowly away and freezes with her eyes wide open.
  EXPRESSION: Horror
- CHARACTER: ROSEMARY
  LINE: What have you done to it? What have you done to its eyes?
  EXPRESSION: Horrified
- CHARACTER: Narrator
  LINE: They stir and look to Mr. Castevet.
  EXPRESSION: null
- CHARACTER: MR. CASTEVET
  LINE: He has His Father’s eyes.
  EXPRESSION: Ominous
- CHARACTER: Narrator
  LINE: Rosemary looks at him, looks at Guy - whose eyes are hidden behind a hand - looks at Mr. Castevet again.
  EXPRESSION: null
- CHARACTER: ROSEMARY
  LINE: What are you talking about? Guy’s eyes are normal. What have you done to him, you maniacs?
  EXPRESSION: Furious
- CHARACTER: Narrator
  LINE: She moves from the bassinet, ready to kill him.
  EXPRESSION:null
- CHARACTER: MR. CASTEVET
  LINE: Satan is His Father, not Guy. He came up from Hell and begat a Son of mortal woman!
  EXPRESSION: Grandiose
- CHARACTER: MR. WEES
  LINE: Hail Satan.
  EXPRESSION: Reverent
- CHARACTER: Narrator
  LINE: Mr. Castevet cries, his voice growing louder and prouder, his bearing more strong and forceful.
  EXPRESSION: null
- CHARACTER: MR. CASTEVET
  LINE: Satan is His Father and His Name is Adrian! He shall overthrow the mighty and lay waste their temples! He shall redeem the despised and wreak vengeance in the name of the burned and the tortured! Hail Adrian!
  EXPRESSION: Thundering
- CHARACTER: VOICES
  LINE: Hail Adrian! Hail Adrian!
  EXPRESSION: Chanting
- CHARACTER: MR. CASTEVET
  LINE: Hail Satan! Hail Satan.
  EXPRESSION: Thundering
- CHARACTER: VOICES
  LINE: Hail Satan!
  EXPRESSION: Chanting
- CHARACTER: Narrator
  LINE: Rosemary shakes her head.
  EXPRESSION:null
- CHARACTER: ROSEMARY
  LINE: No.
  EXPRESSION: Denying
- CHARACTER: MRS. CASTEVET
  LINE: He chose you out of all the world, Rosemary. Out of all the women in the whole world, He chose you. He arranged everything ’cause He wanted you to be the mother of His only living Son.
  EXPRESSION: Persuasive
- CHARACTER: MR. CASTEVET
  LINE: His power is stronger than stronger.
  EXPRESSION: Boasting
- CHARACTER: MRS. WEES
  LINE: Hail Satan.
  EXPRESSION: Reverent
- CHARACTER: MR. CASTEVET
  LINE: His might will last longer than longer.
  EXPRESSION: Boasting
- CHARACTER: JAPANESE
  LINE: Hail Satan!
  EXPRESSION: Chanting
- CHARACTER: Narrator
  LINE: Laura-Louise uncovers her mouth. Guy looks out at Rosemary from under his hand.
  EXPRESSION:null
- CHARACTER: ROSEMARY
  LINE: No, it can't be. No.
  EXPRESSION: Despairing
- CHARACTER: MRS. CASTEVET
  LINE: Go look at His hands.
  EXPRESSION: Commanding
- CHARACTER: LAURA-LOUISE
  LINE: And His feet.
  EXPRESSION: Commanding
- CHARACTER: ROSEMARY
  LINE: Oh God.
  EXPRESSION: Anguished
- CHARACTER: Narrator
  LINE: She covers her face. The knife falls into the floor and sways, upright.
  EXPRESSION:null
- CHARACTER: MR. CASTEVET
  LINE: God is DEAD!
  EXPRESSION: Thundering
- CHARACTER: ROSEMARY
  LINE: Oh God! Oh God! Oh God!
  EXPRESSION: Anguished
- CHARACTER: MR. CASTEVET
  LINE: God is dead. Satan lives! The year is One.
  EXPRESSION: Triumphant
- CHARACTER: VOICES
  LINE: Hail Satan! Hail Adrian! Hail Adrian! Hail Satan!
  EXPRESSION: Chanting
- CHARACTER: MR. CASTEVET
  LINE: The year is One, God is done! The year is One, Adrian’s begun!
  EXPRESSION: Triumphant
- CHARACTER: Narrator
  LINE: Rosemary backs away.
  EXPRESSION:null
- CHARACTER: ROSEMARY
  LINE: No, no.
  EXPRESSION: Panicked
- CHARACTER: Narrator
  LINE: She backs further and further away through the shouting people. In the confusion of movement, a faint fragment of her dream flashes. A chair is behind her; she sits down on it and stares at them. Mrs. Castevet goes over and, grunting as she stoops, pulls out the knife and takes it into the kitchen. Guy follows her. Laura-Louise rocks the bassinet possessively, making faces into it. Rosemary sits staring. Mr. Castevet comes over to her.
  EXPRESSION:null
- CHARACTER: MR. CASTEVET
  LINE: Why don’t you help us out, Rosemary, be a real mother to Adrian. You don't have to join if you don’t want to; just be a mother to your baby.
  EXPRESSION: Coaxing
- CHARACTER: Narrator
  LINE: (Bends down and whispers) Minnie and Laura-Louise are too old. It's not right.
  EXPRESSION: Seductive
- CHARACTER: Narrator
  LINE: Rosemary looks at Mr. Castevet. He straightens up. The doorbell rings.
  EXPRESSION:null
- CHARACTER: MR. CASTEVET
  LINE: Think about it, Rosemary.
  EXPRESSION: Coaxing
- CHARACTER: ROSEMARY
  LINE: Oh God.
  EXPRESSION: Desperate
- CHARACTER: LAURA-LOUISE
  LINE: Shut up with your ’Oh God's, or we'll kill you, milk or no milk.
  EXPRESSION: Threatening
- CHARACTER: MRS. WEES
  LINE: You shut up.
  EXPRESSION: Protective
- CHARACTER: Narrator
  LINE: She comes to Rosemary and puts a dampened handkerchief in her hand.
  EXPRESSION:null
- CHARACTER: MRS. WEES
  LINE: Rosemary is His mother, so you show some respect.
  EXPRESSION: Stern
- CHARACTER: Narrator
  LINE: Laura-Louise mutters. Rosemary wipes her forehead and cheeks with the handkerchief. The Japanese, sitting across the room on a hassock, catches Rosemary's eye, grins and ducks his head. He holds up an opened camera into which he is putting film. Rosemary looks down and starts crying.
  EXPRESSION:null
- CHARACTER: Narrator
  LINE: Mr. Castevet comes in, holding the arm of ARGYRON STAVROPOULOS. He is a robust, handsome, dark-skinned man, wearing a white suit, white shoes and carrying a large box wrapped in light blue paper patterned with Teddy bears and candy canes. Musical sounds come from it.
  EXPRESSION:null
- CHARACTER: Narrator
  LINE: Everyone gathers to meet him and shake his hand. There is a confused, hushed conversation from which words like "Worried - pleasure — airport — Stavropoulos — occasion" can be heard. Laura-Louise brings the box to the bassinet. She holds it up for the baby to see, shakes it, and puts it on the window seat. There are other boxes similarly wrapped and a few that are wrapped in black with black ribbon.
  EXPRESSION:null
- CHARACTER: MR. CASTEVET
  LINE: Come, my friend. Come see Him. Come see the Child.
  EXPRESSION: Inviting
- CHARACTER: Narrator
  LINE: They go to the bassinet. Laura-Louise waits with a proprietary smile. They close around it and look into it silently. Argyron Stavropoulos lowers himself to his knees.
  EXPRESSION:null
- CHARACTER: Narrator
  LINE: Guy comes back from the kitchen, over to Rosemary. He stands looking down at her.
  EXPRESSION:null
- CHARACTER: GUY
  LINE: They promised me you wouldn't be hurt, and you haven't been, really. I mean, suppose you'd had a baby and lost it; wouldn’t it be the same? And we're getting so much in return, Ro.
  EXPRESSION: Justifying
- CHARACTER: Narrator
  LINE: Rosemary puts the handkerchief on the table, looks at Guy, and, as hard as she can, spits at him. Guy flushes and turns away, wiping his face.
  EXPRESSION:null
- CHARACTER: Narrator
  LINE: Laura-Louise rocks the bassinet. The baby starts whimpering. Mr. Castevet catches Guy by the arm.
  EXPRESSION:null
- CHARACTER: MR. CASTEVET
  LINE: Guy, let me introduce you to Argyron Stavropoulos.
  EXPRESSION: Formal
- CHARACTER: Narrator
  LINE: Argyron Stavropoulos clasps Guy's hand in both his own.
  EXPRESSION:null
- CHARACTER: STAVROPOULOS
  LINE: How proud you must be.
  EXPRESSION: Polite
- CHARACTER: Narrator
  LINE: He looks over Guy's shoulder, at Rosemary.
  EXPRESSION:null
- CHARACTER: STAVROPOULOS
  LINE: Is this the mother? Why in the name of -
  EXPRESSION: Shocked
- CHARACTER: Narrator
  LINE: Mr. Castevet draws him away, speaking in his ear. Mrs. Castevet brings a mug of steaming tea to Rosemary.
  EXPRESSION:null
- CHARACTER: MRS. CASTEVET
  LINE: Here. Drink this and you'll feel a little better.
  EXPRESSION: Soothing
- CHARACTER: Narrator
  LINE: Rosemary looks at the mug and looks up at Mrs. Castevet.
  EXPRESSION:null
- CHARACTER: ROSEMARY
  LINE: What’s in it? Tannis root?
  EXPRESSION: Suspicious
- CHARACTER: MRS. CASTEVET
  LINE: Nothing is in it. It’s plain ordinary Lipton tea. You drink it.
  EXPRESSION: Reassuring
- CHARACTER: Narrator
  LINE: Rosemary looks at Laura-Louise rocking the bassinet. The baby is still whimpering, and Laura-Louise rocks it faster and faster. Rosemary gets up and goes over.
  EXPRESSION:null
- CHARACTER: LAURA-LOUISE
  LINE: Get away from here. Roman!
  EXPRESSION: Territorial
- CHARACTER: ROSEMARY
  LINE: You’re rocking him too fast.
  EXPRESSION: Concerned
- CHARACTER: LAURA-LOUISE
  LINE: Sit down! Get her out of here. Put her where she belongs.
  EXPRESSION: Aggressive
- CHARACTER: ROSEMARY
  LINE: You’re rocking him too fast. That’s why he’s whimpering.
  EXPRESSION: Insistent
- CHARACTER: LAURA-LOUISE
  LINE: Mind your own business!
  EXPRESSION: Hostile
- CHARACTER: MR. CASTEVET
  LINE: Let Rosemary rock Him.
  EXPRESSION: Commanding
- CHARACTER: Narrator
  LINE: Laura-Louise stares at him. He stands behind the bassinet’s head.
  EXPRESSION:null
- CHARACTER: MR. CASTEVET
  LINE: Go on. Sit down with the others. Let Rosemary rock Him.
  EXPRESSION: Commanding
- CHARACTER: LAURA-LOUISE
  LINE: She's liable -
  EXPRESSION: Reluctant
- CHARACTER: MR. CASTEVET
  LINE: Sit down with the others, Laura-Louise.
  EXPRESSION: Firm
- CHARACTER: Narrator
  LINE: Laura-Louise huffs and marches away.
  EXPRESSION:null
- CHARACTER: MR. CASTEVET
  LINE: Rock him.
  EXPRESSION: Encouraging
- CHARACTER: Narrator
  LINE: He smiles at Rosemary and moves the bassinet back and forth towards her, holding it by its hood. Rosemary stands still and looks at him;
  EXPRESSION:null
- CHARACTER: ROSEMARY
  LINE: You’re trying to get me to be his mother.
  EXPRESSION: Realizing
- CHARACTER: MR. CASTEVET
  LINE: Aren’t you His mother?
  EXPRESSION: Accusatory
- CHARACTER: Narrator
  LINE: Slowly, Rosemary lets the black-covered handle come into her hand, and closes her fingers around it. For a few moments they rock the bassinet between them, then Mr. Castevet lets go and Rosemary rocks it alone, nice and slowly. Mr. Castevet withdraws silently to where everybody now stands in a semi-circle, watching.
  EXPRESSION:null
- CHARACTER: Narrator
  LINE: Dr. Sapirstein comes into the room and looks at the scene, in surprise. Mrs. Castevet puts her finger to her lips. The Japanese steps forward and crouching down to find an angle, clicks his camera. Very softly, Rosemary is humming. From behind the window, we can hear the distant noise of the street and cars hooting. The sun has already set behind the buildings and the pleasant evening light covers the city.
  EXPRESSION:null

::PATHS::
- CHOICE: "End Scene"
  TARGET: end
  STATE_CHANGE: null
  CONDITION: null

