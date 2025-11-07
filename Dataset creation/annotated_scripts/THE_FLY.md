::SCENE::
LOCATION: Hotel Conference Room
MOOD: Engaging Curiosity
CHARACTERS: Seth Brundle, Veronica Quaife, Narrator, Science Types (background)
BACKGROUND_IMAGE: hotel_conference_room.png
BACKGROUND_EDIT: "Nighttime, large conference room, full of eccentric science types, with a gaudy banner"

::SCRIPT::
- CHARACTER: Narrator
  LINE: We are close on the face of SETH BRUNDLE, aging molecular physics wunderkind. He is not aging too badly, however, and looks much younger than his 38 years - playful child face, slightly heavy - a big kid. Even his arrogance is somehow engaging, especially now as he talks to someone who is, for the moment, off camera. Someone he seems eager to impress.
  EXPRESSION: null
- CHARACTER: Brundle
  LINE: What am I working on? I’m working on something that will change the world and human life as we know it.
  EXPRESSION: Eager
- CHARACTER: Narrator
  LINE: The off-camera voice that replies is female and matter-of-fact, and belongs to VERONICA QUAIFE, who is evidently someone not likely to be easily impressed.
  EXPRESSION: null
- CHARACTER: Veronica (OC)
  LINE: Change it a lot or just a bit? You’ll have to be more specific.
  EXPRESSION: Analytical
- CHARACTER: Narrator
  LINE: Brundle lifts a glass of Scotch to his mouth and takes a sip. He glances around the room which we have not yet seen.
  EXPRESSION: null
- CHARACTER: Brundle
  LINE: You want me to be specific here, in this room, with half the scientific community of North America eavesdropping?
  EXPRESSION: Sarcastic
- CHARACTER: Narrator
  LINE: Veronica is a very attractive woman in her mid-twenties. She is as focused and analytical as Brundle is sloppy and puppyish. She toys with a drink but does not taste it.
  EXPRESSION: null
- CHARACTER: Veronica
  LINE: Is there another way?
  EXPRESSION: Direct
- CHARACTER: Narrator
  LINE: Brundle chews nervously on a fingernail.
  EXPRESSION: Nervous
- CHARACTER: Brundle
  LINE: You could come back to my lab. I’ll make you a cappuccino. I have a Faema of my very own. Not the dilettante’s plastic kitchen model. A real restaurant espresso machine.
  EXPRESSION: Eager
- CHARACTER: Narrator
  LINE: Veronica studies Brundle carefully.
  EXPRESSION: Thoughtful
- CHARACTER: Veronica
  LINE: Somehow I get the feeling you don’t get out much.
  EXPRESSION: Observant
- CHARACTER: Brundle
  LINE: You can tell that?
  EXPRESSION: Amazed
- CHARACTER: Veronica
  LINE: Yeah.
  EXPRESSION: Matter-of-fact
- CHARACTER: Brundle
  LINE: Actually I’ve been alone working for a long time now.
  EXPRESSION: Honest
- CHARACTER: Narrator
  LINE: Veronica picks up her bag - it's big and leathery and full of notes and books - and starts to move off through the room. Brundle grabs his drink and follows her. Scotch slops all over Brundle's hand and cuff, but he doesn't seem to notice it.
  EXPRESSION: null
- CHARACTER: Brundle
  LINE: Hey! How about it? Are you coming with me?
  EXPRESSION: Desperate
- CHARACTER: Veronica
  LINE: Sorry, I've got three other interviews to do before the party's over.
  EXPRESSION: Apologetic
- CHARACTER: Narrator
  LINE: We pop back and take a look at the room Brundle and Veronica are in. It is an enormous HOTEL CONFERENCE ROOM full of rather eccentric science types. A GAUDY BANNER running the entire length of the room proclaims: BARTOK science industries FOURTH ANNUAL MEET-THE-PRESS LUNCHEON.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Brundle has to struggle through the crowd to keep Veronica within earshot.
  EXPRESSION: null
- CHARACTER: Brundle
  LINE: Yeah. But they're not working on something that will change the world as we know it.
  EXPRESSION: Persistent
- CHARACTER: Veronica
  LINE: They say they are.
  EXPRESSION: Skeptical
- CHARACTER: Narrator
  LINE: Brundle manages to wedge himself in front of Veronica and slow her down. He takes a quick sip of his drink, but there's almost nothing left: it's all on his sleeve.
  EXPRESSION: null
- CHARACTER: Brundle
  LINE: Yeah, but they’re lying.
  EXPRESSION: Confident
- CHARACTER: Brundle
  LINE: I'm not.
  EXPRESSION: Serious
- CHARACTER: Narrator
  LINE: Veronica takes a closer look at Brundle. Despite his soggy sleeves, he is very convincing.
  EXPRESSION: null

::PATHS::
- CHOICE: "Go to Brundle's lab"
  TARGET: veronicas_car
  STATE_CHANGE: Veronica_curiosity = +1, Brundle_hope = +1
  CONDITION: null

::SCENE::
LOCATION: Veronica’s Car
MOOD: Awkward
CHARACTERS: Veronica, Brundle, Narrator
BACKGROUND_IMAGE: veronica_car.png
BACKGROUND_EDIT: "Nighttime, interior of an old Renault Le Car"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Veronica drives through the night in her clapped-out Renault Le Car. Brundle is turning green.
  EXPRESSION: null
- CHARACTER: Veronica
  LINE: Are you sick?
  EXPRESSION: Concerned
- CHARACTER: Brundle
  LINE: Oh, sure.
  EXPRESSION: Queasy
- CHARACTER: Veronica
  LINE: You’re not a very accomplished drunk.
  EXPRESSION: Teasing
- CHARACTER: Brundle
  LINE: I’m always like this. Motion sickness. When I was a kid I puked on my tricycle. I hate vehicles.
  EXPRESSION: Annoyed
- CHARACTER: Veronica
  LINE: Should I drive more slowly?
  EXPRESSION: Considerate
- CHARACTER: Brundle
  LINE: No, just turn left. We’re almost there.
  EXPRESSION: Eager

::PATHS::
- CHOICE: "Continue to the lab"
  TARGET: lab_warehouse
  STATE_CHANGE: Brundle_nausea = +1
  CONDITION: null

::SCENE::
LOCATION: Lab Warehouse Exterior
MOOD: Dilapidated
CHARACTERS: Veronica, Brundle, Narrator
BACKGROUND_IMAGE: lab_warehouse_exterior.png
BACKGROUND_EDIT: "Nighttime, huge, dilapidated warehouse by the waterfront, under a freeway"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Le Car pulls up outside a huge, dilapidated warehouse by the waterfront under a freeway. Veronica helps Brundle out of the car.
  EXPRESSION: null
- CHARACTER: Veronica
  LINE: This is it?
  EXPRESSION: Surprised
- CHARACTER: Brundle
  LINE: It's cleaner on the inside.
  EXPRESSION: Defensive

::PATHS::
- CHOICE: "Enter the warehouse"
  TARGET: warehouse_stairway
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Warehouse Stairway
MOOD: Old, slightly eerie
CHARACTERS: Veronica, Brundle, Narrator
BACKGROUND_IMAGE: warehouse_stairway.png
BACKGROUND_EDIT: "Nighttime, warped wooden stairs, ornate railing, dim lighting"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Veronica and Brundle climb the warped wooden stairs to the fourth floor. Brundle is breathing hard, very out of shape. He uses the ornate railing to haul himself from step to step.
  EXPRESSION: null
- CHARACTER: Veronica
  LINE: Nice rai1ings.
  EXPRESSION: Observant
- CHARACTER: Brundle
  LINE: Yeah. They’re original.
  EXPRESSION: Exerted
- CHARACTER: Veronica
  LINE: You doing marine experiments?
  EXPRESSION: Curious
- CHARACTER: Brundle
  LINE: No, why?
  EXPRESSION: Confused
- CHARACTER: Veronica
  LINE: That fishy smell.
  EXPRESSION: Direct
- CHARACTER: Brundle
  LINE: Oh, that. Used to be a packing house for fish. It’s deserted right now, except for me. I’ve got the whole fourth floor. The top floor.
  EXPRESSION: Explaining
- CHARACTER: Veronica
  LINE: Want me to carry you?
  EXPRESSION: Teasing
- CHARACTER: Brundle
  LINE: Maybe next time.
  EXPRESSION: Playful

::PATHS::
- CHOICE: "Continue upstairs to the lab"
  TARGET: brundles_lab
  STATE_CHANGE: Brundle_exhaustion = +1
  CONDITION: null

::SCENE::
LOCATION: Brundle’s Lab
MOOD: Chaotic, mysterious
CHARACTERS: Veronica, Brundle, Narrator
BACKGROUND_IMAGE: brundles_lab.png
BACKGROUND_EDIT: "Nighttime, immense warehouse space, messy, junk everywhere, two distinct glass booths"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Veronica and Brundle enter Brundle’s lab through an ancient steel-and-rotting-wood sliding door. It is immediately obvious that the lab is not just a lab: Brundle lives here, and he lives messy. There is junk everywhere, amongst which are a couple of mattresses lying on the floor.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The immense warehouse space is only partially divided by a couple of brick half-walls and by the square wooden pillars which soar up to a system of interlocking sky 1ights above.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Almost unnoticed amid the chaos stand TWO GLASS BOOTHS with molded plastic bases. They are at opposite ends of the room and look very much like an Italian designer's version of hi-tech telephone booths or, possibly, portable shower stalls.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The whole thing feels completely wrong to Veronica.
  EXPRESSION: null
- CHARACTER: Veronica
  LINE: Listen, maybe this is a bad idea.
  EXPRESSION: Uneasy
- CHARACTER: Brundle
  LINE: Too late. You’ve already seen it. I can’t let you leave here alive.
  EXPRESSION: Joking
- CHARACTER: Veronica
  LINE: I haven’t seen anything.
  EXPRESSION: Dismissive
- CHARACTER: Narrator
  LINE: Brundle carefully points out the glass booths.
  EXPRESSION: null
- CHARACTER: Brundle
  LINE: Those.
  EXPRESSION: Pointing
- CHARACTER: Veronica
  LINE: Designer phone booths. Very cute. I’ll bet you’ve got a really neat jukebox in here somewhere, too. Over there, maybe?
  EXPRESSION: Sarcastic
- CHARACTER: Narrator
  LINE: She points to a huge shape in a corner covered by a tarpaulin.
  EXPRESSION: null
- CHARACTER: Brundle
  LINE: No, that’s the prototype of these. First one I had made. It works, but it’s clunky.
  EXPRESSION: Explaining
- CHARACTER: Narrator
  LINE: Brundle pulls a blue bathrobe being used as an impromptu dust cover off an extremely serious-looking control­ module complete with computer console and monitor. The information storage system is all laser disc. The module is on wheels, but is plugged into a heavy-duty wiring loom at the base of one of the pillars.
  EXPRESSION: null

::PATHS::
- CHOICE: "Ask about the control module"
  TARGET: module_explanation
  STATE_CHANGE: Veronica_curiosity = +1
  CONDITION: null

::SCENE::
LOCATION: Brundle's Lab
MOOD: Curious, then amazed, then tense
CHARACTERS: Narrator, Brundle, Veronica
BACKGROUND_IMAGE: brundle_lab.png
BACKGROUND_EDIT: "A dimly lit scientific lab with two futuristic booths and a computer workstation"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Brundle flips a couple of switches. Lights come on. The monitor flickers to life. Very bright white interior lights also come on in the two booths.
  EXPRESSION: null
- CHARACTER: Brundle
  LINE: I call them telepods. They’re controlled by this.
  EXPRESSION: null
- CHARACTER: Veronica
  LINE: Thank God for that.
  EXPRESSION: Sarcastic
- CHARACTER: Narrator
  LINE: Veronica takes a careful look at Brundle.
  EXPRESSION: null
- CHARACTER: Veronica
  LINE: You’re very eccentric.
  EXPRESSION: null
- CHARACTER: Brundle
  LINE: You think so? That would be great. I’ve always considered myself invisibly middle-class.
  EXPRESSION: Happy
- CHARACTER: Veronica
  LINE: I don’t think you should worry about it. OK. So what do they do? The phone booths?
  EXPRESSION: null
- CHARACTER: Brundle
  LINE: Telepods. All right. As the magician says, 'Give me something personal, an item of clothing or jewelry, something uniquely you.'
  EXPRESSION: null
- CHARACTER: Veronica
  LINE: You’re joking.
  EXPRESSION: Surprised
- CHARACTER: Brundle
  LINE: No, I'm serious.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Veronica studies him once again. Yes, he’s serious.
  EXPRESSION: null
- CHARACTER: Veronica
  LINE: OK. Here goes.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Veronica hikes up her skirt and slips off her panties -an impulsive act rather than a calculated one. She holds them out to Brundle. They’re lacy and pretty. Brundle is shocked.
  EXPRESSION: Surprised
- CHARACTER: Brundle
  LINE: Ah... well...
  EXPRESSION: Surprised
- CHARACTER: Veronica
  LINE: I don’t wear jewelry.
  EXPRESSION: null
- CHARACTER: Brundle
  LINE: Yeah. OK.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: He takes the panties, gingerly.
  EXPRESSION: null
- CHARACTER: Brundle
  LINE: Nice.
  EXPRESSION: null
- CHARACTER: Veronica
  LINE: Thanks.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Brundle walks over to the nearest telepod and presses a button on the doorframe. The door unlatches with a click.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Brundle carefully places the panties on the floor of the telepod, then closes the door again.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Brundle returns to the computer, sits down on an old steno chair, and starts to click away at the computer keys. Veronica looks over his shoulder.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The screen fills with techno-babble. This soon makes way for a three-dimensional graphic of Veronica’s panties which rotates on the screen. A DATA LIST appears in the corner of the screen outlining the panties’ vital statistics - weight, dimensions, density, molecular configuration, etc.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Satisfied, Brundle smiles, presses the ACCEPT button, and points to the first telepod.
  EXPRESSION: Happy
- CHARACTER: Brundle
  LINE: Watch.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The first thing that happens is that the automatic doorlatch on the outside of the telepod slides shut. The latch is substantial, even massive, suggesting that it would not be a good thing for the door to open accidentally.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Now, as Veronica watches, the panties begin to disintegrate in the telepod. It’s almost as though we can see the atoms breaking off from the cloth itself and begin to float, swirl, swarm about in the bright cold light of the telepod. In moments, there is nothing left of the panties.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The telepod lights flash once, then go out.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Brundle turns proudly to Veronica.
  EXPRESSION: Happy
- CHARACTER: Brundle
  LINE: Well?
  EXPRESSION: null
- CHARACTER: Veronica
  LINE: Great. The world’s largest microwave oven. I’m glad I didn’t give you my Rolex.
  EXPRESSION: Sarcastic
- CHARACTER: Brundle
  LINE: No, no - you’re missing the point. Look.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Brundle points to the screen. The words TELEPORTATION SUCCESSFUL are flashing on and off.
  EXPRESSION: null
- CHARACTER: Veronica
  LINE: Teleportation?
  EXPRESSION: Confused
- CHARACTER: Narrator
  LINE: Brundle gets up and takes Veronica by the hand.
  EXPRESSION: null
- CHARACTER: Brundle
  LINE: Now come with me.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Brundle marches Veronica across the room to the second telepod. Inside the telepod are her panties.
  EXPRESSION: null
- CHARACTER: Veronica
  LINE: Wait a minute. Is that a hologram? Where are my panties?
  EXPRESSION: Surprised
- CHARACTER: Narrator
  LINE: Brundle press the door button and the door to the second telepod pops open.
  EXPRESSION: null
- CHARACTER: Brundle
  LINE: That’s them. The real ones. Go ahead. Pick them up.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Veronica hesitates a beat, then reaches into the telepod and picks up her panties. She crumples them in her hand. They feel the same.
  EXPRESSION: null
- CHARACTER: Brundle
  LINE: Examine them carefully for authenticity. Make sure nothing has been lost in translation.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Veronica looks at the label, the lace trim. It all checks out.
  EXPRESSION: null
- CHARACTER: Veronica
  LINE: I don’t think I get it. What happened?
  EXPRESSION: Confused
- CHARACTER: Brundle
  LINE: You get it, all right. You just can’t handle it. Your panties have just been teleported from one pod to another. Disintegrated there, and reintegrated there. Sort of. It’ll change the world as we know it, right? Want me to autograph them?
  EXPRESSION: Excited
- CHARACTER: Veronica
  LINE: This is incredible. How have you managed to keep this quiet? How could you do this alone?
  EXPRESSION: Surprised
- CHARACTER: Brundle
  LINE: I don’t work alone. There’s a lot of stuff in there I don’t even understand. I’m really a systems-management man. I farm bits and pieces of this stuff out to guys who are much more brilliant than I am. But none of them knows what the project really is. I say - build me a laser this, design me a molecular analyzer that - and they do. I just stick ’em together.
  EXPRESSION: null
- CHARACTER: Veronica
  LINE: And the money? Bartok Science Industries finances this?
  EXPRESSION: null
- CHARACTER: Brundle
  LINE: They leave me alone. I’m not expensive. They know they’ll end up owning it all, whatever it is.
  EXPRESSION: null
- CHARACTER: Veronica
  LINE: You haven’t told them?
  EXPRESSION: Surprised
- CHARACTER: Brundle
  LINE: When I’m ready.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: An insistent little beep begins to sound from somewhere under Veronica’s chic padded jacket. She drops the panties onto a coffee table, fumbles around in her jacket and pulls out a small tape recorder from an inner pocket.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Brundle is stunned: she’s been taping him.
  EXPRESSION: Surprised
- CHARACTER: Brundle
  LINE: Oh, no! Not that!
  EXPRESSION: Surprised
- CHARACTER: Narrator
  LINE: Veronica deftly flips over the cassette, sets the machine on RECORD, and drops it back into the pocket.
  EXPRESSION: null
- CHARACTER: Veronica
  LINE: Why not? You want me to get the quotes right, don't you?
  EXPRESSION: null
- CHARACTER: Brundle
  LINE: Don't do it. If this gets out now, it'll be a disaster.
  EXPRESSION: Afraid
- CHARACTER: Veronica
  LINE: Oh, I'm sure you're exaggerating.
  EXPRESSION: Sarcastic
- CHARACTER: Brundle
  LINE: But I'm not exaggerating...
  EXPRESSION: Afraid
- CHARACTER: Veronica
  LINE: What do you think I'm doing here, anyway? Don't give me that naïve bullshit. I'm a journalist. I was sent to that party by PARTICLE Magazine. You knew that.
  EXPRESSION: Angry
- CHARACTER: Brundle
  LINE: But I thought this was... you know, personal. I wouldn't tell any of this stuff to a journalist.
  EXPRESSION: Sad
- CHARACTER: Veronica
  LINE: But you did tell this stuff to a journalist. And you know what? I think you did it intentionally. I think you want me to tell the world about this. You just haven’t admitted it to yourself. Listen - it’s been real.
  EXPRESSION: Angry
- CHARACTER: Narrator
  LINE: Veronica’s almost out the door. She obviously has no intention of hanging around to discuss it. Brundle picks up her panties from the coffee table.
  EXPRESSION: null
- CHARACTER: Brundle
  LINE: Hey - you forgot s
  EXPRESSION: Angry

::PATHS::
- CHOICE: "Continue"
  TARGET: next_scene
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Brundle's Apartment
MOOD: Awkward, Departing
CHARACTERS: Narrator, Veronica, Brundle
BACKGROUND_IMAGE: brundle_apartment.png
BACKGROUND_EDIT: "Daytime, interior, messy, scientific equipment hinted"

::SCRIPT::
- CHARACTER: Brundle
  LINE: omething!
  EXPRESSION: Alert
- CHARACTER: Narrator
  LINE: Veronica pauses, turns. Brundle balls up the panties and throws them at her. They unfold in midair and flop harmlessly on the floor between them.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Veronica shrugs and smiles a "What can I do?" kind of smile. She leaves. Brundle slides the door closed after her with a slam.
  EXPRESSION: Amused

::PATHS::
- CHOICE: "Veronica leaves"
  TARGET: monolith_publishing_building_ext
  STATE_CHANGE: brundle_feelings_veronica = +1, veronica_curiosity = +1
  CONDITION: null

::SCENE::
LOCATION: Monolith Publishing Building
MOOD: Neutral, Professional
CHARACTERS: Narrator
BACKGROUND_IMAGE: monolith_publishing.png
BACKGROUND_EDIT: "Sleek, modern office building, morning"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Establishing shot of sleeko modern office building.
  EXPRESSION: null

::PATHS::
- CHOICE: "Enter the building"
  TARGET: particle_magazine_office
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Particle Magazine Editorial Offices
MOOD: Professional, Argumentative, Flirty
CHARACTERS: Narrator, Stathis Borans, Veronica, Brundle
BACKGROUND_IMAGE: particle_magazine_office.png
BACKGROUND_EDIT: "Morning, sleek, powerful editor's office, art-deco couch"

::SCRIPT::
- CHARACTER: Narrator
  LINE: We are in the office of STATHIS BORANS, the Editor-in-Chief of PARTICLE Magazine. The office itself oozes power and influence - the office of a starmaker in the arcane world of modern science. Stathis himself seems a bit more like the editor of a self-consciously chic New York glossy, say VANITY FAIR. He wears small, round, horn­ rimmed glasses and immaculate classic clothes. Despite his stylistic pretensions, however, his background is solidly scientific, and the walls are covered with his degrees, both honorary and hard-science.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Veronica is draped comfortably over an art-deco couch - obviously very much at home. They are listening to her tape.
  EXPRESSION: null
- CHARACTER: Veronica
  LINE: You just haven’t admitted it to yourself.
  EXPRESSION: Thoughtful (ON TAPE)
- CHARACTER: Narrator
  LINE: (PAUSE)
  EXPRESSION: null
- CHARACTER: Veronica
  LINE: Listen - it's been real.
  EXPRESSION: Resigned (ON TAPE)
- CHARACTER: Brundle
  LINE: Hey... you forgot something!
  EXPRESSION: Surprised (ON TAPE)
- CHARACTER: Narrator
  LINE: Veronica flicks off the tape recorder.
  EXPRESSION: null
- CHARACTER: Veronica
  LINE: That’s it. What do you think?
  EXPRESSION: Curious
- CHARACTER: Stathis
  LINE: I think you’re an opportunistic slut.
  EXPRESSION: Contemptuous
- CHARACTER: Veronica
  LINE: What do you think about teleportation?
  EXPRESSION: Curious (IGNORING THE COMMENT)
- CHARACTER: Stathis
  LINE: It’s a joke.
  EXPRESSION: Dismissive
- CHARACTER: Veronica
  LINE: What?
  EXPRESSION: Surprised
- CHARACTER: Stathis
  LINE: He’s conning you. He’s doing an old nightclub routine. The two cabinets. And you fell for it.
  EXPRESSION: Dismissive
- CHARACTER: Veronica
  LINE: Hey, wait a minute...
  EXPRESSION: Defensive
- CHARACTER: Stathis
  LINE: Are we having lunch?
  EXPRESSION: Annoyed
- CHARACTER: Veronica
  LINE: Listen, that was no nightclub routine.
  EXPRESSION: Defensive
- CHARACTER: Narrator
  LINE: The intercom buzzes.
  EXPRESSION: null
- CHARACTER: Stathis
  LINE: Yes?
  EXPRESSION: Neutral (PICKING UP PHONE)
- CHARACTER: Narrator
  LINE: (PAUSE)
  EXPRESSION: null
- CHARACTER: Stathis
  LINE: Sure. Send him in.
  EXPRESSION: Authoritative
- CHARACTER: Narrator
  LINE: Stathis hangs up.
  EXPRESSION: null
- CHARACTER: Stathis
  LINE: You must have made an impression.
  EXPRESSION: Teasing
- CHARACTER: Veronica
  LINE: What do you mean?
  EXPRESSION: Confused
- CHARACTER: Stathis
  LINE: Your magician has followed you here.
  EXPRESSION: Teasing
- CHARACTER: Narrator
  LINE: A young woman wearing a brisk business suit shows Brundle in. Stathis smiles a professional smile and extends his hand.
  EXPRESSION: null
- CHARACTER: Stathis
  LINE: Stathis Borans. I’m the editor of PARTICLE Magazine.. Nice to meet you.
  EXPRESSION: Professional
- CHARACTER: Brundle
  LINE: Uh... Seth Brundle.
  EXPRESSION: Nervous
- CHARACTER: Stathis
  LINE: Oh, I know who you are.
  EXPRESSION: Knowing
- CHARACTER: Narrator
  LINE: Brundle is about to ask "How?” but doesn’t get the chance.
  EXPRESSION: null
- CHARACTER: Stathis
  LINE: Listen... why don’t you two use my office? I’ve got to run. If you plan to make anything disappear, let me know. I have an assistant editor who’s outlived his usefulness.
  EXPRESSION: Dismissive (TO BRUNDLE)
- CHARACTER: Narrator
  LINE: Stathis leaves.
  EXPRESSION: null
- CHARACTER: Brundle
  LINE: You haven’t wasted any time.
  EXPRESSION: Slightly Annoyed
- CHARACTER: Veronica
  LINE: I’m not getting any younger.
  EXPRESSION: Playful
- CHARACTER: Brundle
  LINE: I take it he wasn’t too impressed by your tape.
  EXPRESSION: Questioning
