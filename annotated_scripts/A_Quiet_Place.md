::SCENE::
LOCATION: Black Screen
MOOD: Eerie
CHARACTERS: Narrator
BACKGROUND_IMAGE: black_screen.png
BACKGROUND_EDIT: "Fade in from black"

::SCRIPT::
- CHARACTER: Narrator
  LINE: We hear, very clearly, the sound of light wind.
  EXPRESSION: null

::PATHS::
- CHOICE: "Proceed"
  TARGET: town_main_street
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Town - Main Street
MOOD: Desolate
CHARACTERS: Narrator
BACKGROUND_IMAGE: town_main_street.png
BACKGROUND_EDIT: "Late afternoon, dusty, no movement"

::SCRIPT::
- CHARACTER: Narrator
  LINE: We come up on a streetlight. There is no illumination and no movement.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: We hold on it for a long moment when suddenly-- The streetlight bobs and then begins to sway.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: We slowly begin to rise up on the streetlight to reveal a small bird has landed on it.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: We continue to rise to reveal, behind the bird.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Wind blows through the gargantuan evergreens that seem to engulf the narrow main street of a small town in upstate New York.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Shop windows and cars on either side covered in dust, the place seems frozen in time. There is no movement.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: In the very middle of the road one can see sand.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: A bizarre incongruity, a long pathway about a shovels width runs the full length of the street with offshoots into open doorways of some of the shops.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: We hold for a long moment.
  EXPRESSION: null

::PATHS::
- CHOICE: "Enter general store"
  TARGET: general_store_front
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: General Store - Front
MOOD: Suspenseful
CHARACTERS: Narrator
BACKGROUND_IMAGE: general_store_front.png
BACKGROUND_EDIT: "Late afternoon, dusty, abandoned-looking interior"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Slowly pushing through the doorway of a large general store, also covered in dust.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: To the left, a cash register with small shelves of nearly empty candy boxes below.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: To the right, a towering shelf full of bags of potato chips, nacho chips and pretzels. None are missing.
  EXPRESSION: null

::PATHS::
- CHOICE: "Move to aisles"
  TARGET: general_store_aisles
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: General Store Aisles
MOOD: Tense
CHARACTERS: Narrator, Tiny Feet, Small Dark Figure, Woman (Mother), 8 year old boy (Son)
BACKGROUND_IMAGE: general_store_aisles.png
BACKGROUND_EDIT: "Late afternoon, towering shelves, dusty floor, dim lighting"

::SCRIPT::
- CHARACTER: Narrator
  LINE: WE MOVE SLOWLY across the floor, down the middle of a general store.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Amid the towering shelves of goods on either side, one may recognize a barely perceptible pattern of which shelves are bare and which are not. There is no movement. No sound.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Suddenly, TINY FEET JUMP INTO OUR MOVING FRAME! Then, as fast as they appeared. They’re gone.
  EXPRESSION: Surprised
- CHARACTER: Narrator
  LINE: WE NOW MOVE UP the side of the store, looking down one aisle and the next.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: As we arrive at the next aisle we catch a glimpse of A SMALL DARK FIGURE!!! And then it's gone.
  EXPRESSION: Surprised
- CHARACTER: Narrator
  LINE: WE CONTINUE along the side of the store until we arrive at the last aisle.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: At the far end of the store we see a counter. With a window. And shelves.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Suddenly A WOMAN APPEARS IN THE WINDOW!
  EXPRESSION: Surprised
- CHARACTER: Narrator
  LINE: WE GO CLOSE ON THE WOMAN as she scans the shelves, slowly lowering herself to the ground until behind her we see an 8 year old boy sitting slumped against the wall HE IS BAREFOOT.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: On closer inspection we see sweat on the boy’s brow, his skin pale from fever.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The woman’s knee touches down on the ground next to the boy as she sees what she’s been looking for. She reaches out her hand.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: WE GO CLOSE ON HER HAND as it reaches toward a shell of orange prescription drug bottles.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Her hand suddenly begins to shift certain bottles ever so slightly AT A BIZARRELY SLOW PACE, she does not make a sound.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: As she does this, we get our first glimpse of names. Names of drugs. Names of people.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: HER HAND finally arrives at the very back of the shelf as she gently twists a bottle that reads AMOXICILLIN.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: ON THE MOTHER as she inhales slowly.
  EXPRESSION: Anxious
- CHARACTER: Narrator
  LINE: And then, as if doing surgery, she slowly closes her hand around the bottle and GENTLY begins to move it through the shelf toward her.
  EXPRESSION: Cautious
- CHARACTER: Narrator
  LINE: Her hand, once again moves incredibly slowly, her now wider closed hand shifts even more bottles as it passes.
  EXPRESSION: Cautious
- CHARACTER: Narrator
  LINE: JUST as she gets to the end of the shelf a bottle shifts with a RATTLE of pills. This is the first, deliberate sound we’ve heard. The mother FREEZES!!!!
  EXPRESSION: Afraid
- CHARACTER: Narrator
  LINE: WE RACK FOCUS to the boy on the ground, who now looks up with panic.
  EXPRESSION: Afraid
- CHARACTER: Narrator
  LINE: The mother’s eyes look all around the room. The way one does when they are waiting for something, LISTENING for something.
  EXPRESSION: Afraid
- CHARACTER: Narrator
  LINE: After a long moment, she pulls the bottle in her hand the final few inches, and off the shelf.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The mother draws a huge breath of relief.
  EXPRESSION: Relieved
- CHARACTER: Narrator
  LINE: As she stands up, we reveal, just over the counter TWO EYES LOOKING UP AT HER!!!
  EXPRESSION: Surprised

::PATHS::
- CHOICE: "Continue in store"
  TARGET: general_store_aisle_daughter
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Aisle - General Store
MOOD: Calm
CHARACTERS: Narrator, 10 year old girl (Daughter), Mother, Small boy (Son)
BACKGROUND_IMAGE: general_store_aisle_daughter.png
BACKGROUND_EDIT: "Late afternoon, counter, dusty aisle, children playing silently"

::SCRIPT::
- CHARACTER: Narrator
  LINE: A 10 year old girl stands on her toes, barely able to see over the wooden counter to her mother.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: She smiles at her mother and gives her a thumbs up.
  EXPRESSION: Happy
- CHARACTER: Narrator
  LINE: With that she’s off.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: WE FOLLOW HER as she runs lightly through the store, she is also barefoot.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The GIRL turns down an aisle to reveal a small boy sitting on the floor. He too is barefoot.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: As the girl approaches we see, in the thick dust on the floor he has drawn a rocket ship. She sits with him.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: He silently puts his hand to his chest, palm to the side, crosses his first two fingers of his other hand with deliberate focus, and then slowly puts his two hands together.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: He then looks up at her and quickly shoots his crossed fingers into the air like a rocket.
  EXPRESSION: Happy
- CHARACTER: Narrator
  LINE: She beams with pride for a moment and then signs back to hi
  EXPRESSION: Happy

::PATHS::
- CHOICE: "End of excerpt"
  TARGET: end
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: General Store Aisle
MOOD: Playful
CHARACTERS: Daughter, Boy, Narrator
BACKGROUND_IMAGE: general_store_aisle.png
BACKGROUND_EDIT: "Inside a general store, tall shelves, late afternoon light"

::SCRIPT::
- CHARACTER: Daughter
  LINE: Very good job!
  EXPRESSION: Happy
- CHARACTER: Boy
  LINE: That’s how--we get away.
  EXPRESSION: Struggling
- CHARACTER: Narrator
  LINE: The girl’s smile falls ever so slightly. Then the boy suddenly TAPS her on the shoulder and scurries away. She’s “it”.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: As the girl slowly gets up to follow him, we see for the first time A HEARING AID.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The boy disappears around a corner.
  EXPRESSION: null

::PATHS::
- CHOICE: "Follow the boy"
  TARGET: next_aisle
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Next Aisle
MOOD: Terrified
CHARACTERS: Girl, Boy, Figure, Narrator
BACKGROUND_IMAGE: general_store_next_aisle.png
BACKGROUND_EDIT: "Inside a general store, tall shelves, late afternoon light, a boy reaching for a toy"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The girl comes around the tall shelf into the next aisle when suddenly her eyes go wide!!! What she sees is the boy standing on a small box, STRETCHING to reach a toy on a high shelf. She walks quickly to him when suddenly the toy FALLS.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The girl instinctively SLIDES to the ground and catches the toy JUST as it’s about to hit the ground! On her face we can see she is TERRIFIED! She closes her eyes, taking a breath with relief. When she opens them, in the foreground, we see the toy she is holding a small TOY SPACE SHUTTLE. Then in the distance past the toy we see a FIGURE.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: She sits up to see a man standing outside the door of the general store, holding a large box with what looks like a quilt hanging out of it. A look of fear on his face softens, as he mimes wiping his brow with relief. She smiles, puts the toy back on a shelf and runs to him.
  EXPRESSION: null

::PATHS::
- CHOICE: "Run to the man"
  TARGET: general_store_front
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: General Store - Front
MOOD: Preparatory
CHARACTERS: Father, Mother, Daughter, Older Son, Young Boy, Narrator
BACKGROUND_IMAGE: general_store_front.png
BACKGROUND_EDIT: "Front area of a general store, late afternoon, a large box on the ground, items being packed"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The father gently puts the box on the ground and pulls back the pieces of thick quilt to reveal that all the contents are actually wrapped in it.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: He then reaches for a LARGE HIKING BACKPACK, and begins transferring the contents of the box into the bag. As he does, we see, cans of food, a variety of prescription pills, bandages and wrapped syringes.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The girl arrives at his side and excitedly starts rummaging through the box as well. As she does, we see thick paint brushes, bottles of glue, bottles of lighter fluid and a stack of old newspapers.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Then, her face lights up. From the box, she pulls out a SALVAGED SECURITY CAMERA with wires exposed. The girl gives it a brief once over and then removes, two exposed CIRCUIT BOARDS, very obviously only recently removed from whatever appliance they belonged to. The girl scans the boards with a voracity, pointing out to the father particular areas of interest. Her father can’t help but smile.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Suddenly, the box of Amoxicillin comes into frame and is placed on top along with two boxes of sugar. The father looks up at his wife. After a beat, she signs:
  EXPRESSION: null
- CHARACTER: Mother
  LINE: For my tea.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: He just keeps looking at her.
  EXPRESSION: null
- CHARACTER: Mother
  LINE: Fine. I have a sweet tooth.
  EXPRESSION: Happy
- CHARACTER: Narrator
  LINE: The father smiles and is about to close the bag when a candy bar is placed on top.
  EXPRESSION: null
- CHARACTER: Daughter
  LINE: Me too!
  EXPRESSION: Happy
- CHARACTER: Narrator
  LINE: The father looks up at her with fake incredulity. Suddenly the sick son in his mother’s arms weakly signs:
  EXPRESSION: null
- CHARACTER: Older Son
  LINE: Me too.
  EXPRESSION: Weakly Happy
- CHARACTER: Narrator
  LINE: The whole family laughs silently as the daughter GENTLY takes another candy bar from a box below the cash register. We can now see why the boxes are almost empty.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The father looks back to his arriving four year old son, expecting the same, but from behind his back the young boy reveals the toy space shuttle.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: With a sweet empathy the father reaches for the toy and shakes his head no. He turns the toy over and silently explains it has batteries, this toy can make noise.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The little boy watches, confused, hurt, as his father gently places the space shuttle on the counter. And then gently grabs a big lollipop and puts it in the bag for the boy.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The mother hands their sick son to the father who picks him up and walks out. The mother kisses her 4 year old on the head, shuffles the hiking bag onto her back and walks out too.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The daughter looks at the boy as tears begin to fill his eyes.
  EXPRESSION: null
- CHARACTER: Daughter
  LINE: It’s ok.
  EXPRESSION: Empathetic
- CHARACTER: Narrator
  LINE: The boy shakes his head no.
  EXPRESSION: Sad
- CHARACTER: Narrator
  LINE: After a moment, the girl looks back to see if her parents are there. She then reaches up and takes the shuttle down from the counter. With wide eyes her little brother watches as she surgically removes the batteries and places the shuttle in the hood of her brother’s sweatshirt. Covering it from view, she holds a finger up to her lips in the obligatory big sister way of telling him not to get her in trouble. He beams!
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: She then stands up and places the batteries back on the counter, smiles at her brother and gestures “let’s go”.
  EXPRESSION: null

::PATHS::
- CHOICE: "Exit the store"
  TARGET: main_street
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Main Street
MOOD: Tense
CHARACTERS: Daughter, Mother, Father, Four year old brother, Narrator
BACKGROUND_IMAGE: main_street.png
BACKGROUND_EDIT: "Deserted main street, late afternoon, sand path, characters walking silently"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The daughter exits the General Store and follows her mother and father, who are walking down the street only stepping on the sand path. Their steps are almost silent.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: After a moment, her four year old brother follows behind her.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: We watch everyone walk in total silence.
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue journey"
  TARGET: end
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: General Store
MOOD: Suspense
CHARACTERS: Narrator
BACKGROUND_IMAGE: general_store_interior.png
BACKGROUND_EDIT: "Late afternoon, dimly lit, cluttered counter"

::SCRIPT::
- CHARACTER: Narrator
  LINE: We slowly push in to the counter of the store and then realize THE BATTERIES ARE GONE!
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue journey"
  TARGET: road_woods
  STATE_CHANGE: supplies = -1
  CONDITION: null

::SCENE::
LOCATION: Road
MOOD: Foreboding
CHARACTERS: Narrator, Father, Mother, Daughter, Son
BACKGROUND_IMAGE: wooded_road.png
BACKGROUND_EDIT: "Late afternoon, heavily wooded, fading sun, sand path"

::SCRIPT::
- CHARACTER: Narrator
  LINE: A long road slices its way through a heavily wooded area, which further blocks the already fading sun.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: In WIDE PROFILE we see the family walking in a line, continuing only on a sand path. The father is in front carrying their sick son, then the mother with the backpack, then their blonde daughter and trailing a bit behind rumbles their robust 4 year old.
  EXPRESSION: null

::PATHS::
- CHOICE: "Approach the bridge"
  TARGET: bridge
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Bridge
MOOD: Terrifying
CHARACTERS: Narrator, Father, Mother, Daughter, Boy (4-year-old)
BACKGROUND_IMAGE: old_bridge.png
BACKGROUND_EDIT: "Late afternoon, rusted bridge towering eerily, sand path continues"

::SCRIPT::
- CHARACTER: Narrator
  LINE: From the ground we look up at an old and rusted bridge towering over us eerily, the sand path continues across it.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: WE TRACK WITH THE FAMILY as they walk across the bridge.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: There are minor creaks underneath the sand.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Suddenly we see, the four year old stops just before the entrance of bridge. The family continues not seeing him.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: WE FOLLOW THE BOY’S HANDS as he fishes around in his hood and pulls out THE TOY SHUTTLE.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: HEAD ON, we walk with the father, each member of his proud brood can be seen walking behind him. We can hear his strained breath and the tiniest swish of the footsteps in sand.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: HEAD ON, walking with the daughter, we now suddenly hear nothing. As she looks to be in her own world. So we are in hers. A smile breaks on her face as she walks and breathes in total silence. We walk with her for a long moment, when suddenly behind her A FLICKERING RED AND BLUE LIGHT.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The girl does not turn. She just keeps walking. Still smiling. As she looks up to her mother, we go into: SLOW MOTION
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: FROM THE GIRL’S POV, we see her mother and father spin around with a frantic shock on their faces.
  EXPRESSION: Shocked
- CHARACTER: Narrator
  LINE: BACK ON THE GIRL. She looks confused at her parents behavior LIGHTS AGAIN FLASH EERILY BEHIND HER.
  EXPRESSION: Confused
- CHARACTER: Narrator
  LINE: ON THE FATHER rushing to put the boy on the ground and turning to run.
  EXPRESSION: Terrified
- CHARACTER: Narrator
  LINE: ON THE MOTHER, spinning around with terror in her eyes, she looks to be holding in a SCREAM.
  EXPRESSION: Terrified
- CHARACTER: Narrator
  LINE: BACK ON THE GIRL slowly beginning to turn around at what her parents could be looking at as we: SPEED BACK UP TO NORMAL
  EXPRESSION: Curious
- CHARACTER: Narrator
  LINE: A loud playful beeping rushes in from the blinking shuttle.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Then, from the woods we hear THE MOST UNMISTAKABLE HORRIFYING SCREEEEEEEECH!!!
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: ON THE MOTHER as she slowly lowers the backpack to the ground and her legs begin to fail her.
  EXPRESSION: Terrified
- CHARACTER: Narrator
  LINE: ON THE FATHER running, violently shaking his head. It looks like he’s HOLDING IN A SCREAM.
  EXPRESSION: Terrified
- CHARACTER: Narrator
  LINE: THE TREES BEHIND THEM RUSTLE AND SNAP as something barrels through.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: ON THE BOY holding up his space ship proudly to his incoming father an enormous smile on his face.
  EXPRESSION: Happy
- CHARACTER: Narrator
  LINE: ON THE FATHER 20 feet away his face is a still frame of pure fear as he runs to camera. Then: THE MOST IMMEDIATE AND TERRIFYING COMBINATION OF SOUND ONE COULD EVER IMAGINE. A SHRIEK? A SCREAM? A CRUNCH? Then...
  EXPRESSION: Terrified
- CHARACTER: Narrator
  LINE: ON THE FATHER as a thin line of blood splatters on his face.
  EXPRESSION: Terrified
- CHARACTER: Narrator
  LINE: Mid run, the father’s body immediately goes limp failing him as he comes to a halt just in front of camera.
  EXPRESSION: Lifeless
- CHARACTER: Narrator
  LINE: Then, as quickly as it came THE SOUND IS GONE.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: IN WIDE PROFILE, The father stands lifeless. The two children stand frozen with fear, the MOTHER drops to her knees and a space shuttle blinks silently in the sand.
  EXPRESSION: Frozen
- CHARACTER: Narrator
  LINE: The four year old IS GONE.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Once again, only the wind can be heard.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: BLACK.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: SILENCE.
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue to title"
  TARGET: black_screen_title
  STATE_CHANGE: boy_status = 'missing', father_status = 'deceased', family_trauma = +5
  CONDITION: null

::SCENE::
LOCATION: Black Screen
MOOD: Eerie, Contemplative
CHARACTERS: Narrator
BACKGROUND_IMAGE: black_screen.png
BACKGROUND_EDIT: "Pure black, title fades in and out"

::SCRIPT::
- CHARACTER: Narrator
  LINE: FADE IN: TITLE A QUIET PLACE
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Still in BLACK. A new sound. Almost like that of the ocean.
  EXPRESSION: null

::PATHS::
- CHOICE: "Proceed to beach"
  TARGET: beach
  STATE_CHANGE: time_elapsed = '2 years'
  CONDITION: null

::SCENE::
LOCATION: Beach
MOOD: Serene, then unsettling
CHARACTERS: Narrator, Regan Abbott
BACKGROUND_IMAGE: empty_beach.png
BACKGROUND_EDIT: "Late afternoon, pink lit sand, sounds like ocean"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The new sound continues. In the last of the day’s sunlight:
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: WE TRACK, LOOKING STRAIGHT DOWN, on what appears to be an empty beach. The pink lit sand, now combined with a sound like the ocean, feels serene, almost otherworldly.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Slowly coming into frame, we see the face of the daughter. This is REGAN ABBOTT. Her hair is much longer. She is now TWO YEARS OLDER, 12. She just looks different.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: REGAN lays in the sand with eyes closed, but she is not asleep.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: With her brow furrowed and her closed eyes darting back and forth she looks oddly painted, almost as if she is wishing herself to another place.
  EXPRESSION: Disturbed
- CHARACTER: Narrator
  LINE: There is movement in her hands as her fingers caress an object.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Her eyes suddenly POP OPEN as she sits up violently CLOSE UP INTO OUR FRAME! She looks around with eyes wet and red, attempting to regain her bearings.
  EXPRESSION: Startled
