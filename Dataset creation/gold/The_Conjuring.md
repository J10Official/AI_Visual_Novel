



::SCENE::
LOCATION: House Exterior (Porch/Yard)
MOOD: Eerie
CHARACTERS: Andrea, Voice, Grey Cat (implied)
BACKGROUND_IMAGE: house_exterior_porch.png
BACKGROUND_EDIT: "Nighttime, dark surroundings, bird feeder hanging"

::SCRIPT::
- CHARACTER: Narrator
  LINE: As she gets up on her tiptoes to hang it.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: A HISS OF A VOICE CALLS HER NAME.
  EXPRESSION: null
- CHARACTER: Voice
  LINE: Andrea --
  EXPRESSION: Hissing
- CHARACTER: Narrator
  LINE: She slowly turns her head, can’t figure out where it’s coming from as she scans the darkness.
  EXPRESSION: Confused
- CHARACTER: Andrea
  LINE: -- Hello?
  EXPRESSION: Confused
- CHARACTER: Narrator
  LINE: No answer. More confused than scared, she hangs up the bird feeder. Then just as she’s about to head inside, she spots a large, mangy-looking GREY CAT passing by the bottom step of the porch, it looks oddly similar to the one in the opening.
  EXPRESSION: null
- CHARACTER: Andrea
  LINE: Oh, hello --
  EXPRESSION: Curious
- CHARACTER: Narrator
  LINE: It continues walking. She heads down the steps to catch up.
  EXPRESSION: null
- CHARACTER: Andrea
  LINE: Where’d you come from? C’mere kitty.
  EXPRESSION: Playful
- CHARACTER: Narrator
  LINE: The cat walks around the corner of the house.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Andrea’s pov, as she walks around the corner. There’s no cat. She looks around for a place it could have gone, but there isn’t one. Her expression says it all, that’s weird.
  EXPRESSION: Confused

::PATHS::
- CHOICE: "Head inside"
  TARGET: kitchen_back_door
  STATE_CHANGE: confusion = +1
  CONDITION: null

::SCENE::
LOCATION: Kitchen - Back Door
MOOD: Domestic with unease
CHARACTERS: Andrea, Roger, Carolyn
BACKGROUND_IMAGE: kitchen_interior.png
BACKGROUND_EDIT: "Daytime, boxes, newly moved in, small clock and monkeys on windowsill"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Andrea comes back in just as Roger enters from the hallway. In passing --
  EXPRESSION: null
- CHARACTER: Andrea
  LINE: Were you calling me?
  EXPRESSION: Curious
- CHARACTER: Roger
  LINE: No.
  EXPRESSION: Neutral
- CHARACTER: Narrator
  LINE: As she walks away --
  EXPRESSION: null
- CHARACTER: Andrea
  LINE: I think there’s a cat that lives here --
  EXPRESSION: Thoughtful
- CHARACTER: Narrator
  LINE: Andrea continues out of the kitchen as Roger comes up behind Carolyn, who’s unpacking a small clock. Sets it on the windowsill next to the monkeys. He slides his arms around her and kisses her neck, she likes it.
  EXPRESSION: Loving
- CHARACTER: Carolyn
  LINE: Careful -- this may turn into something fun.
  EXPRESSION: Playful
- CHARACTER: Roger
  LINE: -- If only I had the energy. I was thinking about running into town and grabbing a pizza at that place we passed.
  EXPRESSION: Tired
- CHARACTER: Carolyn
  LINE: That’d be great.
  EXPRESSION: Happy
- CHARACTER: Narrator
  LINE: She turns and faces him. Loves this man dearly.
  EXPRESSION: null
- CHARACTER: Carolyn
  LINE: Thank you for this. I know it was a lot for us to chew off, but it’s going to be great, isn’t it --
  EXPRESSION: Hopeful
- CHARACTER: Roger
  LINE: Yeah -- it is.
  EXPRESSION: Reassuring

::PATHS::
- CHOICE: "Continue settling in"
  TARGET: perron_house_master_bedroom
  STATE_CHANGE: energy_roger = -1
  CONDITION: null

::SCENE::
LOCATION: Perron House - Master Bedroom
MOOD: Ominous
CHARACTERS: Carolyn, Roger, Sadie (O.C.)
BACKGROUND_IMAGE: master_bedroom.png
BACKGROUND_EDIT: "Nighttime, unpacked boxes, matching bedroom set, window overlooking tree, flickering lights"

::SCRIPT::
- CHARACTER: Narrator
  LINE: A matching bedroom set has been set up. Numerous boxes are stacked and waiting to be unpacked as Carolyn pulls some clothes from a wardrobe box at the foot of her bed and walks them into -- THE CLOSET Just as she begins to hang them up, the noise of CREAKING WOOD draws her attention to the ceiling where it sounds like someone’s trying to walk quietly then it stops.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: She’s a little unnerved, walks back out into THE BEDROOM and crosses to a nearby window. Looks out to a tree, its leaves rustling in the wind. She cranes her head to see if any of the branches are touching the roof above the closet. Can’t tell.
  EXPRESSION: Unnerved
- CHARACTER: Narrator
  LINE: Just as she’s about to turn away, she notices Sadie down in the yard near the front porch below, nervously pacing back and forth.
  EXPRESSION: Concerned
- CHARACTER: Roger
  LINE: I don’t know what her problem is. I’ve tried ten times to get her to come inside.
  EXPRESSION: Annoyed
- CHARACTER: Narrator
  LINE: She turns, sees Roger setting a box down amongst the others.
  EXPRESSION: null
- CHARACTER: Roger
  LINE: Last box for tonight. I’m beat.
  EXPRESSION: Tired
- CHARACTER: Carolyn
  LINE: We can’t just leave her out there, she might run away.
  EXPRESSION: Concerned
- CHARACTER: Roger
  LINE: I’ll find something to tether her to. Maybe a night outside will help change her mind.
  EXPRESSION: Resigned
- CHARACTER: Narrator
  LINE: As Roger heads back out --
  EXPRESSION: null
- CHARACTER: Carolyn
  LINE: You weren’t just on the roof, were you?
  EXPRESSION: Suspicious
- CHARACTER: Narrator
  LINE: He turns around, huh?
  EXPRESSION: Surprised
- CHARACTER: Carolyn
  LINE: I heard something, sounded like footsteps.
  EXPRESSION: Concerned
- CHARACTER: Roger
  LINE: It’s an old house honey, it’s going to make some noises.
  EXPRESSION: Dismissive
- CHARACTER: Narrator
  LINE: The lights flicker for a moment.
  EXPRESSION: null
- CHARACTER: Roger
  LINE: Oh great.
  EXPRESSION: Annoyed
- CHARACTER: Carolyn
  LINE: Maybe grab a flashlight too --
  EXPRESSION: Practical
- CHARACTER: Narrator
  LINE: Roger heads out.
  EXPRESSION: null

::PATHS::
- CHOICE: "Go to sleep"
  TARGET: master_bedroom_later
  STATE_CHANGE: fear_carolyn = +1, unease = +1
  CONDITION: null

::SCENE::
LOCATION: Master Bedroom
MOOD: Terrifying
CHARACTERS: Carolyn, Roger (asleep)
BACKGROUND_IMAGE: master_bedroom.png
BACKGROUND_EDIT: "Nighttime, bed, sleeping Roger, Carolyn awake and disturbed"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Carolyn’s eyes open, she’s awakened to what sounds like the distant screams of hundreds of children, but that can’t be right. She glances to Roger, who is sound asleep. She slips out of bed to investigate.
  EXPRESSION: Terrified

::PATHS::
- CHOICE: "Investigate the sound"
  TARGET: house_back_porch
  STATE_CHANGE: fear_carolyn = +2
  CONDITION: null

::SCENE::
LOCATION: House - Back Porch
MOOD: Terrified then humorous, ending with unease
CHARACTERS: Carolyn, Roger
BACKGROUND_IMAGE: house_back_porch.png
BACKGROUND_EDIT: "Nighttime, woods in background, sounds of 'screaming children' / 'tree frogs'"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Carolyn comes out the back door. Listens, it’s much louder. Her attention is drawn to the woods directly behind the house where the screaming is coming from.
  EXPRESSION: Terrified
- CHARACTER: Narrator
  LINE: A HAND touches her shoulder, she about jumps out of her skin. She whirls. Roger is standing right behind her.
  EXPRESSION: Startled
- CHARACTER: Roger
  LINE: Whoa -- sorry.
  EXPRESSION: Apologetic
- CHARACTER: Narrator
  LINE: Carolyn slowly turns back around to face the woods.
  EXPRESSION: null
- CHARACTER: Carolyn
  LINE: What is that?
  EXPRESSION: Terrified
- CHARACTER: Roger
  LINE: Tree frogs -- about as big as softballs. They’re fucking.
  EXPRESSION: Amused
- CHARACTER: Narrator
  LINE: She looks back at him over her shoulder.
  EXPRESSION: null
- CHARACTER: Carolyn
  LINE: And you know this because?
  EXPRESSION: Skeptical
- CHARACTER: Roger
  LINE: I used to catch them as a kid at my Grand-dad’s.
  EXPRESSION: Explaining
- CHARACTER: Narrator
  LINE: Carolyn looks back out into the night.
  EXPRESSION: null
- CHARACTER: Carolyn
  LINE: Sounds like some pretty rough sex.
  EXPRESSION: Amused
- CHARACTER: Narrator
  LINE: Roger playfully pulls her into an embrace.
  EXPRESSION: Playful
- CHARACTER: Roger
  LINE: I think it’s going to take some time for this city girl to get used to this country living.
  EXPRESSION: Loving
- CHARACTER: Carolyn
  LINE: I think you’re right.
  EXPRESSION: Accepting
- CHARACTER: Narrator
  LINE: She snuggles up.
  EXPRESSION: Loving
- CHARACTER: Carolyn
  LINE: You still too tired?
  EXPRESSION: Coy
- CHARACTER: Roger
  LINE: Those frogs make you horny?
  EXPRESSION: Teasing
- CHARACTER: Carolyn
  LINE: No -- you do.
  EXPRESSION: Loving
- CHARACTER: Narrator
  LINE: As they head in, Carolyn’s gaze drifts back over her shoulder one more time into the darkness, still slightly uneasy.
  EXPRESSION: Uneasy

::PATHS::
- CHOICE: "Head inside for the night"
  TARGET: house_exterior_later
  STATE_CHANGE: fear_carolyn = -1, romance = +1, unease = +1
  CONDITION: null

::SCENE::
LOCATION: House Exterior
MOOD: Foreboding
CHARACTERS: Narrator
BACKGROUND_IMAGE: house_exterior.png
BACKGROUND_EDIT: "Nighttime, cloudy sky, house with ill-boding presence, silence"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Clouds have moved in, swallowing any illumination from the moon and stars, giving the house an ill-boding presence. The frogs have stopped, replaced by a lingering, unholy silence.
  EXPRESSION: null

::PATHS::
- CHOICE: "Awaken to morning"
  TARGET: house_upstairs_hallway
  STATE_CHANGE: fear = +1
  CONDITION: null

::SCENE::
LOCATION: House - Upstairs Hallway
MOOD: Mundane with hints of weirdness
CHARACTERS: Carolyn, Cindy
BACKGROUND_IMAGE: upstairs_hallway.png
BACKGROUND_EDIT: "Morning light, unpacked boxes, bathroom door"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Carolyn, wearing a robe, comes out of the bedroom, side steps a few boxes. Morning light streaks in through several windows, illuminating the fact that the Perrons are far from being unpacked.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The bathroom door opens and Cindy sticks her head out --
  EXPRESSION: null
- CHARACTER: Cindy
  LINE: Do you think maybe we could’ve bought a house that has a toilet that works --
  EXPRESSION: Annoyed
- CHARACTER: Carolyn
  LINE: Tell your dad.
  EXPRESSION: Dismissive
- CHARACTER: Narrator
  LINE: As Carolyn walks away --
  EXPRESSION: null
- CHARACTER: Cindy
  LINE: And there was this really funky smell in my bedroom last night -- like something died.
  EXPRESSION: Concerned
- CHARACTER: Carolyn
  LINE: Is it there now?
  EXPRESSION: Practical
- CHARACTER: Cindy
  LINE: No.
  EXPRESSION: Neutral
- CHARACTER: Carolyn
  LINE: Problem solved.
  EXPRESSION: Dismissive
- CHARACTER: Narrator
  LINE: Cindy rolls her eyes, then retreats back into the bathroom.
  EXPRESSION: Annoyed

::PATHS::
- CHOICE: "Continue morning routine"
  TARGET: house_stairs
  STATE_CHANGE: normalcy = +1, unease = +1
  CONDITION: null

::SCENE::
LOCATION: House - Stairs
MOOD: Curious
CHARACTERS: Carolyn
BACKGROUND_IMAGE: house_stairs.png
BACKGROUND_EDIT: "Morning light, clock at base of stairs"

::SCRIPT::
- CHARACTER: Narrator
  LINE: As Carolyn passes a clock at the base of the stairs, she notices that it reads: 5:15 AM. She stops, checks her watch, resets the clock to 7:38 AM.
  EXPRESSION: Curious

::PATHS::
- CHOICE: "Go to the kitchen"
  TARGET: kitchen_morning
  STATE_CHANGE: unease_carolyn = +1, confusion = +1
  CONDITION: null

::SCENE::
LOCATION: Kitchen
MOOD: Eerie
CHARACTERS: Carolyn, Andrea, Roger
BACKGROUND_IMAGE: kitchen_interior.png
BACKGROUND_EDIT: "Morning, window ledge with deformed wax monkeys, stopped clock, packing boxes"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Carolyn crosses to a packing box on the counter. Digs a kettle out of it. She moves to the sink and as she turns on the water to fill it --
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: -- she freezes. On the window ledge before her are --
  EXPRESSION: Startled
- CHARACTER: Narrator
  LINE: -- The THREE WAX MONKEYS, but instead of being lined up in a row like they were before, they are now facing each other -- their heads all melted into one, like some deformed creature.
  EXPRESSION: Horrified
- CHARACTER: Narrator
  LINE: She then notices that the small clock she put next to them has stopped at 5:15 as well --
  EXPRESSION: Shocked
- CHARACTER: Andrea
  LINE: Mommy, where’s Sadie?
  EXPRESSION: Inquisitive
- CHARACTER: Narrator
  LINE: Carolyn turns to see Andrea standing at the kitchen door.
  EXPRESSION: null
- CHARACTER: Carolyn
  LINE: She’s out front. Why don’t you see if she’ll come in. She’s got to be hungry.
  EXPRESSION: Dismissive
- CHARACTER: Narrator
  LINE: Andrea tears out of the kitchen, dodging Roger as he enters.
  EXPRESSION: null
- CHARACTER: Roger
  LINE: Slow down there, kiddo.
  EXPRESSION: Playful
- CHARACTER: Narrator
  LINE: He looks to Carolyn standing at the sink, knows something’s up.
  EXPRESSION: Concerned
- CHARACTER: Roger
  LINE: What is it?
  EXPRESSION: Concerned
- CHARACTER: Narrator
  LINE: She steps aside, showing him the monkeys. As Roger approaches --
  EXPRESSION: null
- CHARACTER: Roger
  LINE: -- Damn. Is the ledge hot?
  EXPRESSION: Surprised
- CHARACTER: Carolyn
  LINE: Not at all. And look at the clock -- it stopped at 5:15. So did the one in the hall.
  EXPRESSION: Spooked

::PATHS::
- CHOICE: "Check on Sadie"
  TARGET: front_of_house_same
  STATE_CHANGE: fear_carolyn = +2, fear_roger = +1
  CONDITION: null

::SCENE::
LOCATION: Front of House
MOOD: Horrifying
CHARACTERS: Andrea, Sadie (dead)
BACKGROUND_IMAGE: front_of_house.png
BACKGROUND_EDIT: "Morning, front porch, bush obscuring view, iron post with chain"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Andrea comes out of the front door. She sees an iron post pounded into the ground with a chain snaking off it. Sadie’s tail is visible, but a full view of her is hidden by a bush at the bottom of the stairs.
  EXPRESSION: null
- CHARACTER: Andrea
  LINE: Sadie --
  EXPRESSION: Calling
- CHARACTER: Narrator
  LINE: The tail remains motionless.
  EXPRESSION: Concerned
- CHARACTER: Andrea
  LINE: Wake up girl --
  EXPRESSION: Calling
- CHARACTER: Narrator
  LINE: Andrea takes a step down to the next. She claps her hands together.
  EXPRESSION: Encouraging
- CHARACTER: Andrea
  LINE: C’mon girl -- time for breakfast!
  EXPRESSION: Encouraging
- CHARACTER: Narrator
  LINE: There’s still no response --
  EXPRESSION: Concerned
- CHARACTER: Narrator
  LINE: Andrea comes down off the last step, she blanches. Her little lips start to tremble at what she sees.
  EXPRESSION: Terrified
- CHARACTER: Narrator
  LINE: Sadie lies dead on the ground, the chain wrapped aroun
  EXPRESSION: Horrified

::PATHS::
- CHOICE: "End of excerpt"
  TARGET: end
  STATE_CHANGE: sadness_andrea = +5, horror_family = +5
  CONDITION: null

::SCENE::
LOCATION: Black Screen
MOOD: Ominous
CHARACTERS: Ed (V.O.)
BACKGROUND_IMAGE: black_screen.png
BACKGROUND_EDIT: "Pure black screen"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Over black.
  EXPRESSION: null
- CHARACTER: Ed
  LINE: Fear is defined as a feeling of agitation and anxiety caused by the presence or imminence of danger. I don’t care if it’s a demon, a ghost, a spirit or an entity -- they all feed on it.
  EXPRESSION: null
- CHARACTER: Ed
  LINE: Take Maurice here --
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue to lecture"
  TARGET: lecture_hall
  STATE_CHANGE: fear = +1
  CONDITION: null

::SCENE::
LOCATION: Lecture Hall
MOOD: Informative, Creepy
CHARACTERS: Ed, Lorraine Warren, Maurice, Catholic Priest, Jerome Davis, Afro, Glasses, Ponytail, Narrator
BACKGROUND_IMAGE: lecture_hall.png
BACKGROUND_EDIT: "Nighttime, stage with podium, audience of students, large screen showing film footage"

::SCRIPT::
- CHARACTER: Narrator
  LINE: ED and LORRAINE WARREN (early thirties) are up on a stage standing behind a podium. An audience of three hundred captivated college students are seated before them as rough film footage rolls on a LARGE SCREEN of a despondent looking man, rail thin, late 20’s, sitting in a chair. His eyes are black, matching his hair. His skin is pasty white. A Catholic priest is next to him, reciting Latin from a bible in barely audible words.
  EXPRESSION: null
- CHARACTER: Ed
  LINE: -- He was a French Canadian farmer with nothing more than a third grade education -- yet after being possessed by a demon, spoke some of the best Latin I had ever heard -- sometimes backwards. He had been molested by his father, who also exposed him to bestiality. Evil found its home in this man because he was conflicted, and forced into this -- he never had a choice. He thought he was saving his wife by shooting her -- like his father did to his mother.
  EXPRESSION: null
- CHARACTER: Lorraine
  LINE: If you look at his eyes, you can see them tearing blood onto his shirt.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Maurice’s white T-shirt slowly starts to get blotted with drips of blood; dark, crimson red. He suddenly SCREAMS OUT IN PAIN, his body writhing.
  EXPRESSION: Afraid
- CHARACTER: Lorraine
  LINE: And upside down crosses started appearing on his body.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: We see Ed lifting up the side of Maurice’s shirt, exposing for the camera.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: TWO UPSIDE DOWN CROSSES pushing OUT at his skin from the inside. Camera closes in.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The audience can’t believe what they’re seeing.
  EXPRESSION: Surprised
- CHARACTER: Ed
  LINE: That’s good, Jerome, why don’t you hit the lights --
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: As the house lights kick back on, we see JEROME DAVIS (20’s), Ed and Lorraine’s technical assistant standing in the back of the lecture hall. He has longish hair, wears cords and a flannel shirt. A leather necklace with peace sign is draped around his neck. He turns the projector off.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Ed and Lorraine are in the middle of a Q & A with the audience. A male student with a tie-dyed shirt and wild Afro is standing up.
  EXPRESSION: null
- CHARACTER: Lorraine
  LINE: -- We investigate roughly a hundred or so cases a year.
  EXPRESSION: null
- CHARACTER: Afro
  LINE: Cool. Thanks.
  EXPRESSION: Happy
- CHARACTER: Narrator
  LINE: As Afro takes a seat, hands go up. Ed points to another student who wears GLASSES four rows back. He gets to his feet.
  EXPRESSION: null
- CHARACTER: Glasses
  LINE: This is some creepy shit you two do for a living --
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Subtle laughs escape from the crowd.
  EXPRESSION: Happy
- CHARACTER: Glasses
  LINE: So how do you keep these things from going after you?
  EXPRESSION: null
- CHARACTER: Ed
  LINE: We don’t get personally involved with people we’re working with or what we’re investigating -- it makes you emotionally vulnerable which gives them a way in. And of course, our faith in God.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: He sits back down. Hands fly up again. Lorraine points to a female student with a PONYTAIL in the front row, who gets to her feet. She seems a little hesitant to speak, then --
  EXPRESSION: null
- CHARACTER: Ponytail
  LINE: -- I wake up at night sometimes and it feels like someone’s laying next to me. Have you ever dealt with anything like that before?
  EXPRESSION: Afraid
- CHARACTER: Lorraine
  LINE: Many times.
  EXPRESSION: null
- CHARACTER: Lorraine
  LINE: Does it scare you?
  EXPRESSION: null
- CHARACTER: Ponytail
  LINE: I’m a little freaked, yeah.
  EXPRESSION: Afraid
- CHARACTER: Lorraine
  LINE: Freaked is normal, do you feel threatened?
  EXPRESSION: null
- CHARACTER: Ponytail
  LINE: -- Not really. It’s just weird.
  EXPRESSION: null
- CHARACTER: Lorraine
  LINE: Come here for a sec --
  EXPRESSION: Gentle
- CHARACTER: Narrator
  LINE: Lorraine moves up to the edge of the stage, joining the girl who does the same.
  EXPRESSION: null
- CHARACTER: Lorraine
  LINE: Give me your hands.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The girl offers them to her. Lorraine takes hold, then closes her eyes. A moment later --
  EXPRESSION: null
- CHARACTER: Lorraine
  LINE: The bed you sleep in, belonged to your Grandmother, didn’t it?
  EXPRESSION: null
- CHARACTER: Ponytail
  LINE: Yeah.
  EXPRESSION: Amazed
- CHARACTER: Lorraine
  LINE: And you were very close before she died.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Ponytail is getting blown away.
  EXPRESSION: Surprised
- CHARACTER: Ponytail
  LINE: She raised me.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Lorraine opens her eyes.
  EXPRESSION: null
- CHARACTER: Lorraine
  LINE: It’s her.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Ponytail’s eyes well as she tries to contain her emotions.
  EXPRESSION: Afraid
- CHARACTER: Lorraine
  LINE: You need to let her know that you’re okay so she can move on. She still worries about you.
  EXPRESSION: null
- CHARACTER: Ponytail
  LINE: How do I do that?
  EXPRESSION: null
- CHARACTER: Lorraine
  LINE: Next time you have that feeling, tell her.
  EXPRESSION: Gentle
- CHARACTER: Narrator
  LINE: Lorraine lets go of her hands. As Ponytail sits back down, Ed nods to another male student in the front row. Wears a beanie.
  EXPRESSION: null
- CHARACTER: Glasses
  LINE: I’d love to know what scares you the most?
  EXPRESSION: null
- CHARACTER: Ed
  LINE: Being married to a clairvoyant -- there’s not a whole lot I can get away with.
  EXPRESSION: Happy
- CHARACTER: Narrator
  LINE: The crowd laughs.
  EXPRESSION: Happy

::PATHS::
- CHOICE: "Exit lecture hall"
  TARGET: auditorium_parking_lot
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Auditorium Parking Lot
MOOD: Casual, Amused
CHARACTERS: Jerome, Ed, Lorraine, Ponytail, Narrator
BACKGROUND_IMAGE: auditorium_parking_lot.png
BACKGROUND_EDIT: "Nighttime, VW van, Plymouth car"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Jerome slides open the side door of a VW van. There’s a sticker on the window that reads, “When this van’s a rockin’, don’t bother knockin’”. He sets the projector next to an array of other electronic equipment, then turns to Ed and Lorraine, who are about to get into a Plymouth parked right next to him.
  EXPRESSION: null
- CHARACTER: Ed
  LINE: So, you feel like Chinese?
  EXPRESSION: Happy
- CHARACTER: Jerome
  LINE: I hate to bail on you, but I think I’m going to do some “tutoring”.
  EXPRESSION: Happy
- CHARACTER: Narrator
  LINE: Ed and Lorraine are slightly confused, until Jerome turns and smiles at a young woman approaching them. It’s the Pony Tail girl.
  EXPRESSION: Surprised
- CHARACTER: Narrator
  LINE: Ed lets an amused laugh escape his lips as he gets into the car.
  EXPRESSION: Happy

::PATHS::
- CHOICE: "Leave the parking lot"
  TARGET: perron_house_side
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Perron House - Side of House
MOOD: Concerned
CHARACTERS: Roger, Carl, Carolyn, Narrator
BACKGROUND_IMAGE: perron_house_side.png
BACKGROUND_EDIT: "Daytime, guy peering into a septic system hole, fenced garden with scarecrow, big rig parked"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Roger approaches a guy wearing incredibly dirty pants and shirt, who’s peering down a hole in the ground into a septic system, Carolyn can be seen in the background tending to a newly sprouting, completely fenced in garden. A SCARECROW, secured to a make-shift cross of 2x4’s, stands at attention in the middle of it. It’s wearing overalls, plaid shirt and donning a wig with shoulder length hair capped over a small pillow that has a crude face drawn on. Roger’s big rig is parked next to the barn.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Roger gets to the guy, who turns and faces him. His shirt has a name tag, reads: Carl.
  EXPRESSION: null
- CHARACTER: Roger
  LINE: Did you find the problem?
  EXPRESSION: null
- CHARACTER: Carl
  LINE: Yeah -- but you’re not going to like it.
  EXPRESSION: null
- CHARACTER: Roger
  LINE: They teach you guys to say that, right?
  EXPRESSION: Happy
- CHARACTER: Narrator
  LINE: Carl isn’t humored.
  EXPRESSION: Angry
- CHARACTER: Carl
  LINE: It’s the septic -- needs to be replaced. It’s got to be at least forty years old.
  EXPRESSION: null
- CHARACTER: Roger
  LINE: Can’t you just rig it somehow?
  EXPRESSION: null
- CHARACTER: Carl
  LINE: Someone’s already used that one up.
  EXPRESSION: null
- CHARACTER: Roger
  LINE: So -- what’re we looking at?
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Carl runs some numbers in his head.
  EXPRESSION: null
- CHARACTER: Carl
  LINE: All in -- about fourteen grand.
  EXPRESSION: null

::PATHS::
- CHOICE: "Discuss with Carolyn"
  TARGET: garden_right_after
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Garden
MOOD: Anxious, Worried
CHARACTERS: Roger, Carolyn, Narrator
BACKGROUND_IMAGE: garden.png
BACKGROUND_EDIT: "Daytime, Carolyn tending garden, stressed Roger"

::SCRIPT::
- CHARACTER: Narrator
  LINE: A stressed Roger stands opposite Carolyn, who continues to tend the garden.
  EXPRESSION: null
- CHARACTER: Roger
  LINE: Seven grand for the new electrical and now fourteen for this --
  EXPRESSION: Angry
- CHARACTER: Carolyn
  LINE: We knew there could be problems, honey.
  EXPRESSION: null
- CHARACTER: Roger
  LINE: Yeah, but I don’t know how much more we can afford.
  EXPRESSION: Angry
- CHARACTER: Narrator
  LINE: She stops. Looks at him, what do you mean?
  EXPRESSION: Surprised
- CHARACTER: Narrator
  LINE: Roger takes a beat.
  EXPRESSION: null
- CHARACTER: Roger
  LINE: I got a call from Mike this morning -- because of this damn gas crunch, they’re going to have to start laying people off.
  EXPRESSION: null
- CHARACTER: Carolyn
  LINE: Does that mean you?
  EXPRESSION: Afraid
- CHARACTER: Roger
  LINE: I’m not exactly senior there --
  EXPRESSION: null

::PATHS::
- CHOICE: "End of discussion"
  TARGET: garden_night
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Garden
MOOD: Eerie, Foreboding
CHARACTERS: Narrator
BACKGROUND_IMAGE: garden_night.png
BACKGROUND_EDIT: "Nighttime, full moon spotlights scarecrow, fully flourishing garden"

::SCRIPT::
- CHARACTER: Narrator
  LINE: A full moon spotlights THE SCARECROW like it’s standing center stage. It’s now surrounded by a FULLY FLOURISHING GARDEN; tall rows of corn stalks, bright yellow squash, red tomatoes and beans.
  EXPRESSION: null

::PATHS::
- CHOICE: "Move inside"
  TARGET: house_upstairs_hallway
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: House - Upstairs Hallway
MOOD: Quiet, Anticipatory
CHARACTERS: Carolyn, Narrator
BACKGROUND_IMAGE: house_upstairs_hallway.png
BACKGROUND_EDIT: "Late night, upstairs hallway, Carolyn with laundry"

::SCRIPT::
- CHARACTER: Narrator
  LINE: It’s late. Carolyn has a basket of laundry tucked under her arm as she heads down the hallway toward her room at the end.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: She stops at the closed bathroom door which ha
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue"
  TARGET: end
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Cindy's Room
MOOD: Mundane
CHARACTERS: Narrator, Cindy (O.C.), Carolyn
BACKGROUND_IMAGE: null
BACKGROUND_EDIT: "Daytime, phone cord on floor, a girl's bedroom"

::SCRIPT::
- CHARACTER: Narrator
  LINE: a phone cord running across the floor from Cindy’s room into it.
  EXPRESSION: null
- CHARACTER: Cindy
  LINE: -- School basically sucks, there’s no cute guys -- and there’s so many friggin bugs --
  EXPRESSION: Annoyed
- CHARACTER: Narrator
  LINE: Carolyn just sighs as she opens the door. Sees Cindy standing in front of a mirror, phone to ear, comparing two different colors of eye shadow, closing one eye at a time.
  EXPRESSION: null
- CHARACTER: Carolyn
  LINE: Bed. Five minutes.
  EXPRESSION: Neutral
- CHARACTER: Narrator
  LINE: She closes the door.
  EXPRESSION: null

::SCENE::
LOCATION: Andrea's Room
MOOD: Calm
CHARACTERS: Narrator, Andrea, Cat
BACKGROUND_IMAGE: null
BACKGROUND_EDIT: "Nighttime, cozy girl's room, lamp light"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Paper butterflies adorn her walls. Stuffed animals line a small shelf above a vanity mirror and dresser. An Easy Bake oven and Barbie play-set are lined up neatly against a wall.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Andrea is under her covers in a frilly four posted bed, head propped slightly by a pillow as she reads a book. A lamp on a nightstand next to her cascades a four foot radius of light.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Her body tightens as she catches a quick glimpse of something furry jumping onto her bed, but her book has obscured a full view, she slowly lowers it to get a better look, finds the cat she saw earlier standing on the foot of her bed.
  EXPRESSION: Startled
- CHARACTER: Narrator
  LINE: It’s looking right at her.
  EXPRESSION: null
- CHARACTER: Andrea
  LINE: How’d you get in here?
  EXPRESSION: Surprised
- CHARACTER: Narrator
  LINE: As she sits upright, the cat scurries off the bed and out of her room into the hallway.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Andrea scrambles out from under the covers and quickly follows. She looks out her door in time to see the cat slip into Cindy’s room just down the hall.
  EXPRESSION: Curious

::SCENE::
LOCATION: Hallway
MOOD: Observation
CHARACTERS: Narrator, Andrea, Cindy (O.C.), Carolyn (O.C.)
BACKGROUND_IMAGE: null
BACKGROUND_EDIT: "Nighttime, residential hallway"

::SCRIPT::
- CHARACTER: Narrator
  LINE: As Andrea moves to Cindy’s room, she can hear her sister still talking on the phone in the bathroom. Her mom is folding clothes on the bed in the master bedroom at the end, unaware of her presence.
  EXPRESSION: null

::SCENE::
LOCATION: Cindy's Room
MOOD: Mysterious
CHARACTERS: Narrator, Andrea, Cat, Carolyn
BACKGROUND_IMAGE: null
BACKGROUND_EDIT: "Nighttime, blacklight glowing posters, messy room"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Andrea stands in the doorway looking to see where the cat went. Her face is hit by a PURPLE HUE cascading from a BLACKLIGHT hanging above a bed; posters of The Jackson Five, peace signs and Alice in Wonderland, all glow from the light. Scattered clothes litter the floor. The bed’s unmade.
  EXPRESSION: Curious
- CHARACTER: Narrator
  LINE: Andrea can’t see the cat anywhere, then she hears it HISSING from under the bed.
  EXPRESSION: Surprised
- CHARACTER: Andrea
  LINE: What’s wrong, Kitty?
  EXPRESSION: Concerned
- CHARACTER: Narrator
  LINE: Andrea comes into the room and over to the bed.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: She kneels. As she looks underneath, her eyes immediately fall upon a Raggedy Anne doll, seemingly staring at her, scares her slightly. The hissing starts up again, but she can’t see where the cat is as her vision is obscured by other dolls stuffed under the bed.
  EXPRESSION: Scared
- CHARACTER: Narrator
  LINE: She reaches in and moves a couple aside, sees the cat, but her breath gets caught in her throat, the blacklight has made its eyes look wild, almost demonic as it stares at something that’s seemingly right behind her. She snaps a look back over her shoulder, but nothing’s there.
  EXPRESSION: Terrified
- CHARACTER: Narrator
  LINE: The cat suddenly bolts right past her, the movement startling Andrea, who instinctively recoils. She watches the cat slip through a partially opened closet door into the darkness beyond.
  EXPRESSION: Startled
- CHARACTER: Narrator
  LINE: As she gets to her feet, Carolyn appears in the doorway.
  EXPRESSION: null
- CHARACTER: Carolyn
  LINE: Hey, you’re supposed to be asleep.
  EXPRESSION: Neutral
- CHARACTER: Andrea
  LINE: I saw that cat again, it went into the closet.
  EXPRESSION: Urgent
- CHARACTER: Narrator
  LINE: Andrea heads to it. A very curious Carolyn flips a light switch on the wall as she enters.
  EXPRESSION: null
- CHARACTER: Carolyn
  LINE: Really--?
  EXPRESSION: Curious
- CHARACTER: Narrator
  LINE: She joins Andrea at the closet. Opens the door wider.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Carolyn reaches overhead and pulls on a light string, filling the large walk-in closet with bright light. There’s an array of clothes and shoes, but no cat. Carolyn turns to Andrea.
  EXPRESSION: null
- CHARACTER: Carolyn
  LINE: You sure?
  EXPRESSION: Doubtful
- CHARACTER: Andrea
  LINE: Yeah, I swear.
  EXPRESSION: Insistent
- CHARACTER: Carolyn
  LINE: It’s not here now. It probably just slipped out and we didn’t see it.
  EXPRESSION: Reassuring
- CHARACTER: Narrator
  LINE: Andrea bends down, looking under Cindy’s bed again, it’s not there.
  EXPRESSION: Disappointed
- CHARACTER: Carolyn
  LINE: C’mon, let’s get you back into bed. I’ll look for it.
  EXPRESSION: Gentle

::SCENE::
LOCATION: Andrea's Room
MOOD: Tender
CHARACTERS: Narrator, Andrea, Carolyn
BACKGROUND_IMAGE: null
BACKGROUND_EDIT: "Nighttime, cozy girl's room, dimly lit"