- CHARACTER: Veronica
  LINE: He thinks you’re a con man.
  EXPRESSION: Neutral
- CHARACTER: Brundle
  LINE: Excellent!
  EXPRESSION: Excited (BRIGHTENING)
- CHARACTER: Veronica
  LINE: Yeah? Well, let’s see what the people at Omni think about it.
  EXPRESSION: Defiant
- CHARACTER: Brundle
  LINE: Hold on, hold on. Look. I’ve come here to say two magic words to you.
  EXPRESSION: Sincere
- CHARACTER: Narrator
  LINE: She stops at the door.
  EXPRESSION: null
- CHARACTER: Veronica
  LINE: Yeah?
  EXPRESSION: Curious
- CHARACTER: Brundle
  LINE: Cheese-burger.
  EXPRESSION: Playful
- CHARACTER: Narrator
  LINE: Brundle says these words as though they are indeed magical, irresistible. Veronica shakes her head and laughs. For her, it’s Brundle himself who’s rapidly becoming irresistible.
  EXPRESSION: Amused

::PATHS::
- CHOICE: "Leave Stathis's office with Brundle"
  TARGET: editorial_offices_hallway
  STATE_CHANGE: veronica_attraction_brundle = +1
  CONDITION: null

::SCENE::
LOCATION: Editorial Offices Hallway
MOOD: Suspicious, Scheming
CHARACTERS: Narrator, Stathis, Veronica, Brundle
BACKGROUND_IMAGE: editorial_hallway.png
BACKGROUND_EDIT: "Morning, hallway with glass walls, conference room visible"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Veronica leaves with Brundle. They are showing signs of liking each other.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Stathis watches them through the glass wall of the conference room. His eyes are laser bright. He is not smiling. He picks up the phone.
  EXPRESSION: Scheming
- CHARACTER: Stathis
  LINE: Renee? Get me everything you’ve got on Seth Brundle. Yeah. He’s with Bartok. Yeah - their stable of geniuses. He was part of their dog and pony show two days ago. Yeah. But I mean, everything, including personal. Dig deep, darling. Thanks.
  EXPRESSION: Demanding

::PATHS::
- CHOICE: "Stathis makes a call"
  TARGET: macdonaldsesque_restaurant
  STATE_CHANGE: stathis_suspicion_brundle = +1
  CONDITION: null

::SCENE::
LOCATION: Macdonaldsesque Restaurant
MOOD: Revealing, Developing Relationship, Negotiation
CHARACTERS: Narrator, Brundle, Veronica
BACKGROUND_IMAGE: macdonalds_restaurant.png
BACKGROUND_EDIT: "Daytime, fast food restaurant, assembly line food preparation visible"

::SCRIPT::
- CHARACTER: Narrator
  LINE: CU Burgers sliding down a ramp in assembly-line style. CU cheese slices being slapped onto each burger by machine.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Brundle is taking Veronica out to lunch.
  EXPRESSION: null
- CHARACTER: Veronica
  LINE: You always eat here?
  EXPRESSION: Curious
- CHARACTER: Brundle
  LINE: I hate surprises. Scientists love things to be repeatable. Every time you walk in, it’s exactly the same thing. I love it. Makes me feel secure.
  EXPRESSION: Content
- CHARACTER: Narrator
  LINE: Veronica takes a bite of her burger. It is obvious that she is used to better things.
  EXPRESSION: Disgusted
- CHARACTER: Veronica
  LINE: It’s a high price to pay for security.
  EXPRESSION: Sarcastic
- CHARACTER: Brundle
  LINE: Let’s talk turkey.
  EXPRESSION: Direct
- CHARACTER: Narrator
  LINE: Veronica is amused at Brundle’s turn of phrase. He hasn't been on the streets since he was eight years old.
  EXPRESSION: Amused
- CHARACTER: Veronica
  LINE: Sure. Turkey.
  EXPRESSION: Playful
- CHARACTER: Brundle
  LINE: You were right. I’ve been working alone too long. I have a very strong urge to talk about what I'm doing. But still... if this gets out now, it'll kill me. The Bartok people will kill me, my colleagues will kill me. It's not ready yet.
  EXPRESSION: Concerned
- CHARACTER: Veronica
  LINE: Seems to work OK.
  EXPRESSION: Skeptical
- CHARACTER: Brundle
  LINE: No. Something important is missing.
  EXPRESSION: Serious
- CHARACTER: Veronica
  LINE: Yeah?
  EXPRESSION: Questioning