- CHARACTER: Narrator
  LINE: WE SLOWLY MOVE AROUND her to see what she sees and are met with a jarringly incongruous landscape! Instead of a glistening ocean, there in front of REGAN stand the tall swaying stalks of A CORNFIELD.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: As REGAN looks to her lap WE SLOWLY TRAVEL DOWN to reveal, she is holding THE TOY SHUTTLE. As she maneuvers it through her fingers we see the shuttle is damaged, there a
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue scene"
  TARGET: end
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Sand Path near Farm
MOOD: Observant, Startled
CHARACTERS: Narrator, Regan, Evelyn Abbott
BACKGROUND_IMAGE: farm_sand_path.png
BACKGROUND_EDIT: "Daytime, sandy path, farm background, toy shuttle"

::SCRIPT::
- CHARACTER: Narrator
  LINE: re 2 large gouges in the fuselage.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Suddenly... Something startles her as she snaps her head to the side!
  EXPRESSION: Surprised
- CHARACTER: Narrator
  LINE: WE GO CLOSE on her hand driving the TOY SHUTTLE into the sand, not wanting it to be seen. Now ONLY THE SHUTTLE’S TAIL is exposed in the foreground as we see a figure walking toward REGAN.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Coming into focus is her mother. This is EVELYN ABBOTT.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: EVELYN too has changed. Hair longer, frame lower. She carries a basket of vegetables. She is barefoot.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: EVELYN stops and looks down at her daughter giving her a comforting smile. REGAN can’t seem to return the same.
  EXPRESSION: Sad
- CHARACTER: Narrator
  LINE: EVELYN gently gestures with her head. REGAN nods and EVELYN walks on. After a moment REGAN places the TOY SHUTTLE into the large pocket in her dress and follows her mother. As she goes:
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: WE PAN TO FOLLOW REGAN as she joins her mother and then SLOWLY RISE to reveal that the two women are walking along. A LONG AND WIDE SAND PATH IN THE MIDDLE OF A FARM! In the distance we can see they are heading to A WEATHERED RED BARN.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: WE END OUR RISE just as we reveal in the foreground, Christmas lights? Like parallel telephone wires, 2 cables of large bulbs, one with red and one with white. They dance playfully in the wind.
  EXPRESSION: null

::PATHS::
- CHOICE: "Follow Evelyn"
  TARGET: farm_path_to_barn
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Truck Interior
MOOD: Somber, Apathetic
CHARACTERS: Narrator, Marcus Abbott
BACKGROUND_IMAGE: truck_interior.png
BACKGROUND_EDIT: "Late afternoon, steering wheel close-up, orange sky reflection"

::SCRIPT::
- CHARACTER: Narrator
  LINE: CLOSE UP PROFILE of a steering wheel in the foreground. A weathered CHEVY emblem reflects the fire orange sky in the background.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: HANDS come into frame and gently grip the steering wheel. The right hand then slowly moves to the ignition block and turns.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: There is no sound. After a moment, the hand turns again again without sound. The hand turns a third time, this time, the hand begins to bob ever so slightly, as if the old car has started up. As the hand retracts:
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: WE PULL BACK to reveal... The little brother. This is MARCUS ABBOTT, now 10. Moving ever so slightly, MARCUS is obviously pretending to drive, though his impassive face betrays the idea that he is having any fun. MARCUS seems to have aged much more than the mere 2 years. His vacant eyes tell us a large toll has been taken on him, though perhaps not as easily recognizable on the exterior.
  EXPRESSION: Sad

::PATHS::
- CHOICE: "Continue driving"
  TARGET: farm_vehicle_graveyard
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Farm Vehicle Graveyard
MOOD: Eerie, Anticipatory
CHARACTERS: Narrator, Dark Figure
BACKGROUND_IMAGE: farm_vehicle_graveyard.png
BACKGROUND_EDIT: "Late afternoon, sand path, high grass, abandoned farm equipment"

::SCRIPT::
- CHARACTER: Narrator
  LINE: WE MOVE SLOWLY IN POV along another large sand path with high grass on either side when suddenly it opens up into a large clearing and we see a tractor? Shells of untouched farm equipment litter the open area.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: WE SLOWLY MOVE LEFT, making our way through, what is now nothing more than an eerie farming vehicle graveyard.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Suddenly, A DARK FIGURE ENTERS THE FRAME.
  EXPRESSION: null

::PATHS::
- CHOICE: "Observe the figure"
  TARGET: truck_interior_figure_appears
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Truck Interior
MOOD: Focused, then Alarmed
CHARACTERS: Narrator, Marcus Abbott, Dark Figure
BACKGROUND_IMAGE: truck_interior_rearview.png
BACKGROUND_EDIT: "Late afternoon, Marcus driving, rearview mirror showing figure"

::SCRIPT::
- CHARACTER: Narrator
  LINE: MARCUS’s hands move silently along the steering wheel as he stares out the windshield. His body moves ever so slightly, his face, relaxes, the hint of a smile. For a moment we could almost believe he is driving. His eyes routinely check the side mirror, then the rearview mirror, then stop. His hands, and face fall.
  EXPRESSION: Surprised
- CHARACTER: Narrator
  LINE: THROUGH THE REAR VIEW MIRROR, we see a figure standing behind the truck amidst the sea of farm equipment. Behind the figure we see, A TOWERING SILO.
  EXPRESSION: null

::PATHS::
- CHOICE: "Exit the truck"
  TARGET: truck_exterior_marcus_exits
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Truck Exterior / Driveway
MOOD: Somber, Revealing
CHARACTERS: Narrator, Marcus Abbott, Lee Abbott
BACKGROUND_IMAGE: truck_exterior_driveway.png
BACKGROUND_EDIT: "Late afternoon, vintage Chevy pickup, descending driveway, farm equipment, silo"

::SCRIPT::
- CHARACTER: Narrator
  LINE: OVER THE DARK FIGURE onto the truck as we see MARCUS expertly slip out of the cab window of a VINTAGE CHEVY PICKUP that sits at the edge of a DESCENDING DRIVEWAY connecting to the road that heads back toward the BARN. He lands in the sand without a sound and begins to walk, head held low, toward the dark figure, who reaches his hand out and briefly touches Marcus’ shoulder. Marcus walks straight past.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: As MARCUS exits we BOOM UP the dark figure as it turns, revealing LEON ABBOTT (LEE), 38.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: LEE too has changed, though much more obviously. He has lost weight on his strong farmer frame, he wears a beard and his sunken eyes indicate that he hasn’t slept well in a long time.
  EXPRESSION: Sad
- CHARACTER: Narrator
  LINE: WE PULL BACK WIDE to reveal the sea of farm equipment sits in front of a long, dilapidated, work shed roof a makeshift repair shop. The word ‘REPAIR’ is written in flaking white paint that clings to the wood above.
  EXPRESSION: null

::PATHS::
- CHOICE: "Walk towards the barn"
  TARGET: barn_exterior
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Barn Exterior
MOOD: Peaceful, then Purposeful
CHARACTERS: Narrator, Marcus Abbott
BACKGROUND_IMAGE: barn_exterior.png
BACKGROUND_EDIT: "Sunset, weathered red barn, open doors, Christmas lights in foreground"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The line of Christmas lights dance in the foreground.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: WE TILT DOWN to see that the lights run right in between two towering doors of a weathered red BARN. The doors have been left open by a gap of just over 2 feet. The edges of the doors are wrapped in foam.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Suddenly MARCUS walks into frame and enters the barn.
  EXPRESSION: null

::PATHS::
- CHOICE: "Enter the barn"
  TARGET: barn_interior
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Barn Interior
MOOD: Enclosed, Quiet
CHARACTERS: Narrator, Marcus Abbott
BACKGROUND_IMAGE: barn_interior.png
BACKGROUND_EDIT: "Sunset, barn interior, high ceiling, unilluminated Christmas lights, heavy quilts at entry"

::SCRIPT::
- CHARACTER: Narrator
  LINE: WE TILT DOWN from the lines of unilluminated Christmas lights running below the high reaching ceiling and ONTO MARCUS’ BACK as he walks through two heavy quilts at the entry of the barn hanging from the ceiling. Through the quilts, a dirt floor guides us through this
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue deeper into the barn"
  TARGET: deep_barn
  STATE_CHANGE: null
  CONDITION: null





::SCENE::
LOCATION: Farm / Silo / Ridge (Outdoors)
MOOD: Mysterious
CHARACTERS: Narrator, Lee
BACKGROUND_IMAGE: farm_sundown.png
BACKGROUND_EDIT: "Sundown, Christmas lights illuminating paths, distant fires on ridge, vast landscape"

::SCRIPT::
- CHARACTER: Narrator
  LINE: white Christmas lights flicker on, this time revealing a path that connects the weathered red BARN to an old white FARMHOUSE. Then another line of lights and another! Like the image of a city power grid coming back to life, we see a labyrinth of countless sand paths, meticulously laid out, illuminate all over the farm in a beautiful expanse.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: NOW IN PROFILE, LEE stares down seemingly at nothing. The unfiltered cigarette burns to his fingers, causing LEE to snap out of his stupor. He looks around at the horizon, it is officially sundown.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: He reaches for a plastic bottle of lighter fluid and sprays all its contents into a shallow metal drum in front of him.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Another cigarette appears from below frame. He puts it in his mouth and then reaches his hands into his jacket. His right arm jiggles slightly. There is no sound. His arm jiggles again. Then from his jacket, LEE pulls a FULLY LIT LIGHTER, that he protects from the wind. He lights his cigarette and then leans his hands to the metal drum A HUGE FLAME ERUPTS.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: In the glowing orange we see LEE take a long drag of his cigarette. His face has no effect. After several moments the flame begins to weaken and slowly fade.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Suddenly, far FAR off in the distance on the ridge ANOTHER FLAME ILLUMINATES. LEE doesn’t even look up. Then, miles past the first ANOTHER FLAME! THEN ANOTHER! Until we can see behind LEE 5 glowing fires scattered far off across the ridge.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: ON LEE as he glances over and registers, then back to staring front as we: MOVE AROUND BEHIND him to see where his gaze is focused.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Then, we see it. There, in his left hand LEE holds a 5X6 nursery school photo of a 4 year old boy.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: LEE takes a last drag of his cigarette and then places the photo in a small box at his feet.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: WE ARE TIGHT ON THE BOX as LEE stands and walks toward two curved bars on the side of the SILO. He turns around and begins to descend A LADDER.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: WE HOLD ON THE SMALL BOX, then just as LEE’s head disappears WE SLOWLY BEGIN TO RISE.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Now looking at the opposite side of the ridge than we did in the beginning, the rising moon’s light now spills across the vista of rock and trees and onto an enormous and bizarrely out of place CRATER!
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: WE HOLD ON THE CRATER FOR A LONG MOMENT Then:
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue following Lee"
  TARGET: barn_living_room
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Barn - Living Room (Makeshift Kitchen Area)
MOOD: Resourceful
CHARACTERS: Narrator, Evelyn
BACKGROUND_IMAGE: barn_living_room_kitchen.png
BACKGROUND_EDIT: "Nighttime, makeshift kitchen, shelves with paper goods, workbench, mid-70s refrigerator"

::SCRIPT::
- CHARACTER: Narrator
  LINE: WE ARE CLOSE on a small mound of dirt. Suddenly two hands covered in winter gloves enter frame and begin to dig down about 3 inches to reveal a plank of wood.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: WIDER NOW, we see EVELYN on her hands and knees just behind the living room set up in an open, very makeshift kitchen.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: One wall of shelves cluttered with stacks of paper plates, bowls and cups. Another wall is a workbench acting as a countertop and a mid 70’s refrigerator.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: EVELYN extracts from the dirt a long wooden box. Beneath it red hot rocks let off a combination of steam and smoke.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: EVELYN brings the box to the counter top and carefully lifts the lid to reveal a perfectly cooked fish with lemon and rosemary and garlic scattered all around.
  EXPRESSION: null

::PATHS::
- CHOICE: "Prepare for dinner"
  TARGET: barn_bedrooms
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Barn - Bedrooms (Horse Stalls)
MOOD: Somber
CHARACTERS: Narrator, Regan, Lee
BACKGROUND_IMAGE: barn_bedrooms.png
BACKGROUND_EDIT: "Nighttime, row of horse stall bedrooms, long trough-like sink"

::SCRIPT::
- CHARACTER: Narrator
  LINE: WE TRACK with REGAN as she walks down the row of horse stall bedrooms.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: REGAN arrives at the threshold of LEE and EVELYN’s bedroom.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: LEE is faced away from her, washing his face in a long trough like sink that runs the length of the room. Suddenly, through the mirror leaning on the wall, LEE sees her, but does not turn.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Through the mirror, the two of them looking silently at each other for a moment too long, it is heartbreaking.
  EXPRESSION: null
- CHARACTER: Regan
  LINE: eating
  EXPRESSION: Suggesting
- CHARACTER: Narrator
  LINE: As LEE nods, trying to muster a polite smile we can see very clearly something is broken.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: LEE wipes his face with a towel and then turns to face an empty doorway.
  EXPRESSION: null

::PATHS::
- CHOICE: "Go to dinner"
  TARGET: barn_table
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Barn - Table
MOOD: Quiet
CHARACTERS: Narrator, Evelyn, Lee, Regan, Marcus
BACKGROUND_IMAGE: barn_table.png
BACKGROUND_EDIT: "Nighttime, old workbench as table, family eating without plates or utensils"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The family sits down together for dinner around an old workbench. Their heads bowed in prayer, after a moment EVELYN lifts her head and they begin to eat. There are no plates.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The food sits on various children’s plastic placemats. There are no utensils. The family uses only bread to collect food.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: We slowly pull back on this silent, but comfortingly familiar scene.
  EXPRESSION: null

::PATHS::
- CHOICE: "Finish dinner"
  TARGET: barn_living_room_monopoly
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Barn - Living Room (Monopoly Area)
MOOD: Quiet
CHARACTERS: Narrator, Regan, Marcus
BACKGROUND_IMAGE: barn_living_room_monopoly.png
BACKGROUND_EDIT: "Nighttime, dim oil lantern light, Monopoly board with homemade pieces"

::SCRIPT::
- CHARACTER: Narrator
  LINE: REGAN and MARCUS lie on the floor playing Monopoly.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: By the dim light of an oil lantern, we can see the game’s board is the same, but the pieces are small colored bobbles of wool, the kind you would find on a children’s Christmas sweater. The houses and hotels are empty sugar packets, blue and pink. And the money? Small pieces of green, red, blue and orange fabric rectangles, all equally sized.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: MARCUS is five spaces away from his sister’s hotel on Boardwalk.
  EXPRESSION: null

::PATHS::
- CHOICE: "End of excerpt"
  TARGET: end
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Farmhouse Interior
MOOD: Playful, then Terrified, then Tense, then Relieved, then Terrified again
CHARACTERS: Narrator, Marcus, Regan, Lee
BACKGROUND_IMAGE: farmhouse_interior.png
BACKGROUND_EDIT: "Dimly lit, makeshift side table with crates, dirt floor, oil lantern"

::SCRIPT::
- CHARACTER: Narrator
  LINE: He takes a sip of water and places the cup on top of a tall crate being used as a makeshift side table.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: MARCUS looks at his sister, who can’t hide her smile. He mimes a prayer before rolling the dice on the dirt floor, where it makes no noise 5!
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: MARCUS slowly looks up to REGAN, knowing his fate.
  EXPRESSION: Apprehensive
- CHARACTER: Narrator
  LINE: REGAN smiles pointedly and then reaches for MARCUS’ money.
  EXPRESSION: Victorious
- CHARACTER: Narrator
  LINE: As MARCUS thrusts his arm back to protect his bank, his elbow hits the oil lantern!!
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: A BOOMING CRASH!!!! As the oil lantern hits the ground and shatters. THE SOUND FEELS HUGE! AS IT IS THE FIRST BIG SOUND WE’VE HEARD! FIRE ERUPTS ON THE FLOOR!!! The children stare frozen in horror!
  EXPRESSION: Horrified
- CHARACTER: Narrator
  LINE: LEE immediately jumps up from the table and instinctively grabs a quilt and throws it on the fire. With a few silent pats the fire is gone.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: SILENCE. EVERYONE FREEZES!!!! NO ONE IS BREATHING!!!
  EXPRESSION: Terrified
- CHARACTER: Narrator
  LINE: REGAN shoots MARCUS a look of concern.
  EXPRESSION: Concerned
- CHARACTER: Narrator
  LINE: MARCUS shoots LEE a look of terror.
  EXPRESSION: Terrified
- CHARACTER: Narrator
  LINE: LEE shoots a look to the roof.
  EXPRESSION: Alert
- CHARACTER: Narrator
  LINE: ON LEE as he stands up INTO frame. He has almost physically transformed from a man into protection incarnate. He slowly raises a stiff finger to his lips, his body so tense, it looks painful. This is the unwanted version of himself that lies just millimeters under his skin 24 hours a day.
  EXPRESSION: Intense
- CHARACTER: Narrator
  LINE: After a long moment nothing. It would have happened by now.
  EXPRESSION: null
- CHARACTER: Lee
  LINE: (nods that everything is OK)
  EXPRESSION: Relieved
- CHARACTER: Narrator
  LINE: MARCUS stares at REGAN with a painfully apologetic face as she leans in and touches his hand.
  EXPRESSION: Apologetic
- CHARACTER: Narrator
  LINE: BANG!!! The whole family startles in silence!!!
  EXPRESSION: Startled
- CHARACTER: Narrator
  LINE: Something has hit the roof.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: EVERYONE IS FROZEN LOOKING AT THE CEILING.
  EXPRESSION: Wary
- CHARACTER: Narrator
  LINE: Seconds later a high pitched SHRIEEEEEEK of CLAWS sliding down the aluminum roof. The family follows the sound exactly with their eyes. Then silence.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: LEE crouches down and walks to a small window where the sound stopped above.
  EXPRESSION: null
- CHARACTER: Marcus
  LINE: (wildly shakes his head “no”, evidence of his traumatic anxiety resurfacing)
  EXPRESSION: Anxious
- CHARACTER: Narrator
  LINE: REGAN slowly stands, looking on with wide eyes.
  EXPRESSION: Wary
- CHARACTER: Narrator
  LINE: LEE arrives at the window, crouched. From his low vantage point we can see the lip of the gutter and the eerily swaying Christmas lights.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: LEE begins to stand up slowly, his face now virtually pressed against the glass.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Suddenly, A WHIR OF SCREECHING AND GROWLING!!! A LARGE SHAPE FALLS PAST THE WINDOW!!!!
  EXPRESSION: Startled

::SCENE::
LOCATION: Cornfield
MOOD: Terrifying, Violent
CHARACTERS: Narrator
BACKGROUND_IMAGE: cornfield.png
BACKGROUND_EDIT: "Moonlit path, dark cornfield"

::SCRIPT::
- CHARACTER: Narrator
  LINE: As two raccoons hit the ground, fighting then scamper off into the dark.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: LEE somehow exhales slowly and calmly a trick that, no doubt, took much practice and walks away from the window.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The two raccoons round the corner onto a moonlit path heading toward camera, just as they come into CLOSE UP.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: A GIANT BLACK CLAW CRUSHES DOWN ONTO THE FIRST RACCOONS HEAD and then rips it out of frame. We hold on the second raccoon running off with a soft but piercing scream.
  EXPRESSION: Terrified

::SCENE::
LOCATION: Farm - Night
MOOD: Eerie, Mysterious
CHARACTERS: Narrator
BACKGROUND_IMAGE: farm_overview.png
BACKGROUND_EDIT: "High angle shot of farm, sand path, red barn, white farmhouse, telephone pole with bird silhouettes"

::SCRIPT::
- CHARACTER: Narrator
  LINE: It is night. From high above, we look down to the sand path between the RED BARN and the WHITE FARMHOUSE. In the foreground we see the shadow of a telephone pole. Sitting on the wire in silhouette are BIRDS.
  EXPRESSION: null