::SCRIPT::
- CHARACTER: Narrator
  LINE: As Andrea climbs back into bed.
  EXPRESSION: null
- CHARACTER: Andrea
  LINE: When’s daddy going to be back?
  EXPRESSION: Curious
- CHARACTER: Carolyn
  LINE: He said he’s going to try to make it home tonight.
  EXPRESSION: Neutral
- CHARACTER: Narrator
  LINE: Carolyn begins to tuck her in.
  EXPRESSION: null
- CHARACTER: Andrea
  LINE: How come he’s gone so much?
  EXPRESSION: Curious
- CHARACTER: Carolyn
  LINE: He lost his job, sweetie, so he’s driving for anyone he can right now -- we gotta pay the bills.
  EXPRESSION: Somber
- CHARACTER: Andrea
  LINE: Well, bills suck.
  EXPRESSION: Annoyed
- CHARACTER: Narrator
  LINE: Carolyn smiles.
  EXPRESSION: null
- CHARACTER: Carolyn
  LINE: They sure do.
  EXPRESSION: Amused
- CHARACTER: Andrea
  LINE: Will you lie down with me?
  EXPRESSION: Pleading
- CHARACTER: Carolyn
  LINE: -- Sure.
  EXPRESSION: Affectionate

::SCENE::
LOCATION: Andrea's Room (Later)
MOOD: Tense
CHARACTERS: Narrator, Carolyn
BACKGROUND_IMAGE: null
BACKGROUND_EDIT: "Nighttime, dark bedroom"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Carolyn, who’s fallen asleep next to Andrea, awakens to a distant SCRATCHING NOISE. She listens for few beats, there it is again. She climbs out of bed to investigate.
  EXPRESSION: Startled

::SCENE::
LOCATION: House - Upstairs Hallway
MOOD: Rising Tension
CHARACTERS: Narrator, Carolyn
BACKGROUND_IMAGE: null
BACKGROUND_EDIT: "Nighttime, dark hallway, family pictures on walls"

::SCRIPT::
- CHARACTER: Narrator
  LINE: She comes out of the bedroom. The SCRATCHING NOISE is coming from downstairs. She walks by several pictures of Cindy, Andrea and the family together hanging on the walls as she heads toward the staircase.
  EXPRESSION: Curious
- CHARACTER: Narrator
  LINE: Suddenly the noise turns violent, DEEP, VICIOUS SCRATCHES like nails across wood. She slows her pace dramatically.
  EXPRESSION: Afraid
- CHARACTER: Narrator
  LINE: Carolyn moves to the top of the staircase, almost too afraid to look down. Digs up some courage.
  EXPRESSION: Terrified
- CHARACTER: Narrator
  LINE: Her pov - THE CELLAR DOOR rattles upon impact as something continues to dig and claw at the door from the other side.
  EXPRESSION: Terrified

::SCENE::
LOCATION: House - Stairs
MOOD: Dread
CHARACTERS: Narrator, Carolyn
BACKGROUND_IMAGE: null
BACKGROUND_EDIT: "Nighttime, dark staircase"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Carolyn heads down as the scratching continues.
  EXPRESSION: Afraid

::SCENE::
LOCATION: House - Downstairs Hallway
MOOD: Intense Fear
CHARACTERS: Narrator, Carolyn, Cindy (O.C.), Andrea (O.C.)
BACKGROUND_IMAGE: null
BACKGROUND_EDIT: "Nighttime, dark hallway, cellar door"

::SCRIPT::
- CHARACTER: Narrator
  LINE: She comes off the bottom step and guardedly moves down the hallway to the door.
  EXPRESSION: Cautious
- CHARACTER: Narrator
  LINE: Just as she gets to it, THE SCRATCHING INSTANTLY STOPS. The house gets church quiet. She listens intently, torn with what to do.
  EXPRESSION: Suspenseful
- CHARACTER: Narrator
  LINE: Carolyn retreats momentarily back into the kitchen, comes out a second later with a flashlight.
  EXPRESSION: Determined
- CHARACTER: Narrator
  LINE: She slowly gets onto her hands and knees. Targets a one inch gap between the bottom of the door and floor with the flashlight, then thumbs the switch.
  EXPRESSION: Cautious
- CHARACTER: Narrator
  LINE: THE LIGHT INSTANTLY REFLECTS OFF TWO EYES BORING RIGHT BACK AT HER from within the dark recess but there’s nothing human, nor animal about them.
  EXPRESSION: Terrified
- CHARACTER: Narrator
  LINE: Carolyn freaks, recoils in a frenzy of motion. She scrambles back to the kitchen door where she grabs a RUBBER DOOR-WEDGE from the floor next to it. She ushers it back to the cellar door and SLAMS it into the gap.
  EXPRESSION: Panicked
- CHARACTER: Cindy
  LINE: What’s going on?
  EXPRESSION: Concerned
- CHARACTER: Narrator
  LINE: Carolyn spins. Sees Cindy and Andrea staring down at her from the top of the stairs.
  EXPRESSION: null
- CHARACTER: Carolyn
  LINE: Stay up there!
  EXPRESSION: Urgent

::SCENE::
LOCATION: Big Rig Cab
MOOD: Anxious
CHARACTERS: Narrator, Roger, Carolyn (O.C.)
BACKGROUND_IMAGE: null
BACKGROUND_EDIT: "Late night, big rig interior, headlights illuminating driveway"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Roger heads down his driveway. His headlights capture Carolyn looking out the living room window at him, she looks terrorized, anxious.
  EXPRESSION: null

::SCENE::
LOCATION: Living Room
MOOD: Prepared for Danger
CHARACTERS: Narrator, Roger
BACKGROUND_IMAGE: null
BACKGROUND_EDIT: "Nighttime, living room, open gun case"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Roger stands in front of the open gun case; exposing a shotgun and a couple of rifles. He’s quickly loading ammo into a hand gun.
  EXPRESSION: Determined

::SCENE::
LOCATION: House - Downstairs Hallway
MOOD: Confrontational
CHARACTERS: Narrator, Roger, Carolyn, Girls
BACKGROUND_IMAGE: null
BACKGROUND_EDIT: "Nighttime, downstairs hallway, cellar door barricaded"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Roger comes out of the living room, gun in hand. Carolyn and the girls watch him from the top of the stairs as he heads for the cellar door, which now has a chair propped up under the handle as well as the door-wedge.
  EXPRESSION: Determined
- CHARACTER: Carolyn
  LINE: Careful.
  EXPRESSION: Worried
- CHARACTER: Narrator
  LINE: Roger removes the chair and wedge. Gun ready. He slowly opens the door. Carolyn gasps at DEEP SCRATCHES that crisscross the back of it.
  EXPRESSION: Scared
- CHARACTER: Narrator
  LINE: Roger stands still for a moment, looking at them as well, then heads down a steep set of wooden stairs that get lost in the darkness.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: He flips a nearby wall switch, washing the cellar in a dull, yellow light.
  EXPRESSION: null

::SCENE::
LOCATION: Cellar
MOOD: Investigation
CHARACTERS: Narrator, Roger
BACKGROUND_IMAGE: null
BACKGROUND_EDIT: "Nighttime, dull yellow light, shelves of goods, moving boxes"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Roger inches down the stairs. Alert. Ready. He steps off the bottom step, pauses, gun out, eyes perusing the shelves of canned goods and stacked moving boxes.
  EXPRESSION: Cautious
- CHARACTER: Narrator
  LINE: There are no windows or other exits.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: He moves toward two wardrobe boxes, big enough for something to hide behind. Closer. Closer. The knuckle on his trigger finger whi
  EXPRESSION: Tense

::SCENE::
LOCATION: Downstairs Hallway
MOOD: Tense
CHARACTERS: Roger, Carolyn, Andrea, Cindy
BACKGROUND_IMAGE: downstairs_hallway.png
BACKGROUND_EDIT: "Right after, dim lighting, base of stairs"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Roger comes up off the stairs. Closes the door behind him. Looks up to Carolyn and the girls who are waiting with baited breath upstairs.
  EXPRESSION: null
- CHARACTER: Roger
  LINE: There’s nothing down there. The scratches were probably already on the door and your light just was playing tricks on you; maybe reflected off the railing or something.
  EXPRESSION: Dismissive
- CHARACTER: Carolyn
  LINE: I know what I saw Roger, and heard it digging at the door.
  EXPRESSION: Adamant
- CHARACTER: Roger
  LINE: Then I don’t know what to tell you -- nothing’s down there and there’s no way out.
  EXPRESSION: Frustrated
- CHARACTER: Narrator
  LINE: Andrea’s nervously chewing on her fingernails.
  EXPRESSION: Anxious
- CHARACTER: Andrea
  LINE: Maybe it was the cat.
  EXPRESSION: Nervous
- CHARACTER: Cindy
  LINE: This house gives me the creeps, we never should’ve moved here. I want to go back to New Jersey.
  EXPRESSION: Scared
- CHARACTER: Narrator
  LINE: Andrea folds into her mom’s arms.
  EXPRESSION: null
- CHARACTER: Andrea
  LINE: I’m scared, mommy
  EXPRESSION: Scared
- CHARACTER: Roger
  LINE: Just stop, both of you. There’s nothing down there. Now it’s late -- just go to bed.
  EXPRESSION: Annoyed
- CHARACTER: Narrator
  LINE: The girls walk away, leaving Carolyn standing there. Roger’s shifts his attention to her, shakes his head.
  EXPRESSION: null
- CHARACTER: Carolyn
  LINE: You think I’m making this up?
  EXPRESSION: Accusatory
- CHARACTER: Roger
  LINE: I think moving here has been a big adjustment. Maybe too big.
  EXPRESSION: Thoughtful

::PATHS::
- CHOICE: "Continue"
  TARGET: victorian_home
  STATE_CHANGE: tension = -1, doubt = +1
  CONDITION: null

::SCENE::
LOCATION: Old Two-Story Victorian Home
MOOD: Investigative
CHARACTERS: Ed, Lorraine, Rachel, David
BACKGROUND_IMAGE: victorian_home.png
BACKGROUND_EDIT: "Narrow staircase, dim lighting"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Ed and Lorraine move up a narrow staircase to a second story. Trailing behind them are RACHEL and DAVID, a slightly overweight couple in their late twenties. Neither wear stress well.
  EXPRESSION: null
- CHARACTER: Rachel
  LINE: It’s always in the middle of the night, around two-thirty.
  EXPRESSION: Stressed
- CHARACTER: Lorraine
  LINE: And they’re different sounds?
  EXPRESSION: Neutral
- CHARACTER: David
  LINE: Creaking and moaning -- like someone’s in pain.
  EXPRESSION: Worried
- CHARACTER: Rachel
  LINE: I think it’s David’s dad haunting me -- trying to get me out of this house.
  EXPRESSION: Worried
- CHARACTER: Lorraine
  LINE: Why would he do that?
  EXPRESSION: Curious
- CHARACTER: Rachel
  LINE: Because he hated me when we were dating -- he told me I wasn’t good enough for his son. He died before we got married, and he’s the one who left him this house.
  EXPRESSION: Resentful
- CHARACTER: Rachel
  LINE: He’s frickin buried fifty yards across the street. I don’t even like living here -- it gives me the heebs.
  EXPRESSION: Scared
- CHARACTER: Narrator
  LINE: Ed stops at the top.
  EXPRESSION: null
- CHARACTER: Ed
  LINE: And this is where it’s strongest?
  EXPRESSION: Inquisitive
- CHARACTER: Narrator
  LINE: Both nod. Ed looks up to see AN ATTIC DOOR DIRECTLY ABOVE THEM. He pulls on a rope, opening it up -- unfurling a set of attic steps.
  EXPRESSION: null
- CHARACTER: Rachel
  LINE: We don’t have to go up there with you, do we?
  EXPRESSION: Anxious
- CHARACTER: Lorraine
  LINE: No -- you can wait here.
  EXPRESSION: Reassuring
- CHARACTER: Narrator
  LINE: Ed reaches into his hip pocket and retrieves a flashlight. Heads up into the dark abyss.
  EXPRESSION: null

::PATHS::
- CHOICE: "Go to the attic"
  TARGET: victorian_attic_1
  STATE_CHANGE: fear = +1, investigation_progress = +1
  CONDITION: null

::SCENE::
LOCATION: Victorian House - Attic
MOOD: Eerie
CHARACTERS: Ed, Lorraine
BACKGROUND_IMAGE: victorian_attic.png
BACKGROUND_EDIT: "Continuous, dark, dusty, old furniture"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Ed stands half in and out as he sweeps the interior with his light. The place is full of old furniture, wooden trunks, boxes, clothing racks. He continues up the creaky steps into the attic. Lorraine follows him up.
  EXPRESSION: null
- CHARACTER: Lorraine
  LINE: Funny how all attics smell the same --
  EXPRESSION: Observant
- CHARACTER: Narrator
  LINE: Lorraine moves over to a broken dormer window where filtered moonlight pours in. It casts a blue hue across the room. She looks out, unfolding across a street is a large cemetery full of tombstones, hundreds and hundreds of them. A thick, wet fog drifts through.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Ed’s light falls on a cobwebbed covered bookshelf loaded with dust. He moves to it to get a look at several URN-LIKE containers that have caught his attention. Lorraine joins him.
  EXPRESSION: null
- CHARACTER: Lorraine
  LINE: Forgotten relatives, maybe?
  EXPRESSION: Curious
- CHARACTER: Narrator
  LINE: Ed uses his finger to wipe clean an inscription written on the bottom of one.
  EXPRESSION: null
- CHARACTER: Ed
  LINE: No -- First Place Curling.
  EXPRESSION: Surprised
- CHARACTER: Ed
  LINE: You’re not getting anything, are you?
  EXPRESSION: Inquisitive
- CHARACTER: Lorraine
  LINE: Not a thing.
  EXPRESSION: Pensive

::PATHS::
- CHOICE: "Continue investigation"
  TARGET: attic_right_after
  STATE_CHANGE: investigation_progress = +1
  CONDITION: null

::SCENE::
LOCATION: Attic
MOOD: Revealing
CHARACTERS: Ed, Lorraine, David, Rachel
BACKGROUND_IMAGE: victorian_attic.png
BACKGROUND_EDIT: "Right after, attic, dim light, with David and Rachel"

::SCRIPT::
- CHARACTER: Narrator
  LINE: David and Rachel come up the stairs with Ed. Both look nervous to be up there. Lorraine’s standing over by the broken window.
  EXPRESSION: null
- CHARACTER: Ed
  LINE: I know a lot of people would be creeped out living by a cemetery and -- throw a very old home into the equation, and you’re going to get the creaking, moaning sounds -- especially at night when temperature and humidity changes are the greatest and can cause some shifting in the structure.
  EXPRESSION: Explaining
- CHARACTER: David
  LINE: It’s not that. We would know the difference.
  EXPRESSION: Skeptical
- CHARACTER: Narrator
  LINE: Just then, a MOANING NOISE that sounds LIKE SOMEONE’S IN AGONY, emanates through the room. Rachel grabs onto David’s arm.
  EXPRESSION: Afraid
- CHARACTER: Rachel
  LINE: Ohmygod, that’s it --
  EXPRESSION: Terrified
- CHARACTER: Ed
  LINE: Do it again, Lorraine --
  EXPRESSION: Instructing
- CHARACTER: Narrator
  LINE: David and Rachel look to Lorraine, huh? They watch as she steps on TWO, water-stained WOODEN FLOORBOARDS that run near an old heating radiator next to her, producing the same sound.
  EXPRESSION: null
- CHARACTER: Ed
  LINE: Right now, it’s Lorraine’s weight, but add the moisture coming in through this broken window at night -- the boards are going to expand and rub against each other.
  EXPRESSION: Explaining
- CHARACTER: Ed
  LINE: You’ve heard it in different parts of the house because of the radiator.
  EXPRESSION: Explaining
- CHARACTER: Rachel
  LINE: So this place isn’t haunted?
  EXPRESSION: Hopeful
- CHARACTER: Lorraine
  LINE: No.
  EXPRESSION: Calm
- CHARACTER: Ed
  LINE: You’re not alone, a lot of what we investigate turns out like this.
  EXPRESSION: Reassuring

::PATHS::
- CHOICE: "Resolve the case"
  TARGET: warren_house_ext
  STATE_CHANGE: fear = -2, investigation_solved = true
  CONDITION: null

::SCENE::
LOCATION: Warren House - Exterior
MOOD: Calm
CHARACTERS: Ed, Lorraine
BACKGROUND_IMAGE: warren_house_ext.png
BACKGROUND_EDIT: "Night, well-kept house, driveway"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Nice. Well kept. Ed and Lorraine pull up into the driveway. Get out of the car, and head to the front door.
  EXPRESSION: null

::PATHS::
- CHOICE: "Enter backyard"
  TARGET: warren_house_backyard
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Warren House - Backyard
MOOD: Warm
CHARACTERS: Ed, Lorraine, Judy, Mom
BACKGROUND_IMAGE: warren_house_backyard.png
BACKGROUND_EDIT: "Right after, well-lit yard, chicken coop"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Ed and Lorraine exit a door off the kitchen. Across a well lit yard is a large chicken coop with a henhouse inside, where their daughter JUDY (7), carrying a basket full of eggs, is with Ed’s MOM (60’s). They’re both exiting the coop, there’s a dozen or so chickens moving about, and one of them is at their feet.
  EXPRESSION: null
- CHARACTER: Mom
  LINE: Be careful honey, you don’t want to let Gertrude out.
  EXPRESSION: Caring
- CHARACTER: Narrator
  LINE: Just as they close the coop door, Judy spots her parents.
  EXPRESSION: null
- CHARACTER: Judy
  LINE: Daddy!!
  EXPRESSION: Excited
- CHARACTER: Ed
  LINE: Hey there pumpkin!
  EXPRESSION: Happy
- CHARACTER: Narrator
  LINE: Judy hands the egg basket to her grandmother, and races toward them.
  EXPRESSION: null
- CHARACTER: Judy
  LINE: Hi mommy!
  EXPRESSION: Happy
- CHARACTER: Narrator
  LINE: Judy runs across the yard and leaps into Ed’s arms. Gives him a big hug. Lorraine sees that she’s got something dark smeared all over her face.
  EXPRESSION: null
- CHARACTER: Lorraine
  LINE: What’cha got on your face?
  EXPRESSION: Curious
- CHARACTER: Judy
  LINE: Fudgesicles!
  EXPRESSION: Proud
- CHARACTER: Narrator
  LINE: Her little eyes go wide with great pride, as --
  EXPRESSION: null
- CHARACTER: Judy
  LINE: I ate the whole box!
  EXPRESSION: Proud
- CHARACTER: Narrator
  LINE: Ed’s mom approaches, all smiles.
  EXPRESSION: null
- CHARACTER: Mom
  LINE: Oh, not the whole box -- I did manage to have one.
  EXPRESSION: Amused
- CHARACTER: Ed
  LINE: Hi mom.
  EXPRESSION: Affectionate
- CHARACTER: Narrator
  LINE: He gives her a kiss on the cheek, then looks to Lorraine, half laughing. Passes Judy over to her, who gives her a big hug.
  EXPRESSION: null
- CHARACTER: Lorraine
  LINE: I missed you!
  EXPRESSION: Affectionate

::PATHS::
- CHOICE: "Go inside the house"
  TARGET: warren_house_kitchen
  STATE_CHANGE: family_bonding = +1
  CONDITION: null

::SCENE::
LOCATION: Warren House - Kitchen
MOOD: Domestic
CHARACTERS: Ed, Woman's Voice (V.O.)
BACKGROUND_IMAGE: warren_house_kitchen.png
BACKGROUND_EDIT: "Later, kitchen, phone on wall"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Ed reaches for a phone hanging on the kitchen wall. As he dials a number, he smiles when he sees a photo of Judy on the counter next to him. It’s framed in Fudgesicle sticks, and made to look like a church with a cross. Scribbled along the bottom is, “I love you, daddy”.
  EXPRESSION: null
- CHARACTER: Woman's Voice (V.O.)
  LINE: Father Jordan -- Ed Warren is on the phone for you.
  EXPRESSION: Neutral

::PATHS::
- CHOICE: "Talk to Father Jordon"
  TARGET: cathedral_office
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Cathedral of the Holy Cross - Office
MOOD: Professional
CHARACTERS: Father Jordon, Ed (V.O.)
BACKGROUND_IMAGE: cathedral_office.png
BACKGROUND_EDIT: "Same time, opulent office, antique furniture"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Walking into an opulent office full of antique furniture and religious icons, is FATHER JORDON (late thirties). He takes a seat in a chair, then picks up a phone on his desk.
  EXPRESSION: null
- CHARACTER: Father Jordon
  LINE: Hey Ed -- how’d it go?
  EXPRESSION: Inquisitive
- CHARACTER: Ed (V.O.)
  LINE: The house was empty --
  EXPRESSION: Calm
- CHARACTER: Father Jordon
  LINE: That’s good news. I appreciate your help.
  EXPRESSION: Relieved
- CHARACTER: Ed (V.O.)
  LINE: You bet.
  EXPRESSION: Casual
- CHARACTER: Ed (V.O.)
  LINE: Was your father any better today?
  EXPRESSION: Concerned
- CHARACTER: Father Jordon
  LINE: Yeah -- we actually got him up and walking around. I think he’s going to be fine. Thanks for asking.
  EXPRESSION: Grateful

::PATHS::
- CHOICE: "End call"
  TARGET: judy_room
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Judy’s Room
MOOD: Tender
CHARACTERS: Lorraine, Judy
BACKGROUND_IMAGE: judy_room.png
BACKGROUND_EDIT: "Night, cozy bedroom"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Lorraine and Judy, who’s now wearing pajamas, sit on the edge of the bed as Lorraine finishes braiding Judy’s hair.
  EXPRESSION: null
- CHARACTER: Judy
  LINE: Grandma really snores.
  EXPRESSION: Amused
- CHARACTER: Lorraine
  LINE: C’mon, let’s get you into bed.
  EXPRESSION: Gentle
- CHARACTER: Narrator
  LINE: Lorraine stands and lifts the covers. Judy slides in under them.
  EXPRESSION: null
- CHARACTER: Lorraine
  LINE: I missed you so much.
  EXPRESSION: Affectionate
- CHARACTER: Judy
  LINE: I missed you too.
  EXPRESSION: Affectionate
- CHARACTER: Lorraine
  LINE: Sleep tight.
  EXPRESSION: Affectionate
- CHARACTER: Narrator
  LINE: Lorraine gives Judy a tender kiss good-nig
  EXPRESSION: null

::PATHS::
- CHOICE: "End of day"
  TARGET: end
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: House - Bedroom
MOOD: Calm
CHARACTERS: Narrator
BACKGROUND_IMAGE: bedroom.png
BACKGROUND_EDIT: "Nighttime, interior, dim light, someone turning off a light"

::SCRIPT::
- CHARACTER: Narrator
  LINE: reaches over and turns off a light on a nightstand next to the bed.
  EXPRESSION: null

::PATHS::
- CHOICE: "Time passes"
  TARGET: perron_backyard_afternoon
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Perron House - Back Yard
MOOD: Melancholy
CHARACTERS: Narrator, Andrea, Cindy, Carolyn
BACKGROUND_IMAGE: perron_backyard.png
BACKGROUND_EDIT: "Afternoon, dark rain clouds, autumn leaves, bare garden, dead scarecrow"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Dark rain clouds threaten. The leaves in the trees have begun to turn color. The garden off to the side is now void of any growth -- the ground bare. The Scarecrow looks dead itself; it’s stringy hair drawn across its face by a small breeze.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Andrea, wearing a warm sweater, is kneeling before a small grave at the base of a tree. There’s a wooden cross with the name SADIE written on it. She’s pulling several weeds away.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Cindy’s helping Carolyn take down some sheets from a clothing line as they ripple in the wind.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Roger’s Rig is parked next to the barn.
  EXPRESSION: null

::PATHS::
- CHOICE: "Go inside"
  TARGET: perron_house_kitchen
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Perron House - Kitchen
MOOD: Strained
CHARACTERS: Narrator, Carolyn, Roger
BACKGROUND_IMAGE: perron_house_kitchen.png
BACKGROUND_EDIT: "Soon after, interior, Roger on phone, family entering"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Carolyn comes in with the girls. Roger’s on the phone. He looks tired. Strained. As they cross --
  EXPRESSION: null
- CHARACTER: Roger
  LINE: Glen, I’m just looking for anything, man -- I need to get something going on or I’m going to lose the insurance on the rig.
  EXPRESSION: Frustrated
- CHARACTER: Narrator
  LINE: (listens; frustrated)
  EXPRESSION: null
- CHARACTER: Roger
  LINE: That’s half my rate and twice the distance.
  EXPRESSION: Frustrated
- CHARACTER: Narrator
  LINE: (listens; giving in)
  EXPRESSION: null
- CHARACTER: Roger
  LINE: Yeah, alright, alright, I’ll take it.
  EXPRESSION: Resigned
- CHARACTER: Narrator
  LINE: Roger hangs up the phone. Looks to Carolyn, shakes his head.
  EXPRESSION: null
- CHARACTER: Carolyn
  LINE: What’s the route?
  EXPRESSION: Sympathetic
- CHARACTER: Roger
  LINE: Fucking Florida. Two week turn arounds. I start tomorrow.
  EXPRESSION: Angry
- CHARACTER: Narrator
  LINE: She’s shocked that he just cussed in front of the kids.
  EXPRESSION: Surprised

::PATHS::
- CHOICE: "Later that night"
  TARGET: house_bedroom_night
  STATE_CHANGE: roger_starts_tomorrow = true
  CONDITION: null

::SCENE::
LOCATION: House - Bedroom
MOOD: Terrifying
CHARACTERS: Narrator, Andrea, Cat
BACKGROUND_IMAGE: house_bedroom.png
BACKGROUND_EDIT: "Later that night, pouring rain, Andrea in bed, grey cat hissing"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Andrea is in bed, sound asleep. Pouring rain pelts against her window, her eyes snap open. She finds herself facing the grey cat back on her bed, its ears drawn back, HISSING through exposed fangs, ready for a fight, it’s eyes slowly tracking something moving just behind her.
  EXPRESSION: Afraid
- CHARACTER: Narrator
  LINE: Andrea’s peripheral vision suddenly picks up the OUTLINES OF TWO HANDS with only THREE FINGERS ON EACH pressing out from within her pillow case, folding her pillow up on the sides, closing in on her face.
  EXPRESSION: Shocked
- CHARACTER: Narrator
  LINE: The cat HISSES, then leaps to the floor.
  EXPRESSION: Afraid

::PATHS::
- CHOICE: "Scream"
  TARGET: perron_home_master_bedroom
  STATE_CHANGE: andrea_scared = true
  CONDITION: null

::SCENE::
LOCATION: Perron Home - Master Bedroom
MOOD: Urgent
CHARACTERS: Narrator, Carolyn, Roger
BACKGROUND_IMAGE: perron_home_master_bedroom.png
BACKGROUND_EDIT: "Same night, parents startled awake, scrambling out of bed"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Carolyn and Roger are rattled from a dead sleep by Andrea’s blood curdling scream both scramble out of the covers to get to her.
  EXPRESSION: Surprised

::PATHS::
- CHOICE: "Rush to Andrea's room"
  TARGET: andreas_room_right_after
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Andrea’s Room
MOOD: Fear
CHARACTERS: Narrator, Roger, Carolyn, Andrea
BACKGROUND_IMAGE: andreas_room.png
BACKGROUND_EDIT: "Right after, darkness, Roger in doorway, Andrea curled in corner"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Roger’s to the doorway first. Looks in to see the bed’s empty. Eyes shift looking for his girl, but areas of the room are swallowed in darkness.
  EXPRESSION: Concerned
- CHARACTER: Roger
  LINE: Andrea--?
  EXPRESSION: Concerned
- CHARACTER: Narrator
  LINE: Carolyn joins him. Roger hits the switch on the wall, shedding light on Andrea, who’s curled up in a corner, hyperventilating with fear. The tears are flowing as she stares at her bed.
  EXPRESSION: null

::PATHS::
- CHOICE: "Move to hallway"
  TARGET: hallway_later
  STATE_CHANGE: andrea_traumatized = true
  CONDITION: null

::SCENE::
LOCATION: Hallway
MOOD: Tense
CHARACTERS: Narrator, Roger, Carolyn, Andrea
BACKGROUND_IMAGE: hallway.png
BACKGROUND_EDIT: "Later, outside bedroom, Roger and Carolyn arguing quietly"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Roger is pissed as he faces Carolyn just outside their bedroom, where Andrea can be seen tucked into their bed, now sleeping.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Carolyn’s an emotional wreck. Wipes tears with a tissue. Both speak in hushed tones.
  EXPRESSION: null
- CHARACTER: Roger
  LINE: Demons peering in through windows, cold spots, doors rattling, voices -- everyone was fine until you started putting all this scared, city-girl bullshit in their heads.
  EXPRESSION: Angry
- CHARACTER: Carolyn
  LINE: No I haven’t -- there’s something wrong with this place.
  EXPRESSION: Defensive
- CHARACTER: Roger
  LINE: Then how come I haven’t seen it?
  EXPRESSION: Skeptical
- CHARACTER: Carolyn
  LINE: I don’t know.
  EXPRESSION: Pleading
- CHARACTER: Carolyn
  LINE: I’m scared to death, Roger. We need to get someone out here, a priest or someone.
  EXPRESSION: Afraid
- CHARACTER: Roger
  LINE: To do what?
  EXPRESSION: Skeptical
- CHARACTER: Carolyn
  LINE: I have no idea. Bless it -- whatever they do.
  EXPRESSION: Uncertain
- CHARACTER: Roger
  LINE: Yeah -- that’s just what the girls need to see next -- someone walking around here with a cross damning everything out of this house.
  EXPRESSION: Sarcastic
- CHARACTER: Narrator
  LINE: (beat)
  EXPRESSION: null
- CHARACTER: Roger
  LINE: I can’t listen to anymore of this shit.
  EXPRESSION: Angry
- CHARACTER: Narrator
  LINE: He heads downstairs.
  EXPRESSION: null
- CHARACTER: Carolyn
  LINE: Roger, please.
  EXPRESSION: Pleading
- CHARACTER: Narrator
  LINE: He doesn’t turn around.
  EXPRESSION: null

::PATHS::
- CHOICE: "Roger goes downstairs"
  TARGET: house_living_room_later
  STATE_CHANGE: roger_frustrated = +1, carolyn_desperate = +1
  CONDITION: null

::SCENE::
LOCATION: House - Living Room
MOOD: Eerie
CHARACTERS: Narrator, Roger
BACKGROUND_IMAGE: house_living_room.png
BACKGROUND_EDIT: "Later, night, Roger asleep on sofa, fireplace embers, fuzzy TV"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Roger’s asleep on one of two sofas that face each other in front of the fireplace, that’s glowing red from embers. There’s a coffee table between the sofas with a half empty bottle of scotch. A nearby TV is fuzzy white, that is, until something dark, ominous, crosses in front of it.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Roger awakens. Sits up. Rubs his groggy eyes, then rises. Goes to the TV. Just as he turns off the TV, he hears the LOW CREAKING SOUND OF A DOOR opening. He heads to the hallway to investigate. As he passes a Grandfather clock, the time reads: 5:15.
  EXPRESSION: Surprised

::PATHS::
- CHOICE: "Investigate the sound"
  TARGET: downstairs_hallway_continuous
  STATE_CHANGE: roger_alert = true
  CONDITION: null

::SCENE::
LOCATION: Downstairs Hallway
MOOD: Puzzling
CHARACTERS: Narrator, Roger
BACKGROUND_IMAGE: downstairs_hallway.png
BACKGROUND_EDIT: "Continuous, kitchen door closing, Roger investigating"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Just as Roger comes into the hallway, HE SEES the kitchen door closing shut. As he moves toward it, it starts to BANG against the door jam in bursts of three. Bangbangbang. Bangbangbang. Roger’s mind is racing, what the hell?
  EXPRESSION: Surprised
- CHARACTER: Narrator
  LINE: The banging stops the minute he gets to the door. The house falls into an awful silence. He opens the kitchen door, looks inside.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: A night-light cascading from a socket next to the sink, kicks out enough glow to see that no one’s in there. A soft breeze coming in through the kitchen window caresses the curtains. His mind settles, that must’ve been it.
  EXPRESSION: Relieved

::PATHS::
- CHOICE: "Roger leaves for work"
  TARGET: barn_day
  STATE_CHANGE: roger_dismissive = true
  CONDITION: null

::SCENE::
LOCATION: Barn
MOOD: Somber
CHARACTERS: Narrator, Roger, Carolyn
BACKGROUND_IMAGE: barn.png
BACKGROUND_EDIT: "Daytime, Roger pulling out in big rig, Carolyn watching"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Roger is pulling out in his big rig. Carolyn is standing outside the house, wrapped in a sweater. She looks soul weary as she watches him drive off.
  EXPRESSION: null

::PATHS::
- CHOICE: "Return inside"
  TARGET: cindys_room_night
  STATE_CHANGE: roger_absent = true, carolyn_weary = true
  CONDITION: null

::SCENE::
LOCATION: Cindy’s Room
MOOD: Suspenseful
CHARACTERS: Narrator, Cindy, Carolyn
BACKGROUND_IMAGE: cindys_room.png
BACKGROUND_EDIT: "Nighttime, Cindy doing homework, door opening, strange banging"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Cindy’s listening to some music as she sits on her bed, doing homework. Her bedroom door opens and her mom pokes her head in.
  EXPRESSION: null
- CHARACTER: Carolyn
  LINE: How’s the homework going?
  EXPRESSION: Calm
- CHARACTER: Cindy
  LINE: It’s going.
  EXPRESSION: Casual
- CHARACTER: Carolyn
  LINE: Andrea and I are going to bed.
  EXPRESSION: Calm
- CHARACTER: Cindy
  LINE: I’ll be in, in a little bit.
  EXPRESSION: Casual
- CHARACTER: Narrator
  LINE: LATER.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Just as Cindy finishes her homework, her bedroom door begins to make a soft, repetitive bangbangbang noise, like something’s pushing against it from the other side.
  EXPRESSION: null
- CHARACTER: Cindy
  LINE: Mom--?
  EXPRESSION: Afraid
- CHARACTER: Narrator
  LINE: No response.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Keeping her eyes on the door, Cindy slides out of bed. Moves toward it as the bangbangbang continues, the soft impact barely rattling the door. She hits the brakes when she sees a shadow of something appear in the gap between the base of the door and the floor.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Cindy digs deep for courage, then continues toward it. She’s a foot away and the banging suddenly stops. She waits in silence, listening, that’s when the door slowly opens on its own.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Cindy takes a cautionary step backwards, but nothing’s there. She takes reluctant steps up to the door jamb and cranes her head both directions in the hallway for a look. All clear. She sees that her mom’s door is open a couple of inches.
  EXPRESSION: null

::PATHS::
- CHOICE: "Step into the hallway"
  TARGET: hallway_continuous_apparition
  STATE_CHANGE: cindy_fear = +1
  CONDITION: null

::SCENE::
LOCATION: Hallway
MOOD: Terrifying
CHARACTERS: Narrator, Cindy, Apparition, Carolyn, Andrea
BACKGROUND_IMAGE: hallway.png
BACKGROUND_EDIT: "Continuous, foul smell, apparition appearing, terrifying moment"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Two steps into the hallway, Cindy pauses momentarily, reacting to some sort of foul smell. She then moves forward, and as she’s about to step into her mom’s room, she stops mid-stride, her face goes taut, standing next to the bed is AN APPARITION of a woman; dark matted hair, white white skin, her body awkwardly hunched forward over Carolyn and Andrea, who are sleeping, completely unaware of her presence.
  EXPRESSION: Shocked
- CHARACTER: Narrator
  LINE: The Apparition slowly cranes her head toward Cindy. Stares at her with pupil-less, snow-white eyes. She suddenly surges toward Cindy lightning fast, passing right through her body, and vanishes.
  EXPRESSION: Terrified
