::SCENE::
LOCATION: Woods - Hälsingland
MOOD: Serene
CHARACTERS: Narrator
BACKGROUND_IMAGE: woods_day.png
BACKGROUND_EDIT: "Beautifully composed midday landscapes in Hälsingland, Sweden, with no people or human habitation."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Hälsingland, North Sweden. We cycle through a series of beautifully composed midday landscapes. None of them feature people or human habitation.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: A spare Swedish lullaby plays over this quiet montage. This is the song of the Hårgas. When it concludes, we CUT HARD TO:
  EXPRESSION: null

::PATHS::
- CHOICE: "Transition to next scene"
  TARGET: house_minnesota
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: House - Minnesota
MOOD: Eerie Calm
CHARACTERS: Narrator
BACKGROUND_IMAGE: house_minnesota_night.png
BACKGROUND_EDIT: "Beautiful suburban home bathed in vivid moonlight. The neighborhood is very quiet."

::SCRIPT::
- CHARACTER: Narrator
  LINE: A beautiful suburban home, bathed in vivid moonlight. The neighborhood is very quiet.
  EXPRESSION: null

::PATHS::
- CHOICE: "Enter the house"
  TARGET: bedroom_night_minnesota
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Bedroom - Minnesota
MOOD: Foreboding Stillness
CHARACTERS: Narrator, Man, Woman, Answering Machine, Young Woman
BACKGROUND_IMAGE: bedroom_night_minnesota.png
BACKGROUND_EDIT: "Man and Woman (early sixties) lay asleep in bed, extremely still."

::SCRIPT::
- CHARACTER: Narrator
  LINE: A MAN and WOMAN (early sixties) lay asleep in bed. They are extremely still.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The PHONE rings. The Man and Woman do not stir. After a few rings, the ANSWERING MACHINE takes it.
  EXPRESSION: null
- CHARACTER: Answering Machine (V.O.)
  LINE: Hello. You’ve reached --
  EXPRESSION: null
- CHARACTER: Man & Woman (V.O.)
  LINE: -- the Ardor residence.
  EXPRESSION: null
- CHARACTER: Answering Machine (V.O.)
  LINE: Please leave your message at the tone. When you’re finished with your message, press pound.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: BEEP. Enter the voice of a YOUNG WOMAN:
  EXPRESSION: null
- CHARACTER: Young Woman (V.O.)
  LINE: Hey mom and dad, it’s Dani. Sorry I’m calling so late. I’m just checking in to make sure everyone’s okay. I got kind of a scary email from Terri and it sounded like you guys were having some sort of conflict? Anyway, I just got a little worried, so call me when you can, and if there’s anything I can do, just please know that I’m here. Okay. All right. I love you.
  EXPRESSION: Worried

::PATHS::
- CHOICE: "Continue to Dani's location"
  TARGET: bedroom_brooklyn
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Bedroom - Brooklyn, NY
MOOD: Anxiety
CHARACTERS: Narrator, Dani, Christian, Mark
BACKGROUND_IMAGE: bedroom_brooklyn_night.png
BACKGROUND_EDIT: "Young woman, Dani (25), a beautiful but delicate brunette, is by her laptop. An email from Terri Ardor is displayed."

::SCRIPT::
- CHARACTER: Narrator
  LINE: The young woman lowers the cell from her ear. This is DANI (25), a beautiful but delicate brunette. She hangs up, and turns to her laptop. An EMAIL from Terri Ardor, titled “dear dani,” is displayed. It reads:
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: i cant anymore - everything’s black - mom and dad are coming too. goodbye.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Dani stares at this, anxiety rising. She picks up her phone, hesitates, and then calls Christian.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Four rings. CHRISTIAN (25) answers. The rest of this scene will be shot in a VERY TIGHT CLOSE-UP of Dani.
  EXPRESSION: null
- CHARACTER: Christian (V.O.)
  LINE: Hi...!
  EXPRESSION: null
- CHARACTER: Dani
  LINE: Hey baby. What you up to?
  EXPRESSION: Carefree
- CHARACTER: Christian (V.O.)
  LINE: Oh, just smoked some resin at Mark’s and now we’re getting pizza.
  EXPRESSION: null
- CHARACTER: Dani
  LINE: Oh nice.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: In the b.g., we hear a young man repeating “hi Dani, hi Dani, hi Dani...”
  EXPRESSION: null
- CHARACTER: Christian (V.O.)
  LINE: Yeah - he’s saying hi right now, over and over.
  EXPRESSION: null
- CHARACTER: Dani
  LINE: Hi Mark!
  EXPRESSION: Playful
- CHARACTER: Christian (V.O.)
  LINE: (off-phone) “Hi Mark.”
  EXPRESSION: null
- CHARACTER: Dani
  LINE: So I was just calling to see if you were still wanting to get together.
  EXPRESSION: Hopeful
- CHARACTER: Christian (V.O.)
  LINE: Oh - did we talk about doing something tonight?
  EXPRESSION: Ambivalent
- CHARACTER: Dani
  LINE: I mean, not concretely. I was just seeing.
  EXPRESSION: Tentative
- CHARACTER: Christian (V.O.)
  LINE: Uh, well - okay. Yeah. I should be able to swing by.
  EXPRESSION: Reluctant
- CHARACTER: Dani
  LINE: All right...!
  EXPRESSION: Excited
- CHARACTER: Christian (V.O.)
  LINE: Yeah. Okay... How’s the sister situation?
  EXPRESSION: Concerned
- CHARACTER: Dani
  LINE: Well. I’ve now sent her three emails and still no response... I’m starting to get a little nervous.
  EXPRESSION: Anxious
- CHARACTER: Christian (V.O.)
  LINE: I’m sure it’s fine.
  EXPRESSION: Dismissive
- CHARACTER: Dani
  LINE: Yeah. Probably. I hope so.
  EXPRESSION: Doubtful
- CHARACTER: Christian (V.O.)
  LINE: She does this every other day, Dani. And only because you let her.
  EXPRESSION: Exasperated
- CHARACTER: Dani
  LINE: Well, I don’t LET her. She’s bipolar.
  EXPRESSION: Defensive
- CHARACTER: Christian (V.O.)
  LINE: I know, but you do, though, babe. You go straight to crisis mode.
  EXPRESSION: Patronizing
- CHARACTER: Dani
  LINE: Well - but she’s my sister. And even you admit this last email was different...
  EXPRESSION: Pleading
- CHARACTER: Christian (V.O.)
  LINE: Okay, but is it, though? It’s still another clear ploy for attention - just like every other panic attack she’s given you.
  EXPRESSION: Skeptical
- CHARACTER: Narrator
  LINE: Dani looks like she wants to argue with this. She stifles it.
  EXPRESSION: Resigned
- CHARACTER: Dani
  LINE: Okay. Yeah. You’re right. You are right.
  EXPRESSION: Submissive
- CHARACTER: Christian (V.O.)
  LINE: The more you respond, the more she’s encouraged to keep this crap up.
  EXPRESSION: Stern
- CHARACTER: Dani
  LINE: No, I do know you’re right. I just needed to be reminded. Thank you. I’m really lucky to have you.
  EXPRESSION: Grateful
- CHARACTER: Christian (V.O.)
  LINE: Me too.
  EXPRESSION: Fond
- CHARACTER: Dani
  LINE: I love you.
  EXPRESSION: Sincere
- CHARACTER: Christian (V.O.)
  LINE: ...So do I.
  EXPRESSION: Fond
- CHARACTER: Dani
  LINE: Okay. See you later?
  EXPRESSION: Hopeful
- CHARACTER: Christian (V.O.)
  LINE: Yup.
  EXPRESSION: Affirmative
- CHARACTER: Dani
  LINE: Okay. “Bye Mark!”
  EXPRESSION: Playful
- CHARACTER: Christian (V.O.)
  LINE: “Bye Mark.”
  EXPRESSION: Amused
- CHARACTER: Dani
  LINE: All right. Love you. Bye.
  EXPRESSION: Affectionate
- CHARACTER: Narrator
  LINE: Dani hangs up. Her eyes are wide with insecurity.
  EXPRESSION: Insecure

::PATHS::
- CHOICE: "Continue to kitchen scene"
  TARGET: kitchen_minutes_later
  STATE_CHANGE: anxiety = +1
  CONDITION: null

::SCENE::
LOCATION: Kitchen
MOOD: Mounting Panic
CHARACTERS: Narrator, Dani, Girlfriend
BACKGROUND_IMAGE: kitchen.png
BACKGROUND_EDIT: "Dani stands in the kitchen, mid-phone conversation, pacing when she's not speaking."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Dani stands in the kitchen, mid-phone conversation. FRAUGHT. She paces when she’s not speaking.
  EXPRESSION: Agitated
- CHARACTER: Dani
  LINE: It’s just in his tone - you can hear it. It’s like he’s trying to work up the nerve to say something and I just keep staving it off.
  EXPRESSION: Anxious
- CHARACTER: Girlfriend (V.O.)
  LINE: So don’t stave him off. Be direct! Confront him!
  EXPRESSION: Encouraging
- CHARACTER: Girlfriend (V.O.)
  LINE: Well - what if I scared him? I’m always roping him into my family crap... I’m always leaning on him! I tell him everything! I even called him today in tears because my sister sent me another scary email. What if I’m scaring him off?
  EXPRESSION: Worried
- CHARACTER: Dani
  LINE: Oh - how do you rope him in? That’s what he’s there for!
  EXPRESSION: Defensive
- CHARACTER: Girlfriend (V.O.)
  LINE: What did your sister write?
  EXPRESSION: Curious
- CHARACTER: Dani
  LINE: Oh - just some ominous bullshit! She does it all the time! It’s torture, and I’ve been completely leaning on him for support! What if I overwhelmed him and now he thinks I have too much baggage?
  EXPRESSION: Distressed
- CHARACTER: Narrator
  LINE: Dani opens a prescription bottle of ATIVAN. She pops one.
  EXPRESSION: null
- CHARACTER: Girlfriend (V.O.)
  LINE: Well, if that’s the case, then good riddance! Right?
  EXPRESSION: Blunt
- CHARACTER: Dani
  LINE: No! Not if I went too far! What if I leaned too heavily?
  EXPRESSION: Panicked
- CHARACTER: Narrator
  LINE: Dani has returned to her laptop.
  EXPRESSION: null
- CHARACTER: Girlfriend (V.O.)
  LINE: You didn’t! He should be there when you need him.
  EXPRESSION: Reassuring
- CHARACTER: Dani
  LINE: But what if I need him too often? If it becomes a chore? Then he's not the right guy. Because it shouldn't ever be a chore. Would it be a chore if he leaned on you?
  EXPRESSION: Fearful
- CHARACTER: Narrator
  LINE: Dani breaks from writing to respond:
  EXPRESSION: null
- CHARACTER: Dani
  LINE: But he never asks for anything from me! I've never even seen him cry! So I'm the only one leaning!
  EXPRESSION: Frustrated
- CHARACTER: Girlfriend (V.O.)
  LINE: Or the only one opening up! The only one making yourself vulnerable. That's intimacy.
  EXPRESSION: Insightful
- CHARACTER: Narrator
  LINE: As the friend says that, Dani finishes typing. Her email reads: "PLEASE write me back, Terri. You can't just write me something like that and then disappear. I'm worried sick and I think my boyfriend is breaking up with me and I'm freaking out. Please write back. Please."
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Dani’s phone beeps with an INCOMING CALL. It’s an UNKNOWN NUMBER.
  EXPRESSION: null

::PATHS::
- CHOICE: "Answer the unknown call"
  TARGET: pizza_parlor
  STATE_CHANGE: anxiety = +2
  CONDITION: null

::SCENE::
LOCATION: Pizza Parlor - New York
MOOD: Casual then Tense
CHARACTERS: Narrator, Christian, Mark, Josh, Pelle, Waitress
BACKGROUND_IMAGE: pizza_parlor_ny.png
BACKGROUND_EDIT: "A grubby pizza parlor. Outside the window looms a purple NYU sign. Christian, Mark, Josh, and Pelle sit at a booth. Pelle doodles on a napkin."

::SCRIPT::
- CHARACTER: Narrator
  LINE: A grubby pizza parlor. Outside the window looms a purple NYU sign. CHRISTIAN, very handsome and fit, sits at a booth. Beside him are his friends MARK (26, droll, shaggy hair), JOSH (27, a skinny, sometimes snobbish academic), and PELLE (26), a nice-looking Swedish exchange student. Pelle doodles on his napkin (drawing the flowers on the table).
  EXPRESSION: null
- CHARACTER: Mark
  LINE: Dude: you need to stop sitting on the fence with this.
  EXPRESSION: Direct
- CHARACTER: Christian
  LINE: But what if I end up regretting it a week later, and then I can’t get her back?
  EXPRESSION: Conflicted
- CHARACTER: Mark
  LINE: You don’t want her back!
  EXPRESSION: Insistent
- CHARACTER: Christian
  LINE: I might!
  EXPRESSION: Uncertain
- CHARACTER: Mark
  LINE: So then you can bitch to us for that week about how much you regret it, and we'll be like “Dude: you’ve been wanting out of this absurd relationship for the last year,” and you’ll be like “oh shit, that’s right” and then you can find some new chick who actually likes sex and who doesn’t drag you through a million hoops a day.
  EXPRESSION: Blunt
- CHARACTER: Narrator
  LINE: Christian is thinking about this. Extremely conflicted.
  EXPRESSION: Contemplative
- CHARACTER: Josh
  LINE: Do you think a masochistic part of you is playing this drama out to distract you from the work you actually need to be doing?
  EXPRESSION: Analytical
- CHARACTER: Christian
  LINE: (prepared to be offended) And what work do I actually need to do, Josh?
  EXPRESSION: Defensive
- CHARACTER: Josh
  LINE: Uhhh - your prospectus maybe? I dunno. Your PhD...?
  EXPRESSION: Unsure
- CHARACTER: Narrator
  LINE: Christian clearly doesn’t want to be told his priorities by Josh. Before he can snap back, an attractive WAITRESS (early 20s) brings over the check.
  EXPRESSION: Annoyed
- CHARACTER: Waitress
  LINE: Whenever you guys are ready.
  EXPRESSION: Professional
- CHARACTER: Pelle
  LINE: Thank you.
  EXPRESSION: Polite
- CHARACTER: Narrator
  LINE: She SMILES -- at Christian.
  EXPRESSION: null
- CHARACTER: Waitress
  LINE: Thank you.
  EXPRESSION: Flirtatious
- CHARACTER: Narrator
  LINE: She HOLDS the smile with Christian and walks bashfully off. Mark definitely caught that.
  EXPRESSION: Observant
- CHARACTER: Mark
  LINE: Dude. You could be getting that girl pregnant right now.
  EXPRESSION: Teasing
- CHARACTER: Pelle
  LINE: And don’t forget all the Swedish women you can impregnate in June.
  EXPRESSION: Playful
- CHARACTER: Mark
  LINE: Yeah, dude - don’t forget all the Swedish milkmaids.
  EXPRESSION: Joking
- CHARACTER: Narrator
  LINE: Christian’s PHONE rings. He checks. It’s DANI. He deflates.
  EXPRESSION: Disappointed
- CHARACTER: Mark
  LINE: Who is that?
  EXPRESSION: Curious
- CHARACTER: Narrator
  LINE: Christian doesn’t respond.
  EXPRESSION: Silent
- CHARACTER: Mark
  LINE: That’s not her again? Seriously?
  EXPRESSION: Exasperated
- CHARACTER: Narrator
  LINE: Christian lets the call go.
  EXPRESSION: Indifferent
- CHARACTER: Mark
  LINE: That’s ridiculous, dude. She needs a therapist.
  EXPRESSION: Firm
- CHARACTER: Christian
  LINE: She has one.
  EXPRESSION: Resigned
- CHARACTER: Mark
  LINE: So she should call him! That’s insane, dude. She’s using you.
  EXPRESSION: Annoyed
- CHARACTER: Narrator
  LINE: The phone starts ringing again. Christian checks it. “Dani again.”
  EXPRESSION: Frustrated
- CHARACTER: Mark
  LINE: Oh my God.
  EXPRESSION: Exasperated
- CHARACTER: Narrator
  LINE: Christian answers. He rises from the booth to get some privacy.
  EXPRESSION: null
- CHARACTER: Christian
  LINE: Hello?
  EXPRESSION: Weary
- CHARACTER: Narrator
  LINE: On the other end: an extended, agonized MOAN.
  EXPRESSION: null
- CHARACTER: Christian
  LINE: Dani?
  EXPRESSION: Concerned
- CHARACTER: Dani (V.O.)
  LINE: ...no, no, no, no, no, no, no...
  EXPRESSION: Distressed
- CHARACTER: Christian
  LINE: Sweetheart? What’s going on?
  EXPRESSION: Scared
- CHARACTER: Narrator
  LINE: But now there’s only heavy, frightening CRYING on the other end. It’s a deep, horrible cry. One of pure animal grief.
  EXPRESSION: null
- CHARACTER: Christian
  LINE: (now scared) What’s happening, baby? Please talk to me.
  EXPRESSION: Terrified
- CHARACTER: Narrator
  LINE: The crying has curdled into a sustained WAIL OF ANGUISH.
  EXPRESSION: null

::PATHS::
- CHOICE: "Witness the unfolding horror"
  TARGET: garage_minnesota
  STATE_CHANGE: fear = +3
  CONDITION: null

::SCENE::
LOCATION: Garage - Minnesota
MOOD: Ominous Revelation
CHARACTERS: Narrator, Firefighter
BACKGROUND_IMAGE: garage_minnesota_night.png
BACKGROUND_EDIT: "The house from the beginning. Two cars are parked. Engines hum quietly. A firefighter opens one car’s door and turns off the ignition."

::SCRIPT::
- CHARACTER: Narrator
  LINE: The house from the beginning (scene 2).
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Two CARS are parked. Their engines hum quietly. A FIREFIGHTER opens one car’s door and turns OFF the ignition.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: We now reveal that the end of a GARDENING HOSE has been taped to one car’s EXHAUST PIPE. A second hose has been taped to the other car’s exhaust pipe. Both hoses TRAIL out of the garage and INTO the house...
  EXPRESSION: null

::PATHS::
- CHOICE: "Follow the hoses into the house"
  TARGET: hallway_continuous
  STATE_CHANGE: horror = +1
  CONDITION: null

::SCENE::
LOCATION: Hallway - Continuous
MOOD: Disturbing Discovery
CHARACTERS: Narrator
BACKGROUND_IMAGE: hallway_continuous.png
BACKGROUND_EDIT: "One gardening hose leads to a bedroom door. The door is now open, but the end of the hose has been taped to the bottom."

::SCRIPT::
- CHARACTER: Narrator
  LINE: One gardening hose leads to a BEDROOM DOOR. The door is now open, but the end of the hose has been TAPED to the bottom...
  EXPRESSION: null

::PATHS::
- CHOICE: "Enter the bedroom"
  TARGET: bedroom_continuous
  STATE_CHANGE: horror = +2
  CONDITION: null

::SCENE::
LOCATION: Bedroom - Continuous
MOOD: Tragic End
CHARACTERS: Narrator, Man, Woman
BACKGROUND_IMAGE: bedroom_continuous.png
BACKGROUND_EDIT: "The bedroom of the sleeping Man and Woman (in their 60s, from the beginning)."

::SCRIPT::
- CHARACTER: Narrator
  LINE: The bedroom of the sleeping MAN and WOMAN (in their 60s, from the beginning
  EXPRESSION: null

::PATHS::
- CHOICE: "End of excerpt"
  TARGET: end
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Unspecified
MOOD: Grim
CHARACTERS: Narrator, Police Officers
BACKGROUND_IMAGE: crime_scene.png
BACKGROUND_EDIT: "Room with deceased individuals, police presence"

::SCRIPT::
- CHARACTER: Narrator
  LINE: ). It is very clear now that they are DEAD.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Two police officers survey the room.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: HARD CUTS to the man and woman being ZIPPED UP into body bags.
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue"
  TARGET: terri_bedroom
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Terri’s Bedroom
MOOD: Disturbing
CHARACTERS: Narrator, Terri
BACKGROUND_IMAGE: terri_bedroom.png
BACKGROUND_EDIT: "Bedroom floor, desk with laptop, gardening hose taped to mouth"

::SCRIPT::
- CHARACTER: Narrator
  LINE: TERRI (24), Dani’s sister, sits on the floor of her bedroom, beside her desk. The end of the other gardening hose has been DUCT-TAPED TO HER MOUTH. A mess of vomit has dried around the edges of the hastily applied tape.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: On Terri’s desk: her LAPTOP. It is open to the EMAIL THREAD between her and Dani. In the bottom right corner of the screen: “3 New Messages from Dani Ardor.”
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue"
  TARGET: street_brooklyn
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Street - Brooklyn
MOOD: Hesitant Urgency
CHARACTERS: Narrator, Christian
BACKGROUND_IMAGE: street_brooklyn.png
BACKGROUND_EDIT: "Snowy Brooklyn street at night, Christian running"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Dreamy snowfall in Brooklyn.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Christian, bundled up in layers, RUNS down the street. He’s approaching DANI’S BUILDING, but even as he rushes, he’s not going as fast as he possibly could. There’s an ambivalence in his stride.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: He enters the front door of Dani’s building.
  EXPRESSION: null

::PATHS::
- CHOICE: "Enter the apartment"
  TARGET: dani_apartment
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Dani’s Apartment - Living Room
MOOD: Despair
CHARACTERS: Narrator, Christian, Dani
BACKGROUND_IMAGE: dani_living_room.png
BACKGROUND_EDIT: "Living room, Dani weeping in Christian's lap, snowy window"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Wide on the LIVING ROOM. We’re centered on the COUCH, where Christian sits. Dani has crumbled there, her head shaking violently against Christian’s lap as she WEEPS. Behind them: a WINDOW showcases snowfall against the dark night.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Dani’s sobs are possessed of a profound despair. It’s so intense that it looks painful - dangerous even.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: We are pushing in on this, toward them. Christian’s eyes are wide with worry. A worry that goes beyond Dani’s well-being. He stares into space, imagining a future that he’s being chained to. He looks TRAPPED.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: We continue pushing toward them until we have pushed PAST them. The window behind them FILLS our frame. Through the window - HEAVY SNOW raging in a black vacuum. We hold on this as our OPENING CREDITS ROLL, accompanied by intense, groaning score.
  EXPRESSION: null

::PATHS::
- CHOICE: "Transition to next scene"
  TARGET: dani_bedroom_later
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Dani’s Bedroom
MOOD: Numbness, Anticipation
CHARACTERS: Narrator, Dani, Christian
BACKGROUND_IMAGE: dani_bedroom_6months_later.png
BACKGROUND_EDIT: "Dani's bedroom, late afternoon, 6 months later"

::SCRIPT::
- CHARACTER: Narrator
  LINE: DAYLIGHT. We are still looking out the window, but it’s now late afternoon. LATE SPRING.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Dani lies on her bed, fully clothed. Her eyes are numb as she stares at the wall.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: A KNOCK at the door. A well-dressed Christian pops his head in. He’s grown a beard since we last saw him.
  EXPRESSION: null
- CHARACTER: Christian
  LINE: Hey babers. How we feeling?
  EXPRESSION: Casual
- CHARACTER: Dani
  LINE: Hey.
  EXPRESSION: Neutral
- CHARACTER: Dani
  LINE: I’m up.
  EXPRESSION: Neutral
- CHARACTER: Christian
  LINE: I’m just going to that party for like 45 minutes. You should keep sleeping.
  EXPRESSION: Casual
- CHARACTER: Dani
  LINE: Oh - I’ll come with you...!
  EXPRESSION: Eager
- CHARACTER: Christian
  LINE: You sure you got enough rest?
  EXPRESSION: Hesitant
- CHARACTER: Dani
  LINE: I wasn’t sleeping anyway.
  EXPRESSION: Resigned
- CHARACTER: Christian
  LINE: Okay, great! Well, I was gonna leave in like three minutes, so I’ll just be at the door.
  EXPRESSION: Agreeable
- CHARACTER: Dani
  LINE: Okay. I’ll just get dressed.
  EXPRESSION: Agreeable
- CHARACTER: Narrator
  LINE: Christian nods for a little too long, then “smiles” and leaves the room. Dani rises. Stands for a moment. Heavy.
  EXPRESSION: null

::PATHS::
- CHOICE: "Go to the party"
  TARGET: apartment_party
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Apartment Party
MOOD: Social, Undercurrent of Deception
CHARACTERS: Narrator, Dani, Christian, Josh, Mark, Pelle, Hipster Guy
BACKGROUND_IMAGE: apartment_party.png
BACKGROUND_EDIT: "Brownstone apartment full of young people, evening"

::SCRIPT::
- CHARACTER: Narrator
  LINE: A PARTY in a brownstone full of circulating twenty-somethings.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Dani stands with Christian, who chats with Josh, Mark (holding two beers), Pelle, and a stoned HIPSTER GUY (26).
  EXPRESSION: null
- CHARACTER: Hipster Guy
  LINE: I’m fucking dreading the summer. Stuck in Boulder while my dad watches Law & Order all day.
  EXPRESSION: Complaining
- CHARACTER: Mark
  LINE: Yeah, man - I have to visit my parents in shit-ass Tucson after we all get back.
  EXPRESSION: Complaining
- CHARACTER: Narrator
  LINE: Dani squints with curiosity. Christian suddenly looks nervous.
  EXPRESSION: null
- CHARACTER: Hipster Guy
  LINE: Oh - you guys are going somewhere?
  EXPRESSION: Curious
- CHARACTER: Josh
  LINE: To Sweden!
  EXPRESSION: Excited
- CHARACTER: Pelle
  LINE: Hälsingland.
  EXPRESSION: Excited
- CHARACTER: Mark
  LINE: Mr. Pelle’s invited us for an authentic hippie midsummer at his yodeling farm.
  EXPRESSION: Excited
- CHARACTER: Narrator
  LINE: Dani has PAUSED. She hadn’t heard this before.
  EXPRESSION: null
- CHARACTER: Dani
  LINE: ...Oh yeah?
  EXPRESSION: Surprised
- CHARACTER: Narrator
  LINE: Dani turns to Christian, who now looks semi-panicked.
  EXPRESSION: null
- CHARACTER: Christian
  LINE: I mean, yeah, we were thinking about maybe - we were talking about it.
  EXPRESSION: Evasive
- CHARACTER: Dani
  LINE: For when?
  EXPRESSION: Inquiring
- CHARACTER: Narrator
  LINE: Dani feigns casualness as she looks inquiringly to the guys.
  EXPRESSION: null
- CHARACTER: Josh
  LINE: ...Mid June to late July?
  EXPRESSION: Casual
- CHARACTER: Mark
  LINE: In two weeks.
  EXPRESSION: Casual
- CHARACTER: Christian
  LINE: I mean, if we even go. I probably won’t. We were just talking about it.
  EXPRESSION: Dismissive
- CHARACTER: Narrator
  LINE: Mark, Josh and Pelle stand awkwardly, confused. Christian clearly hasn’t been honest with Dani.
  EXPRESSION: null

::PATHS::
- CHOICE: "Leave the party"
  TARGET: subway_train
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Subway - Moving
MOOD: Tense Silence
CHARACTERS: Narrator, Christian, Dani
BACKGROUND_IMAGE: subway_train.png
BACKGROUND_EDIT: "L train carriage, moving at night"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Christian and Dani ride the L train back home.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Christian stands, gripping the rail. Dani sits to his side. Her eyes are BUSY with nagging, paranoid thoughts. Christian, very tense, looks down at her from the corner of his eye.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Dani looks up at Christian uncertainly. Christian forces a casual “hey” smile. She “smiles” back.
  EXPRESSION: null

::PATHS::
- CHOICE: "Go to Christian's apartment"
  TARGET: christians_apartment
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Christian’s Apartment
MOOD: Confrontational
CHARACTERS: Narrator, Christian, Dani
BACKGROUND_IMAGE: christians_apartment.png
BACKGROUND_EDIT: "Apartment filled with cultural artifacts, evening"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Christian’s apartment is choked with cultural artifacts (pieces acquired in China, South America, Africa, etc.).
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The door opens. Christian and Dani enter. Christian goes to his laptop and turns it on. Dani stays by the door, still preoccupied. Christian looks to her.
  EXPRESSION: null
- CHARACTER: Christian
  LINE: Are you okay?
  EXPRESSION: Concerned
- CHARACTER: Narrator
  LINE: Dani looks at him, hesitant to start a fight. Christian gives her an impatient look: “Yes? No?”
  EXPRESSION: null
- CHARACTER: Dani
  LINE: I mean - yeah. I’m okay. That was just...very weird.
  EXPRESSION: Hesitant
- CHARACTER: Christian
  LINE: What was?
  EXPRESSION: Feigning Ignorance
- CHARACTER: Narrator
  LINE: Dani looks at him: “Seriously?” Christian widens his eyes: “What was weird?”
  EXPRESSION: null
- CHARACTER: Dani
  LINE: The...Sweden! I had no idea.
  EXPRESSION: Accusatory
- CHARACTER: Christian
  LINE: Well - what do you mean? I told you I wanted to go.
  EXPRESSION: Defensive
- CHARACTER: Dani
  LINE: Okay, fine, but I didn’t know you were going.
  EXPRESSION: Frustrated
- CHARACTER: Christian
  LINE: Well, I just decided today. I wasn’t keeping it from you.
  EXPRESSION: Defensive
- CHARACTER: Dani
  LINE: You already have a ticket!
  EXPRESSION: Accusatory
- CHARACTER: Narrator
  LINE: Beat. Christian now looks cornered.
  EXPRESSION: null
- CHARACTER: Christian
  LINE: I’m sorry.
  EXPRESSION: Resigned
- CHARACTER: Narrator
  LINE: Christian looks extremely defensive. He has LOCKED DOWN. Dani sees this, gathers herself, and tries to explain:
  EXPRESSION: null
- CHARACTER: Dani
  LINE: It’s just -- imagine if we were at a party and someone asks "what are you doing this summer," and my friends say: "oh, we’re all going to Alaska for three months, A month and a half. we’re leaving in two weeks,” and imagine that was the first you’d ever heard of it!
  EXPRESSION: Explanatory
- CHARACTER: Christian
  LINE: (correcting) A month and a half.
  EXPRESSION: Pedantic
- CHARACTER: Christian
  LINE: Okay: I told you I wanted to go to Sweden.
  EXPRESSION: Defensive
- CHARACTER: Dani
  LINE: You told me it would be “cool to go.”
  EXPRESSION: Clarifying
- CHARACTER: Christian
  LINE: Yeah! And then I got the opportunity to go and I decided to do it.
  EXPRESSION: Justifying
- CHARACTER: Dani
  LINE: I have no problem with you going! I just wish you'd involve me!
  EXPRESSION: Frustrated
- CHARACTER: Christian
  LINE: Well, I just apologized, Dani.
  EXPRESSION: Defensive
- CHARACTER: Dani
  LINE: You didn't apologize, you said - (shrugs) - "sorry." Which sounds more like "too bad."
  EXPRESSION: Frustrated
- CHARACTER: Narrator
  LINE: Beat. Christian’s eyes are now very cold.
  EXPRESSION: null
- CHARACTER: Christian
  LINE: Maybe I should just go home.
  EXPRESSION: Cold
- CHARACTER: Dani
  LINE: ...I’m just trying to understand.
  EXPRESSION: Pleading
- CHARACTER: Christian
  LINE: And I tried apologizing.
  EXPRESSION: Defensive
- CHARACTER: Dani
  LINE: I don't need an apology. I just wanna talk about it.
  EXPRESSION: Pleading
- CHARACTER: Narrator
  LINE: Pause.
  EXPRESSION: null
- CHARACTER: Christian
  LINE: I think I should just prob’ly go home.
  EXPRESSION: Cold
- CHARACTER: Narrator
  LINE: Dani looks helpless.
  EXPRESSION: null
- CHARACTER: Dani
  LINE: I'm not trying to attack you.
  EXPRESSION: Pleading
- CHARACTER: Christian
  LINE: Well, it feels like that.
  EXPRESSION: Defensive
- CHARACTER: Dani
  LINE: Well -- I’m sorry! I am sorry. I just got confused.
  EXPRESSION: Pleading
- CHARACTER: Narrator
  LINE: Christian’s eyes, looking down, haven’t begun to thaw. Dani, now desperate to reverse the mood, sits on the couch. She beckons him.
  EXPRESSION: null
- CHARACTER: Dani
  LINE: Come on: Sit with me. I'm sorry. That just felt weird, that's all. I think going to Sweden could be really great for you. That sounds amazing. Are you going for your thesis?
  EXPRESSION: Soothing
- CHARACTER: Christian
  LINE: (quietly) I don’t know what my thesis is.
  EXPRESSION: Lost
- CHARACTER: Dani
  LINE: (brightly) I know! It could be inspiring! Right?
  EXPRESSION: Optimistic
- CHARACTER: Christian
  LINE: (still looking down) -- I think I’m just gonna leave.
  EXPRESSION: Determined
- CHARACTER: Narrator
  LINE: Dani’s eyes start to well intensely with TEARS.
  EXPRESSION: null
- CHARACTER: Dani
  LINE: Please. I'm sorry. I didn't mean to overreact. Please.
  EXPRESSION: Desperate
- CHARACTER: Narrator
  LINE: Christian SOFTENS when he sees that she’s crying. Still distant, he sits with her.
  EXPRESSION: null
- CHARACTER: Christian
  LINE: Okay - shhh. It’s okay. I’m sorry, too. All right?
  EXPRESSION: Soothing
- CHARACTER: Dani
  LINE: I get paranoid. I'm sorry. I'm going through all this stuff and I've been dealing with all this panic and I just - overreacted. I'm not trying to put pressure or accuse you of anything. I just got crazy for a second. I didn't mean to project.
  EXPRESSION: Apologetic
- CHARACTER: Christian
  LINE: It’s okay. I’m sorry, too. It’s okay.
  EXPRESSION: Reassuring
- CHARACTER: Narrator
  LINE: Beat.
  EXPRESSION: null
- CHARACTER: Christian
  LINE: (uncertainly) I was gonna ask you to come with me.
  EXPRESSION: Hesitant
- CHARACTER: Narrator
  LINE: Pause. Dani looks at him.
  EXPRESSION: null
- CHARACTER: Dani
  LINE: What do you mean?
  EXPRESSION: Curious
- CHARACTER: Christian
  LINE: -- What I just said.
  EXPRESSION: Direct
- CHARACTER: Dani
  LINE: To Sweden?
  EXPRESSION: Surprised
- CHARACTER: Narrator
  LINE: Christian nods a stiff “yes.”
  EXPRESSION: null
- CHARACTER: Dani
  LINE: You don’t want me to.
  EXPRESSION: Hurt
- CHARACTER: Christian
  LINE: I just asked you.
  EXPRESSION: Defensive
- CHARACTER: Dani
  LINE: After I broke down crying!
  EXPRESSION: Hurt
- CHARACTER: Christian
  LINE: Well...you ruined the surprise.
  EXPRESSION: Petty
- CHARACTER: Narrator
  LINE: Dani searches Christian’s eyes. They aren’t especially warm.
  EXPRESSION: null
- CHARACTER: Christian
  LINE: I wanted it to be romantic.
  EXPRESSION: Justifying

::PATHS::
- CHOICE: "Continue"
  TARGET: marks_joshs_apartment
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Mark & Josh’s Apartment
MOOD: Relaxed, Preoccupied
CHARACTERS: Narrator, Christian, Mark, Josh, Pelle
BACKGROUND_IMAGE: marks_joshs_apartment.png
BACKGROUND_EDIT: "Stoner den mixed with anthropologist's study, smoking bong"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Mark & Josh’s apartment is essentially a stoner’s den crossed with a serious anthropologist’s home. Ironic posters (a portrait of Ronald Reagan, etc.) are countered by a huge poster of James George Frazer. There are stacks of books in every corner.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Christian, Mark, Pelle and Josh sit in the living room, smoking from a bong. Josh holds a book by Johannes Bureus (titled Adalruna) and Pelle is drawing in his notepad.
  EXPRESSION: null
- CHARACTER: Josh
  LINE: Are the Swedes sensitive about their history of Nazi collaboration?
  EXPRESSION: Curious
- CHARACTER: Pelle
  LINE: Are you sensitive about Hiroshima? Or slavery? Or the trail of tears?
  EXPRESSION: Sarcastic
- CHARACTER: Josh
  LINE: (deadpan) Yes.
  EXPRESSION: Deadpan
- CHARACTER: Narrator
  LINE: Christian looks extremely preoccupied. His foot pumps involuntarily. He receives a TEXT.
  EXPRESSION: null
- CHARACTER: Christian
  LINE: (anxiously) Hey guys, it’s Dani - she’s coming up.
  EXPRESSION: Anxious
- CHARACTER: Mark
  LINE: ...Okay.
  EXPRESSION: Neutral
- CHARACTER: Josh
  LINE: (re: weed and bong) Should we clear all this?
  EXPRESSION: Concerned
- CHARACTER: Christian
  LINE: No no, it doesn’t matter. But uh - listen...
  EXPRESSION: Casual
- CHARACTER: Narrator
  LINE: Christian goes to buzz her in.
  EXPRESSION: null
- CHARACTER: Christian
  LINE: ...just so you guys know: she’s not gonna actually come, but I invited her on the trip. Just to not make it weird.
  EXPRESSION: Strategic
- CHARACTER: Narrator
  LINE: A moment of silence. Pelle sits especially frozen.
  EXPRESSION: null
- CHARACTER: Mark
  LINE: You invited her?
  EXPRESSION: Surprised
- CHARACTER: Christian
  LINE: Yeah, but she’s not coming.
  EXPRESSION: Definitive
- CHARACTER: Josh
  LINE: She doesn’t want to?
  EXPRESSION: Curious
- CHARACTER: Christian
  LINE: (measuredly) No: I "invited" her and she "accepted," but she's not gonna actually come.
  EXPRESSION: Measured
- CHARACTER: Narrator
  LINE: Mark and Josh just stare at him.
  EXPRESSION: null
- CHARACTER: Christian
  LINE: You guys know what she’s dealing with!
  EXPRESSION: Justifying
- CHARACTER: Mark
  LINE: No, we know. I just didn’t realize. It’s totally fine if she joins.
  EXPRESSION: Understanding
- CHARACTER: Josh
  LINE: Yeah, dude, nobody minds.
  EXPRESSION: Agreeable
- CHARACTER: Narrator
  LINE: A KNO
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue"
  TARGET: end
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Not Specified (Implied: A room with Christian, Josh, Mark, and Pelle)
MOOD: Casual but expectant
CHARACTERS: Christian, Dani, Josh, Mark, Pelle
BACKGROUND_IMAGE: not_specified.png
BACKGROUND_EDIT: "Interior, a gathering of friends"

::SCRIPT::
- CHARACTER: Christian
  LINE: Okay, so just: you guys told me to invite her and you know that she’s coming. Agreed?
  EXPRESSION: Assertive
- CHARACTER: Narrator
  LINE: They don’t respond.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Christian now OPENS the door to DANI.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: She enters with an almost apologetic smile on her face.
  EXPRESSION: null
- CHARACTER: Dani
  LINE: Hey.
  EXPRESSION: Apologetic
- CHARACTER: Dani
  LINE: Hey guys!
  EXPRESSION: Cheerful
- CHARACTER: Christian
  LINE: Hi baby.
  EXPRESSION: Affectionate
- CHARACTER: Josh, Mark, Pelle
  LINE: Hey!
  EXPRESSION: Cheerful
- CHARACTER: Dani
  LINE: How’s it going?
  EXPRESSION: Inquisitive
- CHARACTER: Mark
  LINE: Just chillin’.
  EXPRESSION: Relaxed
- CHARACTER: Dani
  LINE: Nice.
  EXPRESSION: Content
- CHARACTER: Narrator
  LINE: A brief, awkward pause.
  EXPRESSION: null
- CHARACTER: Josh
  LINE: So, Sweden--!
  EXPRESSION: Excited
- CHARACTER: Dani
  LINE: Yeah!
  EXPRESSION: Excited
- CHARACTER: Pelle
  LINE: You’re coming, right?
  EXPRESSION: Hopeful
- CHARACTER: Dani
  LINE: I think so--! If it’s not completely destroying your guys’ male bonding plans.
  EXPRESSION: Playful
- CHARACTER: Mark, Josh, Pelle
  LINE: Nope. / Not at all.
  EXPRESSION: Dismissive
- CHARACTER: Christian
  LINE: Oh, shut the fuck up.
  EXPRESSION: Playful
- CHARACTER: Narrator
  LINE: Dani smiles bashfully.
  EXPRESSION: Shy
- CHARACTER: Narrator
  LINE: Mark abruptly addresses Christian:
  EXPRESSION: null
- CHARACTER: Mark
  LINE: Hey man, can I get you to look at that paragraph real quick?
  EXPRESSION: Casual
- CHARACTER: Christian
  LINE: Sure. Yeah. Okay.
  EXPRESSION: Confused
- CHARACTER: Christian
  LINE: Right back.
  EXPRESSION: Casual
- CHARACTER: Narrator
  LINE: Christian kisses Dani, and leaves the room with Mark.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Dani looks to the ROOM. Josh has returned to his book. Pelle, alone on the couch, warmly gestures for Dani to join him. She obliges.
  EXPRESSION: null
- CHARACTER: Dani
  LINE: Hey Pelle.
  EXPRESSION: Friendly
- CHARACTER: Pelle
  LINE: Hi Dani.
  EXPRESSION: Friendly
- CHARACTER: Narrator
  LINE: She notices that Pelle has been composing a DRAWING in his notepad. It’s a drawing of the room.
  EXPRESSION: null
- CHARACTER: Dani
  LINE: Ooh, that’s a nice drawing.
  EXPRESSION: Admiring
- CHARACTER: Pelle
  LINE: Oh, thanks, yeah, I’m trying to be a naturalist.
  EXPRESSION: Humble
- CHARACTER: Narrator
  LINE: Pelle closes the drawing pad. Gives Dani his full attention.
  EXPRESSION: null
- CHARACTER: Dani
  LINE: How’ve you been?
  EXPRESSION: Inquisitive
- CHARACTER: Pelle
  LINE: Pretty good! Survived finals. You?
  EXPRESSION: Enthusiastic
- CHARACTER: Dani
  LINE: Uh, well - didn’t quite finish! But they’re giving me a break this year...
  EXPRESSION: Resigned
- CHARACTER: Pelle
  LINE: Oh, right. God. Of course.
  EXPRESSION: Realizing
- CHARACTER: Narrator
  LINE: Dani makes an embarrassed “bleh” face.
  EXPRESSION: Embarrassed
- CHARACTER: Dani
  LINE: How did you like the anthropology department?
  EXPRESSION: Curious
- CHARACTER: Pelle
  LINE: It’s good! I just can’t seem to choose if I hate academia or not. Unlike this one. You’re doing psychiatry?
  EXPRESSION: Thoughtful
- CHARACTER: Dani
  LINE: Psychology. Yeah. That’s how you know I’m nuts.
  EXPRESSION: Self-deprecating
- CHARACTER: Pelle
  LINE: Also that funny look in your eye.
  EXPRESSION: Teasing
- CHARACTER: Narrator
  LINE: Dani LAUGHS, a bit unnaturally. An awkward moment.
  EXPRESSION: null
- CHARACTER: Pelle
  LINE: So! You’re coming to Hälsingland!
  EXPRESSION: Excited
- CHARACTER: Dani
  LINE: Yeah! I can’t wait. Christian says you’ve got a special thing in the woods planned?
  EXPRESSION: Eager
- CHARACTER: Pelle
  LINE: Oh yeah - a sort of crazy, nine-day festival we’re doing...
  EXPRESSION: Enthusiastic
- CHARACTER: Dani
  LINE: Do you do that every midsummer?
  EXPRESSION: Curious
- CHARACTER: Pelle
  LINE: Uh - well...not quite like this one.
  EXPRESSION: Hesitant
- CHARACTER: Dani
  LINE: Ooh. What makes this guy different?
  EXPRESSION: Playful
- CHARACTER: Pelle
  LINE: Well, “this guy” happens only once every ninety years. So it’ll be a first and a last for everybody.
  EXPRESSION: Mysterious
- CHARACTER: Narrator
  LINE: Pelle raises his eyebrows, mock-menacing.
  EXPRESSION: null
- CHARACTER: Dani
  LINE: ...Christian says you’re from a really small community?
  EXPRESSION: Inquisitive
- CHARACTER: Pelle
  LINE: Oh yes - tiny. Very sort of... Incestuous? Incestual?
  EXPRESSION: Searching
- CHARACTER: Dani
  LINE: Depends on which of those you mean.
  EXPRESSION: Witty
- CHARACTER: Pelle
  LINE: Oh - ha! No: we’re just very secluded...
  EXPRESSION: Reassuring
- CHARACTER: Narrator
  LINE: Pelle pulls up a PHOTO on his phone. Shows it to Dani. It features a lush, impossibly green field. Young men and women stand about - all dressed like hippies in white.
  EXPRESSION: null
- CHARACTER: Dani
  LINE: Oh wow! Flower children.
  EXPRESSION: Amazed
- CHARACTER: Pelle
  LINE: Big time! We do our own thing, love our astrology...
  EXPRESSION: Proud
- CHARACTER: Dani
  LINE: What’s your sign?
  EXPRESSION: Playful
- CHARACTER: Pelle
  LINE: Taurus! You?
  EXPRESSION: Eager
- CHARACTER: Dani
  LINE: Cancer!
  EXPRESSION: Playful
- CHARACTER: Pelle
  LINE: Ooh, yes, I do see that. Your birthday?
  EXPRESSION: Observing
- CHARACTER: Dani
  LINE: July seven.
  EXPRESSION: Casual
- CHARACTER: Narrator
  LINE: Pelle makes an “Ah” face. A thoughtful pause before he asserts:
  EXPRESSION: null
- CHARACTER: Pelle
  LINE: You know, I think it’s actually very good you’re coming.
  EXPRESSION: Sincere
- CHARACTER: Dani
  LINE: Oh yeah? For who?
  EXPRESSION: Curious
- CHARACTER: Pelle
  LINE: For you! And for my family. I think you’ll be very...
  EXPRESSION: Suggestive
- CHARACTER: Narrator
  LINE: Pelle weaves his fingers together, signifying a tight-knit connection. Dani smiles.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Pelle PAUSES again, and his tone now CHANGES. He leans forward, sensitively:
  EXPRESSION: null
- CHARACTER: Pelle
  LINE: You know...I never had the chance to tell you, but I was really so very sorry to hear about - your loss...
  EXPRESSION: Empathetic
- CHARACTER: Dani
  LINE: Oh...!
  EXPRESSION: Surprised
- CHARACTER: Pelle
  LINE: ...and what happened. I can’t even fathom. I mean, I lost my parents, too, so I have some idea, but...
  EXPRESSION: Sympathetic
- CHARACTER: Narrator
  LINE: Dani looks cornered. TEARS have welled up in her eyes.
  EXPRESSION: null
- CHARACTER: Pelle
  LINE: Oh, no. Sorry to bring it up!
  EXPRESSION: Regretful
- CHARACTER: Dani
  LINE: No, I mean - thank you. I just... I'm sorry.
  EXPRESSION: Distraught
- CHARACTER: Narrator
  LINE: (stands up suddenly)
  EXPRESSION: null
- CHARACTER: Dani
  LINE: I'll be right back. Bathroom. Thank you.
  EXPRESSION: Flustered
- CHARACTER: Narrator
  LINE: Dani rushes off. Pelle watches her with blank eyes.
  EXPRESSION: null

::SCENE::
LOCATION: Airplane Lavatory
MOOD: Grief
CHARACTERS: Dani
BACKGROUND_IMAGE: airplane_lavatory.png
BACKGROUND_EDIT: "In-flight lavatory, Dani crying"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Dani, stifling tears, enters the BATHROOM.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Dani has entered an airplane’s lavatory, stifling an oncoming deluge. After shutting the door behind her, she BREAKS DOWN in a fit of violent SOBS.
  EXPRESSION: Grief-stricken

::SCENE::
LOCATION: Airplane Cabin
MOOD: Somber but hopeful
CHARACTERS: Dani, Christian
BACKGROUND_IMAGE: airplane_cabin.png
BACKGROUND_EDIT: "In-flight cabin, passengers, Dani and Christian seated"

::SCRIPT::
- CHARACTER: Narrator
  LINE: We are WIDE, looking down the length of the plane. We track forward, drifting over the heads of passengers.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: In the b.g., Dani exits the lavatory and returns to her seat. Christian is seated beside her at the window. We have arrived at a PROFILE CU of them (the window in the b.g.).
  EXPRESSION: null
- CHARACTER: Christian
  LINE: Hand gesture - takes Dani's hand and smiles at her.
  EXPRESSION: Reassuring
- CHARACTER: Narrator
  LINE: It’s clear she’s been crying, but she hides it behind a determinedly casual “all is well” expression.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Christian goes along with the pretending, and looks out the WINDOW. We have begun a slow ZOOM past them, toward the window. The window soon FILLS the frame. We are flying over beautiful terrain. We have entered SWEDEN.
  EXPRESSION: null

::SCENE::
LOCATION: Stockholm Airport
MOOD: Transition
CHARACTERS: Dani, Christian, Josh, Mark, Pelle, Customs Officer
BACKGROUND_IMAGE: stockholm_airport.png
BACKGROUND_EDIT: "Airport customs area"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Dani, Christian, Josh, Mark and Pelle stand at a CUSTOMS DESK.
  EXPRESSION: null
- CHARACTER: Customs Officer
  LINE: Purpose of your trip?
  EXPRESSION: Neutral
- CHARACTER: Pelle
  LINE: Visiting my home in Hälsingland.
  EXPRESSION: Direct
- CHARACTER: Customs Officer
  LINE: All of you?
  EXPRESSION: Inquisitive
- CHARACTER: Narrator
  LINE: They all say “yes.”
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Christian, meanwhile, is desperately searching his backpack for his passport.
  EXPRESSION: Anxious
- CHARACTER: Narrator
  LINE: The Customs Officer scrutinizes Dani’s passport.
  EXPRESSION: Neutral
- CHARACTER: Customs Officer
  LINE: Happy birthday tomorrow.
  EXPRESSION: Friendly
- CHARACTER: Dani
  LINE: Oh - thank you.
  EXPRESSION: Pleased
- CHARACTER: Narrator
  LINE: Christian, distracted from that, FINDS his passport.
  EXPRESSION: Relieved

::SCENE::
LOCATION: Rental Minivan
MOOD: Road trip, lighthearted
CHARACTERS: Pelle, Mark, Dani, Christian, Josh
BACKGROUND_IMAGE: rental_minivan.png
BACKGROUND_EDIT: "Moving vehicle, Stockholm traffic"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Our group, now in a rental minivan, drives through Stockholm traffic. Pelle is at the wheel.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Mark sits passenger, holding a film theory book. In the back: Dani, Christian and Josh. Josh is reading the Poetic Edda.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: They pass a group of BEAUTIFUL BLONDE WOMEN.
  EXPRESSION: null
- CHARACTER: Mark
  LINE: Oh my God, dude, the women here...!
  EXPRESSION: Awed
- CHARACTER: Narrator
  LINE: Christian, aware of Dani, gives a self-conscious half-nod. Dani happily pretends to ignore this.
  EXPRESSION: null
- CHARACTER: Mark
  LINE: What is it that makes them hotter?
  EXPRESSION: Curious
- CHARACTER: Christian
  LINE: The Vikings grabbed all the best ones and dragged them over.
  EXPRESSION: Jokingly
- CHARACTER: Josh
  LINE: Makes a pretty good case for rape, from a nationalist point of view.
  EXPRESSION: Provocative
- CHARACTER: Narrator
  LINE: Dani WINCES at that one.
  EXPRESSION: Uncomfortable
- CHARACTER: Narrator
  LINE: They have now pulled onto the FREEWAY - leaving Stockholm.
  EXPRESSION: null
- CHARACTER: Dani
  LINE: How far are we driving?
  EXPRESSION: Inquisitive
- CHARACTER: Pelle
  LINE: Four hours, about.
  EXPRESSION: Direct
- CHARACTER: Mark
  LINE: Oh my God.
  EXPRESSION: Exasperated
- CHARACTER: Narrator
  LINE: Dani notices a book on Josh’s lap: The Secret Nazi Language of the Uthark. Its cover is a runic pattern.
  EXPRESSION: null
- CHARACTER: Dani
  LINE: Why are you reading that?
  EXPRESSION: Curious
- CHARACTER: Josh
  LINE: Ha. Ask Pelle.
  EXPRESSION: Teasing
- CHARACTER: Pelle
  LINE: We’re taught the runic alphabet in my village. Josh just carries that around to annoy me.
  EXPRESSION: Explaining
- CHARACTER: Dani
  LINE: What are you doing your thesis on, again?
  EXPRESSION: Curious
- CHARACTER: Josh
  LINE: Uhhhh - Well! My focus is actually on European midsummer traditions. Which was actually sorta the impetus behind this whole trip.
  EXPRESSION: Enthusiastic
- CHARACTER: Dani
  LINE: That’s similar to what you’re thinking of doing - right, baby? For your thesis?
  EXPRESSION: Connecting
- CHARACTER: Christian
  LINE: Well, I don’t know quite what I’m doing.
  EXPRESSION: Uncertain
- CHARACTER: Christian
  LINE: But I’m thinking about rooting it in something Scandinavian.
  EXPRESSION: Considering
- CHARACTER: Dani
  LINE: See that, Pelle? You’ve managed to brainwash all your friends.
  EXPRESSION: Playful
- CHARACTER: Pelle
  LINE: Josh was already brainwashed when I found him.
  EXPRESSION: Amused
- CHARACTER: Josh
  LINE: Thank you.
  EXPRESSION: Sarcastic

::SCENE::
LOCATION: Rental Minivan
MOOD: Quiet, observant
CHARACTERS: Pelle, Christian, Mark, Josh, Dani
BACKGROUND_IMAGE: rental_minivan.png
BACKGROUND_EDIT: "Moving vehicle, rural landscape"

::SCRIPT::
- CHARACTER: Narrator
  LINE: DISSOLVE TO: TWO HOURS LATER
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Pelle is still driving. Everyone is silent and zoning out as the radio plays an old Swedish folk tune.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Mark suddenly notices a DEAD BOAR on the side of the road.
  EXPRESSION: null
- CHARACTER: Mark
  LINE: That’s the second of those I’ve seen.
  EXPRESSION: Noticing
- CHARACTER: Pelle
  LINE: Yeah, they’re a huge problem out here. Everybody hunts them.
  EXPRESSION: Informative
- CHARACTER: Mark
  LINE: You ever gone boar huntin’?
  EXPRESSION: Curious
- CHARACTER: Pelle
  LINE: Yep!
  EXPRESSION: Direct
- CHARACTER: Mark
  LINE: Is it fun?
  EXPRESSION: Inquisitive
- CHARACTER: Pelle
  LINE: ...It’s cathartic and then it’s sad.
  EXPRESSION: Reflective
- CHARACTER: Narrator
  LINE: Beat. They drive past another dead boar, also in a field.
  EXPRESSION: null
- CHARACTER: Josh
  LINE: They’re allowed to just leave them?
  EXPRESSION: Surprised
- CHARACTER: Narrator
  LINE: Mark alights on something ahead.
  EXPRESSION: null
- CHARACTER: Mark
  LINE: ...the fuck?
  EXPRESSION: Shocked
- CHARACTER: Narrator
  LINE: Everyone looks up. In the distance, about 300 feet off the road, is an OAK TREE with SEVERAL BOAR CARCASSES HANGING FROM ITS BRANCHES.
  EXPRESSION: null
- CHARACTER: Christian
  LINE: What is that?
  EXPRESSION: Confused
- CHARACTER: Dani
  LINE: Oh my God.
  EXPRESSION: Horrified
- CHARACTER: Josh
  LINE: Wait: slow down. Can you pull over to it?
  EXPRESSION: Urgent
- CHARACTER: Dani
  LINE: Why??
  EXPRESSION: Fearful
- CHARACTER: Josh
  LINE: Please, Pelle.
  EXPRESSION: Pleading
- CHARACTER: Narrator
  LINE: Pelle reluctantly slows down. He veers off the road and idles to a STOP beside the tree.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Josh marvels at it.
  EXPRESSION: Stunned

::SCENE::
LOCATION: Roadside - Oak Tree
MOOD: Disturbing, ritualistic
CHARACTERS: Josh, Pelle, Dani, Mark, Christian
BACKGROUND_IMAGE: roadside_oak_tree.png
BACKGROUND_EDIT: "Rural road, an oak tree with boar carcasses"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The back door opens and Josh emerges from the car. Everyone else filters out behind him.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Josh approaches the tree, stunned. A cacophony of buzzing FLIES.
  EXPRESSION: null
- CHARACTER: Josh
  LINE: Do you know what this is?
  EXPRESSION: Awed
- CHARACTER: Pelle
  LINE: No idea.
  EXPRESSION: Innocent
- CHARACTER: Narrator
  LINE: Josh has pulled out his CELL PHONE. He starts to take photographs of the tree from every possible angle.
  EXPRESSION: null
- CHARACTER: Dani
  LINE: This is horrible.
  EXPRESSION: Disturbed
- CHARACTER: Mark
  LINE: Is this how you people hunt out here?
  EXPRESSION: Skeptical
- CHARACTER: Christian
  LINE: It looks almost ritualistic.
  EXPRESSION: Speculative
- CHARACTER: Josh
  LINE: It looks absolutely ritualistic! This is fucking amazing.
  EXPRESSION: Ecstatic
- CHARACTER: Narrator
  LINE: Dani looks extremely disturbed. She swipes away flies. Christian pulls out his phone to take a single wide shot of the tree.
  EXPRESSION: null
- CHARACTER: Pelle
  LINE: Okay, let’s go. We still have a lot of driving.
  EXPRESSION: Impatient
- CHARACTER: Dani
  LINE: Fantastic. Thank you.
  EXPRESSION: Sarcastic

::SCENE::
LOCATION: Rental Minivan
MOOD: Tired, quiet
CHARACTERS: Pelle, Christian, Dani, Mark, Josh
BACKGROUND_IMAGE: rental_minivan.png
BACKGROUND_EDIT: "Moving vehicle, rural landscape, later"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Everyone returns to the car. Except for Josh, who continues his ecstatic photo-taking.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Pelle is still driving. Christian sleeps in the back. Everyone looks notably more tired. It’s been a long drive.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: They pass a sign announcing (in Swedish) that they have arrived in Hälsingland.
  EXPRESSION: null
- CHARACTER: Pelle
  LINE: Entering Hälsingland!
  EXPRESSION: Announcing
- CHARACTER: Narrator
  LINE: Everyone looks up.
  EXPRESSION: null
- CHARACTER: Mark
  LINE: Are we getting high right when we get there?
  EXPRESSION: Eager
- CHARACTER: Narrator
  LINE: TEN MINUTES LATER
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Pelle idles up to a LARGE GRASSY MEADOW. It’s lush, impossibly green - magical. About fifty YOUNG PEOPLE (teens to twenties) lounge about. Tents and camping equipment abound. Many of the
  EXPRESSION: null

::SCENE::
LOCATION: Meadow
MOOD: Festive
CHARACTERS: Narrator, Pelle, Dani, Christian, Mark, Josh
BACKGROUND_IMAGE: meadow_festive.png
BACKGROUND_EDIT: "Women in white dresses and floral crowns, men like 19th century farmers"

::SCRIPT::
- CHARACTER: Narrator
  LINE: women are dressed in traditional white dresses and don floral garland crowns. Some of the men look like 19th century farmers.
  EXPRESSION: null
- CHARACTER: Pelle
  LINE: Look, guys! New friends.
  EXPRESSION: Cheerful
- CHARACTER: Narrator
  LINE: Pelle parks the minivan in the field.
  EXPRESSION: null

::PATHS::
- CHOICE: "Exit the minivan"
  TARGET: meadow_continuous
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Meadow - Continuous
MOOD: Mesmerized, Welcoming
CHARACTERS: Narrator, Pelle, Dani, Christian, Mark, Josh, Girls, Ingemar
BACKGROUND_IMAGE: meadow_continuous.png
BACKGROUND_EDIT: "People gathered in a field, some waving"

::SCRIPT::
- CHARACTER: Narrator
  LINE: They all emerge, yawning and stretching. Dani is mesmerized.
  EXPRESSION: null
- CHARACTER: Pelle
  LINE: WAVES to a bunch of people on the grass. They clearly know each other well. Pelle gestures for our group to follow him as he approaches a crowd of GIRLS.
  EXPRESSION: Friendly
- CHARACTER: Girls
  LINE: Pelle!!
  EXPRESSION: Excited
- CHARACTER: Narrator
  LINE: We cut WIDE as Pelle happily introduces everyone.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Then, across the field, a Chubby Blonde Guy (25) calls out to Pelle. This is INGEMAR.
  EXPRESSION: null
- CHARACTER: Ingemar
  LINE: (in Swedish) Holy shit! Pelle!!
  EXPRESSION: Surprised
- CHARACTER: Narrator
  LINE: Pelle turns to Ingemar. His face LIGHTS UP, and he runs over to him. Dani, Christian, Mark and Josh follow.
  EXPRESSION: null
- CHARACTER: Ingemar
  LINE: (in Swedish) Happy St. John’s!
  EXPRESSION: Joyful
- CHARACTER: Narrator
  LINE: Pelle laughs. They hug.
  EXPRESSION: null
- CHARACTER: Ingemar
  LINE: (in Swedish) Christ - you’re so skinny! Where’d the rest of you go?
  EXPRESSION: Teasing
- CHARACTER: Pelle
  LINE: (in Swedish) Looks like you got it.
  EXPRESSION: Amused
- CHARACTER: Ingemar
  LINE: (in Swedish) What the fuck? I look fatter?
  EXPRESSION: Concerned
- CHARACTER: Pelle
  LINE: Here: English. These are my great friends - Josh, Christian, Mark, Dani: meet my brother Ingemar. Best friend since we were babies.
  EXPRESSION: Introducing
- CHARACTER: Ingemar
  LINE: Josh, Christian, Mark... Dani? Awesome! And say hello to my friends, Simon and Connie from London.
  EXPRESSION: Recalling
- CHARACTER: Narrator
  LINE: He gestures to an attractive British couple, CONNIE (24, skinny) and SIMON (26, spectacled, tattooed).
  EXPRESSION: null
- CHARACTER: Ingemar
  LINE: Simon and Connie, this is Pelle and...all the names I just remembered two seconds ago.
  EXPRESSION: Joking
- CHARACTER: Simon
  LINE: Hey.
  EXPRESSION: Casual
- CHARACTER: Connie
  LINE: Hello.
  EXPRESSION: Friendly
- CHARACTER: Ingemar
  LINE: Perfect timing, by the way:
  EXPRESSION: Ominous
- CHARACTER: Narrator
  LINE: Ingemar pulls out a bag of MAGIC MUSHROOMS. Hands them to Pelle.
  EXPRESSION: null
- CHARACTER: Ingemar
  LINE: We just took these five minutes ago. Haven’t even started coming up yet.
  EXPRESSION: Excited
- CHARACTER: Mark
  LINE: Ohhh shit.
  EXPRESSION: Overjoyed
- CHARACTER: Narrator
  LINE: Mark grabs the bag from Pelle and studies the contents.
  EXPRESSION: null
- CHARACTER: Pelle
  LINE: Do you guys wanna take it now? Or should we settle in first?
  EXPRESSION: Questioning
- CHARACTER: Mark
  LINE: Fuck it. Let’s just take ‘em.
  EXPRESSION: Decisive
- CHARACTER: Dani
  LINE: (to Christian) I think I might need to find my footing first.
  EXPRESSION: Hesitant
- CHARACTER: Christian
  LINE: Yeah. Of course. (quietly) And you know you don’t need to take them. If you’re feeling unsure.
  EXPRESSION: Reassuring
- CHARACTER: Dani
  LINE: No, I just need to get settled.
  EXPRESSION: Firm
- CHARACTER: Christian
  LINE: Okay. Well. I’ll wait for you.
  EXPRESSION: Patient
- CHARACTER: Dani
  LINE: No - go ahead!
  EXPRESSION: Encouraging
- CHARACTER: Christian
  LINE: No, I’ll wait. We’ll come up together.
  EXPRESSION: Loyal
- CHARACTER: Narrator
  LINE: Josh and Mark and Pelle have pulled their mushrooms from the bag. They look to Christian, ready to go.
  EXPRESSION: null
- CHARACTER: Pelle
  LINE: Ready?
  EXPRESSION: Eager
- CHARACTER: Christian
  LINE: I’m waiting for Dani. You guys go on.
  EXPRESSION: Steadfast
- CHARACTER: Mark
  LINE: Dude. We can’t come up at different times. They’ll be totally separate trips.
  EXPRESSION: Frustrated
- CHARACTER: Christian
  LINE: Then you can wait for us.
  EXPRESSION: Insistent
- CHARACTER: Narrator
  LINE: Mark looks frustrated - angry even.
  EXPRESSION: null
- CHARACTER: Dani
  LINE: You know what? That’s okay. I’m ready.
  EXPRESSION: Resigned
- CHARACTER: Christian
  LINE: Baby. Don’t feel rushed.
  EXPRESSION: Gentle
- CHARACTER: Dani
  LINE: I don’t. I’m ready.
  EXPRESSION: Firm
- CHARACTER: Mark
  LINE: (false concern) You sure?
  EXPRESSION: Manipulative
- CHARACTER: Dani
  LINE: (bluntly) Yeah, Mark, thanks.
  EXPRESSION: Annoyed
- CHARACTER: Ingemar
  LINE: They made mushroom tea if you prefer against the taste.
  EXPRESSION: Helpful
- CHARACTER: Dani
  LINE: Okay. Yeah. I’ll have that. Thank you - Ingmar?
  EXPRESSION: Considering
- CHARACTER: Narrator
  LINE: Ingemar smiles confirmation and goes to fetch her a mug of tea.
  EXPRESSION: null
- CHARACTER: Christian
  LINE: Don’t let Mark pressure you. Of all people.
  EXPRESSION: Protective
- CHARACTER: Dani
  LINE: He’s not. It’ll get too complicated otherwise. It’s fine.
  EXPRESSION: Pragmatic
- CHARACTER: Narrator
  LINE: Ingemar hands Dani her TEA.
  EXPRESSION: null
- CHARACTER: Pelle
  LINE: (to Dani) Ready?
  EXPRESSION: Encouraging
- CHARACTER: Narrator
  LINE: Dani, now holding the tea, nods yes.
  EXPRESSION: null
- CHARACTER: Pelle
  LINE: Okay. Here we go. Think happy thoughts!
  EXPRESSION: Enthusiastic
- CHARACTER: Narrator
  LINE: They eat their shrooms. Dani hesitates before SIPPING the tea.
  EXPRESSION: null
- CHARACTER: Christian
  LINE: You okay?
  EXPRESSION: Concerned
- CHARACTER: Dani
  LINE: Yeah. It’s good. I’m excited.
  EXPRESSION: Optimistic
- CHARACTER: Christian
  LINE: Cool. Me too.
  EXPRESSION: Enthusiastic

::PATHS::
- CHOICE: "Take the mushrooms/tea"
  TARGET: meadow_minutes_later
  STATE_CHANGE: trip_started = true
  CONDITION: null

::SCENE::
LOCATION: Meadow - Minutes Later
MOOD: Unease, Nausea
CHARACTERS: Narrator, Dani, Christian, Pelle, Mark, Josh
BACKGROUND_IMAGE: meadow_unease.png
BACKGROUND_EDIT: "Group sitting on grass, one is retching, another is staring at hands"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Dani sits on the grass with Christian and Pelle. Mark is off to the side, stabbing at an ANT COLONY with a stick. Josh paces nearby. His stomach TURNS audibly.
  EXPRESSION: null
- CHARACTER: Josh
  LINE: Uggghhh, I really don’t feel good.
  EXPRESSION: Sick
- CHARACTER: Narrator
  LINE: Josh hunches over to RETCH.
  EXPRESSION: null
- CHARACTER: Mark
  LINE: Don’t puke, dude. Keep it down.
  EXPRESSION: Harsh
- CHARACTER: Christian
  LINE: (to Dani) How are you feeling?
  EXPRESSION: Concerned
- CHARACTER: Dani
  LINE: A little like I have food poisoning.
  EXPRESSION: Unwell
- CHARACTER: Pelle
  LINE: Technically you do. It’ll go away soon.
  EXPRESSION: Informative
- CHARACTER: Christian
  LINE: And you can throw it up if you need to.
  EXPRESSION: Reassuring
- CHARACTER: Narrator
  LINE: JUMP CUT to Dani VOMITING into a bush. Christian stands near her.
  EXPRESSION: null
- CHARACTER: Christian
  LINE: That’s good, baby. It’s okay. Throw it up.
  EXPRESSION: Comforting
- CHARACTER: Narrator
  LINE: Dani rises to take a breath.
  EXPRESSION: null
- CHARACTER: Christian
  LINE: Does that feel better?
  EXPRESSION: Inquiring
- CHARACTER: Pelle
  LINE: Don’t worry - you had it down long enough. You’re still gonna trip.
  EXPRESSION: Reassuring

::PATHS::
- CHOICE: "Continue experiencing the trip"
  TARGET: meadow_minutes_later_2
  STATE_CHANGE: nausea_gone = true
  CONDITION: null

::SCENE::
LOCATION: Meadow - Minutes Later (2)
MOOD: Disorientation, Paranoia
CHARACTERS: Narrator, Dani, Christian, Pelle, Mark, Josh, Young Man
BACKGROUND_IMAGE: meadow_disorientation.png
BACKGROUND_EDIT: "Twilight approaching, large speakers set up in the background"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The group sits on the grass together. The sun is still shining.
  EXPRESSION: null
- CHARACTER: Christian
  LINE: What time is it?
  EXPRESSION: Distracted
- CHARACTER: Pelle
  LINE: Ten at night.
  EXPRESSION: Casual
- CHARACTER: Mark
  LINE: What do you mean?!
  EXPRESSION: Alarmed
- CHARACTER: Pelle
  LINE: What do you mean?
  EXPRESSION: Confused
- CHARACTER: Mark
  LINE: That doesn’t feel right.
  EXPRESSION: Uneasy
- CHARACTER: Pelle
  LINE: Why? It’s the midnight sun.
  EXPRESSION: Explaining
- CHARACTER: Mark
  LINE: It doesn’t feel like ten. I don’t like that! It feels wrong.
  EXPRESSION: Panicked
- CHARACTER: Narrator
  LINE: A YOUNG MAN approaches.
  EXPRESSION: null
- CHARACTER: Christian
  LINE: Oh fuck. It’s a new person.
  EXPRESSION: Apprehensive
- CHARACTER: Mark
  LINE: What? I don’t want new people.
  EXPRESSION: Rejective
- CHARACTER: Pelle
  LINE: No - new people are good!
  EXPRESSION: Enthusiastic
- CHARACTER: Narrator
  LINE: The Young Man walks past.
  EXPRESSION: null
- CHARACTER: Young Man
  LINE: Hey hey!
  EXPRESSION: Friendly
- CHARACTER: Narrator
  LINE: The group mumbles hello.
  EXPRESSION: null
- CHARACTER: Mark
  LINE: I wanna lay down.
  EXPRESSION: Seeking comfort
- CHARACTER: Narrator
  LINE: Mark lies down.
  EXPRESSION: null
- CHARACTER: Mark
  LINE: Oh my God. Lay down. Guys. It’s so nice.
  EXPRESSION: Blissful
- CHARACTER: Narrator
  LINE: Everyone lies down. Except for Josh. For the rest of the scene, our focus is on DANI - even as everyone else speaks.
  EXPRESSION: null
- CHARACTER: Mark
  LINE: Lie down, Josh.
  EXPRESSION: Insistent
- CHARACTER: Narrator
  LINE: Josh doesn’t. Stubborn.
  EXPRESSION: null
- CHARACTER: Pelle
  LINE: Can you feel the energy come up from the earth?
  EXPRESSION: Awe-struck
- CHARACTER: Christian
  LINE: Yeah, like a - pulsing. Oh my God, they are. And the grass!
  EXPRESSION: Amazed
- CHARACTER: Pelle
  LINE: And so are the trees. They’re breathing.
  EXPRESSION: Wonder
- CHARACTER: Narrator
  LINE: The trees do seem to be breathing - visibly swelling and deflating with psychedelic life. They LOOM IMPOSINGLY over Dani. They GROAN in the wind, their branches leaning (almost reaching) down.
  EXPRESSION: Foreboding
- CHARACTER: Narrator
  LINE: Pelle, marveling at his surroundings, sits up:
  EXPRESSION: null
- CHARACTER: Pelle
  LINE: Nature just knows instinctually how to stay in harmony! It’s mechanical. Everything doing its part.
  EXPRESSION: Profound
- CHARACTER: Mark
  LINE: You guys are my family.
  EXPRESSION: Emotional
- CHARACTER: Narrator
  LINE: The word “family” HITS Dani.
  EXPRESSION: null
- CHARACTER: Mark
  LINE: I really mean that. You’re like my real actual Family.
  EXPRESSION: Sincere
- CHARACTER: Narrator
  LINE: Dani SITS UP, suddenly overwhelmed. Christian looks to her. She looks to him. He SMILES, but there’s something false about it.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Dani looks SCARED now. This scares Christian.
  EXPRESSION: null
- CHARACTER: Christian
  LINE: Dani? Don’t look like that.
  EXPRESSION: Worried
- CHARACTER: Narrator
  LINE: Dani STANDS, panic mounting. Her eyes look crazed.
  EXPRESSION: null
- CHARACTER: Dani
  LINE: I’m sorry. I’m gonna walk.
  EXPRESSION: Desperate
- CHARACTER: Christian
  LINE: I can walk, too.
  EXPRESSION: Supportive
- CHARACTER: Dani
  LINE: No no. Sorry. I’m gonna...
  EXPRESSION: Agitated
- CHARACTER: Narrator
  LINE: Dani starts to walk off, a terrible feeling rising in her.
  EXPRESSION: null
- CHARACTER: Josh
  LINE: Is she mad at us?
  EXPRESSION: Confused
- CHARACTER: Mark
  LINE: I don’t like how she did that.
  EXPRESSION: Disapproving
- CHARACTER: Narrator
  LINE: Dani continues to walk. She’s starting to think very bad thoughts.
  EXPRESSION: null
- CHARACTER: Dani
  LINE: (to herself) No, that’s not good. No. No.
  EXPRESSION: Fearful
- CHARACTER: Narrator
  LINE: She then stumbles onto a group of TEENAGERS - all wearing flower garlands. They sit in a circle, passing around a homemade POTION of some sort. They all look at Dani and then BURST OUT LAUGHING.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Dani turns stiffly around, tears welling.
  EXPRESSION: null
- CHARACTER: Dani
  LINE: No, no, no, no --
  EXPRESSION: Distressed
- CHARACTER: Narrator
  LINE: Dani tensely speed-walks away. Her surroundings are THROBBING visibly (and more intensely than before).
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Ingemar calls out to Dani.
  EXPRESSION: null
- CHARACTER: Ingemar
  LINE: Hey! Dani!
  EXPRESSION: Casual
- CHARACTER: Narrator
  LINE: Dani freezes. Terrified, she looks in his direction. He waves her over. He’s sitting with a group of happy twenty-somethings.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Dani warily approaches.
  EXPRESSION: null
- CHARACTER: Ingemar
  LINE: How are you feeling? Everyone: this is Pelle’s friend, Dani.
  EXPRESSION: Welcoming
- CHARACTER: Narrator
  LINE: Everyone says hi.
  EXPRESSION: null
- CHARACTER: Dani
  LINE: They were laughing at me over there.
  EXPRESSION: Accusatory
- CHARACTER: Ingemar
  LINE: What? No, I’m sure they weren’t. They probably just wanted you to laugh with them.
  EXPRESSION: Dismissive
- CHARACTER: Narrator
  LINE: But Ingemar’s face was MUTATING as he said that.
  EXPRESSION: null
- CHARACTER: Dani
  LINE: Okay. Sorry. Never mind. Thank you.
  EXPRESSION: Terrified
- CHARACTER: Narrator
  LINE: Dani turns around and walks stiffly off.
  EXPRESSION: null
- CHARACTER: Dani
  LINE: It’s okay. It’s not that. You’re okay. It’s drugs.
  EXPRESSION: Rationalizing
- CHARACTER: Narrator
  LINE: She continues toward a sturdy wooden OUTHOUSE. She hastily enters.
  EXPRESSION: null

::PATHS::
- CHOICE: "Enter the outhouse"
  TARGET: outhouse_interior
  STATE_CHANGE: panic = +1
  CONDITION: null

::SCENE::
LOCATION: Outhouse - Continuous
MOOD: Claustrophobic, Hallucinatory
CHARACTERS: Narrator, Dani
BACKGROUND_IMAGE: outhouse_interior.png
BACKGROUND_EDIT: "Candle-lit interior of a clean outhouse"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The interior of the outhouse is illuminated by CANDLE-LIGHT.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: It’s very clean. Dani stands here for a moment.
  EXPRESSION: null
- CHARACTER: Dani
  LINE: This is a coffin.
  EXPRESSION: Paranoid
- CHARACTER: Narrator
  LINE: (immediately reprimanding herself) Hey! No it’s not.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Dani sees a MIRROR on the wall. She looks at it. Hard.
  EXPRESSION: null
- CHARACTER: Dani
  LINE: Fuck you. Stop it.
  EXPRESSION: Defiant
- CHARACTER: Narrator
  LINE: Suddenly her skin seems to take on a translucent quality. Her veins become faintly visible. Beneath her cheeks, it looks like organic gears are turning.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: DANI SQUEEZES HER EYES SHUT. She takes a moment, trying to will that vision away.
  EXPRESSION: null
- CHARACTER: Dani
  LINE: Don’t look in the mirror. It’s not your face.
  EXPRESSION: Self-soothing
- CHARACTER: Narrator
  LINE: (saying that again, under scrutiny) “It’s not your face.”
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: After a long moment, Dani OPENS her eyes again. When they open, TEN ADDITIONAL EYES open simultaneously - all over her face. Like spider eyes.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Dani SCREAMS and FLEES the outhouse...
  EXPRESSION: null

::PATHS::
- CHOICE: "Flee the outhouse"
  TARGET: outhouse_exterior
  STATE_CHANGE: terror = +1
  CONDITION: null

::SCENE::
LOCATION: Outhouse - Continuous (2)
MOOD: Panic, Desperation
CHARACTERS: Narrator, Dani
BACKGROUND_IMAGE: outhouse_exterior.png
BACKGROUND_EDIT: "Dani running frantically across a field"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Dani runs frantically across the field, desperately wiping off her face (as if to wipe off the extra eyes). We CHASE AFTER HER before CUTTING TO:
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue chasing Dani"
  TARGET: field_same_time
  STATE_CHANGE: fear = +1
  CONDITION: null

::SCENE::
LOCATION: Field - Same Time
MOOD: Peak Trip, Discord
CHARACTERS: Narrator, Christian, Josh, Mark, Pelle, Dani
BACKGROUND_IMAGE: field_peak_trip.png
BACKGROUND_EDIT: "Group lying on grass, twilight, speakers in background"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Christian, Josh, Mark and Pelle are still lying in the same spot. They’ve hit the peak of their trip. Twilight is coming.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: In the b.g., a group has finished setting up LARGE SPEAKERS.
  EXPRESSION: null
- CHARACTER: Christian
  LINE: Where did she go?
  EXPRESSION: Anxious
- CHARACTER: Mark
  LINE: It’s okay.
  EXPRESSION: Dismissive
- CHARACTER: Josh
  LINE: (looking at his hands) Why the fuck do we have fingerprints?
  EXPRESSION: Bewildered
- CHARACTER: Narrator
  LINE: Christian STANDS, panic starting to build.
  EXPRESSION: null
- CHARACTER: Christian
  LINE: Dani’s gone. We need to find Dani.
  EXPRESSION: Panicked
- CHARACTER: Josh
  LINE: I don’t feel like standing.
  EXPRESSION: Lethargic
- CHARACTER: Mark
  LINE: Yeah - I don’t wanna move.
  EXPRESSION: Apathetic
- CHARACTER: Christian
  LINE: Hey! Dani’s our friend!
  EXPRESSION: Pleading
- CHARACTER: Mark
  LINE: She isn’t all of our friend.
  EXPRESSION: Cold
- CHARACTER: Christian
  LINE: What? Yes she is. That’s not nice! Why aren’t you ever nice?! You’re being mean!
  EXPRESSION: Furious
- CHARACTER: Narrator
  LINE: MARK looks scared by this
  EXPRESSION: null
- CHARACTER: Mark
  LINE: What? I am nice. (tearing up) I’m not being mean!
  EXPRESSION: Defensive
- CHARACTER: Narrator
  LINE: Droning techno begins to THROB from the speakers in the b.g. With every bass punch, the surrounding environment THUMPS visibly.
  EXPRESSION: null
- CHARACTER: Christian
  LINE: Dani’s our friend. And she’s sad.
  EXPRESSION: Concerned
- CHARACTER: Mark
  LINE: But that makes me sad! (suddenly angry) And she’s NOT our friend! She’s barely YOUR friend! You only invited her because you’re too scared to be honest with her!
  EXPRESSION: Enraged
- CHARACTER: Narrator
  LINE: Christian pauses, FURIOUS, and then:
  EXPRESSION: null
- CHARACTER: Christian
  LINE: Her family is dead, Mark! Do you get that? They all died!
  EXPRESSION: Accusatory
- CHARACTER: Mark
  LINE: (suddenly)
  EXPRESSION: Aghast

::PATHS::
- CHOICE: "Continue the argument"
  TARGET: argument_escalates
  STATE_CHANGE: conflict = +1
  CONDITION: null

::SCENE::
LOCATION: Woods
MOOD: Tension
CHARACTERS: Christian, Mark, Josh, Pelle
BACKGROUND_IMAGE: woods_interior.png
BACKGROUND_EDIT: "Interior of dense woods, muted light"

::SCRIPT::
- CHARACTER: Christian
  LINE: Why are you saying that?
  EXPRESSION: Confused
- CHARACTER: Mark
  LINE: Because they are! They’re dead!
  EXPRESSION: Resolute
- CHARACTER: Christian
  LINE: Why???
  EXPRESSION: Confused
- CHARACTER: Josh
  LINE: HEY! NO! We need to connect back to the good things! This is getting bad! Everything’s alive right now.
  EXPRESSION: Insistent
- CHARACTER: Christian
  LINE: But that’s just so it can die later.
  EXPRESSION: Pessimistic
- CHARACTER: Mark
  LINE: Oh God...!
  EXPRESSION: Fearful
- CHARACTER: Narrator
  LINE: Silence. Everyone looks at Pelle, catching up to what he just said. Christian stomps off.
  EXPRESSION: null
- CHARACTER: Mark
  LINE: Wait! Christian! We need to stay together!
  EXPRESSION: Pleading

::PATHS::
- CHOICE: "Follow Christian"
  TARGET: woods_interior_2
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Woods
MOOD: Disorientation
CHARACTERS: Dani
BACKGROUND_IMAGE: woods_exterior.png
BACKGROUND_EDIT: "Exterior of woods, dusky light, muffled techno music in distance"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Dani paces in the woods. Muffled techno drones in the distance.
  EXPRESSION: null
- CHARACTER: Dani
  LINE: Hello?!... HELLO??!!
  EXPRESSION: Calling out
- CHARACTER: Narrator
  LINE: (redirecting her thoughts) It’s almost your birthday. Fuck.
  EXPRESSION: null
- CHARACTER: Dani
  LINE: What time is it?
  EXPRESSION: Inquisitive
- CHARACTER: Narrator
  LINE: (then, PAUSES) You were almost born... You’re a baby.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: This gets to Dani. She now looks around the woods, fearfully. Like a lost child.
  EXPRESSION: null
- CHARACTER: Dani
  LINE: MOMMY?!... DADDY?!...
  EXPRESSION: Panicked
- CHARACTER: Dani
  LINE: Mommy daddy mommy daddy...
  EXPRESSION: Mumbling
- CHARACTER: Dani
  LINE: CHRISTIAN?!
  EXPRESSION: Desperate

::PATHS::
- CHOICE: "Continue searching"
  TARGET: woods_interior_3
  STATE_CHANGE: fear = +1
  CONDITION: null

::SCENE::
LOCATION: Woods
MOOD: Terror
CHARACTERS: Dani
BACKGROUND_IMAGE: woods_interior_3.png
BACKGROUND_EDIT: "Interior of woods, increasingly unsettling"

::SCRIPT::
- CHARACTER: Dani
  LINE: No...no.... You’re alone.
  EXPRESSION: Despairing
- CHARACTER: Narrator
  LINE: Then it hits Dani. Her eyes well intensely with tears. This idea is now horribly significant.
  EXPRESSION: null
- CHARACTER: Dani
  LINE: You’re alone.
  EXPRESSION: Revelation
- CHARACTER: Narrator
  LINE: Dani sees a dead rabbit. Its innards are splayed.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Dani warily approaches. Magnetized but repulsed. As she nears, the fear rises in her. She gets close enough to finally see... The rabbit is being devoured by ants.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Dani looks mortified, but her eyes are glued. She leans in to look closer, but then -- she sees ants on her arm. (Whether they’re there or not is unclear.)
  EXPRESSION: null
- CHARACTER: Dani
  LINE: SCREAMS. She violently slaps at her arm. She then swipes at her other arm, and starts slapping at her neck and face, as if she were engulfed in ants. (She’s not.)
  EXPRESSION: Screaming
- CHARACTER: Narrator
  LINE: Dani looks down. The earth seems to now be a pulsating carpet of ants.
  EXPRESSION: null
- CHARACTER: Dani
  LINE: SCREAMS and RUNS for her life.
  EXPRESSION: Screaming
- CHARACTER: Christian (O.S.)
  LINE: Dani!
  EXPRESSION: Calling out
- CHARACTER: Dani
  LINE: ...Christian?!
  EXPRESSION: Surprised
- CHARACTER: Christian (O.S.)
  LINE: Dani!!
  EXPRESSION: Calling out
- CHARACTER: Narrator
  LINE: Dani searches desperately for his voice. She finds him standing at a clearing. She runs for him, crying.
  EXPRESSION: null
- CHARACTER: Christian
  LINE: Where the hell did you go?!
  EXPRESSION: Concerned
- CHARACTER: Narrator
  LINE: They embrace. She hugs him. Squeezes him.
  EXPRESSION: null
- CHARACTER: Dani
  LINE: I got lost.
  EXPRESSION: Tearful
- CHARACTER: Christian
  LINE: Let’s go back to the group.
  EXPRESSION: Reassuring
- CHARACTER: Dani
  LINE: Christian. Nothing means anything.
  EXPRESSION: Lost
- CHARACTER: Christian
  LINE: What?
  EXPRESSION: Confused
- CHARACTER: Dani
  LINE: Nothing means anything! We’re just alone. And I felt this presence - like God but not God - and it was telling me this and it was laughing at me.
  EXPRESSION: Despairing
- CHARACTER: Christian
  LINE: You heard laughing?
  EXPRESSION: Scared
- CHARACTER: Dani
  LINE: I felt it laughing! I figured it out, that nothing means anything and we’re born alone and we die alone, and it was getting pleasure from that.
  EXPRESSION: Distraught
- CHARACTER: Narrator
  LINE: Christian is getting scared. He takes Dani’s arm -
  EXPRESSION: null
- CHARACTER: Christian
  LINE: Okay: no. We’re going back to the friends.
  EXPRESSION: Firm
- CHARACTER: Narrator
  LINE: - and starts leading her away.
  EXPRESSION: null
- CHARACTER: Christian
  LINE: You’re having a bad trip, and you’re thinking you’re alone because you went off and you made yourself alone. You just got scared.
  EXPRESSION: Reassuring
- CHARACTER: Narrator
  LINE: He’s now pulling Dani, aggressively.
  EXPRESSION: null
- CHARACTER: Christian
  LINE: You have me. Everything’s connected. We’re all one. Those are the good things you’re supposed to think about when you trip. We’re all unified. Fuck.
  EXPRESSION: Assertive

::PATHS::
- CHOICE: "Walk back to the field"
  TARGET: field_interior
  STATE_CHANGE: fear = -1, connection = +1
  CONDITION: null

::SCENE::
LOCATION: Field
MOOD: Uneasy Calm
CHARACTERS: Dani, Christian, Josh, Mark, Pelle, Connie, Simon, Ingemar, Blonde Swedish Guy
BACKGROUND_IMAGE: field_interior.png
BACKGROUND_EDIT: "Open field, visible surroundings throbbing to techno beat"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Christian has been leading her out of the woods. They emerge onto the field, where the droning techno is now very present (and making the visible surroundings throb to its beat).
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: We track alongside Dani and Christian as they walk uneasily through the grass - past groups of happy, tripping strangers.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Christian’s eyes are glued tensely to the ground, combating dark thoughts. Dani looks less frightened now than disconnected.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: They arrive at Josh, Mark and Pelle, who are now accompanied by Connie, Simon, Ingemar and a Blonde Swedish Guy (20s).
  EXPRESSION: null
- CHARACTER: Blonde Swedish Guy
  LINE: Hey hey!
  EXPRESSION: Friendly
- CHARACTER: Mark
  LINE: Where were you?
  EXPRESSION: Concerned
- CHARACTER: Pelle
  LINE: How are you, Dani?
  EXPRESSION: Inquisitive
- CHARACTER: Christian
  LINE: We’re fine. She’s fine. Just took a little walk.
  EXPRESSION: Insistent
- CHARACTER: Connie
  LINE: Are you feeling it?!
  EXPRESSION: High
- CHARACTER: Dani
  LINE: I wanna sleep. How can I sleep?
  EXPRESSION: Weary

::PATHS::
- CHOICE: "Wait for sleep"
  TARGET: sleeping_dani
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Sleeping Dani
MOOD: Peaceful
CHARACTERS: Dani, Christian, Mark, Pelle, Josh
BACKGROUND_IMAGE: sleeping_dani.png
BACKGROUND_EDIT: "Close-up of Dani's sleeping face, faint music in the distance"

::SCRIPT::
- CHARACTER: Narrator
  LINE: HOURS LATER. CLOSE-UP OF DANI’S SLEEPING FACE. In the distance: a faint, barely discernible melody. It sounds like a flute.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: A hand reaches into frame to nudge Dani. She stirs awake.
  EXPRESSION: null
- CHARACTER: Christian (O.C.)
  LINE: It’s time to get up.
  EXPRESSION: Gentle
- CHARACTER: Dani
  LINE: ...how long was I asleep?
  EXPRESSION: Drowsy
- CHARACTER: Narrator
  LINE: Dani sits up. It’s still bright outside. The visual surroundings are no longer morphing. Mark and Pelle and Josh are standing. Christian is crouched beside her.
  EXPRESSION: null
- CHARACTER: Dani
  LINE: Did it get dark at all?
  EXPRESSION: Inquisitive
- CHARACTER: Pelle
  LINE: For a couple hours. Not completely.
  EXPRESSION: Matter-of-fact
- CHARACTER: Narrator
  LINE: Then something occurs to Dani:
  EXPRESSION: null
- CHARACTER: Dani
  LINE: Is it tomorrow?
  EXPRESSION: Hopeful
- CHARACTER: Christian
  LINE: ...It’s today.
  EXPRESSION: Blank
- CHARACTER: Narrator
  LINE: Dani looks at Christian, whose expression is blank. She sinks with quiet disappointment. (He forgot her birthday.) Christian helps Dani up. She wobbles.
  EXPRESSION: null
- CHARACTER: Dani
  LINE: Where are we going?
  EXPRESSION: Lost
- CHARACTER: Pelle
  LINE: Where we came for.
  EXPRESSION: Resolute

::PATHS::
- CHOICE: "Head back to the village"
  TARGET: woods_exterior_2
  STATE_CHANGE: disappointment = +1
  CONDITION: null

::SCENE::
LOCATION: Woods
MOOD: Transition
CHARACTERS: Narrator, Group
BACKGROUND_IMAGE: woods_exterior_2.png
BACKGROUND_EDIT: "Exterior of woods, bright daylight"

::SCRIPT::
- CHARACTER: Narrator
  LINE: EXT. WOODS - DAY. Everyone from the meadow crunches through the woods. Our group is at the end of the queue (carrying their bags). As they walk, the melody is growing clearer and louder. It’s a happy tune.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The group’s footing is unsteady. Dani, especially, keeps stumbling over her own feet. She grips Christian’s wrist.
  EXPRESSION: null
- CHARACTER: Mark
  LINE: The come-down on these mushrooms is really intense.
  EXPRESSION: Drained
- CHARACTER: Narrator
  LINE: Dani notices a few disparate flowers sprouting up from the ground. As she walks, the flowers continue to accumulate. Soon she’s walking down a controlled, narrow trail of wild yellow flowers - all leading toward a clearing.
  EXPRESSION: null
- CHARACTER: Mark
  LINE: Okay: am I still tripping or is there a lot that people aren’t acknowledging right now?
  EXPRESSION: Confused

::PATHS::
- CHOICE: "Follow the flowers"
  TARGET: clearing_village
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Clearing to Village
MOOD: Utopian
CHARACTERS: Group, Floutist, Fiddler, Key Harpist
BACKGROUND_IMAGE: clearing_village.png
BACKGROUND_EDIT: "Clearing opening to a field, a small village in the distance, music playing"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The group finally arrives at the clearing. It opens to another field, beyond which is a small village. The melody is being played by a floutist, a fiddler and a key harpist. The scene is utopian.
  EXPRESSION: null
- CHARACTER: Josh
  LINE: This is the place?
  EXPRESSION: Mesmerized
- CHARACTER: Pelle
  LINE: The tranquil and majestic Hårga.
  EXPRESSION: Tongue-in-cheek

::PATHS::
- CHOICE: "Approach the village"
  TARGET: hargafarmstead_entrance
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Hårga Farmstead Entrance
MOOD: Welcoming
CHARACTERS: Group, Welcoming Committee
BACKGROUND_IMAGE: hargafarmstead_entrance.png
BACKGROUND_EDIT: "Approaching a Hälsingegård (farmstead) with about a hundred people waiting on the grass, dressed in Amish-like clothing"

::SCRIPT::
- CHARACTER: Narrator
  LINE: They continue toward it, approaching a Hälsingegård (a farm). About a hundred people stand on the grass, waiting. They are dressed like Amish people, but less formal. They appear to be a welcoming committee.
  EXPRESSION: null
- CHARACTER: Christian
  LINE: You know all these people?
  EXPRESSION: Inquisitive
- CHARACTER: Pelle
  LINE: These are my family!
  EXPRESSION: Proud

::PATHS::
- CHOICE: "Enter the farmstead"
  TARGET: hargafarmstead_interior
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Hårga Farmstead Interior
MOOD: Festive Reunion
CHARACTERS: Group, Pelle, Welcoming Committee, Dagny
BACKGROUND_IMAGE: hargafarmstead_interior.png
BACKGROUND_EDIT: "Interior of a large barn-like main house and surrounding buildings, adorned with St. John's Wort"

::SCRIPT::
- CHARACTER: Narrator
  LINE: They arrive at the farmstead. At the center is one particularly large building in the shape of a barn; this is the main house. Surrounding this are several houses, a horse stable, a temple, and different gardens. The windows and doorways are all adorned in St. John's Wort (flowers with bright yellow petals and golden stamens). Beyond the farmstead are vast fields of crops.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Most of the arriving crowd is embraced ecstatically by the welcoming committee. They hug and kiss and squeal with excitement. It appears to be something of a reunion. Pelle, in particular, is bombarded with affection.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Josh and Christian notice a towering Maypole. Immense in height and width, it is entangled in lush green shrubbery and marked by a wealth of symbols (some runic, some more esoteric, all colorful). At the top of the pole is a triangle, beneath which hang two rings.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Pelle brings a beautiful, blonde woman over to the group. This is Dagny (25). She wears a white dress with intricate embroidery (featuring a pentagon and distinct Pagan runes).
  EXPRESSION: null
- CHARACTER: Pelle
  LINE: Dagny - this is Dani, Christian, Josh, Mark. This is my sister Dagny. Born on the same exact week as me.
  EXPRESSION: Introducing
- CHARACTER: Dagny
  LINE: Välkommen till Hårga!
  EXPRESSION: Welcoming
- CHARACTER: Dani
  LINE: Tack!
  EXPRESSION: Grateful
- CHARACTER: Josh/Christian
  LINE: Thank you!
  EXPRESSION: Grateful
- CHARACTER: Narrator
  LINE: Dagny smiles and walks off.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: An older man, Odd (50s), approaches. He is wearing a dress. Pelle lights up at the sight of him.
  EXPRESSION: null
- CHARACTER: Pelle
  LINE: Father Odd!
  EXPRESSION: Excited
- CHARACTER: Odd
  LINE: Little Pelle!
  EXPRESSION: Affectionate
- CHARACTER: Narrator
  LINE: They embrace. There is a moment where they rest their foreheads together. (Note: throughout the film, the Hårgas will communicate little things through subtly modulated expressions and gestures. These are their affects, a language known only to them.)
  EXPRESSION: null
- CHARACTER: Odd
  LINE: How is the pilgrimage?
  EXPRESSION: Inquisitive
- CHARACTER: Pelle
  LINE: Wonderful. Amazing. These are my friends - Christian, Mark, Josh, Dani...
  EXPRESSION: Enthusiastic
- CHARACTER: Odd
  LINE: Hello, hello...yes, hello, welcome. Welcome home!
  EXPRESSION: Welcoming
- CHARACTER: Narrator
  LINE: Odd shakes their hands as Pelle introduces them.
  EXPRESSION: null
- CHARACTER: Odd
  LINE: We are very happy to have you! Pelle has an immaculate sense for people.
  EXPRESSION: Happy
- CHARACTER: Narrator
  LINE: Pelle smiles.
  EXPRESSION: null
- CHARACTER: Dani
  LINE: I love what you’re wearing.
  EXPRESSION: Admiring
- CHARACTER: Odd
  LINE: Oh - my frock? Quite girly, no? Ha! We do this as a tribute: Because of nature’s, em, hermaphrodite-ick - sorry - her-ma-phro-DI-TIC qualities - the men do like women and visa versa.
  EXPRESSION: Explaining
- CHARACTER: Josh
  LINE: Like the cult of Aphroditus! I think the sakhis saints do the same thing, too - in Brajbhoomi?
  EXPRESSION: Thoughtful
- CHARACTER: Narrator
  LINE: If Odd is annoyed by this, he hides it well. He shines a tight-lipped smile at Josh.
  EXPRESSION: null
- CHARACTER: Odd
  LINE: So! We’re your hosts! Yes? So whatever you need, you tell us and we’ll do everything to accommodate! Today is all festivities, yet tomorrow the official ceremonies begin. So have yourselves ready! It’s a sincere pleasure to have you, and you are Welcome-Welcome-Welcome. So enjoy!
  EXPRESSION: Hostly
- CHARACTER: Narrator
  LINE: They all say thanks and Odd walks happily away.
  EXPRESSION: null
- CHARACTER: Mark
  LINE: Nice guy.
  EXPRESSION: Appreciative

::PATHS::
- CHOICE: "Observe the ceremony preparations"
  TARGET: ceremony_preparation
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Ceremony Preparation
MOOD: Anticipation
CHARACTERS: Group, Ten Girls, Ten Old Men and Women
BACKGROUND_IMAGE: ceremony_preparation.png
BACKGROUND_EDIT: "Music swells, ten girls in white dresses holding floral crowns walk towards a platform where ten old men and women sit"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The music suddenly gets louder. Percussion is introduced, and the music swells to become a regal melody. Everyone’s attention moves to ten girls (different ages - from 7 to 13), all dressed in identical white dresses. They hold floral garland crowns (made of mugwort and vervain) and sprigs of larkspur. They are walking single-file towards a platform...
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Sitting on the platform are ten old men and women (60s to 70s)
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue watching"
  TARGET: end
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Platform - Hårga Farmstead
MOOD: Festive, Ritualistic
CHARACTERS: Elders, Girls, Siv, Children, Josh, Dani, Christian, Connie, Pelle
BACKGROUND_IMAGE: platform_midsummer.png
BACKGROUND_EDIT: "70s style, festive outdoor setting with a platform"

::SCRIPT::
- CHARACTER: Narrator
  LINE: ly 70s). These are the ELDERS. They wear severe or neutral expressions, and are dressed in finely embroidered linen.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The girls march onto the platform. They each stop before one of the seated elders. Upon a cue, they simultaneously lay the crowns onto the elders’ heads. They then hand the elders the larkspur sprigs. After this, the girls return bashfully to the crowd.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: One of the elders - a sturdy old woman (70) - rises to address the crowd. The music drops out. She is beautiful, composed, elegant. This is SIV, the matriarch.
  EXPRESSION: null
- CHARACTER: SIV
  LINE: (in Swedish) Happy midsummer, all!
  EXPRESSION: Cheerful
- CHARACTER: Narrator
  LINE: As she speaks, several children - all wearing outfits to distinguish them as waiters - pass out shot glasses of AQUAVIT.
  EXPRESSION: null
- CHARACTER: SIV
  LINE: Ni är så oerhört välkomna hit. Till oss. Vi vill att ni är med och firar Midsommar med oss. Ni får boende, mat och vara en del av det som är den största festen här hos oss i Hårga. Faktiskt den största på nästan hundra år.
  EXPRESSION: Welcoming
- CHARACTER: Narrator
  LINE: She notices the non-Swedish speakers.
  EXPRESSION: null
- CHARACTER: SIV
  LINE: Forgive me - I’m excluding the ones who aren’t of Swedish tongue. Welcome to Hårga, and happy midsummer! I believe it is the hottest and brightest that we’ve had in at least a decade, and this is our biggest party in almost a century! So - wow, yah?
  EXPRESSION: Enthusiastic
- CHARACTER: JOSH/DANI/CHRISTIAN/CONNIE
  LINE: Yeah. Wow.
  EXPRESSION: Amazed
- CHARACTER: Narrator
  LINE: Siv smiles, and proceeds to wrap it up.
  EXPRESSION: null
- CHARACTER: SIV
  LINE: All right, my fellow merrymakers. Without any further blathering - let’s raise our glasses -
  EXPRESSION: Jovial
- CHARACTER: Narrator
  LINE: Everyone raises their aquavit.
  EXPRESSION: null
- CHARACTER: SIV
  LINE: - and let our Nine-Day Feast begin!
  EXPRESSION: Grand
- CHARACTER: SIV
  LINE: (announcing) Skål!
  EXPRESSION: Exuberant
- CHARACTER: EVERYONE
  LINE: Skål!!
  EXPRESSION: Exuberant
- CHARACTER: Narrator
  LINE: The crowd drinks. Everyone CHEERS. Including our group. The MUSIC begins again.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: On one side of the platform: A young GIRL, also wearing an embroidered white dress, walks up with a JUNIPER BOUGH in each hand. She is accompanied by a TEENAGE BOY, who holds two FLAMING TORCHES. Meanwhile, two of the ELDERLY MEN (72) have risen from their seats.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Siv now speaks in English, presumably for our group’s benefit. (As she does this, the young girl and teen boy hand the elderly men a juniper bough and flaming stick.)
  EXPRESSION: null
- CHARACTER: SIV
  LINE: And now, in keeping with tradition: Hjalmar and Josef will make three trips. If they make it back with the flame intact, our vintage will be abundant this year! On the other hand, if it burns out - that will be an omen of bad luck and we will know to prepare.
  EXPRESSION: Solemn
- CHARACTER: Narrator
  LINE: Josh turns to Pelle.
  EXPRESSION: null
- CHARACTER: JOSH
  LINE: What does “bad luck” mean?
  EXPRESSION: Curious
- CHARACTER: PELLE
  LINE: Usually that the cattle will get sick.
  EXPRESSION: Informative
- CHARACTER: Narrator
  LINE: Siv yells something in Swedish to the air.
  EXPRESSION: null
- CHARACTER: JOSH
  LINE: (to Pelle) What did she just say?
  EXPRESSION: Curious
- CHARACTER: PELLE
  LINE: Told any lingering spirits to go back to the dead.
  EXPRESSION: Matter-of-fact
- CHARACTER: Narrator
  LINE: The two elderly men, now BLINDFOLDED, begin to run around the Main House, holding up their flaming sticks. (Everyone watches, rapt.) They pick up the pace to finish their first cycle around the house. They then begins circling it again.
  EXPRESSION: null
- CHARACTER: JOSH
  LINE: (to Pelle) Can I takes photos?
  EXPRESSION: Eager
- CHARACTER: PELLE
  LINE: Discreetly.
  EXPRESSION: Cautious
- CHARACTER: Narrator
  LINE: The men finish their second cycle around the house, and immediately begin a third. The community seems to be holding its collective breath. The men FINISH the third run-around, but...one man’s flame has been EXTINGUISHED.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: A man in the audience, ISAK (50s), lets out a GASP when he sees this. Everyone else sinks audibly with disappointment.
  EXPRESSION: Disappointed
- CHARACTER: Narrator
  LINE: The men, having finished, remove their blindfold. The elder with the extinguished torch DEFLATES. Siv gestures sadly to the crowd: “There we have it.”
  EXPRESSION: Sad
- CHARACTER: Narrator
  LINE: Isak looks absolutely devastated. Christian notices.
  EXPRESSION: null
- CHARACTER: CHRISTIAN
  LINE: (to Pelle) Is he okay?
  EXPRESSION: Concerned
- CHARACTER: PELLE
  LINE: The cattle are his responsibility.
  EXPRESSION: Serious
- CHARACTER: Narrator
  LINE: Isak’s eyes stare off, unblinking. Heartbroken. He looks to the CATTLE HOUSE, eyes filling with tears.
  EXPRESSION: Devastated
- CHARACTER: MARK
  LINE: (to Pelle and Christian) How do you think he’d react if I just put my finger in his butt right now?
  EXPRESSION: Crude
- CHARACTER: Narrator
  LINE: Continuing the ritual, Siv takes the torches from the men and walks to a healthy FIRE in a pit. She deposits the sticks into the fire.
  EXPRESSION: null
- CHARACTER: SIV
  LINE: (in Swedish) This high my fire, but no higher, no hotter!
  EXPRESSION: Authoritative
- CHARACTER: PELLE
  LINE: (translating) Uh - this high is my fire, but not higher or hotter.
  EXPRESSION: Explanatory
- CHARACTER: PELLE
  LINE: (explaining) It’s to keep the fire from growing out of control.
  EXPRESSION: Informative
- CHARACTER: Narrator
  LINE: Josh WRITES this down in his notebook. Christian WATCHES Josh, slightly perturbed.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Siv now accepts a BOWL OF BEER from one of the children. She drinks a healthy gulp, and then throws the rest into the fire.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Everyone now APPLAUDS. This seems to be the end of the ritual.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: A group of TEENAGERS (all dressed in bright, formal garb) emerge from a kitchen. They carry PLATES OF FOOD (lamb and blood pudding) and BEER. They begin by serving the elders.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Dani sees that one of the teens is carrying an ornate platter featuring a LAMB’S SKULL (brain exposed) and a LAMB’S HEART. The platter is bordered by a dense spiral of INTESTINES. This is laid onto the center of a table that has been painstakingly decorated with local flowers.
  EXPRESSION: null
- CHARACTER: PELLE
  LINE: That’s a tradition. They just killed that lamb today.
  EXPRESSION: Factual
- CHARACTER: Narrator
  LINE: The servers now move to our group, which has settled onto the grass. They are handed plates and beers.
  EXPRESSION: null
- CHARACTER: DANI
  LINE: (to Pelle) Can we help at all?
  EXPRESSION: Willing
- CHARACTER: PELLE
  LINE: No no. You’re the guests. Let yourself be spoiled.
  EXPRESSION: Gracious
- CHARACTER: Narrator
  LINE: One boy, RUBEN (15), walks up to Dani. He is severely mentally handicapped and his hands are palsied. He’s dressed in gorgeous linen.
  EXPRESSION: null
- CHARACTER: RUBEN
  LINE: (with difficulty) Hey hey!
  EXPRESSION: Strained
- CHARACTER: DANI
  LINE: (warmly) Hello!
  EXPRESSION: Kind
- CHARACTER: Narrator
  LINE: Ruben walks off. As he ambles aimlessly, people reach out to lovingly TOUCH him - as if in reverence.
  EXPRESSION: null
- CHARACTER: PELLE
  LINE: You just met Ruben.
  EXPRESSION: Informative
- CHARACTER: DANI
  LINE: Ruben is lovely.
  EXPRESSION: Admiring
- CHARACTER: Narrator
  LINE: The teens finish serving. They now sit with plates of their own.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Mark has already started eating. Josh NUDGES him. Nobody else has begun. Mark bashfully sets down his fork.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Silence.
  EXPRESSION: Tense
- CHARACTER: Narrator
  LINE: Siv, the matriarch, looks to a PLUMP ELDER (60s) sitting beside her. He stands, takes a moment, and then speaks loudly in Swedish, as if in PRAYER.
  EXPRESSION: null
- CHARACTER: PELLE
  LINE: (whispering to Josh and Christian) He’s giving thanks.
  EXPRESSION: Quiet
- CHARACTER: JOSH
  LINE: For the food?
  EXPRESSION: Inquisitive
- CHARACTER: PELLE
  LINE: Yes. And the weather, and the crops...
  EXPRESSION: Explanatory
- CHARACTER: Narrator
  LINE: The Plump Man finishes his speech, and then announces:
  EXPRESSION: null
- CHARACTER: PLUMP MAN
  LINE: Låt oss äta!
  EXPRESSION: Resonant
- CHARACTER: Narrator
  LINE: Everyone digs in.
  EXPRESSION: null
- CHARACTER: CHRISTIAN
  LINE: Who was he praying to?
  EXPRESSION: Confused
- CHARACTER: PELLE
  LINE: Uh - well, that wasn’t really “praying.” But he was just addressing the...everything. The harmony and the balance.
  EXPRESSION: Thoughtful
- CHARACTER: JOSH
  LINE: Can you translate what was said?
  EXPRESSION: Eager
- CHARACTER: PELLE
  LINE: ...I can get an exact translation later.
  EXPRESSION: Evasive
- CHARACTER: CHRISTIAN
  LINE: (jumping in) Yeah, please, that would be amazing.
  EXPRESSION: Eager
- CHARACTER: JOSH
  LINE: (eyes now burning on Christian) ...Yes, Pelle, thank you.
  EXPRESSION: Tense
- CHARACTER: Narrator
  LINE: Christian looks at Josh. A CHARGED moment. They start eating.
  EXPRESSION: null

::SCENE::
LOCATION: Bathroom - Hårga Farmstead
MOOD: Anxious
CHARACTERS: Maja
BACKGROUND_IMAGE: bathroom_maja.png
BACKGROUND_EDIT: "Rustic bathroom, 70s style"

::SCRIPT::
- CHARACTER: Narrator
  LINE: A beautiful, curly-haired BLONDE GIRL (16) stands before a mirror, anxiously fussing with her hair. She clearly needs it to look perfect. This is MAJA.
  EXPRESSION: Anxious

::SCENE::
LOCATION: Hårga Farmstead - Main House Exterior
MOOD: Joyful, Celebratory
CHARACTERS: Maja, Hårgan Youth, Josh, Dani, Christian, Connie, Ingemar, Simon, Pelle
BACKGROUND_IMAGE: Hårga_farmstead_dance.png
BACKGROUND_EDIT: "Nighttime, outdoors, maypole, dancing"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Maja emerges from the MAIN HOUSE. All the younger Hårgans have joined hands to form a train of people. They run and dance in a wide circle, singing a variation of Visa i midsommartid. The MAYPOLE stands at the center of their circle.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Maja timidly watches the dance, smiling. Her eyes trail off to find our group. She alights on CHRISTIAN, instantly smitten. It almost looks like she recognizes him.
  EXPRESSION: Shy
- CHARACTER: Narrator
  LINE: One of the dancing boys suddenly GRABS Maja’s hand. He PULLS her into the train. She LAUGHS as she joins.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: MEANWHILE: Our group is still sitting in the same place (along with Connie and Ingemar). They watch the passing dancers with fascination.
  EXPRESSION: null
- CHARACTER: PELLE
  LINE: You guys should join!
  EXPRESSION: Encouraging
- CHARACTER: DANI
  LINE: I’m too scared.
  EXPRESSION: Hesitant
- CHARACTER: Narrator
  LINE: SIMON approaches, carrying two beers. He momentarily gets caught in the crossfire of a group of YOUNG BOYS CHASING EACH OTHER. He finally reaches Connie, and hands her a beer.
  EXPRESSION: null
- CHARACTER: SIMON
  LINE: Alright?
  EXPRESSION: Casual
- CHARACTER: CONNIE
  LINE: Ta.
  EXPRESSION: Grateful
- CHARACTER: SIMON
  LINE: (re: the boys) What are they playing?
  EXPRESSION: Curious
- CHARACTER: PELLE
  LINE: “Skin the fool!”
  EXPRESSION: Amused
- CHARACTER: SIMON
  LINE: (sarcastic) Ah. Precious.
  EXPRESSION: Sarcastic
- CHARACTER: Narrator
  LINE: Dani notices Ingemar STARING at Simon and Connie. He looks resentful. He finally averts his eyes and forces a smile.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: MAJA, in the dancing train, is about to pass the group. She summons the nerve to gently KICK Christian’s back. Christian looks up to see Maja passing by. She SMILES bashfully at him.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: He confusedly smiles back.
  EXPRESSION: Confused
- CHARACTER: Narrator
  LINE: Dani notices Christian smiling, but doesn’t see Maja (who has already turned away).
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Christian RISES, suddenly feeling bold.
  EXPRESSION: Bold
- CHARACTER: CHRISTIAN
  LINE: (to Pelle) How can I join the...?
  EXPRESSION: Eager
- CHARACTER: PELLE
  LINE: You’re American. Just jam yourself in there.
  EXPRESSION: Pragmatic
- CHARACTER: Narrator
  LINE: Christian uneasily JUMPS IN. He joins hands with two girls. Josh rises to follow Christian. Dani’s eyes follow them.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Pelle takes this opportunity to turn covertly to Dani:
  EXPRESSION: null
- CHARACTER: PELLE
  LINE: Hey: very quick:
  EXPRESSION: Secretive
- CHARACTER: Narrator
  LINE: He hands her a folded up DRAWING.
  EXPRESSION: null
- CHARACTER: PELLE
  LINE: Happy birthday.
  EXPRESSION: Warm
- CHARACTER: Narrator
  LINE: Dani, surprised, opens the paper. It’s a drawing of her FACE (donned with an extremely lush floral crown). The style is simple, but her likeness is captured beautifully.
  EXPRESSION: null
- CHARACTER: DANI
  LINE: Oh - my gosh. Pelle!
  EXPRESSION: Surprised
- CHARACTER: PELLE
  LINE: It’s just something I do for birthdays. Maybe it’s not appropriate?
  EXPRESSION: Hesitant
- CHARACTER: DANI
  LINE: Oh my God, not at all! It’s wonderful. Thank you, Pelle. I’m so touched.
  EXPRESSION: Grateful
- CHARACTER: PELLE
  LINE: Anyway. Just between us.
  EXPRESSION: Discreet
- CHARACTER: DANI
  LINE: Yeah, well - don’t worry. Christian forgot.
  EXPRESSION: Regretful
- CHARACTER: Narrator
  LINE: Pelle PAUSES, surprised. He doesn’t know what to say.
  EXPRESSION: null
- CHARACTER: DANI
  LINE: Or - I forgot to remind him. It doesn’t matter. Thank you so much for this, Pelle. It’s beautiful.
  EXPRESSION: Sincere
- CHARACTER: Narrator
  LINE: She folds the drawing back up.
  EXPRESSION: null

::SCENE::
LOCATION: Hårga Field
MOOD: Relaxed, Curious
CHARACTERS: Pelle, Josh, Dani, Christian, Connie, Ingemar, Simon
BACKGROUND_IMAGE: Hårga_field_tour.png
BACKGROUND_EDIT: "Field adjacent to farmstead, groups still dancing and playing in background"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The dance is over, although separate groups are still dancing and playing in the b.g.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Pelle is now leading our group on a TOUR. (Ingemar, Connie and Simon have joined along.) We track alongside.
  EXPRESSION: null
- CHARACTER: JOSH
  LINE: How do you guys support this place?
  EXPRESSION: Inquisitive
- CHARACTER: PELLE
  LINE: Lumbering, wheat, ve
  EXPRESSION: Factual

::SCENE::
LOCATION: Farmstead - Exterior
MOOD: Curious
CHARACTERS: Narrator, Ingemar, Pelle, Christian, Dani, Teacher, Children, Josh, Connie, Simon
BACKGROUND_IMAGE: farm_exterior.png
BACKGROUND_EDIT: "Sunny day, passing various points of interest on a farm"

::SCRIPT::
- CHARACTER: Narrator
  LINE: They pass a CIRCLE OF CHILDREN, accompanied by a TEACHER (60s). They’re carving RUNIC SYMBOLS into smooth, well-sanded STONES.
  EXPRESSION: null
- CHARACTER: Pelle
  LINE: Schooltime over here.
  EXPRESSION: null
- CHARACTER: Christian
  LINE: Carving runes?
  EXPRESSION: null
- CHARACTER: Teacher
  LINE: (smiles confirmation)
  EXPRESSION: null
- CHARACTER: Pelle
  LINE: Then they put it under their pillow and dream about its meaning.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Dani makes an “ooh” face. Josh makes a NOTE of this.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Christian sees that they’re now passing an old RUNESTONE (on their other side). It stands erect in an untended field.
  EXPRESSION: null
- CHARACTER: Christian
  LINE: Oh man - there’s a serious one.
  EXPRESSION: null
- CHARACTER: Josh
  LINE: Oh shit!
  EXPRESSION: null
- CHARACTER: Christian
  LINE: Which alphabet is that from?
  EXPRESSION: null
- CHARACTER: Josh
  LINE: Looks like the Elder Futhark. Right? Or is that medieval?
  EXPRESSION: null
- CHARACTER: Ingemar
  LINE: That’s actually the younger Futhark.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Josh nods “Ah, right” - visibly pained to be wrong.
  EXPRESSION: null
- CHARACTER: Connie
  LINE: So, how long’ve you two been together?
  EXPRESSION: null
- CHARACTER: Dani
  LINE: Oh, jeez...almost three years now!
  EXPRESSION: null
- CHARACTER: Christian
  LINE: Uhhh, well...two and half.
  EXPRESSION: null
- CHARACTER: Dani
  LINE: ...You’re joking. It’ll be three in fifteen days.
  EXPRESSION: null
- CHARACTER: Christian
  LINE: Okay, no, that is true. It is! You’re absolutely right.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: He makes a “sowwy” face, kisses her incredulous cheek, and changes the subject by asking Simon, Connie and Ingemar:
  EXPRESSION: null
- CHARACTER: Christian
  LINE: How did you guys all meet?
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: They look at each other. “Who answers?”
  EXPRESSION: null
- CHARACTER: Ingemar
  LINE: Well...we were all working on the same farm, and funny enough: I was dating Connie when Simon and me first became pals.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Simon’s eyes narrow.
  EXPRESSION: null
- CHARACTER: Connie
  LINE: Well - we‘d been on a date. Which I wasn’t even actually aware that it was a date.
  EXPRESSION: null
- CHARACTER: Ingemar
  LINE: Right, no, I meant that Connie and me had just become friends - we decided to be friends - and that was just before Connie and Simon started dating. And now they're engaged!
  EXPRESSION: null
- CHARACTER: Dani
  LINE: Oh wow. Congratulations.
  EXPRESSION: null
- CHARACTER: Ingemar
  LINE: Which is amazing. Yes. Congratulations.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Simon and Connie look uncomfortable. They smile “thank you.”
  EXPRESSION: null
- CHARACTER: Simon
  LINE: We’ve actually asked Ingemar to officiate the wedding.
  EXPRESSION: null
- CHARACTER: Dani
  LINE: You did?!
  EXPRESSION: null
- CHARACTER: Simon
  LINE: Nope.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Everybody LAUGHS - including Ingemar.
  EXPRESSION: null
- CHARACTER: Pelle
  LINE: And now...behold!
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: They have all arrived at a SMALL TREE.
  EXPRESSION: null
- CHARACTER: Pelle
  LINE: My tree.
  EXPRESSION: null
- CHARACTER: Christian
  LINE: Why your tree?
  EXPRESSION: null
- CHARACTER: Pelle
  LINE: When someone’s born, we plant a tree for that person and they grow up together. This one’s mine.
  EXPRESSION: null
- CHARACTER: Dani
  LINE: That’s so beautiful.
  EXPRESSION: null
- CHARACTER: Josh
  LINE: Is there a specific name for that practice?
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Christian points out a SMALL HOUSE which stands isolated in a large field. It has been painted a vivid yellow.
  EXPRESSION: null
- CHARACTER: Christian
  LINE: What about that house?
  EXPRESSION: null
- CHARACTER: Pelle
  LINE: Ah, that’s like a sacred temple. No one’s allowed in there.
  EXPRESSION: null
- CHARACTER: Christian
  LINE: Looks like it was just built.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Changing the subject, Pelle motions toward the MAIN HOUSE.
  EXPRESSION: null
- CHARACTER: Pelle
  LINE: This is where we sleep!
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: He leads them toward it. Meanwhile, Ingemar leads Simon and Connie in another direction.
  EXPRESSION: null
- CHARACTER: Ingemar
  LINE: Here: come see my tree!
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: On our group’s way to the Main House, they pass a CAGED BEAR.
  EXPRESSION: null
- CHARACTER: Mark
  LINE: So we’re just gonna ignore the bear, then.
  EXPRESSION: null
- CHARACTER: Pelle
  LINE: That’s a bear.
  EXPRESSION: null

::SCENE::
LOCATION: The Main House - Interior
MOOD: Awe
CHARACTERS: Narrator, Josh, Mark, Pelle, Christian, Dani
BACKGROUND_IMAGE: main_house_interior.png
BACKGROUND_EDIT: "Two-story barn-shaped house interior, beds lining walls, map on floor"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Josh leads our group through the two-storied interior of the huge, barn-shaped house. There is a large, square HOLE in the floor of the second story (so both stories are visible to each other). On both floors, the walls are lined with BEDS. The center of the bottom story is bare, like a dance floor. A MAP TO THE COSMOS has been painted on the floor, featuring sacred lines connecting notable stars.
  EXPRESSION: null
- CHARACTER: Pelle
  LINE: These’ll be yours.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Mark throws his bag onto one of them.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The group marvels at the walls, which are covered in INTRICATE MURALS. Runic letters abound. The CEILING is especially impressive. It’s painted to tell an epic story in hundreds of sequenced panels. At the center of the ceiling is a painting of the SUN. All stories lead to this (or do they come from this?).
  EXPRESSION: null
- CHARACTER: Christian
  LINE: Who all sleeps in here?
  EXPRESSION: null
- CHARACTER: Pelle
  LINE: All the younger ones. Until we turn thirty-two. Then we move to the houses.
  EXPRESSION: null
- CHARACTER: Josh
  LINE: Why thirty-two?
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Josh has pulled out his MOLESKIN NOTEPAD, ready to write down Pelle’s answer. Christian (almost in response) pulls out his phone, ready to type. Pelle PAUSES at this. He then explains, gesturing to a MURAL that dramatizes the following:
  EXPRESSION: null
- CHARACTER: Pelle
  LINE: We think of life like the seasons. You are a child until you’re 16, and that is the Spring. At some point we all do our Pilgrimage, and that’s between 17 and 32. That’s Summer. Then, from 33 to 52, you’re of working age: Fall. And finally from 53 to 72, you become a mentor.
  EXPRESSION: null
- CHARACTER: Josh
  LINE: Winter.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Josh and Christian have written all this down - their eyes intermittently piercing each other.
  EXPRESSION: null
- CHARACTER: Dani
  LINE: What happens when you turn 72, then?
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Pelle makes a comical THROAT SLASH gesture. Dani laughs, and begins to walk off.
  EXPRESSION: null
- CHARACTER: Mark
  LINE: Not a lot of privacy. What do you do when you wanna jerk off?
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Now that Dani is away, Pelle crosses quietly to Christian. He covertly ushers him aside.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Dani has found a wall of twelve FRAMED PHOTOGRAPHS. They all feature a different young woman dressed in ceremonial garb. In each photo, the woman is richly adorned in summer flowers and wears an impressive FLORAL CROWN. These photos have been taken annually for the last dozen years.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Dani looks over to notice Pelle WHISPERING to Christian, who now looks extremely GUILTY. She interrupts by bluntly asking:
  EXPRESSION: null
- CHARACTER: Dani
  LINE: Who are these of?
  EXPRESSION: null
- CHARACTER: Pelle
  LINE: Oh - those are our May Queens. You’ll actually be here for that.
  EXPRESSION: null
- CHARACTER: Josh
  LINE: Who are the “May Queens”?
  EXPRESSION: null
- CHARACTER: Pelle
  LINE: Every midsummer we do the dance of the Hårgas. All the younger women compete and the winner gets crowned.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Outside we hear:
  EXPRESSION: null
- CHARACTER: Odd (O.S.)
  LINE: Movie in twenty minutes! Field five!
  EXPRESSION: null

::SCENE::
LOCATION: Farmstead - Exterior
MOOD: Ominous
CHARACTERS: Narrator, Dani, Hårgan Man, Doctor, Doting Woman, Christian
BACKGROUND_IMAGE: farm_exterior_overcast.png
BACKGROUND_EDIT: "Overcast sky, outdoor film setup, ceremony with a baby"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Several Hårgans set up chairs on the grass. A 16MM FILM PROJECTOR is wheeled in to face a large PROJECTOR SCREEN.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Dani stands on the grass, under a now-overcast sky. An ominous RUMBLING in the distance. She closes her eyes, breathes deeply - practicing mindfulness.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: She is suddenly distracted by a baby’s CRYING. Dani looks off to see in the distance...
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: SEVERAL HÅRGANS are gathered around an OAK TREE. The VILLAGE DOCTOR (50) is crouched, cradling a CRYING BABY. He directs a doting WOMAN (50s) to pour some fresh dew (from a vial) into the baby’s mouth.
  EXPRESSION: null
- CHARACTER: Dani
  LINE: Excuse me? Can I ask if you know what’s happening over there?
  EXPRESSION: null
- CHARACTER: Hårgan Man
  LINE: Ah. Poor little Einar has the, em - where the bones are bad?
  EXPRESSION: null
- CHARACTER: Dani
  LINE: Oh no. Rickets?
  EXPRESSION: null
- CHARACTER: Hårgan Man
  LINE: (shrugs) Sorry, I don’t know.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The Doctor is now passing the baby through a WIDE CLEFT in the tree. The baby is received on the other side by the doting woman.
  EXPRESSION: null
- CHARACTER: Dani
  LINE: Do you know what they’re doing?
  EXPRESSION: null
- CHARACTER: Hårgan Man
  LINE: Old cure. Three times through the Oak.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The woman hands the baby to the Doctor again, and he passes the child back through the cleft. Again, the woman hands the child to the Doctor, and the baby is passed through one last time.
  EXPRESSION: null
- CHARACTER: Hårgan Man
  LINE: Now the healths of the baby and the tree are - together.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: On “together,” he illustratively hooks two fingers.
  EXPRESSION: null
- CHARACTER: Dani
  LINE: Like a - sympathetic connection?
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The man shrugs, confused. They SMILE at each other and the man walks off. Dani continues watching the ceremony, until--
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: CHRISTIAN appears behind her, holding a SOCKERKAKA (sponge cake). A lit candle protrudes from it. He approaches carefully...
  EXPRESSION: null
- CHARACTER: Christian
  LINE: Happy birthday to you -
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Dani turns, mortified.
  EXPRESSION: null
- CHARACTER: Christian
  LINE: Happy birthday to you, Happy birthday dear Dani (I love you) ... Happy birthday to you.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: She doesn’t blow out the candle.
  EXPRESSION: null
- CHARACTER: Christian
  LINE: You thought I forgot, didn’t you?
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Dani just glares at him.
  EXPRESSION: null
- CHARACTER: Christian
  LINE: You’re not surprised?
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Dani doesn’t soften. He finally RELENTS with a guilty smile:
  EXPRESSION: null
- CHARACTER: Christian
  LINE: Okay - I’m sorry. I’m really sorry. I thought it was tomorrow because of the sun. It’s impossible to tell.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: He kisses her. She doesn’t kiss back. He keeps kissing.
  EXPRESSION: null
- CHARACTER: Christian
  LINE: Happy birthday, happy birthday, I’m sorry. - You should be.
  EXPRESSION: null
- CHARACTER: Dani
  LINE: Fine. It’s fine. I’m not upset. - I know I should!
  EXPRESSION: null
- CHARACTER: Christian
  LINE: Happy birthday, mouse.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: She forces a tight smile and BLOWS OUT the candle.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: MEANWHILE: WOMEN fill the baby’s tree’s cleft with MUD and CLAY. They pack it tight. Then the MEN tie a ROPE around the tree. They draw it as TIGHTLY as possible.
  EXPRESSION: null

::SCENE::
LOCATION: Farmstead - Interior/Exterior
MOOD: Anticipatory
CHARACTERS: Narrator, Dani, Christian, Mark, Josh, Pelle, Plump Elder
BACKGROUND_IMAGE: farm_film_screening.png
BACKGROUND_EDIT: "People gathered, projector set up, screen ready"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Everyone has gathered to either sit in chairs or on the grass. They all face the PROJECTOR SCREEN.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Dani, Christian, Mark, Josh and Pelle sit crossed-legged in the front. The PLUMP ELDER stands before the screen to announce:
  EXPRESSION: null
- CHARACTER: Plump Elder
  LINE: And now, for tradition and for fun: a work of antique escapism - and an annual mood-setter, made by one of our own lost Hårgans!
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The Plump Elder joins the audience, and the projector starts to RATTLE. Before the film starts, Christian WHISPERS to Dani:
  EXPRESSION: null
- CHARACTER: Christian
  LINE: Happy birthday.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: ON THE PROJECTOR SCREEN: A SILENT COLOR FILM begins. It is weathered and grainy. The film seems to have been made in the late 1960s or early ‘70s (shot on a Bolex camera). The TITLE appears (in Swedish): A Midsummer Romance
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The film opens on a beautiful BLONDE GIRL (15) walking through a field with her friends. They pause to admire a GANG OF BOYS. The girl fixes on one BLONDE BOY (15). It’s love
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue watching the film"
  TARGET: midsummer_romance_film
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Not specified
MOOD: Enchantment
CHARACTERS: Narrator, Group of Girls, Group of Boys
BACKGROUND_IMAGE: null
BACKGROUND_EDIT: "Daytime, outdoors"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The group of girls walks over to the boys. They talk.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Hello lads! Happy midsummer to you.”
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Why thank you, girls! And a happy midsummer to you.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: One of the girls looks mischievously to her friends, and then puts an idea to the boys.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Why don’t you lads come to our house for lunch tomorrow? We will prepare a feast and you can be our special guests!
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The boys look to each other and nod. They agree.
  EXPRESSION: null

::PATHS::
- CHOICE: "Accept the invitation"
  TARGET: midsummer_rituals
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Meadow
MOOD: Ritualistic
CHARACTERS: Narrator, Girls
BACKGROUND_IMAGE: meadow.png
BACKGROUND_EDIT: "Lush meadow, daytime"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The next scene depicts the girls gathering flowers from a lush meadow. They pick these flowers with their left hand as they walk backwards. We cycle through nine close-ups of different flowers being picked.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Nine Flowers Picked (don’t forget the Orpine!) and Nine Fences Jumped.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The girls jump over a series of small fences. This is done nine times.
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue to the bedroom ritual"
  TARGET: bedroom_ritual
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Bedroom
MOOD: Anticipation
CHARACTERS: Narrator, Blonde Girl
BACKGROUND_IMAGE: bedroom.png
BACKGROUND_EDIT: "Bedroom, daytime"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The next scene reveals the blonde girl in her bedroom. She puts the nine flowers under her pillow, and then lies down in bed. She closes her eyes to sleep.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: With the nine flowers under her pillow, she will now dream of the boy she is to marry.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The blonde girl has fallen asleep, and a cloudy dream bubble appears beside her head. Inside the bubble, we are given a scene in which the blonde girl is marrying the blonde boy. He lifts her bride’s veil to kiss her.
  EXPRESSION: null

::PATHS::
- CHOICE: "Proceed to the next day"
  TARGET: kitchen_ritual
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Kitchen
MOOD: Preparation
CHARACTERS: Narrator, Girls, Boys, Blonde Girl, Blonde Boy
BACKGROUND_IMAGE: kitchen.png
BACKGROUND_EDIT: "Kitchen, daytime"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The next morning the girl wakes up. She wears a wicked smile. Later that day, the girls are gathered in the kitchen. They are cooking. The boys all arrive in the living room. Our blonde girl says “hello” to the boy of her dreams.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Hello! Can I bring you some coffee while you wait for your pancake?
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The boy nods excitedly. The girl goes off to the kitchen.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: In the kitchen, the girl takes a cup of coffee and sets it on the floor. She then crouches over the coffee.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Three droplets of menstrual blood for the spell to take effect.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Three drops of blood drip from between the girl’s legs. They land in the coffee.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: In the audience, Dani and Mark wince at this. Christian and Josh (along with the surrounding Hårgans) are delighted.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: On the projector screen: The girl brings the coffee to the boy. She smiles mischievously as he takes a sip.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: In the kitchen, the girl now props her leg up onto a chair. She takes a pair of scissors and snips between her legs. She pulls a few strands of pubic hair from her groin.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The girl chops up the pubic hair into fine pieces. She then sprinkles them into a bowl of pancake batter. The batter is then poured onto a burning skillet.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Hair from the vulva will complete the spell.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The girl hands the boy his pancake. He eats the pancake, and then looks up at the girl. Spirals appear in his eyes. Spellbound, he moves toward her, like a love-stricken zombie.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Voilà! The spell was a success.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The boy and girl kiss in close-up. We pull out from the CU to reveal that the girl is now pregnant with a grossly distended belly. They are surrounded by a huge and adoring crowd, all wearing identical clothing.
  EXPRESSION: null

::PATHS::
- CHOICE: "Fade to white"
  TARGET: ending
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Main House Interior
MOOD: Unease
CHARACTERS: Narrator, Dani, Pelle, Christian, Josh, Babies, Women
BACKGROUND_IMAGE: main_house_interior.png
BACKGROUND_EDIT: "Main house interior, night, windows boarded up, sunlight peeking through"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Fade to white. The end. The audience applauds politely. Maja, however, looks entranced. Mark and Dani wear inscrutable grins. (Slightly charmed, mostly disturbed.) Josh and Christian are buzzing.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The windows have been boarded up for the night. Sunlight peeks from the edges. People are climbing into their beds. There are two baby cribs in the corner, stationed near the beds of women in their twenties. Both bedframes are made of severe-looking iron and metal.
  EXPRESSION: null
- CHARACTER: Dani
  LINE: Pretty serious-looking cribs.
  EXPRESSION: Curious
- CHARACTER: Pelle
  LINE: For the iron. Keeps away the “invisibles.” So the babies don’t get “changed.”
  EXPRESSION: Sarcastic
- CHARACTER: Narrator
  LINE: Pelle smiles sardonically, knowing how it sounds.
  EXPRESSION: null
- CHARACTER: Dani
  LINE: How real is that stuff for you guys?
  EXPRESSION: Inquisitive
- CHARACTER: Pelle
  LINE: Ah, who knows?
  EXPRESSION: Deflecting
- CHARACTER: Narrator
  LINE: Dani smiles. She looks over to Christian, whose eyes are glued tensely to Josh’s notepad as he scrawls “Iron. Babies changed. ‘Invisibles.’” Christian looks threatened.
  EXPRESSION: null
- CHARACTER: Pelle
  LINE: All right - beauty rest! Tomorrow’s a big day.
  EXPRESSION: Determined
- CHARACTER: Josh
  LINE: And what’s tomorrow?
  EXPRESSION: Curious
- CHARACTER: Pelle
  LINE: First of the big ceremonies.
  EXPRESSION: Mysterious
- CHARACTER: Josh
  LINE: So you’re just gonna be weird and cryptic?
  EXPRESSION: Annoyed
- CHARACTER: Narrator
  LINE: Pelle pauses, then takes Josh’s notepad. He writes “Ättestupan” and hands it back.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Josh happens to know that word. His eyes widen. “Are you serious?” Pelle smiles mischievously.
  EXPRESSION: null
- CHARACTER: Christian
  LINE: What’s that? What’s Ättestupan?
  EXPRESSION: Curious
- CHARACTER: Narrator
  LINE: Pelle gestures for Christian to keep his voice down. Christian pulls out his phone and types “Atestupan” into a search engine. But there’s no internet connection.
  EXPRESSION: null
- CHARACTER: Christian
  LINE: Fuck. What’s Ättestupan?
  EXPRESSION: Frustrated
- CHARACTER: Narrator
  LINE: Josh smugly climbs into bed. This has made Dani nervous.
  EXPRESSION: null
- CHARACTER: Dani
  LINE: Is it scary?
  EXPRESSION: Nervous
- CHARACTER: Josh
  LINE: You’ll see.
  EXPRESSION: Teasing

::PATHS::
- CHOICE: "Go to sleep"
  TARGET: main_house_night_sleep
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Main House Interior
MOOD: Quiet Vigil
CHARACTERS: Narrator, Dani, Christian, Mark, Baby, Woman, Happy Man, Friends, Sun
BACKGROUND_IMAGE: main_house_interior_night.png
BACKGROUND_EDIT: "Main house interior, night, everyone asleep"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Everyone is asleep. Silence, save for the baby’s crying.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Dani lies awake. Beside her: Christian sleeping soundly. To her other side: Mark snoring.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Dani shifts her weight. She looks over at the wall mural, and notices an illustration of a happy man opening his wrist with a special knife. He is surrounded by smiling friends, and above him, a smiling sun. Dani looks unnerved, but her attention is suddenly drawn away by the sound of...
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: A teenaged boy and girl (clearly new lovers) sneak quietly out of their beds. Giggling. They tip-toe out of the house, careful to make no noise.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Dani stares at this. Heavy.
  EXPRESSION: null

::PATHS::
- CHOICE: "Wait for morning"
  TARGET: field_morning_goat
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Field
MOOD: Ceremony
CHARACTERS: Narrator, Men, Onlookers
BACKGROUND_IMAGE: field_goat_figure.png
BACKGROUND_EDIT: "Field, morning, goat-shaped straw figure"

::SCRIPT::
- CHARACTER: Narrator
  LINE: A goat-shaped straw figure. It’s the size of an actual goat and notably well-crafted.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: An axe comes down to swiftly lop off its head.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Then another axe comes down to strike its body in half.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: We cut wide to reveal that it’s being chopped into clean pieces by three men in ceremonial garb. Onlookers abound.
  EXPRESSION: null

::PATHS::
- CHOICE: "Observe the next ritual"
  TARGET: crop_field_burial
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Crop Field
MOOD: Sacred Burial
CHARACTERS: Narrator, Farmers, Man
BACKGROUND_IMAGE: crop_field_burial.png
BACKGROUND_EDIT: "Crop field, morning"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Farmers bury different pieces of the chopped-up straw goat into four corners of a flourishing grain field.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: At the field’s center: A man pours a bowl of lamb’s blood into a carefully hollowed hole in the earth. After this, the straw goat’s head is dropped in. The hole is then covered up with soil.
  EXPRESSION: null

::PATHS::
- CHOICE: "Move to the next location"
  TARGET: field_morning_tables
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Field
MOOD: Festive Preparation
CHARACTERS: Narrator, Men, Women, Group
BACKGROUND_IMAGE: field_tables_dew.png
BACKGROUND_EDIT: "Field, morning, dining tables being set up, women collecting dew"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Near the Main House, several men are setting up dining tables on the grass. They are laying them out to form a pattern.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: In one field, a group of women collect the morning dew (in small vials) from the leaves and grass. They throw a sheet over the wet grass. It absorbs the dew, and they wring it out into a pail.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: We pan away from this to yet another field, where a large group has assembled for what appears to be some sort of dance class. They stand in rows of ten. Dani, Josh, Mark, Pelle and Christian are among them.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: At the head of the class is a thin elder (60s) with an impressive physique. In demonstration, he lifts his arm and waves it fluidly, rhythmically, emotionally, back and forth.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The class imitates him. They strive to perfectly match his movements and emotions.
  EXPRESSION: null
- CHARACTER: Thin Elder
  LINE: Don’t just copy me. Feel me.
  EXPRESSION: Encouraging
- CHARACTER: Narrator
  LINE: The class continues to mimic his movements. Mark, Josh and Christian are looking quite graceless. Dani, however, matches the Elder’s movements with surprising sensitivity. Pelle notices this.
  EXPRESSION: null
- CHARACTER: Thin Elder
  LINE: The Elder stops. So does everyone else. The Elder swiftly affects a different posture. (This time he goes to his tip-toes, one hand curled at his abdomen and the other arm draped mournfully around his head.)
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The class now imitates this. The Hårgas are impressive in their poise and precision, and Dani is fitting right in. (Josh and Christian - not so much.) Once everybody finds this position, the Elder fluidly contorts his body to assume another.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: A sleepy Mark has stopped trying altogether. He looks over to a woman beside him. He smiles at her, but her gaze remains fixed seriously ahead. For the Hårgas, this is a spiritual practice.
  EXPRESSION: null
- CHARACTER: Pretty Brunette
  LINE: Try.
  EXPRESSION: Encouraging
- CHARACTER: Mark
  LINE: What?
  EXPRESSION: Confused
- CHARACTER: Pretty Brunette
  LINE: Try.
  EXPRESSION: Smiling
- CHARACTER: Narrator
  LINE: Mark smiles, not understanding. He’s smitten. He half-attempts to join in, only to immediately give up again.
  EXPRESSION: null

::PATHS::
- CHOICE: "Proceed to the feast setup"
  TARGET: farmstead_feast
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Farmstead
MOOD: Communal Gathering
CHARACTERS: Narrator, Community, Our Group, Girls, Dani, Christian, Boy, Elderly Men
BACKGROUND_IMAGE: farmstead_feast.png
BACKGROUND_EDIT: "Farmstead, one hour later, dining tables in a circle"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The dining tables have been set up to form a wide circle. Inside the circle, at the center, is a round yellow table (representing the sun). There are no seats for this table. Half of the community is already standing at the surrounding tables. The other half is arriving now. Plates of food have already been placed. No one sits.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Our group (minus Dani) arrives at one of the tables. They gaze around, trying to understand the etiquette. They notice that a few lingering girls walk backwards through a neighboring field, picking flowers.
  EXPRESSION: null
- CHARACTER: Dani
  LINE: Ja!
  EXPRESSION: Happy
- CHARACTER: Christian
  LINE: ...Tack så mycket.
  EXPRESSION: Strained appreciation
- CHARACTER: Narrator
  LINE: He kisses her cheek.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Now that everyone is stationed at the tables, a boy runs off to officially summon the guests of honor...
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: After a moment, two elderly men (72), both wearing ornate golden dresses, enter the scene. (We will recognize them as the elderly men who ran around the Main House three times with the flaming torches.) They stand with alert posture, maintaining an awareness of their bodies as they walk. They arrive at two large wooden chairs
  EXPRESSION: null

::PATHS::
- CHOICE: "Witness the arrival of guests of honor"
  TARGET: end
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Dining Hall
MOOD: Ceremony
CHARACTERS: Narrator, Josh, Pelle, Mark, Christian, Maja, Blonde Woman, Siv, Simon, Connie, Ingemar
BACKGROUND_IMAGE: dining_hall.png
BACKGROUND_EDIT: "Beautifully decorated table with fine silverware and golden plates, other tables seat five, but this one has been reserved for two."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Josh mouths to Pelle: “Are those the ones?” Pelle smiles.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The two men SIT. This prompts everyone else to sit.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Mark picks up his fork, only to notice that no one else has begun eating. Everyone waits patiently. Total SILENCE, save for the baby who is still crying.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Finally, the two men pick up their silverware and begin to eat. Now everyone starts eating.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Josh is scrutinizing every detail. Christian scrutinizes Josh.
  EXPRESSION: null

::SCENE::
LOCATION: Dining Hall - Mid-Meal
MOOD: Suspense
CHARACTERS: Narrator, Maja, Two Elderly Men, Dani, Blonde Woman, Josh, Christian
BACKGROUND_IMAGE: dining_hall_midmeal.png
BACKGROUND_EDIT: "Maja feverishly carves a small rune stone in her lap. The two elderly men are receiving lots of attention. Near Dani, a blonde woman cradles the crying baby."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Maja feverishly carves a small RUNE STONE in her lap. She is hunched over to conceal her progress from curious eyes.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The two elderly men are receiving lots of attention.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Near Dani, a BLONDE WOMAN (30s) cradles the CRYING BABY.
  EXPRESSION: null
- CHARACTER: Dani
  LINE: Is your baby okay?
  EXPRESSION: Concerned
- CHARACTER: Blonde Woman
  LINE: Oh, she will be. She has a bone problem. She is not “mine,” though.
  EXPRESSION: Neutral
- CHARACTER: Dani
  LINE: Oh, I’m sorry...!
  EXPRESSION: Apologetic
- CHARACTER: Blonde Woman
  LINE: No no - her birth mother is on pilgrimage. It helps them to detach. The babies are raised here by everyone.
  EXPRESSION: Neutral
- CHARACTER: Narrator
  LINE: Dani smiles at this idea. Josh and Christian are also taken by this. Josh SEES Christian’s excitement, and quietly HARDENS.
  EXPRESSION: null
- CHARACTER: Blonde Woman
  LINE: How is your family like?
  EXPRESSION: Inquiring
- CHARACTER: Dani
  LINE: Mine? Oh no, mine are...not here anymore.
  EXPRESSION: Embarrassed
- CHARACTER: Narrator
  LINE: Christian suddenly looks nervous about this exchange.
  EXPRESSION: null
- CHARACTER: Blonde Woman
  LINE: “Not here”?
  EXPRESSION: Inquiring
- CHARACTER: Dani
  LINE: Ha. Unfortunately not. It’s okay...
  EXPRESSION: Embarrassed
- CHARACTER: Blonde Woman
  LINE: Not any?
  EXPRESSION: Concerned
- CHARACTER: Narrator
  LINE: The Blonde Woman has TEARS in her eyes. She looks sincerely affected by this.
  EXPRESSION: null
- CHARACTER: Dani
  LINE: Oh God, no, I’m sorry. I shouldn’t have said. We’re enjoying our food.
  EXPRESSION: Panicked
- CHARACTER: Blonde Woman
  LINE: Am I making you sad to ask?
  EXPRESSION: Worried
- CHARACTER: Dani
  LINE: No no. I just shouldn’t have mentioned it.
  EXPRESSION: Reassuring
- CHARACTER: Blonde Woman
  LINE: Please know we can talk if you like. Please. I am happy to talk.
  EXPRESSION: Empathetic
- CHARACTER: Dani
  LINE: Okay, thank you. Sorry. I feel silly. Thank you. Sorry.
  EXPRESSION: Uncomfortable
- CHARACTER: Narrator
  LINE: Christian shrugs: “Don’t apologize to me.”
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Siv, a table over, has been avidly watching this exchange.
  EXPRESSION: null

::SCENE::
LOCATION: Dining Hall - Minutes Later
MOOD: Somber Ceremony
CHARACTERS: Narrator, Mark, Pretty Brunette, Elderly Men, Siv, Musicians, Middle-Aged Men, Dani, Christian, Josh, Pelle
BACKGROUND_IMAGE: dining_hall_after_meal.png
BACKGROUND_EDIT: "Everyone has finished eating. A hush falls awkwardly over the procession. Silence, save for the wailing baby. Mark, half-asleep, looks around. The Pretty Brunette smiles at him. One of the elderly men stands, clears his throat, and begins to sing a wordless, choral song. The other man joins in. Siv stands to raise her glass."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Everyone has finished eating. Another HUSH falls awkwardly over the procession. Silence, save for the wailing baby.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Mark, half-asleep, confusedly looks around. He sees the Pretty Brunette SMILING at him. Caught off guard, he BLUSHES and smiles back (a little too eagerly).
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: One of the two elderly men STANDS. Clears his throat. Closes his eyes. After a moment, he begins to SING a wordless, choral song.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Everyone watches, rapt and emotional.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: At the appropriate time, the OTHER MAN begins to sing along, softly and awkwardly at first. Soon he rises, singing with greater projection. When the song comes to a finish, Siv stands to RAISE her glass. This prompts everyone else to stand. They all raise their aquavit.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: A long silence. Siv finally DRINKS. So does everyone else.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The MUSICIANS begin to play their handmade instruments, and EIGHT MIDDLE-AGED MEN break into two groups. They walk to either of the elderly men’s chairs, HOIST them up, and start CARRYING THEM OFF.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The congregation follows behind as the elevated men are carried up a hill. Our group JOINS them, confused. Mark lags behind.
  EXPRESSION: null
- CHARACTER: Mark
  LINE: I think I’m gonna take a nap. Jetlag and the shrooms...
  EXPRESSION: Tired
- CHARACTER: Narrator
  LINE: Mark heads back toward the Main House. Dani, Christian, Josh and Pelle proceed to follow the community.
  EXPRESSION: null

::SCENE::
LOCATION: Hill
MOOD: Procession
CHARACTERS: Narrator, Elderly Men, Procession, Mark, Dani, Christian, Josh, Pelle
BACKGROUND_IMAGE: hill.png
BACKGROUND_EDIT: "Everyone happily follows the elderly men of honor (still carried on hoisted thrones). They follow a narrow trail of flowers up a hill. There is a fork in the trail, leading either to the left and downward or continuing straight ahead and upward. The elderly men are carried straight ahead, continuing to ascend the rising hill. The following procession branches off to veer left. They continue down a slope that leads to a beach."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Everyone happily follows the elderly men of honor (still carried on hoisted thrones). They follow a narrow TRAIL OF FLOWERS up a hill.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: There is a FORK in the trail, leading either to the left and downward or continuing straight ahead and upward.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The elderly men are carried straight ahead, continuing to ascend the rising hill. The following procession BRANCHES OFF to veer left. They continue down a slope that leads to a BEACH.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Our group, squinting with curiosity, begins following the procession toward the beach. But Pelle slows down.
  EXPRESSION: null
- CHARACTER: Pelle
  LINE: Okay - actually: let’s stop a moment.
  EXPRESSION: Pausing
- CHARACTER: Narrator
  LINE: He holds them back.
  EXPRESSION: null
- CHARACTER: Pelle
  LINE: I need to warn you before we go down... because you might not want to.
  EXPRESSION: Serious
- CHARACTER: Dani
  LINE: Is this gonna be something weird?
  EXPRESSION: Nervous
- CHARACTER: Pelle
  LINE: Uhhh - it might seem very weird, but it’s a great honor for them.
  EXPRESSION: Hesitant
- CHARACTER: Dani
  LINE: ...Is this the thing you mentioned last night?
  EXPRESSION: Inquiring
- CHARACTER: Josh
  LINE: Ättestupan.
  EXPRESSION: Knowing
- CHARACTER: Pelle
  LINE: We’re about to perform a centuries-old rite that is very important to us and very beautiful, but also - very far from anything you have in America.
  EXPRESSION: Explaining
- CHARACTER: Dani
  LINE: ...Do I not want to do this?
  EXPRESSION: Apprehensive
- CHARACTER: Pelle
  LINE: Well - that’s what I’m saying. You’re invited to. I just... You remember I explained the winter stage of a man’s life goes from 53 to 72? Well, this is what happens when 72 is reached.
  EXPRESSION: Explaining
- CHARACTER: Dani
  LINE: Okay. And what is “this”?
  EXPRESSION: Inquiring
- CHARACTER: Narrator
  LINE: Pelle pauses, considering his words. Dani grows more nervous.
  EXPRESSION: null
- CHARACTER: Dani
  LINE: What is Ättestupan?
  EXPRESSION: Inquiring
- CHARACTER: Narrator
  LINE: Josh can’t suppress a smile - anticipating Pelle’s answer.
  EXPRESSION: null

::SCENE::
LOCATION: Beach
MOOD: Foreboding
CHARACTERS: Narrator, Community, Our Group, Simon, Connie, Ingemar, Christian, Dani, Siv, Josh, Pelle, Two Elderly Men
BACKGROUND_IMAGE: beach.png
BACKGROUND_EDIT: "The community has gathered on the rocky beach. Tall cliffs loom imposingly. The baby cries in the background. Our group stands to the side, along with Simon, Connie and Ingemar. Christian turns to Dani, who looks extremely uneasy."

::SCRIPT::
- CHARACTER: Narrator
  LINE: The community has gathered on the rocky beach. Tall CLIFFS loom imposingly. The baby cries in the b.g.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Our group stands to the side, along with Simon, Connie and Ingemar. Christian turns to DANI, who looks extremely uneasy.
  EXPRESSION: null
- CHARACTER: Christian
  LINE: Are you sure you can handle this?
  EXPRESSION: Concerned
- CHARACTER: Narrator
  LINE: Dani doesn’t know the answer to this.
  EXPRESSION: null
- CHARACTER: Christian
  LINE: Maybe you should go back to the main house? It’s not too late.
  EXPRESSION: Concerned
- CHARACTER: Narrator
  LINE: Dani starts to wrestle with this, but then:
  EXPRESSION: null
- CHARACTER: Dani
  LINE: No. I need to try.
  EXPRESSION: Determined
- CHARACTER: Narrator
  LINE: A HORN sounds. All eyes go to...
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: SIV, the Matriarch, holds a LEATHER-BOUND BOOK whose cover is marked by runic letters. In Swedish, she formally addresses the congregation - like a priest to a parish - before opening the book. Its scripture is written in runes and unknown hieroglyphs (the AFFECT language).
  EXPRESSION: null
- CHARACTER: Josh
  LINE: What’s that book?
  EXPRESSION: Inquiring
- CHARACTER: Narrator
  LINE: Christian leans in to hear the answer:
  EXPRESSION: null
- CHARACTER: Pelle
  LINE: Rubi Radr. Our scripture.
  EXPRESSION: Informative
- CHARACTER: Josh
  LINE: Can I possibly read that?
  EXPRESSION: Curious
- CHARACTER: Pelle
  LINE: You would not be able.
  EXPRESSION: Firm
- CHARACTER: Narrator
  LINE: Siv, eyes on the page, surprises our group by beginning to SING a wordless hymn. It’s beautiful, yet feels improvised, as if inspired (on the spot) by emotions provoked by the text.
  EXPRESSION: null

::SCENE::
LOCATION: Cliff
MOOD: Ritualistic Sacrifice
CHARACTERS: Narrator, Two Elderly Men, Rune Stones
BACKGROUND_IMAGE: cliff.png
BACKGROUND_EDIT: "The two elderly men have been carried to the top of a cliff overlooking the beach. Their chairs are set down near the precipice. They are placed beside freshly carved (and impressively sized) rune stones. The elders rise from their seats. They are each handed a ceremonial blade. They stoically drag the blade across their palms, drawing blood. The men rub their palms together, making their hands nice and bloody. They press their palms onto their rune stones, both leaving two bloody hand-prints."

::SCRIPT::
- CHARACTER: Narrator
  LINE: The two elderly men have been carried to the top of a CLIFF over looking the beach. Their chairs are SET DOWN near the precipice. They are placed beside freshly carved (and impressively sized) RUNE STONES.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The elders rise from their seats. They are each handed a CEREMONIAL BLADE. They stoically drag the blade across their palms, DRAWING BLOOD.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The men rub their palms together, making their hands nice and bloody. They press their palms onto their rune stones, both leaving TWO BLOODY HAND-PRINTS.
  EXPRESSION: null

::SCENE::
LOCATION: Beach
MOOD: Horrified Silence
CHARACTERS: Narrator, Everyone, Dani, Christian, Connie, Simon, Pelle, Two Elderly Men, Birds
BACKGROUND_IMAGE: beach_cliff_view.png
BACKGROUND_EDIT: "Everyone looks up at the cliff's peak. Dani is sweating beads now, her breathing erratic. Finally, the two elderly men appear at the edge. Rapt silence. One of the elderly men announces something loudly in Swedish. The elderly man LEAPS OFF THE PRECIPICE. Connie and Simon SCREAM. The man plummets 200 feet to land fatally on the jagged rocks below. Upon impact, a flock of birds alights from a tree. Our group is shocked into horrified silence. Dani looks like she’s been knocked out of her body. The birds fly over Dani’s head, and a sudden rush courses through her."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Everyone looks up at the cliff’s peak. Dani is SWEATING BEADS now, her breathing erratic.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Finally, the TWO ELDERLY MEN appear at the edge.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Rapt silence.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: One of the elderly men ANNOUNCES something loudly in Swedish.
  EXPRESSION: null
- CHARACTER: Josh
  LINE: What did he say?
  EXPRESSION: Inquiring
- CHARACTER: Narrator
  LINE: But Pelle ignores Josh. His eyes are glued to the men. Josh redirects his attention to the cliff-top.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Dani BRACES herself. Her TEETH begin to chatter. She GRABS Christian’s arm, and then --
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The elderly man LEAPS OFF THE PRECIPICE. Connie and Simon SCRAM. The man plummets 200 feet to LAND FATALLY on the jagged rocks below. Upon impact, a FLOCK OF BIRDS ALIGHTS from a tree.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Our group is shocked into horrified silence. Dani looks like she’s been knocked out of her body. The birds fly over Dani’s head, and a sudden rush courses through her.
  EXPRESSION: null

::SCENE::
LOCATION: Beach
MOOD: Grim Resolution
CHARACTERS: Narrator, Other Elderly Man, Simon, Connie, Community, Three Men, Plump Elder, Dying Man, Mentor, Laborer, Youth
BACKGROUND_IMAGE: beach_cliff_view_second_jump.png
BACKGROUND_EDIT: "The other elderly man steps up to the precipice. He announces something in Swedish. The man LAUNCHES HIMSELF OFF THE CLIFF. Connie GASPS. The man plummets straight down, landing not only on his feet, but also on the fresh corpse of his friend. This softens the blow, preventing the fall from killing him. The man, all broken bones now, WAILS in horrible pain. The community grumbles with concern. Everyone turns to three men. Simon panics. The plump elder approaches the three men with a cudgel. The cudgel is handed over to the Mentor."

::SCRIPT::
- CHARACTER: Narrator
  LINE: The OTHER ELDERLY MAN - the one whose torch burnt out before circling the house three times - now steps up to the precipice. He also announces something in Swedish.
  EXPRESSION: null
- CHARACTER: Simon
  LINE: What’s happening? Is he gonna jump, too? No--
  EXPRESSION: Panicked
- CHARACTER: Narrator
  LINE: The man LAUNCHES HIMSELF OFF THE CLIFF. Connie GASPS. The man plummets straight down, landing not only ON HIS FEET, but also on the fresh corpse of his friend. This softens the blow, preventing the fall from killing him. The man, all broken bones now, WAILS in horrible pain.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The community grumbles with concern. Everyone turns to THREE MEN, each the oldest of their respective generations (the youths, the laborers, and the mentors). They understand what they must do.
  EXPRESSION: null
- CHARACTER: Simon
  LINE: Why did that just happen? We need to call an ambulance.
  EXPRESSION: Panicked
- CHARACTER: Ingemar
  LINE: It’s okay.
  EXPRESSION: Calm
- CHARACTER: Simon
  LINE: What’s okay?! CALL AN AMBULANCE! Everybody’s just watching!
  EXPRESSION: Panicked
- CHARACTER: Narrator
  LINE: The PLUMP ELDER approaches the three men with a CUDGEL. This is a long-handled club with a pointed block of wood at the end. The cudgel is handed over to the MENTOR.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Dani watches, overwhelmed, as the three men (now armed with the cudgel) stalk over to the dying man. The dying man moans pathetically, in too much pain to scream.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: From DANI’S POV: The men have arrived at the dying elder’s feet. The mentor RAISES the cudgel, and brutally swings it down onto the old man’s HEAD. This isn’t a fatal blow. The man raises the cudgel again, and this time he STRIKES the elder with enough force to silence him.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The mentor hands the cudgel to the LABORER. He raises the cudgel and brings it down onto the old man’s crown. The elder’s leg goes into pathetic SPASMS. Blood gurgling. The laborer BLUDGEONS him once more. He goes limp, probably dead.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The YOUTH is now handed the cudgel. He delivers two brutal swings to the old man’s head. The mentor gently takes the cudgel away from the youth, and they all return to the community. The mentor hands the Plump Elder the cudgel, and everyone sta
  EXPRESSION: null

::SCENE::
LOCATION: FIELD
MOOD: Contemplative, Shocked
CHARACTERS: Narrator, Dani, Christian, Josh, Siv, Connie, Simon, Ingemar
BACKGROUND_IMAGE: field.png
BACKGROUND_EDIT: "Daytime, group observing something traumatic"

::SCRIPT::
- CHARACTER: Narrator
  LINE: ...nds in respectful, contemplative silence.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Dani is GRIPPING Christian’s arm. She is completely shell-shocked. Christian turns to Josh; they exchange “holy shit” looks. More EXCITED than troubled.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Siv bounds over to Connie and Simon, who are in a panic. Dani trembles, powder-white. Traumatized.
  EXPRESSION: null
- CHARACTER: Siv
  LINE: Ingemar! Did you not warn them?
  EXPRESSION: Agitated
- CHARACTER: Ingemar
  LINE: I’m sorry, grandmother Siv! I kind of warned them.
  EXPRESSION: Apologetic
- CHARACTER: Simon
  LINE: Nobody did anything! Everyone just watched that!
  EXPRESSION: Angry
- CHARACTER: Siv
  LINE: Oh my, poor things--
  EXPRESSION: Empathetic
- CHARACTER: Simon
  LINE: You’re all just standing calmly around!!
  EXPRESSION: Angry
- CHARACTER: Narrator
  LINE: Siv lays an empathic hand on Simon and Connie’s shoulder.
  EXPRESSION: null
- CHARACTER: Siv
  LINE: Oh, mercy - please: You should have been warned better. What you just saw is a long, long, long observed custom. Those two men has just reached end of the Hårga life-cycle.
  EXPRESSION: Empathetic
- CHARACTER: Narrator
  LINE: Siv now looks into DANI’S eyes, but Dani is in a daze. She seems to have been knocked into a dissociative state.
  EXPRESSION: null
- CHARACTER: Siv
  LINE: It is a great joy for them, you must realize. And when I do so, it will be a great joy for me.
  EXPRESSION: Serene
- CHARACTER: Siv
  LINE: We view life as a circle. Okay? A re-cycle. One thing falls and another rises. The first man who jumped: his name was Olof. Yes?
  EXPRESSION: Calm
- CHARACTER: Narrator
  LINE: Siv points to a PREGNANT WOMAN:
  EXPRESSION: null
- CHARACTER: Siv
  LINE: That baby, who is not yet born, will inherit this name. He will be Olof. And if it is a girl, she will take the name of our last fallen lady, which was Dagmar.
  EXPRESSION: Calm
- CHARACTER: Narrator
  LINE: Dani gazes at Siv, who has taken on a strange ETHEREAL GLOW (like an angel).
  EXPRESSION: null
- CHARACTER: Siv
  LINE: But instead of growing old and getting sick and dying in pain and shame and fear, we’ll give our life - as a gesture. Yes? A gift. And we will leave this chapter with dignity and gratitude. Before it can spoil.
  EXPRESSION: Serene
- CHARACTER: Narrator
  LINE: Siv releases Simon and Connie, who are no less fraught. Siv now addresses the whole group.
  EXPRESSION: null
- CHARACTER: Siv
  LINE: It does no good to die kicking and screaming and lashing back at the inevitable. It corrupts the soul.
  EXPRESSION: Wise
- CHARACTER: Ingemar
  LINE: I’m sorry I did not warn you better.
  EXPRESSION: Apologetic

::PATHS::
- CHOICE: "Walk back from the beach"
  TARGET: field_2
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: EXT. FIELD - DAY
MOOD: Urgency, Distress
CHARACTERS: Narrator, Josh, Christian, Dani, Simon
BACKGROUND_IMAGE: field_day.png
BACKGROUND_EDIT: "Daytime, group walking back from beach, Josh rushing"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Everyone is walking back from the beach. JOSH rushes feverishly toward the Main House. Christian’s eyes are trained on him as he moves to Dani, who looks destroyed.
  EXPRESSION: null
- CHARACTER: Christian
  LINE: You okay, baby?
  EXPRESSION: Concerned
- CHARACTER: Dani
  LINE: I need to not be here right now.
  EXPRESSION: Distressed
- CHARACTER: Christian
  LINE: Okay. Good idea. You walk. I’ll find you in a second - okay?
  EXPRESSION: Reassuring
- CHARACTER: Narrator
  LINE: Dani walks off, addled. Christian ACCELERATES to follow Josh.
  EXPRESSION: null

::PATHS::
- CHOICE: "Follow Josh"
  TARGET: woods
  STATE_CHANGE: null
  CONDITION: null
- CHOICE: "Follow Dani"
  TARGET: woods_2
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: EXT. WOODS - MOMENTS LATER
MOOD: Panic, Despair
CHARACTERS: Narrator, Dani
BACKGROUND_IMAGE: woods.png
BACKGROUND_EDIT: "Daytime, Dani sprinting into woods, then stopping at a tree"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Dani’s walk speeds into a SPRINT. Once out of sight, she stops at a tree, now HYPERVENTILATING. She tries to steady her breath, but it’s too erratic. She breaks down into violent SOBS. These are interrupted by a shrill RETCH.
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue into woods"
  TARGET: main_house
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: INT. THE MAIN HOUSE - SAME TIME
MOOD: Anxious, Tense
CHARACTERS: Narrator, Josh, Christian
BACKGROUND_IMAGE: main_house_interior.png
BACKGROUND_EDIT: "Daytime interior, Josh with laptop, Christian entering"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Josh anxiously goes through his backpack to find his LAPTOP. He sits on the mattress as the computer boots up. Christian enters awkwardly - eyes on Josh. He appears to be summoning the courage to say something.
  EXPRESSION: null
- CHARACTER: Christian
  LINE: Hey dude...
  EXPRESSION: Hesitant
- CHARACTER: Josh
  LINE: Hey! Holy fuck, right?
  EXPRESSION: Excited
- CHARACTER: Christian
  LINE: Holy fuck. Incredible.
  EXPRESSION: Awestruck
- CHARACTER: Josh
  LINE: Incredible!
  EXPRESSION: Awestruck
- CHARACTER: Narrator
  LINE: Christian works up the nerve:
  EXPRESSION: null
- CHARACTER: Christian
  LINE: So listen: I’ve been wanting to ask you, or tell you, or just - mention to you something I’ve been thinking about...
  EXPRESSION: Nervous
- CHARACTER: Narrator
  LINE: Josh looks up. He DARKENS with concern.
  EXPRESSION: null
- CHARACTER: Christian
  LINE: I’ve just been thinking, and I’ve decided...I really think I wanna do my thesis here. On the Hårgas.
  EXPRESSION: Determined
- CHARACTER: Narrator
  LINE: Josh doesn’t react. Christian nervously continues:
  EXPRESSION: null
- CHARACTER: Christian
  LINE: And I wanted to tell you first, so that it didn’t seem like I wasn’t telling you.
  EXPRESSION: Anxious
- CHARACTER: Josh
  LINE: I feel like I can’t tell if you’re joking.
  EXPRESSION: Suspicious
- CHARACTER: Narrator
  LINE: Christian doesn’t respond. Josh becomes incredulous.
  EXPRESSION: null
- CHARACTER: Josh
  LINE: Oh my God. I honestly can’t even... You know I’m out here doing my thesis, on midsummer. That’s why I’m here.
  EXPRESSION: Incredulous
- CHARACTER: Christian
  LINE: Yeah, but not on this community.
  EXPRESSION: Defensive
- CHARACTER: Narrator
  LINE: Josh’s eyes BURN on Christian.
  EXPRESSION: null
- CHARACTER: Christian
  LINE: What?
  EXPRESSION: Confused
- CHARACTER: Josh
  LINE: ...You knew I was gonna want to do this.
  EXPRESSION: Accusatory
- CHARACTER: Christian
  LINE: How would I know that? Did you even know that before I just told you?
  EXPRESSION: Deflecting
- CHARACTER: Josh
  LINE: Oh my God, Christian, of course you did!
  EXPRESSION: Certain
- CHARACTER: Josh
  LINE: You think I don’t know what you’re doing? It’s actually kind of outrageously unsubtle. The fact that you’re being this bald about it. It’s impressive. It is. I’m honestly impressed.
  EXPRESSION: Sarcastic
- CHARACTER: Christian
  LINE: What the fuck?
  EXPRESSION: Shocked
- CHARACTER: Josh
  LINE: Oh, yeah - “What the fuck.” This is what I’ve been working towards and you know it. That’s why you looked so guilty when you brought it up. Because you know - you know - that what you’re doing is unethical and leechy and lazy and frankly kind of sad--
  EXPRESSION: Furious
- CHARACTER: Christian
  LINE: Okay, wow, fuck you--
  EXPRESSION: Angry
- CHARACTER: Josh
  LINE: No dude, not fuck me! Find your own subject - or your own passion. Because I’m actually invested in this. It’s not some glorified hobby that I’m casually dipping my feet into.
  EXPRESSION: Angry
- CHARACTER: Christian
  LINE: Oh my God! You are so arrogant! In case you forgot, we’re both earning the same degree--
  EXPRESSION: Angry
- CHARACTER: Josh
  LINE: But we’re not doing it in the same way, Christian. Okay? I have to hold your hand through everything. You didn’t even know how to use J-Stor before I taught you, and you’re a fucking grad student. I mean, why are you even in academia? You don’t care! Which is fine! That’s your prerogative! Just don’t appropriate my actual work for your new shortcut!
  EXPRESSION: Incensed
- CHARACTER: Narrator
  LINE: This cuts Christian like a knife. His eyes are flaring with RAGE. But he stifles it. Determined to remain collected, he concludes:
  EXPRESSION: null
- CHARACTER: Christian
  LINE: I wanna do my thesis here. If you want to as well, I’d be happy to discuss collaborating. If not, I guess we’ll have two separate theses on the Hårgas.
  EXPRESSION: Cold
- CHARACTER: Narrator
  LINE: Christian leaves.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Josh sits motionless.
  EXPRESSION: null

::PATHS::
- CHOICE: "Leave the house"
  TARGET: farmstead
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: EXT. FARMSTEAD - CONTINUOUS
MOOD: Tense, Observant
CHARACTERS: Narrator, Christian, Simon, Maja, Ulla
BACKGROUND_IMAGE: farmstead.png
BACKGROUND_EDIT: "Daytime, Christian emerging from house, Simon smoking"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Christian emerges from the Main House, extremely tense. A very pale SIMON smokes a joint near the door, looking very ill. He notices Christian’s demeanor.
  EXPRESSION: null
- CHARACTER: Simon
  LINE: You traumatized too, mate?
  EXPRESSION: Weak
- CHARACTER: Christian
  LINE: What? Oh. Yeah...
  EXPRESSION: Agitated
- CHARACTER: Simon
  LINE: You want some? It’s laced with hydrocodone.
  EXPRESSION: Tired
- CHARACTER: Narrator
  LINE: Christian notices in the FIELD: a group of WOMEN collecting Linum usitatissimum (FLAX), which is in abundance. Among thme he sees MAJA, working with her friend ULLA (28). They laugh as they work.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Christian gestures “excuse me” to Simon, and approaches Maja.
  EXPRESSION: null
- CHARACTER: Christian
  LINE: Hey. Hi. Sorry to bother you...
  EXPRESSION: Polite
- CHARACTER: Narrator
  LINE: Maja looks up - not understanding. She looks almost panicked.
  EXPRESSION: null
- CHARACTER: Christian
  LINE: I’m Christian.
  EXPRESSION: Introducing
- CHARACTER: Narrator
  LINE: Ulla insert herself:
  EXPRESSION: null
- CHARACTER: Ulla
  LINE: Hello. I am Ulla. She is Maja.
  EXPRESSION: Friendly
- CHARACTER: Christian
  LINE: Hi Ulla. Maja. I was wondering if I could ask, uh - - how many of those Attestupans you guys have seen performed.
  EXPRESSION: Inquisitive
- CHARACTER: Ulla
  LINE: Every time one reaches age.
  EXPRESSION: Matter-of-fact
- CHARACTER: Christian
  LINE: Okay...
  EXPRESSION: Processing
- CHARACTER: Ulla
  LINE: So lots.
  EXPRESSION: Confident
- CHARACTER: Christian
  LINE: Right. Okay. And you don’t have like, a typical mourning period? For grieving?
  EXPRESSION: Curious
- CHARACTER: Ulla
  LINE: We grieve and celebrate.
  EXPRESSION: Balanced
- CHARACTER: Narrator
  LINE: Maja has been staring at Christian, love-stricken. He is aware of it, but tries to ignore.
  EXPRESSION: null
- CHARACTER: Ulla
  LINE: We must go now and keep working.
  EXPRESSION: Urgent
- CHARACTER: Christian
  LINE: Okay. No problem. Thank you. I might find you to ask more later?
  EXPRESSION: Hopeful
- CHARACTER: Narrator
  LINE: Ulla smiles “okay” and walks off with Maja. They wave goodbye.
  EXPRESSION: null
- CHARACTER: Christian
  LINE: Goodbye. ‘Bye Maja.
  EXPRESSION: Waving
- CHARACTER: Narrator
  LINE: Maja smiles timidly and waves again.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: In the b.g., Josh stands at the Main House’s door, STARING.
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue observing"
  TARGET: meadow
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: EXT. MEADOW - EVENING
MOOD: Calm, Attempting Peace
CHARACTERS: Narrator, Dani, Christian, Dagny, Connie
BACKGROUND_IMAGE: meadow.png
BACKGROUND_EDIT: "Evening, Dani meditating by a river"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Dani sits cross-legged near the river. Her eyes are closed. She’s trying to meditate, but her breathing is still unstable.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Christian appears behind her.
  EXPRESSION: null
- CHARACTER: Christian
  LINE: Hey.
  EXPRESSION: Gentle
- CHARACTER: Narrator
  LINE: Dani’s eyes open with a start. She turns to him.
  EXPRESSION: null
- CHARACTER: Christian
  LINE: How we doing?
  EXPRESSION: Caring
- CHARACTER: Dani
  LINE: I can’t stop fucking shaking and my teeth keep chattering.
  EXPRESSION: Distressed
- CHARACTER: Christian
  LINE: I can imagine. Today was a lot.
  EXPRESSION: Understanding
- CHARACTER: Dani
  LINE: I feel like the neck on my skin is getting tighter. Like I’m choking.
  EXPRESSION: Panicked
- CHARACTER: Narrator
  LINE: Dani pulls at her neck. Christian puts a hand on her shoulder.
  EXPRESSION: null
- CHARACTER: Christian
  LINE: You okay, baby?
  EXPRESSION: Reassuring
- CHARACTER: Narrator
  LINE: Dani looks up at him.
  EXPRESSION: null
- CHARACTER: Dani
  LINE: Are you just not at all disturbed by what happened?
  EXPRESSION: Searching
- CHARACTER: Christian
  LINE: I mean, of course, it was shocking. But I’m also trying to keep an open mind.
  EXPRESSION: Neutral
- CHARACTER: Narrator
  LINE: Dani just stares at him.
  EXPRESSION: null
- CHARACTER: Christian
  LINE: It’s - cultural. We put our elderly in nursing homes. I’m sure they find that disturbing.
  EXPRESSION: Explaining
- CHARACTER: Narrator
  LINE: Dani EYES him, disturbed by his nonchalance. She then sees... In the b.g., a congregation of WOMEN are migrating off together.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: DAGNY, whom we met earlier, splits from the group to RUN over to Dani and Christian.
  EXPRESSION: null
- CHARACTER: Dagny
  LINE: Dani! Do you like to join us?
  EXPRESSION: Inviting
- CHARACTER: Dani
  LINE: Why? What’s happening?
  EXPRESSION: Curious
- CHARACTER: Dagny
  LINE: A special ceremony - for the womans. The mans are joining for a - meditate. At the houses.
  EXPRESSION: Informative
- CHARACTER: Narrator
  LINE: Dani looks to Christian, fraught. He gives her a “go ahead” look.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Dani looks over to the flock of women and sees an equally unnerved CONNIE.
  EXPRESSION: null

::PATHS::
- CHOICE: "Join the ceremony"
  TARGET: river_ceremony
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: MOMENTS LATER
MOOD: Uneasy, Uncertain
CHARACTERS: Narrator, Dani, Connie
BACKGROUND_IMAGE: river_approach.png
BACKGROUND_EDIT: "Evening, Dani and Connie joining a group of women approaching a glowing river"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Dani uneasily joins Connie in the migrating crowd of women. They’re approaching a RIVER, which seems to GLOW in the distance.
  EXPRESSION: null
- CHARACTER: Dani
  LINE: Did they tell you what this is?
  EXPRESSION: Anxious
- CHARACTER: Connie
  LINE: Someone better not be jumping off another fucking cliff.
  EXPRESSION: Fearful
- CHARACTER: Narrator
  LINE: Dani pulls again at her neck - still feeling claustrophobic in her own skin.
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue towards the river"
  TARGET: field_meditation
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: EXT. FIELD - MOMENTS LATER
MOOD: Meditative, Focused
CHARACTERS: Narrator, Christian, Mark, Pretty Brunette
BACKGROUND_IMAGE: field_meditation.png
BACKGROUND_EDIT: "Evening, men in a circle for meditation, tree decoration outside"

::SCRIPT::
- CHARACTER: Narrator
  LINE: All the men are seated in a mass circle for a GROUP MEDITATION (which hasn’t yet begun). Isolated in the center of the circle is an Elder. He is the MEDITATION LEADER. (Outside the circle, a GROUP OF MEN decorate a TREE that has been pulled from the earth. They adorn it in various FLOWERS and HANDMADE ORNAMENTS.)
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Christian joins Mark in the circle.
  EXPRESSION: null
- CHARACTER: Christian
  LINE: Nice nap?
  EXPRESSION: Teasing
- CHARACTER: Narrator
  LINE: Mark, eyes elsewhere, leans over to WHISPER:
  EXPRESSION: null
- CHARACTER: Mark
  LINE: That girl over there keeps chatting me up, but she speaks like zero English.
  EXPRESSION: Frustrated
- CHARACTER: Narrator
  LINE: Mark is pointing to the PRETTY BRUNETTE from earlier.
  EXPRESSION: null
- CHARACTER: Christian
  LINE: Oh yeah. She’s cute.
  EXPRESSION: Agreeing
- CHARACTER: Mark
  LINE: Right? She keeps eyeing me.
  EXPRESSION: Hopeful
- CHARACTER: Narrator
  LINE: Christian pauses, and then:
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue conversation"
  TARGET: end_scene
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Water Well
MOOD: Intrigue
CHARACTERS: Christian, Pelle, Josh
BACKGROUND_IMAGE: water_well.png
BACKGROUND_EDIT: "Same time, Pelle drawing water, Josh appearing"

::SCRIPT::
- CHARACTER: Christian
  LINE: Don’t you kinda hate Josh?
  EXPRESSION: Teasing
- CHARACTER: Josh
  LINE: Hey. Can I talk to you?
  EXPRESSION: Earnest
- CHARACTER: Pelle
  LINE: Sure. But we’re being called for the meditation--
  EXPRESSION: Polite
- CHARACTER: Josh
  LINE: Has Christian come to you yet?
  EXPRESSION: Searching
- CHARACTER: Pelle
  LINE: ...About what?
  EXPRESSION: Confused
- CHARACTER: Josh
  LINE: Okay - so listen: And you can obviously say “no,” but point-blank: I wanna do my thesis here. On this.
  EXPRESSION: Direct
- CHARACTER: Pelle
  LINE: Oh which? The nine-day feast?
  EXPRESSION: Inquiring
- CHARACTER: Josh
  LINE: Or - yes, but no: On you guys. On the Hårgas. And I told Christian this already, and now I think he’s trying to pretend that it was his idea, so if he comes to you--
  EXPRESSION: Explaining
- CHARACTER: Pelle
  LINE: Okay, well... Well, no, hey, wait a minute: I seriously doubt the elders will approve of anything being written. They’re extremely protective.
  EXPRESSION: Doubtful
- CHARACTER: Josh
  LINE: Yeah, of course, and I wouldn’t do anything without their approval or permission.
  EXPRESSION: Reassuring
- CHARACTER: Pelle
  LINE: Yeah, but - they won’t approve, Josh. The only reason we’ve survived at all is because we operate in total isolation.
  EXPRESSION: Firm
- CHARACTER: Josh
  LINE: Right: So I can just use aliases for everything!
  EXPRESSION: Suggestive
- CHARACTER: Pelle
  LINE: Then what would be the point? You couldn’t even get it peer reviewed! Christian did already ask me this, by the way. I told him the exact same thing I’m telling you.
  EXPRESSION: Exasperated
- CHARACTER: Josh
  LINE: ...I thought you just said he hadn’t talked to you.
  EXPRESSION: Accusatory
- CHARACTER: Pelle
  LINE: Fuck, look: I’ll ask the elders. Okay? But if it’s approved, you either both do it together or you fight it out between yourselves.
  EXPRESSION: Annoyed
::STAGE DIRECTION::
Pelle puts his hands up to signify “That’s it.” He walks off toward the MEDITATION CIRCLE.

::SCENE::
LOCATION: Field
MOOD: Suspenseful
CHARACTERS: Pelle, Josh, Christian, Meditation Leader, Mark
BACKGROUND_IMAGE: field.png
BACKGROUND_EDIT: "Moments later, Pelle whispering to an Elder, Josh watching, Christian paranoid"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Pelle walks to an Elder near the back of the circle. He WHISPERS in his ear. As this happens, Josh hovers in the distance. He WATCHES Pelle’s interaction, in suspense. Christian, still sitting in the circle, SEES Josh staring at Pelle. Christian becomes instantly PARANOID. He RISES.
  EXPRESSION: null
- CHARACTER: Christian
  LINE: I’m gonna - take a leak.
  EXPRESSION: Evasive
- CHARACTER: Narrator
  LINE: Christian walks off towards a wall of BUSHES. Josh sees this, hesitates, and then warily FOLLOWS. He keeps a healthy distance. (Pelle’s EYES are now on both of them.)
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Once Christian is hidden by foliage, he sneakily RUNS off. He pursues the crowd of women, who are off in the distance.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: MEANWHILE, Mark looks helpless in the meditation circle.
  EXPRESSION: null
- CHARACTER: Meditation Leader
  LINE: (in Swedish) We begin now. Close your eyes.
  EXPRESSION: Authoritative

::SCENE::
LOCATION: River
MOOD: Mystical
CHARACTERS: Women, Siv, Dani, Connie, Elders, Nude Women
BACKGROUND_IMAGE: river.png
BACKGROUND_EDIT: "Same time, hundreds of lanterns, nine burning torches in the river"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The women arrive at the river. Hundreds of LANTERNS have been set up around the water to resemble a FIERY NECKLACE. In the river’s center, NINE BURNING TORCHES protrude from a BUOY atop the water.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The women have stopped at a spot near the river. Everyone stands seriously about. Siv walks up to a mystified Dani and Connie.
  EXPRESSION: null
- CHARACTER: Siv
  LINE: Do you admire the Brísingamen?
  EXPRESSION: Inquisitive
- CHARACTER: Connie
  LINE: The lanterns?
  EXPRESSION: Confused
- CHARACTER: Siv
  LINE: Glädje’s necklace made by the fairies. We give it now to her mother, Kärlek, as praise for creating our sun.
  EXPRESSION: Explanatory
- CHARACTER: Narrator
  LINE: Dani and Connie don’t understand, nor do they inquire further.
  EXPRESSION: null
- CHARACTER: Siv
  LINE: Think of it like theatre. Strictly presentational. Yes?
  EXPRESSION: Playful
- CHARACTER: Narrator
  LINE: Dani placates her by nodding. Siv smiles and directs their attention to the CENTER of the congregation.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: One of the female elders - a LARGE WOMAN (60s) with sturdy legs - holds the sacred book Rubi Radr. She takes a moment as everyone quiets down. She then reads a passage (in Swedish) out loud. She reads with clarity and authority. After she has finished...
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: A GROUP OF NINE WOMEN (three in their 20s, three in their 30s/ 40s, and three in their 50s/60s) all DISROBE. They are now NUDE.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: A woman begins playing the KEY-HARP. After the tune is established, three women begin to SING. It is a WORDLESS choral song - comprised only of expressive/abstract sounds that evoke a range of feelings and tell a strictly emotional story.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: As this is sung, the nude women walk to the RIVER. They descend into the water and swim towards the center. The song continues.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The nude women arrive at the burning buoy. They wait for the song to reach a bridge, and then they each draw a FLAMING TORCH from the buoy. Holding up their torches, the nude women now step carefully onto what must be underwater planks. They are still up to their necks in water. As the song crescendos, they slowly walk up the planks (each of which move in separate directions) to emerge from the water.
  EXPRESSION: null
- CHARACTER: Siv
  LINE: The women represents the sun. The sea gave birth to the sun, so they’re like - (gestures “rising up”) - from the womb.
  EXPRESSION: Explanatory
- CHARACTER: Narrator
  LINE: Dani and Connie watch. It is hypnotic.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Christian, having just caught up, WATCHES this ritual from behind a tree. Josh, a good distance behind Christian, also watches. Transfixed.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The women all arrive onto the shore at the same time. They rest their torches, and the song comes to an end.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Siv looks to a young RED-HAIRED WOMAN (30s), who runs off to now fetch the men.
  EXPRESSION: null

::SCENE::
LOCATION: Farmstead
MOOD: Transition
CHARACTERS: Red-Haired Woman, Odd, Men, Meditation Leader
BACKGROUND_IMAGE: farmstead.png
BACKGROUND_EDIT: "Moments later, Red-Haired Woman giving signal, men handling decorated tree, bell struck"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The Red-Haired Woman gives a signal to ODD. Odd then gestures to the MEN handling the decorated tree. They all LIFT the tree, and one man strikes a BELL. This ROUSES the men from their meditation.
  EXPRESSION: null
- CHARACTER: Meditation Leader
  LINE: (in Swedish) Now we stop.
  EXPRESSION: Announcing
- CHARACTER: Odd
  LINE: Okay everyone! Let us form a procession. Following the tree.
  EXPRESSION: Directing
- CHARACTER: Narrator
  LINE: Everybody rises, still coming out of their collective trance. They queue up to follow the decorated tree.
  EXPRESSION: null

::SCENE::
LOCATION: River
MOOD: Ceremonial
CHARACTERS: Men, Women, Christian, Josh, Large Woman, Thin Man, Young Boy (Ame), Hårgan #1, Hårgan #2
BACKGROUND_IMAGE: river.png
BACKGROUND_EDIT: "Moments later, men carrying tree arrive, women dressed, Christian and Josh join"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The men carrying the tree ARRIVE at the river, joining the women. The nude women are now dressed. Christian awkwardly joins the crowd. As does Josh.
  EXPRESSION: null
- CHARACTER: Large Woman
  LINE: (in Swedish) In thanks and praise, Great Goddess, we bestow upon you this modest gift.
  EXPRESSION: Solemn
- CHARACTER: Narrator
  LINE: Music is played as the men HOIST up the lavish tree, run it towards the river, and HURL it into the water. The river gulps the tree down.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: A horn bellows.
  EXPRESSION: null
- CHARACTER: Thin Man
  LINE: (in Swedish) Oh no! Did you hear that rumbling? I think she is still hungry.
  EXPRESSION: Theatrical
- CHARACTER: Large Woman
  LINE: (in Swedish) I heard no rumbling. Did any of you?
  EXPRESSION: Inquiring
- CHARACTER: Narrator
  LINE: Grumbling all around. The consensus is “no.”
  EXPRESSION: null
- CHARACTER: Thin Man
  LINE: (in Swedish) Ah, well - I suppose it could have been my own belly.
  EXPRESSION: Humorous
- CHARACTER: Narrator
  LINE: Some polite laughter among the congregation.
  EXPRESSION: null
- CHARACTER: Thin Man
  LINE: (in Swedish) But I do not wish to risk offending our generous Mother.
  EXPRESSION: Respectful
- CHARACTER: Large Woman
  LINE: (in Swedish) Nor do I. Yet we have already given our finest jewels and most fruitful tree. What else could we possibly offer?
  EXPRESSION: Pondering
- CHARACTER: Young Boy (O.S.)
  LINE: You can use me!
  EXPRESSION: Eager
- CHARACTER: Narrator
  LINE: The crowd OPENS UP to reveal the young boy. He is adorned in the same jewels and flowers as the tree. His costume is an imitation of the tree’s. He is clearly reciting lines (with less confidence than the Thin Man and Large Woman).
  EXPRESSION: null
- CHARACTER: Large Woman
  LINE: (in Swedish) You, young Ame, wish to offer your life to our beloved Goddess?
  EXPRESSION: Solemn
- CHARACTER: Young Boy
  LINE: (in Swedish) If She will have it.
  EXPRESSION: Resolute
- CHARACTER: Thin Man
  LINE: (in Swedish) How brave you are, little Ame!
  EXPRESSION: Admiring
- CHARACTER: Young Boy
  LINE: (in Swedish) Brave? What is brave in going home?
  EXPRESSION: Philosophical
- CHARACTER: Narrator
  LINE: Horns are played as the Young Boy steps forward to stand before the men who tossed the tree. They reluctantly lift the boy up and carry him to the river.
  EXPRESSION: null
- CHARACTER: Dani
  LINE: No. What’s happening?
  EXPRESSION: Panicked
- CHARACTER: Siv
  LINE: Smiles.
  EXPRESSION: Serene
- CHARACTER: Narrator
  LINE: The boy is taken to the edge of the river, and the men begin to SWING him back and forth. They are preparing to launch him into the water.
  EXPRESSION: null
- CHARACTER: Dani
  LINE: NO!!!
  EXPRESSION: Desperate
- CHARACTER: HÅRGAN #1
  LINE: (in Swedish) No! Don’t!
  EXPRESSION: Protesting
- CHARACTER: HÅRGAN #2
  LINE: (in Swedish) Leave him be! He has shown his bravery!
  EXPRESSION: Demanding
- CHARACTER: Narrator
  LINE: The crowd erupts into a CACOPHONY OF STAGED PROTEST. The men stop swinging the boy. After sufficient heckling, the men RELEASE the boy. He then runs to SIV, bashfully burying his face into her dress. She pats his head with pride.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Everyone APPLAUDS. The performance seems to be over. Dani looks completely disoriented.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Connie, who has now been joined by Simon, turns to Siv.
  EXPRESSION: null
- CHARACTER: Connie
  LINE: So, is this like a Wiccan thing?
  EXPRESSION: Inquisitive
- CHARACTER: Siv
  LINE: Wicca? Oh my dear no! This is about reciprocity.
  EXPRESSION: Confused, then Explaining
- CHARACTER: Connie
  LINE: Okay...
  EXPRESSION: Skeptical
- CHARACTER: Siv
  LINE: Strictly presentational.
  EXPRESSION: Reassuring
- CHARACTER: Narrator
  LINE: Connie looks skeptical. Dani still looks crazed. She turns to find CHRISTIAN, who (in contrast) looks very amused.
  EXPRESSION: null

::SCENE::
LOCATION: Field
MOOD: Confrontational
CHARACTERS: Dani, Christian, Hårgas' Water Power Plant
BACKGROUND_IMAGE: field.png
BACKGROUND_EDIT: "Minutes later, Dani and Christian in a secluded spot, water plant visible"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Dani has pulled Christian to a secluded spot. She is very high-strung. In the b.g., the Hårgas’ WATER POWER PLANT is visible.
  EXPRESSION: null
- CHARACTER: Dani
  LINE: Please Christian - we need to leave. This is feeling really wrong.
  EXPRESSION: Urgent
- CHARACTER: Christian
  LINE: Okay: look: I know it’s weird. That’s because it’s alien. We haven’t ever been exposed to anything like this.
  EXPRESSION: Defensive
- CHARACTER: Dani
  LINE: No, Christian: this is pagan nature worship. This is completely backwards. We shouldn’t be here.
  EXPRESSION: Repulsed
- CHARACTER: Christian
  LINE: We just need to acclimate--
  EXPRESSION: Persuasive
- CHARACTER: Dani
  LINE: I don’t want to acclimate! I want to leave.
  EXPRESSION: Insistent
- CHARACTER: Christian
  LINE: Baby, I cannot leave right now. Period. I’m doing my thesis on these guys--
  EXPRESSION: Frustrated
- CHARACTER: Dani
  LINE: What? Since when?!
  EXPRESSION: Surprised
- CHARACTER: Christian
  LINE: Since I decided! Today. Which you know has been a nightmare for me to figure out. And I made the mistake of telling Josh and now he’s competing with me--
  EXPRESSION: Resentful
- CHARACTER: Dani
  LINE: So let him have it if he wants it! We shouldn’t be here, Christian. But why have they invited us? And why did Pelle?!
  EXPRESSION: Confused and Angry
- CHARACTER: Christian
  LINE: No, hey - have you even seen what’s happening here?! This level of tradition? And nobody knows about it, nobody’s written on it - and they’ve invited us to be part of it! Can’t you see what a privilege that is?! Because Pelle did!
  EXPRESSION: Enthusiastic and Defensive

::SCENE::
LOCATION: Main House - Interior
MOOD: Tense
CHARACTERS: Dani, Christian
BACKGROUND_IMAGE: main_house_interior.png
BACKGROUND_EDIT: "Nighttime, dimly lit room"

::SCRIPT::
- CHARACTER: Dani
  LINE: Because he trusts us!
  EXPRESSION: null
- CHARACTER: Dani
  LINE: And why would he trust you, of all people? You’re opportunistic anthropology students.
  EXPRESSION: null
- CHARACTER: Christian
  LINE: Not necessarily.
  EXPRESSION: stubborn
- CHARACTER: Narrator
  LINE: Dani hesitates, seeing that she’s getting nowhere.
  EXPRESSION: null
- CHARACTER: Dani
  LINE: I want to leave.
  EXPRESSION: null
- CHARACTER: Christian
  LINE: Then you can leave. I invited you to come, and I don’t regret that, but I’m here for a reason.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Beat. Christian’s eyes are ice cold.
  EXPRESSION: null
- CHARACTER: Dani
  LINE: ...Do you not love me anymore?
  EXPRESSION: null
- CHARACTER: Christian
  LINE: What does that have to do with this?
  EXPRESSION: momentarily stunned
- CHARACTER: Dani
  LINE: This is the devaluation phase. We've been in it for a long time now. Next comes the discard.
  EXPRESSION: almost to herself
- CHARACTER: Christian
  LINE: Oh fuck - can you maybe spare our relationship the psychology 101?
  EXPRESSION: null
- CHARACTER: Dani
  LINE: No - this has been happening for a long time! You’ve been pulling away... And I've been in denial.
  EXPRESSION: null
- CHARACTER: Christian
  LINE: Oh, please babe - give yourself some credit. Looks to me like you've got it all figured out.
  EXPRESSION: finished
- CHARACTER: Narrator
  LINE: Christian turns and storms away.
  EXPRESSION: null
- CHARACTER: Dani
  LINE: Oh my -- you’re gonna walk away now??
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: As he leaves, she cries out:
  EXPRESSION: null
- CHARACTER: Dani
  LINE: You’re just gonna leave me like this?!
  EXPRESSION: null

::PATHS::
- CHOICE: "Christian continues to leave"
  TARGET: main_house_night_59
  STATE_CHANGE: relationship_tension = +5
  CONDITION: null

::SCENE::
LOCATION: The Main House - Night
MOOD: Somber
CHARACTERS: Narrator, Dani, Christian, Josh
BACKGROUND_IMAGE: main_house_night.png
BACKGROUND_EDIT: "Nighttime, people boarding up windows, darkening the house"

::SCRIPT::
- CHARACTER: Narrator
  LINE: People are laying boards over the windows, bringing the Main House into darkness.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Dani enters with sunken eyes. Christian’s already in bed. Staring at him, Dani walks to Josh. (She is pulling at her neck again.)
  EXPRESSION: null
- CHARACTER: Dani
  LINE: Do you have a sleeping pill?
  EXPRESSION: null
- CHARACTER: Josh
  LINE: Sure. Uh...
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Josh fishes a pill out of his bag.
  EXPRESSION: null
- CHARACTER: Josh
  LINE: They’re intense, though. You might wanna cut it in half.
  EXPRESSION: null
- CHARACTER: Dani
  LINE: I just need to sleep.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: She swallows it whole.
  EXPRESSION: null

::PATHS::
- CHOICE: "Dani falls asleep"
  TARGET: main_house_night_60
  STATE_CHANGE: sleep_medication = true
  CONDITION: null

::SCENE::
LOCATION: The Main House - Night
MOOD: Eerie
CHARACTERS: Narrator, Dani, Christian, Mark, Josh, Pelle
BACKGROUND_IMAGE: main_house_night_60.png
BACKGROUND_EDIT: "Nighttime, everyone asleep, dark room"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Silence. Everyone is asleep, including Dani.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: There is rustling heard off-screen. Dani wakes. She sits up to see...
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Christian’s bed is now empty. So is Mark’s bed. And Josh’s. Concerned, Dani looks to the door. Mark, Josh, Pelle and Christian are quietly tip-toeing out of the house. They giggle. Christian is the last to exit.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Confused, Dani climbs out of bed. She rushes to the door.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Dani looks outside to see that the group is now inside the rental minivan, which is idling off. Pelle drives, laughing. Christian, in the back seat, looks out the back window. He smiles giddily at Dani as they drive away.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Dani watches this in utter horror.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The diminishing car’s tailpipe belches thick black smoke.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Dani opens her mouth in anguish. An impossible amount of black smoke (the same color as that from the tailpipe) escapes her lungs, filling the frame, and then--
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: We slam to a harsh insert of the gored face of the second Elder who jumped off the cliff. He gasps wretchedly.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: We then punch out, wider, to reveal that the dashed bodies on the rocks are Dani’s parents and her sister. We then cut to:
  EXPRESSION: null

::PATHS::
- CHOICE: "Wake up from nightmare"
  TARGET: main_house_night_61
  STATE_CHANGE: nightmare_level = 1
  CONDITION: null

::SCENE::
LOCATION: The Main House - Night
MOOD: Anxious
CHARACTERS: Narrator, Dani, Maja, Christian, Josh
BACKGROUND_IMAGE: main_house_night_61.png
BACKGROUND_EDIT: "Nighttime, Dani asleep, Maja awake and watchful"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Dani is asleep in bed. The last scene was a dream. Her eyelids twitch as she continues to suffer the nightmare.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: We pan away from Dani to reveal that Maja, several beds over, is awake. She anxiously fingers a freshly carved rune stone. Her eyes are glued to Christian, who is fast asleep.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Maja climbs out of bed and tip-toes to Christian’s bed. She crouches to slide the rune stone under his mattress. She then runs nervously back to her bed.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Josh, whom we now reveal to be awake, has been watching this.
  EXPRESSION: null

::PATHS::
- CHOICE: "Morning comes"
  TARGET: main_house_morning_62
  STATE_CHANGE: paranoia = +1
  CONDITION: null

::SCENE::
LOCATION: The Main House - Morning
MOOD: Quiet
CHARACTERS: Narrator, Dani, Pelle, Josh, Mark, Christian
BACKGROUND_IMAGE: main_house_morning_62.png
BACKGROUND_EDIT: "Morning, beds are empty, sounds of activity outside"

::SCRIPT::
- CHARACTER: Narrator
  LINE: All of the beds are now empty, and morning activity is heard outside. Dani, however, is still asleep.
  EXPRESSION: null

::PATHS::
- CHOICE: "Go outside"
  TARGET: meadow_next_morning_63
  STATE_CHANGE: none
  CONDITION: null

::SCENE::
LOCATION: Meadow - Next Morning
MOOD: Hopeful
CHARACTERS: Narrator, Pelle, Josh, Mark, Christian, Hårgans
BACKGROUND_IMAGE: meadow_next_morning.png
BACKGROUND_EDIT: "Morning, Pelle planting vegetables, Josh and Mark approach"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Pelle plants vegetables in the garden.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Josh, accompanied by Mark, approaches Pelle. Watching this, Christian lingers in the b.g.
  EXPRESSION: null
- CHARACTER: Josh
  LINE: Hey man. Any word?
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Pelle looks up to see Josh. He sighs and rises.
  EXPRESSION: null
- CHARACTER: Pelle
  LINE: They said you can do it as long as you absolutely don’t use names and the location is never even hinted at. And they’re gonna have you sign an agreement to that.
  EXPRESSION: null
- CHARACTER: Josh
  LINE: Okay. Wow. Okay.
  EXPRESSION: nodding, excited
- CHARACTER: Narrator
  LINE: Josh can’t contain his glee.
  EXPRESSION: null
- CHARACTER: Pelle
  LINE: And you split it with Christian. Because he came to me first.
  EXPRESSION: null
- CHARACTER: Josh
  LINE: Well, that’s -- We’ll figure that out.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Mark notices in the distance: One man has climbed to the top of a tree to fetch a strange, flowering pinecone from the tip of a branch. At the base of the tree is a crowd of observing men.
  EXPRESSION: null
- CHARACTER: Mark
  LINE: What are they doing?
  EXPRESSION: null
- CHARACTER: Josh
  LINE: Gathering...charms.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The climbing man cuts the cone with a golden blade. The men cheer.
  EXPRESSION: null
- CHARACTER: Josh
  LINE: Here: can I ask you something?
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Josh pulls Maja’s rune stone out of his pocket.
  EXPRESSION: null
- CHARACTER: Josh
  LINE: I found this under Christian’s bed. Do you know what this is?
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Pelle looks over it.
  EXPRESSION: null
- CHARACTER: Pelle
  LINE: Love rune. It casts a love spell.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Christian walks over. Josh conceals the rune.
  EXPRESSION: null
- CHARACTER: Christian
  LINE: What’s going on?
  EXPRESSION: null
- CHARACTER: Pelle
  LINE: The elders said you can do your thesis as long as you don’t use actual names or location.
  EXPRESSION: null
- CHARACTER: Christian
  LINE: Holy shit. That’s incredible. Thank you so much.
  EXPRESSION: null
- CHARACTER: Pelle
  LINE: You’re splitting it with Josh.
  EXPRESSION: null
- CHARACTER: Christian
  LINE: I already told him that’s totally fine with me.
  EXPRESSION: as if Josh isn’t there
- CHARACTER: Narrator
  LINE: Pelle notices Christian glancing over at Maja.
  EXPRESSION: null
- CHARACTER: Pelle
  LINE: I think my sister Maja has taken a liking to you.
  EXPRESSION: null
- CHARACTER: Christian
  LINE: Yeah. I think I noticed.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: In the b.g., a cow and a lamb are being led across the field by different Hårgans.
  EXPRESSION: null
- CHARACTER: Pelle
  LINE: You know, she just got her byxmyndig.
  EXPRESSION: raising eyebrows
- CHARACTER: Christian
  LINE: Ha. What’s that?
  EXPRESSION: null
- CHARACTER: Pelle
  LINE: It means - “pants license”? When you turn fifteen, you’re allowed to have sex.
  EXPRESSION: smiling at the silly expression
- CHARACTER: Mark
  LINE: How ‘bout that one? Is she licensed?
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Mark is pointing out the brunette that he has a crush on.
  EXPRESSION: null
- CHARACTER: Pelle
  LINE: Inga? Oh yes.
  EXPRESSION: laughs
- CHARACTER: Narrator
  LINE: Pelle is summoned by a few men struggling to carry equipment. He goes off to help them.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: At the same time, Mark catches the brunette, Inga, looking at him again. He suddenly feels compelled to do something. He starts marching in the direction of the climbing men.
  EXPRESSION: null
- CHARACTER: Christian
  LINE: Mark?
  EXPRESSION: null

::PATHS::
- CHOICE: "Mark climbs the tree"
  TARGET: main_house_morning_64
  STATE_CHANGE: none
  CONDITION: null

::SCENE::
LOCATION: The Main House - Morning
MOOD: Groggy
CHARACTERS: Narrator, Dani
BACKGROUND_IMAGE: main_house_morning_64.png
BACKGROUND_EDIT: "Morning, Dani stirring awake in bed"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Dani stirs awake. Extremely groggy.
  EXPRESSION: null
- CHARACTER: Dani
  LINE: Christian?
  EXPRESSION: as if still dreaming
  

::PATHS::
- CHOICE: "Go to the farmstead"
  TARGET: farmstead_same_time_65
  STATE_CHANGE: none
  CONDITION: null

::SCENE::
LOCATION: Farmstead - Same Time
MOOD: Chaotic
CHARACTERS: Narrator, Mark, Christian, Josh, Bearded Man (Ulf), Pelle, Thin Elder, Hårgans
BACKGROUND_IMAGE: farmstead_same_time.png
BACKGROUND_EDIT: "Morning, Mark climbing an oak tree, Ulf approaching enraged"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Mark has arrived at an oak tree with a particularly large pinecone (also bearing a flower) at the top. Its base has been tied with rope. Mark begins to climb it.
  EXPRESSION: null
- CHARACTER: Christian
  LINE: Wait, dude. Maybe hold off.
  EXPRESSION: null
- CHARACTER: Mark
  LINE: I’m gonna “gather a charm.”
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Josh and Christian look uneasy as Mark quickly scales the oak. As he climbs past a few branches, a bearded man (40s) is heard off-screen:
  EXPRESSION: null
- CHARACTER: Bearded Man (O.S.)
  LINE: NEJ!!!
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Mark freezes. The Bearded Man runs over. This is Ulf.
  EXPRESSION: null
- CHARACTER: Ulf
  LINE: WHAT ARE YOU DOING?! GET OFF! GET DOWN!
  EXPRESSION: in Swedish
- CHARACTER: Narrator
  LINE: Mark, now standing motionless on a branch, looks stupefied. The branch suddenly snaps beneath his feet, and he comes tumbling to the ground. He lands hard on his ass.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Ulf desperately picks up the broken branch. He then notices that the tree’s mud-plugged cleft (wrapped in rope) has broken open.
  EXPRESSION: null
- CHARACTER: Ulf
  LINE: Oh no no no... What have you done?
  EXPRESSION: in Swedish
- CHARACTER: Narrator
  LINE: People have started gathering around. He appeals to them:
  EXPRESSION: null
- CHARACTER: Ulf
  LINE: Can we put it back on? Can we...?
  EXPRESSION: in Swedish
- CHARACTER: Mark
  LINE: What’s wrong? What did I do?
  EXPRESSION: null
- CHARACTER: Pelle
  LINE: What happened?
  EXPRESSION: null
- CHARACTER: Ulf
  LINE: Your American friend. He desecrated my tree.
  EXPRESSION: in Swedish, heartbroken
- CHARACTER: Pelle
  LINE: I’m so sorry, Father Ulf! He didn’t know.
  EXPRESSION: gasps, in Swedish
- CHARACTER: Mark
  LINE: What happened? What did I do?
  EXPRESSION: null
- CHARACTER: Pelle
  LINE: You climbed his tree.
  EXPRESSION: null
- CHARACTER: Mark
  LINE: His tree? So what? I’m sorry.
  EXPRESSION: null
- CHARACTER: Ulf
  LINE: “So what?!”
  EXPRESSION: suddenly enraged
- CHARACTER: Mark
  LINE: What?! I didn’t know!
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Ulf is clearly in a fury. He stifles it, but his eyes are frighteningly wide.
  EXPRESSION: null
- CHARACTER: Pelle
  LINE: Here, Mark: let’s just...
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Pelle leads Mark away.
  EXPRESSION: null
- CHARACTER: Mark
  LINE: What the fuck? How is it his tree? What’s even happening?
  EXPRESSION: null
- CHARACTER: Pelle
  LINE: That tree cured him of pneumonia when he was a baby.
  EXPRESSION: null
- CHARACTER: Mark
  LINE: What? How?! No it didn’t.
  EXPRESSION: null
- CHARACTER: Pelle
  LINE: He believes it did. And now his health and his life are tied to that tree. If it gets hurt, he gets hurt.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Mark looks over to Ulf, who has collapsed into tears. The Thin Elder speaks soothingly to him.
  EXPRESSION: null
- CHARACTER: Thin Elder
  LINE: We can reattach the branch. It’s a minor wound. Barely anything.
  EXPRESSION: in Swedish
- CHARACTER: Ulf
  LINE: What about the cleft?
  EXPRESSION: in Swedish
- CHARACTER: Mark
  LINE: Well - fuck. I am sorry. I still don’t understand what I did... Do I apologize?
  EXPRESSION: null
- CHARACTER: Pelle
  LINE: Apologize later.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The pretty brunette, Inga, has walked up.
  EXPRESSION: null
- CHARACTER: Mark
  LINE: Oh shit. Hi.
  EXPRESSION: null
- CHARACTER: Inga
  LINE: Tell him it’s okay. He didn’t know. I will talk to father Ulf.
  EXPRESSION: to Pelle, in Swedish
- CHARACTER: Narrator
  LINE: She smiles at Mark and walks off.
  EXPRESSION: null
- CHARACTER: Pelle
  LINE: She said to tell you it’s okay and that she’ll explain to him your mistake.
  EXPRESSION: explaining
- CHARACTER: Mark
  LINE: Seriously? What else did she say?
  EXPRESSION: overjoyed
- CHARACTER: Narrator
  LINE: Christian sees Dani in the distance, woozily looking for him. He walks over to her, affecting pleasantness.
  EXPRESSION: null
- CHARACTER: Christian
  LINE: Hey!
  EXPRESSION: null
- CHARACTER: Dani
  LINE: Oh!
  EXPRESSION: seeing him
- CHARACTER: Christian
  LINE: You get some good sleep?
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: They arrive at each other. He gives her a peck.
  EXPRESSION: null
- CHARACTER: Dani
  LINE: I’m sorry about last night.
  EXPRESSION: null
- CHARACTER: Christian
  LINE: ...How you feeling?
  EXPRESSION: null
- CHARACTER: Dani
  LINE: I don’t want us to be fighting, Christian.
  EXPRESSION: pause, emotional
- CHARACTER: Christian
  LINE: Well - me neither.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Christian looks like he wants to say more. Dani waits for it. Finally, Christian thinks better of it.
  EXPRESSION: null
- CHARACTER: Christian
  LINE: Are you feeling less nervous today?
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Dani pauses uncertainly at this.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Horns bellow in the b.g. A ceremony is beginning somewhere, and all the Hårgans are presently migrating over a hill. Pelle, standing at a distance, is waving Dani and Christian over.
  EXPRESSION: null

::PATHS::
- CHOICE: "Go to the ceremony"
  TARGET: hill_day_66
  STATE_CHANGE: none
  CONDITION: null

::SCENE::
LOCATION: Hill - Day
MOOD: Ritualistic
CHARACTERS: Narrator
BACKGROUND_IMAGE: hill_day.png
BACKGROUND_EDIT: "Daytime, top of a hill, animals being prepared"

::SCRIPT::
- CHARACTER: Narrator
  LINE: ECU of a baby bull’s hind legs, tied together with rope. The rope is pulled swiftly up.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: ECU of a lamb’s hind legs, also tied. The rope is yanked up.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: ECU of a baby horse’s hind legs, also tied. The rope pulls up.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: We now cut to a wide shot of the top of a hill. Nine animals (lamb, goat, dog, baby horse, baby bull,
  EXPRESSION: null

::PATHS::
- CHOICE: "Observe the ceremony"
  TARGET: end
  STATE_CHANGE: none
  CONDITION: null

::SCENE::
LOCATION: Hill
MOOD: Disturbing
CHARACTERS: Narrator, Dani, Pelle, Christian, Josh, Simon, Ingemar, Thin Elder, Red-Haired Woman, Nine Young Men
BACKGROUND_IMAGE: hill_ceremony.png
BACKGROUND_EDIT: "Dusk, a hill with animals hung upside down, community gathered below"

::SCRIPT::
- CHARACTER: Narrator
  LINE: A baby cow, pig, rabbit, and three tied-together chickens have been strung upside-down. They are all alive. Each of them is separated by about five feet.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The Thin Elder stands to the side of the line-up. On the other side is Siv. The entire community has congregated at the bottom of the hill. Dani looks very nervous. She turns to Pelle, who already looks concerned for her.
  EXPRESSION: null
- CHARACTER: Dani
  LINE: Do I want to stay for this?
  EXPRESSION: Nervous
- CHARACTER: Pelle
  LINE: ...Maybe you should not.
  EXPRESSION: Concerned
- CHARACTER: Narrator
  LINE: Dani looks to Christian. He looks very excited. She turns back to the top of the hill, anxious.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Siv speaks exultantly to the air (in Swedish). When she finishes, steady percussion begins. The Thin Elder strikes a different pose (physically and emotionally) with every percussive hit.
  EXPRESSION: null
- CHARACTER: Red-Haired Woman
  LINE: (WORDLESS CHORAL SONG)
  EXPRESSION: Singing
- CHARACTER: Narrator
  LINE: Nine young men, each holding a blade, walk up to the animals. Simultaneously, they all slit the animals’ throats. The animals thrash wildly as blood drains from their necks. (The song has degraded into anguished snarls and cries.)
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: That does it. Dani storms off. Christian is too awe-stricken to care. Josh, meanwhile, is taking covert photos with his phone.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Beneath each animal, a narrow channel has been pre-carved into the earth. Each channel winds and loops to eventually converge, thus forming a massive runic symbol (symbolizing fertility). The blood pours from each animal to run down the separate canals. Soon, the blood has co-mingled to fill the carefully-engineered runic sculpture. It’s horrible and beautiful.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Josh and Christian, briefly joined in their excitement, trade looks of amazement. Mark looks mystified.
  EXPRESSION: null
- CHARACTER: Mark
  LINE: This is fuckin’ weird, no?
  EXPRESSION: Bewildered
- CHARACTER: Narrator
  LINE: Pelle now goes after Dani, who is speed-walking away.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: In the b.g., Simon can be heard saying:
  EXPRESSION: null
- CHARACTER: Simon (O.S.)
  LINE: What the fuck did you bring us to?
  EXPRESSION: Scared
- CHARACTER: Narrator
  LINE: Christian looks over at this. Simon, who looks very scared, is confronting a grinning Ingemar.
  EXPRESSION: null
- CHARACTER: Simon
  LINE: Why are you smiling, mate?
  EXPRESSION: Aggressive
- CHARACTER: Ingemar
  LINE: (Grinning)
  EXPRESSION: Grinning

::PATHS::
- CHOICE: "Follow Dani"
  TARGET: field_same_time
  STATE_CHANGE: Dani_leaving = +1, Pelle_concerned = +1
  CONDITION: null
- CHOICE: "Observe the ceremony"
  TARGET: field_same_time
  STATE_CHANGE: Christian_awe = +1, Josh_curious = +1
  CONDITION: null

::SCENE::
LOCATION: Field - Same Time
MOOD: Urgent
CHARACTERS: Narrator, Dani, Pelle, Simon, Connie, Ingemar
BACKGROUND_IMAGE: field_escape.png
BACKGROUND_EDIT: "Dusk, Dani running towards the main house, Pelle following"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Dani speed-walks (with intermittent running) toward the Main House in the distance. Pelle follows her, glancing over his shoulder to view more of the ceremony.
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue to Main House"
  TARGET: main_house_minutes_later
  STATE_CHANGE: Dani_panic = +1
  CONDITION: null

::SCENE::
LOCATION: The Main House - Minutes Later
MOOD: Panicked
CHARACTERS: Narrator, Dani, Pelle
BACKGROUND_IMAGE: main_house_packing.png
BACKGROUND_EDIT: "Interior of a rustic house, Dani packing frantically"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Dani enters the Main House, eyes crazed. She goes to her bed and begins hastily packing her bag. Her breathing is erratic and she’s pulling at her neck again (as if to loosen the skin).
  EXPRESSION: Crazed
- CHARACTER: Pelle
  LINE: Dani?
  EXPRESSION: Concerned
- CHARACTER: Narrator
  LINE: Dani looks up, teeth chattering with anxiety.
  EXPRESSION: Anxious
- CHARACTER: Dani
  LINE: I’m really sorry, Pelle. Thank you for inviting me, but I really need to go. Can someone maybe drive me?
  EXPRESSION: Desperate
- CHARACTER: Pelle
  LINE: I did warn you this time. I know it looks extreme, but we only do this once every ninety years. It’s - what’s the word...?
  EXPRESSION: Calm
- CHARACTER: Dani
  LINE: I understand that it’s momentous.
  EXPRESSION: Resigned
- CHARACTER: Pelle
  LINE: Right! Exactly!
  EXPRESSION: Relieved
- CHARACTER: Dani
  LINE: I don’t know why we’re here, Pelle! I don’t know why you invited us!
  EXPRESSION: Frustrated
- CHARACTER: Pelle
  LINE: Okay: Here: Sit down. Please.
  EXPRESSION: Gentle
- CHARACTER: Narrator
  LINE: He sits Dani down. He plants himself beside her, taking her hands.
  EXPRESSION: null
- CHARACTER: Pelle
  LINE: I invited my friends because this is a once-in-a-lifetime thing and I wanted to share it. Especially with my friends who I knew would appreciate it, because I am proud of this place.
  EXPRESSION: Earnest
- CHARACTER: Dani
  LINE: But I’m not an anthropologist. I don’t have the foundation to understand this.
  EXPRESSION: Defensive
- CHARACTER: Pelle
  LINE: And yet I was the most excited for you to come.
  EXPRESSION: Sincere
- CHARACTER: Narrator
  LINE: Pelle has pulled a special pouch from his pocket. He draws something out.
  EXPRESSION: null
- CHARACTER: Pelle
  LINE: Here: smell this.
  EXPRESSION: Encouraging
- CHARACTER: Narrator
  LINE: He places a homemade sachet (containing a special herb) under her nose.
  EXPRESSION: null
- CHARACTER: Dani
  LINE: What is it?
  EXPRESSION: Curious
- CHARACTER: Pelle
  LINE: It calms you down.
  EXPRESSION: Reassuring
- CHARACTER: Narrator
  LINE: She pauses before smelling it.
  EXPRESSION: null
- CHARACTER: Pelle
  LINE: Go on. Inhale. I will, too.
  EXPRESSION: Demonstrative
- CHARACTER: Narrator
  LINE: Demonstrating, he inhales the herb deeply. He puts it back to her nose, and she does the same. She’s still trembling.
  EXPRESSION: null
- CHARACTER: Pelle
  LINE: Isn’t that nice?... I know what you’re going through, Dani.
  EXPRESSION: Empathetic
- CHARACTER: Dani
  LINE: What am I going through? I’m scared. I can’t breathe.
  EXPRESSION: Distressed
- CHARACTER: Pelle
  LINE: You’re going through a lot.
  EXPRESSION: Understanding
- CHARACTER: Pelle
  LINE: I know you are, and I’m gonna say something now, because my birth parents are both gone, too--
  EXPRESSION: Somber
- CHARACTER: Dani
  LINE: What?! (crying now) That’s not what I’m talking about!
  EXPRESSION: Upset
- CHARACTER: Pelle
  LINE: I know, and that’s fine, but please... My birth-parents both died when I was a little boy. They burned up in a fire, and I became - technically - an orphan. So believe me when I say I know what that is, because I do. Yet my difference is: I didn’t get a chance to feel lost. Because I had a family - here - where everyone embraced me and swept me up and I was raised by a community that doesn’t distinguish between what is theirs and what is not theirs. That’s what you were sacrificed to. But I - have always felt...held. By a family. A real family. Which everyone deserves. And you deserve.
  EXPRESSION: Emotional
- CHARACTER: Narrator
  LINE: Dani looks down at Pelle’s hands gripping hers.
  EXPRESSION: null
- CHARACTER: Dani
  LINE: Christian could walk in.
  EXPRESSION: Anxious
- CHARACTER: Pelle
  LINE: He’s what I’m talking about. And he’s my good friend and I like him... But do you feel held by him, Dani? Does he feel like a home to you?
  EXPRESSION: Intense
- CHARACTER: Narrator
  LINE: His eyes are locked intensely on Dani’s. She doesn’t turn away.
  EXPRESSION: null
- CHARACTER: Pelle
  LINE: My pilgrimage has been fun. New York is fun... But I also find it terrifying how people live. As if it’s necessary and even good to be lost and drifting...and I haven’t spent one night over there that I haven’t longed to be back here...in the lap of the Hårgas.
  EXPRESSION: Longing
- CHARACTER: Narrator
  LINE: Dani looks almost hypnotized as she looks into Pelle’s eyes.
  EXPRESSION: null
- CHARACTER: Pelle
  LINE: Stay, Dani. Please. It will be good... And I swear we’re all finished sacrificing animals.
  EXPRESSION: Pleading
- CHARACTER: Narrator
  LINE: Dani gives a weak half-laugh. She relents. She sits up straight and wipes her eyes, regaining composure.
  EXPRESSION: null
- CHARACTER: Pelle
  LINE: Good.
  EXPRESSION: Satisfied
- CHARACTER: Narrator
  LINE: Pelle stands up.
  EXPRESSION: null
- CHARACTER: Dani
  LINE: You’re a very empathic person, do you know that?
  EXPRESSION: Grateful
- CHARACTER: Pelle
  LINE: Well, our first language here is strictly emotion-based. So I could just be using that to manipulate you.
  EXPRESSION: Teasing
- CHARACTER: Narrator
  LINE: Dani pauses at this. Pelle sticks his tongue out, teasing.
  EXPRESSION: null
- CHARACTER: Pelle
  LINE: You are very vulnerable, though. And I mean that in a great way. It’s very rare. It’s beautiful.
  EXPRESSION: Admiring
- CHARACTER: Narrator
  LINE: Dani is touched, but tries to hide it.
  EXPRESSION: null
- CHARACTER: Dani
  LINE: Can I smell that again?
  EXPRESSION: Vulnerable

::PATHS::
- CHOICE: "Stay"
  TARGET: hill_same_time_2
  STATE_CHANGE: Dani_calm = +1, Dani_stays = true
  CONDITION: null
- CHOICE: "Leave"
  TARGET: hill_same_time_2
  STATE_CHANGE: Dani_leaves = true
  CONDITION: null

::SCENE::
LOCATION: Hill - Same Time
MOOD: Confrontational
CHARACTERS: Narrator, Simon, Connie, Ingemar, Plump Elder, Woman
BACKGROUND_IMAGE: hill_lunch_setup.png
BACKGROUND_EDIT: "Dusk, tables being set up for lunch, ceremony ending"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The ceremony has ended. Groups are now setting up tables for lunch. As usual, they’re being laid out in a particular pattern.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Simon and Connie stand frozen, traumatized. Simon is visibly distraught. He stares up at the top of the hill, where the dangling, blood-drained animals are now being cut down.
  EXPRESSION: Distraught
- CHARACTER: Simon
  LINE: Are we eating those animals?
  EXPRESSION: Horrified
- CHARACTER: Ingemar
  LINE: Not those ones.
  EXPRESSION: Matter-of-fact
- CHARACTER: Simon
  LINE: And why not?
  EXPRESSION: Aggressive
- CHARACTER: Ingemar
  LINE: ...Because they weren’t killed for that.
  EXPRESSION: Calm
- CHARACTER: Simon
  LINE: So what were they killed for? So we could watch that shit and clap?
  EXPRESSION: Enraged
- CHARACTER: Narrator
  LINE: Ingemar smiles. This infuriates Simon.
  EXPRESSION: null
- CHARACTER: Simon
  LINE: What the fuck is that smile, mate? Get it off.
  EXPRESSION: Furious
- CHARACTER: Connie
  LINE: Simon...
  EXPRESSION: Pleading
- CHARACTER: Narrator
  LINE: This has drawn attention. People are now looking over.
  EXPRESSION: null
- CHARACTER: Ingemar
  LINE: We can talk about this over here.
  EXPRESSION: Inviting
- CHARACTER: Simon
  LINE: Why didn’t we talk about it before you took us here?
  EXPRESSION: Accusatory
- CHARACTER: Narrator
  LINE: Ingemar gently touches Simon’s arm to lead him away.
  EXPRESSION: null
- CHARACTER: Simon
  LINE: Don’t sort me out, mate!
  EXPRESSION: Rebellious
- CHARACTER: Plump Elder
  LINE: What’s offending you, son?
  EXPRESSION: Inquisitive
- CHARACTER: Simon
  LINE: What’s offending me? Besides the fact I just saw something I can’t ever unsee, I’m offended that you’re teaching impressionable kids to sacrifice living, innocent animals - including a fucking defenseless dog--
  EXPRESSION: Outraged
- CHARACTER: Woman
  LINE: We sacrificed defenseless animals yesterday, too! To fill your belly!
  EXPRESSION: Defensive
- CHARACTER: Plump Elder
  LINE: Why are we using “sacrifice” like it’s a dirty word?
  EXPRESSION: Questioning
- CHARACTER: Simon
  LINE: Because it’s fucking medieval!
  EXPRESSION: Indignant
- CHARACTER: Woman
  LINE: Why are you swearing?! We’re not swearing!
  EXPRESSION: Scolding
- CHARACTER: Plump Elder
  LINE: You’ll find that sacrifice is essential in any relationship. Let’s put it in your terms--
  EXPRESSION: Authoritative
- CHARACTER: Simon
  LINE: You don’t know my terms!
  EXPRESSION: Defiant
- CHARACTER: Plump Elder
  LINE: Say you find yourself entangled with a lover who can’t put your needs before her own. Say you learn that your partner can’t part with even a fraction of his own comfort to give you what you need. And show that you’re appreciated. Wouldn’t you start to resent this person? Wouldn’t your own performance begin to lack, knowing they’re not pulling their weight? Wouldn’t you want to punish that person for taking you for granted? Sacrifice is proof. And without it, no union can last.
  EXPRESSION: Eloquent
- CHARACTER: Narrator
  LINE: Beat. Simon pops the bubble:
  EXPRESSION: null
- CHARACTER: Simon
  LINE: Alright. Thank you for that. And now we’ve seen two people kill themselves and nine animals get bled to death, so I think we’re leaving.
  EXPRESSION: Resolute
- CHARACTER: Plump Elder
  LINE: I’ll happily drive you to the station.
  EXPRESSION: Polite
- CHARACTER: Simon
  LINE: Lovely. Thank you. Let’s go. We’re getting our things.
  EXPRESSION: Relieved
- CHARACTER: Plump Elder
  LINE: I do need your help jumping the truck, if you’ll be so kind.
  EXPRESSION: Requesting
- CHARACTER: Narrator
  LINE: Simon pauses.
  EXPRESSION: null
- CHARACTER: Simon
  LINE: Go pack our stuff. I’ll pick you up out front in - five minutes?
  EXPRESSION: Decisive
- CHARACTER: Plump Elder
  LINE: Fine.
  EXPRESSION: Agreeable
- CHARACTER: Narrator
  LINE: Connie doesn’t want to go alone. She hesitates and then walks quickly off. We track alongside Connie, following her away.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: As Connie speed-walks, panic rises in her. She looks back a few times, making sure that she’s not being followed.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: She arrives at the Main House. Dani and Josh are standing outside. They watch her storm past.
  EXPRESSION: null
- CHARACTER: Dani
  LINE: Are you okay, Connie?
  EXPRESSION: Concerned
- CHARACTER: Connie
  LINE: Yeah. Sorry. We’re actually leaving.
  EXPRESSION: Hurried

::PATHS::
- CHOICE: "Help jump the truck"
  TARGET: main_house_continuous
  STATE_CHANGE: Simon_cooperates = true
  CONDITION: null
- CHOICE: "Go pack"
  TARGET: main_house_continuous
  STATE_CHANGE: Connie_leaves = true
  CONDITION: null

::SCENE::
LOCATION: The Main House - Continuous
MOOD: Hectic
CHARACTERS: Narrator, Connie
BACKGROUND_IMAGE: main_house_connie.png
BACKGROUND_EDIT: "Interior of a rustic house, Connie rushing to her bed"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Connie rushes to her bed.
  EXPRESSION: null
::SCENE::
LOCATION: Hill - Same Time
MOOD: Disturbing
CHARACTERS: Narrator, Dani, Pelle, Christian, Josh, Simon, Ingemar, Thin Elder, Red-Haired Woman, Nine Young Men
BACKGROUND_IMAGE: hill_ceremony.png
BACKGROUND_EDIT: "Dusk, a hill with animals hung upside down, community gathered below"

::SCRIPT::
- CHARACTER: Narrator
  LINE: A baby cow, pig, rabbit, and three tied-together chickens have been strung upside-down. They are all alive. Each of them is separated by about five feet.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The Thin Elder stands to the side of the line-up. On the other side is Siv. The entire community has congregated at the bottom of the hill. Dani looks very nervous. She turns to Pelle, who already looks concerned for her.
  EXPRESSION: null
- CHARACTER: Dani
  LINE: Do I want to stay for this?
  EXPRESSION: Nervous
- CHARACTER: Pelle
  LINE: ...Maybe you should not.
  EXPRESSION: Concerned
- CHARACTER: Narrator
  LINE: Dani looks to Christian. He looks very excited. She turns back to the top of the hill, anxious.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Siv speaks exultantly to the air (in Swedish). When she finishes, steady percussion begins. The Thin Elder strikes a different pose (physically and emotionally) with every percussive hit.
  EXPRESSION: null
- CHARACTER: Red-Haired Woman
  LINE: (WORDLESS CHORAL SONG)
  EXPRESSION: Singing
- CHARACTER: Narrator
  LINE: Nine young men, each holding a blade, walk up to the animals. Simultaneously, they all slit the animals’ throats. The animals thrash wildly as blood drains from their necks. (The song has degraded into anguished snarls and cries.)
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: That does it. Dani storms off. Christian is too awe-stricken to care. Josh, meanwhile, is taking covert photos with his phone.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Beneath each animal, a narrow channel has been pre-carved into the earth. Each channel winds and loops to eventually converge, thus forming a massive runic symbol (symbolizing fertility). The blood pours from each animal to run down the separate canals. Soon, the blood has co-mingled to fill the carefully-engineered runic sculpture. It’s horrible and beautiful.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Josh and Christian, briefly joined in their excitement, trade looks of amazement. Mark looks mystified.
  EXPRESSION: null
- CHARACTER: Mark
  LINE: This is fuckin’ weird, no?
  EXPRESSION: Bewildered
- CHARACTER: Narrator
  LINE: Pelle now goes after Dani, who is speed-walking away.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: In the b.g., Simon can be heard saying:
  EXPRESSION: null
- CHARACTER: Simon (O.S.)
  LINE: What the fuck did you bring us to?
  EXPRESSION: Scared
- CHARACTER: Narrator
  LINE: Christian looks over at this. Simon, who looks very scared, is confronting a grinning Ingemar.
  EXPRESSION: null
- CHARACTER: Simon
  LINE: Why are you smiling, mate?
  EXPRESSION: Aggressive
- CHARACTER: Ingemar
  LINE: (Grinning)
  EXPRESSION: Grinning

::PATHS::
- CHOICE: "Follow Dani"
  TARGET: field_same_time
  STATE_CHANGE: Dani_leaving = +1, Pelle_concerned = +1
  CONDITION: null
- CHOICE: "Observe the ceremony"
  TARGET: field_same_time
  STATE_CHANGE: Christian_awe = +1, Josh_curious = +1
  CONDITION: null

::SCENE::
LOCATION: Field - Same Time
MOOD: Urgent
CHARACTERS: Narrator, Dani, Pelle, Simon, Connie, Ingemar
BACKGROUND_IMAGE: field_escape.png
BACKGROUND_EDIT: "Dusk, Dani running towards the main house, Pelle following"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Dani speed-walks (with intermittent running) toward the Main House in the distance. Pelle follows her, glancing over his shoulder to view more of the ceremony.
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue to Main House"
  TARGET: main_house_minutes_later
  STATE_CHANGE: Dani_panic = +1
  CONDITION: null

::SCENE::
LOCATION: The Main House - Minutes Later
MOOD: Panicked
CHARACTERS: Narrator, Dani, Pelle
BACKGROUND_IMAGE: main_house_packing.png
BACKGROUND_EDIT: "Interior of a rustic house, Dani packing frantically"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Dani enters the Main House, eyes crazed. She goes to her bed and begins hastily packing her bag. Her breathing is erratic and she’s pulling at her neck again (as if to loosen the skin).
  EXPRESSION: Crazed
- CHARACTER: Pelle
  LINE: Dani?
  EXPRESSION: Concerned
- CHARACTER: Narrator
  LINE: Dani looks up, teeth chattering with anxiety.
  EXPRESSION: Anxious
- CHARACTER: Dani
  LINE: I’m really sorry, Pelle. Thank you for inviting me, but I really need to go. Can someone maybe drive me?
  EXPRESSION: Desperate
- CHARACTER: Pelle
  LINE: I did warn you this time. I know it looks extreme, but we only do this once every ninety years. It’s - what’s the word...?
  EXPRESSION: Calm
- CHARACTER: Dani
  LINE: I understand that it’s momentous.
  EXPRESSION: Resigned
- CHARACTER: Pelle
  LINE: Right! Exactly!
  EXPRESSION: Relieved
- CHARACTER: Dani
  LINE: I don’t know why we’re here, Pelle! I don’t know why you invited us!
  EXPRESSION: Frustrated
- CHARACTER: Pelle
  LINE: Okay: Here: Sit down. Please.
  EXPRESSION: Gentle
- CHARACTER: Narrator
  LINE: He sits Dani down. He plants himself beside her, taking her hands.
  EXPRESSION: null
- CHARACTER: Pelle
  LINE: I invited my friends because this is a once-in-a-lifetime thing and I wanted to share it. Especially with my friends who I knew would appreciate it, because I am proud of this place.
  EXPRESSION: Earnest
- CHARACTER: Dani
  LINE: But I’m not an anthropologist. I don’t have the foundation to understand this.
  EXPRESSION: Defensive
- CHARACTER: Pelle
  LINE: And yet I was the most excited for you to come.
  EXPRESSION: Sincere
- CHARACTER: Narrator
  LINE: Pelle has pulled a special pouch from his pocket. He draws something out.
  EXPRESSION: null
- CHARACTER: Pelle
  LINE: Here: smell this.
  EXPRESSION: Encouraging
- CHARACTER: Narrator
  LINE: He places a homemade sachet (containing a special herb) under her nose.
  EXPRESSION: null
- CHARACTER: Dani
  LINE: What is it?
  EXPRESSION: Curious
- CHARACTER: Pelle
  LINE: It calms you down.
  EXPRESSION: Reassuring
- CHARACTER: Narrator
  LINE: She pauses before smelling it.
  EXPRESSION: null
- CHARACTER: Pelle
  LINE: Go on. Inhale. I will, too.
  EXPRESSION: Demonstrative
- CHARACTER: Narrator
  LINE: Demonstrating, he inhales the herb deeply. He puts it back to her nose, and she does the same. She’s still trembling.
  EXPRESSION: null
- CHARACTER: Pelle
  LINE: Isn’t that nice?... I know what you’re going through, Dani.
  EXPRESSION: Empathetic
- CHARACTER: Dani
  LINE: What am I going through? I’m scared. I can’t breathe.
  EXPRESSION: Distressed
- CHARACTER: Pelle
  LINE: You’re going through a lot.
  EXPRESSION: Understanding
- CHARACTER: Pelle
  LINE: I know you are, and I’m gonna say something now, because my birth parents are both gone, too--
  EXPRESSION: Somber
- CHARACTER: Dani
  LINE: What?! (crying now) That’s not what I’m talking about!
  EXPRESSION: Upset
- CHARACTER: Pelle
  LINE: I know, and that’s fine, but please... My birth-parents both died when I was a little boy. They burned up in a fire, and I became - technically - an orphan. So believe me when I say I know what that is, because I do. Yet my difference is: I didn’t get a chance to feel lost. Because I had a family - here - where everyone embraced me and swept me up and I was raised by a community that doesn’t distinguish between what is theirs and what is not theirs. That’s what you were sacrificed to. But I - have always felt...held. By a family. A real family. Which everyone deserves. And you deserve.
  EXPRESSION: Emotional
- CHARACTER: Narrator
  LINE: Dani looks down at Pelle’s hands gripping hers.
  EXPRESSION: null
- CHARACTER: Dani
  LINE: Christian could walk in.
  EXPRESSION: Anxious
- CHARACTER: Pelle
  LINE: He’s what I’m talking about. And he’s my good friend and I like him... But do you feel held by him, Dani? Does he feel like a home to you?
  EXPRESSION: Intense
- CHARACTER: Narrator
  LINE: His eyes are locked intensely on Dani’s. She doesn’t turn away.
  EXPRESSION: null
- CHARACTER: Pelle
  LINE: My pilgrimage has been fun. New York is fun... But I also find it terrifying how people live. As if it’s necessary and even good to be lost and drifting...and I haven’t spent one night over there that I haven’t longed to be back here...in the lap of the Hårgas.
  EXPRESSION: Longing
- CHARACTER: Narrator
  LINE: Dani looks almost hypnotized as she looks into Pelle’s eyes.
  EXPRESSION: null
- CHARACTER: Pelle
  LINE: Stay, Dani. Please. It will be good... And I swear we’re all finished sacrificing animals.
  EXPRESSION: Pleading
- CHARACTER: Narrator
  LINE: Dani gives a weak half-laugh. She relents. She sits up straight and wipes her eyes, regaining composure.
  EXPRESSION: null
- CHARACTER: Pelle
  LINE: Good.
  EXPRESSION: Satisfied
- CHARACTER: Narrator
  LINE: Pelle stands up.
  EXPRESSION: null
- CHARACTER: Dani
  LINE: You’re a very empathic person, do you know that?
  EXPRESSION: Grateful
- CHARACTER: Pelle
  LINE: Well, our first language here is strictly emotion-based. So I could just be using that to manipulate you.
  EXPRESSION: Teasing
- CHARACTER: Narrator
  LINE: Dani pauses at this. Pelle sticks his tongue out, teasing.
  EXPRESSION: null
- CHARACTER: Pelle
  LINE: You are very vulnerable, though. And I mean that in a great way. It’s very rare. It’s beautiful.
  EXPRESSION: Admiring
- CHARACTER: Narrator
  LINE: Dani is touched, but tries to hide it.
  EXPRESSION: null
- CHARACTER: Dani
  LINE: Can I smell that again?
  EXPRESSION: Vulnerable

::PATHS::
- CHOICE: "Stay"
  TARGET: hill_same_time_2
  STATE_CHANGE: Dani_calm = +1, Dani_stays = true
  CONDITION: null
- CHOICE: "Leave"
  TARGET: hill_same_time_2
  STATE_CHANGE: Dani_leaves = true
  CONDITION: null

::SCENE::
LOCATION: Hill - Same Time
MOOD: Confrontational
CHARACTERS: Narrator, Simon, Connie, Ingemar, Plump Elder, Woman
BACKGROUND_IMAGE: hill_lunch_setup.png
BACKGROUND_EDIT: "Dusk, tables being set up for lunch, ceremony ending"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The ceremony has ended. Groups are now setting up tables for lunch. As usual, they’re being laid out in a particular pattern.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Simon and Connie stand frozen, traumatized. Simon is visibly distraught. He stares up at the top of the hill, where the dangling, blood-drained animals are now being cut down.
  EXPRESSION: Distraught
- CHARACTER: Simon
  LINE: Are we eating those animals?
  EXPRESSION: Horrified
- CHARACTER: Ingemar
  LINE: Not those ones.
  EXPRESSION: Matter-of-fact
- CHARACTER: Simon
  LINE: And why not?
  EXPRESSION: Aggressive
- CHARACTER: Ingemar
  LINE: ...Because they weren’t killed for that.
  EXPRESSION: Calm
- CHARACTER: Simon
  LINE: So what were they killed for? So we could watch that shit and clap?
  EXPRESSION: Enraged
- CHARACTER: Narrator
  LINE: Ingemar smiles. This infuriates Simon.
  EXPRESSION: null
- CHARACTER: Simon
  LINE: What the fuck is that smile, mate? Get it off.
  EXPRESSION: Furious
- CHARACTER: Connie
  LINE: Simon...
  EXPRESSION: Pleading
- CHARACTER: Narrator
  LINE: This has drawn attention. People are now looking over.
  EXPRESSION: null
- CHARACTER: Ingemar
  LINE: We can talk about this over here.
  EXPRESSION: Inviting
- CHARACTER: Simon
  LINE: Why didn’t we talk about it before you took us here?
  EXPRESSION: Accusatory
- CHARACTER: Narrator
  LINE: Ingemar gently touches Simon’s arm to lead him away.
  EXPRESSION: null
- CHARACTER: Simon
  LINE: Don’t sort me out, mate!
  EXPRESSION: Rebellious
- CHARACTER: Plump Elder
  LINE: What’s offending you, son?
  EXPRESSION: Inquisitive
- CHARACTER: Simon
  LINE: What’s offending me? Besides the fact I just saw something I can’t ever unsee, I’m offended that you’re teaching impressionable kids to sacrifice living, innocent animals - including a fucking defenseless dog--
  EXPRESSION: Outraged
- CHARACTER: Woman
  LINE: We sacrificed defenseless animals yesterday, too! To fill your belly!
  EXPRESSION: Defensive
- CHARACTER: Plump Elder
  LINE: Why are we using “sacrifice” like it’s a dirty word?
  EXPRESSION: Questioning
- CHARACTER: Simon
  LINE: Because it’s fucking medieval!
  EXPRESSION: Indignant
- CHARACTER: Woman
  LINE: Why are you swearing?! We’re not swearing!
  EXPRESSION: Scolding
- CHARACTER: Plump Elder
  LINE: You’ll find that sacrifice is essential in any relationship. Let’s put it in your terms--
  EXPRESSION: Authoritative
- CHARACTER: Simon
  LINE: You don’t know my terms!
  EXPRESSION: Defiant
- CHARACTER: Plump Elder
  LINE: Say you find yourself entangled with a lover who can’t put your needs before her own. Say you learn that your partner can’t part with even a fraction of his own comfort to give you what you need. And show that you’re appreciated. Wouldn’t you start to resent this person? Wouldn’t your own performance begin to lack, knowing they’re not pulling their weight? Wouldn’t you want to punish that person for taking you for granted? Sacrifice is proof. And without it, no union can last.
  EXPRESSION: Eloquent
- CHARACTER: Narrator
  LINE: Beat. Simon pops the bubble:
  EXPRESSION: null
- CHARACTER: Simon
  LINE: Alright. Thank you for that. And now we’ve seen two people kill themselves and nine animals get bled to death, so I think we’re leaving.
  EXPRESSION: Resolute
- CHARACTER: Plump Elder
  LINE: I’ll happily drive you to the station.
  EXPRESSION: Polite
- CHARACTER: Simon
  LINE: Lovely. Thank you. Let’s go. We’re getting our things.
  EXPRESSION: Relieved
- CHARACTER: Plump Elder
  LINE: I do need your help jumping the truck, if you’ll be so kind.
  EXPRESSION: Requesting
- CHARACTER: Narrator
  LINE: Simon pauses.
  EXPRESSION: null
- CHARACTER: Simon
  LINE: Go pack our stuff. I’ll pick you up out front in - five minutes?
  EXPRESSION: Decisive
- CHARACTER: Plump Elder
  LINE: Fine.
  EXPRESSION: Agreeable
- CHARACTER: Narrator
  LINE: Connie doesn’t want to go alone. She hesitates and then walks quickly off. We track alongside Connie, following her away.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: As Connie speed-walks, panic rises in her. She looks back a few times, making sure that she’s not being followed.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: She arrives at the Main House. Dani and Josh are standing outside. They watch her storm past.
  EXPRESSION: null
- CHARACTER: Dani
  LINE: Are you okay, Connie?
  EXPRESSION: Concerned
- CHARACTER: Connie
  LINE: Yeah. Sorry. We’re actually leaving.
  EXPRESSION: Hurried

::PATHS::
- CHOICE: "Help jump the truck"
  TARGET: main_house_continuous
  STATE_CHANGE: Simon_cooperates = true
  CONDITION: null
- CHOICE: "Go pack"
  TARGET: main_house_continuous
  STATE_CHANGE: Connie_leaves = true
  CONDITION: null

::SCENE::
LOCATION: The Main House - Continuous
MOOD: Hectic
CHARACTERS: Narrator, Connie
BACKGROUND_IMAGE: main_house_connie.png
BACKGROUND_EDIT: "Interior of a rustic house, Connie rushing to her bed"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Connie rushes to her bed.
  EXPRESSION: null

::SCENE::
LOCATION: The Main House
MOOD: Anxious
CHARACTERS: Connie, Dani, Simon, Odd
BACKGROUND_IMAGE: main_house.png
BACKGROUND_EDIT: "Exterior, woman (Connie) holding bags, ready to leave"

::SCRIPT::
- CHARACTER: Narrator
  LINE: She starts throwing her things into her suitcase.
  EXPRESSION: null
- CHARACTER: Connie
  LINE: It was really lovely meeting you, Dani.
  EXPRESSION: Anxious
- CHARACTER: Dani
  LINE: Yeah, it was lovely meeting you, too.
  EXPRESSION: null
- CHARACTER: Connie
  LINE: Sorry to just leave like this. Simon’s coming with the car.
  EXPRESSION: Anxious
- CHARACTER: Dani
  LINE: I understand. I might be right behind you.
  EXPRESSION: null
- CHARACTER: Connie
  LINE: Simon went mental. Christ. I feel sick. We exchanged emails an’ all that, yeah?
  EXPRESSION: Overdrive
- CHARACTER: Dani
  LINE: No. We didn’t.
  EXPRESSION: null
- CHARACTER: Connie
  LINE: Oh. I’m Connie-dot-Brahms at AOL.com.
  EXPRESSION: null
- CHARACTER: Dani
  LINE: Connie-dot-Brahms. I’ll write you.
  EXPRESSION: null
- CHARACTER: Connie
  LINE: Yeah. Lovely. Sorry to just leave like this.
  EXPRESSION: null
- CHARACTER: Odd
  LINE: Connie! Simon told me to tell you... Jan drove him to the train station. After Simon gets dropped off, he’s sending the truck straight back for you -
  EXPRESSION: null
- CHARACTER: Connie
  LINE: What?
  EXPRESSION: null
- CHARACTER: Odd
  LINE: - and you’ll meet him there.
  EXPRESSION: null
- CHARACTER: Connie
  LINE: No. Why would he go without me? He wouldn’t do that.
  EXPRESSION: null
- CHARACTER: Odd
  LINE: The truck only had room for two.
  EXPRESSION: null
- CHARACTER: Connie
  LINE: What does that mean? That’s not real. Why wouldn’t he tell me?
  EXPRESSION: null
- CHARACTER: Odd
  LINE: Today’s only train leaves in ninety minutes. It takes forty-five minutes to drive there and back. They didn’t want to waste time.
  EXPRESSION: null
- CHARACTER: Connie
  LINE: So I could have sat on his lap!
  EXPRESSION: null
- CHARACTER: Odd
  LINE: Simon mentioned that, too. We don’t break traffic laws.
  EXPRESSION: null
- CHARACTER: Connie
  LINE: They just left without me, just now?
  EXPRESSION: null
- CHARACTER: Odd
  LINE: There wasn’t room in the truck. Yet it is coming right back. For you.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Connie shakes her head, not buying it. She WALKS OFF, on a mission to find out more. Odd turns to Dani:
  EXPRESSION: null
- CHARACTER: Odd
  LINE: Lunch has been called.
  EXPRESSION: null

::PATHS::
- CHOICE: "Connie walks off"
  TARGET: field_lunch
  STATE_CHANGE: null
  CONDITION: null
- CHOICE: "Dani stays"
  TARGET: field_lunch
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Field
MOOD: Tension, Investigation
CHARACTERS: Ulf, Elder, Mark, Christian, Happy Man, Dani, Josh
BACKGROUND_IMAGE: field.png
BACKGROUND_EDIT: "Daytime, people seated at tables in a helix shape, some engaged in conversation"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Lunch time. Everyone is seated at the tables (which are connected to form a HELIX shape).
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Ulf, still panicked over the damage done to “his tree,” is consulting a bespectacled elder.
  EXPRESSION: null
- CHARACTER: Ulf
  LINE: It feels like a tingling. Like a numbness in my arm.
  EXPRESSION: Panicked
- CHARACTER: Narrator
  LINE: The Elder presses his arm. Mark watches this, very nervous. Farther down the table, Christian sits beside a Happy Man (30s). Christian takes notes as he asks questions. Two Hårga women listen in, smiling. Christian’s eyes keep straying to Josh, who is also questioning people. They are now racing to gather info.
  EXPRESSION: null
- CHARACTER: Christian
  LINE: How are roles or jobs assigned?
  EXPRESSION:null
- CHARACTER: Happy Man
  LINE: Well - that’s based on traits we show as children. For example: He was assigned “to protect,” so he did his pilgrimage as doctor.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Christian quickly writes this down as Dani arrives at the table. She sits next to Christian.
  EXPRESSION: null
- CHARACTER: Christian
  LINE: Hey. You okay?
  EXPRESSION: null
- CHARACTER: Dani
  LINE: ...Simon left without Connie.
  EXPRESSION: null
- CHARACTER: Christian
  LINE: Really? That’s so shitty.
  EXPRESSION: Faux concern
- CHARACTER: Narrator
  LINE: Christian bluntly returns his attention to the Happy Man. Dani pauses, disturbed by Christian’s indifference. For the first time, she actually looks scared of him.
  EXPRESSION: null
- CHARACTER: Christian
  LINE: Is incest ever a problem?
  EXPRESSION: null
- CHARACTER: Happy Man
  LINE: Ha! Well...the bloodlines are very well preserved, so - the elders must approve mates.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Christian is taking feverish notes. Dani watches him with a new kind of scrutiny; a new kind of distrust. As Christian writes, he glances over at: Josh, who is now interrogating an uncomfortable Bald Man (40s).
  EXPRESSION: null
- CHARACTER: Josh
  LINE: What about the holy text? Ruby Radr?
  EXPRESSION: null
- CHARACTER: Bald Man
  LINE: Um...I cannot answer this for you. You might ask a elder.
  EXPRESSION: null

::PATHS::
- CHOICE: "Dani continues to observe Christian"
  TARGET: field_lunch_later
  STATE_CHANGE: distrust_christian = +1
  CONDITION: null

::SCENE::
LOCATION: Field
MOOD: Investigation, Growing Suspicion
CHARACTERS: Josh, Thin Elder
BACKGROUND_IMAGE: field.png
BACKGROUND_EDIT: "Daytime, lunch has concluded, some people remain seated, others move about"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Lunch is over. Josh is now interrogating the Thin Elder on the grass.
  EXPRESSION: null
- CHARACTER: Thin Elder
  LINE: I don’t understand: You want to see it?
  EXPRESSION: null
- CHARACTER: Josh
  LINE: I wouldn’t even touch.
  EXPRESSION: null
- CHARACTER: Thin Elder
  LINE: It’s written in our Affect language. You would not be able to read it...
  EXPRESSION: null

::PATHS::
- CHOICE: "Josh continues interrogation"
  TARGET: farmstead_kitchen
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Farmstead
MOOD: Contemplation, Community
CHARACTERS: Dani, Pelle, Small Woman, Other Women, Maja, Siv
BACKGROUND_IMAGE: farmstead.png
BACKGROUND_EDIT: "Daytime, exterior of a farmstead, women preparing food"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Dani walks idly around, thinking about her exchange with Pelle (and about Simon leaving Connie). She holds the folded drawing that Pelle gave her for her birthday. As the gears turn in her head, her attention falls on... A large kitchen in one of the houses. A group of women (all ages) collaborate to prepare dinner. One small woman (40s) sees Dani and waves her over. Dani pauses and then approaches.
  EXPRESSION: null
- CHARACTER: Small Woman
  LINE: Would you like to help join us?
  EXPRESSION: null
- CHARACTER: Dani
  LINE: Sure! But actually - have you seen Simon?
  EXPRESSION: null
- CHARACTER: Small Woman
  LINE: Oh, yes, he was driven to the station. Did you not say goodbye?
  EXPRESSION: null
- CHARACTER: Dani
  LINE: No. I didn’t. But that’s okay... What are we making?
  EXPRESSION: null
- CHARACTER: Small Woman
  LINE: Meat tarts!
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Dani smiles “ooh!” and joins the women. She’s handed an apron. Another Woman says something to Dani in Swedish.
  EXPRESSION: null
- CHARACTER: Small Woman
  LINE: She says you’re so beautiful.
  EXPRESSION: null
- CHARACTER: Dani
  LINE: Oh! She’s so beautiful!
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Meanwhile, Maja is preparing a tray of unbaked meat pies. One of the pies is clearly very special. She distinguishes this one by laying a special basil leaf on top.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Siv stands among labouring men, staring at the kitchen window. She watches Dani.
  EXPRESSION: null

::PATHS::
- CHOICE: "Dani helps with the food"
  TARGET: temple_interior
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Temple
MOOD: Esoteric, Revealing
CHARACTERS: Josh, Thin Elder, Ruben
BACKGROUND_IMAGE: temple.png
BACKGROUND_EDIT: "Interior, altar, ancient texts"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The holy temple. Josh stands near the altar with the Thin Elder, who has pulled the Rubi Radr from an elevated pedestal. He shows Josh the text (written in the graphic Affect language - a combination of runes and abstract hand paintings).
  EXPRESSION: null
- CHARACTER: Thin Elder
  LINE: We describe it like “emotional sheet music.”
  EXPRESSION: null
- CHARACTER: Josh
  LINE: What does it say?
  EXPRESSION: null
- CHARACTER: Thin Elder
  LINE: Well...each runic letter represents one of the 16 affects, which are graded from most holy to most unholy. This here is about Grief. You can see at the end, however, we have blank pages?
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Indeed the last half of the book is blank.
  EXPRESSION: null
- CHARACTER: Thin Elder
  LINE: This is because the Rubi Radr is a constant work in progress. Always evolving.
  EXPRESSION: null
- CHARACTER: Josh
  LINE: And who decides what’s added?
  EXPRESSION: null
- CHARACTER: Thin Elder
  LINE: Well - this iteration is being written by Ruben.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The Thin Elder points to Ruben, the mentally disabled boy, who is playing outside.
  EXPRESSION: null
- CHARACTER: Josh
  LINE: Wait. The...disabled?
  EXPRESSION: null
- CHARACTER: Thin Elder
  LINE: Since birth. He draws and the Elders interpret.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: He shows Josh the first pages. They are marked by a baby’s handprints - all in different colors of paint. (Below the drawings are runic interpretations.)
  EXPRESSION: null
- CHARACTER: Thin Elder
  LINE: Ruben is unclouded by normal cognition. It makes him open for the source.
  EXPRESSION: null
- CHARACTER: Josh
  LINE: So...what happens when Ruben dies? Do you just wait until a new baby isn't “clouded”?
  EXPRESSION: null
- CHARACTER: Thin Elder
  LINE: Ruben was a product of inbreeding. All of our Oracles have been deliberate products of inbreeding.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Josh’s jaw hangs. He hides his amazement.
  EXPRESSION: null
- CHARACTER: Josh
  LINE: Can I possibly take a photograph?
  EXPRESSION: null
- CHARACTER: Thin Elder
  LINE: What? No. Absolutely not.
  EXPRESSION: Alarmed
- CHARACTER: Narrator
  LINE: The Elder closes the book.
  EXPRESSION: null
- CHARACTER: Josh
  LINE: Okay. Sorry.
  EXPRESSION: null
- CHARACTER: Thin Elder
  LINE: Absolutely not.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: A tense beat. Broken suddenly by: Screaming, outside. They turn.
  EXPRESSION: null
- CHARACTER: Connie (O.S.)
  LINE: SIMON!! SIMON!!
  EXPRESSION: Panicked

::PATHS::
- CHOICE: "Investigate the screaming"
  TARGET: field_screaming
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Field
MOOD: Panic, Desperation
CHARACTERS: Connie, Hårgan Man #1, Hårgan Man #2, Christian, Mark
BACKGROUND_IMAGE: field.png
BACKGROUND_EDIT: "Daytime, woman (Connie) is distressed, surrounded by Hårgans"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Connie, panicked and crying, backs away from three encroaching Hårgans (all 30s). They approach her carefully, trying to calm her down. Connie desperately appeals to Christian and Mark:
  EXPRESSION: null
- CHARACTER: Connie
  LINE: Please! I’m begging you! I saw them pulling Simon! I swear I saw them!
  EXPRESSION: Panicked
- CHARACTER: Hårgan Man #1
  LINE: He was driven to town an hour ago. We all watched them drive off.
  EXPRESSION: null
- CHARACTER: Connie
  LINE: I’m not talking to you!! Please. You have to believe me. I saw them dragging Simon through the woods. He was unconscious.
  EXPRESSION: Panicked
- CHARACTER: Christian
  LINE: Where?
  EXPRESSION: null
- CHARACTER: Connie
  LINE: Back there. Near the river. Please.
  EXPRESSION: null
- CHARACTER: Christian
  LINE: Can you show us? Can she show us?
  EXPRESSION: null
- CHARACTER: Connie
  LINE: Please.
  EXPRESSION: Crying
- CHARACTER: Hårgan Man #1
  LINE: Of course. Just please - calm down. I promise it’s not what you think you saw.
  EXPRESSION: null
- CHARACTER: Hårgan Man #2
  LINE: And the truck is already back for you, by the way! You can leave.
  EXPRESSION: Impatient
- CHARACTER: Connie
  LINE: I’M NOT GOING WITHOUT SIMON!
  EXPRESSION: Panicked

::PATHS::
- CHOICE: "Connie leads them to the woods"
  TARGET: woods_search
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Woods
MOOD: Desperate Search, Growing Distrust
CHARACTERS: Connie, Christian, Mark, Hårgan Man #1, Hårgan Man #2
BACKGROUND_IMAGE: woods.png
BACKGROUND_EDIT: "Daytime, dense woods, the group is searching"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Connie desperately leads the group (Christian, Mark, and the two Hårgans) into the woods. She keeps her eyes locked on Christian, as if begging him to believe her.
  EXPRESSION: null
- CHARACTER: Connie
  LINE: It was right back here! I swear to God. Right over there! They were dragging him by the arms and he wasn’t moving and his head was bleeding!
  EXPRESSION: Panicked
- CHARACTER: Hårgan Man #1
  LINE: So why didn’t you try to stop them? Or follow them? So where did they go?
  EXPRESSION: null
- CHARACTER: Connie
  LINE: I couldn’t even breathe! They went behind the bushes. I ran back for help. I wanted to find someone!
  EXPRESSION: Panicked
- CHARACTER: Christian
  LINE: Which direction were they going?
  EXPRESSION: null
- CHARACTER: Connie
  LINE: That way! They rushed behind the bushes when they saw me.
  EXPRESSION: null
- CHARACTER: Hårgan Man #1
  LINE: Okay: I can tell you’re saying the truth. Let’s all go in the direction you saw them. If he’s here, we’ll find him.
  EXPRESSION: Placating
- CHARACTER: Connie
  LINE: They’d have already hid him by now! You’re lying!!
  EXPRESSION: Panicked
- CHARACTER: Narrator
  LINE: The Hårgan Man wears a false smile, but his eyes buzz.
  EXPRESSION: null
- CHARACTER: Christian
  LINE: I’ll go. Okay? They went in that direction? I’ll go looking. Great. You and Mark go together. Okay, Mark? We’ll cover more ground.
  EXPRESSION: null
- CHARACTER: Connie
  LINE: I’m coming, too.
  EXPRESSION: null
- CHARACTER: Christian
  LINE: I don’t want them.
  EXPRESSION: null
- CHARACTER: Christian
  LINE: They’ll go away. Right? Thanks guys. Sorry.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The Hårgan men concede. They begin walking off.
  EXPRESSION: null
- CHARACTER: Hårgan Man #1
  LINE: I hope you find him.
  EXPRESSION: null
- CHARACTER: Hårgan Man #2
  LINE: And the truck is waiting for you when you finally choose to leave.
  EXPRESSION: null

::PATHS::
- CHOICE: "Christian and Mark search separately"
  TARGET: woods_blood_trail
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Woods
MOOD: Unease, Discovery
CHARACTERS: Christian, Mark
BACKGROUND_IMAGE: woods.png
BACKGROUND_EDIT: "Daytime, woods, Christian is walking"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Christian walks alone through the woods, half-heartedly searching. He suddenly stumbles upon a vague trail of dried blood, streaked across the grass. Christian pauses at this. Tree limbs groan in the wind.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Christian looks up, left and right. Nobody’s around.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Minutes later, Christian sees Mark in the distance. He walks over.
  EXPRESSION: null
- CHARACTER: Christian
  LINE: Where’s Connie?
  EXPRESSION: null
- CHARACTER: Mark
  LINE: She got freaked out and ran back. I dunno.
  EXPRESSION: null
- CHARACTER: Christian
  LINE: She went off alone?
  EXPRESSION: Skeptical
- CHARACTER: Mark
  LINE: She’s fucking nuts, dude. So are the rest of th
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue the search"
  TARGET: end
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Field
MOOD: Suspicion
CHARACTERS: Narrator, Mark, Christian
BACKGROUND_IMAGE: field_day.png
BACKGROUND_EDIT: "Daytime, open field, woods in background"

::SCRIPT::
- CHARACTER: Narrator
  LINE: These people. The whole fuckin’ place is crazy.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: They arrive at each other.
  EXPRESSION: null
- CHARACTER: Mark
  LINE: Did you find anything?
  EXPRESSION: null
- CHARACTER: Christian
  LINE: Not really.
  EXPRESSION: null
- CHARACTER: Mark
  LINE: ...I do really wanna fuck that brunette.
  EXPRESSION: null

::PATHS::
- CHOICE: "Return from the woods"
  TARGET: field_rock_circle
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Field - Rock Circle
MOOD: Ominous
CHARACTERS: Narrator, Christian, Mark, Hårgan Man #1, Hårgan Boy
BACKGROUND_IMAGE: field_rock_circle.png
BACKGROUND_EDIT: "Daytime, field with a dense circle of rocks around a yellow sacred house"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Christian and Mark return from the woods. They approach the two Hårgan men, who are now laying a dense circle of rocks around the ominous, yellow sacred house (which we saw earlier, isolated in the field).
  EXPRESSION: null
- CHARACTER: Christian
  LINE: Did Connie come back here?
  EXPRESSION: null
- CHARACTER: Hårgan Man #1
  LINE: Uh - yes. Her boyfriend called our landline from the station and they talked on the phone. Then she begged our pardon and Jan drove her to the station.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Christian squints with burgeoning suspicion.
  EXPRESSION: Suspicious
- CHARACTER: Christian
  LINE: Okay. Huh. I guess that’s a relief.
  EXPRESSION: null
- CHARACTER: Hårgan Man #1
  LINE: For her it was. We already saw him leave the first time.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: In the b.g., a Hårgan Boy (13) runs from one group to another, announcing:
  EXPRESSION: null
- CHARACTER: Boy
  LINE: Supper is ready! ... They’re calling supper!
  EXPRESSION: null

::PATHS::
- CHOICE: "Go to the hill for supper"
  TARGET: hill_supper
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Hill - Supper
MOOD: Tense
CHARACTERS: Narrator, Christian, Dani, Josh, Mark, Pelle, Servers, Coy-Looking Server
BACKGROUND_IMAGE: hill_supper.png
BACKGROUND_EDIT: "Daytime, tables set in a star pattern at the base of a hill, people seated"

::SCRIPT::
- CHARACTER: Narrator
  LINE: At the base of the hill, the dining tables are now set in the pattern of a star. Everyone is seated, save for some stragglers.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Christian, Dani, Josh and Mark sit at a table. Pelle is seated a few seats away. Dani glances over at him. He smiles warmly and looks away. Dani’s eyes linger on him.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The servers are laying plates in front of everyone. One especially coy-looking server sets a plate in front of Christian.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: It features the special meat pie with the basil leaf on top.
  EXPRESSION: null
- CHARACTER: Christian
  LINE: Thanks.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Dani turns to Christian.
  EXPRESSION: null
- CHARACTER: Dani
  LINE: Do you know what happened with Connie?
  EXPRESSION: null
- CHARACTER: Christian
  LINE: She supposedly got driven to the station.
  EXPRESSION: null
- CHARACTER: Dani
  LINE: Why do you think Simon would leave without her?
  EXPRESSION: null
- CHARACTER: Christian
  LINE: ...The fuck does that mean?
  EXPRESSION: Angry
- CHARACTER: Narrator
  LINE: Christian stares at Dani. Surprised at the uncharacteristic defiance.
  EXPRESSION: Surprised
- CHARACTER: Narrator
  LINE: Meanwhile, Mark has noticed Ulf staring at him from a distance.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Ulf has murder in his eyes.
  EXPRESSION: Angry
- CHARACTER: Mark
  LINE: Fuck. Somebody’s still sore about “his tree.”
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Josh looks up to see Ulf, whose eyes really are trained on Mark.
  EXPRESSION: null
- CHARACTER: Josh
  LINE: Yikes.
  EXPRESSION: Scared
- CHARACTER: Mark
  LINE: Is he gonna kill me?
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Josh, preoccupied, turns to Christian. He asks, faux-casually:
  EXPRESSION: null
- CHARACTER: Josh
  LINE: Did you learn anything about the Rubi Radr?
  EXPRESSION: null
- CHARACTER: Christian
  LINE: Oh, what? You wanna collaborate now?
  EXPRESSION: Mocking
- CHARACTER: Narrator
  LINE: Josh ignores this and moves on to his food.
  EXPRESSION: null
- CHARACTER: Christian
  LINE: I know that one elder showed you through it...
  EXPRESSION: null
- CHARACTER: Josh
  LINE: Yeah, barely. Never mind. Sorry I brought it up.
  EXPRESSION: Annoyed
- CHARACTER: Narrator
  LINE: Christian seethes. He takes a bite of his tart. As he chews, he catches something on his tongue. He turns away from Dani, and pulls a pubic hair from his mouth. His eyes widen with alarm.
  EXPRESSION: Alarmed
- CHARACTER: Mark
  LINE: Oh my God, dude. What the fuck?
  EXPRESSION: Shocked
- CHARACTER: Dani
  LINE: What is it?
  EXPRESSION: Curious
- CHARACTER: Christian
  LINE: Just a piece of bone.
  EXPRESSION: Lying
- CHARACTER: Dani
  LINE: Ew.
  EXPRESSION: Disgusted
- CHARACTER: Christian
  LINE: Yeah. It’s okay.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Mark leans in to whisper to Christian:
  EXPRESSION: null
- CHARACTER: Mark
  LINE: Was that a fucking pube?
  EXPRESSION: Whispering
- CHARACTER: Christian
  LINE: Shhh! Calm down.
  EXPRESSION: Whispering
- CHARACTER: Narrator
  LINE: Christian sits “casually” back into his chair. He tucks the pubic hair into his pocket. He looks around to finally alight on Maja. She is smiling at him. Dani catches this.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Christian self-consciously breaks the gaze, taking a sip of his drink (a pink-tinted mead). He then pauses, realizing what he might be drinking (namely, menstrual blood). Paranoid, he sets the drink back down.
  EXPRESSION: Paranoid
- CHARACTER: Narrator
  LINE: Mark notices that Ulf is still staring him down.
  EXPRESSION: null
- CHARACTER: Mark
  LINE: Jesus. He’s still lookin’ at me. I don’t like this.
  EXPRESSION: Nervous
- CHARACTER: Narrator
  LINE: Josh looks tensely at his notes. He stares at a line that reads: Affects -- runic combinations, “emotional sheet music”
  EXPRESSION: Tense
- CHARACTER: Narrator
  LINE: Inga, the pretty brunette, sneaks up behind Mark. She whispers in his ear.
  EXPRESSION: null
- CHARACTER: Inga
  LINE: You will come with me?
  EXPRESSION: Seductive
- CHARACTER: Narrator
  LINE: Mark turns to her, startled. He smiles widely.
  EXPRESSION: Startled
- CHARACTER: Mark
  LINE: What?
  EXPRESSION: null
- CHARACTER: Inga
  LINE: You will come? I show you.
  EXPRESSION:null
- CHARACTER: Mark
  LINE: Uhhh... Oh-kay.
  EXPRESSION: Uncertain
- CHARACTER: Inga
  LINE: Yes?
  EXPRESSION:null
- CHARACTER: Mark
  LINE: Yeah. Okay. Sure. Great.
  EXPRESSION: Excited
- CHARACTER: Narrator
  LINE: Mark rises from his seat.
  EXPRESSION: null
- CHARACTER: Mark
  LINE: I’ll be back, I guess? She’s gonna show me...
  EXPRESSION: Excited
- CHARACTER: Narrator
  LINE: Mark looks very excited as he walks off with Inga. She takes his hand and leads him toward the woods.
  EXPRESSION: null
- CHARACTER: Dani
  LINE: Somebody for everybody, I guess.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Josh is so immersed in his thoughts, he didn’t even notice Mark being lured away.
  EXPRESSION: null

::PATHS::
- CHOICE: "Go to bed"
  TARGET: main_house_night
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: The Main House - Night
MOOD: Tense
CHARACTERS: Narrator, Josh, Dani
BACKGROUND_IMAGE: main_house_night.png
BACKGROUND_EDIT: "Nighttime interior of a house, people getting ready for bed"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Everybody is climbing into bed. Josh’s eyes, however, are busy. He’s thinking intensely about something.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Dani sneaks up on him.
  EXPRESSION: null
- CHARACTER: Dani
  LINE: Hey, can I steal another sleeping pill? Only half this time.
  EXPRESSION: null
- CHARACTER: Josh
  LINE: Oh. Yeah. Okay.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Josh fetches her a pill. She takes it and moves to her bed.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Josh crawls stiffly into his bed. He’s still wearing his shoes.
  EXPRESSION: null

::PATHS::
- CHOICE: "Stay awake and leave the house"
  TARGET: main_house_later
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: The Main House - Later
MOOD: Tense
CHARACTERS: Narrator, Josh
BACKGROUND_IMAGE: main_house_later.png
BACKGROUND_EDIT: "Later nighttime interior of a house, everyone asleep except Josh"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Everyone is asleep, except for Josh, who looks as tense as before. He sits up, scanning the room to make sure nobody is awake. He then climbs quietly out of bed. He creeps to the door and silently exits.
  EXPRESSION: Tense
  EXPRESSION: null

::PATHS::
- CHOICE: "Go to the temple"
  TARGET: temple_foyer
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: The Main House - Continuous
MOOD: Dark
CHARACTERS: Narrator, Josh
BACKGROUND_IMAGE: main_house_continuous.png
BACKGROUND_EDIT: "Dark twilight exterior of a house"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Josh rushes across the grass. It’s now darkest twilight. He hustles to the temple, glancing nervously about.
  EXPRESSION: Nervous

::PATHS::
- CHOICE: "Enter the temple"
  TARGET: temple_interior
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Temple - Foyer
MOOD: Dark
CHARACTERS: Narrator, Josh
BACKGROUND_IMAGE: temple_foyer.png
BACKGROUND_EDIT: "Dark foyer of a temple"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Josh passes the dark foyer to enter through the temple doors...
  EXPRESSION: null

::PATHS::
- CHOICE: "Enter the temple's main area"
  TARGET: temple_main
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Temple
MOOD: Tense
CHARACTERS: Narrator, Josh, Mark, Ulf
BACKGROUND_IMAGE: temple.png
BACKGROUND_EDIT: "Interior of a temple, holy book on a pedestal"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Josh sneaks into the temple. He creeps over to the pedestal featuring the holy book Rubi Radr. He pulls out his phone, turns on the flashlight, and begins taking silent photos - page by page - of Rubi Radr’s text.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: While he anxiously photographs, Josh keeps glancing up at the temple doors, making sure he’s still alone. He has photographed about fifteen pages when he hears the front door creak open.
  EXPRESSION: Anxious
- CHARACTER: Narrator
  LINE: Josh freezes. He looks up. Through the temple’s open doors, he sees someone standing in the dark foyer. The person is barely visible in the dimness. After some scrutiny, Josh makes it out to be Mark. He is standing motionless.
  EXPRESSION: Frozen
- CHARACTER: Josh
  LINE: Holy fuck. Mark?
  EXPRESSION: Relieved
- CHARACTER: Narrator
  LINE: But Mark doesn’t move or speak.
  EXPRESSION: null
- CHARACTER: Josh
  LINE: What the fuck are you doing? Close the door! We’re not supposed to be here.
  EXPRESSION: Whispering
- CHARACTER: Narrator
  LINE: Mark still doesn’t move. Despite how hard it is to see, one can tell that his body looks bulkier than usual. And his face seems somewhat swollen.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Josh looks unsettled. He starts moving toward the door.
  EXPRESSION: Unsettled
- CHARACTER: Josh
  LINE: Mark? Hello? What the fu--?
  EXPRESSION: Whispering
- CHARACTER: Narrator
  LINE: Mark steps forward. It is now bright enough to see... This isn’t Mark. It’s a larger man, and he’s wearing Mark’s skin (which is stretched uneasily over the man’s bulkier features). Upon closer inspection, one might identify these features as belonging to Ulf.
  EXPRESSION: Horrified
- CHARACTER: Narrator
  LINE: Before the full horror of this revelation can register on Josh’s face, he is struck against the head by a bludgeoning force (a block of wood wielded by an off-screen Hårgan). Josh collapses to make a sustained, involuntary groaning noise.
  EXPRESSION: Pain
- CHARACTER: Narrator
  LINE: A quiet moment as “Mark,” eyes invisible behind the skin mask, stares down at Josh’s twitching body.
  EXPRESSION: Null
- CHARACTER: Narrator
  LINE: Josh’s body is swiftly dragged out of frame.
  EXPRESSION: Null

::PATHS::
- CHOICE: "Continue to morning"
  TARGET: main_house_morning
  STATE_CHANGE: Josh_missing = true, Mark_missing = true
  CONDITION: null

::SCENE::
LOCATION: The Main House - Morning
MOOD: Empty
CHARACTERS: Narrator
BACKGROUND_IMAGE: main_house_morning.png
BACKGROUND_EDIT: "Morning interior of a house, Josh's and Mark's beds are empty"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Outside, the rooster crows.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: People stir awake in their beds. Josh’s bed is empty. As is Mark’s.
  EXPRESSION: null

::PATHS::
- CHOICE: "Go to breakfast"
  TARGET: farmstead_morning
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Farmstead - Morning
MOOD: Confused
CHARACTERS: Narrator, Dani, Christian, Pelle, Plump Elder
BACKGROUND_IMAGE: farmstead_morning.png
BACKGROUND_EDIT: "Morning exterior of a farmstead, breakfast time"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Breakfast time. Dani, Christian and Pelle look quizzically around.
  EXPRESSION: Quizzical
- CHARACTER: Dani
  LINE: Could Mark still be off with that girl?
  EXPRESSION: null
- CHARACTER: Pelle
  LINE: I wouldn’t be surprised.
  EXPRESSION: null
- CHARACTER: Dani
  LINE: Then what about Josh?
  EXPRESSION: null
- CHARACTER: Christian
  LINE: I’m honestly not too concerned.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The Plump Elder stands up. A hush falls cleanly over the scene.
  EXPRESSION: null
- CHARACTER: Plump Elder
  LINE: We have something regretful to announce. This morning the third book of Rubi Radr was found missing from the south house. We are not hoping to point fingers, yet we ask kindly that whoever took it, please return it to its original place. You can leave it in the south house, which will be left unguarded and unwatched. Nobody need know it was you. If it is not returned by tonight, other actions will be taken. Thank you.
  EXPRESSION: Solemn
- CHARACTER: Narrator
  LINE: He sits down and everyone uneasily resumes eating.
  EXPRESSION: Uneasy
- CHARACTER: Christian
  LINE: Fuck. Which of you is surprised?
  EXPRESSION: Under his breath
- CHARACTER: Narrator
  LINE: Later. Breakfast has ended. People leave their tables, carrying their empty plates.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Christian, Dani and Pelle stand up to see the Thin Elder and the Plump Elder walking toward them. Our group anticipates the following question:
  EXPRESSION: null
- CHARACTER: Thin Elder
  LINE: Where is your friend Josh?
  EXPRESSION: null
- CHARACTER: Christian
  LINE: I know. We have no idea.
  EXPRESSION: null
- CHARACTER: Thin Elder
  LINE: He and your other friend go disappearing on the same day. You see how it looks.
  EXPRESSION: Suspicious
- CHARACTER: Christian
  LINE: Yes, obviously, but I swear to you - we are completely in the dark on this. We are every bit as confused as you are.
  EXPRESSION: Insistent
- CHARACTER: Dani
  LINE: We did see Mark go off with one of the girls last night.
  EXPRESSION: Hesitant
- CHARACTER: Plump Elder
  LINE: What girl?
  EXPRESSION: null
- CHARACTER: Pelle
  LINE: Inga.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The Plump Elder thinks about this. Christian interjects:
  EXPRESSION: null
- CHARACTER: Christian
  LINE: But Mark wouldn’t have done this. Josh, though: he came to bed with us, and when we woke up, he was gone. And if he did take that book, I just pray you understand: we do not identify as friends of his, or collaborators, or anything. I certainly don't vouch for him and we'd be so embarrassed to be connected to this in any way.
  EXPRESSION: Dismissive
- CHARACTER: Narrator
  LINE: Beat. The Thin Elder relents.
  EXPRESSION: null
- CHARACTER: Thin Elder
  LINE: ...Let’s just hope it gets returned.
  EXPRESSION: Resigned
- CHARACTER: Christian
  LINE: Yes. I hope that very much.
  EXPRESSION: null
- CHARACTER: Pelle
  LINE: I feel responsible.
  EXPRESSION: null
- CHARACTER: Thin Elder
  LINE: Well - you and Odd can go looking for them. Maybe you can redeem this.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Pelle nods, walks to Odd, and they proceed toward the truck.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The Plump Elder turns to Dani and Christian.
  EXPRESSION: null
- CHARACTER: Plump Elder
  LINE: You’ll be going with the women for the day’s activity.
  EXPRESSION: null
- CHARACTER: Plump Elder
  LINE: And Siv asks to see you in her house.
  EXPRESSION: null
- CHARACTER: Christian
  LINE: Why?
  EXPRESSION: Nervous
- CHARACTER: Narrator
  LINE: The Elder doesn’t have the answer.
  EXPRESSION: null
- CHARACTER: Christian
  LINE: ...Which one is hers?
  EXPRESSION: null

::PATHS::
- CHOICE: "Follow Elder's instructions"
  TARGET: day_activity
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Field
MOOD: Uneasy
CHARACTERS: Narrator, Christian, Pelle, Odd, Plump Elder
BACKGROUND_IMAGE: field_day.png
BACKGROUND_EDIT: "Christian points to a small white house across a field."

::SCRIPT::
- CHARACTER: Narrator
  LINE: points to a SMALL WHITE HOUSE across the field.
  EXPRESSION: null
- CHARACTER: Christian
  LINE: nods “okay” and starts toward it. As he walks, he hears:
  EXPRESSION: null
- CHARACTER: Pelle (O.S.)
  LINE: Grandfather Sten!
  EXPRESSION: null
- CHARACTER: Odd (O.S.)
  LINE: The truck is gone!
  EXPRESSION: null
- CHARACTER: Plump Elder (O.S.)
  LINE: What?!
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Christian turns to see a distraught Pelle and Odd.
  EXPRESSION: null
- CHARACTER: Odd
  LINE: They took the truck.
  EXPRESSION: Distraught
- CHARACTER: Narrator
  LINE: Pelle stares daggers at Christian, and then turns back to Odd.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Christian, very uneasy now, proceeds to the small white house...
  EXPRESSION: Uneasy

::PATHS::
- CHOICE: "Continue to the house"
  TARGET: small_white_house
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Field
MOOD: Ritualistic
CHARACTERS: Narrator, Women, Dani, Blonde Woman
BACKGROUND_IMAGE: field_ritual.png
BACKGROUND_EDIT: "Close-up of bright yellow-green paste being mashed, a queue of women, a maypole in the background."

::SCRIPT::
- CHARACTER: Narrator
  LINE: ECU of a BRIGHT YELLOW-GREEN PASTE. It’s being MASHED vigorously in a bowl. The paste is made of ground-up flowers.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: A fat SCOOP of the paste is dropped into a LARGE JUG OF SPRING WATER (perched on a table). The paste is STIRRED into the water.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: A queue of WOMEN (between 16 and 35) has formed behind the table. One by one, the women accept a CUP of the water. They drink it (sometimes after nervous hesitation). In the b.g. is the MAYPOLE.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Dani has joined the line. The BLONDE WOMAN (whom she befriended earlier) is in front of her.
  EXPRESSION: null
- CHARACTER: Dani
  LINE: Do you know what we’re doing?
  EXPRESSION: Curious
- CHARACTER: Blonde Woman
  LINE: Oh yes. This is the big one.
  EXPRESSION: Mischievous
- CHARACTER: Narrator
  LINE: The Blonde Woman smiles mischievously. Dani smiles skeptically back. They arrive at the “water” table. Both are handed a cup.
  EXPRESSION: null
- CHARACTER: Dani
  LINE: It’s just water?
  EXPRESSION: Skeptical
- CHARACTER: Blonde Woman
  LINE: Not just. It is for the competition.
  EXPRESSION: Smiling
- CHARACTER: Narrator
  LINE: The Blonde Woman gulps hers down, and then gestures “You now.” Dani pauses, and then knocks it back.
  EXPRESSION: null
- CHARACTER: Blonde Woman
  LINE: Uh-oh.
  EXPRESSION: Smiling
- CHARACTER: Narrator
  LINE: She LAUGHS and HUGS Dani.
  EXPRESSION: null
- CHARACTER: Blonde Woman
  LINE: Here we go!
  EXPRESSION: Excited
- CHARACTER: Narrator
  LINE: Dani looks very nervous.
  EXPRESSION: Nervous

::PATHS::
- CHOICE: "Continue watching"
  TARGET: later_dance_competition
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Field (Later)
MOOD: Intense / Psychedelic
CHARACTERS: Narrator, Women, Dani, Blonde Woman, Large Woman, Musicians
BACKGROUND_IMAGE: field_dance.png
BACKGROUND_EDIT: "Three circles of women around a maypole, men, children, and older women watching. Musicians are present."

::SCRIPT::
- CHARACTER: Narrator
  LINE: LATER
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Three CIRCLES OF WOMEN have formed around the Maypole. The inside circle (of about 8 women) is surrounded by the middle circle (about 15 women), which is surrounded by the largest, outside circle (about 22 women).
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The men, children and older women have gathered on the grass to watch. The LARGE WOMAN stands with musicians (fiddler, key-harpist, and floutist).
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Dani stands in the middle circle. All the neighboring women look very excited.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Dani looks down at the earth. At first everything looks normal, but then she notices...GRASS has begun to sprout from her shoes.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Dani looks up. Fuck. She’s tripping.
  EXPRESSION: Panicked
- CHARACTER: Large Woman
  LINE: (in Swedish) It was here, long ago, that the Black One lured the youths of Hårga to the grass and seduced them into dance. Once they began, they could not stop, and they danced themselves to death. Now, in life-holding defiance of the Black One, we dance until we fall. And she who survives last will be crowned for her stamina.
  EXPRESSION: Solemn
- CHARACTER: Narrator
  LINE: The Large Woman CLAPS her hands ONCE. The musicians play a long, sustained NOTE. All of the women join hands and slowly dip to a cross-legged BOW. The musical note dies. A brief moment of SILENCE, and then...THE MUSIC BEGINS! (It is the song of Hårgas.) The women begin to DANCE. The inside circle dances to the right. The middle circle to the left. The outside circle to the right.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Dani stumbles as she finds her way into the dance. Once she hits her stride, she smiles. The Blonde Woman looks back at her and LAUGHS good-naturedly. Dani laughs back!
  EXPRESSION: Joyful

::PATHS::
- CHOICE: "Continue dancing"
  TARGET: small_white_house_interior
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Small White House - Living Room
MOOD: Cryptic
CHARACTERS: Narrator, Christian, Siv
BACKGROUND_IMAGE: small_white_house_living_room.png
BACKGROUND_EDIT: "Christian sits in a small wooden chair in an empty living room covered in runic mural art. A striking illustration of a bear being burned alive is central."

::SCRIPT::
- CHARACTER: Narrator
  LINE: INT. SMALL WHITE HOUSE - SAME TIME
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Christian sits in a small wooden chair in the empty LIVING ROOM. The walls are completely covered in RUNIC MURAL ART.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Christian lingers on a particularly striking ILLUSTRATION (painted in the wall’s center) in which a BEAR is being BURNED ALIVE before several onlookers.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: A door opens to reveal SIV.
  EXPRESSION: null
- CHARACTER: Siv
  LINE: Please. Come in.
  EXPRESSION: Welcoming
- CHARACTER: Narrator
  LINE: Christian rises to follow Siv into the other room.
  EXPRESSION: null

::PATHS::
- CHOICE: "Follow Siv"
  TARGET: small_room_conversation
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Small Room
MOOD: Tense / Conflicted
CHARACTERS: Narrator, Christian, Siv
BACKGROUND_IMAGE: small_room_conversation.png
BACKGROUND_EDIT: "A spare room with two chairs facing each other. Siv and Christian are seated."

::SCRIPT::
- CHARACTER: Narrator
  LINE: INT. SMALL ROOM - CONTINUOUS
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: A spare room. Two chairs face each other in the center. Siv takes a seat in one of them.
  EXPRESSION: null
- CHARACTER: Siv
  LINE: Please. Sit.
  EXPRESSION: Polite
- CHARACTER: Narrator
  LINE: Christian obliges.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Siv’s posture is perfect. Christian self-consciously corrects his posture. A long silence, and then:
  EXPRESSION: null
- CHARACTER: Christian
  LINE: I just need to say, I have no idea where Josh went, and I can swear to that on my mother’s life.
  EXPRESSION: Earnest
- CHARACTER: Siv
  LINE: How do you feel about Maja?
  EXPRESSION: Direct
- CHARACTER: Narrator
  LINE: Christian pauses.
  EXPRESSION: null
- CHARACTER: Christian
  LINE: About Maja?
  EXPRESSION: Confused
- CHARACTER: Narrator
  LINE: Siv’s lack of response says “yes.”
  EXPRESSION: null
- CHARACTER: Christian
  LINE: How do I feel about her how?
  EXPRESSION: Seeking clarification
- CHARACTER: Siv
  LINE: You have been approved to mate with her. You’re an ideal astrological match and she has fallen in love with you.
  EXPRESSION: Factual
- CHARACTER: Christian
  LINE: We haven’t even spoken.
  EXPRESSION: Disbelieving
- CHARACTER: Siv
  LINE: She fell in love with you before you came. Pelle showed her a photo.
  EXPRESSION: Informative
- CHARACTER: Christian
  LINE: (pause) I have someone here with me. I’m with Dani.
  EXPRESSION: Hesitant
- CHARACTER: Siv
  LINE: Dani will not know. I am not proposing marriage. You wouldn’t be approved for that.
  EXPRESSION: Clear
- CHARACTER: Christian
  LINE: So... you’re asking me to what?
  EXPRESSION: Perplexed
- CHARACTER: Siv
  LINE: I’m asking you if you care to mate with Maja. It is a one-night offer.
  EXPRESSION: Proposing
- CHARACTER: Christian
  LINE: ...She’s very beautiful.
  EXPRESSION: Admiring
- CHARACTER: Siv
  LINE: She is very beautiful.
  EXPRESSION: Agreeing
- CHARACTER: Christian
  LINE: I think I ate one of her pubic hairs.
  EXPRESSION: Disgusted
- CHARACTER: Siv
  LINE: That sounds probably right.
  EXPRESSION: Matter-of-fact
- CHARACTER: Narrator
  LINE: Beat. Christian doesn’t know what to say.
  EXPRESSION: null
- CHARACTER: Siv
  LINE: From an academic perspective, it would also serve as a unique glimpse into our sexual rites.
  EXPRESSION: Analytical
- CHARACTER: Christian
  LINE: Can I not have a unique glimpse without participating?
  EXPRESSION: Questioning
- CHARACTER: Narrator
  LINE: Siv smiles at the silly question.
  EXPRESSION: Amused
- CHARACTER: Christian
  LINE: Can I think about it?
  EXPRESSION: Pondering
- CHARACTER: Siv
  LINE: You can think about it here. Tonight is the time of alignment. Then it’s done.
  EXPRESSION: Urgent
- CHARACTER: Narrator
  LINE: A long, conflicted pause.
  EXPRESSION: null
- CHARACTER: Christian
  LINE: I don’t think I can.
  EXPRESSION: Resigned
- CHARACTER: Siv
  LINE: Okay. Is that your answer?
  EXPRESSION: Accepting
- CHARACTER: Narrator
  LINE: Christian hesitates. He’s very torn.
  EXPRESSION: Torn

::PATHS::
- CHOICE: "Refuse the offer"
  TARGET: small_white_house_exterior
  STATE_CHANGE: conflicted = false
  CONDITION: null
- CHOICE: "Accept the offer"
  TARGET: unknown
  STATE_CHANGE: conflicted = false, accepted_mate_offer = true
  CONDITION: null

::SCENE::
LOCATION: Small White House - Exterior
MOOD: Dazed / Reflective
CHARACTERS: Narrator, Christian
BACKGROUND_IMAGE: small_white_house_exterior.png
BACKGROUND_EDIT: "Christian emerges from the house in a daze, a faint smile developing as he walks towards the dance competition."

::SCRIPT::
- CHARACTER: Narrator
  LINE: EXT. SMALL WHITE HOUSE - MINUTES LATER
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Christian emerges from the house in a daze. We track back with him. His eyes are fraught as he wrestles with the moral quandary. But as he continues to walk/think, a vague SMILE sneaks onto his face.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Christian looks forward to see the DANCE COMPETITION in the distance. He’s walking toward it.
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue towards the dance"
  TARGET: field_dance_competition_later
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Field
MOOD: Frenetic / Disorienting
CHARACTERS: Narrator, Dani, Blonde Woman, Large Woman, Maja, Christian
BACKGROUND_IMAGE: field_dance_competition_later.png
BACKGROUND_EDIT: "Dani is still dancing, hallucinations are intensifying. The music stops and starts, with women being disqualified."

::SCRIPT::
- CHARACTER: Narrator
  LINE: EXT. FIELD - SAME TIME
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Dani is still engaged in the dance. It’s a dizzying spectacle, and the mounting hallucinations are clearly taking their toll on the dancers.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The music STOPS abruptly, and everyone FREEZES.
  EXPRESSION: null
- CHARACTER: Large Woman
  LINE: (in Swedish) Around!
  EXPRESSION: Authoritative
- CHARACTER: Narrator
  LINE: Everybody turns around to face the OPPOSITE DIRECTION. They switch hands, and the music RESUMES. They now dance in the opposite direction.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: One woman STUMBLES to her knees, laughing. She is now disqualified. She walks off to sit on the grass and watch.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Another WOMAN pulls out of the circle to RETCH nearby. She is also disqualified.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Dani, who was having fun, is suddenly disturbed by the retching sound. She feels sick for a second.
  EXPRESSION: Disturbed
- CHARACTER: Dani
  LINE: (thoughts turning) Josh...?
  EXPRESSION: Worried
- CHARACTER: Narrator
  LINE: The Blonde Woman turns happily to Dani.
  EXPRESSION: null
- CHARACTER: Blonde Woman
  LINE: Don’t slip!
  EXPRESSION: Encouraging
- CHARACTER: Narrator
  LINE: Dani looks to her.
  EXPRESSION: null
- CHARACTER: Blonde Woman
  LINE: Can you holding on?!
  EXPRESSION: Encouraging
- CHARACTER: Narrator
  LINE: Dani gets a second wind. She’s back.
  EXPRESSION: Determined
- CHARACTER: Narrator
  LINE: Maja, who is dancing in the outside circle, sees CHRISTIAN arriving. He joins the onlookers.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Maja decisively feigns COLLAPSE, opting out of the dance. She stumbles over to the onlookers, affecting dizziness. She glances over at Christian, smiling at him. He SMILES back. She coyly sits a few people over. The electricity between them is palpable.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The music STOPS abruptly again. All the dancers turn around, switching hands. As the music starts again, one woman TOPPLES to her side, bringing down two of her neighbors. She and one other laugh; the third woman is furious.
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue observing the dance"
  TARGET: later_fence_jumping
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Field (Later)
MOOD: Competitive / Psychedelic
CHARACTERS: Narrator, Dani, Blonde Woman, Large Woman, Women
BACKGROUND_IMAGE: field_fence_jumping.png
BACKGROUND_EDIT: "Many women have been disqualified. Dani is still in the running. Nine small fences are set up in a field."

::SCRIPT::
- CHARACTER: Narrator
  LINE: LATER
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Many of the women have now been disqualified. Dani is still in the running! She seems determined to stay alert and compete.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The music CEASES. The women STOP. Their attention is turned to a field where NINE SMALL FENCES extend one after the other.
  EXPRESSION: null
- CHARACTER: Large Woman
  LINE: (in Swedish) Nine fences jumped clean! Three ladies at a time!
  EXPRESSION: Announcing
- CHARACTER: Blonde Woman
  LINE: (to Dani, translating) Now we are jumping the nine fences. We go three and then three.
  EXPRESSION: Explaining
- CHARACTER: Dani
  LINE: What?
  EXPRESSION: Confused
- CHARACTER: Blonde Woman
  LINE: Just watch first.
  EXPRESSION: Reassuring
- CHARACTER: Narrator
  LINE: The Large Woman CLAPS once. Three women - including the Blonde Woman - walk up to form a row. Standing side-by-side, they face the nine fences.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The fiddler suddenly WAILS on his fiddle, creating an intense treble. The women all RUN forwrd.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: They JUMP over each fence and run to the next. One woman’s foot catches the third fence and she FALLS to the grass. Another women collapses over the fifth fence. The Blonde Woman makes it to the end. She happily returns, still eligible.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Another three women go. Again, only one makes it to the end.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Next up, two women line up. DANI is urged forward to join them. She looks to the women beside her. They SMILE at her.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Their smiles stretch wider (and more fluidly) than normal. The edges of their mouths elongate up their cheeks.
  EXPRESSION: Disturbing
- CHARACTER: Narrator
  LINE: The fiddle suddenly TREBLES. The women RUN.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: DANI JUMPS OVER THE FIRST FENCE. She gasps, suddenly filled with confidence. She runs to the next fence and CLEARS it. She runs faster now, to the third fence. Clears it. The fourth fence - clears it! The woman to Dani’s left suddenly BIFFS it, falling on her face. Unshaken, Dani clears the fifth fence, and then the sixth, and then the seventh, and the eighth... Dani makes it to the final (and tallest) fence. She leaps high. Her foot ALMOST connects with the top of the fence, but it PASSES OVER! She lands on her feet, triumphant. She glows with excitement.
  EXPRESSION: Triumphant
- CHARACTER: Narrator
  LINE: The other woman also made it. She walks up to Dani, HUGS her and gives her an encouraging PECK on the lips.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Dani turns to the onlookers. She sees CHRISTIAN. He isn’t paying attention. He claps absent-mindedly.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Dani’s expression CURDLES. She walks back to the maypole. Her trip is turning BAD again.
  EXPRESSION: Distressed
- CHARACTER: Narrator
  LINE: More women have lined up to jump the fences. The fiddle SHRIEKS, and they run.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Christian’s eyes go to Dani. She’s staring at him. Taken aback, he gives her a smile. She doesn’t smile back. She’s very much in the grip of the psychedelics now.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Dani’s HANDS are taken by women on e
  EXPRESSION: null

::PATHS::
- CHOICE: "Observe Dani's state"
  TARGET: end_scene
  STATE_CHANGE: dani_trip_bad = true
  CONDITION: null

::SCENE::
LOCATION: Maypole Circle
MOOD: Ritualistic
CHARACTERS: Dani, Seven Women, Christian, Ulla, Skinny Woman, Short Woman, Blonde Woman, Plump Woman, Large Woman
BACKGROUND_IMAGE: maypole_circle.png
BACKGROUND_EDIT: "A circle of women dancing around a maypole. Christian sits among onlookers."

::SCRIPT::
- CHARACTER: Narrator
  LINE: ither side of her. Confused, she looks around to see that she is now part of a more modest circle surrounding the maypole. Only SEVEN women remain. The music STARTS and they commence dancing.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: MEANWHILE, Christian sits among the onlookers. He’s sneaking obsessive glances at Maja. Suddenly, he notices ULLA (whom he met earlier) walking toward him. She arrives at his feet, holding out the CUP of the flower-spiked water.
  EXPRESSION: null
- CHARACTER: ULLA
  LINE: For you.
  EXPRESSION: null
- CHARACTER: CHRISTIAN
  LINE: What is it?
  EXPRESSION: null
- CHARACTER: ULLA
  LINE: Spring water with special properties.
  EXPRESSION: null
- CHARACTER: CHRISTIAN
  LINE: What’s it do?
  EXPRESSION: Skeptical
- CHARACTER: ULLA
  LINE: Breaks down your defenses and opens you for the influence.
  EXPRESSION: null
- CHARACTER: CHRISTIAN
  LINE: ...I’m worried I’ll have a bad trip.
  EXPRESSION: Worried
- CHARACTER: Narrator
  LINE: Christian looks back to Maja. She’s now looking directly at him. Her eyes are languid, confident. She doesn’t break the gaze.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Christian turns to Ulla, and accepts the water. He sips it. Sips it again. KNOCKS it back.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Settling into the idea that he’s now going to hallucinate, Christian looks back to the MAYPOLE. The women are still dancing in a circle.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: IN THE DANCING CIRCLE, Dani’s eyes betray a rising panic.
  EXPRESSION: null
- CHARACTER: SKINNY WOMAN
  LINE: If we stop, will everything keep spinning?
  EXPRESSION: Provocative
  DIALOGUE_LANGUAGE: Swedish
- CHARACTER: SHORT WOMAN
  LINE: What if we looked down and there were centipedes everywhere?
  EXPRESSION: Laughing
  DIALOGUE_LANGUAGE: Swedish
- CHARACTER: Narrator
  LINE: The Short Woman laughs, and then looks down. As imagined, she sees the ground as a squirming BLANKET OF CENTIPEDES. She SCREAMS in horror, desperately FLEEING the circle. Another woman has looked down to see the same thing. She SCREAMS too, and runs off.
  EXPRESSION: null
- CHARACTER: Dani
  LINE: There’s nothing there.
  EXPRESSION: Panicked
- CHARACTER: Narrator
  LINE: Dani looks up. She laughs with relief, still confused.
  EXPRESSION: null
- CHARACTER: BLONDE WOMAN
  LINE: That’s right! Hold on to your brain!
  EXPRESSION: Smiling
- CHARACTER: Narrator
  LINE: Now there are only five women dancing.
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue dancing"
  TARGET: time_lapse_dancing
  STATE_CHANGE: none
  CONDITION: null

::SCENE::
LOCATION: Maypole Circle (Time Lapse)
MOOD: Competitive
CHARACTERS: Dani, Blonde Woman, Plump Woman, Two Other Women
BACKGROUND_IMAGE: maypole_circle_time_lapse.png
BACKGROUND_EDIT: "Time lapse of women dancing, shadows moving across grass. Two women fall out."

::SCRIPT::
- CHARACTER: Narrator
  LINE: TIME-LAPSE. The shadows of the dancing women crawl across the grass, moving in accordance with the drifting sun. Two women FALL (to be disqualified) over the course of this time lapse.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Now, only Dani and two other women are in the running. One of these is the Blonde Woman. The other is a good-natured Plump Woman. They each dance separately, no longer holding hands. The Plump Woman’s legs are clearly less stable than Dani’s or the Blonde Woman’s, and she is tired and stumbling. Competition has been growing in Dani. She’s so close to winning that she can now taste it.
  EXPRESSION: null
- CHARACTER: BLONDE WOMAN
  LINE: Are you tired?!
  EXPRESSION: Smiling
  DIALOGUE_LANGUAGE: Swedish
- CHARACTER: DANI
  LINE: I don’t speak Swedish!
  EXPRESSION: Determined
- CHARACTER: BLONDE WOMAN
  LINE: What?!
  EXPRESSION: Confused
- CHARACTER: DANI
  LINE: Aewobeemeewish!
  EXPRESSION: null
- CHARACTER: BLONDE WOMAN
  LINE: Waweroobeeny!
  EXPRESSION: null
- CHARACTER: DANI
  LINE: Aewabeeny-sa-aewonnerstabloo!
  EXPRESSION: Amazed
- CHARACTER: Narrator
  LINE: They are speaking complete gibberish, but they understand each other perfectly. Dani is amazed.
  EXPRESSION: null
- CHARACTER: DANI
  LINE: Weerabbleeishcobleraymib!
  EXPRESSION: Excited
- CHARACTER: BLONDE WOMAN
  LINE: Blorishcobleraymib-wonnerstablee!
  EXPRESSION: Agreeing
- CHARACTER: Narrator
  LINE: The Plump Woman suddenly TRIPS over one foot to fall CRASHING to the ground. The Blonde Woman (still facing Dani) TRIPS over the Plump Woman. She COLLAPSES, laughing merrily on the way down.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Dani dances past the fallen women. She doesn’t immediately realize that she’s just won the competition. She still looks determined as she continues dancing manically around the maypole.
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue dancing around maypole"
  TARGET: post_competition_maypole
  STATE_CHANGE: competition_won = true
  CONDITION: null

::SCENE::
LOCATION: Maypole Area (Post-Competition)
MOOD: Celebratory/Confused
CHARACTERS: Dani, Cheering Women, Large Woman, Children
BACKGROUND_IMAGE: maypole_area_celebration.png
BACKGROUND_EDIT: "Women congratulating Dani. Rose petals being fired."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Cheering women rush over to congratulate Dani, but she KEEPS DANCING in the circle, afraid that it’s a trick.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The women tug excitedly at Dani’s arms. They embrace her. Dani decelerates, but does not cease dancing. Finally, enough women have enfolded her. Her dancing feet slow to a confused halt.
  EXPRESSION: null
- CHARACTER: LARGE WOMAN
  LINE: We have our May Queen!!
  EXPRESSION: Joyful
  DIALOGUE_LANGUAGE: Swedish
- CHARACTER: Narrator
  LINE: The LARGE WOMAN approaches with an immense, gorgeously crafted GARLAND CROWN. She lays it on Dani’s head.
  EXPRESSION: null
- CHARACTER: DANI
  LINE: It’s over?
  EXPRESSION: Hallucinating
- CHARACTER: LARGE WOMAN
  LINE: You are our May Queen.
  EXPRESSION:null
- CHARACTER: DANI
  LINE: Why? Me?
  EXPRESSION: Confused
- CHARACTER: LARGE WOMAN
  LINE: You!
  EXPRESSION:null
- CHARACTER: DANI
  LINE: What do you mean?!
  EXPRESSION: Scared
- CHARACTER: Narrator
  LINE: ROSE PETALS are fired out of small air cannons by children. The petals rain down on Dani and the surrounding Hårgans.
  EXPRESSION: null

::PATHS::
- CHOICE: "Be led aside"
  TARGET: photograph_station
  STATE_CHANGE: none
  CONDITION: null

::SCENE::
LOCATION: Field Viewpoint
MOOD: Disoriented
CHARACTERS: Dani, Women, Man with Camera, Christian, Pelle
BACKGROUND_IMAGE: field_viewpoint.png
BACKGROUND_EDIT: "Dani being led aside, Man taking photograph, Christian watching."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Dani, severely disoriented, is led aside by several women. One woman wraps her in a sort of scarf (composed only of greenery and flora), and then she is directed to stand before a gorgeous view of the field. Her distracted attention is pointed to a MAN holding a large, old FILM CAMERA. He takes Dani’s PHOTOGRAPH.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Dani looks for Christian, who stands among the Hårgans with a baffled expression. Dani alights on him.
  EXPRESSION: null
- CHARACTER: DANI
  LINE: What’s happening?!
  EXPRESSION: Desperate
- CHARACTER: Narrator
  LINE: But Christian doesn’t understand it himself. He shakes his head to say “I don’t know!”
  EXPRESSION: null
- CHARACTER: DANI
  LINE: What does this mean? What do I have to do?
  EXPRESSION: Pleadingly
- CHARACTER: Narrator
  LINE: The women answer with hugs, warm smiles, and kisses on the cheek. Their faces morph subtly (a product of the psychedelics). Among the people who kiss her are her MOTHER and FATHER and SISTER (Terri). She looks back for them, but they have disappeared. A figment of her imagination?
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Caught in the hallucination, Dani falls into a traumatized daze.
  EXPRESSION: null
- CHARACTER: PELLE
  LINE: Holy cow, you won! May Queen!
  EXPRESSION: Enthusiastic
- CHARACTER: Narrator
  LINE: He gives her a blunt KISS on the lips. Before she can react, Pelle is replaced by two new women, also kissing and hugging her.
  EXPRESSION: null

::PATHS::
- CHOICE: "Be placed on the sun plank"
  TARGET: sun_plank_hoist
  STATE_CHANGE: none
  CONDITION: null

::SCENE::
LOCATION: Field
MOOD: Exhilarating/Conflicted
CHARACTERS: Dani, Blonde Woman, Eight Men, Crowd, Christian, Maja, Ulla
BACKGROUND_IMAGE: field_sun_plank.png
BACKGROUND_EDIT: "Dani on a sun-shaped plank being hoisted by men. Crowd singing. Christian lagging behind."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Dani is then led to a ROUND WOODEN PLANK (painted gold and shaped like a cartoon SUN) with eight long, protruding handles. She is directed to STAND on it.
  EXPRESSION: null
- CHARACTER: BLONDE WOMAN
  LINE: Careful!
  EXPRESSION:null
- CHARACTER: Narrator
  LINE: The handles are gripped by eight men, and Dani is swiftly HOISTED UP. She almost falls, but doesn’t. She is elevated five feet above the ground as the crowd erupts into mirthful SONG.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The song persists as Dani, still on her pedestal, is carried across the field. All eyes are on her. Everyone follows her.
  EXPRESSION: null
- CHARACTER: DANI
  LINE: Christian?!
  EXPRESSION: Searching
- CHARACTER: Narrator
  LINE: But Christian has lagged to the back of the crowd. He looks extremely conflicted. His eyes move to Maja, whose eyes are TRAINED on him. She smiles widely, but her eyes are faded. Christian slows to a stop as the procession continues. Ulla runs back to fetch him. She takes his hand and pulls him back toward the crowd.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Meanwhile, Dani’s confusion and fear is beginning to subside. She looks down at the procession to see that these people are indeed celebrating her. A few women even persist in throwing rose petals up at her.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Dani, now calm, looks down to see that her FEET and LEGS have assumed the GOLD color of the plank (like a chameleon).
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue being carried"
  TARGET: dining_area_arrival
  STATE_CHANGE: none
  CONDITION: null

::SCENE::
LOCATION: Dining Area
MOOD: Ceremonial/Mysterious
CHARACTERS: Dani, Crowd, Servers, Christian, Large Man, Plump Elder
BACKGROUND_IMAGE: dining_area_throne.png
BACKGROUND_EDIT: "Lush field with long tables. A throne-like chair at the head. Dani's pedestal arrives."

::SCRIPT::
- CHARACTER: Narrator
  LINE: The crowd arrives at today’s DINING AREA. In a LUSH FIELD, the tables are all queued up to form a long, straight line. At the head of the table is a HUGE CHAIR (more like a throne) adorned in lush greenery and bright flora.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Dani’s pedestal is set down. Members of the crowd step aside to create a PATH for Dani’s trajectory (toward the throne). Dani takes a moment before stepping decisively onto the GRASS.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: When Dani’s FOOT touches the grass, small SUMMER FLOWERS magically SPROUT UP around her foot. Her next step is the same. Flowers emerge, impossibly, from the soil. She continues to walk forward, having now assumed a more self-possessed posture. Confidence is rising in her, and with every step, more flowers sprout up. She’s leaving a beautiful trail of wild flowers in her wake.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Dani STOPS at the throne. Everyone now finds their way to their seats, but no one sits. They look to her. She looks momentarily confused, but then understands. She SITS. Now everyone may sit.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Dani admires her green throne. The greenery/flora subtly SWELLS and DEFLATES (as we saw before, with the mushroom trip).
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: SERVERS appear with plates. Dani is the first person to receive food and drink. Her tableware is much finer than the rest.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Before long, everyone has food in front of them. They sit with their hands on their laps, present. They WAIT for Dani.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Dani picks up her FORK. She looks back to the rest of the table. They all look back at her with patience. She then looks down and PIERCES her food with the fork. (The sound of the piercing is heightened.) Dani takes a BITE. Now everyone may begin eating.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Dani looks down the length of the extended table. She alights on CHRISTIAN, who isn’t eating. He looks very disturbed, clearly suffering a bad trip. He looks in Dani’s direction.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: They LOCK EYES, but communicate nothing to each other. They are both lost in confusion, but they don’t share in this. If anything, they look SCARED of each other.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: This moment is broken by a SERVER arriving at Dani’s side. He presents her with a baby SALT HERRING. The community sees this and laughs, knowing what’s in store.
  EXPRESSION: null
- CHARACTER: DANI
  LINE: For what?
  EXPRESSION: Frightened
- CHARACTER: PLUMP ELDER
  LINE: You must eat it whole, but the tail going first.
  EXPRESSION: Chuckling
- CHARACTER: DANI
  LINE: What? I can’t. That’s too big.
  EXPRESSION: Sincere
- CHARACTER: PLUMP ELDER
  LINE: No no - you must try.
  EXPRESSION:null
- CHARACTER: CHRISTIAN
  LINE: How much is happening right now?
  EXPRESSION: Tripping heavily
- CHARACTER: Narrator
  LINE: Inexplicably, the Large Man CLAPS in Christian’s face. This sends Christian on an intense downward spiral.
  EXPRESSION: null
- CHARACTER: CHRISTIAN
  LINE: Why did you do that?
  EXPRESSION: Almost inaudible
- CHARACTER: Narrator
  LINE: The Large Man’s attention is now on Dani, whose head is tilted back as she tries to eat the herring whole (tail first). The Plump Elder holds it above her, feeding it into her mouth.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Dani takes half of the herring into her mouth, starts to
  EXPRESSION: null

::PATHS::
- CHOICE: "Attempt to eat herring"
  TARGET: herring_outcome
  STATE_CHANGE: none
  CONDITION: null

::SCENE::
LOCATION: Dining Hall
MOOD: Tense Celebration
CHARACTERS: Dani, Plump Elder, Blonde Woman, Different Hargans, Large Woman, Thin Elder, Hårgan Woman
BACKGROUND_IMAGE: dining_hall.png
BACKGROUND_EDIT: "A communal dining hall, festive atmosphere, focus on Dani"

::SCRIPT::
- CHARACTER: Narrator
  LINE: chew, and then coughs out the rest. This elicits ecstatic APPLAUSE.
  EXPRESSION: null
- CHARACTER: Dani
  LINE: lets out a childlike LAUGH.
  EXPRESSION: Happy
- CHARACTER: Plump Elder
  LINE: A word from the May Queen!
  EXPRESSION: Excited
- CHARACTER: Blonde Woman
  LINE: Yes! Speech!
  EXPRESSION: Excited
- CHARACTER: Different Hargans
  LINE: Speech!
  EXPRESSION: Excited
- CHARACTER: Large Woman
  LINE: Stand! Stand!
  EXPRESSION: Excited
- CHARACTER: Narrator
  LINE: Dani is urged to stand up. She does so, clearly hallucinating intensely. The silence hangs heavily.
  EXPRESSION: null
- CHARACTER: Dani
  LINE: ...I don’t know if this is real, or what’s happening - but...thank you.
  EXPRESSION: Distressed
- CHARACTER: Narrator
  LINE: Dani lets this hang, and then sits back down. Brief, awkward pause, and then:
  EXPRESSION: null
- CHARACTER: Thin Elder
  LINE: To the May Queen! Skål!!
  EXPRESSION: Joyful
- CHARACTER: Narrator
  LINE: Everyone drinks to that. One Hårgan Woman turns to Dani to excitedly says:
  EXPRESSION: null
- CHARACTER: Hårgan Woman
  LINE: You are the family now! Yes?
  EXPRESSION: Manic
- CHARACTER: Narrator
  LINE: Dani nods, unsure. The woman nods manically.
  EXPRESSION: null
- CHARACTER: Hårgan Woman
  LINE: Yes! Yes! You are the family!
  EXPRESSION: Manic
- CHARACTER: Narrator
  LINE: The Woman rubs Dani’s arm, smiling warmly (and aggressively).
  EXPRESSION: null

::PATHS::
- CHOICE: "Observe the unfolding events"
  TARGET: ongoing_feast
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Dining Hall
MOOD: Observational
CHARACTERS: Pelle, Christian, Maja, Siv
BACKGROUND_IMAGE: dining_hall_observational.png
BACKGROUND_EDIT: "Focus shifts to other characters at the table"

::SCRIPT::
- CHARACTER: Narrator
  LINE: PELLE, we reveal, is composing a drawing of Dani in her throne.
  EXPRESSION: null
- CHARACTER: Christian
  LINE: expression is SOUR.
  EXPRESSION: Angry
- CHARACTER: Narrator
  LINE: He turns to notice that MAJA is looking at him. Taken aback, Christian’s expression slowly SOFTENS (in a slack-jawed, lust-stricken way). Maja is clearly “in heat.” Holding Christian’s gaze, she RISES from her seat (as if in slow-motion) and begins to walk sensually off. Christian watches her go. She passes SIV, whose eyes are also trained on Christian.
  EXPRESSION: null
- CHARACTER: Maja
  LINE: continue toward the TEMPLE, glancing back at Christian to confirm that he’s still watching her. DANI notices this, despite the fact that everyone is competing for her attention.
  EXPRESSION: null
- CHARACTER: Dani
  LINE: looks to Christian. He stares dumbly at the table, lost in conflict.
  EXPRESSION: Conflicted

::PATHS::
- CHOICE: "Continue watching"
  TARGET: ceremony_prep
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Dining Hall / Temple Approach
MOOD: Ritualistic Preparation
CHARACTERS: Siv, Dani, Girls, Man (in lady's clothing), Traditionally Dressed Man
BACKGROUND_IMAGE: ceremony_prep.png
BACKGROUND_EDIT: "Transition from dining hall to the carriage area, torches are present"

::SCRIPT::
- CHARACTER: Narrator
  LINE: MINUTES LATER. Everyone is finished. Siv RISES. All eyes go respectfully to her.
  EXPRESSION: null
- CHARACTER: Siv
  LINE: Now it is traditional for the May Queen to bless our crops and livestock. And after the luck you just inherited from that salt herring, we should all be doubly encouraged.
  EXPRESSION: Solemn
- CHARACTER: Narrator
  LINE: Polite laughter all around.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Siv gestures in the direction of a CARRIAGE, just beyond the tables. Its roof sports THREE UNLIT TORCHES.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Three GIRLS scatter flowers to create a PATH between Dani and the carriage. Dani RISES. Everyone else stands up, too.
  EXPRESSION: null
- CHARACTER: Dani
  LINE: Can Christian come with me?
  EXPRESSION: Hopeful
- CHARACTER: Siv
  LINE: No. The Queen must ride alone.
  EXPRESSION: Firm
- CHARACTER: Narrator
  LINE: Dani pauses to accept this. She steps onto the floral path and approaches the carriage. On the way, one MAN (dressed in lady’s clothing) offers her a LONG, FLAMING STICK. Dani accepts it. The man motions to the carriage’s unlit torches.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Dani walks to the carriage, extends the stick’s flame toward the torches, and sets them each AFIRE.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The man takes the stick back from Dani, and gestures for her to enter the carriage. A TRADITIONALLY DRESSED MAN stands beside the carriage door. He hands Dani a VIAL OF HOLY SPRING WATER, and offers Dani his hand (for support) as she contemplates entering.
  EXPRESSION: null
- CHARACTER: Traditionally Dressed Man
  LINE: Your majesty.
  EXPRESSION: Deferential
- CHARACTER: Narrator
  LINE: Dani accepts his supportive hand as she climbs into the carriage.
  EXPRESSION: null

::PATHS::
- CHOICE: "Enter the carriage"
  TARGET: inside_carriage
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Inside Carriage
MOOD: Moving
CHARACTERS: Dani, Young Women, Red-Haired Woman
BACKGROUND_IMAGE: inside_carriage.png
BACKGROUND_EDIT: "Interior of a carriage, view of the outside"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Dani takes a seat.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Outside, several YOUNG WOMEN (including the RED-HAIRED WOMAN) have gathered in front of the carriage. They each take hold of RODS, prepared to pull the carriage.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: A few other women have gathered to the sides of the carriage. They hold juniper boughs and unlit torches. One girl goes around, IGNITING their torches.
  EXPRESSION: null

::PATHS::
- CHOICE: "Be pulled through the fields"
  TARGET: field_journey
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Field
MOOD: Observational / Transition
CHARACTERS: Community, Christian, Siv
BACKGROUND_IMAGE: field.png
BACKGROUND_EDIT: "Exterior field, community members watching the carriage"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Most of the community remains standing at the dining tables. They WATCH as the women pull the carriage away.
  EXPRESSION: null
- CHARACTER: Christian
  LINE: watches, too. Guilt-ridden. He looks to SIV. She looks unblinkingly back.
  EXPRESSION: Guilt-ridden

::PATHS::
- CHOICE: "Observe Christian's reaction"
  TARGET: christian_transition
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Inside Carriage (Moving)
MOOD: Mystical Journey
CHARACTERS: Dani, Women with torches
BACKGROUND_IMAGE: inside_carriage_moving.png
BACKGROUND_EDIT: "Interior of a carriage, moving through wheat fields, torches waving"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Dani looks out the window as the carriage is pulled through the WHEAT FIELDS. The accompanying women WAVE their torches about, casting away dark spirits.
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue the journey"
  TARGET: field_path_to_temple
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Field
MOOD: Solemn Procession
CHARACTERS: Girl, Christian
BACKGROUND_IMAGE: field_procession.png
BACKGROUND_EDIT: "A new path of flowers is created leading to the temple"

::SCRIPT::
- CHARACTER: Narrator
  LINE: A GIRL begins scattering flowers to create a NEW PATH. This is between Christian and the TEMPLE. All eyes are now on him.
  EXPRESSION: null
- CHARACTER: Christian
  LINE: frozen for a moment, RISES. He takes one abrupt step forward, and then continues warily toward the Temple.
  EXPRESSION: Hesitant

::PATHS::
- CHOICE: "Proceed to the Temple"
  TARGET: inside_temple_foyer
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Temple Foyer
MOOD: Ritualistic Preparation
CHARACTERS: Christian, Bearded Man in Dress
BACKGROUND_IMAGE: temple_foyer.png
BACKGROUND_EDIT: "Entrance of the temple, waiting figure"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Christian enters the foyer of the temple. The temple doors are closed. A BEARDED MAN IN A DRESS stands in waiting. He hands Christian a WHITE GOWN.
  EXPRESSION: null
- CHARACTER: Bearded Man in Dress
  LINE: Put this.
  EXPRESSION: Direct
- CHARACTER: Narrator
  LINE: The man gestures to a MODESTY PANEL in the corner (behind which Christian can disrobe).
  EXPRESSION: null

::PATHS::
- CHOICE: "Change into the gown"
  TARGET: christian_changing
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Field
MOOD: Agricultural Blessing
CHARACTERS: Young Women, Red-Haired Woman, Dani
BACKGROUND_IMAGE: field_blessing.png
BACKGROUND_EDIT: "A hole in the ground, Dani performing a ritual with offerings"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The women pulling the carriage have slowed to a STOP. Dani is directed by the Red-Haired Woman to step out. She is handed a flaming torch, and led to a small HOLE in the ground.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Dani is handed a sack of GRAIN, a raw STEAK, and an EGG. She is directed to pour the grain into the hole, which she does, and then to drop the steak over the grain. She does this, too. She is then instructed to crack the egg and pour its contents into the hole.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The Red-Haired Woman now affects perfect posture. Dani instinctively mimics this.
  EXPRESSION: null
- CHARACTER: Red-Haired Woman
  LINE: Repeat now after me.
  EXPRESSION: Focused
- CHARACTER: Narrator
  LINE: Dani and the Red-Haired Woman are looking directly into each other’s eyes. The Red-Haired Woman begins to SING very slowly, enunciating very carefully, and Dani SINGS ALONG (quite well):
  EXPRESSION: null
- CHARACTER: Red-Haired Woman
  LINE: Vakna upp, vakna upp, både åker och äng Nu har du sovit länge i din säng Nu är det över med snö och med regn Nu har sommarnatten kommit.
  EXPRESSION: Singing
- CHARACTER: Narrator
  LINE: The Red-Haired Woman is impressed. As are the onlooking young women. The hole is COVERED UP with soil.
  EXPRESSION: null

::PATHS::
- CHOICE: "Observe the completion of the ritual"
  TARGET: temple_foyer_steam
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Temple Foyer
MOOD: Altered State
CHARACTERS: Christian, Bearded Man in Dress
BACKGROUND_IMAGE: temple_foyer_steam.png
BACKGROUND_EDIT: "Christian in a white gown, receiving vapors from a stone pot"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Christian has changed into the WHITE GOWN. He steps nervously out from behind the modesty panel.
  EXPRESSION: null
- CHARACTER: Christian
  LINE: What now?
  EXPRESSION: Nervous
- CHARACTER: Bearded Man in Dress
  LINE: Holds up a STONE POT. He lifts off the lid to release a WAVE OF STEAM. Breathe in.
  EXPRESSION: Neutral
- CHARACTER: Christian
  LINE: What does it do?
  EXPRESSION: Curious
- CHARACTER: Bearded Man in Dress
  LINE: For your vitality.
  EXPRESSION: Grave
- CHARACTER: Narrator
  LINE: Christian BREATHES IN the vapors. His eyes begin to cloud. He EXHALES heavily. He’s already feeling the effects. His breathing becomes shallow.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The Bearded Man now OPENS THE DOORS to the temple.
  EXPRESSION: null

::PATHS::
- CHOICE: "Enter the inner temple"
  TARGET: inside_temple_maja
  STATE_CHANGE: hallucination_level = +2
  CONDITION: null

::SCENE::
LOCATION: Temple Interior
MOOD: Erotic Ritual
CHARACTERS: Christian, Maja, Older Women
BACKGROUND_IMAGE: temple_interior_maja.png
BACKGROUND_EDIT: "Dark temple interior, Maja lying nude on twigs and flowers, surrounded by nude older women"

::SCRIPT::
- CHARACTER: Narrator
  LINE: It is dark, save for several burning candles. In the center of the room, lying on a bed of freshly cut birch twigs and WILD FLOWERS, is MAJA. She is NUDE, lying on her back, legs together.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Several OLDER WOMEN, mostly in their 30s and 40s (a few in their 50s and 60s), stand at the back of the room. They are also NUDE.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Christian is too stoned to react. He regards the room as he would a dreamscape.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Ceremonial MUSIC begins. A few women, reading from the Rubi Radr, SING in the Hårgas’ wordless, groaning, microtonal tradition.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: One Woman steps up to draw Christian’s gown OFF of his shoulders. He is fluidly DISROBED. Now standing naked (and erect), he is directed towards Maja, who waits nervously.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Christian seems to LEVITATE half-an-inch off the ground and then FLOATS gently across the room (clearly a product of the escalating hallucination). As he approaches Maja, the singing intensifies. Maja’s LEGS timidly PART. Christian, now standing at her feet, looks down at her. Her eyes are closed as she waits to be taken.
  EXPRESSION: null

::PATHS::
- CHOICE: "Approach Maja"
  TARGET: temple_lovemaking
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Cattle House
MOOD: Blessing of Livestock
CHARACTERS: Dani, Red-Haired Woman
BACKGROUND_IMAGE: cattle_house.png
BACKGROUND_EDIT: "Exterior of a cattle house, Dani holding a torch"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The sun is less intense now. It is nearing twilight. The carriage has pulled up to the cattle house. Dani, holding a torch, proceeds to bless the livestock (according to the Red-Haired Woman’s instructions).
  EXPRESSION: null

::PATHS::
- CHOICE: "Observe the blessing"
  TARGET: temple_lovemaking_cont
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Temple Interior
MOOD: Intimate Union
CHARACTERS: Christian, Maja, Older Women
BACKGROUND_IMAGE: temple_lovemaking.png
BACKGROUND_EDIT: "Christian and Maja making love, surrounded by watchful women"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Christian has descended to his knees. He sits between Maja’s legs, preparing himself. He looks extremely intoxicated.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Maja’s eyes are squeezed shut as she anticipates what’s coming.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Christian awkwardly leans down to gently KISS her lips. Without opening her eyes, she kisses back - slowly, sensually. The singing rises and falls (out of harmony) with trembling impatience.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Christian gently presses himself into Maja. Her mouth opens in anticipation. He ENTERS her. Overwhelmed, Maja digs her nails into his back. Her eyes well with tears. Christian looks unsettled, but he continues...
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Christian is now MAKING LOVE to Maja, very slowly - almost robotically. She lies motionless, mouth agape. She doesn’t move a muscle, nor does she make a sound, but her expression is one of total, paralyzed ECSTASY. The singing has now HARMONIZED.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The Older Women watch this with rapt attention. They are clearly aroused. The lovemaking is dreamily slow. The singing rises steadily. Delayed percussion accompanies each heavy, lagging THRUST.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Maja looks back at one of the WOMEN (50s). The woman smiles tenderly at her. This would be touching if it weren’t so weird.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Maja offers the woman her HAND, and the woman supportively takes it into her hands. The woman lovingly presses her CHEEK against Maja’s open palm, CARESSING her face.
  EXPRESSION: null

::PATHS::
- CHOICE: "Witness the culmination"
  TARGET: farmstead_return
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Farmstead
MOOD: Uneasy Return
CHARACTERS: Dani, Red-Haired Woman, Young Women
BACKGROUND_IMAGE: farmstead_return.png
BACKGROUND_EDIT: "Carriage has returned to the farmstead, Dani is still under influence"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The carriage has returned to the farmstead. Dani steps uneasily out of the wagon, still under the warping influence of the hallucinogen. The SINGING is heard faintly from the Temple.
  EXPRESSION: null
- CHARACTER: Red-Haired Woman
  LINE: We shall go now to Siv’s house.
  EXPRESSION: Directive
- CHARACTER: Dani
  LINE: What’s there?
  EXPRESSION: Questioning
- CHARACTER: Red-Haired Woman
  LINE: It is a special meeting, only for the Queens. She will bless you.
  EXPRESSION: Solemn
- CHARACTER: Narrator
  LINE: The distant singing persists. Dani looks to the Temple. She seems DRAWN to it.
  EXPRESSION: null
- CHARACTER: Dani
  LINE: What about there?
  EXPRESSION: Inquisitive
- CHARACTER: Red-Haired Woman
  LINE: Not for us.
  EXPRESSION: Firm
- CHARACTER: Narrator
  LINE: Dani, attracted by the singing, takes a few steps toward the Temple. The young women look very concerned. The Red-Haired Woman steps up to STAND IN DANI’S WAY.
  EXPRESSION: null
- CHARACTER: Red-Haired Woman
  LINE: I think you should not.
  EXPRESSION: Concerned
- CHARACTER: Dani
  LINE: ...Why?
  EXPRESSION: Inquisitive
- CHARACTER: Narrator
  LINE: The Red-Headed Woman is not convincing when she says:
  EXPRESSION: null
- CHARACTER: Red-Haired Woman
  LINE: It is a ceremony for the men.
  EXPRESSION: Unconvincing
- CHARACTER: Narrator
  LINE: Dani is now ve
  EXPRESSION: null

::PATHS::
- CHOICE: "Be deterred from the Temple"
  TARGET: sivs_house_approach
  STATE_CHANGE: suspicion = +1
  CONDITION: null
- CHOICE: "Persist towards the Temple"
  TARGET: temple_beckoning
  STATE_CHANGE: defiance = +1, danger = +1
  CONDITION: null





::SCENE::
LOCATION: Unknown
MOOD: Solemn
CHARACTERS: Narrator, Plump Elder, Ball Man, Dag, Christian Hughes, Dani
BACKGROUND_IMAGE: null
BACKGROUND_EDIT: "Interior, ceremonial setting"

::SCRIPT::
- CHARACTER: Narrator
  LINE: It's traditional that our Queen, in all her fairness and wisdom, shall choose between a pre-selected newblood and a specially ordained Hårgan...
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The Plump Elder turns to a Man standing beside a large BALL CAGE (as generally used in bingo). The cage holds about a hundred WOODEN BALLS (the size of ping-pong balls) with a different RUNIC NAME carved into each.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The Man rotates the ball cage, which then dispenses a single BALL. The man holds up the ball and reads the name aloud:
  EXPRESSION: null
- CHARACTER: BALL MAN
  LINE: Dag.
  EXPRESSION: null
- CHARACTER: PLUMP ELDER
  LINE: Honorable Dag! Please step forward.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: DAG, a man in his late 50s, looks like he just won the lottery. He takes a step forward, beaming with pride.
  EXPRESSION: null
- CHARACTER: PLUMP ELDER
  LINE: And Christian Hughes...
  EXPRESSION: null
- CHARACTER: PLUMP ELDER
  LINE: (to Dani)
  These are your candidates for the ninth and final offering. We patiently await your verdict.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Christian tries to scream, but this only results in muffled moans. His eyes BEG Dani for mercy. Her eyes are GLASS.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The community waits as Dani makes her silent deliberation.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Dani’s EYES settle fixedly on CHRISTIAN. A wave of intense EMOTION suddenly animates Dani’s face. Sadness, anger, love, heartbreak... These feelings are finally wrestled down, and her expression becomes BLANK again. Her EYES, still trained on Christian, have HARDENED. They narrow pointedly to suggest that she’s made her decision. The Plump Elder understands.
  EXPRESSION: null
- CHARACTER: PLUMP ELDER
  LINE: (to the crowd)
  155. The honor has been bestowed on Christian Hughes, our ninth and most sacred offering!
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Christian’s muffled screams now become hysterical. Dani’s gaze remains steely and absent.
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue to the next scene"
  TARGET: field_evening
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Field
MOOD: Grim
CHARACTERS: Narrator, Connie, Hårgan, Mark, other corpses
BACKGROUND_IMAGE: field.png
BACKGROUND_EDIT: "Evening, grass, a sacred house"

::SCRIPT::
- CHARACTER: Narrator
  LINE: CU of a WHEEL rolling across the grass. Tracking alongside this, we tilt up to reveal that it belongs to a WHEELBARROW. Lying in the wheelbarrow is CONNIE’S CORPSE. It is soaking wet and its flesh is grossly distended (from being left underwater). She is wearing the same outfit (of greenery and jewels) that was used earlier for the sacrificial tree (which was fed to the river).
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Continuing to track alongside the wheelbarrow (which is pushed by a young male Hårgan), we pull back to EXPAND OUR VIEW. We reveal that the Hårgan is carting Connie’s corpse toward the yellow-painted SACRED HOUSE, which was previously off-limits. It stands in the center of an open field. Its door is now OPEN.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: We settle on a static wide of this until a NEW CART is pushed into frame. We now follow this cart, keeping it centered in frame. This cart holds MARK’S “CORPSE.” In fact, it is just his hollowed out SKIN - stuffed with straw and hay.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Peripherally, other bodies are being carted toward the house.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: We continue to track ahead, following Mark’s cart INTO the SACRED HOUSE...
  EXPRESSION: null

::PATHS::
- CHOICE: "Enter the Sacred House"
  TARGET: sacred_house_interior
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Sacred House (Interior)
MOOD: Macabre
CHARACTERS: Narrator, Connie, Mark, Simon, Elderly Man's Son, Doctor, Other Elderly Man
BACKGROUND_IMAGE: sacred_house_interior.png
BACKGROUND_EDIT: "Interior, adorned in greenery, central platform"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The interior is completely adorned in greenery. An impossibly lush mausoleum. In the center is a PLATFORM made of hay.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Connie’s corpse is rested in one corner. Mark’s is placed in the next corner. Simon’s body is placed in between them.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: In the following corner is the corpse of one of the ELDERLY MEN who jumped off the cliff. He is surrounded by his most precious belongings (jewelry, books, etc.). His SON (40s) is overseeing the removal of one of his father’s EYEBALLS by the DOCTOR.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The doctor has effectively drawn the corpse’s eyeball from its socket. He hands the eyeball to the son.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The doctor then moves to the body of the other elderly man who leapt to his death. He is also surrounded by his most prized possessions. The doctor now proceeds to remove his eyeball.
  EXPRESSION: null

::PATHS::
- CHOICE: "Follow the son"
  TARGET: field_day
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Field
MOOD: Ritualistic
CHARACTERS: Narrator, Son, Father's Eyeball
BACKGROUND_IMAGE: field.png
BACKGROUND_EDIT: "Daytime, a small hole in the earth"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The son of the fallen elder has walked to a small HOLE in the earth. He lays his father’s EYEBALL in the hole, and covers it with soil.
  EXPRESSION: null

::PATHS::
- CHOICE: "Proceed to the book-binding room"
  TARGET: book_binding_room
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Book-Binding Room
MOOD: Disturbing
CHARACTERS: Narrator, Dead Bear, Hårgan Labourers, Christian
BACKGROUND_IMAGE: book_binding_room.png
BACKGROUND_EDIT: "Room for book-binding, collector's editions of books"

::SCRIPT::
- CHARACTER: Narrator
  LINE: A room that is typically used for book-binding. Its walls are lined with collector’s editions of books.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: A DEAD BEAR (seen earlier, alive and caged) lies on the island table. A deep INCISION has been drawn from the animal’s neck to its groin. Two Hårgan Labourers pull out the bear’s INNARDS.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: After scooping out the majority of its guts, they pile the waste into a bucket.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Then, with the assistance of two well-built Hårgan men, the Labourers endeavor to lift CHRISTIAN’s paralyzed body. Christian is fitted into the bear’s hollowed out carcass. They start by inserting his limp legs into the bear’s legs.
  EXPRESSION: null

::PATHS::
- CHOICE: "Observe the preparation"
  TARGET: sacred_house_interior_later
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Sacred House (Interior)
MOOD: Horrific
CHARACTERS: Narrator, Christian, Víoarr, Ingemar, Ulf, Doctor, Josh, Hårgan Men
BACKGROUND_IMAGE: sacred_house_interior.png
BACKGROUND_EDIT: "Interior, hay platform, bear carcass"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Christian has been secured into the giant bear carcass. The incision (from its groin to its neck) has been SEWN UP. The bear’s JAW has been removed, creating a gaping HOLE (down to its upper chest) through which Christian’s FACE is visible.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Five Hårgan labourers plant the bear carcass in the CENTER of the hay platform. There is a pole against which its back is rested. Christian is still unable to move or speak. His muffled screams persist.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: A man dressed as “Víoarr” (god of vengeance) stands before Christian. He holds the Rubi Radr in his hands.
  EXPRESSION: null
- CHARACTER: VÍOARR
  LINE: (in Swedish)
  Mighty and dreadful beast. With you, we purge our most unholy affects. We banish you now to the deepest recesses, where you may reflect on your wickedness.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Ingemar and Ulf are now strapped to the walls. They are also surrounded by their most prized belongings. The Doctor stands before Ulf. He pours a thick, sappy LIQUID into Ulf’s mouth.
  EXPRESSION: null
- CHARACTER: DOCTOR
  LINE: (in Swedish)
  Drink from the yew tree. Feel no fear.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The doctor moves to Ingemar, who smiles widely. The doctor pours the liquid into his mouth as well.
  EXPRESSION: null
- CHARACTER: DOCTOR
  LINE: (in Swedish)
  Drink from the yew tree. Feel no pain.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: In the b.g., Josh’s corpse has also been placed. The doctor leaves the house. Now, THREE HÅRGAN MEN enter with FLAMING TORCHES. Music begins outside, including the wordless, microtonal SINGING we’ve come to recognize.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The men approach Christian, whose “screaming” has become horribly frenzied.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The men move to different sides of the hay platform. They form a TRIANGLE. Simultaneously, they touch their torches to the hay - igniting a FIRE.
  EXPRESSION: null

::PATHS::
- CHOICE: "Witness the fire's spread"
  TARGET: field_same_time
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Field
MOOD: Intense
CHARACTERS: Narrator, Hårgan Torch-men, Christian, Ulf, Ruben, Dani, Pelle
BACKGROUND_IMAGE: field.png
BACKGROUND_EDIT: "Same time as interior fire, Hårgan community present"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The torch-men exit the house. Inside, the fire has begun to spread along the platform. The music rises as the fire picks up. The SINGING, which wavers in trembling anticipation, has not yet found harmony.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Dani watches this with dissociated eyes. She stands tensely in the field, eyes locked on the fire. Behind her, all of Hårga is enraptured.
  EXPRESSION: null

::PATHS::
- CHOICE: "Return to the Sacred House"
  TARGET: sacred_house_interior_later_cont
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Sacred House (Interior)
MOOD: Inferno
CHARACTERS: Narrator, Christian, Ulf, Ingemar
BACKGROUND_IMAGE: sacred_house_interior.png
BACKGROUND_EDIT: "Interior, fire has spread significantly"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The fire has grown considerably. Inside the bear, Christian is now being steam-boiled in the animal’s fluids. The bear’s FUR begins to catch fire. Before long, the whole animal is swallowed in the blaze. Christian’s wretched face becomes invisible behind the flames.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Ulf and Ingemar (still smiling) watch this with detached fascination.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The fire has now spread to other piles of hay. It has begun to crawl up the walls of the house.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Ulf is suddenly consumed by flames. He SCREAMS!
  EXPRESSION: null

::PATHS::
- CHOICE: "Witness the community's reaction"
  TARGET: field_same_time_cont
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Field
MOOD: Cataclysmic
CHARACTERS: Narrator, Hårgan Community, Ulf, Ruben, Dani, Pelle
BACKGROUND_IMAGE: field.png
BACKGROUND_EDIT: "Same time, Hårgan community reacting to fire"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Ulf’s screams are heard from the Sacred House. Suddenly, every member of the Hårgan community (who is not singing) begins to SCREAM as well. Feeling Ulf’s pain, they emit a horrible chorus of wails. When Ulf’s screams die down, so do theirs.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Meanwhile, Ruben has been given paper to PAINT on. Two elders encourage him.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: DANI, watching the burning house with fraught eyes, is suddenly met with a wave of conflicting emotions. Her expression curdles into one of sheer HORROR and DISGUST. Then it becomes one of deep SORROW and SHAME. Her eyes well with tears. The singing has now HARMONIZED and has risen to an insane, operatic pitch.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: We cut to an immense WIDE. Dani’s back is in the f.g. and the burning house is in the b.g. Overcome, Dani buries her face in her hands. Breaking into gentle sobs, she begins to walk aimlessly to the side. We TRACK alongside her, keeping her centered. She is circling the house, pulling at her hair and face in increasing anguish. She is WEEPING now, and the house (ever-present in the b.g.) has become ENGULFED in the raging flames.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Dani begins MOANING and SCREAMING. Her howls almost harmonize with the singing in the b.g. The fire ROARS and CRACKLES in the distance. It’s apocalyptic.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Soon it’s uncertain whether Dani is crying or LAUGHING. Her legs become weak and she collapses to her knees. Four Hårgans (one of them being Pelle) run into the scene, carrying a LARGE CHAIR - Dani’s throne.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The Hårgans lift Dani by the arms and SEAT her in the throne. They then HOIST the chair into the air.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: On the upward LIFT, we cut to a tight CLOSE-UP of Dani’s face. She is being carried forward. Her expression, which begins as one of great distress, slowly starts to TURN. Her agony subsides into sudden CONFUSION. What’s happening? Where am I? I’m on this chair, being carried! Her expression goes from FEAR to EXCITEMENT to CONFUSION again. She suddenly lets out an abrupt LAUGH (which we can’t hear over the music and the now-deafening FIRE). Dani is now being taken over by an invading sense of pride and contentment. This soon evolves into a manic exhilaration. Dani BEAMS. She has been embraced by a new family. She is Queen. She is not alone.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: A SMILE finally breaks onto Dani’s face. She has surrendered to a joy known only by the insane. She has lost herself completely, and she is finally free. It is horrible and it is beautiful.
  EXPRESSION: null

::PATHS::
- CHOICE: "Fade to black"
  TARGET: end
  STATE_CHANGE: null
  CONDITION: null