::SCENE::
LOCATION: Sand Path - Night
MOOD: Eerie, Silent, Mysterious
CHARACTERS: Narrator, Evelyn (silhouette)
BACKGROUND_IMAGE: sand_path.png
BACKGROUND_EDIT: "Ground view, farmhouse in distance, odd colors, overexposed foreground, tiny dots flying"

::SCRIPT::
- CHARACTER: Narrator
  LINE: FROM THE GROUND, we see the FARMHOUSE in the distance, but something is different. The color seems wrong, the angle is odd. The foreground is over exposed and tiny dots fly in and out of the frame.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Suddenly, A GIANT FOOTSTEPS INTO FRAME!!!!
  EXPRESSION: Startled
- CHARACTER: Narrator
  LINE: AND THEN ANOTHER as we watch two bare feet then the hem of a dress and then the silhouette of EVELYN walk silently toward the house.
  EXPRESSION: null

::SCENE::
LOCATION: Farmhouse - Basement - Night
MOOD: Suspenseful, Prepared, Mysterious
CHARACTERS: Narrator
BACKGROUND_IMAGE: farmhouse_basement.png
BACKGROUND_EDIT: "Night, wall of security monitors, workbench with notebooks and newspapers, cinder block wall"

::SCRIPT::
- CHARACTER: Narrator
  LINE: WE SLOWLY PULL BACK from THAT SAME SHOT of the FARMHOUSE and reveal a plastic frame, a red light buttons. We realize this image is being viewed on a small monitor. CCTV FOOTAGE from A SECURITY CAMERA.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: WE CONTINUE TO PULL BACK SLOWLY as another monitor comes into frame with another stacked on top of it then one next to it and another until we reveal, like something out of a Dr. Seuss book, a wall of 20 TV’s, all shapes and brands sit on top of a large workbench covered with open notebooks and sliced up newspapers.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: On each screen we see elements of trees... sand paths... the barn... the silo. This is a DIY version of a security console that overlooks the entire farm... and it has taken a long time to put together.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: WE BEGIN TO TRACK past the empty security console and onto a cinder block wall, covered in notes and newspaper clippings.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Then WE BARELY HEAR A TINY, ALMOST FAMILIAR, SOUND.
  EXPRESSION: Alert
- CHARACTER: Narrator
  LINE: THEN A HANDFUL OF SMALL BEEPING SOUNDS.
  EXPRESSION: Alert
- CHARACTER: Narrator
  LINE: Suddenly a portion of one visible newspaper clipping shows a close up and much more detailed image of the enormous crater. The headline reads: ‘NUMBER OF CONFIRMED GLOBAL LANDING SITES GROWS TO 128’ A post-it note sticks to the clip.
  EXPRESSION: null

::SCENE::
LOCATION: Farmhouse Basement - Workbench
MOOD: Urgent, Investigative, Hopeful
CHARACTERS: Narrator, Lee
BACKGROUND_IMAGE: basement_workbench.png
BACKGROUND_EDIT: "A cluttered, dimly lit workbench covered with research materials and electronic equipment"

::SCRIPT::
- CHARACTER: Narrator
  LINE: We pass by a clipping that reads: LANDED 10-18-2018.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: We pass by more clippings, catching glimpses of dramatic headlines and surreal images: ‘PRESIDENT CALLS FOR EMERGENCY EVAC IN ALL MAJOR CITIES’ ‘CHURCHES, MOSQUES, TEMPLES FLOODED WITH PEOPLE’.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: We pass by a grainy newspaper photo of a military stand off with one creature. The headline reads: ‘MILITARY EXPERTS AGREE: “INDESTRUCTIBLE”’.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Again we hear that familiar sound as it gets louder.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: We continue to travel as a map enters frame. Like one you would get at a gas station, it is covered in illustrated forests and rivers, it is a map of The State of New York.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The portion above Manhattan is covered in hand drawn red circles and pins, each accompanied with a date and names of the dead.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: We move further along to reveal low quality stills of security footage barely showing The Creature. Each still is drawn on and analyzed.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Then a large white board covered in writing comes into frame, leaning against the wall.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Amidst the scratches of written and rewritten thoughts, we can make out two lists labeled, ‘QUESTIONS’ and ‘CONFIRMED’.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: In the ‘QUESTIONS’ column are listed; ”NO DEMANDS?”, “NO SIGN OF ORGANIZATION”, “BLIND?” “HOW MANY?” “SOUND?" "WHY NOT ATTACK ALL SOUND?”
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: In the ‘CONFIRMED’ column are phrases like; “4-6 CONFIRMED IN PACK”, “DO NOT ATTACK SMALL SOUNDS”.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Then we see the phrase “DO NOT EAT KILL”.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: We move to the very bottom of the white board where we see the word “WEAPON???”.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Listed below words are crossed out “EXPLOSIVES”, “FIRE”, “CHEMICAL”.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Again we hear that familiar sound now louder.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Then again the handful of small beeping sounds.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: We move off of the white board and scan past anatomical drawings of a shark sensing prey using magnetic fields, dolphins navigating through minefields, the electromagnetic spectrum and finally images of the inner ear.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: We now move through meticulously organized shelves covered in tools and wires and various pieces of salvaged electronic equipment and finally onto Lee’s back.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: He is hunched over the workbench working intensely on something, he is wearing large black headphones.
  EXPRESSION: Focused
- CHARACTER: Narrator
  LINE: We see him reach out of frame as we push past an old microphone that is connected to an old transatlantic ham radio.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: In the glowing light from the box we see all kinds of knobs and needles. Below a switch labeled with two stickers that say “RADIO” and “SPEAKER”, Lee’s hand comes into frame and turns a large knob revealing the source of our familiar sound.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Lee is searching for a signal. Any sign. Any sign of life.
  EXPRESSION: Hopeful
- CHARACTER: Narrator
  LINE: Suddenly, he presses down on a button on the microphone.
  EXPRESSION: Determined
- CHARACTER: Narrator
  LINE: The handful of small beeping sounds is Morse Code.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: There is no response.
  EXPRESSION: Sad
- CHARACTER: Narrator
  LINE: We follow Lee’s hand off of the button and onto a small soldering iron. As he picks it up, we go to Lee at his workspace.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: With magnifying glasses in front of his eyes, he works with surgery like precision on a small contraption. A small string of smoke rises from his work.
  EXPRESSION: Focused

::PATHS::
- CHOICE: "Continue working"
  TARGET: farmhouse_basement_steps
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Farmhouse Basement - Steps
MOOD: Tender, Anticipatory, Hopeful
CHARACTERS: Narrator, Evelyn, Lee
BACKGROUND_IMAGE: basement_steps.png
BACKGROUND_EDIT: "Warmly lit stairwell leading down to a basement workbench, evening"

::SCRIPT::
- CHARACTER: Narrator
  LINE: We are over the warmly, lit from above, stairwell with Lee at his workstation in the background as delicate bare feet touch down softly, and deliberately on the steps, like a child knowing where to step so they don’t wake their parents.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: We boom up to reveal Evelyn as she stares at her husband, who hasn’t heard her, worried? Admiring? Lost?
  EXPRESSION: Worried
- CHARACTER: Narrator
  LINE: A flicker of a memory echoes through her face as she smiles and then walks to him. Evelyn is wearing earbuds.
  EXPRESSION: Happy
- CHARACTER: Narrator
  LINE: On Lee as a hand touches down gently on his shoulder, he doesn’t flinch at all. There is immediate recognition there. Safety.
  EXPRESSION: Calm
- CHARACTER: Narrator
  LINE: The hands then reach down and remove Lee’s headphones. The sound of the searching radio in the headphones is nearly inaudible.
  EXPRESSION: null
- CHARACTER: Lee
  LINE: (Sits back and holds up a hearing aid. It looks like a somewhat common hearing aid, but with handcrafted modifications, upgrades. There is a wire extension that extends from the top, almost like an adapter or plug.)
  EXPRESSION: Neutral
- CHARACTER: Narrator
  LINE: The hands gently grab Lee’s face and turn it. Lee looks up at Evelyn who he now sees is wearing lipstick, has pulled her hair back and has changed into a beautiful dress. This is date night.
  EXPRESSION: Surprised
- CHARACTER: Lee
  LINE: (Smiles as Evelyn takes a step back and with the gentlest of movements, she sweetly beckons him to her.)
  EXPRESSION: Happy
- CHARACTER: Lee
  LINE: (Looks back at his work for just a moment, his face once again focused. Then he lays the hearing aid down on the table and stands up.)
  EXPRESSION: Focused
- CHARACTER: Narrator
  LINE: We hold on the hearing aid and then slowly pull back to reveal a pile of more hearing aids, each with a variety of different modifications, scattered all around his work bench. This is something he has been working on for a long while.
  EXPRESSION: null

::PATHS::
- CHOICE: "Go on a date with Evelyn"
  TARGET: end_of_scene
  STATE_CHANGE: relationship_lee_evelyn = +1, hope = +1
  CONDITION: null

::SCENE::
LOCATION: Basement
MOOD: Intimate, then concerned
CHARACTERS: Lee, Evelyn, Narrator
BACKGROUND_IMAGE: basement_workshop.png
BACKGROUND_EDIT: "Dimly lit basement, workbench visible, two people embracing"

::SCRIPT::
- CHARACTER: Narrator
  LINE: WE TILT UP from the workbench to see LEE arrive at his wife’s side as she puts her hand up on his neck and smiles up at him warmly, as if there is no where else to be nothing to make her happier.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: FACE TO FACE NOW, LEE finally allows a smile, looking down at his time tested partner.
  EXPRESSION: Happy
- CHARACTER: Narrator
  LINE: EVELYN’s eyes close as she places her forehead to his and the two begin to gently sway in total silence.
  EXPRESSION: Peaceful
- CHARACTER: Narrator
  LINE: Suddenly, EVELYN takes LEE’s hands from around her back and places them on her protruding belly. After a moment she looks up lovingly at her husband to see
  EXPRESSION: Loving
- CHARACTER: Narrator
  LINE: LEE’S SMILE HAS DISAPPEARED. STARING DOWN AT THE BELLY, HIS FACE LOOKS LOST.
  EXPRESSION: Concerned
- CHARACTER: Narrator
  LINE: Knowing this man inside and out, EVELYN keeps her gaze firmly into her husband’s eyes and slowly moves her hands up LEE’S arms and gently onto his face. Holding more than his visage in her hands, LEE finally looks up at her.
  EXPRESSION: Understanding
- CHARACTER: Narrator
  LINE: EVELYN smiles with recognition of the man she married as her right hand travels to her right ear. She removes the earbud from her ear and seamlessly places it in his, as: MUSIC RUSHES IN! The only record on the record player, this is the song they were married to. This is NEIL YOUNG’S HARVEST MOON, 21.
  EXPRESSION: Happy
- CHARACTER: Narrator
  LINE: Perhaps it’s due to the lack of sound thus far in the movie or maybe the marrying image of the two dancing, but the sounds of the song are crystal clear. We can perfectly hear every chord, every tremor of vocal chord as we PULL BACK on this perfect moment through the basement to the small rectangular basement window to reveal water hitting the glass.
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue"
  TARGET: farmhouse_exterior_night
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Farmhouse Exterior
MOOD: Somber
CHARACTERS: Narrator
BACKGROUND_IMAGE: farmhouse_exterior_night.png
BACKGROUND_EDIT: "Nighttime, strong rain pouring down around the house"

::SCRIPT::
- CHARACTER: Narrator
  LINE: We see a strong rain pouring down around the house.
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue"
  TARGET: farm_exterior_morning
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Farm Exterior
MOOD: Peaceful
CHARACTERS: Narrator
BACKGROUND_IMAGE: farm_exterior_morning.png
BACKGROUND_EDIT: "Beautiful, crisp morning after the rain"

::SCRIPT::
- CHARACTER: Narrator
  LINE: A beautiful crisp morning.
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue"
  TARGET: farmhouse_sand_path_day
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Farmhouse Sand Path
MOOD: Diligent
CHARACTERS: Lee, Narrator
BACKGROUND_IMAGE: farmhouse_sand_path.png
BACKGROUND_EDIT: "Daytime, water dripping, sand path with a stream"

::SCRIPT::
- CHARACTER: Narrator
  LINE: FROM THE PORCH of the farmhouse, as water drips down from overhead, WE SLOWLY travel along the sand path toward the barn when suddenly we arrive at a small stream of water cutting right through a, now washed away, segment of the sand path.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Suddenly LEE’s bare feet enter frame and then a large hiking backpack enters frame next to him.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: ON LEE as we see a momentary glimpse into the painstaking, and never ending, workload that goes into maintaining this farm.
  EXPRESSION: Focused
- CHARACTER: Narrator
  LINE: CLOSE on hands as LEE’s bare fingers gouge into the unforgiving earth at the edge of the sand path to divert the water. Stones come into frame to form a temporary wall. Then LEE hoists, the very obviously heavy, hiking bag onto his knee. He then slowly and silently undoes a handmade flap at the bottom of the backpack. From the opening of the bag pours SAND.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Quickly and silently, sand piles up on the ground as we witness for the first time, LEE’s ingenious system that has kept his family safe all this time.
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue"
  TARGET: barn_safe_room_day
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Barn Safe Room
MOOD: Tense, hopeful
CHARACTERS: Evelyn, Narrator
BACKGROUND_IMAGE: barn_safe_room.png
BACKGROUND_EDIT: "Daytime, Evelyn sitting on a hay bale, medical supplies visible"

::SCRIPT::
- CHARACTER: Narrator
  LINE: CLOSE UP OF A GAUGE Very faint bursts of air can be heard.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: WE SLOWLY PULL BACK to reveal EVELYN sitting on a hay bale with a blood pressure sleeve on her arm and a stethoscope in her ears. Behind her is a shelf full of bandages and IV bags. 22.
  EXPRESSION: Cautious
- CHARACTER: Narrator
  LINE: She stops pumping the bulb, stares down at the gauge and then gently lets the air out and removes the sleeve.
  EXPRESSION: Focused
- CHARACTER: Narrator
  LINE: EVELYN marks her daily blood pressure on a calendar next to her. On this calendar we see her estimated due date is 4 weeks away.
  EXPRESSION: Diligent
- CHARACTER: Narrator
  LINE: After a moment, she leans over and places the bottom part of the stethoscope onto her belly.
  EXPRESSION: Listening
- CHARACTER: Narrator
  LINE: A faint sound of adjusting and then LUB DUB, LUB DUB, THE BABY’S HEARTBEAT ENGULFS US!!!
  EXPRESSION: Hopeful

::PATHS::
- CHOICE: "Continue"
  TARGET: farmhouse_exterior_day
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Farmhouse Exterior
MOOD: Eerie, suspenseful
CHARACTERS: Regan, Narrator
BACKGROUND_IMAGE: farmhouse_exterior_day.png
BACKGROUND_EDIT: "Daytime, sand path leading to the front door of the farmhouse"

::SCRIPT::
- CHARACTER: Narrator
  LINE: WE CREEP SLOWLY ALONG the sand path heading toward the front door of the FARMHOUSE.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Suddenly REGAN steps into frame, walking deliberately, as if tiptoeing.
  EXPRESSION: Cautious

::PATHS::
- CHOICE: "Continue"
  TARGET: farmhouse_interior_day
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Farmhouse Interior
MOOD: Tense, precise
CHARACTERS: Regan, Narrator
BACKGROUND_IMAGE: farmhouse_interior_day.png
BACKGROUND_EDIT: "Daytime, worn wood floor with deliberate painted markings near the front door"

::SCRIPT::
- CHARACTER: Narrator
  LINE: REGAN reaches the front door of the FARMHOUSE and stops at the threshold. As she looks down at the worn wood floor, scanning, we can notice deliberately painted markings on the floor.
  EXPRESSION: Observant
- CHARACTER: Narrator
  LINE: Just then, REGAN takes a dramatically long step inside, placing her foot down directly on the first colored marking silence. Looking almost relieved, REGAN once again scans the floor and then focuses on another marking. She takes another long step, this time far to her right and touches down on the next marking silence. It almost looks like she’s playing ‘TWISTER’. Getting more confident, she scans the room, finds another spot and steps quickly.
  EXPRESSION: Cautious

::PATHS::
- CHOICE: "Continue"
  TARGET: farmhouse_basement_stairs_day
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Farmhouse Basement Stairs
MOOD: Climactic, terrifying
CHARACTERS: Regan, Dark Figure, Narrator
BACKGROUND_IMAGE: farmhouse_basement_stairs.png
BACKGROUND_EDIT: "Daytime, dark stairwell leading up to a warm hallway"

::SCRIPT::
- CHARACTER: Narrator
  LINE: WE LOOK DIRECTLY up the basement stairs toward the warm hallway at the top.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Suddenly, REGAN takes a long step into frame. Her silhouette looks down the dark stairwell.
  EXPRESSION: Hesitant
- CHARACTER: Narrator
  LINE: After a moment, she slowly puts her foot down on the first step when suddenly A DARK FIGURE APPEARS BEHIND HER AND GRABS HER!!!
  EXPRESSION: Terrified

::PATHS::
- CHOICE: "Continue"
  TARGET: end
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Farmhouse
MOOD: Tense
CHARACTERS: Regan, Lee, Narrator
BACKGROUND_IMAGE: farmhouse.png
BACKGROUND_EDIT: "Daytime, sand path, rural setting"

::SCRIPT::
- CHARACTER: Narrator
  LINE: CLOSE ON REGAN as she is placed down onto the sand path.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: A HAND COVERS HER MOUTH!
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: AS REGAN spins around we see LEE kneeling in front of her.
  EXPRESSION: null
- CHARACTER: Lee
  LINE: (SIGNING) You CANNOT go down there!
  EXPRESSION: Concerned
- CHARACTER: Regan
  LINE: (SIGNING) WHY NOT???
  EXPRESSION: Frustrated
- CHARACTER: Lee
  LINE: (SIGNING) You know why.
  EXPRESSION: Firm
- CHARACTER: Regan
  LINE: (SIGNING) I won’t make a sound!!! I’m not a child!!!
  EXPRESSION: Angry
- CHARACTER: Narrator
  LINE: LEE pauses that line stings.
  EXPRESSION: null
- CHARACTER: Lee
  LINE: (SIGNING) Just--don’t.
  EXPRESSION: Resigned
- CHARACTER: Narrator
  LINE: The two stare into each other’s eyes communicating more than any sign language could.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Suddenly LEE reaches up to her face. His still dirty hands push the hair back over her right ear. It seems so uncharacteristically warm and gentle when suddenly LEE reaches into his pocket with his right hand and pulls out THE HEARING AID from the night before.
  EXPRESSION: null
- CHARACTER: Lee
  LINE: (SIGNING) This time, I was able to use small amplifiers from the stereo speaker to--
  EXPRESSION: Hopeful
- CHARACTER: Regan
  LINE: (SIGNING) It won’t work.
  EXPRESSION: Skeptical
- CHARACTER: Lee
  LINE: (SIGNING) No, our problem has always been power, but this should increase the frequency to--
  EXPRESSION: Explaining
- CHARACTER: Regan
  LINE: (SIGNING) It never works!!
  EXPRESSION: Frustrated
- CHARACTER: Lee
  LINE: (SIGNING) ... But we’ll keep trying til it does.
  EXPRESSION: Determined
- CHARACTER: Narrator
  LINE: REGAN looks up at him blankly as LEE reaches to bring the new hearing aid up to her ear when suddenly REGAN pushes his hand away.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: LEE reaches up to her ear to try again, REGAN pushes his hand away again, giving him a cold stare. With so much history behind it, it’s a bizarrely heartbreaking altercation.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: He tries again, she pushes again, even harder.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: LEE looks at his daughter as she looks at him, her venomous face, betrayed by the large tears that roll down her cheek.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: After a long moment, REGAN snatches the hearing aid from her father’s hand and walks away.
  EXPRESSION: null