- CHARACTER: Narrator
  LINE: Off Cindy’s scream.
  EXPRESSION: null

::PATHS::
- CHOICE: "Seek help"
  TARGET: catholic_church_lawn_harrisville
  STATE_CHANGE: carolyn_seeks_priest = true
  CONDITION: null

::SCENE::
LOCATION: Catholic Church - Front Lawn - Harrisville
MOOD: Hopeful
CHARACTERS: Narrator, Father Thornton, Carolyn
BACKGROUND_IMAGE: catholic_church.png
BACKGROUND_EDIT: "Daytime, simple white church, Father Thornton by marquee"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Simple white structure with a steeple. FATHER THORNTON; late 20’s, is getting ready to take down letters from a small, glass encased marquee posted into the ground that says: A CHURCH IS A GIFT FROM GOD. ASSEMBLY REQUIRED.
  EXPRESSION: null
- CHARACTER: Carolyn
  LINE: Excuse me, Father Thorton?
  EXPRESSION: Desperate
- CHARACTER: Narrator
  LINE: He looks over to see Carolyn approaching.
  EXPRESSION: null

::PATHS::
- CHOICE: "Talk with Father Thornton"
  TARGET: church_grounds_right_after
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Church Grounds
MOOD: Serious
CHARACTERS: Narrator, Father Thornton, Carolyn
BACKGROUND_IMAGE: church_grounds.png
BACKGROUND_EDIT: "Right after, under a large willow tree, shared table"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Father Thorton and Carolyn share a table under the shade of a large willow.
  EXPRESSION: null
- CHARACTER: Father Thornton
  LINE: 
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue story"
  TARGET: end_of_excerpt
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Unspecified (phone call, continuation from prior scene)
MOOD: Serious, transitional
CHARACTERS: Priest, Carolyn
BACKGROUND_IMAGE: null
BACKGROUND_EDIT: null

::SCRIPT::
- CHARACTER: Priest
  LINE: It sounds to me that it’s far beyond just needing a blessing. Let me make a call to the Diocese and see if we can get someone out here to help that’s a little more qualified in these matters.
  EXPRESSION: Concerned
- CHARACTER: Narrator
  LINE: Carolyn breathes a slight sigh of relief --
  EXPRESSION: Relieved
- CHARACTER: Carolyn
  LINE: Thank you --
  EXPRESSION: Relieved

::PATHS::
- CHOICE: "Receive a call from Father Jordan"
  TARGET: warren_house_backyard
  STATE_CHANGE: time_passed = "one week", fear = +1
  CONDITION: null

::SCENE::
LOCATION: Warren House - Backyard
MOOD: Domestic, tense
CHARACTERS: Lorraine, Ed, Judy, Narrator, Woman's Voice (V.O.)
BACKGROUND_IMAGE: warren_house_backyard.png
BACKGROUND_EDIT: "Daytime, Judy feeding chickens in the background"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Super - One week later. S.O. Of a PHONE RINGING.
  EXPRESSION: null
- CHARACTER: Ed (V.O.)
  LINE: -- Hello?
  EXPRESSION: Neutral
- CHARACTER: Woman's Voice (V.O.)
  LINE: Mr. Warren, I have Father Jordan calling.
  EXPRESSION: Neutral
- CHARACTER: Narrator
  LINE: Lorraine is seated at an outdoor table and has a cup of coffee in hand. Ed sits opposite her. Judy is in the background, feeding the chickens in the coup.
  EXPRESSION: null
- CHARACTER: Lorraine
  LINE: I just wish you had talked to me.
  EXPRESSION: Disappointed
- CHARACTER: Ed
  LINE: I’m sorry, I didn’t think it was that big of a deal. Sounds like this family really needs some help.
  EXPRESSION: Apologetic
- CHARACTER: Narrator
  LINE: Lorraine lets her eyes drift to Judy --
  EXPRESSION: Concerned
- CHARACTER: Lorraine
  LINE: We were in Maine last week, New York the week before --
  EXPRESSION: Tired
- CHARACTER: Narrator
  LINE: Ed looks at her, he knows her too well.
  EXPRESSION: Understanding
- CHARACTER: Ed
  LINE: C’mon, what’s going on?
  EXPRESSION: Concerned
- CHARACTER: Narrator
  LINE: Lorraine pauses, then --
  EXPRESSION: null
- CHARACTER: Lorraine
  LINE: I’m just not sure how much longer I want to do this. There’s always going to be another case, Ed. Judy’s growing up so fast -- we’re on the road all the time... it was different when she was younger.
  EXPRESSION: Tired
- CHARACTER: Narrator
  LINE: They sit still for a few silent beats, then --
  EXPRESSION: null
- CHARACTER: Ed
  LINE: Tell you what, let’s check this one out, then take a break -- see how you feel after that -- okay?
  EXPRESSION: Reassuring
- CHARACTER: Lorraine
  LINE: -- Sure.
  EXPRESSION: Resigned
- CHARACTER: Narrator
  LINE: Ed rises.
  EXPRESSION: null

::PATHS::
- CHOICE: "Head to the Perron's house"
  TARGET: warren_plymouth
  STATE_CHANGE: ed_resolved = true, lorraine_reluctant = true
  CONDITION: null

::SCENE::
LOCATION: Warren's Plymouth - Rural Countryside
MOOD: Eerie, foreboding
CHARACTERS: Ed, Lorraine, Narrator
BACKGROUND_IMAGE: rural_road_night.png
BACKGROUND_EDIT: "Nighttime, lonely two-lane road, dense trees"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Ed and Lorraine ride in silence along a lonely two-lane stretch of road through rural countryside. The framed picture of Judy now dangles from the rearview mirror. Their headlights hit a small road sign riddled with buckshot that’s posted at a turnoff just ahead: COLLINS TAFT RD.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Ed turns. Heads down a gravel strip of road that winds its way through the trees to a mailbox. They turn in the driveway. Although it’s dark and cloudy, scattered moonlight casts an eerie glow over the farmhouse, we see it’s the Perron’s. Lights on inside splinter out through several windows. The Perron’s station wagon is out front.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Ed pulls up and parks. As they get out of the car, he goes to the trunk. Pops it open. Lorraine suddenly stops cold, her smile vanishes. She stands still, slowly scans over the property; past the house, the woods, the barn, something’s definitely got her attention.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Ed retrieves a handheld tape recorder and note pad out of a box in the trunk and closes it. Goes up to Lorraine. She shows him her arms, has GOOSEBUMPS all over them.
  EXPRESSION: Concerned
- CHARACTER: Ed
  LINE: I guess we’re in the right place.
  EXPRESSION: Serious
- CHARACTER: Narrator
  LINE: The two of them head up the walkway. Just as they round a slight turn.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Lorraine’s pov - WHOOSH! A BLACK LAB leaps right at her, it’s TEETH barred as it snarls viciously. Jaws snap. It strains against a chain, which is tethered to a metal post driven into the grass, then --
  EXPRESSION: Scared
- CHARACTER: Narrator
  LINE: Resume -
  EXPRESSION: null
- CHARACTER: Ed
  LINE: You’re getting something --
  EXPRESSION: Observant
- CHARACTER: Lorraine
  LINE: Um-hum.
  EXPRESSION: Unsettled

::PATHS::
- CHOICE: "Approach the front door"
  TARGET: perron_house_front_door
  STATE_CHANGE: lorraine_abilities_active = true, fear = +1
  CONDITION: null

::SCENE::
LOCATION: Perron's House - Front Door
MOOD: Tense, formal introduction
CHARACTERS: Ed, Lorraine, Carolyn, Cindy, Andrea, Narrator
BACKGROUND_IMAGE: perron_house_front_door.png
BACKGROUND_EDIT: "Nighttime, dimly lit farmhouse entrance"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Ed and Lorraine stand at the front door. It opens, revealing Carolyn standing before them.
  EXPRESSION: null
- CHARACTER: Lorraine
  LINE: Carolyn?
  EXPRESSION: Questioning
- CHARACTER: Carolyn
  LINE: -- You found it okay?
  EXPRESSION: Concerned
- CHARACTER: Ed
  LINE: Yeah, no problem.
  EXPRESSION: Casual
- CHARACTER: Narrator
  LINE: The girls join her at the door -- their expressions somber. Soul weary.
  EXPRESSION: Somber
- CHARACTER: Carolyn
  LINE: These are my daughters, Cindy and Andrea.
  EXPRESSION: Neutral
- CHARACTER: Cindy/Andrea
  LINE: -- Hi.
  EXPRESSION: Neutral
- CHARACTER: Carolyn
  LINE: Come in.
  EXPRESSION: Inviting

::PATHS::
- CHOICE: "Enter the house"
  TARGET: perron_house_foyer
  STATE_CHANGE: investigation_started = true
  CONDITION: null

::SCENE::
LOCATION: Perron House - Foyer
MOOD: Investigative, unsettling
CHARACTERS: Ed, Lorraine, Carolyn, Cindy, Narrator
BACKGROUND_IMAGE: perron_house_foyer.png
BACKGROUND_EDIT: "Soon after, interior, old house, dimly lit foyer"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Lorraine and Ed stand with Carolyn and the girls. We catch them mid-conversation:
  EXPRESSION: null
- CHARACTER: Carolyn
  LINE: -- In the last few nights it’s gotten even worse.
  EXPRESSION: Anxious
- CHARACTER: Ed
  LINE: -- And these apparitions, do any of them have a smell?
  EXPRESSION: Investigative
- CHARACTER: Cindy
  LINE: The one I saw. It was horrible, like rotting meat.
  EXPRESSION: Disgusted
- CHARACTER: Narrator
  LINE: Ed glances to Lorraine.
  EXPRESSION: Concerned
- CHARACTER: Carolyn
  LINE: What? What is it? Please.
  EXPRESSION: Anxious
- CHARACTER: Ed
  LINE: It usually indicates some kind of demonic activity.
  EXPRESSION: Serious
- CHARACTER: Narrator
  LINE: An elevated wave of fear washes over Carolyn and the girls.
  EXPRESSION: Afraid
- CHARACTER: Carolyn
  LINE: -- Ohmygod.
  EXPRESSION: Terrified
- CHARACTER: Narrator
  LINE: Ed’s eyes drift to a couple of door handles that line the hallway where pieces of rope are dangling off them.
  EXPRESSION: Observant
- CHARACTER: Carolyn
  LINE: It keeps them from banging at night.
  EXPRESSION: Tired
- CHARACTER: Ed
  LINE: Comes in threes -- bang bang bang?
  EXPRESSION: Knowing
- CHARACTER: Narrator
  LINE: She nods.
  EXPRESSION: null
- CHARACTER: Ed
  LINE: It’s an insult to the trinity; father, son & Holy Spirit -- and I bet it stops at dawn.
  EXPRESSION: Explanatory
- CHARACTER: Narrator
  LINE: Another nod.
  EXPRESSION: null
- CHARACTER: Ed
  LINE: God’s light.
  EXPRESSION: Serious
- CHARACTER: Lorraine
  LINE: Do you have a dog?
  EXPRESSION: Questioning
- CHARACTER: Carolyn
  LINE: Used to.
  EXPRESSION: Sad
- CHARACTER: Lorraine
  LINE: A black lab?
  EXPRESSION: Questioning
- CHARACTER: Carolyn
  LINE: Yes. Sadie.
  EXPRESSION: Neutral
- CHARACTER: Lorraine
  LINE: What happened to her?
  EXPRESSION: Questioning
- CHARACTER: Carolyn
  LINE: The first night we moved in she wouldn’t come in the house -- so Roger had to tether her out front. Andrea found her dead in the morning -- she had choked herself to death on the chain.
  EXPRESSION: Disturbed
- CHARACTER: Narrator
  LINE: Lorraine notices the cellar door that’s been blocked closed with the chair and door-wedge. She starts toward it. Carolyn stays behind.
  EXPRESSION: Observant
- CHARACTER: Carolyn
  LINE: We don’t go down there anymore.
  EXPRESSION: Afraid
- CHARACTER: Ed
  LINE: Why?
  EXPRESSION: Questioning
- CHARACTER: Carolyn
  LINE: Because there’s something in there that keeps scratching from the other side.
  EXPRESSION: Afraid
- CHARACTER: Narrator
  LINE: Lorraine gets to the door and pulls the chair and wedge free, opens the door, revealing. Tons more of the DEEP, VIOLENT SCRATCHES. Lorraine hits the switch on the wall, lighting up the basement.
  EXPRESSION: Determined

::PATHS::
- CHOICE: "Go into the cellar"
  TARGET: cellar
  STATE_CHANGE: cellar_door_open = true, fear = +2
  CONDITION: null

::SCENE::
LOCATION: Cellar
MOOD: Horrific, disturbing, dark
CHARACTERS: Lorraine, Ed, Narrator
BACKGROUND_IMAGE: cellar.png
BACKGROUND_EDIT: "Continuously, dark, newly lit, violent scratches on walls"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Lorraine heads down the stairs. As she steps off the bottom step, she’s hit with a BOMBARDMENT OF FAST, HARD HITTING IMAGES OF FIVE DEAD, SKINLESS RABBITS sprawled out across the bottom of a large cage; entrails dangling through the meshing. The leg on one of them twitches.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: -- The CEMENT FLOOR flowing with BLOOD.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: -- A large, BLOOD-RED PENTAGRAM is plastered like graffiti on a wall.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: -- A CLOAKED FIGURE is having sex with a naked, dead woman, her eyes locked wide open. Other cloaked figures, faces hidden within hoods are close by, watching.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: -- A HYPODERMIC NEEDLE being pushed into a vein on an arm full of tracts.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: -- Shadowed individuals surrounding an UPSIDE DOWN CROSS.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: -- The FLASH of a GUN’S MUZZLE illuminating the face of a heavy set woman as she pulls the trigger of a pistol with its barrel pressed up under her chin.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Resume. Lorraine looks sickened. Ed comes off the stairs and joins her. She shakes her head in disgust at what’s happened in this cellar.
  EXPRESSION: Disgusted
- CHARACTER: Lorraine
  LINE: -- This is bad, Ed.
  EXPRESSION: Horrified

::PATHS::
- CHOICE: "Exit the cellar"
  TARGET: perron_house_living_room
  STATE_CHANGE: lorraine_traumatized = true, fear = +3
  CONDITION: null

::SCENE::
LOCATION: Perron House - Living Room
MOOD: Investigative, unsettling
CHARACTERS: Ed, Lorraine, Carolyn, Narrator
BACKGROUND_IMAGE: perron_house_living_room.png
BACKGROUND_EDIT: "Right after, interior, old living room, fireplace"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Ed lags behind as Lorraine follows Carolyn and the girls into the living room. She takes a moment, looking it over.
  EXPRESSION: null
- CHARACTER: Ed
  LINE: When did you move in?
  EXPRESSION: Questioning
- CHARACTER: Carolyn
  LINE: About five months ago.
  EXPRESSION: Neutral
- CHARACTER: Narrator
  LINE: Lorraine’s eyes drift over to the fireplace where she’s hit with ANOTHER IMAGE OF blood dripping off the hearth onto the set of long, narrow knitting needles swallowed in red.
  EXPRESSION: null
- CHARACTER: Lorraine
  LINE: Do any of you knit?
  EXPRESSION: Questioning
- CHARACTER: Narrator
  LINE: Carolyn shakes her head, no.
  EXPRESSION: null

::PATHS::
- CHOICE: "Move upstairs"
  TARGET: perron_house_stairs
  STATE_CHANGE: investigation_deeper = true
  CONDITION: null

::SCENE::
LOCATION: Perron House - Stairs
MOOD: Unsettling, strange occurrences
CHARACTERS: Carolyn, Andrea, Cindy, Ed, Lorraine, Narrator
BACKGROUND_IMAGE: perron_house_stairs.png
BACKGROUND_EDIT: "Right after, interior, old wooden staircase"

::SCRIPT::
- CHARACTER: Narrator
  LINE: As Carolyn, Andrea and Cindy lead Ed and Lorraine up the stairs --
  EXPRESSION: null
- CHARACTER: Andrea
  LINE: Tell’em about the birds, mom.
  EXPRESSION: Excited
- CHARACTER: Carolyn
  LINE: It’s the strangest thing, they fly into the side of the barn -- necks get broken. All kinds of ‘em.
  EXPRESSION: Perplexed
- CHARACTER: Narrator
  LINE: Cindy looks back to Lorraine and Ed.
  EXPRESSION: null
- CHARACTER: Cindy
  LINE: And things have been getting moved around a lot. The table in the kitchen was blocking the door this morning.
  EXPRESSION: Worried
- CHARACTER: Narrator
  LINE: As Carolyn steps onto the landing.
  EXPRESSION: null
- CHARACTER: Carolyn
  LINE: And the clocks -- they stop at 5:15 a.m.
  EXPRESSION: Confused
- CHARACTER: Lorraine
  LINE: All of them?
  EXPRESSION: Surprised
- CHARACTER: Carolyn
  LINE: Um-hum.
  EXPRESSION: Affirmative

::PATHS::
- CHOICE: "Continue into the upstairs hallway"
  TARGET: perron_house_upstairs_hallway
  STATE_CHANGE: new_anomalies = +1
  CONDITION: null

::SCENE::
LOCATION: Perron House - Upstairs Hallway
MOOD: Eerie, unsettling
CHARACTERS: Ed, Lorraine, Girls, Carolyn, Narrator
BACKGROUND_IMAGE: perron_house_upstairs_hallway.png
BACKGROUND_EDIT: "Continuously, old hallway, empty walls with protruding nails"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Ed and Lorraine continue to follow the girls toward the master bedroom. The walls are empty except for several protruding nails from each.
  EXPRESSION: null
- CHARACTER: Carolyn
  LINE: We used to have family pictures, but something keeps knocking them of
  EXPRESSION: Frustrated

::PATHS::
- CHOICE: "Continue exploring upstairs"
  TARGET: next_upstairs_room
  STATE_CHANGE: investigation_continues = true
  CONDITION: null

::SCENE::
LOCATION: Perron House - Hallway
MOOD: Tense
CHARACTERS: Lorraine, Carolyn, Ed
BACKGROUND_IMAGE: perron_house_hallway.png
BACKGROUND_EDIT: "Daytime, interior, slightly worn, ominous feeling"

::SCRIPT::
- CHARACTER: Lorraine
  LINE: And your husband hasn’t seen any of this?
  EXPRESSION: Concerned
- CHARACTER: Narrator
  LINE: Carolyn shakes her head.
  EXPRESSION: null
- CHARACTER: Carolyn
  LINE: Things only happen when he’s gone. He thinks it’s all in our heads.
  EXPRESSION: Tired
- CHARACTER: Ed
  LINE: He’s not being shown anything on purpose.
  EXPRESSION: Serious
- CHARACTER: Narrator
  LINE: Off her look.
  EXPRESSION: null
- CHARACTER: Ed
  LINE: It creates friction in the relationship, a negative energy for whatever’s here to feed on.
  EXPRESSION: Explaining
- CHARACTER: Carolyn
  LINE: Well, it’s working.
  EXPRESSION: Resigned
- CHARACTER: Narrator
  LINE: As they pass Andrea’s room --
  EXPRESSION: null
- CHARACTER: Carolyn
  LINE: This is where Andrea had that experience on the bed.
  EXPRESSION: Neutral
- CHARACTER: Narrator
  LINE: Lorraine pauses for a moment looking in. Notices that none of the pillows have cases on them.
  EXPRESSION: Observant

::PATHS::
- CHOICE: "Continue investigation"
  TARGET: master_bedroom
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Master Bedroom
MOOD: Investigative
CHARACTERS: Lorraine, Ed, Carolyn, Cindy
BACKGROUND_IMAGE: master_bedroom.png
BACKGROUND_EDIT: "Nighttime, antique furniture, slightly unsettling"

::SCRIPT::
- CHARACTER: Lorraine
  LINE: Where was the apparition?
  EXPRESSION: Inquisitive
- CHARACTER: Narrator
  LINE: Lorraine and Ed enter, leaving Carolyn and the girls at the doorframe.
  EXPRESSION: null
- CHARACTER: Cindy
  LINE: On the left side of the bed.
  EXPRESSION: Recollecting
- CHARACTER: Narrator
  LINE: Lorraine walks over to it. Ed moves to a dresser, looks to a framed photo of the girls, then to a framed wedding picture of Roger and Carolyn. There’s another photo of Roger kneeling on one knee, posing next to a twelve-point buck he’s shot. His rifle rests across his arms.
  EXPRESSION: null

::PATHS::
- CHOICE: "Move to kitchen"
  TARGET: kitchen
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Kitchen
MOOD: Serious
CHARACTERS: Ed, Carolyn
BACKGROUND_IMAGE: kitchen.png
BACKGROUND_EDIT: "Later, kitchen table, tape recorder"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Ed sits with Carolyn at the kitchen table with his tape recorder between them.
  EXPRESSION: null
- CHARACTER: Ed
  LINE: I just want you to start from the beginning.
  EXPRESSION: Professional
- CHARACTER: Narrator
  LINE: Carolyn nods. Ed hits the PLAY and RECORD buttons at the same time.
  EXPRESSION: null
- CHARACTER: Ed
  LINE: My name’s Ed Warren. It’s November 1st, 1972. I’m sitting here with Carolyn Perron who, with her family, has been experiencing supernatural occurrences --
  EXPRESSION: Professional
- CHARACTER: Ed
  LINE: Okay, go ahead --
  EXPRESSION: Encouraging

::PATHS::
- CHOICE: "Cut to another interview"
  TARGET: family_room
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Perron House - Family Room
MOOD: Troubled
CHARACTERS: Lorraine, Andrea, Cindy
BACKGROUND_IMAGE: family_room.png
BACKGROUND_EDIT: "Same time, sofa, fireplace, dim lighting"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Lorraine is sitting on the sofa with Andrea. She notices that she’s bitten her nails down to nothing.
  EXPRESSION: null
- CHARACTER: Lorraine
  LINE: -- Anything else?
  EXPRESSION: Concerned
- CHARACTER: Andrea
  LINE: -- Sometimes I hear a baby crying in the fireplace.
  EXPRESSION: Fearful
- CHARACTER: Narrator
  LINE: Andrea’s eyes drift over to the fireplace, which is blackened, and full of ash.
  EXPRESSION: null
- CHARACTER: Lorraine
  LINE: Do you feel like any one of these things want to hurt you?
  EXPRESSION: Serious
- CHARACTER: Andrea
  LINE: Um-hum --
  EXPRESSION: Afraid
- CHARACTER: Andrea
  LINE: -- How do you know when they’re around?
  EXPRESSION: Curious
- CHARACTER: Lorraine
  LINE: I get Goose bumps.
  EXPRESSION: Explaining
- CHARACTER: Andrea
  LINE: When I get Goose bumps, does that mean they’re near me?
  EXPRESSION: Anxious
- CHARACTER: Lorraine
  LINE: Maybe -- can you tell me what you’ve seen?
  EXPRESSION: Gentle
- CHARACTER: Narrator
  LINE: Lorraine is with Cindy, who has her arms wrapped around her knees, all hunched up on the sofa. She stares off blankly.
  EXPRESSION: null
- CHARACTER: Cindy
  LINE: -- I don’t know what it was. My mom thinks it might be what’s been scratching at the cellar door --
  EXPRESSION: Disturbed

::PATHS::
- CHOICE: "Recall Cindy's experience"
  TARGET: flashback_hallway
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Hallway (Flashback)
MOOD: Horrifying
CHARACTERS: Cindy
BACKGROUND_IMAGE: hallway.png
BACKGROUND_EDIT: "Nighttime, moonlight casting shadows, eerie"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Cindy, wrapped in a towel, walks out of the upstairs bathroom. She stops dead in her tracks, staring at the floor, where backlit by the moon, a tree lays shadows on it through a window at the far end. But it’s not the tree branches that disturbs her, it’s that SOMETHING IS SITTING on the branches with crooked arms, taloned claws, and legs sprouted grotesquely from a bulky torso.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: She forces herself to look out the window but nothing’s there.
  EXPRESSION: Terrified

::PATHS::
- CHOICE: "Return to present"
  TARGET: perron_house_hallway_later
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Perron House - Hallway
MOOD: Reflective
CHARACTERS: Lorraine, Ed
BACKGROUND_IMAGE: perron_house_hallway.png
BACKGROUND_EDIT: "Later, interior, natural light"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Lorraine walks into the kitchen, where Ed is still interviewing Carolyn. He pauses the tape, looks to her.
  EXPRESSION: null
- CHARACTER: Lorraine
  LINE: I’m going to go outside.
  EXPRESSION: Determined
- CHARACTER: Ed
  LINE: Almost done.
  EXPRESSION: Neutral

::PATHS::
- CHOICE: "Go outside"
  TARGET: perron_house_side_door
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Perron House - Side Door
MOOD: Ominous
CHARACTERS: Lorraine
BACKGROUND_IMAGE: perron_house_side_door.png
BACKGROUND_EDIT: "Right after, exterior, dark, old house"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Lorraine exits the house.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: She pauses on the landing for a moment, looking around, sees the Scarecrow now standing in the empty garden, worn, weathered, looking like someone crucified with its arms out.
  EXPRESSION: Observant
- CHARACTER: Narrator
  LINE: Her eyes move to the barn, shadowed in the dark like some ill-boding beast. We can see that she’s drawn to it.
  EXPRESSION: Sensing
- CHARACTER: Narrator
  LINE: She steps off the porch. Halfway across the yard, she stops, as if she senses something, like she’s being watched.
  EXPRESSION: Alert
- CHARACTER: Narrator
  LINE: She shifts her gaze just beyond the barn, where a restless breeze has the entire landscape in motion. She lets it go, continues on to the barn.
  EXPRESSION: Calm

::PATHS::
- CHOICE: "Approach the barn"
  TARGET: barn_exterior
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Barn Exterior
MOOD: Horrific
CHARACTERS: Lorraine
BACKGROUND_IMAGE: barn_exterior.png
BACKGROUND_EDIT: "Nighttime, dark barn, dead pigeons on ground"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Lorraine’s about to open the door when she sees two dead pigeons on the ground, necks broken.
  EXPRESSION: Apprehensive
- CHARACTER: Narrator
  LINE: She opens the barn door and looks in. She sees sabers of moonlight pierce in through gaps in the tired, dilapidated wood siding, then Lorraine’s immediately hit with ANOTHER HARD HITTING image of Judson on the ground, his bloody face smashed in.
  EXPRESSION: Horrified
- CHARACTER: Narrator
  LINE: Resume.
  EXPRESSION: null

::PATHS::
- CHOICE: "Enter the barn"
  TARGET: barn_interior
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Barn Interior
MOOD: Terrifying
CHARACTERS: Lorraine, Ed
BACKGROUND_IMAGE: barn_interior.png
BACKGROUND_EDIT: "Continuous, dark, old barn, faint moonlight"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Lorraine steps into the barn and continues several feet in. She stops, takes in her environment. An old CHEVY PICKUP is parked toward the back next to an elongated work bench. Six abandoned horse stalls are tucked along one side. There’s a ladder that leads up to a loft.
  EXPRESSION: Observant
- CHARACTER: Narrator
  LINE: As Lorraine turns to leave -- KA-THUMP!
  EXPRESSION: Startled
- CHARACTER: Narrator
  LINE: A SET OF BARE FEET COME JERKING TO A STOP RIGHT IN FRONT OF HER FACE, the toenails are incredibly long. Cracked. Dirty.
  EXPRESSION: Terrified
- CHARACTER: Narrator
  LINE: Lorraine looks up. Sees a woman dangling from a rafter by a rope, her neck broken at an odd angle.
  EXPRESSION: Horrified
- CHARACTER: Narrator
  LINE: She’s in a long grey dress, and has scraggly dark hair framing her face. Her eyes are bulging wide open, and seem to be staring at Lorraine.
  EXPRESSION: null
- CHARACTER: Ed
  LINE: There you are.
  EXPRESSION: Relieved
- CHARACTER: Narrator
  LINE: Lorraine’s eyes shift to Ed standing in the doorway, she walks toward him, literally passing through the dangling legs as they fade from her psychic vision.
  EXPRESSION: Recovering

::PATHS::
- CHOICE: "Return to the house"
  TARGET: perron_house_kitchen_later
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Perron House - Kitchen
MOOD: Grave
CHARACTERS: Ed, Lorraine, Carolyn
BACKGROUND_IMAGE: kitchen.png
BACKGROUND_EDIT: "Later, kitchen table, coffee cups, melted monkeys"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Ed and Lorraine are sitting at the kitchen table. Carolyn refills coffee cups. Lorraine’s looking at the melted monkeys on the table before her.
  EXPRESSION: null
- CHARACTER: Carolyn
  LINE: Do you think she’s the same one Cindy saw?
  EXPRESSION: Anxious
- CHARACTER: Lorraine
  LINE: -- I don’t know.
  EXPRESSION: Uncertain
- CHARACTER: Ed
  LINE: When these things invade a home, it’s quite possible that something has invited them here, or conjured them up somehow.
  EXPRESSION: Explaining
- CHARACTER: Lorraine
  LINE: I’ve asked the girls, but we need to know -- have either you or your husband ever practiced any kind of Satanic worship -- anything of the occult?
  EXPRESSION: Direct
- CHARACTER: Carolyn
  LINE: My God, no.
  EXPRESSION: Appalled
- CHARACTER: Ed
  LINE: People dabble, think it’s kind of fun. Play with a Ouija board, invoke things up in a Seance -- and then can’t get rid of them. It happens more often than you know.
  EXPRESSION: Warning
- CHARACTER: Lorraine
  LINE: With what I saw in the basement, this house was some sort of satanic shrine at some point.
  EXPRESSION: Serious
- CHARACTER: Lorraine
  LINE: Do you know the history of this farm?
  EXPRESSION: Inquisitive
- CHARACTER: Carolyn
  LINE: Just that it was built sometime in the late 1800’s. We bought it from an auction through a Bank Trust -- we never knew who the owners were. I always wanted to live in the country -- this was supposed to be someplace safer than the city.
  EXPRESSION: Reflective
- CHARACTER: Narrator
  LINE: Ed takes a moment, then --
  EXPRESSION: null
- CHARACTER: Ed
  LINE: This house obviously has to be exorcised, but to do that, we need the church to authorize a Priest to perform one.
  EXPRESSION: Firm
- CHARACTER: Carolyn
  LINE: I’m fine with that.
  EXPRESSION: Relieved
- CHARACTER: Ed
  LINE: It’s not that easy. We have to provide proof that what you’re claiming is in fact happening, but that can be the hard part.
  EXPRESSION: Realistic
- CHARACTER: Carolyn
  LINE: Why’s that?
  EXPRESSION: Confused
- CHARACTER: Lorraine
  LINE: Because it doesn’t always happen when we need it to.
  EXPRESSION: Explaining
- CHARACTER: Carolyn
  LINE: So what happens if we don’t get it?
  EXPRESSION: Concerned
- CHARACTER: Ed
  LINE: We don’t have the church.
  EXPRESSION: Grave
- CHARACTER: Narrator
  LINE: Carolyn deflates.
  EXPRESSION: Discouraged

::PATHS::
- CHOICE: "Prepare to leave"
  TARGET: house_foyer
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: House - Foyer
MOOD: Solemn
CHARACTERS: Ed, Lorraine, Carolyn
BACKGROUND_IMAGE: house_foyer.png
BACKGROUND_EDIT: "Right after, front door, clock in hand"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Ed and Lorraine stand at the front door, ready to leave. Carolyn’s with them. Ed, who’s holding the clock from the kitchen, looks at her, straightforward.
  EXPRESSION: null
- CHARACTER: Ed
  LINE: What’s your faith?
  EXPRESSION: Direct
- CHARACTER: Carolyn
  LINE: -- I was raised Methodist, I guess --
  EXPRESSION: Hesitant
- CHARACTER: Ed
  LINE: Have your children been Baptized?
  EXPRESSION: Inquisitive
- CHARACTER: Carolyn
  LINE: No -- we’re not really a church going family.
  EXPRESSION: Honest
- CHARACTER: Narrator
  LINE: Ed glances to Lorraine, then --
  EXPRESSION: null
- CHARACTER: Ed
  LINE: You may want to rethink that. Without faith, you have no protection.
  EXPRESSION: Warning
- CHARACTER: Narrator
  LINE: Carolyn’s not quite sure where Ed is going with this --
  EXPRESSION: Confused
- CHARACTER: Ed
  LINE: -- Our presence here could make things worse.
  EXPRESSION: Grave
- CHARACTER: Carolyn
  LINE: -- Why?
  EXPRESSION: Worried
- CHARACTER: Ed
  LINE: Because we’re a threa
  EXPRESSION: Explaining

::PATHS::
- CHOICE: "End of excerpt"
  TARGET: end
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Perron House
MOOD: Emotional, Tense
CHARACTERS: Carolyn, Lorraine, Ed, Cindy, Andrea
BACKGROUND_IMAGE: perron_house_living_room.png
BACKGROUND_EDIT: "Nighttime, interior of an old house, emotional atmosphere"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Carolyn floods with emotion. It’s all too much. Lorraine pulls her into an embrace.
  EXPRESSION: null
- CHARACTER: Lorraine
  LINE: This is your house -- and Ed and I are going to do everything we can to keep it that way. No one likes uninvited guests. Okay?
  EXPRESSION: Reassuring
- CHARACTER: Narrator
  LINE: Carolyn wipes away a tear.
  EXPRESSION: Sad
- CHARACTER: Ed
  LINE: We’ll talk to the Historian in the morning and see what we can find out, but it’ll be a few days before we can get back here. We have to make sure our tech guy is available and we also need to get someone to film everything for us.
  EXPRESSION: Serious
- CHARACTER: Narrator
  LINE: Lorraine’s attention is drawn to Cindy and Andrea, looking down at them from the top of the stairs with scared, worried faces.
  EXPRESSION: Concerned

::PATHS::
- CHOICE: "The Warrens leave for the motel"
  TARGET: warrens_plymouth
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Warren’s Plymouth
MOOD: Calm, Transition
CHARACTERS: Ed
BACKGROUND_IMAGE: warrens_plymouth.png
BACKGROUND_EDIT: "Nighttime, car interior, pulling up to a motel"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Ed pulls up to the entrance of the Harrisville Motel, single story, maybe thirty rooms.
  EXPRESSION: null

::PATHS::
- CHOICE: "Enter the motel room"
  TARGET: motel_room_night_76
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Motel Room
MOOD: Reflective
CHARACTERS: Lorraine, Ed
BACKGROUND_IMAGE: motel_room.png
BACKGROUND_EDIT: "Nighttime, simple motel room, Lorraine on bed with phone"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Lorraine is sitting on the edge of a queen-size bed, the cradle of a dial phone to her ear, listening. She makes eye contact with Ed, who enters from outside, carrying a small suitcase and the cardboard box with the tape recorder and kitchen clock inside.
  EXPRESSION: null
- CHARACTER: Lorraine
  LINE: Well that’s very nice of grandma -- seeing as it’s so far past your bed time and you have school tomorrow.
  EXPRESSION: Loving
- CHARACTER: Narrator
  LINE: Ed grins, places the box and suitcase on a dresser.
  EXPRESSION: null
- CHARACTER: Lorraine
  LINE: Yes honey, daddy’s right here.
  EXPRESSION: Loving
- CHARACTER: Lorraine
  LINE: I love you too.
  EXPRESSION: Loving
- CHARACTER: Narrator
  LINE: She holds out the phone for Ed, who takes a seat next to her, mouths “she promised”. Ed seems somewhat amused.
  EXPRESSION: null
- CHARACTER: Ed
  LINE: Hi pumpkin, what’cha doing up so late?
  EXPRESSION: Amused
- CHARACTER: Narrator
  LINE: While he listens --
  EXPRESSION: null
