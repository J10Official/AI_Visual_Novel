::SCENE::
LOCATION: Grave Marker
MOOD: Melancholy
CHARACTERS: Narrator
BACKGROUND_IMAGE: grave_marker_smucky.png
BACKGROUND_EDIT: "Plywood cross leaning aslant, faded black paint"

::SCRIPT::
- CHARACTER: Narrator
  LINE: that most persistent summer SOUND: crickets in high grass--ree-ree-ree-ree... This in dark which slowly
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: It’s a plywood cross leaning aslant. Written on the crossarm in black paint which has faded: SMUCKY HE WAS OBEDIENT. The letters are faded. They are also straggling and ill-formed--the work of a child.
  EXPRESSION: null

::PATHS::
- CHOICE: Continue to next marker
  TARGET: grave_marker_biffer
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Grave Marker
MOOD: Melancholy
CHARACTERS: Narrator
BACKGROUND_IMAGE: grave_marker_biffer.png
BACKGROUND_EDIT: "Chunk of warped crating with child's printing"

::SCRIPT::
- CHARACTER: Narrator
  LINE: A child’s printing again, this time on a chunk of warped crating: BIFFER BIFFER A HELLUVA SNIFFER UNTIL HE DIED HE MADE US RICHER 1971-1974.
  EXPRESSION: null

::PATHS::
- CHOICE: Continue to next marker
  TARGET: grave_marker_two
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Grave Markers
MOOD: Melancholy, Eerie
CHARACTERS: Narrator
BACKGROUND_IMAGE: grave_markers_two.png
BACKGROUND_EDIT: "Two child-made markers in grass, flowers in cheap vases"

::SCRIPT::
- CHARACTER: Narrator
  LINE: I think all these shots are LAP DISSOLVES. All is silence but for the crickets and the wind stirring the grass. Around the markers themselves, the grass has been clipped short, and by some markers there are flowers in cheap vases. Crisco cans, Skippy peanut butter jars, etc.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: These two markers: IN MEMORY OF MARTA OUR PET RABIT DYED MARCH 1, 1965 (on a wide flat board) and GEN PATTON (OUR! GOOD! DOG!) APRIL 1958 (another board).
  EXPRESSION: null

::PATHS::
- CHOICE: Continue to next marker
  TARGET: grave_marker_five_six
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Grave Markers
MOOD: Eerie
CHARACTERS: Narrator
BACKGROUND_IMAGE: grave_markers_five_six.png
BACKGROUND_EDIT: "Woodland clearing with numerous animal gravestones"

::SCRIPT::
- CHARACTER: Narrator
  LINE: We can't read all of them; some are too faded (or the "gravestones" themselves too degenerated), but we can see now that this woodland clearing’s a rather eerie -- and well-populated -- animal graveyard.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: We can see: POLYNESIA, 1953 and HANNAH THE BEST DOG THAT EVER LIVED. HANNAH’S tombstone is part of an old Chevrolet hood, painstakingly hammered flat.
  EXPRESSION: null

::PATHS::
- CHOICE: Continue to overview of graveyard
  TARGET: pet_sematary_overview
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Pet Sematary Overview
MOOD: Eerie, Foreboding
CHARACTERS: Narrator
BACKGROUND_IMAGE: pet_sematary_overview.png
BACKGROUND_EDIT: "Clearing surrounded by pines, graves in concentric circles, archway"

::SCRIPT::
- CHARACTER: Narrator
  LINE: From here we can see most of the clearing, which is surrounded by forest pines. We can see that the graves--maybe 80 in all--are arranged in rough concentric circles. On the far side of this clearing is the end of a path which spills into this graveyard clearing. The end of the path is flanked by wooden poles which hold up a crude arch. We can see no writing on this side -- the words on the arch face those arriving along the path.
  EXPRESSION: null

::PATHS::
- CHOICE: Continue to archway
  TARGET: archway_cu
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Archway (from path side, CU)
MOOD: Ominous
CHARACTERS: Narrator
BACKGROUND_IMAGE: archway_cu.png
BACKGROUND_EDIT: "Close-up of faded child's writing on crude arch"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Written on the arch in faded black paint is the work of some long-gone child: PET SEMATARY.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: THE CAMERA HOLDS ON THIS FOR A MOMENT OR TWO, THEN PANS SLOWLY DOWN to look through the arch. From this angle we are looking across to a deadfall--a tangle of weather-whitened old dead branches at the back of the graveyard. It’s maybe twenty-five feet from side to side and about nine feet high. At either end are thick tangles of underbrush that look impassible.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: AS MAIN TITLES CONCLUDE, THE CAMERA MOVES SLOWLY IN on the deadfall. And as it does, we realize that there is a horrible snarling face in those branches. Is this an accident? Coincidence? Our imagination? Perhaps the audience will wonder. THE CAMERA HOLDS ON IT and then we
  EXPRESSION: null

::PATHS::
- CHOICE: Fade to black
  TARGET: black_title_card
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Black
MOOD: Transition
CHARACTERS: Narrator
BACKGROUND_IMAGE: black.png
BACKGROUND_EDIT: "Solid black screen"

::SCRIPT::
- CHARACTER: Narrator
  LINE: BLACK. And a white title card: MOVING DAY.
  EXPRESSION: null

::PATHS::
- CHOICE: Continue to new house
  TARGET: country_house_evening
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: A House in the Country
MOOD: Peaceful, Transition
CHARACTERS: Narrator
BACKGROUND_IMAGE: country_house_evening.png
BACKGROUND_EDIT: "Two-story New England dwelling with 'SOLD' sign, field and woods behind, road in front"

::SCRIPT::
- CHARACTER: Narrator
  LINE: SOUND of crickets: ree-ree-ree-ree...
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: To the left of this house: a big empty field. Behind it: the woods. Before it: a wide two-lane road. The house is a pleasant two-story New England dwelling with a shed/garage attached. In front of it is a sign which reads QUINN REALTORS 292 HAMMOND STREET, BANGOR. A big SOLD strip, like a bumper sticker, has been plastered across it diagonally.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: GROWING SOUND: the rumble of a truck. A big, big truck. It belches between the CAMERA and the house --a tanker truck with a silver body and the word ORINCO written on the side in blue letters. Its short-stack is blowing quantities of dark brown smoke. Behind it comes a Ford wagon, which slows, signals, and turns into the driveway of the house we've been looking at.
  EXPRESSION: null

::PATHS::
- CHOICE: Follow the wagon
  TARGET: rear_of_wagon
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Rear of the Wagon
MOOD: Arrival
CHARACTERS: Louis Creed, Narrator
BACKGROUND_IMAGE: rear_of_wagon.png
BACKGROUND_EDIT: "Ford wagon stopping, license plate visible, bumper sticker"

::SCRIPT::
- CHARACTER: Narrator
  LINE: As LOUIS CREED brings it to a stop we get a good look at the license plate (Illinois) and a bumper sticker (HAVE YOU HUGGED YOUR M.D. TODAY?)
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The ENGINE SOUND stops. For a moment or two we hear only the ree-ree-ree-ree of crickets. Then:
  EXPRESSION: null
- CHARACTER: Ellie Creed (VOICE)
  LINE: Is this our new house, daddy?
  EXPRESSION: null
- CHARACTER: Louis Creed (VOICE)
  LINE: This is it.
  EXPRESSION: null

::PATHS::
- CHOICE: Continue to new angle of wagon
  TARGET: wagon_new_angle
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: The Wagon (New Angle)
MOOD: Family Arrival
CHARACTERS: Louis Creed, Rachel Creed, Ellie Creed, Narrator
BACKGROUND_IMAGE: wagon_new_angle.png
BACKGROUND_EDIT: "Ford wagon doors open, family exits and stares at house"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The two front doors and one back door open. LOUIS CREED, about 32, gets out from the driver's side. RACHEL CREED, his wife, gets out from the passenger side. From the rear door comes ELLIE CREED, a girl of 6. They are staring, fascinated, at the house.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: They come together, the three of them, by the front of the wagon, still staring at the house. LOUIS is clearly nervous.
  EXPRESSION: null
- CHARACTER: Louis
  LINE: So... what do you think?
  EXPRESSION: Nervous
- CHARACTER: Rachel
  LINE: It's gorgeous!
  EXPRESSION: Happy
- CHARACTER: Ellie
  LINE: Am I really gonna have my own room?
  EXPRESSION: Excited
- CHARACTER: Louis
  LINE: Yes.
  EXPRESSION: null
- CHARACTER: Ellie
  LINE: Yaay!
  EXPRESSION: Excited
- CHARACTER: Narrator
  LINE: She looks toward the side lawn and sees a tire on a rope hanging down from the bough of a tree.
  EXPRESSION: null
- CHARACTER: Ellie (to Rachel)
  LINE: Is that a swing?
  EXPRESSION: Excited
- CHARACTER: Rachel
  LINE: Yes, but the rope might be--
  EXPRESSION: Cautious
- CHARACTER: Ellie
  LINE: Yaay!
  EXPRESSION: Excited
- CHARACTER: Narrator
  LINE: She goes running toward it. RACHEL gives LOUIS a tired smile.
  EXPRESSION: null
- CHARACTER: Louis
  LINE: Let her go. It’s cool.
  EXPRESSION: Relaxed
- CHARACTER: Rachel
  LINE: Louis, the house is beautiful.
  EXPRESSION: Happy
- CHARACTER: Narrator
  LINE: They kiss--gently at first, then more passionately. As he draws her more tightly against him, a baby--GAGE--begins to cry from the car. LOUIS and RACHEL break the clinch.
  EXPRESSION: null
- CHARACTER: Rachel
  LINE: The Master of Disaster awakes.
  EXPRESSION: Amused
- CHARACTER: Narrator
  LINE: This SOUND is joined by the unhappy yowling of a pent-up tomcat.
  EXPRESSION: null
- CHARACTER: Louis
  LINE: And Buckaroo Banzai.
  EXPRESSION: Amused
- CHARACTER: Rachel
  LINE: Come on--let’s parole 'em.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: They walk to the car, RACHEL going to one of the back seat doors, LOUIS to the rear of the wagon.
  EXPRESSION: null

::PATHS::
- CHOICE: Continue to interior of front seat
  TARGET: front_seat_rachel_gage
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: The Front Seat (with Rachel and Gage)
MOOD: Mild Chaos
CHARACTERS: Rachel Creed, Gage, Narrator
BACKGROUND_IMAGE: front_seat_rachel_gage.png
BACKGROUND_EDIT: "Interior of car, cluttered with travel debris, Gage in car seat"

::SCRIPT::
- CHARACTER: Narrator
  LINE: GAGE is sitting in his car seat, not exactly crying but certainly yelling to be let out. The seat, dash, and floorboards are littered with roadmaps, soda cans, Big Mac boxes, and similar crud. These folks have driven all the way from Chicago to Maine in this station wagon, and the wagon looks it.
  EXPRESSION: null
- CHARACTER: Rachel
  LINE: Decided to wake up and see what home looks like, huh?
  EXPRESSION: Amused
- CHARACTER: Narrator
  LINE: She begins to unbuckle the straps and harnesses. GAGE is just wearing a t-shirt and a diaper. He’s fifteen months old.
  EXPRESSION: null

::PATHS::
- CHOICE: Continue to rear of wagon
  TARGET: rear_of_wagon_louis
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: The Rear of the Wagon (with Louis)
MOOD: Arrival
CHARACTERS: Louis Creed, Narrator
BACKGROUND_IMAGE: rear_of_wagon_louis.png
BACKGROUND_EDIT: "Louis opening rear door of wagon, cat carrier inside"

::SCRIPT::
- CHARACTER: Narrator
  LINE: He opens the doorgate and lifts out a cat carrier. We see a big tomcat inside--mostly what we're aware of are shining green eyes.
  EXPRESSION: null
- CHARACTER: Ellie Creed (VOICE)
  LINE: Daddy! Mommy! I see a path!
  EXPRESSION: null

::PATHS::
- CHOICE: Follow Ellie's voice
  TARGET: ellie_tire_swing
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Ellie in the Tire Swing
MOOD: Playful, Carefree
CHARACTERS: Ellie Creed, Narrator
BACKGROUND_IMAGE: ellie_tire_swing.png
BACKGROUND_EDIT: "Ellie swinging high on a tire swing"

::SCRIPT::
- CHARACTER: Narrator
  LINE: She’s got it penduluming back and forth in long wide arcs.
  EXPRESSION: null

::PATHS::
- CHOICE: View from Ellie's POV
  TARGET: woods_ellie_pov
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: The View Up Toward the Woods (Ellie's POV)
MOOD: Expansive
CHARACTERS: Narrator
BACKGROUND_IMAGE: woods_ellie_pov.png
BACKGROUND_EDIT: "View of field, path leading into dark woods"

::SCRIPT::
- CHARACTER: Narrator
  LINE: We see the field, and a clearly marked and mown path leading up its flank and into the dark woods.
  EXPRESSION: null

::PATHS::
- CHOICE: Camera dips and pendulums
  TARGET: rachel_gage_wagon
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Rachel and Gage (Front of the Car)
MOOD: Parental Concern
CHARACTERS: Rachel Creed, Gage, Narrator
BACKGROUND_IMAGE: rachel_gage_wagon.png
BACKGROUND_EDIT: "Rachel with Gage, looking towards Ellie"

::SCRIPT::
- CHARACTER: Rachel (Irritated)
  LINE: Not so high, Ellie! You don’t know how strong that rope is.
  EXPRESSION: Irritated
- CHARACTER: Narrator
  LINE: She puts GAGE down. He totters a bit on his little legs and then stands there, looking at his sister.
  EXPRESSION: null

::PATHS::
- CHOICE: Focus on the rope and branch
  TARGET: rope_and_branch_cu
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: The Rope and the Branch (CU)
MOOD: Ominous, Decay
CHARACTERS: Narrator
BACKGROUND_IMAGE: rope_and_branch_cu.png
BACKGROUND_EDIT: "Close-up of frayed rope and worn tree branch"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The bark has rubbed off the branch--it looks like a bone peeping through decayed flesh. The rope is old, discolored. And it is fraying away as we look at it. Soon ELLIE, like Humpty Dumpty, is going to have a great fall.
  EXPRESSION: null

::PATHS::
- CHOICE: Return to Louis
  TARGET: louis_rear_wagon
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Louis (Rear of the Car)
MOOD: Casual
CHARACTERS: Louis Creed, Narrator
BACKGROUND_IMAGE: louis_rear_wagon.png
BACKGROUND_EDIT: "Louis setting down cat carrier"

::SCRIPT::
- CHARACTER: Narrator
  LINE: He's set the cat-carrier down and is straightening up.
  EXPRESSION: null
- CHARACTER: Ellie (Rapturous Voice)
  LINE: Wheee!
  EXPRESSION: null
- CHARACTER: Louis
  LINE: Ellie, you heard your m—
  EXPRESSION: Interrupted
- CHARACTER: Narrator
  LINE: His eyes widen.
  EXPRESSION: Shocked

::PATHS::
- CHOICE: Cut to Ellie
  TARGET: ellie_rope_break
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Ellie
MOOD: Shocking, Traumatic
CHARACTERS: Ellie Creed, Narrator
BACKGROUND_IMAGE: ellie_rope_break.png
BACKGROUND_EDIT: "Ellie in tire swing as rope snaps"

::SCRIPT::
- CHARACTER: Ellie
  LINE: Wh—
  EXPRESSION: Shocked
- CHARACTER: Narrator
  LINE: SOUND: A heavy twang! as the rope breaks. The tire swing--with ELLIE still inside it--goes crashing to the grass. ELLIE screams and begins to cry--a little hurt and a lot surprised.
  EXPRESSION: null
- CHARACTER: Louis
  LINE: Ellie! Are you all right?
  EXPRESSION: Panicked
- CHARACTER: Rachel
  LINE: Honey? Are you okay?
  EXPRESSION: Panicked

::PATHS::
- CHOICE: Focus on Ellie and parents
  TARGET: ellie_rachel_louis_closer
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Ellie, Rachel, Louis (A Closer Shot)
MOOD: Concern, Minor Injury
CHARACTERS: Ellie Creed, Rachel Creed, Louis Creed, Narrator
BACKGROUND_IMAGE: ellie_rachel_louis_closer.png
BACKGROUND_EDIT: "Parents tending to Ellie who has fallen from swing"

::SCRIPT::
- CHARACTER: Narrator
  LINE: ELLIE'S parents reach the tangle of tire, rope, and six-year-old girl.
  EXPRESSION: null
- CHARACTER: Ellie
  LINE: Hurrts! It hurrrrts!
  EXPRESSION: Crying
- CHARACTER: Louis
  LINE: Anyone who can scream that loud isn't ready for intensive care just yet-- looks like she just skinned her knee.
  EXPRESSION: Reassuring
- CHARACTER: Narrator
  LINE: Nevertheless, he begins to rapidly disentangle his daughter from the tire. RACHEL helps.
  EXPRESSION: null

::PATHS::
- CHOICE: Shift focus to Gage
  TARGET: gage_forgotten
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Gage
MOOD: Neglected, Curious
CHARACTERS: Gage, Narrator
BACKGROUND_IMAGE: gage_forgotten.png
BACKGROUND_EDIT: "Gage standing alone by the car, looking at cat carrier"

::SCRIPT::
- CHARACTER: Narrator
  LINE: He's standing in the driveway by the front of the car, utterly forgotten in the heat of the moment. His diaper is sagging quite a bit; the boy needs a change.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: He stares toward the scene of the accident for a bit, then loses interest. CAMERA FOLLOWS as he walks down the side of the station wagon, little bare feet slapping on the asphalt. He stops for a moment at the back, looking at the cat-
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: carrier, which LOUIS never got around to opening. CHURCH is staring hopefully out through the mesh.
  EXPRESSION: null
- CHARACTER: Gage
  LINE: Hi-Durch!
  EXPRESSION: Curious
- CHARACTER: Church
  LINE: Waow!
  EXPRESSION: Excited
- CHARACTER: Narrator
  LINE: GAGE bends down and tries to open the cat-carrier’s door. No soap.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Either he can't solve the latch or his fingers don't have the
  EXPRESSION: null

::PATHS::
- CHOICE: End of excerpt
  TARGET: end
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: THE ROAD (GAGE'S POV)
MOOD: Growing Tension
CHARACTERS: Narrator, Gage
BACKGROUND_IMAGE: road_gage_pov.png
BACKGROUND_EDIT: "Daytime, dusty road with a large tanker truck approaching"

::SCRIPT::
- CHARACTER: Narrator
  LINE: A big tanker truck--silver body, ORINCO written on the side in blue letters--blasts by.
  EXPRESSION: null

::SCENE::
LOCATION: GAGE, BY THE CAT CARRIER
MOOD: Unsettled Calm
CHARACTERS: Narrator, Gage
BACKGROUND_IMAGE: gage_cat_carrier.png
BACKGROUND_EDIT: "Daytime, dusty roadside with a cat carrier, Gage is smiling"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The windlash if the passing truck blows GAGE'S hair back from his forehead. We should be scared here--not by the truck, but by GAGE'S lack of fear. He's smiling, happy.
  EXPRESSION: null
- CHARACTER: Gage
  LINE: Druck!
  EXPRESSION: Joyful
- CHARACTER: Narrator
  LINE: He starts down the driveway toward the road.
  EXPRESSION: null

::SCENE::
LOCATION: LOUIS, RACHEL, ELLIE (AT THE SWING)
MOOD: Distress
CHARACTERS: Narrator, Ellie, Louis, Rachel
BACKGROUND_IMAGE: swing_wreckage.png
BACKGROUND_EDIT: "Daytime, near a damaged tire swing, Ellie is crying"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Ellie has been disentangled from the swing. She's sitting by the wreckage at the end of the driveway, weeping hysterically (as much from tiredness as from pain, I think) as Louis and Rachel examine her scraped knee. The wound doesn't look too serious.
  EXPRESSION: null
- CHARACTER: Louis
  LINE: Would you get the first aid kit?
  EXPRESSION: Concerned
  (TO RACHEL)
- CHARACTER: Ellie
  LINE: Not the stingy stuff! I don't want the stingy stuff, daddy!
  EXPRESSION: Panicked

::SCENE::
LOCATION: THE FRONT OF THE WAGON (RACHEL'S POV)
MOOD: Unease
CHARACTERS: Narrator, Rachel
BACKGROUND_IMAGE: wagon_front_rachel_pov.png
BACKGROUND_EDIT: "Daytime, looking from Rachel's perspective towards the front of a station wagon"

::SCRIPT::
- CHARACTER: Narrator
  LINE: No one there.
  EXPRESSION: null

::SCENE::
LOCATION: RACHEL, ELLIE, LOUIS, BY THE SWING
MOOD: Growing Panic
CHARACTERS: Narrator, Rachel, Ellie, Louis
BACKGROUND_IMAGE: swing_wreckage_panic.png
BACKGROUND_EDIT: "Daytime, near the damaged swing, Rachel is looking around frantically"

::SCRIPT::
- CHARACTER: Rachel
  LINE: Gage's gone!
  EXPRESSION: Alarmed
- CHARACTER: Louis
  LINE: Jesus, the road!
  EXPRESSION: Alarmed
- CHARACTER: Narrator
  LINE: They get up together.
  EXPRESSION: null

::SCENE::
LOCATION: GAGE, AT THE EDGE OF THE ROAD
MOOD: Imminent Danger
CHARACTERS: Narrator, Gage
BACKGROUND_IMAGE: gage_road_edge.png
BACKGROUND_EDIT: "Daytime, Gage is standing at the edge of a road with a large truck approaching"

::SCRIPT::
- CHARACTER: Narrator
  LINE: A truck is coming. A great big one.
  EXPRESSION: null

::SCENE::
LOCATION: ANGLE ON THE TRUCK, CU
MOOD: Menacing
CHARACTERS: Narrator
BACKGROUND_IMAGE: truck_grille_cu.png
BACKGROUND_EDIT: "Daytime, close-up on the grille of a large truck"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The grille looks like a tombstone that's learned how to snarl.
  EXPRESSION: null

::SCENE::
LOCATION: GAGE
MOOD: Surprise
CHARACTERS: Narrator, Gage
BACKGROUND_IMAGE: gage_grabbed.png
BACKGROUND_EDIT: "Daytime, Gage is about to step into the road when hands grab him"

::SCRIPT::
- CHARACTER: Narrator
  LINE: He takes a step into the road...and then big, gnarled hands grab him.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Gage looks rather surprised at this, but not worried--this kid is used to being picked up and treated humanely. To Gage strangers are as interesting as...well, as interesting as Orinco trucks.
  EXPRESSION: null

::SCENE::
LOCATION: GAGE AND JUD CRANDALL
MOOD: Gentle Intervention
CHARACTERS: Narrator, Gage, Jud Crandall
BACKGROUND_IMAGE: gage_jud_crandall.png
BACKGROUND_EDIT: "Daytime, Jud Crandall is holding Gage, looking kindly"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The fellow who has picked Gage up is a man of about eighty in old blue jeans, a faded Bruce Springsteen T-shirt. Over this he wears a faded khaki vest with bright silver buttons. His face is deeply wrinkled and kindly.
  EXPRESSION: null
- CHARACTER: Jud Crandall
  LINE: No you don't, my friend--not in that road.
  EXPRESSION: Firm but Kind
  (TO GAGE)
- CHARACTER: Narrator
  LINE: But he softens this with a grin. Gage grins back at him.
  EXPRESSION: null
- CHARACTER: Gage
  LINE: Drucks!
  EXPRESSION: Happy
- CHARACTER: Jud
  LINE: No shit, Sherlock.
  EXPRESSION: Amused
- CHARACTER: Narrator
  LINE: Jud carries him up the driveway to the station wagon. Here he's joined by Louis and Rachel, out of breath and really scared. Ellie brings up the rear. She's still sniffling.
  EXPRESSION: null

::SCENE::
LOCATION: THE SWING (AFTERMATH)
MOOD: Relief and Gratitude
CHARACTERS: Narrator, Rachel, Jud Crandall, Louis, Ellie, Gage
BACKGROUND_IMAGE: swing_aftermath.png
BACKGROUND_EDIT: "Daytime, station wagon, Louis and Rachel looking relieved, Jud is handing Gage to Rachel"

::SCRIPT::
- CHARACTER: Rachel
  LINE: Gage!
  EXPRESSION: Relieved
- CHARACTER: Jud
  LINE: He was headed for the road, looked like. I corralled him for you, missus.
  EXPRESSION: Helpful
  (HANDS HIM TO HER)
- CHARACTER: Rachel
  LINE: Thank you. Thank you so much.
  EXPRESSION: Grateful
- CHARACTER: Louis
  LINE: Yes--thanks. I'm Louis Creed.
  EXPRESSION: Grateful
- CHARACTER: Narrator
  LINE: He sticks out his hand and Jud shakes it. Louis takes it easy--no crushing Jaycees grip, or anything like that--the old guy looks as if he might have arthritis.
  EXPRESSION: null
- CHARACTER: Jud
  LINE: Jud Crandall. I live just across the road.
  EXPRESSION: Friendly
- CHARACTER: Rachel
  LINE: I'm Rachel. Thanks again for saving the wandering minstrel boy, here.
  EXPRESSION: Grateful
- CHARACTER: Jud
  LINE: No harm, no foul. But you want to watch out for that road. Those damn trucks go back and forth all day and most of the night.
  EXPRESSION: Warning
- CHARACTER: Narrator
  LINE: He leans over toward Ellie.
  EXPRESSION: null
- CHARACTER: Jud
  LINE: Who might you be, little Miss?
  EXPRESSION: Kindly
- CHARACTER: Ellie
  LINE: I'm Ellen Creed and I live at 642 Alden Lone, Dearburri, Michigan. At least, I used to.
  EXPRESSION: Matter-of-fact
- CHARACTER: Jud
  LINE: And now you live on Route 9 in Ludlow, and your dad's gonna be the new doctor up to the college, I hear, and I think you're going to be just as happy as a clam here, Ellen Creed.
  EXPRESSION: Knowing
- CHARACTER: Ellie
  LINE: Are clams really happy?
  EXPRESSION: Curious
- CHARACTER: Narrator
  LINE: They all laugh--even Gage.
  EXPRESSION: null
- CHARACTER: Rachel
  LINE: Excuse me, Mr. Crandall--I've got to change this kid. It's nice to meet you.
  EXPRESSION: Polite
- CHARACTER: Jud
  LINE: Same here. Come over and visit when you get the chance.
  EXPRESSION: Welcoming
- CHARACTER: Narrator
  LINE: As Rachel, carrying Gage, moves away:
  EXPRESSION: null
- CHARACTER: Ellie
  LINE: Daddy, do I really have to have the stingy stuff?
  EXPRESSION: Worried
- CHARACTER: Louis
  LINE: No-I guess not.
  EXPRESSION: Indulgent
- CHARACTER: Ellie
  LINE: Yayyy!
  EXPRESSION: Joyful
- CHARACTER: Narrator
  LINE: She goes belting off.
  EXPRESSION: null
- CHARACTER: Jud
  LINE: I guess your daughter there ain't going to die after all.
  EXPRESSION: Amused
- CHARACTER: Louis
  LINE: I guess not.
  EXPRESSION: Amused
- CHARACTER: Jud
  LINE: House has stood empty for too long. It's damn good to see people in it again.
  EXPRESSION: Content

::SCENE::
LOCATION: A MOVING VAN
MOOD: Arrival
CHARACTERS: Narrator
BACKGROUND_IMAGE: moving_van.png
BACKGROUND_EDIT: "Daytime, a moving van is lumbering into a driveway"

::SCRIPT::
- CHARACTER: Narrator
  LINE: It blinks and comes lumbering into the Creed's driveway.
  EXPRESSION: null

::SCENE::
LOCATION: LOUIS AND JUD
MOOD: Welcoming
CHARACTERS: Narrator, Louis, Jud
BACKGROUND_IMAGE: louis_jud_van.png
BACKGROUND_EDIT: "Daytime, Louis and Jud are standing near the moving van"

::SCRIPT::
- CHARACTER: Louis
  LINE: Hey--they actually found the place!
  EXPRESSION: Surprised
- CHARACTER: Jud
  LINE: Movin' in's mighty thirsty work. I usually sit out on my porch of an evening and pour a couple of beers over m’dinner. Come on over and join me, if you want.
  EXPRESSION: Inviting
- CHARACTER: Louis
  LINE: Well, maybe I--
  EXPRESSION: Hesitant

::SCENE::
LOCATION: RACHEL AND GAGE
MOOD: Exploration
CHARACTERS: Narrator, Rachel, Gage
BACKGROUND_IMAGE: rachel_gage_homestead.png
BACKGROUND_EDIT: "Daytime, Rachel is following Gage as he explores near the homestead"

::SCRIPT::
- CHARACTER: Rachel
  LINE: Louis, what's this?
  EXPRESSION: Curious
- CHARACTER: Narrator
  LINE: Gage has been changed, and Rachel is following him as he explores the nearest edges of the new homestead. They are fairly close to the wreckage of the tire swing, and here is the head of the path Ellie has already glimpsed.
  EXPRESSION: null

::SCENE::
LOCATION: LOUIS AND JUD
MOOD: Anticipation
CHARACTERS: Narrator, Louis, Jud, First Mover, Second Mover
BACKGROUND_IMAGE: louis_jud_movers.png
BACKGROUND_EDIT: "Daytime, Louis and Jud are crossing to the moving van, movers are exiting"

::SCRIPT::
- CHARACTER: Narrator
  LINE: They cross to the van. The First and Second Movers are just climbing out of the van.
  EXPRESSION: null
- CHARACTER: First Mover
  LINE: You Mr. Creed?
  EXPRESSION: Professional
- CHARACTER: Louis
  LINE: Yes. Just a second.
  EXPRESSION: Busy

::SCENE::
LOCATION: RACHEL AND GAGE, AT THE HEAD OF THE PATH
MOOD: Intrigue
CHARACTERS: Narrator, Rachel, Gage, Louis, Jud
BACKGROUND_IMAGE: rachel_gage_path.png
BACKGROUND_EDIT: "Daytime, Rachel and Gage are looking at a path disappearing into the twilight"

::SCRIPT::
- CHARACTER: Narrator
  LINE: She's holding Gage on her hip now, and both of them are looking at that strange (and oddly enticing) path which disappears into the deepening twilight. Louis and Jud join them.
  EXPRESSION: null
- CHARACTER: Louis
  LINE: The movers--
  EXPRESSION: Distracted
- CHARACTER: Rachel
  LINE: Yes--I know. This path, Louis? Where does it go?
  EXPRESSION: Curious
- CHARACTER: Louis
  LINE: I don't have the slightest idea. When I saw the house, this field was under four feet of snow.
  EXPRESSION: Uncertain
- CHARACTER: Rachel
  LINE: I bet Mr. Crandall knows!
  EXPRESSION: Hopeful
- CHARACTER: Narrator
  LINE: Jud nods. He smiles, too, but underneath the smile we sense that he is serious.
  EXPRESSION: null
- CHARACTER: Jud
  LINE: Oh, ayuh! I know. It’s a good story, and a good walk, too. I’ll take you up there sometime, and tell you the story, too-- after you get settled in.
  EXPRESSION: Mysterious
- CHARACTER: Narrator
  LINE: He smiles at them and they smile back--it is a look of understanding and real liking, in spite of the age difference between the Creeds and Jud.
  EXPRESSION: null

::SCENE::
LOCATION: THE CREED HOUSE - NIGHT
MOOD: Peaceful Settling
CHARACTERS: Narrator
BACKGROUND_IMAGE: creed_house_night.png
BACKGROUND_EDIT: "Nighttime, exterior of the Creed house, a few lights are on, crickets chirping"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Sound: Crickets. Ree--ree--ree-ree...
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: There's one light upstairs, one downstairs. Perhaps we see the path, glimmering away into the field? Either by virtue of it being mown, or by virtue of some gentle optical trick? Maybe.
  EXPRESSION: null

::SCENE::
LOCATION: THE LIVING ROOM - NIGHT
MOOD: Exhaustion
CHARACTERS: Narrator, Louis, Rachel
BACKGROUND_IMAGE: living_room_night.png
BACKGROUND_EDIT: "Nighttime, interior of a bare living room filled with moving boxes, Louis is sitting on a box, smoking"

::SCRIPT::
- CHARACTER: Narrator
  LINE: There's a light on in the kitchen, but it just casts a dim glow in here. The room has a fireplace and a lovely wooden floor. It's going to be nice, but now it's just a big bare box with movers' cartons stacked all over the place.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Louis is drinking a can of Pepsi, and he looks pretty damned tired--anyone who's ever moved house and can remember the first night in the new place will understand.
  EXPRESSION: Tired
- CHARACTER: Narrator
  LINE: He finishes the last of the Pepsi and surveys the living room. He sits on one of the bigger boxes, takes cigarettes from his pocket, and lights one. He drops the spent match in the empty can, and taps into the can during the scene.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Sound: Feet coming down the stairs. The door on the far side of the room opens and Rachel comes in, wearing a nightgown.
  EXPRESSION: null
- CHARACTER: Rachel
  LINE: Kids are asleep, doc.
  EXPRESSION: Tired
  (CROSSING TO LOUIS)
- CHARACTER: Louis
  LINE: Great.
  EXPRESSION: Relieved
- CHARACTER: Narrator
  LINE: He hugs her. She hugs him back warmly--for a moment they are just two good people in all the big darkness of their new house.
  EXPRESSION: null
- CHARACTER: Rachel
  LINE: You're not really going over to have a beer with that old guy, are you?
  EXPRESSION: Skeptical
- CHARACTER: Louis
  LINE: Well, I’ve got a million questions about the area, and—
  EXPRESSION: Hesitant
- CHARACTER: Rachel
  LINE: —and you'll end up doing a free consultation on his arthritis or urinary problems and—
  EXPRESSION: Teasing
- CHARACTER: Louis
  LINE: Did you see his shirt?
  EXPRESSION: Curious
- CHARACTER: Rachel
  LINE: Sure. Bruce Springsteen.
  EXPRESSION: Amused
- CHARACTER: Louis
  LINE: I really do have a million questions about the area...but the thing I'm really curious about is how come this octogenarian Yankee is decorating the slumped remains of his pecs with the Boss.
  EXPRESSION: Amused
- CHARACTER: Narrator
  LINE: She laughs.
  EXPRESSION: null

::SCENE::
LOCATION: THE PATH OF THE CRANDALL HOUSE - NIGHT
MOOD: Trepidation
CHARACTERS: Narrator, Louis, Dud
BACKGROUND_IMAGE: crandall_path_night.png
BACKGROUND_EDIT: "Nighttime, Louis is hesitantly walking up a crazy-paved path"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Pervasive Sound of the crickets as Louis comes rather hesitantly up the crazy-paved path from the road's edge.
  EXPRESSION: null
- CHARACTER: Dud
  LINE: That you, doc?
  EXPRESSION: Expectant
  (VOICE)

::SCENE::
LOCATION: THE SCREENED-IN PORCH OF THE CRANDALL HOUSE
MOOD: Relaxed Conversation
CHARACTERS: Narrator, Dud
BACKGROUND_IMAGE: crandall_porch_night.png
BACKGROUND_EDIT: "Nighttime, dim glow of a cigarette, Dud wearing earphones, rocking"

::SCRIPT::
- CHARACTER: Narrator
  LINE: We hear the squeak of a rocker; we see the dim red fitful glow of Dud's Pall Mall. We see by its glow that he is wearing Walkman earphones.
  EXPRESSION: null

::SCENE::
LOCATION: LOUIS
MOOD: Responding
CHARACTERS: Narrator, Louis
BACKGROUND_IMAGE: louis_approaching_porch.png
BACKGROUND_EDIT: "Nighttime, Louis is standing near the porch of the Crandall house"

::SCRIPT::
- CHARACTER: Louis
  LINE: It's me.
  EXPRESSION: Calling out

::SCENE::
LOCATION: THE PORCH, WITH DUD
MOOD: Welcoming
CHARACTERS: Narrator, Dud, Louis
BACKGROUND_IMAGE: dud_porch_louis_arriving.png
BACKGROUND_EDIT: "Nighttime, Dud is on his porch, taking off earphones, Louis is approaching"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The Walkman is in his lap. He switches it off and puts the headphones casually around his neck, like a kid.
  EXPRESSION: null
- CHARACTER: Dud
  LINE: Well, come on up and have a beer.
  EXPRESSION: Welcoming

::SCENE::
LOCATION: THE PORCH, A SLIGHTLY WIDER SHOT
MOOD: Camaraderie
CHARACTERS: Narrator, Dud, Louis
BACKGROUND_IMAGE: porch_wider_shot_beer.png
BACKGROUND_EDIT: "Nighttime, Dud is offering Louis a beer on the porch"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Louis comes on up. Dud has got a pail of ice beside his chair with some cans of beer in it. He opens one and hands it to Louis.
  EXPRESSION: null
- CHARACTER: Dud
  LINE: You need a glass?
  EXPRESSION: Polite
- CHARACTER: Louis
  LINE: Not at all.
  EXPRESSION: Casual
- CHARACTER: Dud
  LINE: Good for you.
  EXPRESSION: Agreeable
- CHARACTER: Narrator
  LINE: Louis drinks half the can at a draught.
  EXPRESSION: null
- CHARACTER: Louis
  LINE: God, that's fine.
  EXPRESSION: Satisfied
- CHARACTER: Dud
  LINE: Ain't it just? The man who invented beer, Louis, that man was having a prime day for himself.
  EXPRESSION: Appreciative
- CHARACTER: Louis
  LINE: What were you listening to?
  EXPRESSION: Curious
- CHARACTER: Dud
  LINE: Allman Brothers.
  EXPRESSION: Casual
- CHARACTER: Louis
  LINE: What?
  EXPRESSION: Surprised
- CHARACTER: Dud
  LINE: The Eat A Peach album. God, they were good before drugs and bad luck caught up with them. Listen to this, Louis.
  EXPRESSION: Nostalgic
- CHARACTER: Narrator
  LINE: He passes the headphones over. Louis puts them on. Dud presses the Walkman's PLAY button.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Sound: Ramblin' Man blasts us out of our seats.
  EXPRESSION: null
- CHARACTER: Louis
  LINE: (WINCES)
  EXPRESSION: Uncomfortable
- CHARACTER: Narrator
  LINE: Louis winces and rakes the spidery earphones off his head.
  EXPRESSION: null

::SCENE::
LOCATION: The Porch
MOOD: Companionable
CHARACTERS: Narrator, Dud, Louis
BACKGROUND_IMAGE: porch.png
BACKGROUND_EDIT: "Daytime, porch with screen door"

::SCRIPT::
- CHARACTER: Dud
  LINE: I’m sorry. Wait.
  EXPRESSION: null
- CHARACTER: Dud
  LINE: Try that.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Louis puts the earphones back on and listens for a few moments. It’s the instrumental break. Gregg and Duane Allman dueling hot Fenders. Louis takes the earphones off.
  EXPRESSION: null
- CHARACTER: Louis
  LINE: Nice.
  EXPRESSION: null
- CHARACTER: Dud
  LINE: I like rock and roll. No... I guess that's too mild. I love it. Since my ears started to die out on me, it's the only music I can really hear. And since my wife died... I dunno, sometimes a little rock and roll fills up night. Not always, but sometimes.
  EXPRESSION: Reflective
- CHARACTER: Dud
  LINE: One more time--welcome to Ludlow. Hope your time here will be a happy one.
  EXPRESSION: Warm
- CHARACTER: Louis
  LINE: Thank you, Mr. Crandall.
  EXPRESSION: Grateful
- CHARACTER: Narrator
  LINE: He drinks again--they both do. There’s a moment of companionable silence here, broken by the sound of a big truck. They look
  EXPRESSION: null

::PATHS::
- CHOICE: "Observe the truck"
  TARGET: road_through_screen
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: The Road (through the porch screen)
MOOD: Transient
CHARACTERS: Narrator
BACKGROUND_IMAGE: road_through_screen.png
BACKGROUND_EDIT: "View of road through screen, daytime"

::SCRIPT::
- CHARACTER: Narrator
  LINE: One of those big tanker trucks goes rumbling by--now there are little amber running lights on top of it. It's going fast, too--sweeps by in a blast of air.
  EXPRESSION: null

::PATHS::
- CHOICE: "Return to the porch"
  TARGET: porch_with_louis_and_dud
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: The Porch, with Louis and Dud
MOOD: Reflective
CHARACTERS: Narrator, Louis, Dud
BACKGROUND_IMAGE: porch_with_louis_and_dud.png
BACKGROUND_EDIT: "Daytime, porch with screen door"

::SCRIPT::
- CHARACTER: Louis
  LINE: Desus!
  EXPRESSION: Wincing
- CHARACTER: Dud
  LINE: That's one mean road, all right--you remember that path your wife commented on?
  EXPRESSION: null
- CHARACTER: Louis
  LINE: The one that goes into the woods--sure.
  EXPRESSION: null
- CHARACTER: Dud
  LINE: That road--and those Orinco trucks--are the two main reasons it's there.
  EXPRESSION: null
- CHARACTER: Louis
  LINE: What's at the end of it?
  EXPRESSION: Curious
- CHARACTER: Dud
  LINE: Another day--after you get settled in a bit. Meantime, doc—
  EXPRESSION: Smiling
- CHARACTER: Dud
  LINE: Here's to your bones.
  EXPRESSION: Toasting
- CHARACTER: Louis
  LINE: And yours.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: They drink.
  EXPRESSION: null

::PATHS::
- CHOICE: "Walk up the driveway"
  TARGET: route_9_night
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Route 9 - Night
MOOD: Hopeful
CHARACTERS: Narrator, Louis
BACKGROUND_IMAGE: route_9_night.png
BACKGROUND_EDIT: "Nighttime, driveway leading to a house"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Louis crosses from the Crandall side to his own, and the camera follows as he walks slowly up the driveway and past the wagon. He pauses for a moment, looking thoughtfully--hopefully--at his new house. Then something--the cry of an owl, perhaps--draws his attention the other way...toward the path.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: He walks to its head and stands looking out at it--it glimmers in a wide cut swath that's a bit ghostly in the dark.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: A shape suddenly lurches out of the high grass at him, and Louis recoils with a startled, muffled cry.
  EXPRESSION: null

::PATHS::
- CHOICE: "Investigate the shape"
  TARGET: church_cat
  STATE_CHANGE: surprise = +1
  CONDITION: null

::SCENE::
LOCATION: Church
MOOD: Startled
CHARACTERS: Narrator, Louis, Church (cat)
BACKGROUND_IMAGE: church_cat.png
BACKGROUND_EDIT: "Nighttime, dark grass, cat's eyes glowing"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The cat, sure; who--or what--else? We see his big green eyes in the dark as he cries his strange feline hello: Waow!
  EXPRESSION: null

::PATHS::
- CHOICE: "Approach the cat"
  TARGET: louis_and_church_at_path
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Louis and Church, at the Head of the Path
MOOD: Relief
CHARACTERS: Narrator, Louis, Church (cat)
BACKGROUND_IMAGE: louis_and_church_at_path.png
BACKGROUND_EDIT: "Nighttime, head of a path"

::SCRIPT::
- CHARACTER: Louis
  LINE: Church! God, you scared the life out of me!
  EXPRESSION: Relieved
- CHARACTER: Church (cat)
  LINE: Waow!
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Louis bends and picks up the cat. As he does, that truck sound comes again and he looks toward:
  EXPRESSION: null

::PATHS::
- CHOICE: "Look toward the sound"
  TARGET: road_louis_pov
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: The Road, Louis's POV
MOOD: Acknowledging
CHARACTERS: Narrator
BACKGROUND_IMAGE: road_louis_pov.png
BACKGROUND_EDIT: "Nighttime, view of the road"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Another Orinco tanker drones by, fast.
  EXPRESSION: null

::PATHS::
- CHOICE: "Return to Louis and Church"
  TARGET: louis_and_church
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Louis and Church
MOOD: Preparatory
CHARACTERS: Narrator, Louis, Church (cat)
BACKGROUND_IMAGE: louis_and_church.png
BACKGROUND_EDIT: "Nighttime, Louis holding Church"

::SCRIPT::
- CHARACTER: Louis
  LINE: I know one thing that will keep you home, good buddy.
  EXPRESSION: Determined
- CHARACTER: Narrator
  LINE: He starts toward the house. BLACK. And in that blackness, we see a second title card: THE DEAD SPEAK.
  EXPRESSION: null

::PATHS::
- CHOICE: "Fade to black"
  TARGET: kitchen_blackboard_cu
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: A Kitchen Blackboard, CU - Day
MOOD: Informative
CHARACTERS: Narrator
BACKGROUND_IMAGE: kitchen_blackboard_cu.png
BACKGROUND_EDIT: "Close-up of a blackboard with writing"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Written on it is: MONDAY 1.) CHURCH SPAYED 10 A.M. QUENTIN DOLANDER, D.V.M. And below, in even bigger letters: 2.) ELLIE'S FIRST DAY OF SCHOOL!!
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The camera pans left, showing us the kitchen. There are still a few cardboard cartons around, but the place is getting in shape.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: We look out the window and see the Creeds, led by Dud Crandall, climbing the path toward the woods. Louis has Gage in a Gerrypak.
  EXPRESSION: null

::PATHS::
- CHOICE: "Follow them to the woods"
  TARGET: top_of_hill_creeds_and_dud
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: At the Top of the Hill, with Creeds and Dud
MOOD: Awe-Inspiring
CHARACTERS: Narrator, Dud, Louis, Rachel, Ellie, Gage (implied)
BACKGROUND_IMAGE: top_of_hill_creeds_and_dud.png
BACKGROUND_EDIT: "Daytime, edge of woods, view of valley"

::SCRIPT::
- CHARACTER: Narrator
  LINE: They are also at the edge of the woods. Dud stops and lets them catch up.
  EXPRESSION: null
- CHARACTER: Dud
  LINE: Take a look behind you.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: They turn around, and their faces express their wonder.
  EXPRESSION: null
- CHARACTER: Louis
  LINE: My God!
  EXPRESSION: Amazed
- CHARACTER: Rachel
  LINE: It's beautiful!
  EXPRESSION: Amazed

::PATHS::
- CHOICE: "Admire the view"
  TARGET: the_view
  STATE_CHANGE: wonder = +2
  CONDITION: null

::SCENE::
LOCATION: The View
MOOD: Majestic
CHARACTERS: Narrator
BACKGROUND_IMAGE: the_view.png
BACKGROUND_EDIT: "Daytime, panoramic view of river valley and sky"

::SCRIPT::
- CHARACTER: Narrator
  LINE: It is indeed beautiful. The Creed house is in the f.g., Route 9 just behind it (with one of the ever-present Orinco trucks droning along), but behind that is the great sweep of the Penobscot river valley, dozing under a fall sky of clear blue.
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue towards the woods"
  TARGET: top_of_hill_dud_and_creeds
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: At the Top of the Hill, with Dud and the Creeds
MOOD: Anticipatory
CHARACTERS: Narrator, Dud, Louis, Ellie
BACKGROUND_IMAGE: top_of_hill_dud_and_creeds.png
BACKGROUND_EDIT: "Daytime, edge of woods, starting on path"

::SCRIPT::
- CHARACTER: Dud
  LINE: You folks ready to go on?
  EXPRESSION:null
- CHARACTER: Louis
  LINE: Sure.
  EXPRESSION: null
- CHARACTER: Ellie
  LINE: But where are we going, Mr. Crandall?
  EXPRESSION: Curious
- CHARACTER: Dud
  LINE: You'll see soon enough, hon.
  EXPRESSION: Reassuring
- CHARACTER: Narrator
  LINE: They go into the woods, still following the path.
  EXPRESSION: null

::PATHS::
- CHOICE: "Enter the woods"
  TARGET: forest_day
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Forest - Day
MOOD: Ancient
CHARACTERS: Narrator, Jud, Louis, Ellie, Rachel (implied)
BACKGROUND_IMAGE: forest_day.png
BACKGROUND_EDIT: "Daytime, old forest with large trees and sun shafts"

::SCRIPT::
- CHARACTER: Narrator
  LINE: These are old woods indeed--huge trunks with dusty sunlight shafting through them. It looks as though man has never made his mark here.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The camera pans slowly down to them, on the path. Here it is carpeted with pine needles, but it is just as clearly marked.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Jud stops. Louis looks glad of the rest; he’s sweating and there are wide dark patches under his arms where the Gerrypak’s straps are.
  EXPRESSION: null
- CHARACTER: Louis
  LINE: Who owns the woods up ahead? Paper companies?
  EXPRESSION: Curious
- CHARACTER: Jud
  LINE: Nope. The Micmac Indians. What's up ahead is all that's left of their tribal lands.
  EXPRESSION: null
- CHARACTER: Ellie
  LINE: Micmac, Ricmac, Kickmac, Sickmac.
  EXPRESSION: Giggling
- CHARACTER: Jud
  LINE: Ayuh, it's a funny word, ain't it? You tired of totin' that yowwen yet, doc?
  EXPRESSION: Smiling
- CHARACTER: Louis
  LINE: Not yet...how much further is it?
  EXPRESSION: Inquisitive
- CHARACTER: Jud
  LINE: Aw, you'll be okay. Less than a mile.
  EXPRESSION: Encouraging
- CHARACTER: Narrator
  LINE: He starts off again, fresh as a daisy. Ellie scampers after him.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Louis rolls his eyes at his wife and Rachel rolls hers back. Then they press on.
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue on the path"
  TARGET: arch_reading_pet_sematary
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: The Arch Reading Pet Sematary
MOOD: Foreboding
CHARACTERS: Narrator
BACKGROUND_IMAGE: arch_reading_pet_sematary.png
BACKGROUND_EDIT: "Daytime, an archway with writing"

::SCRIPT::
- CHARACTER: Narrator
  LINE: null
  EXPRESSION: null

::PATHS::
- CHOICE: "Approach the arch"
  TARGET: jud_and_creeds_on_path
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Jud and the Creeds, on the Path
MOOD: Unsettling
CHARACTERS: Narrator, Jud, Ellie, Rachel
BACKGROUND_IMAGE: jud_and_creeds_on_path.png
BACKGROUND_EDIT: "Daytime, path leading to an archway"

::SCRIPT::
- CHARACTER: Jud
  LINE: This is the place, honey.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Ellie is of course second. She tries to read the words on the arch but can’t. She whips around to look at her mother.
  EXPRESSION: null
- CHARACTER: Ellie
  LINE: What's it say, mommy?
  EXPRESSION: Curious
- CHARACTER: Narrator
  LINE: A strange expression has come over Rachel's face--she doesn't like this. Not a bit.
  EXPRESSION: Uneasy
- CHARACTER: Rachel
  LINE: It says Pet Cemetery, hon. It's misspelled, but...that’s what it says.
  EXPRESSION: Uneasy
- CHARACTER: Narrator
  LINE: She runs for the arch. Rachel starts; looks more uneasy than ever.
  EXPRESSION: null
- CHARACTER: Rachel
  LINE: Ellen--!
  EXPRESSION: Alarmed

::PATHS::
- CHOICE: "Follow Ellie"
  TARGET: ellie_under_arch
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Ellie
MOOD: Eager
CHARACTERS: Narrator, Ellie
BACKGROUND_IMAGE: ellie_under_arch.png
BACKGROUND_EDIT: "Daytime, Ellie about to enter an archway"

::SCRIPT::
- CHARACTER: Narrator
  LINE: She's almost under the arch. She looks back, questioning.
  EXPRESSION: null

::PATHS::
- CHOICE: "Enter the Pet Sematary"
  TARGET: rachel_louis_jud
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Rachel, Louis, Jud
MOOD: Concerned
CHARACTERS: Narrator, Rachel, Louis, Jud
BACKGROUND_IMAGE: rachel_louis_jud.png
BACKGROUND_EDIT: "Daytime, standing at the entrance of the Pet Sematary"

::SCRIPT::
- CHARACTER: Rachel
  LINE: Be careful.
  EXPRESSION: Wary
- CHARACTER: Narrator
  LINE: They stop and look in.
  EXPRESSION: null
- CHARACTER: Jud
  LINE: I told you it was a bad road, Louis--it's killed a lot of pets and made a lot of kids unhappy. But at least something good come of it. This place.
  EXPRESSION: Philosophical
- CHARACTER: Ellie
  LINE: Mom! Dad! Y’oughtta see it!
  EXPRESSION: Excited
- CHARACTER: Narrator
  LINE: They are walking slowly toward that rude archway. Louis is extremely interested in all this, but it’s becoming clearer and clearer that Rachel is troubled. They stop and look in.
  EXPRESSION: null
- CHARACTER: Rachel
  LINE: How can you call it a good thing? A graveyard for pets killed in the road! Built and maintained by broken-hearted children!
  EXPRESSION: Upset
- CHARACTER: Jud
  LINE: Well, but Missus Creed! It ain't quite that way, dear!
  EXPRESSION: Pacifying
- CHARACTER: Louis
  LINE: I think it's rather extraordinary.
  EXPRESSION: Intrigued
- CHARACTER: Rachel
  LINE: Extraordinarily morbid, maybe.
  EXPRESSION: Displeased
- CHARACTER: Narrator
  LINE: She's growing more and more upset. Jud looks at her curiously.
  EXPRESSION: null
- CHARACTER: Jud
  LINE: Well...they have to learn about death somehow, now don't they, Missus Creed? The little ones?
  EXPRESSION: Questioning
- CHARACTER: Rachel
  LINE: Why?
  EXPRESSION: Coldly
- CHARACTER: Jud
  LINE: Well...well, because--
  EXPRESSION: Hesitant
- CHARACTER: Ellie
  LINE: Mommy! Daddy! Look at me!
  EXPRESSION: Excited
  EXPRESSION: Excited

::PATHS::
- CHOICE: "Observe Ellie"
  TARGET: ellie_on_deadfall
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Ellie, on the Deadfall
MOOD: Adventurous
CHARACTERS: Narrator, Ellie
BACKGROUND_IMAGE: ellie_on_deadfall.png
BACKGROUND_EDIT: "Daytime, Ellie climbing on a fallen tree"

::SCRIPT::
- CHARACTER: Narrator
  LINE: She has begun to climb it, and this looks like an extremely dangerous proposition. Ellie, however, is having the time of her life. A branch breaks under one of her feet and she switches nimbly to the next one up.
  EXPRESSION: null

::PATHS::
- CHOICE: "Watch Ellie's actions"
  TARGET: grownups_at_arch
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: The Grownups, at the Arch
MOOD: Alarmed
CHARACTERS: Narrator, Jud, Ellie
BACKGROUND_IMAGE: grownups_at_arch.png
BACKGROUND_EDIT: "Daytime, Jud hurrying towards Ellie"

::SCRIPT::
- CHARACTER: Jud
  LINE: No, honey! You don't want to go climbing on that! Come on down!
  EXPRESSION: Alarmed
- CHARACTER: Narrator
  LINE: He hurries in.
  EXPRESSION: null

::PATHS::
- CHOICE: "Follow Jud"
  TARGET: ellie_on_deadfall_again
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Ellie, on the Deadfall
MOOD: Confident
CHARACTERS: Narrator, Ellie, Jud
BACKGROUND_IMAGE: ellie_on_deadfall_again.png
BACKGROUND_EDIT: "Daytime, Ellie on a fallen tree, talking to Jud"

::SCRIPT::
- CHARACTER: Ellie
  LINE: It's okay, Mr. Crandall--
  EXPRESSION: Confident

::PATHS::
- CHOICE: "Observe Ellie's foot"
  TARGET: ellie_foot_cu
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Ellie's Foot, CU
MOOD: Dangerous
CHARACTERS: Narrator
BACKGROUND_IMAGE: ellie_foot_cu.png
BACKGROUND_EDIT: "Close-up of a foot on a breaking branch"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The branch she's on breaks with a dry CRRRACK. Her foot drops down suddenly.
  EXPRESSION: null

::PATHS::
- CHOICE: "Witness the catch"
  TARGET: ellie_and_dud
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Ellie and Dud
MOOD: Secure
CHARACTERS: Narrator, Ellie, Dud, Louis
BACKGROUND_IMAGE: ellie_and_dud.png
BACKGROUND_EDIT: "Daytime, Dud catching Ellie, Louis joining them"

::SCRIPT::
- CHARACTER: Narrator
  LINE: She totters backward, pinwheeling her arms, and Dud catches her as she falls. Not much of a catch because she wasn't too far up.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Louis joins Dud and Ellie. Gage jounces along on his back.
  EXPRESSION: null
- CHARACTER: Louis
  LINE: Have you got a death-wish, Ellen?
  EXPRESSION: Concerned
- CHARACTER: Ellie
  LINE: Well, I thought it was safe--
  EXPRESSION: Defensive
- CHARACTER: Dud
  LINE: Best never to go climbing on old blowdowns like this, Ellie--sometimes they bite.
  EXPRESSION: Warning
- CHARACTER: Ellie
  LINE: Bite?
  EXPRESSION: Curious
- CHARACTER: Dud
  LINE: Ayuh.
  EXPRESSION: Affirmative

::PATHS::
- CHOICE: "Observe Rachel"
  TARGET: rachel_standing_at_arch
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Rachel, Standing at the Arch
MOOD: Hesitant
CHARACTERS: Narrator, Rachel
BACKGROUND_IMAGE: rachel_standing_at_arch.png
BACKGROUND_EDIT: "Daytime, Rachel at the arch of the Pet Sematary"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Her discomfort makes one thing very clear--she doesn't want to come in.
  EXPRESSION: null
- CHARACTER: Rachel
  LINE: Is she all right, Louis?
  EXPRESSION: Calling

::PATHS::
- CHOICE: "Call back to Rachel"
  TARGET: louis_dud_ellie
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Louis, Dud, Ellie
MOOD: Inviting
CHARACTERS: Narrator, Louis, Ellie
BACKGROUND_IMAGE: louis_dud_ellie.png
BACKGROUND_EDIT: "Daytime, near the fallen tree"

::SCRIPT::
- CHARACTER: Louis
  LINE: Fine! Come and see!
  EXPRESSION: Calling

::PATHS::
- CHOICE: "Rachel's response"
  TARGET: rachel_standing_at_arch_again
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Rachel, Standing at the Arch
MOOD: Withdrawn
CHARACTERS: Narrator, Rachel
BACKGROUND_IMAGE: rachel_standing_at_arch_again.png
BACKGROUND_EDIT: "Daytime, Rachel sitting on the path"

::SCRIPT::
- CHARACTER: Rachel
  LINE: I think I'll sit this one out, doc.
  EXPRESSION: Declining
- CHARACTER: Narrator
  LINE: Rachel has retreated a bit. She sits on the pine needle carpet of the path, opens her purse, and draws out cigarettes.
  EXPRESSION: null

::PATHS::
- CHOICE: "Observe Louis and Dud"
  TARGET: louis_and_dud
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Louis and Dud
MOOD: Pensive
CHARACTERS: Narrator, Dud, Louis, Ellie (voice)
BACKGROUND_IMAGE: louis_and_dud.png
BACKGROUND_EDIT: "Daytime, Louis and Dud talking"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Dud looks at Louis as if to say "What's all this about?" Louis looks away.
  EXPRESSION: null
- CHARACTER: Ellie
  LINE: I want to look around, daddy-- may I?
  EXPRESSION: Voice
- CHARACTER: Louis
  LINE: For a little while.
  EXPRESSION: Granting

::PATHS::
- CHOICE: "Ellie explores"
  TARGET: ellie_explores
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: EXT. ELLIE
MOOD: Cheerful
CHARACTERS: Ellie
BACKGROUND_IMAGE: tombstones.png
BACKGROUND_EDIT: "Child running between tombstones, daytime"

::SCRIPT::
- CHARACTER: Ellie
  LINE: Dad! Daddy! Look! A goldfishie!
  EXPRESSION: Excited

::PATHS::
- CHOICE: "Continue exploring"
  TARGET: EXT. ELLIE_NEXT
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: EXT. ELLIE
MOOD: Observing
CHARACTERS: Ellie
BACKGROUND_IMAGE: tombstones.png
BACKGROUND_EDIT: "Child looking at tombstones (Biffer, Smucky)"

::SCRIPT::
- CHARACTER: Ellie
  LINE: She runs from one tombstone to the next, cheerful as maybe only a kid could be in such a place. She looks at BIFFER’S tombstone; at SMUCKY'S.
  EXPRESSION: Cheerful

::PATHS::
- CHOICE: "Return to adults"
  TARGET: EXT. LOUIS AND DUD
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: EXT. LOUIS AND DUD
MOOD: Contemplative
CHARACTERS: Louis, Dud, Ellie
BACKGROUND_IMAGE: cemetery_path.png
BACKGROUND_EDIT: "Two adults walking towards a child in a cemetery"

::SCRIPT::
- CHARACTER: Louis
  LINE: I can hardly read these.
  EXPRESSION: Faint
- CHARACTER: Dud
  LINE: Ayuh--they get older as you go toward the middle.
  EXPRESSION: Matter-of-fact
- CHARACTER: Dud
  LINE: Pete LaVasseur's dog is buried there...
  EXPRESSION: Indicating
- CHARACTER: Dud
  LINE: ...the Stoppard boys’ racing pigeon,
  EXPRESSION: Indicating
- CHARACTER: Dud
  LINE: LidL MibbUb Cowley'b <\_dl got...and I think that's the cat himself right there, although it's been so many years I can't tell for sure.
  EXPRESSION: Indicating
- CHARACTER: Dud
  LINE: Missy Ellen! Come over here just a minute!
  EXPRESSION: Calling

::PATHS::
- CHOICE: "Ellie approaches"
  TARGET: EXT. ELLEN
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: EXT. ELLEN
MOOD: Energetic
CHARACTERS: Ellie, Louis, Dud
BACKGROUND_IMAGE: cemetery_center.png
BACKGROUND_EDIT: "Child running towards adults in the center of the cemetery"

::SCRIPT::
- CHARACTER: Ellie
  LINE: She runs amid the tombstones--they have worked their way near to the center and there are quite a few of them--and joins the adults.
  EXPRESSION: Energetic
- CHARACTER: Dud
  LINE: I see you're quite a reader for such a little girl. Can you read that?
  EXPRESSION: Curious
- CHARACTER: Ellie
  LINE: He points again, and Ellen goes over for a look-see.
  EXPRESSION: null

::PATHS::
- CHOICE: "Examine the grave marker"
  TARGET: EXT. ELLEN, AT THE GRAVE MARKER
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: EXT. ELLEN, AT THE GRAVE MARKER
MOOD: Puzzled
CHARACTERS: Ellen
BACKGROUND_IMAGE: small_marker.png
BACKGROUND_EDIT: "Child looking closely at a small, slanted slate grave marker"

::SCRIPT::
- CHARACTER: Ellen
  LINE: "Spot a good fellow we love you boy."
  EXPRESSION: Reading laboriously
- CHARACTER: Ellen
  LINE: "Owned by Dudson...Dudson..." Gee, I can't read the rest.
  EXPRESSION: Puzzled

::PATHS::
- CHOICE: "Return to adults"
  TARGET: EXT. DUD AND LOUIS
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: EXT. DUD AND LOUIS
MOOD: Informative
CHARACTERS: Dud, Louis, Ellie
BACKGROUND_IMAGE: cemetery_path.png
BACKGROUND_EDIT: "Adults and child standing together, discussing a grave marker"

::SCRIPT::
- CHARACTER: Dud
  LINE: Last name's Crandall, little missy.
  EXPRESSION: Explaining
- CHARACTER: Louis
  LINE: Looks at him sharply as ELLIE rejoins them.
  EXPRESSION: Sharp
- CHARACTER: Dud
  LINE: That's where I buried my dog Spot when he died of old age in 19 and 14. Dug it good and deep. By the time I finished, I had blisters all over my hands and a hell of a crick in my back. Soil's stony up here.
  EXPRESSION: Reminiscing
- CHARACTER: Ellie
  LINE: Looks awed.
  EXPRESSION: Awed
- CHARACTER: Louis
  LINE: Looks a little awed, too.
  EXPRESSION: Awed
- CHARACTER: Dud
  LINE: Do you know what this place is, Ellie? Oh, I know you know it's a boneyard, but a bone ain’t nothing and even a whole pile of 'em don't amount to much. Do you know what a graveyard really lb?
  EXPRESSION: Questioning
- CHARACTER: Ellie
  LINE: Well...I guess not.
  EXPRESSION: Uncertain
- CHARACTER: Dud
  LINE: It's a place where the dead speak, Missy.
  EXPRESSION: Profound
- CHARACTER: Dud
  LINE: No--not right out loud. Their stones speak...or their markers. Even if the marker ain't nothing but a tin can someone wrote on with a Magic Marker, it speaks. Ain't that so, Louis?
  EXPRESSION: Reassuring
- CHARACTER: Louis
  LINE: I think it is so, Ellie.
  EXPRESSION: Agreeing
- CHARACTER: Ellie
  LINE: What if you can't read what’s written on there anymore?
  EXPRESSION: Concerned
- CHARACTER: Dud
  LINE: Well, it still says some animal got laid down here after, don't it?
  EXPRESSION: Practical
- CHARACTER: Ellie
  LINE: Yes--
  EXPRESSION: Affirmative
- CHARACTER: Louis
  LINE: And that someone cared enough about that animal to mark the spot.
  EXPRESSION: Thoughtful
- CHARACTER: Ellie
  LINE: To remember.
  EXPRESSION: Understanding
- CHARACTER: Dud
  LINE: Yes. To remember. This ain't a scary place, Ellie. It's a place of rest and speaking. Can you remember that?
  EXPRESSION: Gentle
- CHARACTER: Ellie
  LINE: Yes, sir.
  EXPRESSION: Awed

::PATHS::
- CHOICE: "Walk back towards the arch"
  TARGET: EXT. RACHEL, OUTSIDE THE ARCH
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: EXT. RACHEL, OUTSIDE THE ARCH
MOOD: Impatient
CHARACTERS: Rachel, Louis, Ellie, Dud
BACKGROUND_IMAGE: cemetery_arch.png
BACKGROUND_EDIT: "Woman standing impatiently outside a cemetery arch, calling out"

::SCRIPT::
- CHARACTER: Rachel
  LINE: Louis, can we go? I’m tired!
  EXPRESSION: Impatient

::PATHS::
- CHOICE: "Ellie calls out"
  TARGET: EXT. LOUIS, ELLIE, IUD
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: EXT. LOUIS, ELLIE, IUD
MOOD: Excited
CHARACTERS: Ellie, Rachel, Louis, Dud
BACKGROUND_IMAGE: cemetery_arch.png
BACKGROUND_EDIT: "Child excitedly talking to an adult, another adult looks on, one woman stands by arch"

::SCRIPT::
- CHARACTER: Ellie
  LINE: Mommy! This is a place where dead animals talk! Mr. Crandall said so!
  EXPRESSION: Excited

::PATHS::
- CHOICE: "Rachel's reaction"
  TARGET: EXT. RACHEL AND ELLIE
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: EXT. RACHEL AND ELLIE
MOOD: Displeased
CHARACTERS: Rachel, Ellie
BACKGROUND_IMAGE: cemetery_arch.png
BACKGROUND_EDIT: "Woman looking displeased at a child's excited pronouncement"

::SCRIPT::
- CHARACTER: Rachel
  LINE: Did he.
  EXPRESSION: Unamused

::PATHS::
- CHOICE: "Return to Louis and Dud"
  TARGET: EXT. LOUIS AND JUD
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: EXT. LOUIS AND JUD
MOOD: Tense
CHARACTERS: Louis, Dud, Rachel
BACKGROUND_IMAGE: cemetery_arch.png
BACKGROUND_EDIT: "Two men talking, one woman observes, archway in background"

::SCRIPT::
- CHARACTER: Louis
  LINE: My wife is not crazy about cemeteries of any kind. As you may have noticed.
  EXPRESSION: Observant
- CHARACTER: Dud
  LINE: He neither. But I believe in knowing your enemy.
  EXPRESSION: Cryptic
- CHARACTER: Louis
  LINE: Looks at him, startled, then decides this is a joke. He laughs.
  EXPRESSION: Startled, then amused
- CHARACTER: Dud
  LINE: Smiles, a trifle thinly.
  EXPRESSION: Thin smile

::PATHS::
- CHOICE: "Rejoin the women"
  TARGET: EXT. THE ARCH, A NEW ANGLE
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: EXT. THE ARCH, A NEW ANGLE
MOOD: Departing
CHARACTERS: Louis, Rachel, Ellie, Dud
BACKGROUND_IMAGE: cemetery_arch.png
BACKGROUND_EDIT: "Group of people rejoining by the archway, preparing to leave"

::SCRIPT::
- CHARACTER: Louis
  LINE: Did we take too long?
  EXPRESSION: Inquiring
- CHARACTER: Rachel
  LINE: Well, if supper's burned, I'm not the one going out for pizza.
  EXPRESSION: Curt

::PATHS::
- CHOICE: "Move away"
  TARGET: EXT. THE DEADFALL, FROM THE ARCH
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: EXT. THE DEADFALL, FROM THE ARCH
MOOD: Ominous
CHARACTERS: Narrator
BACKGROUND_IMAGE: deadfall.png
BACKGROUND_EDIT: "View from the archway towards a dark, foreboding area (deadfall)"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The face we saw at the beginning of the movie wasn't there when the visitors were there...but it's sure there now, leering at us.
  EXPRESSION: Ominous

::PATHS::
- CHOICE: "Transition to kitchen"
  TARGET: INT. THE KITCHEN TRASH CAN - NIGHT
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: INT. THE KITCHEN TRASH CAN - NIGHT
MOOD: Disarray
CHARACTERS: Narrator, Louis
BACKGROUND_IMAGE: kitchen_trash.png
BACKGROUND_EDIT: "Kitchen trash can with pizza boxes, camera pulls back to show Louis at a table"

::SCRIPT::
- CHARACTER: Narrator
  LINE: There are two greasy boxes poking out with NAPOLI PIZZA stamped on them. Guess dinner was burned.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The camera pulls back and we see LOUIS sitting at the kitchen table. The table is covered with newspapers. On it, LOUIS is putting together a complicated model boat, using glue and tweezers. He's wearing glasses.
  EXPRESSION: Focused

::PATHS::
- CHOICE: "Ellie enters"
  TARGET: INT. THE KITCHEN TRASH CAN - NIGHT_ELLIE_ENTERS
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: INT. THE KITCHEN TRASH CAN - NIGHT
MOOD: Pensive
CHARACTERS: Ellie, Louis
BACKGROUND_IMAGE: kitchen_table_model.png
BACKGROUND_EDIT: "Child in nightgown watching father build a model boat"

::SCRIPT::
- CHARACTER: Ellie
  LINE: Comes in, wearing a nightgown. She watches him for awhile.
  EXPRESSION: Observant
- CHARACTER: Louis
  LINE: Hi, babe.
  EXPRESSION: Casual
- CHARACTER: Ellie
  LINE: Daddy, that Pet Sematary is there because of the road, isn't it?
  EXPRESSION: Questioning
- CHARACTER: Louis
  LINE: Looks around at her, surprised.
  EXPRESSION: Surprised
- CHARACTER: Ellie
  LINE: That's what I think. I heard Missy Dandridge tell Mom when Church was fixed he wouldn't cross the road so much.
  EXPRESSION: Theorizing

::PATHS::
- CHOICE: "Louis responds"
  TARGET: INT. LOUIS_RESPONSE
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: INT. LOUIS_RESPONSE
MOOD: Reassuring
CHARACTERS: Louis, Ellie
BACKGROUND_IMAGE: kitchen_table_model.png
BACKGROUND_EDIT: "Father reassuring his daughter"

::SCRIPT::
- CHARACTER: Louis
  LINE: Well, it's always better to take precautions--but I'm sure Church will be all right, honey...
  EXPRESSION: Reassuring

::PATHS::
- CHOICE: "Rachel overhears"
  TARGET: INT. JUST OUTSIDE THE KITCHEN DOOR
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: INT. JUST OUTSIDE THE KITCHEN DOOR
MOOD: Troubled
CHARACTERS: Rachel
BACKGROUND_IMAGE: kitchen_doorway.png
BACKGROUND_EDIT: "Woman standing outside a kitchen door, listening with a troubled expression"

::SCRIPT::
- CHARACTER: Narrator
  LINE: RACHEL is coming along with some dirty dishes. She hears voices and stops, listening, her face troubled and afraid.
  EXPRESSION: null
- CHARACTER: Ellie
  LINE: No he won't! Not in the end! He won't be all right in the end no matter how you fix 'im!
  EXPRESSION: Upset (voice)

::PATHS::
- CHOICE: "Ellie's despair continues"
  TARGET: INT. LOUIS AND ELLIE
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: INT. LOUIS AND ELLIE
MOOD: Heartbroken
CHARACTERS: Ellie, Louis
BACKGROUND_IMAGE: kitchen_table_comfort.png
BACKGROUND_EDIT: "Child crying in father's arms"

::SCRIPT::
- CHARACTER: Ellie
  LINE: In the end he’s gonna croak, isn't he?
  EXPRESSION: Crying
- CHARACTER: Louis
  LINE: Lovey...Church might be still alive when you're in a high school...and that’s a very long time.
  EXPRESSION: Comforting
- CHARACTER: Ellie
  LINE: It doesn't seem long to me. It seems short. I think the whole thing about pets dying s-s-sucks!
  EXPRESSION: Sobbing
- CHARACTER: Narrator
  LINE: Poor kid’s bawling her eyes out now. LOUIS folds her into his arms and she hugs him tightly, wanting his comfort.
  EXPRESSION: null
- CHARACTER: Louis
  LINE: If it was up to me I'd let Church live to be a hundred...but I don't make up the rules.
  EXPRESSION: Resigned
- CHARACTER: Ellie
  LINE: Well who does? God, I suppose. But he's not God's cat! He's my cat! Let God get His own, if He wants one! Not mine! Not mine! Not--
  EXPRESSION: Despairing
- CHARACTER: Ellie
  LINE: She breaks down completely, sobbing, and LOUIS rocks her back and forth.
  EXPRESSION: Sobbing

::PATHS::
- CHOICE: "Rachel's reaction"
  TARGET: INT. THE HALLWAY OUTSIDE THE KITCHEN, WITH RACHEL
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: INT. THE HALLWAY OUTSIDE THE KITCHEN, WITH RACHEL
MOOD: Sad
CHARACTERS: Rachel
BACKGROUND_IMAGE: hallway_crying.png
BACKGROUND_EDIT: "Woman crying silently in a hallway"

::SCRIPT::
- CHARACTER: Narrator
  LINE: She is crying silently.
  EXPRESSION: null

::PATHS::
- CHOICE: "Move to Ellie's room"
  TARGET: INT. ELLIE'S BEDROOM - NIGHT
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: INT. ELLIE'S BEDROOM - NIGHT
MOOD: Peaceful Sleep
CHARACTERS: Ellie
BACKGROUND_IMAGE: ellies_bedroom.png
BACKGROUND_EDIT: "Child sleeping peacefully in bed, illuminated by a shaft of light"

::SCRIPT::
- CHARACTER: Narrator
  LINE: She is a dimly perceived hump in the darkness. An oblong shaft of light falls on her, illuminating her more clearly. She's asleep with her teddy encircled by one arm and her thumb corked into her mouth.
  EXPRESSION: null

::PATHS::
- CHOICE: "Rachel checks on Ellie"
  TARGET: INT. THE DOORWAY, WITH RACHEL
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: INT. THE DOORWAY, WITH RACHEL
MOOD: Loving
CHARACTERS: Rachel, Ellie
BACKGROUND_IMAGE: ellies_bedroom_doorway.png
BACKGROUND_EDIT: "Woman looking lovingly at sleeping daughter through a doorway"

::SCRIPT::
- CHARACTER: Rachel
  LINE: Looks at her daughter with infinite love and then quietly closes the door.
  EXPRESSION: Loving

::PATHS::
- CHOICE: "Move to parents' bedroom"
  TARGET: INT. LOUIS'S AND RACHEL'S BEDROOM - NIGHT
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: INT. LOUIS'S AND RACHEL'S BEDROOM - NIGHT
MOOD: Studious, Tense
CHARACTERS: Louis, Rachel
BACKGROUND_IMAGE: parents_bedroom_books.png
BACKGROUND_EDIT: "Man studying medical books in bed, woman enters"

::SCRIPT::
- CHARACTER: Narrator
  LINE: LOUIS is in his pajamas, propped up on pillows on his side of the bed. There are a number of medical books scattered around him and he's making notes from one as RACHEL comes in.
  EXPRESSION: null
- CHARACTER: Rachel
  LINE: She's finally asleep.
  EXPRESSION: Tired
- CHARACTER: Louis
  LINE: She was a little over-excited, that's all. Poor kid.
  EXPRESSION: Reassuring
- CHARACTER: Rachel
  LINE: It was that place. That creepy cemetery up in the woods. Whatever disease the kids in this town have got, I don't want Ellie to catch it.
  EXPRESSION: Worried
- CHARACTER: Louis
  LINE: Jesus, Rachel, what’s got into you?
  EXPRESSION: Concerned
- CHARACTER: Rachel
  LINE: Do you think I didn't hear her tonight, crying as if her heart would break? Here she is thinking Church is going to die.
  EXPRESSION: Upset
- CHARACTER: Narrator
  LINE: It should be clear to us by now that, despite her words, RACHEL is much more upset than ELLIE was. LOUIS slowly puts his notebook aside and caps his pen.
  EXPRESSION: null
- CHARACTER: Louis
  LINE: Rachel... someday Church is going to die.
  EXPRESSION: Gentle
- CHARACTER: Rachel
  LINE: That is hardly the point! Church is not going to die today, or tomorrow-- Never mind. I can see you don't have the slightest idea what I'm talking about.
  EXPRESSION: Frustrated
- CHARACTER: Narrator
  LINE: She stalks to the bathroom, which adjoins. LOUIS follows. She goes in and slams the door.
  EXPRESSION: null
- CHARACTER: Louis
  LINE: Rachel--!
  EXPRESSION: Pleading
- CHARACTER: Narrator
  LINE: SOUND: CLICK OF THE LOCK. LOUIS stares at the door, bewildered and upset.
  EXPRESSION: null

::PATHS::
- CHOICE: "Truck headlights"
  TARGET: EXT. ROUTE 9 - NIGHT
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: EXT. ROUTE 9 - NIGHT
MOOD: Passing
CHARACTERS: Narrator
BACKGROUND_IMAGE: route9_truck.png
BACKGROUND_EDIT: "Large truck driving on a road at night, headlights visible"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Here comes a big Orinco truck, droning along, headlights glaring.
  EXPRESSION: null

::PATHS::
- CHOICE: "Lights illuminate room"
  TARGET: INT. LOUIS'S AND RACHEL'S BEDROOM
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: INT. LOUIS'S AND RACHEL'S BEDROOM
MOOD: Estranged Sleep
CHARACTERS: Louis, Rachel
BACKGROUND_IMAGE: bedroom_separated_sleep.png
BACKGROUND_EDIT: "Couple asleep on opposite sides of a bed, illuminated by truck headlights"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The headlights of the truck illuminate the room and we see LOUIS and RACHEL asleep, each as far over to his/her own side as he/she can get, with a big empty space in the middle. Lights and TRUCK SOUNDS slowly fade.
  EXPRESSION: null

::PATHS::
- CHOICE: "Morning in Gage's high chair"
  TARGET: INT. GAGE - MORNING
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: INT. GAGE - MORNING
MOOD: Messy Play
CHARACTERS: Gage
BACKGROUND_IMAGE: highchair_eggs.png
BACKGROUND_EDIT: "Baby in high chair, with scrambled eggs scattered around"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Cheerful little clots of scrambled eggs are scattered all the way across the tray of his high-chair--it looks a little like a map of the Pacific islands done by a guy who only had a yellow crayon.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Now he scoops up a handful and throws them.
  EXPRESSION: Playful

::PATHS::
- CHOICE: "Eggs fly onto toast"
  TARGET: INT. THE KITCHEN TABLE, WITH ELLIE
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: INT. THE KITCHEN TABLE, WITH ELLIE
MOOD: Disgusted
CHARACTERS: Ellie
BACKGROUND_IMAGE: eggs_on_toast.png
BACKGROUND_EDIT: "Child reacting to eggs splattering on toast"

::SCRIPT::
- CHARACTER: Ellie
  LINE: Yee-uck! Gross!
  EXPRESSION: Disgusted

::PATHS::
- CHOICE: "Wider kitchen shot"
  TARGET: INT. THE KITCHEN, A WIDER SHOT
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: INT. THE KITCHEN, A WIDER SHOT
MOOD: Domestic Morning
CHARACTERS: Rachel, Louis, Ellie
BACKGROUND_IMAGE: kitchen_dishes_setup.png
BACKGROUND_EDIT: "Woman doing dishes, blackboard visible, man and child dressed for the day"

::SCRIPT::
- CHARACTER: Narrator
  LINE: RACHEL is at the sink, doing dishes (we see the blackboard with its message near her).
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: LOUIS comes in, wearing a sport-coat and slacks, ready for his first day on the job...and ELLIE is in a pretty first day of school dress.
  EXPRESSION: null
- CHARACTER: Louis
  LINE: He can't help it, babe. Emily Post is going to be beyond him for a few years.
  EXPRESSION: Amused

::PATHS::
- CHOICE: "Cat carrier appears"
  TARGET: INT. BY THE KITCHEN DOOR
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: INT. BY THE KITCHEN DOOR
MOOD: Unhappy
CHARACTERS: Church (cat)
BACKGROUND_IMAGE: cat_carrier_unhappy.png
BACKGROUND_EDIT: "Cat carrier with a cat inside, cat is meowing unhappily"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Here is the cat-carrier with CHURCH inside it. He waows unhappily.
  EXPRESSION: null

::PATHS::
- CHOICE: "Ellie approaches carrier"
  TARGET: INT. THE KITCHEN TABLE, WITH ELLIE AND GAGE
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: INT. THE KITCHEN TABLE, WITH ELLIE AND GAGE
MOOD: Anxious
CHARACTERS: Ellie, Louis, Gage
BACKGROUND_IMAGE: ellie_cat_carrier.png
BACKGROUND_EDIT: "Child looking at cat carrier with anxiety, father nearby"

::SCRIPT::
- CHARACTER: Ellie
  LINE: I don't want him to get his nuts cut, daddy! What if he dies?
  EXPRESSION: Anxious

::PATHS::
- CHOICE: "Transition to Rachel and Louis"
  TARGET: INT. RACHEL AND LOUIS
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: RACHEL AND LOUIS, BY THE SINK
MOOD: AMUSED, CONCERNED
CHARACTERS: NARRATOR, LOUIS, ELLIE
BACKGROUND_IMAGE: kitchen_sink.png
BACKGROUND_EDIT: "Morning light, slightly cluttered kitchen counter"

::SCRIPT::
- CHARACTER: NARRATOR
  LINE: Louis looks shocked and amused by Ellie's colorful choice of words.
  EXPRESSION: null
- CHARACTER: LOUIS
  LINE: Good God! Where'd you hear that?
  EXPRESSION: Amused

::SCENE::
LOCATION: ELLIE
MOOD: EXPLANATORY
CHARACTERS: NARRATOR, ELLIE
BACKGROUND_IMAGE: kitchen_table.png
BACKGROUND_EDIT: "Close up on Ellie, perhaps holding a toy or doll"

::SCRIPT::
- CHARACTER: ELLIE
  LINE: Missy Dandridge. And she says it's a operation!
  EXPRESSION: Matter-of-fact

::SCENE::
LOCATION: RACHEL AND LOUIS, BY THE SINK
MOOD: DISAPPOINTED, ANNOYED
CHARACTERS: NARRATOR, LOUIS, RACHEL
BACKGROUND_IMAGE: kitchen_sink.png
BACKGROUND_EDIT: "Morning light, slightly cluttered kitchen counter"

::SCRIPT::
- CHARACTER: NARRATOR
  LINE: Louis tries to kiss Rachel's mouth. She turns her head slightly so he gets her cheek instead. She's still mad. Louis’s amusement dies.
  EXPRESSION: null
- CHARACTER: RACHEL
  LINE: Honey, Church will be fine.
  EXPRESSION: Reassuring

::SCENE::
LOCATION: ELLIE, BY THE CAT CARRIER
MOOD: FEARFUL
CHARACTERS: NARRATOR, ELLIE
BACKGROUND_IMAGE: cat_carrier.png
BACKGROUND_EDIT: "Close up on a cat carrier, perhaps with a cat visible inside"

::SCRIPT::
- CHARACTER: ELLIE
  LINE: But what if he dies and has to go to the Pet Sematary?
  EXPRESSION: Afraid

::SCENE::
LOCATION: LOUIS AND RACHEL, BY THE SINK
MOOD: CONFLICTED, TRYING TO REASSURE
CHARACTERS: NARRATOR, LOUIS, RACHEL, ELLIE
BACKGROUND_IMAGE: kitchen_sink.png
BACKGROUND_EDIT: "Morning light, slightly cluttered kitchen counter"

::SCRIPT::
- CHARACTER: NARRATOR
  LINE: She gives him a look as if to say: "There! Now do you understand what you did?"
  EXPRESSION: null
- CHARACTER: RACHEL
  LINE: Don't be silly. Church is not going to die.
  EXPRESSION: Dismissive
- CHARACTER: LOUIS
  LINE: According to what Mr. Crandall says, the road's a lot more dangerous than the operation. Church will be just the same. Well--almost the same--and we won’t have to worry about him getting turned into catburgers by one of those damn Orinco trucks.
  EXPRESSION: Reassuring, slightly dismissive
- CHARACTER: NARRATOR
  LINE: At this Rachel tightens up still more in that funny way--she's actually angered by Louis's reference to catburgers--but under the anger we sense she is deeply shocked, as a prudish woman might be shocked by a dirty joke. For Rachel, that's just what death is.
  EXPRESSION: null
- CHARACTER: RACHEL
  LINE: That's enough of that kind of talk!
  EXPRESSION: Stern
- CHARACTER: LOUIS
  LINE: I just said--
  EXPRESSION: Incredulous
- CHARACTER: RACHEL
  LINE: I know what you just said. Ellie, clear your place.
  EXPRESSION: Authoritative
- CHARACTER: NARRATOR
  LINE: Ellie goes slowly back to the table.
  EXPRESSION: null
- CHARACTER: ELLIE
  LINE: I'm scared. What if school here isn’t like in Chicago! I’m scared and I want to go h-h-home!
  EXPRESSION: Terrified
- CHARACTER: NARRATOR
  LINE: Ellie bursts into loud tears and puts her hands over her face.
  EXPRESSION: null

::SCENE::
LOCATION: THE KITCHEN, A NEW ANGLE (FEATURES LOUIS AND RACHEL)
MOOD: COMFORTING, REASSURING
CHARACTERS: NARRATOR, LOUIS, RACHEL, ELLIE
BACKGROUND_IMAGE: kitchen.png
BACKGROUND_EDIT: "Morning light, Louis and Rachel approaching a table where Ellie is crying"

::SCRIPT::
- CHARACTER: NARRATOR
  LINE: The camera follows as they go to the table to comfort Ellie.
  EXPRESSION: null
- CHARACTER: RACHEL
  LINE: You’ll be fine, Ellie. Now you can be excused. Go and wash your face.
  EXPRESSION: Gentle
- CHARACTER: LOUIS
  LINE: And Church will be fine.
  EXPRESSION: Reassuring
- CHARACTER: ELLIE
  LINE: Do you promise, Daddy?
  EXPRESSION: Anxious
- CHARACTER: LOUIS
  LINE: Well, honey...you know that...
  EXPRESSION: Hesitant
- CHARACTER: RACHEL
  LINE: Don't shilly-shally, Louis. Give the little girl her promise.
  EXPRESSION: Firm
- CHARACTER: LOUIS
  LINE: Church will be fine. I promise.
  EXPRESSION: Reluctantly reassuring
- CHARACTER: ELLIE
  LINE: Yayyyy!
  EXPRESSION: Elated
- CHARACTER: NARRATOR
  LINE: She runs off, cheered up. And Rachel is cheered up, too.
  EXPRESSION: null
- CHARACTER: RACHEL
  LINE: Thank you, Louis.
  EXPRESSION: Grateful
- CHARACTER: LOUIS
  LINE: Oh, you’re welcome. Only if something should go wrong while he's under the gas--it’s a one-in-a-thousand shot, but it happens--you explain to her.
  EXPRESSION: Matter-of-fact, slightly grim
- CHARACTER: NARRATOR
  LINE: He gets up and leaves the table. She looks after him, stunned and a little frightened.
  EXPRESSION: null

::SCENE::
LOCATION: GAGE
MOOD: PLAYFUL, UNCARING
CHARACTERS: NARRATOR, GAGE
BACKGROUND_IMAGE: tray_of_food.png
BACKGROUND_EDIT: "Close up on a lunch tray with scrambled eggs"

::SCRIPT::
- CHARACTER: GAGE
  LINE: Here, Durch!
  EXPRESSION: Playful
- CHARACTER: NARRATOR
  LINE: He picks up a large glob of scrambled eggs from his tray and throws it in the direction of the cat-carrier.
  EXPRESSION: null

::SCENE::
LOCATION: THE CAT-CARRIER
MOOD: STARTLED, SURPRISED
CHARACTERS: NARRATOR, CHURCH
BACKGROUND_IMAGE: cat_carrier_inside.png
BACKGROUND_EDIT: "Inside a cat carrier, with a cat looking out"

::SCRIPT::
- CHARACTER: NARRATOR
  LINE: Church is close to the mesh, looking out. Scrambled eggs hit the mesh, driving him back, surprised.
  EXPRESSION: null

::SCENE::
LOCATION: THE CREED HOUSE MORNING
MOOD: BUSY, ORDINARY
CHARACTERS: NARRATOR, ELLIE
BACKGROUND_IMAGE: front_lawn_bus.png
BACKGROUND_EDIT: "Morning, a school bus pulling up to a house"

::SCRIPT::
- CHARACTER: NARRATOR
  LINE: The school bus pulls up, red lights flashing. Ellie runs toward it across the lawn, with her lunch-box.
  EXPRESSION: null

::SCENE::
LOCATION: LOUIS, RACHEL, AND GAGE, IN THE FRONT DOORWAY
MOOD: AFFECTIONATE, ORDINARY
CHARACTERS: NARRATOR, RACHEL, LOUIS, GAGE
BACKGROUND_IMAGE: front_doorway.png
BACKGROUND_EDIT: "Morning, Louis, Rachel, and Gage standing in the doorway"

::SCRIPT::
- CHARACTER: RACHEL
  LINE: Have a great day!
  EXPRESSION: Affectionate
- CHARACTER: LOUIS
  LINE: Louis grabs Gage’s hand and makes him wave it.
  EXPRESSION: Playful
- CHARACTER: GAGE
  LINE: Bye-bye!
  EXPRESSION: Enthusiastic

::SCENE::
LOCATION: THE BUS
MOOD: ORDINARY GOODBYE
CHARACTERS: NARRATOR, ELLIE
BACKGROUND_IMAGE: bus_interior.png
BACKGROUND_EDIT: "Ellie climbing the steps of a school bus"

::SCRIPT::
- CHARACTER: NARRATOR
  LINE: Ellie climbs aboard. The red flashers go out and the bus pulls away.
  EXPRESSION: null

::SCENE::
LOCATION: THE CREED DRIVEWAY - MORNING
MOOD: PREPARING FOR A TRIP, UNEXPECTED ARRIVAL
CHARACTERS: NARRATOR, LOUIS, MISSY DANDRIDGE
BACKGROUND_IMAGE: driveway_morning.png
BACKGROUND_EDIT: "Morning, a station wagon parked in a driveway, Louis with a briefcase and cat carrier"

::SCRIPT::
- CHARACTER: NARRATOR
  LINE: The station wagon is parked there. Louis comes out with a heavy briefcase in one hand and the cat-carrier in the other. He opens the wagon’s doorgate.
  EXPRESSION: null
- CHARACTER: NARRATOR
  LINE: A small car turns into the Creed driveway and parks beside Louis.
  EXPRESSION: null
- CHARACTER: NARRATOR
  LINE: A rather sour-looking middle-aged woman gets out and crosses the front of her car. Her color is bad. This is Missy Dandridge. She looks at the cat-carrier.
  EXPRESSION: null
- CHARACTER: MISSY
  LINE: Gonna get his--
  EXPRESSION: Conversational
- CHARACTER: LOUIS
  LINE: --nuts cut, yes. Thank you, Missy, for introducing that colorful phrase into my daughter's vocabulary.
  EXPRESSION: Dryly amused
- CHARACTER: MISSY
  LINE: Don't mention it.
  EXPRESSION: Indifferent
- CHARACTER: NARRATOR
  LINE: She opens the passenger side door of her car and we see a big neat pile of folded sheets. She reaches for them, then winces and presses her hands against her midriff for a moment, as if with an attack of indigestion.
  EXPRESSION: null
- CHARACTER: LOUIS
  LINE: How's that belly-ache of yours?
  EXPRESSION: Concerned

::SCENE::
LOCATION: THE SIDE YARD - MORNING
MOOD: HASTY, SLIGHTLY WORRIED
CHARACTERS: NARRATOR, RACHEL, MISSY DANDRIDGE, LOUIS
BACKGROUND_IMAGE: side_yard.png
BACKGROUND_EDIT: "Morning, Rachel passing Missy Dandridge as Louis loads the cat carrier"

::SCRIPT::
- CHARACTER: NARRATOR
  LINE: Rachel hurries past Missy, who turns to look and then goes on into the house. Louis has just put the cat-carrier into the back of the wagon and closed the doorgate as Rachel reaches him.
  EXPRESSION: null
- CHARACTER: RACHEL
  LINE: Still friends, doc?
  EXPRESSION: Anxious
- CHARACTER: NARRATOR
  LINE: Louis appears to consider this seriously for a moment...and then he smiles and hugs her. They kiss.
  EXPRESSION: null
- CHARACTER: RACHEL
  LINE: Thank God. I was a little worried there. Have a great first day at school, doc. No broken bones.
  EXPRESSION: Relieved, affectionate
- CHARACTER: LOUIS
  LINE: Not so much as a sprain.
  EXPRESSION: Smiling

::SCENE::
LOCATION: VICTOR PASCOW AND FRIENDS - MORNING
MOOD: CHAOTIC, GRUESOME
CHARACTERS: NARRATOR, PASCOW, VICTOR PASCOW, FRIENDS
BACKGROUND_IMAGE: college_campus_morning.png
BACKGROUND_EDIT: "Morning, a group of students carrying an injured person on a blanket"

::SCRIPT::
- CHARACTER: NARRATOR
  LINE: PascoW is in a blanket that is being carried by three boys and one girl. They are all yelling at each other not to joggle him, not to drop him. A small knot of horrified college kids moves with the bearers.
  EXPRESSION: null
- CHARACTER: NARRATOR
  LINE: PascoW's head is upside down to the camera, which retreats ahead of the advancing students. Fixed eyes stare. Half of his head has been shattered inward. Before the catastrophe he was a husky male of about twenty. He's dressed in a U of M muscle shirt and red jogging shorts.
  EXPRESSION: null
- CHARACTER: NARRATOR
  LINE: The camera pulls jerkily to one side, allowing the bearers to mount the steps of a brick building. The infirmary. The lookers-on break to either side. The infirmary doors open.
  EXPRESSION: null

::SCENE::
LOCATION: NURSE CHARLTON, AT THE DOORS
MOOD: SHOCKED, URGENT
CHARACTERS: NARRATOR, CHARLTON, NURSE CHARLTON
BACKGROUND_IMAGE: infirmary_entrance.png
BACKGROUND_EDIT: "Infirmary doorway, a nurse looking out"

::SCRIPT::
- CHARACTER: CHARLTON
  LINE: Holy Jesus. (turns) Steve! Steve! Dr. Creed! Dr. Creed, we've got a mess here! Stat!
  EXPRESSION: Shocked, urgent
- CHARACTER: NARRATOR
  LINE: The bearers sweep past her and inside, leaving a red smear of blood across the midriff of Marcy Charlton’s uniform.
  EXPRESSION: null

::SCENE::
LOCATION: THE INFIRMARY RECEPTION AREA
MOOD: HORRIFIED, PANICKED
CHARACTERS: NARRATOR, LOUIS, STEVE MASTERTON, CHARLTON, CANDYSTRIPER, GIRL
BACKGROUND_IMAGE: infirmary_reception.png
BACKGROUND_EDIT: "Infirmary reception area, chaos and medical personnel"

::SCRIPT::
- CHARACTER: NARRATOR
  LINE: The camera will show us all we need to see, but its movements will seem almost random; this is like being in the hotel kitchen after Sirhan shot Bobby.
  EXPRESSION: null
- CHARACTER: NARRATOR
  LINE: As the students bring in PascoW, Louis comes running, followed by Steve Masterton, his P.A. Standing to one side are two student nurses in candystriper uniforms. They're boggled and horrified.
  EXPRESSION: null
- CHARACTER: NARRATOR
  LINE: Louis kneels. The camera rushes forward, shoving between onlookers. Louis looks at the wound. There’s shattered bone and pulsing brain tissue beneath.
  EXPRESSION: null
- CHARACTER: NARRATOR
  LINE: There's a scream; the girl who was carrying one corner of the blanket is having hysterics.
  EXPRESSION: null
- CHARACTER: GIRL
  LINE: Vic! Vic! Oh Christ! Vic!
  EXPRESSION: Hysterical
- CHARACTER: LOUIS
  LINE: Get her out. Get them all out.
  EXPRESSION: Commanding
- CHARACTER: CHARLTON
  LINE: Charlton puts her arms around the girl.
  EXPRESSION: Comforting
- CHARACTER: GIRL
  LINE: No! No, he can't die! He can't die!
  EXPRESSION: Desperate
- CHARACTER: NARRATOR
  LINE: The camera moves back down as Louis takes an opthalmascope from Steve and shines it in PascoW's bulging, fixed eyes.
  EXPRESSION: null
- CHARACTER: CHARLTON
  LINE: Charlton is just pushing the last of them gawkers and bearers out the door.
  EXPRESSION: null
- CHARACTER: LOUIS
  LINE: Steve, get the ambulance over here right now. He’s got to go to EMMC.
  EXPRESSION: Urgent
- CHARACTER: STEVE
  LINE: The ambulance is at Sonny's Sunoco downtown, getting--
  EXPRESSION: Stressed
- CHARACTER: LOUIS
  LINE: --a new muffler, oh shit--
  EXPRESSION: Exasperated
- CHARACTER: NARRATOR
  LINE: PascoW makes a weird gargling noise. Blood suddenly spurts out of his mouth. He begins to seizure.
  EXPRESSION: null
- CHARACTER: NARRATOR
  LINE: One of the candystripers shrieks. The camera jerks up to cover the student nurses. One turns and throws up on the wall.
  EXPRESSION: null
- CHARACTER: CANDYSTRIPER
  LINE: I can't look at it... I can't stand it...
  EXPRESSION: Distraught
- CHARACTER: CHARLTON
  LINE: Yes you by God can. Go get the hard stretcher!
  EXPRESSION: Stern
- CHARACTER: NARRATOR
  LINE: As they start away, one helping the other down the hall, and as Charlton starts over to where PascoW lies dying on his blanket, the camera drops to Louis and Steve.
  EXPRESSION: null
- CHARACTER: LOUIS
  LINE: Help me hold him.
  EXPRESSION: Determined
- CHARACTER: NARRATOR
  LINE: They hold PascoW's spasming body.
  EXPRESSION: null
- CHARACTER: STEVE
  LINE: It wouldn't matter if we did have the ambulance.
  EXPRESSION: Resigned
- CHARACTER: LOUIS
  LINE: It wouldn't matter if we had the SST.
  EXPRESSION: Resigned
- CHARACTER: NARRATOR
  LINE: PascoW begins to quiet.
  EXPRESSION: null
- CHARACTER: LOUIS
  LINE: He's going. Steve, go call the motor pool. Marcy, roll out the crash wagon.
  EXPRESSION: Urgent
- CHARACTER: CHARLTON
  LINE: It won't--
  EXPRESSION: Resigned
- CHARACTER: LOUIS
  LINE: I know it won't! But let's for God's sake do it by the rules!
  EXPRESSION: Frustrated
- CHARACTER: NARRATOR
  LINE: She leaves. Louis is alone with PascoW. Charlton has drawn the drapes, so the doctor and the dying man have complete if temporary privacy.
  EXPRESSION: null

::SCENE::
LOCATION: LOUIS AND PASCOW, A CLOSER SHOT
MOOD: INTENSE, FOREBODING
CHARACTERS: NARRATOR, LOUIS, PASCOW
BACKGROUND_IMAGE: infirmary_curtained_area.png
BACKGROUND_EDIT: "Draped area of the infirmary, Louis and PascoW"

::SCRIPT::
- CHARACTER: LOUIS
  LINE: There wasn't even supposed to be a sprain today, my friend--that's what I told her.
  EXPRESSION: Somber
- CHARACTER: NARRATOR
  LINE: PascoW's fixed eyes suddenly roll and his left hand bear-traps Louis's right wrist. The dying man pulls him slowly but relentlessly down, until their faces are only inches apart.
  EXPRESSION: null
- CHARACTER: PASCOW
  LINE: ...Pet Sematary...
  EXPRESSION: Gurgling, weak
- CHARACTER: NARRATOR
  LINE: Louis recoils, breaking the grip of the hand...but he cannot quite snap the grip of those bright dying eyes. Blood leaks from PascoW's mouth.
  EXPRESSION: null
- CHARACTER: LOUIS
  LINE: W-What did you say...?
  EXPRESSION: Whispering, shocked
- CHARACTER: NARRATOR
  LINE: PascoW struggles hard to speak again. At first he can only gurgle.
  EXPRESSION: null
- CHARACTER: PASCOW
  LINE: It's not the real cemetery... (Long pause) The soil of a man's heart is stonier, Louis... a man grows what he can... and tends it.
  EXPRESSION: Gurgling, broken
- CHARACTER: NARRATOR
  LINE: Louis leans forward again
  EXPRESSION: null

::SCENE::
LOCATION: Hallway Entrance to Reception
MOOD: Terrified, Urgent
CHARACTERS: Louis, Pascow
BACKGROUND_IMAGE: hallway_reception.png
BACKGROUND_EDIT: "Dimly lit hallway, with Steve present"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Terrified, yet needing to know.
  EXPRESSION: Terrified
- CHARACTER: Louis
  LINE: How do you know my name?
  EXPRESSION: Terrified
- CHARACTER: Pascow
  LINE: I'll come...to you.
  EXPRESSION: Gurgling
- CHARACTER: Narrator
  LINE: Louis grabs Pascow's bloody shoulder.
  EXPRESSION: Urgent
- CHARACTER: Louis
  LINE: Dammit, how do you know my name?
  EXPRESSION: Low but Urgent
- CHARACTER: Steve
  LINE: Louis, they’re sending a--
  EXPRESSION: Concerned

::PATHS::
- CHOICE: "Continue speaking to Pascow"
  TARGET: louis_pas_scene
  STATE_CHANGE: fear = +2
  CONDITION: null

::SCENE::
LOCATION: Louis and Pascow
MOOD: Desperate, Shocked
CHARACTERS: Louis, Pascow
BACKGROUND_IMAGE: louis_pas_scene.png
BACKGROUND_EDIT: "Close-up on Louis and Pascow"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Pascow begins to spasm again.
  EXPRESSION: null
- CHARACTER: Louis
  LINE: Help me!
  EXPRESSION: Snapping
- CHARACTER: Narrator
  LINE: Pascow spews more blood as Steve kneels beside Louis.
  EXPRESSION:null

::PATHS::
- CHOICE: "Seek help from Steve"
  TARGET: the_hain_infirmary_hallway
  STATE_CHANGE: desperation = +1
  CONDITION: null

::SCENE::
LOCATION: The Hain Infirmary Hallway
MOOD: Professional, Prepared
CHARACTERS: Charlton
BACKGROUND_IMAGE: hain_hallway.png
BACKGROUND_EDIT: "Hallway with a medical cart"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Charlton is pushing along your basic MEDCU goodie-cart, covered with emergency life-saving gear.
  EXPRESSION: null

::PATHS::
- CHOICE: "Wait for Charlton to arrive"
  TARGET: louis_steve_pas_scene
  STATE_CHANGE: anticipation = +1
  CONDITION: null

::SCENE::
LOCATION: Louis, Steve, Pascow
MOOD: Resigned, Tragic
CHARACTERS: Louis, Steve, Pascow, Charlton
BACKGROUND_IMAGE: louis_steve_pas_scene.png
BACKGROUND_EDIT: "Louis, Steve, and Pascow in a room"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Pascow's spasms are weakening.
  EXPRESSION: null
- CHARACTER: Louis
  LINE: Never mind. He's going.
  EXPRESSION: To Charlton
- CHARACTER: Narrator
  LINE: Pasow's hand comes up and paws at Louis's shirt, leaving a bloody handprint. Then it falls limply back. Pasow is dead.
  EXPRESSION: null
- CHARACTER: Louis
  LINE: Steve, will you get a sheet to cover him with?
  EXPRESSION: Somber
- CHARACTER: Narrator
  LINE: Steve leaves the frame and Louis stares fixedly down at the body of Victor Pascow. He closes the eyes.
  EXPRESSION: Somber

::PATHS::
- CHOICE: "Cover Pascow's body and reflect"
  TARGET: country_road_aftermath
  STATE_CHANGE: grief = +1
  CONDITION: null

::SCENE::
LOCATION: A Country Road
MOOD: Serene, Contrasting
CHARACTERS: Louis
BACKGROUND_IMAGE: country_road_aftermath.png
BACKGROUND_EDIT: "Sunny autumn afternoon, leading edge of fall"

::SCRIPT::
- CHARACTER: Narrator
  LINE: It’s the leading edge of Maine fall, sunny and wonderful. Here comes Louis's station wagon. As it reaches the camera, it swivels to track.
  EXPRESSION: null
- CHARACTER: Radio (Voice-over)
  LINE: Tragedy struck on the first day of the University of Maine's fall semester when Victor Pascow, a nineteen-year-old sophomore--
  EXPRESSION: News report

::PATHS::
- CHOICE: "Continue driving"
  TARGET: car_interior_aftermath
  STATE_CHANGE: reflection = +1
  CONDITION: null

::SCENE::
LOCATION: The Car
MOOD: Shocked, Disturbed
CHARACTERS: Louis
BACKGROUND_IMAGE: car_interior_aftermath.png
BACKGROUND_EDIT: "Inside Louis's station wagon"

::SCRIPT::
- CHARACTER: Narrator
  LINE: He still looks shocked by the tragedy. The dying man's bloody handprint is partly visible on Louis's shirt in spite of his sport-coat.
  EXPRESSION: Shocked
- CHARACTER: Louis
  LINE: He said my name. I heard it. He said my name.
  EXPRESSION: Distraught
- CHARACTER: Narrator
  LINE: He stares blankly through the windshield.
  EXPRESSION: Blank

::PATHS::
- CHOICE: "Pull over to the side of the road"
  TARGET: station_wagon_stop
  STATE_CHANGE: distress = +1
  CONDITION: null

::SCENE::
LOCATION: The Station Wagon
MOOD: Abrupt, Violent
CHARACTERS: Louis
BACKGROUND_IMAGE: station_wagon_stop.png
BACKGROUND_EDIT: "Station wagon stopping abruptly on a country road"

::SCRIPT::
- CHARACTER: Narrator
  LINE: It comes to a slueing, shuddering stop, almost going in the ditch.
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue driving"
  TARGET: louis_behind_wheel_aftermath
  STATE_CHANGE: frustration = +1
  CONDITION: null

::SCENE::
LOCATION: Louis, Behind the Wheel
MOOD: Agitated, Disbelieving
CHARACTERS: Louis
BACKGROUND_IMAGE: louis_behind_wheel_aftermath.png
BACKGROUND_EDIT: "Close-up on Louis in the driver's seat"

::SCRIPT::
- CHARACTER: Louis
  LINE: He said my name. I heard it. He said my name.
  EXPRESSION: Agitated
- CHARACTER: Narrator
  LINE: He stares blankly through the windshield.
  EXPRESSION: Blank

::PATHS::
- CHOICE: "Continue driving home"
  TARGET: creed_house_night
  STATE_CHANGE: obsession = +1
  CONDITION: null

::SCENE::
LOCATION: The Creed House
MOOD: Peaceful, Deceptive
CHARACTERS: Narrator
BACKGROUND_IMAGE: creed_house_night.png
BACKGROUND_EDIT: "Exterior of the Creed house at night, all lights off"

::SCRIPT::
- CHARACTER: Narrator
  LINE: All lights are off. It’s late.
  EXPRESSION: null

::PATHS::
- CHOICE: "Enter the house"
  TARGET: creed_bedroom_night
  STATE_CHANGE: peace = +1
  CONDITION: null

::SCENE::
LOCATION: The Creed Bedroom
MOOD: Peaceful, Then Terror
CHARACTERS: Louis, Rachel
BACKGROUND_IMAGE: creed_bedroom_night.png
BACKGROUND_EDIT: "Bedroom interior, Louis and Rachel asleep"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Louis and Rachel are asleep, each on his/her own side of the big double. The camera moves in on Louis.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: SOUND: Loud, hollow BANG. It's very loud--loud enough to wake the dead.
  EXPRESSION: Terrifying
- CHARACTER: Narrator
  LINE: Louis sits up. Beside him, Rachel sleeps on. Louis's eyes widen in terror as he stares at:
  EXPRESSION: Terrified

::PATHS::
- CHOICE: "Look at the doorway"
  TARGET: doorway_pas_scene
  STATE_CHANGE: terror = +2
  CONDITION: null

::SCENE::
LOCATION: The Doorway
MOOD: Horrifying, Unnatural
CHARACTERS: Pascow
BACKGROUND_IMAGE: doorway_pas_scene.png
BACKGROUND_EDIT: "Pasow standing in the doorway, dead"

::SCRIPT::
- CHARACTER: Narrator
  LINE: He's exquisitely dead. Now pallid as well as smashed up.
  EXPRESSION: Horrifying
- CHARACTER: Pascow
  LINE: Come on, doc. We got places to go.
  EXPRESSION: Unnatural

::PATHS::
- CHOICE: "Respond to Pascow"
  TARGET: louis_scene_terror
  STATE_CHANGE: fear = +1
  CONDITION: null

::SCENE::
LOCATION: Louis
MOOD: Terror and Trance
CHARACTERS: Louis
BACKGROUND_IMAGE: louis_scene_terror.png
BACKGROUND_EDIT: "Close-up on Louis's face"

::SCRIPT::
- CHARACTER: Narrator
  LINE: He is in terror...but he is also in a state of near-trance.
  EXPRESSION: Terrified

::PATHS::
- CHOICE: "Listen to Pascow"
  TARGET: pascow_scene_insist
  STATE_CHANGE: compulsion = +1
  CONDITION: null

::SCENE::
LOCATION: Pascow
MOOD: Insistent, Demanding
CHARACTERS: Pascow
BACKGROUND_IMAGE: pascow_scene_insist.png
BACKGROUND_EDIT: "Close-up on Pascow's face"

::SCRIPT::
- CHARACTER: Pascow
  LINE: Come on, doc--don't make me tell you twice.
  EXPRESSION: Insistent

::PATHS::
- CHOICE: "Look at Rachel"
  TARGET: louis_scene_rachel_glance
  STATE_CHANGE: conflict = +1
  CONDITION: null

::SCENE::
LOCATION: Louis
MOOD: Disbelief, Isolation
CHARACTERS: Louis, Rachel, Pascow
BACKGROUND_IMAGE: louis_scene_rachel_glance.png
BACKGROUND_EDIT: "Louis glancing at Rachel, then back at Pascow"

::SCRIPT::
- CHARACTER: Narrator
  LINE: He glances at Rachel. Although Pascow has spoken in a fairly loud voice--and the opening door was like a bomb--she's still fast asleep. Louis looks back toward Pascow...and then gets out of bed.
  EXPRESSION: Disbelieving
- CHARACTER: Narrator
  LINE: He's naked except for a pair of pajama bottoms.
  EXPRESSION: Vulnerable

::PATHS::
- CHOICE: "Follow Pascow"
  TARGET: pascow_scene_leaves
  STATE_CHANGE: surrender = +1
  CONDITION: null

::SCENE::
LOCATION: Pascow
MOOD: Leading, Unseen
CHARACTERS: Pascow
BACKGROUND_IMAGE: pascow_scene_leaves.png
BACKGROUND_EDIT: "Pasow turning and leaving the doorway"

::SCRIPT::
- CHARACTER: Narrator
  LINE: He turns and leaves the doorway.
  EXPRESSION: null

::PATHS::
- CHOICE: "Follow Pascow out of the room"
  TARGET: louis_scene_bedroom_doorway
  STATE_CHANGE: obedience = +1
  CONDITION: null

::SCENE::
LOCATION: Louis
MOOD: Relief, Then Dread
CHARACTERS: Louis
BACKGROUND_IMAGE: louis_scene_bedroom_doorway.png
BACKGROUND_EDIT: "Louis at the bedroom doorway, looking back"

::SCRIPT::
- CHARACTER: Narrator
  LINE: He reaches the bedroom doorway himself and looks back at:
  EXPRESSION:null
- CHARACTER: Narrator
  LINE: Oh. Thank God.
  EXPRESSION: Relieved

::PATHS::
- CHOICE: "Exit the bedroom"
  TARGET: bed_louis_pov
  STATE_CHANGE: relief = +1
  CONDITION: null

::SCENE::
LOCATION: The Bed, Louis's POV
MOOD: Deceptive Peace
CHARACTERS: Rachel, Louis
BACKGROUND_IMAGE: bed_louis_pov.png
BACKGROUND_EDIT: "Louis's POV of Rachel and himself asleep in bed"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Rachel is sleeping as before, and Louis himself is also in bed asleep, although his rest is uneasy...as if he's having a bad dream.
  EXPRESSION: Uneasy

::PATHS::
- CHOICE: "Exit the bedroom"
  TARGET: doorway_louis_scene
  STATE_CHANGE: dream_state = +1
  CONDITION: null

::SCENE::
LOCATION: The Doorway
MOOD: False Relief, Lingering Threat
CHARACTERS: Louis, Pascow (voice)
BACKGROUND_IMAGE: doorway_louis_scene.png
BACKGROUND_EDIT: "Louis in the doorway, Pascow's voice heard"

::SCRIPT::
- CHARACTER: Louis
  LINE: Oh. Thank God.
  EXPRESSION: Relieved
- CHARACTER: Pascow (voice)
  LINE: Hurry up, doc.
  EXPRESSION: Impatient

::PATHS::
- CHOICE: "Go to the kitchen"
  TARGET: kitchen_scene
  STATE_CHANGE: apprehension = +1
  CONDITION: null

::SCENE::
LOCATION: The Kitchen
MOOD: Anticipation, Unease
CHARACTERS: Louis, Pascow
BACKGROUND_IMAGE: kitchen_scene.png
BACKGROUND_EDIT: "Kitchen interior, door to shed/garage open"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Louis enters and crosses toward the door which gives on the shed/garage. This door stands open. Louis pauses by it.
  EXPRESSION: Uneasy
- CHARACTER: Pascow
  LINE: Come on, doc...
  EXPRESSION: Low

::PATHS::
- CHOICE: "Enter the shed/garage"
  TARGET: shed_garage_scene
  STATE_CHANGE: dread = +1
  CONDITION: null

::SCENE::
LOCATION: The Shed/Garage
MOOD: Foreboding, Confrontational
CHARACTERS: Louis, Pascow
BACKGROUND_IMAGE: shed_garage_scene.png
BACKGROUND_EDIT: "Interior of shed/garage with station wagon"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The station wagon is a dark hulk. Louis crosses to it and stands, perplexed.
  EXPRESSION: Perplexed
- CHARACTER: Narrator
  LINE: Pascow looms softly behind him and puts an arm around him. Louis turns... and suddenly his face is less than an inch from Pascow's mutilated face.
  EXPRESSION: Shocked
- CHARACTER: Pascow
  LINE: Let's go, doc.
  EXPRESSION: Demanding
- CHARACTER: Louis
  LINE: I don't like this dream.
  EXPRESSION: Moaning
- CHARACTER: Pascow
  LINE: Who said you were dreaming?
  EXPRESSION: Menacing

::PATHS::
- CHOICE: "Follow Pascow towards the garage door"
  TARGET: field_behind_house_long_night
  STATE_CHANGE: resignation = +1
  CONDITION: null

::SCENE::
LOCATION: The Field Behind the House, Long
MOOD: Eerie, Ascending
CHARACTERS: Pascow, Louis
BACKGROUND_IMAGE: field_behind_house_long_night.png
BACKGROUND_EDIT: "Two figures walking towards the woods at night"

::SCRIPT::
- CHARACTER: Narrator
  LINE: We can see two shapes moving up the path toward the woods--Pascow and, behind him, Louis.
  EXPRESSION: Eerie

::PATHS::
- CHOICE: "Follow them to the Pet Sematary Arch"
  TARGET: pet_sematary_arch
  STATE_CHANGE: journey = +1
  CONDITION: null

::SCENE::
LOCATION: The Pet Sematary Arch
MOOD: Ominous, Descending
CHARACTERS: Louis
BACKGROUND_IMAGE: pet_sematary_arch.png
BACKGROUND_EDIT: "Camera panning down as Louis passes under the arch"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Camera holds, then pans down as Louis passes under the arch.
  EXPRESSION: null

::PATHS::
- CHOICE: "Enter the Pet Sematary"
  TARGET: louis_close_pet_sematary
  STATE_CHANGE: fear = +1
  CONDITION: null

::SCENE::
LOCATION: Louis, Close
MOOD: Fearful, Hesitant
CHARACTERS: Louis
BACKGROUND_IMAGE: louis_close_pet_sematary.png
BACKGROUND_EDIT: "Close-up on Louis's face, looking around"

::SCRIPT::
- CHARACTER: Narrator
  LINE: He looks around, obviously afraid.
  EXPRESSION: Afraid

::PATHS::
- CHOICE: "Observe the Pet Sematary"
  TARGET: pet_sematary_louis_pov
  STATE_CHANGE: dread = +1
  CONDITION: null

::SCENE::
LOCATION: The Pet Sematary, Louis's POV
MOOD: Terrifying, Starlit
CHARACTERS: Narrator
BACKGROUND_IMAGE: pet_sematary_louis_pov.png
BACKGROUND_EDIT: "Louis's view of the Pet Sematary by starlight"

::SCRIPT::
- CHARACTER: Narrator
  LINE: We can see why. By starlight this is one scary place.
  EXPRESSION: Terrifying

::PATHS::
- CHOICE: "Look for something specific"
  TARGET: louis_sees_something_else
  STATE_CHANGE: terror = +1
  CONDITION: null

::SCENE::
LOCATION: Louis
MOOD: Approaching Terror
CHARACTERS: Louis
BACKGROUND_IMAGE: louis_sees_something_else.png
BACKGROUND_EDIT: "Louis suddenly sees something"

::SCRIPT::
- CHARACTER: Narrator
  LINE: He suddenly sees something else, and now his fear is close to terror.
  EXPRESSION: Terror

::PATHS::
- CHOICE: "Look towards the deadfall"
  TARGET: the_deadfall_louis_pov
  STATE_CHANGE: terror = +2
  CONDITION: null

::SCENE::
LOCATION: The Deadfall, Louis's POV
MOOD: Visceral Terror, Primal
CHARACTERS: Narrator
BACKGROUND_IMAGE: the_deadfall_louis_pov.png
BACKGROUND_EDIT: "The face in the tumbled branches, yawning and snarling"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The face is back in the tumbled branches. It yawns and snarls.
  EXPRESSION: Primal

::PATHS::
- CHOICE: "Walk towards the deadfall"
  TARGET: louis_hypnotized
  STATE_CHANGE: hypnotized = +1
  CONDITION: null

::SCENE::
LOCATION: Louis
MOOD: Hypnotized, Terrified
CHARACTERS: Louis, Pascow
BACKGROUND_IMAGE: louis_hypnotized.png
BACKGROUND_EDIT: "Louis walking towards the deadfall, Pascow's hand on his shoulder"

::SCRIPT::
- CHARACTER: Narrator
  LINE: He walks toward the deadfall as if hypnotized. Pascow's hand falls on his shoulder. Louis turns, terrified.
  EXPRESSION: Terrified

::PATHS::
- CHOICE: "Turn to Pascow"
  TARGET: pascow_close_dreadful
  STATE_CHANGE: fear = +2
  CONDITION: null

::SCENE::
LOCATION: Pascow, Close
MOOD: Dreadful, Revelatory
CHARACTERS: Pascow
BACKGROUND_IMAGE: pascow_close_dreadful.png
BACKGROUND_EDIT: "Close-up of Pascow's mangled face"

::SCRIPT::
- CHARACTER: Narrator
  LINE: He really is a dreadful mangled mess.
  EXPRESSION: Dreadful
- CHARACTER: Pascow
  LINE: This is the place where the dead speak.
  EXPRESSION: Grave

::PATHS::
- CHOICE: "Acknowledge the place"
  TARGET: louis_closes_eyes
  STATE_CHANGE: understanding = +1
  CONDITION: null

::SCENE::
LOCATION: Louis
MOOD: Desperate to Wake
CHARACTERS: Louis
BACKGROUND_IMAGE: louis_closes_eyes.png
BACKGROUND_EDIT: "Louis closing his eyes, wanting to wake up"

::SCRIPT::
- CHARACTER: Narrator
  LINE: He closes his eyes.
  EXPRESSION: null
- CHARACTER: Louis
  LINE: I want to wake up. I want to wake up, that's all. I--
  EXPRESSION: Desperate

::PATHS::
- CHOICE: "Continue wishing to wake up"
  TARGET: louis_pas_combination
  STATE_CHANGE: desperation = +2
  CONDITION: null

::SCENE::
LOCATION: Louis and Pascow
MOOD: Warning, Supernatura
CHARACTERS: Pascow, Narrator
BACKGROUND_IMAGE: louis_pas_combination.png
BACKGROUND_EDIT: "Visual effects of red light and mist"

::SCRIPT::
- CHARACTER: Pascow
  LINE: The door must not be opened. The barrier must not be crossed. Don’t go on, doc. No matter how much you
  EXPRESSION: Warning
- CHARACTER: Narrator
  LINE: That grinning face--and perhaps now there are other effects as well, subtle but there? Dim red light? A misty smoke drifting through the tumbled dead branches? The director will know.
  EXPRESSION: Supernatural
- CHARACTER: Narrator
  LINE: After a moment there is a HUGE GRUNTING ROAR from the woods behind the deadfall--it sounds like no animal we've ever heard before.
  EXPRESSION: Primal
- CHARACTER: Narrator
  LINE: There is the sound of something huge shifting and snapping a tree like a toothpick.
  EXPRESSION: Destructive

::PATHS::
- CHOICE: "React to the sounds"
  TARGET: pascow_louis_crumpled
  STATE_CHANGE: terror = +3
  CONDITION: null

::SCENE::
LOCATION: Pascow and Louis
MOOD: Crushed, Defeated
CHARACTERS: Louis, Pascow
BACKGROUND_IMAGE: pascow_louis_crumpled.png
BACKGROUND_EDIT: "Louis crumpled at Pascow's feet, eyes shut tight"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Louis has crumbled to Pascow's feet. His eyes are squeezed tightly shut.
  EXPRESSION: Defeated
- CHARACTER: Louis
  LINE: Please, I want to wake up. Leave me alone. It's not my fault you died; you were as good as dead when they brought you in--
  EXPRESSION: Pleading
- CHARACTER: Pascow
  LINE: The power of this place is old and always restless. Sometimes the dead do more than speak. Remember, doc.
  EXPRESSION: Ominous

::PATHS::
- CHOICE: "Be filmed closely"
  TARGET: camera_moving_on_louis
  STATE_CHANGE: dread = +2
  CONDITION: null

::SCENE::
LOCATION: Camera Moving Slowly In On Louis
MOOD: Intense Focus, Desperation
CHARACTERS: Louis, Pascow
BACKGROUND_IMAGE: camera_moving_on_louis.png
BACKGROUND_EDIT: "Camera moving slowly in on Louis"

::SCRIPT::
- CHARACTER: Narrator
  LINE: CAMERA BEGINS MOVING SLOWLY IN ON LOUIS.
  EXPRESSION: null
- CHARACTER: Louis
  LINE: Leave me alone!
  EXPRESSION: Desperate
- CHARACTER: Pascow
  LINE: Remember.
  EXPRESSION: Whispering

::PATHS::
- CHOICE: "Hold the focus on Louis"
  TARGET: camera_tight_on_louis
  STATE_CHANGE: obsession = +2
  CONDITION: null

::SCENE::
LOCATION: Camera Is Tight On Louis
MOOD: Absolute Terror
CHARACTERS: Louis, Radio (Voice)
BACKGROUND_IMAGE: camera_tight_on_louis.png
BACKGROUND_EDIT: "Camera is tight on Louis's face"

::SCRIPT::
- CHARACTER: Narrator
  LINE: CAMERA IS TIGHT ON LOUIS.
  EXPRESSION: null
- CHARACTER: Radio (Voice)
  LINE: --another beautiful day in Maine! This is Michael O'Hara sayin' that the git-go ain't gonna be that bad. Temps are going all the way up to 70... We got the Ramones for Ludlow...here's "Sheena."
  EXPRESSION: Cheerful broadcast

::PATHS::
- CHOICE: "Wake up"
  TARGET: louis_in_bed_wakes
  STATE_CHANGE: relief = +2
  CONDITION: null

::SCENE::
LOCATION: Louis, In Bed
MOOD: Waking Confusion, Then Relief
CHARACTERS: Louis, Rachel (off-screen)
BACKGROUND_IMAGE: louis_in_bed_wakes.png
BACKGROUND_EDIT: "Louis in his own bedroom, sitting up"

::SCRIPT::
- CHARACTER: Narrator
  LINE: His eyes snap open. He's in his own bedroom. As he sits up the camera angle widens out so we can see that he's in bed alone; the covers on Rachel’s side are thrown back.
  EXPRESSION: Confused
- CHARACTER: Narrator
  LINE: After the initial confusion and fear, Louis looks deeply relieved; he looks the way I suppose we all look upon waking up and realizing our worst dreams were only dreams after all.
  EXPRESSION: Relieved
- CHARACTER: Rachel (calls)
  LINE: You up, doc?
  EXPRESSION: Off-screen
- CHARACTER: Louis
  LINE: Getting there.
  EXPRESSION: Groggily
- CHARACTER: Rachel
  LINE: I got eggs down here!
  EXPRESSION: Off-screen
- CHARACTER: Louis
  LINE: Good d--
  EXPRESSION: Startled
- CHARACTER: Narrator
  LINE: He throws the covers back and freezes.
  EXPRESSION: Frozen

::PATHS::
- CHOICE: "Look down at his feet"
  TARGET: louis_feet_louis_pov
  STATE_CHANGE: dawning_horror = +1
  CONDITION: null

::SCENE::
LOCATION: Louis's Feet, Louis's POV
MOOD: Utter Terror
CHARACTERS: Louis
BACKGROUND_IMAGE: louis_feet_louis_pov.png
BACKGROUND_EDIT: "Close-up on Louis's feet covered in mud and pine needles"

::SCRIPT::
- CHARACTER: Narrator
  LINE: They are covered with mud and pine needles. The sheets are greased with woods-muck.
  EXPRESSION: Horrified

::PATHS::
- CHOICE: "Examine himself further"
  TARGET: louis_cu_utter_terror
  STATE_CHANGE: terror = +3
  CONDITION: null

::SCENE::
LOCATION: Louis, CU
MOOD: Absolute Terror
CHARACTERS: Louis
BACKGROUND_IMAGE: louis_cu_utter_terror.png
BACKGROUND_EDIT: "Extreme close-up on Louis's face"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Utter terror.
  EXPRESSION: Absolute Terror

::PATHS::
- CHOICE: "Deal with the evidence"
  TARGET: laundry_chute_cu
  STATE_CHANGE: panic = +1
  CONDITION: null

::SCENE::
LOCATION: The Laundry Chute, CU
MOOD: Desperate Cleanup
CHARACTERS: Louis
BACKGROUND_IMAGE: laundry_chute_cu.png
BACKGROUND_EDIT: "Close-up of Louis's hands dumping sheets into the laundry chute"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Louis's hands enter the shot and dump a bundle of sheets into the chute.
  EXPRESSION: Desperate

::PATHS::
- CHOICE: "Go to the upstairs hall"
  TARGET: louis_upstairs_hall
  STATE_CHANGE: denial = +1
  CONDITION: null

::SCENE::
LOCATION: Louis, In the Upstairs Hall
MOOD: Attempting Normalcy
CHARACTERS: Louis
BACKGROUND_IMAGE: louis_upstairs_hall.png
BACKGROUND_EDIT: "Louis in the upstairs hall, wearing a towel"

::SCRIPT::
- CHARACTER: Narrator
  LINE: He's naked but for a towel around his waist. He's obviously fresh from the shower.
  EXPRESSION: Normalcy
- CHARACTER: Narrator
  LINE: He starts down to the bedroom to dress.
  EXPRESSION: null

::PATHS::
- CHOICE: "Black out and hear a phone ring"
  TARGET: black_out_phone_ring
  STATE_CHANGE: transition = +1
  CONDITION: null

::SCENE::
LOCATION: BLACK
MOOD: Suspenseful
CHARACTERS: Louis (voice)
BACKGROUND_IMAGE: black_screen.png
BACKGROUND_EDIT: "Black screen with title card 'CHURCH'"

::SCRIPT::
- CHARACTER: Narrator
  LINE: BLACK. And on it a third title card: CHURCH.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Over this the SOUND of a RINGING TELEPHONE.
  EXPRESSION: Ringing
- CHARACTER: Louis (voice)
  LINE: Hello?
  EXPRESSION: Questioning

::PATHS::
- CHOICE: "Answer the phone"
  TARGET: creed_living_room_afternoon
  STATE_CHANGE: anticipation = +1
  CONDITION: null

::SCENE::
LOCATION: The Creed Living Room
MOOD: Mundane, Disturbed
CHARACTERS: Louis, Jud (phone filter)
BACKGROUND_IMAGE: creed_living_room_afternoon.png
BACKGROUND_EDIT: "Living room with TV on, Louis on the phone"

::SCRIPT::
- CHARACTER: Narrator
  LINE: There's a bowling match on TV. Louis, dressed in his Saturday afternoon grubs (jeans and a Maine sweatshirt), has the phone to his ear.
  EXPRESSION: Casual
- CHARACTER: Iud Crandall (phone filter)
  LINE: Louis? 'Fraid you may have a spot of trouble.
  EXPRESSION: Concerned
- CHARACTER: Louis
  LINE: Jud? What trouble?
  EXPRESSION: Frowning

::PATHS::
- CHOICE: "Listen to Jud"
  TARGET: crandall_living_room_jud
  STATE_CHANGE: worry = +1
  CONDITION: null

::SCENE::
LOCATION: The Crandall Living Room, With Jud
MOOD: Concerned, Observant
CHARACTERS: Jud
BACKGROUND_IMAGE: crandall_living_room_jud.png
BACKGROUND_EDIT: "Jud on the phone, looking out his window"

::SCRIPT::
- CHARACTER: Narrator
  LINE: He's on the phone, looking out his window.
  EXPRESSION:null
- CHARACTER: Jud
  LINE: Did you tell me Rachel took the kids back to Chicago for a few days?
  EXPRESSION: Concerned

::PATHS::
- CHOICE: "Answer Jud's question"
  TARGET: creed_living_room_louis_jud
  STATE_CHANGE: confusion = +1
  CONDITION: null

::SCENE::
LOCATION: The Creed Living Room, With Louis
MOOD: Defensive, Confused
CHARACTERS: Louis
BACKGROUND_IMAGE: creed_living_room_louis_jud.png
BACKGROUND_EDIT: "Louis on the phone, looking confused"

::SCRIPT::
- CHARACTER: Louis
  LINE: For Ellie's birthday, yes. I didn't go because her old man thinks I'm a shit and the feeling is heartily reciprocated...they'll be back tomorrow night. Jud, what's this about?
  EXPRESSION: Defensive

::PATHS::
- CHOICE: "Press Jud for information"
  TARGET: crandall_living_room_jud_dead_cat
  STATE_CHANGE: urgency = +1
  CONDITION: null

::SCENE::
LOCATION: The Crandall Living Room, With Jud
MOOD: Grave, Foreboding
CHARACTERS: Jud
BACKGROUND_IMAGE: crandall_living_room_jud_dead_cat.png
BACKGROUND_EDIT: "Jud on the phone, looking grave"

::SCRIPT::
- CHARACTER: Jud
  LINE: Well, there's a dead cat over here on the edge of my lawn, Louis. I think it might be your daughter's.
  EXPRESSION: Grave

::PATHS::
- CHOICE: "React to the news"
  TARGET: creed_living_room_louis_church
  STATE_CHANGE: shock = +1
  CONDITION: null

::SCENE::
LOCATION: The Creed Living Room, With Louis
MOOD: Shocked, Distressed
CHARACTERS: Louis
BACKGROUND_IMAGE: creed_living_room_louis_church.png
BACKGROUND_EDIT: "Louis on the phone, reacting with shock"

::SCRIPT::
- CHARACTER: Louis
  LINE: Church? Oh. Oh, Jesus.
  EXPRESSION: Shocked

::PATHS::
- CHOICE: "Go to Jud's house"
  TARGET: crandall_house_medium_long
  STATE_CHANGE: dread = +1
  CONDITION: null

::SCENE::
LOCATION: The Crandall House, Medium-Long
MOOD: Cold, Somber
CHARACTERS: Louis, Jud
BACKGROUND_IMAGE: crandall_house_medium_long.png
BACKGROUND_EDIT: "Outside the Crandall house, cold and windy"

::SCRIPT::
- CHARACTER: Narrator
  LINE: We’re looking across from the Creed lawn. Louis waits for one of those trucks to go blasting by and then crosses. It's cold and windy. Downed autumn leaves fly.
  EXPRESSION: Somber
- CHARACTER: Narrator
  LINE: Louis and Jud stand over a small furry body like mourners.
  EXPRESSION: Mournful
- CHARACTER: Dud (voice)
  LINE: Well?
  EXPRESSION: Somber

::PATHS::
- CHOICE: "Examine the cat's body"
  TARGET: cat_body_exam
  STATE_CHANGE: grief = +1
  CONDITION: null

::SCENE::
LOCATION: The Cat's Body
MOOD: Disturbing, Unsettling
CHARACTERS: Louis
BACKGROUND_IMAGE: cat_body_exam.png
BACKGROUND_EDIT: "Close-up of the cat's body"

::SCRIPT::
- CHARACTER: Narrator
  LINE: It’s lying on its belly and doesn't look much damaged. Hands--Louis's--come into the frame. He puts one hand under the cat's head and lifts it so the open eyes, now a dull green, stare into the camera. There's some blood on its ruff. That's all.
  EXPRESSION: Unsettling

::PATHS::
- CHOICE: "Turn to Jud"
  TARGET: louis_jud_edge_lawn
  STATE_CHANGE: realization = +1
  CONDITION: null

::SCENE::
LOCATION: Louis and Dud, On the Edge of the Crandall Lawn
MOOD: Hesitant, Questioning
CHARACTERS: Louis
BACKGROUND_IMAGE: louis_jud_edge_lawn.png
BACKGROUND_EDIT: "Louis and Jud standing on the edge of the lawn"

::SCRIPT::
- CHARACTER: Louis
  LINE: (Staring at the cat)
  EXPRESSION: Hesitant

::PATHS::
- CHOICE: "Discuss the cat's condition"
  TARGET: end
  STATE_CHANGE: foreboding = +1
  CONDITION: null

::SCENE::
LOCATION: Church
MOOD: Somber
CHARACTERS: Dud, Louis
BACKGROUND_IMAGE: church.png
BACKGROUND_EDIT: "Interior of a church, somber atmosphere"

::SCRIPT::
- CHARACTER: Dud
  LINE: I’m sorry. At least it don’t look like he suffered.
  EXPRESSION: Sad
- CHARACTER: Louis
  LINE: Ellie will, though. She'll suffer plenty.
  EXPRESSION: Grim

::PATHS::
- CHOICE: "Continue with Louis"
  TARGET: kitchen
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Church - Outside
MOOD: Grim
CHARACTERS: Louis, Dud
BACKGROUND_IMAGE: church_outside.png
BACKGROUND_EDIT: "Outside a church, Louis and Dud are handling a body"

::SCRIPT::
- CHARACTER: Narrator
  LINE: From his jacket pocket he takes a green plastic garbage bag and hands it to DUD. DUD holds the bag's mouth open on the ground while LOUIS kind of shoves the body in.
  EXPRESSION: null
- CHARACTER: Dud
  LINE: Loved that cat pretty well, didn’t she?
  EXPRESSION: Questioning
- CHARACTER: Louis
  LINE: Yes.
  EXPRESSION: Neutral
- CHARACTER: Louis
  LINE: Bagged cat. What a mess.
  EXPRESSION: Resigned
- CHARACTER: Dud
  LINE: You going to bury him in the Pet Sematary?
  EXPRESSION: Questioning
- CHARACTER: Louis
  LINE: I guess that’s what it’s there for, huh?
  EXPRESSION: Bitter
- CHARACTER: Narrator
  LINE: During all of this DUD has grown peculiarly intense.
  EXPRESSION: null
- CHARACTER: Dud
  LINE: Going to tell Ellie?
  EXPRESSION: Intense
- CHARACTER: Louis
  LINE: I don't know.
  EXPRESSION: Uncertain
- CHARACTER: Dud
  LINE: Seems like you told me about a promise you made--
  EXPRESSION: Intense

::PATHS::
- CHOICE: "Proceed to the kitchen"
  TARGET: kitchen
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: The Creed Kitchen
MOOD: Uneasy
CHARACTERS: Gage, Ellie, Louis, Rachel
BACKGROUND_IMAGE: creed_kitchen.png
BACKGROUND_EDIT: "Morning in the Creed kitchen, a disturbing breakfast scene"

::SCRIPT::
- CHARACTER: Narrator
  LINE: GAGE is in his high chair. ELLIE, in her first-day-of-school dress, is in her place. LOUIS is sitting at his own place staring, hypnotized, at the middle of the table, where there is a large serving dish. On the dish is scrambled eggs, strips of bacon, and CHURCH’S corpse--staring eyes, bloody ruff and all.
  EXPRESSION: null
- CHARACTER: Rachel
  LINE: Don't shilly-shally, Louis. Give the little girl her promise.
  EXPRESSION: Impatient

::PATHS::
- CHOICE: "Discuss Rachel's past"
  TARGET: crandall_lawn
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: The Crandall Lawn
MOOD: Defensive, Somber
CHARACTERS: Louis, Dud
BACKGROUND_IMAGE: crandall_lawn.png
BACKGROUND_EDIT: "Exterior of the Crandall house, Louis and Dud are talking"

::SCRIPT::
- CHARACTER: Louis
  LINE: That was a mistake. But Rachel... she doesn't like to talk about death, or even think of it. Her younger sister died of spinal meningitis when Rachel was eight. Rachel was there when it happened. Alone. I guess you could say it made a complex.
  EXPRESSION: Defensive
- CHARACTER: Dud
  LINE: Cat's just as dead, Louis.
  EXPRESSION: Blunt
- CHARACTER: Louis
  LINE: Well that's a big help! I’m sorry, Dud.
  EXPRESSION: Snapping, then apologetic
- CHARACTER: Dud
  LINE: No need to apologize.
  EXPRESSION: Understanding
- CHARACTER: Louis
  LINE: Maybe when they call I’ll just tell Ellie I haven't seen the damn cat around. You know?
  EXPRESSION: Hesitant
- CHARACTER: Dud
  LINE: Maybe there’s a better way.
  EXPRESSION: Thoughtful

::PATHS::
- CHOICE: "Go to the Pet Sematary"
  TARGET: path_to_pet_sematary
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Path to the Pet Sematary
MOOD: Foreboding
CHARACTERS: Louis, Dud
BACKGROUND_IMAGE: path_to_pet_sematary.png
BACKGROUND_EDIT: "Early evening, road leading to the Pet Sematary, Louis and Dud walking"

::SCRIPT::
- CHARACTER: Narrator
  LINE: LOUIS and DUD cross the road from the CRANDALL side. LOUIS is carrying the plastic bag in one hand and a flashlight in the other. DUD has a pick and shovel in one hand and a flashlight of his own in the other. Evening shadows have grown long. It’s maybe an hour until dark.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: DUD and LOUIS stop near the replaced tire-swing.
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue towards the Pet Sematary"
  TARGET: louis_and_dud_walkman
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Louis and Dud
MOOD: Determined
CHARACTERS: Dud, Louis
BACKGROUND_IMAGE: louis_dud_walkman.png
BACKGROUND_EDIT: "Early evening, Dud has a Walkman and earphones"

::SCRIPT::
- CHARACTER: Narrator
  LINE: DUD has a Walkman clipped to the belt of his pants and earphones slung around his neck.
  EXPRESSION: null
- CHARACTER: Louis
  LINE: Dud, this is crazy. It's going to be almost dark before we get back.
  EXPRESSION: Anxious
- CHARACTER: Dud
  LINE: It's going to be dark before we even get where we’re going, Louis. But we can do it...and we're going to.
  EXPRESSION: Determined
- CHARACTER: Louis
  LINE: But --
  EXPRESSION: Hesitant
- CHARACTER: Dud
  LINE: Does she love the cat?
  EXPRESSION: Questioning
- CHARACTER: Louis
  LINE: Yes, but--
  EXPRESSION: Yielding
- CHARACTER: Dud
  LINE: Then come on.
  EXPRESSION: Insistent
- CHARACTER: Narrator
  LINE: He puts the earphones on, effectively forestalling further argument, and pushes the PLAY button on the Walkman. We can hear Marshall Crenshaw singing "Crystal Girl." DUD starts away. After a moment, LOUIS follows.
  EXPRESSION: null

::PATHS::
- CHOICE: "Follow Dud"
  TARGET: pet_sematary_arch
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: The Pet Sematary and the Back of the Arch
MOOD: Eerie
CHARACTERS: Louis, Dud
BACKGROUND_IMAGE: pet_sematary_arch.png
BACKGROUND_EDIT: "Late evening, the Pet Sematary, twilight setting in"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The SOUND of crickets...ree-ree-ree...The SOUND of footfalls. Faintly, the SOUND of Huey Lewis and the News, singing "Working For A Living." It's now almost twilight.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: JUD and LOUIS enter the Pet Sematary. LOUIS is looking around curiously.
  EXPRESSION: null
- CHARACTER: Louis
  LINE: Well, folks, here we are, in Louis Creed Dreamland.
  EXPRESSION: Sarcastic
- CHARACTER: Dud
  LINE: What say, Louis?
  EXPRESSION: Questioning
- CHARACTER: Louis
  LINE: Nothing. Do we plant him on the outer circle or start a new one?
  EXPRESSION: Questioning
- CHARACTER: Dud
  LINE: We're still not where we’re going.
  EXPRESSION: Direct
- CHARACTER: Narrator
  LINE: He walks past LOUIS and toward the deadfall. LOUIS follows.
  EXPRESSION: null
- CHARACTER: Louis
  LINE: What do you mean?
  EXPRESSION: Confused
- CHARACTER: Dud
  LINE: The place we’re going is on the other side of that.
  EXPRESSION: Direct
- CHARACTER: Narrator
  LINE: He points at the deadfall.
  EXPRESSION: null
- CHARACTER: Louis
  LINE: We can't climb over that. We'll break our necks!
  EXPRESSION: Fearful
- CHARACTER: Dud
  LINE: No. We won't. I have climbed it a time or two before, and I know all the places to step. Just follow me...move easy...don't look down...and don't stop. If you stop, you'll crash through for sure.
  EXPRESSION: Authoritative
- CHARACTER: Louis
  LINE: I'm not climbing that.
  EXPRESSION: Refusal
- CHARACTER: Dud
  LINE: Give me the cat. I'll take care of it myself.
  EXPRESSION: Determined
- CHARACTER: Narrator
  LINE: He holds out his hand and LOUIS sees the old man means exactly as he says. After a moment he says:
  EXPRESSION: null
- CHARACTER: Louis
  LINE: Let's go.
  EXPRESSION: Resigned

::PATHS::
- CHOICE: "Attempt to climb the deadfall"
  TARGET: louis_and_dud_climbing
  STATE_CHANGE: fear = +1
  CONDITION: null

::SCENE::
LOCATION: Louis and Dud Climbing
MOOD: Tense, Adventurous
CHARACTERS: Dud, Louis
BACKGROUND_IMAGE: louis_dud_climbing.png
BACKGROUND_EDIT: "Twilight, Louis and Dud are climbing a large deadfall"

::SCRIPT::
- CHARACTER: Narrator
  LINE: JUD starts up one side of the deadfall, and in spite of its snarled tangles, he mounts as easily as a man climbing a flight of stairs. After a few second, LOUIS follows.
  EXPRESSION: null
- CHARACTER: Louis
  LINE: Thank God my Blue Cross is paid up.
  EXPRESSION: Nervous joke

::PATHS::
- CHOICE: "Continue climbing"
  TARGET: their_feet_climbing
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Their Feet
MOOD: Focused
CHARACTERS: Dud, Louis
BACKGROUND_IMAGE: their_feet_climbing.png
BACKGROUND_EDIT: "Close-up of feet navigating the deadfall"

::SCRIPT::
- CHARACTER: Narrator
  LINE: First JUD'S pass THE CAMERA, then LOUIS'S, partly obscured by the swinging cat-bag. Their feet unerringly find the right branches and just as unerringly miss holes which look like ankle-breakers.
  EXPRESSION: null

::PATHS::
- CHOICE: "Observe Louis's progress"
  TARGET: louis_climbing_exhilarated
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Louis
MOOD: Exhilarated
CHARACTERS: Louis
BACKGROUND_IMAGE: louis_climbing_exhilarated.png
BACKGROUND_EDIT: "Louis is climbing the deadfall, looking exhilarated"

::SCRIPT::
- CHARACTER: Louis
  LINE: God, this is amazing!
  EXPRESSION: Amazed, Exhilarated

::PATHS::
- CHOICE: "Observe Dud's progress"
  TARGET: jud_climbing_intense
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Jud
MOOD: Intense, Scared
CHARACTERS: Dud
BACKGROUND_IMAGE: jud_climbing_intense.png
BACKGROUND_EDIT: "Dud is climbing the deadfall, showing signs of strain"

::SCRIPT::
- CHARACTER: Dud
  LINE: Just don't stop and--
  EXPRESSION: Stern, Scared

::PATHS::
- CHOICE: "Observe Louis looking down"
  TARGET: louis_looking_down
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Louis
MOOD: Reckless
CHARACTERS: Louis
BACKGROUND_IMAGE: louis_looking_down.png
BACKGROUND_EDIT: "Louis is looking down while climbing the deadfall"

::SCRIPT::
- CHARACTER: Narrator
  LINE: He looks down.
  EXPRESSION: null

::PATHS::
- CHOICE: "Observe Louis's feet"
  TARGET: louis_feet_slipping
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Louis's Feet
MOOD: Critical
CHARACTERS: Louis
BACKGROUND_IMAGE: louis_feet_slipping.png
BACKGROUND_EDIT: "Close-up of Louis's foot on a dead branch"

::SCRIPT::
- CHARACTER: Narrator
  LINE: A dead branch snaps under one of them like a gunshot and that foot plunges down maybe six inches.
  EXPRESSION: null

::PATHS::
- CHOICE: "Observe Louis regaining balance"
  TARGET: louis_lurching
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Louis
MOOD: Recovering
CHARACTERS: Louis
BACKGROUND_IMAGE: louis_lurching.png
BACKGROUND_EDIT: "Louis lurches to regain balance on the deadfall"

::SCRIPT::
- CHARACTER: Narrator
  LINE: He lurches to the edge of balance, then regains it.
  EXPRESSION: null
- CHARACTER: Louis
  LINE: And don't look down. Right.
  EXPRESSION: Self-admonishing
- CHARACTER: Narrator
  LINE: He continues.
  EXPRESSION: null

::PATHS::
- CHOICE: "Observe the deadfall reverse view"
  TARGET: deadfall_reverse_twilight
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: The Deadfall, Reverse
MOOD: Transition
CHARACTERS: Dud, Louis
BACKGROUND_IMAGE: deadfall_reverse_twilight.png
BACKGROUND_EDIT: "Twilight, view from the far side of the deadfall"

::SCRIPT::
- CHARACTER: Narrator
  LINE: JUD reaches the top and starts down the far side. LOUIS reaches the top.
  EXPRESSION: null

::PATHS::
- CHOICE: "Observe Louis's amazement"
  TARGET: louis_amazed_deadfall
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Louis
MOOD: Astonished
CHARACTERS: Louis
BACKGROUND_IMAGE: louis_amazed_deadfall.png
BACKGROUND_EDIT: "Louis is at the top of the deadfall, looking amazed"

::SCRIPT::
- CHARACTER: Louis
  LINE: Holy...!
  EXPRESSION: Astonished

::PATHS::
- CHOICE: "Show Louis's POV"
  TARGET: big_god_woods_pov
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Big God Woods, Louis's POV
MOOD: Majestic, Awe-inspiring
CHARACTERS: Louis
BACKGROUND_IMAGE: big_god_woods_pov.png
BACKGROUND_EDIT: "Twilight view of an ancient, majestic forest"

::SCRIPT::
- CHARACTER: Narrator
  LINE: In the dying glow of twilight, this should be a mystic, awe-inspiring shot. There’s no more scrub underbrush and junk pines and juniper-bracken here; ancient firs rise almost like Sequoias. The sunset light shafts among them. This is a real forest... an old forest. And winding upward among the trees along that needle-carpeted floor, clearly marked by large white stones, the path goes on.
  EXPRESSION: null

::PATHS::
- CHOICE: "Observe Louis on the deadfall"
  TARGET: louis_atop_deadfall
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Louis, Atop the Deadfall
MOOD: Amazed
CHARACTERS: Louis
BACKGROUND_IMAGE: louis_atop_deadfall.png
BACKGROUND_EDIT: "Louis stands atop the deadfall, surveying the forest"

::SCRIPT::
- CHARACTER: Narrator
  LINE: He's stopped on top of the deadfall, still surveying all this with frank amazement.
  EXPRESSION: null

::PATHS::
- CHOICE: "Observe Dud calling Louis"
  TARGET: jud_calling_louis
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Jud
MOOD: Urgent
CHARACTERS: Dud
BACKGROUND_IMAGE: jud_calling_louis.png
BACKGROUND_EDIT: "Dud looks back at Louis, urging him on"

::SCRIPT::
- CHARACTER: Dud
  LINE: Come on, Louis--don't stop!
  EXPRESSION: Urgent

::PATHS::
- CHOICE: "Observe Louis grinning"
  TARGET: louis_grinning_deadfall
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Louis, Atop the Deadfall
MOOD: Confident
CHARACTERS: Louis
BACKGROUND_IMAGE: louis_grinning_deadfall.png
BACKGROUND_EDIT: "Louis is grinning at the top of the deadfall"

::SCRIPT::
- CHARACTER: Louis
  LINE: I'm all right! I'm f—
  EXPRESSION: Confident, then interrupted

::PATHS::
- CHOICE: "Observe Louis's feet slipping"
  TARGET: louis_feet_snap_branch
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Louis's Feet
MOOD: Precarious
CHARACTERS: Louis
BACKGROUND_IMAGE: louis_feet_snap_branch.png
BACKGROUND_EDIT: "A branch snaps under Louis's foot on the deadfall"

::SCRIPT::
- CHARACTER: Narrator
  LINE: One of the branches snaps. LOUIS'S foot plunges. His cuff rips.
  EXPRESSION: null

::PATHS::
- CHOICE: "Observe Louis falling"
  TARGET: louis_falling
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Louis, Jud's POV
MOOD: Falling
CHARACTERS: Louis
BACKGROUND_IMAGE: louis_falling.png
BACKGROUND_EDIT: "Louis loses his balance and falls from the deadfall"

::SCRIPT::
- CHARACTER: Narrator
  LINE: We’re looking up at a fairly steep angle as LOUIS staggers off-balance. He steps with his other foot, misses, and goes flying.
  EXPRESSION: null

::PATHS::
- CHOICE: "Observe Louis hitting the deadfall"
  TARGET: louis_hitting_deadfall
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Louis, Closer
MOOD: Impact
CHARACTERS: Louis
BACKGROUND_IMAGE: louis_hitting_deadfall.png
BACKGROUND_EDIT: "Louis lands heavily on the deadfall"

::SCRIPT::
- CHARACTER: Narrator
  LINE: He does a half-somersault in the air and hits the deadfall on his back, the green garbage bag flying out of his hand. His flashlight also goes. Branches crack. White dust puffs out from under him.
  EXPRESSION: null

::PATHS::
- CHOICE: "Observe Dud's reaction"
  TARGET: dud_at_base_deadfall
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Dud, At the Base of the Deadfall
MOOD: Concerned
CHARACTERS: Dud, Louis
BACKGROUND_IMAGE: dud_at_base_deadfall.png
BACKGROUND_EDIT: "Dud rushes to Louis after his fall"

::SCRIPT::
- CHARACTER: Narrator
  LINE: LOUIS thumps to the ground nearby. DUD kneels beside him.
  EXPRESSION: null
- CHARACTER: Dud
  LINE: Louis! You all right?
  EXPRESSION: Concerned
- CHARACTER: Narrator
  LINE: LOUIS sits up groggily. His pants are torn. His sweatshirt is torn. His ankle is bleeding.
  EXPRESSION: null
- CHARACTER: Louis
  LINE: Sure. I guess I just lost my happy thoughts for a second there.
  EXPRESSION: Dazed, Trying to be brave
- CHARACTER: Narrator
  LINE: LOUIS gets slowly up and retrieves the bag, which is rather shredded now--and we can see catfur through some of the rents.
  EXPRESSION: null
- CHARACTER: Louis
  LINE: I shouldn't have stopped...and it does bite.
  EXPRESSION: Grim
- CHARACTER: Narrator
  LINE: He whaps the flashlight against his palm a time or two and the light comes on. Satisfied, he shuts it off.
  EXPRESSION: null
- CHARACTER: Dud
  LINE: No, you shouldn't have stopped. But you got away with it. Important thing is are you sure you're all right?
  EXPRESSION: Reassuring
- CHARACTER: Louis
  LINE: Yes. Where are we going, Dud?
  EXPRESSION: Resigned
- CHARACTER: Dud
  LINE: You'll see before long. Let’s go.
  EXPRESSION: Mysterious
- CHARACTER: Narrator
  LINE: He starts off up the path. After a moment LOUIS follows, carrying the bag.
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue following Dud"
  TARGET: louis_dud_from_deadfall
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Louis and Dud, From the Deadfall
MOOD: Mysterious, Awe-inspiring
CHARACTERS: Louis, Dud
BACKGROUND_IMAGE: louis_dud_from_deadfall.png
BACKGROUND_EDIT: "Louis and Dud walk into the twilight woods"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Again, there should be a sense of awe and mystery as they go tolling up the path into the twilight, dwarfed by those ancient firs.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: SOUND OF CRICKETS, LOW at first, then UP TO LOUD: Ree-ree-ree...
  EXPRESSION: null

::PATHS::
- CHOICE: "Dissolve to Little God Swamp"
  TARGET: little_god_swamp_builights
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Louis and Dud, At the Edge of Little God Swamp
MOOD: Eerie, Mist-shrouded
CHARACTERS: Louis, Dud
BACKGROUND_IMAGE: little_god_swamp_builights.png
BACKGROUND_EDIT: "Twilight at the edge of a swamp, fog and mist"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Lots of undergrowth here, and creeping ground-mist, too. The SOUND OF CRICKETS is now only a part of the soundtrack: BUZZ OF CICADAS, THUMP OF FROGS. Swamp-sounds.
  EXPRESSION: null
- CHARACTER: Louis
  LINE: This next bit's like the deadfall, Louis-- you got to walk steady and easy. Dust follow me and don't look down.
  EXPRESSION: Doubtful

::PATHS::
- CHOICE: "Enter the swamp"
  TARGET: little_god_swamp_pov
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Little God Swamp, Louis's and Dud's POV
MOOD: Mysterious, Awesome, Scary
CHARACTERS: Louis, Dud
BACKGROUND_IMAGE: little_god_swamp_pov.png
BACKGROUND_EDIT: "Deep twilight view of a scary, overgrown swamp"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Mysterious...awesome...scary. Dead trees poke out of the murk like twisted hands. There's scummy water standing around tussocks covered with long grass, most of it dead. There's a lot of choking underbrush. All of this fades away into a grim, obscuring fog.
  EXPRESSION: null

::PATHS::
- CHOICE: "Observe Louis and Dud in the swamp"
  TARGET: louis_dud_swamp
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Louis and Dud
MOOD: Foreboding
CHARACTERS: Louis, Dud
BACKGROUND_IMAGE: louis_dud_swamp.png
BACKGROUND_EDIT: "Louis and Dud are in the swamp, Dud speaks"

::SCRIPT::
- CHARACTER: Dud
  LINE: Micmacs used to call it Little God Swamp.
  EXPRESSION: Informative
- CHARACTER: Louis
  LINE: Is there quicksand?
  EXPRESSION: Nervous, Joking
- CHARACTER: Dud
  LINE: Ayuh.
  EXPRESSION: Affirmative
- CHARACTER: Louis
  LINE: Are there ghosts?
  EXPRESSION: Nervous, Joking
- CHARACTER: Dud
  LINE: Ayuh.
  EXPRESSION: Affirmative
- CHARACTER: Narrator
  LINE: DUD starts off, stepping to the first tussock. After a moment, LOUIS follows.
  EXPRESSION: null

::PATHS::
- CHOICE: "Follow Dud"
  TARGET: dud_close_up_face
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Dud, CU
MOOD: Intense, Strange
CHARACTERS: Dud
BACKGROUND_IMAGE: dud_close_up_face.png
BACKGROUND_EDIT: "Close-up on Dud's face, set and strange"

::SCRIPT::
- CHARACTER: Dud
  LINE: There's a lot of funny things down this way, Louis.
  EXPRESSION: Intense, Foreboding

::PATHS::
- CHOICE: "Observe Louis behind Dud"
  TARGET: louis_behind_dud
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Louis, Behind Dud
MOOD: Apprehensive
CHARACTERS: Louis
BACKGROUND_IMAGE: louis_behind_dud.png
BACKGROUND_EDIT: "Louis follows Dud, looking apprehensive"

::SCRIPT::
- CHARACTER: Louis
  LINE: You're telling me.
  EXPRESSION: Apprehensive

::PATHS::
- CHOICE: "Observe Dud"
  TARGET: dud_speaking
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Dud
MOOD: Mysterious
CHARACTERS: Dud
BACKGROUND_IMAGE: dud_speaking.png
BACKGROUND_EDIT: "Dud speaks, his expression unreadable"

::SCRIPT::
- CHARACTER: Dud
  LINE: (
  EXPRESSION: null

::PATHS::
- CHOICE: "End of excerpt"
  TARGET: end
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Louis, POV - Swamp Path
MOOD: Eerie
CHARACTERS: Narrator, Louis
BACKGROUND_IMAGE: swamp_path.png
BACKGROUND_EDIT: "Night, heavy mist, air feels charged"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The air's heavier...more electrical... something. You might see St. Elmo’s Fire...what the sailors call 'foo-lights.' It makes funny shapes, but it's nothing.
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue walking"
  TARGET: louis_swamp_pov
  STATE_CHANGE: fear = +1
  CONDITION: null

::SCENE::
LOCATION: Little Goo Swamp, Louis's POV
MOOD: Unsettling
CHARACTERS: Narrator, Louis
BACKGROUND_IMAGE: little_goo_swamp.png
BACKGROUND_EDIT: "Faintly glowing, ethereal shape in dead tree branches, resembling Pascow's corpse"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Louis looks up and his eyes widen as he sees:
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: A faintly glowing, ethereal shape hangs in the branches of one of the dead trees. It looks a bit like a corpse. In fact, I think it looks quite a bit like PASCOW'S corpse.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: As we watch it fades...fades... is gone.
  EXPRESSION: null

::PATHS::
- CHOICE: "Observe the fading light"
  TARGET: louis_swamp
  STATE_CHANGE: fear = +2
  CONDITION: null

::SCENE::
LOCATION: Louis, Swamp
MOOD: Mystified and Scared
CHARACTERS: Narrator, Louis
BACKGROUND_IMAGE: louis_swamp.png
BACKGROUND_EDIT: "Glowing fireball rolling across standing water towards Louis, then fading into mist"

::SCRIPT::
- CHARACTER: Narrator
  LINE: He's somewhere between being mystified and puzzled and being scared. Now a weakly glowing fireball rolls slowly across the surface of the standing water toward him...and then just fades into the thick mist.
  EXPRESSION: null
- CHARACTER: Louis
  LINE: It's funny, all right.
  EXPRESSION: Puzzled

::PATHS::
- CHOICE: "Acknowledge the strangeness"
  TARGET: dud_swamp
  STATE_CHANGE: curiosity = +1
  CONDITION: null

::SCENE::
LOCATION: Dud, Swamp Path
MOOD: Cautionary
CHARACTERS: Narrator, Dud, Louis
BACKGROUND_IMAGE: dud_swamp_path.png
BACKGROUND_EDIT: "Night, thick mist, Louis and Jud walking"

::SCRIPT::
- CHARACTER: Dud
  LINE: Just don't stop, Louis. You don't ever want to stop down here in Little God.
  EXPRESSION: Serious
- CHARACTER: Dud
  LINE: And you don’t ever want to look behind you, whatever you hear.
  EXPRESSION: Stern

::PATHS::
- CHOICE: "Heed Jud's warning"
  TARGET: jud_louis_long_angle
  STATE_CHANGE: caution = +2
  CONDITION: null

::SCENE::
LOCATION: Jud and Louis, Long Angle - Swamp
MOOD: Spectral
CHARACTERS: Narrator, Jud, Louis
BACKGROUND_IMAGE: jud_louis_swamp.png
BACKGROUND_EDIT: "Night, mist, Jud and Louis moving like wraiths, swamp dimly glowing"

::SCRIPT::
- CHARACTER: Narrator
  LINE: We see them moving through the mist like wraiths, Jud with his digging tools, Louis with his light and his Hefty-Bag coffin. The whole swamp is glowing dimly.
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue through the swamp"
  TARGET: far_side_swamp
  STATE_CHANGE: dread = +1
  CONDITION: null

::SCENE::
LOCATION: The Far Side of Little God Swamp
MOOD: Transition
CHARACTERS: Narrator, Jud, Louis
BACKGROUND_IMAGE: far_side_swamp.png
BACKGROUND_EDIT: "Night, emerging from swamp onto firm ground, entering woods"

::SCRIPT::
- CHARACTER: Narrator
  LINE: In the extreme f.g. we can see firm ground sloping up. Ahead is a thick white mist. And here comes Jud and Louis slogging through it and out of it. Both of them are wet from the knees down. They head into the woods on the far side.
  EXPRESSION: null

::PATHS::
- CHOICE: "Enter the woods"
  TARGET: stony_bluff
  STATE_CHANGE: weariness = +1
  CONDITION: null

::SCENE::
LOCATION: A Low, Stony Bluff or Steep Hill
MOOD: Ascending
CHARACTERS: Narrator, Louis, Jud
BACKGROUND_IMAGE: stony_bluff.png
BACKGROUND_EDIT: "Night, rocky hill with steps cut into the side, Louis and Jud climbing"

::SCRIPT::
- CHARACTER: Narrator
  LINE: In the book this is described as being almost a cliff, but a rocky hill rising out of the woods would serve just as well. We can see steps cut into the side, and two figures--Louis and Jud--toiling up them.
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue climbing"
  TARGET: jud_louis_closer
  STATE_CHANGE: exhaustion = +1
  CONDITION: null

::SCENE::
LOCATION: Jud and Louis, Closer Shot
MOOD: Exhausted
CHARACTERS: Narrator, Jud, Louis
BACKGROUND_IMAGE: jud_louis_closer.png
BACKGROUND_EDIT: "Night, rocky summit, stars, wind blowing"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Jud's panting and out of breath; Louis is, if anything, in worse shape.
  EXPRESSION: null
- CHARACTER: Jud
  LINE: Almost there, Louis.
  EXPRESSION: Panting
- CHARACTER: Louis
  LINE: You keep saying that.
  EXPRESSION: Weary
- CHARACTER: Jud
  LINE: This time I mean it.
  EXPRESSION: Determined
- CHARACTER: Narrator
  LINE: He tops the last step and stands on a rocky level under the stars, the wind blowing his hair off his deeply lined brow. A few moments later Louis joins him and stares with undisguised wonder.
  EXPRESSION: null

::PATHS::
- CHOICE: "Reach the summit"
  TARGET: micmac_burying_ground_pov
  STATE_CHANGE: awe = +1
  CONDITION: null

::SCENE::
LOCATION: The Micmac Burying Ground, Louis and Jud's POV
MOOD: Ancient and Sacred
CHARACTERS: Narrator, Louis, Jud
BACKGROUND_IMAGE: micmac_burying_ground_pov.png
BACKGROUND_EDIT: "Night, rocky and bare hilltop, piles of rocks, concentric circles"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The top of this hill or bluff is rocky and bare, but there are a number of rocky piles. But for every pile of rocks we can see, there are ten littered heaps, as if the neat piles had been burst apart. There's a shape to all of this, and it is the shape of the Pet Sematary: concentric circles.
  EXPRESSION: null
- SOUND: The wind, blowing ceaselessly.
  EXPRESSION: null

::PATHS::
- CHOICE: "Observe the burying ground"
  TARGET: louis_jud_edge
  STATE_CHANGE: wonder = +2
  CONDITION: null

::SCENE::
LOCATION: Louis and Jud, At the Edge of the Burying Ground
MOOD: Questioning and Somber
CHARACTERS: Narrator, Louis, Jud
BACKGROUND_IMAGE: louis_jud_edge.png
BACKGROUND_EDIT: "Night, edge of the burying ground, Louis and Jud looking around"

::SCRIPT::
- CHARACTER: Louis
  LINE: What is this place?
  EXPRESSION: Awed
- CHARACTER: Jud
  LINE: This was their burying ground, Louis.
  EXPRESSION: Solemn
- CHARACTER: Louis
  LINE: Whose burying ground?
  EXPRESSION: Confused
- CHARACTER: Jud
  LINE: The Micmac Indians. I brought you here to bury Ellen's cat.
  EXPRESSION: Resigned
- CHARACTER: Louis
  LINE: Why? For God’s sake, why?
  EXPRESSION: Incredulous
- CHARACTER: Jud
  LINE: I had my reasons, Louis. We’ll talk later. All right?
  EXPRESSION: Evasive
- CHARACTER: Louis
  LINE: I guess so... but...
  EXPRESSION: Hesitant
- CHARACTER: Jud
  LINE: You want to rest a bit before you start?
  EXPRESSION: Offering
- CHARACTER: Louis
  LINE: No, I’m okay. Will I really be able to dig him a grave? The soil looks thin.
  EXPRESSION: Concerned
- CHARACTER: Jud
  LINE: Soil's thin, all right. But you’ll manage.
  EXPRESSION: Encouraging
- CHARACTER: Narrator
  LINE: He hands him the pick and shovel.
  EXPRESSION: null
- CHARACTER: Jud
  LINE: I'm going to sit over yonder and have a smoke. I’d help you, but you’ve got to do it yourself. Each buries his own. That’s how it was done then.
  EXPRESSION: Firm
- CHARACTER: Narrator
  LINE: Jud walks away, leaving Louis with the digging tools in one hand and the flashlight in the other. After a minute, Louis walks out into the burying ground.
  EXPRESSION: null

::PATHS::
- CHOICE: "Begin digging"
  TARGET: shallow_hole
  STATE_CHANGE: determination = +1
  CONDITION: null

::SCENE::
LOCATION: Looking Down Into a Shallow Hole
MOOD: Difficult Work
CHARACTERS: Narrator, Louis
BACKGROUND_IMAGE: shallow_hole.png
BACKGROUND_EDIT: "Night, shallow grave being dug, rocky soil, pickaxe striking rock"

::SCRIPT::
- SOUND: The wind. It blows ceaselessly up here.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The hole’s about two and a half feet deep. Stubby rocks protrude from the sides. The pick comes down, hits a rock at the bottom, and flashes fire.
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue digging"
  TARGET: louis_dirt_pile
  STATE_CHANGE: frustration = +1
  CONDITION: null

::SCENE::
LOCATION: Louis, Dirt Pile
MOOD: Accomplished, then Curious
CHARACTERS: Narrator, Louis, Jud
BACKGROUND_IMAGE: louis_dirt_pile.png
BACKGROUND_EDIT: "Night, Louis beside shallow grave with pile of rocks and earth, Jud approaches with rocks"

::SCRIPT::
- CHARACTER: Narrator
  LINE: He drops the pick and sticks his hurt hands in his armpits. Beside him we see a low pile of rocks and earth.
  EXPRESSION: null
- CHARACTER: Jud (VOICE)
  LINE: Should be deep enough.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: He joins Louis. He's got a lot of rocks in his arms.
  EXPRESSION: null
- CHARACTER: Louis
  LINE: You think so?
  EXPRESSION: Skeptical
- CHARACTER: Narrator
  LINE: He notices the rocks.
  EXPRESSION: null
- CHARACTER: Louis
  LINE: What are those for?
  EXPRESSION: Inquisitive
- CHARACTER: Jud
  LINE: Your cairn.
  EXPRESSION: Matter-of-fact

::PATHS::
- CHOICE: "Ask about the cairn"
  TARGET: micmac_burying_ground_louis_pov
  STATE_CHANGE: curiosity = +2
  CONDITION: null

::SCENE::
LOCATION: The Micmac Burying Ground, Louis's POV
MOOD: Observational
CHARACTERS: Narrator, Louis
BACKGROUND_IMAGE: micmac_burying_ground_louis_pov_cairn.png
BACKGROUND_EDIT: "Night, Louis observing the tumbled piles of rock"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Those tumbled piles of rock are very obvious.
  EXPRESSION: null

::PATHS::
- CHOICE: "Examine the cairn"
  TARGET: louis_jud_church_grave
  STATE_CHANGE: observation = +1
  CONDITION: null

::SCENE::
LOCATION: Louis and Jud, By Church's Grave
MOOD: Reflective
CHARACTERS: Narrator, Louis, Jud
BACKGROUND_IMAGE: louis_jud_church_grave.png
BACKGROUND_EDIT: "Night, beside the shallow grave, Louis and Jud stand together"

::SCRIPT::
- CHARACTER: Louis
  LINE: Doesn't look like they last long.
  EXPRESSION: Doubtful
- CHARACTER: Jud
  LINE: Don’t worry about that.
  EXPRESSION: Reassuring
- CHARACTER: Louis
  LINE: Jud, why am I doing all this?
  EXPRESSION: Questioning
- CHARACTER: Jud
  LINE: Because it's right.
  EXPRESSION: Adamant
- CHARACTER: Narrator
  LINE: He walks off again. Louis looks after him for a moment, then kneels down.
  EXPRESSION: null

::PATHS::
- CHOICE: "Kneel by the grave"
  TARGET: louis_garbage_bag
  STATE_CHANGE: contemplation = +1
  CONDITION: null

::SCENE::
LOCATION: Louis, By the Garbage Bag
MOOD: Sadness and Affection
CHARACTERS: Narrator, Louis
BACKGROUND_IMAGE: louis_garbage_bag.png
BACKGROUND_EDIT: "Night, Louis opens Hefty bag, looking at Church's corpse"

::SCRIPT::
- CHARACTER: Narrator
  LINE: He opens it and looks in at Church’s stiffening corpse.
  EXPRESSION: null
- CHARACTER: Louis
  LINE: Pax vobiscum, Church old buddy. You were a hell of a god cat. I doubt if you were worth all this aggravation, but you were a hell of a good cat.
  EXPRESSION: Affectionate
- CHARACTER: Narrator
  LINE: He tumbles the bag containing the body into the grave, and then begins pushing the stony soil over it with the spade.
  EXPRESSION: null

::PATHS::
- CHOICE: "Bury Church"
  TARGET: cairn_cu
  STATE_CHANGE: grief = +1
  CONDITION: null

::SCENE::
LOCATION: The Cairn, Close Up
MOOD: Finality
CHARACTERS: Narrator, Louis
BACKGROUND_IMAGE: cairn_cu.png
BACKGROUND_EDIT: "Night, Louis's hands placing the final stones on the cairn"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Louis's hands come into the frame and add a final two or three stones.
  EXPRESSION: null

::PATHS::
- CHOICE: "Complete the cairn"
  TARGET: louis_by_cairn
  STATE_CHANGE: closure = +1
  CONDITION: null

::SCENE::
LOCATION: Louis, By the Cairn
MOOD: Weary Accomplishment
CHARACTERS: Narrator, Louis, Jud
BACKGROUND_IMAGE: louis_by_cairn.png
BACKGROUND_EDIT: "Night, Louis stands by the completed cairn, Jud approaches"

::SCRIPT::
- CHARACTER: Narrator
  LINE: He looks at it for a moment and stands up. Jud is right there.
  EXPRESSION: null
- CHARACTER: Jud
  LINE: That's fine. You did real good.
  EXPRESSION: Approving
- CHARACTER: Narrator
  LINE: Louis looks at him.
  EXPRESSION: null

::PATHS::
- CHOICE: "Acknowledge Jud's approval"
  TARGET: creed_house_night
  STATE_CHANGE: relief = +1
  CONDITION: null

::SCENE::
LOCATION: The Creed House
MOOD: Foreboding
CHARACTERS: Narrator
BACKGROUND_IMAGE: creed_house_night.png
BACKGROUND_EDIT: "Night, house with light on in the kitchen, silence, then phone rings"

::SCRIPT::
- CHARACTER: Narrator
  LINE: There's a light on in the kitchen, but that's all. There’s silence at first, and then the PHONE STARTS RINGING.
  EXPRESSION: null

::PATHS::
- CHOICE: "Hear the phone ring"
  TARGET: louis_iud_path
  STATE_CHANGE: anxiety = +1
  CONDITION: null

::SCENE::
LOCATION: Louis's Field
MOOD: Urgent
CHARACTERS: Narrator, Louis, Jud
BACKGROUND_IMAGE: louis_field.png
BACKGROUND_EDIT: "Night, Louis and Jud walking back from swamp, tools in hand, phone heard faintly"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Louis and Jud are coming down the path with their tools and their lights. They are both clearly fagged out.
  EXPRESSION: null
- SOUND, FAINT: The telephone.
  EXPRESSION: null
- CHARACTER: Louis
  LINE: Oh, shit! Rachel!
  EXPRESSION: Panicked
- CHARACTER: Narrator
  LINE: He drops the tools and sprints.
  EXPRESSION: null

::PATHS::
- CHOICE: "Sprint towards the house"
  TARGET: creed_side_yard
  STATE_CHANGE: urgency = +2
  CONDITION: null

::SCENE::
LOCATION: The Creed's Side Yard, By the Tire Swing
MOOD: Frantic
CHARACTERS: Narrator, Louis
BACKGROUND_IMAGE: creed_side_yard.png
BACKGROUND_EDIT: "Night, Louis running into the side yard, phone ringing louder"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Louis runs into the side yard. SOUND of the phone is louder.
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue to the kitchen door"
  TARGET: kitchen_door_louis
  STATE_CHANGE: desperation = +1
  CONDITION: null

::SCENE::
LOCATION: The Kitchen Door of the Creed House, With Louis
MOOD: Desperate
CHARACTERS: Narrator, Louis
BACKGROUND_IMAGE: kitchen_door_louis.png
BACKGROUND_EDIT: "Night, Louis running to the kitchen door"

::SCRIPT::
- CHARACTER: Narrator
  LINE: He runs to the door and inside.
  EXPRESSION: null

::PATHS::
- CHOICE: "Enter the house"
  TARGET: end_of_path_jud
  STATE_CHANGE: hope = -1
  CONDITION: null

::SCENE::
LOCATION: The End of the Path, With Jud
MOOD: Impassive
CHARACTERS: Narrator, Jud
BACKGROUND_IMAGE: end_of_path_jud.png
BACKGROUND_EDIT: "Night, Jud standing at the end of the path, eyes inscrutable"

::SCRIPT::
- CHARACTER: Narrator
  LINE: He stands there, eyes inscrutable.
  EXPRESSION: null

::PATHS::
- CHOICE: "Wait"
  TARGET: living_room_phone
  STATE_CHANGE: mystery = +1
  CONDITION: null

::SCENE::
LOCATION: The Living Room, With the Phone
MOOD: Resignation
CHARACTERS: Narrator, Louis
BACKGROUND_IMAGE: living_room_phone.png
BACKGROUND_EDIT: "Night, living room, phone stops ringing, Louis enters"

::SCRIPT::
- CHARACTER: Narrator
  LINE: It stops. A beat later Louis enters the room. He picks it up, although he already knows it's too late. He listens to the SOUND of the dial tone and then drops it back into the cradle, disgusted.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: He starts to dial a number from memory.
  EXPRESSION: null
- CHARACTER: Jud (VOICE)
  LINE: Louis.
  EXPRESSION: null

::PATHS::
- CHOICE: "Dial the number"
  TARGET: kitchen_living_room_doorway_jud
  STATE_CHANGE: despair = +1
  CONDITION: null

::SCENE::
LOCATION: The Kitchen/Living Room Doorway, With Jud
MOOD: Secretive
CHARACTERS: Narrator, Jud, Louis
BACKGROUND_IMAGE: kitchen_living_room_doorway_jud.png
BACKGROUND_EDIT: "Night, Jud at the doorway, speaking to Louis"

::SCRIPT::
- CHARACTER: Jud
  LINE: When you talk to 'em, not one word about what we done tonight. 'S'far’s you know, the cat's still fine.
  EXPRESSION: Stern

::PATHS::
- CHOICE: "Follow Jud's instructions"
  TARGET: louis_by_phone
  STATE_CHANGE: deception = +1
  CONDITION: null

::SCENE::
LOCATION: Louis, By the Phone
MOOD: Troubled
CHARACTERS: Narrator, Louis
BACKGROUND_IMAGE: louis_by_phone.png
BACKGROUND_EDIT: "Night, Louis by the phone, lowering the receiver"

::SCRIPT::
- CHARACTER: Narrator
  LINE: After a moment he lowers it into the cradle.
  EXPRESSION: null

::PATHS::
- CHOICE: "End the call"
  TARGET: jud_room
  STATE_CHANGE: guilt = +1
  CONDITION: null

::SCENE::
LOCATION: Jud
MOOD: Philosophic and Stern
CHARACTERS: Narrator, Jud, Louis
BACKGROUND_IMAGE: jud_philosophy.png
BACKGROUND_EDIT: "Night, Jud speaking to Louis, hand on his shoulder"

::SCRIPT::
- CHARACTER: Jud
  LINE: You'll understand. In the meantime, keep your peace. What we did, Louis, was a secret thing. Women are supposed to be the ones who are good at keeping secrets, but any woman who knows anything at all would tell you she's never seen into a man’s heart. The soil of a man’s heart is stonier, Louis--like the soil up there in the old Micmac burying ground. A man grows what he can...and tends it.
  EXPRESSION: Profound
- CHARACTER: Narrator
  LINE: During this, he's come across the room to Louis and dropped his hand on Louis's shoulder.
  EXPRESSION: null
- CHARACTER: Louis
  LINE: But --
  EXPRESSION: Interrupted
- CHARACTER: Jud
  LINE: No buts! Accept what’s done, Louis. What we done was right. Another time it might not be, but tonight it was... at least I hope to Christ it was. Now you make your call...but not a word about tonight.
  EXPRESSION: Forceful

::PATHS::
- CHOICE: "Accept Jud's words and make the call"
  TARGET: road_jud
  STATE_CHANGE: acceptance = +1
  CONDITION: null

::SCENE::
LOCATION: The Road, With Jud
MOOD: Anxious and Fearful
CHARACTERS: Narrator, Jud, Dory Goldman (VOICE)
BACKGROUND_IMAGE: road_jud.png
BACKGROUND_EDIT: "Night, Jud on the side of the road, truck passing, fear on his face"

::SCRIPT::
- SOUNDS: Boops and beeps of a touch-tone telephone. Ringing. Then:
  EXPRESSION: null
- CHARACTER: DORY GOLDMAN (VOICE)
  LINE: Goldman residence.
  EXPRESSION: null
- CHARACTER: Louis
  LINE: Hi, Dory...it's Louis--
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: During this, another SOUND has been growing: an approaching truck. As Jud gains his side of the road, he looks back, and we read fear on his face--no matter what he said to Louis, he’s sorry for tonight's piece of work.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: A moment later a highballing Orinco truck cuts between THE CAMERA and Jud.
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue the call"
  TARGET: louis_living_room
  STATE_CHANGE: fear = +2
  CONDITION: null

::SCENE::
LOCATION: Louis, In the Living Room
MOOD: Forced Happiness
CHARACTERS: Narrator, Louis, Rachel (VOICE), Ellie (VOICE)
BACKGROUND_IMAGE: louis_living_room.png
BACKGROUND_EDIT: "Night, Louis on the phone, smiling and happy"

::SCRIPT::
- CHARACTER: Narrator
  LINE: He's on the phone, smiling and happy.
  EXPRESSION: null
- CHARACTER: RACHEL (VOICE)
  LINE: You want to talk to the birthday girl?
  EXPRESSION: null
- CHARACTER: Louis
  LINE: That'd be real fine.
  EXPRESSION: Enthusiastic
- CHARACTER: ELLIE (VOICE)
  LINE: Hi...daddy?
  EXPRESSION: null
- CHARACTER: Louis (SINGS)
  LINE: Happy birthday to you/Happy birthday to you/Happy birthday, dear Ellie/Happy birthday to you!
  EXPRESSION: Singing
- CHARACTER: ELLIE (VOICE)
  LINE: That was awful, daddy.
  EXPRESSION: Teasing
- CHARACTER: Louis
  LINE: Yeah, I know...how are things out there in Chicagoland?
  EXPRESSION: Casual
- CHARACTER: ELLIE (VOICE)
  LINE: Fine...except when Hom was airing Gage's diaper rash, he walked away and got into Grampa's study and pooped in Grampa’s favorite chair.
  EXPRESSION: Amused
- CHARACTER: Louis (GRINNING BROADLY)
  LINE: Way to go, Gage!
  EXPRESSION: Playful
- CHARACTER: ELLIE (VOICE)
  LINE: What?
  EXPRESSION: Confused
- CHARACTER: Louis
  LINE: I said that's too bad. What did you get for presents from Gramma and Grampa?
  EXPRESSION: Inquiring
- CHARACTER: ELLIE (VOICE)
  LINE: Lots of stuff! I got two dresses...and a Chatty Cathy doll...
  EXPRESSION: Excited

::PATHS::
- CHOICE: "Continue the conversation"
  TARGET: ellie_goldman_living_room
  STATE_CHANGE: normalcy = +1
  CONDITION: null

::SCENE::
LOCATION: The Goldman Living Room, With Ellie
MOOD: Innocent
CHARACTERS: Narrator, Ellie
BACKGROUND_IMAGE: ellie_goldman_living_room.png
BACKGROUND_EDIT: "Night, Ellie in pajamas, holding Chatty Cathy, Garfield radio in lap"

::SCRIPT::
- CHARACTER: Narrator
  LINE: She's dressed for bed, in fuzzy pink pajamas. Her Chatty Cathy is crooked in one arm. In her lap is a Garfield transistor radio.
  EXPRESSION: null
- CHARACTER: ELLIE (VOICE)
  LINE: ...and a Garfield radio! How's Church, dad? Does he miss me?
  EXPRESSION: Hopeful

::PATHS::
- CHOICE: "End the call"
  TARGET: creed_living_room_louis
  STATE_CHANGE: longing = +1
  CONDITION: null

::SCENE::
LOCATION: The Creed Living Room, With Louis
MOOD: Guilt and Unhappiness
CHARACTERS: Narrator, Louis
BACKGROUND_IMAGE: creed_living_room_louis.png
BACKGROUND_EDIT: "Night, Louis by the phone, smile fading, looking at his dirt-stained hands"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The smile fades off his face. It's replaced with a look of combined guilt and unhappiness. He’s looking at his hands, which are still dark with the dirt from Church’s grave.
  EXPRESSION: Troubled

::PATHS::
- CHOICE: "Contemplate his actions"
  TARGET: end
  STATE_CHANGE: guilt = +2, sorrow = +1
  CONDITION: null

::SCENE::
LOCATION: The Goldman Living Room
MOOD: Domestic, Amused
CHARACTERS: Louis (Voice), Ellie, Rachel, Gage
BACKGROUND_IMAGE: goldman_living_room.png
BACKGROUND_EDIT: "Ellie's living room, evening"

::SCRIPT::
- CHARACTER: Louis
  LINE: Well...I guess he's just fine, Ellie. I haven't seen him this evening, but--
  EXPRESSION: null
- CHARACTER: Ellie
  LINE: Well, make sure you put him down cellar before you go to bed so he can't run out in the road and get greased. And kiss him goodnight for me.
  EXPRESSION: Affectionate
- CHARACTER: Louis (Voice)
  LINE: Yuck! Kiss your own cat!
  EXPRESSION: Disgusted
- CHARACTER: Ellie
  LINE: Want to talk to Gage?
  EXPRESSION: Playful
- CHARACTER: Narrator
  LINE: Before he can answer, she puts the phone in Gage’s hand. Ellie and Rachel watch, amused, as Gage gobbles into it. Perhaps Rachel encourages him to say a few words.
  EXPRESSION: null

::PATHS::
- CHOICE: Continue to the Creed Living Room
  TARGET: creed_living_room
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: The Creed Living Room
MOOD: Distant, Troubled
CHARACTERS: Louis, Gage (Voice)
BACKGROUND_IMAGE: creed_living_room.png
BACKGROUND_EDIT: "Louis's living room, evening"

::SCRIPT::
- CHARACTER: Narrator
  LINE: From the telephone comes the sound of Gage talking and chortling.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Louis is not listening. His eyes--and his mind--are far away.
  EXPRESSION: Preoccupied

::PATHS::
- CHOICE: Go outside to rake leaves
  TARGET: creed_house_exterior
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: The Creed House - Exterior
MOOD: Mundane, Foreboding
CHARACTERS: Louis
BACKGROUND_IMAGE: creed_house_exterior.png
BACKGROUND_EDIT: "Morning, side lawn with a tree and tire swing"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Louis is raking leaves on the side lawn, near the tree with the tire swing. After a moment or two of this he props the rake against the tree and starts toward the garage. He goes in.
  EXPRESSION: null

::PATHS::
- CHOICE: Enter the garage
  TARGET: garage_interior
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: The Garage
MOOD: Dim, Startled
CHARACTERS: Louis, Church (Sound)
BACKGROUND_IMAGE: garage_interior.png
BACKGROUND_EDIT: "Dimly lit garage interior"

::SCRIPT::
- CHARACTER: Narrator
  LINE: It’s dim in here. Louis is crossing to the door which communicates to the kitchen. As he passes the station wagon, he hears a cat HISS. He turns.
  EXPRESSION: null

::PATHS::
- CHOICE: Investigate the hiss
  TARGET: church_on_car
  STATE_CHANGE: fear = +1
  CONDITION: null

::SCENE::
LOCATION: Church on Car
MOOD: Aggressive, Threatening
CHARACTERS: Church
BACKGROUND_IMAGE: church_on_car.png
BACKGROUND_EDIT: "Extreme close-up on Church, the cat, on top of a car, hissing"

::SCRIPT::
- CHARACTER: Narrator
  LINE: He's on top of the car, but at this point we probably don't notice; the camera is so close that Church looks like he's coming right down our throats. He's hissing angrily.
  EXPRESSION: Angry

::PATHS::
- CHOICE: React to the cat
  TARGET: louis_reaction_garage
  STATE_CHANGE: fear = +2
  CONDITION: null

::SCENE::
LOCATION: Louis's Reaction in Garage
MOOD: Shocked, Panicked
CHARACTERS: Louis
BACKGROUND_IMAGE: louis_garage_reaction.png
BACKGROUND_EDIT: "Louis recoiling in the garage after being startled"

::SCRIPT::
- CHARACTER: Narrator
  LINE: He recoils and stumbles backward with a cry. He hits a tool-rack on the wall and a lot of them fall down with a loud jangling noise.
  EXPRESSION: Crying, Panicked

::PATHS::
- CHOICE: Observe the cat's escape
  TARGET: church_escape_garage
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Church's Escape from Garage
MOOD: Frightened, Escaping
CHARACTERS: Church
BACKGROUND_IMAGE: church_garage_escape.png
BACKGROUND_EDIT: "Church the cat jumping out of the garage door into sunlight"

::SCRIPT::
- CHARACTER: Narrator
  LINE: He jumps down, frightened by the noise, and the camera tracks as he goes flying out the garage door into the sunlight.
  EXPRESSION: Frightened

::PATHS::
- CHOICE: Recover from the fright and call for the cat
  TARGET: louis_recover_garage
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Louis Recovering in Garage
MOOD: Recovering, Uneasy
CHARACTERS: Louis
BACKGROUND_IMAGE: louis_garage_recover.png
BACKGROUND_EDIT: "Louis slowly getting to his feet in the garage"

::SCRIPT::
- CHARACTER: Narrator
  LINE: He gets slowly to his feet again. He’s getting over his fright but we can see he's totally freaked out by what gave him that fright.
  EXPRESSION: Freaked Out
- CHARACTER: Narrator
  LINE: He goes to the garage door and looks out.
  EXPRESSION: null
- CHARACTER: Louis (Calls)
  LINE: Church?
  EXPRESSION: Calling

::PATHS::
- CHOICE: Look for the cat outside
  TARGET: side_yard_louis_pov
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Side Yard - Louis's POV
MOOD: Empty, Searching
CHARACTERS: Louis (Implied), Church (Not Present)
BACKGROUND_IMAGE: side_yard_louis_pov.png
BACKGROUND_EDIT: "View of grass and fallen leaves in the side yard"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Grass and fallen leaves. No sign of Church.
  EXPRESSION: null

::PATHS::
- CHOICE: Observe Louis's stunned face
  TARGET: louis_stunned_face
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Louis's Stunned Face
MOOD: Stunned, Disbelieving
CHARACTERS: Louis
BACKGROUND_IMAGE: louis_stunned_face.png
BACKGROUND_EDIT: "Close-up on Louis's face, looking stunned"

::SCRIPT::
- CHARACTER: Narrator
  LINE: null
  EXPRESSION: Stunned

::PATHS::
- CHOICE: Go inside to the kitchen to prepare food
  TARGET: kitchen_interior
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: The Kitchen
MOOD: Domestic, Routine
CHARACTERS: Louis
BACKGROUND_IMAGE: kitchen_interior.png
BACKGROUND_EDIT: "Kitchen interior, showing three doors"

::SCRIPT::
- CHARACTER: Narrator
  LINE: He's spooning cat-food into a dish. He goes to the door--there should be a total of three doors in the kitchen: one to the living room, one to the shed/garage, and one which leads directly outside. Louis uses this latter door now.
  EXPRESSION: null

::PATHS::
- CHOICE: Go out to the kitchen stoop with the food
  TARGET: kitchen_stoop_exterior
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: The Kitchen Stoop
MOOD: Waiting, Calling
CHARACTERS: Louis, Church (Sound)
BACKGROUND_IMAGE: kitchen_stoop_exterior.png
BACKGROUND_EDIT: "Exterior of the kitchen stoop with a dish of cat food"

::SCRIPT::
- CHARACTER: Narrator
  LINE: He puts the dish of food down and sits beside it.
  EXPRESSION: null
- CHARACTER: Louis
  LINE: Food, Church...food!
  EXPRESSION: Calling
- CHARACTER: Narrator
  LINE: SOUND: Miaow.
  EXPRESSION: null

::PATHS::
- CHOICE: Observe Church emerging from bushes
  TARGET: side_house_louis_pov
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Side of the House - Louis's POV
MOOD: Suspicious, Cautious
CHARACTERS: Church
BACKGROUND_IMAGE: side_house_church_pov.png
BACKGROUND_EDIT: "Church the cat slinking out of bushes towards the camera"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Church comes slinking out of the bushes and comes slowly toward the camera. He stops, looking mistrustful.
  EXPRESSION: Mistrustful

::PATHS::
- CHOICE: Encourage Church to eat
  TARGET: louis_and_church_stoop
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Louis and Church on the Stoop
MOOD: Uneasy, Concerned
CHARACTERS: Louis, Church
BACKGROUND_IMAGE: louis_and_church_stoop.png
BACKGROUND_EDIT: "Louis and Church on the kitchen stoop"

::SCRIPT::
- CHARACTER: Louis
  LINE: Come on, Church! Chow down!
  EXPRESSION: Encouraging
- CHARACTER: Narrator
  LINE: He crosses to the stoop and begins eating the food.
  EXPRESSION: null
- CHARACTER: Louis
  LINE: Christ. I don't believe this.
  EXPRESSION: Disbelieving
- CHARACTER: Narrator
  LINE: He picks Church up. Church miaows again--he wants the food.
  EXPRESSION: null
- CHARACTER: Louis (Wincing)
  LINE: God, you stink, Church.
  EXPRESSION: Disgusted
- CHARACTER: Narrator
  LINE: Church is looking at the food, trying to get out of Louis's arms.
  EXPRESSION: null
- CHARACTER: Louis
  LINE: In a second.
  EXPRESSION: Reassuring
- CHARACTER: Narrator
  LINE: He tilts the cat's head back so he can get a look at Church's neck.
  EXPRESSION: null

::PATHS::
- CHOICE: Examine Church's neck for injuries
  TARGET: church_neck_cu
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Church's Neck - CU (Louis's POV)
MOOD: Injured, Scarred
CHARACTERS: Church
BACKGROUND_IMAGE: church_neck_cu.png
BACKGROUND_EDIT: "Close-up on Church's neck, showing a scar or white fur line"

::SCRIPT::
- CHARACTER: Narrator
  LINE: There's some sort of mark here--a clear remnant of the crash. A line of white fur, or perhaps a dark red scar where no fur at all grows.
  EXPRESSION: null

::PATHS::
- CHOICE: Continue examining Louis and Church
  TARGET: louis_and_church_stoop_second
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Louis and Church on the Stoop
MOOD: Alarmed, Disgusted
CHARACTERS: Louis, Church
BACKGROUND_IMAGE: louis_and_church_stoop_second.png
BACKGROUND_EDIT: "Louis and Church on the kitchen stoop, Louis examining Church"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Louis sees something else as he lets the cat's neck go. He tweezes something out of Church's whiskers.
  EXPRESSION: null

::PATHS::
- CHOICE: Examine what Louis found in Church's whiskers
  TARGET: louis_hand_ecu
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Louis's Hand - ECU
MOOD: Disturbing, Unsettling
CHARACTERS: Louis
BACKGROUND_IMAGE: louis_hand_ecu.png
BACKGROUND_EDIT: "Extreme close-up on Louis's hand holding a shred of green plastic"

::SCRIPT::
- CHARACTER: Narrator
  LINE: It’s a shred of green plastic.
  EXPRESSION: null

::PATHS::
- CHOICE: Observe Louis's reaction and Church's attack
  TARGET: louis_and_church_attack
  STATE_CHANGE: fear = +3
  CONDITION: null

::SCENE::
LOCATION: Louis and Church
MOOD: Violent, Shocking
CHARACTERS: Louis, Church
BACKGROUND_IMAGE: louis_and_church_attack.png
BACKGROUND_EDIT: "Louis and Church on the stoop, Church attacking Louis"

::SCRIPT::
- CHARACTER: Louis
  LINE: Chewed his way out. Jesus Daldheaded Christ, he ch--
  EXPRESSION: Shocked
- CHARACTER: Narrator
  LINE: Church suddenly claws at his face.
  EXPRESSION: null
- CHARACTER: Louis
  LINE: Ow!
  EXPRESSION: In Pain
- CHARACTER: Narrator
  LINE: He claps his hand to his face. Church leaps for the food. Louis slowly takes his hand away. There are claw marks on his cheek, welling blood. He looks at the cat.
  EXPRESSION: null

::PATHS::
- CHOICE: Go to Jud Crandall's garden
  TARGET: jud_crandall_garden
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Jud Crandall's Garden
MOOD: Peaceful, then Startled
CHARACTERS: Jud, Louis
BACKGROUND_IMAGE: jud_crandall_garden.png
BACKGROUND_EDIT: "Jud Crandall's garden with pumpkins and a wheelbarrow"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The garden is a plot of about half an acre. Jud comes trundling slowly along a row, pushing a wheelbarrow. There are several pumpkins in it. Jud is wearing old khaki gardening pants and a Ramones sweatshirt. He’s wearing his headphones and we can hear the Romantics doing "What I Like About You." Jud is singing along and bopping a little--as much as his arthritis will allow, if you can dig it.
  EXPRESSION: Singing, Bopping
- CHARACTER: Narrator
  LINE: He sees a real big pumpkin, stops, and bends over to get it. He takes out his pocket-knife and slits the pumpkin-vine. He gets the pumpkin in his arms and stands up. He turns...and Louis is right there (kind of a cheap jump, but always fun), looking totally stunned.
  EXPRESSION: Stunned
- CHARACTER: Jud
  LINE: (Startled)
  EXPRESSION: Startled
- CHARACTER: Narrator
  LINE: ...drops the pumpkin. Louis reaches out and slides the phones off Jud's ears.
  EXPRESSION: null
- CHARACTER: Louis
  LINE: What did we do?
  EXPRESSION: Desperate

::PATHS::
- CHOICE: Go to Jud's kitchen
  TARGET: crandall_kitchen
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: The Crandall Kitchen
MOOD: Confused, Reassuring
CHARACTERS: Louis, Jud
BACKGROUND_IMAGE: crandall_kitchen.png
BACKGROUND_EDIT: "Jud's kitchen, with Louis at the table and Jud at the fridge"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Louis is sitting at the kitchen table. Jud is at the fridge. Jud comes back with a couple of long-necked bottles of beer and opens them.
  EXPRESSION: null
- CHARACTER: Jud
  LINE: I most generally don't start before noon, but this looks like an exception.
  EXPRESSION: Casual
- CHARACTER: Louis
  LINE: What did we do, Jud?
  EXPRESSION: Desperate
- CHARACTER: Jud
  LINE: Why, saved a little girl from being unhappy...that's all. Drink up, Louis!
  EXPRESSION: Reassuring
- CHARACTER: Narrator
  LINE: Louis drinks about half the beer.
  EXPRESSION: null
- CHARACTER: Louis
  LINE: I tried to tell myself I buried him alive. You know--Edgar Allan Poe meets Felix the Cat. But...
  EXPRESSION: Troubled
- CHARACTER: Jud
  LINE: Wouldn't wash?
  EXPRESSION: Understanding
- CHARACTER: Louis
  LINE: No. I'm a doctor. I know death when I see it, and Church was dead. He smells horrible and he uses his claws, but he's alive...and I feel like I’m going crazy. It was that place, wasn't it?
  EXPRESSION: Unsettled
- CHARACTER: Jud
  LINE: Ayuh. It was the rag-man told me about the place--Stanley Bouchard. Us kids just called him Stanny B. He was half Micmac himself.
  EXPRESSION: Informative
- CHARACTER: Louis
  LINE: Can I have another one?
  EXPRESSION: Thirsty
- CHARACTER: Jud
  LINE: I guess it wouldn't hurt.
  EXPRESSION: Agreeing
- CHARACTER: Narrator
  LINE: He gets up and goes to the fridge.
  EXPRESSION: null

::PATHS::
- CHOICE: Hear Jud's explanation about the burial ground
  TARGET: jud_fridge
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Jud, at the Fridge
MOOD: Explanatory, Historical
CHARACTERS: Jud
BACKGROUND_IMAGE: jud_fridge.png
BACKGROUND_EDIT: "Jud at the fridge, getting another beer"

::SCRIPT::
- CHARACTER: Jud
  LINE: The Micmacs used to bury their dead up there long before the whites came.
  EXPRESSION: Explanatory
- CHARACTER: Narrator
  LINE: He returns to the table with the beer.
  EXPRESSION: null
- CHARACTER: Jud
  LINE: They buried their dead and for a long time their dead stayed buried. Then something happened. Half the tribe died in a season. The rest moved on. They said a Wendigo had soured the ground.
  EXPRESSION: Storytelling
- CHARACTER: Louis
  LINE: Wendigo?
  EXPRESSION: Curious
- CHARACTER: Jud
  LINE: Spirit of the north country. Not a good spirit. Wendigos are great liars and tricksters, according to the stories. And if one touches you...
  EXPRESSION: Paused, Gathering Thoughts
- CHARACTER: Narrator
  LINE: Maybe it really was a Wendigo-- I ain’t the one to say it wasn't-- or maybe it was just some disease. Whatever the reason, those that were left moved on. But they left that place...the way it is now.
  EXPRESSION: Shrugging, Reflective
- CHARACTER: Narrator
  LINE: Jud shrugs, and drinks.
  EXPRESSION: null

::PATHS::
- CHOICE: View Jud as a boy in sepia tone
  TARGET: jud_boy_sepia
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Jud as a Boy - CU/Sepia Tone
MOOD: Sad, Melancholy
CHARACTERS: Jud (as a boy), Louis (Voice)
BACKGROUND_IMAGE: jud_boy_sepia.png
BACKGROUND_EDIT: "Sepia toned close-up of a young Jud crying, 1910"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The time here is about 1910. Jud is wearing short pants. He's crying, not in any big-deal histrionic way, but as if he means to keep doing it for a long time. I mean he looks really sad.
  EXPRESSION: Sad
- CHARACTER: Jud (Voice)
  LINE: I loved my dog a lot, Louis. When Spot died, I thought I was gonna die.
  EXPRESSION: Grieving
- CHARACTER: Narrator
  LINE: Jud is sitting on the front stoop. It's the same house Jud lives in now, but the porch hasn't been added yet, and the road is dirt rather than tar. Along this road comes a horse-drawn wagon--Stanny B.'s wagon. The wagon's full of junk, rags, bottles...stuff to sell and swap. Strung across the top are bells, and we can hear their chiming sound...but faint, like bells heard in a dream. Stanny B. is old and drunk. Dust spumes up behind the wagon as he draws up to the Crandall house and stops. He gets down, almost falls, takes a bottle out of his back pocket, drinks, and approaches Jud. We can see him speaking.
  EXPRESSION: null

::PATHS::
- CHOICE: Return to Jud's kitchen with Louis
  TARGET: crandall_kitchen_jud_louis
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Jud's Kitchen - With Jud and Louis
MOOD: Reflective, Shared Experience
CHARACTERS: Louis, Jud
BACKGROUND_IMAGE: crandall_kitchen_jud_louis.png
BACKGROUND_EDIT: "Jud's kitchen, Jud and Louis talking"

::SCRIPT::
- CHARACTER: Louis
  LINE: You and this old Indian rag-man--
  EXPRESSION: Reflective
- CHARACTER: Jud
  LINE: Stanny B. did for me what I did for you last night, Louis. Only I wasn't alone when Spot came back.
  EXPRESSION: Somber

::PATHS::
- CHOICE: Witness the flashback to Jud's backyard
  TARGET: crandall_backyard_sepia
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: The Crandall Backyard/Sepia Tone
MOOD: Disturbing, Horrifying
CHARACTERS: Jud's Mother, Spot (Dog)
BACKGROUND_IMAGE: crandall_backyard_sepia.png
BACKGROUND_EDIT: "Sepia toned backyard, Jud's mother hanging sheets, Spot emerges"

::SCRIPT::
- CHARACTER: Jud's Mother
  LINE: null
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The sheets billow. And suddenly, pushing out from behind them, quite near her, is a small mongrel dog. Spot. He's covered with graveyard dirt. His eyes are red and rolling. He splashes the sheets with the muck of his passage.
  EXPRESSION: null
- CHARACTER: Jud (Voice)
  LINE: My mother was with me.
  EXPRESSION: Somber
- CHARACTER: Narrator
  LINE: She sees who it is--what it is--and backs away, screaming, horrified.
  EXPRESSION: Horrified

::PATHS::
- CHOICE: Focus on Spot, the resurrected dog
  TARGET: spot_closer_sepia
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Spot, Closer/Sepia
MOOD: Unsettling, Infected
CHARACTERS: Spot (Dog)
BACKGROUND_IMAGE: spot_closer_sepia.png
BACKGROUND_EDIT: "Sepia toned close-up of Spot the dog, showing marks"

::SCRIPT::
- CHARACTER: Jud (Voice)
  LINE: He’d got caught in bobwire that infected. You could still see the marks on him.
  EXPRESSION: Descriptive
- CHARACTER: Narrator
  LINE: And so we can, around his neck and along the side of his head. These marks are the counterpart of the marks we've already seen on Church.
  EXPRESSION: Observational
- CHARACTER: Narrator
  LINE: SOUND of Jud's Mom screaming. Like the bells, these are screams heard in a dream.
  EXPRESSION: null

::PATHS::
- CHOICE: Show young Jud running out
  TARGET: back_stoop_crandall_sepia
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: The Back Stoop of the Crandall House/Sepia
MOOD: Frightened, Young
CHARACTERS: Jud (as a boy)
BACKGROUND_IMAGE: back_stoop_crandall_sepia.png
BACKGROUND_EDIT: "Sepia toned view of the back stoop, young Jud in a nightshirt"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The Boy Jud comes running out, dressed in a night-shirt.
  EXPRESSION: null

::PATHS::
- CHOICE: Show Jud's Mom's reaction from Jud's POV
  TARGET: jud_moms_reaction_sepia
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Jud's Mom/Sepia (Jud's POV)
MOOD: Terrified, Cornered
CHARACTERS: Jud's Mother, Spot (Dog)
BACKGROUND_IMAGE: jud_moms_reaction_sepia.png
BACKGROUND_EDIT: "Sepia toned view of Jud's mother cringing against a fence, Spot in front of her"

::SCRIPT::
- CHARACTER: Narrator
  LINE: She’s cringing against the fence at the rear of the yard. Spot stands in front of her, swaying from side to side, as if
  EXPRESSION: Cringing, Swaying

::PATHS::
- CHOICE: End of excerpt
  TARGET: end
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Jud's Kitchen
MOOD: Tension
CHARACTERS: Jud's Mom, Jud
BACKGROUND_IMAGE: jud_kitchen.png
BACKGROUND_EDIT: "Dimly lit kitchen"

::SCRIPT::
- CHARACTER: Jud's Mom
  LINE: Get your dog, Jud! He stinks of the ground you buried him in! Come here and get your dog!
  EXPRESSION: Dim, Far

::SCENE::
LOCATION: The Boy Jud / Sepia
MOOD: Horror, Shame
CHARACTERS: Jud
BACKGROUND_IMAGE: boy_jud_sepia.png
BACKGROUND_EDIT: "Sepia toned image of Jud"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Horrified...ashamed.
  EXPRESSION: null

::SCENE::
LOCATION: Jud's Mom / Sepia
MOOD: Terror
CHARACTERS: Jud's Mom
BACKGROUND_IMAGE: juds_mom_sepia.png
BACKGROUND_EDIT: "Sepia toned image of Jud's Mom"

::SCRIPT::
- CHARACTER: Jud's Mom
  LINE: COME AND GET YOUR DOG!!
  EXPRESSION: Terror

::SCENE::
LOCATION: Jud's Kitchen
MOOD: Unease
CHARACTERS: Louis, Jud
BACKGROUND_IMAGE: jud_kitchen_interior.png
BACKGROUND_EDIT: "Jud's kitchen"

::SCRIPT::
- CHARACTER: Louis
  LINE: How did your mother take it, Jud? How did she take it when your dog came back from the dead?
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Jud's face is a complication. He's lying to Louis, certainly-but is he also lying to himself? Yes, I think so.
  EXPRESSION: null
- CHARACTER: Jud
  LINE: Well, she was a little upset at first, and that's why I thought you ought to hold your peace when you talked to your people last night...you did, didn't you, Louis?
  EXPRESSION: Deceptive
- CHARACTER: Louis
  LINE: Yes.
  EXPRESSION: null
- CHARACTER: Jud
  LINE: Why, then, things should be fine.
  EXPRESSION: Reassuring
- CHARACTER: Louis
  LINE: A little upset is all she was? Because I'll tell you, Jud, my brains feel a little like a nuclear reactor on the edge of a meltdown.
  EXPRESSION: Worried
- CHARACTER: Jud
  LINE: She got used to the idea. Spot lived another four years. He died peacefully in the night that second time, and I buried him in the Pet Sematary. ..where his bones still lie.
  EXPRESSION: Calm

::PATHS::
- CHOICE: "Continue conversation"
  TARGET: road_between_houses
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: The Road Between The Two Houses, With Louis And Jud
MOOD: Reflective
CHARACTERS: Louis, Jud
BACKGROUND_IMAGE: road_between_houses.png
BACKGROUND_EDIT: "Louis and Jud walking on a road"

::SCRIPT::
- CHARACTER: Narrator
  LINE: We see them crossing.
  EXPRESSION: null
- CHARACTER: Louis (Voice)
  LINE: You still haven't told me why you did it.
  EXPRESSION: Inquisitive

::PATHS::
- CHOICE: "Continue walking"
  TARGET: creed_front_lawn
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Jud And Louis, On The Creed Front Lawn
MOOD: Intense
CHARACTERS: Jud, Louis
BACKGROUND_IMAGE: creed_front_lawn.png
BACKGROUND_EDIT: "Louis and Jud on the Creed front lawn"

::SCRIPT::
- CHARACTER: Jud
  LINE: A man doesn’t always know why he does things, Louis. I think I did it because your daughter ain't ready for her favorite pet to die.
  EXPRESSION: Resigned
- CHARACTER: Louis
  LINE: What?
  EXPRESSION: Confused
- CHARACTER: Jud
  LINE: Ellie’s a little scared of death. And the main reason Ellie's that way is because your wife is a lot scared of death. Now you just go ahead and tell me I'm wrong.
  EXPRESSION: Insightful
- CHARACTER: Narrator
  LINE: But Louis’s reaction tells him he's not wrong--in fact, Jud has hit the nail right on the head.
  EXPRESSION: null

::PATHS::
- CHOICE: "Walk to the house"
  TARGET: bathtub_fixtures_cu
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Bathtub Fixtures, CU
MOOD: Domestic
CHARACTERS: Louis
BACKGROUND_IMAGE: bathtub_fixtures_cu.png
BACKGROUND_EDIT: "Close-up of bathtub fixtures"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Louis's hands come into the frame and turn the spigots.
  EXPRESSION: null

::PATHS::
- CHOICE: "Turn on water"
  TARGET: bathroom_with_louis
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: The Bathroom, With Louis
MOOD: Troubled
CHARACTERS: Louis
BACKGROUND_IMAGE: bathroom_louis.png
BACKGROUND_EDIT: "Louis in a bathroom, door shut, no windows"

::SCRIPT::
- CHARACTER: Narrator
  LINE: He starts to undress, still looking troubled. We should notice that the door behind him is firmly shut. The bathroom has no windows.
  EXPRESSION: null

::PATHS::
- CHOICE: "Undress"
  TARGET: bathtub_spigots
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: The Bathtub Spigots
MOOD: Relaxing
CHARACTERS: Louis
BACKGROUND_IMAGE: bathtub_spigots.png
BACKGROUND_EDIT: "Steaming hot water in a bathtub"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The hot water is steaming. Louis's hands enter the frame and turn off the faucets.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: SOUND of Louis climbing in.
  EXPRESSION: null

::PATHS::
- CHOICE: "Get in the tub"
  TARGET: louis_in_the_tub
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Louis In The Tub
MOOD: Pleasure, Relaxation
CHARACTERS: Louis
BACKGROUND_IMAGE: louis_in_the_tub.png
BACKGROUND_EDIT: "Louis relaxing in a bathtub"

::SCRIPT::
- CHARACTER: Narrator
  LINE: A big sigh and an expression of exquisite pleasure. He relaxes in the hot water. After a few moments he puts a wet washcloth over his face.
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue relaxing"
  TARGET: kitchen_sink_rachel
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: By The Kitchen Sink, With Rachel
MOOD: Urgent
CHARACTERS: Rachel
BACKGROUND_IMAGE: kitchen_sink_rachel.png
BACKGROUND_EDIT: "Rachel at a kitchen sink"

::SCRIPT::
- CHARACTER: Rachel
  LINE: Don't shilly-shally, Louis. Give the little girl her promise.
  EXPRESSION: Urgent

::PATHS::
- CHOICE: "Wait for Louis"
  TARGET: kitchen_table
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: The Kitchen Table
MOOD: Disturbed, Eerie
CHARACTERS: Gage, Ellie, Victor Pascow, Louis, Church
BACKGROUND_IMAGE: kitchen_table.png
BACKGROUND_EDIT: "Kitchen table with Gage, Ellie, Pascow, Louis, and Church's body"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Gage is in his high chair. Ellie is at her place, crying. In Rachel’s place sits Victor Pascow, bloody and wrecked. Louis sits in his place. On the platter of bacon and scrambled eggs is Church’s mangled body.
  EXPRESSION: null
- CHARACTER: Pascow
  LINE: The door must not be opened. The barrier must not be crossed.
  EXPRESSION: Ominous
- CHARACTER: Louis
  LINE: You don't understand--
  EXPRESSION: Frustrated

::PATHS::
- CHOICE: "Continue explaining"
  TARGET: bathtub_louis_mutter
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: The Bathtub, With Louis
MOOD: Distracted
CHARACTERS: Louis
BACKGROUND_IMAGE: bathtub_louis.png
BACKGROUND_EDIT: "Louis in a bathtub, washcloth over his face"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The washrag is slipping, but it still covers his face.
  EXPRESSION: null
- CHARACTER: Louis (Mutters)
  LINE: --I'm a doctor.
  EXPRESSION: Drowsy

::PATHS::
- CHOICE: "Fall asleep"
  TARGET: creed_kitchen_table_2
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: The Creed Kitchen Table
MOOD: Gruesome, Foreboding
CHARACTERS: Pascow, Louis, Ellie, Gage, Spot
BACKGROUND_IMAGE: creed_kitchen_table.png
BACKGROUND_EDIT: "Creed kitchen table with Pascow, Louis, Ellie, Gage, and Spot's corpse"

::SCRIPT::
- CHARACTER: Narrator
  LINE: In attendance: Pascow, Louis, Ellie, Gage in his high chair. Lying in the middle of the table, clotted with dirt and blood, eyes staring, neck a gory mess of infected wounds, is Spot. He's also dotted with clots of scrambled egg and bits of bacon.
  EXPRESSION: null
- CHARACTER: Pascow
  LINE: Sometimes the dead do more than speak. Remember, doc.
  EXPRESSION: Warning

::PATHS::
- CHOICE: "Listen to Pascow"
  TARGET: rachel_kitchen_sink
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Rachel, At The Kitchen Sink
MOOD: Desperate
CHARACTERS: Rachel
BACKGROUND_IMAGE: rachel_kitchen_sink.png
BACKGROUND_EDIT: "Rachel at the kitchen sink"

::SCRIPT::
- CHARACTER: Rachel
  LINE: Don't shilly-shally, Louis. Promise me. Promise me. Promise me.
  EXPRESSION: Great Force

::PATHS::
- CHOICE: "Make a promise"
  TARGET: bathtub_louis_dozing
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: The Bathtub, With Louis
MOOD: Dozing
CHARACTERS: Louis
BACKGROUND_IMAGE: bathtub_louis_dozing.png
BACKGROUND_EDIT: "Louis dozing in a bathtub"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The washcloth has slipped enough so we can see his eyes are closed--he's dozing.
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue dozing"
  TARGET: creed_kitchen_table_3
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: The Creed Kitchen Table
MOOD: Shocking, Disturbing
CHARACTERS: Louis, Ellie, Pascow, Gage, Spot, Jud
BACKGROUND_IMAGE: creed_kitchen_table_2.png
BACKGROUND_EDIT: "Creed kitchen table with corpses and Jud entering"

::SCRIPT::
- CHARACTER: Narrator
  LINE: To Louis, Ellie, Pascow, Gage, and the corpse of Spot enters Jud, his eyes shocked and staring.
  EXPRESSION: null
- CHARACTER: Jud
  LINE: You do it for all the best reasons, but that ain't why. You do it because it gets hold of you...you do it because you have to.
  EXPRESSION: Resigned

::PATHS::
- CHOICE: "Observe Jud"
  TARGET: louis_bathtub_cu
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Louis, In The Bathtub, CU
MOOD: Shocked
CHARACTERS: Louis
BACKGROUND_IMAGE: louis_bathtub_cu.png
BACKGROUND_EDIT: "Close-up of Louis in a bathtub"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The washrag has worked its way down to his mouth by now. His doze is deepening; he's started to snore a little. SOUND: A splash. Something has been dropped into the bath. Louis opens his eyes. Looks puzzled. Looks down. Eyes widen in shock.
  EXPRESSION: null

::PATHS::
- CHOICE: "Look down"
  TARGET: bathwater_louis_pov
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: The Bathwater, Louis's POV
MOOD: Horrifying
CHARACTERS: Louis
BACKGROUND_IMAGE: bathwater_louis_pov.png
BACKGROUND_EDIT: "Louis's POV of a dead rat in the bathtub"

::SCRIPT::
- CHARACTER: Narrator
  LINE: A very large and very mangled dead rat floats in the bath, actually brushing against Louis's chest. Blood has begun to stain the water.
  EXPRESSION: null

::PATHS::
- CHOICE: "Leap out"
  TARGET: louis_reacts
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Louis
MOOD: Shocked, Disgusted
CHARACTERS: Louis
BACKGROUND_IMAGE: louis_reacts.png
BACKGROUND_EDIT: "Louis reacting to the rat in the bath"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Turns his head, preparatory to leaping out.
  EXPRESSION: null

::PATHS::
- CHOICE: "Leap out of the tub"
  TARGET: toilet_lid_church
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: The Toilet Lid, With Church
MOOD: Menacing
CHARACTERS: Church
BACKGROUND_IMAGE: toilet_lid_church.png
BACKGROUND_EDIT: "Church the cat on a toilet lid, mouth open"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Its mouth yawns open. It hisses, showing bloodstained teeth.
  EXPRESSION: null

::PATHS::
- CHOICE: "Observe the cat"
  TARGET: bathroom_louis_panic
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: The Bathroom
MOOD: Panic, Disgust
CHARACTERS: Louis, Church
BACKGROUND_IMAGE: bathroom_panic.png
BACKGROUND_EDIT: "Louis leaping from the tub, Church hissing"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Louis leaps from the tub. Grabs a towel and begins to rub himself frantically. He’s grossed out. The cat tries to arch against him and he hits it. Church falls to the floor, hissing. Louis looks at the closed door.
  EXPRESSION: null
- CHARACTER: Louis
  LINE: How the hell did you get in?
  EXPRESSION: Angry
- CHARACTER: Narrator
  LINE: He may not know that, but he knows how it’s going to get out. He opens the door to the upstairs hall. If Church doesn't go at once, Louis helps it with his foot. Then he looks down at:
  EXPRESSION: null

::PATHS::
- CHOICE: "Open the door"
  TARGET: bathtub_brer_rat
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: The Bathtub With Brer Rat, Louis's POV
MOOD: Lingering Horror
CHARACTERS: Louis
BACKGROUND_IMAGE: bathtub_brer_rat.png
BACKGROUND_EDIT: "Louis's POV of the rat in the bathtub"

::SCRIPT::
- CHARACTER: Narrator
  LINE: null
  EXPRESSION: null

::PATHS::
- CHOICE: "Stare at the rat"
  TARGET: louis_staring_rat
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Louis
MOOD: Stunned, Overwhelmed
CHARACTERS: Louis
BACKGROUND_IMAGE: louis_staring_rat.png
BACKGROUND_EDIT: "Louis staring at the rat in the bathtub"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Staring at the rat. Over this: THE SOUND OF JET ENGINES.
  EXPRESSION: null

::PATHS::
- CHOICE: "Listen to the sound"
  TARGET: delta_727
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: A Delta 727
MOOD: Arrival
CHARACTERS: None
BACKGROUND_IMAGE: delta_727.png
BACKGROUND_EDIT: "A Delta 727 jet preparing to land"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Its landing gear unfolds preparatory to touching down at Bangor International Airport.
  EXPRESSION: null

::PATHS::
- CHOICE: "Land at airport"
  TARGET: delplanting_area
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: A Delplanting Area - Day
MOOD: Busy
CHARACTERS: Passengers
BACKGROUND_IMAGE: delplanting_area.png
BACKGROUND_EDIT: "People deplaning a jet"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Lots of people making their way up the jetway.
  EXPRESSION: null

::PATHS::
- CHOICE: "Exit the plane"
  TARGET: louis_outside_security
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Louis, Outside The Security Point
MOOD: Anxious, Joyful
CHARACTERS: Louis
BACKGROUND_IMAGE: louis_outside_security.png
BACKGROUND_EDIT: "Louis waiting outside security with roses"

::SCRIPT::
- CHARACTER: Narrator
  LINE: He's looking anxiously for his people. In one hand he's got half a dozen roses. His face lights up.
  EXPRESSION: null

::PATHS::
- CHOICE: "See his family"
  TARGET: deplaning_area_louis_pov
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: The Deplaning Area, Louis's POV
MOOD: Loving
CHARACTERS: Louis, Ellie, Rachel, Gage
BACKGROUND_IMAGE: deplaning_area_louis_pov.png
BACKGROUND_EDIT: "Louis's family deplaning"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Here comes Louis's family. Ellie is a little ahead. Rachel is pushing Gage in his stroller. Ellie sees Louis and lights up.
  EXPRESSION: null
- CHARACTER: Ellie
  LINE: Daddy!
  EXPRESSION: Joyful
- CHARACTER: Narrator
  LINE: She runs for him.
  EXPRESSION: null

::PATHS::
- CHOICE: "Embrace Ellie"
  TARGET: dust_outside_security
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Dust Outside The Security Point
MOOD: Affectionate
CHARACTERS: Ellie, Louis
BACKGROUND_IMAGE: dust_outside_security.png
BACKGROUND_EDIT: "Ellie running into Louis's arms"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Ellie comes belting up to Louis, weaving among the deplanees like a slalom skier. She leaps into his arms. Louis swings her cheerfully.
  EXPRESSION: null
- CHARACTER: Louis
  LINE: Hi, sugar!
  EXPRESSION: Affectionate
- CHARACTER: Narrator
  LINE: She smacks him noisily. He smacks her back just as noisily.
  EXPRESSION: null
- CHARACTER: Ellie
  LINE: Daddy, is Church all right?
  EXPRESSION: Concerned
- CHARACTER: Narrator
  LINE: Louis's face changes. All at once he's watchful.
  EXPRESSION:null
- CHARACTER: Louis
  LINE: Yes...I guess so. He was sleeping on the front porch when I left.
  EXPRESSION: Hesitant
- CHARACTER: Ellie
  LINE: Cause I had a bad dream about him. I dreamed he got hit by a car and you and Mr. Crandall buried him in the Pet Sematary.
  EXPRESSION: Fearful
- CHARACTER: Louis (Trying to smile)
  LINE: That was a silly dream, wasn't it?
  EXPRESSION: Reassuring
- CHARACTER: Ellie
  LINE: Is he really all right?
  EXPRESSION: Anxious
- CHARACTER: Louis
  LINE: Yes.
  EXPRESSION: Calm
- CHARACTER: Ellie
  LINE: Because you promised.
  EXPRESSION: Hopeful
- CHARACTER: Louis
  LINE: I know.
  EXPRESSION: Resigned
- CHARACTER: Narrator
  LINE: Rachel reaches them. She's pretty tired. Hair hanging in her face, good travelling clothes now looking a bit wrinkled and a bit stale.
  EXPRESSION: null
- CHARACTER: Rachel
  LINE: Want to take your son, doc?
  EXPRESSION: Tired
- CHARACTER: Narrator
  LINE: Louis does. Gage is ecstatic. Louis kisses Rachel deeply.
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue to the house"
  TARGET: creed_kitchen_night
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: The Creed Kitchen - Night
MOOD: Concerned
CHARACTERS: Church, Ellie
BACKGROUND_IMAGE: creed_kitchen_night.png
BACKGROUND_EDIT: "Church at the door of the Creed kitchen"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Church at the door, waiting to be let out. Ellie does the honors. Church oils out into the shed/garage. Ellie closes the door. She looks distressed. She crosses the kitchen again.
  EXPRESSION: null

::PATHS::
- CHOICE: "Go to the living room"
  TARGET: creed_living_room_night
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: The Creed Living Room - Night
MOOD: Quiet, Domestic
CHARACTERS: Rachel, Louis, Gage, Ellie
BACKGROUND_IMAGE: creed_living_room_night.png
BACKGROUND_EDIT: "Rachel watching TV, Louis reading, Gage sleeping"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Rachel, in a flannel nightgown, is watching TV. Louis is reading a medical tome and making notes. Gage, zipped into a warm blanket suit, is sacking on the couch.
  EXPRESSION: null
- CHARACTER: Ellie (Entering)
  LINE: Can cats have shampoos?
  EXPRESSION: Curious
- CHARACTER: Rachel
  LINE: Yes--you have to take them to someone who grooms animals, though. I think it's pretty expensive.
  EXPRESSION: Informative
- CHARACTER: Ellie (Still upset)
  LINE: I don't care. I'll save up my allowance and pay for it. Church smells bad.
  EXPRESSION: Determined
- CHARACTER: Louis
  LINE: I've noticed it, too. I'll cough up the money, Ellen.
  EXPRESSION: Concerned
- CHARACTER: Ellie
  LINE: I hate that smell.
  EXPRESSION: Disgusted

::PATHS::
- CHOICE: "Acknowledge the smell"
  TARGET: louis_cu_grim
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Louis, CU
MOOD: Grim, Sad
CHARACTERS: Louis
BACKGROUND_IMAGE: louis_cu_grim.png
BACKGROUND_EDIT: "Close-up of Louis's face"

::SCRIPT::
- CHARACTER: Narrator
  LINE: He looks both grim and sad--a man discovering that what you pay for you own, and what you own always comes home to you.
  EXPRESSION: null
- CHARACTER: Louis
  LINE: Yes--I hate it, too.
  EXPRESSION: Resigned

::PATHS::
- CHOICE: "Fade to black"
  TARGET: black_screen
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Black
MOOD: Somber
CHARACTERS: None
BACKGROUND_IMAGE: black_screen.png
BACKGROUND_EDIT: "Black screen with a title card"

::SCRIPT::
- CHARACTER: Narrator
  LINE: BLACK. And on it, a fourth title card: MISSY DANDRIDGE.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: SOUND: A pen scratching over paper.
  EXPRESSION: null

::PATHS::
- CHOICE: "Proceed to study"
  TARGET: study_desk_cu
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: A Study Desk, CU
MOOD: Desperate, Final
CHARACTERS: Missy Dandridge
BACKGROUND_IMAGE: study_desk_cu.png
BACKGROUND_EDIT: "Close-up of a hand writing a note"

::SCRIPT::
- CHARACTER: Narrator
  LINE: A single sheet of lined paper is spotlighted by the glow of the desk-lamp. On it, Missy's right hand is just finishing: "Dr. says Intestinal Cancer. Cannot face this Pain. Sorry."
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The hand puts the pen down. It tears the paper in two, leaving just the half with the message.
  EXPRESSION: null

::PATHS::
- CHOICE: "Tear the paper"
  TARGET: dandridge_cellar
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: The Dandridge Cellar - Night
MOOD: Grim, Foreboding
CHARACTERS: Missy Dandridge
BACKGROUND_IMAGE: dandridge_cellar.png
BACKGROUND_EDIT: "A cellar with a hangman's noose"

::SCRIPT::
- CHARACTER: Narrator
  LINE: A light comes on and we see a hangman's noose strung over a beam. It dangles above a kitchen table which has been relegated to cellar duty. SOUND: Descending footsteps.
  EXPRESSION: null

::PATHS::
- CHOICE: "Approach the noose"
  TARGET: noose_cu
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: The Noose, CU
MOOD: Desperate, Final
CHARACTERS: Missy Dandridge
BACKGROUND_IMAGE: noose_cu.png
BACKGROUND_EDIT: "Close-up of a hangman's noose"

::SCRIPT::
- CHARACTER: Narrator
  LINE: SOUND of Missy climbing onto the table. Her face enters the frame. She looks very sick. She puts her head into the noose and rakes it tight at the hyoid bone.
  EXPRESSION: null

::PATHS::
- CHOICE: "Secure the noose"
  TARGET: dandridge_house_night
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: The Dandridge House - Night
MOOD: Tragic
CHARACTERS: Missy Dandridge
BACKGROUND_IMAGE: dandridge_house_night.png
BACKGROUND_EDIT: "A house with a cellar light on"

::SCRIPT::
- CHARACTER: Narrator
  LINE: One light on...a cellar light. SOUND: Ree-ree-ree...then... SOUND: Kick! THUMP! SOUND: Ree-ree-ree...
  EXPRESSION: null

::PATHS::
- CHOICE: "Witness the aftermath"
  TARGET: cellar_missy_dandridge
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: The Cellar, With Missy Dandridge
MOOD: Finality, Tragedy
CHARACTERS: Missy Dandridge
BACKGROUND_IMAGE: cellar_missy_dandridge.png
BACKGROUND_EDIT: "Missy Dandridge hanging in the cellar"

::SCRIPT::
- CHARACTER: Narrator
  LINE: She hangs limply, hands dangling at her sides, above the table, which now lies upon its side. We can see the note clearly. She pinned it to the bodice of her housedress. SOUND
  EXPRESSION: null

::SCENE::
LOCATION: In Front of the Grace Methodist Church
MOOD: Somber
CHARACTERS: Narrator, People, Pallbearers
BACKGROUND_IMAGE: church_exterior_day.png
BACKGROUND_EDIT: "Mid-morning, cars gathering outside a church, people exiting."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Car engines starting up.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: People are coming out and getting into their cars and turning on the headlights, even though it is only mid-morning.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: In the immediate f.g. is a hearse. Four pallbearers are loading a coffin into it.
  EXPRESSION: null

::PATHS::
- CHOICE: "Observe the scene"
  TARGET: church_steps
  STATE_CHANGE: none
  CONDITION: null

::SCENE::
LOCATION: On the Church Steps
MOOD: Confused, Somber
CHARACTERS: Ellie, Louis, Jud
BACKGROUND_IMAGE: church_steps_day.png
BACKGROUND_EDIT: "Mid-morning, people turning on car headlights, a coffin being loaded into a hearse."

::SCRIPT::
- CHARACTER: Ellie
  LINE: They're all turning on their lights! Daddy, why are they all turning on their lights in the middle of the day?
  EXPRESSION: Confused
- CHARACTER: Narrator
  LINE: JUD, dressed in a rusty old black suit and a black tie, comes out and stands with them. He looks haggard and old.
  EXPRESSION: null
- CHARACTER: Jud
  LINE: They do it to honor the dead, Ellen.
  EXPRESSION: Somber
- CHARACTER: Ellie
  LINE: Is that right, dad?
  EXPRESSION: Curious
- CHARACTER: Louis
  LINE: Yes. To honor the dead.
  EXPRESSION: Somber

::PATHS::
- CHOICE: "Follow the procession"
  TARGET: church_parking_area
  STATE_CHANGE: none
  CONDITION: null

::SCENE::
LOCATION: The Church Parking Area
MOOD: Somber
CHARACTERS: Narrator
BACKGROUND_IMAGE: church_parking_area_day.png
BACKGROUND_EDIT: "Mid-morning, more cars starting, hearse doors closing."

::SCRIPT::
- CHARACTER: Narrator
  LINE: More cars start up; more lights come on; the back doors of the hearse swing closed.
  EXPRESSION: null

::PATHS::
- CHOICE: "Proceed to the cemetery"
  TARGET: ludlow_cemetery
  STATE_CHANGE: none
  CONDITION: null

::SCENE::
LOCATION: Ludlow Cemetery
MOOD: Solemn
CHARACTERS: Narrator, Minister (Voice), Mourners
BACKGROUND_IMAGE: ludlow_cemetery_day.png
BACKGROUND_EDIT: "Daytime, graveside service, coffin on runners."

::SCRIPT::
- CHARACTER: Narrator
  LINE: [NOTE: In the book LOUIS finds it difficult to enter at night because of a high iron fence. Here we should see there's no such problem; there's only a low stone wall between the graveyard and the public road.]
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The mourners are of course gathered around the grave of MISSY DANDRIDGE. The coffin rests above it on runners.
  EXPRESSION: null
- CHARACTER: Minister (Voice)
  LINE: May the Lord bless you and keep you; may the Lord make his face to shine upon you, and comfort you, and lift you up, and give you peace. Amen.
  EXPRESSION: Solemn

::PATHS::
- CHOICE: "Observe the mourners"
  TARGET: louis_ellie_jud_exit
  STATE_CHANGE: none
  CONDITION: null

::SCENE::
LOCATION: Louis, Ellie, Jud
MOOD: Reflective, Somber
CHARACTERS: Jud, Louis, Ellie
BACKGROUND_IMAGE: louis_ellie_jud_exit.png
BACKGROUND_EDIT: "Daytime, leaving the cemetery, walking towards a car."

::SCRIPT::
- CHARACTER: Jud
  LINE: Rachel not feeling well?
  EXPRESSION: Concerned
- CHARACTER: Louis
  LINE: Well...a touch of the flu...
  EXPRESSION: Evasive
- CHARACTER: Ellie
  LINE: She's in bed. She was throwing up. Ever since Mrs. Rogers called and said Missy—
  EXPRESSION: Upset
- CHARACTER: Louis
  LINE: That's enough, Ellen.
  EXPRESSION: Firm
- CHARACTER: Narrator
  LINE: They've reached the CREED station wagon.
  EXPRESSION: null
- CHARACTER: Jud
  LINE: Out of the mouths of babes, Louis.
  EXPRESSION: Cynical
- CHARACTER: Louis
  LINE: This babe has said enough.
  EXPRESSION: Annoyed
- CHARACTER: Louis
  LINE: Hop in, Ellie.
  EXPRESSION: Gentle
- CHARACTER: Narrator
  LINE: She does, and LOUIS closes the door.
  EXPRESSION: null
- CHARACTER: Jud
  LINE: Poor Missy. God, I was sorry to hear. I remember when she was no older'n Ellen there, walking down to the store with her Raggedy Anne doll draggin' behind her in the dust. I don't know why God takes someone like her, who should have a bunch of years still in front of them, and lets an old shit like me just go on and on.
  EXPRESSION: Melancholy
- CHARACTER: Louis
  LINE: My father used to have a saying, Jud-- "God sees the truth, but waits."
  EXPRESSION: Thoughtful
- CHARACTER: Jud
  LINE: Ayuh...how is your cat, Louis?
  EXPRESSION: Sarcastic
- CHARACTER: Louis
  LINE: It's Ellie's cat.
  EXPRESSION: Correcting
- CHARACTER: Jud
  LINE: Nope. He's your cat now.
  EXPRESSION: Assertive
- CHARACTER: Narrator
  LINE: JUD opens one of the back doors as LOUIS goes around to the driver's side.
  EXPRESSION: null

::PATHS::
- CHOICE: "Get in the car"
  TARGET: back_seat_wagon
  STATE_CHANGE: none
  CONDITION: null

::SCENE::
LOCATION: The Back Seat of the Wagon
MOOD: Discomfort, Sadness
CHARACTERS: Jud, Narrator
BACKGROUND_IMAGE: back_seat_wagon.png
BACKGROUND_EDIT: "Daytime, inside a car, Jud is asleep."

::SCRIPT::
- CHARACTER: Narrator
  LINE: JUD has tilted over in one corner and is snoring. His Walkman 'phones are on and we can hear the tinny sounds of Billy Idol. A little old man's drool trickles down from one corner of his mouth.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: SOUND: ELLEN is crying.
  EXPRESSION: null

::PATHS::
- CHOICE: "Observe Ellie"
  TARGET: front_seat_wagon
  STATE_CHANGE: none
  CONDITION: null

::SCENE::
LOCATION: The Front of the Wagon, With Louis and Ellie
MOOD: Grief, Sadness
CHARACTERS: Ellie, Louis
BACKGROUND_IMAGE: front_seat_wagon.png
BACKGROUND_EDIT: "Daytime, inside a car, Louis and Ellie are in the front seats."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Tears are spilling freely down ELLIE'S face.
  EXPRESSION: null
- CHARACTER: Louis
  LINE: Ellie? What's wrong?
  EXPRESSION: Concerned
- CHARACTER: Ellie
  LINE: No more chocolate chip cookies.
  EXPRESSION: Distraught
- CHARACTER: Louis
  LINE: Huh?
  EXPRESSION: Confused
- CHARACTER: Ellie
  LINE: Missy made the best chocolate chip cookies in the world--even Mom said so. Now there won't be any more because she's gonna be dead forever!
  EXPRESSION: Wailing
- CHARACTER: Narrator
  LINE: She cries harder. LOUIS reaches out and strokes her hair.
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue driving"
  TARGET: station_wagon_driving
  STATE_CHANGE: none
  CONDITION: null

::SCENE::
LOCATION: The Station Wagon
MOOD: Transition, Melancholy
CHARACTERS: Narrator
BACKGROUND_IMAGE: station_wagon_driving.png
BACKGROUND_EDIT: "Daytime, car driving on a country road with fall foliage."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Moving up the country road toward home through blazing fall foliage.
  EXPRESSION: null

::PATHS::
- CHOICE: "Arrive home"
  TARGET: tv_screen_cu_night
  STATE_CHANGE: none
  CONDITION: null

::SCENE::
LOCATION: TV Screen, CU
MOOD: Unease
CHARACTERS: News Anchor, Ellie (Voice)
BACKGROUND_IMAGE: tv_screen_night.png
BACKGROUND_EDIT: "Nighttime, close-up of a TV screen showing a horror movie scene."

::SCRIPT::
- CHARACTER: Narrator
  LINE: On it is a scene from "Night of the Living Dead."
  EXPRESSION: null
- CHARACTER: News Anchor
  LINE: Bizarre as it may seem, it now seems almost beyond doubt: the dead are returning to eat the living.
  EXPRESSION: Serious
- CHARACTER: Ellie (Voice)
  LINE: Daddy?
  EXPRESSION: Concerned

::PATHS::
- CHOICE: "Turn off the TV"
  TARGET: creed_living_room_night
  STATE_CHANGE: none
  CONDITION: null

::SCENE::
LOCATION: The Creed Living Room
MOOD: Quiet, Troubled
CHARACTERS: Louis, Ellie
BACKGROUND_IMAGE: creed_living_room_night.png
BACKGROUND_EDIT: "Nighttime, living room with a TV and VCR."

::SCRIPT::
- CHARACTER: Narrator
  LINE: There's a VCR on top of the TV; LOUIS has been watching "Night."
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Now he quickly uses the remote control to shut down the TV.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: She's dressed for bed, and comes toward him slowly.
  EXPRESSION: null
- CHARACTER: Louis
  LINE: What's up, sugar?
  EXPRESSION: Gentle
- CHARACTER: Ellie
  LINE: Daddy, do you think Missy Dandridge went to heaven?
  EXPRESSION: Anxious
- CHARACTER: Louis
  LINE: What?
  EXPRESSION: Perplexed

::PATHS::
- CHOICE: "Answer Ellie's question"
  TARGET: kitchen_rachel
  STATE_CHANGE: none
  CONDITION: null

::SCENE::
LOCATION: The Kitchen, With Rachel
MOOD: Worried, Observant
CHARACTERS: Rachel
BACKGROUND_IMAGE: kitchen_rachel.png
BACKGROUND_EDIT: "Nighttime, kitchen, Rachel is cleaning up."

::SCRIPT::
- CHARACTER: Narrator
  LINE: She's putting away the last of the supper things. She hears this and moves toward the living room door to listen. She doesn't look at all well. Her eyes are red from crying and her face is haggard.
  EXPRESSION: null

::PATHS::
- CHOICE: "Listen to the conversation"
  TARGET: living_room_louis_ellie
  STATE_CHANGE: none
  CONDITION: null

::SCENE::
LOCATION: The Living Room, With Louis and Ellie
MOOD: Comforting, Philosophical
CHARACTERS: Ellie, Louis
BACKGROUND_IMAGE: living_room_louis_ellie.png
BACKGROUND_EDIT: "Nighttime, living room, Ellie is on Louis's lap."

::SCRIPT::
- CHARACTER: Narrator
  LINE: She's gotten up into his lap.
  EXPRESSION: null
- CHARACTER: Ellie
  LINE: At school Michael McDowell said she was gonna fry in hell. Michael McDowell says all sewersides fry in hell.
  EXPRESSION: Fearful
- CHARACTER: Louis
  LINE: Well, I think Michael McDowell is so full of shit he probably squeaks when he walks, my dear.
  EXPRESSION: Dismissive

::PATHS::
- CHOICE: "Continue the conversation"
  TARGET: rachel_door
  STATE_CHANGE: none
  CONDITION: null

::SCENE::
LOCATION: Rachel, At the Door
MOOD: Amused, Wary
CHARACTERS: Rachel
BACKGROUND_IMAGE: rachel_door.png
BACKGROUND_EDIT: "Nighttime, doorway to the living room."

::SCRIPT::
- CHARACTER: Narrator
  LINE: She smiles a little at this.
  EXPRESSION: null

::PATHS::
- CHOICE: "Listen further"
  TARGET: louis_ellie_living_room
  STATE_CHANGE: none
  CONDITION: null

::SCENE::
LOCATION: Louis and Ellie, In the Living Room
MOOD: Reassuring, Explanatory
CHARACTERS: Ellie, Louis
BACKGROUND_IMAGE: louis_ellie_living_room.png
BACKGROUND_EDIT: "Nighttime, living room, Ellie is on Louis's lap."

::SCRIPT::
- CHARACTER: Louis
  LINE: But don't you dare say that.
  EXPRESSION: Stern
- CHARACTER: Ellie
  LINE: I won't...is Missy in heaven, do you think?
  EXPRESSION: Anxious
- CHARACTER: Louis
  LINE: I don't know, honey. Different people believe all sorts of different things happen to us when we die. Some believe in heaven or hell. Some think we're born again as little children—
  EXPRESSION: Pondering
- CHARACTER: Ellie
  LINE: Sure, carnation. Like in that movie you rented, Audrey Rose.
  EXPRESSION: Misunderstanding
- CHARACTER: Louis
  LINE: Well, it's actually reincarnation, but you get the idea. And some people think we just wink out...like a candle flame when the wind blows hard.
  EXPRESSION: Explaining
- CHARACTER: Ellie
  LINE: Do you believe that?
  EXPRESSION: Curious

::PATHS::
- CHOICE: "Explain belief"
  TARGET: living_room_sofa_louis_pov
  STATE_CHANGE: none
  CONDITION: null

::SCENE::
LOCATION: The Living Room Sofa, With Church, Louis's POV
MOOD: Peaceful
CHARACTERS: Church
BACKGROUND_IMAGE: living_room_sofa_church_pov.png
BACKGROUND_EDIT: "Nighttime, living room, Church is asleep on the sofa."

::SCRIPT::
- CHARACTER: Narrator
  LINE: CHURCH is sleeping.
  EXPRESSION: null

::PATHS::
- CHOICE: "Return to Louis and Ellie"
  TARGET: louis_ellie
  STATE_CHANGE: none
  CONDITION: null

::SCENE::
LOCATION: Louis and Ellie
MOOD: Reassuring, Philosophical
CHARACTERS: Louis, Ellie
BACKGROUND_IMAGE: louis_ellie_return.png
BACKGROUND_EDIT: "Nighttime, living room, Ellie is on Louis's lap."

::SCRIPT::
- CHARACTER: Louis
  LINE: I think we go on. I'm not sure what happens after we die, but yeah-- I have faith in that.
  EXPRESSION: Confident
- CHARACTER: Ellie
  LINE: You believe in it.
  EXPRESSION: Hopeful
- CHARACTER: Louis
  LINE: Oh, faith's a little more than just believing.
  EXPRESSION: Clarifying

::PATHS::
- CHOICE: "Explain faith"
  TARGET: rachel_kitchen_door
  STATE_CHANGE: none
  CONDITION: null

::SCENE::
LOCATION: Rachel, At the Kitchen Door
MOOD: Attentive
CHARACTERS: Rachel
BACKGROUND_IMAGE: rachel_kitchen_door.png
BACKGROUND_EDIT: "Nighttime, kitchen doorway, Rachel is listening."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Listening intently.
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue explaining"
  TARGET: louis_ellie_continue
  STATE_CHANGE: none
  CONDITION: null

::SCENE::
LOCATION: Louis and Ellie
MOOD: Explanatory, Comforting
CHARACTERS: Louis, Ellie
BACKGROUND_IMAGE: louis_ellie_continue.png
BACKGROUND_EDIT: "Nighttime, living room, Ellie is on Louis's lap."

::SCRIPT::
- CHARACTER: Louis
  LINE: I'll tell you what faith is--it's the evidence of the heart; the assurance of things not seen.
  EXPRESSION: Wise
- CHARACTER: Ellie
  LINE: I don't get it.
  EXPRESSION: Confused
- CHARACTER: Louis
  LINE: Well, here we are, sitting in my chair. Do you think my chair will be here tomorrow?
  EXPRESSION: Illustrative
- CHARACTER: Ellie
  LINE: Yeah, sure.
  EXPRESSION: Certain
- CHARACTER: Louis
  LINE: Then you have faith in that. But we don't know it will be; after all, some crazed chair-burglar might break in while we’re away and steal it, right?
  EXPRESSION: Playful
- CHARACTER: Narrator
  LINE: ELLIE'S giggling.
  EXPRESSION: null

::PATHS::
- CHOICE: "Observe Rachel's reaction"
  TARGET: rachel_door_smile
  STATE_CHANGE: none
  CONDITION: null

::SCENE::
LOCATION: Rachel, At the Door
MOOD: Emotional, Understanding
CHARACTERS: Rachel
BACKGROUND_IMAGE: rachel_door_smile.png
BACKGROUND_EDIT: "Nighttime, doorway to the living room, Rachel is smiling through tears."

::SCRIPT::
- CHARACTER: Narrator
  LINE: She's smiling, too...but tears are running down her cheeks.
  EXPRESSION: null

::PATHS::
- CHOICE: "Conclude the conversation"
  TARGET: louis_ellie_conclusion
  STATE_CHANGE: none
  CONDITION: null

::SCENE::
LOCATION: Louis and Ellie
MOOD: Loving, Concluding
CHARACTERS: Louis, Ellie
BACKGROUND_IMAGE: louis_ellie_conclusion.png
BACKGROUND_EDIT: "Nighttime, living room, Louis is holding Ellie."

::SCRIPT::
- CHARACTER: Louis
  LINE: But we plan on that chair. We believe in that chair. And I plan on going on somehow as Louis Creed, after I die. it is now time for Ellen Creed to get ready for bed. So buzz.
  EXPRESSION: Reassuring
- CHARACTER: Narrator
  LINE: He gets her off his lap.
  EXPRESSION: null
- CHARACTER: Ellie
  LINE: I'm not tired!
  EXPRESSION: Stubborn
- CHARACTER: Louis
  LINE: I’m sure you’re not.
  EXPRESSION: Understanding
- CHARACTER: Ellie
  LINE: Then why do I have to go to bed?
  EXPRESSION: Questioning
- CHARACTER: Louis
  LINE: Because your mother and I need the rest, sugar. Now buzz.
  EXPRESSION: Firm but loving
- CHARACTER: Narrator
  LINE: She heads toward the stairs.
  EXPRESSION: null

::PATHS::
- CHOICE: "Go to the bedroom"
  TARGET: louis_rachel_bedroom
  STATE_CHANGE: none
  CONDITION: null

::SCENE::
LOCATION: Louis and Rachel’s Bedroom
MOOD: Intimate, Reflective
CHARACTERS: Louis, Rachel
BACKGROUND_IMAGE: louis_rachel_bedroom.png
BACKGROUND_EDIT: "Nighttime, bedroom, Louis is reading in bed, Rachel enters."

::SCRIPT::
- CHARACTER: Narrator
  LINE: LOUIS is in bed, reading. RACHEL, wearing a robe over her nightgown, comes in.
  EXPRESSION: null
- CHARACTER: Rachel
  LINE: I heard you tonight.
  EXPRESSION: Softly
- CHARACTER: Louis
  LINE: I thought maybe you did. I know you don't approve of the subject being raised—
  EXPRESSION: Gentle
- CHARACTER: Rachel
  LINE: That's not true. The subject scares me. Because of Zelda.
  EXPRESSION: Vulnerable
- CHARACTER: Narrator
  LINE: Louis puts his book down and looks at her thoughtfully.
  EXPRESSION: null
- CHARACTER: Louis
  LINE: Your sister, I know.
  EXPRESSION: Understanding
- CHARACTER: Narrator
  LINE: RACHEL sits down on the end of the bed. She’s clasping her hands nervously together.
  EXPRESSION: null
- CHARACTER: Rachel
  LINE: Sometimes you're so good with her, Louis--so straight with her--that you make me ashamed of myself.
  EXPRESSION: Regretful
- CHARACTER: Narrator
  LINE: Louis sits up and scoots down the bed to her. He tries to put an arm around her. She rejects it--but gently.
  EXPRESSION: null
- CHARACTER: Rachel
  LINE: I’m sorry I couldn't go with you to Missy's funeral. And that I blew up when we went to that silly animal graveyard.
  EXPRESSION: Apologetic
- CHARACTER: Louis
  LINE: That’s forgotten.
  EXPRESSION: Forgiving
- CHARACTER: Rachel
  LINE: Not by me, it isn't. I know how badly I acted, how unfair I was. It's just that I..you know.
  EXPRESSION: Remorseful
- CHARACTER: Louis
  LINE: Yes, I guess I do.
  EXPRESSION: Empathetic
- CHARACTER: Narrator
  LINE: He makes a place for her beside him and hugs her. They lie silently together for awhile, taking comfort from each other.
  EXPRESSION: null
- CHARACTER: Rachel
  LINE: I'm going to try to do better.
  EXPRESSION: Hopeful
- CHARACTER: Louis
  LINE: You're doing fine.
  EXPRESSION: Reassuring
- CHARACTER: Narrator
  LINE: DISSOLVE TO: BLACK. And on it, a fifth title card: GAGE.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: SOUND: An idling truck motor.
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue the story"
  TARGET: grille_truck_day
  STATE_CHANGE: none
  CONDITION: null

::SCENE::
LOCATION: The Grille of a Truck
MOOD: Imposing
CHARACTERS: Narrator
BACKGROUND_IMAGE: grille_truck_day.png
BACKGROUND_EDIT: "Daytime, close-up of a large truck's grille."

::SCRIPT::
- CHARACTER: Narrator
  LINE: It looks monstrous...as high as a mountain.
  EXPRESSION: Awestruck

::PATHS::
- CHOICE: "View the truck from a different angle"
  TARGET: truck_new_angle
  STATE_CHANGE: none
  CONDITION: null

::SCENE::
LOCATION: The Truck, A New Angle
MOOD: Industrial, Moving
CHARACTERS: Narrator, Driver
BACKGROUND_IMAGE: truck_new_angle.png
BACKGROUND_EDIT: "Daytime, an Orinco tanker truck."

::SCRIPT::
- CHARACTER: Narrator
  LINE: It’s an Orinco tanker. The driver, a young man in khaki fatigues and a baseball cap, climbs up into the cab. He slams the door and jams the truck into gear.
  EXPRESSION: null
- CHARACTER: Irwin Goldman (Voice)
  LINE: I knew something like this would happen.
  EXPRESSION: Foreboding

::PATHS::
- CHOICE: "Observe the truck leaving"
  TARGET: orinco_shipping_yard
  STATE_CHANGE: none
  CONDITION: null

::SCENE::
LOCATION: The Orinco Shipping Yard
MOOD: Ominous, Transition
CHARACTERS: Narrator, Driver, Irwin Goldman (Voice)
BACKGROUND_IMAGE: orinco_shipping_yard_day.png
BACKGROUND_EDIT: "Daytime, a large tanker truck moving towards the main gate."

::SCRIPT::
- CHARACTER: Narrator
  LINE: The truck comes rolling slowly toward the main gate...stops so the driver can look both ways...and then pulls slowly out onto ROUTE 9.
  EXPRESSION: null
- CHARACTER: Irwin Goldman (Voice)
  LINE: I told her when you were first married. ’You'll have all the grief you can stand, and more,' I said.
  EXPRESSION: Melancholy

::PATHS::
- CHOICE: "Witness the funeral chapel scene"
  TARGET: funeral_chapel_irwin_louis_day
  STATE_CHANGE: none
  CONDITION: null

::SCENE::
LOCATION: A Funeral Chapel, With Irwin Goldman and Louis
MOOD: Devastated, Tense
CHARACTERS: Irwin Goldman, Louis, Others
BACKGROUND_IMAGE: funeral_chapel_irwin_louis_day.png
BACKGROUND_EDIT: "Daytime, a funeral chapel, Irwin Goldman is agitated, Louis is stunned."

::SCRIPT::
- CHARACTER: Narrator
  LINE: There are others here, but they are in the b.g., and concentrating on the scene the old man is making. He's RACHEL’S dad. LOUIS is sitting in the aisle seat of a pew-like bench. He looks terribly shattered- -they both do, actually. He's staring at the old man as if he cannot in the least comprehend what he's saying.
  EXPRESSION: null
- CHARACTER: Irwin Goldman
  LINE: And now look at this!
  EXPRESSION: Agitated
- CHARACTER: Narrator
  LINE: He gestures to
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue observing"
  TARGET: end
  STATE_CHANGE: none
  CONDITION: null

::SCENE::
LOCATION: The Front of the Funeral Chapel
MOOD: Somber
CHARACTERS: Narrator
BACKGROUND_IMAGE: funeral_chapel_front.png
BACKGROUND_EDIT: "Child-sized coffin surrounded by floral tributes"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Here, half-buried in floral tributes, is a child-sized coffin.
  EXPRESSION: null

::SCENE::
LOCATION: Irwin and Louis
MOOD: Grief-stricken
CHARACTERS: Irwin
BACKGROUND_IMAGE: irwin_louis.png
BACKGROUND_EDIT: "Interior, day"

::SCRIPT::
- CHARACTER: Irwin
  LINE: Run over in the road like a...a chipmunk!
  EXPRESSION: Weeping

::SCENE::
LOCATION: Route 9, with Truck
MOOD: Accelerating
CHARACTERS: Narrator
BACKGROUND_IMAGE: route_9_truck.png
BACKGROUND_EDIT: "Daytime, truck getting up to speed"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Getting up to speed.
  EXPRESSION: null

::SCENE::
LOCATION: A Kite, CU
MOOD: Playful
CHARACTERS: Louis, Narrator
BACKGROUND_IMAGE: kite_cu.png
BACKGROUND_EDIT: "Close-up of a hand holding a kite string, kite beginning to move"

::SCRIPT::
- CHARACTER: Narrator
  LINE: There's a hand holding it—LOUIS'S. The kite begins to move and THE CAMERA TRACKS IT. It flaps and flutters.
  EXPRESSION: null

::SCENE::
LOCATION: The Field Beside the Creed House, with Louis
MOOD: Joyful
CHARACTERS: Louis, Ellie, Narrator
BACKGROUND_IMAGE: field_louis_kite.png
BACKGROUND_EDIT: "Louis running with a kite under a gorgeous fall sky"

::SCRIPT::
- CHARACTER: Narrator
  LINE: He runs with the kite beneath a gorgeous fall sky in which fat clouds move like airy ocean liners.
  EXPRESSION: null
- CHARACTER: Ellie
  LINE: Go, daddy!
  EXPRESSION: Excited

::SCENE::
LOCATION: A Picnic Table
MOOD: Lighthearted
CHARACTERS: Rachel, Ellie, Gage, Jud Crandall, Narrator
BACKGROUND_IMAGE: picnic_table.png
BACKGROUND_EDIT: "Remains of a picnic lunch, daytime"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The remains of a picnic lunch are spread here. Looks like everyone ate well. In attendance: RACHEL, ELLIE, GAGE, and JUD CRANDALL.
  EXPRESSION: null
- CHARACTER: Gage
  LINE: Go, dayee!
  EXPRESSION: Excited
- CHARACTER: Narrator
  LINE: They all laugh--JUD ruffles the kid's hair.
  EXPRESSION: null

::SCENE::
LOCATION: Louis, Running with the Kite
MOOD: Ascending
CHARACTERS: Louis, Narrator
BACKGROUND_IMAGE: louis_running_kite.png
BACKGROUND_EDIT: "Louis is paying out string as the kite goes up"

::SCRIPT::
- CHARACTER: Narrator
  LINE: He's paying out string--and the kite is going up.
  EXPRESSION: null
- CHARACTER: Louis
  LINE: Where’s Rachel?
  EXPRESSION: null

::SCENE::
LOCATION: The Funeral Chapel, with Louis and Irwin
MOOD: Tense
CHARACTERS: Irwin, Louis
BACKGROUND_IMAGE: funeral_chapel_louis_irwin.png
BACKGROUND_EDIT: "Interior, day"

::SCRIPT::
- CHARACTER: Narrator
  LINE: IRWIN looks toward:
  EXPRESSION: null

::SCENE::
LOCATION: The Back of the Chapel, with Rachel and Dory Goldman
MOOD: Distraught
CHARACTERS: Rachel, Dory Goldman
BACKGROUND_IMAGE: chapel_back_rachel_dory.png
BACKGROUND_EDIT: "By the sign-in book, dressed in black, looking haggard"

::SCRIPT::
- CHARACTER: Narrator
  LINE: They are by the sign-in book. Both are dressed in black. Both look haggard. But RACHEL looks more than haggard; she looks damned near insane with grief and horror.
  EXPRESSION: null

::SCENE::
LOCATION: Louis and Irwin
MOOD: Furious
CHARACTERS: Irwin, Louis
BACKGROUND_IMAGE: louis_irwin_furious.png
BACKGROUND_EDIT: "Interior, day"

::SCRIPT::
- CHARACTER: Irwin
  LINE: with her mother! where she should be! As for you, I hope you rot in hell! In hell, do you hear me?
  EXPRESSION: Enraged
- CHARACTER: Narrator
  LINE: We should; by now he's screaming his head off.
  EXPRESSION: null

::SCENE::
LOCATION: The Cab of the Orinco Truck
MOOD: Carefree
CHARACTERS: Trucker
BACKGROUND_IMAGE: orinco_truck_cab.png
BACKGROUND_EDIT: "Daytime, trucker whistling, transistor radio on"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The driver is whistling. A transistor radio hangs from the rear­ view mirror on a strap. He turns it on. The Ramones. "Sheena."
  EXPRESSION: null

::SCENE::
LOCATION: Route 9, Trucker's POV
MOOD: Fast-paced
CHARACTERS: Narrator
BACKGROUND_IMAGE: route_9_truckers_pov.png
BACKGROUND_EDIT: "Unrolling road at a good clip"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Unrolling before us at a good clip--too good, maybe.
  EXPRESSION: null

::SCENE::
LOCATION: The Trucker's Foot
MOOD: Urgent
CHARACTERS: Narrator
BACKGROUND_IMAGE: trucker_foot.png
BACKGROUND_EDIT: "Close-up of foot pressing the gas pedal"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Stamping the pedal closer to the metal.
  EXPRESSION: null

::SCENE::
LOCATION: The Oncoming Truck
MOOD: Menacing
CHARACTERS: Narrator
BACKGROUND_IMAGE: oncoming_truck.png
BACKGROUND_EDIT: "Truck belting toward the camera, sound of a growling engine"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Belting toward THE CAMERA. SOUND of the GROWLING ENGINE.
  EXPRESSION: null

::SCENE::
LOCATION: The Sky, with the Kite
MOOD: Ascending
CHARACTERS: Narrator
BACKGROUND_IMAGE: sky_kite_ascend.png
BACKGROUND_EDIT: "Kite is flying high in the sky"

::SCRIPT::
- CHARACTER: Narrator
  LINE: LOUIS has clearly gotten it up okay.
  EXPRESSION: null

::SCENE::
LOCATION: Louis, in the Field
MOOD: Content
CHARACTERS: Louis, Gage, Narrator
BACKGROUND_IMAGE: louis_field_kite_content.png
BACKGROUND_EDIT: "Louis holding the string, looking up, then back at the picnic table"

::SCRIPT::
- CHARACTER: Narrator
  LINE: He’s holding the string, looking up at the sky. now he looks back at the picnic table.
  EXPRESSION: null
- CHARACTER: Louis
  LINE: Hey, Gage!
  EXPRESSION: Playful

::SCENE::
LOCATION: The Picnic Table
MOOD: Engaged
CHARACTERS: Gage, Louis, Narrator
BACKGROUND_IMAGE: picnic_table_gage_louis.png
BACKGROUND_EDIT: "Gage gets down and runs toward his father"

::SCRIPT::
- CHARACTER: Narrator
  LINE: GAGE gets down and runs toward his father.
  EXPRESSION: null

::SCENE::
LOCATION: Route 9 with the Orinco Tanker
MOOD: Fast
CHARACTERS: Narrator
BACKGROUND_IMAGE: route_9_tanker.png
BACKGROUND_EDIT: "Orinco tanker belting along fast, sound of The Ramones"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Belting along fast. SOUND of the Ramones.
  EXPRESSION: null

::SCENE::
LOCATION: The Field, with Louis and Gage
MOOD: Bonding
CHARACTERS: Gage, Louis, Narrator
BACKGROUND_IMAGE: field_louis_gage_kite.png
BACKGROUND_EDIT: "Gage runs to his dad, Louis transfers the kite string to Gage's hands"

::SCRIPT::
- CHARACTER: Narrator
  LINE: GAGE runs to his dad, chubby legs working. He reaches him, and LOUIS transfers thee ball of string to GAGE’S hands.
  EXPRESSION: null
- CHARACTER: Gage
  LINE: Dat?
  EXPRESSION: Inquisitive
- CHARACTER: Louis
  LINE: String! You're flying it. Gage--you got the hammer, my man!
  EXPRESSION: Encouraging
- CHARACTER: Gage
  LINE: Gage fline it?
  EXPRESSION: Eager
- CHARACTER: Louis
  LINE: Bet your boots. Look--
  EXPRESSION: Confident
- CHARACTER: Narrator
  LINE: LOUIS puts his hands over GAGE'S hands and pulls them down.
  EXPRESSION: null

::SCENE::
LOCATION: The Kite
MOOD: Wavering
CHARACTERS: Narrator
BACKGROUND_IMAGE: kite_dipping.png
BACKGROUND_EDIT: "Kite dips in the sky"

::SCRIPT::
- CHARACTER: Narrator
  LINE: It dips in the sky.
  EXPRESSION: null

::SCENE::
LOCATION: Louis and Gage
MOOD: Proud
CHARACTERS: Louis, Gage, Narrator
BACKGROUND_IMAGE: louis_gage_proud.png
BACKGROUND_EDIT: "Louis and Gage looking up at the kite"

::SCRIPT::
- CHARACTER: Louis
  LINE: See?
  EXPRESSION: Proud
- CHARACTER: Gage
  LINE: Gage fline it!!
  EXPRESSION: Elated
- CHARACTER: Louis
  LINE: Bet your ass, little hero.
  EXPRESSION: Affectionate
- CHARACTER: Narrator
  LINE: He kisses his son. They look up at:
  EXPRESSION: null

::SCENE::
LOCATION: The Kite
MOOD: Majestic
CHARACTERS: Narrator
BACKGROUND_IMAGE: kite_majestic.png
BACKGROUND_EDIT: "Kite dipping and drifting in a gorgeous fall sky"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Dipping and drifting in that gorgeous fall sky.
  EXPRESSION: null

::SCENE::
LOCATION: Irwin Goldman (Voice)
MOOD: Accusatory
CHARACTERS: Irwin Goldman
BACKGROUND_IMAGE: irwin_goldman_voice.png
BACKGROUND_EDIT: "N/A"

::SCRIPT::
- CHARACTER: Irwin Goldman
  LINE: Where were you while he was playing in the road? Thinking about your stupid medical articles? You stinking shit! You killer of children!
  EXPRESSION: Furious

::SCENE::
LOCATION: The Funeral Chapel, with Louis and Irwin
MOOD: Violent
CHARACTERS: Irwin, Louis, Narrator
BACKGROUND_IMAGE: funeral_chapel_louis_irwin_fight.png
BACKGROUND_EDIT: "Irwin punches Louis, who sprawls backward onto the floor"

::SCRIPT::
- CHARACTER: Narrator
  LINE: IRWIN
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: But there is no way he can express his outrage with mere words. As LOUIS sits staring numbly up at him, IRWIN punches him in the nose. LOUIS sprawls backward, falling out of the pew onto the floor.
  EXPRESSION: null

::SCENE::
LOCATION: The Rear of the Chapel, Featuring Rachel and Dory
MOOD: Panicked
CHARACTERS: Rachel, Dory
BACKGROUND_IMAGE: chapel_rear_rachel_dory_panic.png
BACKGROUND_EDIT: "Rachel screams and starts forward, Dory pulls her back"

::SCRIPT::
- CHARACTER: Narrator
  LINE: RACHEL screams and starts forward. DORY pulls her back.
  EXPRESSION: null
- CHARACTER: Rachel
  LINE: Louis! Daddy! Stop it! STOP IT!
  EXPRESSION: Distraught

::SCENE::
LOCATION: Louis and Irwin
MOOD: Painful
CHARACTERS: Louis, Irwin, Narrator
BACKGROUND_IMAGE: louis_irwin_painful.png
BACKGROUND_EDIT: "Louis getting up groggily, nose pouring blood. Irwin punches him in the stomach."

::SCRIPT::
- CHARACTER: Narrator
  LINE: LOUIS is getting up groggily. Hs nose is pouring blood.
  EXPRESSION: null
- CHARACTER: Irwin
  LINE: How do you like that, you son of a bitch? I should have done it sooner!
  EXPRESSION: Vicious
- CHARACTER: Narrator
  LINE: IRWIN punches him in the stomach. LOUIS "oofs” arid doubles over.
  EXPRESSION: null

::SCENE::
LOCATION: Angle on the Other Mourners
MOOD: Concerned
CHARACTERS: Steve Masterton, Marcy Charlton, Narrator
BACKGROUND_IMAGE: mourners_steve_marcy.png
BACKGROUND_EDIT: "Mourners watching the altercation"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Among them we see STEVE MASTERTON and MARCY CHARLTON.
  EXPRESSION: null
- CHARACTER: Steve
  LINE: Hey!
  EXPRESSION: Concerned

::SCENE::
LOCATION: Louis and Irwin
MOOD: Escalating
CHARACTERS: Louis, Irwin, Narrator
BACKGROUND_IMAGE: louis_irwin_escalating.png
BACKGROUND_EDIT: "Louis slowly straightening up. Irwin is in a sour frenzy of glee. Louis pushes Irwin."

::SCRIPT::
- CHARACTER: Narrator
  LINE: LOUIS is slowly straightening up. IRWIN is in a sour frenzy of glee.
  EXPRESSION: null
- CHARACTER: Irwin
  LINE: How do you like that? How do--
  EXPRESSION: Gleeful
- CHARACTER: Narrator
  LINE: LOUIS pushes the old man with both hands.
  EXPRESSION: null

::SCENE::
LOCATION: Irwin Goldman
MOOD: Chaotic
CHARACTERS: Irwin, Narrator
BACKGROUND_IMAGE: irwin_goldman_falling.png
BACKGROUND_EDIT: "Irwin stumbling backwards, striking the coffin, knocking it off its bier"

::SCRIPT::
- CHARACTER: Narrator
  LINE: He goes stumbling and flailing backwards... strikes the coffin, knocks it off its bier. A SCREAM goes up from the mourners.
  EXPRESSION: null

::SCENE::
LOCATION: Rachel and Dory
MOOD: Desperate
CHARACTERS: Rachel, Dory, Narrator
BACKGROUND_IMAGE: rachel_dory_desperate.png
BACKGROUND_EDIT: "Rachel screams and breaks free, running down the aisle"

::SCRIPT::
- CHARACTER: Narrator
  LINE: RACHEL screams. Her mother struggles to hold her but RACHEL easily breaks free and goes running down the aisle.
  EXPRESSION: null

::SCENE::
LOCATION: Angle on Mourners, with Marcy and Steve
MOOD: Urgent Intervention
CHARACTERS: Marcy, Steve, Narrator
BACKGROUND_IMAGE: mourners_marcy_steve_intervention.png
BACKGROUND_EDIT: "Marcy tells Steve to stop them. Steve gets up and goes toward the front."

::SCRIPT::
- CHARACTER: Marcy
  LINE: Stop them. Right now.
  EXPRESSION: Urgent
- CHARACTER: Narrator
  LINE: STEVE gets up and goes toward:
  EXPRESSION: null

::SCENE::
LOCATION: The Front of the Chapel, with Irwin
MOOD: Disheveled
CHARACTERS: Irwin, Louis, Steve, Narrator
BACKGROUND_IMAGE: chapel_front_irwin_disheveled.png
BACKGROUND_EDIT: "Irwin picking himself out of a mess of coffin and floral tributes, suit wet."

::SCRIPT::
- CHARACTER: Narrator
  LINE: He's picking himself out of a tangled mess of coffin and overturned floral tributes. His suit is wet from spilled water. He's weeping.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: LOUIS has just reached him, and that stunned look is gone. I think he intends to do the Cool Jerk all over IRWIN GOLDMAN'S puny little body. IRWIN strikes a Gentleman Jim Corbett pugilistic pose.
  EXPRESSION: null
- CHARACTER: Irwin
  LINE: Come on! I'm ready for ya! I'll take y'apart!
  EXPRESSION: Defiant
- CHARACTER: Narrator
  LINE: As LOUIS wades in, STEVE MASTERTON gets between them...at the last possible moment.
  EXPRESSION: null
- CHARACTER: Steve
  LINE: Stop it!
  EXPRESSION: Calming
- CHARACTER: Narrator
  LINE: LOUIS swings. STEVE manages to block the punch with his body.
  EXPRESSION: null
- CHARACTER: Steve
  LINE: Stop it! Jesus, what's wrong with you, Louis? It's your son's funeral, not a boxing match!
  EXPRESSION: Exasperated
- CHARACTER: Narrator
  LINE: That gets to LOUIS. He drops his fists. That stunned expression creeps over his face again--that look that says he doesn't have the slightest clue as to what’s going on or how it could possibly have happened.
  EXPRESSION: null

::SCENE::
LOCATION: Louis
MOOD: Realization
CHARACTERS: PasCow (voice), Louis, Narrator
BACKGROUND_IMAGE: louis_realization.png
BACKGROUND_EDIT: "Louis turns toward PasCow"

::SCRIPT::
- CHARACTER: PasCow
  LINE: The soil of a man’s heart is stonier, doc--
  EXPRESSION:null
- CHARACTER: Narrator
  LINE: LOUIS turns toward:
  EXPRESSION: null

::SCENE::
LOCATION: The Front Pew, with PasCow and Church
MOOD: Solitary
CHARACTERS: PasCow, Church, Narrator
BACKGROUND_IMAGE: front_pew_pasCow_church.png
BACKGROUND_EDIT: "PasCow, bloody, with Church on his lap, purring"

::SCRIPT::
- CHARACTER: PasCow
  LINE: A man grows what he can...and tends it.
  EXPRESSION:null

::SCENE::
LOCATION: Louis, CU
MOOD: Devastated
CHARACTERS: Louis, Narrator
BACKGROUND_IMAGE: louis_cu_sob.png
BACKGROUND_EDIT: "Close-up of Louis's face, covering it with his hands and sobbing"

::SCRIPT::
- CHARACTER: Narrator
  LINE: A sense of horrible awareness comes into his face...and then he covers it with his hands and begins to SOB.
  EXPRESSION: null
SOUND: Coming up: A truck motor.

::SCENE::
LOCATION: The Cab of the Tanker
MOOD: Mundane
CHARACTERS: Trucker
BACKGROUND_IMAGE: tanker_cab_singing.png
BACKGROUND_EDIT: "Trucker singing along with the radio"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The trucker is singing along with the radio.
  EXPRESSION: null

::SCENE::
LOCATION: The Gas Pedal
MOOD: Accelerating
CHARACTERS: Narrator
BACKGROUND_IMAGE: gas_pedal.png
BACKGROUND_EDIT: "Gas pedal closer to the floorboards than ever"

::SCRIPT::
- CHARACTER: Narrator
  LINE: It’s closer to the floorboards than ever.
  EXPRESSION: null

::SCENE::
LOCATION: Louis and Gage with the Kite, in the Field
MOOD: Unaware
CHARACTERS: Louis, Gage, Narrator
BACKGROUND_IMAGE: louis_gage_kite_field_distant.png
BACKGROUND_EDIT: "Distant view of Louis and Gage close to the road, kite in the air"

::SCRIPT::
- CHARACTER: Narrator
  LINE: We are at some distance--far enough to see that the two of them have moved quite close to the road.
  EXPRESSION: null

::SCENE::
LOCATION: Louis and Gage, a New Angle (Kite's POV)
MOOD: Foreshadowing
CHARACTERS: Louis, Gage, Narrator
BACKGROUND_IMAGE: louis_gage_kite_pov.png
BACKGROUND_EDIT: "Faces upturned, amplified rattling sound of the kite. Camera pans to the road, truck visible and approaching."

::SCRIPT::
- CHARACTER: Narrator
  LINE: We can see their faces upturned to us--we can hear the AMPLIFIED RATTLING SOUND of the kite itself. THE CAMERA PANS TO THE LEFT--to the road. And we can see the truck, fairly close by now, and coming closer.
  EXPRESSION: null

::SCENE::
LOCATION: The Picnic Table, with Rachel, Ellie, and Jud
MOOD: Normalcy
CHARACTERS: Jud, Ellie, Rachel, Narrator
BACKGROUND_IMAGE: picnic_table_normalcy.png
BACKGROUND_EDIT: "Jud lighting a cigarette, Walkman phones around his neck. Ellie asks to fly the kite."

::SCRIPT::
- CHARACTER: Jud
  LINE: null
  EXPRESSION: null
- CHARACTER: Ellie
  LINE: I want to fly it! Can I fly it now, mommy!
  EXPRESSION: Eager
- CHARACTER: Rachel
  LINE: In a minute, hon. Let Gage finish his turn.
  EXPRESSION: Patient

::SCENE::
LOCATION: Louis and Gage
MOOD: Fleeting Happiness
CHARACTERS: Louis, Gage, Narrator
BACKGROUND_IMAGE: louis_gage_kite_last_moment.png
BACKGROUND_EDIT: "Louis and Gage stare up at the kite, a moment of happiness"

::SCRIPT::
- CHARACTER: Narrator
  LINE: This is the last moment of happiness in this man’s life--so let’s make it very happy. As he and GAGE stare up at the kite:
  EXPRESSION: null
- CHARACTER: Irwin
  LINE: Jesus. Louis. I'm sorry--
  EXPRESSION: Apologetic

::SCENE::
LOCATION: The Funeral Chapel
MOOD: Resolution
CHARACTERS: Irwin, Steve, Rachel, Narrator
BACKGROUND_IMAGE: funeral_chapel_resolution.png
BACKGROUND_EDIT: "Irwin and Steve have backed away. Mourners gathered at the front. Rachel and her mother weeping."

::SCRIPT::
- CHARACTER: Narrator
  LINE: The fight has gone out of IRWIN and STEVE has backed away--but cautiously. He's ready to jump back in if one or the other goes mad again. But IRWIN is shuffling toward LOUIS, hands out--everyone else has gathered in a knot near the front of the chapel. Among them is RACHEL and her mother, weeping in each others' arms.
  EXPRESSION: null
- CHARACTER: Irwin
  LINE: I don't know what happened to me. Louis, please--
  EXPRESSION: Remorseful
- CHARACTER: Narrator
  LINE: LOUIS brushes by him with no acknowledgement that IRWIN even exists. He kneels down slowly by the coffin and puts his head against it.
  EXPRESSION: null

::SCENE::
LOCATION: Louis (Weeping)
MOOD: Heartbroken
CHARACTERS: Louis, Narrator
BACKGROUND_IMAGE: louis_weeping_coffin.png
BACKGROUND_EDIT: "Louis kneels by the coffin, weeping"

::SCRIPT::
- CHARACTER: Louis
  LINE: I’m sorry, Gage--I’m so sorry, little hero.
  EXPRESSION: Weeping

::SCENE::
LOCATION: Louis and Gage, in the Field
MOOD: Sudden Loss
CHARACTERS: Gage, Narrator
BACKGROUND_IMAGE: louis_gage_field_wind.png
BACKGROUND_EDIT: "Strong gust of wind, ball of string falls from Gage's hand"

::SCRIPT::
- CHARACTER: Narrator
  LINE: There's a strong gust of wind. The ball of string falls out of GAGE'S hand.
  EXPRESSION: null

::SCENE::
LOCATION: The Kite, Blowing Away
MOOD: Uncontrolled
CHARACTERS: Narrator
BACKGROUND_IMAGE: kite_blowing_away.png
BACKGROUND_EDIT: "Kite is blowing away in the wind"

::SCRIPT::
- CHARACTER: Narrator
  LINE: It got away from him! That numb shit!
  EXPRESSION: null

::SCENE::
LOCATION: The Picnic Table
MOOD: Outraged
CHARACTERS: Ellie, Rachel, Narrator
BACKGROUND_IMAGE: picnic_table_ellie_outraged.png
BACKGROUND_EDIT: "Ellie's outburst about the kite getting away"

::SCRIPT::
- CHARACTER: Ellie
  LINE: It got away from him! That numb shit!
  EXPRESSION: Outraged
- CHARACTER: Rachel
  LINE: Ellen Creed!
  EXPRESSION: Reprimanding

::SCENE::
LOCATION: The Ball of Kite Twine
MOOD: Drifting
CHARACTERS: Narrator
BACKGROUND_IMAGE: kite_twine_drifting.png
BACKGROUND_EDIT: "Ball of kite twine bouncing, unraveling, and heading toward the highway"

::SCRIPT::
- CHARACTER: Narrator
  LINE: It is bouncing and unraveling. More importantly, it is being carried directly toward the highway.
  EXPRESSION: null

::SCENE::
LOCATION: Gage
MOOD: Chasing
CHARACTERS: Gage, Narrator
BACKGROUND_IMAGE: gage_chasing_twine.png
BACKGROUND_EDIT: "Gage takes off after the ball of twine"

::SCRIPT::
- CHARACTER: Narrator
  LINE: He takes off after the ball of twine.
  EXPRESSION: null
- CHARACTER: Gage
  LINE: Kite fline too fast!
  EXPRESSION: Frustrated
SOUND: The oncoming truck.

::SCENE::
LOCATION: The Truck
MOOD: Imminent
CHARACTERS: Narrator
BACKGROUND_IMAGE: truck_slamming.png
BACKGROUND_EDIT: "Truck slamming toward the camera, a brutal leviathan on eighteen wheels"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Slamming toward us--a brutal leviathan on eighteen wheels.
  EXPRESSION: null

::SCENE::
LOCATION: Louis
MOOD: Unconcerned
CHARACTERS: Louis, Narrator
BACKGROUND_IMAGE: louis_looking_table.png
BACKGROUND_EDIT: "Louis looking toward his people at the picnic table"

::SCRIPT::
- CHARACTER: Narrator
  LINE: He's looking--looking toward his people at the picnic table.
  EXPRESSION: null
- CHARACTER: Louis
  LINE: What can you d-
  EXPRESSION: Shrugs, good-humored
TRUCK SOUND CONTINUES.

::SCENE::
LOCATION: The Picnic Table
MOOD: Alarmed
CHARACTERS: Jud, Rachel, Narrator
BACKGROUND_IMAGE: picnic_table_alarm.png
BACKGROUND_EDIT: "Jud's face registers alarm. Rachel looks and registers terrible alarm."

::SCRIPT::
- CHARACTER: Narrator
  LINE: TRUCK SOUND LOUDER. Alarm hits IUD'S face. He rises.
  EXPRESSION: null
- CHARACTER: Jud
  LINE: Don't let him go in the road, Louis!
  EXPRESSION: Panicked
- CHARACTER: Narrator
  LINE: RACHEL looks; registers terrible alarm.
  EXPRESSION: null
- CHARACTER: Rachel
  LINE: Get him, Louis!
  EXPRESSION: Screaming

::SCENE::
LOCATION: Gage
MOOD: Close Call
CHARACTERS: Gage, Narrator
BACKGROUND_IMAGE: gage_almost_road.png
BACKGROUND_EDIT: "Gage scampering after the kite-twine, which has almost reached the road"

::SCRIPT::
- CHARACTER: Narrator
  LINE: He's still scampering after the bouncing ball of kite-twine, which has now almost reached the road
  EXPRESSION: null
TRUCK SOUND LOUDER.

::SCENE::
LOCATION: Louis
MOOD: Distant
CHARACTERS: Narrator
BACKGROUND_IMAGE: louis_loud_sound.png
BACKGROUND_EDIT: "The truck sound is loud"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The SOUND is loud
  EXPRESSION: null





::SCENE::
LOCATION: The Creed Kitchen
MOOD: Ominous
CHARACTERS: Louis, Dud
BACKGROUND_IMAGE: creed_kitchen.png
BACKGROUND_EDIT: "Night, cluttered kitchen"

::SCRIPT::
- CHARACTER: Narrator
  LINE: all right.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: As LOUIS goes to get a cloth to wipe up the mess:
  EXPRESSION: null
- CHARACTER: Dud
  LINE: I know the Micmacs thought it was a holy place...and then they thought it was a cursed place. That's why they moved on.
  EXPRESSION: null
- CHARACTER: Louis
  LINE: 102.
  EXPRESSION: null
- CHARACTER: Louis
  LINE: Because something called a wendigo soured the ground.
  EXPRESSION: null
- CHARACTER: Dud
  LINE: And because the dead walked.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: LOUIS stops sopping and looks at him.
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue cleaning"
  TARGET: dud_close_up
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Dud (Close Up)
MOOD: Ominous
CHARACTERS: Dud
BACKGROUND_IMAGE: dud_close_up.png
BACKGROUND_EDIT: "Close up on Dud's face"

::SCRIPT::
- CHARACTER: Dud
  LINE: Oh, ayuh. It's been done. What you've been thinking of has been done.
  EXPRESSION: null

::PATHS::
- CHOICE: "Transition to flashback"
  TARGET: country_railroad_station_sepia
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: A Country Railroad Station / Sepia
MOOD: Melancholy
CHARACTERS: Narrator
BACKGROUND_IMAGE: country_railroad_station_sepia.png
BACKGROUND_EDIT: "Late summer, 1944, sepia toned. Station sign reads LUDLOW. 40s cars with gas ration coupons. A hearse. A train approaching."

::SCRIPT::
- CHARACTER: Narrator
  LINE: The time is the late summer of 1944, although I don't believe we need to know that specifically. The sign on the station reads LUDLOW. There are a few 40s cars parked near the station--they have gas-ration coupons on the windshields. And a hearse.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: A train is coming.
  EXPRESSION: null

::PATHS::
- CHOICE: "Observe the undertaker and Bill"
  TARGET: hearse_undertaker_bill_baterman_sepia
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: The Hearse, with Undertaker and Bill Baterman / Sepia
MOOD: Grief
CHARACTERS: Narrator, Undertaker, Bill Baterman
BACKGROUND_IMAGE: hearse_undertaker_bill_baterman_sepia.png
BACKGROUND_EDIT: "Sepia toned. Undertaker talking to Bill Baterman, who wipes his brow. Bill walks away, grief-stricken and bitter."

::SCRIPT::
- CHARACTER: Narrator
  LINE: We can see the UNDERTAKER is trying to talk to BILL BATERMAN, a man in his forties who periodically wipes his brow with a bandana.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: BILL walks away. He doesn't want to talk; he doesn't want comfort.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: He's a grief-stricken, bitter man.
  EXPRESSION: null
- CHARACTER: Jud (Voice Over)
  LINE: Timmy Baterman was on his way home from the war with his Purple Heart when he got killed in some stupid car accident down in Georgia.
  EXPRESSION: null

::PATHS::
- CHOICE: "Witness the coffin unloading"
  TARGET: train_depot_sepia
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: The Train, in front of the Depot / Sepia
MOOD: Somber
CHARACTERS: Narrator, Undertaker, Trainmen, Bill Baterman
BACKGROUND_IMAGE: train_depot_sepia.png
BACKGROUND_EDIT: "Sepia toned. Mail-car door open. Undertaker and trainmen unloading Timmy Baterman's coffin draped in a 48-star flag. Bill Baterman watches balefully."

::SCRIPT::
- CHARACTER: Narrator
  LINE: The door of the mail-car is open. The UNDERTAKER and three trainmen are unloading TIMMY BATERMAN'S coffin, which is draped in a 48-star flag. BILL BATERMAN stands by, watching balefully as they carry his son's final apartment to the back of the hearse and load it in.
  EXPRESSION: null
- CHARACTER: Jud (V-O Continues)
  LINE: Bill was bitter--his son had been in the thick of it two years and then got shot in the leg--a clean flesh-wound. He was supposed to be coming home safe and sound, instead, he come home in a box after all.
  EXPRESSION: null

::PATHS::
- CHOICE: "Follow the hearse"
  TARGET: rear_hearse_sepia
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: The Rear of the Hearse / Sepia
MOOD: Resignation
CHARACTERS: Narrator, Bill Baterman
BACKGROUND_IMAGE: rear_hearse_sepia.png
BACKGROUND_EDIT: "Sepia toned. Hearse doors close and pull away. Camera pans to Bill Baterman staring after it, mopping his brow."

::SCRIPT::
- CHARACTER: Narrator
  LINE: The doors close. The hearse pulls away. THE CAMERA PANS TO BILL BATERMAN, who stands staring balefully after it and mopping his brow.
  EXPRESSION: null
- CHARACTER: Dud (V-O Continues)
  LINE: He wasn't able to get to the bottom of the truth, Louis.
  EXPRESSION: null

::PATHS::
- CHOICE: "Return to the Creed kitchen"
  TARGET: creed_kitchen_louis_jud_night
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: The Creed Kitchen, with Louis and Jud - Night
MOOD: Confrontational
CHARACTERS: Louis, Jud
BACKGROUND_IMAGE: creed_kitchen_louis_jud_night.png
BACKGROUND_EDIT: "Night, Louis and Jud sitting, Louis drinking a beer, staring at Jud."

::SCRIPT::
- CHARACTER: Louis
  LINE: I'll bite--what's the bottom of the truth, Jud?
  EXPRESSION:null
- CHARACTER: Jud
  LINE: Why...that sometimes dead is better. That’s all. Sometimes dead is better.
  EXPRESSION: null
- CHARACTER: Louis (Bitter)
  LINE: Tell that to my wife and little girl.
  EXPRESSION: Bitter
- CHARACTER: Jud
  LINE: It ain't your wife and little girl that's got me worried, Louis.
  EXPRESSION: null

::PATHS::
- CHOICE: "Transition to the cemetery"
  TARGET: ludlow_cemetery_sepia
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: The Ludlow Cemetery / Sepia
MOOD: Desolate
CHARACTERS: Narrator, Bill Baterman
BACKGROUND_IMAGE: ludlow_cemetery_sepia.png
BACKGROUND_EDIT: "Sepia toned dusk. A fresh grave of Timmy Baterman. A truck with only parking lights drives up. Bill Baterman gets out and looks at the grave, then goes to the back of his truck."

::SCRIPT::
- CHARACTER: Narrator
  LINE: We’re featuring a fresh grave...that of TIMMY BATERMAN. A truck, showing only parking lights, turns into the graveyard and drives slowly up to it. It stops, and BILL BATERMAN gets out. HE looks at the grave and then goes to the back of his truck.
  EXPRESSION: null
- CHARACTER: Jud (Voice-Over)
  LINE: Timmy was buried on July 22nd, as I remember.
  EXPRESSION: null

::PATHS::
- CHOICE: "Reveal Bill's intentions"
  TARGET: bill_baterman_truck_sepia
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Bill Baterman at the Back of His Truck / Sepia
MOOD: Sinister
CHARACTERS: Narrator, Bill Baterman
BACKGROUND_IMAGE: bill_baterman_truck_sepia.png
BACKGROUND_EDIT: "Sepia toned dusk. Bill reaches into his truck and brings out a pick and shovel."

::SCRIPT::
- CHARACTER: Narrator
  LINE: He reaches in...and brings out a pick and shovel.
  EXPRESSION: null

::PATHS::
- CHOICE: "Dissolve to Margie"
  TARGET: margie_washburn_porch_sepia
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Margie Washburn, on Her Porch / Sepia
MOOD: Horrified
CHARACTERS: Narrator, Margie Washburn
BACKGROUND_IMAGE: margie_washburn_porch_sepia.png
BACKGROUND_EDIT: "Sepia toned day. Middle-aged woman in 40s attire, holding a rug beater, shading her eyes, staring horrified at something."

::SCRIPT::
- CHARACTER: Narrator
  LINE: She's a middle-aged woman dressed in mid-forties style. She's got a rug-beater in one hand; the other is up to her eyes to shade the sun. She's staring at something, horrified.
  EXPRESSION: null
- CHARACTER: Jud (V-O Continues)
  LINE: It was four or five days later when...
  EXPRESSION: null

::PATHS::
- CHOICE: "Show Timmy Baterman"
  TARGET: country_dirt_road_timmy_baterman_sepia
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: A Country Dirt Road, with Timmy Baterman / Sepia
MOOD: Unsettling
CHARACTERS: Narrator, Timmy Baterman
BACKGROUND_IMAGE: country_dirt_road_timmy_baterman_sepia.png
BACKGROUND_EDIT: "Sepia toned day. Young man in jeans and plaid shirt shambling up the road. Vacant eyes, untucked shirt, wild hair. Healed scars on neck and face, one ear possibly gone."

::SCRIPT::
- CHARACTER: Narrator
  LINE: A young man dressed in Jeans and a plaid shirt is shambling up the road. His eyes are vacant. His shirt is half untucked. His hair is sticking up in a wild crow's-nest thatch. There is an ugly mess of healed scars on his neck and one side of his face. I think one of his ears may be gone--torn off in the accident.
  EXPRESSION: null
- CHARACTER: Jud (V-O Continues)
  LINE: ...Margie Washburn seen him walking up the road toward Yorkie's Livery.
  EXPRESSION: null

::PATHS::
- CHOICE: "Show Margie's reaction"
  TARGET: margie_sepia
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Margie / Sepia
MOOD: Terrified
CHARACTERS: Narrator, Margie
BACKGROUND_IMAGE: margie_sepia.png
BACKGROUND_EDIT: "Sepia toned. Margie screaming faintly."

::SCRIPT::
- CHARACTER: Narrator
  LINE: She's screaming--we hear her faintly.
  EXPRESSION: null

::PATHS::
- CHOICE: "Show Timmy's chilling grin"
  TARGET: timmy_sepia
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Timmy / Sepia
MOOD: Menacing
CHARACTERS: Narrator, Timmy
BACKGROUND_IMAGE: timmy_sepia.png
BACKGROUND_EDIT: "Sepia toned. Timmy turns toward Margie, a faint green light in his eyes. He grins."

::SCRIPT::
- CHARACTER: Narrator
  LINE: He turns toward her and we see a green light like the St. Elmo’s fire in the Little God Swamp glow dimly deep in his eyes. He grins at MARGIE.
  EXPRESSION: null

::PATHS::
- CHOICE: "Show Margie's decision"
  TARGET: front_ludlow_town_offices_margie_sepia
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: In Front of the Ludlow Town Offices, with Margie / Sepia
MOOD: Determined
CHARACTERS: Narrator, Margie
BACKGROUND_IMAGE: front_ludlow_town_offices_margie_sepia.png
BACKGROUND_EDIT: "Sepia toned. Margie hesitates, then walks toward the door of the town offices."

::SCRIPT::
- CHARACTER: Narrator
  LINE: She hesitates for a moment or two and then walks up toward the door.
  EXPRESSION: null
- CHARACTER: Jud (V.O.)
  LINE: Lots of people saw Timmy Baterman walking back and forth between the home place and the town line. But it was Margie...
  EXPRESSION: null

::PATHS::
- CHOICE: "Enter the town offices"
  TARGET: town_offices_margie_sepia
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: The Town Offices, with Margie / Sepia
MOOD: Urgent
CHARACTERS: Narrator, Margie
BACKGROUND_IMAGE: town_offices_margie_sepia.png
BACKGROUND_EDIT: "Sepia toned. Margie in a hallway, in front of a frosted glass door labeled LUDLOW SELECTMEN. She opens it and goes in."

::SCRIPT::
- CHARACTER: Narrator
  LINE: She's in a hallway in front of a door with LUDLOW SELECTMEN printed on the frosted glass. After a moment she opens it and goes in.
  EXPRESSION: null
- CHARACTER: Jud (V.O. Continues)
  LINE: ...who finally got up enough guts to talk to the town fathers about it. She knew it had to be stopped, Louis.
  EXPRESSION: null

::PATHS::
- CHOICE: "Enter the Selectmen's Office"
  TARGET: selectmens_office_sepia
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: The Selectmen's Office / Sepia
MOOD: Serious
CHARACTERS: Narrator, Margie, Jud (Young Man), George Anderson, Alan Purinton, Hannibal Benson
BACKGROUND_IMAGE: selectmens_office_sepia.png
BACKGROUND_EDIT: "Sepia toned. Margie and four men (including young Jud) gathered around a desk. Margie is talking, they are listening. Camera pans the men."

::SCRIPT::
- CHARACTER: Narrator
  LINE: MARGIE and four men are grouped around a desk. She’s talking; they're listening. THE CAMERA LAZILY PANS the four men--one, of course, is JUD as a YOUNG MAN.
  EXPRESSION: null
- CHARACTER: Jud (V.O. Continues)
  LINE: She knew it was an abomination. George Anderson, the town postmaster, was there...and Alan Purinton...Hannibal Benson...and me. I was there.
  EXPRESSION: null

::PATHS::
- CHOICE: "Go to the Baterhan Place"
  TARGET: baterhan_place_sepia_sunset
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: The Baterhan Place / Sepia Sunset
MOOD: Foreboding
CHARACTERS: Narrator, Jud, George Anderson, Alan Purinton, Hannibal Benson
BACKGROUND_IMAGE: baterhan_place_sepia_sunset.png
BACKGROUND_EDIT: "Sepia toned sunset. Ramshackle farm. An old Ford pulls in, the four men get out. Sound of crickets. They approach the door. Jud knocks, no answer. Crazy laughter heard."

::SCRIPT::
- CHARACTER: Narrator
  LINE: It’s a ramshackle old farm which looks remarkably like the estate of that gentleman farmer Jordy Verrill.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: An old Ford pulls into the driveway, and the four men get out.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: SOUND BLEEDS IN: Most of all the SOUND OF THE CRICKETS.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: They go to the door, and JUD is wordlessly elected as the prime honcho. He knocks. No answer. Again. No answer.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: SOUND: Crazy laughter.
  EXPRESSION: null
- CHARACTER: Bill Baterhan (Voice)
  LINE: Stop that, Timmy!
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The four men look at each other.
  EXPRESSION: null
- CHARACTER: Jud
  LINE: Come on.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: They start around to the back.
  EXPRESSION: null

::PATHS::
- CHOICE: "Observe the backyard scene"
  TARGET: backyard_bill_timmy_sepia
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: The Back Yard, with Bill and Timmy / Sepia
MOOD: Disturbing
CHARACTERS: Narrator, Timmy Baterman, Bill Baterman
BACKGROUND_IMAGE: backyard_bill_timmy_sepia.png
BACKGROUND_EDIT: "Sepia toned. Timmy Baterman staring into the setting sun, eyes glowing green. Laughing manically. Bill Baterman, scared, tries to make him stop."

::SCRIPT::
- CHARACTER: Narrator
  LINE: TIMMY BATERHAN is staring directly into the setting sun, his eyes glowing with green fire. He’s laughing like Goofy gone insane.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: BILL, scared, is trying to make him stop, to turn away from the sun.
  EXPRESSION: null

::PATHS::
- CHOICE: "Show the arrival of the four men"
  TARGET: backyard_new_angle_sepia
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: The Back Yard, a New Angle / Sepia
MOOD: Shocking
CHARACTERS: Narrator, Alan, Bill Baterman, Jud, Hannibal
BACKGROUND_IMAGE: backyard_new_angle_sepia.png
BACKGROUND_EDIT: "Sepia toned. The four men come around the side of the house and freeze, seeing Bill and Timmy. Alan exclaims."

::SCRIPT::
- CHARACTER: Narrator
  LINE: The four men come around the side of the house. They freeze when they see BILL and TIMMY.
  EXPRESSION: null
- CHARACTER: Alan
  LINE: Oh holy Jesus look at that.
  EXPRESSION: Shocked
- CHARACTER: Narrator
  LINE: BILL whirls around and sees them.
  EXPRESSION: null
- CHARACTER: Bill
  LINE: You men get out of here!
  EXPRESSION: Agitated
- CHARACTER: Jud
  LINE: I heard your boy was killed down Georgia.
  EXPRESSION: null
- CHARACTER: Bill
  LINE: That was a mistake!
  EXPRESSION: Agitated
- CHARACTER: Hannibal
  LINE: Was it?
  EXPRESSION: null
- CHARACTER: Bill
  LINE: You see him standing there, don’t you? Now get out! Get the Christ off my land!
  EXPRESSION: Enraged
- CHARACTER: Narrator
  LINE: Now TIMMY turns around and comes shambling forward.
  EXPRESSION: null
- CHARACTER: Timmy
  LINE: Ge ow! Ge Cwise off eye an!
  EXPRESSION: Laughing
- CHARACTER: George
  LINE: Oh Jesus, Jud! He's dead! I can smell him!
  EXPRESSION: Revolted
- CHARACTER: Bill
  LINE: He ain’t dead! Give him a day or two and he’ll be fine! Don't you say that!
  EXPRESSION: Desperate
- CHARACTER: Jud
  LINE: Bill, this ain't right--you can see that yourself--
  EXPRESSION: Concerned
- CHARACTER: Bill
  LINE: GET OUT! YOU HEAR? GET OUT!!!
  EXPRESSION: Screaming

::PATHS::
- CHOICE: "Show Timmy's disturbing words"
  TARGET: timmy_baterman_sepia_exclamation
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Timmy Baterman / Sepia
MOOD: Unholy
CHARACTERS: Narrator, Timmy
BACKGROUND_IMAGE: timmy_baterman_sepia_exclamation.png
BACKGROUND_EDIT: "Sepia toned. Timmy laughs, then scratches his cheeks, goring deep grooves. Blood flows sluggishly."

::SCRIPT::
- CHARACTER: Timmy
  LINE: Dead! We love dead! Hate living!
  EXPRESSION: Laughing
- CHARACTER: Narrator
  LINE: Abruptly he reaches up with both hands and scratches down his cheeks, goring deep grooves in his flesh. Blood flows sluggishly out. Very weird blood.
  EXPRESSION: null

::PATHS::
- CHOICE: "Show the group's reaction and Bill's dominance"
  TARGET: entire_group_sepia
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: The Entire Group / Sepia
MOOD: Tense
CHARACTERS: Narrator, Bill, Timmy, Jud, Alan, Hannibal, George
BACKGROUND_IMAGE: entire_group_sepia.png
BACKGROUND_EDIT: "Sepia toned. Bill grabs Timmy, turns him around. Timmy shambles back. Bill warns the men off."

::SCRIPT::
- CHARACTER: Narrator
  LINE: BILL grabs TIMMY, who’s still laughing wildly, and gets him turned around. TIMMY shambles back to where he was originally standing.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: BILL goes with him like a man who has charge over a trained baboon. A stupid trained baboon.
  EXPRESSION: null
- CHARACTER: Bill
  LINE: You want to get out of here before I get my shotgun! You boys are trespassing!
  EXPRESSION: Threatening

::PATHS::
- CHOICE: "Show Jud's parting words"
  TARGET: four_men_sepia
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: The Four Men / Sepia
MOOD: Grim
CHARACTERS: Narrator, Jud
BACKGROUND_IMAGE: four_men_sepia.png
BACKGROUND_EDIT: "Sepia toned. The four men walking away. Jud speaks to Bill."

::SCRIPT::
- CHARACTER: Jud
  LINE: God help you, Bill.
  EXPRESSION: Solemn

::PATHS::
- CHOICE: "Show Bill's defiant response"
  TARGET: bill_timmy_baterman_sepia
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Bill and Timmy Baterman / Sepia
MOOD: Desperate defiance
CHARACTERS: Narrator, Bill, Timmy
BACKGROUND_IMAGE: bill_timmy_baterman_sepia.png
BACKGROUND_EDIT: "Sepia toned. Bill snarls at the departing men."

::SCRIPT::
- CHARACTER: Bill
  LINE: God never helped me. I helped myself.
  EXPRESSION: Snarling

::PATHS::
- CHOICE: "Close up on Timmy"
  TARGET: timmy_baterhan_cu_sepia
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Timmy Baterhan, CU / Sepia
MOOD: Unnatural
CHARACTERS: Narrator, Timmy
BACKGROUND_IMAGE: timmy_baterhan_cu_sepia.png
BACKGROUND_EDIT: "Sepia toned close-up on Timmy Baterman, staring into the sun and laughing mindlessly."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Staring directly into the setting sun and laughing wildly, mindlessly.
  EXPRESSION: null

::PATHS::
- CHOICE: "Return to Louis and Jud"
  TARGET: creed_kitchen_louis_jud
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: The Creed Kitchen, with Louis and Jud
MOOD: Curious
CHARACTERS: Louis, Jud
BACKGROUND_IMAGE: creed_kitchen_louis_jud.png
BACKGROUND_EDIT: "Night, Louis and Jud sitting, Louis drinking a beer, staring at Jud."

::SCRIPT::
- CHARACTER: Louis
  LINE: What happened?
  EXPRESSION:null

::PATHS::
- CHOICE: "Begin montage of the fire"
  TARGET: baterhan_place_montage_night
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: The Baterhan Place -- Montage Night
MOOD: Arson
CHARACTERS: Narrator, Jud (V.O.)
BACKGROUND_IMAGE: baterhan_place_montage_night.png
BACKGROUND_EDIT: "Night montage. a) Car pulls up with lights off. b) Legs get out, carrying gasoline cans. c) Gasoline splashed on the sides of the house."

::SCRIPT::
- CHARACTER: Narrator
  LINE: a.) A car pulls up with its lights off and stops.
  EXPRESSION: null
- CHARACTER: Jud (V.O.)
  LINE: There was a fire.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: b.) We see legs as people get out of the car, and hands holding tin cans of gasoline.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: c.) Hands splash gasoline from the cans along the sides of the house.
  EXPRESSION: null

::PATHS::
- CHOICE: "Show Jud ringing the bell"
  TARGET: baterhan_porch_night
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: The Baterhan Porch - Night
MOOD: Tense Confrontation
CHARACTERS: Narrator, Jud, Bill, Timmy
BACKGROUND_IMAGE: baterhan_porch_night.png
BACKGROUND_EDIT: "Night. Jud (as young man) rings the bell. Bill answers from inside. Timmy is heard laughing outside."

::SCRIPT::
- CHARACTER: Narrator
  LINE: JUD (as a young man) rings the bell--an old-fashioned twist type.
  EXPRESSION: null
- CHARACTER: Bill
  LINE: Who's there?
  EXPRESSION: null
- CHARACTER: Timmy
  LINE: Ooo air? Ooo air?
  EXPRESSION: Laughing, Screeching
- CHARACTER: Jud
  LINE: Get out, Billy--the place is going up.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: He walks away. BILL BATERMAN, wearing a strappy tee-shirt, looks out the window.
  EXPRESSION: null
- CHARACTER: Bill
  LINE: I seen you! I seen you, Dud Crandall!
  EXPRESSION: Angry

::PATHS::
- CHOICE: "Show the fire being set"
  TARGET: baterhan_place_montage_night_fire
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: The Baterhan Place -- Montage - Night
MOOD: Devastating
CHARACTERS: Narrator
BACKGROUND_IMAGE: baterhan_place_montage_night_fire.png
BACKGROUND_EDIT: "Night montage. a) Match struck and applied to wet boards. b) Other side of house catches fire. c) Torch thrown through kitchen window. d) Men draw away, faces grim."

::SCRIPT::
- CHARACTER: Narrator
  LINE: a.) A match is struck...and applied to wet boards. Whoosh!
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: b.) The other side of the house: The same.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: c.) In the back yard, JUD lights a torch and heaves it through the kitchen windows. Ka-PLOOM!
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: d.) The men draw away toward the front, their faces grim and judgmental.
  EXPRESSION: null

::PATHS::
- CHOICE: "Show the burning house"
  TARGET: baterhan_place_night_burning
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: The Baterhan Place - Night
MOOD: Destruction
CHARACTERS: Narrator
BACKGROUND_IMAGE: baterhan_place_night_burning.png
BACKGROUND_EDIT: "Night. The Baterhan place is burning fiercely."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Burning. Going up fast.
  EXPRESSION: null

::PATHS::
- CHOICE: "Show the men's reaction to the fire"
  TARGET: the_men_sepia
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: The Men
MOOD: Grim
CHARACTERS: Narrator, Alan, Jud
BACKGROUND_IMAGE: the_men_sepia.png
BACKGROUND_EDIT: "Sepia toned. Alan asks Jud about Bill's survival. Jud is stony."

::SCRIPT::
- CHARACTER: Narrator
  LINE: ALAN
  EXPRESSION: null
- CHARACTER: Alan
  LINE: You think Bill's gonna get out, Jud?
  EXPRESSION: Concerned
- CHARACTER: Jud
  LINE: If he don't, he don’t.
  EXPRESSION: Stony

::PATHS::
- CHOICE: "Show the front door bursting open"
  TARGET: front_door_struggle
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: The Front Door
MOOD: Chaotic
CHARACTERS: Narrator
BACKGROUND_IMAGE: front_door_struggle.png
BACKGROUND_EDIT: "Sepia toned. The front door bursts open. Two men are seen struggling."

::SCRIPT::
- CHARACTER: Narrator
  LINE: It bursts open. We see two men struggling
  EXPRESSION: null

::PATHS::
- CHOICE: "End of excerpt"
  TARGET: end
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: The Front Yard
MOOD: Horror, Grief
CHARACTERS: Timmy, Bill, Timhe, Narrator
BACKGROUND_IMAGE: inferno.png
BACKGROUND_EDIT: "Foreground: a man and an undead monster engulfed in flames."

::SCRIPT::
- CHARACTER: Narrator
  LINE: At the forefront of an inferno--correction, one man and an undead monster. TIMMY is giggling and screaming, trying to pull his father back into the flames.
  EXPRESSION: null
- CHARACTER: BILL
  LINE: No! No, Timmy! Let me go!
  EXPRESSION: Struggling
- CHARACTER: TIMHE
  LINE: Love dead! Hate living!
  EXPRESSION: Laughing
- CHARACTER: Narrator
  LINE: He sinks his teeth into his father's arm. BILL screams.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: A beam falls on TIMMY, lighting him afire. BILL breaks free and runs down the porch steps.
  EXPRESSION: null

::PATHS::
- CHOICE: "Follow Bill"
  TARGET: front_hall_timmy
  STATE_CHANGE: fear = +2
  CONDITION: null

::SCENE::
LOCATION: The Front Hall
MOOD: Horror, Madness
CHARACTERS: Timmy, Narrator
BACKGROUND_IMAGE: burning_hall.png
BACKGROUND_EDIT: "Interior of a house, a young boy is on fire and laughing."

::SCRIPT::
- CHARACTER: Narrator
  LINE: He's burning and laughing.
  EXPRESSION: null
- CHARACTER: TIMMY
  LINE: LOVE DEAD! HATE LIVING!
  EXPRESSION: Laughing
- CHARACTER: Narrator
  LINE: And into the fire he goes, still shrieking and laughing.
  EXPRESSION: null

::PATHS::
- CHOICE: "Cut to the front yard"
  TARGET: front_yard_bill
  STATE_CHANGE: horror = +3
  CONDITION: null

::SCENE::
LOCATION: The Front Yard
MOOD: Grief, Despair
CHARACTERS: Bill Baterhan, Narrator
BACKGROUND_IMAGE: bill_grieving.png
BACKGROUND_EDIT: "A man collapses on the lawn as sparks drift down around him, weeping."

::SCRIPT::
- CHARACTER: Narrator
  LINE: BILL BATERHAN is collapsed on the lawn as sparks drift down around him, his face hidden against his thighs, weeping.
  EXPRESSION: null

::PATHS::
- CHOICE: "Observe the farmhouse"
  TARGET: blazing_farmhouse
  STATE_CHANGE: awe = +1
  CONDITION: null

::SCENE::
LOCATION: The Blazing Farmhouse
MOOD: Destruction, Awe
CHARACTERS: Narrator
BACKGROUND_IMAGE: blazing_farmhouse.png
BACKGROUND_EDIT: "A farmhouse is engulfed in flames."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Dissolve to:
  EXPRESSION: null

::PATHS::
- CHOICE: "Transition to the kitchen"
  TARGET: kitchen_louis_jud
  STATE_CHANGE: transition = true
  CONDITION: null

::SCENE::
LOCATION: The Kitchen
MOOD: Somber, Reflective
CHARACTERS: Jud, Louis, Narrator
BACKGROUND_IMAGE: kitchen_somber.png
BACKGROUND_EDIT: "Interior of a kitchen, dimly lit."

::SCRIPT::
- CHARACTER: JUD
  LINE: Sometimes dead is better, Louis.
  EXPRESSION: Softly
- CHARACTER: Narrator
  LINE: Black. And on it, a sixth title card: THE DEAD WALK.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Sound bleeds in: JET ENGINES.
  EXPRESSION: null

::PATHS::
- CHOICE: "Fade to black and transition to airport"
  TARGET: airport_terminal
  STATE_CHANGE: transition = true
  CONDITION: null

::SCENE::
LOCATION: Bangor International Terminal
MOOD: Departure, Transition
CHARACTERS: Narrator
BACKGROUND_IMAGE: jet_rising.png
BACKGROUND_EDIT: "A jet plane rises into the sky from behind a building."

::SCRIPT::
- CHARACTER: GATE AGENT'S VOICE
  LINE: This is the final call for United’s flight 61 to Chicago...
  EXPRESSION: null

::PATHS::
- CHOICE: "Enter the boarding gate"
  TARGET: boarding_gate
  STATE_CHANGE: transition = true
  CONDITION: null

::SCENE::
LOCATION: A Boarding Gate
MOOD: Grief, Confusion, Fading Hope
CHARACTERS: Louis, Rachel, Irwin, Dory Goldman, Ellie, Gate Agent, Narrator
BACKGROUND_IMAGE: boarding_gate.png
BACKGROUND_EDIT: "A busy boarding gate, passengers are boarding a jetway."

::SCRIPT::
- CHARACTER: Narrator
  LINE: In the b.g. we can see IRWIN and DORY GOLDMAN waiting by the jetway with ELLIE as the last few passengers board. RACHEL looks confused and grief-stricken. She also looks punchy, doped up. I imagine she's floating on a sea of Valium, and that makes her easier to deal with. LOUIS'S battle-scars are fading a little.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The GATE AGENT is standing by the jetway with a mike in one hand and a bunch of boarding passes in the other.
  EXPRESSION: null
- CHARACTER: GATE AGENT
  LINE: All passengers should now be aboard.
  EXPRESSION: null
- CHARACTER: LOUIS
  LINE: You better get going, hon.
  EXPRESSION: null
- CHARACTER: RACHEL
  LINE: Oh Louis, I just don't know about this—
  EXPRESSION: null
- CHARACTER: LOUIS
  LINE: I told you last night--this can be the start of patching things up with your folks. If something good doesn’t come of Gage's death, I think I'll go crazy.
  EXPRESSION: null
- CHARACTER: RACHEL
  LINE: Louis, are you sure?
  EXPRESSION: null
- CHARACTER: LOUIS
  LINE: I'm sure.
  EXPRESSION: null

::PATHS::
- CHOICE: "Proceed to the Goldman's house"
  TARGET: goldmans_house_ellie
  STATE_CHANGE: hope = +1
  CONDITION: null

::SCENE::
LOCATION: The Goldmans' House
MOOD: Unease, Sadness
CHARACTERS: Ellie, Dory, Irwin, Narrator
BACKGROUND_IMAGE: goldmans_house.png
BACKGROUND_EDIT: "Interior of a house, a child is talking to her grandparents."

::SCRIPT::
- CHARACTER: ELLIE
  LINE: I don't want to go to Chicago, Gramma Dory.
  EXPRESSION: null
- CHARACTER: DORY
  LINE: Why not, darling?
  EXPRESSION: null
- CHARACTER: ELLIE
  LINE: I had a bad dream last night. A nightmare.
  EXPRESSION: null
- CHARACTER: IRWIN
  LINE: About what?
  EXPRESSION: Kindly
- CHARACTER: ELLIE
  LINE: About Daddy.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: (Pause)
  EXPRESSION: null
- CHARACTER: ELLIE
  LINE: And Gage.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: DORY and IRWIN exchange a knowing, sad glance over the child's head.
  EXPRESSION: null
- CHARACTER: ELLIE
  LINE: And someone named Paxcow.
  EXPRESSION: null

::PATHS::
- CHOICE: "Return to Louis and Rachel"
  TARGET: rachel_louis_jetway
  STATE_CHANGE: unease = +1
  CONDITION: null

::SCENE::
LOCATION: Rachel and Louis
MOOD: Farewell, Lingering Sadness
CHARACTERS: Louis, Dory, Irwin, Rachel, Ellie, Narrator
BACKGROUND_IMAGE: jetway_farewell.png
BACKGROUND_EDIT: "A man guides a woman towards a jetway, while others wait."

::SCRIPT::
- CHARACTER: Narrator
  LINE: LOUIS guides her to the jetway.
  EXPRESSION: null
- CHARACTER: LOUIS
  LINE: Come on, you guys--before you miss the boat.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: He kisses DORY. IRWIN hugs him.
  EXPRESSION: null
- CHARACTER: IRWIN
  LINE: Louis, I am sorry. What can I say? That I lost my mind? It's the truth, but no good excuse.
  EXPRESSION: null
- CHARACTER: LOUIS
  LINE: We all lost our minds, Irwin.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: LOUIS kisses RACHEL. Then he kneels and hugs ELLIE.
  EXPRESSION: null
- CHARACTER: LOUIS
  LINE: Be good to your mother, darlin'. She needs you.
  EXPRESSION: null
- CHARACTER: ELLIE
  LINE: Come with us, daddy. Please come with us!
  EXPRESSION: null
- CHARACTER: LOUIS
  LINE: I'll be there in three days--four at the most. I've got to get the electricity shut off and square things with your school so the truant officer ain't after you, and--
  EXPRESSION: null

::PATHS::
- CHOICE: "Focus on Ellie's plea"
  TARGET: ellie_cu_plea
  STATE_CHANGE: desperation = +2
  CONDITION: null

::SCENE::
LOCATION: Ellie, CU
MOOD: Fear, Desperation
CHARACTERS: Ellie, Louis, Narrator
BACKGROUND_IMAGE: ellie_crying_plea.png
BACKGROUND_EDIT: "Close-up of a child crying, begging her father."

::SCRIPT::
- CHARACTER: ELLIE
  LINE: Please, daddy! I'm scared!
  EXPRESSION: Crying
- CHARACTER: Narrator
  LINE: LOUIS
  EXPRESSION: null

::PATHS::
- CHOICE: "Return to Louis and Ellie"
  TARGET: louis_ellie_reassurance
  STATE_CHANGE: fear = +2
  CONDITION: null

::SCENE::
LOCATION: Louis and Ellie
MOOD: Reassurance, Farewell
CHARACTERS: Louis, Ellie, Narrator
BACKGROUND_IMAGE: louis_reassuring_ellie.png
BACKGROUND_EDIT: "A father reassures his crying daughter before she boards a plane."

::SCRIPT::
- CHARACTER: LOUIS
  LINE: Of what?
  EXPRESSION: null
- CHARACTER: ELLIE
  LINE: I don’t know.
  EXPRESSION: Crying harder
- CHARACTER: LOUIS
  LINE: Everything's going to be all right, Ellie. Now go on--get aboard.
  EXPRESSION: Great emphasis
- CHARACTER: ELLIE
  LINE: Do you swear?
  EXPRESSION: null
- CHARACTER: LOUIS
  LINE: I swear.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The Voice of Authority has spoken. We can tell by ELLIE'S face that while things are still not all right, they are a little better. She joins her mother. The four of them--RACHEL, ELLIE, and THE GOLDMANS--start down the jetway. ELLIE looks back once, as if begging him to come...and then they’re gone.
  EXPRESSION: null

::PATHS::
- CHOICE: "Observe Louis's changing expression"
  TARGET: louis_cu_stony
  STATE_CHANGE: resolve = +2
  CONDITION: null

::SCENE::
LOCATION: Louis, CU
MOOD: Stony, Contemplative, Ominous
CHARACTERS: Louis, Narrator
BACKGROUND_IMAGE: louis_stony_face.png
BACKGROUND_EDIT: "Close-up of a man's face, which is now stony and contemplative."

::SCRIPT::
- CHARACTER: Narrator
  LINE: LOUIS'S face changes. Nov; it is a stony and contemplative face. Not, when you get right down to it, a very nice face.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: He turns and strides away.
  EXPRESSION: null

::PATHS::
- CHOICE: "Move to the airport parking lot"
  TARGET: airport_parking_lot_louis
  STATE_CHANGE: transition = true
  CONDITION: null

::SCENE::
LOCATION: The Airport Parking Lot
MOOD: Solitude, Determination
CHARACTERS: Louis, Narrator
BACKGROUND_IMAGE: louis_in_parking_lot.png
BACKGROUND_EDIT: "A man stands in a parking lot, watching a jet take off."

::SCRIPT::
- CHARACTER: Narrator
  LINE: The family station wagon is in the f.g. We hear the SOUND OF JET ENGINES, and as LOUIS reaches the wagon he turns and watches:
  EXPRESSION: null

::PATHS::
- CHOICE: "Observe the terminal from Louis's POV"
  TARGET: terminal_louis_pov
  STATE_CHANGE: contemplation = +1
  CONDITION: null

::SCENE::
LOCATION: The Terminal, Louis's POV
MOOD: Departure, Isolation
CHARACTERS: Louis, Narrator
BACKGROUND_IMAGE: jet_banks_away.png
BACKGROUND_EDIT: "A United Airlines jet lifts into view and banks away."

::SCRIPT::
- CHARACTER: Narrator
  LINE: From behind it a United Airlines jet lifts into view and banks away.
  EXPRESSION: null

::PATHS::
- CHOICE: "Get into the car and drive away"
  TARGET: route_15_brewer
  STATE_CHANGE: departure = true
  CONDITION: null

::SCENE::
LOCATION: Route 15 in Brewer
MOOD: Purposeful, Determined
CHARACTERS: Louis, Narrator
BACKGROUND_IMAGE: creed_mobile_parked.png
BACKGROUND_EDIT: "A car pulls up across from a hardware store."

::SCRIPT::
- CHARACTER: Narrator
  LINE: The CREED mobile pulls up across from the Brewer Tru-Value Hardware and LOUIS crosses to it.
  EXPRESSION: null

::PATHS::
- CHOICE: "Enter the hardware store"
  TARGET: hardware_store_counter
  STATE_CHANGE: purpose = +2
  CONDITION: null

::SCENE::
LOCATION: The Hardware Store Counter
MOOD: Preparation, Grim
CHARACTERS: Narrator, Clerk
BACKGROUND_IMAGE: hardware_store_items.png
BACKGROUND_EDIT: "A counter with a flashlight, batteries, a pick, a shovel, and a drop-sheet."

::SCRIPT::
- CHARACTER: Narrator
  LINE: On it: A six-cell flashlight, Duracell D-batteries, a pick, a shovel, and a nylon drop-sheet in cellophane packaging. Nov; the CLERK'S hands come into the frame and drop a pair of heavy work­ gloves into the pile.
  EXPRESSION: null

::PATHS::
- CHOICE: "Engage with the clerk"
  TARGET: louis_clerk_small_talk
  STATE_CHANGE: preparation = +1
  CONDITION: null

::SCENE::
LOCATION: The Hardware Store
MOOD: Uneasy, Unnatural
CHARACTERS: Louis, Clerk, Narrator
BACKGROUND_IMAGE: louis_buying_supplies.png
BACKGROUND_EDIT: "A man is buying tools at a hardware store counter."

::SCRIPT::
- CHARACTER: CLERK
  LINE: Anything else for you today?
  EXPRESSION: null
- CHARACTER: LOUIS
  LINE: I think we got it all.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The CLERK starts to ring things up.
  EXPRESSION: null
- CHARACTER: CLERK
  LINE: Looks like heavy work.
  EXPRESSION: null
- CHARACTER: LOUIS
  LINE: It could be.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The quality of LOUIS'S reply is somehow unnatural. The CLERK looks at him, momentarily unsure and uncertain. Then he starts ringing things up again.
  EXPRESSION: null

::PATHS::
- CHOICE: "Transition to the jetliner"
  TARGET: jetliner_ellie_rachel
  STATE_CHANGE: transition = true
  CONDITION: null

::SCENE::
LOCATION: A United Jetliner
MOOD: Fear, Nightmare
CHARACTERS: Ellie, Rachel, Narrator
BACKGROUND_IMAGE: jetliner_ellie_dreaming.png
BACKGROUND_EDIT: "A child is asleep in a window seat, her sleep troubled."

::SCRIPT::
- CHARACTER: Narrator
  LINE: ELLIE is in the window-seat, asleep. RACHEL is holding a paperback but not reading it. Her eyes are red. She's looking into space.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: CAMERA DRIFTS TO ELLIE. Her sleep is not easy. Her head turns from side to side, as if in negation. She becomes steadily more upset.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: She’s starting to mutter. Suddenly her eyes flare open and she screams.
  EXPRESSION: null

::PATHS::
- CHOICE: "Widen the shot to show the cabin"
  TARGET: jetliner_wider
  STATE_CHANGE: fear = +3
  CONDITION: null

::SCENE::
LOCATION: Jetliner, Slightly Wider
MOOD: Startled, Concerned
CHARACTERS: Ellie, Rachel, The Goldmans, Passengers, Stewardess, Narrator
BACKGROUND_IMAGE: jetliner_cabin_reaction.png
BACKGROUND_EDIT: "A child screams in her sleep on a plane, startling other passengers."

::SCRIPT::
- CHARACTER: Narrator
  LINE: We can see the GOLDMANS in the seats behind the CREEDS. They are startled. So are other passengers. A stewardess comes running.
  EXPRESSION: null
- CHARACTER: ELLIE
  LINE: Paxcow says it's almost too late!
  EXPRESSION: null
- CHARACTER: RACHEL
  LINE: Ellie...Ellie...what...
  EXPRESSION: null
- CHARACTER: ELLIE
  LINE: Paxcow says it's almost too late! We have to go back! Paxcow says it's almost too late!
  EXPRESSION: null

::PATHS::
- CHOICE: "Cut to Ludlow Cemetery"
  TARGET: ludlow_cemetery_louis
  STATE_CHANGE: transition = true
  CONDITION: null

::SCENE::
LOCATION: Ludlow Cemetery
MOOD: Grief, Determination, Supernatural
CHARACTERS: Louis, Narrator
BACKGROUND_IMAGE: louis_at_grave.png
BACKGROUND_EDIT: "A man sits by a fresh grave, holding a flower."

::SCRIPT::
- CHARACTER: Narrator
  LINE: The CREED wagon turns in and drives up one of the lanes. It stops and LOUIS gets out. He walks to a fresh grave on which the first flowers are already starting to wilt. He sits down and takes a flower. He plucks it, looking at the grave steadily. He says nothing for a long time.
  EXPRESSION: null
- CHARACTER: LOUIS
  LINE: It's wrong.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: (Pause)
  EXPRESSION: null
- CHARACTER: LOUIS
  LINE: What happened to you is wrong.
  EXPRESSION: null

::PATHS::
- CHOICE: "Show Gage running in slow motion"
  TARGET: gage_running_slow_motion
  STATE_CHANGE: hope = -2, sorrow = +2
  CONDITION: null

::SCENE::
LOCATION: Gage, In The Field
MOOD: Joyful, Innocent, Tragic Irony
CHARACTERS: Gage, Narrator
BACKGROUND_IMAGE: gage_running_field.png
BACKGROUND_EDIT: "A child runs toward the camera in slow motion, happy and laughing."

::SCRIPT::
- CHARACTER: Narrator
  LINE: He runs toward THE CAMERA, happy and laughing, in SLOW MOTION.
  EXPRESSION: null

::PATHS::
- CHOICE: "Return to Louis by Gage's grave"
  TARGET: louis_by_gages_grave_weeping
  STATE_CHANGE: transition = true
  CONDITION: null

::SCENE::
LOCATION: Louis, By Gage's Grave
MOOD: Grief, Calm Resolve
CHARACTERS: Louis, Narrator
BACKGROUND_IMAGE: louis_weeping_calm.png
BACKGROUND_EDIT: "A man is weeping by a grave, but appears calm."

::SCRIPT::
- CHARACTER: Narrator
  LINE: LOUIS is now weeping, but he seems calm just the same.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: PASCOW (VOICE)
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Remember, doc.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: LOUIS looks at:
  EXPRESSION: null

::PATHS::
- CHOICE: "Show PascoW by the tomb"
  TARGET: tomb_pascow_bloody
  STATE_CHANGE: supernatural = +2
  CONDITION: null

::SCENE::
LOCATION: A Tomb, Louis's POV
MOOD: Supernatural, Mutilated
CHARACTERS: PascoW, Narrator
BACKGROUND_IMAGE: pascow_bloody_mutilated.png
BACKGROUND_EDIT: "PascoW, bloody and mutilated, stands by a tomb."

::SCRIPT::
- CHARACTER: PASCOW
  LINE: The barrier was not meant to be crossed. The ground is sour.
  EXPRESSION: null

::PATHS::
- CHOICE: "Return to Louis by Gage's grave"
  TARGET: louis_by_gages_grave_argument
  STATE_CHANGE: supernatural = +1
  CONDITION: null

::SCENE::
LOCATION: Louis, By Gage's Grave
MOOD: Defiant, Heartbroken
CHARACTERS: Louis, PascoW, Narrator
BACKGROUND_IMAGE: louis_arguing_with_pascoW.png
BACKGROUND_EDIT: "A man stands by a grave, arguing with a supernatural figure."

::SCRIPT::
- CHARACTER: Narrator
  LINE: He is not put out of countenance in the slightest by PASCOW'S appearance; he probably knows PASCOW is just a figment of his conscience or imagination, and so do we.
  EXPRESSION: null
- CHARACTER: LOUIS
  LINE: I'll tell you where the ground is sour--the ground in my heart is sour. Let me tell you something else, Vic-baby: Wrong is wrong.
  EXPRESSION: null

::PATHS::
- CHOICE: "Show PascoW responding"
  TARGET: pascoW_responding
  STATE_CHANGE: confrontation = +1
  CONDITION: null

::SCENE::
LOCATION: PascoW
MOOD: Judgmental
CHARACTERS: PascoW, Narrator
BACKGROUND_IMAGE: pascoW_judgmental.png
BACKGROUND_EDIT: "PascoW stands mute, looking."

::SCRIPT::
- CHARACTER: PASCOW
  LINE: Timmy Baterman. That was wrong.
  EXPRESSION: null

::PATHS::
- CHOICE: "Return to Louis by Gage's grave"
  TARGET: louis_by_gages_grave_retort
  STATE_CHANGE: anger = +1
  CONDITION: null

::SCENE::
LOCATION: Louis, By Gage's Grave
MOOD: Angry, Heartbroken
CHARACTERS: Louis, PascoW, Narrator
BACKGROUND_IMAGE: louis_retorting_to_pascoW.png
BACKGROUND_EDIT: "A man angrily retorts to a supernatural figure by a grave."

::SCRIPT::
- CHARACTER: LOUIS
  LINE: Don't talk like an asshole even if you are just a bit of underdone potato or a blot of mustard.
  EXPRESSION: null

::PATHS::
- CHOICE: "Show PascoW by the tomb"
  TARGET: pascoW_by_tomb_mute
  STATE_CHANGE: silence = +1
  CONDITION: null

::SCENE::
LOCATION: PascoW, By The Tomb
MOOD: Silent, Watching
CHARACTERS: PascoW, Narrator
BACKGROUND_IMAGE: pascoW_by_tomb_mute.png
BACKGROUND_EDIT: "PascoW stands by the tomb, looking."

::SCRIPT::
- CHARACTER: Narrator
  LINE: He stands mute, just looking.
  EXPRESSION: null

::PATHS::
- CHOICE: "Return to Louis by Gage's grave"
  TARGET: louis_by_gages_grave_plea
  STATE_CHANGE: grief = +2
  CONDITION: null

::SCENE::
LOCATION: Louis, By Gage's Grave
MOOD: Desperate, Heartbroken
CHARACTERS: Louis, PascoW, Narrator
BACKGROUND_IMAGE: louis_pleading_at_grave.png
BACKGROUND_EDIT: "A man weeps by a grave, pleading."

::SCRIPT::
- CHARACTER: LOUIS
  LINE: He was my son! He wasn't even two and he was run down in the fucking road and he was almost in pieces, and if you don't think I'm going to try...
  EXPRESSION: Weeping
- CHARACTER: Narrator
  LINE: VIC has put on his boogie shoes.
  EXPRESSION: null

::PATHS::
- CHOICE: "Show the tomb without PascoW"
  TARGET: tomb_sans_pascoW
  STATE_CHANGE: resolve = +1
  CONDITION: null

::SCENE::
LOCATION: The Tomb, Sans PascoW
MOOD: Determined, Risky
CHARACTERS: Narrator
BACKGROUND_IMAGE: tomb_alone.png
BACKGROUND_EDIT: "A tomb stands alone."

::SCRIPT::
- CHARACTER: Narrator
  LINE: VIC has put on his boogie shoes.
  EXPRESSION: null

::PATHS::
- CHOICE: "Return to Louis by Gage's grave"
  TARGET: louis_by_gages_grave_action
  STATE_CHANGE: resolve = +2
  CONDITION: null

::SCENE::
LOCATION: Louis, By Gage's Grave
MOOD: Desperate, Determined, Fearful
CHARACTERS: Louis, Narrator
BACKGROUND_IMAGE: louis_knocking_over_tributes.png
BACKGROUND_EDIT: "A man cries harder by a grave and knocks over floral tributes."

::SCRIPT::
- CHARACTER: Narrator
  LINE: He's crying harder. Abruptly he reaches out at the floral tributes and knocks a bunch of them over.
  EXPRESSION: null
- CHARACTER: LOUIS
  LINE: If it doesn't work--if he comes back like Timmy Baterman--I'11 put him to sleep. But I'm going to try.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: (Pause)
  EXPRESSION: null
- CHARACTER: LOUIS
  LINE: And if it doesn't work...they don't ever need to know.
  EXPRESSION: null

::PATHS::
- CHOICE: "Transition to the Goldman house"
  TARGET: goldman_house_illinois_night
  STATE_CHANGE: transition = true
  CONDITION: null

::SCENE::
LOCATION: The Goldman House in Lake Forest, Illinois
MOOD: Uneasy Night, Lingering Fear
CHARACTERS: Narrator
BACKGROUND_IMAGE: goldman_house_exterior_night.png
BACKGROUND_EDIT: "Exterior of a house at night."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Dissolve to:
  EXPRESSION: null

::PATHS::
- CHOICE: "Move to the upstairs hall"
  TARGET: upstairs_hall_night
  STATE_CHANGE: transition = true
  CONDITION: null

::SCENE::
LOCATION: Upstairs Hall
MOOD: Uneasy, Frightened
CHARACTERS: Narrator, Rachel, Ellie
BACKGROUND_IMAGE: upstairs_hall_pictures.png
BACKGROUND_EDIT: "A hallway lined with pictures, a door is open with light spilling out."

::SCRIPT::
- CHARACTER: Narrator
  LINE: The CAMERA MOVES LEISURELY along this hallway, which is lined with pictures of RACHEL, ELLIE...and GAGE (there may even be a couple in which LOUIS is featured, but damned few). Near the end of the hall a door is open and light spills out.
  EXPRESSION: null
- CHARACTER: RACHEL
  LINE: Honey, you just had a bad dream. You know that, don't you?
  EXPRESSION: null
- CHARACTER: ELLIE
  LINE: It wasn't a dream. It was Paxcow.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: THE CAMERA GOES THROUGH THE DOOR and into the room where ELLIE is staying. She's in bed, still badly upset. RACHEL is sitting on the bed beside her. There's a single lamp on the bedside table.
  EXPRESSION: null
- CHARACTER: ELLIE
  LINE: Paxcow says Daddy's going to do something really bad. He--
  EXPRESSION: null
- CHARACTER: RACHEL
  LINE: Who is this Paxcow? Is he like the boogeyman?
  EXPRESSION: null
- CHARACTER: ELLIE
  LINE: He’s a ghost. But he's a good ghost.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: RACHEL turns off the bed-lamp.
  EXPRESSION: null
- CHARACTER: RACHEL
  LINE: There are no ghosts, Ellie. I want you to go to sleep and forget all this nonsense.
  EXPRESSION: null
- CHARACTER: ELLIE
  LINE: Will y
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue the dialogue"
  TARGET: rachel_ellie_dialogue_end
  STATE_CHANGE: fear = +2, denial = +1
  CONDITION: null

::SCENE::
LOCATION: The Goldman Living Room
MOOD: Anxious
CHARACTERS: Rachel, Ellie, Narrator
BACKGROUND_IMAGE: goldman_living_room_night.png
BACKGROUND_EDIT: "Nighttime interior, warm but tense"

::SCRIPT::
- CHARACTER: Narrator
  LINE: You at least call and make sure daddy's okay?
  EXPRESSION: null
- CHARACTER: Rachel
  LINE: Of course I will.
  EXPRESSION: Calm
- CHARACTER: Rachel
  LINE: Now will you try to go to sleep?
  EXPRESSION: Calm
- CHARACTER: Ellie
  LINE: Yes, Mom.
  EXPRESSION: Sleepy
- CHARACTER: Narrator
  LINE: Rachel gets up and leaves the room.
  EXPRESSION: null

::SCENE::
LOCATION: The Upstairs Hallway
MOOD: Ominous
CHARACTERS: Pasacow, Rachel, Narrator
BACKGROUND_IMAGE: upstairs_hallway_night.png
BACKGROUND_EDIT: "Nighttime interior, dimly lit hallway"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Pascow is here, halfway down the hall to the stairs, bloody as ever. Rachel doesn't see him. She looks perplexed, a woman trying to think of something. She stops very near him.
  EXPRESSION: null
- CHARACTER: Rachel
  LINE: Pascow, why do I know that name?
  EXPRESSION: Perplexed
- CHARACTER: Pascow
  LINE: Pascow.
  EXPRESSION: Ominous
- CHARACTER: Rachel
  LINE: Pascow? Was she saying Pascow?
  EXPRESSION: Startled
- CHARACTER: Narrator
  LINE: She suddenly heads for the stairs, fast.
  EXPRESSION: Urgent

::SCENE::
LOCATION: The Creed Home in Ludlow
MOOD: Foreboding
CHARACTERS: Louis, Narrator
BACKGROUND_IMAGE: creed_home_ludlow_night.png
BACKGROUND_EDIT: "Nighttime exterior, imposing house"

::SCRIPT::
- CHARACTER: Narrator
  LINE: SOUND: A car starting up.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The station wagon backs out and heads down the driveway. As it passes the camera, we see Louis driving. The wagon turns onto Route 9 and heads off.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: CAMERA HOLDS ON THE HOUSE. A beat of silence. Then: the telephone starts ringing.
  EXPRESSION: null

::SCENE::
LOCATION: The Goldman Living Room
MOOD: Anxious
CHARACTERS: Irwin, Dory, Rachel, Narrator
BACKGROUND_IMAGE: goldman_living_room_night.png
BACKGROUND_EDIT: "Nighttime interior, tense atmosphere"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Irwin and Dory are watching Rachel with some anxiety. Rachel is holding the phone to her ear. We can hear the FILTERED SOUND of one ring after another. She hangs up.
  EXPRESSION: null
- CHARACTER: Rachel
  LINE: He's not home.
  EXPRESSION: Worried
- CHARACTER: Dory
  LINE: Why, he probably went out for a hamburger or a chicken dinner, dear, you know how men are when they're alone.
  EXPRESSION: Dismissive
- CHARACTER: Narrator
  LINE: Good old Irwin's face says that maybe Louis went out for a couple of grams of coke and a whore in Nazi SS boots.
  EXPRESSION: Skeptical
- CHARACTER: Narrator
  LINE: Rachel is dialing another number.
  EXPRESSION: Determined

::SCENE::
LOCATION: The Crandall House
MOOD: Anticipatory
CHARACTERS: Narrator
BACKGROUND_IMAGE: crandall_house_night.png
BACKGROUND_EDIT: "Nighttime exterior, quiet house"

::SCRIPT::
- CHARACTER: Narrator
  LINE: SOUND: Phone starts to ring.
  EXPRESSION: null

::SCENE::
LOCATION: The Crandall Kitchen, With Jud
MOOD: Relaxed, then Concerned
CHARACTERS: Jud, Narrator
BACKGROUND_IMAGE: crandall_kitchen_night.png
BACKGROUND_EDIT: "Nighttime interior, casual setting"

::SCRIPT::
- CHARACTER: Narrator
  LINE: He shuffles to the telephone. His Walkman phones are around his neck. He's got a bottle of beer in one hand.
  EXPRESSION: null
- CHARACTER: Jud
  LINE: Hello--you got Hudson.
  EXPRESSION: Casual

::SCENE::
LOCATION: The Goldman Living Room, With Rachel
MOOD: Clarifying
CHARACTERS: Rachel, Jud, Narrator
BACKGROUND_IMAGE: goldman_living_room_night.png
BACKGROUND_EDIT: "Nighttime interior, tense atmosphere"

::SCRIPT::
- CHARACTER: Rachel
  LINE: It's Rachel Creed, Jud. I'm calling from Chicago.
  EXPRESSION: Calm
- CHARACTER: Jud
  LINE: Chicago! Is Louis with you?
  EXPRESSION: Surprised

::SCENE::
LOCATION: The Goldman Living Room, With Rachel
MOOD: Evasive
CHARACTERS: Rachel, Jud, Narrator
BACKGROUND_IMAGE: goldman_living_room_night.png
BACKGROUND_EDIT: "Nighttime interior, tense atmosphere"

::SCRIPT::
- CHARACTER: Rachel
  LINE: No...we're going to be here awhile, and he wanted a few days to wind up our affairs there. I just wondered if he was with you.
  EXPRESSION: Evasive
- CHARACTER: Narrator
  LINE: 119.
  EXPRESSION: null

::SCENE::
LOCATION: The Crandall Kitchen, With Jud
MOOD: Serious
CHARACTERS: Jud, Narrator
BACKGROUND_IMAGE: crandall_kitchen_night.png
BACKGROUND_EDIT: "Nighttime interior, concerned expression"

::SCRIPT::
- CHARACTER: Narrator
  LINE: His face says this is very serious.
  EXPRESSION: Serious
- CHARACTER: Jud
  LINE: No--but if he drops by, I'll tell him to call you.
  EXPRESSION: Concerned

::SCENE::
LOCATION: The Goldman Living Room
MOOD: Questioning
CHARACTERS: Rachel, Jud, Narrator
BACKGROUND_IMAGE: goldman_living_room_night.png
BACKGROUND_EDIT: "Nighttime interior, focused tension"

::SCRIPT::
- CHARACTER: Rachel
  LINE: Jud, do you remember the name of the student that died on Louis's first day at work? The one that was hit by a car?
  EXPRESSION: Focused
- CHARACTER: Jud
  LINE: I don't--
  EXPRESSION: Uncertain
- CHARACTER: Rachel
  LINE: Was it Pascow?
  EXPRESSION: Questioning

::SCENE::
LOCATION: The Crandall Kitchen, With Jud
MOOD: Affirming, then Alarmed
CHARACTERS: Jud, Narrator
BACKGROUND_IMAGE: crandall_kitchen_night.png
BACKGROUND_EDIT: "Nighttime interior, dawning realization"

::SCRIPT::
- CHARACTER: Jud
  LINE: Ayuh, I think 'twas. If I see Louis come home before I go to bed, I'll tell him to--
  EXPRESSION: Affirming
- CHARACTER: Narrator
  LINE: 120.
  EXPRESSION: null

::SCENE::
LOCATION: The Goldman Living Room, With Rachel
MOOD: Decisive, then Alarmed
CHARACTERS: Rachel, Jud, Narrator
BACKGROUND_IMAGE: goldman_living_room_night.png
BACKGROUND_EDIT: "Nighttime interior, decisive action"

::SCRIPT::
- CHARACTER: Rachel
  LINE: Don't bother. I'm coming home.
  EXPRESSION: Decisive
- CHARACTER: Jud
  LINE: Rachel!
  EXPRESSION: Alarmed
- CHARACTER: Rachel
  LINE: Thank you, Jud. Goodbye.
  EXPRESSION: Final
- CHARACTER: Narrator
  LINE: She hangs up.
  EXPRESSION: null

::SCENE::
LOCATION: The Crandall Kitchen, With Jud
MOOD: Frustrated
CHARACTERS: Jud, Narrator
BACKGROUND_IMAGE: crandall_kitchen_night.png
BACKGROUND_EDIT: "Nighttime interior, frustration evident"

::SCRIPT::
- CHARACTER: Jud
  LINE: No! Rachel! Don't do that! Rachel--!
  EXPRESSION: Frustrated
- CHARACTER: Narrator
  LINE: The buzz of an open line. Connection broken. Jud slowly replaces the receiver. The man looks very grim.
  EXPRESSION: Grim

::SCENE::
LOCATION: The Front Hall of the Goldman House
MOOD: Urgent Departure
CHARACTERS: Rachel, Dory, Irwin, Ellie, Narrator
BACKGROUND_IMAGE: goldman_front_hall_night.png
BACKGROUND_EDIT: "Nighttime interior, packed and ready"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Rachel comes down the stairs, dressed for travelling. She's carrying a suitcase in one hand. Her parents meet her at the foot of the stairs.
  EXPRESSION: null
- CHARACTER: Dory
  LINE: Rachel...darling...you're upset... a night's sleep...
  EXPRESSION: Concerned
- CHARACTER: Rachel
  LINE: I have to go. The connections are tight, and I have to be at O'Hare in forty minutes. Will you drive me, daddy?
  EXPRESSION: Urgent
- CHARACTER: Irwin
  LINE: You know something's wrong, don't you? You know. And Ellie does, too.
  EXPRESSION: Knowing
- CHARACTER: Rachel
  LINE: Yes.
  EXPRESSION: Affirming
- CHARACTER: Irwin
  LINE: I'll drive you.
  EXPRESSION: Determined
- CHARACTER: Ellie
  LINE: Mommy?
  EXPRESSION: Anxious

::SCENE::
LOCATION: Ellie, On the Stairs
MOOD: Pleading
CHARACTERS: Ellie, Narrator
BACKGROUND_IMAGE: ellie_on_stairs_night.png
BACKGROUND_EDIT: "Nighttime interior, pleading expression"

::SCRIPT::
- CHARACTER: Narrator
  LINE: They all turn to:
  EXPRESSION: null
- CHARACTER: Ellie
  LINE: Please hurry.
  EXPRESSION: Pleading

::SCENE::
LOCATION: Rachel and the Goldmans
MOOD: Affectionate Farewell
CHARACTERS: Rachel, Ellie, Narrator
BACKGROUND_IMAGE: goldman_living_room_night.png
BACKGROUND_EDIT: "Nighttime interior, emotional embrace"

::SCRIPT::
- CHARACTER: Rachel
  LINE: I will. Come and kiss me.
  EXPRESSION: Affectionate
- CHARACTER: Narrator
  LINE: Ellie races into her arms.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: 121.
  EXPRESSION: null

::SCENE::
LOCATION: Ludlow Cemetery
MOOD: Secretive, Desperate
CHARACTERS: Louis, Narrator
BACKGROUND_IMAGE: ludlow_cemetery_night.png
BACKGROUND_EDIT: "Nighttime exterior, dark and desolate"

::SCRIPT::
- CHARACTER: Narrator
  LINE: SOUND Of a car engine, THROBBING AND LOW. It cuts off.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: CAMERA MOVES IN on the low stone wall between the cemetery and the road. Beyond it we can see the roof of the Creed station wagon.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Louis appears, dressed in dark clothes. He looks both ways, then tosses a big duffle bag over the wall. Stuff clanks inside.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Louis climbs over the wall, grabs his bag, and checks out the scene.
  EXPRESSION: null

::SCENE::
LOCATION: Ludlow Cemetery, Louis's POV
MOOD: Eerie
CHARACTERS: Narrator
BACKGROUND_IMAGE: ludlow_cemetery_night_pov.png
BACKGROUND_EDIT: "Nighttime POV, spooky and quiet"

::SCRIPT::
- CHARACTER: Narrator
  LINE: A quiet city of the dead. Spooky. SOUND of crickets: Ree-ree-ree...
  EXPRESSION: null

::SCENE::
LOCATION: Louis
MOOD: Determined
CHARACTERS: Louis, Narrator
BACKGROUND_IMAGE: louis_at_cemetery_night.png
BACKGROUND_EDIT: "Nighttime exterior, determined stride"

::SCRIPT::
- CHARACTER: Narrator
  LINE: He heads for Gage's grave.
  EXPRESSION: null

::SCENE::
LOCATION: The Goldman Car, With Rachel and Irwin
MOOD: Reassuring
CHARACTERS: Irwin, Rachel, Narrator
BACKGROUND_IMAGE: goldman_car_night.png
BACKGROUND_EDIT: "Nighttime interior, car driving"

::SCRIPT::
- CHARACTER: Irwin
  LINE: I'll come with you if you want, honey.
  EXPRESSION: Reassuring
- CHARACTER: Rachel
  LINE: I've got three planes to catch and I got the last seats on two of them. It's like God saved them for me.
  EXPRESSION: Determined

::SCENE::
LOCATION: O'Hare United Airlines Terminal, With Irwin's Car
MOOD: Transit
CHARACTERS: Narrator
BACKGROUND_IMAGE: ohare_terminal_night.png
BACKGROUND_EDIT: "Nighttime exterior, airport terminal"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Irwin's car heads for it.
  EXPRESSION: null

::SCENE::
LOCATION: The Grave of Gage Creed
MOOD: Somber, Determined
CHARACTERS: Louis, Narrator
BACKGROUND_IMAGE: gage_creed_grave_night.png
BACKGROUND_EDIT: "Nighttime exterior, grave site"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Louis approaches it slowly and sets down his bag of grave-robbing equipment. He sets aside the remaining floral tributes and then opens the bag and takes out the spade. He looks down at the grave for a long second.
  EXPRESSION: null
- CHARACTER: Louis
  LINE: Gonna bust you out, son.
  EXPRESSION: Determined
- CHARACTER: Narrator
  LINE: He starts to shovel.
  EXPRESSION: null

::SCENE::
LOCATION: The Shovel, CU
MOOD: Laborious
CHARACTERS: Narrator
BACKGROUND_IMAGE: shovel_digging_night.png
BACKGROUND_EDIT: "Nighttime close-up, dirt being moved"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Digging...throwing...digging again. Already the shape of the excavation is beginning to show. The work is easy; this earth is new and fresh.
  EXPRESSION: null

::SCENE::
LOCATION: Jetliner, In a Line-up of Jetliners
MOOD: Anticipatory
CHARACTERS: Narrator
BACKGROUND_IMAGE: jetliner_night.png
BACKGROUND_EDIT: "Nighttime exterior, airport tarmac"

::SCRIPT::
- CHARACTER: Narrator
  LINE: 122.
  EXPRESSION: null

::SCENE::
LOCATION: Jetliner, With Rachel
MOOD: Impatient, Anxious
CHARACTERS: Rachel, Pilot, Narrator
BACKGROUND_IMAGE: jetliner_interior_night.png
BACKGROUND_EDIT: "Nighttime interior, airplane cabin"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Everyone looks impatient, but Rachel looks half crazy.
  EXPRESSION: null
- CHARACTER: Pilot
  LINE: This is the Captain speaking. I'm sorry about this delay, folks, but we’ve got a real low ceiling tonight and air traffic control's playing it safe. Looks like it's going to be about half an hour before we get on a roll, so I'm turning off the NO SMOKING sign.
  EXPRESSION: Apologetic
- CHARACTER: Narrator
  LINE: SOUND: Bing!
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: There's a general groan. CAMERA MOVES IN ON RACHEL, who has closed her eyes. I think she’s praying.
  EXPRESSION: null

::SCENE::
LOCATION: Gage's Grave - Night
MOOD: Intense Labor
CHARACTERS: Louis, Narrator
BACKGROUND_IMAGE: gage_grave_louis_digging_night.png
BACKGROUND_EDIT: "Nighttime exterior, deep grave"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Now it's pretty deep. Four feet, maybe. Louis is standing in it.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: We see his feet as the shovel goes up and down, up and down.
  EXPRESSION: null

::SCENE::
LOCATION: Louis - Night
MOOD: Straining, then Alert
CHARACTERS: Louis, Narrator
BACKGROUND_IMAGE: louis_digging_night.png
BACKGROUND_EDIT: "Nighttime exterior, dirt-covered and sweating"

::SCRIPT::
- CHARACTER: Narrator
  LINE: He's sweating and dirt-streaked. He's tossing dirt on a big pile.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Suddenly, as he takes another shovelful, we hear a SCRAPING SOUND.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: He tosses the shovel aside and squats.
  EXPRESSION: null

::SCENE::
LOCATION: In The Grave, With Louis
MOOD: Discovery
CHARACTERS: Louis, Narrator
BACKGROUND_IMAGE: louis_in_grave_night.png
BACKGROUND_EDIT: "Nighttime interior, close-up of coffin"

::SCRIPT::
- CHARACTER: Narrator
  LINE: There's a white streak on the bottom of the grave--the top of Gage's coffin. Louis swipes his hand through the loose dirt, uncovering more, and then he begins to sweep off the top of the coffin with his hands.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: 123.
  EXPRESSION: null

::SCENE::
LOCATION: The Crandall Porch
MOOD: Resigned, Isolated
CHARACTERS: Jud, Narrator
BACKGROUND_IMAGE: crandall_porch_night.png
BACKGROUND_EDIT: "Nighttime exterior, solitary figure"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Jud comes out. He's wearing a light jacket. His Walkman phones are around his neck. He's got a six-pack. He looks at:
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: It's dark.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: He sits down.
  EXPRESSION: null
- CHARACTER: Jud
  LINE: You done it, you stupid old man... now you got to undo it.
  EXPRESSION: Resigned
- CHARACTER: Narrator
  LINE: He puts his earphones on. Cracks a beer. Lights a cigarette. Pushes the PLAY button on the deck. Faint SOUNDS of The Clash buzz-sawing "Rock The Casbah."
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Jud begins to watch.
  EXPRESSION: null

::SCENE::
LOCATION: Louis
MOOD: Preparing, then Alert
CHARACTERS: Louis, Narrator
BACKGROUND_IMAGE: louis_preparing_grave_night.png
BACKGROUND_EDIT: "Nighttime exterior, preparing for next step"

::SCRIPT::
- CHARACTER: Narrator
  LINE: He climbs out of the grave and opens his duffle bag. He starts to pull out the pick.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: SOUND of an approaching car.
  EXPRESSION: null
- CHARACTER: Louis
  LINE: LOUIS FREEZES.
  EXPRESSION: Frozen

::SCENE::
LOCATION: The Road Outside of the Cemetery
MOOD: Wary
CHARACTERS: Narrator
BACKGROUND_IMAGE: road_outside_cemetery_night.png
BACKGROUND_EDIT: "Nighttime exterior, police car"

::SCRIPT::
- CHARACTER: Narrator
  LINE: A police car comes cruising slowly along. The spotlight on the driver's side comes on and runs along the graveyard's stone wall.
  EXPRESSION: null

::SCENE::
LOCATION: Louis
MOOD: Relieved, Resuming
CHARACTERS: Louis, Narrator
BACKGROUND_IMAGE: louis_resuming_dig_night.png
BACKGROUND_EDIT: "Nighttime exterior, returning to the grave"

::SCRIPT::
- CHARACTER: Narrator
  LINE: He relaxes perceptibly. He gets the pick and drops back into the grave.
  EXPRESSION: null

::SCENE::
LOCATION: The Top of the Coffin, CU
MOOD: Breaking Point
CHARACTERS: Louis, Narrator
BACKGROUND_IMAGE: coffin_lid_breaking_night.png
BACKGROUND_EDIT: "Nighttime close-up, coffin lid"

::SCRIPT::
- CHARACTER: Narrator
  LINE: LOUIS inserts the tip of the pick in the flange of the coffin and levers it. CRACKING SOUND. Again. More CRACKING. Again. And the lock breaks. The coffin lid comes up a little, dirt gritting in the hinges.
  EXPRESSION: null

::SCENE::
LOCATION: Louis, CU
MOOD: Descent into Madness
CHARACTERS: Louis, Narrator
BACKGROUND_IMAGE: louis_face_madness_night.png
BACKGROUND_EDIT: "Nighttime close-up, tormented face"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Here’s a man on the thinnest edge between sanity and madness.
  EXPRESSION: null

::SCENE::
LOCATION: Jetliner Lifting Off from O'Hare
MOOD: Escape, Hope
CHARACTERS: Narrator
BACKGROUND_IMAGE: jetliner_takeoff_night.png
BACKGROUND_EDIT: "Nighttime exterior, plane ascending"

::SCRIPT::
- CHARACTER: Narrator
  LINE: 124.
  EXPRESSION: null

::SCENE::
LOCATION: Int. Rachel And Her Seatemate
MOOD: Hopeful, Determined
CHARACTERS: Rachel, Seatemate, Narrator
BACKGROUND_IMAGE: jetliner_interior_night.png
BACKGROUND_EDIT: "Nighttime interior, airplane cabin"

::SCRIPT::
- CHARACTER: Seatemate
  LINE: Think you'll make your connection in Boston?
  EXPRESSION: Inquisitive
- CHARACTER: Rachel
  LINE: I have to.
  EXPRESSION: Determined

::SCENE::
LOCATION: Louis, By Gage’s Grave
MOOD: Grief-Stricken
CHARACTERS: Louis, Narrator
BACKGROUND_IMAGE: louis_reaching_into_grave_night.png
BACKGROUND_EDIT: "Nighttime exterior, grave site, reaching"

::SCRIPT::
- CHARACTER: Narrator
  LINE: He's lying on his stomach, reaching in. We hear the SOUND of dirt grating in hinges again.
  EXPRESSION: null

::SCENE::
LOCATION: Louis, CU
MOOD: Devastating Grief
CHARACTERS: Louis, Narrator
BACKGROUND_IMAGE: louis_face_grief_night.png
BACKGROUND_EDIT: "Nighttime close-up, face contorted in sorrow"

::SCRIPT::
- CHARACTER: Narrator
  LINE: We’re looking up into his face. If Gage had a POV, this would be it. Louis's face fills with a terrible grief.
  EXPRESSION: null
- CHARACTER: Louis
  LINE: Oh, Gage--oh, honey.
  EXPRESSION: Heartbroken

::SCENE::
LOCATION: Jud Crandall, On His Porch
MOOD: Resigned, Drowsy
CHARACTERS: Jud, Narrator
BACKGROUND_IMAGE: jud_crandall_porch_night.png
BACKGROUND_EDIT: "Nighttime exterior, solitary figure on porch"

::SCRIPT::
- CHARACTER: Narrator
  LINE: His chin slips to his chest, even though we hear Creedence on his ’phones and to him the sound must be at blastoff levels. There’s a long round ash on his cigarette in the tray. A couple of empty beer cans on the table beside him.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: 125.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: A truck blasts by, startling him out of his doze. He jerks his head up suddenly...and slaps himself. He’s okay...for now.
  EXPRESSION: null

::SCENE::
LOCATION: The Graveyard, With Louis
MOOD: Desperate Comfort
CHARACTERS: Louis, Gage, Narrator
BACKGROUND_IMAGE: louis_holding_gage_night.png
BACKGROUND_EDIT: "Nighttime exterior, embracing his son"

::SCRIPT::
- CHARACTER: Narrator
  LINE: He is sitting on the edge of the grave, holding his dead son in his arms, rocking him. Gage is back to us. We see only a small limp figure in a dark suit. Hair flops limply.
  EXPRESSION: null
- CHARACTER: Louis
  LINE: It’s going to be all right...I swear it’s going to be all right...
  EXPRESSION: Desperate
- CHARACTER: Narrator
  LINE: The canvas tarp has been spread open to the right. Louis begins to lay his son down on it.
  EXPRESSION: null

::SCENE::
LOCATION: T
MOOD: Unspecified
CHARACTERS: Narrator
BACKGROUND_IMAGE: t_image.png
BACKGROUND_EDIT: "Unspecified"

::SCRIPT::
- CHARACTER: Narrator
  LINE: EXT. T
  EXPRESSION: null

::SCENE::
LOCATION: Ground beside a tarp
MOOD: Somber
CHARACTERS: Narrator
BACKGROUND_IMAGE: ground_tarp.png
BACKGROUND_EDIT: "Close-up on the ground beside a tarp, littered with flower petals."

::SCRIPT::
- CHARACTER: Narrator
  LINE: It’s littered with flower petals. One limp hand appears among them.
  EXPRESSION: null

::SCENE::
LOCATION: Louis
MOOD: Grim, Determined
CHARACTERS: Louis, Gage (deceased)
BACKGROUND_IMAGE: louis_burying.png
BACKGROUND_EDIT: "Louis closing a tarp over Gage's body, producing rope."

::SCRIPT::
- CHARACTER: Louis
  LINE: He closes the tarp over GAGE, making a roll. He then produces rope from the duffle bag. He cuts the rope and begins to tie one piece around one end of the canvas roll containing the corpse of his son.
  EXPRESSION: null

::SCENE::
LOCATION: Jetliner in the night sky
MOOD: Neutral
CHARACTERS: Pilot (voice)
BACKGROUND_IMAGE: jetliner_night.png
BACKGROUND_EDIT: "A jetliner flying through the night sky."

::SCRIPT::
- CHARACTER: Pilot (voice)
  LINE: Good evening again, ladies and gentlemen...
  EXPRESSION: null

::SCENE::
LOCATION: The Jetliner, with Rachel
MOOD: Tense
CHARACTERS: Rachel, PascoW, Seatmate
BACKGROUND_IMAGE: jetliner_interior.png
BACKGROUND_EDIT: "Interior of a jetliner. Rachel is seated, looking tense. PascoW is across the aisle, bloody but serene. Her seatmate is knitting."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Her seatmate is knitting something. Across the aisle sits VICTOR PASCOW, bloody but serene, hands clasped in his lap, looking straight ahead. RACHEL looks around tensely.
  EXPRESSION: null
- CHARACTER: Pilot (continues)
  LINE: I’m delighted to tell you that we've got a strong tail-wind tonight and we expect to arrive at Boston’s Logan Airport almost on time.
  EXPRESSION: null
- CHARACTER: PascoW
  LINE: That’s one for our side!
  EXPRESSION: Triumphant
- CHARACTER: Rachel
  LINE: Thank God.
  EXPRESSION: Relieved
- CHARACTER: Narrator
  LINE: Her SEATMATE looks at her a bit strangely.
  EXPRESSION: Curious

::SCENE::
LOCATION: The Graveyard, with Louis
MOOD: Anxious, Urgent
CHARACTERS: Louis
BACKGROUND_IMAGE: graveyard_louis.png
BACKGROUND_EDIT: "Louis carrying the rolled body and duffle bag, running bent over. He reaches a wall. Sound of another motor."

::SCRIPT::
- CHARACTER: Narrator
  LINE: He's got the bundle containing his son and the duffle-bag with the tools. He runs bent over. He reaches the wall and there's the SOUND of another motor. He crouches at the base of the wall.
  EXPRESSION: null

::SCENE::
LOCATION: The Road
MOOD: Ominous
CHARACTERS: Narrator
BACKGROUND_IMAGE: road_police_car.png
BACKGROUND_EDIT: "A police car with a spotlight moving along a wall."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Here comes that same police car. The spotlight runs along the wall.
  EXPRESSION: null

::SCENE::
LOCATION: Louis
MOOD: Fearful
CHARACTERS: Louis
BACKGROUND_IMAGE: louis_hiding.png
BACKGROUND_EDIT: "Louis crouching at the base of a wall, sweating."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Crouching against his side of the wall and sweating.
  EXPRESSION: null

::SCENE::
LOCATION: The Police Car
MOOD: Suspenseful
CHARACTERS: Narrator, Cop
BACKGROUND_IMAGE: police_car_stopped.png
BACKGROUND_EDIT: "A police car stops. A cop gets out and walks slowly toward a wall."

::SCRIPT::
- CHARACTER: Narrator
  LINE: It stops. The COP gets out. He walks slowly toward the wall.
  EXPRESSION: null

::SCENE::
LOCATION: Louis
MOOD: Terrified
CHARACTERS: Louis, Cop
BACKGROUND_IMAGE: louis_scared.png
BACKGROUND_EDIT: "Louis crouching. A cop looks over the top of the wall, then turns his back."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Crouched. Now we see the COP looking over the top. If he looks down... but he doesn’t, instead he turns around so we see his back. LOUIS looks up, miserably scared, pouring sweat.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Silence. Then: SOUND of the cop taking a whiz.
  EXPRESSION: null

::SCENE::
LOCATION: The Cop
MOOD: Relieved, then dismissive
CHARACTERS: Cop
BACKGROUND_IMAGE: cop_relieved.png
BACKGROUND_EDIT: "The cop zips up his fly. He looks back at the cemetery for a moment."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Ah! Relief. SOUND of his fly being zipped. He looks back at the cemetery for a moment.
  EXPRESSION: null
- CHARACTER: Cop
  LINE: I ain’t afraid of no ghost.
  EXPRESSION: Defiant
- CHARACTER: Narrator
  LINE: He walks back to his cruiser, gets in, and hauls ass.
  EXPRESSION: null

::SCENE::
LOCATION: Louis, Behind the Wall
MOOD: Relief, Cautious
CHARACTERS: Louis
BACKGROUND_IMAGE: louis_post_escape.png
BACKGROUND_EDIT: "Louis collapses with relief, then gets up and looks cautiously over the wall. His car is parked on the other side."

::SCRIPT::
- CHARACTER: Narrator
  LINE: He collapses with relief. Then he gets up and looks cautiously over the wall. Nothing there but his car, parked a little way down on the other side of the road.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: He tosses the duffle bag over the top of the wall. He puts the canvas roll containing GAGE on top of the wall. Then he vaults over.
  EXPRESSION: null

::SCENE::
LOCATION: The Street Side of the Wall, with Louis
MOOD: Hurried, Anxious
CHARACTERS: Louis
BACKGROUND_IMAGE: louis_street_side.png
BACKGROUND_EDIT: "Louis taking the roll and duffle bag, running across the road like a soldier crossing enemy territory."

::SCRIPT::
- CHARACTER: Narrator
  LINE: He takes the roll, gets the duttle bag hooked over his shoulder by the string, and runs across the road like a soldier crossing enemy territory. He goes to the rear of the wagon.
  EXPRESSION: null

::SCENE::
LOCATION: The Rear of the Wagon, with Louis
MOOD: Frustrated, Exposed
CHARACTERS: Louis
BACKGROUND_IMAGE: louis_wagon_rear.png
BACKGROUND_EDIT: "Louis puts the body down, searching his pockets for keys. Mild consternation, then more."

::SCRIPT::
- CHARACTER: Narrator
  LINE: He puts the body down. He feels in his pocket for his keys. No keys. Mild consternation. He looks around, feeling exposed. The other pocket. Still no keys. More consternation. He begins to hunt feverishly through his pockets. Maybe in his jacket? Nope.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: SOUND: An approaching car.
  EXPRESSION: null

::SCENE::
LOCATION: Passing Car
MOOD: Neutral
CHARACTERS: Narrator
BACKGROUND_IMAGE: passing_car.png
BACKGROUND_EDIT: "A civilian car passes, not the police car."

::SCRIPT::
- CHARACTER: Narrator
  LINE: A civilian--not the ubiquitous cop.
  EXPRESSION: null

::SCENE::
LOCATION: Louis
MOOD: Desperate
CHARACTERS: Louis
BACKGROUND_IMAGE: louis_pockets_empty.png
BACKGROUND_EDIT: "Louis turns his pockets out, spilling change everywhere. Nothing."

::SCRIPT::
- CHARACTER: Narrator
  LINE: He turns his pockets out, spilling change everywhere. Nothing.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Suddenly a little light goes on in his eyes. He goes to the driver's side of the car and looks in at:
  EXPRESSION: null

::SCENE::
LOCATION: Ignition, Louis's POV
MOOD: Hopeful
CHARACTERS: Louis
BACKGROUND_IMAGE: ignition_keys.png
BACKGROUND_EDIT: "Louis's point of view looking into the car's ignition, showing the keys are in the switch."

::SCRIPT::
- CHARACTER: Narrator
  LINE: The keys are in the switch.
  EXPRESSION: null

::SCENE::
LOCATION: Louis
MOOD: Urgent, Then Frozen
CHARACTERS: Louis
BACKGROUND_IMAGE: louis_snatching_keys.png
BACKGROUND_EDIT: "Louis snatches the keys and returns to the wagon. He opens the doorgate, puts Gage's body in gently, then the duffle bag. He closes the doorgate and returns to the front of the car. He opens the driver's door and freezes."

::SCRIPT::
- CHARACTER: Narrator
  LINE: He snatches the keys and returns to the back of the wagon. He uses the key to open the doorgate. He puts gage's body in gently, then the duffle bag. He closes the doorgate and returns to the front of the car. He opens the driver's door and freezes.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: LOUIS returns to the rear, gets his keys from the doorgate, comes back to the front, gets in, and drives away.
  EXPRESSION: null

::SCENE::
LOCATION: A Jetway at Logan International
MOOD: Rushed, Determined
CHARACTERS: Rachel, PascoW, Debarking Passengers
BACKGROUND_IMAGE: logan_jetway.png
BACKGROUND_EDIT: "People debarking into the gate area. Rachel is running fast, pushing people. PascoW is walking near her."

::SCRIPT::
- CHARACTER: Narrator
  LINE: People are debarking into the gate area. Through them comes RACHEL, running fast, pushing some people, excusing herself incoherently. PASCOW is walking near her.
  EXPRESSION: null
- CHARACTER: PascoW
  LINE: There's just time. If you run.
  EXPRESSION: Encouraging
- CHARACTER: Narrator
  LINE: Without looking at PASCOW, RACHEL takes off her shoes and runs.
  EXPRESSION: null

::SCENE::
LOCATION: The Concourse, with Rachel
MOOD: Frantic
CHARACTERS: Rachel
BACKGROUND_IMAGE: concourse_rachel.png
BACKGROUND_EDIT: "Rachel sprinting down the concourse at high speed."

::SCRIPT::
- CHARACTER: Narrator
  LINE: She's sprinting down the concourse--look out, Joanie Benoit!
  EXPRESSION: null

::SCENE::
LOCATION: Gate 27, with Female Gate Agent and PascoW
MOOD: Urgent, Puzzled
CHARACTERS: Female Gate Agent, PascoW
BACKGROUND_IMAGE: gate_27.png
BACKGROUND_EDIT: "A female gate agent is closing the jetway door. PascoW is present."

::SCRIPT::
- CHARACTER: Female Gate Agent
  LINE: Don't do that, babe.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The GATE AGENT looks puzzled, as if she just had a thought (or maybe a gas pain). She stops closing the door. RACHEL runs into the area. She sees:
  EXPRESSION: null

::SCENE::
LOCATION: The Jet Plane, through the Gate Windows
MOOD: Just Missed
CHARACTERS: Narrator
BACKGROUND_IMAGE: jet_plane_moving.png
BACKGROUND_EDIT: "The jet plane is just starting to swing ponderously away from the jetway."

::SCRIPT::
- CHARACTER: Narrator
  LINE: It is just starting to swing ponderously away from the jetway.
  EXPRESSION: null

::SCENE::
LOCATION: Rachel and Female Gate Agent (PascoW is gone)
MOOD: Desperate
CHARACTERS: Rachel, Female Gate Agent
BACKGROUND_IMAGE: rachel_gate_agent.png
BACKGROUND_EDIT: "Rachel is distraught. The gate agent is at her stand."

::SCRIPT::
- CHARACTER: Rachel
  LINE: Hake it come back!
  EXPRESSION: Pleading
- CHARACTER: Female Gate Agent
  LINE: I can't--
  EXPRESSION: Helpless
- CHARACTER: Narrator
  LINE: RACHEL bolts down the jetway. The GATE AGENT stares after her, and then runs for her stand, where we can see FLIGHT 61 and BANGOR on the slide-cards. She picks up her mike.
  EXPRESSION: null

::SCENE::
LOCATION: The Jetway Night
MOOD: Desperate, Furious
CHARACTERS: Rachel
BACKGROUND_IMAGE: jetway_night_rachel.png
BACKGROUND_EDIT: "Rachel stands alone at the end of the jetway. Amplified sounds of jet engines."

::SCRIPT::
- CHARACTER: Narrator
  LINE: RACHEL stands all alone at the end of it.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: AMPLIFIED SOUNDS OF JET ENGINES.
  EXPRESSION: null
- CHARACTER: Rachel
  LINE: COME BACK, MOTHERFUCKER!!
  EXPRESSION: Furious

::SCENE::
LOCATION: The Jet, Rachel's POV
MOOD: Hopeful
CHARACTERS: Narrator
BACKGROUND_IMAGE: jet_turning_back.png
BACKGROUND_EDIT: "Rachel's point of view. The jet starts to swing back to pick her up."

::SCRIPT::
- CHARACTER: Narrator
  LINE: It starts to swing back to pick her up.
  EXPRESSION: null

::SCENE::
LOCATION: Rachel
MOOD: Reassured
CHARACTERS: Rachel, PascoW
BACKGROUND_IMAGE: rachel_pascoW_return.png
BACKGROUND_EDIT: "PascoW appears behind Rachel and puts a hand on her shoulder."

::SCRIPT::
- CHARACTER: Narrator
  LINE: PASCOW appears behind her and puts a hand on her shoulder.
  EXPRESSION: null
- CHARACTER: PascoW
  LINE: You're doing just fine.
  EXPRESSION: Reassuring

::SCENE::
LOCATION: Jud Crandall, On His Porch
MOOD: Asleep, Unaware
CHARACTERS: Jud Crandall
BACKGROUND_IMAGE: jud_porch_sleep.png
BACKGROUND_EDIT: "Jud is fast asleep on his porch with Walkman headphones on."

::SCRIPT::
- CHARACTER: Narrator
  LINE: He's fast asleep with the tinny sound of Graham Parker coming out of his Walkman 'phones.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: SOUND: An approaching car.
  EXPRESSION: null

::SCENE::
LOCATION: The Creed House
MOOD: Purposeful
CHARACTERS: Louis
BACKGROUND_IMAGE: creed_house_wagon.png
BACKGROUND_EDIT: "A station wagon turns in and parks at the Creed house. Louis gets out."

::SCRIPT::
- CHARACTER: Narrator
  LINE: The station wagon turns in and parks. LOUIS gets out. He opens the back, removes the body in the tarp and the duffle bag filled with tools. He manages to get everything together and walks to the edge of the path. He looks at:
  EXPRESSION: null

::SCENE::
LOCATION: The Path to the Pet Sematary, Louis's POV
MOOD: Foreboding
CHARACTERS: Louis
BACKGROUND_IMAGE: path_pet_sematary.png
BACKGROUND_EDIT: "Louis's point of view looking down a path, glimmering in the dark."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Off it goes, glimmering in the dark.
  EXPRESSION: null

::SCENE::
LOCATION: Louis
MOOD: Pleading, Determined
CHARACTERS: Louis, Gage (deceased)
BACKGROUND_IMAGE: louis_holding_gage.png
BACKGROUND_EDIT: "Louis holding the corpse of his little boy."

::SCRIPT::
- CHARACTER: Louis
  LINE: Please God--let this work.
  EXPRESSION: Pleading
- CHARACTER: Narrator
  LINE: He sets off.
  EXPRESSION: null

::SCENE::
LOCATION: Jud, On His Porch
MOOD: Unaware
CHARACTERS: Jud
BACKGROUND_IMAGE: jud_porch_still_asleep.png
BACKGROUND_EDIT: "Jud is still zonked out on his porch."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Zonked out. He missed the whole thing. Nice going, Jud.
  EXPRESSION: Sarcastic

::SCENE::
LOCATION: Outside the Arch to the Pet Sematary, with Louis
MOOD: Ethereal, Solemn
CHARACTERS: Louis
BACKGROUND_IMAGE: pet_sematary_arch.png
BACKGROUND_EDIT: "Louis passes under the arch like a ghost."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Louis passes under like a ghost.
  EXPRESSION: null

::SCENE::
LOCATION: The Pet Sematary, with Louis
MOOD: Grieving, Determined
CHARACTERS: Louis
BACKGROUND_IMAGE: pet_sematary_louis.png
BACKGROUND_EDIT: "Louis is crying as he crosses to the deadfall."

::SCRIPT::
- CHARACTER: Narrator
  LINE: LOUIS is crying. He crosses to the deadfall.
  EXPRESSION: null
- CHARACTER: Louis
  LINE: Ain't gonna stop, Gage. Ain't gonna look down.
  EXPRESSION: Determined

::SCENE::
LOCATION: Louis, A New Angle
MOOD: Foreboding
CHARACTERS: Louis
BACKGROUND_IMAGE: louis_deadfall_top.png
BACKGROUND_EDIT: "Louis reaches the top of the deadfall. A snarling face is woven into it behind him."

::SCRIPT::
- CHARACTER: Narrator
  LINE: He reaches the top. And woven into the deadfall, behind him, facing the Pet Sematary, is that snarling face.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: LOUIS descends the other side.
  EXPRESSION: null

::SCENE::
LOCATION: The Foot of the Deadfall, Woods Side
MOOD: Mysterious, Eerie
CHARACTERS: Louis
BACKGROUND_IMAGE: woods_path_glow.png
BACKGROUND_EDIT: "Louis reaches the bottom and looks at the path winding through gigantic trees, which glows slightly."

::SCRIPT::
- CHARACTER: Narrator
  LINE: LOUIS reaches the bottom and looks at:
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The path winds onward through those gigantic trees--it glows slightly.
  EXPRESSION: null

::SCENE::
LOCATION: Louis, Moving Up the Path
MOOD: Determined, Uneasy
CHARACTERS: Louis
BACKGROUND_IMAGE: louis_woods_path.png
BACKGROUND_EDIT: "Louis is moving up the glowing path in the woods."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Louis, Moving Up the Path
  EXPRESSION: null

::SCENE::
LOCATION: Louis, At the Edge of Little God Swamp
MOOD: Apprehensive, Eerie
CHARACTERS: Louis
BACKGROUND_IMAGE: louis_swamp_edge.png
BACKGROUND_EDIT: "The phosphorescent glow is more pronounced. Crickets and frogs sound. Mucky water, hummocks, and fog drift through dead trees."

::SCRIPT::
- CHARACTER: Narrator
  LINE: That phosphorescent glow is a lot more pronounced. SOUNDS of CRICKETS and FROGS. The water is mucky and still. Hummocks stick up like knobs on the back of a creature best not seen. Fog drifts through the dead trees. LOUIS doesn't want to go in there. Smart man. I wouldn't either.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: But he does.
  EXPRESSION: null

::SCENE::
LOCATION: The Hertz Desk, at BIA with Rachel and Clerk--and PascoW
MOOD: Impatient, Determined
CHARACTERS: PascoW, Rachel, Hertz Clerk
BACKGROUND_IMAGE: hertz_desk.png
BACKGROUND_EDIT: "PascoW is lounging. Rachel and the Clerk are at the desk. Papers are scattered."

::SCRIPT::
- CHARACTER: Narrator
  LINE: PASCOW is lounging back against the rack of folders--and getting some of them bloody.
  EXPRESSION: null
- CHARACTER: Hertz Clerk
  LINE: I'm sorry...it's been very busy tonight. I really don't have anything.
  EXPRESSION: Apologetic
- CHARACTER: PascoW
  LINE: What about the Aries K with the scratch on the side?
  EXPRESSION: Insistent
- CHARACTER: Hertz Clerk
  LINE: I do have an Aries K, but it came in sort of beat up--there's a long scrape up one side--
  EXPRESSION: Hesitant
- CHARACTER: Rachel
  LINE: I'll take it.
  EXPRESSION: Determined

::SCENE::
LOCATION: Louis, In Little God Swamp
MOOD: Surreal, Ominous
CHARACTERS: Louis, Gage (deceased)
BACKGROUND_IMAGE: louis_swamp_walking.png
BACKGROUND_EDIT: "Louis walks toward the camera with Gage in his arms and the duffle bag. Mist swirls. The landscape is weird. Many swampy sounds."

::SCRIPT::
- CHARACTER: Narrator
  LINE: He comes walking toward THE CAMERA with GAGE in his arms and the duffle bag over his shoulder. Mist swirls around him. The landscape is weird, surreal. CRICKET SOUNDS, AMPLIFIED. In fact there are a lot of swampy, marshy SOUNDS--too many. It sounds almost prehistoric.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: SOUND: HARSH, SCREAMING LAUGHTER
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: LOUIS stops. He looks slowly around at:
  EXPRESSION: null

::SCENE::
LOCATION: Mist-Face, Louis's POV
MOOD: Demonic, Terrifying
CHARACTERS: Narrator
BACKGROUND_IMAGE: mist_face_demonic.png
BACKGROUND_EDIT: "Louis's point of view. A demonic face takes shape in the mist, floating slowly toward the camera, with a long tongue. Its eyes blow out blood and goo."

::SCRIPT::
- CHARACTER: Narrator
  LINE: A demonic face takes shape in the mist and FLOATS SLOWLY TOWARD THE CAMERA. It runs out a tongue that's about nine feet long. Its eyes blow out. Blood and thick, gooey stuff runs from the sockets.
  EXPRESSION: null

::SCENE::
LOCATION: Louis
MOOD: Disbelieving, Recovering
CHARACTERS: Louis
BACKGROUND_IMAGE: louis_eyes_closed.png
BACKGROUND_EDIT: "Louis closes his eyes, then opens them."

::SCRIPT::
- CHARACTER: Narrator
  LINE: He closes his eyes. After a moment he opens them.
  EXPRESSION: null

::SCENE::
LOCATION: Little God Swamp, Louis's POV
MOOD: Unchanged, Still Eerie
CHARACTERS: Narrator
BACKGROUND_IMAGE: swamp_empty_mist.png
BACKGROUND_EDIT: "Louis's point of view. Nothing is there."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Nothing there.
  EXPRESSION: null

::SCENE::
LOCATION: Louis
MOOD: Self-Reassuring
CHARACTERS: Louis
BACKGROUND_IMAGE: louis_rationalizing.png
BACKGROUND_EDIT: "Louis speaking, trying to dismiss what he saw."

::SCRIPT::
- CHARACTER: Louis
  LINE: See? Dust imagination. Dust--
  EXPRESSION:null

::SCENE::
LOCATION: Louis's Feet
MOOD: Uneasy, Threatened
CHARACTERS: Louis
BACKGROUND_IMAGE: louis_feet_tentacle.png
BACKGROUND_EDIT: "Louis's feet are in mist. A thick tentacle slimes its way out of the water and wraps around his ankle."

::SCRIPT::
- CHARACTER: Narrator
  LINE: We can barely see them because they are thick in mist, but he is standing on a couple of low, marshy tussocks. Suddenly a thick tentacle slimes its way out of the standing water and slithers around his ankle.
  EXPRESSION: null

::SCENE::
LOCATION: Louis, Looking Down
MOOD: Denying
CHARACTERS: Louis
BACKGROUND_IMAGE: louis_looking_down.png
BACKGROUND_EDIT: "Louis looks down, acknowledging something but denying its reality."

::SCRIPT::
- CHARACTER: Louis
  LINE: Nothing...there.
  EXPRESSION: Denying

::SCENE::
LOCATION: Louis's Feet
MOOD: Normalizing
CHARACTERS: Narrator
BACKGROUND_IMAGE: louis_feet_tentacle_gone.png
BACKGROUND_EDIT: "The tentacle falls away from his ankle."

::SCRIPT::
- CHARACTER: Narrator
  LINE: The tentacle falls away.
  EXPRESSION: null

::SCENE::
LOCATION: Louis, In Little God Swamp
MOOD: Disturbing, Persistent
CHARACTERS: Louis
BACKGROUND_IMAGE: louis_swamp_noises.png
BACKGROUND_EDIT: "Myriad unpleasant sounds emanate from the swamp as Louis continues on."

::SCRIPT::
- CHARACTER: Narrator
  LINE: MYRIAD SOUNDS, none of them pleasant--laughter, gobbling howls, screams. Sounds like the swamp has been invaded by a pack of escaped lunatics. LOUIS continues on regardless.
  EXPRESSION: null

::SCENE::
LOCATION: Woods
MOOD: Transitional
CHARACTERS: Narrator
BACKGROUND_IMAGE: woods_transition.png
BACKGROUND_EDIT: "Transition to a new scene in the woods."

::SCRIPT::
- CHARACTER: Narrator
  LINE: LO
  EXPRESSION: null

::SCENE::
LOCATION: Woods
MOOD: Terror
CHARACTERS: Narrator, Louis
BACKGROUND_IMAGE: woods_louis_pov.png
BACKGROUND_EDIT: "Louis's point of view, woods, approaching sounds"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Uis comes into the frame. He's obviously tiring now, but he keeps moving along.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: SOUND: Approaching footsteps. Big ones. Thudding ones. Something is coming which sounds approximately the size of a Tyrannosaurus Rex. And it just keeps getting louder and louder and louder.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: LOUIS looks plenty scared.
  EXPRESSION: Scared
- CHARACTER: Narrator
  LINE: SOUND: A falling tree.
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue moving"
  TARGET: woods_louis_pov_2
  STATE_CHANGE: fear = +2
  CONDITION: null

::SCENE::
LOCATION: Woods, Louis's POV
MOOD: Growing Terror
CHARACTERS: Narrator
BACKGROUND_IMAGE: woods_louis_pov_2.png
BACKGROUND_EDIT: "Louis's point of view, woods, falling trees"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Those SOUNDS keep getting closer and closer. Another tree falls--we see this one. And now we see a SHAPE--just a SHAPE.
  EXPRESSION: null

::PATHS::
- CHOICE: "Observe the shape"
  TARGET: louis_2
  STATE_CHANGE: fear = +3
  CONDITION: null

::SCENE::
LOCATION: Louis
MOOD: Extreme Terror
CHARACTERS: Narrator, Louis
BACKGROUND_IMAGE: louis_2.png
BACKGROUND_EDIT: "Louis looking up in terror"

::SCRIPT::
- CHARACTER: Narrator
  LINE: He's scared almost to death. His face turns up...up...up.
  EXPRESSION: Terrified

::PATHS::
- CHOICE: "Look up"
  TARGET: the_woods_and_the_shape_louis_pov
  STATE_CHANGE: fear = +5
  CONDITION: null

::SCENE::
LOCATION: The Woods--and the Shape, Louis's POV
MOOD: Unspeakable Horror
CHARACTERS: Narrator, Louis
BACKGROUND_IMAGE: the_woods_and_the_shape_louis_pov.png
BACKGROUND_EDIT: "Louis's point of view, a monstrous shape looming"

::SCRIPT::
- CHARACTER: Narrator
  LINE: It is vaguely manlike: perhaps sixty feet tall, perhaps eighty. We don't see it very well, nor do we have to--I'm not even sure it's flesh and blood. But there is a clear suggestion of a head. Now it turns and looks down...looks at LOUIS CREED. We see great yellow eyes the size of lighthouse lamps.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: It makes a huge GRUNTING SOUND...and then walks on.
  EXPRESSION: null

::PATHS::
- CHOICE: "Observe its departure"
  TARGET: louis_3
  STATE_CHANGE: fear = -5, shock = +5
  CONDITION: null

::SCENE::
LOCATION: Louis
MOOD: Shock and Realization
CHARACTERS: Narrator, Louis
BACKGROUND_IMAGE: louis_3.png
BACKGROUND_EDIT: "Louis looking in the direction the shape departed"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The SOUND OF FOOTFALLS is slowly diminishing.
  EXPRESSION: null
- CHARACTER: Louis
  LINE: It was the Wendigo. Dear God, I think the Wendigo just passed within sixty feet of me.
  EXPRESSION: Trembling
- CHARACTER: Narrator
  LINE: Slowly he begins to walk again.
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue walking"
  TARGET: louis_4
  STATE_CHANGE: resolve = +2
  CONDITION: null

::SCENE::
LOCATION: Louis, a New Angle
MOOD: Grim Determination
CHARACTERS: Narrator, Louis
BACKGROUND_IMAGE: louis_4.png
BACKGROUND_EDIT: "Louis approaching a fallen tree"

::SCRIPT::
- CHARACTER: Narrator
  LINE: In the extreme f.g. is a tree which has just fallen--it is no small tree, either, but a great big old fir.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: LOUIS approaches it. Stops. Looks at the tree. Looks down at:
  EXPRESSION: null

::PATHS::
- CHOICE: "Examine the ground"
  TARGET: the_forest_floor_louis_pov
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: The Forest Floor, Louis's POV
MOOD: Unnatural and Disturbing
CHARACTERS: Narrator
BACKGROUND_IMAGE: the_forest_floor_louis_pov.png
BACKGROUND_EDIT: "Louis's point of view, giant animal track"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Here is a gigantic animal track--if it was full of water, LOUIS could swim in it. It looks like no animal track we've ever seen before. Three big claws at the end of it.
  EXPRESSION: null

::PATHS::
- CHOICE: "Look up again"
  TARGET: louis_5
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Louis
MOOD: Set Jaw
CHARACTERS: Narrator, Louis
BACKGROUND_IMAGE: louis_5.png
BACKGROUND_EDIT: "Louis looking up with a determined expression"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Looks up again. His face is set and hard.
  EXPRESSION: Determined
- CHARACTER: Louis
  LINE: It doesn't matter. Come on, Gage.
  EXPRESSION: Resolute
- CHARACTER: Narrator
  LINE: He starts to walk again.
  EXPRESSION: null

::PATHS::
- CHOICE: "Walk on"
  TARGET: the_micmac_burying_ground
  STATE_CHANGE: grief = +2, determination = +3
  CONDITION: null

::SCENE::
LOCATION: The Micmac Burying Ground
MOOD: Desolate and Mournful
CHARACTERS: Narrator, Louis
BACKGROUND_IMAGE: the_micmac_burying_ground.png
BACKGROUND_EDIT: "Micmac burying ground, wind, damaged cairns"

::SCRIPT::
- CHARACTER: Narrator
  LINE: SOUND: The wind, lonesome and keening.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: THE CAMERA MOVES SLOWLY toward the slope, dreaming its way over those rocky cairns...most of them burst apart.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: SOUND: Tortured breathing. Panting.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: LOUIS toils his way into view, carrying his bundle. He reaches the top. He makes his way slowly into the burying ground. He stumbles over a rock. Falls down. Slowly gathers his things together and gets up again. He goes a little further and then stops and looks at:
  EXPRESSION: Exhausted

::PATHS::
- CHOICE: "Observe the grave"
  TARGET: a_broken_cairn_and_the_grave_beneath_louis_pov
  STATE_CHANGE: exhaustion = +3
  CONDITION: null

::SCENE::
LOCATION: A Broken Cairn and the Grave Beneath, Louis's POV
MOOD: Disturbing Remnants
CHARACTERS: Narrator
BACKGROUND_IMAGE: a_broken_cairn_and_the_grave_beneath_louis_pov.png
BACKGROUND_EDIT: "Louis's point of view, broken cairn, shredded garbage bag"

::SCRIPT::
- CHARACTER: Narrator
  LINE: We can also see the shredded remains of a green garbage bag.
  EXPRESSION: null

::PATHS::
- CHOICE: "Prepare for the task"
  TARGET: louis_6
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Louis
MOOD: Utter Exhaustion
CHARACTERS: Narrator, Louis
BACKGROUND_IMAGE: louis_6.png
BACKGROUND_EDIT: "Louis kneeling, preparing tools"

::SCRIPT::
- CHARACTER: Narrator
  LINE: He slowly kneels down. He puts the canvas tarp to one side and slowly takes the pick and shovel from the duffle bag. By now he is clearly a man approaching total exhaustion.
  EXPRESSION: Exhausted

::PATHS::
- CHOICE: "Continue the task"
  TARGET: a_country_road_with_an_aries_k
  STATE_CHANGE: exhaustion = +5
  CONDITION: null

::SCENE::
LOCATION: A Country Road, With an Aries K
MOOD: Ominous Presence
CHARACTERS: Narrator
BACKGROUND_IMAGE: a_country_road_with_an_aries_k.png
BACKGROUND_EDIT: "Aries K driving on a country road"

::SCRIPT::
- CHARACTER: Narrator
  LINE: It tracks past THE CAMERA.
  EXPRESSION: null

::PATHS::
- CHOICE: "Enter the car"
  TARGET: the_aries_k_with_rachel_and_pascow
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: The Aries K With Rachel and Pascow
MOOD: Tense and Frightened
CHARACTERS: Narrator, Rachel, Pascow
BACKGROUND_IMAGE: the_aries_k_with_rachel_and_pascow.png
BACKGROUND_EDIT: "Interior of an Aries K, Rachel driving, Pascow tense"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Both of them look tense. RACHEL is bolt upright behind the wheel.
  EXPRESSION: Tense
- CHARACTER: Narrator
  LINE: Suddenly BANG! as one of the tires blow.
  EXPRESSION: null

::PATHS::
- CHOICE: "Observe the consequence"
  TARGET: the_aries_k_2
  STATE_CHANGE: shock = +3
  CONDITION: null

::SCENE::
LOCATION: The Aries K
MOOD: Catastrophic
CHARACTERS: Narrator
BACKGROUND_IMAGE: the_aries_k_2.png
BACKGROUND_EDIT: "Aries K skidding off the road and hitting a tree"

::SCRIPT::
- CHARACTER: Narrator
  LINE: It goes skidding and slueing across the road, the rear tire half off the rim. IT climbs the curb and hits a tree.
  EXPRESSION: null

::PATHS::
- CHOICE: "Exit the vehicle"
  TARGET: rachel_2
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Rachel
MOOD: Shaken but Resilient
CHARACTERS: Narrator, Rachel
BACKGROUND_IMAGE: rachel_2.png
BACKGROUND_EDIT: "Rachel inside the crashed car, wearing a seatbelt"

::SCRIPT::
- CHARACTER: Narrator
  LINE: She lurches forward, but she’s wearing her seat-belt--good girl!
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: She unbuckles it and gets out.
  EXPRESSION: null

::PATHS::
- CHOICE: "Assess the damage"
  TARGET: rachel_3
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Rachel
MOOD: Despair and Confusion
CHARACTERS: Narrator, Rachel, Pascow
BACKGROUND_IMAGE: rachel_3.png
BACKGROUND_EDIT: "Rachel standing by the crashed car, Pascow approaching"

::SCRIPT::
- CHARACTER: Narrator
  LINE: She looks at the car, which now has quite a bit more wrong with it than just a scratch up the side.
  EXPRESSION: Distraught
- CHARACTER: Narrator
  LINE: RACHEL slumps, near tears. LOUIS isn't the only one who’s been through a lot tonight.
  EXPRESSION: Despairing
- CHARACTER: Rachel
  LINE: Now what?
  EXPRESSION: Lost
- CHARACTER: Narrator
  LINE: PASCOW comes from around the tree as RACHEL walks to the road, looking for cars, or something. He looks urgent and upset.
  EXPRESSION: Urgent
- CHARACTER: Pascow
  LINE: It's trying to stop you. Do you hear me? It's trying to stop you.
  EXPRESSION: Urgent
- CHARACTER: Narrator
  LINE: RACHEL looks around uncertainly... a little afraid. As she scans the scene she looks at--and through--PASCOW.
  EXPRESSION: Afraid
- CHARACTER: Rachel
  LINE: Is anyone there?
  EXPRESSION: Uncertain
- CHARACTER: Narrator
  LINE: After a moment of silence she turns back to the road. Lights appear and brighten as a car approaches. RACHEL steps to the shoulder and after a moment she sticks out her thumb, surely for the first time in her life.
  EXPRESSION: Hopeful
- CHARACTER: Narrator
  LINE: The car sweeps by her without slowing.
  EXPRESSION: Dejected

::PATHS::
- CHOICE: "Continue walking and hitchhiking"
  TARGET: gages_cairn_cu
  STATE_CHANGE: hope = -3, despair = +2
  CONDITION: null

::SCENE::
LOCATION: Gage's Cairn, CU
MOOD: Somber Finality
CHARACTERS: Narrator, Louis
BACKGROUND_IMAGE: gages_cairn_cu.png
BACKGROUND_EDIT: "Close-up on Gage's cairn, Louis placing rocks"

::SCRIPT::
- CHARACTER: Narrator
  LINE: LOUIS'S hands enter the shot and put a few more rocks on it. THE CAMERA PULLS BACK and we see him surveying his work. Beside him is the canvas tarp, now open and empty.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Absently, LOUIS stuffs the tarp into the duffle bag (where his tools have also been replaced) and stands up with a wince. One hand goes to his lower back. He looks down at the cairn.
  EXPRESSION: Painful
- CHARACTER: Louis
  LINE: Come back to me, Gage. Come back to us.
  EXPRESSION: Heartbroken
- CHARACTER: Narrator
  LINE: He turns away toward the stairs.
  EXPRESSION: null

::PATHS::
- CHOICE: "Leave the burying ground"
  TARGET: rachel_on_route_9
  STATE_CHANGE: grief = +5
  CONDITION: null

::SCENE::
LOCATION: Rachel, On Route 9
MOOD: Frustrated and Angry
CHARACTERS: Narrator, Rachel
BACKGROUND_IMAGE: rachel_on_route_9.png
BACKGROUND_EDIT: "Rachel walking on the shoulder of Route 9, heels in hand"

::SCRIPT::
- CHARACTER: Narrator
  LINE: She's walking down the shoulder with her high heels in one hand.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Lights. An approaching car. She turns, thumb out. The car blasts by.
  EXPRESSION: null
- CHARACTER: Rachel
  LINE: MAY THE SEWERS OF RANGOON BACK UP IN YOUR BEDROOM, ASSHOLE!
  EXPRESSION: Furious
- CHARACTER: Narrator
  LINE: She starts walking again.
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue walking"
  TARGET: the_field_beside_louis_house
  STATE_CHANGE: anger = +3
  CONDITION: null

::SCENE::
LOCATION: The Field Beside Louis's House
MOOD: Weary Return
CHARACTERS: Narrator, Louis
BACKGROUND_IMAGE: the_field_beside_louis_house.png
BACKGROUND_EDIT: "Louis walking through a field, pushing a tire swing"

::SCRIPT::
- CHARACTER: Narrator
  LINE: LOUIS is moving down the path. As he passes the tire swing he pushes it, setting it in motion.
  EXPRESSION: null

::PATHS::
- CHOICE: "Enter the house"
  TARGET: the_garage_2
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: The Garage
MOOD: Exhaustion and Unawareness
CHARACTERS: Narrator, Louis, Church
BACKGROUND_IMAGE: the_garage_2.png
BACKGROUND_EDIT: "Louis entering the garage, Church hiding"

::SCRIPT::
- CHARACTER: Narrator
  LINE: LOUIS slings the duffle bag wearily to one side and goes into the kitchen. CHURCH is under the table but LOUIS Doesn't see him.
  EXPRESSION: Weary

::PATHS::
- CHOICE: "Go into the kitchen"
  TARGET: the_upstairs_hall
  STATE_CHANGE: exhaustion = +4
  CONDITION: null

::SCENE::
LOCATION: The Upstairs Hall
MOOD: Heavy Steps
CHARACTERS: Narrator, Louis
BACKGROUND_IMAGE: the_upstairs_hall.png
BACKGROUND_EDIT: "Louis walking slowly up the stairs and down the hall"

::SCRIPT::
- CHARACTER: Narrator
  LINE: SOUND of LOUIS slowly plodding up the stairs. He comes into view, dirty and exhausted, his hair hanging in his face. He walks down the hall toward the master bedroom.
  EXPRESSION: Exhausted

::PATHS::
- CHOICE: "Enter the bedroom"
  TARGET: the_bedroom_2
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: The Bedroom
MOOD: Stillness Before the Storm
CHARACTERS: Narrator
BACKGROUND_IMAGE: the_bedroom_2.png
BACKGROUND_EDIT: "Bedroom with an open closet door, Louis lying on the bed"

::SCRIPT::
- CHARACTER: Narrator
  LINE: on the immaculate bedspread and lies still.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: In this shot we should note the closet door is standing open.
  EXPRESSION: null

::PATHS::
- CHOICE: "Observe the burying ground"
  TARGET: the_micmac_burying_ground_featuring_gages_cairn
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: The Micmac Burying Ground, Featuring Gage’s Cairn
MOOD: Terrifying Resurrection
CHARACTERS: Narrator, Gage
BACKGROUND_IMAGE: the_micmac_burying_ground_featuring_gages_cairn.png
BACKGROUND_EDIT: "Close-up on Gage's cairn, a hand emerging"

::SCRIPT::
- CHARACTER: Narrator
  LINE: THE CAMERA MOVES IN SLOWLY. Holds. Nothing for a beat. Then: A small white hand slams up through the rocks, hopefully scaring the living shit out of us.
  EXPRESSION: Terrifying
- CHARACTER: Narrator
  LINE: CAMERA MOVES CLOSER as the hand begins to feel around. It takes one of the rocks and pushes it aside. Another. Another. Another.
  EXPRESSION:null
- CHARACTER: Narrator
  LINE: The SOUNDS are not encouraging. It is GRUNTING and GROWLING. There is nothing human here.
  EXPRESSION: Disturbing
- CHARACTER: Narrator
  LINE: Rocks begin to tumble as GAGE starts to come out of his grave.
  EXPRESSION: Horrific

::PATHS::
- CHOICE: "Return to Louis"
  TARGET: the_creed_bedroom_with_louis
  STATE_CHANGE: horror = +10
  CONDITION: null

::SCENE::
LOCATION: The Creed Bedroom, With Louis
MOOD: Deep Sleep
CHARACTERS: Narrator, Louis
BACKGROUND_IMAGE: the_creed_bedroom_with_louis.png
BACKGROUND_EDIT: "Louis sleeping soundly on the bed"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Fast asleep on the coverlet in his dirty jeans and black sweater.
  EXPRESSION: Peaceful

::PATHS::
- CHOICE: "Observe Rachel's progress"
  TARGET: rachel_4
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Rachel
MOOD: Hopeful
CHARACTERS: Narrator
BACKGROUND_IMAGE: rachel_4.png
BACKGROUND_EDIT: "Rachel walking on Route 9, another vehicle approaching"

::SCRIPT::
- CHARACTER: Narrator
  LINE: My babe is still takin’ a hike. But here comes another vehicle.
  EXPRESSION: Hopeful

::PATHS::
- CHOICE: "Witness the truck"
  TARGET: the_deadfall_in_the_pet_sematary
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: The Deadfall in the Pet Sematary
MOOD: Imminent Threat
CHARACTERS: Narrator, Gage
BACKGROUND_IMAGE: the_deadfall_in_the_pet_sematary.png
BACKGROUND_EDIT: "A snarling face at the deadfall, Gage approaching"

::SCRIPT::
- CHARACTER: Narrator
  LINE: THE CAMERA MOVES IN on that snarling face.
  EXPRESSION: Menacing
- CHARACTER: Narrator
  LINE: SOUNDS: GAGE coming. Dead dry breath. Low snarling noises.
  EXPRESSION: Sinister
- CHARACTER: Narrator
  LINE: Now we see small feet in dirty black shoes walking down the deadfall.
  EXPRESSION: Disturbing

::PATHS::
- CHOICE: "Observe Rachel's encounter"
  TARGET: rachel_5
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Rachel
MOOD: Strategic Seduction
CHARACTERS: Narrator, Rachel
BACKGROUND_IMAGE: rachel_5.png
BACKGROUND_EDIT: "Rachel on Route 9, exhibiting her leg as a truck approaches"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Suddenly, as the lights appear, she does a Claudette Colbert, pulling her skirt up and exhibiting a very lovely leg.
  EXPRESSION: Calculated
- CHARACTER: Narrator
  LINE: Lights--it's an Orinco truck, naturally--spotlight her. The truck stops.
  EXPRESSION: null

::PATHS::
- CHOICE: "Enter the truck"
  TARGET: rachel_and_the_truck
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Rachel and the Truck
MOOD: Transactional
CHARACTERS: Narrator, Rachel, Driver
BACKGROUND_IMAGE: rachel_and_the_truck.png
BACKGROUND_EDIT: "Truck driver leaning over to open the door for Rachel"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The driver leans over and opens the door.
  EXPRESSION: null
- CHARACTER: Driver
  LINE: Hop in, baby.
  EXPRESSION: Casual
- CHARACTER: Rachel
  LINE: Thank you.
  EXPRESSION: Grateful

::PATHS::
- CHOICE: "Get in the truck"
  TARGET: the_creed_kitchen_with_church
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: The Creed Kitchen, With Church
MOOD: Patient Malevolence
CHARACTERS: Narrator, Church
BACKGROUND_IMAGE: the_creed_kitchen_with_church.png
BACKGROUND_EDIT: "Church hiding under the kitchen table, eyes gleaming"

::SCRIPT::
- CHARACTER: Narrator
  LINE: He's under the kitchen table, green eyes gleaming. I think he loves dead, hates living.
  EXPRESSION: Sinister
- CHARACTER: Narrator
  LINE: SOUND: The doorlatch. CHURCH MIAOWS.
  EXPRESSION: null

::PATHS::
- CHOICE: "Observe Gage's entry"
  TARGET: the_kitchen_a_new_low_angle
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: The Kitchen, A New (Low) Angle
MOOD: Ominous Approach
CHARACTERS: Narrator, Church, Gage
BACKGROUND_IMAGE: the_kitchen_a_new_low_angle.png
BACKGROUND_EDIT: "Low angle view of Gage's shoes walking across the kitchen floor"

::SCRIPT::
- CHARACTER: Narrator
  LINE: GAGE'S shoes grit slowly across the linoleum, leaving dirty tracks. CHURCH turns to watch GAGE'S passage, and then follows.
  EXPRESSION: Disturbing

::PATHS::
- CHOICE: "Follow Gage to the bedroom"
  TARGET: the_bedroom_with_louis_2
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: The Bedroom, With Louis
MOOD: Lethal Awareness
CHARACTERS: Narrator, Louis, Gage
BACKGROUND_IMAGE: the_bedroom_with_louis_2.png
BACKGROUND_EDIT: "Louis sleeping, footsteps approaching, Gage entering closet"

::SCRIPT::
- CHARACTER: Narrator
  LINE: CAMERA HOLDS ON LOUIS as those gritting footsteps approach. Then we pan to the closet. On the floor is LOUIS'S little black bag. We hold on this as the footfalls near. A small white hand enters the frame and pulls the doctor-bag out of the closet. Now another hand enters the frame and opens the bag. The hands search around inside and bring out a scalpel.
  EXPRESSION: Tense
- CHARACTER: Narrator
  LINE: They hold it up. The GAGE-THING makes a contented SOUND.
  EXPRESSION: Evil

::PATHS::
- CHOICE: "Observe the truck's movement"
  TARGET: the_orinco_truck_on_route_9_night
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: The Orinco Truck, On Route 9 - Night
MOOD: Speeding Towards Destination
CHARACTERS: Narrator
BACKGROUND_IMAGE: the_orinco_truck_on_route_9_night.png
BACKGROUND_EDIT: "Orinco truck driving down Route 9 at night"

::SCRIPT::
- CHARACTER: Narrator
  LINE: It sweeps past THE CAMERA
  EXPRESSION: null

::PATHS::
- CHOICE: "Enter the truck's cab"
  TARGET: the_cab_with_rachel_and_driver
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: The Cab, With Rachel and Driver
MOOD: Urgency and Risk
CHARACTERS: Narrator, Rachel, Trucker
BACKGROUND_IMAGE: the_cab_with_rachel_and_driver.png
BACKGROUND_EDIT: "Interior of the Orinco truck cab, Rachel pleading with the driver"

::SCRIPT::
- CHARACTER: Narrator
  LINE: RACHEL
  Can't you go any faster?
  EXPRESSION: Pleading
- CHARACTER: Trucker
  LINE: Lady, I got nine points on my license right now.
  EXPRESSION: Cautious
- CHARACTER: Rachel
  LINE: I understand. It's just that--
  EXPRESSION: Desperate
- CHARACTER: Narrator
  LINE: She looks at him, pleading. The TRUCKER speeds up.
  EXPRESSION: Hopeful
- CHARACTER: Rachel
  LINE: Thank you. If you only understood how important this is--
  EXPRESSION: Grateful
- CHARACTER: Trucker
  LINE: That's all right, babe. Only if we get stopped, next time I'll be the one hitchin' and you can give me a ride.
  EXPRESSION: Winking

::PATHS::
- CHOICE: "Observe Jud's situation"
  TARGET: dud_on_his_porch
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Dud, On His Porch
MOOD: Sudden Awakening
CHARACTERS: Narrator, Jud
BACKGROUND_IMAGE: dud_on_his_porch.png
BACKGROUND_EDIT: "Jud asleep on his porch, loud music starts"

::SCRIPT::
- CHARACTER: Narrator
  LINE: More deeply asleep than ever. Suddenly, from inside, comes the sound of Quiet Riot singing/screaming "Bang Your Head." It's the stereo, and boy, is it cranked.
  EXPRESSION: Shocked
- CHARACTER: Narrator
  LINE: JUD straightens up so suddenly he almost falls off his chair. His hands go first to his earphones--his first thought on waking is that it's coming from there--and then he hurries inside.
  EXPRESSION: Startled
- CHARACTER: Narrator
  LINE: CAMERA PANS DOWN to small muddy tracks on the porch floor.
  EXPRESSION: Foreboding

::PATHS::
- CHOICE: "Investigate the noise"
  TARGET: the_living_room_with_jud
  STATE_CHANGE: confusion = +3
  CONDITION: null

::SCENE::
LOCATION: The Living Room, With Jud
MOOD: Bewildered Investigation
CHARACTERS: Narrator, Jud
BACKGROUND_IMAGE: the_living_room_with_jud.png
BACKGROUND_EDIT: "Jud in his living room, turning off the stereo"

::SCRIPT::
- CHARACTER: Narrator
  LINE: He hurries in, turns on the light, and rushes across to his stereo system, which is state-of-the-art digital--it looks like a flying saucer among the more traditional furnishings of the room. He shuts it off and looks around, frowning.
  EXPRESSION: Puzzled
- CHARACTER: Narrator
  LINE: SOUND: Todd Rundgren, singing "Bang on the Drum All Day" at the top of his voice.
  EXPRESSION: Loud
- CHARACTER: Narrator
  LINE: JUD'S head
  EXPRESSION: Confused

::SCENE::
LOCATION: Interior of a Sony Radio, Extreme Close-Up
MOOD: Tense
CHARACTERS: Jud
BACKGROUND_IMAGE: sony_radio_cu.png
BACKGROUND_EDIT: "Extreme close-up on a Sony radio dial."

::SCRIPT::
- CHARACTER: Narrator
  LINE: snaps toward the SOUND.
  EXPRESSION: null

::SCENE::
LOCATION: Kitchen
MOOD: Tense
CHARACTERS: Jud
BACKGROUND_IMAGE: kitchen_jud.png
BACKGROUND_EDIT: "Jud hurries across the kitchen to the counter where the radio is. He turns it off."

::SCRIPT::
- CHARACTER: Narrator
  LINE: THE CAMERA PULLS BACK as JUD hurries across the kitchen to the counter, where the radio is. He turns it off, looking around, more bewildered than ever.
  EXPRESSION: null
- CHARACTER: Jud
  LINE: Who's here?
  EXPRESSION: Sharp

::SCENE::
LOCATION: Hallway
MOOD: Tense
CHARACTERS: Jud
BACKGROUND_IMAGE: hallway_jud.png
BACKGROUND_EDIT: "Dimly lit hallway, light spilling from adjacent rooms."

::SCRIPT::
- CHARACTER: Narrator
  LINE: It's dimly lit by light-spill from the living room and kitchen.
  EXPRESSION: null
- CHARACTER: Jud
  LINE: Come on, stop playing games!
  EXPRESSION: null

::SCRIPT::
- CHARACTER: Narrator
  LINE: SOUND: Molly Hatchet, "Flirtin' with Disaster," being played top end, from upstairs.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: DUD hurries up. Let me suggest that there is a certain psychology at work here--for the moment he's more concerned about waking the neighborhood with all this high-decible rock and roll than with the prowler...and he would certainly know who--or what--that prowler was, if he had time to think.
  EXPRESSION: null

::SCENE::
LOCATION: Dud's Bedroom
MOOD: Tense
CHARACTERS: Dud
BACKGROUND_IMAGE: duds_bedroom.png
BACKGROUND_EDIT: "Dud enters his bedroom and turns on the light. A portable phonograph with a record is visible."

::SCRIPT::
- CHARACTER: Narrator
  LINE: He enters and turns on the light. We see a portable phonograph with the record, turning.
  EXPRESSION: null
- CHARACTER: Dud
  LINE: DUD rushes over and turns it off. He looks around, and we see by his face that he knows.
  EXPRESSION: null
- CHARACTER: Dud
  LINE: Gage? Are you the one playing games?
  EXPRESSION: null

::SCENE::
LOCATION: The Creed House, with the Station Wagon, Dud's POV
MOOD: Tense
CHARACTERS: Dud
BACKGROUND_IMAGE: creed_house_wagon_duds_pov.png
BACKGROUND_EDIT: "View from Dud's window, looking out at the station wagon in front of the Creed house."

::SCENE::
LOCATION: Dud's Bedroom
MOOD: Tense
CHARACTERS: Dud
BACKGROUND_IMAGE: duds_bedroom_bed.png
BACKGROUND_EDIT: "Dud turns slowly and walks toward the bed."

::SCRIPT::
- CHARACTER: Narrator
  LINE: He turns slowly and walks toward the bed.
  EXPRESSION: null
- CHARACTER: Dud
  LINE: Gage? Come on out.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: He reaches in his pocket and brings out a pocket-knife. He unfolds the blade.
  EXPRESSION: null
- CHARACTER: Dud
  LINE: I want to show you something.
  EXPRESSION: null

::SCRIPT::
- CHARACTER: Narrator
  LINE: SOUND: Miaow!
  EXPRESSION: null

::SCENE::
LOCATION: Doorway, with Church, Dud's POV
MOOD: Tense
CHARACTERS: Dud, Church
BACKGROUND_IMAGE: doorway_church_duds_pov.png
BACKGROUND_EDIT: "Dud's point of view, looking at Church in the doorway."

::SCENE::
LOCATION: Dud, by the Bed
MOOD: Tense
CHARACTERS: Dud, Church
BACKGROUND_IMAGE: dud_by_bed.png
BACKGROUND_EDIT: "Dud addresses the cat."

::SCRIPT::
- CHARACTER: Dud
  LINE: How did you--?!
  EXPRESSION: null

::SCENE::
LOCATION: Dud's Feet
MOOD: Violent
CHARACTERS: Dud, Gage
BACKGROUND_IMAGE: duds_feet.png
BACKGROUND_EDIT: "A small hand holding a scalpel shoots out from beneath the coverlet and slashes Dud's calf."

::SCRIPT::
- CHARACTER: Narrator
  LINE: A small hand holding a scalpel shoots out from beneath the skirt of the coverlet and slashes DUD'S calf,
  EXPRESSION: null

::SCENE::
LOCATION: Dud
MOOD: Painful
CHARACTERS: Dud
BACKGROUND_IMAGE: dud_screaming.png
BACKGROUND_EDIT: "Dud screams with pain and staggers backward."

::SCRIPT::
- CHARACTER: Dud
  LINE: He screams with pain and staggers backward.
  EXPRESSION: null

::SCENE::
LOCATION: Dud's Feet
MOOD: Violent
CHARACTERS: Dud, Gage
BACKGROUND_IMAGE: duds_feet_grab.png
BACKGROUND_EDIT: "The other hand shoots out. Gage grabs one of Dud's ankles and pulls."

::SCRIPT::
- CHARACTER: Narrator
  LINE: The other hand shoots out. GAGE grabs one of DUD'S ankles and pulls.
  EXPRESSION: null

::SCENE::
LOCATION: Dud
MOOD: Shocked
CHARACTERS: Dud
BACKGROUND_IMAGE: dud_falling.png
BACKGROUND_EDIT: "With a startled yell, Dud falls."

::SCRIPT::
- CHARACTER: Narrator
  LINE: With a startled yell, he falls.
  EXPRESSION: null

::SCENE::
LOCATION: Dud and Gage
MOOD: Violent, Horrific
CHARACTERS: Dud, Gage
BACKGROUND_IMAGE: dud_and_gage_struggle.png
BACKGROUND_EDIT: "A violent struggle ensues. Dud is repeatedly slashed with the scalpel."

::SCRIPT::
- CHARACTER: Narrator
  LINE: This one's gotta be pretty rough. George will know what to do. We finally see GAGE, but it should be clear to us that it's not really GAGE at all. Some daemonic presence is riding inside the mouldering, disfigured shell of GAGE.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: There is a struggle. DUD is repeatedly slashed with the scalpel.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Perhaps he gets GAGE a time or two with the pocketknife.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: GAGE screams and gibbers--nothing intelligible here; only sounds.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: DUD expires.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: GAGE sits on top of him...and then bites into his throat.
  EXPRESSION: null

::SCENE::
LOCATION: Route 9, Between the Crandall and Creed Houses
MOOD: Ominous
CHARACTERS: Rachel, Trucker, Pascow
BACKGROUND_IMAGE: route9_truck.png
BACKGROUND_EDIT: "Rachel's truck arrives on Route 9 and pulls up. Headlights illuminate the scene."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Headlights. RACHEL'S truck has arrived. It pulls up.
  EXPRESSION: null

::SCENE::
LOCATION: Angle on the Cab
MOOD: Ominous
CHARACTERS: Rachel, Pascow, Trucker
BACKGROUND_IMAGE: cab_angle.png
BACKGROUND_EDIT: "Pascow is seen sitting in the passenger seat where Rachel was."

::SCRIPT::
- CHARACTER: Narrator
  LINE: We can see PASCOW sitting in the passenger seat where RACHEL just was.
  EXPRESSION: null
- CHARACTER: Rachel
  LINE: Thank you so much.
  EXPRESSION: Grateful
- CHARACTER: Trucker
  LINE: I didn't get a ticket, so you're welcome, lady. Whatever your problems are, I hope they work out.
  EXPRESSION: Friendly
- CHARACTER: Pascow
  LINE: It's the end of the line for me, too--I'm not allowed any further.
  EXPRESSION: Resigned
- CHARACTER: Rachel
  LINE: I'm sure things will be fine.
  EXPRESSION: Hopeful
- CHARACTER: Pascow
  LINE: I'm not.
  EXPRESSION: Pessimistic

::SCENE::
LOCATION: Route 9
MOOD: Ominous
CHARACTERS: Rachel, Gage
BACKGROUND_IMAGE: route9_rachel.png
BACKGROUND_EDIT: "The truck pulls away. Rachel starts to cross the road and is startled by a soft voice."

::SCRIPT::
- CHARACTER: Narrator
  LINE: She closes the door and steps down. The truck starts off with a HISS OF RELEASED AIRBRAKES. As it pulls past her, RACHEL starts across the road, when:
  EXPRESSION: null
- CHARACTER: Gage
  LINE: Mummy!
  EXPRESSION: Soft, Childlike
- CHARACTER: Narrator
  LINE: She stops, startled. Her face wears a "did I hear that?" expression. She looks back toward DUD'S house.
  EXPRESSION: null
- CHARACTER: Gage
  LINE: Mummy!
  EXPRESSION: Soft, Childlike

::SCENE::
LOCATION: Dud's Paved Walk
MOOD: Hesitant
CHARACTERS: Rachel, Gage
BACKGROUND_IMAGE: dud_walk_rachel.png
BACKGROUND_EDIT: "Rachel walks halfway up Dud's paved walk and looks towards the house."

::SCRIPT::
- CHARACTER: Narrator
  LINE: RACHEL walks halfway up DUD'S paved walk and looks at:
  EXPRESSION: null

::SCENE::
LOCATION: Dud's House, Rachel's POV
MOOD: Ominous
CHARACTERS: Rachel
BACKGROUND_IMAGE: dud_house_rachel_pov.png
BACKGROUND_EDIT: "Rachel's point of view, looking at Dud's house. The narrator describes it as 'the one place in the whole world we do not want RACHEL to go.'"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The one place in the whole world we do not want RACHEL to go.
  EXPRESSION: null

::SCENE::
LOCATION: Rachel
MOOD: Hesitant, Drawn
CHARACTERS: Rachel, Gage
BACKGROUND_IMAGE: rachel_porch.png
BACKGROUND_EDIT: "Rachel, carrying two bags, walks towards the porch of Dud's house."

::SCRIPT::
- CHARACTER: Narrator
  LINE: She goes. Up the steps to the porch. All through this she's been travelling with two bags: her handbag and a light tote with her initials on it. Now she sets the tote down on the top step and opens the porch door.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: She looks very uncertain. This is the wee hours of the morning, and someone else's house. But...that voice...
  EXPRESSION: null
- CHARACTER: Gage
  LINE: Mummy, I need you!
  EXPRESSION: Pleading
- CHARACTER: Narrator
  LINE: RACHEL looks stunned-- rocked. She steps onto the porch.
  EXPRESSION: null
- CHARACTER: Rachel
  LINE: Who--
  EXPRESSION: Uncertain
- CHARACTER: Narrator
  LINE: The door to the house swings open. After a moment CHURCH comes into the doorway and sits down.
  EXPRESSION: null
- CHARACTER: Church
  LINE: Miaow!
  EXPRESSION: null
- CHARACTER: Rachel
  LINE: Church!
  EXPRESSION: Surprised
- CHARACTER: Gage
  LINE: Mummy, I need you!
  EXPRESSION: Pleading
- CHARACTER: Narrator
  LINE: She crosses to the open door.
  EXPRESSION: null
- CHARACTER: Rachel
  LINE: Gage? Gage?
  EXPRESSION: Concerned
- CHARACTER: Narrator
  LINE: No answer. RACHEL steps in.
  EXPRESSION: null

::SCENE::
LOCATION: The Creed House
MOOD: Morning, Ominous
CHARACTERS: Narrator
BACKGROUND_IMAGE: creed_house_morning.png
BACKGROUND_EDIT: "Exterior shot of the Creed house in the morning light."

::SCRIPT::
- CHARACTER: Narrator
  LINE: EXT. THE CREED HOUSE MORNING
  EXPRESSION: null

::SCENE::
LOCATION: Louis' Bedroom
MOOD: Troubled
CHARACTERS: Louis
BACKGROUND_IMAGE: louis_bedroom_dream.png
BACKGROUND_EDIT: "Louis is restless in bed, having a bad dream."

::SCRIPT::
- CHARACTER: Narrator
  LINE: INT. THE CREED BEDROOM, WITH LOUIS
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: He's restless, having a very bad dream, from the look. He rolls back and forth. Closer and closer to the edge. Finally, with a wild yell, he goes over onto the floor.
  EXPRESSION: null

::SCENE::
LOCATION: Louis, on the Floor
MOOD: Pained, Confused
CHARACTERS: Louis
BACKGROUND_IMAGE: louis_floor_ouch.png
BACKGROUND_EDIT: "Louis comes awake on the floor, experiencing pain."

::SCRIPT::
- CHARACTER: Narrator
  LINE: INT. LOUIS, ON THE FLOOR
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: He comes awake, sits up. Ouch! He's aches from top to bottom and side to side...but his back is worst. His hands go to it.
  EXPRESSION: null
- CHARACTER: Louis
  LINE: Jesus!
  EXPRESSION: Pained
- CHARACTER: Narrator
  LINE: He starts to get up very slowly, and this his eyes fix on:
  EXPRESSION: null

::SCENE::
LOCATION: Gage's Tracks on the Bedroom Floor, Louis's POV
MOOD: Perplexed
CHARACTERS: Louis
BACKGROUND_IMAGE: gage_tracks_bed.png
BACKGROUND_EDIT: "Louis's point of view, seeing Gage's tracks on the bedroom floor."

::SCRIPT::
- CHARACTER: Narrator
  LINE: INT. GAGE'S TRACKS ON THE BEDROOM FLOOR, LOUIS'S POV
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: They enter the house, go to the closet, then leave again.
  EXPRESSION: null

::SCENE::
LOCATION: Louis
MOOD: Concerned, Panicked
CHARACTERS: Louis, Gage
BACKGROUND_IMAGE: louis_searching.png
BACKGROUND_EDIT: "Louis calls out for Gage and scrambles for the closet."

::SCRIPT::
- CHARACTER: Narrator
  LINE: INT. LOUIS
  EXPRESSION: null
- CHARACTER: Louis
  LINE: Gage--?
  EXPRESSION: Concerned
- CHARACTER: Narrator
  LINE: He scrambles for the closet, his aches and pains forgotten. He stares in wildly.
  EXPRESSION: null

::SCENE::
LOCATION: The Doctor-Bag
MOOD: Anxious
CHARACTERS: Louis
BACKGROUND_IMAGE: doctor_bag_open.png
BACKGROUND_EDIT: "The doctor-bag is open."

::SCRIPT::
- CHARACTER: Narrator
  LINE: INT. THE DOCTOR-BAG
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: It’s open.
  EXPRESSION: null

::SCENE::
LOCATION: Louis
MOOD: Fearful
CHARACTERS: Louis
BACKGROUND_IMAGE: louis_bag_fear.png
BACKGROUND_EDIT: "Louis pulls out the doctor-bag, his hope fading into fear. He finds an empty case."

::SCRIPT::
- CHARACTER: Narrator
  LINE: INT. LOUIS
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: He pulls the doctor-bag out. His original hope is now tempered with the first signs of fear. He begins to go through the doctor-bag. Suddenly he brings out a case and opens it. The case is empty, but the indented shape is clear. There was a scalpel in this case...but not anymore.
  EXPRESSION: null
- CHARACTER: Louis
  LINE: Oh my God. Gage!
  EXPRESSION: Terrified

::SCENE::
LOCATION: The Hall, with Louis
MOOD: Frantic
CHARACTERS: Louis, Gage
BACKGROUND_IMAGE: louis_hall_frantic.png
BACKGROUND_EDIT: "Louis rushes down the hallway, calling for Gage."

::SCRIPT::
- CHARACTER: Narrator
  LINE: INT. THE HALL, WITH LOUIS
  EXPRESSION: null
- CHARACTER: Louis
  LINE: Gage!
  EXPRESSION: Frantic
- CHARACTER: Narrator
  LINE: LOUIS stands there, tensely listening, for a moment or two, but there's only silence. He rushes down the hallway and opens the door to GAGE'S room.
  EXPRESSION: null

::SCENE::
LOCATION: Gage's Room, Louis's POV
MOOD: Empty, Eerie
CHARACTERS: Louis
BACKGROUND_IMAGE: gages_room_empty.png
BACKGROUND_EDIT: "Louis's point of view, looking into Gage's empty room."

::SCRIPT::
- CHARACTER: Narrator
  LINE: INT. GAGE'S ROOM, LOUIS'S POV
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Empty.
  EXPRESSION: null

::SCENE::
LOCATION: Louis, on the Stairs
MOOD: Desperate
CHARACTERS: Louis
BACKGROUND_IMAGE: louis_stairs_down.png
BACKGROUND_EDIT: "Louis goes downstairs, still yelling Gage's name."

::SCRIPT::
- CHARACTER: Narrator
  LINE: INT. LOUIS, ON THE STAIRS
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: He goes downstairs, yelling GAGE'S name.
  EXPRESSION: null

::SCENE::
LOCATION: The Kitchen, with Louis
MOOD: Anxious, Startled
CHARACTERS: Louis, Irwin
BACKGROUND_IMAGE: louis_kitchen_phone.png
BACKGROUND_EDIT: "Louis is in the kitchen. The phone rings, startling him. He answers it."

::SCRIPT::
- CHARACTER: Narrator
  LINE: INT. THE KITCHEN, WITH LOUIS
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Nothing. The phone RINGS. LOUIS almost jumps out of his skin reaching for it.
  EXPRESSION: null
- CHARACTER: Louis
  LINE: Hello!
  EXPRESSION: Anxious

::SCRIPT::
- CHARACTER: Irwin
  LINE: Hello, Louis--it's Irwin. I just wanted to be sure Rachel got back all right.
  EXPRESSION: Concerned

::SCENE::
LOCATION: The Floor, with Two Sets of Gage-Tracks, Louis's POV
MOOD: Revealing
CHARACTERS: Louis
BACKGROUND_IMAGE: gage_tracks_kitchen_louis_pov.png
BACKGROUND_EDIT: "Louis's point of view, seeing two sets of Gage's tracks on the kitchen floor."

::SCRIPT::
- CHARACTER: Narrator
  LINE: AS IRWIN says this, LOUIS'S eyes fix upon something.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: INT. THE FLOOR, WITH TWO SETS OF GAGE-TRACKS, LOUIS'S POV
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: One set comes in from the shed-garage and heads for the parlor and upstairs. The other comes out of the parlor and crosses to the kitchen door giving directly on the outside.
  EXPRESSION: null

::SCENE::
LOCATION: The Kitchen, with Louis
MOOD: Realization, Horror
CHARACTERS: Louis, Irwin, Gage
BACKGROUND_IMAGE: louis_kitchen_realization.png
BACKGROUND_EDIT: "Louis looks at the tracks, a dawning realization of horror in his eyes."

::SCRIPT::
- CHARACTER: Narrator
  LINE: INT. THE KITCHEN, WITH LOUIS
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: In his eyes we suddenly see that he understands everything...or almost everything.
  EXPRESSION: null
- CHARACTER: Irwin
  LINE: Louis...are you there?
  EXPRESSION: Impatient
- CHARACTER: Louis
  LINE: Yes--I'm here.
  EXPRESSION: Slow, Dazed
- CHARACTER: Irwin
  LINE: Did she get there all right?
  EXPRESSION: Concerned
- CHARACTER: Louis
  LINE: Yes, she's fine.
  EXPRESSION: False Assurance
- CHARACTER: Irwin
  LINE: Well, put her on at that end and I'll put Ellie on at this one. Ellie's very worried about her mother. She’s almost in hysterics.
  EXPRESSION: Anxious
- CHARACTER: Louis
  LINE: She...Rachel's asleep.
  EXPRESSION: Evasive
- CHARACTER: Irwin
  LINE: Then I suggest you wake her up. Ellie...I think she had a dream that her mother was dead.
  EXPRESSION: Urgent
- CHARACTER: Louis
  LINE: I'll call you right back.
  EXPRESSION: Distracted
- CHARACTER: Irwin
  LINE: Louis--!
  EXPRESSION: Desperate
- CHARACTER: Narrator
  LINE: But LOUIS, whose last few responses have been almost trancelike, hangs up. He looks at the tracks, then goes into the parlor.
  EXPRESSION: null

::SCENE::
LOCATION: The Crandall Living Room, with the Phone
MOOD: Eerie, Sinister
CHARACTERS: Gage
BACKGROUND_IMAGE: crandall_living_room_phone.png
BACKGROUND_EDIT: "Tiny bloody hands lift the living room phone and dial."

::SCRIPT::
- CHARACTER: Narrator
  LINE: INT. THE CRANDALL LIVING ROOM, WITH THE PHONE
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Tiny bloody hands lift it off the cradle. A tiny bloody finger diddl.
  EXPRESSION: null

::SCENE::
LOCATION: The Creed Kitchen
MOOD: Tense, Fateful
CHARACTERS: Louis, Gage
BACKGROUND_IMAGE: creed_kitchen_phone_ring.png
BACKGROUND_EDIT: "The phone in the Creed kitchen starts to ring. Louis, upset, answers it."

::SCRIPT::
- CHARACTER: INT. THE CREED KITCHEN
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The phone starts to ring. After two or three ringy-dingys, LOUIS, looking extremely upset, comes out of the parlor and picks it up.
  EXPRESSION: null
- CHARACTER: Louis
  LINE: Irwin, you'll just have to--
  EXPRESSION: Agitated

::SCRIPT::
- CHARACTER: Gage
  LINE: I’m at Dud's, daddy. Will you come over and play with me?
  EXPRESSION: Creepy, Childlike

::SCRIPT::
- CHARACTER: Narrator
  LINE: LOUIS is dumbfounded...slack-mouthed with terror.
  EXPRESSION: null
- CHARACTER: Louis
  LINE: Gage?
  EXPRESSION: Whispered Terror
- CHARACTER: Gage
  LINE: Mommy already came. We played, daddy. First I played with Dud and then mommy came and I played with mommy. We had an awful good time. Nov; I want to play with you.
  EXPRESSION: Giggling, Disturbing
- CHARACTER: Narrator
  LINE: GAGE begins to giggle...a really awful sound.
  EXPRESSION: null
- CHARACTER: Louis
  LINE: What did you do? What did you--
  EXPRESSION: Horrified
- CHARACTER: Narrator
  LINE: CLICK! The GAGE-THING hangs up, still giggling.
  EXPRESSION: null

::SCENE::
LOCATION: The Creed Bed, Close-Up
MOOD: Desperate, Grim
CHARACTERS: Louis
BACKGROUND_IMAGE: creed_bed_cu_morphine.png
BACKGROUND_EDIT: "Close-up on the Creed bed as Louis places the doctor-bag down and searches through it for syringes and morphine."

::SCRIPT::
- CHARACTER: Narrator
  LINE: INT. THE CREED BED, CU
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: He puts the doctor-bag down on the bed and roots through it. He comes up with three syringes, still wrapped in paper, and puts them aside. Then he roots around some more and comes up with several ampoules. He holds one up for inspection and we can read the word MORPHINE on it very clearly.
  EXPRESSION: null

::SCENE::
LOCATION: The Bedroom, with Louis
MOOD: Grim, Descending into Madness
CHARACTERS: Louis
BACKGROUND_IMAGE: bedroom_louis_morphine.png
BACKGROUND_EDIT: "Louis carries syringes and ampoules of morphine to the window. His hair has partially turned white."

::SCRIPT::
- CHARACTER: Narrator
  LINE: INT. THE BEDROOM, WITH LOUIS
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: He carries the syringes and ampoules of morphine over to the window. His hair has gone partially white.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: He fills all three syringes with morphine (using two ampoules for each syringe--i.e., enough to kill a polar bear) and puts them in the left breast pocket of his shirt. He puts the spare ampoules in the right breast pocket of his shirt.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: LOUIS is slowly going insane. What remains of his rationality is like a rapidly fraying rope.
  EXPRESSION: null
- CHARACTER: Louis
  LINE: What you buy is what you own, and sooner or later what you own comes home to you. Wasn't that what you said, Dud? Wasn’t that pretty much it?
  EXPRESSION: Distraught, Rambling

::SCENE::
LOCATION: The Front Door
MOOD: Finality
CHARACTERS: Louis
BACKGROUND_IMAGE: front_door_exit.png
BACKGROUND_EDIT: "Louis leaves the bedroom."

::SCRIPT::
- CHARACTER: Narrator
  LINE: He leaves the room.
  EXPRESSION: null

::SCENE::
LOCATION: The Creed House Exterior
MOOD: Ominous
CHARACTERS: Louis, Church, Narrator
BACKGROUND_IMAGE: creed_house_exterior.png
BACKGROUND_EDIT: "Daytime, Louis emerges from the house with a raw pork chop and rubber gloves."

::SCRIPT::
- CHARACTER: Narrator
  LINE: LOUIS comes out the door. In one hand he's got a raw pork chop. In the other he is carrying a pair of Playtex rubber gloves. He walks to the soft shoulder and waits for an Orinco truck to pass. Then he crosses.
  EXPRESSION: null

::PATHS::
- CHOICE: "Cross the street"
  TARGET: crandall_walk_louis
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: The Crandall Walk, with Louis
MOOD: Tense
CHARACTERS: Louis, Narrator
BACKGROUND_IMAGE: crandall_walk_louis.png
BACKGROUND_EDIT: "Daytime, Louis walks towards the house, then stops."

::SCRIPT::
- CHARACTER: Narrator
  LINE: He walks most of the way to the house, then stops.
  EXPRESSION: null

::PATHS::
- CHOICE: "Approach the church"
  TARGET: church_louis_pov
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Church, Louis's POV
MOOD: Wary
CHARACTERS: Louis, Church, Narrator
BACKGROUND_IMAGE: church_louis_pov.png
BACKGROUND_EDIT: "Daytime, Louis cautiously gets up."

::SCRIPT::
- CHARACTER: Narrator
  LINE: He gets up, humping his back warily.
  EXPRESSION: null

::PATHS::
- CHOICE: "Offer food"
  TARGET: louis_church
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Louis
MOOD: Reassuring
CHARACTERS: Louis, Church
BACKGROUND_IMAGE: louis_church.png
BACKGROUND_EDIT: "Daytime, Louis holds a pork chop, addressing the cat."

::SCRIPT::
- CHARACTER: Louis
  LINE: Hi, Church. Want some grub?
  EXPRESSION: Friendly
- CHARACTER: Narrator
  LINE: He tosses the pork chop onto the grass.
  EXPRESSION: null

::PATHS::
- CHOICE: "Watch the cat eat"
  TARGET: church
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Church
MOOD: Focused
CHARACTERS: Church, Narrator
BACKGROUND_IMAGE: church.png
BACKGROUND_EDIT: "Daytime, the cat hurries down steps, sniffs the chop, and begins eating."

::SCRIPT::
- CHARACTER: Narrator
  LINE: He hurries down the steps, goes to the chop, sniffs it, and starts to chow up. He looks up at:
  EXPRESSION: null

::PATHS::
- CHOICE: "Observe Louis"
  TARGET: louis_church_gloves
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Louis
MOOD: Deliberate
CHARACTERS: Louis, Narrator
BACKGROUND_IMAGE: louis_church_gloves.png
BACKGROUND_EDIT: "Daytime, Louis is pulling on rubber gloves."

::SCRIPT::
- CHARACTER: Narrator
  LINE: He is pulling on the rubber gloves.
  EXPRESSION: null
- CHARACTER: Louis
  LINE: Don't mind me. Eat it while you can. Eat all you want.
  EXPRESSION: Soothing

::PATHS::
- CHOICE: "Continue watching the cat"
  TARGET: church_chop
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Church
MOOD: Engaged
CHARACTERS: Church, Narrator
BACKGROUND_IMAGE: church_chop.png
BACKGROUND_EDIT: "Daytime, the cat continues to eat the chop, making smacking sounds."

::SCRIPT::
- CHARACTER: Narrator
  LINE: He starts worrying the chop again. Smack-smack-smack.
  EXPRESSION: null

::PATHS::
- CHOICE: "Listen to Louis's monologue"
  TARGET: angle_louis_church
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Angle on Louis and Church
MOOD: Unsettling
CHARACTERS: Louis, Church, Narrator
BACKGROUND_IMAGE: angle_louis_church.png
BACKGROUND_EDIT: "Daytime, Louis speaks to the cat while preparing a syringe."

::SCRIPT::
- CHARACTER: Louis
  LINE: Eat all you can...all you want... that's right...today’s Thanksgiving day for cats, but only if they came back from the dead...
  EXPRESSION: Monotone
- CHARACTER: Narrator
  LINE: He finishes with the gloves, gets one of the loaded syringes out of his breast pocket, holds it up, squirts a drop out of the tip, then moves toward CHURCH. CHURCH looks up. LOUIS stops moving. CHURCH starts eating again, and LOUIS starts moving again as soon as he does. All the time he talks to the cat in that soothing voice. He bends down...and grabs him. CHURCH begins to squall and fight. LOUIS holds onto him. He tries to get the syringe into the cat and CHURCH almost gets away.
  EXPRESSION: null
- CHARACTER: Louis
  LINE: No, you don’t!
  EXPRESSION: Firm

::PATHS::
- CHOICE: "Administer the injection"
  TARGET: church_cu
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Church, CU
MOOD: Painful
CHARACTERS: Church, Narrator
BACKGROUND_IMAGE: church_cu.png
BACKGROUND_EDIT: "Daytime, close-up of the syringe plunging into Church's haunch."

::SCRIPT::
- CHARACTER: Narrator
  LINE: The syringe plunges into his haunch.
  EXPRESSION: null

::PATHS::
- CHOICE: "Observe the aftermath"
  TARGET: church_louis
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Church and Louis
MOOD: Dazed
CHARACTERS: Church, Louis, Narrator
BACKGROUND_IMAGE: church_louis.png
BACKGROUND_EDIT: "Daytime, the needle dangles from Church's haunch. The cat looks dazed and falls over."

::SCRIPT::
- CHARACTER: Narrator
  LINE: The needle is still dangling out of CHURCH'S haunch. The cat looks dazed. It tries to walk and falls over on its side. It tries to get up...and then falls over again.
  EXPRESSION: null
- CHARACTER: Louis
  LINE: Go on. Lie down. Play dead. Be dead.
  EXPRESSION: Cold

::PATHS::
- CHOICE: "Retrieve the tote-bag"
  TARGET: tote_bag_louis_pov
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: The Tote-Bag, Louis's POV
MOOD: Foreboding
CHARACTERS: Narrator
BACKGROUND_IMAGE: tote_bag_louis_pov.png
BACKGROUND_EDIT: "Daytime, close-up of a tote bag with the initials R.C."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Any doubt he might have allowed himself the luxury of having is erased by the initials--R.C. , same as the cola.
  EXPRESSION: null

::PATHS::
- CHOICE: "Return to Louis"
  TARGET: louis_sanity
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Louis
MOOD: Breaking
CHARACTERS: Louis, Narrator
BACKGROUND_IMAGE: louis_sanity.png
BACKGROUND_EDIT: "Daytime, Louis experiences a breakdown, a strand of sanity snapping."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Twang! One of the few remaining strands of sanity has now parted.
  EXPRESSION: null

::PATHS::
- CHOICE: "Look back at the church"
  TARGET: church_on_path_louis_pov
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Church, on the Path, Louis's POV
MOOD: Deathly
CHARACTERS: Narrator
BACKGROUND_IMAGE: church_on_path_louis_pov.png
BACKGROUND_EDIT: "Daytime, view of the church, which appears dead."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Dead.
  EXPRESSION: null

::PATHS::
- CHOICE: "Go to the house"
  TARGET: louis_steps
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Louis
MOOD: Determined
CHARACTERS: Louis, Narrator
BACKGROUND_IMAGE: louis_steps.png
BACKGROUND_EDIT: "Daytime, Louis climbs the porch steps."

::SCRIPT::
- CHARACTER: Narrator
  LINE: He climbs the steps and goes onto the porch.
  EXPRESSION: null

::PATHS::
- CHOICE: "Enter the house"
  TARGET: louis_porch
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Louis, on the Porch
MOOD: Resolute
CHARACTERS: Louis, Narrator
BACKGROUND_IMAGE: louis_porch.png
BACKGROUND_EDIT: "Daytime, Louis on the porch, preparing to enter."

::SCRIPT::
- CHARACTER: Narrator
  LINE: He strips off the rubber gloves. He tosses them onto the table beside JUD'S beer-cans as he goes inside.
  EXPRESSION: null

::PATHS::
- CHOICE: "Enter the foyer"
  TARGET: foyer_crandall_home_louis
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: The Foyer of the Crandall Home, with Louis
MOOD: Spooky
CHARACTERS: Louis, Narrator
BACKGROUND_IMAGE: foyer_crandall_home_louis.png
BACKGROUND_EDIT: "Dimly lit foyer of the Crandall home."

::SCRIPT::
- CHARACTER: Narrator
  LINE: It’s dark in here, and spooky.
  EXPRESSION: null
- CHARACTER: Louis
  LINE: Rachel? (Pause) Jud? (Longer pause) Gage?
  EXPRESSION: Calling out, searching

::PATHS::
- CHOICE: "Look down"
  TARGET: shoe_louis_pov
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: A Shoe, Louis's POV
MOOD: Unsettling
CHARACTERS: Narrator
BACKGROUND_IMAGE: shoe_louis_pov.png
BACKGROUND_EDIT: "Close-up of one of Rachel's shoes lying by the stairs."

::SCRIPT::
- CHARACTER: Narrator
  LINE: One of RACHEL'S shoes. It lies by the foot of the stairs.
  EXPRESSION: null

::PATHS::
- CHOICE: "Pick up the shoe"
  TARGET: louis_shoe
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Louis
MOOD: Concerned
CHARACTERS: Louis, Narrator
BACKGROUND_IMAGE: louis_shoe.png
BACKGROUND_EDIT: "Louis picks up Rachel's scuffed shoe with a bloodstain."

::SCRIPT::
- CHARACTER: Narrator
  LINE: He goes over and picks up the shoe. It's a three-quarter heel, and it's pretty badly scuffed. RACHEL, after all, did some pretty hard travelling to get here. There's a spot of blood on it.
  EXPRESSION: null
- SOUND: A low giggle.
- CHARACTER: Louis
  LINE: null
  EXPRESSION: Looks up, startled

::PATHS::
- CHOICE: "Look up the stairs"
  TARGET: stairs_louis_pov
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: The Stairs, Louis's POV
MOOD: Dark
CHARACTERS: Narrator
BACKGROUND_IMAGE: stairs_louis_pov.png
BACKGROUND_EDIT: "Mighty dark. Mighty shadowy."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Mighty dark. Mighty shadowy.
  EXPRESSION: null
- SOUND: Another giggle.

::PATHS::
- CHOICE: "Call out to Gage"
  TARGET: louis_foot_stairs
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Louis, at the Foot of the Stairs
MOOD: Calling
CHARACTERS: Louis, Narrator
BACKGROUND_IMAGE: louis_foot_stairs.png
BACKGROUND_EDIT: "Louis at the bottom of the stairs, calling out."

::SCRIPT::
- CHARACTER: Louis
  LINE: Gage?
  EXPRESSION: Calling

::PATHS::
- CHOICE: "Respond to Gage"
  TARGET: stairs_gage_voice
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: The Stairs
MOOD: Playful
CHARACTERS: Gage (Voice), Narrator
BACKGROUND_IMAGE: stairs_gage_voice.png
BACKGROUND_EDIT: "Voice from upstairs."

::SCRIPT::
- CHARACTER: Gage (Voice)
  LINE: Let's play, daddy! Let's play hide and go seek!
  EXPRESSION: Childlike, eerie

::PATHS::
- CHOICE: "Agree to play"
  TARGET: louis_upstairs
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Louis
MOOD: Agreeing
CHARACTERS: Louis, Narrator
BACKGROUND_IMAGE: louis_upstairs.png
BACKGROUND_EDIT: "Louis draws a syringe from his pocket."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Takes one of the loaded syringes from his pocket.
  EXPRESSION: null
- CHARACTER: Louis
  LINE: All right, Gage...let's.
  EXPRESSION: Resigned

::PATHS::
- CHOICE: "Climb the stairs"
  TARGET: upstairs_louis
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Upstairs, with Louis
MOOD: Searching
CHARACTERS: Louis, Narrator
BACKGROUND_IMAGE: upstairs_louis.png
BACKGROUND_EDIT: "Upstairs landing, Louis methodically checks rooms."

::SCRIPT::
- CHARACTER: Narrator
  LINE: LOUIS arrives on the landing. We begin the nerve-wracking business of checking rooms. First, the bathroom...and the shower curtain is of course pulled. LOUIS yanks it back. Nothing. He checks the linen closet. Nothing. Goes back to the hall. Looks down it. He walks slowly along it. He checks one room. It's a guest room. Shadowy and empty. Down the hall. A closet door. A bag falls off the top shelf, and a bunch of ceramics inside it SHATTER LOUDLY. LOUIS flinches back. Down the hall. Now he’s at JUD'S room. He goes in.
  EXPRESSION: Tense

::PATHS::
- CHOICE: "Enter Jud's room"
  TARGET: juds_room_louis
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Jud's Room, with Louis
MOOD: Shocking
CHARACTERS: Louis, Narrator
BACKGROUND_IMAGE: juds_room_louis.png
BACKGROUND_EDIT: "Louis in Jud's room, checks the closet, then sees a bloodstain on the floor."

::SCRIPT::
- CHARACTER: Narrator
  LINE: He checks the closet. No go. He steps around the bed and sees:
  EXPRESSION: null

::PATHS::
- CHOICE: "Examine the bloodstain"
  TARGET: floor_juds_room_louis_pov
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: The Floor, Jud's Room, Louis's POV
MOOD: Gruesome
CHARACTERS: Narrator
BACKGROUND_IMAGE: floor_juds_room_louis_pov.png
BACKGROUND_EDIT: "Close-up of a bloodstain on the floor."

::SCRIPT::
- CHARACTER: Narrator
  LINE: A bloodstain.
  EXPRESSION: null

::PATHS::
- CHOICE: "Investigate further"
  TARGET: louis_bloodstain
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Louis
MOOD: Horrified
CHARACTERS: Louis, Narrator
BACKGROUND_IMAGE: louis_bloodstain.png
BACKGROUND_EDIT: "Louis kneels to examine the bloodstain, lifts the bedspread to reveal Jud's dead body."

::SCRIPT::
- CHARACTER: Narrator
  LINE: He gets down on his hands and knees and examines the bloodstain. He sees the skirt on the bedspread. He lifts it. He is nose to nose with JUD, who is dead with his eyes open, an expression of incredible horror on his face.
  EXPRESSION: null
- SOUND: The DOOR SLAMS.
- CHARACTER: Louis
  LINE: null
  EXPRESSION: Bolts upright in fear

::PATHS::
- CHOICE: "Listen to the giggles"
  TARGET: hallway_louis_giggles
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: The Hallway, with Louis
MOOD: Grief and Resolve
CHARACTERS: Louis, Narrator
BACKGROUND_IMAGE: hallway_louis_giggles.png
BACKGROUND_EDIT: "Louis kneels by the bed, apologizes to Jud, then rises with a new resolve."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Slowly, he kneels down and speaks to the skirt of the spread, which has mercifully fallen back into place.
  EXPRESSION: null
- CHARACTER: Louis
  LINE: I'm sorry, Jud. I'm so sorry. I'm—
  EXPRESSION: Apologetic
- SOUND: A SQUEAKING, SQUEALING SOUND.
- CHARACTER: Louis
  LINE: null
  EXPRESSION: Turns around, then back to Jud
- CHARACTER: Louis
  LINE: I'm going to set things back in order. I...I know just what to do.
  EXPRESSION: Determined

::PATHS::
- CHOICE: "Leave the room and get a syringe"
  TARGET: hallway_louis_syringe
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: The Hallway, with Louis
MOOD: Tense
CHARACTERS: Louis, Narrator
BACKGROUND_IMAGE: hallway_louis_syringe.png
BACKGROUND_EDIT: "Louis holds a loaded syringe in the hallway, calls out to Gage."

::SCRIPT::
- CHARACTER: Narrator
  LINE: He takes one of the two remaining loaded syringes from his breast pocket.
  EXPRESSION: null
- CHARACTER: Louis
  LINE: Gage?
  EXPRESSION: Calling
- SOUND: Another SQUEAKING SOUND. And another GIGGLE.
- CHARACTER: Narrator
  LINE: LOUIS starts slowly forward. He gets about halfway down the hall--and our nerves are tuned to the breaking point--when there is a SQUEALING CREAK and a GRATING THUMP from overhead.
  EXPRESSION: null

::PATHS::
- CHOICE: "Look up at the ceiling trapdoor"
  TARGET: ceiling_trapdoor
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Ceiling Trapdoor
MOOD: Horrific
CHARACTERS: Rachel's Body, Narrator
BACKGROUND_IMAGE: ceiling_trapdoor.png
BACKGROUND_EDIT: "A trapdoor opens, and Rachel's body plummets down, bound and half-eaten."

::SCRIPT::
- CHARACTER: Narrator
  LINE: This happens fast. The trap--which presumably gives on the attic with a set of folding stairs--rises, and RACHEL'S body plunges down through and then hangs, swinging: she has been bound around the armpits and as become a grotesque parody of MISSY DANDRIDGE. Half her face is gone. Eaten.
  EXPRESSION: null

::PATHS::
- CHOICE: "React to the sight"
  TARGET: louis_scream
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Louis
MOOD: Terrified
CHARACTERS: Louis, Narrator
BACKGROUND_IMAGE: louis_scream.png
BACKGROUND_EDIT: "Louis screams and backs against the wall, his sanity fracturing completely."

::SCRIPT::
- CHARACTER: Narrator
  LINE: He SCREAMS and backs against the wall. Twang! The last silver
  EXPRESSION: Terror

::PATHS::
- CHOICE: "Observe Gage's descent"
  TARGET: trapdoor_gage
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: The Trapdoor, with Gage
MOOD: Frenzied
CHARACTERS: Gage, Narrator
BACKGROUND_IMAGE: trapdoor_gage.png
BACKGROUND_EDIT: "Gage leaps down from the trapdoor, waving a scalpel."

::SCRIPT::
- CHARACTER: Narrator
  LINE: He leaps down, crashes on the floor, and then picks himself up. He is waving the scalpel.
  EXPRESSION: null
- CHARACTER: Gage
  LINE: Allee-allee-in-free! allee-allee-in-free! Allee-allee-in-free!
  EXPRESSION: Screeching

::PATHS::
- CHOICE: "Witness the attack"
  TARGET: louis_gage_fight
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Louis and Gage
MOOD: Violent Struggle
CHARACTERS: Louis, Gage, Narrator
BACKGROUND_IMAGE: louis_gage_fight.png
BACKGROUND_EDIT: "Gage attacks Louis with a scalpel. Louis tries to inject Gage, but the syringe is knocked away. They fall. Louis retrieves another syringe and injects Gage."

::SCRIPT::
- CHARACTER: Narrator
  LINE: I won't choreograph all the moves, but GAGE slashes his stunned father up pretty badly with the scalpel. He's screeching the whole time. LOUIS finally begins to react. He grapples with the little critter, and tries to get the syringe into him. No good. It's batted out of his hand just before he can do it. It breaks. LOUIS and GAGE fall to the floor. LOUIS gets the other syringe out of his pocket, but it's also knocked out of his hand. Only consolation is this one isn't broken. It rolls off along the floor. LOUIS finally manages to get it again as the struggle goes on, and plunges it into GAGE'S neck.
  EXPRESSION: Brutal
- CHARACTER: Gage
  LINE: No fair! NO FAIR!
  EXPRESSION: Irate
- CHARACTER: Narrator
  LINE: He gets to his feet, clawing for the needle lolling out of his neck. He's lost all interest in his father. He goes staggering away. He’s slowing down. He goes to his knees...and falls on his face.
  EXPRESSION: null

::PATHS::
- CHOICE: "Watch Gage fall"
  TARGET: rachel_louis_pov
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Rachel, Louis's POV
MOOD: Haunting
CHARACTERS: Narrator
BACKGROUND_IMAGE: rachel_louis_pov.png
BACKGROUND_EDIT: "Gage falls. Louis's gaze drifts to Rachel's body, still swinging."

::SCRIPT::
- CHARACTER: Narrator
  LINE: She swings slowly back and forth.
  EXPRESSION: null

::PATHS::
- CHOICE: "Move to the backyard"
  TARGET: backyard_crandall_house
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: The Back Yard of the Crandall House
MOOD: Somber
CHARACTERS: Louis, Rachel's Body, Narrator
BACKGROUND_IMAGE: backyard_crandall_house.png
BACKGROUND_EDIT: "Late afternoon. Louis carries Rachel's sheet-wrapped body out of the house."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Time has passed. It's late afternoon. LOUIS comes out with a sheet-wrapped form in his arms. RACHEL, of course.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: He sets the body down and goes back inside.
  EXPRESSION: null

::PATHS::
- CHOICE: "Go to the kitchen"
  TARGET: kitchen_louis
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: The Kitchen, with Louis
MOOD: Destructive
CHARACTERS: Louis, Narrator
BACKGROUND_IMAGE: kitchen_louis.png
BACKGROUND_EDIT: "Louis douses the kitchen with coal oil and sets it on fire."

::SCRIPT::
- CHARACTER: Narrator
  LINE: He's splashing around a can of coal-oil. When he's got the room wetted down to his satisfaction, he goes to the door, lights a match, and tosses it. Flame runs across the floor. The fire is slow at first, but then it begins to gain rapidly.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: LOUIS goes out.
  EXPRESSION: null

::PATHS::
- CHOICE: "Go to the back lawn"
  TARGET: back_lawn_louis
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: The Back Lawn, with Louis
MOOD: Grim
CHARACTERS: Louis, Narrator
BACKGROUND_IMAGE: back_lawn_louis.png
BACKGROUND_EDIT: "Flames erupt from the kitchen windows as Louis carries Rachel's body around the side of the house."

::SCRIPT::
- CHARACTER: Narrator
  LINE: He picks up the sheet-wrapped form of his wife and walks around the side of the house as flames shoot through the kitchen windows.
  EXPRESSION: null

::PATHS::
- CHOICE: "Head to the front of the house"
  TARGET: front_crandall_house_road
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: The Front of the Crandall House, from Across the Road
MOOD: Devastated
CHARACTERS: Louis, Narrator
BACKGROUND_IMAGE: front_crandall_house_road.png
BACKGROUND_EDIT: "Louis, carrying Rachel's shrouded body, approaches the road."

::SCRIPT::
- CHARACTER: Narrator
  LINE: LOUIS appears with his shrouded burden and approaches the road.
  EXPRESSION: null

::PATHS::
- CHOICE: "Observe the ruins at night"
  TARGET: shoulder_ruins_crandall_house_night
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: The Shouldering Ruins of the Crandall House
MOOD: Desolate, Eerie
CHARACTERS: Louis, Narrator
BACKGROUND_IMAGE: shoulder_ruins_crandall_house_night.png
BACKGROUND_EDIT: "Nighttime. The ruined Crandall house. A single light is on in the Creed house kitchen."

::SCRIPT::
- CHARACTER: Narrator
  LINE: CAMERA HOLDS FOR A MOMENT, then rises and looks toward the CREED house. There's one light on--in the kitchen.
  EXPRESSION: null
- SOUND: TOLLING CONTINUES: Three...four...five...

::PATHS::
- CHOICE: "Enter the kitchen"
  TARGET: kitchen_table_louis
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: The Kitchen Table, with Louis
MOOD: Weary, Resigned
CHARACTERS: Louis, Narrator
BACKGROUND_IMAGE: kitchen_table_louis.png
BACKGROUND_EDIT: "Louis, covered in dried blood, plays solitaire at the kitchen table. The tolling continues."

::SCRIPT::
- CHARACTER: Narrator
  LINE: LOUIS is filthy, covered with dried blood. He is playing at Patience. He holds a handful of cards.
  EXPRESSION: null
- SOUND: TOLLING CONTINUES: Six...seven...
- SOUND: The back door opens.
- SOUND: Crickets from outside. Ree-ree-ree...
- SOUND: Gritting footsteps.
- CHARACTER: Louis
  LINE: And what you own always comes home to you.
  EXPRESSION: Resigned
- CHARACTER: Narrator
  LINE: He flips up one card.
  EXPRESSION: null
- SOUND: TOLLING CONTINUES: Eight...

::PATHS::
- CHOICE: "Observe the card"
  TARGET: card_bitch
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: The Card
MOOD: Foreboding
CHARACTERS: Narrator
BACKGROUND_IMAGE: card_bitch.png
BACKGROUND_EDIT: "Close-up of the Queen of Spades."

::SCRIPT::
- CHARACTER: Narrator
  LINE: It’s the Bitch, the Queen of Spades, she who supposedly poisoned the laddies in the Tower.
  EXPRESSION: null
- SOUND: TOLLING CONTINUES: Nine...ten...

::PATHS::
- CHOICE: "Observe Louis's hand"
  TARGET: louis_cu
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Louis, CU
MOOD: Confronted
CHARACTERS: Louis, Rachel (Voice), Narrator
BACKGROUND_IMAGE: louis_cu.png
BACKGROUND_EDIT: "Close-up on Louis's hand, clotted with grave-dirt, resting on his shoulder. A woman's hand is on his shoulder. Rachel's voice speaks."

::SCRIPT::
- CHARACTER: Narrator
  LINE: A hand clotted with grave-dirt falls on his shoulder. A woman's hand.
  EXPRESSION: null
- SOUND: TOLLING CONCLUDES: Eleven...twelve...
- CHARACTER: Rachel (Voice)
  LINE: Darling.
  EXPRESSION: Soft, chilling

::PATHS::
- CHOICE: "Fade out"
  TARGET: fade_out
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Fade Out
MOOD: Lingering Dread
CHARACTERS: Narrator
BACKGROUND_IMAGE: fade_out.png
BACKGROUND_EDIT: "Fade to black, the sound of crickets remains."

::SCRIPT::
- CHARACTER: Narrator
  LINE: FADE OUT ON THE SOUND OF CRICKETS.
  EXPRESSION: null