::PATHS::
- CHOICE: "Regan walks away from Lee"
  TARGET: barn_hay_loft
  STATE_CHANGE: regan_frustration = +1, lee_sadness = +1
  CONDITION: null

::SCENE::
LOCATION: Barn Hay Loft
MOOD: Anxious
CHARACTERS: Marcus, Evelyn, Narrator
BACKGROUND_IMAGE: barn_hay_loft.png
BACKGROUND_EDIT: "Daytime, interior, curated area with desk and whiteboard"

::SCRIPT::
- CHARACTER: Narrator
  LINE: ON MARCUS’ back as he scribbles in a notebook. WE GO CLOSE to see MARCUS is writing in a math notebook. His pencil suddenly pauses, moves up the page through a long math problem and stops again. Suddenly a finger comes into frame and points at a different part of the problem.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: WE PULL OUT to reveal EVELYN and MARCUS sitting in a small curated area with a desk, book shelves and a white board covered in various phrases, shapes and equations. We suddenly realize EVELYN is HOME SCHOOLING him!
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: MARCUS suddenly nods and once again begins writing as EVELYN looks out the small door of the hay loft and down to the sand path below as LEE arrives. Suddenly...
  EXPRESSION: null
- CHARACTER: Marcus
  LINE: (SIGNING) ...please don’t make me go...
  EXPRESSION: Panicked
- CHARACTER: Narrator
  LINE: EVELYN looks over to see MARCUS’s face awash with panic.
  EXPRESSION: null
- CHARACTER: Evelyn
  LINE: (SIGNING) You will be fine. Your father will always protect you.
  EXPRESSION: Reassuring
- CHARACTER: Narrator
  LINE: MARCUS GRABS HER ARM TIGHT! IT STARTLES HER. With tears in his eyes, he mouths to her “PLEASE!”
  EXPRESSION: null
- CHARACTER: Evelyn
  LINE: (SIGNING) Listen to me. It is important that you learn these things. He just wants you to be able to take care of yourself.
  EXPRESSION: Serious
- CHARACTER: Narrator
  LINE: MARCUS looks at her.
  EXPRESSION: null
- CHARACTER: Evelyn
  LINE: (SIGNING) Take care of ME!
  EXPRESSION: Playful
- CHARACTER: Narrator
  LINE: EVELYN lightens the conversation by pretending to age in front of our eyes.
  EXPRESSION: null
- CHARACTER: Evelyn
  LINE: (SIGNING) ... when I’m old and grey...
  EXPRESSION: Playful
- CHARACTER: Narrator
  LINE: EVELYN leans on him. MARCUS can’t help but smile.
  EXPRESSION: null
- CHARACTER: Evelyn
  LINE: and I have no teeth.
  EXPRESSION: Playful
- CHARACTER: Narrator
  LINE: EVELYN pretending to have no teeth is too much for MARCUS to hold back his silent laugh.
  EXPRESSION: null

::PATHS::
- CHOICE: "Lee arrives at the barn"
  TARGET: barn_exterior
  STATE_CHANGE: marcus_anxiety = +1, evelyn_comfort = +1
  CONDITION: null

::SCENE::
LOCATION: Barn Exterior
MOOD: Resistant
CHARACTERS: Lee, Marcus, Evelyn, Regan, Narrator
BACKGROUND_IMAGE: barn_exterior.png
BACKGROUND_EDIT: "Daytime, outside the barn, sand path leading to woods"

::SCRIPT::
- CHARACTER: Narrator
  LINE: OVER LEE’S large shoulder we barely see MARCUS moving ever so slightly in one direction and then another.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: ON LEE, with a large hiking pack on his back. He adjusts the straps of a backpack on MARCUS.
  EXPRESSION: null
- CHARACTER: Lee
  LINE: (SIGNING) Too tight?
  EXPRESSION: Concerned
- CHARACTER: Marcus
  LINE: (SIGNING) No.
  EXPRESSION: Neutral
- CHARACTER: Lee
  LINE: (SIGNING) Good.
  EXPRESSION: Satisfied
- CHARACTER: Marcus
  LINE: (SIGNING) No, I don’t want to go.
  EXPRESSION: Resistant
- CHARACTER: Narrator
  LINE: LEE looks up at EVELYN. Then back to MARCUS.
  EXPRESSION: null
- CHARACTER: Lee
  LINE: (SIGNING) There’s nothing to be scared of.
  EXPRESSION: Reassuring
- CHARACTER: Marcus
  LINE: (SIGNING) Of course there is.
  EXPRESSION: Scared
- CHARACTER: Narrator
  LINE: Suddenly behind LEE we see REGAN appear.
  EXPRESSION: null
- CHARACTER: Regan
  LINE: (SIGNING) I’ll go.
  EXPRESSION: Determined
- CHARACTER: Narrator
  LINE: LEE looks over at his daughter and pauses.
  EXPRESSION: null
- CHARACTER: Lee
  LINE: (SIGNING) No, no. I need you to stay here and help your mother.
  EXPRESSION: Firm
- CHARACTER: Narrator
  LINE: LEE stands up. To EVELYN:
  EXPRESSION: null
- CHARACTER: Lee
  LINE: (SIGNING) We’ll be back before dinner.
  EXPRESSION: Reassuring
- CHARACTER: Regan
  LINE: (SIGNING) I want to go.
  EXPRESSION: Persistent
- CHARACTER: Lee
  LINE: (SIGNING) Just stay here. You’ll be safe.
  EXPRESSION: Protective
- CHARACTER: Narrator
  LINE: LEE turns to EVELYN who looks at him with slight disappointment.
  EXPRESSION: null
- CHARACTER: Lee
  LINE: (SIGNING) Next time.
  EXPRESSION: Consoling
- CHARACTER: Narrator
  LINE: LEE pauses and then kisses EVELYN. LEE and MARCUS walk down a sand path toward the woods.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: EVELYN turns to REGAN who is already walking away.
  EXPRESSION: null

::PATHS::
- CHOICE: "Lee and Marcus leave for the woods"
  TARGET: regans_room
  STATE_CHANGE: regan_frustration = +1, marcus_fear = +1, lee_resolve = +1
  CONDITION: null

::SCENE::
LOCATION: Barn, Regan's Room
MOOD: Frustrated
CHARACTERS: Regan, Narrator
BACKGROUND_IMAGE: regans_room.png
BACKGROUND_EDIT: "Daytime, interior, sparse bedroom with electronic equipment"

::SCRIPT::
- CHARACTER: Narrator
  LINE: REGAN enters and throws the hearing aid her father made her onto the dirt floor. This is the first time we have seen her bedroom. It is sparse. A hay bale covered in bed sheets, a small crate with a neat pile of books inside and several candles on top, a small wooden mirror leant against the wall.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: REGAN drops to her knees. On the ground we now see all kinds of electronic equipment and tools.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Architectural drawings are pinned to the wall. It is li
  EXPRESSION: null

::PATHS::
- CHOICE: "Regan starts working on her project"
  TARGET: end
  STATE_CHANGE: regan_determination = +1, regan_frustration = +1
  CONDITION: null

::SCENE::
LOCATION: Farmhouse - Regan's Room
MOOD: Disappointment
CHARACTERS: Regan, Narrator
BACKGROUND_IMAGE: regans_room.png
BACKGROUND_EDIT: "Daytime, makeshift workbench, packing clothes"

::SCRIPT::
- CHARACTER: Narrator
  LINE: REGAN grabs her pillow, rips the pillow case off and begins furiously packing.
  EXPRESSION: Angry
- CHARACTER: Narrator
  LINE: She grabs clothes, a water bottle, a notepad and the THE TOY SHUTTLE. She gets up to leave and then looks back at the hearing aid on the ground.
  EXPRESSION: Determined
- CHARACTER: Narrator
  LINE: CLOSE ON REGAN’s PROFILE as her hand comes into frame and moves to the hearing aid she currently wears. Suddenly, a long wire is slowly pulled from deep in her ear canal.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: REGAN’s eyes wince with almost a snap of pressure as the wire comes loose.
  EXPRESSION: Pain
- CHARACTER: Narrator
  LINE: REGAN then gently feeds the new hearing aid into her ear and pauses.
  EXPRESSION: Hopeful
- CHARACTER: Narrator
  LINE: Suddenly REGAN clicks on the new hearing aid.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Nothing.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: WE WATCH the thin veil of anger on REGAN’s face cascade into honest sorrow as REGAN’s eyes squeeze shut brutal disappointment.
  EXPRESSION: Sad
- CHARACTER: Narrator
  LINE: WE PULL OUT to see REGAN sitting quietly on the floor. The quake of her shoulders betray her as we watch her cry.
  EXPRESSION: Sad
- CHARACTER: Narrator
  LINE: After a moment, she reaches for a pillow case and exits.
  EXPRESSION: Resigned

::PATHS::
- CHOICE: "Exit the room"
  TARGET: woods_valley_pathway
  STATE_CHANGE: regan_sad = true, regan_determined = true
  CONDITION: null

::SCENE::
LOCATION: Woods - Valley Pathway
MOOD: Serene
CHARACTERS: Lee, Marcus, Narrator, Deer
BACKGROUND_IMAGE: valley_pathway.png
BACKGROUND_EDIT: "Daytime, thin sand path, lush evergreens, steep valley side"

::SCRIPT::
- CHARACTER: Narrator
  LINE: FROM A DISTANCE LEE leads MARCUS down a thin sand path that cuts down the steep valley side and through the lush and learned evergreens of the mountain’s canopy.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: MARCUS walks rigid, like one would in the dark. His saucer eyes furtively clock every detail of his surroundings. LEE walks casually and confidently, periodically turning to wait patiently for his son. This is a day of teaching.
  EXPRESSION: Cautious
- CHARACTER: Narrator
  LINE: ON MARCUS as LEE puts a hand quickly, but gently on his son’s chest, stopping him in his tracks. LEE focuses down the path.
  EXPRESSION: Cautious
- CHARACTER: Narrator
  LINE: OFF MARCUS’s quaking face peering around his father:
  EXPRESSION: Afraid
- CHARACTER: Narrator
  LINE: WE TOO MOVE around from behind LEE to see a DEER sitting in the middle of the sand path. An adolescent buck, it holds it’s impressive, but still delicate antlers upright and proud as it stares directly at LEE and MARCUS.
  EXPRESSION: Surprised
- CHARACTER: Narrator
  LINE: An image obviously long thought impossible, the moment carries a certain calm, almost spiritual.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: After a long moment, the buck efforts its way to its feet.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Then turns and deftly steps perfectly along the sand path and disappears.
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue through the woods"
  TARGET: farmhouse_exterior
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Farmhouse Exterior
MOOD: Observational
CHARACTERS: Narrator
BACKGROUND_IMAGE: farmhouse_exterior.png
BACKGROUND_EDIT: "Daytime, dripping roof, drainpipe leading to basement"

::SCRIPT::
- CHARACTER: Narrator
  LINE: CLOSE ON the roof of the farmhouse. Water from the previous night’s storm still drips off the edge.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: WE SLOWLY TRAVEL down the drainpipe running along the side of the house when suddenly the drain stops and we see PVC pipe has been attached instead.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: WE CONTINUE along the PVC piping to the bottom where we see THE PVC PIPE bend AND GO STRAIGHT THROUGH A SHATTERED PANE OF THE BASEMENT WINDOW.
  EXPRESSION: null

::PATHS::
- CHOICE: "Follow the pipe into the basement"
  TARGET: farmhouse_basement
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Farmhouse - Basement
MOOD: Tense
CHARACTERS: Evelyn, Narrator
BACKGROUND_IMAGE: farmhouse_basement.png
BACKGROUND_EDIT: "Daytime, old washing machine, shattered window, dim light"

::SCRIPT::
- CHARACTER: Narrator
  LINE: FROM INSIDE THE SHATTERED PANE, we now follow the PVC pipe into an old washing machine now filled with rain water.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Suddenly a piece of clothing slowly comes into frame and silently descends into the water.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: WE WIDEN OUT TO SEE EVELYN places more clothes into a WASHER that is unplugged. We see that she is simply using the corrugated tumbler inside as a washboard.
  EXPRESSION: Determined
- CHARACTER: Narrator
  LINE: She removes a large plaid shirt just above the water line (still inside the tumbler) and squeezes it dry. The action is virtually inaudible.
  EXPRESSION: Determined
- CHARACTER: Narrator
  LINE: CLOSE UP on a small pile of clothes being stacked onto other clothes. Then a CINCH.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: EVELYN stands up over the newly packed cloth laundry bag then bends backward, attempting to relieve a pain in her back.
  EXPRESSION: Pain
- CHARACTER: Narrator
  LINE: When she’s done, she picks up the full laundry bag with one hand and another full laundry bag with the other.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: EVELYN struggles to the foot of the stairs with the two bags and puts them down. She then takes a deep breath looks up the stairwell and begins to ascend again carefully placing her feet on specific spots on each step. Holding one bag as high as she can and dragging the second behind her. It’s uncomfortable watching a fully pregnant woman traverse in this manner.
  EXPRESSION: Strained
- CHARACTER: Narrator
  LINE: WE GO CLOSE ON several stairs as EVELYN’S feet step up and drag the bag up the first step then the second.
  EXPRESSION: Strained
- CHARACTER: Narrator
  LINE: Her feet disappear. As she drags the bag up onto the third IT CATCHES ON A BENT NAIL IN THE STAIR!!
  EXPRESSION: Tense
- CHARACTER: Narrator
  LINE: ON EVELYN, not seeing the cause, pulls again AND BEGINS TO FALL!!!!!!
  EXPRESSION: Surprised
- CHARACTER: Narrator
  LINE: She catches herself on the wall, her eyes lit up breathing heavily, she’s ok!
  EXPRESSION: Relieved
- CHARACTER: Narrator
  LINE: She quietly picks up the bags again and pulls once more.
  EXPRESSION: Determined
- CHARACTER: Narrator
  LINE: CLOSE UP ON: THE TIP OF A NAIL IN THE STEP LIFTING OFF THE STEP, ALMOST STRAIGHT UP AND THEN RELEASING THE BAG.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: ON EVELYN, satisfied, as she drags the bags to the top of the stairs and disappears.
  EXPRESSION: Satisfied
- CHARACTER: Narrator
  LINE: WE RACK FOCUS to reveal, in the foreground THE NAIL STANDING STRAIGHT UP!!!
  EXPRESSION: Ominous

::PATHS::
- CHOICE: "Continue with the story"
  TARGET: farm_driveway
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Farm - Driveway
MOOD: Determined
CHARACTERS: Regan, Narrator
BACKGROUND_IMAGE: farm_driveway.png
BACKGROUND_EDIT: "Late afternoon, sandy path, bare feet"

::SCRIPT::
- CHARACTER: Narrator
  LINE: CLOSE ON BARE FEET walking along a sand path.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: WE BOOM UP TO REVEAL REGAN walking with purpose. In her hands she carries a pillowcase. Inside the pillowcase an irregular
  EXPRESSION: Determined

::PATHS::
- CHOICE: "End of excerpt"
  TARGET: end
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: River
MOOD: Rising Tension
CHARACTERS: Narrator, Lee, Marcus
BACKGROUND_IMAGE: river.png
BACKGROUND_EDIT: "Late afternoon, tight on moving water over rocks, tall grass, peaceful then chaotic"

::SCRIPT::
- CHARACTER: Narrator
  LINE: An immediate and jarring sound of water rushes in as we are: TIGHT ON MOVING WATER over rocks.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: [NOTE: THE SOUND WILL CONTINUE THROUGHOUT THE ENTIRETY OF THIS SCENE]
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: WE TILT UP to the tall grass of a riverbed. Suddenly LEE and MARCUS exit from the trees.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: ON MARCUS as he takes in the picturesque landscape. He has never been here before. Suddenly, his eyes slowly move down to the ground.
  EXPRESSION: Curious
- CHARACTER: Narrator
  LINE: CLOSE ON HIS BARE FEET at the very edge of the sand path.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: There is nowhere else to go.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: MARCUS watches as LEE takes off his backpack and places it at the edge of the river. Then, he kneels down and looks intently into the water. Suddenly, LEE’s face softens. He takes one more look back at his son and then plunges his hands into the river.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: MARCUS looks on confused as his father seems to yank and pull at something. Suddenly, LEE’s hands burst out of the water holding a handmade wooden contraption. MARCUS starts to back away pulling that contraption out of the water DEFINITELY MADE A SOUND!!! MARCUS’ eyes shoot around into the trees, up the river, looking, listening when suddenly LEE PULLS OUT A LARGE TROUT FROM THE TRAP. THE FISH THRASHES WILDLY AND THEN IT BREAKS FREE FROM LEE’S HAND! IT DROPS DOWN ONTO LEE’S BAG FLAPPING AND THRASHING AND MAKING NOISE!!!!
  EXPRESSION: Scared
- CHARACTER: Narrator
  LINE: MARCUS goes white! WHAT HAS HIS FATHER DONE???? MARCUS signs.
  EXPRESSION: Terrified
- CHARACTER: Marcus
  LINE: (SIGNING) They’re going to hear you. They’re going to HEAR YOU!!
  EXPRESSION: Terrified
- CHARACTER: Narrator
  LINE: In one swift move, LEE pins the trout to the ground and grabs his son, pulling him in close. LEE silently calms his son down, coaxing him to take deep breaths. As MARCUS trembles LEE raises his hand and signs.
  EXPRESSION: Calm
- CHARACTER: Lee
  LINE: (SIGNING) Not, if there is a constant sound nearby that is louder.
  EXPRESSION: Calm
- CHARACTER: Narrator
  LINE: MARCUS doesn’t understand. LEE shows him. First, he reaches down to the ground and places his hand off the path moving the dirt slightly. He repeats.
  EXPRESSION: Confused
- CHARACTER: Lee
  LINE: (SIGNING) Small sounds safe.
  EXPRESSION: Instructive
- CHARACTER: Narrator
  LINE: LEE’s hand moves back to the trout. Repeats.
  EXPRESSION: null
- CHARACTER: Lee
  LINE: (SIGNING) Big sounds not. Unless...
  EXPRESSION: Instructive
- CHARACTER: Narrator
  LINE: LEE’s hands move to the moving water of the river. Repeats.
  EXPRESSION: null
- CHARACTER: Lee
  LINE: (SIGNING) There is a constant sound nearby that is louder to mask it.
  EXPRESSION: Instructive
- CHARACTER: Narrator
  LINE: Suddenly the trout flaps again. MARCUS looks down then up to his dad. His brain processing.
  EXPRESSION: Thoughtful
- CHARACTER: Lee
  LINE: (SIGNING) You know what?
  EXPRESSION: Thoughtful
- CHARACTER: Narrator
  LINE: LEE checks his watch, then looks up river, then back to his son.
  EXPRESSION: Observant
- CHARACTER: Lee
  LINE: (SIGNING) I want to show you something.
  EXPRESSION: Determined

::PATHS::
- CHOICE: "Follow Lee"
  TARGET: farmhouse_exterior
  STATE_CHANGE: marcus_understanding = +1
  CONDITION: null

::SCENE::
LOCATION: Farmhouse Exterior
MOOD: Ethereal
CHARACTERS: Narrator, Evelyn
BACKGROUND_IMAGE: farmhouse.png
BACKGROUND_EDIT: "Late afternoon, dancing colors from clothesline, old fallen tree visible through house"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Disoriented, WE MOVE THROUGH a wall of dancing color. Then suddenly we see EVELYN, as she holds up a piece of clothing and pins it to a clothes line. The scene is oddly beautiful.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: As the clothes on the line dance, we can suddenly see, behind EVELYN AN OLD FALLEN TREE THROUGH THE BACKSIDE OF THE HOUSE.
  EXPRESSION: null

::PATHS::
- CHOICE: "Enter the farmhouse"
  TARGET: farmhouse_upstairs_hall
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Farmhouse Upstairs Hall
MOOD: Melancholy
CHARACTERS: Narrator, Evelyn
BACKGROUND_IMAGE: farmhouse_upstairs.png
BACKGROUND_EDIT: "Late afternoon, tracking slowly through bannister, empty children's rooms without doors"