- CHARACTER: Brundle
  LINE: Yeah.
  EXPRESSION: Evasive (HE WON'T TALK)
- CHARACTER: Veronica
  LINE: "Yeah” what?
  EXPRESSION: Impatient
- CHARACTER: Brundle
  LINE: I can only teleport inanimate objects. Dead things.
  EXPRESSION: Reluctant (HE DECIDES TO TALK)
- CHARACTER: Veronica
  LINE: Are you criticizing my taste in underwear?
  EXPRESSION: Teasing
- CHARACTER: Brundle
  LINE: No! I love your taste in underwear!
  EXPRESSION: Excited (BRIGHTENING)
- CHARACTER: Veronica
  LINE: What happens when you try to teleport living things?
  EXPRESSION: Intrigued
- CHARACTER: Brundle
  LINE: Not while we’re eating.
  EXPRESSION: Disgusted (MAKES A FACE, SHAKES HIS HEAD)
- CHARACTER: Veronica
  LINE: It can’t be worse than this.
  EXPRESSION: Teasing (LAUGHS, INDICATES BURGER)
- CHARACTER: Narrator
  LINE: (PAUSE)
  EXPRESSION: null
- CHARACTER: Veronica
  LINE: You’re not doing a very good job of convincing me. I think the world should know about it now, and I think I should be the one to tell it.
  EXPRESSION: Insistent
- CHARACTER: Brundle
  LINE: How about half of that?
  EXPRESSION: Negotiating
- CHARACTER: Veronica
  LINE: What do you mean?
  EXPRESSION: Confused
- CHARACTER: Brundle
  LINE: You should tell it, but not yet. Look, what have you got so far?
  EXPRESSION: Negotiating
- CHARACTER: Veronica
  LINE: Just enough to make you nervous.
  EXPRESSION: Playful
- CHARACTER: Brundle
  LINE: Why not get more? Let me become your major project. I’m talking about a book, not a magazine article. Follow me and my work day by day, in as much detail as you can stand. I don’t have a life - so there’s nothing for you to interfere with. Research the background. Cover the process.
  EXPRESSION: Persuasive
- CHARACTER: Narrator
  LINE: (PAUSE)
  EXPRESSION: null
- CHARACTER: Brundle
  LINE: You could even move in with me if you wanted to. I mean... you know, in a professional context.
  EXPRESSION: Suggestive
- CHARACTER: Veronica
  LINE: Sure. I know.
  EXPRESSION: Calm
- CHARACTER: Narrator
  LINE: (WRITING HER DUST-COVER BLU
  EXPRESSION: null

::PATHS::
- CHOICE: "Consider Brundle's proposal"
  TARGET: end
  STATE_CHANGE: veronica_relationship_brundle = +1, brundle_trust_veronica = +1
  CONDITION: null

::SCENE::
LOCATION: Cafe/Restaurant
MOOD: Ambitious, Convincing
CHARACTERS: Brundle, Veronica, Narrator
BACKGROUND_IMAGE: null
BACKGROUND_EDIT: "Daytime, cafe interior"

::SCRIPT::
- CHARACTER: Brundle
  LINE: "The complete record of the most earth-shattering invention ever. The one that ended all concepts of transport, of time and space, of borders and frontiers.”
  EXPRESSION: Ambitious
- CHARACTER: Narrator
  LINE: (DRAMATIC PAUSE)
  EXPRESSION: null
- CHARACTER: Brundle
  LINE: And your book will end with me transporting myself fifteen feet through space, from one telepod to another. That’s what’s really missing. Wait for me that long.
  EXPRESSION: Determined
- CHARACTER: Narrator
  LINE: Veronica has mustard on her upper lip and her eyes are bright. Brundle is pushing the right buttons.
  EXPRESSION: Impressed

::SCENE::
LOCATION: Veronica’s Apartment. Living Room
MOOD: Everyday, then curious
CHARACTERS: Veronica, Narrator
BACKGROUND_IMAGE: null
BACKGROUND_EDIT: "Daytime, stylish apartment living room"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Veronica opens the door to her apartment - one of those places in which something stylish has been done with not really very much. As she dumps the day’s accumulated gear onto a floppy couch, she hears the shower going in the bathroom.
  EXPRESSION: null

::SCENE::
LOCATION: Veronica’s Bathroom
MOOD: Confrontational, Disgusted
CHARACTERS: Veronica, Stathis, Narrator
BACKGROUND_IMAGE: null
BACKGROUND_EDIT: "Daytime, apartment bathroom, shower running"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Veronica cautiously approaches the bathroom. The door is open. Veronica approaches the shower and, taking a deep breath, pulls aside the shower curtain. Stathis is calmly taking a shower.
  EXPRESSION: Curious
- CHARACTER: Veronica
  LINE: What are you doing in my apartment?
  EXPRESSION: Shocked
- CHARACTER: Stathis
  LINE: I happened to be in the neighborhood, felt a bit scummy. Rough day.
  EXPRESSION: Calm
- CHARACTER: Narrator
  LINE: Veronica pulls the shower curtain back into place in disgust and slams the bathroom door on the way out.
  EXPRESSION: Disgusted

::SCENE::
LOCATION: Veronica’s Living Room
MOOD: Annoyed, Tense
CHARACTERS: Veronica, Stathis, Narrator
BACKGROUND_IMAGE: null
BACKGROUND_EDIT: "Daytime, stylish apartment living room"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Veronica is drinking coffee and sorting through some papers when Stathis walks into the room, fully dressed but still toweling off his hair.
  EXPRESSION: null
- CHARACTER: Stathis
  LINE: No coffee for me?
  EXPRESSION: Amiable
- CHARACTER: Veronica
  LINE: As far as I’m concerned, you’re not here.
  EXPRESSION: Annoyed
- CHARACTER: Stathis
  LINE: The invisible man.
  EXPRESSION: Sarcastic
- CHARACTER: Veronica
  LINE: How did you get in?
  EXPRESSION: Demanding
- CHARACTER: Stathis
  LINE: I still have a key. You gave it to me, remember?
  EXPRESSION: Matter-of-fact
- CHARACTER: Veronica
  LINE: I knew I should have changed the locks.
  EXPRESSION: Regretful
- CHARACTER: Stathis
  LINE: I knew you wouldn’t.
  EXPRESSION: Confident
- CHARACTER: Veronica
  LINE: Yeah?
  EXPRESSION: Challenging
- CHARACTER: Stathis
  LINE: Yeah. That’s because, unconsciously, you want me to come back to you, move in again.
  EXPRESSION: Smug
- CHARACTER: Veronica
  LINE: No. That’s because, very consciously, I’m lazy and disorganized.
  EXPRESSION: Defensive
- CHARACTER: Stathis
  LINE: You new playmate is an interesting guy.
  EXPRESSION: Observant
- CHARACTER: Veronica
  LINE: What playmate?
  EXPRESSION: Confused
- CHARACTER: Stathis
  LINE: The nightclub act. Brundle.
  EXPRESSION: Knowing
- CHARACTER: Veronica
  LINE: Yeah?
  EXPRESSION: Curious
- CHARACTER: Stathis
  LINE: Yeah, I was wrong. He’s really very brilliant. He was the leader of the F32 team. Remember that? An inch away from the Nobel Prize for physics. He was only twenty at the time.
  EXPRESSION: Impressed
- CHARACTER: Veronica
  LINE: Well, he acts like he’s sixteen right now.
  EXPRESSION: Exasperated
- CHARACTER: Narrator
  LINE: (PAUSE)
  EXPRESSION: null
- CHARACTER: Veronica
  LINE: I'm not sure I'm going to do Brundle. I'm still considering the Psychology Today gig.
  EXPRESSION: Undecided
- CHARACTER: Stathis
  LINE: That's not like you.
  EXPRESSION: Suspicious
- CHARACTER: Veronica
  LINE: How would you know? We only lived together for two years. You were just beginning to not ice me when we split up.
  EXPRESSION: Wry
- CHARACTER: Stathis
  LINE: Now that is like you.
  EXPRESSION: Amused
- CHARACTER: Veronica
  LINE: Are you getting out or am I?
  EXPRESSION: Impatient
- CHARACTER: Stathis
  LINE: I'll go. I've got to put this issue to bed. Shall I come back later?
  EXPRESSION: Amiable
- CHARACTER: Veronica
  LINE: No.
  EXPRESSION: Firm
- CHARACTER: Narrator
  LINE: (HOLDS OUT HER HAND)
  EXPRESSION: null
- CHARACTER: Veronica
  LINE: Key.
  EXPRESSION: Demanding
- CHARACTER: Stathis
  LINE: I'll keep it, for old time’s sake. You want to keep me out, you change the locks.
  EXPRESSION: Teasing
- CHARACTER: Narrator
  LINE: He leaves.
  EXPRESSION: null

::SCENE::
LOCATION: Brundle’s Lab
MOOD: Scientific, Horrific, Despairing
CHARACTERS: Brundle, Veronica, Narrator
BACKGROUND_IMAGE: null
BACKGROUND_EDIT: "Nighttime, laboratory with high-tech equipment, telepods, video monitors"

::SCRIPT::
- CHARACTER: Narrator
  LINE: On a video monitor, we are close on a small monkey, the monkey is in the sending telepod. We pop back to a general view of Brundle's lab. He is, indeed, about to transmit a monkey and is hard at work at his computer keyboard.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Veronica is also hard at work.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: She’s got the entire place wired now - videotape, still cameras, sound tapes. Tapes recording his computer screens. She’s trying to keep track of everything from behind a small bank of video monitors stacked on a table.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Brundle plays the keyboard like Glenn Gould at his most eccentric - he mutters, mumbles, sings to himself.
  EXPRESSION: Focused
- CHARACTER: Narrator
  LINE: Finally, he sits back in satisfaction and presses the ACCEPT button.
  EXPRESSION: Satisfied
- CHARACTER: Narrator
  LINE: CU the MASSIVE TELEPOD DOOR LATCH as it slides shut.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The control monitor diagrams the monkey, the outlined figure on the screen duplicating the movement of its real-life counterpart inside the transmitter. The animals vital satisfies are calculated and appear. Then...
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The light goes on in the transmitter, lancing through the ape who is frozen in fear. The animal disintegrates.
  EXPRESSION: Horrified
- CHARACTER: Narrator
  LINE: Brundle dances up from the keyboard and runs over to the receiving telepod. As he peers through the window, SOMETHING, presumably the monkey’s body, lurches with a thump against the window. A RED SPLOTCH smears across the glass pane. From inside the chamber comes a sickening, tormented thrashing sound as the bloody, misshapen lump - a monkey turned inside out - splatters itself all over the glass of the telepod.
  EXPRESSION: Horrified
- CHARACTER: Narrator
  LINE: Veronica turns away from the spectacle, sickened. Brundle is devastated.
  EXPRESSION: Sickened
- CHARACTER: Narrator
  LINE: QUICK DISSOLVE TO:
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Brundle, in CU on monitor and in life. Brundle’s expression says "despair." We hear Veronica’s voice off-camera as she interviews him.
  EXPRESSION: Despairing
- CHARACTER: Veronica (OC)
  LINE: We’ve got to do this, Brundle. Talk to the tapes. Get in the habit. The world will want to know what you’re thinking.
  EXPRESSION: Professional
- CHARACTER: Brundle
  LINE: Fuck! Is what I’m thinking.
  EXPRESSION: Frustrated
- CHARACTER: Veronica (OC)
  LINE: Good. The world will want to know that. What else? Why didn’t it work?
  EXPRESSION: Inquisitive
- CHARACTER: Brundle
  LINE: I think it turned the monkey inside out.
  EXPRESSION: Distraught
- CHARACTER: Veronica (OC)
  LINE: Why?
  EXPRESSION: Curious
- CHARACTER: Brundle
  LINE: It can’t deal with flesh, with living things. It only seems to work with inanimate objects. Nothing that’s alive.
  EXPRESSION: Analytical
- CHARACTER: Narrator
  LINE: (THOUGHTFUL PAUSE)
  EXPRESSION: null
- CHARACTER: Brundle
  LINE: It must be my fault.
  EXPRESSION: Self-blaming
- CHARACTER: Veronica
  LINE: Why?
  EXPRESSION: Inquisitive
- CHARACTER: Brundle
  LINE: Computers are dumb. They only know what you tell them. I must not know enough about the flesh myself. Gonna have to learn.
  EXPRESSION: Determined
- CHARACTER: Narrator
  LINE: (HEAVY, RAGGED SIGH)
  EXPRESSION: null
- CHARACTER: Brundle
  LINE: I don’t want to talk now.
  EXPRESSION: Exhausted

::SCENE::
LOCATION: Lab. Bedroom Area
MOOD: Intimate, Reflective
CHARACTERS: Brundle, Veronica, Narrator
BACKGROUND_IMAGE: null
BACKGROUND_EDIT: "Nighttime, simple mattress, free-standing closet in a lab setting"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Brundle lies on his mattress, despondent. Veronica sits nearby.
  EXPRESSION: Despondent
- CHARACTER: Veronica
  LINE: Do you ever change your clothes?
  EXPRESSION: Curious
- CHARACTER: Brundle
  LINE: Huh?
  EXPRESSION: Confused
- CHARACTER: Veronica
  LINE: Your clothes. You’re always wearing the same clothes.
  EXPRESSION: Observant
- CHARACTER: Brundle
  LINE: No... these are clean. I change my clothes every day.
  EXPRESSION: Defensive
- CHARACTER: Narrator
  LINE: Veronica gets up and goes over to his free-standing closet. She opens the canvas door. Inside are neatly hung five versions of exactly the same clothes - sweater, pants, etc.
  EXPRESSION: null
- CHARACTER: Veronica
  LINE: Five sets of exactly the same clothes?
  EXPRESSION: Surprised
- CHARACTER: Brundle
  LINE: I learned it from Einstein.
  EXPRESSION: Proud
- CHARACTER: Veronica
  LINE: Repeatability?
  EXPRESSION: Understanding
- CHARACTER: Brundle
  LINE: Yeah. This way, I don’t have to expend any thought on what I’m going
  EXPRESSION: Practical

::SCENE::
LOCATION: Brundle's Apartment/Lab Living Area
MOOD: Romantic, then painful, then curious
CHARACTERS: Veronica, Brundle, Narrator
BACKGROUND_IMAGE: living_area.png
BACKGROUND_EDIT: "Messy apartment, mattress on floor, night"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Veronica lets the canvas door of the closet swing closed and drifts back to Brundle.
  EXPRESSION: null
- CHARACTER: Veronica
  LINE: I bought some steaks. Can I make you one?
  EXPRESSION: Neutral
- CHARACTER: Brundle
  LINE: We could go out
  EXPRESSION: Neutral
- CHARACTER: Veronica
  LINE: Cheese-burgers?
  EXPRESSION: Neutral
- CHARACTER: Brundle
  LINE: Well, I... We don’t have to go there...
  EXPRESSION: Self-Conscious
- CHARACTER: Narrator
  LINE: Veronica gets on the mattress with him.
  EXPRESSION: null
- CHARACTER: Veronica
  LINE: You’re very cute.
  EXPRESSION: Seductive
- CHARACTER: Brundle
  LINE: Am I?
  EXPRESSION: Nervous
- CHARACTER: Narrator
  LINE: She runs a finger over his lips. He tries to talk while she does this.
  EXPRESSION: null
- CHARACTER: Brundle
  LINE: I... I think you’re very beautiful.
  EXPRESSION: Nervous
- CHARACTER: Narrator
  LINE: Veronica’s finger ends up stuck in one corner of his mouth. She laughs.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Veronica bends close to Brundle and kisses him full on the lips. It makes Brundle very nervous.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Brundle tries top roll elegantly out from under Veronica’s advance but instead rolls half off the mattress and onto something sharp which has been lying on the floor. He yelps in pain.
  EXPRESSION: null
- CHARACTER: Brundle
  LINE: Ouch!
  EXPRESSION: Pain
- CHARACTER: Narrator
  LINE: Brundle detaches himself from Veronica.
  EXPRESSION: null
- CHARACTER: Veronica
  LINE: What happened?
  EXPRESSION: Concerned
- CHARACTER: Brundle
  LINE: I rolled onto something sharp. Take a look.
  EXPRESSION: Pain
- CHARACTER: Narrator
  LINE: Brundle turns his back to Veronica. Stuck to his back at the end of three tiny streaks of blood staining through his shirt is an old circuit board.
  EXPRESSION: null
- CHARACTER: Veronica
  LINE: Oh, God. Something’s stuck to your back!
  EXPRESSION: Shocked
- CHARACTER: Brundle
  LINE: Well, pull it off.
  EXPRESSION: Calm
- CHARACTER: Narrator
  LINE: Veronica is - perhaps surprisingly -squeamish. She grimaces as she pulls the board away. Three sharp metal connectors are the culprits. She shows it to Brundle.
  EXPRESSION: null
- CHARACTER: Brundle
  LINE: Oh, yeah. I was wondering what happened to this.
  EXPRESSION: Neutral
- CHARACTER: Narrator
  LINE: Brundle feels for the scratches and brings back blood on his finger tips.
  EXPRESSION: null
- CHARACTER: Veronica
  LINE: We’d better take a look.
  EXPRESSION: Concerned
- CHARACTER: Narrator
  LINE: Veronica begins to unbutton Brundle’s shirt.
  EXPRESSION: null
- CHARACTER: Brundle
  LINE: Uh... I can do that.
  EXPRESSION: Nervous
- CHARACTER: Narrator
  LINE: Veronica brushes his hands away.
  EXPRESSION: null
- CHARACTER: Veronica
  LINE: No, you’ve lost some blood. Better let me do it.
  EXPRESSION: Seductive
- CHARACTER: Narrator
  LINE: Veronica takes Brundle’s shirt off, caressing his shoulders as she does it. There are three long, deep scratches high on his back near the shoulder blade. Each scratch ends with a puncture mark.
  EXPRESSION: null
- CHARACTER: Veronica
  LINE: Have you got any disinfectant?
  EXPRESSION: Concerned
- CHARACTER: Narrator
  LINE: Brundle hands her a nearby dusty old glass of Scotch.
  EXPRESSION: null
- CHARACTER: Brundle
  LINE: This oughta do the trick.
  EXPRESSION: Neutral
- CHARACTER: Narrator
  LINE: Veronica dabs it on the scratches with her fingers.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Brundle gasps at the sharpness. Veronica gives his shoulder a gentle bite.
  EXPRESSION: null
- CHARACTER: Brundle
  LINE: Ah, please. No more pain.
  EXPRESSION: Pain
- CHARACTER: Veronica
  LINE: Sorry. I just suddenly wanted to eat you up. You know - that’s why old ladies pinch baby cheeks. It’s the flesh, it makes them crazy.
  EXPRESSION: Playful
- CHARACTER: Brundle
  LINE: Uh-huh. The flesh. Yes. Wanna try an experiment?
  EXPRESSION: Distracted
- CHARACTER: Veronica
  LINE: Sure.
  EXPRESSION: Excited
- CHARACTER: Narrator
  LINE: To her consternation, Brundle jumps out of bed and heads for the kitchen.
  EXPRESSION: null
- CHARACTER: Brundle
  LINE: Let’s make a steak.
  EXPRESSION: Excited

::PATHS::
- CHOICE: "Go to the kitchen to experiment"
  TARGET: lab_kitchen_area
  STATE_CHANGE: brundle_mood = "excited", veronica_mood = "confused"
  CONDITION: null

::SCENE::
LOCATION: Lab Kitchen Area
MOOD: Experimental, curious, passionate
CHARACTERS: Brundle, Veronica, Narrator
BACKGROUND_IMAGE: lab_kitchen.png
BACKGROUND_EDIT: "Scientific kitchen, night, teleporter visible"

::SCRIPT::
- CHARACTER: Narrator
  LINE: CU raw steak as it is cut into two halves. We pop back to see Brundle at work in the kitchen.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: MONTAGE SEQUENCE as Brundle puts one half of the steak through the teleporter on a white plate, and keeps the other half on a brown plate. Brundle takes the teleported half out of the receiver and begins to cook each half in a pan, without seasoning. He is careful to remember which half is which. Brundle pulls the steak halves off the stove. Brundle places the teleported half of the steak on a table in front of Veronica. END OF MONTAGE SEQUENCE
  EXPRESSION: null
- CHARACTER: Brundle
  LINE: OK. Eat this. I need an objective opinion.
  EXPRESSION: Eager
- CHARACTER: Veronica
  LINE: Are you serious? A monkey just came apart in that booth.
  EXPRESSION: Skeptical
- CHARACTER: Brundle
  LINE: Eat!
  EXPRESSION: Demanding
- CHARACTER: Narrator
  LINE: Veronica takes a bite of the steak.
  EXPRESSION: null
- CHARACTER: Veronica
  LINE: Hmph.
  EXPRESSION: Disgusted
- CHARACTER: Brundle
  LINE: So?
  EXPRESSION: Eager
- CHARACTER: Veronica
  LINE: It tastes - funny.
  EXPRESSION: Confused
- CHARACTER: Brundle
  LINE: Funny how?
  EXPRESSION: Curious
- CHARACTER: Veronica
  LINE: It tastes - synthetic.
  EXPRESSION: Disgusted
- CHARACTER: Brundle
  LINE: Now try this half.
  EXPRESSION: Neutral
- CHARACTER: Narrator
  LINE: She takes a bit e of the non-teleported half.
  EXPRESSION: null
- CHARACTER: Veronica
  LINE: Ok. It could use some finesse, but... it tastes like a steak. What have we proved?
  EXPRESSION: Neutral
- CHARACTER: Narrator
  LINE: Brundle begins to free-associate with a passion.
  EXPRESSION: null
- CHARACTER: Brundle
  LINE: Computers are dumb. They have no poetry. They do exactly what you tell them to do. Life is poetry. Even a good steak is poetry. The computer is giving us its interpretation of a steak. It’s rethinking it for us, translating it rather than reproducing it. And something is getting lost in the translation.
  EXPRESSION: Passionate
- CHARACTER: Veronica
  LINE: Me. I'm lost.
  EXPRESSION: Confused
- CHARACTER: Brundle
  LINE: The ghost in the machine. The life essence. Soul. Yeah. So. I know what you’re gonna say. You’re gonna say, "But a steak is dead.” Sure, a steak is dead - but it’s dead life!
  EXPRESSION: Passionate
- CHARACTER: Veronica
  LINE: I don’t think I was going to say that.
  EXPRESSION: Skeptical
- CHARACTER: Narrator
  LINE: Brundle gets up and starts to back out of the kitchen, headed more or less for the lab’s work area.
  EXPRESSION: null
- CHARACTER: Brundle
  LINE: It's what you've already said. It's the flesh. It should make the machine crazy, just like those old ladies pinching babies. But it doesn't, not yet. I haven't taught the machine how to be made crazy by the flesh, the poetry, the steak. I'm going to start teaching it now.
  EXPRESSION: Determined
- CHARACTER: Veronica
  LINE: What are you going to do, read it "Naked Lunch?"
  EXPRESSION: Amused
- CHARACTER: Narrator
  LINE: But Brundle is already gone. The sound of the keyboard clacking away madly floats back to Veronica from the lab work area. She shrugs and starts to finish off the good half of the steak.
  EXPRESSION: null

::PATHS::
- CHOICE: "Brundle continues working in the lab"
  TARGET: lab_warehouse_exterior
  STATE_CHANGE: brundle_activity = "working", veronica_activity = "eating"
  CONDITION: null

::SCENE::
LOCATION: Lab Warehouse
MOOD: Suspenseful, observant
CHARACTERS: Veronica, Stathis, Narrator
BACKGROUND_IMAGE: lab_warehouse_exterior.png
BACKGROUND_EDIT: "Morning, industrial area, nondescript cars"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Veronica leaves the lab and walks down the street. She walks past a nondescript car out of which rises Stathis, who is unshaven, half-asleep, lurking like a common maniac. He's obviously been there all night.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Veronica gets into her car and starts it. Stathis starts his and follows her down the street.
  EXPRESSION: null

::PATHS::
- CHOICE: "Veronica drives to the clothing store"
  TARGET: mens_clothing_store_exterior
  STATE_CHANGE: stathis_following = true
  CONDITION: null

::SCENE::
LOCATION: Men's Clothing Store
MOOD: Tense, stalking
CHARACTERS: Veronica, Stathis, Narrator
BACKGROUND_IMAGE: mens_clothing_store_exterior.png
BACKGROUND_EDIT: "Morning, retail street, store facade"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Veronica goes into the store. Stathis waits a beat, then gets out of his car and follows her in.
  EXPRESSION: null

::PATHS::
- CHOICE: "Stathis follows Veronica inside the store"
  TARGET: mens_clothing_store_interior
  STATE_CHANGE: stathis_jealousy = +1
  CONDITION: null

::SCENE::
LOCATION: Men's Clothing Store
MOOD: Jealous, confrontational
CHARACTERS: Veronica, Stathis, Narrator
BACKGROUND_IMAGE: mens_clothing_store_interior.png
BACKGROUND_EDIT: "Morning, clothing racks, retail environment"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Stathis watches her shop - for a man. It’s making him crazy. He no longer looks cool and powerful, just jealous and unbalanced.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Finally, unable to bear it any longer, Stathis intercepts her amongst the clothes racks just as she’s picked a jacket out for Brundle.
  EXPRESSION: null
- CHARACTER: Stathis
  LINE: I should have known it!
  EXPRESSION: Angry
- CHARACTER: Veronica
  LINE: What are y
  EXPRESSION: Shocked

::SCENE::
LOCATION: Store Aisle
MOOD: Tense
CHARACTERS: Stathis, Veronica, Narrator, Clerk
BACKGROUND_IMAGE: store_interior.png
BACKGROUND_EDIT: "Nighttime, public store aisle, clothes racks, shoppers in background"

::SCRIPT::
- CHARACTER: Stathis
  LINE: I followed you. Psychology Today, my ass. You stayed with Brundle all night. Why didn’t I believe you? I wonder.
  EXPRESSION: Accusatory
- CHARACTER: Narrator
  LINE: Stathis grabs the jacket out of her hand and holds it up to himself.
  EXPRESSION: Aggressive
- CHARACTER: Stathis
  LINE: Yeah, I think he’d look great in this, don’t you? I mean, for your TIME magazine cover you’ve gotta look good.
  EXPRESSION: Sarcastic
- CHARACTER: Veronica
  LINE: Listen Stath. Don’t you get it? I’m finally onto something that’s big. Huge.
  EXPRESSION: Defiant
- CHARACTER: Stathis
  LINE: Oh yeah? His cock?
  EXPRESSION: Crude
- CHARACTER: Veronica
  LINE: Crude, Stath. Very crude.
  EXPRESSION: Annoyed
- CHARACTER: Narrator
  LINE: Stathis throws the jacket at her - rather viciously.
  EXPRESSION: Aggressive
- CHARACTER: Stathis
  LINE: It's too perfect to believe! You’re a goddess. I give thanks to you for making my most paranoid fantasies come true!
  EXPRESSION: Sarcastic
- CHARACTER: Narrator
  LINE: He gets on his knees right in the middle of the aisle and bows down to her. Shoppers and clerks try to ignore them, hoping it will all just go away soon.
  EXPRESSION: Dramatic
- CHARACTER: Veronica
  LINE: I don’t have to report to you, you creep!
  EXPRESSION: Furious
- CHARACTER: Narrator
  LINE: She turns and starts to walk away.
  EXPRESSION: Angry
- CHARACTER: Narrator
  LINE: Stathis struggles to his feet.
  EXPRESSION: Strained
- CHARACTER: Stathis
  LINE: Ronnie! You’ve got to talk to me!
  EXPRESSION: Hurt
- CHARACTER: Veronica
  LINE: I don’t have to do anything! We’re finished, remember? I’ll spend the night anywhere I damn well please!
  EXPRESSION: Angry
- CHARACTER: Narrator
  LINE: She stomps over to the cash, where there is a pile of men's clothes already assembled.
  EXPRESSION: Determined
- CHARACTER: Veronica
  LINE: I’ll take this too.
  EXPRESSION: Decisive
- CHARACTER: Clerk
  LINE: Certainly.
  EXPRESSION: Neutral
- CHARACTER: Narrator
  LINE: Stathis watches from a distance, glowering.
  EXPRESSION: Resentful

::PATHS::
- CHOICE: null
  TARGET: null
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Lab
MOOD: Triumphant, then tense
CHARACTERS: Brundle, Veronica, Narrator
BACKGROUND_IMAGE: lab_interior.png
BACKGROUND_EDIT: "Nighttime, scientific lab with glowing telepod receiver, monitors, champagne"

::SCRIPT::
- CHARACTER: Narrator
  LINE: CLOSE-UP OF RECEIVER. The screen is filled with GLOWING LIGHT. AS THE CAMERA PULLS BACK, we realize it's the light of the receiver chamber.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: INTERCUTTING SHOTS...as the reintegration process completes its cycle.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: ON BRUNDLE...as he bites his nails, nervously waiting for the light to go out.
  EXPRESSION: Nervous
- CHARACTER: Narrator
  LINE: ON VERONICA... behind the stack of video monitors, recording it all.
  EXPRESSION: Focused
- CHARACTER: Narrator
  LINE: ON COMPUTER MONITOR...there is a computerized diagram of something forming...
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: ON RECEIVING CHAMBER DOOR...inside the same shape forming in the diagram is forming here. It is some sort of PRIMATE.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: ON MONITOR...the diagram is filling out more. We hear the machine shut off and the reflected light from the receiver disappears. The diagram of the ape starts to move, reflecting the movements of the actual subject in the telepod. Its statistics are also calculated on screen.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: ON RECEIVER DOOR...as Brundle opens it. Inside a SMALL MONKEY sits, apparently healthy, happy, and totally whole.
  EXPRESSION: Relieved
- CHARACTER: Narrator
  LINE: ANOTHER ANGLE. Brundle opens the receiver and the monkey playfully scrambles up his arm, clinging to his neck. Brundle smiles and strokes him.
  EXPRESSION: Happy
- CHARACTER: Narrator
  LINE: Making a cursory inspection of the monkey, Brundle takes it over to a table and deposits it in its CAGE. It chatters at him contentedly.
  EXPRESSION: Content
- CHARACTER: Narrator
  LINE: Brundle looks up into the lens of the nearest camera. He can barely suppress his pride and excitement.
  EXPRESSION: Proud
- CHARACTER: Brundle
  LINE: I think it’s time for champagne!
  EXPRESSION: Excited
- CHARACTER: Narrator
  LINE: Veronica flicks off the monitors and comes out from behind the stack to join Brundle.
  EXPRESSION: null
- CHARACTER: Veronica
  LINE: Oh, God, Brundle! It’s really happened! You did it! And all because you get car sick!
  EXPRESSION: Excited
- CHARACTER: Brundle
  LINE: Yeah, I did it! I really... Car sick?
  EXPRESSION: Exuberant
- CHARACTER: Veronica
  LINE: I finally figured it out. You came up with this so you wouldn’t have to travel in my car.
  EXPRESSION: Amused
- CHARACTER: Narrator
  LINE: They laugh, they kiss. We notice that Brundle is wearing new clothes, including the jacket that Stathis saw Veronica buying in the store.
  EXPRESSION: Affectionate
- CHARACTER: Narrator
  LINE: Brundle takes the bottle of champagne waiting in its cooler and struggles to pop the cork. He’s not really very good at it. Veronica gently takes over and does it for him while they talk.
  EXPRESSION: null
- CHARACTER: Veronica
  LINE: What next?
  EXPRESSION: Curious
- CHARACTER: Brundle
  LINE: I send the monkey out for tests, see if he’s really OK.
  EXPRESSION: Practical
- CHARACTER: Veronica
  LINE: How long will that take?
  EXPRESSION: Impatient
- CHARACTER: Brundle
  LINE: Could be weeks. Why?
  EXPRESSION: Questioning
- CHARACTER: Veronica
  LINE: I was thinking - we could take a holiday.
  EXPRESSION: Hopeful
- CHARACTER: Brundle
  LINE: We could?
  EXPRESSION: Pleased
- CHARACTER: Veronica
  LINE: Yeah. Like an old married couple. You know - the old man’s got a coupla weeks off, so they go to Florida, someplace warm.
  EXPRESSION: Playful
- CHARACTER: Brundle
  LINE: Just you and me?
  EXPRESSION: Inquiring
- CHARACTER: Veronica
  LINE: Why, is there somebody else you want to bring along?
  EXPRESSION: Teasing
- CHARACTER: Brundle
  LINE: No, no... it's just... is this a romance we’re having? Is that what it is?
  EXPRESSION: Uncertain
- CHARACTER: Narrator
  LINE: Veronica laughs and hugs him.
  EXPRESSION: Affectionate
- CHARACTER: Veronica
  LINE: Could be a romance.
  EXPRESSION: Playful
- CHARACTER: Narrator
  LINE: She’s about to pour the champagne when she spots a manila envelope on the table. It has the PARTICLE Magazine logo stamped on it, and clipped to it is a piece of expensive PARTICLE notepaper which says "From the Desk of Stathis Borans, Editor, PARTICLE Magazine." In handwriting, it says: "Thought you’d like to see this before it went to the printer. All my love, Stath.”
  EXPRESSION: null
- CHARACTER: Veronica
  LINE: What’s that?
  EXPRESSION: Suspicious
- CHARACTER: Brundle
  LINE: Somebody slipped it under the door. Hand delivered - there’s no postage.
  EXPRESSION: Informative
- CHARACTER: Narrator
  LINE: Veronica hands the champagne bottle to Brundle and rips open the envelope. It’s a mockup of the next issue of PARTICLE. On the cover is Brundle - in his new jacket (artists’s rendering). He’s been made to look a little crazed.
  EXPRESSION: Shocked
- CHARACTER: Narrator
  LINE: Under his photo it says, TELEPORTATION A REALITY? SETH BRUNDLE -Youthful Father of a New Age. In the background are sketched two telepods. The sketch of the telepods is all wrong - Stathis hasn’t actually seen the telepods - but the message is clear: Stathis intends to blow the entire deal.
  EXPRESSION: Threatening
- CHARACTER: Veronica
  LINE: Shit!
  EXPRESSION: Alarmed
- CHARACTER: Brundle
  LINE: What is it?
  EXPRESSION: Concerned
- CHARACTER: Narrator
  LINE: Veronica slips the magazine back into the envelope.
  EXPRESSION: Concealing
- CHARACTER: Veronica
  LINE: It’s...uh... just personal bullshit...
  EXPRESSION: Evasive
- CHARACTER: Brundle
  LINE: I thought old married couples shared all their personal bullshit. That’s how they stayed old and married.
  EXPRESSION: Suspicious
- CHARACTER: Veronica
  LINE: Don’t rush it, Brundle, and it’ll all happen. I’ve got to go out for a few hours.
  EXPRESSION: Tender
- CHARACTER: Brundle
  LINE: But... right now? The champagne...
  EXPRESSION: Disappointed
- CHARACTER: Veronica
  LINE: Just a few hours. I've still got the residue of another life, you know? I gotta scrape it off my shoe and get rid of it for once and for all.
  EXPRESSION: Determined
- CHARACTER: Narrator
  LINE: Veronica leaves.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Brundle sighs and pours himself a glass of champagne.
  EXPRESSION: Disappointed

::PATHS::
- CHOICE: null
  TARGET: null
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Monolith Publishing Building Exterior
MOOD: Establishing
CHARACTERS: Narrator
BACKGROUND_IMAGE: monolith_building_exterior.png
BACKGROUND_EDIT: "Nighttime, large corporate building, establishing shot"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Establishing shot.
  EXPRESSION: null

::PATHS::
- CHOICE: null
  TARGET: null
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Stathis's Offices
MOOD: Setting the scene
CHARACTERS: Narrator
BACKGROUND_IMAGE: stathis_office_interior.png
BACKGROUND_EDIT: "Nighttime, office interior"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The offices
  EXPRESSION: null

::PATHS::
- CHOICE: null
  TARGET: null
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Office
MOOD: Tense, Confrontational, then Emotional
CHARACTERS: Narrator, Veronica, Stathis, Janitor
BACKGROUND_IMAGE: office.png
BACKGROUND_EDIT: "Evening, almost deserted, janitor polishing floors, modern office setting"

::SCRIPT::
- CHARACTER: Narrator
  LINE: are all but deserted. A janitor is polishing the floors. Veronica walks in on Stathis and throws the magazine mockup on his desk.
  EXPRESSION: null
- CHARACTER: Veronica
  LINE: What’s this supposed to mean?
  EXPRESSION: Angry
- CHARACTER: Stathis
  LINE: It means that I’m your editor and I’m shaping your material into a story.
  EXPRESSION: Assertive
- CHARACTER: Veronica
  LINE: You’re the one who told me there was no story. You said Brundle was a con man.
  EXPRESSION: Angry
- CHARACTER: Stathis
  LINE: I've decided to trust your journalistic instincts.
  EXPRESSION: Sarcastic
- CHARACTER: Veronica
  LINE: Thanks a lot. But this isn't your story. It's mine.
  EXPRESSION: Defiant
- CHARACTER: Stathis
  LINE: Says who? I sent you to the Bartok party to see what you could find. Your discovery is my discovery.
  EXPRESSION: Challenging
- CHARACTER: Veronica
  LINE: Don't be a bastard.
  EXPRESSION: Angry
- CHARACTER: Stathis
  LINE: Don't be a bitch.
  EXPRESSION: Angry
- CHARACTER: Veronica
  LINE: You don't have anything.
  EXPRESSION: Confident
- CHARACTER: Stathis
  LINE: I have your tape. I have a lot of background on Brundle. He's been working on this thing for six years. There's material out there to find if you dig deep. I dug deep. Enough to unearth a cover story.
  EXPRESSION: Boastful
- CHARACTER: Veronica
  LINE: I'll sue you. I'll get an injunction!
  EXPRESSION: Threatening
- CHARACTER: Stathis
  LINE: Great! Let's play. But that's my game. You know that.
  EXPRESSION: Confident
- CHARACTER: Narrator
  LINE: Veronica flops into a chair with a big sigh. She's going to have to negotiate.
  EXPRESSION: Annoyed
- CHARACTER: Veronica
  LINE: What do you want from me?
  EXPRESSION: Resigned
- CHARACTER: Stathis
  LINE: I care about you and I worry about you. I want to know what’s going on. Everything.
  EXPRESSION: Concerned
- CHARACTER: Veronica
  LINE: I don’t want you to know everything.
  EXPRESSION: Resistant
- CHARACTER: Stathis
  LINE: You really like this guy. You’re fucking him. I hate it!
  EXPRESSION: Angry
- CHARACTER: Veronica
  LINE: Yeah, I like him. He’s funny.
  EXPRESSION: Defiant
- CHARACTER: Stathis
  LINE: You told me I was funny.
  EXPRESSION: Hurt
- CHARACTER: Veronica
  LINE: You were funny.
  EXPRESSION: Dismissive
- CHARACTER: Stathis
  LINE: Not any more, huh?
  EXPRESSION: Sarcastic
- CHARACTER: Veronica
  LINE: You’re scaring me.
  EXPRESSION: Afraid
- CHARACTER: Stathis
  LINE: I’m not a psychotic! I won’t hurt you!
  EXPRESSION: Yelling
- CHARACTER: Veronica
  LINE: Your gravity scares me.
  EXPRESSION: Afraid
- CHARACTER: Stathis
  LINE: I love you. Is that what you mean?
  EXPRESSION: Desperate
- CHARACTER: Veronica
  LINE: You’re in pain because of me. That scares me. I really don’t want that power. I wish you would take it back.
  EXPRESSION: Distressed
- CHARACTER: Stathis
  LINE: I wish I could. What do we do now?
  EXPRESSION: Resigned
- CHARACTER: Veronica
  LINE: Are you gonna wreck me with this Brundle thing?
  EXPRESSION: Concerned
- CHARACTER: Stathis
  LINE: You really think it's the Pulitzer Prize for little Ronnie Quaife, do you?
  EXPRESSION: Sarcastic
- CHARACTER: Veronica
  LINE: Stath! It's teleportation! It’s one of the great dreams - and it's on the verge of coming true! No more planes, trains, ships, cars, roads... Everything to do with transportation will become obsolete! And I'm right there in the middle of it - the only recorder of the event from the inside out!
  EXPRESSION: Excited
- CHARACTER: Stathis
  LINE: OK. OK. Look - just keep me informed, all right? As a friend, as a professional confidante. And if you need any help, you come to me.
  EXPRESSION: Calmer
- CHARACTER: Veronica
  LINE: That's all?
  EXPRESSION: Surprised
- CHARACTER: Stathis
  LINE: I don't want you to disappear from my life.
  EXPRESSION: Vulnerable
- CHARACTER: Narrator
  LINE: They kiss, delicately - a friendly kiss.
  EXPRESSION: null
- CHARACTER: Veronica
  LINE: OK.
  EXPRESSION: Calm
- CHARACTER: Stathis
  LINE: What about sex? I'm not saying love or affection. Just stress-relieving sex, you and me.
  EXPRESSION: Suggestive
- CHARACTER: Narrator
  LINE: Veronica laughs, stands up and heads for the door.
  EXPRESSION: Amused
- CHARACTER: Veronica
  LINE: You're disgusting - as always.
  EXPRESSION: Laughing
- CHARACTER: Stathis
  LINE: I wouldn't want to disappoint you.
  EXPRESSION: Witty

::PATHS::
- CHOICE: "Leave the office"
  TARGET: lab
  STATE_CHANGE: veronica_mood = 'relieved', stathis_mood = 'complicated'
  CONDITION: null

::SCENE::
LOCATION: Lab
MOOD: Ominous, Drunken, Suspenseful
CHARACTERS: Narrator, Brundle, Monkey, Fly
BACKGROUND_IMAGE: lab.png
BACKGROUND_EDIT: "Nighttime, scientific equipment, champagne bottles, dim lighting"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Brundle is drinking the champagne himself. He has let the monkey roam free and is playing with it. He’s a little drunk.
  EXPRESSION: null
- CHARACTER: Brundle
  LINE: "From the desk of Stathis Borans.” Sure. How about, "Under the desk of Stathis Borans." Is that where she is right now? Right. It’s the Ronnie game, and I’m catching on fast.
  EXPRESSION: Drunk
- CHARACTER: Narrator
  LINE: The monkey chatters amiably. A fly buzzes around its face. Brundle brushes it away.
  EXPRESSION: null
- CHARACTER: Brundle
  LINE: I never meant to kill your brother, you know. It was a mistake. Manslaughter but not homicide. As the general said, "There’s nothing I’d ask you to do that I wouldn’t do myself, boys. You know that."
  EXPRESSION: Drunk
- CHARACTER: Narrator
  LINE: This gives him an idea.
  EXPRESSION: null
- CHARACTER: Brundle
  LINE: Hey, you’re all right. I’m looking at you, and I can tell you’re OK. So - what are we waiting for? Let’s do it?
  EXPRESSION: Impulsive
- CHARACTER: Narrator
  LINE: He takes a hefty slug of champagne, then takes off his clothes.
  EXPRESSION: null
- CHARACTER: Brundle
  LINE: "All my love," huh? That means he’s her lover, doesn't it? "From the desk of your lover, Stathis Borans."
  EXPRESSION: Bitter
- CHARACTER: Narrator
  LINE: Brundle rises and walks up to the transmitter, examining it. He chews on a fingernail for a moment, then opens the door.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: ANOTHER ANGLE Brundle moves to each of the VIDEO CAMERAS and turns them on.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: He moves to the control board. He fingers the TIMER nervously, hesitating...he glances at the transmitter, then back at the timer.
  EXPRESSION: Nervous
- CHARACTER: Narrator
  LINE: The FLY buzzes about Brundle’s head. Brundle distractedly brushes the insect away.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: ON FLY THE CAMERA FOLLOWS THE FLY as it alights on the outside of the transmitter door.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: ON BRUNDLE Resets his empty champagne glass down on a table, still gazing at the control panel timer. He glances once more at the transmitter, then, heaving a deep sigh, turns once more to the timer, resolved to action.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: CLOSE ON BRUNDLE’S HAND As his fingers set the timer. A DIGITAL READOUT displays: ”00:20”...TWENTY SECONDS, then: ”00:19”.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: ON TRANSMITTER TELEPOD Brundle quickly enters it and closes the door. THE CAMERA MOVES IN CLOSE ON THE GLASS WINDOW OF THE TRANSMITTER DOOR. THERE WE SEE CRAWLING ACROSS THE PANE... THE FLY — BUT NOW ON THE INSIDE!
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: INTERCUTTING SHOTS...as the Transmission process commences.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: ON TIMER...the display readout has moved to "00:08.”
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: ON MASSIVE TELEPOD DOOR LATCH...as it slides shut with great finality.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: ON BRUNDLE...little droplets of sweat bead his brow as he stares down at the floor of the chamber...waiting...
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: ON FLY...crawling in the corner of the glass door, quite unnoticed by Brundle.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: ON TIMER...”00:04"
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: ON MONKEY... outside the door of the transmitter, pawing at it, watching Brundle inside -a strange reversal of the usual routine.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: ON BRUNDLE... noticing the monkey outside. He manages a nervous smile.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: ON VIDEO EYEPIECE MONITOR... as it dispassionately records everything.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: ON FLY... its buzzing drowned out by the hum of machinery.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: ON TIMER...as it goes from "00:01 to "00:00".
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: ON BRUNDLE...waiting...
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: ON MONITOR...Brundle’s outline is diagrammed, his vital statistics computed down to the minutest fraction. But not only Brundle is charted on the monitor -- so is the fly!
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: ON FLY...cra
  EXPRESSION: null

::PATHS::
- CHOICE: "Initiate teleportation"
  TARGET: end
  STATE_CHANGE: brundle_transformed = true, fly_integrated = true
  CONDITION: null

::SCENE::
LOCATION: Lab - Teleportation Chamber
MOOD: Intense, Suspenseful
CHARACTERS: Narrator, Brundle, Monkey
BACKGROUND_IMAGE: lab_telepod.png
BACKGROUND_EDIT: "Teleportation chamber, glowing light, scientific equipment"

::SCRIPT::
- CHARACTER: Narrator
  LINE: wling along the glass.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: ON BRUNDLE...anxious, sweat pouring from his brow.
  EXPRESSION: Anxious
- CHARACTER: Narrator
  LINE: ON MONKEY... cavorting outside the door.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: ON BRUNDLE'S EYES...seen only for an instant, before the ENTIRE SCREEN is filled with BRILLIANT LIGHT.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: ON MONKEY... as it screeches and runs in terror.
  EXPRESSION: Afraid
- CHARACTER: Narrator
  LINE: ON TRANSMITTER TELEPOD...its interior bathed in light, Brundle fading from view...
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: ON MONITOR...Brundle’s out line becomes fragmented. THE FLY has already disappeared!
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: ON TRANSMITTER TELEPOD...The light goes off, the chamber is empty. There is a FLASH OF LIGHT in another part of the room.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: ON RECEIVER...now full of light, the reintegration process has commenced. Brundle begins to re-form.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: ON MONITOR...duplicating Brundle’s reintegration in the receiver. A human outline fragmentedly appears.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: ON BRUNDLE...as the light shuts off abruptly. He shakes himself as though coming out of a daze.
  EXPRESSION: Surprised
- CHARACTER: Narrator
  LINE: Brundle opens the receiver door and steps out.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: THE CAMERA PANS PAST BRUNDLE TO THE INTERIOR OF THE GLASS WINDOW -- BUT THERE IS NOTHING THERE!
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Brundle looks around for his audience. He sees the monkey cowering on the sofa. Brundle smiles at it triumphantly.
  EXPRESSION: Happy
- CHARACTER: Brundle
  LINE: Now you tell me - am I different somehow? Is it live, or is it Memorex?
  EXPRESSION: Happy
- CHARACTER: Brundle
  LINE: Too bad you missed it, Ronnie. Too bad.
  EXPRESSION: Happy
- CHARACTER: Narrator
  LINE: In a mood of righteous anger, Brundle grabs the champagne bottle and finishes off the champagne.
  EXPRESSION: Angry

::PATHS::
- CHOICE: "Continue"
  TARGET: lab_warehouse_ext_night
  STATE_CHANGE: brundle_changed = true
  CONDITION: null

::SCENE::
LOCATION: Lab Warehouse Exterior
MOOD: Eerie, Quiet
CHARACTERS: Narrator, Veronica
BACKGROUND_IMAGE: lab_warehouse_ext.png
BACKGROUND_EDIT: "Deserted street, warehouse exterior, night, all lights out"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Veronica’s car pulls up and stops on the desterted street outside the lab warehouse. She gets out of the car and looks up. All the lights in the lab are out.
  EXPRESSION: null

::PATHS::
- CHOICE: "Enter the warehouse"
  TARGET: lab_warehouse_stairwell_night
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Lab Warehouse Stairwell
MOOD: Spooky, Solitary
CHARACTERS: Narrator, Veronica
BACKGROUND_IMAGE: lab_warehouse_stairwell.png
BACKGROUND_EDIT: "Dark stairwell, night, echoey"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Veronica makes her way up the stairs. It is spooky there in the dark, alone with the echo of her footsteps.
  EXPRESSION: Afraid

::PATHS::
- CHOICE: "Proceed into the lab"
  TARGET: lab_living_room_night
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Lab Living Room Area
MOOD: Anticipatory
CHARACTERS: Narrator, Veronica
BACKGROUND_IMAGE: lab_living_room.png
BACKGROUND_EDIT: "Interior of lab, living room area, dark, night"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Veronica slides open the big front door. No sign of Brundle.
  EXPRESSION: null

::PATHS::
- CHOICE: "Check the bedroom"
  TARGET: lab_bedroom_night
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Lab Bedroom
MOOD: Intimate, Tense
CHARACTERS: Narrator, Veronica, Brundle
BACKGROUND_IMAGE: lab_bedroom.png
BACKGROUND_EDIT: "Bedroom, night, intimate lighting"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Veronica creeps in to Brundle’s bedroom. He’s asleep. She slips off her clothes and gets into bed with him. She gently strokes his shoulder.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Brundle stirs, wakes up, turns sleepily to Veronica.
  EXPRESSION: null
- CHARACTER: Brundle
  LINE: I missed you last night.
  EXPRESSION: Sleepy
- CHARACTER: Veronica
  LINE: It’s still night. I came back. You had to celebrate without me. I'm sorry.
  EXPRESSION: Sad
- CHARACTER: Brundle
  LINE: I went through last night.
  EXPRESSION: Neutral
- CHARACTER: Veronica
  LINE: You went through? Without testing the monkey?
  EXPRESSION: Surprised
- CHARACTER: Brundle
  LINE: I was a bit drunk. I was upset.
  EXPRESSION: Ashamed
- CHARACTER: Veronica
  LINE: You could have killed yourself! You’re like a little pouty kid. I can’t believe it!
  EXPRESSION: Angry
- CHARACTER: Brundle
  LINE: Me neither. I keep surprising myself. Are you sleeping with Stathis Borans?
  EXPRESSION: Curious
- CHARACTER: Veronica
  LINE: What are you talking about?
  EXPRESSION: Surprised
- CHARACTER: Brundle
  LINE: I dunno. I just have that feeling...
  EXPRESSION: Suspicious
- CHARACTER: Veronica
  LINE: That's why you were upset?
  EXPRESSION: Surprised
- CHARACTER: Brundle
  LINE: I got jealous.
  EXPRESSION: Ashamed
- CHARACTER: Veronica
  LINE: Oh, God. But... you don't have to be jealous. He’s an old boyfriend. He was teaching at college, I was a science major. He got me started in journalism.
  EXPRESSION: Explaining
- CHARACTER: Brundle
  LINE: Did you manage to scrape him off your shoe?
  EXPRESSION: Sarcastic
- CHARACTER: Veronica
  LINE: We’re just platonic. We talk business.
  EXPRESSION: Neutral
- CHARACTER: Brundle
  LINE: Is he still in love with you?
  EXPRESSION: Curious
- CHARACTER: Veronica
  LINE: How could he not be? What about our deal? You went through and I wasn’t there!
  EXPRESSION: Playful
- CHARACTER: Brundle
  LINE: Don’t worry. I taped it for you.
  EXPRESSION: Reassuring
- CHARACTER: Veronica
  LINE: You did?
  EXPRESSION: Surprised
- CHARACTER: Narrator
  LINE: Brundle nods.
  EXPRESSION: null
- CHARACTER: Veronica
  LINE: But why? You were mad at me.
  EXPRESSION: Confused
- CHARACTER: Brundle
  LINE: I wanted to hurt you. But I'm finding that if I don’t share everything with you, then it's... as if it hasn’t really happened.
  EXPRESSION: Thoughtful
- CHARACTER: Veronica
  LINE: That sounds like love.
  EXPRESSION: Soft
- CHARACTER: Brundle
  LINE: It does?
  EXPRESSION: Surprised
- CHARACTER: Veronica
  LINE: Yeah, it does.
  EXPRESSION: Soft
- CHARACTER: Narrator
  LINE: She kisses him. They begin to make love.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The camera finds Veronica's hands as they clasp Brundle, then follows one of her hands as it moves down Brundle's side. There, we see that the skin in the area of the three scratches has taken on a strange, rough texture. Even more startling, we see that HAIRS are growing out of the scratches - three from the top one, one from the middle scratch. And these hairs are decidedly NOT HUMAN: they are coarse, strong, and METALLIC-GREEN in color.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Veronica’s fingers glide past the hairs without quite touching them.
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue to next morning"
  TARGET: lab_bedroom_very_early_morning
  STATE_CHANGE: brundle_transformation_hint = true
  CONDITION: null

::SCENE::
LOCATION: Lab Bedroom
MOOD: Mysterious, Observant
CHARACTERS: Narrator, Brundle, Fly
BACKGROUND_IMAGE: lab_bedroom_close_up.png
BACKGROUND_EDIT: "Close-up of Brundle asleep, very early morning light"

::SCRIPT::
- CHARACTER: Narrator
  LINE: CU BRUNDLE, asleep, lying on his back. We hear a faint buzzing. A FLY hovers near Brundle's cheek, then lands.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: He unconsciously brushes it away.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The FLY continues to buzz over Brundle's head. Suddenly, Brundle makes an instinctive, eyes-closed grab for the insect.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: With an amazing display of reflexes and speed, Brundle’s hand sweeps through the air and snatches the fly. We hear it BUZZING in Brundle’s hand.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The hand has not moved. Brundle’s arm remains in mid-air.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: His fist clenches. He opens his eyes, now stone-cold awake, fully realizing what he’s done.
  EXPRESSION: Surprised
- CHARACTER: Narrator
  LINE: Brundle stares up at his hand. He slowly opens his fingers, releasing the fly. It buzzes off.
  EXPRESSION: Thoughtful
- CHARACTER: Narrator
  LINE: Brundle stares up at his hand, wondering about the feat he just performed. Blind luck? A fluke? Or something more? He flexes his fingers open and shut several times.
  EXPRESSION: Curious
- CHARACTER: Narrator
  LINE: He smiles.
  EXPRESSION: Happy
- CHARACTER: Narrator
  LINE: Brundle, totally nude, sits up on the edge of the bed, staring at his hands in curious pleasure. He turns, notices VERONICA in bed with him. He smiles at her sleeping form, turns, rubs his hands over his own chest.
  EXPRESSION: Happy

::PATHS::
- CHOICE: "Wake up later"
  TARGET: lab_bedroom_morning
  STATE_CHANGE: brundle_enhanced_senses = true
  CONDITION: null

::SCENE::
LOCATION: Lab Bedroom
MOOD: Curious, Slightly Nervous
CHARACTERS: Narrator, Veronica
BACKGROUND_IMAGE: lab_bedroom_morning.png
BACKGROUND_EDIT: "Bedroom, morning light, empty bed"

::SCRIPT::
- CHARACTER: Narrator
  LINE: CU VERONICA
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Veronica wakes up. She hears noise, motion in the lab.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: She turns to Brundle, but he’s no longer in bed with her.
  EXPRESSION: Surprised
- CHARACTER: Narrator
  LINE: Still half asleep, slightly nervous, Veronica gets up out of bed and follows the sound.
  EXPRESSION: Curious

::PATHS::
- CHOICE: "Investigate the sound"
  TARGET: lab_main_area_morning
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Lab Main Area
MOOD: Puzzled, Wondrous
CHARACTERS: Narrator, Veronica, Brundle
BACKGROUND_IMAGE: lab_main_area.png
BACKGROUND_EDIT: "Lab interior, morning light, half wall separating areas"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Veronica peers tentatively around the corner of the half wall which separates the bedroom from the lab proper and finds herself looking at a strangely beautiful and unexpected sight.
  EXPRESSION: Surprised
- CHARACTER: Narrator
  LINE: Brundle, nude, bathed in shafts of soft morning light which highlight the rough textures of the warehouse walls and floors, is performing a series of slow, complex, hig
  EXPRESSION: null

::PATHS::
- CHOICE: "Approach Brundle"
  TARGET: end
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Lab
MOOD: Astonishment
CHARACTERS: Veronica, Brundle
BACKGROUND_IMAGE: lab_interior.png
BACKGROUND_EDIT: "Interior of a lab, with exposed pipes and wooden studs"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Brundle performs highly controlled gymnastic maneuvers on the pipes and wooden studs which link the pillars of the lab.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Veronica is quietly astonished. She walks slowly into the lab, drawn and hypnotized by the beauty of the moment, not wanting to disturb it.
  EXPRESSION: Awe
- CHARACTER: Narrator
  LINE: But soon she finds herself reaching out to touch Brundle as he twists and turns in slow motion. The spell doesn’t break; it’s as though he expected her. Brundle keeps performing, now with a sweet, shy smile.
  EXPRESSION: null
- CHARACTER: Veronica
  LINE: I didn’t know you could do that stuff.
  EXPRESSION: Surprised
- CHARACTER: Brundle
  LINE: When I woke up, I felt like doing this. And I just started to do it.
  EXPRESSION: Happy
- CHARACTER: Brundle
  LINE: I always... thought I could do something like this if I just... wanted to enough.
  EXPRESSION: Reflective
- CHARACTER: Narrator
  LINE: Brundle finally stops his exercises and stands squarely in front of Veronica. He is sweating, breathing hard.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: He’s the same Brundle, and yet... he seems so much more physically self-aware, vibrant.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Veronica studies him carefully. She touches him again, traces the line of his collarbone with her finger. She takes his hand in hers and kisses it with great tenderness.
  EXPRESSION: Loving

::PATHS::
- CHOICE: "Continue to the next day"
  TARGET: tv_interview
  STATE_CHANGE: brundle_changed = true, veronica_curious = true
  CONDITION: null

::SCENE::
LOCATION: TV Broadcast
MOOD: Informative
CHARACTERS: Brundle (ON TAPE), Veronica (OC)
BACKGROUND_IMAGE: tv_screen.png
BACKGROUND_EDIT: "Close-up of Brundle being interviewed on a TV screen"

::SCRIPT::
- CHARACTER: Narrator
  LINE: From time to time we cut to the live (film) version of these same images. When We are live, we also see reactions from Veronica.
  EXPRESSION: null
- CHARACTER: Veronica
  LINE: We've just seen the first teleportation of a human being. Dr. Seth Brundle, how did it feel going through? What did it feel like?
  EXPRESSION: Neutral
- CHARACTER: Brundle
  LINE: It feels like a stutter.
  EXPRESSION: Thoughtful
- CHARACTER: Veronica
  LINE: A what?
  EXPRESSION: Questioning
- CHARACTER: Brundle
  LINE: A stutter. A hiccup. A slight dislocation of my physical life. Not unpleasant. Just a title interruption of rhythm. For a second I thought it didn't work. I thought I was in the same telepod I started out in.
  EXPRESSION: Explaining
- CHARACTER: Veronica
  LINE: And did you feel at all different?
  EXPRESSION: Questioning
- CHARACTER: Brundle
  LINE: A little... unbalanced. That's all.
  EXPRESSION: Calm
- CHARACTER: Veronica
  LINE: And now?
  EXPRESSION: Questioning
- CHARACTER: Brundle
  LINE: I should feel exactly the same as before, but I don’t. I’m not complaining. I feel very - coordinated. And very energized. I feel as though I work better, physically. Everything seems to just - work together better than it ever did before.
  EXPRESSION: Confident
- CHARACTER: Veronica
  LINE: Why should that be?
  EXPRESSION: Questioning
- CHARACTER: Brundle
  LINE: It’s possible that the teleporter has somehow... improved me.
  EXPRESSION: Speculative
- CHARACTER: Veronica
  LINE: But that's fantastic! How is it possible?
  EXPRESSION: Excited
- CHARACTER: Brundle
  LINE: In reassembling me it might have - this is just a guess - but it might have just - seen where things could be improved - theoretically, and it did it. I told it to be creative, and I guess it has been.
  EXPRESSION: Explaining
- CHARACTER: Veronica
  LINE: Could this ever be dangerous?
  EXPRESSION: Concerned
- CHARACTER: Brundle
  LINE: Well, it's certainly unexpected. The monkeys don't seem to exhibit any changes from their norm at all. We’ll see when they come back from testing.
  EXPRESSION: Calm
- CHARACTER: Veronica
  LINE: But you haven’t really answered me. Could this be dangerous?
  EXPRESSION: Concerned
- CHARACTER: Brundle
  LINE: It feels too perfect to be dangerous.
  EXPRESSION: Confident
- CHARACTER: Veronica
  LINE: You like the way it feels?
  EXPRESSION: Questioning
- CHARACTER: Brundle
  LINE: Yes, I do.
  EXPRESSION: Happy
- CHARACTER: Brundle
  LINE: Want to try it?
  EXPRESSION: Playful

::PATHS::
- CHOICE: "Observe Veronica's reaction"
  TARGET: veronica_reaction
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Unknown (Veronica's location, watching TV)
MOOD: Apprehensive
CHARACTERS: Veronica
BACKGROUND_IMAGE: veronica_closeup.png
BACKGROUND_EDIT: "Close-up of Veronica's face, live"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Veronica shakes her head "No."
  EXPRESSION: Disapproving

::PATHS::
- CHOICE: "Transition to outdoor market"
  TARGET: kensington_market
  STATE_CHANGE: veronica_hesitant = true
  CONDITION: null

::SCENE::
LOCATION: Kensington Outdoor Market
MOOD: Lively
CHARACTERS: Brundle, Veronica
BACKGROUND_IMAGE: kensington_market.png
BACKGROUND_EDIT: "Bustling outdoor market, daytime"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Lyrical montage as Brundle and Veronica walk the lively, bustling streets of Kensington Market hand in hand.
  EXPRESSION: null

::PATHS::
- CHOICE: "Go to a cafe"
  TARGET: italian_cafe
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Italian Sidewalk Cafe
MOOD: Concerned
CHARACTERS: Brundle, Veronica
BACKGROUND_IMAGE: italian_cafe.png
BACKGROUND_EDIT: "Outdoor cafe, close on a cup of cappuccino"

::SCRIPT::
- CHARACTER: Narrator
  LINE: We are CLOSE on a cup of cappuccino. Brundle’s hand comes into the shot and begins to dump spoonful after spoonful of sugar into the cup.
  EXPRESSION: null
- CHARACTER: Brundle
  LINE: ... so I asked the computer if it had improved me and it said it didn’t know what I was talking about.
  EXPRESSION: Explaining
- CHARACTER: Narrator
  LINE: We pull back to see VERONICA sitting across from Brundle, watching him with some CONCERN. They sit at a table under an Alfa Romeo umbrella - a small Italian sidewalk café.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: She bites a fingernail - Brundle’s habit - as the FIFTH TEASPOON OF SUGAR is dumped into the cup, but says nothing. Brundle, excited, wired-up, doesn’t seem to notice that he is doing anything odd. He speaks with a rapid fervour.
  EXPRESSION: Concerned
- CHARACTER: Brundle
  LINE: That made me think very carefully about what I’m feeling and why. I'm beginning to think that the sheer process of being taken apart, atom by atom, and then put back together again, why, it's like coffee being put through a filter. It's somehow a purifying process, it's purified me, it's cleansed me, it's allowed me to realize the personal potential I've been neglecting all these years that I've been obsessively pursuing goal after goal...
  EXPRESSION: Manic
- CHARACTER: Narrator
  LINE: Brundle has been stirring the sugar into the cappuccino.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Now he pauses to drain the cup - without the slightest reaction to the incredible sweetness of the drink. He puts the cup down.
  EXPRESSION: null
- CHARACTER: Veronica
  LINE: Do you normally take coffee with your sugar?
  EXPRESSION: Sarcastic
- CHARACTER: Brundle
  LINE: What?
  EXPRESSION: Confused
- CHARACTER: Narrator
  LINE: Veronica just shakes her head. Brundle reaches across the table and takes her hand. He continues to rattle on with incredible intensity.
  EXPRESSION: null
- CHARACTER: Brundle
  LINE: I just don't think I've ever given me a chance to be me. And now that I’ve achieved what will probably prove to be my life’s work... I can be me, the real me, at last.
  EXPRESSION: Intense
- CHARACTER: Narrator
  LINE: For some reason, Veronica finds herself looking away.
  EXPRESSION: Uneasy

::PATHS::
- CHOICE: "Go to the lab bedroom"
  TARGET: lab_bedroom
  STATE_CHANGE: veronica_uneasy = true, brundle_manic = true
  CONDITION: null

::SCENE::
LOCATION: Lab Bedroom
MOOD: Tense
CHARACTERS: Veronica, Brundle
BACKGROUND_IMAGE: lab_bedroom.png
BACKGROUND_EDIT: "Bedroom, late day, intimate setting"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Veronica and Brundle are in bed making love - but something’s wrong. Veronica pushes Brundle away and rolls over in the bed, obviously exhausted.
  EXPRESSION: Exhausted
- CHARACTER: Veronica
  LINE: I've got to stop. I have to sleep.
  EXPRESSION: Exhausted
- CHARACTER: Narrator
  LINE: Brundle begins to caress her, kiss her.
  EXPRESSION: null
- CHARACTER: Brundle
  LINE: Not yet.
  EXPRESSION: Demanding
- CHARACTER: Narrator
  LINE: Veronica sits up to get away from him.
  EXPRESSION: null
- CHARACTER: Veronica
  LINE: I’ve got to. How can you keep going? You can't possibly have any fluid left in your body. We’ve been doing this for hours.
  EXPRESSION: Exasperated
- CHARACTER: Narrator
  LINE: Brundle sits up behind her and begins to kiss her shoulder.
  EXPRESSION: null
- CHARACTER: Brundle
  LINE: I’m not ready to stop.
  EXPRESSION: Insistent
- CHARACTER: Narrator
  LINE: Despite her fatigue, Veronica begins to respond. She holds Brundle, runs her hands down his back. Suddenly, she feels something that disturbs her. She stops, pulls away, searches Brundle’s body for whatever it was she felt.
  EXPRESSION: Disturbed
- CHARACTER: Veronica
  LINE: Hey, what’s this?
  EXPRESSION: Worried
- CHARACTER: Brundle
  LINE: It’s an attempt to distract me, that’s what it is.
  EXPRESSION: Dismissive
- CHARACTER: Veronica
  LINE: N
  EXPRESSION: Concerned

::PATHS::
- CHOICE: "Investigate what Veronica felt"
  TARGET: end
  STATE_CHANGE: brundle_changes_continue = true, veronica_fear = +1
  CONDITION: null

::SCENE::
LOCATION: Brundle's Apartment - Bedroom
MOOD: Anxious, Manic
CHARACTERS: Narrator, Brundle, Veronica
BACKGROUND_IMAGE: null
BACKGROUND_EDIT: null

::SCRIPT::
- CHARACTER: Veronica
  LINE: I’m serious. Look at these.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Brundle lifts his arm and cranes his head around to get a look. What he sees are the STRANGE, METALLIC-GREEN HAIRS growing out of the scratches in his back - only now there are more of them, and they are longer, almost... bristly.
  EXPRESSION: null
- CHARACTER: Brundle
  LINE: Happens when you get older. Weird hair configurations.
  EXPRESSION: Not Concerned
- CHARACTER: Veronica
  LINE: They’re very coarse.
  EXPRESSION: null
- CHARACTER: Brundle
  LINE: I’ve never really been hairy enough, you know what I mean? Always too boyish. I’m looking forward to a hairy body. One of the compensations of old age.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Veronica jumps up and grabs a pair of toenail scissors from the edge of the sink. She flops back down onto the bed and begins to attack the hairs with the scissors.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Brundle protests - but not seriously.
  EXPRESSION: null
- CHARACTER: Brundle
  LINE: Hey - not my new hairs!
  EXPRESSION: null
- CHARACTER: Veronica
  LINE: Relax, Brundle. I don’t think you really want a body covered with these. God, they’re really tough!
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Veronica is having difficulty getting the scissors to cut through the hairs. Finally, she gets the first one trimmed off and starts on the next one. Brundle sits happily on the bed and begins to speed-rap again.
  EXPRESSION: null
- CHARACTER: Brundle
  LINE: Listen. I want you to go through. I want to teleport you. As soon as possible. Right now. You’ll feel incredible. Ronnie - I hardly need to sleep any more. And I feel wonderful. It’s like a drug, but a perfectly pure and benign drug. The power I feel surging inside me - you’ll feel fantastic. And I won’t be able to wear you out... We’ll be the perfect couple. The dynamic duo! C’mon. Right now!
  EXPRESSION: Speedy but Happy
- CHARACTER: Narrator
  LINE: He grabs her by the arm and begins to pull her off the bed. She pulls back, shrinking away from his craziness.
  EXPRESSION: null
- CHARACTER: Veronica
  LINE: Hey, lay off, will you? Don’t give me that born-again teleportation rap. I told you I was scared to do it. What more do I need to say? I’m not going to do it!
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: When he sees that she’s resisting, he lets go.
  EXPRESSION: null
- CHARACTER: Brundle
  LINE: You're a fucking drag, you know that?
  EXPRESSION: Angry
- CHARACTER: Narrator
  LINE: Veronica looks at Brundle, wide-eyed.
  EXPRESSION: Surprised
- CHARACTER: Veronica
  LINE: Something went wrong, Brundle. When you went through. Something went wrong.
  EXPRESSION: Very Quietly
- CHARACTER: Narrator
  LINE: Brundle completely ignores her words. He begins to throw on an outrageously wrong combination of clothes.
  EXPRESSION: null
- CHARACTER: Brundle
  LINE: No? Not you? You’re too chicken-shit to be a member of the dynamic duo club? OK, then, great, I’ll find somebody else. Somebody who can keep up with me!
  EXPRESSION: null
- CHARACTER: Veronica
  LINE: Brundle, you’ve got to listen to me!
  EXPRESSION: Frustrated
- CHARACTER: Brundle
  LINE: You’re afraid to dive into the plasma pool, aren’t you? You’re afraid to be destroyed and reconsidered, aren’t you? You might think you were the one to teach me about the flesh, but you only know society’s straight line about the flesh, you can’t penetrate beyond society’s sick, gray fear of the flesh! Drink deep, or taste not the plasma spring, you see what I’m sayin’...? I’m not just talking about sex and penetration, I’m talking PENETRATION beyond the veil of the flesh, a deep, penetrating dive into the plasma pool...!
  EXPRESSION: Angry, Speedy
- CHARACTER: Narrator
  LINE: Brundle storms out the door, slamming it behind him.
  EXPRESSION: null
- CHARACTER: Veronica
  LINE: No! Brundle, please, wait!
  EXPRESSION: Panicked
- CHARACTER: Narrator
  LINE: Veronica slides open the heavy door, thinking she might run after him - but the sound of his footsteps tells her she’ll never catch him: he’s fast, and he's gone.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: She comes back in, distraught but thinking. She goes back to the bed and looks for something in the twisted sheets.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: She soon finds what she’s looking for - the FOUR OR FIVE STRANGE METALLIC-GREEN HAIRS she managed to trim from Brundle’s back.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Veronica lays the hairs out on the night table, then picks up the longest one and studies it in the light of the bed-lamp.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: It’s coarse and very animal-like, but also somehow beautiful in its iridescent greenness.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Veronica dumps an old telephone bill out of its envelope and drops all the hairs into the envelope for safe-keeping.
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue"
  TARGET: downtown_street
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Downtown Street
MOOD: Driven, Ominous
CHARACTERS: Narrator, Brundle
BACKGROUND_IMAGE: null
BACKGROUND_EDIT: "Neon-lit, night"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Brundle stalks the neon-lit downtown streets, looking for a place to put his seething energy.
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue"
  TARGET: bar_entrance
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Bar Entrance
MOOD: Grimy, Seeking
CHARACTERS: Narrator, Brundle, Shady Women, Hungry Men
BACKGROUND_IMAGE: null
BACKGROUND_EDIT: "Night, three or four shady women and hungry men at entrance"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Brundle spots a bar that looks just about right - three or four shady women hanging around the entrance, along with an assortment of hungry men. Brundle pushes through the small group at the entrance and enters the bar.
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue"
  TARGET: bar_interior
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Bar Interior
MOOD: Aggressive, Predatory, Chaotic
CHARACTERS: Narrator, Brundle, Tawny, Marky, Second Man, Bartender
BACKGROUND_IMAGE: null
BACKGROUND_EDIT: "Garish neon lighting, night"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Brundle stands alone at the bar. In the garish neon of the place he no longer looks friendly and cuddly; he is angry, manic and, somehow... predatory.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Two large men with tattoos on their arms are arm-wrestling at a small table, egged on by a VOLUPTUOUSLY SLEAZY WOMAN. Beer is sloshing everywhere as the men struggle for an advantage.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The bartender puts a drink down - a double Scotch - in front of Brundle, who is in the process of unwrapping an O’Henry chocolate bar. The bartender winces as Brundle bites off a piece of chocolate then washes it down with some Scotch.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Brundle gets up and, still munching on his bar, begins to drift over to the table and the sleazy woman, whose name is TAWNY.
  EXPRESSION: null
- CHARACTER: Brundle
  LINE: Who’s winning?
  EXPRESSION: null
- CHARACTER: Tawny
  LINE: Dunno. Hope it’s Marky.
  EXPRESSION: null
- CHARACTER: Brundle
  LINE: How come?
  EXPRESSION: null
- CHARACTER: Tawny
  LINE: ’Cause the winner wins me, and I like Marky tonight.
  EXPRESSION: null
- CHARACTER: Brundle
  LINE: Yeah? Well, I like you tonight. Maybe I’d better get involved in this, too.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The two men ease off their wrestling. The biggest one, MARKY, grabs Brundle by the lapels.
  EXPRESSION: null
- CHARACTER: Marky
  LINE: You’re disturbing us.
  EXPRESSION: Annoyed
- CHARACTER: Brundle
  LINE: I got a hundred bucks says I can beat either one of you.
  EXPRESSION: Confident
- CHARACTER: Narrator
  LINE: The men laugh. Marky grabs Brundle’s arm and rips his jacket sleeve right off. He folds Brundle’s arm back and displays it to Tawny.
  EXPRESSION: null
- CHARACTER: Marky
  LINE: Like those biceps, Tawny?
  EXPRESSION: Taunting
- CHARACTER: Second Man
  LINE: Hey, I know his secret. He eats chocolates and peanuts for energy!
  EXPRESSION: Grabbing chocolate bar, slurping
- CHARACTER: Narrator
  LINE: They howl in laughter. Brundle pulls out a hundred-dollar bill which has been wadded up in his pocket. He slams the hundred on the table.
  EXPRESSION: null
- CHARACTER: Brundle
  LINE: A hundred. And I get to take the lady home for the night if I win.
  EXPRESSION: Confident
- CHARACTER: Tawny
  LINE: Says who?
  EXPRESSION: Questioning
- CHARACTER: Marky
  LINE: Hey
  EXPRESSION: Surprised

::PATHS::
- CHOICE: "Continue"
  TARGET: end_of_excerpt
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Bar
MOOD: Tense, then Gruesome
CHARACTERS: Marky, Tawny, Brundle, Second Man, Spectators, Narrator
BACKGROUND_IMAGE: bar_interior.png
BACKGROUND_EDIT: "Nighttime, dimly lit, crowded with a few spectators"

::SCRIPT::
- CHARACTER: Marky
  LINE: - an easy hundred, Tawny.
  EXPRESSION: Confident
- CHARACTER: Tawny
  LINE: Yeah, but says who? It’s the idea of it. I ain’t no hooker.
  EXPRESSION: Disgusted
- CHARACTER: Narrator
  LINE: Marky ignores her and sits down, ready to rumble.
  EXPRESSION: null
- CHARACTER: Marky
  LINE: C’mon, let’s get it over with.
  EXPRESSION: Eager
- CHARACTER: Narrator
  LINE: Having said her piece, Tawny sits down to enjoy the fun.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Brundle sits down opposite Marky. They spend a few minutes gripping and re-gripping each other’s hand under the scrutiny of the second man. A few spectators accumulate around the table.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Finally, they’re ready to wrestle.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: ON BRUNDLE, as they start.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: ON MARKY, confident.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: ON BRUNDLE, having no trouble.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: ON TAWNY, wondering what’s happening.
  EXPRESSION: Confused
- CHARACTER: Narrator
  LINE: ON MARKY, his confidence turning to mush as he meets the steel in Brundle’s skinny forearm.
  EXPRESSION: Losing Confidence
- CHARACTER: Narrator
  LINE: The tension is building between the two arms: they are shaking.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: CU BRUNDLE - he’s doing well but it’s an effort.
  EXPRESSION: Strained
- CHARACTER: Narrator
  LINE: CU BRUNDLE’S FINGERTIPS - the hand that’s wrestling.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Under the pressure of the fight, a STRANGE, PUS-LIKE SECRETION begins to ooze from under his fingernails and down the back of Marky’s hand. It goes unnoticed in the general sweat and beer.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The strain is enormous. Veins are bulging. Arms are quivering. Muscles are fibrillating. Then SUDDENLY, all the pent-up energy is released with a sickening CRACK!
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: as MARKY’S FOREARM SHATTERS! Splintered bone slices out through the skin of Marky’s wristband glints in the icy light of the bar.
  EXPRESSION: null
- CHARACTER: Marky
  LINE: (shrieks)
  EXPRESSION: Agonized
- CHARACTER: Narrator
  LINE: Brundle lets go. Marky holds his arm and stares at it as though it belonged to someone else. His hand dangles at an impossible angle; the piece of cracked ulna looks white as a tooth. The second man and Tawny look on in disbelief.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: People begin to gather around. Marky starts to moan as blood begins to well up in a serious way and spill out of the wound onto the table top.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Brundle grabs his hundred dollars in one hand and takes Tawny by the wrist with the other. She's stunned and she lets herself be dragged out of the bar.
  EXPRESSION: null

::PATHS::
- CHOICE: "Leave the bar"
  TARGET: ext_bar_night
  STATE_CHANGE: brundle_power = +1, tawny_impressed = +1
  CONDITION: null

::SCENE::
LOCATION: Outside Bar
MOOD: Amazement, Proposition
CHARACTERS: Brundle, Tawny, Narrator
BACKGROUND_IMAGE: bar_exterior.png
BACKGROUND_EDIT: "Nighttime, street outside a dive bar"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Once Brundle and Tawny are out on the street, Tawny recovers enough to talk.
  EXPRESSION: null
- CHARACTER: Tawny
  LINE: Jesus! Are you a body-builder or something?
  EXPRESSION: Amazed
- CHARACTER: Brundle
  LINE: Yeah, I build bodies. I take ’em apart and then I put ’em back together again.
  EXPRESSION: Eerie
- CHARACTER: Tawny
  LINE: You sure took Marky apart.
  EXPRESSION: Admiring
- CHARACTER: Brundle
  LINE: Let’s go back to my place.
  EXPRESSION: Suggestive
- CHARACTER: Tawny
  LINE: Your place? Yeah, well, OK. I live with my mother anyway. But could we go to a few more bars first? It’s too early to quit.
  EXPRESSION: Coy
- CHARACTER: Brundle
  LINE: Sure. A few more bars.
  EXPRESSION: Agreeable

::PATHS::
- CHOICE: "Continue to bars (and eventually his place)"
  TARGET: ext_lab_warehouse_early_morning
  STATE_CHANGE: tawny_curiosity = +1, brundle_intent = +1
  CONDITION: null

::SCENE::
LOCATION: Lab Warehouse Exterior
MOOD: Exhausted, New Beginnings
CHARACTERS: Brundle, Tawny, Narrator
BACKGROUND_IMAGE: lab_warehouse_exterior.png
BACKGROUND_EDIT: "Early morning light, industrial building"

::SCRIPT::
- CHARACTER: Narrator
  LINE: A cab pulls up outside. Brundle and Tawny get out, blinking in the early morning light.
  EXPRESSION: null

::PATHS::
- CHOICE: "Enter the warehouse"
  TARGET: int_lab_warehouse_stairwell_early_morning
  STATE_CHANGE: tawny_tired = +1
  CONDITION: null

::SCENE::
LOCATION: Lab Warehouse Stairwell
MOOD: Humorous, Energetic
CHARACTERS: Brundle, Tawny, Narrator
BACKGROUND_IMAGE: stairwell_interior.png
BACKGROUND_EDIT: "Early morning, long, industrial stairwell"

::SCRIPT::
- CHARACTER: Tawny
  LINE: Oh, no. No elevator. I’ll never make it.
  EXPRESSION: Exasperated
- CHARACTER: Brundle
  LINE: There is an elevator.
  EXPRESSION: Playful
- CHARACTER: Narrator
  LINE: Brundle picks her up effortlessly.
  EXPRESSION: null
- CHARACTER: Brundle
  LINE: Don’t you feel elevated?
  EXPRESSION: Playful
- CHARACTER: Narrator
  LINE: He sprints up the ten flights of stairs with Tawny in his arms.
  EXPRESSION: null
- CHARACTER: Tawny
  LINE: You’re sure in good shape for somebody who only eats candy bars.
  EXPRESSION: Impressed

::PATHS::
- CHOICE: "Reach the lab"
  TARGET: int_lab_morning
  STATE_CHANGE: brundle_strength = +1
  CONDITION: null

::SCENE::
LOCATION: Lab
MOOD: Scientific, Wondrous, then Tense and Ominous
CHARACTERS: Brundle, Tawny, Veronica, Narrator
BACKGROUND_IMAGE: lab_interior.png
BACKGROUND_EDIT: "Morning, cluttered scientific lab with telepods, mattress"

::SCRIPT::
- CHARACTER: Narrator
  LINE: MONTAGE SEQUENCE as Brundle, naked, teleports himself from one telepod to the other.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: During this sequence, we watch Tawny’s amazed reactions as she sits on the mattress watching the process with a drink in her hand.
  EXPRESSION: Amazed
- CHARACTER: Narrator
  LINE: END MONTAGE SEQUENCE
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Brundle steps from the receiving telepod. Tawny is impressed.
  EXPRESSION: null
- CHARACTER: Tawny
  LINE: Wow! Are you a magician?
  EXPRESSION: Amazed
- CHARACTER: Brundle
  LINE: Yeah. Now it’s your turn.
  EXPRESSION: Eager
- CHARACTER: Tawny
  LINE: I don’t think I want to try it.
  EXPRESSION: Hesitant
- CHARACTER: Brundle
  LINE: Why not? It’ll make you feel sexy.
  EXPRESSION: Persuasive
- CHARACTER: Tawny
  LINE: I already feel sexy. How about a nice alcohol rub?
  EXPRESSION: Flirtatious
- CHARACTER: Narrator
  LINE: Tawny pushes Brundle down onto the mattress and starts to rub the booze over his skin. The instant the stuff hits his skin, he screams in pain, whipping around to slap the bottle out of her hand.
  EXPRESSION: null
- CHARACTER: Brundle
  LINE: Don’t do that! It hurts!
  EXPRESSION: Agonized
- CHARACTER: Narrator
  LINE: Tawny doesn’t seem to be the slightest bit intimidated by Brundle’s violence.
  EXPRESSION: null
- CHARACTER: Tawny
  LINE: Sorry, Hun. I didn't realize you had the skin of a princess. Real sensitive, huh?
  EXPRESSION: Sarcastic
- CHARACTER: Narrator
  LINE: Brundle jumps up from the mattress and begins to pace back and forth like a maniac.
  EXPRESSION: null
- CHARACTER: Brundle
  LINE: I want you to go through. I think you’ll like it.
  EXPRESSION: Obsessed
- CHARACTER: Tawny
  LINE: But I don’t want to. I’m afraid.
  EXPRESSION: Afraid
- CHARACTER: Brundle
  LINE: Don’t be afraid.
  EXPRESSION: Reassuring
- CHARACTER: Narrator
  LINE: A voice comes from out of the shadows by the door.
  EXPRESSION: null
- CHARACTER: Veronica
  LINE: No - be afraid. Be very afraid.
  EXPRESSION: Ominous
- CHARACTER: Narrator
  LINE: Veronica steps into the light. Tawny is weirded out by Veronica’s dark tone of voice, by her gravity.
  EXPRESSION: null
- CHARACTER: Tawny
  LINE: Who’s this?
  EXPRESSION: Confused
- CHARACTER: Brundle
  LINE: I live with my mother, too. Mum, meet Tawny.
  EXPRESSION: Sarcastic
- CHARACTER: Tawny
  LINE: I think I’d better go. Thanks for the wonderful time.
  EXPRESSION: Anxious
- CHARACTER: Narrator
  LINE: Tawny gets herself together in an amazingly short time - she's had practice - and is out the door in seconds. She doesn't look back.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Now Brundle comes out into the light and we take a close look at him - as does Veronica. We see that his skin seems very red and rough, his beard stubble thick, coarse, and flecked with the same metallic green of the first few hairs that grew from his side. His cheeks are gaunt, his eyes seem unnaturally wide-open.
  EXPRESSION: null
- CHARACTER: Brundle
  LINE: Why did you scare her off? Jealous?
  EXPRESSION: Confrontational
- CHARACTER: Narrator
  LINE: Brundle’s tone doesn’t bother Veronica. She’s functioning on a different level altogether.
  EXPRESSION: null
- CHARACTER: Veronica
  LINE: You’re changing, Brundle. Everything about you is changing. You look bad. You smell bad.
  EXPRESSION: Concerned
- CHARACTER: Brundle
  LINE: I’ve never been much of a bather.
  EXPRESSION: Defensive
- CHARACTER: Narrator
  LINE: Veronica throws down the phone bill envelope with the metallic-green hairs in it. We can see the hairs through the plastic window in the envelope.
  EXPRESSION: null
- CHARACTER: Veronica
  LINE: Those weird hairs that were growing out of your side - I took them to a lab, Brundle. Had them analyzed.
  EXPRESSION: Serious
- CHARACTER: Narrator
  LINE: Brundle nervously picks up a candy bar and begins to eat it.
  EXPRESSION: null
- CHARACTER: Brundle
  LINE: The hairs? Oh yeah. That’s a strange thing to do.
  EXPRESSION: Nervous
- CHARACTER: Veronica
  LINE: Not as strange as the results. The guy at the lab had trouble identifying them. He finally came to the conclusion that they were definitely not human.
  EXPRESSION: Grave
- CHARACTER: Brundle
  LINE: Yeah?
  EXPRESSION: Disbelieving
- CHARACTER: Veronica
  LINE: Not human, Brun
  EXPRESSION: Deadly Serious

::PATHS::
- CHOICE: "Continue the conversation"
  TARGET: end_of_excerpt
  STATE_CHANGE: brundle_mutation = +1, veronica_concern = +1
  CONDITION: null

::SCENE::
LOCATION: Lab
MOOD: Intense, panicked, violent
CHARACTERS: Brundle, Veronica
BACKGROUND_IMAGE: lab_interior.png
BACKGROUND_EDIT: "Messy, industrial lab, with damaged equipment"

::SCRIPT::
- CHARACTER: Brundle
  LINE: That’s ridiculous. That’s silly.
  EXPRESSION: Denying
- CHARACTER: Narrator
  LINE: She turns Brundle around. More hairs have already sprouted from the three scratches, thick, coarse, metal-green.
  EXPRESSION: null
- CHARACTER: Veronica
  LINE: Look.
  EXPRESSION: Urgent
- CHARACTER: Veronica
  LINE: Something happened when you went through, Brundle. You’ve got to get help! You’ve got to find out what went wrong!
  EXPRESSION: Worried
- CHARACTER: Narrator
  LINE: Brundle freaks out.
  EXPRESSION: null
- CHARACTER: Brundle
  LINE: Get out of here! You’re jealous, jealous! I’ve become free, I’ve been released and you can’t stand it! You’ll do anything to bring me down. Look at me! Does this look like a sick man? Does this look sick?
  EXPRESSION: Freaking out
- CHARACTER: Narrator
  LINE: He begins to PUNCH AWAY chunks of an immense wooden support beam with his right fist! Shards of wood fly everywhere. He smashes it and smashes it until Veronica puts her hands over her ears and screams at him.
  EXPRESSION: Violent
- CHARACTER: Veronica
  LINE: Stop! Stop it!
  EXPRESSION: Screaming
- CHARACTER: Brundle
  LINE: Do you know any sick old men who can do that? GET OUT! Get out!
  EXPRESSION: Angry
- CHARACTER: Narrator
  LINE: Brundle actually pushes and shoves her out the door, then slides it closed behind her. He makes a lot of noise locking it up, so that she knows he’s serious.
  EXPRESSION: Violent

::SCENE::
LOCATION: Lab Warehouse Stairwell
MOOD: Desperate, emotional, sad
CHARACTERS: Veronica, Brundle (OC)
BACKGROUND_IMAGE: warehouse_stairwell.png
BACKGROUND_EDIT: "Exterior of an old industrial warehouse stairwell, daytime"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Veronica bursts into tears. Brundle yells at her through the door.
  EXPRESSION: null
- CHARACTER: Veronica
  LINE: Brundle! You’re committing suicide! Please don’t do it! Please don’t!
  EXPRESSION: Sobbing
- CHARACTER: Brundle (OC)
  LINE: Don’t come back. The deal’s off. I don’t need you any more!
  EXPRESSION: Dismissive
- CHARACTER: Narrator
  LINE: She runs off down the stairs, crying as she goes.
  EXPRESSION: Sad

::SCENE::
LOCATION: Lab
MOOD: Reflective, worried
CHARACTERS: Brundle
BACKGROUND_IMAGE: lab_interior.png
BACKGROUND_EDIT: "Lab interior, quiet, daytime"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Brundle, now very alone, feels his beard, then feels the hairs on his side.
  EXPRESSION: Worried

::SCENE::
LOCATION: Lab Bathroom
MOOD: Horrified, disgusted, fearful
CHARACTERS: Brundle
BACKGROUND_IMAGE: lab_bathroom.png
BACKGROUND_EDIT: "Grungy bathroom with mirror, daytime"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Brundle is in the bathroom, studying himself in the mirror. He does not look well. He looks cancerously gaunt.
  EXPRESSION: Worried
- CHARACTER: Narrator
  LINE: He picks up his electric razor and begins to shave the strange hairs off his face. The razor snags painfully in the hairs and keeps jamming. Finally it stops working.
  EXPRESSION: Frustrated
- CHARACTER: Narrator
  LINE: Brundle throws the razor down in anger, then begins to bite nervously at his fingernail.
  EXPRESSION: Angry
- CHARACTER: Narrator
  LINE: To his (and our) horror, THE NAIL COMES OFF IN HIS MOUTH! THE ENTIRE NAIL. Brundle spits it out in disgust. He examines the tip of his now nail-less finger. It is swollen and sore-looking, and there is a series of small holes where there used to be a nail.
  EXPRESSION: Horrified
- CHARACTER: Narrator
  LINE: Brundle squeezes his fingertip. A STICKY PUS-LIKE FLUID SPURTS from the nail onto the mirror, then continues to ooze for seconds after Brundle has stopped squeezing.
  EXPRESSION: Disgusted
- CHARACTER: Narrator
  LINE: Brundle takes toilet paper and tries to clean off his finger, but the paper sticks to the fluid and makes a complete, gooey mess.
  EXPRESSION: Frustrated
- CHARACTER: Narrator
  LINE: Brundle now gingerly tests another fingernail. It seems loose. He squeezes that fingertip and the nail pops off, goo oozing out from underneath it. The nail next to it splits open of its own accord, ready to fall off at any instant.
  EXPRESSION: Horrified
- CHARACTER: Narrator
  LINE: Brundle is weak in the knees. He clutches the towel rack for support and sits on the edge of the tub.
  EXPRESSION: Afraid
- CHARACTER: Brundle
  LINE: Oh, no. What’s happening? Am I dying? Is that it?
  EXPRESSION: Afraid
- CHARACTER: Brundle
  LINE: Is this how it starts? Am I dying?
  EXPRESSION: Yelling

::SCENE::
LOCATION: Lab
MOOD: Tense, scientific, terrifying discovery
CHARACTERS: Brundle
BACKGROUND_IMAGE: lab_computer.png
BACKGROUND_EDIT: "Lab interior, late day, focused on a computer monitor"

::SCRIPT::
- CHARACTER: Narrator
  LINE: We are tight on the keyboard of the computer. Brundle's hands - clothed in a mismatched pair of old cloth gardening gloves - come into the shot and take a disc out of the disc-holder. The title of the disc is "FIRST TRANSMISSION - S. BRUNDLE."
  EXPRESSION: Focused
- CHARACTER: Narrator
  LINE: The disc goes into the slot. The machine is turned on.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Brundle’s face is sweaty and intense. Brundle's gloved fingers dance over the keys.
  EXPRESSION: Intense
- CHARACTER: Narrator
  LINE: MONITOR - we see a flood of figures and tables as the machine retraces the steps recorded during Brundle's first tipsy teleportation of himself.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: On the monitor Brundle sees himself outlined and analyzed and diagrammed. AND THEN he sees something strange: ANOTHER OUTLINE - THE OUTLINE OF A FLY! It's in CU, complete with tables, etc.
  EXPRESSION: Surprised
- CHARACTER: Narrator
  LINE: Now the screen splits into two and the outlines disintegrate. A few beats later, the reintegration is charted, BUT THERE IS ONLY AN OUTLINE OF BRUNDLE!
  EXPRESSION: Ominous
- CHARACTER: Narrator
  LINE: Brundle now types into the machine: WHAT HAPPENED TO THE FLY? by using the code number attached to the outline of the fly.
  EXPRESSION: Investigative
- CHARACTER: Narrator
  LINE: The machine answers: FUSION.
  EXPRESSION: Revealing
- CHARACTER: Narrator
  LINE: Brundle asks for clarification. DO YOU MEAN ASSIMILATION? DID BRUNDLE ABSORB THE FLY?
  EXPRESSION: Desperate
- CHARACTER: Narrator
  LINE: The answer is NO: FUSION OF FLY AND BRUNDLE AT THE MOLECULAR-GENETIC LEVEL.
  EXPRESSION: Shocking
- CHARACTER: Narrator
  LINE: He is now very afraid.
  EXPRESSION: Afraid

::SCENE::
LOCATION: Veronica's Apt. Living Room
MOOD: Weary, worried, tense, desperate
CHARACTERS: Veronica, Brundle (phone)
BACKGROUND_IMAGE: veronica_apt_livingroom.png
BACKGROUND_EDIT: "Cozy but cluttered apartment living room at night, papers spread everywhere"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Veronica is working late on her mini-word processor. The small, cheap printer is printing. She’s drinking coffee, smoking too many cigarettes. There are scientific journals and reference books spread open everywhere. The phone rings.
  EXPRESSION: Tired
- CHARACTER: Veronica
  LINE: Yeah?
  EXPRESSION: Distracted
- CHARACTER: Narrator
  LINE: There is a long pause before anyone speaks. Veronica immediately knows it’s Brundle.
  EXPRESSION: Tense
- CHARACTER: Veronica
  LINE: Brundle?
  EXPRESSION: Worried
- CHARACTER: Narrator
  LINE: (NO ANSWER)
  EXPRESSION: Tense
- CHARACTER: Veronica
  LINE: Brundle, I’ve been trying to reach you for five days. Where are you?
  EXPRESSION: Concerned
- CHARACTER: Brundle (Phone)
  LINE: I’ve been afraid to see you. Now, I’m afraid not to.
  EXPRESSION: Afraid
- CHARACTER: Veronica
  LINE: Where are you? Are you at home?
  EXPRESSION: Concerned
- CHARACTER: Brundle (Phone)
  LINE: Veronica... you... you don’t know how right you were... Please come to see me. Please come now.
  EXPRESSION: Desperate

::SCENE::
LOCATION: Lab
MOOD: Eerie, disgusting, fearful, deteriorated
CHARACTERS: Veronica, Brundle
BACKGROUND_IMAGE: lab_interior_night.png
BACKGROUND_EDIT: "Darkened lab at night, messy with trash and strange growths"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Veronica slides open the door, which is unlocked. She comes inside, sliding the door closed behind her.
  EXPRESSION: Cautious
- CHARACTER: Narrator
  LINE: She begins to walk from the darkness into the light. As she walks towards the bedroom, she sees that the place is littered with candy wrappers, donut boxes, empty soda cans, half-eaten pastries, chocolate boxes... you name it.
  EXPRESSION: Eerie
- CHARACTER: Narrator
  LINE: Brundle is lying slumped on an old sofa. He wears socks on his feet and gloves on his hands. The gloves and socks are wet and sticky.
  EXPRESSION: Disgusted
- CHARACTER: Narrator
  LINE: She approaches him, fearful. He doesn’t seem to know she’s in the room.
  EXPRESSION: Fearful
- CHARACTER: Veronica
  LINE: I’m here, Brundle.
  EXPRESSION: Concerned
- CHARACTER: Narrator
  LINE: Brundle looks up, dazed. He’s gotten worse fast. His cheeks have sunk more, but now his temples have swollen grotesquely and there are two separate lumps high on his forehead. The metal-green hair seems to have grown all over his face - it’s patchy in spots, but is growin
  EXPRESSION: Horrified

::SCENE::
LOCATION: Brundle's Apartment
MOOD: Despair, Horror, Sadness
CHARACTERS: Narrator, Brundle, Veronica
BACKGROUND_IMAGE: brundle_apartment_messy.png
BACKGROUND_EDIT: "Interior, cluttered with junk food, dim lighting"

::SCRIPT::
- CHARACTER: Narrator
  LINE: where hair shouldn't grow - right up to the rims of his eyes and over his forehead.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Brundle looks up at Veronica. His eyes finally manage to focus on her, then well up with tears which stream down his face and get tangled in his beard. When he speaks, his voice is scratchy, raspy.
  EXPRESSION: null
- CHARACTER: Brundle
  LINE: Don't come too close to me.
  EXPRESSION: Afraid
- CHARACTER: Veronica
  LINE: Why not?
  EXPRESSION: Concerned
- CHARACTER: Brundle
  LINE: I’m diseased. You were right. It could be contagious somehow. I wouldn’t want to infect you.
  EXPRESSION: Afraid
- CHARACTER: Narrator
  LINE: Veronica sits down on the sofa amid all the junk-food remains.
  EXPRESSION: null
- CHARACTER: Veronica
  LINE: What happened?
  EXPRESSION: Concerned
- CHARACTER: Brundle
  LINE: I know an old lady who swallowed a fly. Perhaps she’ll die.
  EXPRESSION: Ironic, Sad
- CHARACTER: Veronica
  LINE: Brundle, please...
  EXPRESSION: Very Disturbed
- CHARACTER: Brundle
  LINE: Impurity. Lack of integrity. Where does the body stop and the outside world begin?
  EXPRESSION: Intense
- CHARACTER: Brundle
  LINE: I was not pure. The teleporter insists on inner purity, and I was not pure.
  EXPRESSION: Intense
- CHARACTER: Veronica
  LINE: I don’t know what you mean.
  EXPRESSION: Quietly Sad
- CHARACTER: Brundle
  LINE: A fly got into the transmitter pod with me. That first time. When I was alone. The computer got confused - there weren’t supposed to be two separate genetic patterns - and it decided to splice us together.
  EXPRESSION: Explaining
- CHARACTER: Brundle
  LINE: It mated us, me and the fly. We hadn’t even been properly introduced. My teleporter turned into a gene-splicer, and a very good one. And now I’m not Seth Brundle any more - I’m the offspring of Brundle and housefly.
  EXPRESSION: Laughing, Despairing
- CHARACTER: Veronica
  LINE: Oh, my God. What... what will happen?
  EXPRESSION: Horrified
- CHARACTER: Brundle
  LINE: I think it’s showing itself as a bizarre form of cancer. General cellular chaos and revolution. I’m just going to disintegrate - in a novel way, no doubt. And then I’ll die, and then it’ll be over.
  EXPRESSION: Resigned
- CHARACTER: Veronica
  LINE: No! I don’t accept that. There must be something we can do. There must be somebody we can go to, tests that can be done...
  EXPRESSION: Desperate
- CHARACTER: Brundle
  LINE: No. I won’t be just another tumorous bore, talking endlessly about his hair falling out and his lost lymph nodes. I know what that's all about and I won’t go through it!
  EXPRESSION: Sarcastic, Irritated
- CHARACTER: Veronica
  LINE: Then what do you want me to do? Why did you call me?
  EXPRESSION: Angry
- CHARACTER: Brundle
  LINE: Keep to your part of the deal. Tape me, record me. This is, after all, the continuation of the Pulitzer prize-winning epic, isn’t it? And everyone is just as interested to know what went wrong, as what went right - maybe more interested.
  EXPRESSION: Manipulative
- CHARACTER: Narrator
  LINE: He leans forward and spills out the contents of a plastic bag at the foot of the sofa - junk food, all of it sweet.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: He grabs a donut and jams it into his mouth. White goop instead of saliva drips from his chin. Thicker, more viscous. He talks while he chews.
  EXPRESSION: null
- CHARACTER: Brundle
  LINE: It’s disgusting, isn’t it? You’ve got to get back behind the video camera. People will want to know... they’ll want to see with their own eyes...
  EXPRESSION: Disgusted, Manipulative
- CHARACTER: Narrator
  LINE: Brundle suddenly begins to scratch and tug again at one of his ears. IT COMES OFF and drops onto the sofa, looking like a black, shriveled-up potato chip amongst the junk food.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Brundle stops in his tracks and stares at the ear.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Despite his foray into angry wit, Brundle is now stunned, broken. He picks the ear up and cradles it in his hand.
  EXPRESSION: null
- CHARACTER: Brundle
  LINE: My... my ear...!
  EXPRESSION: Stunned, Shocked
- CHARACTER: Narrator
  LINE: Veronica stares on, horrified, paralyzed. Brundle begins to cry, to wail hopelessly, and Veronica has to go to him, to hold him, to rock him in her arms. But even as she does so, she sees that Brundle’s other ear is also turning black around the edges, shriveling...
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Brundle keeps sobbing.
  EXPRESSION: null
- CHARACTER: Brundle
  LINE: Help me, help me. Please... please help me!
  EXPRESSION: Sobbing Uncontrollably

::PATHS::
- CHOICE: "Seek help from Stathis"
  TARGET: stathis_office
  STATE_CHANGE: brundle_state = 'deteriorating', veronica_resolve = 'increased'
  CONDITION: null

::SCENE::
LOCATION: Stathis’s Office
MOOD: Urgent, Conflicted
CHARACTERS: Narrator, Stathis, Veronica
BACKGROUND_IMAGE: stathis_office.png
BACKGROUND_EDIT: "Daytime, professional office environment"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Veronica and Stathis are talking about Brundle.
  EXPRESSION: null
- CHARACTER: Stathis
  LINE: Don’t go back to him. Call the police, the Public Health Department.
  EXPRESSION: Urgent, Warning
- CHARACTER: Veronica
  LINE: That’s your advice? That's it?
  EXPRESSION: Disappointed, Angry
- CHARACTER: Stathis
  LINE: But he’s right, don’t you see? It could be contagious. It could turn into an epidemic.
  EXPRESSION: Concerned, Warning
- CHARACTER: Veronica
  LINE: I’ve got to go back to him. He’s got no one else. If you saw him Stath... if you saw how scared and angry and pitiful he is...
  EXPRESSION: Desperate, Empathic
- CHARACTER: Stathis
  LINE: I’m sure Typhoid Mary was a very nice lady, too. When you met her socially.
  EXPRESSION: Sarcastic
- CHARACTER: Stathis
  LINE: Listen, I don’t want you to...
  EXPRESSION: Concerned, Grabbing Arm
- CHARACTER: Veronica
  LINE: I don't care what you want!
  EXPRESSION: Angry, Shaking Him Off
- CHARACTER: Stathis
  LINE: Sure, OK. Just tell me... do I have your permission to claim your body after it's all over ?
  EXPRESSION: Sarcastic, Concerned
- CHARACTER: Narrator
  LINE: Veronica can’t stop a bit of a smile from showing.
  EXPRESSION: null
- CHARACTER: Stathis
  LINE: Look... how about this? You say if I only saw him. OK - show me. Tape him. He wants you to anyway, right? Show me, and let me think about what we might be able to do. But don’t get close. Please.
  EXPRESSION: Conciliatory, Strategic, Warning

::PATHS::
- CHOICE: "Return to the lab to tape Brundle"
  TARGET: lab_warehouse_ext
  STATE_CHANGE: stathis_trust = 'increased', veronica_resolve = 'confirmed'
  CONDITION: null

::SCENE::
LOCATION: Lab Warehouse - Exterior
MOOD: Apprehensive
CHARACTERS: Narrator, Veronica
BACKGROUND_IMAGE: lab_warehouse_ext.png
BACKGROUND_EDIT: "Daytime, exterior of an industrial lab building"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Veronica gets out of her car in front of the lab. She hesitates just that telltale beat before she slams the car door and begins to walk towards the front door.
  EXPRESSION: null

::PATHS::
- CHOICE: "Enter the lab"
  TARGET: lab_interior
  STATE_CHANGE: veronica_courage = 'increased', brundle_proximity = 'close'
  CONDITION: null

::SCENE::
LOCATION: Lab - Interior
MOOD: Disgust, Horror, Shock
CHARACTERS: Narrator, Veronica, Brundle
BACKGROUND_IMAGE: lab_interior.png
BACKGROUND_EDIT: "Daytime, interior, extremely messy, strong stench, dim lighting, scientific equipment scattered"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Veronica enters the lab and immediately puts her hand to her face - the stench is very, very strong, and the litter on the floor and everywhere else has accumulated at an alarming rate.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: ANGLE FROM CEILING LOOKING DOWN ON VERONICA as she makes her way through the litter, looking for Brundle.
  EXPRESSION: null
- CHARACTER: Veronica
  LINE: Brundle?
  EXPRESSION: Concerned, Calling Out
- CHARACTER: Brundle
  LINE: I'm here.
  EXPRESSION: Off-screen Voice
- CHARACTER: Narrator
  LINE: Veronica’s gaze follows the voice - up to the ceiling.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: VERONICA’S POV We realize that a moment ago we were looking at Veronica from Brundle’s POV FOR HE HANGS UPSIDE DOWN FROM THE CEILING BY ALL FOURS!
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: If this weren’t startling enough, the changes in his appearance most certainly are. He’s completely naked, and his torso is beginning to be covered all over with metallic-green hair.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: And his musculature has changed again - stringy and powerful, not like a gymnast. Not human. A hernia-like bulge protruding from his left side is the only suggestion of weakness in his grotesquely sleek shape.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Brundle scrambles adroitly across the ceiling, then d
  EXPRESSION: null

::PATHS::
- CHOICE: "Confront Brundle"
  TARGET: (Continues with confrontation)
  STATE_CHANGE: brundle_state = 'advanced_mutation', veronica_shock = 'extreme'
  CONDITION: null

::SCENE::
LOCATION: Brundle's Lab
MOOD: Horrific
CHARACTERS: Veronica, Brundle, Narrator
BACKGROUND_IMAGE: brundle_lab.png
BACKGROUND_EDIT: "Dark, shadowy lab with strange equipment, grotesque human-fly creature"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Veronica watches with her eyes huge.
  EXPRESSION: Afraid
- CHARACTER: Veronica
  LINE: Brundle... I...
  EXPRESSION: Stunned
- CHARACTER: Brundle
  LINE: Gotten pretty good at it, haven’t I? It’s almost second nature. Stopped biting my nails, too.
  EXPRESSION: Eerie
- CHARACTER: Narrator
  LINE: Veronica can only stare at him. He approaches her, still in shadow.
  EXPRESSION: Afraid
- CHARACTER: Brundle
  LINE: I seem to be stricken by a disease with a purpose, wouldn’t you say? Maybe not such a bad disease after all.
  EXPRESSION: Philosophical
- CHARACTER: Narrator
  LINE: She shakes her head in disbelief, then turns to leave.
  EXPRESSION: Disbelief
- CHARACTER: Veronica
  LINE: I can’t stay here.
  EXPRESSION: Overwhelmed
- CHARACTER: Narrator
  LINE: Brundle grabs her. His fingers are longer, thinner. They have no more nails on them, they glisten with the oily secretion. His palms are forming small, cushion-like pads. His feet - the same, the toes long and oily.
  EXPRESSION: null
- CHARACTER: Brundle
  LINE: Why not? Why can’t you?
  EXPRESSION: Insistent
- CHARACTER: Narrator
  LINE: Veronica can not bear to look at him.
  EXPRESSION: Disgusted
- CHARACTER: Veronica
  LINE: Can’t take it... Too much.
  EXPRESSION: With Difficulty
- CHARACTER: Narrator
  LINE: Brundle moves out into the light and we can now see how much more his face has changed. His skull has swollen even more at the temples and his forehead as well, so that the entire shape of his skull has altered. And his face is now covered with the metallic-green hair, so that there is not a square centimeter of normal flesh showing. Brundle’s eyes are almost lost in this new face, but they are now very bright and piercing.
  EXPRESSION: null
- CHARACTER: Brundle
  LINE: What's there to take? The disease has just revealed its purpose. We don't have to worry about contagion any more. I know what the disease wants.
  EXPRESSION: Eerie
- CHARACTER: Narrator
  LINE: Veronica looks down at the hand holding her arm, then forces herself to look Brundle in the face.
  EXPRESSION: Hesitant
- CHARACTER: Veronica
  LINE: What...what does the disease want?
  EXPRESSION: Afraid
- CHARACTER: Brundle
  LINE: It wants to turn me into something else. That's not too terrible, is it? Most people would give anything to be turned into something else.
  EXPRESSION: Matter-of-fact
- CHARACTER: Veronica
  LINE: Turned into what? An insect?
  EXPRESSION: Disgusted
- CHARACTER: Narrator
  LINE: Brundle lets her go - his fingers stick momentarily to the arm of her blouse - and laughs, a harsh, grating little laugh.
  EXPRESSION: null
- CHARACTER: Brundle
  LINE: You mean a fly? Am I turning into a hundred-and-eighty-pound fly?
  EXPRESSION: Mocking
- CHARACTER: Narrator
  LINE: He laughs again.
  EXPRESSION: null
- CHARACTER: Brundle
  LINE: No, I’m becoming something that never existed before. I’m becoming... Brundlefly. B-R-U-N-D-L-E-F-L-Y. Don’t you think that’s worth a Nobel Prize or two?
  EXPRESSION: Delusional
- CHARACTER: Narrator
  LINE: Veronica just stands there, defeated by his sarcasm and defeated by the rapidly accelerating bizarreness of his condition.
  EXPRESSION: Defeated
- CHARACTER: Brundle
  LINE: C’MON, NOW. LET’S GO.
  EXPRESSION: Enthusiastic
- CHARACTER: Narrator
  LINE: Brundle begins to take charge, full of enthusiasm. He gently but firmly places Veronica behind the ever-present video camera, and then bustles around, his movements awkward and strange, setting up a chair and table in front of the camera.
  EXPRESSION: null
- CHARACTER: Brundle
  LINE: I want to give a demonstration that I think you’ll want to record for posterity. Yes, yes. I think you must chronicle the rise and fall of Brundlefly, don't you? At the very least, it should make a fabulous children’s book. Do they give Pulitzer Prizes for kiddies' books?
  EXPRESSION: Enthusiastic

::PATHS::
- CHOICE: "Witness the demonstration"
  TARGET: veronica_apt_living_room
  STATE_CHANGE: fear = +3
  CONDITION: null

::SCENE::
LOCATION: Veronica's Apt. Living Room
MOOD: Shock
CHARACTERS: Narrator, Stathis, Veronica, Brundle (on tape)
BACKGROUND_IMAGE: veronica_apt_living_room.png
BACKGROUND_EDIT: "Daytime, apartment living room, TV playing a disturbing video"

::SCRIPT::
- CHARACTER: Narrator
  LINE: We are tight on the screen of Veronica's TV set, watching the demonstration that Brundle was just talking about.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: On the tape, Brundle is sitting at a table in his lab with a pile of his usual junk food in front of him. He is smiling - a still-recognizable smile, since his jaw and mouth have not undergone any change in shape, though his jaw is covered with metallic-green beard.
  EXPRESSION: null
- CHARACTER: Brundle (on tape)
  LINE: How does Brundlefly eat? Well, he found out the hard and painful way that he eats very much the way a fly eats. His teeth are now useless, because although he can chew up solid food, he can’t digest it. Solid food hurts. So, like a fly, Brundlefly breaks down solids with a corrosive enzyme playfully called "vomit drop.” He regurgitates on his food, liquefies it, then sucks it back up. Ready for a demonstration, kids? Here goes.
  EXPRESSION: Explanatory
- CHARACTER: Narrator
  LINE: Brundle now bends close to the food until his face is almost touching it.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: We pop back to AN ANGLE WHICH EXCLUDES THE TV SCREEN and see that Stathis is watching alone in the living room. He is shaken by what he is watching.
  EXPRESSION: null
- CHARACTER: Stathis
  LINE: Oh my God, my God.
  EXPRESSION: Shaken
- CHARACTER: Narrator
  LINE: From the TV’s speaker we hear hideous, enthusiastic slurping and sucking sounds, BUT WE DO NOT SEE WHAT STATHIS SEES.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Stathis runs his hands through his hair. He leans forward and switches off the tape machine. His upper lip is beaded with sweat. He wipes it off with his sleeve.
  EXPRESSION: Anxious
- CHARACTER: Narrator
  LINE: Veronica comes in the front door and, without a word, sweeps past Stathis and down the hall.
  EXPRESSION: Distraught
- CHARACTER: Stathis
  LINE: Hey, Ronnie? I don’t blame you for not wanting to watch it. Ronnie?
  EXPRESSION: Concerned
- CHARACTER: Narrator
  LINE: No response.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: He gets up and leaves the living room, looking for Veronica.
  EXPRESSION: null

::PATHS::
- CHOICE: "Follow Veronica"
  TARGET: veronica_apt_hallway
  STATE_CHANGE: concern = +1
  CONDITION: null

::SCENE::
LOCATION: Veronica’s Apt. Hallway
MOOD: Concern
CHARACTERS: Narrator, Stathis
BACKGROUND_IMAGE: veronica_apt_hallway.png
BACKGROUND_EDIT: "Daytime, apartment hallway, slightly dim"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Stathis walks down the hallway, worried.
  EXPRESSION: Worried
- CHARACTER: Stathis
  LINE: Ronnie? Where are you?
  EXPRESSION: Concerned
- CHARACTER: Narrator
  LINE: Stathis hears sobbing coming from the direction of the bathroom. He turns and sprints down the hallway.
  EXPRESSION: null

::PATHS::
- CHOICE: "Check the bathroom"
  TARGET: veronica_apt_bathroom
  STATE_CHANGE: concern = +1
  CONDITION: null

::SCENE::
LOCATION: Veronica’s Apt. Bathroom
MOOD: Despair
CHARACTERS: Narrator, Stathis, Veronica
BACKGROUND_IMAGE: veronica_apt_bathroom.png
BACKGROUND_EDIT: "Daytime, apartment bathroom, dim lighting, a person sobbing"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Stathis appears in the doorway of the bathroom. Veronica is sobbing her heart out, slumped against the bathroom counter. She’s still wearing her coat. Stathis steps inside the bathroom and puts his arm around her.
  EXPRESSION: null
- CHARACTER: Stathis
  LINE: What is it?
  EXPRESSION: Very Gently
- CHARACTER: Narrator
  LINE: Veronica tries to answer but can’t, she’s sobbing so profoundly. She turns to him, barely able to get it out.
  EXPRESSION: null
- CHARACTER: Veronica
  LINE: I saw a doctor. I’m... I’m pregnant, Stath.
  EXPRESSION: With Difficulty
- CHARACTER: Stathis
  LINE: Oh, no. Oh, no.
  EXPRESSION: Shock
- CHARACTER: Narrator
  LINE: He holds her tight.
  EXPRESSION: null
- CHARACTER: Veronica
  LINE: I'm pregnant with Brundle’s baby!
  EXPRESSION: Renewed Sobbing
- CHARACTER: Narrator
  LINE: Stathis hugs her again, then holds her at arms length so that he can look her in the eye.
  EXPRESSION: null
- CHARACTER: Stathis
  LINE: What do you want to do?
  EXPRESSION: Concerned
- CHARACTER: Narrator
  LINE: Veronica, still racked by sobs, tries to wipe her eyes.
  EXPRESSION: null
- CHARACTER: Veronica
  LINE: I don’t know. I just don’t know.
  EXPRESSION: Tearfully

::PATHS::
- CHOICE: "Discuss options"
  TARGET: lab_night
  STATE_CHANGE: despair = +1
  CONDITION: null

::SCENE::
LOCATION: Lab
MOOD: Unsettling
CHARACTERS: Narrator, Brundle
BACKGROUND_IMAGE: brundle_lab.png
BACKGROUND_EDIT: "Nighttime, computer keyboard, mutated fingers with rubber gloves"

::SCRIPT::
- CHARACTER: Narrator
  LINE: We are close on Brundle’s fingers as they dance over the keys of the computer keyboard. Brundle has cut the fingers off a pair of yellow rubber kitchen gloves and jammed them down over his fingertips,
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue"
  TARGET: end
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Brundle's Lab
MOOD: Horrific, Tense
CHARACTERS: Narrator, Brundle, Monkey, Cat, Fused Creature
BACKGROUND_IMAGE: null
BACKGROUND_EDIT: null

::SCRIPT::
- CHARACTER: Narrator
  LINE: so that his fingers won’t stick to the keyboard.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: MONITOR which reads : GENE-SPLICING PROGRAM NOW IN PLACE TELEPOD 1: TRANSMITTER POD SUBJECT A TELEPOD 2: TRANSMITTER POD SUBJECT B TELEPOD 3: RECEIVER POD FOR GENETICALLY FUSED A-B COMBINATION SUBJECT
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: We pull back to see that in front of Brundle and his keyboard stand not two, but THREE telepods, the third one of a somewhat older and more handbuilt vintage than the other two - the original PROTOTYPE TELEPOD which has been sitting in corner of the lab under a tarpaulin and was noticed by Veronica on her first visit to the lab.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: In TELEPOD A sits a monkey, in TELEPOD B an alley cat. TELEPOD C, the old prototype receiver, is empty.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Brundle operates the machine. The monitor says, READY FOR FUSION
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Brundle presses the ACCEPT button.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The telepods go through their normal disintegration routine as the animals’ outlines appear on the monitor in split screen fashion.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: But now, as the reintegration process begins, a stream of data concerning this new experiment, the fusion of monkey and cat, floods the screen. The basic message that gets across to us through all the hi-tech compu-talk is: PERENTAGE OF MONKEY - 63 PERCENTAGE OF CAT - 37
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: These numbers fluctuate as the machine tries to strike a molecular balance between the two creatures.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Finally, an outline of the fused creature begins to form on the screen. Brundle looks up at the old third telepod to see the actual creature forming, and it is indeed grotesque: two heads - one monkey, one eat - at odd angles to each other, six legs which are not quite symmetrically placed on the monkey torso, cat tail.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: As the creature solidifies and the light goes off, it sits there in the telepod for a moment, stunned, half­ reclining as though crippled.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Brundle gets up, goes to the third telepod, and with great apprehension, opens the door.
  EXPRESSION: Afraid
- CHARACTER: Narrator
  LINE: The thing just sits there, slumped for a beat, then SUDDENLY LEAPS UP AT HIM, its two heads SHRIEKING! It jumps on his arm, clinging, snarling, then drops to the floor. The two heads begin to bite each other, blood begins to flow - the thing now running around in mad floppy circles, smearing blood everywhere.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Brundle is horrified. He grabs a metal rod leaning in a corner and begins to smash at the deformed thing. He keeps smashing at it until it stops its hideous screeching and lies dead, mangled on the floor.
  EXPRESSION: Angry
- CHARACTER: Narrator
  LINE: Brundle wraps it up in a towel and throws it into the refrigerator. He draws the old torn sheet back down over the third telepod so that he doesn't have to look at it again.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Back at the monitor, the screen is flashing the words: FUSION SUCCESSFUL RECEIVER TELEPOD 3
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Brundle puts his face in his hands for a few moments, then pulls himself together. He pulls the rubber fingertips off his fingers and throws them to the ground.
  EXPRESSION: Angry
- CHARACTER: Narrator
  LINE: Brundle has now developed some insect-like tics and mannerisms, his head twitching with nervous little jerks and his long fingers in constant motion. We now see clearly that all of Brundle’s fly characteristics have been accentuated even further. The metal 1ic-green hair which completely covers his face is much thicker than before, and the hernia-like bulge in his side is more protuberant now, stretched to the bursting point and obviously causing Brundle some pain.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Brundle looks up at the skylight. The sky is clear, the moon is a scimitar. On an impulse, he jumps up on the wall, sticking there for a beat. Then, with incredible agility, he ascends the wall, crosses the ceiling towards the skylight.
  EXPRESSION: null

::PATHS::
- CHOICE: "Ascend the wall"
  TARGET: ceiling_climb
  STATE_CHANGE: brundle_state = "transformed_active"
  CONDITION: null

::SCENE::
LOCATION: Brundle's Lab - On the Ceiling
MOOD: Eerie, Agile
CHARACTERS: Narrator, Brundle
BACKGROUND_IMAGE: null
BACKGROUND_EDIT: null

::SCRIPT::
- CHARACTER: Narrator
  LINE: Brundle glides on all fours, upside down, towards the skylight. Once there, he crawls into it and opens it up.
  EXPRESSION: null

::PATHS::
- CHOICE: "Open the skylight"
  TARGET: lab_rooftop
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Lab Rooftop
MOOD: Hopeful, Sublime
CHARACTERS: Narrator, Brundle
BACKGROUND_IMAGE: null
BACKGROUND_EDIT: "Nighttime, clear sky, stars"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Brundle clambers out of the skylight onto the roof. The night is gorgeous, clean and bright, the sky pocked with stars. Brundle breathes deeply. He is still alive, isn’t he? He can still respond to the beauty of the night, can’t he?
  EXPRESSION: null

::PATHS::
- CHOICE: "Explore the city"
  TARGET: brundles_travels_montage
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: City - Montage - Brundle's Travels
MOOD: Euphoric, Poetic
CHARACTERS: Narrator, Brundle
BACKGROUND_IMAGE: null
BACKGROUND_EDIT: "Nighttime cityscapes, various vantage points"

::SCRIPT::
- CHARACTER: Narrator
  LINE: We follow Brundle on his solitary sojourn in a MONTAGE SEQUENCE. He climbs walls with amazing ability, leaps from rooftop to rooftop, hangs upside down from ledges and lampposts, eavesdropping on the city life around and below him, the inhabitants unaware of the unusual and shadowy observer in their midst.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: He scurries along the girder of a bridge, gazing down on the traffic and the river below him.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: These moments should be poetic, even beautiful, joyous.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The moon is luminous, the dark night exquisite. Resigned to his fate and momentarily forgetful of his future, Brundle seems to be revealing in his unique powers.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: A brief euphoric fling.
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue journey"
  TARGET: city_building
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Building - Narrow Alleyway
MOOD: Agonizing, Horrific
CHARACTERS: Narrator, Brundle
BACKGROUND_IMAGE: null
BACKGROUND_EDIT: "Nighttime, brick building, alley"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Brundle leaps across a narrow alleyway to the wall of the building opposite him. He smiles with smug satisfaction at his feat, then suddenly winces, grabbing his side with one of his hands.
  EXPRESSION: Happy
- CHARACTER: Narrator
  LINE: WE HEAR A CRACKING, SPLITTING SOUND. Brundle muffles a startled cry and, losing his balance, slides several feet down the wall before regaining hold.
  EXPRESSION: Surprised
- CHARACTER: Narrator
  LINE: He looks down at the huge bulge in his side... IT IS STARTING TO SPLIT OPEN! Brundle is horrified and in pain.
  EXPRESSION: Afraid
- CHARACTER: Narrator
  LINE: He starts to quickly move down the side of the building, but the pain impedes his progress.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: He manages to get down at least another floor before he’s hit with another sharp pain. He doubles up and his tenuous grip on the wall causes him to slide another several feet downward before he regains his grip.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The side is gaping wide open now and SOMETHING is starting to protrude. Brundle is in shock. Another ripple of pain causes him to release his grasp entirely and he falls to the ground in a dirty narrow alley, where he writhes on his back in pain, as a STRANGE, HAIRY STICKLIKE APPENDAGE — ACTUALLY THE BEGINNINGS OF A FLYLIKE LEG -- begins to unfold awkwardly out of his side. Despite his e
  EXPRESSION: Afraid

::PATHS::
- CHOICE: "End of scene"
  TARGET: next_scene
  STATE_CHANGE: brundle_state = "further_transformed"
  CONDITION: null

::SCENE::
LOCATION: Brundle's Lair / Alley
MOOD: Horror, Agony
CHARACTERS: Narrator, Brundle
BACKGROUND_IMAGE: brundle_transformation.png
BACKGROUND_EDIT: "Dark, grimy location, Brundle mid-transformation in excruciating pain"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Brundle watches with fixated, wide-eyed terror at his latest transformation! The insect leg now begins to probe around, function like a real leg, almost with a mind of its own. Grotesque as Brundle himself has become, he can’t accept the next step towards real insectness which this new leg represents. He screams at the leg.
  EXPRESSION: Terrified
- CHARACTER: Brundle
  LINE: No I No, I won’t! I won’t, I won’t, I won’t...!
  EXPRESSION: Screaming at the leg
- CHARACTER: Narrator
  LINE: Brundle grabs at the leg, holds it, subdues it, and then begins to gnaw with his teeth at its base, twisting himself into an agonized ball in order to do it. The leg begins to lever at his back, small hooklike protrusions all along its underside catching in the flesh of Brundle’s back, tearing it in protest against Brundle’s attempt at amputation.
  EXPRESSION: Agonized
- CHARACTER: Narrator
  LINE: Finally, Brundle has severed the leg with his teeth. The leg drops off leaving a strand or two of stringy gristle hanging from the knobby stump in Brundle’s side. The leg twitches on the ground, tries to extend itself.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Brundle looks at the leg in shock, his eyes crazed, like an animal who has been caught in a leg-trap and has had to gnaw the leg off to be free. Brundle tries to steady himself, then staggers away down the alley. As he goes, he wipes the insect blood from his lips with his two forearms - IN EXACTLY THE SAME WAY THAT FLIES CLEAN THEIR FACES!
  EXPRESSION: Crazed

::SCENE::
LOCATION: Street Outside Hospital
MOOD: Somber, Anxious
CHARACTERS: Narrator, Stathis, Veronica
BACKGROUND_IMAGE: hospital_exterior.png
BACKGROUND_EDIT: "Daytime, taxi pulling up to a hospital entrance"

::SCRIPT::
- CHARACTER: Narrator
  LINE: A taxi pulls up and Stathis gets out. He helps a very pale and fragile-looking Veronica out of the car.
  EXPRESSION: null

::SCENE::
LOCATION: Hospital Corridor
MOOD: Fear, Reassurance
CHARACTERS: Narrator, Stathis, Veronica
BACKGROUND_IMAGE: hospital_corridor.png
BACKGROUND_EDIT: "Daytime, sterile hospital corridor, Veronica being wheeled"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Stathis holds Veronica’s hand as she is wheeled down the corridor. She is very nervous, almost in tears.
  EXPRESSION: Nervous
- CHARACTER: Veronica
  LINE: Stath...I’m scared!
  EXPRESSION: Nervous
- CHARACTER: Stathis
  LINE: It’s going to be all right, Ronnie. It’s going to be fine.
  EXPRESSION: Reassuring
- CHARACTER: Veronica
  LINE: I don’t think I want to lose it. Is there something wrong with me? Why am I losing it?
  EXPRESSION: Tearful
- CHARACTER: Stathis
  LINE: It’s better this way, Ronnie. You’ll see. It’s the best thing that could happen.
  EXPRESSION: Reassuring

::SCENE::
LOCATION: Hospital Ward
MOOD: Horror, Pain
CHARACTERS: Narrator, Voice #1 (OS), Veronica (OS), Doctor, Nurse, Stathis
BACKGROUND_IMAGE: operating_room.png
BACKGROUND_EDIT: "Close-up of bright operating light, sterile environment, later panning to operating table with medical team"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The dehumanizing blue-white light of an OVERHEAD OPERATING-ROOM LAMP. WE HEAR VERONICA'S MOANS... AND VOICES.
  EXPRESSION: null
- CHARACTER: Voice #1 (OS)
  LINE: She's expelling it. We won’t even have to go in. It’s going to be easy. Don’t worry, honey.
  EXPRESSION: Reassuring
- CHARACTER: Veronica (OS)
  LINE: Please, Brundle, please don’t...
  EXPRESSION: Pained
- CHARACTER: Narrator
  LINE: THE CAMERA PANS FROM THE LAMP TO AN OPERATING TABLE BELOW. Veronica is miscarrying right there on the table. A TEAM OF DOCTORS AND NURSES work over her. STATHIS stands at the head of the table, still holding Veronica’s hand. Veronica grimaces and groans. A NURSE mops her sweaty brow.
  EXPRESSION: Pained
- CHARACTER: Nurse
  LINE: OK, that’s it. We’ve got it.
  EXPRESSION: null
- CHARACTER: Doctor
  LINE: No, no. There’s more in there. A lot more.
  EXPRESSION: Determined
- CHARACTER: Nurse
  LINE: There’s more?
  EXPRESSION: Surprised
- CHARACTER: Doctor
  LINE: C’mon, girl. You can help us out. Give us a push. Push! Thatta girl. We’re getting it.
  EXPRESSION: Encouraging
- CHARACTER: Veronica
  LINE: No, no...wait! Brundle, please, no...!
  EXPRESSION: Pained
- CHARACTER: Doctor
  LINE: That’s it. That’s it. It’s coming. It’s... Ohh, my God!
  EXPRESSION: Horrified
- CHARACTER: Narrator
  LINE: VERONICA'S POV - ON EXPELLED FOETUS ...as the doctor lifts it out of the womb. Perhaps there are some human features about the face, if indeed there is a face at all on THE HIDEOUS, SQUIRMING GIANT FLY-MAGGOT! Stathis registers unutterable HORROR. Veronica SCREAMS.
  EXPRESSION: Horrified

::SCENE::
LOCATION: Veronica’s Bedroom
MOOD: Nightmare, Despair
CHARACTERS: Narrator, Veronica
BACKGROUND_IMAGE: veronica_bedroom.png
BACKGROUND_EDIT: "Nighttime, dark bedroom, Veronica alone in bed"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Veronica wakes up screaming. She’s alone in bed. She’s been dreaming. Once she realizes she has not given birth to a fly-maggot baby, she starts to laugh at herself - then, remembering that she is pregnant by Brundle, she begins to weep again.
  EXPRESSION: Despairing

::SCENE::
LOCATION: Lab
MOOD: Grotesque, Tragic
CHARACTERS: Narrator, Brundle, Veronica
BACKGROUND_IMAGE: brundle_lab.png
BACKGROUND_EDIT: "Nighttime, laboratory, computer screen glowing, Brundle partially transformed"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Brundle is working away at the computer keyboard - only now he has to use pencils, one in each hand, to push the keys: his fingers are losing their human flexibility. The words on the monitor read: THE BRUNDLEFLY PROJECT PROBLEM: TO REFINE GENETIC FUSION PROGRAM GOAL: TO DECREASE TO A MINIMUM THE PERCENTAGE OF ”FLY” IN BRUNDLEFLY SOLUTION: THE FUSION BY GENE-SPLICING OF BRUNDLEFLY WITH ONE OR MORE "PURE” HUMAN BEINGS
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: As Brundle thinks about his next step, he begins to chew on one of the pencils. He is soon distracted by the sound of several small, hard things dropping onto the keyboard. Brundle looks down. Five small, white chunks of something lie partially hidden in the crevices between the plastic keys, Brundle digs one out with the pencil. It is a tooth, its jagged root smeared with blood, and it has just fallen out of Brundle’s mouth.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Brundle begins to roar with laughter. He clumsily digs the rest of the teeth out of the keys, then carries them over to the refrigerator. As he walks, he delivers a little speech to the teeth which sit attentively in the palm of what used to be his hand.
  EXPRESSION: Laughing
- CHARACTER: Brundle
  LINE: You’re relics. Yes, you are. You can’t deny it. Vestigial, archaeological, redundant. Artifacts of a bygone era. Of historical interest only. How long will it take for you and all the other manifestations of the Brundle Age, the Stone Age, to fall away, to reveal the Future...?
  EXPRESSION: Laughing, Talking to his teeth
- CHARACTER: Narrator
  LINE: He opens the fridge and carefully places the teeth in an ice cube tray. The fridge is empty except for a few other barely recognizable lost appendages - Brundle’s shriveled ears, his fingernails.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Suddenly, Brundle hears the door to the lab slide noisily open. He turns, startled.
  EXPRESSION: Startled
- CHARACTER: Narrator
  LINE: Veronica steps warily into the lab - she has kept her keys to the building. Brundle looks wildly around the room - in guilt? in shame? - closes the fridge door and walks quickly over to the computer keyboard. He picks up a pencil with desperate awkwardness and uses it to press the keyboard's STORE button. It is obvious that he does not want Veronica to see what he’s been working on.
  EXPRESSION: Ashamed
- CHARACTER: Narrator
  LINE: Veronica approaches him but stops some distance away. She is stunned by the changes in his appearance, struggling for some kind of emotional equilibrium. They stand frozen for a beat.
  EXPRESSION: Stunned

::SCENE::
LOCATION: Brundle's Lab
MOOD: Horrifying, Emotional
CHARACTERS: Narrator, Brundle, Veronica
BACKGROUND_IMAGE: brundle_lab.png
BACKGROUND_EDIT: "Dark, cluttered, experimental lab, night"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Then Brundle begins to speak. But even Brundle’s voice has become a horror: it is scratchy and metallic, and full of guttural, insect twitters.
  EXPRESSION: null
- CHARACTER: Brundle
  LINE: You’ve missed some good moments. Is that why you’re here? To catch up?
  EXPRESSION: Angry
- CHARACTER: Veronica
  LINE: I... wanted... What were you putting in the fridge?
  EXPRESSION: Afraid
- CHARACTER: Brundle
  LINE: My teeth. They’ve started to fall out. The fridge is now the Brundle Museum of Natural History. Want to see what else is in it?
  EXPRESSION: Neutral
- CHARACTER: Veronica
  LINE: No.
  EXPRESSION: Afraid
- CHARACTER: Brundle
  LINE: Then what do you want?
  EXPRESSION: Angry
- CHARACTER: Veronica
  LINE: I came to tell you that... I came to tell you... I... I just had to see you... before...
  EXPRESSION: Afraid
- CHARACTER: Narrator
  LINE: Tears begin to well up in Veronica’s eyes.
  EXPRESSION: null
- CHARACTER: Brundle
  LINE: You’ve got to go, now, and never come back here.
  EXPRESSION: Neutral
- CHARACTER: Brundle
  LINE: Have you ever heard of insect politics?
  EXPRESSION: Neutral
- CHARACTER: Narrator
  LINE: Veronica shakes her head, completely baffled.
  EXPRESSION: null
- CHARACTER: Brundle
  LINE: Well, neither have I. Insects don’t have politics. They’re very brutal. No compassion. No compromise. We can’t trust the insect. But I’d like to become the first... first insect politician. I’d like to, but I’m afraid...
  EXPRESSION: Sad
- CHARACTER: Veronica
  LINE: I don’t... know... what you’re trying to say...
  EXPRESSION: Confused
- CHARACTER: Brundle
  LINE: I’m saying... that I don't... feel very human any more. I'm saying I'm an insect who dreamt he was a man, and loved it, but now the dream is over, and the insect is awake.
  EXPRESSION: Sad
- CHARACTER: Narrator
  LINE: Veronica bursts out crying.
  EXPRESSION: null
- CHARACTER: Veronica
  LINE: Brundle, please... no...
  EXPRESSION: Sad
- CHARACTER: Brundle
  LINE: I’m saying, I’ll hurt you if you stay.
  EXPRESSION: Sad
- CHARACTER: Narrator
  LINE: Veronica bursts out crying. Brundle doesn’t move. Veronica turns and runs out of the lab. Brundle remains motionless, and from a distance seems completely dispassionate. But when we move close to his face, we see that he too is crying.
  EXPRESSION: null

::PATHS::
- CHOICE: "Veronica runs from the lab"
  TARGET: ext_lab_night
  STATE_CHANGE: veronica_fear = +2, brundle_sadness = +1
  CONDITION: null

::SCENE::
LOCATION: Lab Exterior
MOOD: Desperate
CHARACTERS: Narrator, Veronica, Stathis
BACKGROUND_IMAGE: lab_exterior.png
BACKGROUND_EDIT: "Nighttime, outside a lab building, street"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Veronica bursts out of the lab door and runs across the street to where Stathis is leaning against her car, waiting.
  EXPRESSION: null

::PATHS::
- CHOICE: "Veronica reaches the car"
  TARGET: ext_car_night
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Car Exterior
MOOD: Urgent, Conflicted
CHARACTERS: Narrator, Veronica, Stathis
BACKGROUND_IMAGE: car_exterior.png
BACKGROUND_EDIT: "Nighttime, street, car parked"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Veronica tries to pull open the door of the car but Stathis grabs her, puts his arms around her. Veronica pulls free, her eyes streaming tears. But despite the tears, her face is set hard now, determined.
  EXPRESSION: null
- CHARACTER: Veronica
  LINE: Let’s go. Let’s do it now.
  EXPRESSION: Angry
- CHARACTER: Stathis
  LINE: Now? Wait a minute. What did he say when you told him?
  EXPRESSION: Confused
- CHARACTER: Veronica
  LINE: I couldn’t tell him. I couldn’t... Let's go, dammit!
  EXPRESSION: Angry
- CHARACTER: Stathis
  LINE: I think we should wait a few days. I don't think you’re in the right state of mind...
  EXPRESSION: Neutral
- CHARACTER: Veronica
  LINE: No! Now! I want it out of my body now! You should have seen him. There could be anything in there, in me, in my body!
  EXPRESSION: Afraid
- CHARACTER: Stathis
  LINE: But I don’t know if I can arrange it now, right now, tonight. Why do we have to run around in the dark like ...?
  EXPRESSION: Confused
- CHARACTER: Veronica
  LINE: Because I don’t want it in my body! Do you understand? I don’t want it in my body!
  EXPRESSION: Angry
- CHARACTER: Narrator
  LINE: Veronica gets into the car. She hugs herself tightly and turns her face away from Stathis. Stathis stares at her for a beat, then gets into the car himself.
  EXPRESSION: null

::PATHS::
- CHOICE: "Stathis and Veronica leave"
  TARGET: ext_lab_rooftop_night
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Lab Rooftop
MOOD: Melancholy, Observing
CHARACTERS: Narrator, Brundle
BACKGROUND_IMAGE: lab_rooftop.png
BACKGROUND_EDIT: "Nighttime, rooftop of a warehouse, looking down at street"

::SCRIPT::
- CHARACTER: Narrator
  LINE: From the rooftop of the lab warehouse, BRUNDLE IS WATCHING as Veronica’s car pulls away from the curb and moves off down the street. He has heard the whole thing.
  EXPRESSION: null

::PATHS::
- CHOICE: "Veronica's car drives away"
  TARGET: ext_medical_clinic_night
  STATE_CHANGE: brundle_sadness = +1
  CONDITION: null

::SCENE::
LOCATION: Medical Clinic Exterior
MOOD: Clinical
CHARACTERS: Narrator
BACKGROUND_IMAGE: medical_clinic_exterior.png
BACKGROUND_EDIT: "Nighttime, compact modern brick building, softly lit sign"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Establishing shot of a compact, modern brick five-storey downtown building. The softly lit sign on the small, neatly manicured patch of grass in front of it reads: COVENTRY COMMUNITY MEDICAL CLINIC
  EXPRESSION: null

::PATHS::
- CHOICE: "Enter the clinic"
  TARGET: int_dr_cheevers_office_night
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Dr. Cheevers' Office
MOOD: Tense, Clinical
CHARACTERS: Narrator, Cheevers, Stathis, Veronica
BACKGROUND_IMAGE: dr_cheevers_office.png
BACKGROUND_EDIT: "Nighttime, office interior, professional, clean"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Doctor Cheevers opens the door to his office and ushers in Stathis and Veronica. Cheevers is tall and sweet-mannered.
  EXPRESSION: null
- CHARACTER: Cheevers
  LINE: Hi. C’mon in.
  EXPRESSION: Happy
- CHARACTER: Narrator
  LINE: Cheevers shakes hands with Stathis - they obviously know each other.
  EXPRESSION: null
- CHARACTER: Stathis
  LINE: Hi, Brent. Thanks.
  EXPRESSION: Happy
- CHARACTER: Stathis
  LINE: Veronica Quaife.
  EXPRESSION: Neutral
- CHARACTER: Cheevers
  LINE: Hi.
  EXPRESSION: Neutral
- CHARACTER: Narrator
  LINE: (VERONICA JUST NODS)
  EXPRESSION: null
- CHARACTER: Cheevers
  LINE: Well, OK. What’s the story?
  EXPRESSION: Confused
- CHARACTER: Narrator
  LINE: Although Cheevers has directed this question to Veronica, it is Stathis who answers.
  EXPRESSION: null
- CHARACTER: Stathis
  LINE: She's pregnant and she wants an abortion.
  EXPRESSION: Neutral
- CHARACTER: Cheevers
  LINE: In the middle of the night?
  EXPRESSION: Surprised
- CHARACTER: Stathis
  LINE: We have good reason to think that this child will be deformed.
  EXPRESSION: Neutral
- CHARACTER: Cheevers
  LINE: Yeah, but... in the middle of the night?
  EXPRESSION: Surprised
- CHARACTER: Stathis
  LINE: Look, Brent... please.
  EXPRESSION: Sad
- CHARACTER: Cheevers
  LINE: Is it your child?
  EXPRESSION: Confused
- CHARACTER: Stathis
  LINE: No. It 's the child of a man who is deformed.
  EXPRESSION: Neutral
- CHARACTER: Cheevers
  LINE: Listen, I don't mean to interfere, but... I detect a certain... uncertainty here. You know, there are tests that can be done to determine whether or not...
  EXPRESSION: Neutral
- CHARACTER: Veronica
  LINE: I don' t want tests! Tests can't guarantee anything. The baby could start off normal and then become a monster. I want an abortion! I'll do it myself if I have to!
  EXPRESSION: Angry
- CHARACTER: Narrator
  LINE: Although Veronica speaks quietly, Cheevers can easily see how disturbed she is, how close to the edge. He seems to be picturing Veronica trying to abort her own baby.
  EXPRESSION: null
- CHARACTER: Cheevers
  LINE: No, I don’t think you should do that.
  EXPRESSION: Neutral

::PATHS::
- CHOICE: "Proceed to operating room"
  TARGET: int_operating_room_night
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Operating Room
MOOD: Anxious, Clinical
CHARACTERS: Narrator, Cheevers, Stathis, Veronica
BACKGROUND_IMAGE: operating_room.png
BACKGROUND_EDIT: "Nighttime, spartan clinic operating room, large frosted window, TV above table"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The clinic operating room is surprisingly simple, spartan - really not much more than a standard examination room except for two unusual features. The first unusual feature is the immense floor-to-ceiling window which composes one wall of the room - a legacy from the building’s history as a small office complex. The window has been frosted to provide privacy. The second unusual feature is a TV set above the small operating table. Cheevers adjusts the TV set on its swivel so that Veronica wi11 be able to see it when she lies down on the table. She is, at the moment, sitting quietly in a chair in the corner of the room.
  EXPRESSION: null
- CHARACTER: Cheevers
  LINE: I've found TV to be the best anesthetic.
  EXPRESSION: Neutral
- CHARACTER: Narrator
  LINE: He turns it on. &• commercial, for Pampers is on. Adorable kids toddling everywhere.
  EXPRESSION: null
- CHARACTER: Cheevers
  LINE: Oh, shit.
  EXPRESSION: Embarrassed
- CHARACTER: Stathis
  LINE: Uh... maybe no TV...
  EXPRESSION: Embarrassed
- CHARACTER: Narrator
  LINE: To the men's surprise, Veronica, relieved to actually be in the process of aborting Brundle’s baby, comes out with a hearty laugh.
  EXPRESSION: null
- CHARACTER: Veronica
  LINE: Leave it on. This kid wouldn't look like them anyway.
  EXPRESSION: Happy
- CHARACTER: Narrator
  LINE: Cheevers, relieved to see that he hasn’t blown a very
  EXPRESSION: null

::PATHS::
- CHOICE: "End of excerpt"
  TARGET: end
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Operating Room
MOOD: Shock
CHARACTERS: Narrator, Cheevers, Stathis, Veronica, Brundle
BACKGROUND_IMAGE: operating_room.png
BACKGROUND_EDIT: "Nighttime, sterile operating room, shattered window, glass shards everywhere"

::SCRIPT::
- CHARACTER: Narrator
  LINE: delicate moment, smiles and reaches for the door.
  EXPRESSION: Happy
- CHARACTER: Cheevers
  LINE: Great! OK. I’ll just get you a more appropriate costume and we’ll be on our way in no time ...
  EXPRESSION: Relieved
- CHARACTER: Narrator
  LINE: Cheevers leaves the room. There is an awkward, silent moment between Stathis and Veronica. And then...
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: WITHOUT WARNING, the immense floor-to-ceiling WINDOW of the operating room EXPLODES into the room! Shards of glass and pieces of window frame fly everywhere.
  EXPRESSION: Surprised
- CHARACTER: Narrator
  LINE: BRUNDLE hurtles into the room, the force of his entry carrying him crashing into the operating table which tips over and smashes to the floor.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Stathis stands frozen in the corner of the room, but Brundle ignores him. He wants Veronica.
  EXPRESSION: Scared
- CHARACTER: Narrator
  LINE: Brundle finds Veronica cowering in the corner, blood trickling down her left temple from a glass cut, eyes wide in disbelief. Brundle scrambles to his feet, picks Veronica up and effortlessly tucks her under his arm.
  EXPRESSION: Scared
- CHARACTER: Narrator
  LINE: Then, without the slightest acknowledgment of Stathis, he calmly steps out through the broken window and disappears, taking Veronica, who is too stunned to resist, with him.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Stathis manages to shake off his paralysis, runs to the window and tries to look out, but as he leans against a piece of window frame, he cuts himself on the minute fragments of jagged glass lodged in it. Stathis recoils with the pain, but still manages to catch a glimpse of Brundle, silhouetted in the moonlight, carrying Veronica over the rooftops.
  EXPRESSION: Scared
- CHARACTER: Narrator
  LINE: Now Cheevers whips open the door, folded hospital gown in hand. The room is a complete shambles. Stathis turns to meet his astonished gaze. All he can do is shrug.
  EXPRESSION: Surprised

::PATHS::
- CHOICE: "Follow Brundle"
  TARGET: rooftops
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Rooftops
MOOD: Despair
CHARACTERS: Narrator, Brundle, Veronica
BACKGROUND_IMAGE: rooftops.png
BACKGROUND_EDIT: "Nighttime, city rooftops, overlooking a park, moonlight"

::SCRIPT::
- CHARACTER: Narrator
  LINE: We are with Brundle as he carries the terrified Veronica, over the rooftops.
  EXPRESSION: Afraid
- CHARACTER: Narrator
  LINE: Finally he alights in a cozy little rooftop nook overlooking a park.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Brundle lays Veronica down on the slate of the rooftop.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: His eyes are glistening, moist - are they full of tears?
  EXPRESSION: Sad
- CHARACTER: Narrator
  LINE: He speaks with a voice even harsher and more metallic than before, but there is a strange, rhythmic catch in his voice which might be weeping.
  EXPRESSION: Sad
- CHARACTER: Brundle
  LINE: Why did you want to kill Brundle? The baby will be all that’s left of the real Brundle. Please don’t kill me. Please don’t kill me.
  EXPRESSION: Sad
- CHARACTER: Veronica
  LINE: I can’t have it. I’m afraid!
  EXPRESSION: Afraid
- CHARACTER: Brundle
  LINE: Have the baby. Let me live long enough to see the baby.
  EXPRESSION: Relentless
- CHARACTER: Veronica
  LINE: I can’t! I can’t!
  EXPRESSION: Afraid
- CHARACTER: Brundle
  LINE: Too bad. Too bad.
  EXPRESSION: Flat

::PATHS::
- CHOICE: "Return to the lab"
  TARGET: lab_entry
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Lab
MOOD: Suspense
CHARACTERS: Narrator, Stathis
BACKGROUND_IMAGE: lab_interior.png
BACKGROUND_EDIT: "Darkened lab, door broken open, Stathis entering with tools"

::SCRIPT::
- CHARACTER: Narrator
  LINE: We are inside the darkened lab. There is a sharp "crack” from outside the door, which then slides open: someone has just broken in.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Stathis enters the lab with a crowbar in one hand and what looks like an abnormally large, slim attaché case in the other. A soft bag hangs from his shoulder by a webbed strap.
  EXPRESSION: Determined
- CHARACTER: Narrator
  LINE: Stathis switches on a small lamp and puts down the bag, the crowbar, and the case. He now opens the sleek plastic case to reveal a very expensive Italian over-and-under skeet shotgun - not really a great weapon but obviously the only one instantly accessible to him.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Stathis sits on the couch and calmly assembles the shotgun. He then breaks out a box of shells from the bag and loads each barrel of the gun - two shots only. The barrels are swivelled back into place and locked. The safety is slid to OFF.
  EXPRESSION: Calm
- CHARACTER: Narrator
  LINE: Stathis gets up from the couch and, shotgun in hand, walks over to the metal crank which hangs from the main skylight. He cranks the skylight open wide.
  EXPRESSION: Determined
- CHARACTER: Narrator
  LINE: Stathis now settles down to wait in the nearest chair - which happens to be the old steno chair in front of the computer keyboard. It doesn’t take Stathis long to notice the beige plastic box of discs on the table, and it takes no time at all for him to generate enough curiosity to open the box and flick on the computer’s master switch.
  EXPRESSION: Curious

::PATHS::
- CHOICE: "Investigate computer"
  TARGET: lab_investigation
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Lab
MOOD: Discovery
CHARACTERS: Narrator, Stathis, Brundle
BACKGROUND_IMAGE: lab_interior.png
BACKGROUND_EDIT: "Nighttime, lab interior, computer screen displaying data, third telepod revealed"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Stathis is deep into Brundle’s computer discs. We are close on the computer monitor as it plays back for us the computer-graphics version of the disintegration of the cat and the monkey and their subsequent reintegration as the cat-monkey creature. As before, the following final words flash triumphantly on the screen: FUSION SUCCESSFUL RECEIVER TELEPOD 3
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Stathis is confused.
  EXPRESSION: Confused
- CHARACTER: Narrator
  LINE: CU the words "TELEPOD 3” flashing on the computer screen.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Stathis now switches to another disc whose title is "FUSION PROGRAM. He punches up "FUSION PROGRAM MENU," and finds listed: "BRUNDLEFLY PROJECT."
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: "BRUNDLEFLY PROJECT" is duly punched up, and it produces the following: THE BRUNDLEFLY PROJECT PROBLEM: TO REFINE GENETIC FUSION PROGRAM GOAL: TO DECREASE TO A MINIMUM THE PERCENTAGE OF "FLY" IN BRUNDLEFLY SOLUTION: THE FUSION BY GENE-SPLICING OF BRUNDLEFLY WITH ONE OR MORE "PURE” HUMAN BEINGS GENE-SPLICING METHODOLOGY A. HARDWARE: TELEPOD 1: TRANSMITTER OF SUBJECT A TELEPOD 2: TRANSMITTER OF SUBJECT B TELEPOD 3: RECEIVER FOR GENETICALLY-FUSED A-B COMBINATION SUBJECT
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: CU the words ”TELEPOD 3” on the screen.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Stathis gets up from the chair and takes a quick walk through the lab - shotgun always in hand - looking for this mysterious TELEPOD 3. He soon spots the THIRD TELEPOD, once again covered by the tarpaulin.
  EXPRESSION: Determined
- CHARACTER: Narrator
  LINE: Stathis pulls away the tarp to reveal the third telepod. It is clunkier and less tidy than the other two pods, but it’s basically the same machine. Stathis turns and begins to walk back to the computer.
  EXPRESSION: Null
- CHARACTER: Narrator
  LINE: BUT HE DOESN’T GET THERE, because BRUNDLE drops down on top of him from the skylight!
  EXPRESSION: Surprised
- CHARACTER: Narrator
  LINE: Stathis sprawls on the floor, but doesn’t let go of the shotgun. Brundle lands neatly on his feet and stands crouched, ready to do battle. Stathis swings the shotgun around towards Brundle, and Brundle leaps, grabs the barrel of the gun and holds it away from himself.
  EXPRESSION: Aggressive
- CHARACTER: Narrator
  LINE: Stathis tries desperately to wrench the gun free, but Brundle is much too strong. Brundle grabs Stathis by the wrist with his other hideous hand. He slowly, contemptuously brings the wrist towards his
  EXPRESSION: Struggling

::PATHS::
- CHOICE: "Continue confrontation"
  TARGET: end
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Brundle's Lab
MOOD: Horrific, Desperate, Climactic
CHARACTERS: Brundle, Stathis, Veronica, Narrator
BACKGROUND_IMAGE: brundle_lab.png
BACKGROUND_EDIT: "Dark, industrial science lab, filled with strange equipment and telepods, a sense of decay and terror"

::SCRIPT::
- CHARACTER: Narrator
  LINE: As Stathis watches helplessly, Brundle’s ENTIRE FACE OPENS UP to reveal HIDEOUS FLY MOUTH PARTS!
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: A HUGE FLY TONGUE unfolds and spurts milky, viscous vomit onto Stathis’s clenched fist.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Stathis screams as his fist dissolves into a dripping, simmering, bloody pulp.
  EXPRESSION: Terrified
- CHARACTER: Narrator
  LINE: Near fainting, Stathis drops the shotgun.
  EXPRESSION: Weak
- CHARACTER: Narrator
  LINE: Brundles tongue retracts AND HIS FACE CLOSES AGAIN, leaving no trace that it had ever split open!
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Brundle reaches for it but Stathis manages to hook his foot over it.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: BRUNDLE’S TERRIBLE MAW OPENS AGAIN and more fluid spews out over Stathis’s foot.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The shoe, the sock, the flesh, the bone, all bubble and dissolve and drop away, leaving nothing but a steaming, bloody, cauterized stump.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Brundle’s movements, his facial expressions, are completely dispassionate, insect-effective.
  EXPRESSION: Dispassionate
- CHARACTER: Narrator
  LINE: He methodically begins to suck the liquifying, pulpy flesh back up into his crop, mercilessly probing what was Stathis’s foot with his metallic-green tubular tongue.
  EXPRESSION: Dispassionate
- CHARACTER: Narrator
  LINE: Stathis is past screaming now. He simply nods off, almost gently, into semi-consciousness.
  EXPRESSION: Overwhelmed
- CHARACTER: Narrator
  LINE: Brundle’s face hovers like a bad dream over Stathis’s face.
  EXPRESSION: Ominous
- CHARACTER: Narrator
  LINE: Stathis’s mouth is open, he is breathing deeply as though in the deepest kind of sleep; but his eyes are open, he seems to be aware on some praeter-conscious level.
  EXPRESSION: Conscious
- CHARACTER: Narrator
  LINE: Brundle bends closer to Stathis, closer, inches away...
  EXPRESSION: Ominous
- CHARACTER: Narrator
  LINE: A voice shatters the moment, a voice which comes from behind and above Brundle.
  EXPRESSION: null
- CHARACTER: Veronica
  LINE: Don't kill him! If there's anything human left inside you, don't kill him!
  EXPRESSION: Quietly desperate
- CHARACTER: Narrator
  LINE: Brundle turns to see Veronica peering down at him through the skylight.
  EXPRESSION: null
- CHARACTER: Veronica
  LINE: Please.
  EXPRESSION: Almost a whisper, pleading
- CHARACTER: Narrator
  LINE: Brundle turns back to Stathis, who now curls up in the corner like a spider touched by a lit cigarette.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Brundle hesitates, calculates.
  EXPRESSION: Calculating
- CHARACTER: Narrator
  LINE: Then finally, HIS FACE CLOSES AGAIN and he leaves Stathis, gets up, swings up a support beam to the skylight and Veronica.
  EXPRESSION: null
- CHARACTER: Brundle
  LINE: Help me. Help me. Help me to be human.
  EXPRESSION: Desperate
- CHARACTER: Veronica
  LINE: How?
  EXPRESSION: Curious
- CHARACTER: Narrator
  LINE: Brundle tucks Veronica under one arm and effortlessly swings back down into the lab with her.
  EXPRESSION: Effortless
- CHARACTER: Narrator
  LINE: He leaves her in a corner and goes over to the computer.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: He is not really surprised to see that the computer has already been switched on and that the right disc is up.
  EXPRESSION: Unsurprised
- CHARACTER: Narrator
  LINE: Brundle reaches over to the controller and flips some switches.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Operating lights come on in Telepod 1, then Telepod 2, and then, Veronica notices with a start, in Telepod 3.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Brundle gestures towards the appropriate telepods.
  EXPRESSION: null
- CHARACTER: Brundle
  LINE: I go there. You go there. We come apart, and then, we come together - (INDICATING THIRD TELEPOD) - there. You, and me, and the baby, together. We’ll be the ultimate family. A family of three, joined together in one body, more human than I am alone.
  EXPRESSION: Determined, Ominous
- CHARACTER: Narrator
  LINE: Veronica now realizes exactly what Brundle has in mind.
  EXPRESSION: Realizing
- CHARACTER: Narrator
  LINE: She begins to back away, edging towards the door.
  EXPRESSION: Afraid
- CHARACTER: Veronica
  LINE: Oh, no. You can't... you can’t mean that...
  EXPRESSION: Disbelief, Afraid
- CHARACTER: Narrator
  LINE: Without hesitation, Brundle leaps across the room and grabs her.
  EXPRESSION: Determined
- CHARACTER: Narrator
  LINE: Veronica screams in horror.
  EXPRESSION: Terrified
- CHARACTER: Veronica
  LINE: No! No! I won’t do it!
  EXPRESSION: Screaming
- CHARACTER: Narrator
  LINE: Brundle starts to drag her towards the second telepod.
  EXPRESSION: Determined
- CHARACTER: Narrator
  LINE: Veronica begins to fight Brundle. She smashes at him with her fists, she jams her hands up under his chin and pushes with all her might.
  EXPRESSION: Fighting
- CHARACTER: Narrator
  LINE: AND HIS LOWER JAW COMES RIGHT OFF IN HER HANDS!
  EXPRESSION: Shocked
- CHARACTER: Narrator
  LINE: Brundle releases her.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: She stares in disbelief at the dripping human lower jaw, complete with quivering lip, which she now holds in her hands.
  EXPRESSION: Disbelief
- CHARACTER: Narrator
  LINE: She looks back at Brundle, stunned, mesmerized.
  EXPRESSION: Stunned
- CHARACTER: Narrator
  LINE: Where his jaw was there are now vibrating, twitching insect mouth parts.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Veronica screams.
  EXPRESSION: Terrified
- CHARACTER: Narrator
  LINE: With one sudden, vicious swipe of his claw-hand across her face, Brundle drops Veronica as though she had been pole-axed, severing her scream in mid-air.
  EXPRESSION: Vicious
- CHARACTER: Narrator
  LINE: Brundle’s tubular tongue is now completely exposed, and it stretches outwards and upwards, fusing with the other mouth and nose parts to form a true fly proboscis.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: He writhes and twists like a caterpillar weaving a cocoon as the end of his transformation is finally triggered off.
  EXPRESSION: Transforming
- CHARACTER: Narrator
  LINE: The bulges on his forehead split open and short antennae uncoil and spring erect. At the base of the antennae are several small, black, simple eyes, deep and unfathomable, like bullet holes in the skull.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The dome-like swellings of his temples split open to reveal two damp masses of glistening black spheres, like mounds of caviar, which rapidly begin to swell and multiply until they have formed two huge insect compound eyes which swivel on extremely short stalks.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Brundle’s own human eyes burst like raw eggs and dribble down his face as out of the sockets slide two clusters of short, bristly hairs.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: There is a witness to Brundle’s transformation: Stathis has been edging towards his shotgun, inching his way along the floor, fighting the agony, blacking out for seconds at a time and recovering.
  EXPRESSION: Determined
- CHARACTER: Narrator
  LINE: Brundle is now a completely non-human thing - yet he seems bent on completing his fusion project.
  EXPRESSION: Determined
- CHARACTER: Narrator
  LINE: Whether this is out of a sti11-1iving desire to regain some kind of humanity, or out of mere insect momentum, we can’t tell.
  EXPRESSION: Pondering
- CHARACTER: Narrator
  LINE: In either case, he picks up the unconscious Veronica and places her - is it gently or just fastidiously? - into Telepod 2 and closes the door.
  EXPRESSION: Dispassionate
- CHARACTER: Narrator
  LINE: CU - AUTOMATIC EXTERIOR LATCH OF TELEPOD 2 DOOR SLIDING HOME.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: He goes back to the computer and sets it to time a countdown, which we see on the monitor:
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: COUNTDOWN TO FUSION
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: 60 SECONDS
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Now Brundle gets into Telepod 1 and swings the door shut behind him.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: CU - AUTOMATIC EXTERIOR LATCH OF TELEPOD 1 DOOR SLIDING HOME.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: This is Stathis’s cue. He glances at the monitor.
  EXPRESSION: Alert
- CHARACTER: Narrator
  LINE: CU MONITOR - which reads:
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: COUNTDOWN TO FUSION
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: 28 SECONDS
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Stathis struggles to his knees; then, using the shotgun as a crutch, he manages to stand erect.
  EXPRESSION: Struggling
- CHARACTER: Narrator
  LINE: He limps over to Telepod 2, unable to avoid noticing how frail and unreal Veronica looks, slumped in the corner of the telepod like a doll under glas
  EXPRESSION: Concerned

::SCENE::
LOCATION: Lab
MOOD: Intense, Violent, Horrific
CHARACTERS: Narrator, Stathis, Brundle, Veronica, Brundle-Thing
BACKGROUND_IMAGE: lab.png
BACKGROUND_EDIT: "Damaged, high-tech lab, telepods, sparks, smoke"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Now Stathis props himself up against a support beam and raises the shotgun, resting the barrel on his truncated left forearm.
  EXPRESSION: Determined
- CHARACTER: Narrator
  LINE: From inside Telepod 1, Brundle sees Stathis, understands his intention.
  EXPRESSION: Realizing
- CHARACTER: Narrator
  LINE: Brundle throws himself against the door of his telepod, but it won’t move.
  EXPRESSION: Frantic
- CHARACTER: Narrator
  LINE: He starts to slam his claw-hands against the glass like a pair of sledgehammers, but the glass is immensely strong.
  EXPRESSION: Desperate
- CHARACTER: Narrator
  LINE: CU MONITOR - which reads: COUNTDOWN TO FUSION 13 SECONDS
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Stathis is unsteady, has difficulty controlling his weapon.
  EXPRESSION: Unsteady
- CHARACTER: Narrator
  LINE: Brundle continues to hammer at the glass - NOW WITH SOME SUCCESS, as the glass is beginning to craze in star-shaped patterns under Brundle’s blows!
  EXPRESSION: Desperate
- CHARACTER: Narrator
  LINE: Stathis has now managed to draw a bead on his target - the THICK CLUSTER OF CABLES which connect Veronica’s telepod to the computer and to the lab's power supply.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: CU MONITOR - which reads: COUNTDOWN TO FUSION 5 SECONDS
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: STATHIS FIRES! The cables at the foot of Telepod 2 EXPLODE INTO A BALL OF SPARKS AND FLAME!
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Brundle pounds insanely at the glass of his telepod and the GLASS FINALLY SHATTERS. Brundle reaches out of the telepod and slides open the latch. He swings open the door. He steps out of the telepod...
  EXPRESSION: Insane
- CHARACTER: Narrator
  LINE: CU MONITOR - which flicks from 1 SECOND to: COUNTDOWN TO FUSION 0 SECONDS
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: An intense white light spills out of the open telepod door, enveloping Brundle - who has not quite managed to step completely free - AND THE FRONT THIRD OF THE POD ITSELF!
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Brundle begins to disintegrate, AND SO DOES THE FRONT THIRD OF THE TELEPOD! Brundle and part of the telepod are scrupulously analysed and outlined on the monitor, and then they disappear both from the monitor and from Stathis’s sight.
  EXPRESSION: Disintegrating
- CHARACTER: Narrator
  LINE: Now ONLY TWO-THIRDS OF THE TELEPOD ARE LEFT STANDING, edges jagged, wires hanging, as though its front third had been sliced off by a chain saw. The remains of Telepod 1, looking like some kind of alien ruin, slump sideways under their own, now-unsupported weight.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Stathis turns to Telepod 2 - and releases an audible sigh of relief when he sees that Veronica still lies there, untouched.
  EXPRESSION: Relieved
- CHARACTER: Narrator
  LINE: Suddenly, TELEPOD 3 IMPLODES, sucked in on itself as though a complete vacuum has suddenly appeared at its core.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Warily, apprehensively, Stathis limps over to the smoking rubble of Telepod 3, once again using the shotgun as a crutch.
  EXPRESSION: Apprehensive
- CHARACTER: Narrator
  LINE: Now he stands, swaying unsteadily, in trepidation before the heap of rubble, searching for signs of Brundle. A beat, an then...
  EXPRESSION: Trepidation
- CHARACTER: Narrator
  LINE: OUT OF THE SMOKE AND RUBBLE RISES A THING, a confused mass of insect and human flesh, metal, circuit boards, wires and glass - the result of the FUSION OF BRUNDLE AND TELEPOD 1.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Stathis staggers back in horror.
  EXPRESSION: Horrified
- CHARACTER: Narrator
  LINE: The Brundle-Thing comes after him, dragging parts of its lower body along the floor, pieces of black insect flesh fused with electronic circuitry dropping off it as it comes, a hideous, raging, MORTALLY STRICKEN monstrosity.
  EXPRESSION: Raging
- CHARACTER: Narrator
  LINE: Its claw-hands, which now stick out of its body at Crazy, asymmetrical angles, reach out for Stathis.
  EXPRESSION: Threatening
- CHARACTER: Narrator
  LINE: Stathis twists away but falls crashing to the floor.
  EXPRESSION: Falling
- CHARACTER: Narrator
  LINE: Stathis slides himself backwards along the floor with his good hand, his stump, his chin... anything.
  EXPRESSION: Scrabbling
- CHARACTER: Narrator
  LINE: THE BRUNDLE-THING’S MOUTH PARTS - now located somewhere in the middle of its chest - dribble steaming, corrosive vomit-drop.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Stathis now finds himself jammed into a corner. He has no place else to go.
  EXPRESSION: Trapped
- CHARACTER: Narrator
  LINE: The Brundle-Thing's CLAW-FINGERS TREMBLE as it reaches out for Stathis. Is it trying to attack Stathis or is it reaching out for some kind, any kind of human contact? There is no way for us to know.
  EXPRESSION: Ambiguous
- CHARACTER: Narrator
  LINE: The Brundle-Thing begins to go into a dying spasm, shaking, twitching, shuddering. From somewhere deep within its deformed body comes an unearthly whistling sigh, perhaps more an expression of release than pain.
  EXPRESSION: Dying
- CHARACTER: Narrator
  LINE: Stathis finds himself sobbing uncontrollably as the Brundle-Thing gives a last tremor and then is still.
  EXPRESSION: Sobbing
- CHARACTER: Narrator
  LINE: Stathis crawls his way over to Telepod 2 and unlatches the hatch door.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: He works his way halfway into the pod so that he can stroke the hair of Veronica, who responds to his touch and murmurs as she begins to regain consciousness.
  EXPRESSION: Soothing
- CHARACTER: Stathis
  LINE: Ronnie, Ronnie, it’s OK. I'm here. We came through it. We came through it.
  EXPRESSION: Soothing

::SCENE::
LOCATION: Stathis's Bedroom
MOOD: Calm, Intimate, Uneasy
CHARACTERS: Narrator, Stathis, Veronica
BACKGROUND_IMAGE: bedroom.png
BACKGROUND_EDIT: "Stylish and sumptuous bedroom, night"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Veronica is murmuring in her sleep. She's in bed. Stathis is beside her, caressing her.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: He has an artificial rubber left hand, which looks quite real at first glance.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Their bedroom is very stylish and sumptuous.
  EXPRESSION: null
- CHARACTER: Stathis
  LINE: It's OK, darling. I'm here, everything's OK.
  EXPRESSION: Soothing
- CHARACTER: Narrator
  LINE: Veronica sits up. She is somehow disturbed; maybe it's only because she's still half in her dream. She looks down at her stomach. It's big. She's very pregnant.
  EXPRESSION: Disturbed
- CHARACTER: Veronica
  LINE: It was that dream again! Brundle... Brundle’s baby was being born..
  EXPRESSION: Disoriented
- CHARACTER: Stathis
  LINE: This baby is mine, remember? Yours and mine. The most horrible thing that can happen is that it'll look more like me than you.
  EXPRESSION: Patting Her Tummy
- CHARACTER: Narrator
  LINE: Veronica lies back, dreamily.
  EXPRESSION: Dreamy
- CHARACTER: Veronica
  LINE: Oh, yeah. Yeah. I'm awake now. It's OK.
  EXPRESSION: Waking Up
- CHARACTER: Narrator
  LINE: Stathis smiles and kisses her. Despite what she says, Veronica is still disoriented, unsettled. She begins to sink back into her dream.
  EXPRESSION: Unsettled

::SCENE::
LOCATION: Veronica's Dream
MOOD: Surreal, Beautiful, Metaphorical
CHARACTERS: Narrator, Veronica (dreaming)
BACKGROUND_IMAGE: dreamscape.png
BACKGROUND_EDIT: "Brightly surreal landscape, lush with leaves, ethereal light"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Veronica dreams about a gorgeous CHRYSALIS - a butterfly’s cocoon - which resembles that of a Monarch butterfly.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The chrysalis, a translucent jade-green, hangs from a leaf in a brightly surreal landscape.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The chrysalis begins to twist and turn as something inside it struggles to be born.
  EXPRESSION: Strained
- CHARACTER: Narrator
  LINE: Finally, a BEAUTIFUL HUMAN BABY WITH GOSSAMER, INSECT WINGS emerges. The baby clings to the chrysalis for a few moments, fanning its wings slowly until they dry.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Then the baby takes flight and disappears, LEAVING THE BURST AND SHRIVELLED CHRYSALIS BEHIND.
  EXPRESSION: null

::SCENE::
LOCATION: Stathis's Bedroom
MOOD: Serene (with underlying ambiguity)
CHARACTERS: Narrator, Veronica
BACKGROUND_IMAGE: bedroom.png
BACKGROUND_EDIT: "Stylish and sumptuous bedroom, night, Veronica sleeping"

::SCRIPT::
- CHARACTER: Narrator
  LINE: In her sleep, Veronica is now smiling serenely.
  EXPRESSION: Serene
- CHARACTER: Narrator
  LINE: THE END.
  EXPRESSION: null