- CHARACTER: Ed
  LINE: Oh, Tennessee Tuxedo was on?
  EXPRESSION: Amused

::PATHS::
- CHOICE: "Go to the bathroom"
  TARGET: motel_bathroom_later
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Motel Bathroom
MOOD: Intimate, Pensive
CHARACTERS: Lorraine, Ed
BACKGROUND_IMAGE: motel_bathroom.png
BACKGROUND_EDIT: "Late night, steam, bubbles in a tub, Ed and Lorraine soaking"

::SCRIPT::
- CHARACTER: Narrator
  LINE: CU on Lorraine soaking in the tub filled with bubbles, her eyes are closed.
  EXPRESSION: Relaxed
- CHARACTER: Narrator
  LINE: Widen. We see that her head is tilted back on Ed’s chest, who is soaking with her, stroking her arms. Steam rises.
  EXPRESSION: null
- CHARACTER: Ed
  LINE: You seem kinda quiet, you okay?
  EXPRESSION: Concerned
- CHARACTER: Lorraine
  LINE: It’s just hitting close to home. Andrea reminds me so much of Judy.
  EXPRESSION: Sad
- CHARACTER: Ed
  LINE: I know. We’ll get it fixed.
  EXPRESSION: Reassuring

::PATHS::
- CHOICE: "Return to the motel room"
  TARGET: motel_room_later_78
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Motel Room
MOOD: Mysterious, Concerned
CHARACTERS: Lorraine, Ed
BACKGROUND_IMAGE: motel_room.png
BACKGROUND_EDIT: "Late night, Lorraine drying hair, Ed with tape recorder"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Lorraine exits the bathroom, donning a robe. She’s towel drying her hair.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Doesn’t like the look she gets from Ed, who is clad in a pair of pajama bottoms, sitting on the edge of the bed with the tape recorder in his hands.
  EXPRESSION: null
- CHARACTER: Lorraine
  LINE: What’s wrong?
  EXPRESSION: Concerned
- CHARACTER: Ed
  LINE: Carolyn’s voice didn’t record. Listen.
  EXPRESSION: Confused
- CHARACTER: Narrator
  LINE: He hits play. WE HEAR:
  EXPRESSION: null
- CHARACTER: Ed (V.O.)
  LINE: My name’s Ed Warren. It’s November 1st, 1972. I’m sitting here with Carolyn Perron who, with her family, has been experiencing supernatural occurrences -- okay, go ahead.
  EXPRESSION: Narrating
- CHARACTER: Narrator
  LINE: A long silence follows.
  EXPRESSION: null
- CHARACTER: Ed (V.O.)
  LINE: And what happened after that?
  EXPRESSION: Narrating
- CHARACTER: Narrator
  LINE: Another long silence. Ed clicks it off, looks to Lorraine, not sure what to make of it.
  EXPRESSION: Confused

::PATHS::
- CHOICE: "The scene shifts to Perron House"
  TARGET: perron_house_staircase
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Perron House - Staircase
MOOD: Terrifying, Horrified
CHARACTERS: Cindy, Young Boy, Carolyn
BACKGROUND_IMAGE: perron_house_staircase.png
BACKGROUND_EDIT: "Nighttime, old staircase, water cascading down"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Cindy is heading up the staircase with a glass of milk in hand when water slowly cascades down from the stairs above her and slowly caresses her feet before moving on down to the next stair.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: She looks up eyes go wide. Standing on a stair, several up from her, is a YOUNG BOY (12), soaking wet, dressed in vintage clothing. His skin is stark white and rotting in places, and he has a non-stop flow of water dribbling out his mouth.
  EXPRESSION: Terrified
- CHARACTER: Narrator
  LINE: Cindy drops the glass, it shatters. She screams. A second later, a very concerned Carolyn shows up at the top of the stairs. Cindy can barely get the words out.
  EXPRESSION: Terrified
- CHARACTER: Cindy
  LINE: There was a boy standing right there --
  EXPRESSION: Terrified
- CHARACTER: Narrator
  LINE: She points to where she saw him, he’s gone, but the water is still present and dripping down the stairs.
  EXPRESSION: null

::PATHS::
- CHOICE: "The scene shifts back to the motel room"
  TARGET: motel_room_night_80
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Motel Room
MOOD: Supernatural, Shocked
CHARACTERS: Ed, Lorraine
BACKGROUND_IMAGE: motel_room.png
BACKGROUND_EDIT: "Nighttime, dark motel room, faint light from bathroom"

::SCRIPT::
- CHARACTER: Narrator
  LINE: A night light flowing out from the open bathroom door casts a light glow over Ed and Lorraine, who are sound asleep in the bed.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: O.C. A SOFT CLICK, then WE HEAR the tape recorder kicking on by itself.
  EXPRESSION: null
- CHARACTER: Ed (V.O.)
  LINE: My name’s Ed Warren. It’s November first, 1972.
  EXPRESSION: Narrating
- CHARACTER: Narrator
  LINE: The sound of Ed’s voice is LOUD, snapping Ed and Lorraine out of their sleep, unbelieving. Both sets of eyes target the tape recorder sitting on a small table near the foot of their bed.
  EXPRESSION: Shocked
- CHARACTER: Ed (V.O.)
  LINE: I’m sitting here with Carolyn Perron who, with her family, has been experiencing supernatural occurrences -- okay, go ahead.
  EXPRESSION: Narrating
- CHARACTER: Narrator
  LINE: Where as this part of the tape was blank earlier, it’s now filled with an INDISCERNIBLE, HAUNTING WHISPER that sounds female, it continues, until --
  EXPRESSION: Terrified
- CHARACTER: Ed (V.O.)
  LINE: What happened after that?
  EXPRESSION: Narrating
- CHARACTER: Narrator
  LINE: The tape recorder then suddenly SHUTS OFF.
  EXPRESSION: null
- CHARACTER: Lorraine
  LINE: Ed, the clock.
  EXPRESSION: Concerned
- CHARACTER: Narrator
  LINE: He looks where her gaze is locked, she’s staring at the Perron clock next to the recorder. The time on it reads 5:15. They look at it, transfixed. It never moves to: 5:16.
  EXPRESSION: Transfixed

::PATHS::
- CHOICE: "Head to Main Street Harrisville"
  TARGET: main_street_harrisville
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Main Street - Harrisville
MOOD: Calm, Investigative
CHARACTERS: Ed, Lorraine
BACKGROUND_IMAGE: main_street_harrisville.png
BACKGROUND_EDIT: "Daytime, small town, stores, light traffic"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Small town. Stores and businesses line both sides of the street. Light traffic.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Ed and Lorraine are driving through. They pass the Catholic church. The marquee in front reads: LET GOD GIVE YOU A GREAT DAY.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Ed continues for another block, then pulls over, coming to a stop in front of MATHEWS DRY GOODS store. It’s simple, with two large windows, separated by an entrance. A second story sits above it.
  EXPRESSION: null

::PATHS::
- CHOICE: "Enter Mathews Dry Goods Store"
  TARGET: mathews_dry_goods_store
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Mathews Dry Goods Store
MOOD: Informative
CHARACTERS: Ed, Lorraine, Shannon Mathews, Maddy (teenage girl), Customer
BACKGROUND_IMAGE: mathews_dry_goods_store.png
BACKGROUND_EDIT: "Daytime, interior of an old dry goods store, busy"

::SCRIPT::
- CHARACTER: Narrator
  LINE: S.O. of a bell that rings when Ed and Lorraine enter the store. Inside is filled with a potpourri of dry goods.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: SHANNON MATHEWS, a woman in her late 30’s, and a teenage girl are behind a long counter that stretches from the front of the store to a set of steps leading upstairs in the back. A lava lamp sits next to a register.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Shannon’s busy cutting a piece of fabric for a customer when she looks up.
  EXPRESSION: null
- CHARACTER: Shannon
  LINE: Ed and Lorraine?
  EXPRESSION: Surprised
- CHARACTER: Narrator
  LINE: They both smile.
  EXPRESSION: Happy
- CHARACTER: Ed
  LINE: Thanks for seeing us.
  EXPRESSION: Grateful
- CHARACTER: Narrator
  LINE: Shannon looks to the teenage girl next to her.
  EXPRESSION: null
- CHARACTER: Shannon
  LINE: Maddy, finish cutting this for Mrs. Doornbos, will ya?
  EXPRESSION: Directive
- CHARACTER: Narrator
  LINE: Maddy nods that she will, and although she takes the scissors from Shannon, her eyes never leave Ed and Lorraine, neither are sure what it’s all about.
  EXPRESSION: Curious
- CHARACTER: Narrator
  LINE: Shannon looks to Ed and Lorraine.
  EXPRESSION: null
- CHARACTER: Shannon
  LINE: Why don’t you follow me.
  EXPRESSION: Inviting
- CHARACTER: Narrator
  LINE: She grabs a large coffee mug off the counter and heads to a set of stairs in the back of the store. Ed and Lorraine follow.
  EXPRESSION: null
- CHARACTER: Shannon
  LINE: You gotta ignore my niece, she goes to school with the Perron girls -- she’s heard about what’s been happening out there.
  EXPRESSION: Explaining

::PATHS::
- CHOICE: "Follow Shannon upstairs"
  TARGET: store_stairs
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Store Stairs
MOOD: Informative
CHARACTERS: Shannon, Ed, Lorraine
BACKGROUND_IMAGE: store_stairs.png
BACKGROUND_EDIT: "Daytime, old wooden stairs in a dry goods store"

::SCRIPT::
- CHARACTER: Narrator
  LINE: As they head up --
  EXPRESSION: null
- CHARACTER: Shannon
  LINE: Before the Perron’s bought it, that place had been empty for as long as I can remember.
  EXPRESSION: Informative
- CHARACTER: Shannon
  LINE: Please excuse the mess up here, my Nana’s been the Historian for almost sixty years, and when she got Parkinson's, things just sort of -- well, you can imagine.
  EXPRESSION: Apologetic

::PATHS::
- CHOICE: "Reach the upstairs room"
  TARGET: mathews_dry_goods_upstairs
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Mathews Dry Goods - Upstairs
MOOD: Informative
CHARACTERS: Shannon, Ed, Lorraine
BACKGROUND_IMAGE: mathews_dry_goods_upstairs.png
BACKGROUND_EDIT: "Daytime, disheveled room packed with old documents, books"

::SCRIPT::
- CHARACTER: Narrator
  LINE: They come up off the last stair into a large, disheveled looking room packed with stacks of books, filing cabinets, piles of old newspapers and photos.
  EXPRESSION: null
- CHARACTER: Shannon
  LINE: I took over the job, but haven’t had much time to put into it.
  EXPRESSION: Explaining
- CHARACTER: Narrator
  LINE: Shannon heads over to a nearby table that stands in the middle of the room, where pictures, maps, journals and other documents are piled in two large boxes.
  EXPRESSION: null
- CHARACTER: Shannon
  LINE: I pulled everything together for you I could find, but there’s some stretches of time missing. I’ll keep looking and send you anything else I might find.
  EXPRESSION: Helpful

::PATHS::
- CHOICE: "The scene shifts to Perron House Master Bedroom"
  TARGET: perron_house_master_bedroom
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Perron House - Master Bedroom
MOOD: Calm, Anticipatory
CHARACTERS: Carolyn, Roger (implied)
BACKGROUND_IMAGE: perron_house_master_bedroom.png
BACKGROUND_EDIT: "Nighttime, interior of a bedroom, headlights outside"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Carolyn is getting ready for bed. There’s a flare in the window from headlights coming down the driveway. She moves to the window and looks out, it’s Roger returning in the rig.
  EXPRESSION: null

::PATHS::
- CHOICE: "Transition to the kitchen"
  TARGET: perron_house_kitchen
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Perron House - Kitchen
MOOD: Undetermined
CHARACTERS: Narrator
BACKGROUND_IMAGE: perron_house_kitchen.png
BACKGROUND_EDIT: "Interior of an old kitchen, night"

::SCRIPT::
- CHARACTER: Narrator
  LINE: (Scene ends abruptly, implied action of Carolyn going to the kitchen or Roger entering)
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue to next scene"
  TARGET: end
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Perron House - Kitchen
MOOD: Tense
CHARACTERS: Roger, Carolyn, Narrator
BACKGROUND_IMAGE: perron_house_kitchen.png
BACKGROUND_EDIT: "Nighttime, strained atmosphere, scotch bottle visible"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Roger looks clearly irritated as he reaches for a bottle of scotch in a cabinet. Carolyn is leaning against the counter, arms folded, trying to stay strong.
  EXPRESSION: null
- CHARACTER: Roger
  LINE: I can’t believe you did this behind my back.
  EXPRESSION: Angry
- CHARACTER: Carolyn
  LINE: We have to do something. It’s getting worse.
  EXPRESSION: Afraid
- CHARACTER: Roger
  LINE: I told you I didn’t want anymore of this bullshit.
  EXPRESSION: Angry
- CHARACTER: Carolyn
  LINE: They said you haven’t seen anything because it wants to create “this”, this conflict between us.
  EXPRESSION: Explaining
- CHARACTER: Narrator
  LINE: Roger half laughs to himself as he uncorks the bottle.
  EXPRESSION: Sarcastic
- CHARACTER: Roger
  LINE: Of course they did.
  EXPRESSION: Sarcastic
- CHARACTER: Narrator
  LINE: He pours a stiff one.
  EXPRESSION: null
- CHARACTER: Roger
  LINE: And how much are they charging for this little investigation?
  EXPRESSION: Sarcastic
- CHARACTER: Carolyn
  LINE: 57.
  EXPRESSION: Neutral
- CHARACTER: Narrator
  LINE: She moves over to Roger and takes his hands in hers before he can lift the glass to his mouth.
  EXPRESSION: null
- CHARACTER: Carolyn
  LINE: I’m scared to death and so are the girls -- and I hate what it’s doing to us.
  EXPRESSION: Afraid
- CHARACTER: Narrator
  LINE: She looks at him eye to eye.
  EXPRESSION: null
- CHARACTER: Carolyn
  LINE: Please Roger. For me -- please.
  EXPRESSION: Pleading

::PATHS::
- CHOICE: "Continue"
  TARGET: warren_house_kitchen
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Warren House - Kitchen
MOOD: Investigative
CHARACTERS: Ed, Lorraine, Narrator
BACKGROUND_IMAGE: warren_house_kitchen.png
BACKGROUND_EDIT: "Early morning, kitchen, research materials spread on desk"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Ed enters, looking half asleep. Goes to the coffee pot.
  EXPRESSION: null
- CHARACTER: Lorraine O.C.
  LINE: You’re gonna have to make some more.
  EXPRESSION: Neutral
- CHARACTER: Narrator
  LINE: Ed looks to an alcove off the kitchen, spotting Lorraine, who has all the info they got from the Historian spread out on a small desk. She’s holding a hand written journal.
  EXPRESSION: null
- CHARACTER: Ed
  LINE: How long have you been up?
  EXPRESSION: Surprised
- CHARACTER: Lorraine
  LINE: Since four -- couldn’t sleep.
  EXPRESSION: Tired
- CHARACTER: Narrator
  LINE: She looks at him, there’s an intensity in her eyes.
  EXPRESSION: null
- CHARACTER: Lorraine
  LINE: It’s no wonder that family is going through what they are.
  EXPRESSION: Serious
- CHARACTER: Narrator
  LINE: An old, very weathered photograph of the Perron farm house. Widen, we see that Ed is holding the picture, a pile of others are next to him. He nurses a cup of coffee.
  EXPRESSION: null
- CHARACTER: Lorraine
  LINE: -- That’s the original farmhouse. It was built in 1863 by Judson Sherman, who married Bathsheba Bishop when she was nineteen.
  EXPRESSION: Explaining
- CHARACTER: Narrator
  LINE: (beat)
  EXPRESSION: null
- CHARACTER: Lorraine
  LINE: She was a direct descendant of Bridget Bishop --
  EXPRESSION: Explaining
- CHARACTER: Ed
  LINE: We know that name --
  EXPRESSION: Realizing
- CHARACTER: Narrator
  LINE: She pauses.
  EXPRESSION: null
- CHARACTER: Lorraine
  LINE: Yeah, she was the first witch hung in Salem during the trials.
  EXPRESSION: Serious
- CHARACTER: Narrator
  LINE: Ed looks to Lorraine, definitely intrigued.
  EXPRESSION: null
- CHARACTER: Lorraine
  LINE: After she and Judson were married, they had a baby, and when it was seven days old, Judson found it sacrificed -- in front of the fireplace.
  EXPRESSION: Serious
- CHARACTER: Narrator
  LINE: Ed can’t believe it.
  EXPRESSION: Surprised
- CHARACTER: Lorraine
  LINE: I’m assuming with knitting needles. Apparently -- she ran out to the barn, climbed into the rafters, proclaimed her love to Satan, cursed anyone who tried to take her land, then hung herself.
  EXPRESSION: Serious
- CHARACTER: Narrator
  LINE: Lorraine slides an old newspaper clipping mounted on parchment paper over to Ed, who picks it up.
  EXPRESSION: null
- CHARACTER: Lorraine
  LINE: That’s her.
  EXPRESSION: Serious
- CHARACTER: Narrator
  LINE: Ed looks at the picture; it’s of a woman hanging from a rafter, EXACTLY THE SAME IMAGE AND LIKENESS OF THE WOMAN LORRAINE SAW HANGING IN THE BARN STARING DOWN AT HER.
  EXPRESSION: null
- CHARACTER: Ed
  LINE: This is the woman you saw?
  EXPRESSION: Shocked
- CHARACTER: Narrator
  LINE: She nods, then --
  EXPRESSION: null
- CHARACTER: Lorraine
  LINE: Ed -- she hung herself at five fifteen in the morning.
  EXPRESSION: Serious
- CHARACTER: Ed
  LINE: That explains a few things.
  EXPRESSION: Understanding
- CHARACTER: Narrator
  LINE: Lorraine then slides over an old black and white photograph of an obese woman sitting in a wicker chair, flanked by a boy (wears glasses) and a girl, who both look about ten.
  EXPRESSION: null
- CHARACTER: Lorraine
  LINE: And that woman I saw in the basement who shot herself -- I think it’s this woman who lived there in the thirties -- last name is Walker. She had two children who mysteriously disappeared in the woods -- it’s probably why she killed herself. I’m assuming those are them --
  EXPRESSION: Serious
- CHARACTER: Ed
  LINE: Wow --
  EXPRESSION: Surprised
- CHARACTER: Lorraine
  LINE: And I’m not done. What was the original five hundred acre farm, has been divided, and sold off --
  EXPRESSION: Serious
- CHARACTER: Narrator
  LINE: She unfurls an old map next to her. Points to a spot.
  EXPRESSION: null
- CHARACTER: Lorraine
  LINE: There was a boy who drowned in this pond -- he lived in a house over here.
  EXPRESSION: Explaining
- CHARACTER: Narrator
  LINE: Her finger slides across the map to another location close by --
  EXPRESSION: null
- CHARACTER: Lorraine
  LINE: And a hunter who died in the woods -- he lived here.
  EXPRESSION: Explaining
- CHARACTER: Narrator
  LINE: Again, she indicates.
  EXPRESSION: null
- CHARACTER: Lorraine
  LINE: There was a school bus accident on this road.
  EXPRESSION: Explaining
- CHARACTER: Narrator
  LINE: She looks to Ed, more for emphasis than anything else.
  EXPRESSION: null
- CHARACTER: Lorraine
  LINE: The only children who died, were from families who had homes on the property. Four of them.
  EXPRESSION: Serious
- CHARACTER: Ed
  LINE: -- People who took her land.
  EXPRESSION: Realizing

::PATHS::
- CHOICE: "Continue"
  TARGET: rhode_island_road
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Rhode Island - Two Lane Road
MOOD: Transition
CHARACTERS: Narrator
BACKGROUND_IMAGE: rhode_island_road.png
BACKGROUND_EDIT: "Sunset, rural two-lane road, Ariel view of car"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Ariel pov of the Warren’s Plymouth as it slaloms its way along a country road illuminated by a brilliant sunset.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: It turns off onto the Perron’s driveway. Parks by the house.
  EXPRESSION: null

::PATHS::
- CHOICE: "Arrive at Perron House"
  TARGET: perron_house_driveway
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Perron House - Driveway
MOOD: Anticipation
CHARACTERS: Ed, Lorraine, Bruce Levy, Jerome, Narrator
BACKGROUND_IMAGE: perron_house_driveway.png
BACKGROUND_EDIT: "Sunset, outside Perron house, cars arriving, equipment visible"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Ed and Lorraine get out of their car with BRUCE LEVY (30). Clean cut, wears khakis. Gym built muscles gives his shirt a tight fit.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: They move around the back of their car.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Ed opens the trunk. Inside are four large bags of groceries, a cardboard box, which now holds Ed’s tape recorder, the Perron’s clock, a bible, a camera case, some note pads, and dozens of film canisters.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Bruce takes a beat, looking around.
  EXPRESSION: null
- CHARACTER: Bruce
  LINE: Nice place.
  EXPRESSION: Neutral
- CHARACTER: Narrator
  LINE: Lorraine’s attention is drawn to Jerome’s VW van turning onto the driveway and heading toward the house.
  EXPRESSION: null
- CHARACTER: Lorraine
  LINE: Good, Jerome’s here.
  EXPRESSION: Relieved
- CHARACTER: Narrator
  LINE: Jerome drives up right next to them and parks. Climbs out. He’s munching on a large cookie. Smiles to them.
  EXPRESSION: Happy
- CHARACTER: Jerome
  LINE: I forgot how bitchin’ Rhode Island is.
  EXPRESSION: Happy
- CHARACTER: Narrator
  LINE: He notices Bruce.
  EXPRESSION: null
- CHARACTER: Lorraine
  LINE: Jerome, this is Bruce Levy.
  EXPRESSION: Introducing
- CHARACTER: Jerome
  LINE: Oh, the cop -- nice to meet you, man.
  EXPRESSION: Friendly
- CHARACTER: Narrator
  LINE: As they shake hands.
  EXPRESSION: null
- CHARACTER: Jerome
  LINE: I heard you’re not much of a believer.
  EXPRESSION: Teasing
- CHARACTER: Bruce
  LINE: You might say that.
  EXPRESSION: Sarcastic
- CHARACTER: Jerome
  LINE: You know you can’t shoot ghosts, right?
  EXPRESSION: Teasing
- CHARACTER: Ed
  LINE: Easy on him, Jerome. C’mon, let’s get unloaded.
  EXPRESSION: Annoyed

::PATHS::
- CHOICE: "Unload equipment"
  TARGET: perron_house_front_door
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Perron House - Front Door
MOOD: Wary
CHARACTERS: Carolyn, Jerome, Ed, Bruce, Lorraine, Cindy, Andrea, Roger, Narrator
BACKGROUND_IMAGE: perron_house_front_door.png
BACKGROUND_EDIT: "Right after sunset, front door, equipment being brought in"

::SCRIPT::
- CHARACTER: Narrator
  LINE: A troubled looking Carolyn has the door open as Jerome, Ed and Bruce pile in, each loaded with monitors, VCRs, gauges, and various pieces of camera equipment, etc.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Lorraine follows, carrying a box.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Cindy and Andrea are looking down from the landing upstairs.
  EXPRESSION: Curious
- CHARACTER: Ed
  LINE: We’d like to do the main set up in the living room if that’s okay?
  EXPRESSION: Polite
- CHARACTER: Carolyn
  LINE: Yes, of course --
  EXPRESSION: Accommodating
- CHARACTER: Ed
  LINE: This is Jerome, and Officer Levy.
  EXPRESSION: Introducing
- CHARACTER: Bruce
  LINE: Bruce is fine.
  EXPRESSION: Polite
- CHARACTER: Narrator
  LINE: The guys nod hellos and move on just as Roger enters from the kitchen.
  EXPRESSION: null
- CHARACTER: Carolyn
  LINE: Ed and Lorraine, this is my husband, Roger.
  EXPRESSION: Introducing
- CHARACTER: Narrator
  LINE: Even though Ed sees the doubt in Roger’s eyes.
  EXPRESSION: null
- CHARACTER: Ed
  LINE: I hope we can help you out here.
  EXPRESSION: Sincere
- CHARACTER: Roger
  LINE: Yeah -- me too.
  EXPRESSION: Doubtful
- CHARACTER: Narrator
  LINE: (to Carolyn)
  EXPRESSION: null
- CHARACTER: Roger
  LINE: I’ll be in the barn.
  EXPRESSION: Dismissive
- CHARACTER: Narrator
  LINE: Roger heads out front as Ed continues into the living room with Jerome and Bruce.
  EXPRESSION: null
- CHARACTER: Lorraine
  LINE: How are you holding up?
  EXPRESSION: Concerned
- CHARACTER: Narrator
  LINE: Sees she’s not.
  EXPRESSION: null

::PATHS::
- CHOICE: "Go to kitchen"
  TARGET: perron_kitchen
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Perron House - Kitchen
MOOD: Supportive
CHARACTERS: Lorraine, Carolyn, Bruce, Narrator
BACKGROUND_IMAGE: perron_house_kitchen_interior.png
BACKGROUND_EDIT: "Right after arrival, kitchen, laundry baskets on table"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Lorraine is standing against the counter, listening to Carolyn.
  EXPRESSION: null
- CHARACTER: Carolyn
  LINE: -- Water was just pouring out of his mouth.
  EXPRESSION: Distressed
- CHARACTER: Lorraine
  LINE: This is good --
  EXPRESSION: Strategic
- CHARACTER: Narrator
  LINE: Off Carolyn’s surprised look.
  EXPRESSION: null
- CHARACTER: Lorraine
  LINE: We want the activity. It gives us the proof we need.
  EXPRESSION: Strategic
- CHARACTER: Narrator
  LINE: All Carolyn can do is manage a slow, reluctant nod of approval. Silent tears begin to cascade down her cheeks.
  EXPRESSION: Sad
- CHARACTER: Narrator
  LINE: Bruce enters, carrying the bags of groceries, interrupting the moment, isn’t quite sure what to do.
  EXPRESSION: Awkward
- CHARACTER: Narrator
  LINE: Lorraine nods to the kitchen table, which has two baskets of folded laundry sitting on it.
  EXPRESSION: null
- CHARACTER: Lorraine
  LINE: Why don’t you just put them over there.
  EXPRESSION: Directing
- CHARACTER: Narrator
  LINE: He does. Leaves. Carolyn looks over to the groceries.
  EXPRESSION: null
- CHARACTER: Carolyn
  LINE: -- You didn’t have to do that.
  EXPRESSION: Grateful
- CHARACTER: Lorraine
  LINE: Are you kidding me? Jerome will eat you out of house and home, believe me, it’s the least we can do.
  EXPRESSION: Friendly
- CHARACTER: Narrator
  LINE: Carolyn manages a slight smile.
  EXPRESSION: Slightly Happy
- CHARACTER: Lorraine
  LINE: Those have to go upstairs?
  EXPRESSION: Inquiring

::PATHS::
- CHOICE: "Continue"
  TARGET: perron_house_barn
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Perron House - Barn
MOOD: Eerie
CHARACTERS: Roger, Narrator
BACKGROUND_IMAGE: perron_house_barn_interior.png
BACKGROUND_EDIT: "Daytime, dark barn interior, column of light from open door, Chevy pickup in back"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The door opens. A column of outside light slides in, barely stretching to the Chevy pickup in the back. Roger comes in. As he reaches for a wall switch --
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Camera’s pov, over his shoulder toward the truck. We’d
  EXPRESSION: null

::PATHS::
- CHOICE: "End of excerpt"
  TARGET: end
  STATE_CHANGE: null
  CONDITION: null

::SCRIPT::
- CHARACTER: Narrator
  LINE: swear there was the silhouette of a woman sitting inside, seemingly looking at Roger, but the second the light comes on, it illuminates a vacant interior.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Resume. Roger heads over to the truck.
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue"
  TARGET: house_later
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: House Exterior
MOOD: Preparatory
CHARACTERS: Narrator, Ed, Bruce
BACKGROUND_IMAGE: house.png
BACKGROUND_EDIT: "Exterior of a house, later in the day"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Ed comes out of the house carrying a tripod and a 35mm camera. Heads for the barn. Bruce exits a few beats behind him, un-spooling cable.
  EXPRESSION: null

::PATHS::
- CHOICE: "Follow them into the barn"
  TARGET: barn_interior
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Barn Interior
MOOD: Tense, Mysterious
CHARACTERS: Narrator, Roger, Ed, Bruce
BACKGROUND_IMAGE: barn_interior.png
BACKGROUND_EDIT: "Inside a barn, dimly lit, pickup truck in foreground"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Roger has a jack positioned toward the front of the pickup and is working one end of a tire wrench to crank it up off the floor. There’s a small toolbox next to the jack.
  EXPRESSION: null
- CHARACTER: Ed
  LINE: Nice ride. Fifty-five?
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Roger looks back over his shoulder to see Ed coming in.
  EXPRESSION: null
- CHARACTER: Roger
  LINE: 64. Six.
  EXPRESSION: null
- CHARACTER: Ed
  LINE: Two-eighty-three small block?
  EXPRESSION: null
- CHARACTER: Roger
  LINE: You know trucks.
  EXPRESSION: Impressed
- CHARACTER: Narrator
  LINE: Roger finishes jacking up the truck. He flips the “safety” lever into the lock position on the jack.
  EXPRESSION: null
- CHARACTER: Ed
  LINE: My dad had a side-step with the big back window. Every Saturday, we were working on her. What’re you doing?
  EXPRESSION: null
- CHARACTER: Roger
  LINE: Just repacking the bearings.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Bruce enters, continues un-spooling the cable as he approaches Ed.
  EXPRESSION: null
- CHARACTER: Ed
  LINE: Well -- don’t mind us, we’ll only be a few minutes.
  EXPRESSION: null
- CHARACTER: Roger
  LINE: Knock yourself out.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Roger starts to unscrew the lugs. Ed mounts the camera onto the tripod. Takes the other end of the cable from Bruce and plugs into the side of the camera.
  EXPRESSION: null
- CHARACTER: Ed
  LINE: Did Jerome give you the EFD?
  EXPRESSION: null
- CHARACTER: Bruce
  LINE: If that’s what this is --
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: He extracts a small hand-held meter from his pocket. Hands it to him.
  EXPRESSION: null
- CHARACTER: Bruce
  LINE: What’s it do?
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: As Ed begins to hook it up.
  EXPRESSION: null
- CHARACTER: Ed
  LINE: When there’s an energy present, the needle on it will begin to fluctuate, usually between 1.7 and 3 mega-hertz, and that triggers the camera to start shooting.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Roger looks over to him as he pulls the tire off. Sets it down.
  EXPRESSION: null
- CHARACTER: Roger
  LINE: And you’ve actually caught things on film?
  EXPRESSION: null
- CHARACTER: Ed
  LINE: Well yeah -- that’s the point.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Roger, quietly amused, focuses back on the truck. Notices oil dripping from the drain pain. Rolls onto his back and scoots underneath to investigate.
  EXPRESSION: Amused
- CHARACTER: Bruce
  LINE: So why are we putting one in here?
  EXPRESSION: null
- CHARACTER: Ed
  LINE: This is where the witch committed suicide. Hung herself from the rafter right above us.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: As Bruce looks up --
  EXPRESSION: null
- CHARACTER: Ed
  LINE: Apparitions will at times manifest near their points of death.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: At that very moment -- WHAM! THE PICKUP SUDDENLY DROPS back down to the floor, emanating a harsh, crunching sound. Ed and Bruce snap a look over to see Roger’s legs protruding out toward them from a small 10” gap between the barn floor and side of the truck, created by the now crushed tool box. They rush over --
  EXPRESSION: Surprised
- CHARACTER: Ed
  LINE: Roger--?
  EXPRESSION: Concerned

::PATHS::
- CHOICE: "Check on Roger"
  TARGET: under_truck
  STATE_CHANGE: fear = +2
  CONDITION: null

::SCENE::
LOCATION: Under The Truck
MOOD: Terrified
CHARACTERS: Narrator, Roger
BACKGROUND_IMAGE: under_truck.png
BACKGROUND_EDIT: "Close up on Roger's face, confined space under a truck"

::SCRIPT::
- CHARACTER: Narrator
  LINE: CU on Roger’s terrorized face pressed slightly against the bottom of the chassis, another millimeter and it’d be a different story.
  EXPRESSION: Afraid
- CHARACTER: Roger
  LINE: I’m alright, can you pull me out?
  EXPRESSION: Afraid

::PATHS::
- CHOICE: "Pull Roger out"
  TARGET: barn_interior_resume
  STATE_CHANGE: fear = -1
  CONDITION: null

::SCENE::
LOCATION: Barn Interior
MOOD: Relieved, Uneasy
CHARACTERS: Narrator, Ed, Bruce, Roger
BACKGROUND_IMAGE: barn_interior.png
BACKGROUND_EDIT: "Inside a barn, Roger being pulled from under the truck"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Ed and Bruce each take a leg and pull on him. His body slowly emerges. Roger looks to them.
  EXPRESSION: null
- CHARACTER: Roger
  LINE: Thanks.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: He notices the tool box.
  EXPRESSION: null
- CHARACTER: Roger
  LINE: That was close.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Roger gets to his feet. Picks up the Jack that’s fallen over. Looks at it, the safety lock is now off.
  EXPRESSION: null
- CHARACTER: Roger
  LINE: Safety must’ve slipped.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: We see by the look on Ed’s face that he thinks there’s more going on here than that.
  EXPRESSION: Afraid

::PATHS::
- CHOICE: "Move to the house"
  TARGET: cindys_room
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Cindy's Room, House Interior
MOOD: Somber, Explanatory
CHARACTERS: Narrator, Carolyn, Lorraine
BACKGROUND_IMAGE: cindys_room.png
BACKGROUND_EDIT: "Inside a child's bedroom, laundry baskets"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Carolyn is putting clothes away in Cindy’s drawers from the laundry baskets. Lorraine watches.
  EXPRESSION: null
- CHARACTER: Carolyn
  LINE: How could a mother kill her own child?
  EXPRESSION: Sad
- CHARACTER: Lorraine
  LINE: It was never a child to her -- she just used her God given gift as the ultimate offense against him. Witches believe it elevates their status in the eyes of Satan.
  EXPRESSION: null

::PATHS::
- CHOICE: "Proceed to the living room"
  TARGET: living_room_jerome
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Living Room, House Interior
MOOD: Curious, Technical
CHARACTERS: Narrator, Jerome, Cindy
BACKGROUND_IMAGE: living_room.png
BACKGROUND_EDIT: "Inside a living room, spaghetti pile of cables, monitors"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Jerome is munching from a bag of potato chips while sorting through a spaghetti pile of cables that run from SEVEN different VCR’s to SEVEN separate MONITORS, each labeled accordingly; basement, upstairs hallway, downstairs hallway, master, living room, barn, and the girl’s bedroom. Cindy is standing next to Jerome, looks somewhat smitten.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Jerome cuts off a slice of tape with a PAIR OF SCISSORS and secures it around one of the cables, holding several loops in place.
  EXPRESSION: null
- CHARACTER: Cindy
  LINE: And what’s that?
  EXPRESSION: Curious
- CHARACTER: Jerome
  LINE: A VCR -- it’s a video recording device. They think one of these will be in every house one day --
  EXPRESSION: null
- CHARACTER: Cindy
  LINE: Really? Why?
  EXPRESSION: Curious
- CHARACTER: Jerome
  LINE: To record what’s on your TV -- so you can watch it anytime you want.
  EXPRESSION: null
- CHARACTER: Cindy
  LINE: That’d be so cool.
  EXPRESSION: Happy
- CHARACTER: Jerome
  LINE: Pretty far out, isn’t it?
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: She smiles.
  EXPRESSION: Happy