::SCRIPT::
- CHARACTER: Narrator
  LINE: WE TRACK SLOWLY along through the bannister of the upstairs hallway when suddenly EVELYN’S head appears. WE CONTINUE with her as she slowly walks up the stairs almost as if compelled.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: As she ascends, looking right past camera, we get a clear look into the bedrooms behind her. In one room, we catch glimpses of a POP MUSIC POSTER, a PINK DESK and an empty bed frame. In the next, we see a Nerf basketball hoop, a life sized Pokemon doll and half built LEGOs strewn across the floor. Neither room has doors.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: EVELYN finally crests the top of the stairs and walks out of frame.
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue to the next location"
  TARGET: waterfall_interior
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Waterfall Interior
MOOD: Awe
CHARACTERS: Narrator, Lee, Marcus
BACKGROUND_IMAGE: waterfall.png
BACKGROUND_EDIT: "Late afternoon, light dancing through cascading water, rock wall, mysterious and beautiful"

::SCRIPT::
- CHARACTER: Narrator
  LINE: A bizarre and beautiful image and sound! Light dances and bends through a cascading rampart we finally identify as A WATERFALL.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: WE PAN OVER to see LEE and MARCUS enter from outside and slide along the rock wall.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: MARCUS looks up to his father, incredulous. LEE looks down at him.
  EXPRESSION: Incredulous
- CHARACTER: Narrator
  LINE: After a moment, with a mischievous smile on his face, LEE HOOTS LOUDLY!!!
  EXPRESSION: Mischievous
- CHARACTER: Narrator
  LINE: THIS IS THE FIRST VOCALIZED SOUND WE WILL HAVE HEARD IN THE MOVIE!!!!
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: MARCUS’ eyes shoot up to his father, immediately scared again!
  EXPRESSION: Scared
- CHARACTER: Narrator
  LINE: His father looks out at the waterfall and HOOTS AGAIN!!! The way one would walking in a tunnel with their child.
  EXPRESSION: Playful
- CHARACTER: Narrator
  LINE: LEE turns to MARCUS and crouches down, gently holding his trembling son’s shoulders.
  EXPRESSION: Gentle
- CHARACTER: Lee
  LINE: You’re alright.
  EXPRESSION: Comforting
- CHARACTER: Narrator
  LINE: THESE ARE THE FIRST WORDS WE HAVE HEARD IN THE MOVIE AND THE FIRST WORDS MARCUS HAS HEARD IN 4 YEARS!!!!
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: WE ARE ON MARCUS’ face staring, shaking, somewhere between terror and wonderment.
  EXPRESSION: Awestruck
- CHARACTER: Lee
  LINE: I promise.
  EXPRESSION: Reassuring
- CHARACTER: Narrator
  LINE: His father smiles and nods comfortingly.
  EXPRESSION: Comforting
- CHARACTER: Narrator
  LINE: Finally MARCUS meekly HOOTS!
  EXPRESSION: Hopeful
- CHARACTER: Narrator
  LINE: His father’s head gently tilts, as if to say “you c
  EXPRESSION: Encouraging

::PATHS::
- CHOICE: "Experience the waterfall's sound"
  TARGET: end
  STATE_CHANGE: marcus_fear = -1, marcus_wonder = +1
  CONDITION: null

::SCENE::
LOCATION: Waterfall
MOOD: Joy, connection
CHARACTERS: Narrator, Marcus, Lee
BACKGROUND_IMAGE: waterfall.png
BACKGROUND_EDIT: "Rushing water, late afternoon, joyful atmosphere"

::SCRIPT::
- CHARACTER: Marcus
  LINE: an do better”.
  EXPRESSION: Determined
- CHARACTER: Narrator
  LINE: MARCUS looks back out the rushing water, then back to his father and HOOTS LOUDLY!!!
  EXPRESSION: null
- CHARACTER: Lee
  LINE: Now, that’s more like it.
  EXPRESSION: Pleased
- CHARACTER: Narrator
  LINE: The smile on MARCUS and LEE’s face can only be described as once in a lifetime.
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue journey"
  TARGET: ext_road_regan
  STATE_CHANGE: joy = +1
  CONDITION: null

::SCENE::
LOCATION: Road
MOOD: Melancholy, solemn, reflective
CHARACTERS: Narrator, Regan
BACKGROUND_IMAGE: road_bridge.png
BACKGROUND_EDIT: "Late afternoon, gargantuan trees, overgrown bridge with weeds and roots, sandy ground"

::SCRIPT::
- CHARACTER: Narrator
  LINE: WE MOVE SLOWLY ALONG A ROAD, PANNING DOWN from gargantuan trees until we finally reveal REGAN walking towards camera.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Suddenly coming into frame all around her is THE BRIDGE.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: WE FOLLOW REGAN as she walks across the bridge, now more overgrown with weeds and roots. Then suddenly REGAN comes to a stop and kneels down in sand as WE CONTINUE TO MOVE BACK SLOWLY.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Suddenly coming into frame is the top of A HAND MADE CROSS!!!
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: REGAN reaches into her pillow case and pulls ou THE TOY SHUTTLE.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: WE FOLLOW REGAN’S HANDS as she deftly removes one of the colored plastic pieces underneath. It quietly slides off to reveal a battery panel and several multi colored wires. She reaches into the front pocket of her dress and pulls out pliers and quickly cuts the green wire.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: REGAN reaches into the pocket of her dress again and pulls out batteries! She slides the batteries in confidently.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: We follow REGAN’s hands as they move to the base of the cross and place the TOY SHUTTLE in the sand. We now see that the shuttle sits amongst a pile of other weathered toys and flowers.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: REGAN PAUSES and then flips the tiny switch.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: RED AND BLUE LIGHTS CASCADE OVER HER FACE
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: But no sound.
  EXPRESSION: null

::PATHS::
- CHOICE: "Observe Regan's ritual"
  TARGET: int_farmhouse_bedroom_evelyn_1
  STATE_CHANGE: sorrow = +1
  CONDITION: null

::SCENE::
LOCATION: Farmhouse Bedroom
MOOD: Sadness, remembrance, meticulous
CHARACTERS: Narrator, Evelyn
BACKGROUND_IMAGE: farmhouse_bedroom.png
BACKGROUND_EDIT: "Late afternoon, rocket ship wallpaper, planet mobile, perfectly made bed, original paned window with cross shadow, nightstand with lamp and handmade mirror"

::SCRIPT::
- CHARACTER: Narrator
  LINE: WE ARE TIGHT on EVELYN’s back as she walks through another door-less threshold. As she continues into the room, we begin to see the walls covered in rocket ships.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: OVER EVELYN as her eyes stop on a cartoon mobile of the planets. She taps it exactly as she tapped the mobile in the baby’s room. This time watching it orbit around without a smile.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: WIDE ON THE ROOM for the first time we see THE ROOM IS METICULOUS. The bed is made, the toys perfectly placed on the shelves.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: CLOSE ON THE BED AS EVELYN SITS DOWN SLOWLY. Light floods through the original paned window, casting the shadow of a cross on the floor in front of her.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: EVELYN looks over to the small night stand by the bed where a lamp and a hand made mirror sit.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Suddenly, she lifts up the mirror and dusts the table with the washcloth from the line.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: EVELYN stares out the window oddly at peace. As LEE has his ritual atop the silo to contemplate on the irreversible loss of his son EVELYN has this. EVELYN keeps her son’s spirit alive.
  EXPRESSION: null

::PATHS::
- CHOICE: "Reflect with Evelyn"
  TARGET: int_waterfall_lee_marcus
  STATE_CHANGE: sorrow = +1, peace = +1
  CONDITION: null

::SCENE::
LOCATION: Waterfall
MOOD: Calm, intimate, then tense, shocked
CHARACTERS: Narrator, Lee, Marcus
BACKGROUND_IMAGE: waterfall.png
BACKGROUND_EDIT: "Late afternoon, rushing water, rocks, calm setting"

::SCRIPT::
- CHARACTER: Narrator
  LINE: CLOSE ON a water bladder poking into the rushing wall of water. Filling immediately, we PULL BACK and FOLLOW LEE as he sits down on a rock next to his son and hands him the bladder.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: MARCUS drinks as LEE looks on a brightness washing over him.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: This is a moment of calm. A moment of family. A moment of real life.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: WE FOLLOW the bladder as MARCUS hands it up to his father, who happily takes a large swig. Suddenly we HEAR:
  EXPRESSION: null
- CHARACTER: Marcus
  LINE: Why didn’t you let her come with us?
  EXPRESSION: Curious
- CHARACTER: Narrator
  LINE: LEE looks down at his son.
  EXPRESSION: null
- CHARACTER: Lee
  LINE: Because, I need to keep her safe.
  EXPRESSION: Concerned
- CHARACTER: Marcus
  LINE: Is it because you blame her for what happened?
  EXPRESSION: Direct
- CHARACTER: Narrator
  LINE: LEE freezes instantly, his heart stops.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Finally he looks down at his son, in shock, in awe.
  EXPRESSION: null
- CHARACTER: Marcus
  LINE: Because she blames herself.
  EXPRESSION: Sad
- CHARACTER: Narrator
  LINE: LEE’s eyes blink and flutter as he tries to gain control of his thoughts.
  EXPRESSION: null
- CHARACTER: Lee
  LINE: No, I don’t bl--It was no one’s fault.
  EXPRESSION: Shocked
- CHARACTER: Marcus
  LINE: You still love her, right?
  EXPRESSION: Questioning
- CHARACTER: Lee
  LINE: Of-- Of course I do.
  EXPRESSION: Assured
- CHARACTER: Narrator
  LINE: Pause.
  EXPRESSION: null
- CHARACTER: Marcus
  LINE: You should tell her.
  EXPRESSION: Suggestive

::PATHS::
- CHOICE: "Consider Marcus's words"
  TARGET: int_farmhouse_bedroom_evelyn_2
  STATE_CHANGE: guilt = +1, love = +1
  CONDITION: null

::SCENE::
LOCATION: Farmhouse Bedroom
MOOD: Introspective, then sudden tension, fear
CHARACTERS: Narrator, Evelyn
BACKGROUND_IMAGE: farmhouse_bedroom.png
BACKGROUND_EDIT: "Late afternoon, Evelyn's reflection in handmade mirror with zoo animals and "BEAU", doorway"

::SCRIPT::
- CHARACTER: Narrator
  LINE: CLOSE ON EVELYN IN THE HAND MADE MIRROR, as she stares at the frame made up of colorful zoo animals staring back at her. At the top of the mirror, the name “BEAU”
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: FROM THE DOORWAY, WE ARE WIDE ON THE ROOM as EVELYN stands up and slowly makes her way to the door carrying the small mirror.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Just as she reaches the doorway, she stops. Her body tightens. Her face changes. Her hand shakes as it reaches out to the side of the doorway. WE HOLD ON HER a moment and then go CLOSE ON her feet rocking slightly in the doorway.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Suddenly FLUID HITS THE FLOORBOARDS!!!!
  EXPRESSION: null

::PATHS::
- CHOICE: "React to Evelyn's distress"
  TARGET: ext_woods_lee_marcus
  STATE_CHANGE: fear = +2, urgency = +1
  CONDITION: null

::SCENE::
LOCATION: Woods
MOOD: Unsettling, ominous
CHARACTERS: Narrator, Lee, Marcus
BACKGROUND_IMAGE: woods.png
BACKGROUND_EDIT: "Late afternoon, oddly beautiful exit from woods, path, tall thin swamp trees, dilapidated eerie house"

::SCRIPT::
- CHARACTER: Narrator
  LINE: LEE and MARCUS appear through an oddly beautiful exit from the woods and begin walking along a path.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: PROFILE on LEE as we see the tall thin trees of a swamp behind him.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: PROFILE ON MARCUS from the opposite side as swamp trees are also behind him. Suddenly A DILAPIDATED house comes into frame. MARCUS turns to look.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: MARCUS’ POV of the eery house that stands as a reminder that people once lived here happily.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: CLOSE ON MARCUS looking up on the house. His face now
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue through the woods"
  TARGET: end_of_excerpt
  STATE_CHANGE: unease = +1
  CONDITION: null

::SCENE::
LOCATION: Swamp/Forest
MOOD: Extreme Terror
CHARACTERS: Narrator, Marcus, Lee, The Man, Dark Shadow
BACKGROUND_IMAGE: null
BACKGROUND_EDIT: null

::SCRIPT::
- CHARACTER: Narrator
  LINE: Suddenly, behind MARCUS, just out of focus in the short distance A DARK SHADOW!!!
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: No sooner has the FIGURE exited frame, MARCUS CRASHES INTO HIS FATHER WHO IS STANDING COMPLETELY STILL.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: MARCUS looks up at his father who stares off sharply into the short distance OVER MARCUS as he slowly leans around his father to see what he’s looking at, when suddenly we see A TERRIFYING MAN AT THE EDGE OF THE SWAMP!!!
  EXPRESSION: Terrified
- CHARACTER: Narrator
  LINE: A human form unlike anything most of us ever will or should get to see, the man’s emaciated body quakes and then shudders as if a synapses misfire. His face is sunken, almost ghoulish and the look in his pitch black eyes communicates something far beyond fearful. Much worse, this is the rare look of a brain that has accepted a living nightmares as an everyday reality.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: MARCUS slowly raises his hand into a wave.
  EXPRESSION: Surprised
- CHARACTER: Narrator
  LINE: THE MAN doesn’t move.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: LEE’s eyes travel slowly down the man’s frame.
  EXPRESSION: Concerned
- CHARACTER: Narrator
  LINE: We see the man’s dirt covered face, then a ratty and ripped flannel shirt, and then blood covered hands, blood covered jeans and finally at his feet, in the high grass LONG HAIR AND A HAND OF A DEAD WOMAN.
  EXPRESSION: Horrified
- CHARACTER: Narrator
  LINE: LEE’s eyes slowly come back up to meet the man’s. LEE now also raises his hand and places a tense finger on his lips.
  EXPRESSION: Calm
- CHARACTER: Narrator
  LINE: Two large tears run down his face. In his eyes, the knowing fear of the end of his life as he takes a deep breath in.
  EXPRESSION: Afraid
- CHARACTER: Narrator
  LINE: LEE immediately grabs MARCUS.
  EXPRESSION: Panicked
- CHARACTER: Narrator
  LINE: TIGHT ON LEE sprinting down the path carrying his son. OVER HIS SHOULDER, the man in the background: LETS OUT A PRIMAL SCREAM!!!!!! A bottomless sound of pain and surrender, the sound blasts onto us like a wave.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: LEE suddenly dives behind a hollowed out tree trunk and throws MARCUS’ back up against it.
  EXPRESSION: Panicked
- CHARACTER: Narrator
  LINE: MARCUS’ father clasps his hand over his mouth.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: MARCUS’ eyes widen as overwhelming panic takes over.
  EXPRESSION: Panicked
- CHARACTER: Narrator
  LINE: LEE looks down at his son with the most beautiful sense of calm. The way one holds the hand of someone in their last seconds on earth, LEE’s smile is pure comfort, pure love.
  EXPRESSION: Loving
- CHARACTER: Narrator
  LINE: Suddenly we hear THE FAMILIAR TERRIFYING SCREEEEEEEECH!
  EXPRESSION: Terrified
- CHARACTER: Narrator
  LINE: MARCUS begins violently shaking his head, his soul seemingly coming out through his skin. Then suddenly we hear THE SNAPPING OF TREES!
  EXPRESSION: Terrified
- CHARACTER: Narrator
  LINE: LEE’s look now shoots to the tree line behind the man when suddenly WE HEAR the man’s primal scream of pain turn into an animal sound of death.
  EXPRESSION: Terrified
- CHARACTER: Narrator
  LINE: MARCUS covers his ears. Through the muffle of MARCUS’ covered ears we can still hear the most horrific sounds of ultimate pain, crunching, and then a deafening POP!!!!
  EXPRESSION: Terrified
- CHARACTER: Narrator
  LINE: SILENCE
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: MARCUS’ eyes almost seem to dim right before us as he goes limp.
  EXPRESSION: Shocked

::PATHS::
- CHOICE: "Continue to next scene"
  TARGET: farmhouse_upstairs_hall
  STATE_CHANGE: fear = +3, shock = +2
  CONDITION: null

::SCENE::
LOCATION: Farmhouse - Upstairs Hall
MOOD: Intense Pain
CHARACTERS: Narrator, Evelyn
BACKGROUND_IMAGE: null
BACKGROUND_EDIT: "Late afternoon, dimly lit hallway"

::SCRIPT::
- CHARACTER: Narrator
  LINE: FROM THE FLOOR we follow drops of fluid down the hall, leading to EVELYN gripping onto the railing with both hands as she slowly traverses the stairs going down, focusing intently on each step.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: EVELYN’s face as she takes slow, deep breaths. Her eyes surging with panic and pain.
  EXPRESSION: Pained
- CHARACTER: Narrator
  LINE: IT’S 4 WEEKS TOO SOON!
  EXPRESSION: Panicked
- CHARACTER: Narrator
  LINE: Suddenly EVELYN’s eyes go wide. CONTRACTION!!!
  EXPRESSION: Pained
- CHARACTER: Narrator
  LINE: CLOSE ON EVELYN’S BELLY as she slowly sinks down into the steps and INTO A CLOSE UP.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: In EVELYN’s face we will witness, many of us for the first time, the complex and overwhelming sensory overload that is a contraction all swallowed back with every fiber of her being in order to remain silent.
  EXPRESSION: Pained
- CHARACTER: Narrator
  LINE: Just at the moment it looks as though EVELYN may explode, the contraction subsides.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: WE ARE ON EVELYN’s BACK as she struggles up onto her feet and down the remaining stairs. As she rounds the banister and out of frame WE HOLD ON THE FRONT HALL.
  EXPRESSION: Pained
- CHARACTER: Narrator
  LINE: Out the front door and onto the sand path warmly lit white from the Christmas lights above.
  EXPRESSION: null

::PATHS::
- CHOICE: "Descend to basement"
  TARGET: farmhouse_basement
  STATE_CHANGE: pain = +1, urgency = +1
  CONDITION: null

::SCENE::
LOCATION: Farmhouse - Basement
MOOD: Visceral Shock
CHARACTERS: Narrator, Evelyn
BACKGROUND_IMAGE: null
BACKGROUND_EDIT: "Late afternoon, dimly lit, exposed stairs"

::SCRIPT::
- CHARACTER: Narrator
  LINE: WE ARE LOW looking up the basement stairs as suddenly EVELYN appears in the narrow doorway and grabs hold of the wall, still carrying the children’s mirror. She takes a moment and then begins to descend the exposed stairs with the same deliberate effort.
  EXPRESSION: Pained
- CHARACTER: Narrator
  LINE: COMING TOWARDS CAMERA, EVELYN gets bigger and bigger in the frame until her head disappears, then her belly.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Just as her foot comes down into close up we: RACK FOCUS to THE NAIL STANDING STRAIGHT UP!!!! EVELYN’s footsteps STRAIGHT DOWN ON IT!!!!!
  EXPRESSION: Horrified
- CHARACTER: Narrator
  LINE: WE WATCH THE NAIL PIERCE INTO THE BOTTOM OF HER FOOT and then ERUPT THROUGH THE OTHER SIDE!!!!!!!!
  EXPRESSION: Pained
- CHARACTER: Narrator
  LINE: THE SOUND CUTS OUT as we go: CLOSE ON EVELYN as the shock and searing pain collides in her brain behind her eyes. Then CLOSE ON THE MIRROR as it SILENTLY CRASHES DOWN THE STAIRS then rattles around in a
  EXPRESSION: Shocked

::PATHS::
- CHOICE: "End scene"
  TARGET: end
  STATE_CHANGE: pain = +5, shock = +5
  CONDITION: null

::SCENE::
LOCATION: Farmhouse Basement
MOOD: Fear, Pain, Desperation
CHARACTERS: Evelyn, Narrator
BACKGROUND_IMAGE: farmhouse_basement_console.png
BACKGROUND_EDIT: "Dimly lit, cluttered basement, focus on Evelyn's injured foot, then on a makeshift security console"

::SCRIPT::
- CHARACTER: Narrator
  LINE: circle before coming to a standstill.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: SOUND COMES RUSHING BACK IN ON EVELYN as full blown fear washes over her. That sound was most definitely HEARD. She looks down.
  EXPRESSION: Afraid
- CHARACTER: Narrator
  LINE: CLOSE ON EVELYN’s FOOT as she SLIDES THE FOOT SLOWLY UP THE NAIL and POPS IT FREE. Blood immediately begins to drip from the wound.
  EXPRESSION: Pain
- CHARACTER: Narrator
  LINE: EVELYN rushes down the remaining stairs, wincing with every other step.
  EXPRESSION: Pain
- CHARACTER: Narrator
  LINE: WE FOLLOW ON EVELYN’s BACK as she hurriedly shuffles through this basement that once felt familiar in the romantic glow of their slow dance, but now feels stark and desperately lonely.
  EXPRESSION: Desperate
- CHARACTER: Narrator
  LINE: Finally, EVELYN arrives at LEE’s security console. She desperately pushes past stacks of notebooks and files, boxes of various electrical equipment like cellphones, cassette players and EGG TIMERS that have been pillaged for parts.
  EXPRESSION: Desperate
- CHARACTER: Narrator
  LINE: EVELYN finally moves THE BOX OF HEARING AIDS to reveal that there on the wall is a large, handmade switch.
  EXPRESSION: Determined
- CHARACTER: Narrator
  LINE: EVELYN grabs the knob at the top and thrusts it down.
  EXPRESSION: Determined

::PATHS::
- CHOICE: "Activate the signal"
  TARGET: farm_red_lights
  STATE_CHANGE: signal_sent = true, evelyn_hope = +1
  CONDITION: null

::SCENE::
LOCATION: Farm
MOOD: Urgent, Alarming
CHARACTERS: Narrator
BACKGROUND_IMAGE: farm_night_red_lights.png
BACKGROUND_EDIT: "Late afternoon, dusk sky, farm illuminated by bright red Christmas lights"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Suddenly, flickering to life against the dusk colored sky LINES OF RED CHRISTMAS LIGHTS!!!
  EXPRESSION: Alarmed
- CHARACTER: Narrator
  LINE: Like the white lights before, the power grid like system illuminates the farm in bright RED!!!
  EXPRESSION: Alarmed

::PATHS::
- CHOICE: "Show Regan's reaction"
  TARGET: road_regan_red_lights
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Road
MOOD: Unknowing, Tense
CHARACTERS: Regan, Narrator
BACKGROUND_IMAGE: road_dusk_trees.png
BACKGROUND_EDIT: "Late afternoon, sandy road, cross, red lights visible through trees in distance"

::SCRIPT::
- CHARACTER: Narrator
  LINE: REGAN lies in the sand next to the cross. Behind her we see RED LIGHTS THROUGH THE TREES!
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: REGAN doesn’t see them.
  EXPRESSION: Neutral

::PATHS::
- CHOICE: "Return to Evelyn"
  TARGET: farmhouse_basement_shadow
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Farmhouse Basement
MOOD: Brief Relief, then Terror
CHARACTERS: Evelyn, Narrator
BACKGROUND_IMAGE: farmhouse_basement_shadow.png
BACKGROUND_EDIT: "Late afternoon, Evelyn at console, then shadow by doorway"

::SCRIPT::
- CHARACTER: Narrator
  LINE: ON EVELYN, leaning on LEE’s console. Her eyes closed, she takes slow, deep breathes, as if to convince herself that it will all be OK now. The signal has been sent.
  EXPRESSION: Hopeful
- CHARACTER: Narrator
  LINE: For a brief moment a smile as she then opens her eyes and moves back to the stairs.
  EXPRESSION: Relieved
- CHARACTER: Narrator
  LINE: As she clutches the support beam and goes to take her first step up A LARGE SHADOW FLASHES PAST THE DOORWAY!!!!!
  EXPRESSION: Terrified
- CHARACTER: Narrator
  LINE: EVELYN spins back away from the stairs in terror.
  EXPRESSION: Terrified

::PATHS::
- CHOICE: "Follow Lee and Marcus"
  TARGET: woods_pathway_lee_marcus
  STATE_CHANGE: evelyn_fear = +1
  CONDITION: null

::SCENE::
LOCATION: Woods - Valley Pathway
MOOD: Desperate, Urgent, Worried
CHARACTERS: Lee, Marcus, Narrator
BACKGROUND_IMAGE: woods_valley_pathway_dusk.png
BACKGROUND_EDIT: "Dusk, towering trees, Lee carrying Marcus, red lights visible on farm in distance"

::SCRIPT::
- CHARACTER: Narrator
  LINE: As sky begins to settle into dusk above the towering trees LEE enters carrying a limp MARCUS.
  EXPRESSION: Worried
- CHARACTER: Narrator
  LINE: He trudges up the sand path, looking down at MARCUS.
  EXPRESSION: Concerned
- CHARACTER: Narrator
  LINE: MARCUS’ eyes are open, but he is not present.
  EXPRESSION: Injured
- CHARACTER: Narrator
  LINE: ON LEE’S BACK NOW, as he and his son crest the hill.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: WE BOOM UP to see the dark horizon line of sky, give way to the top of the silo and then the fire red ground illuminated by Christmas lights.
  EXPRESSION: Alarmed
- CHARACTER: Narrator
  LINE: ON LEE as we see his face register exactly what this means.
  EXPRESSION: Alarmed
- CHARACTER: Narrator
  LINE: He breaks into a full sprint.
  EXPRESSION: Urgent

::PATHS::
- CHOICE: "Return to Evelyn in the basement"
  TARGET: farmhouse_basement_attack_and_birth
  STATE_CHANGE: lee_urgent = true
  CONDITION: null

::SCENE::
LOCATION: Farmhouse Basement
MOOD: Trapped, Terrified, Excruciating Pain
CHARACTERS: Evelyn, Narrator
BACKGROUND_IMAGE: farmhouse_basement_red_light.png
BACKGROUND_EDIT: "Dusk, red light through window, Evelyn searching, monster sounds, contraction, blood"

::SCRIPT::
- CHARACTER: Narrator
  LINE: CLOSE ON one of the basement windows as red light pours through.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: WE PULL BACK SLOWLY as: EVELYN’s HANDS enter frame. She desperately pushes on the window nothing.
  EXPRESSION: Desperate
- CHARACTER: Narrator
  LINE: EVELYN roams around the basement like a caged animal searching for any way out.
  EXPRESSION: Trapped
- CHARACTER: Narrator
  LINE: She moves back to LEE’s security console, scanning the desk, think, THINK!
  EXPRESSION: Frantic
- CHARACTER: Narrator
  LINE: Suddenly her eyes fall upon the box of small electronics she just moved to get to the switch.
  EXPRESSION: Focused
- CHARACTER: Narrator
  LINE: Suddenly we hear A SCRATCHING OF CLAWS ON A WALL AND A CRASH OF GLASS FROM ABOVE HER!!!!
  EXPRESSION: Startled
- CHARACTER: Narrator
  LINE: EVELYN freezes with fear. Then... THE HORRIFIC SCREEEEEEEEECH CAN BE HEARD!
  EXPRESSION: Terrified
- CHARACTER: Narrator
  LINE: EVELYN closes her eyes as the same sound that preempted her son’s death washes over her.
  EXPRESSION: Traumatized
- CHARACTER: Narrator
  LINE: Then, her eyes shoot open in pain CONTRACTION!!!
  EXPRESSION: Pain
- CHARACTER: Narrator
  LINE: Larger than the second one, this one brings EVELYN to her knees, her head dips to the ground as she grimaces in intense pain.
  EXPRESSION: Extreme Pain
- CHARACTER: Narrator
  LINE: CLOSE ON EVELYN as her head suddenly shoots back up... The red light pouring in from the basement windows cuts a line across her face revealing her exploding eyes trying to swallow the pain. Tears begin to fall, she is unable to breath.
  EXPRESSION: Extreme Pain
- CHARACTER: Narrator
  LINE: Then suddenly air slowly escapes as she exhales the contraction has passed. After a moment of realization, disbelief, she stands up and out of frame.
  EXPRESSION: Shocked
- CHARACTER: Narrator
  LINE: WE HOLD and then slowly pan down to a small pool of blood on the floor.
  EXPRESSION: Horrified

::PATHS::
- CHOICE: "Move upstairs"
  TARGET: farmhouse_first_floor_hallway
  STATE_CHANGE: evelyn_birth_trauma = true
  CONDITION: null

::SCENE::
LOCATION: Farmhouse (First Floor Hallway)
MOOD: Tense, Foreboding
CHARACTERS: Evelyn, Narrator
BACKGROUND_IMAGE: farmhouse_first_floor_hallway.png
BACKGROUND_EDIT: "Dusk, first-floor hallway, looking down stairs, Evelyn passes"

::SCRIPT::
- CHARACTER: Narrator
  LINE: NOW LOOKING DOWN THE STAIRS from the doorway in the first floor hallway we see EVELYN rush through frame past the stairs.
  EXPRESSION: Urgent
- CHARACTER: Narrator
  LINE: WE CAN BARELY MAKE OUT A NONDESCRIPT SOUND.
  EXPRESSION: Mysterious

::PATHS::
- CHOICE: "Return to basement"
  TARGET: farmhouse_basement_hiding
  STATE_CHANGE: sound_awareness = +1
  CONDITION: null

::SCENE::
LOCATION: Farmhouse Basement
MOOD: Intense Fear, Imminent Danger, Extreme Pain
CHARACTERS: Evelyn, Narrator
BACKGROUND_IMAGE: farmhouse_basement_hiding_boiler.png
BACKGROUND_EDIT: "Dusk, Evelyn hiding behind boiler, ticking/scraping sounds, severe contraction"

::SCRIPT::
- CHARACTER: Narrator
  LINE: ON EVELYN as she quickly slides in behind a large boiler. We can see the basement stairs in the background.
  EXPRESSION: Panicked
- CHARACTER: Narrator
  LINE: EVELYN squeezes her eyes shut and begins murmuring to herself THE NONDESCRIPT SOUND IS SLIGHTLY LOUDER A TICKING.
  EXPRESSION: Panicked
- CHARACTER: Narrator
  LINE: And then EVELYN’s eyes shoot open. What now?
  EXPRESSION: Desperate
- CHARACTER: Narrator
  LINE: Suddenly CONTRACTION!!!!
  EXPRESSION: Extreme Pain
- CHARACTER: Narrator
  LINE: We are on EVELYN’S face as she endures this immeasurable pain in this unthinkable moment.
  EXPRESSION: Extreme Pain
- CHARACTER: Narrator
  LINE: Then we hear. TICK SCRAAAAAPE TICK SCRAAAAAPE
  EXPRESSION: Terrified
- CHARACTER: Narrator
  LINE: Whatever IT is it’s coming DOWN THE STAIRS.
  EXPRESSION: Terrified
- CHARACTER: Narrator
  LINE: TICK SCRAAAAAPE TICK SCRAAAAAPE
  EXPRESSION: Terrified
- CHARACTER: Narrator
  LINE: EVELYN crushes herself even tighter against the wall behind the boiler closing her eyes and exhaling in pure, painful, silence as the contraction subsides.
  EXPRESSION: Terrified, Enduring Pain
- CHARACTER: Narrator
  LINE: Suddenly we
  EXPRESSION: Suspense

::PATHS::
- CHOICE: "End of excerpt"
  TARGET: end_cliffhanger
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Basement / Water Tanks
MOOD: Intense, Suspenseful
CHARACTERS: Narrator, Evelyn, Creature
BACKGROUND_IMAGE: basement_tanks.png
BACKGROUND_EDIT: "Dimly lit basement, water tanks, creature partially visible"

::SCRIPT::
- CHARACTER: Narrator
  LINE: hear...
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: SILENCE.
  EXPRESSION: null
- CHARACTER: Evelyn
  LINE: null
  EXPRESSION: null
  STAGE_DIRECTION: turns and peers through the water tanks.
- CHARACTER: Narrator
  LINE: IN EVELYN’S POV as she scans the room through the sliver of a view then suddenly we can barely make out more than a SLIVER of a creature’s shoulder or back from in between the tanks.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: WE CAN SEE THAT IT IS COVERED IN SMALL ARMOR LIKE PLATES!
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Suddenly...
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The small plates on the creature’s shoulder BEGIN TO LIFT UP??!! Like the pieces on a colander, or an old satellite dish, the small plates open up with the crackle and pull of anatomical goo underneath. Then all of the sudden, the plates BEGIN TO ROTATE! Like directional microphones, the plates begin searching the room FOR SOUND!
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: From behind the tanks, EVELYN watches as the creature’s plates turn toward the wall of monitors. Suddenly, each of the screens begins to flicker!!! Then the picture goes completely dark!
  EXPRESSION: null
- CHARACTER: Evelyn
  LINE: null
  EXPRESSION: null
  STAGE_DIRECTION: then suddenly rolls her back against the tanks to look from one side of the room to the other.
- CHARACTER: Narrator
  LINE: Suddenly we now can identify the NONDESCRIPT SOUND FROM EARLIER as TICKING.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Then, sitting on a shelf on the wall opposite the console, we see AN EGG TIMER!!!
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: WE CONTINUE TO PUSH IN, THE TICKING SOUND NOW MUCH LOUDER, when finally, just as we land CLOSE UP on the egg timer RIIIIIIIIIIIIIIIIIIING!!!!!!!!!!!
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: THE CREATURE SCREEEEEEEEEEEECHES!!!!
  EXPRESSION: Terrified
- CHARACTER: Narrator
  LINE: AND ATTACKS THE SOUND!!!!!!!
  EXPRESSION: null
- CHARACTER: Evelyn
  LINE: null
  EXPRESSION: null
  STAGE_DIRECTION: opens her eyes.
- CHARACTER: Narrator
  LINE: That’s it! Her plan worked! EVELYN thrusts herself away from the tanks!!
  EXPRESSION: Determined
- CHARACTER: Narrator
  LINE: WE TRACK WITH HER as she moves as quickly as she can to the exposed stairs and begins to climb.
  EXPRESSION: null

::PATHS::
- CHOICE: "Escape the basement"
  TARGET: front_hall
  STATE_CHANGE: Evelyn_escaped_basement = true
  CONDITION: null

::SCENE::
LOCATION: Front Hall
MOOD: Urgent, Escape
CHARACTERS: Narrator, Evelyn, Dark Shadow
BACKGROUND_IMAGE: farmhouse_hallway.png
BACKGROUND_EDIT: "Dusk, view from kitchen through hallway to front door, Evelyn running"

::SCRIPT::
- CHARACTER: Narrator
  LINE: FROM THE KITCHEN WE LOOK THROUGH THE HALLWAY ONTO THE FRONT DOOR. Suddenly, EVELYN bursts out of the doorway from the basement.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: WE FOLLOW ON HER BACK as she maneuvers her feet desperately from PAINTED SPOT to PAINTED SPOT down the hall to the front door and to freedom!
  EXPRESSION: null
- CHARACTER: Evelyn
  LINE: null
  EXPRESSION: null
  STAGE_DIRECTION: grabs the stair post for support as she crosses through the front hall, only steps from the door when, OVER HER SHOULDER we barely see A DARK SHADOW WALKING UP THE SAND PATH!!!
- CHARACTER: Narrator
  LINE: EVELYN immediately spins around into CLOSE UP as we now LEAD HER as she rushes up the main stairs.
  EXPRESSION: Terrified
- CHARACTER: Narrator
  LINE: At the top of the stairs, WE TILT DOWN as she reaches to the floor and picks up the thick blankets covering the landing.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Behind her THE FRONT HALL LIGHTS BEGIN TO BRIGHTEN!
  EXPRESSION: null

::PATHS::
- CHOICE: "Run upstairs"
  TARGET: farmhouse_upstairs_bathroom
  STATE_CHANGE: Evelyn_upstairs = true
  CONDITION: null

::SCENE::
LOCATION: Barn Exterior
MOOD: Tense, Protective
CHARACTERS: Narrator, Lee, Marcus, Dark Shadow
BACKGROUND_IMAGE: barn_exterior.png
BACKGROUND_EDIT: "Dusk, outside the barn, sand path leading to farmhouse, lit red"

::SCRIPT::
- CHARACTER: Narrator
  LINE: WE HOLD ON the side of the barn as LEE enters with MARCUS and places him on the ground.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: WE FOLLOW LEE as he slowly cranes his neck to look around the barn. There, beautifully lit in RED is the sand path leading to the farmhouse. LEE’s eyes travel down the path and up the stairs and ONTO A LARGE DARK SHADOW NOW IN THE FRONT HALL!!!
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: LEE snaps his back against the wall, his eyes darting with fear as he thinks, thinks. Finally he turns to his son who stands looking at him blankly.
  EXPRESSION: Afraid
- CHARACTER: Lee
  LINE: null
  EXPRESSION: null
  STAGE_DIRECTION: immediately digs into his backpack and pulls out A FLASHLIGHT!
- CHARACTER: Lee
  LINE: null
  EXPRESSION: null
  STAGE_DIRECTION: places the flashlight in MARCUS’s hands. MARCUS looks up to him with familiar panic in his eyes.
- CHARACTER: Narrator
  LINE: LEE then slides closer to his son and gently places his hands on MARCUS shoulders.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Suddenly, LEE places his left hand straight up against his chest, crosses the fingers of his right hand, brings the two together and shoots his right hand into the sky.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: This is the same exact sign his four year old son made in the general store at the beginning of the movie. This means ROCKET.
  EXPRESSION: null
- CHARACTER: Marcus
  LINE: null
  EXPRESSION: Afraid
  STAGE_DIRECTION: shakes his head no.
- CHARACTER: Narrator
  LINE: LEE gently places his hands on MARCUS face and looks directly in his eyes. No doubt informed by the heart opening day they’ve had. It is a beautiful moment of strength as LEE communicates so much to his son.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: First and foremost, there is understanding and even an apology for the situation they are in. But then the look turns to imploring.
  EXPRESSION: null
- CHARACTER: Lee
  LINE: Your mother needs help. I need you to do this for her.
  EXPRESSION: Imploring
  STAGE_DIRECTION: (SIGNING)
- CHARACTER: Narrator
  LINE: MARCUS looks to his dad, his eyes change.
  EXPRESSION: null
- CHARACTER: Lee
  LINE: Please.
  EXPRESSION: Imploring
  STAGE_DIRECTION: (SIGNING)
- CHARACTER: Narrator
  LINE: And with that MARCUS is gone.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: ON LEE as he watches his son run down the side of the barn and disappear around the corner. He takes a deep breath. God protect his son. God protect all of them.
  EXPRESSION: Afraid
- CHARACTER: Narrator
  LINE: LEE turns and runs around the barn.
  EXPRESSION: Determined

::PATHS::
- CHOICE: "Marcus runs for help, Lee heads to farmhouse"
  TARGET: null
  STATE_CHANGE: Marcus_tasked = true, Lee_moving_to_farmhouse = true
  CONDITION: null

::SCENE::
LOCATION: Farmhouse Upstairs Bathroom
MOOD: Painful, Vulnerable
CHARACTERS: Narrator, Evelyn
BACKGROUND_IMAGE: farmhouse_bathroom.png
BACKGROUND_EDIT: "Dusk, upstairs bathroom, Evelyn entering with blankets, blood on floor"

::SCRIPT::
- CHARACTER: Narrator
  LINE: FROM ABOVE we see EVELYN enter the room carrying the thick blankets from the stairs and turns on the bathroom light spots of blood smear on the floor.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: ON EVELYN as she slowly gets into the bathtub. Tears fall down her face as she reaches over the wall of the tub and starts stacking the blankets from her knees to her chest.
  EXPRESSION: Sad