::PATHS::
- CHOICE: "Go to the stairway"
  TARGET: house_stairway
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: House Stairway
MOOD: Social, Uneasy
CHARACTERS: Narrator, Lorraine, Carolyn, Cindy, Andrea, Ed, Bruce
BACKGROUND_IMAGE: house_stairway.png
BACKGROUND_EDIT: "Interior of a house, staircase and foyer area"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Lorraine and Carolyn descend the stairs, each carrying an empty laundry basket. They stop at the foyer where their attention is drawn to Cindy and Jerome in the living room.
  EXPRESSION: null
- CHARACTER: Lorraine
  LINE: Looks like someone might have a crush.
  EXPRESSION: Amused
- CHARACTER: Narrator
  LINE: The edge of Carolyn’s lips curl into a amused smile.
  EXPRESSION: Amused
- CHARACTER: Carolyn
  LINE: He certainly looks like he knows what he’s doing.
  EXPRESSION: Amused
- CHARACTER: Lorraine
  LINE: Top of his class at MIT.
  EXPRESSION: null
- CHARACTER: Carolyn
  LINE: And Bruce is a police officer?
  EXPRESSION: Curious
- CHARACTER: Lorraine
  LINE: Yes, Ed likes to use them as documentarians -- people trust them. I think it’s because Ed’s dad was a cop.
  EXPRESSION: null
- CHARACTER: Andrea
  LINE: Mom, can you braid my hair?
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Carolyn turns to see Andrea on the stairway behind them, holding a hair brush and a tie-off.
  EXPRESSION: null
- CHARACTER: Carolyn
  LINE: Oh honey, I need to get dinner going --
  EXPRESSION: null
- CHARACTER: Lorraine
  LINE: I can do that for you -- I do my daughter’s all the time.
  EXPRESSION: Happy
- CHARACTER: Narrator
  LINE: Lorraine hands her basket to Carolyn, then sits down on the second to last step. Taps the one below her. Andrea takes a seat on it. Carolyn heads in to the kitchen. Lorraine takes the brush from Andrea, and begins to stroke the young girl’s lengthy hair.
  EXPRESSION: null
- CHARACTER: Andrea
  LINE: What’s your daughter’s name?
  EXPRESSION: Curious
- CHARACTER: Lorraine
  LINE: Judy. She’s about your age.
  EXPRESSION: null
- CHARACTER: Andrea
  LINE: And she likes her hair braided too?
  EXPRESSION: Curious
- CHARACTER: Lorraine
  LINE: Um-hum. We braid it every night before she goes to bed.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Cindy walks out of the living room. Takes a seat next to Lorraine, watching her brush Andrea’s hair.
  EXPRESSION: null
- CHARACTER: Cindy
  LINE: Have you always been able to see things?
  EXPRESSION: Curious
- CHARACTER: Andrea
  LINE: Yeah, have you?
  EXPRESSION: Happy
- CHARACTER: Narrator
  LINE: A subtle laugh escapes Lorraine as she gathers the hair in three sections, and begins to braid.
  EXPRESSION: Amused
- CHARACTER: Lorraine
  LINE: Ever since I can remember.
  EXPRESSION: null
- CHARACTER: Cindy
  LINE: What’s the first thing you saw?
  EXPRESSION: Curious
- CHARACTER: Lorraine
  LINE: An aura.
  EXPRESSION: null
- CHARACTER: Andrea
  LINE: What’s that?
  EXPRESSION: Curious
- CHARACTER: Lorraine
  LINE: It’s energy that surrounds your body.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Lorraine looks at both the girls, perusing them slightly.
  EXPRESSION: null
- CHARACTER: Lorraine
  LINE: You both have beautiful one’s, by the way --
  EXPRESSION: Happy
- CHARACTER: Narrator
  LINE: The girls smile. The front door swings open. Ed and Bruce enter.
  EXPRESSION: Happy
- CHARACTER: Bruce
  LINE: I put the other one at the end of the hallway.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Lorraine sends Ed a smile as they head down the hallway toward another camera and tripod waiting to be set up. He looks a little uneasy with her interacting with the girls. She sends him a confused look, what? He stops as Roger and Bruce continue down the hall. Waits for her to join him.
  EXPRESSION: null
- CHARACTER: Lorraine
  LINE: Excuse me one sec.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Lorraine gets to her feet, goes to Ed.
  EXPRESSION: null
- CHARACTER: Ed
  LINE: What’re you doing?
  EXPRESSION: Concerned
- CHARACTER: Lorraine
  LINE: What do you mean?
  EXPRESSION: Confused
- CHARACTER: Ed
  LINE: Getting a little close aren’t we?
  EXPRESSION: Concerned
- CHARACTER: Lorraine
  LINE: I’m braiding hair.
  EXPRESSION: null
- CHARACTER: Ed
  LINE: You know exactly what I’m talking about.
  EXPRESSION: Concerned
- CHARACTER: Lorraine
  LINE: I’m fine, Ed -- just helping out.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Ed looks like he’s not so sure, but lets it go.
  EXPRESSION: Concerned
- CHARACTER: Lorraine
  LINE: Did you guys get all set up in the barn?
  EXPRESSION: Curious
- CHARACTER: Ed
  LINE: Yeah, but we had a little incident out there --
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Off her look --
  EXPRESSION: Curious

::PATHS::
- CHOICE: "Move to the living room"
  TARGET: living_room_ed
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Living Room, House Interior
MOOD: Anticipatory, Mysterious
CHARACTERS: Narrator, Ed, Jerome
BACKGROUND_IMAGE: living_room.png
BACKGROUND_EDIT: "Inside a living room, later in the day"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Ed enters, carrying an ornate, hand-carved wooden case. He glances to Jerome, who is busy tinkering with a contrast adjustment on a monitor. The other monitors all reveal differen
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue monitoring"
  TARGET: end
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Control Room
MOOD: Tense, Focused
CHARACTERS: Ed, Jerome, Roger
BACKGROUND_IMAGE: control_room_monitors.png
BACKGROUND_EDIT: "Interior, various surveillance monitors, equipment, crosses being set up"

::SCRIPT::
- CHARACTER: Jerome
  LINE: Still gotta sync the EFD with the cellar and hallway cameras, then good to go -- this little sucker here is being a pain in the ass, though.
  EXPRESSION: Annoyed
- CHARACTER: Narrator
  LINE: Ed smirks. Sets his box on the coffee table. Begins unloading several velvet wrapped crosses, setting them upright.
  EXPRESSION: Smirking
- CHARACTER: Narrator
  LINE: Ed notices Roger crossing the foyer from the front door --
  EXPRESSION: null
- CHARACTER: Ed
  LINE: Find the oil leak?
  EXPRESSION: Curious
- CHARACTER: Roger
  LINE: Yeah.
  EXPRESSION: Neutral
- CHARACTER: Narrator
  LINE: Roger sees the crosses -- looks to Ed curiously.
  EXPRESSION: Curious
- CHARACTER: Roger
  LINE: That’s a lot of crosses.
  EXPRESSION: Surprised
- CHARACTER: Ed
  LINE: We want to stir things up.
  EXPRESSION: Determined
- CHARACTER: Narrator
  LINE: Ed takes one of the crosses and sets it up on the mantle above the fireplace.
  EXPRESSION: null
- CHARACTER: Ed
  LINE: The presence of religious icons usually brings on some kind of a reaction from anything unholy -- sort of pisses them off.
  EXPRESSION: Explaining
- CHARACTER: Narrator
  LINE: He sets another on top of the Grandfather clock.
  EXPRESSION: null
- CHARACTER: Roger
  LINE: Like holding a cross in front of a vampire?
  EXPRESSION: Joking
- CHARACTER: Ed
  LINE: Yeah, exactly, but I don’t believe in vampires.
  EXPRESSION: Amused
- CHARACTER: Narrator
  LINE: Roger’s amused, then leaves the room.
  EXPRESSION: Amused
- CHARACTER: Narrator
  LINE: Ed moves over to the coffee table where he sets another cross, then --
  EXPRESSION: null
- CHARACTER: Jerome
  LINE: ...Ed.
  EXPRESSION: Urgent
- CHARACTER: Narrator
  LINE: The tone in Jerome’s voice turns Ed immediately.
  EXPRESSION: Concerned
- CHARACTER: Jerome
  LINE: Check it out. Downstairs hallway.
  EXPRESSION: Alarmed
- CHARACTER: Narrator
  LINE: Ed looks to the monitor Jerome has his eyes glued on and see that although the hallway is empty, the cellar door is opening slowly.
  EXPRESSION: null

::PATHS::
- CHOICE: "Observe the cellar door"
  TARGET: control_room_right_after
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Control Room
MOOD: High Tension, Anticipation
CHARACTERS: Perrons, Jerome, Ed, Lorraine, Bruce
BACKGROUND_IMAGE: control_room_right_after.png
BACKGROUND_EDIT: "Room lit by monitors, tense faces, watching screen"

::SCRIPT::
- CHARACTER: Narrator
  LINE: All the Perrons surround Jerome at the monitors, watching Ed, Lorraine and Bruce entering the cellar, you can hear a pin drop. Ed flips on the light.
  EXPRESSION: null

::PATHS::
- CHOICE: "Follow them into the cellar"
  TARGET: cellar_stairway
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Cellar - Stairway
MOOD: Eerie, Suspenseful
CHARACTERS: Bruce, Ed, Lorraine
BACKGROUND_IMAGE: cellar_stairway.png
BACKGROUND_EDIT: "Steep, dark cellar steps, camera rolling, dim lighting"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Bruce follows Ed and Lorraine down the steep set of steps, camera is rolling. They get to the bottom.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Ed takes a moment, looking around the basement, glances to an EFD he’s holding in his hand, the needle is bouncing just between the 1 and the 2.
  EXPRESSION: Focused
- CHARACTER: Ed
  LINE: Something’s definitely here.
  EXPRESSION: Serious
- CHARACTER: Narrator
  LINE: Ed moves into the basement.
  EXPRESSION: null
- CHARACTER: Ed
  LINE: Okay -- you’ve got our attention.
  EXPRESSION: Calm
- CHARACTER: Narrator
  LINE: Silence.
  EXPRESSION: null
- CHARACTER: Ed
  LINE: Give us a sign you want to communicate with us.
  EXPRESSION: Challenging