- CHARACTER: Narrator
  LINE: As she folds the last blanket over herself CONTRACTION!!!
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: This time her eyes go wide with the electric shock like pain.
  EXPRESSION: Pain

::PATHS::
- CHOICE: "Continue in labor"
  TARGET: null
  STATE_CHANGE: Evelyn_in_labor = true
  CONDITION: null

::SCENE::
LOCATION: Farmhouse - Upstairs Bathroom
MOOD: Intense, Terrifying
CHARACTERS: Narrator, Evelyn, Creature (implied)
BACKGROUND_IMAGE: farmhouse_bathroom.png
BACKGROUND_EDIT: "Dusk, dark and tense, sound of creature approaching"

::SCRIPT::
- CHARACTER: Narrator
  LINE: is the big one. THIS IS HAPPENING!
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Suddenly we hear TICK SCRAAAAAPE TICK SCRAAAAAPE Whatever IT is it’s trying to climb the stairs.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: TIGHT ON EVELYN’s hand as it jerks and grips till it turns white from force.
  EXPRESSION: Pain
- CHARACTER: Narrator
  LINE: FROM ABOVE, we see EVELYN in extreme pain, but somehow keeping it all in.
  EXPRESSION: Pain
- CHARACTER: Narrator
  LINE: Suddenly a small stream of blood begins to trickle by her exposed feet.
  EXPRESSION: Pain
- CHARACTER: Narrator
  LINE: ON THE BATHTUB. All that can be seen are EVELYN’s eyes as she peers over the bathtub wall. Through the door and to the steps.
  EXPRESSION: Afraid
- CHARACTER: Narrator
  LINE: Suddenly we hear again TICK SCRAAAAAPE TICK SCRAAAAAPE
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Just then, the light bulb above EVELYN begins to DIM!!!
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: QUICKLY BACK ON EVELYN as she begins to cry, preparing for the end. And then CONTRACTION!!!!
  EXPRESSION: Crying
- CHARACTER: Narrator
  LINE: FROM ABOVE as EVELYN’s face shoots to the sky with no affect. Her eyes wide, the rest of her face is calm.
  EXPRESSION: Pain
- CHARACTER: Narrator
  LINE: Then we see blood and fluid now pool around her feet as the light above her goes out.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: From only the light from the window we see EVELYN’s face finally crack in pain. Her mouth opens releasing the most guttural and now two person SCREEEEEEEAM!
  EXPRESSION: Pain
- CHARACTER: Narrator
  LINE: BUT, right at that moment, the screams of mother and baby are drowned out by a thundering. BOOOOOOOOOOOOOOOOOOM!!!!
  EXPRESSION: null

::PATHS::
- CHOICE: "Endure the birth and creature"
  TARGET: barn_bedroom
  STATE_CHANGE: fear = +3, evelyn_giving_birth = true
  CONDITION: null

::SCENE::
LOCATION: Barn - Lee's Bedroom - Stall
MOOD: Urgent, Determined
CHARACTERS: Narrator, Lee
BACKGROUND_IMAGE: barn_bedroom.png
BACKGROUND_EDIT: "Dusk, dimly lit stall, makeshift bedroom"

::SCRIPT::
- CHARACTER: Narrator
  LINE: LEE rushes into his room and reaches under his mattress and pulls out A SHOT GUN!
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Not the first choice, when trying not to make noise, but he has no other choice.
  EXPRESSION: Determined

::PATHS::
- CHOICE: "Arm himself"
  TARGET: cornfield
  STATE_CHANGE: lee_armed = true, readiness = +1
  CONDITION: null

::SCENE::
LOCATION: Farm - Cornfield
MOOD: Mysterious, Unsettling
CHARACTERS: Narrator, Marcus
BACKGROUND_IMAGE: farm_cornfield.png
BACKGROUND_EDIT: "Dusk, tall corn stalks, looming watering device"

::SCRIPT::
- CHARACTER: Narrator
  LINE: MARCUS walks down a thin sand path, suddenly stops and looks up to a HUGE OVERARCHING FIGURE ABOVE HIM!
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: It is a watering device found in cornfields that tower high above the corn and roll slowly through the fields on giant wheels.
  EXPRESSION: null

::PATHS::
- CHOICE: "Proceed cautiously"
  TARGET: farmhouse_sand_path
  STATE_CHANGE: tension = +1
  CONDITION: null

::SCENE::
LOCATION: Farmhouse - Sand Path
MOOD: Action, Intense, Visually Striking
CHARACTERS: Narrator, Lee
BACKGROUND_IMAGE: farmhouse_sand_path_night.png
BACKGROUND_EDIT: "Night, sand path leading to farmhouse, fireworks exploding overhead"

::SCRIPT::
- CHARACTER: Narrator
  LINE: WE TRACK WITH LEE as he sprints down the sand path holding the shotgun like a civil war soldier rushing into battle as ENORMOUS BLOOMS OF FIREWORKS BURST BEHIND HIM!!!!
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Red, green, white, large plumes, small sparkles falling down.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: In the midst of this unthinkable nightmare, it’s gorgeous.
  EXPRESSION: null

::PATHS::
- CHOICE: "Rush to the farmhouse"
  TARGET: road
  STATE_CHANGE: lee_location = "farmhouse_exterior", fireworks_active = true
  CONDITION: null

::SCENE::
LOCATION: Road
MOOD: Alert, Concerned
CHARACTERS: Narrator, Regan
BACKGROUND_IMAGE: road_night.png
BACKGROUND_EDIT: "Night, silhouettes of towering trees, fireworks lighting the sky"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Huge bursts of fireworks light up through the tops of the towering trees REGAN, sits up abruptly into the fireworks’ silhouette.
  EXPRESSION: Surprised
- CHARACTER: Narrator
  LINE: CLOSE ON REGAN as the colors illuminate on her face.
  EXPRESSION: Concerned

::PATHS::
- CHOICE: "Observe fireworks"
  TARGET: farmhouse_front_hall
  STATE_CHANGE: regan_alert = true
  CONDITION: null

::SCENE::
LOCATION: Farmhouse - Front Hall
MOOD: Tense, Cautious
CHARACTERS: Narrator, Lee
BACKGROUND_IMAGE: farmhouse_front_hall_night.png
BACKGROUND_EDIT: "Night, dimly lit front hall, dining room visible in background"

::SCRIPT::
- CHARACTER: Narrator
  LINE: FROM THE DINING ROOM, we look into the front hall in the background.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: SUDDENLY, FROM THE DOORWAY THE MUZZLE OF A GUN POKES THROUGH.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: THEN MOMENTS LATER, LEE WALKS IN STEALTHILY. MOVING THE GUN EXACTLY WHERE HIS EYES POINT. HE CLEARS THE ROOM.
  EXPRESSION: Determined
- CHARACTER: Narrator
  LINE: ON LEE’S BACK as we look down the gun barrel. He looks to the dining room. He looks to the living room. He looks to the STAIRS!!!
  EXPRESSION: Determined
- CHARACTER: Narrator
  LINE: LEE’S POV as he walks up the stairs. On each stair drops of blood. To the left, along the wall, the wallpaper has been intermittently RIPPED IN THREE EQUIDISTANT MEANDERING LINES.
  EXPRESSION: Concerned

::PATHS::
- CHOICE: "Ascend the stairs"
  TARGET: farmhouse_upstairs_hallway
  STATE_CHANGE: lee_investigating_damage = true
  CONDITION: null

::SCENE::
LOCATION: Farmhouse - Upstairs Hallway
MOOD: Anxious, Relief, Emotional
CHARACTERS: Narrator, Lee, Evelyn, Newborn Baby, Creature (implied)
BACKGROUND_IMAGE: farmhouse_upstairs_hallway_night.png
BACKGROUND_EDIT: "Night, exposed wood floor landing, bannister, bloodstains"

::SCRIPT::
- CHARACTER: Narrator
  LINE: THROUGH A DOORWAY into the now exposed wood floor landing with the bannister outlining the upstairs hall.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Suddenly, the top of LEE’s head enters frame, just as the creature’s had only moments before. Then his gun, facing into the bedrooms to the side. LEE moves the gun confidently in all directions, making sure the upstairs is clear.
  EXPRESSION: Determined
- CHARACTER: Narrator
  LINE: As LEE’s gaze comes around to face directly at us, his gun lowers and WE SLOWLY PULL BACK INTO THE ROOM TO REVEAL the bloodstained edge of the BATHTUB.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: ON LEE’s BACK as he rushes to the tub to find, just blood in an empty bathtub.
  EXPRESSION: Distraught
- CHARACTER: Narrator
  LINE: LEE turns into his own CLOSE UP PROFILE as his back slides down the bathtub and onto the floor. His hand releases the gun to the floor. His eyes close and he begins to softly weep.
  EXPRESSION: Crying
- CHARACTER: Narrator
  LINE: A mirror behind LEE reflects the room back to him, revealing for the first time, a beveled glass shower door at the opposite end of the room. Suddenly A BLOODY HAND HITS THE GLASS!!!! And the shower door slowly opens!!!
  EXPRESSION: Surprised
- CHARACTER: Narrator
  LINE: OVER LEE as he scrambles to the shower and opens the door!
  EXPRESSION: Hopeful
- CHARACTER: Narrator
  LINE: Stuffed inside is a quivering pile of blankets.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: LEE drops to his knees and pulls back the blankets to see his wife. Pale, with eyes closed, she’s breathing. And in her arms a sleeping newborn baby.
  EXPRESSION: Relieved

::PATHS::
- CHOICE: "Find family"
  TARGET: cornfield_return
  STATE_CHANGE: evelyn_safe = true, baby_born = true, lee_emotional_state = "relieved"
  CONDITION: null

::SCENE::
LOCATION: Cornfield
MOOD: Eerie, Safe
CHARACTERS: Narrator, Marcus
BACKGROUND_IMAGE: cornfield_night.png
BACKGROUND_EDIT: "Night, dense corn, watering device silhouette, distant fireworks"

::SCRIPT::
- CHARACTER: Narrator
  LINE: WE HOLD ON THE TOPS OF THE DENSE CORN, the creature like silhouette of the giant watering device looming as the last of a series of bottle rockets fire into the darkening night sky.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: WE MOVE ABOVE THE CORN and then descend through it onto a thin sand path and onto MARCUS.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: WE FOLLOW WITH HIM as he safely walks back toward the BARN, holding his flashlight, as the final bursts of fireworks illuminate behind him.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: On MARCUS’ face is
  EXPRESSION: null

::PATHS::
- CHOICE: "Return to safety"
  TARGET: end
  STATE_CHANGE: marcus_safe = true
  CONDITION: null

::SCENE::
LOCATION: Cornfield Clearing
MOOD: Intense Fear, Panic
CHARACTERS: Narrator, Marcus
BACKGROUND_IMAGE: cornfield.png
BACKGROUND_EDIT: "Nighttime, dense cornstalks, dimming flashlight"

::SCRIPT::
- CHARACTER: Narrator
  LINE: genuine pride. He knows he has done something heroic. Suddenly WE HEAR THE SNAP OF CORNSTALKS!!!
  EXPRESSION: null
- CHARACTER: Marcus
  LINE: (frantically whips his light around the path behind him.)
  EXPRESSION: Afraid
- CHARACTER: Narrator
  LINE: WE FOLLOW HIS LIGHT as it scans the path and the stalks. Even with nothing there, it’s terrifying.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Just then, his flashlight begins to DIM.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: SNAP!!!
  EXPRESSION: null
- CHARACTER: Marcus
  LINE: (whips his light around to the thin sand path in FRONT of him. Nothing.)
  EXPRESSION: Afraid
- CHARACTER: Narrator
  LINE: SNAP!!! CRUNCH!!! SNAP!!! CRUNCH!!! Something ELSE is moving toward him fast!
  EXPRESSION: null
- CHARACTER: Marcus
  LINE: (turns around, away from the BARN AND RUNS!!!!)
  EXPRESSION: Terrified
- CHARACTER: Narrator
  LINE: WE ARE ON MARCUS’ FACE AS HE RUNS
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Scanning, scanning SNAP!!! SCANNING!!! CRUNCH!!! SCANNING!!
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: HIS FLASHLIGHT STARTS TO FLICKER OUT.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: THE CORN TO HIS RIGHT BEGINS TO SNAP.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: IT'S COMING CLOSER!
  EXPRESSION: null
- CHARACTER: Marcus
  LINE: (turns and begins to run INTO THE CORN!!!!)
  EXPRESSION: Panicked
- CHARACTER: Narrator
  LINE: WE ARE NOW IN A TERRIFYING PERSPECTIVE HANDHELD, AS CORN CROSSES RIGHT PAST LENS. THE FLASHLIGHT not able to cast light on anything that’s not right in our face, creating almost a STROBE EFFECT!!! MARCUS is making A TON OF SOUND!!!!
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: ON MARCUS’ FACE pure panic. When suddenly WE ARRIVE into a small clearing to see A TRACTOR, completely overgrown with corn. MARCUS immediately climbs onto the tractor and frantically whips his light around the clearing and into the dense corn.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: THE LIGHT STARTS TO DIM SNAP!!! CRUNCH!!! SNAP!!! CRUNCH!!!
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Something is moving toward him FAST! THE LIGHT BEGINS TO FLICKER and then goes out.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Suddenly, off in the corn in front of him (AND FOR THE FIRST TIME) we hear A LOUD SCREEEEEEEEEEEEEEECH!!!! The light suddenly BLARES BRIGHT as A DEER HEAD POPS OUT OF THE CORN!!!!!!!!
  EXPRESSION: null
- CHARACTER: Marcus
  LINE: (flies back in fear! Slipping from the top of the tractor and SLAMMING HIS HEAD INTO THE WHEEL WELL.)
  EXPRESSION: Terrified
- CHARACTER: Narrator
  LINE: BLACK
  EXPRESSION: null

::PATHS::
- CHOICE: "Black out"
  TARGET: farm_driveway
  STATE_CHANGE: marcus_injured = true, fear = +2
  CONDITION: null

::SCENE::
LOCATION: Farm Driveway
MOOD: Eerie, Somber, Suspenseful
CHARACTERS: Narrator, Regan
BACKGROUND_IMAGE: farm_driveway.png
BACKGROUND_EDIT: "Dark night, firework smoke, flickering cornstalks, silo lights"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Fade in: The night is now dark.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: WE ARE BEHIND REGAN walking. AS WE ARE WITH HER WE ARE IN TOTAL SILENCE.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: She looks around at the remnants of the last horrifying moments more reminiscent of a soldier returning to a battlefield, then a girl returning to a farm, we see countless streamers of firework smoke still falling gracefully from the sky. The tips of dry corn stalks flicker alight with small flames. Off in the distance we see lights of the SILO. Shining like a beacon.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: REGAN walks along the eerie shadows of corn stalks when suddenly at her feet cracks of light.
  EXPRESSION: null
- CHARACTER: Regan
  LINE: (lowers to her knees and puts her head to the ground to see a bright light, cutting through the bottom of the stalks of corn.)
  EXPRESSION: Curious
- CHARACTER: Narrator
  LINE: Suddenly, the pliers REGAN used to work on the TOY SHUTTLE slip out of the pocket of her dress AND CRASH ONTO A ROCK ON THE GROUND!!!
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: REGAN doesn’t even notice because she didn’t even hear it.
  EXPRESSION: null
- CHARACTER: Regan
  LINE: (sits back up to kneeling position when suddenly the cornstalks behind her BEGIN TO LAY DOWN AS A SHADOW EMERGES!!!)
  EXPRESSION: Surprised
- CHARACTER: Narrator
  LINE: At that exact moment, we begin to hear the oddest and unpleasant beeeeeeeeeeeep.
  EXPRESSION: null
- CHARACTER: Regan
  LINE: (eyes begin to squint slightly. Then, her hand slowly reaches up to her ear?)
  EXPRESSION: Confused
- CHARACTER: Narrator
  LINE: SHE CAN HEAR THE BEEP!!!!
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: SUDDENLY the SHADOW moves closer to REGAN and THE BEEEEEEP GROWS!!!
  EXPRESSION: null
- CHARACTER: Regan
  LINE: (face now scrunches up in agony as she grabs her ears!!!)
  EXPRESSION: Pain
- CHARACTER: Regan
  LINE: (digs into her right ear, rips out the hearing aid and launches forward!!)
  EXPRESSION: Pain
- CHARACTER: Narrator
  LINE: SILENCE.
  EXPRESSION: null
- CHARACTER: Regan
  LINE: (kneels back up into frame THE SHADOW IS GONE!)
  EXPRESSION: Relieved
- CHARACTER: Narrator
  LINE: SHE NEVER EVEN KNEW IT WAS THERE.
  EXPRESSION: null
- CHARACTER: Regan
  LINE: (Breathing wildly, looks at the hearing aid in her hand.)
  EXPRESSION: Surprised
- CHARACTER: Narrator
  LINE: Her face is almost electrified! As excruciating as that was THAT IS THE FIRST SOUND SHE HAS EVER HEARD!
  EXPRESSION: null
- CHARACTER: Regan
  LINE: (slowly puts the hearing aid back in her ear.)
  EXPRESSION: Curious
- CHARACTER: Narrator
  LINE: Nothing.
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue towards the clearing"
  TARGET: cornfield_clearing_regan
  STATE_CHANGE: regan_heard_sound = true, fear = +1
  CONDITION: null

::SCENE::
LOCATION: Cornfield Clearing
MOOD: Discovery, Suspense, Relief
CHARACTERS: Narrator, Regan, Marcus
BACKGROUND_IMAGE: cornfield_clearing.png
BACKGROUND_EDIT: "Nighttime, scattered debris, deer carcass, flashlight beam"

::SCRIPT::
- CHARACTER: Narrator
  LINE: WE FOLLOW REGAN as she walks down the small path leading to... the clearing. One ladder stands, the other ladder on the ground, bottles and fireworks litter the ground. And then, there in the center of the clearing, lit by the flashlight one half of a deer carcass.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: No sign of MARCUS.
  EXPRESSION: null
- CHARACTER: Regan
  LINE: (slowly bends down to pick up the flashlight when suddenly THE CARCASS MOVES!)
  EXPRESSION: Curious
- CHARACTER: Regan
  LINE: (jumps back, terrified!!!)
  EXPRESSION: Terrified
- CHARACTER: Narrator
  LINE: Then from under the neck of the dee a hand!!
  EXPRESSION: null
- CHARACTER: Regan
  LINE: (runs over and pushes the carcass off of MARCUS, who has been safely lying underneath.)
  EXPRESSION: Relieved
- CHARACTER: Marcus
  LINE: (Covered in blood, scrambles to try to get to his feet.)
  EXPRESSION: Injured
- CHARACTER: Regan
  LINE: (grabs him and holds him tight. She places her finger to her lips, just like her dad.)
  EXPRESSION: Protective
- CHARACTER: Regan
  LINE: (looks around to see if they have a chance to run and then thinks better of it. She looks back to her brother and places her hand on his chest.)
  EXPRESSION: Determined
- CHARACTER: Narrator
  LINE: WE RISE above the clearing, above the overgrown tractor and once again into the night.
  EXPRESSION: null

::PATHS::
- CHOICE: "Head towards the farmhouse"
  TARGET: farmhouse_exterior
  STATE_CHANGE: marcus_discovered = true, regan_protective = true
  CONDITION: null

::SCENE::
LOCATION: Farmhouse
MOOD: Unsettled, Transition
CHARACTERS: Narrator
BACKGROUND_IMAGE: farmhouse.png
BACKGROUND_EDIT: "Nighttime, distant view of farmhouse"

::SCRIPT::
- CHARACTER: Narrator
  LINE: WE
  EXPRESSION: null