::PATHS::
- CHOICE: "Wait for a sign"
  TARGET: cellar_basement_pov
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Cellar - Basement (Bruce's POV)
MOOD: Tense, Waiting
CHARACTERS: Bruce, Ed
BACKGROUND_IMAGE: cellar_basement.png
BACKGROUND_EDIT: "Basement room from camera POV, looking around, then at Ed"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Bruce’s pov, as he moves the camera about the room, not sure what he’s looking for. Settles on Ed.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Ed waits for a response. Stillness continues to fill the room.
  EXPRESSION: Waiting
- CHARACTER: Ed
  LINE: Close the door -- move the jars, something.
  EXPRESSION: Impatient
- CHARACTER: Narrator
  LINE: Resume.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Ed glances to his EFD, the needle is bouncing wildly.
  EXPRESSION: Alarmed
- CHARACTER: Narrator
  LINE: They wait. And wait some more.
  EXPRESSION: Tense

::PATHS::
- CHOICE: "Exit the cellar"
  TARGET: hallway_cellar_door
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Hallway - Cellar Door
MOOD: Disappointed, then Shocked
CHARACTERS: Carolyn, Roger, Jerome, Bruce, Lorraine, Ed
BACKGROUND_IMAGE: hallway_cellar_door.png
BACKGROUND_EDIT: "Hallway outside cellar, people gathered, dim lighting"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Carolyn, Roger and Jerome stand at the doorway as Bruce, Lorraine and Ed file out of the basement.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Ed looks to Carolyn, reading her disappointment.
  EXPRESSION: Observing
- CHARACTER: Ed
  LINE: Like I said, it doesn’t always happen when we want it to.
  EXPRESSION: Reassuring
- CHARACTER: Narrator
  LINE: As Ed turns to close the basement door -- WHAM! It SLAMS SHUT with a BANG right in his face.
  EXPRESSION: Surprised
- CHARACTER: Narrator
  LINE: Everyone instantly pivots. Bruce looks the most shocked. Carolyn shoots Roger a look, who’s not sure what to make out of it.
  EXPRESSION: Shocked

::PATHS::
- CHOICE: "Discuss what happened"
  TARGET: kitchen_night
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Kitchen
MOOD: Conversational, Skeptical, then Pensive
CHARACTERS: Bruce, Jerome, Lorraine
BACKGROUND_IMAGE: kitchen.png
BACKGROUND_EDIT: "Nighttime, 1:33 AM, homey kitchen, snacks"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The clock on the counter reads 1:33 AM.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Bruce enters. Sees Jerome take a Tuperware container of vegetables from the refrigerator.
  EXPRESSION: null
- CHARACTER: Jerome
  LINE: You hungry?
  EXPRESSION: Friendly
- CHARACTER: Bruce
  LINE: No -- still full.
  EXPRESSION: Neutral
- CHARACTER: Narrator
  LINE: Bruce moves over to the coffee pot.
  EXPRESSION: null
- CHARACTER: Jerome
  LINE: What do you suppose they did with the salt?
  EXPRESSION: Curious
- CHARACTER: Narrator
  LINE: Bruce sees a salt and pepper shaker next to the coffee pot on the counter.
  EXPRESSION: null
- CHARACTER: Bruce
  LINE: It’s over here.
  EXPRESSION: Helpful
- CHARACTER: Jerome
  LINE: Thanks.
  EXPRESSION: Grateful
- CHARACTER: Narrator
  LINE: Jerome begins to salt the veggies, heavily.
  EXPRESSION: null
- CHARACTER: Jerome
  LINE: So I’m curious, what do you think slammed the door closed like that?
  EXPRESSION: Curious
- CHARACTER: Narrator
  LINE: Bruce shrugs.
  EXPRESSION: Indifferent
- CHARACTER: Bruce
  LINE: Had to be a draft.
  EXPRESSION: Dismissive
- CHARACTER: Narrator
  LINE: Jerome seems slightly entertained. Takes a bite of celery.
  EXPRESSION: Amused
- CHARACTER: Jerome
  LINE: That’s funny, drafts never put that look you had on my face before.
  EXPRESSION: Teasing
- CHARACTER: Narrator
  LINE: Bruce glances back to him.
  EXPRESSION: null
- CHARACTER: Jerome
  LINE: That’s why I dig the machines, man. They don’t have emotions or beliefs that get in the way. They either pick something up, or they don’t. So, if you don’t believe, why are you doing this?
  EXPRESSION: Explaining
- CHARACTER: Bruce
  LINE: Got a baby coming -- fifty bucks a day, helps.
  EXPRESSION: Practical
- CHARACTER: Jerome
  LINE: So you think people just make this stuff up?
  EXPRESSION: Curious
- CHARACTER: Bruce
  LINE: I remember growing up with the Boogie Man in my closet, but when my parents checked -- they never found anything.
  EXPRESSION: Skeptical
- CHARACTER: Narrator
  LINE: Jerome smirks.
  EXPRESSION: Smirking
- CHARACTER: Jerome
  LINE: You know, just cause you can’t see it, doesn’t mean it’s not there. Have you ever lost anyone close?
  EXPRESSION: Philosophical
- CHARACTER: Bruce
  LINE: ...My dad, why?
  EXPRESSION: Curious
- CHARACTER: Jerome
  LINE: We should have Lorraine see if she can connect with him.
  EXPRESSION: Suggesting
- CHARACTER: Narrator
  LINE: Bruce can’t hold back his entertained smile.
  EXPRESSION: Amused
- CHARACTER: Bruce
  LINE: What part of “I don’t believe”, didn’t you understand?
  EXPRESSION: Teasing
- CHARACTER: Narrator
  LINE: Jerome takes another bite.
  EXPRESSION: null
- CHARACTER: Jerome
  LINE: What’re you afraid of man, getting busted for being narrow minded? Appease me -- tell me something without revealing what it is, that only you would know.
  EXPRESSION: Challenging
- CHARACTER: Narrator
  LINE: Bruce toys with the thought, then --
  EXPRESSION: Thinking
- CHARACTER: Bruce
  LINE: Okay, I put something in my dad’s casket that meant a lot to both of us.
  EXPRESSION: Revealing
- CHARACTER: Narrator
  LINE: Lorraine enters, Jerome lights up with a smile.
  EXPRESSION: null
- CHARACTER: Jerome
  LINE: You’re timing’s perfect.
  EXPRESSION: Happy
- CHARACTER: Lorraine
  LINE: Why’s that?
  EXPRESSION: Curious
- CHARACTER: Narrator
  LINE: Lorraine heads over to the refrigerator. Opens it.
  EXPRESSION: null
- CHARACTER: Jerome
  LINE: We’re conducting a little experiment. Officer Naysayer here put something in his dad’s casket -- can you tell him what it is?
  EXPRESSION: Excited
- CHARACTER: Narrator
  LINE: She grabs a Tab from a shelf, then looks to Bruce for his approval. He appears skeptical, but smiles anyway.
  EXPRESSION: null
- CHARACTER: Bruce
  LINE: Sure, why not.
  EXPRESSION: Agreeable
- CHARACTER: Narrator
  LINE: Lorraine walks over to him. Sets her soda on the counter.
  EXPRESSION: null
- CHARACTER: Lorraine
  LINE: Give me your hands.
  EXPRESSION: Instructing
- CHARACTER: Narrator
  LINE: She takes them, then closes her eyes. Bruce seems a little uncomfortable.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: After a long moment --
  EXPRESSION: null
- CHARACTER: Lorraine
  LINE: It’s a baseball -- has something written on it, all I can make out are a J and a R.
  EXPRESSION: Concentrating
- CHARACTER: Narrator
  LINE: Lorraine opens her eyes, releases Bruce’s hands.
  EXPRESSION: null
- CHARACTER: Jerome
  LINE: -- So?
  EXPRESSION: Impatient
- CHARACTER: Narrator
  LINE: He shrugs.
  EXPRESSION: Indifferent
- CHARACTER: Bruce
  LINE: -- That wasn’t it.
  EXPRESSION: Skeptical
- CHARACTER: Narrator
  LINE: She looks at him somewhat surprised, really?
  EXPRESSION: Surprised
- CHARACTER: Lorraine
  LINE: Oh well, must be tuning into something else then --
  EXPRESSION: Dismissive

::PATHS::
- CHOICE: "Conclude the experiment"
  TARGET: living_room_night
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Living Room
MOOD: Calm, Reassuring
CHARACTERS: Lorraine, Carolyn, Andrea, Cindy
BACKGROUND_IMAGE: living_room_night.png
BACKGROUND_EDIT: "Night, soft lighting, Carolyn and Lorraine watching sleeping children on monitors"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Lorraine is seated next to Carolyn in front of the monitors, who’s watching Andrea and Cindy curled asleep on Cindy’s bed.
  EXPRESSION: null
- CHARACTER: Carolyn
  LINE: I think you guys being here makes them feel safe.
  EXPRESSION: Grateful

::PATHS::
- CHOICE: "Wait for morning"
  TARGET: living_room_morning
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Living Room
MOOD: Exhausted, Unsettled
CHARACTERS: Ed, Lorraine, Bruce, Jerome
BACKGROUND_IMAGE: living_room_morning.png
BACKGROUND_EDIT: "Morning light, golden, several clocks, exhausted faces"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Shards of morning light pierce through the windows, warming up the room with golden light.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Angle, the Grandfather clock kicks past 5:15 to 5:16 am.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Widen, to reveal Ed, Lorraine, Bruce and Jerome, all keeping their eyes on different clocks. Not one of them have stopped.
  EXPRESSION: Observing
- CHARACTER: Ed
  LINE: Alright -- let’s call it.
  EXPRESSION: Resigned

::PATHS::
- CHOICE: "End day one"
  TARGET: perron_house_ext_day_two
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Perron House (Exterior)
MOOD: Quiet, Foreboding
CHARACTERS: Ed, Lorraine
BACKGROUND_IMAGE: perron_house_ext.png
BACKGROUND_EDIT: "Late afternoon, exterior of house, Perron's car is gone"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Ed and Lorraine drive up and park next to the house. The Perron’s station wagon is gone. They get out. Lorraine heads to the house. Ed heads to the barn.
  EXPRESSION: null

::PATHS::
- CHOICE: "Enter the house"
  TARGET: perron_house_front_door
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Perron House - Front Door
MOOD: Suspenseful, Uneasy
CHARACTERS: Lorraine, Carolyn
BACKGROUND_IMAGE: perron_front_door.png
BACKGROUND_EDIT: "Front door of house, open, dark interior, Carolyn visible in hall"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Lorraine knocks on the front door, but there’s no response. She waits a second longer, then decides to go in anyway. She opens the front door. Even though all the lights are all off, and it’s somewhat dark inside, she sees Carolyn, now wearing her hair down, coming up out of the CELLAR DOOR at the end of the hall, then walk into the kitchen, oblivious to Lorraine’s presence.
  EXPRESSION: null

::PATHS::
- CHOICE: "Confront Carolyn"
  TARGET: kitchen_carolyn_lorraine
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Kitchen
MOOD: Puzzling, Tense
CHARACTERS: Lorraine, Carolyn
BACKGROUND_IMAGE: kitchen.png
BACKGROUND_EDIT: "Kitchen interior, dark, Carolyn at counter with back to Lorraine"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Lorraine stands at the open door. Carolyn is at the counter with her back to her.
  EXPRESSION: null
- CHARACTER: Lorraine
  LINE: Carolyn --
  EXPRESSION: Concerned
- CHARACTER: Narrator
  LINE: Carolyn slowly turns to her -- it seems to take her a second to register it’s Lorraine.
  EXPRESSION: Confused
- CHARACTER: Carolyn
  LINE: -- You’re early.
  EXPRESSION: Neutral
- CHARACTER: Lorraine
  LINE: I can’t believe you went into the cellar.
  EXPRESSION: Shocked
- CHARACTER: Carolyn
  LINE: I wanted to get some soup going. Needed some beets.
  EXPRESSION: Simple
- CHARACTER: Narrator
  LINE: Lorraine finds it odd, but lets it go.
  EXPRESSION: Observing

::PATHS::
- CHOICE: "Continue to evening"
  TARGET: perron_station_wagon
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Perron Station Wagon - Perron Driveway
MOOD: Return, Ominous
CHARACTERS: Roger, girls
BACKGROUND_IMAGE: perron_station_wagon.png
BACKGROUND_EDIT: "Night, Roger driving up driveway, headlights illuminating Warren's car"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Roger drives up to the house, has the girls with him. His headlights drag over the Warren’s parked car.
  EXPRESSION: null

::PATHS::
- CHOICE: "Park the car"
  TARGET: end
  STATE_CHANGE: null
  CONDITION: null

```markdown
::SCENE::
LOCATION: Barn
MOOD: Calm
CHARACTERS: Narrator, Roger, Ed
BACKGROUND_IMAGE: barn_interior.png
BACKGROUND_EDIT: "Right after arrival, Ed working on a pickup truck, tools and grease visible, dim lighting"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Roger walks in to find Ed working on the pickup. The front’s been jacked back up. There are two pieces of firewood lodged under the front axle for extra stability. He’s up to his elbows in grease as he packs the bearings.
  EXPRESSION: null
- CHARACTER: Ed
  LINE: I noticed you didn’t finish the bearings. Hope you don’t mind -- just looking for something to do.
  EXPRESSION: null
- CHARACTER: Roger
  LINE: Not at all.
  EXPRESSION: null
- CHARACTER: Ed
  LINE: Got anymore more grease?
  EXPRESSION: null
- CHARACTER: Roger
  LINE: Yeah.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Roger walks over to the work bench. Opens a cabinet above it and grabs a can from a shelf. Pops it open as he heads over to Ed and hands it to him.
  EXPRESSION: null
- CHARACTER: Ed
  LINE: Thanks.
  EXPRESSION: Happy
- CHARACTER: Narrator
  LINE: Roger grabs a nearby wooden crate. Takes a seat on it. Watches Ed work.
  EXPRESSION: null
- CHARACTER: Roger
  LINE: Carolyn told me you going to be a priest --
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Ed ponders for a moment -- does he want to share this?
  EXPRESSION: null
- CHARACTER: Ed
  LINE: That was the plan -- but when I got to my Ordination, I started having my doubts, and realized I wasn’t going to be good enough, I don’t have the strength they need. So I gave it up.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Roger takes a beat.
  EXPRESSION: null
- CHARACTER: Roger
  LINE: I could scratch my head ‘til I’m bald and never figure out why you do what you do --
  EXPRESSION: Angry
- CHARACTER: Ed
  LINE: Remember as a kid being afraid to hang your hand off the edge of your bed because you thought something underneath was going to grab it?
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Roger nods somewhat skeptically.
  EXPRESSION: null
- CHARACTER: Ed
  LINE: Well -- mine got grabbed.
  EXPRESSION: Afraid
- CHARACTER: Narrator
  LINE: As Ed throws more grease on the bearings --
  EXPRESSION: null
- CHARACTER: Ed
  LINE: Something yanked me to the floor. It was too dark to see under the bed, but I ran my ass out of that room as fast as I could. My dad didn’t believe me, so he dragged me back in there and told me I had to face my fears. I buried myself under the covers, scared to death cause I could still hear it under my bed. Then I remembered what a nun had told me in catechism, “God will be there for all who need. He is your protector.” So I grabbed my Davy Crockett knife from my nightstand and got off the bed and told whatever was under there that God was going to kick its ass if it didn’t leave. I just kept saying it over and over - - and it finally went away. Never came back.
  EXPRESSION: Afraid
- CHARACTER: Narrator
  LINE: Ed looks back to Roger.
  EXPRESSION: null
- CHARACTER: Ed
  LINE: It was the best thing my dad ever did for me. I put my faith in God every day after that, and have been checking under beds ever since.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Ed finishes packing the bearings. Caps it.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: They hear the crunch of gravel under car tires. Roger looks out the barn to see Jerome and Bruce pulling up in Jerome’s van.
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue to the house"
  TARGET: kitchen
  STATE_CHANGE: apprehension = +1
  CONDITION: null

::SCENE::
LOCATION: Kitchen
MOOD: Eerie
CHARACTERS: Narrator, Bruce
BACKGROUND_IMAGE: kitchen_interior.png
BACKGROUND_EDIT: "Later, 3:10 AM, dim lighting, coffee pot on counter"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Bruce enters, carrying a coffee mug. Yawns. A CLOCK ON THE COUNTER reads: 3:10 AM. He sets the mug on the counter next to a coffee pot, pours himself another cup.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Goes to the fridge, and takes out a milk carton from the top shelf, closes the door.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Sets it next to his coffee cup on the counter, then turns to a shelf above the sink for the sugar. As he’s reaching for it A LOUD BANG echoes as the fridge door is SLAMMED SHUT.
  EXPRESSION: Surprised
- CHARACTER: Narrator
  LINE: Bruce spins, looks to it, startled and confused as he’s the only one in the kitchen, then he sees that the milk carton is no longer next to his coffee cup.
  EXPRESSION: Surprised
- CHARACTER: Narrator
  LINE: A DRIPPING NOISE draws his attention back to the fridge, where milk is now seeping out of it onto the floor.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Bruce slowly moves over to it. Hesitates a beat, then opens the fridge. The milk carton is back on the top shelf, but it’s been SMASHED completely flat, its contents spilling down the interior.
  EXPRESSION: Surprised

::PATHS::
- CHOICE: "Report the incident"
  TARGET: living_room
  STATE_CHANGE: fear = +2, confusion = +1
  CONDITION: null

::SCENE::
LOCATION: Living Room
MOOD: Tense
CHARACTERS: Narrator, Bruce, Ed, Lorraine, Carolyn, Roger, Jerome
BACKGROUND_IMAGE: living_room_interior.png
BACKGROUND_EDIT: "Right after the kitchen incident, characters gathered, Jerome looking at monitors"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Bruce enters. Looks to Ed, Lorraine, Carolyn and Roger, who are seated on the sofas, his demeanor, as well as the look on his face, drawing their attention, Jerome looks over from the monitors.
  EXPRESSION: null
- CHARACTER: Bruce
  LINE: There’s a -- um, something going on in the kitchen. The milk carton moved.
  EXPRESSION: Afraid

::PATHS::
- CHOICE: "Investigate the kitchen"
  TARGET: perron_house_kitchen
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Perron House Kitchen
MOOD: Frustrating
CHARACTERS: Narrator, Bruce, Lorraine, Ed, Jerome
BACKGROUND_IMAGE: perron_house_kitchen.png
BACKGROUND_EDIT: "Right after reporting, kitchen appears normal, no spilled milk"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Bruce follows Lorraine, Ed and Jerome into the kitchen. Looks to the fridge, no milk is dripping. In fact, there’s not even any milk on the floor.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Bruce whips a glance to the counter, and there sitting next to Bruce’s coffee mug, is the carton of milk, right where he set it the first time.
  EXPRESSION: null
- CHARACTER: Bruce
  LINE: I swear, the carton wasn’t there, it was back in the fridge, and smashed, milk was everywhere.
  EXPRESSION: Angry
- CHARACTER: Jerome
  LINE: Probably just a draft -- I love moments like this.
  EXPRESSION: null
- CHARACTER: Bruce
  LINE: Alright, I get it.
  EXPRESSION: Angry
- CHARACTER: Narrator
  LINE: As Lorraine follows Ed and Jerome out of the kitchen, Bruce lays a gentle hand on her shoulder, stopping her.
  EXPRESSION: null
- CHARACTER: Bruce
  LINE: Can I talk to you for a sec?
  EXPRESSION: null
- CHARACTER: Lorraine
  LINE: Sure.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The others continue out. Bruce takes a beat, then --
  EXPRESSION: null
- CHARACTER: Bruce
  LINE: You were right earlier about the baseball. The J and R were for Jackie Robinson. When I was ten, my dad took me to the World Series, Yankees and Dodgers -- two dollar seats, left field. Jackie Robinson hit the winning home run, and my dad caught it -- handed it right to me -- best day of my life.
  EXPRESSION: null

::PATHS::
- CHOICE: "Proceed to the hallway"
  TARGET: hallway
  STATE_CHANGE: trust_lorraine = +1
  CONDITION: null

::SCENE::
LOCATION: Hallway
MOOD: Alarming
CHARACTERS: Narrator
BACKGROUND_IMAGE: hallway.png
BACKGROUND_EDIT: "Same time, close up on EMF meter, dark hallway"

::SCRIPT::
- CHARACTER: Narrator
  LINE: CU on the EFD METER on the camera tripod in the hallway. The needle begins to bounce past 1.7 Megahertz then SLAMS to the outer edge of the range to 10.
  EXPRESSION: Surprised
- CHARACTER: Narrator
  LINE: The camera begins to FLASH repeatedly, the CLICK CLICK CLICK sound of the motor drive blending with the popping of the FLASH.
  EXPRESSION: Surprised

::PATHS::
- CHOICE: "React to the flashes"
  TARGET: kitchen_same
  STATE_CHANGE: fear = +3
  CONDITION: null

::SCENE::
LOCATION: Kitchen
MOOD: Urgent
CHARACTERS: Narrator, Lorraine, Bruce
BACKGROUND_IMAGE: kitchen_interior.png
BACKGROUND_EDIT: "Same time, flashes visible from hallway, Lorraine and Bruce startled"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The SUDDEN FLASHES from the hallway pulls Lorraine and Bruce’s attention back out the kitchen door.
  EXPRESSION: Surprised
- CHARACTER: Narrator
  LINE: Lorraine quickly moves out into the hallway to see --
  EXPRESSION: null

::PATHS::
- CHOICE: "Go into the hallway"
  TARGET: downstairs_hallway
  STATE_CHANGE: urgency = +1
  CONDITION: null

::SCENE::
LOCATION: Downstairs Hallway
MOOD: Intense
CHARACTERS: Narrator, Ed, Jerome
BACKGROUND_IMAGE: downstairs_hallway.png
BACKGROUND_EDIT: "Continuous, camera flashing, Ed and Jerome observing"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Another FLASH popping from the camera set up in the hall. Ed and Jerome, who have stopped at the bottom of the stairs, have their eyes glued on it as well.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: A second later, the CAMERA positioned at the top of the stairs starts flashing.
  EXPRESSION: Surprised
- CHARACTER: Ed
  LINE: It’s moving upstairs.
  EXPRESSION: Surprised
- CHARACTER: Narrator
  LINE: Ed moves quickly into the --
  EXPRESSION: null

::PATHS::
- CHOICE: "Follow the activity upstairs"
  TARGET: living_room_continuous
  STATE_CHANGE: urgency = +1
  CONDITION: null

::SCENE::
LOCATION: Living Room
MOOD: Panicked
CHARACTERS: Narrator, Ed, Carolyn, Roger, Lorraine, Bruce, Jerome
BACKGROUND_IMAGE: living_room_interior.png
BACKGROUND_EDIT: "Continuous, characters watching monitor, dark hallway strobing"

::SCRIPT::
- CHARACTER: Narrator
  LINE: -- where he joins Carolyn and Roger, who have their eyes glued the MONITOR as the camera keeps strobing through the dark hallway. Lorraine, Bruce and Jerome come up right behind him --
  EXPRESSION: null
- CHARACTER: Carolyn
  LINE: Oh my God.
  EXPRESSION: Afraid
- CHARACTER: Narrator
  LINE: They look to the monitor showing Cindy’s room. As she and Andrea sleep peacefully, THEIR BREATHS are FREEZING ON EXHALE.
  EXPRESSION: null
- CHARACTER: Jerome
  LINE: That’s gotta be one of the fastest temp drops I’ve ever seen.
  EXPRESSION: Surprised

::PATHS::
- CHOICE: "Check on the children"
  TARGET: cindys_room
  STATE_CHANGE: fear = +2, urgency = +1
  CONDITION: null

::SCENE::
LOCATION: Cindy’s Room
MOOD: Terror
CHARACTERS: Narrator, Cindy, Andrea, Roger
BACKGROUND_IMAGE: cindys_room.png
BACKGROUND_EDIT: "Same time, dark room, camera flashing from closet, girls sleeping"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The CAMERA IN THE CLOSET starts FLASHING, strobing the room with bursting with white light. The girls start to stir.
  EXPRESSION: Surprised
- CHARACTER: Narrator
  LINE: It’s really hard for Roger to stay still.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Cindy’s eyes pop open, she sits up. Freaks as the intermittent light gives her staccato glances of something staring in at her through the window, it’s the beast she saw before as a shadow. She SCREAMS!
  EXPRESSION: Afraid
- CHARACTER: Narrator
  LINE: Andrea bolts upright in fear, then --
  EXPRESSION: Afraid
- CHARACTER: Narrator
  LINE: THE LOUD, ECHOING SOUND OF A SLIDE-BOLT CLOSING OVER AND OVER, joins the mayhem, it’s coming from the closet.
  EXPRESSION: Afraid
- CHARACTER: Narrator
  LINE: Roger can’t stand it, takes off out of the room.
  EXPRESSION: Afraid
- CHARACTER: Narrator
  LINE: The SLIDE BOLT NOISE suddenly stops, along with the FLASHES, casting the room back into darkness.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The girls dash out the bedroom door into the hallway just as Roger gets there, both folding into his arms.
  EXPRESSION: Afraid
- CHARACTER: Narrator
  LINE: The CAMERA at the end of the hallway STROBES A FLASH, the girls scream again, fearful of what they can’t see.
  EXPRESSION: Afraid

::PATHS::
- CHOICE: "Go to the stairs"
  TARGET: house_stairs
  STATE_CHANGE: fear = +4, panic = +1
  CONDITION: null

::SCENE::
LOCATION: House Stairs
MOOD: Urgent
CHARACTERS: Narrator, Ed
BACKGROUND_IMAGE: house_stairs.png
BACKGROUND_EDIT: "Same time, Ed heading up stairs, camera flashes"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Ed is heading up as the camera at the top, pops off another FLASH. A second later the CAMERA in the downstairs hallway FLASHES, drawing Ed’s attention back down the stairs.
  EXPRESSION: Surprised
- CHARACTER: Narrator
  LINE: He waits for more f
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue to observe"
  TARGET: end_of_excerpt
  STATE_CHANGE: null
  CONDITION: null
```

::SCENE::
LOCATION: Living Room
MOOD: Tense
CHARACTERS: Narrator, Lorraine, Ed
BACKGROUND_IMAGE: living_room.png
BACKGROUND_EDIT: "Nighttime, tense atmosphere, focused on action"

::SCRIPT::
- CHARACTER: Narrator
  LINE: lashes, but nothing happens. Lorraine steps out of the living room and looks up to him.
  EXPRESSION: null
- CHARACTER: Ed
  LINE: Whatever it is, it came back down.
  EXPRESSION: Concerned

::SCENE::
LOCATION: Master Bedroom
MOOD: Comforting
CHARACTERS: Narrator, Roger, Andrea, Carolyn, Cindy
BACKGROUND_IMAGE: master_bedroom.png
BACKGROUND_EDIT: "Nighttime, subdued lighting, children sleeping"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Roger is holding Andrea in his arms, sitting on the edge of the bed, while Carolyn is latched onto Cindy, cuddled on the other side. He looks to her.
  EXPRESSION: null
- CHARACTER: Roger
  LINE: Hey --
  EXPRESSION: Hesitant
- CHARACTER: Narrator
  LINE: Her eyes meet his. He tries to say something, but can’t find the words.
  EXPRESSION: null
- CHARACTER: Carolyn
  LINE: -- It’s okay.
  EXPRESSION: Comforting

::SCENE::
LOCATION: Cindy's Room - Closet
MOOD: Investigative
CHARACTERS: Narrator, Bruce, Jerome, Ed, Lorraine, Roger
BACKGROUND_IMAGE: cindys_room_closet.png
BACKGROUND_EDIT: "Nighttime, interior closet, tools for investigation"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Bruce is filming Jerome, who is holding an EFD out front of him as he slowly moves about the closet. He pushes clothing aside to get closer to the wall behind. Ed is at the entrance, unloading film from the camera on the tripod. Lorraine watches.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Jerome pulls the EFD away from the wall.
  EXPRESSION: null
- CHARACTER: Jerome
  LINE: I’m not getting anything.
  EXPRESSION: Disappointed
- CHARACTER: Narrator
  LINE: Roger joins the group.
  EXPRESSION: null
- CHARACTER: Lorraine
  LINE: How are the girls?
  EXPRESSION: Concerned
- CHARACTER: Roger
  LINE: Better.
  EXPRESSION: Relieved
- CHARACTER: Narrator
  LINE: Ed looks to Roger.
  EXPRESSION: null
- CHARACTER: Ed
  LINE: They said that bolting noise definitely came from in here?
  EXPRESSION: Questioning
- CHARACTER: Roger
  LINE: -- Yeah.
  EXPRESSION: Affirming
- CHARACTER: Ed
  LINE: Is there anything behind this wall?
  EXPRESSION: Curious
- CHARACTER: Narrator
  LINE: Ed knuckle taps the panel.
  EXPRESSION: null
- CHARACTER: Roger
  LINE: No idea.
  EXPRESSION: Unsure
- CHARACTER: Ed
  LINE: Do you mind if we take a look?
  EXPRESSION: Asking
- CHARACTER: Roger
  LINE: I don’t care what the hell you do to it.
  EXPRESSION: Frustrated

::SCENE::
LOCATION: Cindy's Room - Closet
MOOD: Discovery
CHARACTERS: Narrator, Ed, Lorraine, Roger
BACKGROUND_IMAGE: closet_trapdoor.png
BACKGROUND_EDIT: "Nighttime, interior closet, revealed trapdoor"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Tight on a section of wood paneling being pried back off the wall with a hammer. Widen to see Ed sliding the hammer up and down along a panel’s seam to loosen it. He finally pulls it back off the wall.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Lorraine is the first to see. A SMALL 2’ x 2’ TRAP DOOR framed within another wall that latches from the outside via a SLIDE BOLT. A WOMAN’S VERY OBESE HAND, fingers like sausages, aggressively SLAMS it CLOSED, then SLIDES A LATCH across to lock it.
  EXPRESSION: Surprised
- CHARACTER: Narrator
  LINE: Resume. Lorraine and the others are looking at the trap door. Ed kneels down. Undoes the latch. Slowly opens the door. It’s too dark to see anything beyond.
  EXPRESSION: null
- CHARACTER: Ed
  LINE: Can someone get me a flashlight --
  EXPRESSION: Requesting
- CHARACTER: Roger
  LINE: Yeah, there’s one in our room.
  EXPRESSION: Helpful
- CHARACTER: Narrator
  LINE: Roger disappears for a moment. Lorraine puts her hand on Ed’s shoulder.
  EXPRESSION: null
- CHARACTER: Lorraine
  LINE: Let me go in.
  EXPRESSION: Determined
- CHARACTER: Narrator
  LINE: Lorraine gets on her hands and knees as Roger comes back with a small flashlight. Hands it to her. She thumbs the switch. Shines it into the open door, the light stretches into what looks like a narrow crawl space framed in wood. Lorraine slips half her body inside, keeping the light shining ahead.
  EXPRESSION: null

::SCENE::
LOCATION: Crawl Space
MOOD: Eerie
CHARACTERS: Narrator, Lorraine, Ghost Children
BACKGROUND_IMAGE: crawl_space.png
BACKGROUND_EDIT: "Dark, narrow crawl space, flashlight beam"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Lorraine can barely make it out, but sees that the crawl space seems to open up.
  EXPRESSION: null
- CHARACTER: Lorraine
  LINE: Looks like there’s some sort of room.
  EXPRESSION: Curious
- CHARACTER: Narrator
  LINE: Her flashlight suddenly dies, casting her into total darkness. She palms it a couple of times, gets the beam to shine again.
  EXPRESSION: Startled
- CHARACTER: Narrator
  LINE: As she points the light down the crawl-space ahead A YOUNG BOY AND GIRL, full of angst and panic, scramble toward Lorraine, PASSING RIGHT THROUGH her body, it’s the two she saw in the photograph earlier.
  EXPRESSION: Terrified
- CHARACTER: Narrator
  LINE: Resume. Lorraine is slightly startled, but continues into the room ahead.
  EXPRESSION: Determined

::SCENE::
LOCATION: Hidden Room
MOOD: Horrific
CHARACTERS: Narrator, Lorraine, Bathsheba
BACKGROUND_IMAGE: hidden_room.png
BACKGROUND_EDIT: "Dark, dusty, cobweb-filled hidden room, crayon writing"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Lorraine slowly stands, her flashlight quartering the darkness. Cobwebs everywhere reflect off the light. It falls upon a makeshift bed with an old, dust covered blanket, which has SLINKY TOY sitting on it. Lorraine picks it up, sees a wooden box next to the bed with other toys in it.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: She lets her light wander, discovering that every wall is completely covered with THE SAME PHRASE scrawled in crayon, over and over. She moves closer. Sees what it says; I’M SORRY MOMMY. I’M SORRY MOMMY. I’M SORRY MOMMY. I’M SORRY MOMMY.
  EXPRESSION: Disturbed
- CHARACTER: Narrator
  LINE: Lorraine stops, senses something. She slowly moves the light off the wall and angles it to her forearm, IT’S COVERED IN GOOSEBUMPS. And for a second, her heart skips a beat, there’s something else she sees, the light cascading past her forearm down to the floor illuminates BATHSHEBA’S DIRTY, CRUSTED BARE FEET, straddling her own from behind.
  EXPRESSION: Terrified
- CHARACTER: Narrator
  LINE: Before Lorraine can turn around she is aggressively shoved into the wall. The movement jars the flashlight and slinky from her grasp and drops to the floor.
  EXPRESSION: Attacked

::SCENE::
LOCATION: Closet
MOOD: Urgent
CHARACTERS: Narrator, Ed
BACKGROUND_IMAGE: closet_dark.png
BACKGROUND_EDIT: "Dark closet entrance, urgent mood"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Ed reacts the noise and immediately heads into the crawl space.
  EXPRESSION: Concerned
- CHARACTER: Ed
  LINE: Lorraine--?
  EXPRESSION: Worried

::SCENE::
LOCATION: Small Room
MOOD: Profoundly Disturbed
CHARACTERS: Narrator, Lorraine, Ed
BACKGROUND_IMAGE: small_room_encounter.png
BACKGROUND_EDIT: "Dark, small room, Ed crawling in, Lorraine shaken"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Lorraine is reaching for the flashlight on the floor just as Ed crawls in.
  EXPRESSION: null
- CHARACTER: Lorraine
  LINE: I’m alright. (beat) It was her, Ed.
  EXPRESSION: Shaken
- CHARACTER: Narrator
  LINE: She looks hard to him, definitely impacted.
  EXPRESSION: null
- CHARACTER: Lorraine
  LINE: I’ve never felt anything so dark. (beat) We have to get her out of this house --
  EXPRESSION: Determined

::SCENE::
LOCATION: Closet
MOOD: Purposeful
CHARACTERS: Narrator, Ed, Lorraine, Jerome
BACKGROUND_IMAGE: closet_aftermath.png
BACKGROUND_EDIT: "Interior closet, daylight, collecting equipment"

::SCRIPT::
- CHARACTER: Narrator
  LINE: As Ed and Lorraine come out, Ed looks to Jerome, direct.
  EXPRESSION: null
- CHARACTER: Ed
  LINE: Grab the cameras -- I want to see what we got.
  EXPRESSION: Instructing

::SCENE::
LOCATION: Downstairs Bathroom
MOOD: Technical
CHARACTERS: Narrator, Ed, Jerome
BACKGROUND_IMAGE: bathroom_darkroom.png
BACKGROUND_EDIT: "Interior bathroom converted to darkroom, red light"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Ed and Jerome’s movements are fast and precise as they are busy converting the bathroom into a small darkroom; a photo enlarger is on the counter with three solution trays lined up next to it. A small rope has been strung up along a shower rod. As Jerome pours developer into one of the trays, Ed finishes screwing in a light bulb and flips the wall switch, washing the room deep in crimson.
  EXPRESSION: null

::SCENE::
LOCATION: Living Room
MOOD: Unsettling
CHARACTERS: Narrator, Lorraine, Roger, Andrea, Carolyn, Cindy, Bruce
BACKGROUND_IMAGE: living_room_monitors.png
BACKGROUND_EDIT: "Nighttime, Lorraine watching monitors, outside view"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Lorraine is sitting before the monitors, her eyes on the one revealing the master bedroom, where Roger is cuddling Andrea on the bed, who is sound asleep. Carolyn is next to him, doing the same with Cindy, who is also asleep.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Chirping crickets and croaking frogs drift in through an open window next to her. A loud THUD pulls her attention outside to where she sees something flopping on the ground by the barn, dust rising as if there were some sort of struggle.
  EXPRESSION: Startled
- CHARACTER: Narrator
  LINE: Bruce walks into the room carrying a cup of steaming coffee.
  EXPRESSION: null
- CHARACTER: Lorraine
  LINE: Keep your eyes on the monitors for me, will you. I’ll be right back.
  EXPRESSION: Concerned
- CHARACTER: Narrator
  LINE: Lorraine heads out of the room.
  EXPRESSION: null

::SCENE::
LOCATION: Perron House Exterior
MOOD: Foreboding
CHARACTERS: Narrator, Lorraine
BACKGROUND_IMAGE: perron_house_exterior.png
BACKGROUND_EDIT: "Nighttime, outside barn, ominous sounds"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Lorraine moves toward the flopping movement, which seems to be slowing with each step she takes. As she gets to it, the flopping stops. Sees it’s an enormous barn owl, neck broken, eyes wide open. Dead.
  EXPRESSION: Saddened
- CHARACTER: Narrator
  LINE: A compassionate look sweeps over Lorraine’s face, until she hears A DISTANT BLEND OF VOICES; pained, fearful, full of anxiety. She follows them to the back of the barn, where through a thick wall of trees and shrubs, she can barely make out an old, beaten pathway that threads through.
  EXPRESSION: Concerned
- CHARACTER: Narrator
  LINE: She heads in.
  EXPRESSION: Determined

::SCENE::
LOCATION: Growth
MOOD: Ominous
CHARACTERS: Narrator, Lorraine, Ghost Voices
BACKGROUND_IMAGE: overgrown_pathway.png
BACKGROUND_EDIT: "Nighttime, dense overgrown pathway, creepy sounds"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The VOICES begin to grow in volume as Lorraine walks deeper into the growth, fighting her way through overgrown branches, following what’s left of the pathway.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: She comes out into a small clearing to see where the voices are coming from.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Before her, surrounded by a crumbling stone wall and completely overgrown with weeds, is an OLD CEMETERY with maybe forty tombstones within; some broken, some toppled, some incredibly worn. The voices seem to be coming from somewhere on the other side.
  EXPRESSION: Uneasy
- CHARACTER: Narrator
  LINE: She moves into it. A wind begins to tumble pieces of foliage across the ground, then one tombstone catches her attention -- the name reads: Bathsheba Sherman. She moves up to it as the voices get louder and louder, it’s almost deafening, then THE VOICES INSTANTLY STOP, and things fall into an awful silence.
  EXPRESSION: Terrified
- CHARACTER: Narrator
  LINE: It becomes unnerving as Lorraine senses something, a presence, very close.
  EXPRESSION: Afraid
- CHARACTER: Narrator
  LINE: She scans the surrounding trees, but everything beyond is swallowed in the shadows of the night, she keeps staring, knowing something is just beyond.
  EXPRESSION: Alert
- CHARACTER: Narrator
  LINE: After a moment Lorraine turns around to Bathsheba Sherma
  EXPRESSION: Startled

::SCENE::
LOCATION: Cemetery (or Woods, near grave)
MOOD: Horror, Panic
CHARACTERS: Lorraine, Narrator, Judy (vision)
BACKGROUND_IMAGE: overgrown_grave.png
BACKGROUND_EDIT: "Daytime, leaves blowing, child's hand protruding from dirt"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Sees something protruding slightly from the ground before it, it’s a child’s hand, half covered with dirt and leaves; the skin is white, nails chipped, full of grime. More leaves blow away, revealing more of a body barely buried.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Lorraine inches closer, it’s a young girl, matted hair clings to the porcelain white skin on the side of her face. The head is turned sideways. As Lorraine moves around to get a better view --
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: She looks to the little girl’s face, blanches, it’s her daughter, Judy.
  EXPRESSION: Panicked
- CHARACTER: Narrator
  LINE: Then, the exposed white skin begins to grey, and continues to darken and becomes ash-like, the breeze blowing every part of her away.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Panic invades Lorraine’s body as a slow realization overwhelms her. She takes off running back the way she came.
  EXPRESSION: Panicked

::PATHS::
- CHOICE: "Run back to the house"
  TARGET: woods_pathway
  STATE_CHANGE: fear = +3, panic = true
  CONDITION: null

::SCENE::
LOCATION: Woods - Pathway
MOOD: Frantic, desperate
CHARACTERS: Lorraine, Narrator
BACKGROUND_IMAGE: woods_pathway_night.png
BACKGROUND_EDIT: "Nighttime, trees clawing at clothes, Lorraine sprinting"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Trees branches claw at Lorraine’s clothes as she retraces her steps on a wild scramble to get back. She can see the barn up head. She blows out the overgrowth and continues her sprint past the barn and to the house, barely slows to whip open the front door.
  EXPRESSION: null

::PATHS::
- CHOICE: "Enter the house"
  TARGET: house_foyer
  STATE_CHANGE: energy = -1, panic = true
  CONDITION: null

::SCENE::
LOCATION: House - Foyer
MOOD: Confused, urgent
CHARACTERS: Lorraine, Bruce, Narrator
BACKGROUND_IMAGE: house_foyer_night.png
BACKGROUND_EDIT: "Nighttime interior, Lorraine dashing, Bruce looking confused from living room"

::SCRIPT::
- CHARACTER: Narrator
  LINE: As Lorraine dashes into the house and heads to the kitchen, Bruce looks at her from the living room, confused by her frenzy of motion.
  EXPRESSION: null

::PATHS::
- CHOICE: "Go to the kitchen"
  TARGET: house_kitchen_call
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: House - Kitchen
MOOD: Panicked, anxious, then relieved, then troubled
CHARACTERS: Lorraine, Ed, Mom (O.C.), Roger (O.C.), Andrea (O.C.), Narrator
BACKGROUND_IMAGE: house_kitchen_night.png
BACKGROUND_EDIT: "Nighttime interior, Lorraine out of breath, dialing phone, Ed enters"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Lorraine comes running into the kitchen. She’s out of breath. Immediately goes to the phone on the wall. Quickly dials. Ed walks in, curious to what’s going on. He’s about to say something when she raises her hand to give her a second.
  EXPRESSION: null
- CHARACTER: Lorraine
  LINE: Mom, it’s Lorraine. Is Judy okay?
  EXPRESSION: Anxious
- CHARACTER: Lorraine
  LINE: Can you go check on her, please.
  EXPRESSION: Anxious
- CHARACTER: Lorraine
  LINE: Damnit! Just check -- please.
  EXPRESSION: Irritated
- CHARACTER: Narrator
  LINE: Lorraine looks to Ed, tears in her eyes. Keeps the phone to her ear.
  EXPRESSION: null
- CHARACTER: Ed
  LINE: Are you going to tell me what’s going on?
  EXPRESSION: Concerned
- CHARACTER: Lorraine
  LINE: It was Judy.
  EXPRESSION: Distraught
- CHARACTER: Ed
  LINE: What do you mean?
  EXPRESSION: Confused
- CHARACTER: Lorraine
  LINE: I saw her, out there -- she was dead --
  EXPRESSION: Panicked
- CHARACTER: Narrator
  LINE: A VOICE comes back on the phone. Lorraine breathes a sigh of relief.
  EXPRESSION: null
- CHARACTER: Lorraine
  LINE: Thank you -- I didn’t mean to scare you like that.
  EXPRESSION: Relieved
- CHARACTER: Lorraine
  LINE: I’ll explain later, okay. Goodnight.
  EXPRESSION: Calmer
- CHARACTER: Narrator
  LINE: Lorraine slowly hangs up.
  EXPRESSION: null
- CHARACTER: Ed
  LINE: What the hell happened to you?
  EXPRESSION: Concerned
- CHARACTER: Narrator
  LINE: Lorraine looks to him, troubled. Tears cascading.
  EXPRESSION: null
- CHARACTER: Lorraine
  LINE: I saw Judy dead in a cemetery. It was some kind of warning, I know it. There are spirits trapped there, I could hear them. She’s dominating both worlds.
  EXPRESSION: Troubled
- CHARACTER: Ed
  LINE: You’ve got to stop.
  EXPRESSION: Stern
- CHARACTER: Lorraine
  LINE: Stop what?
  EXPRESSION: Annoyed
- CHARACTER: Narrator
  LINE: He takes her by the shoulders.
  EXPRESSION: null
- CHARACTER: Ed
  LINE: This -- you know better. I warned you.
  EXPRESSION: Stern
- CHARACTER: Lorraine
  LINE: I thought something had happened to her.
  EXPRESSION: Upset
- CHARACTER: Ed
  LINE: C’mere...
  EXPRESSION: Gentle
- CHARACTER: Narrator
  LINE: He pulls her into an embrace, gentle, sympathetic. Whispers --
  EXPRESSION: null
- CHARACTER: Ed
  LINE: You just can’t give this thing any more strength than it already has.
  EXPRESSION: Sympathetic
- CHARACTER: Narrator
  LINE: Lorraine takes a beat, the realization setting in. She gives the slightest of nods, knowing he’s right.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Roger pokes his head into the kitchen, Andrea, who’s half asleep, is in his arms.
  EXPRESSION: null
- CHARACTER: Roger
  LINE: You okay?
  EXPRESSION: Concerned
- CHARACTER: Narrator
  LINE: Ed looks to Lorraine, then addresses Roger --
  EXPRESSION: null
- CHARACTER: Ed
  LINE: Yeah.
  EXPRESSION: Calm
- CHARACTER: Ed
  LINE: You?
  EXPRESSION: Concerned
- CHARACTER: Roger
  LINE: She woke up and was a little scared --
  EXPRESSION: Worried

::PATHS::
- CHOICE: "Continue investigating"
  TARGET: bathroom_photos
  STATE_CHANGE: fear = +1
  CONDITION: null

::SCENE::
LOCATION: Bathroom
MOOD: Mysterious, focused, building tension
CHARACTERS: Ed, Jerome, Narrator
BACKGROUND_IMAGE: darkroom.png
BACKGROUND_EDIT: "Later, darkroom setting, photo developing trays with liquid"

::SCRIPT::
- CHARACTER: Narrator
  LINE: CU on a pair of tongs holding onto a sheet of photo paper as it’s dipped in a tray of developer. As a photo begins to emerge of the stairway.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Widen to see Ed holding the tongs. Jerome’s busy taking an already developed photo out of the wash tray, and clipping it onto a small rope tied to the shower rod.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Both are focused.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Something in Ed’s picture draws his attention in for a closer look A FIGURE begins to materialize on the staircase.
  EXPRESSION: null

::PATHS::
- CHOICE: "Show the photo to others"
  TARGET: living_room_reveal
  STATE_CHANGE: fear = +2
  CONDITION: null

::SCENE::
LOCATION: Living Room
MOOD: Urgent, mysterious
CHARACTERS: Ed, Andrea (asleep), Roger, Lorraine, Bruce (asleep), Narrator
BACKGROUND_IMAGE: house_living_room_night.png
BACKGROUND_EDIT: "Right after, Ed hurries in, people on sofa and chair, dimly lit"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Ed hurries in. Sees that Andrea is asleep, curled up on the sofa next to Roger, who is stroking her hair. Lorraine is seated close by. Bruce has crashed in the chair by the monitors. Lorraine and Roger look to Ed.
  EXPRESSION: null
- CHARACTER: Ed
  LINE: You’ve got to see this.
  EXPRESSION: Urgent

::PATHS::
- CHOICE: "Go to the kitchen to review photos"
  TARGET: kitchen_photos_analysis
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Kitchen
MOOD: Revelation, dread, fear, increasing tension
CHARACTERS: Ed, Lorraine, Carolyn, Roger, Jerome, Narrator
BACKGROUND_IMAGE: house_kitchen_night.png
BACKGROUND_EDIT: "Right after, group gathered around a table with photographs"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Ed, Lorraine, Carolyn and Roger are standing at the table, looking at a photograph, Jerome stands aside, holding two more photos in his hand.
  EXPRESSION: null
- CHARACTER: Lorraine
  LINE: He’s the boy I saw in the hidden room.
  EXPRESSION: Realization
- CHARACTER: Narrator
  LINE: Angle on the photo, although grainy and transparent, it’s definitely the same boy with glasses Lorraine saw, but he’s at the top of the stairs, heading down.
  EXPRESSION: null
- CHARACTER: Jerome
  LINE: Now check this out.
  EXPRESSION: Eager
- CHARACTER: Narrator
  LINE: He drops a second picture. Although it’s the same angle, the boy is now five steps further down the stairs. He’s got a terrified look on his face as he’s looking back up over his shoulder at something at the top of the stairs.
  EXPRESSION: null
- CHARACTER: Roger
  LINE: What’s he looking at?
  EXPRESSION: Curious
- CHARACTER: Jerome
  LINE: This --
  EXPRESSION: Dramatic
- CHARACTER: Narrator
  LINE: Jerome drops the third photo from his hand onto the table before them. The image of the boy is gone, but at the top of the stairs is the dark presence of Bathsheba Sherman, although grainy and transparent as well, her image is a lot more defined, and what stands out more than anything are her pupil-less, snow white eyes.
  EXPRESSION: null
- CHARACTER: Lorraine
  LINE: It’s her.
  EXPRESSION: Dread
- CHARACTER: Narrator
  LINE: Roger and Carolyn’s eyes are wide, transfixed.
  EXPRESSION: null
- CHARACTER: Roger
  LINE: Why would he be frightened of her? He’s dead.
  EXPRESSION: Confused
- CHARACTER: Lorraine
  LINE: From our perspective, yes. But from that child’s, she’s as real to him as you are to me.
  EXPRESSION: Explaining
- CHARACTER: Lorraine
  LINE: She may have died a witch, but she’s come back with a strength only Satan can give her --
  EXPRESSION: Grim

::PATHS::
- CHOICE: "Face the revealed presence"
  TARGET: living_room_haunting
  STATE_CHANGE: fear = +3, knowledge = +1
  CONDITION: null

::SCENE::
LOCATION: Living Room
MOOD: Supernatural attack, terror, chaos
CHARACTERS: Andrea, Bruce, Ed, Lorraine, Roger, Carolyn, Narrator
BACKGROUND_IMAGE: house_living_room_night.png
BACKGROUND_EDIT: "Same, crosses falling, escalating paranormal activity, furniture disturbed"

::SCRIPT::
- CHARACTER: Narrator
  LINE: CU on the mantle where the cross Ed set up, topples with a soft “clink”.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Widen A SECOND CROSS set on top of the Grandfather clock, falls onto a rug below with a muffled thud.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: A THIRD CROSS on the coffee table joins suit. The noise stirs Bruce, then --
  EXPRESSION: null
- CHARACTER: Andrea
  LINE: Cindy, stop it.
  EXPRESSION: Sleepy
- CHARACTER: Narrator
  LINE: His eyes shift to over to her. Although she’s semi-asleep, she thinks someone’s messing with the back of her hair.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Bruce watches in total shock as the back of Andrea’s hair seems to rise up on its own.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: He slowly grabs his camera to document it.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Camera’s pov as a groggy Andrea reaches behind and irritatingly swats at something that’s not there. Her long hair continues to rise.
  EXPRESSION: null
- CHARACTER: Andrea
  LINE: I said to stop it.
  EXPRESSION: Annoyed
- CHARACTER: Narrator
  LINE: This time, she opens her eyes and sees that no one’s doing it, but her hair SNAPS TAUT and she’s aggressively yanked off the chair and onto the floor.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: She screams as she begins to get wildly snaked all over the floor.
  EXPRESSION: Screaming
- CHARACTER: Narrator
  LINE: Although Bruce drops the camera to its side, it keeps rolling, giving us a side view of Bruce moving over to Andrea and grabbing onto her.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Resume.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Whatever has hold of Andrea’s hair, is strong enough to keep moving them both as Bruce tries to protect her, enveloping the young girl with his large body, tumbling this way, then that way, when the two of them are slammed into the coffee table where Bruce takes most of the impact, pieces of wood go flying.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Ed and Lorraine come running in, Ed joins the fight, struggling to hold Bruce/Andrea in one place, it isn’t working.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The fight continues, Andrea is wild-eyed, screaming hysterically, her hair stretched to its limit.
  EXPRESSION: Screaming
- CHARACTER: Narrator
  LINE: Roger comes racing in, then Carolyn, who seems less disturbed.
  EXPRESSION: null
- CHARACTER: Roger
  LINE: Ohmygod.
  EXPRESSION: Shocked
- CHARACTER: Narrator
  LINE: Bruce and Andrea hit the corner of the sofa, which pushes it four feet across the wood floor, then they’re immediately dragged once again.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Roger attempts to latch on to them, the strain on Andrea’s hair looks like it’s going to be pulled out of her scalp, until WHOOSH! A PAIR OF SCISSORS slices right through it, releasing all tension.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The struggle instantly stops. Standing over Bruce and Andrea is Lorraine, Jerome’s s
  EXPRESSION: null

::PATHS::
- CHOICE: "End of immediate threat"
  TARGET: next_event
  STATE_CHANGE: fear = +4, damage = true
  CONDITION: null

::SCENE::
LOCATION: Perron House
MOOD: Relieved, Tense
CHARACTERS: Roger, Andrea, Ed, Bruce, Narrator
BACKGROUND_IMAGE: perron_house_interior.png
BACKGROUND_EDIT: "Night, messy aftermath of a struggle"

::SCRIPT::
- CHARACTER: Narrator
  LINE: scissors in hand. Roger immediately pulls Andrea into his arms. Ed looks to a very distraught Bruce, whose face is bloody from a wound on his forehead.
  EXPRESSION: null
- CHARACTER: Ed
  LINE: You okay?
  EXPRESSION: Concerned
- CHARACTER: Bruce
  LINE: I’ll take a guy with a gun any day.
  EXPRESSION: Weary
- CHARACTER: Narrator
  LINE: Ed sees the light on the camera.
  EXPRESSION: null
- CHARACTER: Ed
  LINE: Did you get any of it?
  EXPRESSION: Urgent
- CHARACTER: Narrator
  LINE: Bruce nods.
  EXPRESSION: null

::PATHS::
- CHOICE: "Leave the house"
  TARGET: perron_house_front_sunrise
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Perron House Front
MOOD: Hopeful, Urgent
CHARACTERS: Ed, Roger, Narrator
BACKGROUND_IMAGE: perron_house_front.png
BACKGROUND_EDIT: "Sunrise, station wagon, two men carrying suitcases"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Ed and Roger approach the back of the Perron’s station wagon, each carrying two small suitcases. The first rays of morning light pierce the horizon.
  EXPRESSION: null
- CHARACTER: Ed
  LINE: We’re going to get the footage developed and bring it over to the church right away -- this house needs to be exorcised as soon as possible.
  EXPRESSION: Urgent
- CHARACTER: Narrator
  LINE: Roger opens the back of the car.
  EXPRESSION: null
- CHARACTER: Roger
  LINE: I’ll get you paid back for the hotel.
  EXPRESSION: Grateful
- CHARACTER: Ed
  LINE: Let’s not worry about that right now.
  EXPRESSION: Dismissive
- CHARACTER: Narrator
  LINE: We see the gratitude runs deep for Roger as he places the suitcases inside.
  EXPRESSION: null
- CHARACTER: Roger
  LINE: When do you think you can get someone out here?
  EXPRESSION: Anxious
- CHARACTER: Ed
  LINE: It should only take a couple of days. But listen to me --
  EXPRESSION: Serious
- CHARACTER: Narrator
  LINE: Roger looks to him.
  EXPRESSION: null
- CHARACTER: Ed
  LINE: -- Under no circumstances does anyone come back here until we say so.
  EXPRESSION: Authoritative

::PATHS::
- CHOICE: "Enter the house"
  TARGET: perron_house_stairs_same
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Perron House - Base of Stairs
MOOD: Somber, Concerned, Tender
CHARACTERS: Lorraine, Andrea, Bruce, Jerome, Cindy, Narrator
BACKGROUND_IMAGE: perron_house_stairs.png
BACKGROUND_EDIT: "Interior, base of stairs, children present"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Lorraine comes out of the living room. Bruce and Jerome are in the background, breaking down the equipment. She approaches Andrea, who is sitting in Cindy’s lap on the bottom step, the trauma still apparent on her face. It’s hard for Lorraine to see this little girl like this.
  EXPRESSION: null
- CHARACTER: Lorraine
  LINE: It’s going to be okay -- nothing’s going to hurt you again. I promise.
  EXPRESSION: Comforting
- CHARACTER: Narrator
  LINE: Andrea stands and gives Lorraine an unexpected embrace. It lingers. Lorraine is first to unlock from the hug, but Andrea still clings for a few seconds longer, then lets her go. Looks to Cindy --
  EXPRESSION: null
- CHARACTER: Lorraine
  LINE: Is your mom upstairs?
  EXPRESSION: Neutral
- CHARACTER: Cindy
  LINE: No, she’s in the kitchen.
  EXPRESSION: Neutral
- CHARACTER: Narrator
  LINE: Lorraine’s walks to the kitchen doorway, peers in. It’s empty. She notices that the back door is open.
  EXPRESSION: null

::PATHS::
- CHOICE: "Go to back porch"
  TARGET: perron_house_back_porch_right_after
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Perron House - Back Porch
MOOD: Suspenseful
CHARACTERS: Lorraine, Carolyn (glimpse), Narrator
BACKGROUND_IMAGE: perron_house_back_porch.png
BACKGROUND_EDIT: "Exterior, back porch, open door"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Lorraine heads outside. She catches a glimpse of Carolyn heading into the woods behind the barn.
  EXPRESSION: null

::PATHS::
- CHOICE: "Follow Carolyn into the woods"
  TARGET: woods_right_after
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Woods
MOOD: Eerie, Concerned
CHARACTERS: Lorraine, Carolyn, Narrator
BACKGROUND_IMAGE: woods.png
BACKGROUND_EDIT: "Thick canopy, light piercing through, cemetery wall"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Lorraine makes her way through the woods, literally retracing her steps from before. As she approaches the clearing, she can see Carolyn sitting on the wall of the cemetery with her back to her. Light pierces down through the thick canopy above.
  EXPRESSION: null
- CHARACTER: Lorraine
  LINE: Carolyn--?
  EXPRESSION: Concerned
- CHARACTER: Narrator
  LINE: Carolyn doesn’t turn around. Lorraine slowly approaches.
  EXPRESSION: null
- CHARACTER: Lorraine
  LINE: Are you okay?
  EXPRESSION: Concerned
- CHARACTER: Narrator
  LINE: As Lorraine nears, it’s hard to tell if it’s the afternoon light and shadows are playing tricks with her eyes, but it looks like, from the side view, there’s something off about Carolyn’s face, it almost looks like another woman’s. Carolyn slowly swivels her head to Lorraine which seems normal now, but there’s a distance in her eyes.
  EXPRESSION: null
- CHARACTER: Carolyn
  LINE: Yes--?
  EXPRESSION: Distant
- CHARACTER: Lorraine
  LINE: What’re you doing here?
  EXPRESSION: Curious
- CHARACTER: Narrator
  LINE: Lorraine notices that Carolyn is holding the SLINKY she saw in the hidden room.
  EXPRESSION: null

::PATHS::
- CHOICE: "Leave the woods"
  TARGET: warrens_plymouth_right_after
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Warren's Plymouth
MOOD: Urgent, Concerned
CHARACTERS: Ed, Lorraine, Narrator
BACKGROUND_IMAGE: warrens_plymouth_interior.png
BACKGROUND_EDIT: "Interior of a car, driving on a country road"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Ed and Lorraine drive along a country road.
  EXPRESSION: null
- CHARACTER: Lorraine
  LINE: She said she just wanted to see it. And she was holding the slinky I saw in that room. As far as I’m concerned, the church can’t get there fast enough.
  EXPRESSION: Worried

::PATHS::
- CHOICE: "Drive to Boston"
  TARGET: boston_day
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Boston
MOOD: Establishing
CHARACTERS: Narrator
BACKGROUND_IMAGE: boston_skyline.png
BACKGROUND_EDIT: "High camera angle, Bunker Hill Bridge, downtown Boston"

::SCRIPT::
- CHARACTER: Narrator
  LINE: High camera angle - drops down onto the Warren’s Plymouth as they drive across Bunker Hill Bridge and into downtown Boston. Camera keeps dropping down. We’re close enough to see the Plymouth pull curbside to:
  EXPRESSION: null

::PATHS::
- CHOICE: "Arrive at cathedral"
  TARGET: cathedral_holy_cross_boston_continuous
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Cathedral of the Holy Cross - Boston - Exterior
MOOD: Solemn, Anticipatory
CHARACTERS: Ed, Lorraine, Narrator
BACKGROUND_IMAGE: cathedral_exterior.png
BACKGROUND_EDIT: "Large stone structure, peaked roofs, stained glass, open front doors"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Ed parks in front of a very large, impressive stone structure with peaked roofs and stained glass. As Ed and Lorraine get out of the car, THEY HEAR the soft, angelic singing voice of a young boy emanating from the open front doors of the church. They head up the stone steps to the open doors. The singing continues.
  EXPRESSION: null

::PATHS::
- CHOICE: "Enter the church"
  TARGET: church_interior_right_after
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Church Interior
MOOD: Solemn, Reverent
CHARACTERS: Ed, Lorraine, Father Jordon, Narrator
BACKGROUND_IMAGE: church_interior.png
BACKGROUND_EDIT: "Massive size, center aisle, pews, choir rehearsal"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Ed and Lorraine enter. They are dwarfed by its massive size. The center aisle splits through numerous rows of pews. Up front, a choir director stands off to the side during a rehearsal, as a young boy sings his heart out. An all boys choir stand silent behind them. Ed dips his fingertips into a bowl sculpted from marble, full of Holy water. Says a silent prayer, then crosses himself. Lorraine follows suit. The two of them are approached by Father Jordon. Greets them with a warm smile.
  EXPRESSION: null
- CHARACTER: Father Jordon
  LINE: Let’s see what you’ve got.
  EXPRESSION: Expectant

::PATHS::
- CHOICE: "Show the footage"
  TARGET: church_father_jordons_office_day
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Church - Father Jordon's Office
MOOD: Serious, Stunned
CHARACTERS: Ed, Lorraine, Father Jordon, Narrator
BACKGROUND_IMAGE: father_jordons_office.png
BACKGROUND_EDIT: "Interior office, projector, screen, tape recorder"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Camera’s skewed pov of - THE LAST FEW SECONDS WITH BRUCE AND ANDREA thrashing about the floor, just as she gets her hair cut by Roger. Wide to see, we’re -- Ed and Lorraine are sitting down with Father Jordon. Thick curtains are pulled across a paned window. Father Jordon turns off a projector next to him that’s been throwing the sequence onto a screen set up against a wall. We see Ed’s tape recorder on the table as well. Ed and Lorraine look to Father Jordon for his response. He seems a little stunned.
  EXPRESSION: null
- CHARACTER: Father Jordon
  LINE: You weren’t kidding -- I’ll get this to the Archbishop right away.
  EXPRESSION: Stunned

::PATHS::
- CHOICE: "Return home"
  TARGET: warren_house_front_door_evening
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Warren House - Front Door
MOOD: Relief, Affectionate
CHARACTERS: Ed, Lorraine, Judy, Ed's Mom, Narrator
BACKGROUND_IMAGE: warren_house_front_door.png
BACKGROUND_EDIT: "Evening, front door, family reunion"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Ed and Lorraine exit their car. Judy comes out the front door and Lorraine runs to her, swooping her up in her arms. Ed’s mom is in the background.
  EXPRESSION: null

::PATHS::
- CHOICE: "Time passes"
  TARGET: diner_day
  STATE_CHANGE: time_elapsed = "six days"
  CONDITION: null

::SCENE::
LOCATION: Diner
MOOD: Concerned, Stressed
CHARACTERS: Cindy, Andrea, Roger, Ed, Lorraine, Narrator
BACKGROUND_IMAGE: diner_interior.png
BACKGROUND_EDIT: "Day, lunch crowd, bar stools, booth, 6 days later"

::SCRIPT::
- CHARACTER: Narrator
  LINE: SUPERIMPOSE: SIX DAYS LATER. Lunch crowd. Don McLean’s “American Pie” plays in the b.g. as Cindy and Andrea are sitting on bar stools at a linoleum counter, picking through lunch. Out of ear shot, and seated at a booth opposite the counter, is Roger. He’s with Ed and Lorraine, and looks stressed out.
  EXPRESSION: null
- CHARACTER: Roger
  LINE: But you said it’d only take a couple of days.
  EXPRESSION: Stressed
- CHARACTER: Ed
  LINE: We don’t know why it’s taking so long. Father Jordon says that the Vatican keeps telling him to be patient, but I’m driving to New York tomorrow to see if Father Langston can find out what’s going on. He’s a high level Cardinal we’ve worked with before -- and knows the Archbishop pretty well.
  EXPRESSION: Frustrated
- CHARACTER: Roger
  LINE: I’m just so worried about Carolyn. I think all the stress has been too much. She’s not herself at all -- hasn’t showered, doesn’t wear makeup, is barely sleeping. And she just disappears for hours at a time.
  EXPRESSION: Worried
- CHARACTER: Narrator
  LINE: Off their look --
  EXPRESSION: null

::PATHS::
- CHOICE: "Check on Carolyn"
  TARGET: mathews_dry_goods_day
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Mathews Dry Good's
MOOD: Uneasy
CHARACTERS: Carolyn, Maddy, Narrator
BACKGROUND_IMAGE: dry_goods_store.png
BACKGROUND_EDIT: "Day, counter with knitting needles, unkempt Carolyn"

::SCRIPT::
- CHARACTER: Narrator
  LINE: A set of knitting needles are placed on a counter. Widen, we see it’s a very unkept Carolyn who has placed them there to purchase. Shannon’s niece, Maddy, is at the cash register, a little uneasy.
  EXPRESSION: null
- CHARACTER: Maddy
  LINE: Do you need any yarn?
  EXPRESSION: Uneasy
- CHARACTER: Narrator
  LINE: Carolyn shakes her head no.
  EXPRESSION: null

::PATHS::
- CHOICE: "Ed travels to New York"
  TARGET: saint_patricks_cathedral_nyc_next_day
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Saint Patrick’s Cathedral - New York City - Exterior
MOOD: Concerned, Frustrated
CHARACTERS: Ed, Lorraine (V.O.), Narrator
BACKGROUND_IMAGE: st_patricks_cathedral_exterior.png
BACKGROUND_EDIT: "Next day, massive stone structure, phone booth"

::SCRIPT::
- CHARACTER: Narrator
  LINE: A massively impressive structure of stone, stained glass and towering cathedrals. Ed is in a phone booth on the corner, the phone pressed to his ear.
  EXPRESSION: null
- CHARACTER: Ed
  LINE: Father Langston called the Vatican directly and they told him it had been presented by the Archbishop, but there’s some issues.
  EXPRESSION: Concerned
- CHARACTER: Lorraine (V.O.)
  LINE: Issues -- what’s that supposed to mean?
  EXPRESSION: Impatient
- CHARACTER: Ed
  LINE: He didn’t know, they wouldn’t elaborate.
  EXPRESSION: Frustrated

::PATHS::
- CHOICE: "Call Lorraine"
  TARGET: warren_house_kitchen_same
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Warren House - Kitchen
MOOD: Concerned, Resigned
CHARACTERS: Lorraine, Ed (V.O.), Narrator
BACKGROUND_IMAGE: warren_house_kitchen.png
BACKGROUND_EDIT: "Same day, Lorraine sitting at a desk"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Lorraine’s sitting at the desk.
  EXPRESSION: null
- CHARACTER: Lorraine
  LINE: What’re we going to do?
  EXPRESSION: Desperate
- CHARACTER: Ed (V.O.)
  LINE: I don’t know -- I’m going to hit the road, it’s going to be midnight before I get home as it is.
  EXPRESSION: Resigned
- CHARACTER: Lorraine
  LINE: Alright, be safe. Love you.
  EXPRESSION: Affectionate
- CHARACTER: Ed (V.O.)
  LINE: Love you, too.
  EXPRESSION: Affectionate

::PATHS::
- CHOICE: "Wait for the phone to ring"
  TARGET: warren_house_kitchen_later
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Warren House - Kitchen
MOOD: Anticipatory
CHARACTERS: Lorraine, Narrator
BACKGROUND_IMAGE: warren_house_kitchen.png
BACKGROUND_EDIT: "Later, phone rings"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The phone rings. Lorraine enters the
  EXPRESSION: null

::PATHS::
- CHOICE: "Answer the phone"
  TARGET: end
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Warren House Kitchen
MOOD: Normal
CHARACTERS: Lorraine, Narrator
BACKGROUND_IMAGE: kitchen.png
BACKGROUND_EDIT: "Daytime, house interior"

::SCRIPT::
- CHARACTER: Lorraine
  LINE: Hello?
  EXPRESSION: null
- CHARACTER: Lorraine
  LINE: Hey Jerome --
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The doorbell rings.
  EXPRESSION: null
- CHARACTER: Lorraine
  LINE: Honey, I’m on the phone, can you see who that is?
  EXPRESSION: Neutral

::PATHS::
- CHOICE: "Continue scene in foyer"
  TARGET: warren_house_foyer_same
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Warren House Foyer
MOOD: Normal
CHARACTERS: Judy, UPS Delivery Man, Narrator
BACKGROUND_IMAGE: foyer.png
BACKGROUND_EDIT: "Daytime, house interior, front door"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Judy comes down the stairs.
  EXPRESSION: null
- CHARACTER: Judy
  LINE: Okay, mom.
  EXPRESSION: Neutral
- CHARACTER: Narrator
  LINE: She continues to the front door. Opens it to see a UPS DELIVERY MAN standing before in a crisp brown uniform. Holds an over-sized manila envelope.
  EXPRESSION: null
- CHARACTER: Judy
  LINE: Hi.
  EXPRESSION: Neutral
- CHARACTER: UPS Delivery Man
  LINE: Well hi back. Would you be part of the Warren family?
  EXPRESSION: Neutral
- CHARACTER: Judy
  LINE: Yep.
  EXPRESSION: Neutral
- CHARACTER: UPS Delivery Man
  LINE: Well then, here you go.
  EXPRESSION: Neutral
- CHARACTER: Narrator
  LINE: He hands her a large manila envelope.
  EXPRESSION: null
- CHARACTER: UPS Delivery Man
  LINE: Have a nice day.
  EXPRESSION: Neutral
- CHARACTER: Judy
  LINE: Thanks!
  EXPRESSION: Neutral
- CHARACTER: Narrator
  LINE: He leaves.
  EXPRESSION: null

::PATHS::
- CHOICE: "Return to the kitchen"
  TARGET: warren_house_kitchen_right_after
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Warren House Kitchen
MOOD: Normal
CHARACTERS: Judy, Lorraine, Narrator
BACKGROUND_IMAGE: kitchen.png
BACKGROUND_EDIT: "Daytime, house interior, right after"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Judy walks in, Lorraine’s still on the phone.
  EXPRESSION: null
- CHARACTER: Lorraine
  LINE: -- Ed’s about to lose his mind.
  EXPRESSION: Concerned
- CHARACTER: Narrator
  LINE: Lorraine looks to her -- sees the envelope and reads the return address: it’s from Shannon in Harrisville. She motions for Judy to put it on the desk, which she does.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Judy grabs a small basket off the kitchen counter. Looks to her mom.
  EXPRESSION: null
- CHARACTER: Judy
  LINE: I’m gonna go get some eggs, ‘kay?
  EXPRESSION: Neutral
- CHARACTER: Narrator
  LINE: Lorraine covers the mouthpiece.
  EXPRESSION: null
- CHARACTER: Lorraine
  LINE: That’s fine, honey.
  EXPRESSION: Neutral
- CHARACTER: Narrator
  LINE: Judy heads out the back door.
  EXPRESSION: null

::PATHS::
- CHOICE: "Go to the backyard"
  TARGET: warren_house_backyard_continuous
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Warren House Backyard
MOOD: Building Suspense
CHARACTERS: Judy, Narrator
BACKGROUND_IMAGE: backyard.png
BACKGROUND_EDIT: "Daytime, house exterior, chicken coop"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Judy makes her way to the chicken coop. Calls out.
  EXPRESSION: null
- CHARACTER: Judy
  LINE: Gertrude, Henrietta, Lolly --
  EXPRESSION: Neutral
- CHARACTER: Narrator
  LINE: Judy opens the coop door. Steps in. She’s surprised to see that there aren’t any chickens outside the hen house, but something in the dirt at her feet catches her attention.
  EXPRESSION: Surprised
- CHARACTER: Narrator
  LINE: She takes a closer look.
  EXPRESSION: Curious
- CHARACTER: Narrator
  LINE: It’s the SLINKY from the Perron house, half in and out of the dirt. She picks it up. Examines, then puts it in her basket as she heads to the henhouse door.
  EXPRESSION: Curious
- CHARACTER: Judy
  LINE: Gertrude, where are you?
  EXPRESSION: Concerned
- CHARACTER: Narrator
  LINE: More silence. Judy unlatches the door. Swings it open. She steps in.
  EXPRESSION: null

::PATHS::
- CHOICE: "Enter the henhouse"
  TARGET: henhouse_continuous
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Henhouse
MOOD: Dread
CHARACTERS: Judy, Narrator
BACKGROUND_IMAGE: henhouse_interior.png
BACKGROUND_EDIT: "Continuous, minimal light, interior"

::SCRIPT::
- CHARACTER: Narrator
  LINE: As Judy’s eyes slowly adjust to the minimal light, unbeknownst to her, the HENHOUSE DOOR slowly closes behind her.
  EXPRESSION: Afraid

::PATHS::
- CHOICE: "Cut to kitchen"
  TARGET: kitchen_same
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Warren House Kitchen
MOOD: Rising Tension
CHARACTERS: Lorraine, Narrator
BACKGROUND_IMAGE: kitchen.png
BACKGROUND_EDIT: "Continuous, house interior"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Lorraine watches Judy out through the window.
  EXPRESSION: null
- CHARACTER: Lorraine
  LINE: We’ll let you know when we find out anything.
  EXPRESSION: Neutral
- CHARACTER: Lorraine
  LINE: Say hi to your mom.
  EXPRESSION: Neutral
- CHARACTER: Narrator
  LINE: Just as she hangs up, an ear curdling SCREAM from Judy ERUPTS FROM THE HENHOUSE.
  EXPRESSION: Surprised
- CHARACTER: Narrator
  LINE: Lorraine’s body goes tight, then she kicks it into high and races out of the kitchen to the backyard.
  EXPRESSION: Panicked

::PATHS::
- CHOICE: "Race to the backyard"
  TARGET: house_exterior_continuous
  STATE_CHANGE: fear = +2
  CONDITION: null

::SCENE::
LOCATION: Warren House Exterior
MOOD: Panicked
CHARACTERS: Lorraine, Narrator
BACKGROUND_IMAGE: backyard.png
BACKGROUND_EDIT: "Continuous, house exterior, chicken coop"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Lorraine is moving fast as her legs will carry her to the chicken coop.
  EXPRESSION: null
- CHARACTER: Lorraine
  LINE: Judy!
  EXPRESSION: Panicked
- CHARACTER: Narrator
  LINE: No answer and it’s killing her.
  EXPRESSION: Panicked
- CHARACTER: Lorraine
  LINE: Judy?
  EXPRESSION: Panicked
- CHARACTER: Narrator
  LINE: Lorraine barely slows down to open the outer door and move inside the coop.
  EXPRESSION: null
- CHARACTER: Lorraine
  LINE: Honey, answer me.
  EXPRESSION: Panicked
- CHARACTER: Narrator
  LINE: She sprints to the henhouse door and tries to open it, but it won’t budge, she gives it everything she’s got, pulling as hard as she can, then it finally whips open. Lorraine races in --
  EXPRESSION: Panicked

::PATHS::
- CHOICE: "Enter the henhouse"
  TARGET: henhouse_interior_continuous
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Henhouse
MOOD: Dread
CHARACTERS: Judy, Lorraine, Narrator
BACKGROUND_IMAGE: henhouse_interior.png
BACKGROUND_EDIT: "Continuous, interior, dead chickens"

::SCRIPT::
- CHARACTER: Narrator
  LINE: -- Sees Judy on her knees, facing the opposite direction. She turns to her mom, tears rolling down her cheeks. Has one of the chickens in her lap, it’s not moving.
  EXPRESSION: null
- CHARACTER: Judy
  LINE: Gertrude’s dead, mom. They all are.
  EXPRESSION: Crying
- CHARACTER: Narrator
  LINE: Lorraine looks past her daughter, dead chickens are everywhere, all their necks broken at obscured angles.
  EXPRESSION: Shocked
- CHARACTER: Narrator
  LINE: Lorraine sees the slinky in the basket next to her daughter. Dread begins to set in for Lorraine.
  EXPRESSION: Afraid
- CHARACTER: Lorraine
  LINE: Where’d you get that?
  EXPRESSION: Afraid
- CHARACTER: Narrator
  LINE: Through her tears, Judy follows her mom’s sight to the basket.
  EXPRESSION: null
- CHARACTER: Judy
  LINE: It was on the ground.
  EXPRESSION: Neutral

::PATHS::
- CHOICE: "Return to the kitchen"
  TARGET: warren_house_kitchen_soon_after
  STATE_CHANGE: fear = +3
  CONDITION: null

::SCENE::
LOCATION: Warren House Kitchen
MOOD: Somber
CHARACTERS: Lorraine, Judy, Narrator
BACKGROUND_IMAGE: kitchen.png
BACKGROUND_EDIT: "Soon after, house interior"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Lorraine walks Judy in. Dumps the slinky in the trash can.
  EXPRESSION: null

::PATHS::
- CHOICE: "Dissolve to master bedroom"
  TARGET: master_bedroom_night
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Master Bedroom
MOOD: Calm
CHARACTERS: Lorraine, Judy, Narrator
BACKGROUND_IMAGE: master_bedroom.png
BACKGROUND_EDIT: "Nighttime, four-poster bed"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Lorraine and Judy, who’s now wearing pajamas, sit on the edge of a four posted, chiffon-canopied bed as Lorraine finishes braiding Judy’s hair. She has calmed down significantly.
  EXPRESSION: null
- CHARACTER: Judy
  LINE: Did you call daddy and tell him?
  EXPRESSION: Neutral
- CHARACTER: Lorraine
  LINE: He’s on the road honey, I’ll tell him when he gets home.
  EXPRESSION: Neutral

::PATHS::
- CHOICE: "Time cut to later in bedroom"
  TARGET: master_bedroom_later
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Master Bedroom
MOOD: Rising Tension
CHARACTERS: Lorraine, Judy, Narrator
BACKGROUND_IMAGE: master_bedroom.png
BACKGROUND_EDIT: "Later, nighttime, moonlight, interior"

::SCRIPT::
- CHARACTER: Narrator
  LINE: A shaft of moonlight piercing through a window, stretches across Lorraine’s face in bed. Lorraine’s EYES SUDDENLY POP OPEN, startled. She looks to Judy, who’s talking in her sleep, saying:
  EXPRESSION: Surprised
- CHARACTER: Judy
  LINE: I’m sorry mommy, I’m sorry mommy.
  EXPRESSION: Afraid
- CHARACTER: Narrator
  LINE: The words chill her to the bone. She gives Judy a slight nudge.
  EXPRESSION: Concerned
- CHARACTER: Lorraine
  LINE: Judy.
  EXPRESSION: Concerned
- CHARACTER: Narrator
  LINE: Judy doesn’t awaken, continues --
  EXPRESSION: null
- CHARACTER: Judy
  LINE: I’m sorry mommy, I’m --
  EXPRESSION: Afraid
- CHARACTER: Lorraine
  LINE: Honey --
  EXPRESSION: Concerned
- CHARACTER: Narrator
  LINE: She shakes her harder. Judy’s words fade as she rolls over, sound asleep.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Lorraine slowly sits up, digesting the current event. She gasps --
  EXPRESSION: Afraid
- CHARACTER: Narrator
  LINE: -- someone is standing in the far corner of the room.
  EXPRESSION: Afraid
- CHARACTER: Narrator
  LINE: -- it looks like Bathsheba Sherman staring right at her, but --
  EXPRESSION: Afraid
- CHARACTER: Narrator
  LINE: -- it’s not a ghostly image, IT LOOKS REAL.
  EXPRESSION: Afraid
- CHARACTER: Narrator
  LINE: Keeping her eyes on the corner, Lorraine reaches her hand over to turn on the lamp. Flips the switch illuminating the corner, where there is no woman. Only a narrow corner cabinet.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Lorraine lets out a sigh.
  EXPRESSION: Relieved
- CHARACTER: Lorraine
  LINE: Get a grip, Lorraine.
  EXPRESSION: Neutral

::PATHS::
- CHOICE: "Cut to master bathroom"
  TARGET: master_bathroom_right_after
  STATE_CHANGE: fear = +2
  CONDITION: null

::SCENE::
LOCATION: Master Bathroom
MOOD: Normal
CHARACTERS: Lorraine, Narrator
BACKGROUND_IMAGE: master_bathroom.png
BACKGROUND_EDIT: "Nighttime, interior, right after"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Lorraine, now wearing pajamas, finishes washing her face, then exits, turning the light off.
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue to master bedroom"
  TARGET: master_bedroom_continuous
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Master Bedroom
MOOD: Dread
CHARACTERS: Lorraine, Judy, Narrator
BACKGROUND_IMAGE: master_bedroom.png
BACKGROUND_EDIT: "Continuous, nighttime, interior, slinky"

::SCRIPT::
- CHARACTER: Narrator
  LINE: She walks over to the bed where Judy is sound asleep. Crawls under the covers. As she reaches to turn off the light, her blood pressure races north, the SLINKY she threw away is right there.
  EXPRESSION: Shocked
- CHARACTER: Narrator
  LINE: The four posts on her bed begin CREAKING, she slowly looks up, stretched out upon the canopy, is Bathsheba Sherman the contours of her eyes, face and body clearly outlined as she descends closer and closer, the force of which causing each of the bed posts to strain, bending inward like they’re made of rubber.
  EXPRESSION: Afraid
- CHARACTER: Narrator
  LINE: Lorraine remains paralyzed, unable to move, chilled by the ominous reality of this unholy spirit.
  EXPRESSION: Terrified
- CHARACTER: Narrator
  LINE: Lorraine digs deep and finds some inner strength to get herself moving, scoops Judy up. Dashes out through the bedroom doorway just as the door whips closed right behind her.
  EXPRESSION: Panicked

::PATHS::
- CHOICE: "Cut to Denny's Restaurant"
  TARGET: denny's_restaurant_night
  STATE_CHANGE: fear = +4
  CONDITION: null

::SCENE::
LOCATION: Denny's Restaurant
MOOD: Normal
CHARACTERS: Ed, Narrator
BACKGROUND_IMAGE: denny's_exterior.png
BACKGROUND_EDIT: "Nighttime, restaurant exterior"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Ed comes out with a thermos. Gets into the car.
  EXPRESSION: null

::PATHS::
- CHOICE: "Enter the car"
  TARGET: warren's_plymouth_continuous
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Warren's Plymouth
MOOD: Shock
CHARACTERS: Ed, Narrator
BACKGROUND_IMAGE: car_interior.png
BACKGROUND_EDIT: "Continuous, car interior, nighttime"

::SCRIPT::
- CHARACTER: Narrator
  LINE: As he sets the thermos down on the passenger seat, his heart skips a beat.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The PICTURE OF JUDY dangling from the mirror has changed.
  EXPRESSION: Shocked
- CHARACTER: Narrator
  LINE: The CROSS is now broken and hanging upside down, and Judy’s eyes are white, void of pupils, identical to Bathsheba Sherman’s in the earlier photograph.
  EXPRESSION: Terrified

::PATHS::
- CHOICE: "Smash cut to Denny's Restaurant interior"
  TARGET: denny's_restaurant_right_after
  STATE_CHANGE: fear = +3
  CONDITION: null

::SCENE::
LOCATION: Denny's Restaurant
MOOD: Panicked
CHARACTERS: Ed, Narrator
BACKGROUND_IMAGE: denny's_interior.png
BACKGROUND_EDIT: "Right after, restaurant interior, phone booth"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Ed is using a phone at the front counter.
  EXPRESSION: Panicked

::PATHS::
- CHOICE: "Cut to Warren House"
  TARGET: warren_house_same
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Warren House
MOOD: Eerie
CHARACTERS: Narrator
BACKGROUND_IMAGE: warren_house_interior.png
BACKGROUND_EDIT: "Continuous, house interior, phone ringing"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Camera slowly moves through the house. Everything is still. The only thing we hear is the PHONE RINGING and RINGING, no one answers.
  EXPRESSION: null

::PATHS::
- CHOICE: "Smash cut to Warren's Plymouth"
  TARGET: warren's_plymouth_night
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Warren's Plymouth
MOOD: Urgent
CHARACTERS: Ed, Narrator
BACKGROUND_IMAGE: car_exterior.png
BACKGROUND_EDIT: "Nighttime, car speeding, driveway"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Ed’s hauling ass as he slides a turn and pulls up in the driveway of his house. Skids to a stop. Jams out.
  EXPRESSION: Urgent

::PATHS::
- CHOICE: "Cut to Warren House front door"
  TARGET: warren_house_front_door_right_after
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Warren House Front Door
MOOD: Panicked
CHARACTERS: Ed, Narrator
BACKGROUND_IMAGE: front_door_interior.png
BACKGROUND_EDIT: "Right after, house interior, Ed entering"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The door swings open. Ed swiftly enters.
  EXPRESSION: null
- CHARACTER: Ed
  LINE: Lorraine?
  EXPRESSION: Panicked
- CHARACTER: Narrator
  LINE: No answer.
  EXPRESSION: null
- CHARACTER: Ed
  LINE: -- Lorraine?
  EXPRESSION: Panicked
- CHARACTER: Narrator
  LINE: He sprints up a set of stairs before him.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Ed, takes two at a time, speeds to the top, then makes a hard right, heading for the Master bedroom. The door is closed.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Ed gets to the door. Opens it. He looks to the bed. Empty. His panicked gaze shifts about the darkness. Lorraine’s not in there.
  EXPRESSION: Panicked
- CHARACTER: Narrator
  LINE: Ed continues down the hallway to Judy’s room. Door’s closed too. He slowly opens it, afraid of what he’s going to find.
  EXPRESSION: Afraid
- CHARACTER: Narrator
  LINE: He looks to the bed. Empty as well. His panicked gaze shifts about the darkness, then there, tucked in a shadow is the silhouetted body of Lorraine. She’s sitting o
  EXPRESSION: Panicked

::PATHS::
- CHOICE: "End scene"
  TARGET: end
  STATE_CHANGE: fear = +4
  CONDITION: null

::SCENE::
LOCATION: Warren House - Living Room
MOOD: Urgent, Tense
CHARACTERS: Narrator, Ed, Lorraine, Judy
BACKGROUND_IMAGE: warren_house_living_room.png
BACKGROUND_EDIT: "Interior, Judy in lap, bible open, rosary in hand, Ed dashing"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Judy in her lap.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Ed dashes to them, Lorraine’s got a bible open before her, and a Rosary tucked into her hand.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: She and Ed’s eyes meet.
  EXPRESSION: null
- CHARACTER: Ed
  LINE: What happened?
  EXPRESSION: Concerned
- CHARACTER: Narrator
  LINE: She doesn’t say anything, almost as if she can’t, then --
  EXPRESSION: null
- CHARACTER: Lorraine
  LINE: -- She was here, Ed.
  EXPRESSION: Afraid

::PATHS::
- CHOICE: "React to Lorraine's revelation"
  TARGET: warren_house_kitchen_right_after
  STATE_CHANGE: fear = +1, anger = +1
  CONDITION: null

::SCENE::
LOCATION: Warren House - Kitchen
MOOD: Angry, Tense
CHARACTERS: Narrator, Ed, Lorraine
BACKGROUND_IMAGE: warren_house_kitchen.png
BACKGROUND_EDIT: "Interior, Ed full of anger, Lorraine behind him, phone on counter"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Ed moves into the kitchen, full of anger. Lorraine’s behind him.
  EXPRESSION: null
- CHARACTER: Ed
  LINE: I don’t believe this.
  EXPRESSION: Angry
- CHARACTER: Narrator
  LINE: Ed goes to an address book by the phone on the counter, quickly thumbs through it.
  EXPRESSION: null
- CHARACTER: Ed
  LINE: We’re supposed to be safe here, and you opened the door for her.
  EXPRESSION: Angry
- CHARACTER: Lorraine
  LINE: You make it sound like I meant to.
  EXPRESSION: Upset
- CHARACTER: Ed
  LINE: You knew the rules.
  EXPRESSION: Angry
- CHARACTER: Narrator
  LINE: Ed finds it incredulous. Sees the number he’s looking for and dials. Lorraine is near tears.
  EXPRESSION: null

::PATHS::
- CHOICE: "Make the call"
  TARGET: bruce_levy_house_study
  STATE_CHANGE: anger = +1, determination = +1
  CONDITION: null

::SCENE::
LOCATION: Bruce Levy's House - Study
MOOD: Tense, Concerned
CHARACTERS: Narrator, Bruce, Ed (V.O.), Bruce's Wife
BACKGROUND_IMAGE: bruce_levy_house_study.png
BACKGROUND_EDIT: "Interior, single light, Bruce on phone, rain outside, pregnant wife concerned"

::SCRIPT::
- CHARACTER: Narrator
  LINE: A single light illuminates Bruce. Has the phone to his ear. Rain pelts against the windows. His pregnant wife, same age, appears in the doorway, concerned.
  EXPRESSION: null
- CHARACTER: Bruce
  LINE: I will. Did you tell Jerome?
  EXPRESSION: Concerned
- CHARACTER: Ed (V.O.)
  LINE: No. I can’t get hold of him, he’s on his way back from his mom’s.
  EXPRESSION: Frustrated
- CHARACTER: Bruce
  LINE: I’ll get an APB out and have someone pull him over and tell him to call you immediately.
  EXPRESSION: Determined
- CHARACTER: Ed (V.O.)
  LINE: Great. Be careful, Bruce -- do what I said, and say it with conviction.
  EXPRESSION: Serious
- CHARACTER: Bruce
  LINE: I will.
  EXPRESSION: Determined
- CHARACTER: Narrator
  LINE: Bruce slowly hangs up. Looks to his wife.
  EXPRESSION: null
- CHARACTER: Bruce
  LINE: We need a bible.
  EXPRESSION: Serious

::PATHS::
- CHOICE: "Prepare for the coming confrontation"
  TARGET: jeromes_van
  STATE_CHANGE: determination = +1, urgency = +1
  CONDITION: null

::SCENE::
LOCATION: Jerome's Van
MOOD: Calm (initially), then Chaotic
CHARACTERS: Narrator, Jerome
BACKGROUND_IMAGE: jeromes_van.png
BACKGROUND_EDIT: "Interior, early morning, Jerome driving, Eagles music, then sudden braking"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Jerome is behind the wheel listening to an Eagles eight track kick out “TAKE IT EASY”. Early morning light is just peeking over the horizon.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: As the van crests a knoll HE HAS TO LOCK UP HIS BRAKES! Blocking the road before him is a horrible accident between a Ford Pinto and a Chevrolet station wagon. Skid marks scar the pavement. Smoke and steam rise from both.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Jerome holds the wheel tight, fighting for control as his van fishtails and SLIDES onto the dirt shoulder. He clips the front of the Pinto, spinning the van into a three-sixty before it comes to an abrupt stop.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: He looks back at the wreckage. See that two teenagers are emerging out of the Pinto, but the station wagon’s solo occupant, a man in his fifties, is slumped forward, not moving, and flames have engulfed the engine compartment.
  EXPRESSION: null

::PATHS::
- CHOICE: "React to the accident"
  TARGET: ext_road_continuous
  STATE_CHANGE: urgency = +1, surprise = +1
  CONDITION: null

::SCENE::
LOCATION: Road - Accident Site
MOOD: Chaotic, Desperate, Tragic
CHARACTERS: Narrator, Jerome, Teenagers, Radio DJ
BACKGROUND_IMAGE: ext_road_accident.png
BACKGROUND_EDIT: "Exterior, smoking wreckage, early morning, chaos, Jerome races to car"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Jerome exits the van and races to the station wagon, passing the teenagers, who are bloody and confused.
  EXPRESSION: null
- CHARACTER: Jerome
  LINE: Get off the road!
  EXPRESSION: Urgent
- CHARACTER: Narrator
  LINE: He gets to the station wagon, the driver’s window is down. His head leaning against the steering wheel. Still wears his seat belt. Morning news flows from the radio.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Jerome reaches in, feels for a pulse, finds one.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Looks to the engine. Flames are growing. Grabs for the driver’s door handle, but it’s all smashed in.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Reaches through the window to open it from the inside and pulls on the lever, doesn’t work either.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: He quickly moves around to get to the other door, the heat growing intense as he rounds the front and gets to the other side.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: As he pulls the door open --
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The radio continues in the background.
  EXPRESSION: null
- CHARACTER: Radio DJ
  LINE: It’s five-fifteen for you early risers --
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: SKIDDING TIRES drown out the DJ. Jerome looks to see that an EIGHTEEN WHEELER has come over the knoll and is a WALL OF METAL sliding right at him sideways, brakes locked up. Jerome doesn’t even have time to react as WHAMMMM!
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The tail end of the rig picks him clean away from the station wagon, like he was targeted.
  EXPRESSION: null

::PATHS::
- CHOICE: "Witness the tragic event"
  TARGET: warren_house_kitchen_morning
  STATE_CHANGE: shock = +1, despair = +1
  CONDITION: null

::SCENE::
LOCATION: Warren House - Kitchen
MOOD: Frustrated, Grieving, Determined
CHARACTERS: Narrator, Ed, Man's Voice (V.O.), Lorraine
BACKGROUND_IMAGE: warren_house_kitchen_morning.png
BACKGROUND_EDIT: "Interior, morning, Ed frustrated on phone, then distraught, then determined"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Ed’s on the phone as he stands at the counter. Looks frustrated.
  EXPRESSION: null
- CHARACTER: Ed
  LINE: I left a message a couple of hours ago for Father Jordon, is he back yet?
  EXPRESSION: Frustrated
- CHARACTER: Man’s Voice (V.O.)
  LINE: No, I’m sorry -- we don’t expect him to return until this afternoon.
  EXPRESSION: Apologetic
- CHARACTER: Ed
  LINE: There’s got to be some way to get hold of him.
  EXPRESSION: Frustrated
- CHARACTER: Man’s Voice (V.O.)
  LINE: We can’t interrupt him, he’s in a bereavement council.
  EXPRESSION: Calm
- CHARACTER: Ed
  LINE: When he comes in, tell him this is Ed Warren, and it’s imperative that he calls me as soon as possible. He has the number.
  EXPRESSION: Urgent
- CHARACTER: Narrator
  LINE: Just as Ed hangs up the phone, IT RINGS. He finds it odd, but answers.
  EXPRESSION: null
- CHARACTER: Ed
  LINE: -- Hello?
  EXPRESSION: Neutral
- CHARACTER: Narrator
  LINE: As he listens, his face pales, his head lowers into one hand; grieving.
  EXPRESSION: null
- CHARACTER: Ed (sotto)
  LINE: No -- no -- no.
  EXPRESSION: Grieving
- CHARACTER: Narrator
  LINE: Lorraine enters, looks to Ed, immediately sensing more trouble.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Ed continues to listen for a few beats, then --
  EXPRESSION: null
- CHARACTER: Ed
  LINE: -- Alright, thanks.
  EXPRESSION: Resigned
- CHARACTER: Narrator
  LINE: He numbly hangs up.
  EXPRESSION: null
- CHARACTER: Lorraine
  LINE: -- Ed, what is it?
  EXPRESSION: Concerned
- CHARACTER: Narrator
  LINE: He slowly rolls his head toward her.
  EXPRESSION: null
- CHARACTER: Ed
  LINE: That was Bruce. Jerome’s dead.
  EXPRESSION: Grieving
- CHARACTER: Narrator
  LINE: Lorraine couldn’t have heard that right.
  EXPRESSION: null
- CHARACTER: Lorraine
  LINE: What--?
  EXPRESSION: Shocked
- CHARACTER: Ed
  LINE: Car accident, early this morning.
  EXPRESSION: Somber
- CHARACTER: Narrator
  LINE: Lorraine’s eyes well.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Ed gets enraged. Slams his fist hard onto the counter.
  EXPRESSION: null
- CHARACTER: Ed
  LINE: Enough!
  EXPRESSION: Enraged
- CHARACTER: Narrator
  LINE: A wave of determination sweeps over him.
  EXPRESSION: null
- CHARACTER: Ed
  LINE: I’m driving to the church and getting this exorcism done today.
  EXPRESSION: Determined
- CHARACTER: Narrator
  LINE: She moves over to him as he’s grabbing his keys.
  EXPRESSION: null
- CHARACTER: Lorraine
  LINE: I’m going with you.
  EXPRESSION: Determined
- CHARACTER: Ed
  LINE: No -- you’re not.
  EXPRESSION: Firm
- CHARACTER: Narrator
  LINE: The lack of faith in his voice stings her hard. He walks out of the kitchen.
  EXPRESSION: null

::PATHS::
- CHOICE: "Decide to go to the church"
  TARGET: warrens_plymouth_right_after
  STATE_CHANGE: determination = +2, grief = +1
  CONDITION: null

::SCENE::
LOCATION: Warren's Plymouth
MOOD: Determined, Resolute
CHARACTERS: Narrator, Ed, Lorraine, Judy
BACKGROUND_IMAGE: warrens_plymouth_interior.png
BACKGROUND_EDIT: "Interior, Ed in driver's seat, Lorraine and Judy entering the car"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Ed’s sitting in the driver’s seat. Just as he starts the car, the back passenger door opens.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: He looks to see Lorraine, who has the manila envelope from Harrisville tucked under her arm, helping Judy in.
  EXPRESSION: null
- CHARACTER: Ed
  LINE: What’re you doing?
  EXPRESSION: Surprised
- CHARACTER: Lorraine
  LINE: We’re taking Judy to your mom’s, then going to the church. Together. I won’t walk away from these people, they need us -- this is what we do.
  EXPRESSION: Determined
- CHARACTER: Ed
  LINE: You can’t, you’re too involved.
  EXPRESSION: Concerned
- CHARACTER: Lorraine
  LINE: Maybe -- but that’s what gives me the strength to fight for that family too. I’m going.
  EXPRESSION: Resolute
- CHARACTER: Narrator
  LINE: The look on Lorraine’s face leaves no doubt for Ed that she’s back on track. He nods.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: She closes the back door, then climbs into the front.
  EXPRESSION: null

::PATHS::
- CHOICE: "Drive to the church with Lorraine and Judy"
  TARGET: in_the_car_later
  STATE_CHANGE: determination = +1, unity = +1
  CONDITION: null

::SCENE::
LOCATION: In the Car - On the Road
MOOD: Revealing, Tense
CHARACTERS: Narrator, Ed, Lorraine
BACKGROUND_IMAGE: in_the_car_road.png
BACKGROUND_EDIT: "Interior, car driving, passing a sign 'Boston 245 miles', Lorraine reading documents"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Ed is driving as Lorraine reads the pages sent from Shannon, they pass a sign that reads: Boston 245 miles.
  EXPRESSION: null
- CHARACTER: Lorraine
  LINE: -- Between the Shermans and the Perrons living there, the house has only been owned by two other families. One was the Walkers, whose kids were the ones I saw, and the other was the Heichts -- it says they had a son who was drowned by his mother --
  EXPRESSION: Serious

::PATHS::
- CHOICE: "Listen to Lorraine's findings"
  TARGET: underwater_black_and_white_footage
  STATE_CHANGE: revelation = +1, dread = +1
  CONDITION: null

::SCENE::
LOCATION: Underwater (Black and White Footage)
MOOD: Horrific, Tragic
CHARACTERS: Narrator, Lorraine (V.O.)
BACKGROUND_IMAGE: underwater_black_and_white.png
BACKGROUND_EDIT: "Black and white, underwater, boy drowning, last breath, mother's expressionless face above surface"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Of the boy Cindy saw on the stairs, his last breath of life escapes his mouth in an air bubble as his mother holds him under a foot of water near the shore of a pond. The body goes limp, his eyes locked wide open, staring at his mother, standing above the surface of the water, expressionless.
  EXPRESSION: null
- CHARACTER: Lorraine (V.O.)
  LINE: -- Who then killed herself --
  EXPRESSION: Somber

::PATHS::
- CHOICE: "Witness the tragedy"
  TARGET: the_mother_train_footage
  STATE_CHANGE: horror = +1, understanding = +1
  CONDITION: null

::SCENE::
LOCATION: Train Tracks (Flashback)
MOOD: Brutal, Shocking
CHARACTERS: Narrator, Lorraine
BACKGROUND_IMAGE: train_tracks_mother.png
BACKGROUND_EDIT: "Mother stepping in front of a fast-moving train, brutal scene, body tumbling"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The mother stepping right in front of a fast moving train, it’s brutal as we catch glimpses of her body tumbling under the train.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Resume.
  EXPRESSION: null
- CHARACTER: Lorraine (sotto)
  LINE: Oh my Lord --
  EXPRESSION: Shocked
- CHARACTER: Narrator
  LINE: Lorraine looks to Ed with a sudden realization.
  EXPRESSION: null
- CHARACTER: Lorraine
  LINE: -- She possesses the mothers to continue the sacrifices to Satan.
  EXPRESSION: Realizing

::PATHS::
- CHOICE: "Understand the demon's pattern"
  TARGET: church_office_boston_cathedral
  STATE_CHANGE: revelation = +2, fear = +1
  CONDITION: null

::SCENE::
LOCATION: Church Office - Boston Cathedral
MOOD: Tense, Confrontational
CHARACTERS: Narrator, Ed, Lorraine, Father Jordon, Archbishop Father O'Malley
BACKGROUND_IMAGE: church_office_boston.png
BACKGROUND_EDIT: "Interior, church office, night, distinguished figures, Ed and Lorraine intruding"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Ed and Lorraine walk right into Father Jordon’s office, who’s in the middle of speaking with the ARCHBISHOP, FATHER O’MALLEY; distinguished looking, late sixties. Both are caught off guard by the intrusion.
  EXPRESSION: null
- CHARACTER: Ed
  LINE: I want to know what the hell’s going on -- we can’t wait anymore.
  EXPRESSION: Impatient
- CHARACTER: Father Jordon
  LINE: Ed and Lorraine, this is Archbishop, Father O’Malley. I tried to call you.
  EXPRESSION: Surprised
- CHARACTER: Ed
  LINE: We’ve been on the road.
  EXPRESSION: Direct
- CHARACTER: Father O’Malley
  LINE: Please, sit down.
  EXPRESSION: Calm
- CHARACTER: Ed
  LINE: I don’t want to sit down. I want an exorcism performed. Today. What’s the problem here?
  EXPRESSION: Demanding
- CHARACTER: Narrator
  LINE: Father O’Malley takes a beat, what he’s about to say doesn’t look easy.
  EXPRESSION: null

::PATHS::
- CHOICE: "Demand the exorcism"
  TARGET: end
  STATE_CHANGE: determination = +1, confrontation = +1
  CONDITION: null

::SCENE::
LOCATION: Church Interior
MOOD: Tense
CHARACTERS: Narrator, Father O'Malley, Ed, Father Jordon, Lorraine
BACKGROUND_IMAGE: church_office.png
BACKGROUND_EDIT: "Daytime, traditional church office or meeting room"

::SCRIPT::
- CHARACTER: Father O'Malley
  LINE: The church is refusing to grant one.
  EXPRESSION: Resigned
- CHARACTER: Narrator
  LINE: Ed looks like he’s been sucker punched.
  EXPRESSION: Shocked
- CHARACTER: Father Jordon
  LINE: The family aren’t parishioners, and the children haven’t been Baptized.
  EXPRESSION: Explaining
- CHARACTER: Lorraine
  LINE: So what?
  EXPRESSION: Annoyed
- CHARACTER: Father O'Malley
  LINE: Believe me, we’ve tried, but the Vatican is worried about public opinion if they were to step outside the boundaries of the church.
  EXPRESSION: Explaining
- CHARACTER: Ed
  LINE: Tell the Vatican no one gives a shit. This needs to be stopped! Now!
  EXPRESSION: Angry
- CHARACTER: Father O'Malley
  LINE: Please understand, my hands are tied on this matter -- I feel horrible about this.
  EXPRESSION: Regretful
- CHARACTER: Narrator
  LINE: Ed is dumbfounded.
  EXPRESSION: Shocked
- CHARACTER: Ed
  LINE: So you’re going to do nothing?
  EXPRESSION: Disbelieving

::PATHS::
- CHOICE: "Exit the church"
  TARGET: boston_cathedral_front
  STATE_CHANGE: ed_frustration = +1, lorraine_frustration = +1
  CONDITION: null

::SCENE::
LOCATION: Boston Cathedral - Front
MOOD: Desperate
CHARACTERS: Narrator, Ed, Lorraine, Father Jordon
BACKGROUND_IMAGE: boston_cathedral_front.png
BACKGROUND_EDIT: "Daytime, grand cathedral exterior, stone steps"

::SCRIPT::
- CHARACTER: Narrator
  LINE: A bitter Ed and Lorraine walk out of the church with Father Jordon.
  EXPRESSION: null
- CHARACTER: Ed
  LINE: We’re just going to have to find someone else.
  EXPRESSION: Determined
- CHARACTER: Father Jordon
  LINE: You’re not going to get anyone to go against the church, Ed.
  EXPRESSION: Stern
- CHARACTER: Ed
  LINE: I don’t believe this.
  EXPRESSION: Disbelieving
- CHARACTER: Narrator
  LINE: Father Jordon reaches out to Ed and Lorrain, stops them. As their eyes meet, there’s an intensity to his gaze.
  EXPRESSION: null
- CHARACTER: Father Jordon
  LINE: You’ve both have seen it done dozens of times --
  EXPRESSION: Intense
- CHARACTER: Narrator
  LINE: Ed looks at him like he’s out of his mind.
  EXPRESSION: Disbelieving
- CHARACTER: Ed
  LINE: That doesn’t make us qualified.
  EXPRESSION: Dismissive
- CHARACTER: Father Jordon
  LINE: But your strength and knowledge of the scriptures can.
  EXPRESSION: Reassuring
- CHARACTER: Ed
  LINE: We’ve seen it go horribly wrong, even with a Priest.
  EXPRESSION: Skeptical
- CHARACTER: Father Jordon
  LINE: I believe our Lord recognizes faith far more than he does training and education, or politics for that matter. This family doesn’t have a choice, but you do -- and, you have God on your side. If you want to help them, then help them.
  EXPRESSION: Earnest
- CHARACTER: Narrator
  LINE: Ed looks to Lorraine, both their minds a whirl of limited options.
  EXPRESSION: Thoughtful

::PATHS::
- CHOICE: "Decide to help the family"
  TARGET: harrisville_motel
  STATE_CHANGE: ed_resolve = +1, lorraine_resolve = +1
  CONDITION: null

::SCENE::
LOCATION: Harrisville Motel
MOOD: Uneasy
CHARACTERS: Narrator, Cindy, Andrea, Carolyn
BACKGROUND_IMAGE: harrisville_motel_exterior_night.png
BACKGROUND_EDIT: "Nighttime, dimly lit motel corridor, door opens"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Cindy and Andrea approach their hotel room. Just as Cindy reaches for the doorknob, the door swings open, revealing Carolyn standing right before them. Her dirty hair is pulled back and is wearing a long grey dress, she’s even more gaunt and unkempt than the last time we saw her.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: She steps out, closing the door behind her.
  EXPRESSION: null
- CHARACTER: Carolyn
  LINE: Come with me.
  EXPRESSION: Demanding
- CHARACTER: Cindy
  LINE: Where?
  EXPRESSION: Confused
- CHARACTER: Carolyn
  LINE: We’re going home.
  EXPRESSION: Determined
- CHARACTER: Andrea
  LINE: But dad said --
  EXPRESSION: Hesitant
- CHARACTER: Carolyn
  LINE: -- He’s meeting us there. C’mon.
  EXPRESSION: Abrupt

::PATHS::
- CHOICE: "Go with Carolyn"
  TARGET: hotel_room_same
  STATE_CHANGE: girls_unease = +1
  CONDITION: null

::SCENE::
LOCATION: Hotel Room
MOOD: Shock
CHARACTERS: Narrator
BACKGROUND_IMAGE: hotel_room_interior_damaged.png
BACKGROUND_EDIT: "Nighttime, messy hotel room, broken lamp, man on floor"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Camera pans across the room and finds Roger on the floor next to a broken lamp. He’s not moving and the back of his head is bloody from a blow to the head.
  EXPRESSION: null

::PATHS::
- CHOICE: "Cut to Perron's car"
  TARGET: perron_car
  STATE_CHANGE: roger_injured = true
  CONDITION: null

::SCENE::
LOCATION: Perron’s Car
MOOD: Tense
CHARACTERS: Narrator, Carolyn, Cindy, Andrea
BACKGROUND_IMAGE: perron_car_interior_night.png
BACKGROUND_EDIT: "Nighttime, car interior, road passing outside"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Carolyn’s driving. The girls are in the back. They ride in silence for a few moments, then --
  EXPRESSION: null
- CHARACTER: Cindy
  LINE: Are you okay, mom?
  EXPRESSION: Worried
- CHARACTER: Narrator
  LINE: Carolyn doesn’t answer. The girls look to each other, more confused. Their worry continues to escalate.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Carolyn shifts her eyes to the rear view mirror and for a brief moment, THE EYES WE SEE are not hers anymore; these are dark, menacing, soulless.
  EXPRESSION: null

::PATHS::
- CHOICE: "Transition to phone call"
  TARGET: phone_booth
  STATE_CHANGE: carolyn_possessed = true
  CONDITION: null

::SCENE::
LOCATION: Phone Booth
MOOD: Anxious
CHARACTERS: Narrator, Ed, Lorraine
BACKGROUND_IMAGE: phone_booth_night.png
BACKGROUND_EDIT: "Nighttime, dimly lit phone booth, car parked outside"

::SCRIPT::
- CHARACTER: Narrator
  LINE: S.O. OF A PHONE RINGING. AND RINGING.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Ed holds a phone to his ear. Lorrain is in the Plymouth, parked outside the booth.
  EXPRESSION: null

::PATHS::
- CHOICE: "Cut to ringing phone in hotel room"
  TARGET: harrisville_hotel_room
  STATE_CHANGE: ed_calling = true
  CONDITION: null

::SCENE::
LOCATION: Harrisville Hotel Room
MOOD: Urgent
CHARACTERS: Narrator, Roger, Ed (V.O.)
BACKGROUND_IMAGE: hotel_room_phone_ringing.png
BACKGROUND_EDIT: "Nighttime, close up on ringing phone, then wider to Roger"

::SCRIPT::
- CHARACTER: Narrator
  LINE: CU on the phone as it continues to ring. Rings again. And again. A hand then reaches into frame and fumbles for the receiver. Grabs it.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Widen, it’s Roger, who’s fighting some pain as he holds the back of his head.
  EXPRESSION: null
- CHARACTER: Ed (V.O.)
  LINE: Hello...? Hello?
  EXPRESSION: Anxious
- CHARACTER: Roger
  LINE: Ed -- she tried to kill me.
  EXPRESSION: Pained
- CHARACTER: Ed (V.O.)
  LINE: Where are the girls?
  EXPRESSION: Fearful

::PATHS::
- CHOICE: "Cut to Perron car arriving home"
  TARGET: perron_car_later
  STATE_CHANGE: roger_communicated = true
  CONDITION: null

::SCENE::
LOCATION: Perron Car (Later)
MOOD: Ominous
CHARACTERS: Narrator, Carolyn, Cindy, Andrea
BACKGROUND_IMAGE: perron_house_distant_night.png
BACKGROUND_EDIT: "Nighttime, car driving towards a dark, distant house"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Carolyn turns down the driveway and heads toward their house that sits dark in the distance.
  EXPRESSION: null
- CHARACTER: Cindy
  LINE: You said dad was going to be here.
  EXPRESSION: Concerned
- CHARACTER: Narrator
  LINE: No answer from Carolyn, who continues to the front of the house and parks.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: She grabs a bag holding the KNITTING NEEDLES as she gets out.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Cindy and Andrea look at each other, they can’t figure out what’s going on as they watch their mom continue to the front door and disappear inside the house, leaving the entrance completely open.
  EXPRESSION: Worried

::PATHS::
- CHOICE: "Follow girls to the house"
  TARGET: perron_house_front_porch
  STATE_CHANGE: girls_fear = +1, carolyn_intent = "malicious"
  CONDITION: null

::SCENE::
LOCATION: Perron House - Front Porch / Hallway
MOOD: Suspenseful
CHARACTERS: Narrator, Cindy, Andrea, Carolyn (O.C.)
BACKGROUND_IMAGE: perron_house_hallway_open_cellar.png
BACKGROUND_EDIT: "Nighttime, dark hallway, cellar door wide open, scratches visible"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Cindy and Andrea walk up to the front door with caution in their steps. A chill chews on their spines, the cellar door at the end of the hallway is wide open, the deep scratches an eerie reminder of why they’ve kept it closed. The chair and wedge have been pushed aside.
  EXPRESSION: null
- CHARACTER: Cindy
  LINE: Mom, what are you doing? We should go.
  EXPRESSION: Worried
- CHARACTER: Narrator
  LINE: Still no response.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Cindy takes Andrea by the hand, and reluctantly heads inside the house. They go down the hallway toward the cellar, slow step after slow step.
  EXPRESSION: null
- CHARACTER: Cindy
  LINE: Mom -- are you down there?
  EXPRESSION: Apprehensive
- CHARACTER: Narrator
  LINE: When they get to the door, they peer in to see, a vacant staircase.
  EXPRESSION: null
- CHARACTER: Cindy
  LINE: Mom--?
  EXPRESSION: Questioning
- CHARACTER: Narrator
  LINE: A slight shuffling noise is the only response.
  EXPRESSION: null
- CHARACTER: Cindy
  LINE: Mom -- answer me. Are you okay?
  EXPRESSION: Worried
- CHARACTER: Narrator
  LINE: The noise stops. Cindy’s instincts are screaming at her to leave, but this is her mom.
  EXPRESSION: null
- CHARACTER: Cindy
  LINE: Stay here.
  EXPRESSION: Determined
- CHARACTER: Narrator
  LINE: Cindy tries the light switch, doesn’t work.
  EXPRESSION: null
- CHARACTER: Andrea
  LINE: Let’s just go.
  EXPRESSION: Panicked
- CHARACTER: Narrator
  LINE: Cindy ignores her.
  EXPRESSION: null

::PATHS::
- CHOICE: "Cindy enters the cellar"
  TARGET: cellar_continuous
  STATE_CHANGE: cindy_courage = +1, andrea_fear = +1
  CONDITION: null

::SCENE::
LOCATION: Cellar
MOOD: Terror
CHARACTERS: Narrator, Cindy, Carolyn
BACKGROUND_IMAGE: cellar_stairs_dark.png
BACKGROUND_EDIT: "Continuous from hallway, dark, eerie cellar stairs, gaps between steps"

::SCRIPT::
- CHARACTER: Narrator
  LINE: She heads down. Stops halfway.
  EXPRESSION: null
- CHARACTER: Cindy
  LINE: Mom--?
  EXPRESSION: Apprehensive
- CHARACTER: Narrator
  LINE: WHOOSH! A HAND suddenly shoots out from between the stairs, grabbing onto her ankle, tripping her.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Cindy grabs onto the handrail to keep herself from falling. She looks to the gap between the stairs to see her mom staring out at her with those wild, soulless eyes -- hand still latched onto her foot.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Cindy heel drives her free foot against her mother’s wrist, freeing the grasp she has on her and scrambles back up the stairs.
  EXPRESSION: Determined

::PATHS::
- CHOICE: "Escape from cellar"
  TARGET: hallway_continuous
  STATE_CHANGE: cindy_fear = +2, carolyn_aggression = +1
  CONDITION: null

::SCENE::
LOCATION: Hallway
MOOD: Panic
CHARACTERS: Narrator, Cindy, Andrea, Carolyn
BACKGROUND_IMAGE: perron_house_hallway_terror.png
BACKGROUND_EDIT: "Continuous from cellar, cellar door broken, front door slammed shut"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Cindy WHIPS THE DOOR CLOSED! The second she slams the chair back into place A LOUD, VIOLENT BANGING ON THE DOOR reverberates right before her.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The girls recoil from the impact, visibly trembling, how did their mom get there so fast. Either way, they’re getting the hell out of there.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Two steps into their departure THE CELLAR DOOR flies off hinges, the chair goes flying. Standing in the doorway, half in and out of the darkness, is Carolyn; her breath is elevated, almost hissing on each exhale as she grips the knitting needles tight in one hand.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Both the girls spin on their heels. Race for the front door, which SLAMS SHUT right before them. The girls scream. Cindy struggles with the door, but it won’t budge.
  EXPRESSION: null
- CHARACTER: Andrea
  LINE: Open it! Open it!
  EXPRESSION: Panicked
- CHARACTER: Cindy
  LINE: I can’t.
  EXPRESSION: Desperate
- CHARACTER: Narrator
  LINE: Movement through a side window catches her attention, it’s Roger racing up the driveway in the pickup.
  EXPRESSION: null
- CHARACTER: Cindy
  LINE: Daaaaaad!
  EXPRESSION: Relieved, Desperate
- CHARACTER: Narrator
  LINE: Cindy throws a panicked look over her shoulder to see her mom approaching. She grabs her little sister by the hand and races up the stairs.
  EXPRESSION: null

::PATHS::
- CHOICE: "Roger arrives at the house"
  TARGET: house_same
  STATE_CHANGE: roger_arrival = true, girls_trapped = true
  CONDITION: null

::SCENE::
LOCATION: House Exterior
MOOD: Urgent
CHARACTERS: Narrator, Roger, Cindy (O.C.)
BACKGROUND_IMAGE: perron_house_exterior_night_roger.png
BACKGROUND_EDIT: "Nighttime, pickup truck skidding to a stop, house lit by headlights"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Roger slides the truck to a skidding stop. Jumps out.
  EXPRESSION: null
- CHARACTER: Cindy O.C.
  LINE: DAAAAAAAAAD!!!
  EXPRESSION: Desperate
- CHARACTER: Narrator
  LINE: Roger runs to the front door. It’s locked. Front kicks the crap out of it until it busts from its frame. Rushes in.
  EXPRESSION: null

::PATHS::
- CHOICE: "Police and Warrens arrive"
  TARGET: colin_taft_road
  STATE_CHANGE: roger_entered_house = true
  CONDITION: null

::SCENE::
LOCATION: Colin Taft Road / Perron’s Driveway
MOOD: High Tension
CHARACTERS: Narrator, Ed, Lorraine, Bruce Levy
BACKGROUND_IMAGE: police_cruiser_lights_night.png
BACKGROUND_EDIT: "Nighttime, police cruiser lights flashing, cars driving at high speed"

::SCRIPT::
- CHARACTER: Narrator
  LINE: CU ON POLICE CRUISER LIGHTS FLASHING
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Widen. We see Ed and Lorraine’s car traveling right behind Bruce Levy, who is driving a POLICE CRUISER, escorting them at high speed as they slide a turn onto the Perron’s driveway.
  EXPRESSION: null

::PATHS::
- CHOICE: "Cars skid to a stop"
  TARGET: warrens_car_same
  STATE_CHANGE: assistance_arrived = true
  CONDITION: null

::SCENE::
LOCATION: Warren’s Car / House Exterior
MOOD: Shock
CHARACTERS: Narrator, Ed, Lorraine, Bruce
BACKGROUND_IMAGE: perron_house_exterior_night_lit.png
BACKGROUND_EDIT: "Nighttime, Roger's truck with engine running, house lit by headlights"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Ed and Lorraine see Roger’s truck with its door open, engine still running. Its headlights are on, lighting the house like center stage.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The cars skid to a stop. Just as they all get out.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: A GUNSHOT ECHOES OUT IN THE NIGHT as a muzzle flash pops from a bedroom window upstairs.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Lorraine turns and gives Ed a disturbed look. Bruce is with them as they all head into the house. He draws his gun.
  EXPRESSION: null

::PATHS::
- CHOICE: "Enter the Perron house"
  TARGET: end
  STATE_CHANGE: gunshot_heard = true, urgency = +1
  CONDITION: null

::SCENE::
LOCATION: House
MOOD: Urgent, Intense
CHARACTERS: Cindy, Ed, Bruce, Lorraine
BACKGROUND_IMAGE: house_interior.png
BACKGROUND_EDIT: "Dark, tense atmosphere, stairs in view"

::SCRIPT::
- CHARACTER: Cindy
  LINE: DADDY, NO!!
  EXPRESSION: Afraid
- CHARACTER: Narrator
  LINE: Ed, Bruce and Lorraine kick it into high, racing up the stairs.
  EXPRESSION: null

::PATHS::
- CHOICE: "Follow them upstairs"
  TARGET: upstairs_hallway
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Upstairs Hallway - Master Bedroom
MOOD: Desperate, Horrific
CHARACTERS: Ed, Bruce, Lorraine, Cindy, Roger, Carolyn, Andrea
BACKGROUND_IMAGE: master_bedroom_chaos.png
BACKGROUND_EDIT: "Dark, dishevelled master bedroom, rifle pointed, scattered plaster, signs of struggle"

::SCRIPT::
- CHARACTER: Narrator
  LINE: As they come off the top of the stairs --
  EXPRESSION: null
- CHARACTER: Cindy
  LINE: -- please, let her go!
  EXPRESSION: Afraid
- CHARACTER: Narrator
  LINE: Ed races down the hallway to the master bedroom. Door’s closed. Lorraine and Bruce are right behind.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Ed yanks the door open to see Roger has a rifle pointed point blank at Carolyn’s head, who has her arms wrapped around Andrea in a death grip, holding her next to the bed, the knitting needles having fallen to her feet.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: There’s scattered plaster on the floor from a fresh bullet hole in the ceiling above.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Cindy is a short distance away, petrified.
  EXPRESSION: Afraid
- CHARACTER: Roger
  LINE: Carolyn, let her go -- don’t make me do this, please.
  EXPRESSION: Afraid
- CHARACTER: Ed
  LINE: Roger -- no.
  EXPRESSION: Angry
- CHARACTER: Narrator
  LINE: He snaps.
  EXPRESSION: null
- CHARACTER: Roger
  LINE: She tried to stab her!
  EXPRESSION: Angry
- CHARACTER: Ed
  LINE: It’s not her doing this!
  EXPRESSION: Angry
- CHARACTER: Narrator
  LINE: Andrea struggles -- barely able to breath. Ed moves closer to Roger, who’s barely holding it together.
  EXPRESSION: null
- CHARACTER: Andrea
  LINE: Mommy, you’re hurting me.
  EXPRESSION: Afraid
- CHARACTER: Cindy
  LINE: Mom, stop.
  EXPRESSION: Afraid
- CHARACTER: Roger
  LINE: Carolyn, let her go.
  EXPRESSION: Afraid
- CHARACTER: Ed
  LINE: Pulling that trigger is exactly what this witch wants you to do -- it’s another sacrifice.
  EXPRESSION: Angry
- CHARACTER: Narrator
  LINE: Bruce moves into the room, closes in on Roger.
  EXPRESSION: null
- CHARACTER: Bruce
  LINE: Roger, just lower your gun -- give it to me.
  EXPRESSION: Afraid
- CHARACTER: Roger
  LINE: No! Carolyn, let her go!
  EXPRESSION: Angry
- CHARACTER: Narrator
  LINE: Roger looks like he could lose it any second.
  EXPRESSION: null
- CHARACTER: Lorraine
  LINE: Roger, please -- give him the gun...
  EXPRESSION: Afraid
- CHARACTER: Narrator
  LINE: We see Roger struggling with a decision, stares at Carolyn’s maniacal face before him.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: She seems to be enjoying every second of this, tormenting him by pulling Andrea in tighter.
  EXPRESSION: Evil
- CHARACTER: Lorraine
  LINE: C’mon, give it to Bruce.
  EXPRESSION: Afraid
- CHARACTER: Narrator
  LINE: Carolyn immediately puts more pressure on Andrea, who is now beginning to turn slightly blue. He raises it up again.
  EXPRESSION: null
- CHARACTER: Ed
  LINE: Don’t give her what she wants.
  EXPRESSION: Angry
- CHARACTER: Narrator
  LINE: Roger yields.
  EXPRESSION: null
- CHARACTER: Roger
  LINE: You better be right.
  EXPRESSION: Afraid
- CHARACTER: Narrator
  LINE: As he lowers the gun to give to Bruce WHAM! He’s kicked by Carolyn with such brute force, he flies backwards across the room into the wall. Glass flies, gun goes sliding across the floor. Cindy’s losing it fast. Ed and Bruce move in to grab hold of Carolyn.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Ed gets a backhand to the face. Draws blood. Bruce leaps onto Carolyn, bringing she and Andrea to the floor, but her grip remains strong on Andrea, continuing to squeeze the life out of her, now more than ever.
  EXPRESSION: null
- CHARACTER: Lorraine
  LINE: Grab her arms!
  EXPRESSION: Afraid
- CHARACTER: Narrator
  LINE: Loraine and Roger latch onto the arms, her strength overwhelming, Ed gets to his feet, extracting the vial of Holy water. Dips his forefinger into it. Crosses himself.
  EXPRESSION: null
- CHARACTER: Ed
  LINE: My Lord, you are all powerful, you are God, you are our Father --
  EXPRESSION: Praying
- CHARACTER: Narrator
  LINE: Carolyn instantly arches her back, folding her body into an upside down “U”. Ed gets close, reaching out, placing his finger on Carolyn’s forehead, making the sign of the cross.
  EXPRESSION: null
- CHARACTER: Ed
  LINE: Ecce crucem donine, fugite partes adversa!
  EXPRESSION: Angry
- CHARACTER: Narrator
  LINE: Behind it all, we hear Lorraine saying the Lord’s prayer.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The pictures fly off the dresser at sonic speed and disintegrate into the opposing wall. Glass shatters.
  EXPRESSION: null
- CHARACTER: Ed
  LINE: I beg you Lord, through the intercession and help of the arch angels Michael, Rafael and Gabriel, for the deliverance of our sister who is enslaved by the evil one.
  EXPRESSION: Praying
- CHARACTER: Narrator
  LINE: Cindy stands still, paralyzed with fear.
  EXPRESSION: Afraid
- CHARACTER: Ed
  LINE: Imponat extreman parte stolae ejus.
  EXPRESSION: Praying
- CHARACTER: Narrator
  LINE: Ed makes the sign of the cross over his chest, then flicks Holy Water on Carolyn. A GUTTURAL SCREAM escapes Carolyn’s mouth, which looks like a spider web of saliva and for a nano-second, her skin becomes transparent, veiny, pulsating,
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: She begins to writhe and rotate on the wood floor, taking anyone holding on with her, her body is unnaturally stiff.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: A SOURCELESS WIND erupts within the room, spinning everything around, clothing and hair whip uncontrollably.
  EXPRESSION: null
- CHARACTER: Ed
  LINE: Sanctissima vero Eucharistia super caput obssessi, aut aliter ejus corpori ne admoveatur, ob irreverentia periculum.
  EXPRESSION: Praying
- CHARACTER: Narrator
  LINE: Lorraine sees Carolyn’s eyes keep fading back and forth, from pitch black pupils, to blue as if there were an internal struggle going on.
  EXPRESSION: null
- CHARACTER: Lorraine
  LINE: Fight it, Carolyn! Don’t let her take you!
  EXPRESSION: Afraid
- CHARACTER: Narrator
  LINE: The dresser slides across the floor, ripping DEEP SCRATCHES in the wood. It just misses Lorraine by a fraction as it plows right by her, bounces off the bed frame and embeds into the drywall.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Lorraine looks to Cindy.
  EXPRESSION: null
- CHARACTER: Lorraine
  LINE: Help us!
  EXPRESSION: Afraid
- CHARACTER: Ed
  LINE: Keep her away --
  EXPRESSION: Angry
- CHARACTER: Lorraine
  LINE: No Ed -- there’s a reason she hasn’t killed her, Carolyn’s still fighting the possession -- she can help her! Get her to fight this!
  EXPRESSION: Afraid
- CHARACTER: Narrator
  LINE: Ed pauses for a second, his mind racing through limited options. Agrees with Lorraine. Nods.
  EXPRESSION: null
- CHARACTER: Lorraine
  LINE: Take her feet!
  EXPRESSION: Afraid
- CHARACTER: Narrator
  LINE: Cindy quickly obeys, holding down her mom’s feet as Carolyn arches unnaturally; a contortion that would seemingly break anyone’s back.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Carolyn then collapses back down to the floor with a loud thud, but keeps her death grip on Andrea, who’s now limp in her arms; her face turning blue from lack of Oxygen. Ed and Bruce frantically try to pry her fingers off of Andrea, but she’s too strong.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The wind builds in intensity.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Lorraine looks into Carolyn’s eyes that continue to fade back and forth.
  EXPRESSION: null
- CHARACTER: Lorraine
  LINE: You fight her Carolyn, don’t give up.
  EXPRESSION: Afraid
- CHARACTER: Cindy
  LINE: Please mom, please! You can do it. Make her let go of Andrea!
  EXPRESSION: Afraid
- CHARACTER: Ed
  LINE: Nos eriperes de potestate diaboli. Ab omni hoste visibili et invisibili et ubique in hoc saeculo liberetur.
  EXPRESSION: Praying
- CHARACTER: Narrator
  LINE: The bed flips up against the wall, windows blast open, the lights surge with power.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Carolyn gives one last burst of energy; muscles twitch and veins rise from under her skin, but everyone holds her down tight then, like someone pulled the plug, Carolyn stops moving, becomes limp, almost catatonic. Her arms fall off of Andrea, who rolls to the floor in a dead heap.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Everything falls still, not a sound. It’s over.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Roger immediately begins to give his daughter mouth to mouth, everyone watches on. Crying, praying, hoping.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: A cough draws their attention, it’s Carolyn, who is attempting to get her bearings when she finally does, she’s overwhelmed when she sees her daughter not moving, then a small cough erupts from Andrea, who then takes a deep breath. Tears flood from her father and sister.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Carolyn crawls over to them, stares at Andrea eye to eye; both emotional wrecks. Pulls her into an embrace. Roger and Cindy join in.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Lorraine takes a beat watching the Perron’s reunited, then looks to Ed. Goes over to him. Their eyes meet, she smiles.
  EXPRESSION: null
- CHARACTER: Ed
  LINE: You did good.
  EXPRESSION: Happy
- CHARACTER: Lorraine
  LINE: You too.
  EXPRESSION: Happy
- CHARACTER: Narrator
  LINE: Long beat.
  EXPRESSION: null
- CHARACTER: Ed
  LINE: Still feel like quitting?
  EXPRESSION: Calm
- CHARACTER: Narrator
  LINE: A slow smile grows on her lips.
  EXPRESSION: null
- CHARACTER: Lorraine
  LINE: Not just yet.
  EXPRESSION: Happy

::PATHS::
- CHOICE: "Observe the aftermath"
  TARGET: warren_house_exterior
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Warren House - Exterior
MOOD: Peaceful, Hopeful
CHARACTERS: Ed, Lorraine, Judy, Grandmother
BACKGROUND_IMAGE: warren_house_day.png
BACKGROUND_EDIT: "Daytime, calm suburban house, driveway"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Ed and Lorraine pull up in their driveway. Judy and her Grandmother come out the front door to greet them. Judy runs to the car.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: As Lorraine gives her a warm hug, Ed extracts a box from the back seat and hands it to her. She opens the top to see TWELVE BABY CHICKS INSIDE.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Off her smile, we fade out.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The end.
  EXPRESSION: null

::PATHS::
- CHOICE: "End of story"
  TARGET: end_credits
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Over Black
MOOD: Informative
CHARACTERS: Narrator
BACKGROUND_IMAGE: black_screen.png
BACKGROUND_EDIT: "Black screen with white text"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The Perron family left the house that day, and never returned. They relocated to Oregon, where they haven’t had anymore encounters. Shortly after their move, the house was purchased by an anonymous buyer, whom Ed and Lorraine believe was the Catholic Church. The Warrens went on to investigate over eight thousand cases, and to this day, Ed is the only non-ordained Demonologist ever recognized by the Vatican. It was one year later that the Warren’s were called to Amityville.
  EXPRESSION: null

::PATHS::
- CHOICE: "Exit"
  TARGET: final_end
  STATE_CHANGE: null
  CONDITION: null