::PATHS::
- CHOICE: "Enter the farmhouse"
  TARGET: end
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Farmhouse Exterior to Barn Exterior
MOOD: Desperate, terrifying, frantic
CHARACTERS: Narrator, Lee, Evelyn, Baby
BACKGROUND_IMAGE: farmhouse_barn.png
BACKGROUND_EDIT: "Nighttime, calm air initially, then wind, red Christmas lights, long path, barn in distance"

::SCRIPT::
- CHARACTER: Narrator
  LINE: ARE WIDE on the FARMHOUSE. The RED CHRISTMAS lights sway gently in the now calm night air.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: After a long quiet moment LEE appears at the doorway. He carries EVELYN in his arms the baby in hers.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: He slowly descends the porch stairs and begins to walk toward the BARN his eyes locked firmly on his cargo. For a moment, as LEE walks, this all feels almost like a dream. Or the end of a nightmare. Respite.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: WE ARE TIGHT ON EVELYN who we see is unconscious from the trauma and the loss of fluids THEN DOWN TO the tightly wrapped baby sleeping in her arms.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: LEE looks ahead to the doors of the BARN off in the seemingly never ending distance.
  EXPRESSION: Focused
- CHARACTER: Narrator
  LINE: Suddenly THE BABY BEGINS TO STIR!!!
  EXPRESSION: Surprised
- CHARACTER: Narrator
  LINE: LEE’s eyes shoot down to see the baby streeeeeeeeetch and slowly begin to open it’s eyes.
  EXPRESSION: Concerned
- CHARACTER: Narrator
  LINE: ON THE BABY as it looks up, searchingly, at his father as his father picks up his pace!
  EXPRESSION: Null
- CHARACTER: Narrator
  LINE: Suddenly, we begin to notice the dim red light on the baby’s face BEGINS TO FLICKER!
  EXPRESSION: Alarmed
- CHARACTER: Narrator
  LINE: ON THE BARN DOORS getting closer, closer.
  EXPRESSION: Null
- CHARACTER: Narrator
  LINE: ON LEE as he trudges with everything he has to get his baby to safety when suddenly a cold wind blows across LEE’s face and through his hair.
  EXPRESSION: Null
- CHARACTER: Narrator
  LINE: LEE slowly looks down as THE BABY CRIES!!!!!!
  EXPRESSION: Frightened
- CHARACTER: Narrator
  LINE: WE HOLD DIRECTLY ON LEE, LEADING HIM, as he breaks into a full sprint!
  EXPRESSION: Desperate
- CHARACTER: Narrator
  LINE: LEE’S eyes momentarily dart quickly to the side, not at all prepared for what he might find.
  EXPRESSION: Anxious
- CHARACTER: Narrator
  LINE: WE NEVER LEAVE LEE’s FACE. As his head bobs back and forth from running, we intermittently catch glimpses of the long path behind him.
  EXPRESSION: Null
- CHARACTER: Narrator
  LINE: First we see the FARMHOUSE shrinking in the distance behind him. And then we hear SNAP!!!
  EXPRESSION: Startled
- CHARACTER: Narrator
  LINE: BEHIND LEE the large tree near the farmhouse moves wildly!!
  EXPRESSION: Terrified
- CHARACTER: Narrator
  LINE: LEE’s eyes never even widen. There is no surprise. This is the moment he knew would come. As he sprints with everything he has the string of bulbs above him DIM DOWN TO ALMOST NOTHING!!!!
  EXPRESSION: Determined
- CHARACTER: Narrator
  LINE: IN THE DARK DISTANCE BEHIND HIM A SCREEEEEEEEEEEEEEECH!!!!
  EXPRESSION: Terrified
- CHARACTER: Narrator
  LINE: Lee is running running closer, closer then LEE BURSTS THROUGH THE HEAVY QUILTS!!! HE’S IN THE BARN!!
  EXPRESSION: Relieved

::PATHS::
- CHOICE: "Enter barn"
  TARGET: barn_interior
  STATE_CHANGE: fear = +3, adrenaline = +5
  CONDITION: null

::SCENE::
LOCATION: Barn Interior
MOOD: Chaotic, desperate
CHARACTERS: Narrator, Lee, Evelyn, Baby
BACKGROUND_IMAGE: barn_interior.png
BACKGROUND_EDIT: "Nighttime, familiar interior of barn, quilts hanging"

::SCRIPT::
- CHARACTER: Narrator
  LINE: WE ARE ON LEE as he sprints through the familiar interior of the BARN. When suddenly WE HEAR A HUGE BANG!!!
  EXPRESSION: Terrified
- CHARACTER: Narrator
  LINE: Then THE HEAVY QUILTS FLY UP INTO THE AIR!!! JUST AS LEE DESCENDS INTO THE GROUND!
  EXPRESSION: Terrified

::PATHS::
- CHOICE: "Enter safe room"
  TARGET: barn_safe_room
  STATE_CHANGE: adrenaline = +2, fear = +2
  CONDITION: null

::SCENE::
LOCATION: Barn Safe Room
MOOD: Terrifying, desperate, confined
CHARACTERS: Narrator, Lee, Evelyn, Baby
BACKGROUND_IMAGE: barn_safe_room.png
BACKGROUND_EDIT: "Nighttime, dark, confined space, hay bale, hidden room"

::SCRIPT::
- CHARACTER: Narrator
  LINE: LEE falls back onto the steps, barely holding onto his wife and child as his free hand reaches for the mattress!
  EXPRESSION: Desperate
- CHARACTER: Narrator
  LINE: As LEE finally grabs the mattress and slides it over the opening above the stairwell.
  EXPRESSION: Determined
- CHARACTER: Narrator
  LINE: BLACK in total darkness we hear LEE’S BREATH QUICKENS AN ODD SOUND OF SOMETHING HEAVY ABOVE THE CREATURES ARE INSIDE THE BARN!!!! A CACOPHONY OF SCRATCHING, TEARING AND SCREECHING.
  EXPRESSION: Terrified
- CHARACTER: Narrator
  LINE: Then FIRE!! LEE’s lighter cuts through the black and then retreats into a small glow in the room as we try to comprehend what’s happening.
  EXPRESSION: Relieved
- CHARACTER: Narrator
  LINE: We see EVELYN has been placed on a hay bale as ABOVE A CRASH!!!!! THE CREATURES ARE TEARING THROUGH THE ROOMS AND DROWNING THE SOUNDS OF THE FAMILY BELOW.
  EXPRESSION: Terrified
- CHARACTER: Narrator
  LINE: FOR THE MOMENT LEE picks up the crying baby as we PUSH IN.
  EXPRESSION: Caring
- CHARACTER: Narrator
  LINE: For one brief second amidst the fury of nerves and sound we see a father holding his newborn child for the first time. It is a precious, once in a lifetime moment.
  EXPRESSION: Tender
- CHARACTER: Narrator
  LINE: Then A PLASTIC MASK COMES INTO FRAME and ONTO THE BABY’s FACE!!!!
  EXPRESSION: Urgent
- CHARACTER: Narrator
  LINE: As if in an airplane video, LEE wraps the mask’s strap behind the baby’s head and then LOWERS THE BABY INTO THE WOODEN, QUILT LINED BOX!
  EXPRESSION: Desperate
- CHARACTER: Narrator
  LINE: WE PAN TO THE SIDE of the box, along a clear plastic tube to a stand up air canister. LEE’s hand enters frame and turns the valve a quiet whisper of air.
  EXPRESSION: Focused
- CHARACTER: Narrator
  LINE: LEE stares down at his tiny crying baby wearing an oxygen mask. The juxtaposed image seemingly almost as bizarre to him as it is to us.
  EXPRESSION: Sad
- CHARACTER: Narrator
  LINE: THEN LEE PLACES A LARGE STACK OF BLANKETS OVER THE TOP OF THE BOX!!!! AND THEN A COVER!!!!
  EXPRESSION: Determined
- CHARACTER: Narrator
  LINE: THE BABY’S SCREAMS CAN’T BE HEARD.
  EXPRESSION: Relieved
- CHARACTER: Narrator
  LINE: THE BANGING, THE SCREECHING INCREASE IN TEMPO AND SOUND!!!
  EXPRESSION: Terrified
- CHARACTER: Narrator
  LINE: LEE just stares down at the small casket like box.
  EXPRESSION: Resigned
- CHARACTER: Narrator
  LINE: This either work or they’re dead.
  EXPRESSION: Grave

::PATHS::
- CHOICE: "Hide the baby"
  TARGET: cornfield_driveway
  STATE_CHANGE: hope = +1, fear = +5
  CONDITION: null

::SCENE::
LOCATION: Cornfield Driveway
MOOD: Urgent, disorienting
CHARACTERS: Narrator, Regan, Marcus
BACKGROUND_IMAGE: cornfield_driveway.png
BACKGROUND_EDIT: "Nighttime, dark, cornfields, flashlight, farm equipment shadows"

::SCRIPT::
- CHARACTER: Narrator
  LINE: WE FOLLOW REGAN and MARCUS as they sprint up the main sand path/driveway running parallel to the cornfields. With the flashlight slicing through the darkness, it’s nearly impossible to tell where we are.
  EXPRESSION: Null
- CHARACTER: Narrator
  LINE: Suddenly the corn ends and OVER MARCUS AND REGAN we see shadows of farm equipment!
  EXPRESSION: Surprised
- CHARACTER: Narrator
  LINE: REGAN turns her head and looks up.
  EXPRESSION: Curious
- CHARACTER: Narrator
  LINE: REGAN’s POV as we climb higher and higher to the top of the SILO!
  EXPRESSION: Determined

::PATHS::
- CHOICE: "Climb silo"
  TARGET: silo_top
  STATE_CHANGE: height = +1, danger = +1
  CONDITION: null

::SCENE::
LOCATION: Barn Safe Room
MOOD: Eerie, suspenseful
CHARACTERS: Narrator
BACKGROUND_IMAGE: barn_safe_room_later.png
BACKGROUND_EDIT: "Nighttime, total silence, dark brown frame, IV bag"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Silence.
  EXPRESSION: Null
- CHARACTER: Narrator
  LINE: The frame filled with a dark brown.
  EXPRESSION: Null
- CHARACTER: Narrator
  LINE: Time has passed.
  EXPRESSION: Null
- CHARACTER: Narrator
  LINE: Then WE TRAVEL DOWN from the dirt ceiling past a hook on the wooden support beam to a clear plastic IV BAG hanging down a fluid filled plastic tube and into an
  EXPRESSION: Null

::PATHS::
- CHOICE: "Continue observing"
  TARGET: end_excerpt
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Barn
MOOD: Relief, grief, rising anxiety
CHARACTERS: Evelyn, Lee, Baby
BACKGROUND_IMAGE: barn_interior.png
BACKGROUND_EDIT: "Low lit, hay bale, medical IV setup, aftermath of birth"

::SCRIPT::
- CHARACTER: Narrator
  LINE: WE PULL BACK to reveal EVELYN lying on the hay bale comfortably, her eyes still closed. She has been bandaged and wears LEE’s sweater. A single burning candle by her side.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Then EVELYN SHOOTS AWAKE!!! SHE SCRAMBLES TO SIT UP THROUGH THE PAIN!!! HER EYES SEARCH A LOW LIT ROOM!!! SHE GOES TO SIT UP AND WINCES AN IV IS IN HER ARM!!
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Out of the darkness comes LEE! He is holding the baby.
  EXPRESSION: null
- CHARACTER: Lee
  LINE: It’s ok. It’s ok! Your safe.
  EXPRESSION: Reassuring
- CHARACTER: Narrator
  LINE: EVELYN looks up at LEE immediately confused as to why he’s talking then it sinks in.
  EXPRESSION: Confused
- CHARACTER: Evelyn
  LINE: It worked?
  EXPRESSION: Hopeful
- CHARACTER: Lee
  LINE: It worked.
  EXPRESSION: Relieved
- CHARACTER: Evelyn
  LINE: It worked, it worked.
  EXPRESSION: Overjoyed
- CHARACTER: Narrator
  LINE: LEE holds up the sleeping baby and places it in EVELYN’s arms. Tears fall down her face. She looks back up to her husband and then around the room.
  EXPRESSION: Emotional
- CHARACTER: Evelyn
  LINE: Where’s Marcus?
  EXPRESSION: Concerned
- CHARACTER: Narrator
  LINE: Pause.
  EXPRESSION: null
- CHARACTER: Lee
  LINE: I’ll find them.
  EXPRESSION: Determined
- CHARACTER: Evelyn
  LINE: Them?!
  EXPRESSION: Alarmed
- CHARACTER: Narrator
  LINE: EVELYN immediately tenses.
  EXPRESSION: Tensed
- CHARACTER: Narrator
  LINE: LEE takes the sleeping baby from EVELYN and places it in the safe wooden box. No air mask needed now.
  EXPRESSION: null
- CHARACTER: Evelyn
  LINE: She was with me in the house. I was doing laundry and she-- He was with you. How did he--
  EXPRESSION: Frantic
- CHARACTER: Narrator
  LINE: LEE sits next to his wife and begins to lay her back down.
  EXPRESSION: null
- CHARACTER: Lee
  LINE: Rockets.
  EXPRESSION: Somber
- CHARACTER: Narrator
  LINE: EVELYN pauses.
  EXPRESSION: null
- CHARACTER: Evelyn
  LINE: Then he-- then he’s still there. He’d know to--
  EXPRESSION: Anxious
- CHARACTER: Narrator
  LINE: LEE sits next to his wife and begins to lay her back down.
  EXPRESSION: null
- CHARACTER: Lee
  LINE: I’m sure he is.
  EXPRESSION: Reassuring
- CHARACTER: Evelyn
  LINE: She’s smart she’ll have found a place to-- She’s smart.
  EXPRESSION: Desperate hope
- CHARACTER: Narrator
  LINE: EVELYN’s gaze finally lands on her child.
  EXPRESSION: null
- CHARACTER: Evelyn
  LINE: It’s a boy.
  EXPRESSION: Tender
- CHARACTER: Lee
  LINE: It’s a boy.
  EXPRESSION: Tender
- CHARACTER: Evelyn
  LINE: It’s a boy.
  EXPRESSION: Awed
- CHARACTER: Narrator
  LINE: Pause.
  EXPRESSION: null
- CHARACTER: Evelyn
  LINE: I could have carried him.
  EXPRESSION: Regretful
- CHARACTER: Narrator
  LINE: LEE looks at his wife confused.
  EXPRESSION: Confused
- CHARACTER: Evelyn
  LINE: He was so heavy.
  EXPRESSION: Distant
- CHARACTER: Narrator
  LINE: LEE freezes.
  EXPRESSION: Shocked
- CHARACTER: Evelyn
  LINE: I can still feel the weight in my arms. He was small, but so heavy, wasn’t he?
  EXPRESSION: Grief-stricken
- CHARACTER: Narrator
  LINE: LEE can’t speak.
  EXPRESSION: Heartbroken
- CHARACTER: Evelyn
  LINE: My hands were free-- I was carrying the bag, but my hands were still free. I could have carried him. I should have carried him.
  EXPRESSION: Self-blaming
- CHARACTER: Lee
  LINE: Evelyn.
  EXPRESSION: Pleading
- CHARACTER: Evelyn
  LINE: Who are we if we can’t protect them. Who are we?
  EXPRESSION: Desperate
- CHARACTER: Narrator
  LINE: LEE is frozen every image rushing back to him.
  EXPRESSION: Traumatized
- CHARACTER: Evelyn
  LINE: You have to protect them.
  EXPRESSION: Insistent
- CHARACTER: Lee
  LINE: I will.
  EXPRESSION: Resolute
- CHARACTER: Evelyn
  LINE: Promise me. We can’t-- You need to protect them.
  EXPRESSION: Pleading

::PATHS::
- CHOICE: "Continue"
  TARGET: silo_roof_1
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Silo Roof
MOOD: Desperation, dwindling hope
CHARACTERS: Marcus, Regan
BACKGROUND_IMAGE: silo_roof_night.png
BACKGROUND_EDIT: "Nighttime, fire pit, open farm fields, dark"

::SCRIPT::
- CHARACTER: Narrator
  LINE: CLOSE ON A FLAME!!!
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: As it dies down, coming into view we see MARCUS sitting in front of the shallow metal drum their father sat in front of the night before.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: REGAN walks around the fire looking out across the farm for any sign of her father.
  EXPRESSION: Searching
- CHARACTER: Narrator
  LINE: Just as the fire is about to die out, REGAN walks back and squirts the last remaining fluid from the bottle. The fire rages again and illuminates the two children as well as the fading hope on their faces.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The fire begins to die down again. REGAN rummages in the box picking up the empty bottles of lighter fluid and shaking them frantically.
  EXPRESSION: Desperate
- CHARACTER: Narrator
  LINE: She shakes the last empty bottle and slumps down, defeated, scared.
  EXPRESSION: Defeated
- CHARACTER: Narrator
  LINE: In the last moments of the dying flame.
  EXPRESSION: null
- CHARACTER: Marcus
  LINE: He’ll come for us.
  EXPRESSION: Signing, hopeful
- CHARACTER: Narrator
  LINE: The two kids stare off desperately over the farm, preventing them from seeing far off in the distance to the right.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: A fire ignites. Then farther off, another fire.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: BUT THIS TIME ITS ONLY TWO!
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The kids don’t even notice.
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue"
  TARGET: barn_2
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Barn
MOOD: Desolation, lingering danger, quiet aftermath
CHARACTERS: Lee, Narrator
BACKGROUND_IMAGE: barn_interior_destroyed.png
BACKGROUND_EDIT: "Nighttime, interior of barn, tossed and ravaged, monopoly game visible, claw marks"

::SCRIPT::
- CHARACTER: Narrator
  LINE: WE ARE ON THE FAMILIAR image of the interior of the BARN.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Suddenly, the mattress on the ground moves.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Then LEE’s head slowly arises from underground.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: LEE stands to see their barn, their life has been tossed and ravaged.
  EXPRESSION: Somber
- CHARACTER: Narrator
  LINE: LEE places the mattress back over the large unfinished hole leading down to the safe room and stands up. LEE stares down at the mattress and what it protects, then walks out of frame.
  EXPRESSION: Protective
- CHARACTER: Narrator
  LINE: WE HOLD ON THE mattress a moment and then SLOWLY MOVE along the floor of the BARN past the monopoly game until we reach the bedroom stalls to see A LARGE CLAW MARK GOUGED OUT OF THE BARN WALL!
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: As we move down we see a pipe above the long trough on the wall has broken WATER DRIPS FROM THE BROKEN PIPE AND A POOL OF WATER MOVES ACROSS THE FLOOR!
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue"
  TARGET: silo_roof_2
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Silo Roof
MOOD: Frustration, searching for connection, discovery
CHARACTERS: Regan, Marcus
BACKGROUND_IMAGE: silo_roof_night.png
BACKGROUND_EDIT: "Nighttime, close on Regan, stars visible, faint light from dying fire"

::SCRIPT::
- CHARACTER: Narrator
  LINE: CLOSE ON REGAN, oddly lit. She lays on her back staring up at the stars. REGAN fumbles with something in her ear.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: WE GO EXTREME CLOSE on her turning the tiny dial on top of her hearing aid. As she does, she places her other hand by her ear and rubs her fingers together, hoping to hear a sound.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Nothing.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: REGAN turns the dial even more. Nothing.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: REGAN immediately rolls over, frustrated. Sitting directly in her view, on his dad’s small stool is MARCUS looking out hopefully to the farm.
  EXPRESSION: Frustrated
- CHARACTER: Marcus
  LINE: He’ll come.
  EXPRESSION: Signing, hopeful
- CHARACTER: Narrator
  LINE: REGAN scoffs and goes to get up when suddenly, under her dad’s stool she sees a box, the box LEE kept the photo in.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: She reaches under the stool and grabs it.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: NOW CLOSE OVER THE BOX ONTO REGAN as she stares down at it.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Then as the lid opens, it covers frame completely to BLACK.
  EXPRESSION: null

::PATHS::
- CHOICE: "End scene"
  TARGET: end
  STATE_CHANGE: null
  CONDITION: null

