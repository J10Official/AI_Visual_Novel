::SCENE::
LOCATION: Title Card
MOOD: Title Card
CHARACTERS: Narrator
BACKGROUND_IMAGE: title_card.png
BACKGROUND_EDIT: "Black background with white text"

::SCRIPT::
- CHARACTER: Narrator
  LINE: MISERY
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Written by
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Barry Luc
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Based on, If Any
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: "MISERY”
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: by
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: William Goldman
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Based on the Novel by
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Stephen King
  EXPRESSION: null

::SCENE::
LOCATION: Hotel Suite - Cabin
MOOD: Calm before the storm
CHARACTERS: Narrator, Paul Sheldon
BACKGROUND_IMAGE: hotel_suite_cabin.png
BACKGROUND_EDIT: "Western themed cabin, afternoon, grey sky, snow scattered on the ground"

::SCRIPT::
- CHARACTER: Narrator
  LINE: FADE IN ON: A SINGLE CIGARETTE. A MATCH. A HOTEL ICE BUCKET that holds a bottle of champagne. The cigarette is unlit. The match is of the kitchen variety. The champagne, unopened, is Dom Perignon. There is only one sound at first: a strong WIND--
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: --now another sound, sharper--a sudden burst of TYPING as we PULL BACK TO REVEAL PAUL SHELDON typing at a table in his hotel suite. It's really a cabin that's part of a lodge. Not an ornate place. Western themed.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: He is framed by a window looking out at some gorgeous mountains. It's afternoon. The sky is grey. Snow is scattered along the ground. We're out west somewhere. The WIND grows stronger--there could be a storm.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: PAUL pays no attention to what's going on outside as he continues to type.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: He's the hero of what follows. Forty-two, he's got a good face, one with a certain mileage to it. We are not, in other words, looking at a virgin. He's been a novelist for eighteen years and for half that time, the most recent half, a remarkably successful one.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: He pauses for a moment, intently, as if trying to stare a hole in the paper. Now his fingers fly, and there's another burst of TYPING. He studies what he's written, then--
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue typing"
  TARGET: paper_end
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Hotel Suite - Cabin
MOOD: Accomplishment
CHARACTERS: Narrator, Paul Sheldon
BACKGROUND_IMAGE: hotel_suite_cabin.png
BACKGROUND_EDIT: "Paul Sheldon at his desk, holding the final page of his manuscript"

::SCRIPT::
- CHARACTER: Narrator
  LINE: CUT TO: THE PAPER, as he rolls it out of the machine, puts it on the table, prints, in almost childlike letters, these words: THE END
  EXPRESSION: null

::PATHS::
- CHOICE: "Place the final page with the manuscript"
  TARGET: manuscript_pile
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Hotel Suite - Cabin
MOOD: Accomplishment
CHARACTERS: Narrator, Paul Sheldon
BACKGROUND_IMAGE: hotel_suite_cabin.png
BACKGROUND_EDIT: "Paul Sheldon placing the final page onto a pile of manuscript pages"

::SCRIPT::
- CHARACTER: Narrator
  LINE: CUT TO: A PILE OF MANUSCRIPT at the rear of the table. He puts this last page on, gets it straight and in order, hoists it up, folds it to his chest, the entire manuscript--hundreds of pages.
  EXPRESSION: null

::PATHS::
- CHOICE: "Hold the manuscript"
  TARGET: paul_holding_manuscript
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Hotel Suite - Cabin
MOOD: Contentment
CHARACTERS: Narrator, Paul Sheldon
BACKGROUND_IMAGE: hotel_suite_cabin.png
BACKGROUND_EDIT: "Paul Sheldon holding his completed manuscript to his chest"

::SCRIPT::
- CHARACTER: Narrator
  LINE: CUT TO: PAUL, as he holds his book to him. He is, just for a brief moment, moved.
  EXPRESSION: null

::PATHS::
- CHOICE: "Prepare to leave"
  TARGET: suitcase
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Hotel Suite - Cabin
MOOD: Celebration
CHARACTERS: Narrator, Paul Sheldon
BACKGROUND_IMAGE: hotel_suite_cabin.png
BACKGROUND_EDIT: "Paul Sheldon opening a champagne bottle and pouring a glass"

::SCRIPT::
- CHARACTER: Narrator
  LINE: CUT TO: A SUITCASE across the room. PAUL goes to it, opens it and pulls something out from inside: a battered red leather briefcase. Now he takes his manuscript, carefully opens the briefcase, gently puts the manuscript inside. He closes it, and the way he handles it, he might almost be handling a child. Now he crosses over, opens the champagne, pours himself a single glass, lights the one cigarette with the lone match-- there is a distinct feeling of ritual about this. He inhales deeply, makes a toasting gesture, then drinks, smokes, smiles. HOLD BRIEFLY, them--
  EXPRESSION: null

::PATHS::
- CHOICE: "Exit the cabin"
  TARGET: lodge_exterior
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Lodge Exterior
MOOD: Playful
CHARACTERS: Narrator, Paul Sheldon
BACKGROUND_IMAGE: lodge_exterior.png
BACKGROUND_EDIT: "Paul Sheldon exiting his cabin, throwing a snowball at a sign"

::SCRIPT::
- CHARACTER: Narrator
  LINE: CUT TO: INT. LODGE - DAY 1 1 PAUL--exiting his cabin. He stops, makes a snowball, throws it, hitting a sign.
  EXPRESSION: null
- CHARACTER: Paul Sheldon
  LINE: Still got it.
  EXPRESSION: Playful
- CHARACTER: Narrator
  LINE: He throws a suitcase into the trunk of his '65 MUSTANG and, holding his leather case, he hops into the car and drives away.
  EXPRESSION: null

::PATHS::
- CHOICE: "Drive away"
  TARGET: silver_creek_lodge_sign
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Silver Creek Lodge Sign
MOOD: Desolate
CHARACTERS: Narrator
BACKGROUND_IMAGE: silver_creek_lodge_sign.png
BACKGROUND_EDIT: "A sign that reads 'Silver Creek Lodge' with the old, desolate hotel behind it"

::SCRIPT::
- CHARACTER: Narrator
  LINE: CUT TO: A SIGN that reads "Silver Creek Lodge." Behind the sign is the hotel itself--old, desolate. Now the '65 Mustang comes out of the garage, guns ahead toward the sign. As "Shotgun" by Jr. Walker and the Allstars starts, he heads off into the mountains.
  EXPRESSION: null

::PATHS::
- CHOICE: "Head into the mountains"
  TARGET: sky_gunmetal_grey
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Sky
MOOD: Ominous
CHARACTERS: Narrator
BACKGROUND_IMAGE: sky_gunmetal_grey.png
BACKGROUND_EDIT: "Gun-metal grey sky, clouds pregnant with snow"

::SCRIPT::
- CHARACTER: Narrator
  LINE: CUT TO: THE SKY. Gun-metal grey. The clouds seem pregnant with snow.
  EXPRESSION: null

::PATHS::
- CHOICE: "Focus on Paul driving"
  TARGET: paul_driving_mustang
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Paul Driving Mustang
MOOD: Calm
CHARACTERS: Narrator, Paul Sheldon
BACKGROUND_IMAGE: paul_driving_mustang.png
BACKGROUND_EDIT: "Paul Sheldon driving a Mustang, briefcase on the seat beside him"

::SCRIPT::
- CHARACTER: Narrator
  LINE: CUT TO: PAUL, driving the Mustang, the battered briefcase on the seat beside him.
  EXPRESSION: null

::PATHS::
- CHOICE: "Show the road ahead"
  TARGET: road_ahead_snowflakes
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Road Ahead
MOOD: Approaching Storm
CHARACTERS: Narrator
BACKGROUND_IMAGE: road_ahead_snowflakes.png
BACKGROUND_EDIT: "Little dainty flakes of snow suddenly visible on the road ahead"

::SCRIPT::
- CHARACTER: Narrator
  LINE: CUT TO: THE ROAD AHEAD. Little dainty flakes of snow are suddenly visible.
  EXPRESSION: null

::PATHS::
- CHOICE: "Focus on the car"
  TARGET: car_curve
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Car on Curve
MOOD: Building Tension
CHARACTERS: Narrator
BACKGROUND_IMAGE: car_curve.png
BACKGROUND_EDIT: "A car going into a curve"

::SCRIPT::
- CHARACTER: Narrator
  LINE: CUT TO: THE CAR, going into a curve and
  EXPRESSION: null

::PATHS::
- CHOICE: "Show Paul's reaction"
  TARGET: paul_stunned
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Paul's Reaction
MOOD: Shock
CHARACTERS: Narrator, Paul Sheldon
BACKGROUND_IMAGE: paul_stunned.png
BACKGROUND_EDIT: "Paul Sheldon driving, a stunned look hitting his face"

::SCRIPT::
- CHARACTER: Narrator
  LINE: CUT TO: PAUL, driving, and as he comes out of the curve, a stunned look hits his face as we
  EXPRESSION: null

::PATHS::
- CHOICE: "Reveal the storm"
  TARGET: road_ahead_blizzard
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Road Ahead - Blizzard
MOOD: Danger
CHARACTERS: Narrator
BACKGROUND_IMAGE: road_ahead_blizzard.png
BACKGROUND_EDIT: "A mountain storm, a blizzard, as if the top of the sky has been pulled off"

::SCRIPT::
- CHARACTER: Narrator
  LINE: CUT TO: THE ROAD AHEAD--and here it comes--a mountain storm; it's as if the top has been pulled off the sky and with no warning whatsoever, we're into a blizzard and
  EXPRESSION: null

::PATHS::
- CHOICE: "Show the Mustang in the storm"
  TARGET: mustang_slowing
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Mustang Slowing
MOOD: Struggle
CHARACTERS: Narrator
BACKGROUND_IMAGE: mustang_slowing.png
BACKGROUND_EDIT: "A Mustang slowing, driving deeper into the mountains in a blizzard"

::SCRIPT::
- CHARACTER: Narrator
  LINE: CUT TO: THE MUSTANG, slowing, driving deeper into the mountains.
  EXPRESSION: null

::PATHS::
- CHOICE: "Show Paul squinting"
  TARGET: paul_squinting
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Paul Squinting
MOOD: Impaired Vision
CHARACTERS: Narrator, Paul Sheldon
BACKGROUND_IMAGE: paul_squinting.png
BACKGROUND_EDIT: "Paul Sheldon squinting ahead, windshield wipers on"

::SCRIPT::
- CHARACTER: Narrator
  LINE: CUT TO: PAUL, squinting ahead, windshield wipers on now.
  EXPRESSION: null

::PATHS::
- CHOICE: "Show the Mustang losing traction"
  TARGET: mustang_losing_traction
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Mustang Losing Traction
MOOD: Loss of Control
CHARACTERS: Narrator
BACKGROUND_IMAGE: mustang_losing_traction.png
BACKGROUND_EDIT: "A Mustang rounding a curve, losing traction"

::SCRIPT::
- CHARACTER: Narrator
  LINE: CUT TO: THE MUSTANG, rounding another curve, losing traction--
  EXPRESSION: null

::PATHS::
- CHOICE: "Show Paul regaining control"
  TARGET: paul_controlling_car
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Paul Controlling Car
MOOD: Skillful Maneuver
CHARACTERS: Narrator, Paul Sheldon
BACKGROUND_IMAGE: paul_controlling_car.png
BACKGROUND_EDIT: "Paul Sheldon, a skilled driver, bringing the car easily under control"

::SCRIPT::
- CHARACTER: Narrator
  LINE: CUT TO: PAUL, a skilled driver, bringing the car easily under control.
  EXPRESSION: null

::PATHS::
- CHOICE: "Show the road ahead"
  TARGET: road_snow_piling_up
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Road - Snow Piling Up
MOOD: Desolate and Dangerous
CHARACTERS: Narrator
BACKGROUND_IMAGE: road_snow_piling_up.png
BACKGROUND_EDIT: "Snow piling up on the road"

::SCRIPT::
- CHARACTER: Narrator
  LINE: CUT TO: THE ROAD Snow is piling up.
  EXPRESSION: null

::PATHS::
- CHOICE: "Show Paul driving confidently"
  TARGET: paul_driving_confidently
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Paul Driving Confidently
MOOD: Focused
CHARACTERS: Narrator, Paul Sheldon
BACKGROUND_IMAGE: paul_driving_confidently.png
BACKGROUND_EDIT: "Paul Sheldon driving confidently and carefully, ejecting a tape"

::SCRIPT::
- CHARACTER: Narrator
  LINE: CUT TO: PAUL driving confidently, carefully. Now he reaches out, ejects the tape, expertly turns it over, pushes it in and, as the MUSIC continues, he hums along with it.
  EXPRESSION: null

::PATHS::
- CHOICE: "Show the obscured sky"
  TARGET: sky_unseen
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Sky - Unseen
MOOD: Blinding Snow
CHARACTERS: Narrator
BACKGROUND_IMAGE: sky_unseen.png
BACKGROUND_EDIT: "Nothing to see but unending snow, wind getting wilder"

::SCRIPT::
- CHARACTER: Narrator
  LINE: CUT TO: THE SKY. Only you can't see it. There's nothing to see but the unending snow, nothing to hear but the wind which keeps getting wilder.
  EXPRESSION: null

::PATHS::
- CHOICE: "Show the road"
  TARGET: road_inches_of_snow
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Road - Inches of Snow
MOOD: Desolate and Dangerous
CHARACTERS: Narrator
BACKGROUND_IMAGE: road_inches_of_snow.png
BACKGROUND_EDIT: "Inches of snow on the ground, desolate and dangerous road"

::SCRIPT::
- CHARACTER: Narrator
  LINE: CUT TO: THE ROAD. Inches of snow on the ground now. This is desolate and dangerous.
  EXPRESSION: null

::PATHS::
- CHOICE: "Show Paul driving"
  TARGET: paul_driving_snow
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Paul Driving - Snow
MOOD: Continuing Struggle
CHARACTERS: Narrator, Paul Sheldon
BACKGROUND_IMAGE: paul_driving_snow.png
BACKGROUND_EDIT: "Paul Sheldon driving in worsening snow"

::SCRIPT::
- CHARACTER: Narrator
  LINE: CUT TO: PAUL, driving.
  EXPRESSION: null

::PATHS::
- CHOICE: "Show the snow getting worse"
  TARGET: snow_worse
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Snow - Worse
MOOD: Intensifying Danger
CHARACTERS: Narrator
BACKGROUND_IMAGE: snow_worse.png
BACKGROUND_EDIT: "The snow is getting worse"

::SCRIPT::
- CHARACTER: Narrator
  LINE: CUT TO: THE SNOW. Worse.
  EXPRESSION: null

::PATHS::
- CHOICE: "Show the sharp curve"
  TARGET: road_curving_sign
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Road - Curving with Sign
MOOD: Critical Danger
CHARACTERS: Narrator
BACKGROUND_IMAGE: road_curving_sign.png
BACKGROUND_EDIT: "Road curving sharply, dropping, with a sign that reads 'Curved Road, Next 13 Miles.'"

::SCRIPT::
- CHARACTER: Narrator
  LINE: CUT TO: THE ROAD, curving sharply, drop ping. A sign reads: "Curved Road, Next 13 Miles."
  EXPRESSION: null

::PATHS::
- CHOICE: "Show the Mustang hitting the curve"
  TARGET: mustang_skidding_out_of_control
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Mustang Skidding Out of Control
MOOD: Catastrophe
CHARACTERS: Narrator
BACKGROUND_IMAGE: mustang_skidding_out_of_control.png
BACKGROUND_EDIT: "A Mustang coming into view, hitting the curve, skidding out of control"

::SCRIPT::
- CHARACTER: Narrator
  LINE: CUT TO: THE MUSTANG, coming into view, hitting the curve--no problem--no problem at all--and then suddenly, there is a very serious problem and as the car skids out of control--
  EXPRESSION: null

::PATHS::
- CHOICE: "Show Paul fighting for control"
  TARGET: paul_fighting_conditions
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Paul Fighting Conditions
MOOD: Desperate Effort
CHARACTERS: Narrator, Paul Sheldon
BACKGROUND_IMAGE: paul_fighting_conditions.png
BACKGROUND_EDIT: "Paul Sheldon doing his best, fighting the conditions"

::SCRIPT::
- CHARACTER: Narrator
  LINE: CUT TO: PAUL, doing his best, fighting the conditions and just as it looks like he's got things going his way--
  EXPRESSION: null

::PATHS::
- CHOICE: "Show the road swerving"
  TARGET: road_swerving_down
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Road - Swerving Down
MOOD: Uncontrollable Descent
CHARACTERS: Narrator
BACKGROUND_IMAGE: road_swerving_down.png
BACKGROUND_EDIT: "The road swerving down"

::SCRIPT::
- CHARACTER: Narrator
  LINE: CUT TO: THE ROAD, swerving down and
  EXPRESSION: null

::PATHS::
- CHOICE: "Show the Mustang losing traction"
  TARGET: mustang_all_traction_gone
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Mustang - All Traction Gone
MOOD: Helplessness
CHARACTERS: Narrator
BACKGROUND_IMAGE: mustang_all_traction_gone.png
BACKGROUND_EDIT: "A Mustang with all traction gone"

::SCRIPT::
- CHARACTER: Narrator
  LINE: CUT TO: THE MUSTANG, all traction gone and
  EXPRESSION: null

::PATHS::
- CHOICE: "Show Paul's helplessness"
  TARGET: paul_helpless
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Paul - Helpless
MOOD: Utter Helplessness
CHARACTERS: Narrator, Paul Sheldon
BACKGROUND_IMAGE: paul_helpless.png
BACKGROUND_EDIT: "Paul Sheldon, helpless"

::SCRIPT::
- CHARACTER: Narrator
  LINE: CUT TO: PAUL, helpless and
  EXPRESSION: null

::PATHS::
- CHOICE: "Show the Mustang skidding"
  TARGET: mustang_skidding
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Mustang - Skidding
MOOD: Continued Descent
CHARACTERS: Narrator
BACKGROUND_IMAGE: mustang_skidding.png
BACKGROUND_EDIT: "A Mustang skidding, skidding"

::SCRIPT::
- CHARACTER: Narrator
  LINE: CUT TO: THE MUSTANG, skidding, skidding and
  EXPRESSION: null

::PATHS::
- CHOICE: "Show the road and wind"
  TARGET: road_steep_drop_wind
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Road - Steep Drop and Wind
MOOD: Extreme Danger
CHARACTERS: Narrator
BACKGROUND_IMAGE: road_steep_drop_wind.png
BACKGROUND_EDIT: "The road drops more steeply away, wind whips snow across"

::SCRIPT::
- CHARACTER: Narrator
  LINE: CUT TO: THE ROAD as it drops more steeply away and the wind whips the snow across and
  EXPRESSION: null

::PATHS::
- CHOICE: "Show the Mustang spinning"
  TARGET: mustang_spinning
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Mustang - Spinning
MOOD: Out of Control
CHARACTERS: Narrator
BACKGROUND_IMAGE: mustang_spinning.png
BACKGROUND_EDIT: "A Mustang starting to spin"

::SCRIPT::
- CHARACTER: Narrator
  LINE: CUT TO: THE MUSTANG starting to spin and
  EXPRESSION: null

::PATHS::
- CHOICE: "Show the mountainside and impact"
  TARGET: mountainside_crash
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Mountainside - Crash
MOOD: Devastating Crash
CHARACTERS: Narrator
BACKGROUND_IMAGE: mountainside_crash.png
BACKGROUND_EDIT: "The car skids off the road, careens down a mountainside, slams into a tree, bounces off, flips, lands upside down, skids, stops finally, dead"

::SCRIPT::
- CHARACTER: Narrator
  LINE: CUT TO: THE MOUNTAINSIDE as the car skids off the road, careens down, slams into a tree, bounces off, flips, lands upside down, skids, stops finally, dead.
  EXPRESSION: null

::PATHS::
- CHOICE: "Hold on the car"
  TARGET: car_wreck_hold
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Car Wreck - Hold
MOOD: Stillness after Chaos
CHARACTERS: Narrator
BACKGROUND_IMAGE: car_wreck_hold.png
BACKGROUND_EDIT: "The wrecked car, upside down, motionless. Wind and music still playing."

::SCRIPT::
- CHARACTER: Narrator
  LINE: HOLD ON THE CAR A MOMENT 2 2 2 There is still the sound of the WIND, and there is still the music coming from the tape, perhaps the only part of the car left undamaged. Nothing moves inside. There is only the WIND and the TAPE. The wind gets louder.
  EXPRESSION: null

::PATHS::
- CHOICE: "View the wreck from a distance"
  TARGET: wreck_from_distance
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Wreck from a Distance
MOOD: Overwhelming Snow
CHARACTERS: Narrator
BACKGROUND_IMAGE: wreck_from_distance.png
BACKGROUND_EDIT: "The wreck viewed from a distance, music faintly heard, snow covering it"

::SCRIPT::
- CHARACTER: Narrator
  LINE: CUT TO: THE WRECK looked at from a distance. The MUSIC sounds are only faintly heard.
  EXPRESSION: null

::PATHS::
- CHOICE: "View from the road"
  TARGET: wreck_from_road
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Wreck from the Road
MOOD: Disappearing Wreckage
CHARACTERS: Narrator
BACKGROUND_IMAGE: wreck_from_road.png
BACKGROUND_EDIT: "The area where the wreck is, as seen from the road. The car is barely visible as snow covers it."

::SCRIPT::
- CHARACTER: Narrator
  LINE: CUT TO: THE AREA WHERE THE WRECK IS--AS SEEN FROM THE ROAD. The car is barely visible as the snow begins to cover it.
  EXPRESSION: null

::PATHS::
- CHOICE: "Close up on the wreck"
  TARGET: wreck_close_up
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Wreck - Close Up
MOOD: Suffocating Snow
CHARACTERS: Narrator, Paul Sheldon
BACKGROUND_IMAGE: wreck_close_up.png
BACKGROUND_EDIT: "The wreck from outside, close up, snow coming down harder, covering parts of the car. Paul is inside, losing consciousness."

::SCRIPT::
- CHARACTER: Narrator
  LINE: CUT TO: THE WRECK from outside, and we're close to it now, with the snow coming down ever harder--already bits of the car are covered in white. CAMERA MOVES IN TO PAUL. He's inside and doing his best to fight is, but his consciousness is going. He tries to keep his eyes open but they're slits.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Slowly, he manages to reach out with his left arm for his briefcase--and he clutches it to his battered body. The MUSIC cont
  EXPRESSION: null

::PATHS::
- CHOICE: "End Scene"
  TARGET: end
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Undisclosed
MOOD: Fading Life
CHARACTERS: Paul, Narrator
BACKGROUND_IMAGE: null
BACKGROUND_EDIT: "Paul is in physical distress, eyes fluttering"

::SCRIPT::
- CHARACTER: Narrator
  LINE: ...inues on. But PAUL is far from listening. His eyes flutter, flutter again. Nov; they're starting to close. The man is dying.
  EXPRESSION: Dying
- CHARACTER: Narrator
  LINE: Motionless, he still clutches the battered briefcase.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: HOLD ON THE CASE.
  EXPRESSION: null

::PATHS::
- CHOICE: "Dissolve"
  TARGET: office_scene
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Marcia Sindell's Office, New York City
MOOD: Professional, Nostalgic
CHARACTERS: Paul, Marcia Sindell
BACKGROUND_IMAGE: office.png
BACKGROUND_EDIT: "Spacious office, walls covered in book and movie posters of Misery Chastain"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The BRIEFCASE in Paul's hands as he sits at a desk.
  EXPRESSION: null
- CHARACTER: Marcia Sindell (O.S.)
  LINE: What’s that?
  EXPRESSION: Curious
- CHARACTER: Narrator
  LINE: PULL BACK TO REVEAL We are in New York City in the office of Paul's literary agent, MARCIA SINDELL. The walls of the large room are absolutely crammed with book and movie posters, in English and all other kinds of other languages, all of them featuring the character of MISERY CHASTAIN, a perfectly beautiful woman. Misery’s Challenge, Misery's Triumph--eight of them. All written by Paul Sheldon.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: PAUL, lifting up the battered briefcase--maybe when new it cost two bucks, but he treats it like gold.
  EXPRESSION: Sentimental
- CHARACTER: Paul
  LINE: An old friend. I was rummaging through a closet and it was just sitting there. Like it was waiting for me.
  EXPRESSION: Reflective
- CHARACTER: Marcia Sindell
  LINE: It's... it's nice, Paul. It's got... character.
  EXPRESSION: Trying to compliment
- CHARACTER: Paul
  LINE: When I wrote my first book, I used to carry it around in this while I was looking for a publisher. That was a good book, Marcia. I was a writer then.
  EXPRESSION: Nostalgic
- CHARACTER: Marcia Sindell
  LINE: You're still a writer.
  EXPRESSION: Reassuring
- CHARACTER: Paul
  LINE: I haven't been a writer since I got into the Misery business--
  EXPRESSION: Bitter
- CHARACTER: Marcia Sindell
  LINE: Not a bad business. This thing would still be growing, too. The first printing order on Misery's Child was the most ever--over a million.
  EXPRESSION: Matter-of-fact
- CHARACTER: Paul
  LINE: Marcia, please.
  EXPRESSION: Pleading
- CHARACTER: Marcia Sindell
  LINE: No, no. Misery Chastain put braces on your daughter's teeth and is putting her through college, bought you two houses and floor seats to the Knick games and what thanks does she get? You go and kill her.
  EXPRESSION: Accusatory
- CHARACTER: Paul
  LINE: Marcia, you know I started "Misery" on a lark. Do I look like a guy who writes romance novels? Do I sound like Danielle Steel? It was a one-time shot and we got lucky. I never meant it to become my life. And if I hadn't gotten rid of her now, I'd have ended up writing her forever. For the first time in fifteen years, I think I'm really onto something here.
  EXPRESSION: Defensive, Passionate
- CHARACTER: Marcia Sindell
  LINE: I'm glad to hear that, Paul, I really am. But you have to know--when your fans find out that you killed off their favorite heroine, they're not going to say, "Ooh, good, Paul Sheldon can finally write what we've always wanted: An esoteric, semi-autobiographical character study."
  EXPRESSION: Cautionary
- CHARACTER: Paul
  LINE: Marcia, why are you doing this to me? Don't you know I'm scared enough? Don't you think I remember how nobody gave a shit about my first books? You think I'm dying to go back to shouting in the wilderness? I'm doing this because I have to.
  EXPRESSION: Desperate, Passionate
- CHARACTER: Paul
  LINE: Now, I'm leaving for Colorado to try to finish this and I want your good thoughts--because if I can make it work ... I might just have something that I want on my tombstone.
  EXPRESSION: Determined

::PATHS::
- CHOICE: "Visualize tombstone"
  TARGET: tombstone_vision
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Paul's Tombstone Vision
MOOD: Ominous, Tragic
CHARACTERS: Paul, Narrator
BACKGROUND_IMAGE: tombstone.png
BACKGROUND_EDIT: "Upside down car in a blizzard"

::SCRIPT::
- CHARACTER: Narrator
  LINE: PAUL'S TOMBSTONE--the upside down car with the blizzard coming gale-force and his motionless body trapped inside the car.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The WIND screams. PAUL'S EYES flutter, then close. Hold.
  EXPRESSION: null

::PATHS::
- CHOICE: "Keep holding"
  TARGET: car_rescue
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Car Wreckage
MOOD: Desperate Rescue
CHARACTERS: Narrator, Paul, Annie Wilkes
BACKGROUND_IMAGE: car_wreckage.png
BACKGROUND_EDIT: "Snowstorm, car upside down"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Suddenly there’s a new sound as a crowbar SCRATCHES at the door--
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: --and now the door is ripped open as we PULL BACK TO REVEAL A BUNDLED-UP FIGURE gently beginning to pull PAUL and the case from the car. For a moment, it’s hard to tell if it's a man or woman-- --not to let the cat out of the bag or anything, but it is, very much, a woman. Her name is ANNIE WILKES and she is close to Paul’s age. She is in many ways a remarkable creature. Strong, self-sufficient, passionate in her likes and dislikes, loves and hates.
  EXPRESSION: null

::PATHS::
- CHOICE: "Reveal Annie"
  TARGET: paul_annie_cradled
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Car Wreckage
MOOD: Caring, Urgent
CHARACTERS: Paul, Annie Wilkes
BACKGROUND_IMAGE: snow.png
BACKGROUND_EDIT: "Paul is being cradled by Annie in the snow"

::SCRIPT::
- CHARACTER: Narrator
  LINE: PAUL AND ANNIE as she cradles him in her arms. Once he's clear of the car, she lays him carefully in the snow
  EXPRESSION: null

::PATHS::
- CHOICE: "Close up on lips"
  TARGET: resuscitation
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Car Wreckage
MOOD: Life-saving, Intense
CHARACTERS: Paul, Annie Wilkes
BACKGROUND_IMAGE: snow.png
BACKGROUND_EDIT: "Close up on Paul and Annie's lips as she performs CPR"

::SCRIPT::
- CHARACTER: Narrator
  LINE: PAUL AND ANNIE: CLOSE UP. She slowly brings her mouth down close to his. Then their lips touch as she forces air inside him.
  EXPRESSION: null
- CHARACTER: Annie Wilkes
  LINE: You hear me--Breathe! I said breathe!!!
  EXPRESSION: Urgent, Demanding

::PATHS::
- CHOICE: "Paul breathes"
  TARGET: paul_breathing
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Car Wreckage
MOOD: Coming back to life, Shock
CHARACTERS: Paul, Annie Wilkes
BACKGROUND_IMAGE: snow.png
BACKGROUND_EDIT: "Paul's eyes open, he's in shock"

::SCRIPT::
- CHARACTER: Narrator
  LINE: PAUL, as he starts to breathe-- --in a moment his eyes suddenly open wide, but he's in shock, the eyes see nothing--
  EXPRESSION: Shocked
- CHARACTER: Narrator
  LINE: ANNIE--the moment she sees him come to life, she goes into action, lifting PAUL in a fireman's carry, starting the difficult climb back up the steep hill. As she moves away, she and Paul are obliterated by the white failing snow.
  EXPRESSION: Determined

::PATHS::
- CHOICE: "Dissolve"
  TARGET: hospital_vision
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Paul's Blurred Vision (Hospital)
MOOD: Disoriented, Faint
CHARACTERS: Paul, Narrator
BACKGROUND_IMAGE: hospital.png
BACKGROUND_EDIT: "Everything is white and blurred"

::SCRIPT::
- CHARACTER: Narrator
  LINE: THE WHITE OF WHAT SEEMS LIKE A HOSPITAL. Everything is bled of color. It's all vague-- --we are looking at this from Paul’s blurred vision. And throughout this next sequence, there are these SOUNDS, words really, but they make no sense. "...no... worry... ...be... fine... ...good care... you... ...I'm your number one fan..."
  EXPRESSION: Vague
- CHARACTER: Narrator
  LINE: The first thing we see during this is something all white. It takes a moment before we realize it's a ceiling. Now, a white wall.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: An I.V. bottle is next, the medicine dripping down a tube into PAUL'S LEFT ARM. The other arm is bandaged and in a sling.
  EXPRESSION: null

::PATHS::
- CHOICE: "Reveal Annie"
  TARGET: annie_nurse
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Paul's Room (Hospital)
MOOD: Caring, Attentive
CHARACTERS: Annie Wilkes, Paul
BACKGROUND_IMAGE: hospital_room.png
BACKGROUND_EDIT: "Paul is in bed, Annie is by his side like a nurse"

::SCRIPT::
- CHARACTER: Narrator
  LINE: ANNIE is standing beside the bed. She wears off-white and seems very much like a nurse. A good nurse. She has pills in her hands.
  EXPRESSION: null

::PATHS::
- CHOICE: "Show Paul"
  TARGET: paul_feverish
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Paul's Room (Hospital)
MOOD: Weakness, Confusion
CHARACTERS: Paul, Annie Wilkes
BACKGROUND_IMAGE: hospital_room.png
BACKGROUND_EDIT: "Paul is pale and feverish, eyes barely open"

::SCRIPT::
- CHARACTER: Narrator
  LINE: PAUL. Motionless, dead pale. He has a little beard now. Eyes barely open, he's shaking with fever.
  EXPRESSION: Ill
- CHARACTER: Paul
  LINE: ...where... am I...?
  EXPRESSION: Weak
- CHARACTER: Annie Wilkes
  LINE: Shhh... we’re just outside Silver Creek.
  EXPRESSION: Gentle
- CHARACTER: Paul
  LINE: How long...?
  EXPRESSION: Faint
- CHARACTER: Annie Wilkes
  LINE: You've been here two days, You're gonna be okay. My name is Annie Wilkes and I'm--
  EXPRESSION: Relieved
- CHARACTER: Paul
  LINE: --my number one fan.
  EXPRESSION: Realization
- CHARACTER: Annie Wilkes
  LINE: That’s right. I’m also a nurse. Here. Take these.
  EXPRESSION: Assertive
- CHARACTER: Narrator
  LINE: She helps him to swallow, as Paul's eyes close.
  EXPRESSION: null

::PATHS::
- CHOICE: "Dissolve"
  TARGET: farmhouse_exterior
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Farmhouse Exterior
MOOD: Isolated, Remote
CHARACTERS: Narrator
BACKGROUND_IMAGE: farmhouse.png
BACKGROUND_EDIT: "Desolate landscape with mountains, farmhouse on a knoll"

::SCRIPT::
- CHARACTER: Narrator
  LINE: AN EXTERIOR OF THE PLACE. It's a farmhouse--we're in a desolate area with mountains in the background. THE HOUSE is set on a knoll so that Paul’s room, although on the first floor, is ten feet off the ground.
  EXPRESSION: null

::PATHS::
- CHOICE: "Cut to Paul in room"
  TARGET: paul_in_room
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Paul's Room
MOOD: Confinement, Weakness
CHARACTERS: Paul
BACKGROUND_IMAGE: room.png
BACKGROUND_EDIT: "Paul is in his room, still weak"

::SCRIPT::
- CHARACTER: Narrator
  LINE: PAUL, in the room. He's not on t
  EXPRESSION: null

::SCENE::
LOCATION: Paul's Room
MOOD: Recuperation
CHARACTERS: Narrator, Annie, Paul
BACKGROUND_IMAGE: paul_room_1.png
BACKGROUND_EDIT: "Paul's bedside, I.V. removed, fever broken"

::SCRIPT::
- CHARACTER: Narrator
  LINE: He I.V. anymore. His fever has broken. Annie enters, pills in her hand.
  EXPRESSION: null
- CHARACTER: Annie
  LINE: Here.
  EXPRESSION: Concerned
- CHARACTER: Paul
  LINE: What are they...?
  EXPRESSION: Weak
- CHARACTER: Annie
  LINE: They’re called Novril--they're for your pain.
  EXPRESSION: Caring
- CHARACTER: Narrator
  LINE: Annie applies a cool rag to his forehead.
  EXPRESSION: null
- CHARACTER: Paul
  LINE: Shouldn't I be in a hospital?
  EXPRESSION: Anxious
- CHARACTER: Annie
  LINE: The blizzard was too strong. I couldn't risk trying to get you there. I tried calling, but the phone lines are down.
  EXPRESSION: Determined
- CHARACTER: Narrator
  LINE: Paul tries to test his left arm.
  EXPRESSION: null
- CHARACTER: Annie
  LINE: (Gently, her fingers go to his eyelids, close them) Now you mustn't tire yourself. You've got to rest, you almost died.
  EXPRESSION: Soothing

::PATHS::
- CHOICE: "Continue resting"
  TARGET: annie_close_up
  STATE_CHANGE: paul_health = +2
  CONDITION: null

::SCENE::
LOCATION: Annie - Close Up
MOOD: Compassion
CHARACTERS: Narrator, Annie
BACKGROUND_IMAGE: annie_close_up.png
BACKGROUND_EDIT: "Close up on Annie's face, showing deep compassion"

::SCRIPT::
- CHARACTER: Narrator
  LINE: CLOSE UP. Sometimes her face shows the most remarkable compassion. It does now.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: HOLD ON IT briefly.
  EXPRESSION: null

::PATHS::
- CHOICE: "Dissolve to pills"
  TARGET: pills_close_up
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Close Up on Pills
MOOD: Anticipation
CHARACTERS: Narrator, Annie
BACKGROUND_IMAGE: pills_close_up.png
BACKGROUND_EDIT: "Extreme close up on pills in Annie's hand"

::SCRIPT::
- CHARACTER: Annie (O.S.)
  LINE: Open wide.
  EXPRESSION: Caring

::PATHS::
- CHOICE: "Cut to Paul's Room"
  TARGET: paul_room_3
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Paul's Room
MOOD: Weakness
CHARACTERS: Narrator, Paul
BACKGROUND_IMAGE: paul_room_3.png
BACKGROUND_EDIT: "Paul in bed, fever gone but very weak"

::SCRIPT::
- CHARACTER: Narrator
  LINE: He lies in bed. His fever is gone, but he's terribly weak.
  EXPRESSION: null

::PATHS::
- CHOICE: "Cut to Annie administering pills"
  TARGET: annie_administering_pills
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Annie Administering Pills
MOOD: Caregiving
CHARACTERS: Narrator, Annie, Paul
BACKGROUND_IMAGE: annie_administering_pills.png
BACKGROUND_EDIT: "Annie gives Paul pills and water"

::SCRIPT::
- CHARACTER: Narrator
  LINE: As she lays the pills on Paul's tongue, she gives him a glass of water from the nearby bed table.
  EXPRESSION: null

::PATHS::
- CHOICE: "Cut to Paul swallowing"
  TARGET: paul_swallowing
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Paul Swallowing
MOOD: Relief
CHARACTERS: Narrator, Paul
BACKGROUND_IMAGE: paul_swallowing.png
BACKGROUND_EDIT: "Close up on Paul swallowing the pills eagerly"

::SCRIPT::
- CHARACTER: Narrator
  LINE: swallowing eagerly.
  EXPRESSION: null

::PATHS::
- CHOICE: "Cut to Annie watching"
  TARGET: annie_watching
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Annie Watching
MOOD: Sympathy
CHARACTERS: Narrator, Annie, Paul
BACKGROUND_IMAGE: annie_watching.png
BACKGROUND_EDIT: "Annie watches Paul sympathetically"

::SCRIPT::
- CHARACTER: Annie
  LINE: Your legs just sing grand opera when you move, don't they?
  EXPRESSION: Sympathetic
- CHARACTER: Narrator
  LINE: (Paul says nothing, but his pain is clear)
  EXPRESSION: null
- CHARACTER: Annie
  LINE: It’s not going to hurt forever, Paul, I promise you.
  EXPRESSION: Reassuring
- CHARACTER: Paul
  LINE: Will I be able to walk?
  EXPRESSION: Hopeful
- CHARACTER: Annie
  LINE: Of course you will. And your arm will be fine, too. Your shoulder was dislocated pretty badly, but I finally popped it back in there. But what I’m most proud of is the work I did on those legs. Considering what I had around the house, I don’t think there’s a doctor who could have done any better.
  EXPRESSION: Proud

::PATHS::
- CHOICE: "Reveal Paul's legs"
  TARGET: paul_legs_reveal
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Paul's Legs Reveal
MOOD: Shock
CHARACTERS: Narrator, Annie, Paul
BACKGROUND_IMAGE: paul_legs_reveal.png
BACKGROUND_EDIT: "Blanket flicked off, revealing Paul's legs"

::SCRIPT::
- CHARACTER: Narrator
  LINE: And now suddenly she flicks off the blankets, uncovering his body.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: staring, stunned at the bottom half of his body as we
  EXPRESSION: null

::PATHS::
- CHOICE: "Show Paul's legs close up"
  TARGET: paul_legs_close_up
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Paul's Legs Close Up
MOOD: Gruesome
CHARACTERS: Narrator, Paul
BACKGROUND_IMAGE: paul_legs_close_up.png
BACKGROUND_EDIT: "Close up on Paul's legs, splinted and bandaged"

::SCRIPT::
- CHARACTER: Narrator
  LINE: From the knees down he resembles an Egyptian mummy--she's splinted them with slim steel rods that look like the hacksawed remains of aluminum crutches and there's taping circling around. From the knees up they're all swollen and throbbing and horribly bruised and discolored.
  EXPRESSION: null

::PATHS::
- CHOICE: "Cut to Paul's reaction"
  TARGET: paul_reaction
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Paul's Reaction
MOOD: Disbelief
CHARACTERS: Narrator, Paul, Annie
BACKGROUND_IMAGE: paul_reaction.png
BACKGROUND_EDIT: "Paul lying back, stunned with disbelief"

::SCRIPT::
- CHARACTER: Narrator
  LINE: lying back, stunned with disbelief.
  EXPRESSION: null
- CHARACTER: Annie
  LINE: It's not nearly as bad as it looks. You have a compound fracture of the tibia in both legs, and the fibula in the left leg is fractured too. I could hear the bones moving, so it's best for your legs to remain immobile. And as soon as the roads open, I'll take you to a hospital.
  EXPRESSION: Explanatory

::PATHS::
- CHOICE: "Cut to Annie's close up"
  TARGET: annie_close_up_2
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Annie - Close Up
MOOD: Ecstatic
CHARACTERS: Narrator, Annie
BACKGROUND_IMAGE: annie_close_up_2.png
BACKGROUND_EDIT: "Close up on Annie's ecstatic face"

::SCRIPT::
- CHARACTER: Annie
  LINE: In the meantime, you've got a lot of recovering to do, and I consider it an honor that you’ll do it in my home.
  EXPRESSION: Ecstatic
- CHARACTER: Narrator
  LINE: HOLD on her ecstatic face.
  EXPRESSION: null

::PATHS::
- CHOICE: "Transition to New York"
  TARGET: sindell_office
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Sindell's Office, New York
MOOD: Concern
CHARACTERS: Narrator, Sindell
BACKGROUND_IMAGE: sindell_office.png
BACKGROUND_EDIT: "Sindell's office in New York, messy but familiar"

::SCRIPT::
- CHARACTER: Narrator
  LINE: MISERY’S PERFECT FACE. We’re back in Sindell's office in New York. The office looks just the same, posters and manuscripts all over. But she doesn't.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: She holds the phone and she is fidgety, insecure.
  EXPRESSION: Nervous
- CHARACTER: Sindell
  LINE: This is Marcia Sindell calling from New York City. I'd like to speak to the Silver Creek Chief of Police or the Sheriff.
  EXPRESSION: Anxious
- CHARACTER: Male Voice (O.S.)
  LINE: Which one do you want?
  EXPRESSION: Neutral
- CHARACTER: Sindell
  LINE: Whichever one's not busy.
  EXPRESSION: Eager

::PATHS::
- CHOICE: "Cut to Silver Creek office"
  TARGET: silver_creek_office
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Small Office in Silver Creek
MOOD: Unassuming Authority
CHARACTERS: Narrator, Buster
BACKGROUND_IMAGE: silver_creek_office.png
BACKGROUND_EDIT: "Small office with a view of mountains, Buster at desk"

::SCRIPT::
- CHARACTER: Narrator
  LINE: ...with a view of the mountains. A MARVELOUS LOOKING MAN sits at a desk, by himself, holding the phone. In his sixties, he's still as bright, fast and sassy as he was half-a-lifetime ago. Never mind what his name is, everyone calls him BUSTER.
  EXPRESSION: null
- CHARACTER: Buster
  LINE: I'm pretty sure they're both not busy, Ms. Sindell, since they're both me. I also happen to be President of the Policeman's Benefit Association, Chairman of the Patrolman's Retirement Fund, and if you need a good fishing guide, you could do a lot worse; call me Buster, everybody does, what can I do for you?
  EXPRESSION: Jovial

::PATHS::
- CHOICE: "Cut to Sindell in her office"
  TARGET: sindell_her_office
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Sindell's Office
MOOD: Hesitation
CHARACTERS: Narrator, Sindell, Buster
BACKGROUND_IMAGE: sindell_her_office.png
BACKGROUND_EDIT: "Sindell paces in her office, speaking via speakerphone"

::SCRIPT::
- CHARACTER: Narrator
  LINE: SINDELL in her office. She pushes the speakerphone, gets up, paces; she's very hesitant when she speaks about Paul. Almost embarrassed--
  EXPRESSION: null
- CHARACTER: Sindell
  LINE: I'm a literary agent, and I feel like a fool calling you, but I think one of my clients, Paul Sheldon, might be in some kind of trouble.
  EXPRESSION: Embarrassed
- CHARACTER: Buster
  LINE: Paul Sheldon? You mean Paul Sheldon the writer?
  EXPRESSION: Surprised
- CHARACTER: Sindell
  LINE: Yes.
  EXPRESSION: Nervous
- CHARACTER: Buster
  LINE: He’s your client, huh?
  EXPRESSION: Curious
- CHARACTER: Sindell
  LINE: Yes, he is.
  EXPRESSION: Nervous

::PATHS::
- CHOICE: "Cut to Buster's office"
  TARGET: buster_office
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Buster's Office
MOOD: Observant
CHARACTERS: Narrator, Buster, Sindell
BACKGROUND_IMAGE: buster_office.png
BACKGROUND_EDIT: "Buster rolls a penny on his hand, listening to Sindell"

::SCRIPT::
- CHARACTER: Narrator
  LINE: He rolls a penny across the back of one hand--he’s very good at it, doesn’t even look while he does it.
  EXPRESSION: null
- CHARACTER: Sindell
  LINE: People sure like those Misery books.
  EXPRESSION: Confident
- CHARACTER: Buster
  LINE: I'm sure you know Paul’s been going to the Silver Creek Lodge for years to finish his books.
  EXPRESSION: Knowledgeable
- CHARACTER: Sindell
  LINE: Yeah, I understand he's been up here the last six weeks.
  EXPRESSION: Concerned
- CHARACTER: Buster
  LINE: Not quite. I just called, and they said he checked out five days ago. Isn't that a little strange?
  EXPRESSION: Inquisitive
- CHARACTER: Sindell
  LINE: I don't know. Does he always phone you when he checks out of hotels?
  EXPRESSION: Flustered

::PATHS::
- CHOICE: "Cut to Sindell's reaction"
  TARGET: sindell_reaction
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Sindell's Reaction
MOOD: Embarrassment
CHARACTERS: Narrator, Sindell
BACKGROUND_IMAGE: sindell_reaction.png
BACKGROUND_EDIT: "Sindell looking increasingly embarrassed"

::SCRIPT::
- CHARACTER: Narrator
  LINE: SINDELL, really embarrassed now.
  EXPRESSION: null
- CHARACTER: Sindell
  LINE: No, no, of course not. It's just that his daughter hasn’t heard from him, and when he's got a book coming out, he usually keeps in touch. So when there was no word from him...
  EXPRESSION: Anxious
- CHARACTER: Buster
  LINE: You think he might be missing?
  EXPRESSION: Direct
- CHARACTER: Sindell
  LINE: (shakes her head) I hate that I made this call--tell me I'm being silly.
  EXPRESSION: Desperate

::PATHS::
- CHOICE: "Cut to Buster and Virginia"
  TARGET: buster_virginia
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Buster and Virginia
MOOD: Calm Domesticity
CHARACTERS: Narrator, Buster, Virginia
BACKGROUND_IMAGE: buster_virginia.png
BACKGROUND_EDIT: "Buster nods as Virginia enters with lunch"

::SCRIPT::
- CHARACTER: Narrator
  LINE: CUT TO: BUSTER. He nods as a WOMAN enters, carrying lunch. It's his wife, VIRGINIA. She begins putting the food down on a table for the both of them.
  EXPRESSION: null
- CHARACTER: Buster
  LINE: Just a little over-protective, maybe, Tell you what--nothing’s been reported out here--
  EXPRESSION: Reassuring
- CHARACTER: Narrator
  LINE: (he puts Paul Sheldon's name with a ? on a 3 x 5 CARD)
  EXPRESSION: null
- CHARACTER: Buster
  LINE: --but I'll put his name through our system. And if anything turns up, I'll call you right away.
  EXPRESSION: Professional

::PATHS::
- CHOICE: "Cut to Sindell's relief"
  TARGET: sindell_relief
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Sindell's Relief
MOOD: Relief
CHARACTERS: Narrator, Sindell
BACKGROUND_IMAGE: sindell_relief.png
BACKGROUND_EDIT: "Sindell smiles, relieved"

::SCRIPT::
- CHARACTER: Narrator
  LINE: SINDELL. She smiles, a genuine sense of relief.
  EXPRESSION: null
- CHARACTER: Sindell
  LINE: I appreciate that. Thanks a lot.
  EXPRESSION: Grateful

::PATHS::
- CHOICE: "Cut to Buster hanging up"
  TARGET: buster_hanging_up
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Buster Hanging Up
MOOD: Domestic
CHARACTERS: Narrator, Buster, Virginia
BACKGROUND_IMAGE: buster_hanging_up.png
BACKGROUND_EDIT: "Buster hangs up the phone, Virginia brings him lunch"

::SCRIPT::
- CHARACTER: Buster
  LINE: G'bye, Ms. Sindell.
  EXPRESSION: Courteous
- CHARACTER: Narrator
  LINE: As he hangs up--
  EXPRESSION: null
- CHARACTER: Virginia
  LINE: We actually got a phone call. Busy morning.
  EXPRESSION: Observant
- CHARACTER: Buster
  LINE: (smiles) Work, work, work. (gives her a hug) Virginia? When was that blizzard?
  EXPRESSION: Content
- CHARACTER: Virginia
  LINE: Four or five days ago. Why?
  EXPRESSION: Curious

::PATHS::
- CHOICE: "Cut to Buster's contemplation"
  TARGET: buster_contemplation
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Buster's Contemplation
MOOD: Pensive
CHARACTERS: Narrator, Buster
BACKGROUND_IMAGE: buster_contemplation.png
BACKGROUND_EDIT: "Buster plays with a penny, staring out the window"

::SCRIPT::
- CHARACTER: Narrator
  LINE: CUT TO: BUSTER. The penny flies across the back of his hand. He doesn’t look at it, stares instead out the window at the mountains.
  EXPRESSION: null
- CHARACTER: Buster
  LINE: (a beat) ...no reason...
  EXPRESSION: Thoughtful

::PATHS::
- CHOICE: "Hold on Buster"
  TARGET: hold_buster
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Paul's Room
MOOD: Reflective
CHARACTERS: Narrator, Paul
BACKGROUND_IMAGE: paul_room_6.png
BACKGROUND_EDIT: "Paul's room, soft lighting"

::SCRIPT::
- CHARACTER: Paul's Voice
  LINE: (soft) I guess it was kind of a miracle... you findi
  EXPRESSION: Grateful

::PATHS::
- CHOICE: "End Scene"
  TARGET: end
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Paul's Room
MOOD: Intimate
CHARACTERS: Narrator, Annie, Paul
BACKGROUND_IMAGE: paul_room_shaving.png
BACKGROUND_EDIT: "Paul in bed, Annie shaving him with a straight razor."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Annie’s soft, sweet laughter is heard. She stands over him, finishing shaving him with a very sharp straight razor. She wears what we will come to know as her regular costume--plain wool skirts, grey cardigan sweaters.
  EXPRESSION: null
- CHARACTER: Annie
  LINE: No, it wasn't a miracle at all... in a way, I was following you.
  EXPRESSION: Affectionate
- CHARACTER: Paul
  LINE: Following me?
  EXPRESSION: Confused
- CHARACTER: Narrator
  LINE: Annie concentrates on shaving him with great care; she has wonderful, strong hands.
  EXPRESSION: null
- CHARACTER: Annie
  LINE: Well, it wasn't any secret to me that you were staying at the Silver Creek, seeing as how I’m your number-one fan and all. Some nights I'd just tool on down there, sit outside and look up at the light in your cabin--and I'd try to imagine what was going on in the room of the world's greatest writer.
  EXPRESSION: Earnest
- CHARACTER: Narrator
  LINE: (gently moves his head back, exposing his neck; this next is said with total sincerity, almost awe)
  EXPRESSION: null
- CHARACTER: Paul
  LINE: Say that last part again, I didn't
  EXPRESSION: Curious
- CHARACTER: Annie
  LINE: Don’t move now--wouldn’t want to hurt this neck-- Well, the other afternoon I was on my way home, and there you were, leaving the Lodge, and I wondered why a literary genius would go for a drive when there was a big storm coming.
  EXPRESSION: Playful
- CHARACTER: Narrator
  LINE: (shaving away)
  EXPRESSION: null
- CHARACTER: Paul
  LINE: I didn't know it was going to be a big storm.
  EXPRESSION: Naive
- CHARACTER: Annie
  LINE: Lucky for you, I did. Lucky for me too. Because now you're alive and you can write more books. Oh, Paul, I've read everything of yours, but the Misery novels...
  EXPRESSION: Relieved
- CHARACTER: Narrator
  LINE: CUT TO:
  EXPRESSION: null

::SCENE::
LOCATION: Annie's Close Up
MOOD: Intense Devotion
CHARACTERS: Annie
BACKGROUND_IMAGE: annie_close_up.png
BACKGROUND_EDIT: "Close-up on Annie's face as she speaks."

::SCRIPT::
- CHARACTER: Annie
  LINE: I know them all by heart, Paul, all eight of them. I love them so.
  EXPRESSION: Passionate

::SCENE::
LOCATION: Paul's Room
MOOD: Tender
CHARACTERS: Narrator, Paul, Annie
BACKGROUND_IMAGE: paul_room_tender.png
BACKGROUND_EDIT: "Paul looking at Annie with newfound appreciation."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Paul, looking at her. There’s something terribly touching about her now.
  EXPRESSION: null
- CHARACTER: Paul
  LINE: You're very kind...
  EXPRESSION: Grateful
- CHARACTER: Annie
  LINE: And you're very brilliant, and you must be a good man, or you could never have created such a wondrous, loving creature as Misery Chastain. Like a baby. All done.
  EXPRESSION: Adoring
- CHARACTER: Narrator
  LINE: (runs her fingers over his cheek)
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: (smiles)
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: (starts to dab away the last bits of soap)
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Annie starts cleaning up.
  EXPRESSION: null
- CHARACTER: Paul
  LINE: When do you think the phone lines'll be back up? I have to call my daughter, and I should call New York and let my agent know I'm breathing.
  EXPRESSION: Anxious
- CHARACTER: Annie
  LINE: It shouldn't be too much longer, Once the roads are open, the lines'll be up in no time. If you give me their numbers, I'll keep trying them for you.
  EXPRESSION: Reassuring
- CHARACTER: Narrator
  LINE: (suddenly almost embarrassed)
  EXPRESSION: null
- CHARACTER: Annie
  LINE: Could I ask you a favor?
  EXPRESSION: Hopeful
- CHARACTER: Narrator
  LINE: (Paul nods)
  EXPRESSION: null
- CHARACTER: Annie
  LINE: I noticed in your case there was a new Paul Sheldon book and... and I wondered if maybe...
  EXPRESSION: Hesitant
- CHARACTER: Narrator
  LINE: (her voice trails off)
  EXPRESSION: null
- CHARACTER: Paul
  LINE: You want to read it?
  EXPRESSION: Surprised
- CHARACTER: Annie
  LINE: If you wouldn't mind.
  EXPRESSION: Eager
- CHARACTER: Paul
  LINE: I have a hard and fast rule about who can read my stuff at this early stage--only my editor, my agent, and anyone who saves me from freezing to death in a car wreck.
  EXPRESSION: Firm
- CHARACTER: Annie
  LINE: You'll never realize what a rare treat you've given me.
  EXPRESSION: Elated
- CHARACTER: Narrator
  LINE: CUT TO:
  EXPRESSION: null

::SCENE::
LOCATION: Paul
MOOD: Painful
CHARACTERS: Narrator, Paul
BACKGROUND_IMAGE: paul_grimace.png
BACKGROUND_EDIT: "Paul closing his eyes and grimacing in pain."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Paul. His eyes close briefly, he grimaces.
  EXPRESSION: Pained

::SCENE::
LOCATION: Annie
MOOD: Concerned
CHARACTERS: Narrator, Annie
BACKGROUND_IMAGE: annie_concerned.png
BACKGROUND_EDIT: "Annie watching Paul with concern."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Annie, watching him, concerned. She glances at her watch.
  EXPRESSION: null
- CHARACTER: Annie
  LINE: Boy, it's like clockwork, the way your pain comes--I'll get you your Novril, Paul. Forgive me for prattling away and making you feel all groggy.
  EXPRESSION: Apologetic
- CHARACTER: Narrator
  LINE: She turns and goes out of the room.
  EXPRESSION: null

::SCENE::
LOCATION: Paul's Room
MOOD: Curious
CHARACTERS: Narrator, Paul, Annie
BACKGROUND_IMAGE: paul_room_curious.png
BACKGROUND_EDIT: "Paul watching Annie as she asks about his new book."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Paul, watching her.
  EXPRESSION: null
- CHARACTER: Annie
  LINE: What's your new book called?
  EXPRESSION: Inquisitive
- CHARACTER: Paul
  LINE: I don’t have a title yet.
  EXPRESSION: Uncertain
- CHARACTER: Annie
  LINE: What's it about?
  EXPRESSION: Curious
- CHARACTER: Paul
  LINE: It’s crazy, but I don’t really know, I mean I haven't written anything but "Misery" for so long that--you read it you can tell me what you think it's about. Maybe you can come up with a title.
  EXPRESSION: Hesitant
- CHARACTER: Annie
  LINE: Oh, like I could do that?
  EXPRESSION: Doubtful

::SCENE::
LOCATION: The Manager's Office at The Silver Creek Lodge
MOOD: Businesslike
CHARACTERS: Narrator, Buster, Libby
BACKGROUND_IMAGE: manager_office.png
BACKGROUND_EDIT: "Small, neat office with snow visible outside the window. Buster and Libby are going over books."

::SCRIPT::
- CHARACTER: Narrator
  LINE: INT. THE MANAGER'S OFFICE AT THE SILVER CREEK LODGE
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Small, neat, one window--outside, snow covers all.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Buster and Libby, the manager, are going over books and records. Libby is an old guy, walks with a cane.
  EXPRESSION: null
- CHARACTER: Libby
  LINE: Nothing unusual about Mr. Sheldon's leaving, Buster--you can tell by the champagne.
  EXPRESSION: Confident
- CHARACTER: Buster
  LINE: Maybe you can, Libby.
  EXPRESSION: Skeptical
- CHARACTER: Libby
  LINE: No, see, he always ordered a bottle of Dom Perignon when he was ready to go. Then he’d pay up and be out the door.
  EXPRESSION: Certain
- CHARACTER: Buster
  LINE: No long-distance phone calls, Federal Express packages--anything at all out of the ordinary?
  EXPRESSION: Inquiring
- CHARACTER: Libby
  LINE: I don't think Mr. Sheldon likes for things to be out of the ordinary. Considering who he is and all, famous and all, he doesn’t have airs. Drives the same car out from New York each time--'65 Mustang--said it helps him think. He was always a good guest, never made a noise, never bothered a soul. Sure hope nothing happened to him.
  EXPRESSION: Thoughtful
- CHARACTER: Narrator
  LINE: (head shake)
  EXPRESSION: null
- CHARACTER: Buster
  LINE: So do I...
  EXPRESSION: Concerned
- CHARACTER: Libby
  LINE: I'll bet that old Mustang’s pulling into New York right now.
  EXPRESSION: Optimistic
- CHARACTER: Buster
  LINE: I'm sure you're right.
  EXPRESSION: Doubtful
- CHARACTER: Narrator
  LINE: But you can tell he's not sure at all as we
  EXPRESSION: null

::SCENE::
LOCATION: Spoon of Soup
MOOD: Foreshadowing
CHARACTERS: Narrator
BACKGROUND_IMAGE: soup_spoon.png
BACKGROUND_EDIT: "Close-up on a spoon filled with beef barley soup."

::SCRIPT::
- CHARACTER: Narrator
  LINE: CUT TO: A SPOON FILLED TO THE BRIM WITH BEEF BARLEY SOUP
  EXPRESSION: null

::SCENE::
LOCATION: Paul's Room
MOOD: Caring
CHARACTERS: Narrator, Paul, Annie
BACKGROUND_IMAGE: paul_room_soup.png
BACKGROUND_EDIT: "Paul in bed, Annie feeding him soup."

::SCRIPT::
- CHARACTER: Narrator
  LINE: INT. PAUL'S ROOM
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: He lies in bed. Sun comes in the lone window. Annie sits on the bed, a large bowl of soup in her hands, feeding him.
  EXPRESSION: null
- CHARACTER: Annie
  LINE: I know I'm only forty pages into your book, but...
  EXPRESSION: Hesitant
- CHARACTER: Narrator
  LINE: She stops, fills the spoon up again.
  EXPRESSION: null
- CHARACTER: Paul
  LINE: But what?
  EXPRESSION: Inquisitive
- CHARACTER: Annie
  LINE: Nothing.
  EXPRESSION: Reserved
- CHARACTER: Paul
  LINE: No, what is it?
  EXPRESSION: Persistent
- CHARACTER: Annie
  LINE: Oh, it's ridiculous, who am I to make a criticism to someone like you?
  EXPRESSION: Self-deprecating
- CHARACTER: Paul
  LINE: I can take it, go ahead.
  EXPRESSION: Encouraging
- CHARACTER: Annie
  LINE: Well, it's brilliantly written, but then everything you write is brilliant.
  EXPRESSION: Admiring
- CHARACTER: Paul
  LINE: Pretty rough so far.
  EXPRESSION: Amused
- CHARACTER: Annie
  LINE: The swearing, Paul. There, I said it.
  EXPRESSION: Bold
- CHARACTER: Paul
  LINE: The profanity bothers you?
  EXPRESSION: Questioning
- CHARACTER: Annie
  LINE: It has no nobility.
  EXPRESSION: Principled
- CHARACTER: Paul
  LINE: Well, these are slum kids, I was a slum kid, everybody talks like that.
  EXPRESSION: Defensive
- CHARACTER: Narrator
  LINE: Annie. She holds the soup bowl in one hand, the muddy-colored beef barley soup close to spilling.
  EXPRESSION: null
- CHARACTER: Annie
  LINE: They do not. What do you think I say when I go to the feed store in town? "Now, Wally, give me a bag of that effing pigfeed and ten pounds of that bitchly cow-corn"--
  EXPRESSION: Sarcastic
- CHARACTER: Narrator
  LINE: Paul is amused by this.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The soup, almost spilling as she gets more agitated.
  EXPRESSION: null
- CHARACTER: Annie
  LINE: --and in the bank do I tell Mrs. Bollinger, "Here’s one big bastard of a check, give me some of your Christing money."
  EXPRESSION: Exasperated
- CHARACTER: Narrator
  LINE: Paul, almost laughing as some soup hits the coverlet.
  EXPRESSION: null
- CHARACTER: Annie
  LINE: There! Look the
  EXPRESSION: Upset

::SCENE::
LOCATION: Room
MOOD: Embarrassment
CHARACTERS: Annie, Paul
BACKGROUND_IMAGE: room.png
BACKGROUND_EDIT: "Interior of a room"

::SCRIPT::
- CHARACTER: Annie
  LINE: See what you made me do!
  EXPRESSION: Angry
- CHARACTER: Narrator
  LINE: Paul--his smile disappears.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Annie, and she is just totally embarrassed.
  EXPRESSION: null
- CHARACTER: Annie
  LINE: Oh, Paul, I'm sorry. I'm so burry. Sometimes I get so worked up. Can you ever forgive me? Here...
  EXPRESSION: Embarrassed
- CHARACTER: Narrator
  LINE: She hands him his pills and starts to clean the soup off the coverlet. Then she makes the sweetest smile.
  EXPRESSION: null
- CHARACTER: Annie
  LINE: I love you, Paul.
  EXPRESSION: Affectionate
- CHARACTER: Narrator
  LINE: (more embarrassed than ever)
  EXPRESSION: null
- CHARACTER: Annie
  LINE: Your mind. Your creativity--that's all I meant.
  EXPRESSION: Flustered
- CHARACTER: Narrator
  LINE: Flustered, she turns away as we--
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue"
  TARGET: mountains_road
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Road in the Mountains
MOOD: Isolation
CHARACTERS: Narrator
BACKGROUND_IMAGE: mountain_road.png
BACKGROUND_EDIT: "A road in the mountains with piles of snow, plowed for driving"

::SCRIPT::
- CHARACTER: Narrator
  LINE: A road in the mountains. Piles of snow all around but it’s been ploughed enough so it’s driveable.
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue"
  TARGET: car_approach
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Road
MOOD: Foreboding
CHARACTERS: Narrator
BACKGROUND_IMAGE: road_sign.png
BACKGROUND_EDIT: "A car approaching a road sign"

::SCRIPT::
- CHARACTER: Narrator
  LINE: A car coming into view. Up ahead is the sign we've already seen: "Curved Road, Next 13 Miles."
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue"
  TARGET: inside_car
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Inside the Car
MOOD: Unease
CHARACTERS: Buster, Virginia
BACKGROUND_IMAGE: car_interior.png
BACKGROUND_EDIT: "Interior of a car with Buster and Virginia"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Buster and his wife Virginia: Virginia is driving while Buster intently studies the terrain. He reaches for a large thermos, pours some coffee, offers it to her. She shakes her head. He begins to sip it.
  EXPRESSION: null
- CHARACTER: Virginia
  LINE: This sure is fun.
  EXPRESSION: Cheerful
- CHARACTER: Narrator
  LINE: She puts her hand on his leg.
  EXPRESSION: null
- CHARACTER: Buster
  LINE: Virginia, when you're in this car, you’re not my wife, you're my deputy.
  EXPRESSION: Stern
- CHARACTER: Virginia
  LINE: Well, this deputy would rather be home under the covers with the Sheriff.
  EXPRESSION: Playful

::PATHS::
- CHOICE: "Continue driving"
  TARGET: car_spin
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: The Car
MOOD: Danger
CHARACTERS: Virginia
BACKGROUND_IMAGE: car_spin.png
BACKGROUND_EDIT: "A car in an icy spin"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The car. Suddenly, it goes into a little icy spin--she fights it back under control.
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue"
  TARGET: inside_car_stop
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Inside the Car
MOOD: Urgency
CHARACTERS: Buster, Virginia
BACKGROUND_IMAGE: car_interior_stop.png
BACKGROUND_EDIT: "Interior of a car, Buster is looking urgent"

::SCRIPT::
- CHARACTER: Buster
  LINE: Stop--stop right here.
  EXPRESSION: Urgent
- CHARACTER: Virginia
  LINE: What? What is it?
  EXPRESSION: Confused

::PATHS::
- CHOICE: "Stop the car"
  TARGET: car_stop
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: The Car
MOOD: Mystery
CHARACTERS: Buster, Virginia
BACKGROUND_IMAGE: car_stopped.png
BACKGROUND_EDIT: "A car skidding to a stop by the side of the road"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The car, skidding, slowing, stopping. Both of them get out, go to the edge of the road. Mountains of snow. Nothing much else visible. Then Buster points.
  EXPRESSION: null
- CHARACTER: Buster
  LINE: Look at that broken branch there...
  EXPRESSION: Observant

::PATHS::
- CHOICE: "Examine the branch"
  TARGET: virginia_unconvinced
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Virginia
MOOD: Skepticism
CHARACTERS: Virginia
BACKGROUND_IMAGE: virginia_skeptical.png
BACKGROUND_EDIT: "Virginia looking at a broken branch, unconvinced"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Virginia, seeing it, unconvinced.
  EXPRESSION: null
- CHARACTER: Virginia
  LINE: Could be the weight of the snow.
  EXPRESSION: Skeptical

::PATHS::
- CHOICE: "Continue investigation"
  TARGET: buster_reasoning
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Buster
MOOD: Analytical
CHARACTERS: Buster
BACKGROUND_IMAGE: buster_reasoning.png
BACKGROUND_EDIT: "Buster analyzing the situation"

::SCRIPT::
- CHARACTER: Buster
  LINE: Could be--or a rotten branch or a mountain lion could have landed on it. Could be a lot of things.
  EXPRESSION: Analytical
- CHARACTER: Narrator
  LINE: He steps off the road, starts down.
  EXPRESSION: null

::PATHS::
- CHOICE: "Follow Buster"
  TARGET: virginia_watching
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Virginia
MOOD: Worry
CHARACTERS: Virginia
BACKGROUND_IMAGE: virginia_watching.png
BACKGROUND_EDIT: "Virginia watching Buster go down a slippery slope, worried"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Virginia, watching him, worried--it's very slippery.
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue watching"
  TARGET: buster_navigating
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Buster
MOOD: Agility
CHARACTERS: Buster
BACKGROUND_IMAGE: buster_navigating.png
BACKGROUND_EDIT: "Buster gracefully navigating down a snowy slope"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Buster, graceful, in great shape, navigating down easily.
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue"
  TARGET: the_tree
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: The Tree
MOOD: Discovery
CHARACTERS: Buster
BACKGROUND_IMAGE: buster_at_tree.png
BACKGROUND_EDIT: "Buster reaching and studying a tree"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The tree that the car ran into. Buster reaches it, studies it.
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue"
  TARGET: virginia_calling
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Virginia
MOOD: Concern
CHARACTERS: Virginia
BACKGROUND_IMAGE: virginia_calling.png
BACKGROUND_EDIT: "Virginia staring out after Buster, concerned"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Virginia, staring out after him--she can't see him because the drop is both too steep and covered with trees and mounds of snow.
  EXPRESSION: null
- CHARACTER: Virginia
  LINE: Anything down there?
  EXPRESSION: Concerned

::PATHS::
- CHOICE: "Wait for a response"
  TARGET: buster_voice
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Buster
MOOD: Discouragement
CHARACTERS: Buster (Voice)
BACKGROUND_IMAGE: buster_voice.png
BACKGROUND_EDIT: "Buster speaking from off-screen"

::SCRIPT::
- CHARACTER: Buster's Voice (O.S.)
  LINE: Yeah. An enormous amount of snow.
  EXPRESSION: Discouraged

::PATHS::
- CHOICE: "Continue searching"
  TARGET: buster_mustang
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Buster
MOOD: Determination
CHARACTERS: Buster
BACKGROUND_IMAGE: buster_moving_snow.png
BACKGROUND_EDIT: "Buster moving through snow towards a buried car"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Buster. He's moved away from the tree now, going toward where the Mustang is buried.
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue"
  TARGET: mustang_buried
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: The Mound of Snow
MOOD: Hidden Danger
CHARACTERS: Narrator
BACKGROUND_IMAGE: mustang_buried.png
BACKGROUND_EDIT: "A mound of snow with a car buried inside"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The mound of snow with the Mustang inside.
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue"
  TARGET: buster_staring
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: The Area
MOOD: Vastness
CHARACTERS: Buster
BACKGROUND_IMAGE: snow_covered_area.png
BACKGROUND_EDIT: "A vast area covered in snow, everything hidden"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Nothing to be seen--everything is covered with mountains of snow. You could have a house down there and not be able to see it. Just glaring white.
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue"
  TARGET: buster_frustrated
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Buster
MOOD: Frustration
CHARACTERS: Buster
BACKGROUND_IMAGE: buster_frustrated.png
BACKGROUND_EDIT: "Buster frustrated, turning around and around"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Buster, angry, frustrated, turning around and around.
  EXPRESSION: Frustrated

::PATHS::
- CHOICE: "Continue"
  TARGET: buster_angle_hidden
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Buster
MOOD: Frustration (cont.)
CHARACTERS: Buster
BACKGROUND_IMAGE: buster_angle_hidden.png
BACKGROUND_EDIT: "Buster from another angle, a part of a car door is visible but out of his sight"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Buster from another angle, from behind the mound with the Mustang inside--and out of his sight, glistening in the sun, a bit of the door protrudes. But, of course, Buster can't see it.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Hold on Buster, in a sour mood, staring around as the edge of the door continues to glisten.
  EXPRESSION: Frustrated

::PATHS::
- CHOICE: "Continue"
  TARGET: virginia_road
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Virginia
MOOD: Impatience
CHARACTERS: Virginia
BACKGROUND_IMAGE: virginia_road.png
BACKGROUND_EDIT: "Virginia on the road as Buster makes his way back up"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Virginia, on the road as Buster makes his way back up, still ticked.
  EXPRESSION: null
- CHARACTER: Virginia
  LINE: You really think Sheldon’s out there?
  EXPRESSION: Skeptical

::PATHS::
- CHOICE: "Get in the car"
  TARGET: another_car
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Road
MOOD: Coincidence
CHARACTERS: Narrator
BACKGROUND_IMAGE: another_car_driving.png
BACKGROUND_EDIT: "Another car driving by on the road"

::SCRIPT::
- CHARACTER: Narrator
  LINE: As they get in the car--another car driving by--it's Annie in her Deep--neither she nor Buster notice each other.
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue"
  TARGET: int_pauls_room_entry
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: INT. PAUL'S ROOM
MOOD: Comfort
CHARACTERS: Annie, Paul
BACKGROUND_IMAGE: pauls_room_entry.png
BACKGROUND_EDIT: "Annie enters Paul's room"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The door opens and Annie enters.
  EXPRESSION: null
- CHARACTER: Annie
  LINE: Oh, I'm sorry. I didn't mean to wake you.
  EXPRESSION: Apologetic
- CHARACTER: Paul
  LINE: It's fine.
  EXPRESSION: Calm

::PATHS::
- CHOICE: "Reveal the book"
  TARGET: reveal_book
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: INT. PAUL'S ROOM
MOOD: Excitement
CHARACTERS: Annie, Paul
BACKGROUND_IMAGE: reveal_book.png
BACKGROUND_EDIT: "Paul's eyes flutter awake to see his novel in Annie's hands"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Pull back to reveal Paul's eyes fluttering awake to see the hardback copy of his novel, Misery's Child, in Annie's hands. She's never been more excited--
  EXPRESSION: null
- CHARACTER: Annie
  LINE: They had it at the store, Paul, there was a whole batch of them there. As soon as I saw it, I slammed my money down. I got the first copy.
  EXPRESSION: Excited

::PATHS::
- CHOICE: "Confirm road status"
  TARGET: confirm_roads
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: INT. PAUL'S ROOM
MOOD: Information
CHARACTERS: Annie, Paul
BACKGROUND_IMAGE: confirm_roads.png
BACKGROUND_EDIT: "Annie providing information about the roads and hospital"

::SCRIPT::
- CHARACTER: Paul
  LINE: Then the roads are open...
  EXPRESSION: Hopeful
- CHARACTER: Annie
  LINE: The one to town is, but that's about it. I called the hospital and talked to the head orthopedic surgeon. I told him who you were and what had happened. He said as long as there's no infection, you’re not in any danger, and as soon as the road to the hospital is open, they'll send an ambulance for you.
  EXPRESSION: Informative

::PATHS::
- CHOICE: "Confirm phone status"
  TARGET: confirm_phones
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: INT. PAUL'S ROOM
MOOD: Reassurance
CHARACTERS: Annie, Paul
BACKGROUND_IMAGE: confirm_phones.png
BACKGROUND_EDIT: "Annie confirming phone status"

::SCRIPT::
- CHARACTER: Paul
  LINE: The phones are working?
  EXPRESSION: Questioning
- CHARACTER: Annie
  LINE: Well, mine’s still out. But the ones in town were working just fine. I called that agent of yours.
  EXPRESSION: Informative
- CHARACTER: Narrator
  LINE: (soft now)
  EXPRESSION: null
- CHARACTER: Annie
  LINE: Oh, Paul, I peeked at the very beginning.
  EXPRESSION: Tender
- CHARACTER: Narrator
  LINE: (looks at him)
  EXPRESSION: null
- CHARACTER: Annie
  LINE: What a wonderful first page--just to read the name Misery Chastain...
  EXPRESSION: Emotional

::PATHS::
- CHOICE: "Express concern for daughter"
  TARGET: paul_daughter
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: INT. PAUL'S ROOM
MOOD: Reflection
CHARACTERS: Annie, Paul
BACKGROUND_IMAGE: paul_daughter.png
BACKGROUND_EDIT: "Paul reflecting on his daughter"

::SCRIPT::
- CHARACTER: Paul
  LINE: My daughter must be going nuts.
  EXPRESSION: Worried

::PATHS::
- CHOICE: "Continue"
  TARGET: annie_agent
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: INT. PAUL'S ROOM
MOOD: Comfort
CHARACTERS: Annie, Paul
BACKGROUND_IMAGE: annie_agent.png
BACKGROUND_EDIT: "Annie relaying information from Paul's agent"

::SCRIPT::
- CHARACTER: Annie
  LINE: ...it's like a visit from my oldest, dearest friend.
  EXPRESSION: Nostalgic
- CHARACTER: Paul
  LINE: I was supposed to be home for her birthday three days ago.
  EXPRESSION: Regretful
- CHARACTER: Annie
  LINE: Your agent said she would tell her you were okay. But I'm afraid you'll have to wait until tomorrow if you want to speak to her yourself.
  EXPRESSION: Gentle

::PATHS::
- CHOICE: "Leave the room"
  TARGET: annie_leaves
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: INT. PAUL'S ROOM
MOOD: Admiration
CHARACTERS: Annie, Paul
BACKGROUND_IMAGE: annie_leaves.png
BACKGROUND_EDIT: "Annie stops at the door, looking at Paul with amazement"

::SCRIPT::
- CHARACTER: Narrator
  LINE: She starts to leave, stops at the door.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: (She looks at him now with almost a look of amazement)
  EXPRESSION: null
- CHARACTER: Annie
  LINE: Oh, Paul, what a poet you are...
  EXPRESSION: Admiring

::PATHS::
- CHOICE: "Continue"
  TARGET: paul_tray
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: INT. PAUL'S ROOM
MOOD: Care
CHARACTERS: Annie, Paul
BACKGROUND_IMAGE: paul_tray.png
BACKGROUND_EDIT: "Paul watching Annie enter with a tray"

::SCRIPT::
- CHARACTER: Narrator
  LINE: As she leaves--dissolve to: Paul, watching as she enters, moves to him, carrying a tray.
  EXPRESSION: null
- CHARACTER: Annie
  LINE: I made you my specialty--scrambled eggs a la Wilkes. And I'm on page 75.
  EXPRESSION: Caring

::PATHS::
- CHOICE: "Accept the food"
  TARGET: paul_eats
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: INT. PAUL'S ROOM
MOOD: Approval
CHARACTERS: Annie, Paul
BACKGROUND_IMAGE: paul_eats.png
BACKGROUND_EDIT: "Paul starting to eat the eggs with effort"

::SCRIPT::
- CHARACTER: Paul
  LINE: I guess that means it's okay.
  EXPRESSION: Mildly Amused
- CHARACTER: Annie
  LINE: No. No, it isn't, it’s--oh pooh, I can't think of any words. Would "great" be insulting?
  EXPRESSION: Hesitant
- CHARACTER: Paul
  LINE: I can live with "great."
  EXPRESSION: Resigned
- CHARACTER: Narrator
  LINE: He starts, with effort, to eat.
  EXPRESSION: null
- CHARACTER: Annie
  LINE: No, it's not just great, it's perfect, a perfect, perfect thing.
  EXPRESSION: Enthusiastic

::PATHS::
- CHOICE: "Continue"
  TARGET: int_pauls_room_mid_afternoon
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: INT. PAUL'S ROOM - MID-AFTERNOON
MOOD: Admiration
CHARACTERS: Annie, Paul
BACKGROUND_IMAGE: pauls_room_mid_afternoon.png
BACKGROUND_EDIT: "Annie clearing Paul's tray and asking for autograph"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Annie is clearing Paul’s tray. She hands him his Novril; he quickly swallows them.
  EXPRESSION: null
- CHARACTER: Annie
  LINE: I'm up to page 185. I always get sad when I pass the halfway point. Will you do me a favor? I'd love it if you would autograph my copy. I already have your autograph on a picture, but it would mean so much to me to get it in person. I know you're right-handed, so don't worry if it's not so legible. I'll cherish it anyway.
  EXPRESSION: Eager
- CHARACTER: Narrator
  LINE: As Paul signs the book:
  EXPRESSION: null
- CHARACTER: Annie
  LINE: I don't mean to pry, but I've read in two magazines now where you were seeing this model who does those disgusting jeans commercials. And I said it can'
  EXPRESSION: Curious

::PATHS::
- CHOICE: "Continue"
  TARGET: end
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Paul’s Room
MOOD: Tense
CHARACTERS: Narrator, Paul, Annie
BACKGROUND_IMAGE: paul_room.png
BACKGROUND_EDIT: "Late afternoon sunlight through a window"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Paul Sheldon would never waste his time with a trampy woman like that.
  EXPRESSION: null
- CHARACTER: Paul
  LINE: Well, you can't believe everything you read in magazines.
  EXPRESSION: null
- CHARACTER: Annie
  LINE: I knew it. I knew it wasn't true. Boy, how do they get away with printing stuff like that?
  EXPRESSION: null
- CHARACTER: Paul
  LINE: You'd be amazed at what some people will believe.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: He finishes the autograph, hands the book back to her.
  EXPRESSION: null
- CHARACTER: Annie
  LINE: Thank you so much.
  EXPRESSION: Happy
- CHARACTER: Paul
  LINE: My pleasure.
  EXPRESSION: null

::PATHS::
- CHOICE: "Dissolve to next scene"
  TARGET: paul_room_window
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Paul’s Room - The Window
MOOD: Surreal
CHARACTERS: Narrator, Paul, Annie, Pig
BACKGROUND_IMAGE: paul_room_window.png
BACKGROUND_EDIT: "Late afternoon sunlight, room interior"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The door. It opens and guess what--a sow lumbers in.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Paul, kind of stunned as this female pig skitters its way around the room, excited, confused, slipping and sliding.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Annie, all smiles and happiness, laughing in the doorway.
  EXPRESSION: null
- CHARACTER: Annie
  LINE: I thought it was time you two should meet. Paul, say hello to my favorite beast in all the world, my sow, Misery.
  EXPRESSION: Happy
- CHARACTER: Paul
  LINE: Misery?
  EXPRESSION: Confused
- CHARACTER: Narrator
  LINE: The pig, snorting around the room.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Paul and Annie, watching it.
  EXPRESSION: null
- CHARACTER: Annie
  LINE: Yes. I told you I was your number-one fan.
  EXPRESSION: Happy
- CHARACTER: Paul
  LINE: I'm getting to believe you.
  EXPRESSION: Skeptical
- CHARACTER: Annie
  LINE: This farm was getting kind of dreary, what with just the few cows and chickens and me-- But when I got Misery here, everything Changed--she just makes me smile so.
  EXPRESSION: Happy
- CHARACTER: Paul
  LINE: She’s a fine... uh... pig is what she is...
  EXPRESSION: Awkward
- CHARACTER: Annie
  LINE: I'm on page three-hundred now, Paul, and it's better than perfect--it's divine. What's the ceiling that dago painted?
  EXPRESSION: Excited
- CHARACTER: Paul
  LINE: The Sistine Chapel?
  EXPRESSION: Thoughtful
- CHARACTER: Annie
  LINE: Yeah, that and Misery's Child-- those are the only two divine things ever in this world...
  EXPRESSION: Ecstatic
- CHARACTER: Narrator
  LINE: Paul watches as the pig skitters out of the room with Annie in pursuit, happily imitating the pig.
  EXPRESSION: null
- CHARACTER: Annie
  LINE: Woink! Whoink! Whuh-Whuh-WHOINK!
  EXPRESSION: Playful
- CHARACTER: Narrator
  LINE: Paul staring after them--what the hell was that?
  EXPRESSION: Confused

::PATHS::
- CHOICE: "Cut to window at dusk"
  TARGET: window_dusk
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: The Window - Dusk
MOOD: Introspective
CHARACTERS: Narrator, Annie, Paul
BACKGROUND_IMAGE: window_dusk.png
BACKGROUND_EDIT: "Dusk light, room interior"

::SCRIPT::
- CHARACTER: Annie
  LINE: When my husband left me... I wasn't prepared, it wasn’t an easy time...
  EXPRESSION: Sad
- CHARACTER: Narrator
  LINE: Pull back to reveal Annie, standing at the window, her back to the room.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: In bed, Paul is dealing with a bedpan, peeing.
  EXPRESSION: null
- CHARACTER: Annie
  LINE: For a while I thought I might go crazy.
  EXPRESSION: Desperate
- CHARACTER: Paul
  LINE: I know how that can be.
  EXPRESSION: Sympathetic
- CHARACTER: Annie
  LINE: I don't know about you, but what I did to get through it was I dove into work--days, nights--night shifts can be lonely at a hospital. I did a lot of reading. That was hen I first discovered Misery. She made me so happy. She made me forget all my problems. 'Course, I suppose you had a little something to do with that too.
  EXPRESSION: Reflective
- CHARACTER: Narrator
  LINE: There is a peeing sound.
  EXPRESSION: null
- CHARACTER: Paul
  LINE: Yeah, well...
  EXPRESSION: Embarrassed
- CHARACTER: Annie
  LINE: I just kept reading them over and over. I know when I finish this one-- and I've only got two chapters to go-- I'll just turn right to the front page and start reading it again.
  EXPRESSION: Devoted
- CHARACTER: Paul
  LINE: I'm...
  EXPRESSION: Interrupted
- CHARACTER: Annie
  LINE: Done?
  EXPRESSION: Inquiring
- CHARACTER: Paul
  LINE: Yeah, thanks.
  EXPRESSION: Relieved
- CHARACTER: Annie
  LINE: No problem.
  EXPRESSION: Helpful
- CHARACTER: Narrator
  LINE: As she takes the bedpan...
  EXPRESSION: null
- CHARACTER: Annie
  LINE: Don’t get me wrong. I'm not against marriage per se. But it would take a pretty special guy to make me want to go down the aisle again.
  EXPRESSION: Thoughtful
- CHARACTER: Paul
  LINE: Well, it's not something you should enter into lightly.
  EXPRESSION: Cautious
- CHARACTER: Annie
  LINE: It boils down to respect. People just don't respect the institution of marriage any more. They have no sense of real commitment.
  EXPRESSION: Disappointed

::PATHS::
- CHOICE: "Cut to Paul attempting to smile"
  TARGET: paul_attempting_smile
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Annie’s Speech
MOOD: Tense anticipation
CHARACTERS: Narrator, Annie, Paul
BACKGROUND_IMAGE: annie_speech.png
BACKGROUND_EDIT: "Close up on Annie, room interior"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Paul, attempting to smile. There is not much he can say to this.
  EXPRESSION: Resigned
- CHARACTER: Annie
  LINE: I'd love to stay here and chat, but I'm right at the end and I gotta find out what happens.
  EXPRESSION: Eager
- CHARACTER: Paul
  LINE: Well, I hope you like it.
  EXPRESSION: Hopeful
- CHARACTER: Annie
  LINE: Of course I'll like it. Misery's about to have her child. What's it gonna be, a boy or a girl? Ooh, don't tell me.
  EXPRESSION: Excited
- CHARACTER: Narrator
  LINE: With that, she exits.
  EXPRESSION: null

::PATHS::
- CHOICE: "Cut to window at moonlight"
  TARGET: window_moonlight
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: The Window - Moonlight
MOOD: Ominous
CHARACTERS: Narrator, Paul, Annie
BACKGROUND_IMAGE: window_moonlight.png
BACKGROUND_EDIT: "Moonlight through the window"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Paul. He's been dozing but now his eyes flutter awake as we
  EXPRESSION: null

::PATHS::
- CHOICE: "Cut to the door opening"
  TARGET: door_opens_moonlight
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Paul’s Room - Moonlight
MOOD: Terrified
CHARACTERS: Narrator, Paul, Annie
BACKGROUND_IMAGE: paul_room_moonlight.png
BACKGROUND_EDIT: "Moonlight, room interior"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The door. It opens and Annie enters, comes to his bedside.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Paul. Hard to see. He squints up as we
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Annie. Close up: her face is ashen pale.
  EXPRESSION: null
- CHARACTER: Annie
  LINE: You...you dirty bird. She can’t be dead. Misery Chastain cannot be dead! How could you?
  EXPRESSION: Horrified
- CHARACTER: Paul
  LINE: Annie, in 1871, women often died in childbirth, but her spirit is the important thing, and Misery's spirit is still alive--
  EXPRESSION: Pleading
- CHARACTER: Annie
  LINE: I DON'T WANT HER SPIRIT! I want HER! And you MURDERED her!
  EXPRESSION: Screaming
- CHARACTER: Paul
  LINE: I DIDN'T...
  EXPRESSION: Defending
- CHARACTER: Annie
  LINE: Then who did?
  EXPRESSION: Demanding
- CHARACTER: Paul
  LINE: No one--she just died--she slipped away, that's all.
  EXPRESSION: Resigned
- CHARACTER: Annie
  LINE: She slipped away? She slipped away? She didn't just slip away. You did it. You did it. You did it. You did it. You murdered my Misery.
  EXPRESSION: Manic
- CHARACTER: Narrator
  LINE: And now she has lifted a chair--it's heavy but she's very strong--and she raises it and turns on Paul, and it's high above her head, and haul realizes that this might be it, she might shatter him with it, crunch his skull--and that's just what she seems she's about to do--and then she swings it, not against him but against the wall, and it shatters and she's panting from the effort as she turns on him again, her voice surprisingly soft.
  EXPRESSION: Violent
- CHARACTER: Annie
  LINE: I thought you were good, Paul, but you’re not good, you're just another lying old dirty birdie and I don't think I better be around you for awhile. And don't even think about anybody coming for you, not the doctors, not your agent, not your family--because I never called them. Nobody knows you're here. And you better hope nothing happens to me because if I die, you die.
  EXPRESSION: Threatening

::PATHS::
- CHOICE: "Cut to Paul watching Annie leave"
  TARGET: paul_watching_annie_leave
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Paul’s Room - After Annie Leaves
MOOD: Desperate
CHARACTERS: Narrator, Paul
BACKGROUND_IMAGE: paul_room_after_annie.png
BACKGROUND_EDIT: "Dimly lit room, Paul in bed"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Paul, watching as she closes the door behind her. Then there is a rattle of a key and the sound of the door to his room locking.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Annie, getting in her Cherokee and gunning away.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The room.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Paul lies still. He looks around the room and listens for sounds. All he hears are the sounds of a winter night in the mountains. After a few beats, he takes a deep breath and then begins his greatest effort of all: to force his body out of bed, to make it move. He’s still weak from what he’s endured, but that’s not the main thing: it’s the pain. Any attempt at movement and his legs scream. He sags back, lies there still a moment.
  EXPRESSION: Determined but in pain

::PATHS::
- CHOICE: "End of excerpt"
  TARGET: end
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Paul's Room
MOOD: Painful Struggle
CHARACTERS: Paul
BACKGROUND_IMAGE: paul_room_struggle.png
BACKGROUND_EDIT: "Paul in bed, trying to get up"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Slowly he tries to maneuver his body off the bed. He rolls over onto his stomach, then tries to lower himself onto the floor by moving down head first.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: His good arm hits the floor, and he is able to hold himself up but, realizing there is no way to get out of bed without causing tremendous pain, he girds himself and flings himself out of bed and comes crashing to the floor.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The pain is excruciating. After he regains his composure, he slowly crawls toward the door.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: He reaches up and tries the handle, it is, in fact, locked.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: He awkwardly tries to slam up against the door, but it is much too painful and to no avail. He crawls back over to the bed, realizes there’s no way to climb back in, then grabs the blanket from the bed, wraps it around himself, and closes his eyes.
  EXPRESSION: null

::PATHS::
- CHOICE: "Dissolve to Buster's Office"
  TARGET: busters_office
  STATE_CHANGE: pain = +5
  CONDITION: null

::SCENE::
LOCATION: Buster's Office
MOOD: Somber Investigation
CHARACTERS: Buster, Virginia, Marcia Sindell (voice)
BACKGROUND_IMAGE: busters_office.png
BACKGROUND_EDIT: "Buster at his desk, newspaper open"

::SCRIPT::
- CHARACTER: Narrator
  LINE: He sits alone at his desk on the telephone, staring at the Rocky Mountain Gazette spread in front of him.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: In a prominent spot on the top is what is most likely a book­ jacket photo of Paul. Above the picture is the following: "HAVE YOU SEEN PAUL SHELDON?"
  EXPRESSION: null
- CHARACTER: Buster
  LINE: No, Ms. Sindell, there’s no point in coming up here now. Everything that can be done is... Yes, we’re working closely with the state police, and the FBI has been informed. Right... Right... As soon as we know anything we'll let you know. No, it's no bother. Call anytime. Bye, Ms. Sindell.
  EXPRESSION: Professional but concerned
- CHARACTER: Virginia
  LINE: Here’s the list of all Sheldon's credit charges. Nothing after the Silver Creek.
  EXPRESSION: Informative
- CHARACTER: Virginia
  LINE: Any calls?
  EXPRESSION: Inquiring
- CHARACTER: Buster
  LINE: Just from his agent.
  EXPRESSION: Resigned

::PATHS::
- CHOICE: "Continue conversation with Virginia"
  TARGET: buster_virginia_interaction
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Buster's Office (Interaction)
MOOD: Tense Silence
CHARACTERS: Buster, Virginia
BACKGROUND_IMAGE: busters_office_interaction.png
BACKGROUND_EDIT: "Buster and Virginia, newspaper visible"

::SCRIPT::
- CHARACTER: Narrator
  LINE: His eyes flick up to her. An almost imperceptible shake of the head.
  EXPRESSION: null

::PATHS::
- CHOICE: "Hold for a moment, then transition to distorted faces"
  TARGET: distorted_faces
  STATE_CHANGE: suspense = +2
  CONDITION: null

::SCENE::
LOCATION: Abstract Soundscape
MOOD: Unsettling Adulation
CHARACTERS: Distorted Faces, Voices (Annie)
BACKGROUND_IMAGE: distorted_faces_voices.png
BACKGROUND_EDIT: "Rapidly changing, distorted faces with overlapping voices"

::SCRIPT::
- CHARACTER: Narrator
  LINE: FACES. They are distorted, and they come into view but briefly, then change into the next distorted face. All kinds--there is no order to them--young, Oriental, female, male, pretty, sad, black, not so pretty, happy, white, old--what we HEAR is this:
  EXPRESSION: null
- CHARACTER: Voice
  LINE: "...You've changed my life..."
  EXPRESSION: Fanatic
- CHARACTER: Voice
  LINE: "...I'm your number one fan..."
  EXPRESSION: Fanatic
- CHARACTER: Voice
  LINE: "...I'm a really big fan of yours..."
  EXPRESSION: Fanatic
- CHARACTER: Voice
  LINE: "...I’m your biggest fan..."
  EXPRESSION: Fanatic
- CHARACTER: Voice
  LINE: "...Don’t ever stop writing those Misery books..."
  EXPRESSION: Fanatic
- CHARACTER: Voice
  LINE: "...I’ve read all your books, but the Misery's... well..."
  EXPRESSION: Fanatic
- CHARACTER: Voice
  LINE: "...I'm your number one fan..."
  EXPRESSION: Fanatic
- CHARACTER: Voice
  LINE: "...You've given me such pleasure..."
  EXPRESSION: Fanatic
- CHARACTER: Voice
  LINE: "...I feel like you're writing just for me..."
  EXPRESSION: Fanatic
- CHARACTER: Narrator
  LINE: And now, it gets kicked up in speed and all goes faster, many times overlapping.
  EXPRESSION: null
- CHARACTER: Voice
  LINE: "...I love you... I’m your number one fan... I’m your biggest fan... We love you... number one... love you... biggest... love you... number one... number one... you poor dear thing..."
  EXPRESSION: Fanatic, increasing intensity
- CHARACTER: Annie
  LINE: "...you poor dear thing..."
  EXPRESSION: Affectionate, out of focus

::PATHS::
- CHOICE: "Focus on Annie and the room"
  TARGET: annie_and_paul_room
  STATE_CHANGE: tension = +3
  CONDITION: null

::SCENE::
LOCATION: The Room
MOOD: Confrontational Dusk
CHARACTERS: Annie, Paul
BACKGROUND_IMAGE: the_room_dusk.png
BACKGROUND_EDIT: "The room in dusk, Annie by the bed, Paul in bed"

::SCRIPT::
- CHARACTER: Narrator
  LINE: This last was said by Annie, out of focus, and for a moment, she stays that way--
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: CUT TO: THE ROOM, AS IT SNAPS BACK INTO FOCUS--ANNIE is standing by the bed. It is dusk.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: She wears a dark blue dress and a hat with a sprig of flowers.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Her eyes are bright and vivacious--the fact is, this is the prettiest ANNIE WILKES has ever looked.
  EXPRESSION: null
- CHARACTER: Annie
  LINE: What are you doing on the floor?
  EXPRESSION: Concerned, yet slightly accusatory
- CHARACTER: Annie
  LINE: It’s my fault. If I'd had a proper hospital bed, this never would have happened. Here, let me help you back in.
  EXPRESSION: Apologetic, solicitous
- CHARACTER: Narrator
  LINE: (She lifts him back into the bed, which causes considerable pain)
  EXPRESSION: null
- CHARACTER: Annie
  LINE: I know this hurts, but it’ll only take a few seconds. There you go. Comfy?
  EXPRESSION: Reassuring, but with underlying control
- CHARACTER: Paul
  LINE: Perfect.
  EXPRESSION: Sarcastic, in pain
- CHARACTER: Annie
  LINE: You're such a kidder. I have a big surprise for you. But first there's something you must do.
  EXPRESSION: Playful, yet firm
- CHARACTER: Paul
  LINE: I don't suppose I could have a little snack while I wait for the surprise?
  EXPRESSION: Weak attempt at humor
- CHARACTER: Annie
  LINE: I'll get you everything you want, but you must listen first. Sometimes my thinking is a little muddy, I accept that. It's why I couldn't remember all those things they were asking me on the witness stand in Denver.
  EXPRESSION: Frank, slightly defensive
- CHARACTER: Narrator
  LINE: Now she turns, goes to the doorway, keeping on talking. She is never out of sight.
  EXPRESSION: null
- CHARACTER: Annie
  LINE: But this time I thought clearly. I asked God about you and God said "I delivered him unto you so that you may show him the way."
  EXPRESSION: Zealous, devout
- CHARACTER: Paul
  LINE: Show me the way?
  EXPRESSION: Confused
- CHARACTER: Annie
  LINE: Yes.
  EXPRESSION: Affirmative
- CHARACTER: Narrator
  LINE: She exits and re-enters wheeling something toward his bed. It's a charcoal barbecue, the kind you use in summer for cooking hamburgers. She holds several items in her arms: a box of Diamond Blue Tip wooden matches, a can of lighter fluid. And most noticeably, Paul's manuscript.
  EXPRESSION: null

::PATHS::
- CHOICE: "Witness the manuscript in the barbecue"
  TARGET: manuscript_barbecue
  STATE_CHANGE: dread = +4
  CONDITION: null

::SCENE::
LOCATION: Annie and Paul
MOOD: Impending Destruction
CHARACTERS: Annie, Paul
BACKGROUND_IMAGE: annie_paul_manuscript.png
BACKGROUND_EDIT: "Annie setting up a barbecue with Paul's manuscript on it"

::SCRIPT::
- CHARACTER: Narrator
  LINE: CUT TO: ANNIE AND PAUL. He watches, mute, as she takes off the grill, puts the manuscript into the barbecue itself where the charcoal goes, spritzes it with lighter fluid. The grill is close enough to the bed for him to reach out and drop a match.
  EXPRESSION: null
- CHARACTER: Paul
  LINE: When I mentioned a snack, I was thinking more along the lines of a cheese and crackers kind of thing.
  EXPRESSION: Dry humor, a plea
- CHARACTER: Narrator
  LINE: CUT TO: ANNIE, looking at him.
  EXPRESSION: null
- CHARACTER: Annie
  LINE: Paul, this is no time for jokes. You must rid the world of this filth.
  EXPRESSION: Stern, uncompromising
- CHARACTER: Narrator
  LINE: She hands him the box of kitchen matches.
  EXPRESSION: null
- CHARACTER: Paul
  LINE: You want me to burn my book?
  EXPRESSION: Disbelieving
- CHARACTER: Annie
  LINE: Yes.
  EXPRESSION: Firm
- CHARACTER: Paul
  LINE: You want me to burn my book?
  EXPRESSION: Stunned disbelief
- CHARACTER: Annie
  LINE: I know this may be difficult for you, but it's for the best.
  EXPRESSION: Patronizing
- CHARACTER: Paul
  LINE: This isn't difficult, my agent's made dozens of copies. There's gonna be an auction on this, and every publishing house in New York is reading it now. So if you want me to burn it, fine. You're not ridding the world of anything.
  EXPRESSION: Defiant, with a hint of desperation
- CHARACTER: Narrator
  LINE: CUT TO: ANNIE, watching him.
  EXPRESSION: null
- CHARACTER: Annie
  LINE: Then light the match, Paul.
  EXPRESSION: Quietly insistent
- CHARACTER: Paul
  LINE: No big deal.
  EXPRESSION: Feigned indifference
- CHARACTER: Annie
  LINE: So you've indicated. Do it.
  EXPRESSION: Commanding
- CHARACTER: Narrator
  LINE: CUT TO: THE MATCHES. PAUL'S HANDS are starting to tremble now. He can't do it.
  EXPRESSION: null
- CHARACTER: Annie
  LINE: I know this is the only copy, Paul. When you were twenty-four you wrote your first book and you didn't make a copy, because you didn’t think anybody would take it seriously. But they did. And ever since you've never made any copies because you're superstitious--it's why you always come back to the Silver Creek Lodge. You told that story to Merv Griffin eleven years ago.
  EXPRESSION: Manipulative, taunting
- CHARACTER: Paul
  LINE: You know, Annie, this book never would have survived w
  EXPRESSION: Interrupted, defeated

::PATHS::
- CHOICE: "Annie's reaction to Paul's statement"
  TARGET: annie_reaction_to_statement
  STATE_CHANGE: fear = +5, despair = +5
  CONDITION: null

::SCENE::
LOCATION: Not Specified
MOOD: Intense
CHARACTERS: Narrator, Annie, Paul
BACKGROUND_IMAGE: null
BACKGROUND_EDIT: null

::SCRIPT::
- CHARACTER: Narrator
  LINE: Without you. When it gets to New York, there will be a big auction, and whatever it brings we can split. God knows you're entitled to it.
  EXPRESSION: null
- CHARACTER: Annie
  LINE: Oh, Paul. This isn't about money. It's about decency and purity. It's about God's values.
  EXPRESSION: Earnest
- CHARACTER: Paul
  LINE: You're right. You're right. I don't know what I was thinking. I'll tell you what. It doesn't have to be published. Nobody ever has to see it. I’ll just keep it for myself. No one will ever have to know it exists.
  EXPRESSION: Resigned
- CHARACTER: Annie
  LINE: Can't you see it's what God wants?
  EXPRESSION: Pious
- CHARACTER: Narrator
  LINE: She's holding the can of lighter fluid in her hand as she speaks and absentmindedly flicks a few drops of the fluid on the bed.
  EXPRESSION: null
- CHARACTER: Annie
  LINE: You’re so brilliant. I would think you'd certainly be able to see that. We're put on this earth to help people, Paul. Like I'm trying to help you.
  EXPRESSION: Pious
- CHARACTER: Narrator
  LINE: More drops fall on the bed.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Paul watches as the fluid continues to drop on the bed.
  EXPRESSION: null
- CHARACTER: Annie
  LINE: Please let me help you.
  EXPRESSION: Pious

::PATHS::
- CHOICE: Continue
  TARGET: paul_strikes_match
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Not Specified
MOOD: Tense
CHARACTERS: Paul, Annie
BACKGROUND_IMAGE: null
BACKGROUND_EDIT: null

::SCRIPT::
- CHARACTER: Narrator
  LINE: Paul. His hands shaking. Almost robot-like, he strikes one. It flames.
  EXPRESSION: Tense
- CHARACTER: Annie
  LINE: You’re doing the right thing, Paul.

::PATHS::
- CHOICE: Continue
  TARGET: barbecue_fire
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: The Barbecue
MOOD: Explosive
CHARACTERS: Narrator, Paul, Annie
BACKGROUND_IMAGE: null
BACKGROUND_EDIT: null

::SCRIPT::
- CHARACTER: Narrator
  LINE: The barbecue, as Paul's hand appears, drops the match on the fluid-soaked manuscript. For a moment--nothing-- --and then, KABOOM, the goddamn thing practically explodes and
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Paul, staring, dazed, and as the flames leap higher,
  EXPRESSION: Dazed
- CHARACTER: Narrator
  LINE: Annie, suddenly scared and startled at the heat and the size of the flames and the full baking heat and
  EXPRESSION: Scared
- CHARACTER: Annie
  LINE: Goodness!
  EXPRESSION: Startled
- CHARACTER: Narrator
  LINE: The barbecue. The sound is louder as the flames leap up and now charred bits of paper begin floating upward and
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Annie, watching, as more bits of paper rise.
  EXPRESSION: null
- CHARACTER: Annie
  LINE: Goodness--Goodness--Oh, my gracious--
  EXPRESSION: Alarmed
- CHARACTER: Narrator
  LINE: And she starts trying to catch them.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: A piece of burning paper in midair, floating against the gauzy curtain, and for a moment it looks like the curtain will catch fire and
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Annie, panicked, racing out of the room, going "Goodness, heaves to Betsy"--
  EXPRESSION: Panicked
- CHARACTER: Narrator
  LINE: The barbecue, and what's left of the book.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Paul, and he cannot take his eyes off the disaster.
  EXPRESSION: Transfixed

::PATHS::
- CHOICE: Continue
  TARGET: barbecue_water
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: The Barbecue
MOOD: Chaotic
CHARACTERS: Narrator, Annie, Paul
BACKGROUND_IMAGE: null
BACKGROUND_EDIT: null

::SCRIPT::
- CHARACTER: Narrator
  LINE: Annie, hurrying back in, carrying a big bucket, slopping water as she lifts the bucket.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The last of the manuscript as the bucket of water is tossed onto it--there's hissing and steam and as the steam clears it all looks now like a log in a brackish pond.
  EXPRESSION: null
- CHARACTER: Annie
  LINE: Well, isn't that an oogy mess?
  EXPRESSION: Disgusted
- CHARACTER: Narrator
  LINE: As she starts to wheel the barbecue out, suddenly there is a new and different sound as we
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Paul, head turning toward the window.
  EXPRESSION: Alert
- CHARACTER: Narrator
  LINE: Annie taking a step toward the window, stopping for a moment. The sound we're hearing is a motor. A helicopter motor. And it's getting louder. Annie goes to the window now, looks toward the sky as we
  EXPRESSION: Curious
- CHARACTER: Narrator
  LINE: A helicopter flying along.
  EXPRESSION: null

::PATHS::
- CHOICE: Continue
  TARGET: helicopter_interior
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Inside the Helicopter
MOOD: Investigative
CHARACTERS: Narrator, Buster, Pilot
BACKGROUND_IMAGE: null
BACKGROUND_EDIT: null

::SCRIPT::
- CHARACTER: Narrator
  LINE: Buster and a Pilot are in the machine. Buster has a pair of binoculars looped around his neck, a map rumpled in his lap.
  EXPRESSION: null
- CHARACTER: Buster
  LINE: I hat’s the bteadman place up there. The only other place up here is the Wilkes farm.
  EXPRESSION: Pointing
- CHARACTER: Narrator
  LINE: The pilot nods. Buster points again.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Another nod. The Pilot points down. Buster stares through the binoculars.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: What he sees: Annie's Jeep parked in front of her house.
  EXPRESSION: null
- CHARACTER: Buster
  LINE: That's no '65 Mustang. There's nothing else out this way--circle on back.
  EXPRESSION: Decisive
- CHARACTER: Narrator
  LINE: As the pilot starts to change direction
  EXPRESSION: null

::PATHS::
- CHOICE: Continue
  TARGET: annie_watches_helicopter
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Not Specified
MOOD: Wistful
CHARACTERS: Narrator, Annie, Paul
BACKGROUND_IMAGE: null
BACKGROUND_EDIT: null

::SCRIPT::
- CHARACTER: Narrator
  LINE: Annie at the window, watching, as the helicopter turns, starts off.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Paul, listening as the motor sound recedes.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Annie, staring out the window.
  EXPRESSION: null
- CHARACTER: Annie
  LINE: I do believe the winters are getting shorter and shorter every year. People say it has something to do with the ozone layer. What do you think?
  EXPRESSION: Contemplative
- CHARACTER: Paul
  LINE: I don't know.
  EXPRESSION: Indifferent
- CHARACTER: Annie
  LINE: Yeah, well, it's a theory. Here's your Novril. How does tuna casserole sound for dinner?
  EXPRESSION: Casual
- CHARACTER: Paul
  LINE: Great.
  EXPRESSION: Indifferent
- CHARACTER: Narrator
  LINE: She exits. Paul takes the two Novril, stares at them, then deliberately tucks them under his mattress.

::PATHS::
- CHOICE: Continue
  TARGET: paul_room_night
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Paul's Room - Night
MOOD: Mundane
CHARACTERS: Narrator, Paul
BACKGROUND_IMAGE: null
BACKGROUND_EDIT: null

::SCRIPT::
- CHARACTER: Narrator
  LINE: As Paul is finishing the last of his tuna casserole. There are two Novrils on his tray. We hear strains of TV game show theme music. These sounds are not surprising. Paul has heard them before.
  EXPRESSION: null

::PATHS::
- CHOICE: Continue
  TARGET: annie_room_night
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Annie's Room - Night
MOOD: Obsessive
CHARACTERS: Narrator, Annie, Paul
BACKGROUND_IMAGE: null
BACKGROUND_EDIT: null

::SCRIPT::
- CHARACTER: Narrator
  LINE: It is much smaller than Paul's and filled with religious bric-a-brac, pictures of Paul Sheldon, and a TV on a portable stand. Annie lies in bed, with an open bag of Cheetos resting on her stomach and a big quart-sized plastic bottle of Coke on the nightstand. As she munches away, she is heavily engrossed in her favorite TV show, "The Love Connection." As Chuck Woolery extracts the embarrassing details of a couple's romantic interlude, we
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Paul faintly hearing the sounds of the TV. He has now finished eating. He takes the two Novril from under the mattress. He then undoes the sheet, takes his fork and delicately pokes a hole in the mattress, then stuffs all four pills back into the hole.
  EXPRESSION: null

::PATHS::
- CHOICE: Continue
  TARGET: farmhouse_dawn
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Farmhouse
MOOD: Anticipatory
CHARACTERS: Narrator, Paul, Annie
BACKGROUND_IMAGE: null
BACKGROUND_EDIT: null

::SCRIPT::
- CHARACTER: Narrator
  LINE: Coming up to dawn.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Paul's door slowly opening.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Paul, staring at the door.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Wheels, seen from underneath the bed, being rolled around the foot of the bed. We realize Paul is in a wheelchair with Annie pushing him.
  EXPRESSION: null
- CHARACTER: Annie
  LINE: See, isn't this nice?
  EXPRESSION: Cheerful
- CHARACTER: Paul
  LINE: Great. I've always wanted to visit the other side of the room.
  EXPRESSION: Sarcastic
- CHARACTER: Annie
  LINE: And look what I've got for you. An electric razor so you tan shave yourself now.
  EXPRESSION: Proud
- CHARACTER: Paul
  LINE: If I knew this was gonna be the surprise, you could've gotten me to burn all my books.
  EXPRESSION: Bitter
- CHARACTER: Annie
  LINE: Now don't josh. This is a very big day for you, Paul. Here. You just sit tight, and I’ll set everything up.
  EXPRESSION: Encouraging
- CHARACTER: Narrator
  LINE: Annie exits.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Paul, quickly shoving the Novril into the mattress.
  EXPRESSION: Deceptive
- CHARACTER: Paul
  LINE: Set what up?
  EXPRESSION: Curious
- CHARACTER: Annie
  LINE: That’s the big surprise. Your new studio--after all, writers do need a place to work.
  EXPRESSION: Enthusiastic
- CHARACTER: Paul
  LINE: Work? You mean write? What in the world do you think I'd write?
  EXPRESSION: Skeptical
- CHARACTER: Annie
  LINE: Oh, but Paul! I don't think, I know! Now that
  EXPRESSION: Excited

::PATHS::
- CHOICE: Continue
  TARGET: end
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Somewhere
MOOD: Intense
CHARACTERS: Narrator, Annie, Paul
BACKGROUND_IMAGE: null
BACKGROUND_EDIT: null

::SCRIPT::
- CHARACTER: Narrator
  LINE: you've gotten rid of that nasty manuscript, you can go back to doing what you’re great at--
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: --you're going to write a new novel-- your greatest achievement ever-- Misery's Return.
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue"
  TARGET: paul_stunned
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Somewhere
MOOD: Stunned
CHARACTERS: Paul
BACKGROUND_IMAGE: null
BACKGROUND_EDIT: null

::SCRIPT::
- CHARACTER: Paul
  LINE: Misery's Return?
  EXPRESSION: Stunned

::PATHS::
- CHOICE: "Respond to Annie"
  TARGET: annie_fervor
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Somewhere
MOOD: Religious Fervor
CHARACTERS: Narrator, Annie, Paul
BACKGROUND_IMAGE: annie_closeup.png
BACKGROUND_EDIT: "Close up on Annie's face, eyes wide with fervor"

::SCRIPT::
- CHARACTER: Narrator
  LINE: In an almost religious fervor.
  EXPRESSION: null
- CHARACTER: Annie
  LINE: Yes. It will be a book in my honor. For saving your life and nursing you back to health. I'll be the first one to read it.
  EXPRESSION: Excited
- CHARACTER: Narrator
  LINE: Oh, Paul, you're going to make me the envy of the whole world...
  EXPRESSION: Excited

::PATHS::
- CHOICE: "Paul responds"
  TARGET: paul_skeptical
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Somewhere
MOOD: Skeptical
CHARACTERS: Paul
BACKGROUND_IMAGE: null
BACKGROUND_EDIT: null

::SCRIPT::
- CHARACTER: Paul
  LINE: You just expect me to whip something off, that it?
  EXPRESSION: Skeptical

::PATHS::
- CHOICE: "Annie responds"
  TARGET: annie_masterpiece
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Somewhere
MOOD: Demanding
CHARACTERS: Annie
BACKGROUND_IMAGE: null
BACKGROUND_EDIT: null

::SCRIPT::
- CHARACTER: Annie
  LINE: I expect nothing less than your masterpiece.
  EXPRESSION: Demanding

::PATHS::
- CHOICE: "Paul voices concern"
  TARGET: paul_oddball
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Somewhere
MOOD: Uneasy
CHARACTERS: Paul
BACKGROUND_IMAGE: null
BACKGROUND_EDIT: null

::SCRIPT::
- CHARACTER: Paul
  LINE: You do understand that this isn't the ordinary way books get written-- I mean, some people might actually consider this an oddball situation.
  EXPRESSION: Uneasy

::PATHS::
- CHOICE: "Annie moves him"
  TARGET: annie_window_table
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Somewhere
MOOD: Determined
CHARACTERS: Narrator, Annie, Paul
BACKGROUND_IMAGE: null
BACKGROUND_EDIT: null

::SCRIPT::
- CHARACTER: Narrator
  LINE: She rolls him over to a table she has set up by the window.
  EXPRESSION: null
- CHARACTER: Annie
  LINE: I have total confidence in your brilliance--besides, the view will inspire you.
  EXPRESSION: Determined

::PATHS::
- CHOICE: "View the surroundings"
  TARGET: window_view
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: The Window
MOOD: Desolate
CHARACTERS: Narrator, Annie, Paul
BACKGROUND_IMAGE: window_view.png
BACKGROUND_EDIT: "View from the window: clear sky, forest, barn, Jeep, no neighbors."

::SCRIPT::
- CHARACTER: Narrator
  LINE: The sky is innocent of clouds. There's a green forest climbing the flank of the nearest mountain. A plot of open ground between the house and the mountain. A neat red barn where the livestock stay. A Jeep Cherokee, maybe five years old. A Fisher plow. And no neighbors in sight. This is a desolate place.
  EXPRESSION: null

::PATHS::
- CHOICE: "Annie leaves"
  TARGET: annie_leaves
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Somewhere
MOOD: Confident
CHARACTERS: Annie
BACKGROUND_IMAGE: null
BACKGROUND_EDIT: null

::SCRIPT::
- CHARACTER: Annie
  LINE: You just inhale that. I'll be right back.
  EXPRESSION: Confident

::PATHS::
- CHOICE: "Paul calls out"
  TARGET: paul_neighbors
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Somewhere
MOOD: Curious
CHARACTERS: Paul
BACKGROUND_IMAGE: null
BACKGROUND_EDIT: null

::SCRIPT::
- CHARACTER: Paul
  LINE: I guess you don't get bothered by neighbors much.
  EXPRESSION: Curious

::PATHS::
- CHOICE: "Annie reassures Paul"
  TARGET: annie_solitude
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Somewhere
MOOD: Reassuring
CHARACTERS: Annie
BACKGROUND_IMAGE: null
BACKGROUND_EDIT: null

::SCRIPT::
- CHARACTER: Annie
  LINE: Don't worry about that. You'll have total solitude so you can concentrate on your work.
  EXPRESSION: Reassuring

::PATHS::
- CHOICE: "Paul agrees"
  TARGET: paul_great
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Somewhere
MOOD: Accepting
CHARACTERS: Paul
BACKGROUND_IMAGE: null
BACKGROUND_EDIT: null

::SCRIPT::
- CHARACTER: Paul
  LINE: Great.
  EXPRESSION: Accepting

::PATHS::
- CHOICE: "Annie returns"
  TARGET: annie_supplies
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Somewhere
MOOD: Organized
CHARACTERS: Narrator, Annie, Paul
BACKGROUND_IMAGE: annie_supplies.png
BACKGROUND_EDIT: "Annie entering with reams of paper, pens, pencils, sharpener."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Annie in the doorway, carrying reams of typing paper, pencils, pens and sharpener.
  EXPRESSION: null

::PATHS::
- CHOICE: "Paul observes"
  TARGET: paul_amazing
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Somewhere
MOOD: Amazed
CHARACTERS: Narrator, Paul, Annie
BACKGROUND_IMAGE: null
BACKGROUND_EDIT: null

::SCRIPT::
- CHARACTER: Narrator
  LINE: Paul, watching her--it's all kind of amazing.
  EXPRESSION: Amazed
- CHARACTER: Narrator
  LINE: She hands him a box of typing paper.
  EXPRESSION: null
- CHARACTER: Annie
  LINE: I got you this expensive paper to type on.
  EXPRESSION: Proud

::PATHS::
- CHOICE: "Paul examines the paper"
  TARGET: paul_paper_idea
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Somewhere
MOOD: Calculating
CHARACTERS: Narrator, Paul, Annie
BACKGROUND_IMAGE: paul_paper.png
BACKGROUND_EDIT: "Paul looking at the Corrasable Bond paper, an idea forming."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Paul, looking at the paper. It's Corrasable Bond. An idea hits him; he masks it as best he can.
  EXPRESSION: null
- CHARACTER: Annie
  LINE: And I got a great deal on this fifty-pound clunker--on account of it's missing an "n." I told the saleslady "n" was one of the letters in my favorite writer's name.
  EXPRESSION: Proud

::PATHS::
- CHOICE: "Paul compliments Annie"
  TARGET: paul_nurse_name
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Somewhere
MOOD: Affectionate
CHARACTERS: Paul, Annie
BACKGROUND_IMAGE: null
BACKGROUND_EDIT: null

::SCRIPT::
- CHARACTER: Paul
  LINE: It's two of the letters in my favorite nurse's name, Annie.
  EXPRESSION: Affectionate

::PATHS::
- CHOICE: "Annie reacts"
  TARGET: annie_fooler
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Somewhere
MOOD: Flustered
CHARACTERS: Annie
BACKGROUND_IMAGE: null
BACKGROUND_EDIT: null

::SCRIPT::
- CHARACTER: Annie
  LINE: You--fooler...! Did I do good?
  EXPRESSION: Flustered

::PATHS::
- CHOICE: "Paul points out a flaw"
  TARGET: paul_paper_flaw
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Somewhere
MOOD: Direct
CHARACTERS: Paul
BACKGROUND_IMAGE: null
BACKGROUND_EDIT: null

::SCRIPT::
- CHARACTER: Paul
  LINE: You did great, except there's just one little thing--I can't work with this paper. It's Corrasable Bond, it smudges. Maybe you could go back into town and bring me some white, long-grained mimeo.
  EXPRESSION: Direct

::PATHS::
- CHOICE: "Annie questions"
  TARGET: annie_question_smudge
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Somewhere
MOOD: Confused
CHARACTERS: Annie
BACKGROUND_IMAGE: null
BACKGROUND_EDIT: null

::SCRIPT::
- CHARACTER: Annie
  LINE: But mine cost the most so I don't see how it could smudge.
  EXPRESSION: Confused

::PATHS::
- CHOICE: "Paul demonstrates"
  TARGET: paul_demonstrate
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Somewhere
MOOD: Demonstrative
CHARACTERS: Paul, Annie
BACKGROUND_IMAGE: paul_demonstrate.png
BACKGROUND_EDIT: "Paul making a pencil mark and rubbing it off to show smudging."

::SCRIPT::
- CHARACTER: Narrator
  LINE: As she approaches, he rubs his thumb over the pencil mark.
  EXPRESSION: null
- CHARACTER: Annie
  LINE: Well, it does smudge after all--isn't that fascinating?
  EXPRESSION: Fascinated
- CHARACTER: Paul
  LINE: I thought you'd be interested. I'd like you to be in on everything, Annie. Not just the finished book, but how it's written.
  EXPRESSION: Earnest

::PATHS::
- CHOICE: "Annie thanks Paul"
  TARGET: annie_thanks
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Somewhere
MOOD: Gracious
CHARACTERS: Annie
BACKGROUND_IMAGE: null
BACKGROUND_EDIT: null

::SCRIPT::
- CHARACTER: Annie
  LINE: Thank you for thinking of me. (She can be so charming when she wants) Anything else I can get while I’m in town? Any other crucial requirements that need satisfying? Would you like a tiny tape recorder? Or maybe a handmade set of writing slippers?
  EXPRESSION: Gracious

::PATHS::
- CHOICE: "Paul declines"
  TARGET: paul_decline_extras
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Somewhere
MOOD: Calm
CHARACTERS: Paul
BACKGROUND_IMAGE: null
BACKGROUND_EDIT: null

::SCRIPT::
- CHARACTER: Paul
  LINE: No, just the paper will be fine.
  EXPRESSION: Calm

::PATHS::
- CHOICE: "Annie becomes agitated"
  TARGET: annie_agitated
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Somewhere
MOOD: Agitated
CHARACTERS: Annie
BACKGROUND_IMAGE: null
BACKGROUND_EDIT: null

::SCRIPT::
- CHARACTER: Annie
  LINE: Are you sure? 'Cause if you want, I'll bring back the whole store for you.
  EXPRESSION: Agitated

::PATHS::
- CHOICE: "Paul asks what's wrong"
  TARGET: paul_ask_what_matter
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Somewhere
MOOD: Upset
CHARACTERS: Paul, Annie
BACKGROUND_IMAGE: null
BACKGROUND_EDIT: null

::SCRIPT::
- CHARACTER: Paul
  LINE: Annie, what’s the matter?
  EXPRESSION: Concerned
- CHARACTER: Annie
  LINE: What’s the matter? I'll tell you what’s the matter. I go out of my way for you. I do everything to try and make you happy. I feed you, I clean you, I dress you. And what thanks do I get? "You bought the wrong paper, Annie. I can’t write on this paper, Annie." Well, I’ll get your stupid paper, but you just better start showing me a little more appreciation around here, Mister Man.
  EXPRESSION: Upset

::PATHS::
- CHOICE: "Annie throws paper"
  TARGET: annie_throws_paper
  STATE_CHANGE: pain = +1
  CONDITION: null

::SCENE::
LOCATION: Somewhere
MOOD: Painful
CHARACTERS: Narrator, Paul, Annie
BACKGROUND_IMAGE: annie_throws_paper.png
BACKGROUND_EDIT: "Annie throwing the ream of paper into Paul's lap."

::SCRIPT::
- CHARACTER: Narrator
  LINE: With that, she throws the ream of paper in PAUL'S LAP, causing considerable pain.
  EXPRESSION: null

::PATHS::
- CHOICE: "Annie storms out"
  TARGET: annie_storms_out
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: The Door
MOOD: Angry Exit
CHARACTERS: Narrator, Annie
BACKGROUND_IMAGE: annie_door_slam.png
BACKGROUND_EDIT: "Annie slamming the door, locking it, and stomping off."

::SCRIPT::
- CHARACTER: Narrator
  LINE: As she slams it shut, locks it, stomps off and
  EXPRESSION: null

::PATHS::
- CHOICE: "Annie drives away"
  TARGET: annie_drives_away
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: The Window
MOOD: Frustrated Departure
CHARACTERS: Narrator, Annie
BACKGROUND_IMAGE: annie_cherokee_leaves.png
BACKGROUND_EDIT: "Annie in a parka, seen through the window, storming to her Jeep and driving off."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Annie, in a parka, can be seen storming out in the direction where her Cherokee was parked. She gets in and drives off.
  EXPRESSION: null

::PATHS::
- CHOICE: "Paul reacts"
  TARGET: paul_sigh
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Somewhere
MOOD: Weary
CHARACTERS: Narrator, Paul
BACKGROUND_IMAGE: paul_sigh.png
BACKGROUND_EDIT: "Paul heaving a sigh, reaching for his knees, then dropping his head."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Paul. He heaves a sigh, reaches out toward his tortured knees, then drops his head. He sees something.
  EXPRESSION: null

::PATHS::
- CHOICE: "Paul sees bobby pin"
  TARGET: paul_sees_bobby_pin
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Somewhere
MOOD: Determined Struggle
CHARACTERS: Narrator, Paul
BACKGROUND_IMAGE: bobby_pin_floor.png
BACKGROUND_EDIT: "Close up on a bobby pin on the floor."

::SCRIPT::
- CHARACTER: Narrator
  LINE: BOBBY PIN on the floor.
  EXPRESSION: null

::PATHS::
- CHOICE: "Paul attempts to reach it"
  TARGET: paul_reaches_bobby_pin
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Somewhere
MOOD: Painful Effort
CHARACTERS: Narrator, Paul
BACKGROUND_IMAGE: paul_struggles.png
BACKGROUND_EDIT: "Paul in his wheelchair, trying to move towards the bobby pin, straining with each inch."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Paul, as he moves toward the bobby pin. Or tries to. It's brutally hard for him. The chair moves half a foot. Stops. Paul strains again. Another half foot. Another.
  EXPRESSION: null

::PATHS::
- CHOICE: "Wheelchair reaches bobby pin"
  TARGET: bobby_pin_reached
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Somewhere
MOOD: Reaching
CHARACTERS: Narrator, Paul
BACKGROUND_IMAGE: bobby_pin_close.png
BACKGROUND_EDIT: "The wheelchair is beside the bobby pin. Paul reaches down, unable to get it."

::SCRIPT::
- CHARACTER: Narrator
  LINE: The BOBBY PIN. The wheelchair is beside it now. PAUL reaches down for it. Can't make it. Tries again. Can't. He takes a deep breath, forces himself to bend, ignoring the pain. The bobby pin is in his hands.
  EXPRESSION: null

::PATHS::
- CHOICE: "Paul attempts to pick lock"
  TARGET: paul_jimmy_lock
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Somewhere
MOOD: Attempting
CHARACTERS: Narrator, Paul
BACKGROUND_IMAGE: paul_jimmy_lock.png
BACKGROUND_EDIT: "Paul inserting the bobby pin into the keyhole."

::SCRIPT::
- CHARACTER: Narrator
  LINE: PAUL, inserting the bobby pin into the keyhole, beginning to jimmy the lock.
  EXPRESSION: null

::PATHS::
- CHOICE: "Lock clicks"
  TARGET: lock_sound
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: The Lock
MOOD: Hopeful Sound
CHARACTERS: Narrator
BACKGROUND_IMAGE: lock_click.png
BACKGROUND_EDIT: "Close up of the lock, making a clicking sound."

::SCRIPT::
- CHARACTER: Narrator
  LINE: THE LOCK--it makes a SOUND--something has caught.
  EXPRESSION: null

::PATHS::
- CHOICE: "Bobby pin slips"
  TARGET: paul_frustrated
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Somewhere
MOOD: Frustrated
CHARACTERS: Narrator, Paul
BACKGROUND_IMAGE: paul_bobby_pin_slip.png
BACKGROUND_EDIT: "Paul excitedly trying to force the bobby pin, but it slips and falls again."

::SCRIPT::
- CHARACTER: Narrator
  LINE: PAUL, excited, trying to force the bobby pin and he's doing great--until it slips from his hands, falls to the floor again.
  EXPRESSION: null
- CHARACTER: Paul
  LINE: Shit...
  EXPRESSION: Furious

::PATHS::
- CHOICE: "Paul reaches for bobby pin again"
  TARGET: paul_reach_again
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Somewhere
MOOD: Painful Reach
CHARACTERS: Narrator, Paul
BACKGROUND_IMAGE: paul_reach_pain.png
BACKGROUND_EDIT: "Close up on the bobby pin on the floor. Paul reaches for it, crying out in pain, but clutches it tight."

::SCRIPT::
- CHARACTER: Narrator
  LINE: THE BOBBY PIN. Paul reaches for it. The pain has him. He reaches again, involuntarily cries out. But he grabs it, clutches it tight.
  EXPRESSION: null

::PATHS::
- CHOICE: "Paul tries the lock again"
  TARGET: paul_jimmy_second_time
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: The Keyhole
MOOD: Second Attempt
CHARACTERS: Narrator, Paul
BACKGROUND_IMAGE: paul_jimmy_second_time.png
BACKGROUND_EDIT: "Paul trying to jimmy the lock a second time."

::SCRIPT::
- CHARACTER: Narrator
  LINE: THE KEYHOLE. Paul is trying to jimmy the lock a second time. No luck.
  EXPRESSION: null

::PATHS::
- CHOICE: "Paul expresses frustration"
  TARGET: paul_wild_frustration
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Somewhere
MOOD: Wild Frustration
CHARACTERS: Paul
BACKGROUND_IMAGE: null
BACKGROUND_EDIT: null

::SCRIPT::
- CHARACTER: Paul
  LINE: You’ve written how to do this--now do it!
  EXPRESSION: Wild Frustration

::PATHS::
- CHOICE: "Lock clicks audibly"
  TARGET: loud_click
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: The Keyhole
MOOD: Success
CHARACTERS: Narrator
BACKGROUND_IMAGE: loud_click.png
BACKGROUND_EDIT: "Close up of the keyhole. A loud CLICKING sound is heard."

::SCRIPT::
- CHARACTER: Narrator
  LINE: THE KEYHOLE. There is a loud CLICKING sound.
  EXPRESSION: null

::PATHS::
- CHOICE: "Door opens"
  TARGET: door_opens
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: The Door
MOOD: Amazement
CHARACTERS: Narrator, Paul
BACKGROUND_IMAGE: door_opens_crack.png
BACKGROUND_EDIT: "The door opens a crack."

::SCRIPT::
- CHARACTER: Narrator
  LINE: THE DOOR as Paul turns the knob. The door opens a crack.
  EXPRESSION: null
- CHARACTER: Paul
  LINE: What do you know, it actually works.
  EXPRESSION: Amazed

::PATHS::
- CHOICE: "Paul attempts to exit"
  TARGET: paul_exiting_struggle
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Somewhere
MOOD: Exhausting Effort
CHARACTERS: Narrator, Paul
BACKGROUND_IMAGE: paul_exiting_struggle.png
BACKGROUND_EDIT: "Paul struggling to maneuver his wheelchair out of the doorway. He's pale and perspiring."

::SCRIPT::
- CHARACTER: Narrator
  LINE: PAUL, trying to get out of the room--but it's a bitch because in order to get to the lock he had to move the wheelchair up to the door and in order to get out, he’s got to maneuver it out of the way of the door and every turn of the chair’s wheels is an effort for him. He works at it and works at it, but his energy is failing him. He’s pale, perspiring. Finally he succeeds, barely forces hi
  EXPRESSION: null

::PATHS::
- CHOICE: "Paul succeeds in exiting"
  TARGET: end
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Hallway
MOOD: Trapped
CHARACTERS: Narrator, Paul
BACKGROUND_IMAGE: hallway.png
BACKGROUND_EDIT: "Interior hallway, dimly lit"

::SCRIPT::
- CHARACTER: Narrator
  LINE: s way into the hall.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Paul, in the hallway outside. He looks around for a phone. Doesn’t see one. He wheels himself over to the front door, tries it. It's locked from the outside.
  EXPRESSION: null
- CHARACTER: Paul
  LINE: What a surprise.
  EXPRESSION: Sarcastic
- CHARACTER: Narrator
  LINE: He looks off into the living room, and...
  EXPRESSION: null

::PATHS::
- CHOICE: "Enter living room"
  TARGET: living_room
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Living Room
MOOD: Nostalgic then Tense
CHARACTERS: Narrator, Paul, Annie (in photo)
BACKGROUND_IMAGE: living_room.png
BACKGROUND_EDIT: "Dark red interior, musty, barred windows, family photo"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Paul, wheeling into the living room. Dark red predominates. It's a musty room. Over the mantel, a photograph of a six-year-old Annie, with her mother and father in front of the family car--a new 1952 Buick. These were happier times.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The windows have bars on them.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: As Paul begins to wheel as fast as he can toward the phone--
  EXPRESSION: null

::PATHS::
- CHOICE: "Reach for the phone"
  TARGET: phone_grab
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: The Telephone
MOOD: Anticipation
CHARACTERS: Narrator, Paul
BACKGROUND_IMAGE: phone.png
BACKGROUND_EDIT: "Close up of a rotary telephone"

::SCRIPT::
- CHARACTER: Narrator
  LINE: ...the phone as Paul at last grabs for it, gets it, punches the "operator" button--
  EXPRESSION: null

::PATHS::
- CHOICE: "Call for operator"
  TARGET: operator_call
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Operator Call
MOOD: Frustration
CHARACTERS: Narrator, Paul
BACKGROUND_IMAGE: phone.png
BACKGROUND_EDIT: "Close up of Paul holding the telephone receiver"

::SCRIPT::
- CHARACTER: Paul
  LINE: Operator...
  EXPRESSION: Hopeful
- CHARACTER: Narrator
  LINE: (nothing)
  EXPRESSION: null
- CHARACTER: Paul
  LINE: ...OPERATOR...
  EXPRESSION: Desperate
- CHARACTER: Paul
  LINE: ...Shit!
  EXPRESSION: Angry
- CHARACTER: Narrator
  LINE: He shakes the phone. It’s terribly light. He picks it up, turns it over--it's hollow, just a shell of a telephone. He stares at it for a long moment, shaking his head, the disappointment plain.
  EXPRESSION: null
- CHARACTER: Paul
  LINE: You crazy bitch...
  EXPRESSION: Bitter
- CHARACTER: Narrator
  LINE: He puts the phone back on the table.
  EXPRESSION: null

::PATHS::
- CHOICE: "Go to the study"
  TARGET: study
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: The General Store
MOOD: Mundane
CHARACTERS: Narrator, Annie
BACKGROUND_IMAGE: general_store.png
BACKGROUND_EDIT: "Exterior of a store, daytime"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Annie exits the store, carrying new paper, hops into her Cherokee and drives off.
  EXPRESSION: null

::PATHS::
- CHOICE: "Follow Annie"
  TARGET: annie_following
  STATE_CHANGE: null
  CONDITION: null
- CHOICE: "Return to Paul"
  TARGET: study
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: The Study
MOOD: Overwhelmed by Collection
CHARACTERS: Narrator, Paul
BACKGROUND_IMAGE: study.png
BACKGROUND_EDIT: "Study filled with furniture and knickknacks"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The study, as Paul enters. He looks around. It's stuffed with heavy, graceless furniture as well as lots of coffee tables covered with knickknacks. As he, with effort wheels across it--
  EXPRESSION: null

::PATHS::
- CHOICE: "Observe the bookshelf"
  TARGET: bookshelf
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Bookshelf
MOOD: Recognition
CHARACTERS: Narrator, Paul
BACKGROUND_IMAGE: bookshelf.png
BACKGROUND_EDIT: "Shelf filled with books"

::SCRIPT::
- CHARACTER: Narrator
  LINE: A shelf of Books. Paul Sheldon books. EVERY Paul Sheldon book.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Paul, pausing, looking at her collection. The only book on the shelf that isn't his is a large scrapbook. The title on the back reads "My Life."
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: He glances back at the shelf as he forces his wheelchair across the study, and we
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue across the study"
  TARGET: small_table
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Small Table
MOOD: Near Miss
CHARACTERS: Narrator, Paul
BACKGROUND_IMAGE: small_table.png
BACKGROUND_EDIT: "Table with ceramic figurines"

::SCRIPT::
- CHARACTER: Narrator
  LINE: A small table with little ceramic doodads on top. The wheelchair hits it, one of the doodads topples--it's a penguin fragile looking, and as it's about to fall to the floor and shatter--
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Paul, grabbing for it, catching it, putting it back where it was. He continues his slow way across the room and
  EXPRESSION: null

::PATHS::
- CHOICE: "Proceed to the hallway"
  TARGET: hallway_2
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: The Hallway
MOOD: Discovery
CHARACTERS: Narrator, Paul
BACKGROUND_IMAGE: hallway_2.png
BACKGROUND_EDIT: "Interior hallway with a pantry door"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Out in the hallway, on his way toward the kitchen, Paul notices a door to his right. He wheels over and surprisingly it opens. However, this is not a door to the outside of the house, only a storage pantry. He looks around--nothing but canned goods, potato chips, cereals and large plastic Coke containers, etc.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Just as he is about to close the door, he notices an open cardboard box. He opens the flap and sees all kinds of prescription drugs. Among them are a couple of strips of Novril encapsulated in blisters. He grabs them and stuffs them into his sweatpants. Now he closes the pantry door and heads to the kitchen.
  EXPRESSION: null

::PATHS::
- CHOICE: "Head to the kitchen"
  TARGET: kitchen_entry
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Kitchen Entry
MOOD: Frustration
CHARACTERS: Narrator, Paul
BACKGROUND_IMAGE: kitchen_entry.png
BACKGROUND_EDIT: "Narrow kitchen doorway"

::SCRIPT::
- CHARACTER: Narrator
  LINE: As Paul approaches it. He starts to wheel his way in, but he has trouble. He backs up slightly, wheels forward again--but the door is too narrow for the chair to fit through.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: He pounds his fists on the chair arm, staring as we
  EXPRESSION: null

::PATHS::
- CHOICE: "Look at the back door"
  TARGET: back_door
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Back Door
MOOD: Desperate Hope
CHARACTERS: Narrator, Paul
BACKGROUND_IMAGE: back_door.png
BACKGROUND_EDIT: "Back door of the kitchen, barred windows"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The back door. It's at the far end of the kitchen leading to the outside. It seems somehow less formidable than the front door did. The windows around the kitchen are barred.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Paul, staring at the kitchen door--then without warning, he makes his move, starting to lower himself out of the chair gently to the floor--
  EXPRESSION: null

::PATHS::
- CHOICE: "Attempt to exit wheelchair"
  TARGET: exit_wheelchair_fail
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Exit Wheelchair Fail
MOOD: Pain and Struggle
CHARACTERS: Narrator, Paul
BACKGROUND_IMAGE: floor.png
BACKGROUND_EDIT: "Hard floor"

::SCRIPT::
- CHARACTER: Narrator
  LINE: --only it doesn't work that way. It’s too awkward, he doesn't have the strength to maneuver properly--and his body tilts awkwardly out of the chair, slams hard against the hard floor.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Paul, crying out in pain as he lands. He lies there for a moment. Little droplets of sweat are on his forehead now. He is hurting.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: He closes his eyes, gathering strength--and then slowly, very slowly, inch by inch, he moves his body across the floor toward the kitchen door.
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue crawling"
  TARGET: kitchen_door_progress
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Kitchen Door Progress
MOOD: Determined Effort
CHARACTERS: Narrator, Paul
BACKGROUND_IMAGE: kitchen_door.png
BACKGROUND_EDIT: "Kitchen door in the distance"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The kitchen door. It's still a long way away.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Paul, ignoring his pain, his awkwardness, making his body move.
  EXPRESSION: null

::PATHS::
- CHOICE: "Keep moving towards the door"
  TARGET: kitchen_door_closer
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Kitchen Door Closer
MOOD: Nearing the Goal
CHARACTERS: Narrator, Paul
BACKGROUND_IMAGE: kitchen_door.png
BACKGROUND_EDIT: "Kitchen door is closer now"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The kitchen door. Closer now.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Paul, growing pale, but he won't stop, and now the door is just ahead of him, and with his good arm he reaches out and up and grabs the doorknob--
  EXPRESSION: null

::PATHS::
- CHOICE: "Attempt to open the door"
  TARGET: kitchen_door_locked
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Kitchen Door Locked
MOOD: Crushing Disappointment
CHARACTERS: Narrator, Paul
BACKGROUND_IMAGE: kitchen_door.png
BACKGROUND_EDIT: "Kitchen door, locked solid"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The kitchen door. Locked solid.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Paul: CLOSE UP. The disappointment and anger is plain on his face. His arm drops. He lies still for a moment, panting from his effort. Then--
  EXPRESSION: null

::PATHS::
- CHOICE: "Look for another way"
  TARGET: carving_knives
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Carving Knives
MOOD: Dangerous Hope
CHARACTERS: Narrator, Paul
BACKGROUND_IMAGE: counter_knives.png
BACKGROUND_EDIT: "Counter with a set of carving knives"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Paul, and his eyes are wide for a moment. You can feel his wild excitement, as we PULL BACK TO REVEAL Sitting on the counter: A SET OF CARVING KNIVES sticking out of a slotted wooden block.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: They seem to be out of reach, but that doesn't stop him. He starts to crawl over to the counter.
  EXPRESSION: null

::PATHS::
- CHOICE: "Crawl towards the counter"
  TARGET: counter_attempt
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: The Road
MOOD: Heading Home
CHARACTERS: Narrator, Annie
BACKGROUND_IMAGE: road.png
BACKGROUND_EDIT: "Road with a Cherokee driving"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Annie is driving along in her Cherokee. She is heading home.
  EXPRESSION: null

::PATHS::
- CHOICE: "Arrive at the house"
  TARGET: annie_arrives
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: The Kitchen
MOOD: Desperate Attempt
CHARACTERS: Narrator, Paul
BACKGROUND_IMAGE: kitchen_counter.png
BACKGROUND_EDIT: "Paul at the counter, trying to reach knives"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Now at the counter, Paul tries to pull himself up with his one good arm, but even though he is able to chin himself up to the top of the counter, he is still unable to reach the knives. He makes a desperate attempt which sends him crashing to the floor.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: As he starts to force his way up again--from outside there comes a sound--the motor of a car.
  EXPRESSION: null

::PATHS::
- CHOICE: "React to the car sound"
  TARGET: car_sound_reaction
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Outside Annie's
MOOD: Arrival
CHARACTERS: Narrator, Annie
BACKGROUND_IMAGE: annies_house_exterior.png
BACKGROUND_EDIT: "Annie's house, exterior"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Annie, driving up to the house.
  EXPRESSION: null

::PATHS::
- CHOICE: "Enter the house"
  TARGET: paul_wild_crawl
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: INT. THE KITCHEN
MOOD: Panicked Evasion
CHARACTERS: Narrator, Paul
BACKGROUND_IMAGE: kitchen_floor.png
BACKGROUND_EDIT: "Paul crawling rapidly on the kitchen floor"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Paul, throwing himself back to the floor, starting a wild crawl back across the kitchen toward the wheelchair and
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue the race"
  TARGET: annie_back_of_car
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: OUTSIDE ANNIE'S
MOOD: Unloading
CHARACTERS: Narrator, Annie
BACKGROUND_IMAGE: annies_house_exterior.png
BACKGROUND_EDIT: "Annie walking around to the back of her car"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Annie, getting out of her Deep and
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue to the kitchen"
  TARGET: paul_wheelchair_turn
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: KITCHEN
MOOD: Scramble for Mobility
CHARACTERS: Narrator, Paul
BACKGROUND_IMAGE: paul_in_wheelchair.png
BACKGROUND_EDIT: "Paul scrambling into his wheelchair"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Paul, scrambling wildly up into his wheelchair, starting to get it turned and
  EXPRESSION: null

::PATHS::
- CHOICE: "Engage in a race"
  TARGET: race_starts
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: ANNIE'S
MOOD: Unloading Supplies
CHARACTERS: Narrator, Annie
BACKGROUND_IMAGE: annies_car_unloading.png
BACKGROUND_EDIT: "Annie lifting boxes from her car"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Annie, opening the back of the Deep and lifting out several rectangular boxes of paper and
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue the race"
  TARGET: paul_stuck
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: PAUL
MOOD: The Race
CHARACTERS: Narrator, Paul, Annie
BACKGROUND_IMAGE: race_scene.png
BACKGROUND_EDIT: "Fast cuts of Paul in wheelchair and Annie by car"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Paul, straightened out now, forcing the wheelchair to move, and now we're into a race, a crazed life-and-death race and the cuts go fast--
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: --and Annie closes the door of the car--
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: --and Paul is suddenly stuck, there's no traction on the rug--
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: --ow Annie, purchases in hand, starts away from the car for the hou
  EXPRESSION: null

::SCENE::
LOCATION: Hallway/Bedroom Door
MOOD: Urgent
CHARACTERS: Narrator, Paul, Annie
BACKGROUND_IMAGE: hallway_bedroom.png
BACKGROUND_EDIT: "Interior, showing hallway and bedroom door"

::SCRIPT::
- CHARACTER: Narrator
  LINE: and now PAUL is finally moving toward the bedroom.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: and ANNIE is moving swiftly toward the front door.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: he drops one of the packages of paper.
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue action"
  TARGET: paul_struggling
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Paul's Arms/Bedroom
MOOD: Intense Effort
CHARACTERS: Narrator, Paul
BACKGROUND_IMAGE: paul_arms.png
BACKGROUND_EDIT: "Close-up on Paul's arms, straining"

::SCRIPT::
- CHARACTER: Narrator
  LINE: PAUL, still biting down, churning his arms with all the strength he has left. PAUL'S ARMS, aching, start to turn to rubber.
  EXPRESSION: Strained

::PATHS::
- CHOICE: "Continue action"
  TARGET: annie_feet
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Front of House
MOOD: Swift Movement
CHARACTERS: Narrator, Annie
BACKGROUND_IMAGE: annie_feet.png
BACKGROUND_EDIT: "Close-up on Annie's feet walking on snow"

::SCRIPT::
- CHARACTER: Narrator
  LINE: ANNIE'S FEET, walking quickly across the snow-covered area in front of the house
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue action"
  TARGET: bedroom_door_entering
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Bedroom Door
MOOD: Determined Action
CHARACTERS: Narrator, Paul
BACKGROUND_IMAGE: bedroom_door_entering.png
BACKGROUND_EDIT: "Close-up on the bedroom door as Paul enters"

::SCRIPT::
- CHARACTER: Narrator
  LINE: THE BEDROOM DOOR as Paul gets through it, shuts it, and attacks the bedroom lock with the bobby pin
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue action"
  TARGET: annie_unlocking
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Front Door
MOOD: Swift Action
CHARACTERS: Narrator, Annie
BACKGROUND_IMAGE: annie_unlocking.png
BACKGROUND_EDIT: "Close-up on Annie at the front door, unlocking it"

::SCRIPT::
- CHARACTER: Narrator
  LINE: ANNIE, unlocking the front door of the house
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue action"
  TARGET: bedroom_door_locking
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Bedroom Door
MOOD: Secure
CHARACTERS: Narrator, Paul
BACKGROUND_IMAGE: bedroom_door_locking.png
BACKGROUND_EDIT: "Close-up on the bedroom door as it locks"

::SCRIPT::
- CHARACTER: Narrator
  LINE: THE BEDROOM DOOR, as it locks
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue action"
  TARGET: front_door_unlocking
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Front Door
MOOD: Unlocking
CHARACTERS: Narrator, Annie
BACKGROUND_IMAGE: front_door_unlocking.png
BACKGROUND_EDIT: "Close-up on the front door as it unlocks"

::SCRIPT::
- CHARACTER: Narrator
  LINE: THE FRONT DOOR, unlocking
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue action"
  TARGET: annie_balancing
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Front Doorway
MOOD: Prepared to Leave
CHARACTERS: Narrator, Annie
BACKGROUND_IMAGE: annie_balancing.png
BACKGROUND_EDIT: "Annie at the front door, balancing packages"

::SCRIPT::
- CHARACTER: Narrator
  LINE: ANNIE balancing the bundles under her chin as she jiggles the key out of the front door lock
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue action"
  TARGET: paul_soaked
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Bedroom Interior
MOOD: Distressed
CHARACTERS: Narrator, Paul
BACKGROUND_IMAGE: paul_soaked.png
BACKGROUND_EDIT: "Paul is visibly sweating"

::SCRIPT::
- CHARACTER: Narrator
  LINE: PAUL, soaked.
  EXPRESSION: Distressed

::PATHS::
- CHOICE: "Continue action"
  TARGET: annie_voice
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Hallway/Bedroom
MOOD: Approaching
CHARACTERS: Narrator, Annie
BACKGROUND_IMAGE: annie_voice.png
BACKGROUND_EDIT: "Sound implied from hallway, moving towards bedroom"

::SCRIPT::
- CHARACTER: ANNIE (V.O.)
  LINE: Paul, I've got your paper.
  EXPRESSION: Close, growing closer

::PATHS::
- CHOICE: "Continue action"
  TARGET: paul_relief
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Bedroom Interior
MOOD: Relief
CHARACTERS: Narrator, Paul
BACKGROUND_IMAGE: paul_relief.png
BACKGROUND_EDIT: "Paul in the bedroom, showing relief"

::SCRIPT::
- CHARACTER: Narrator
  LINE: PAUL. He wheels to exactly where he was when she left him. He at last allows himself a sigh of relief.
  EXPRESSION: Relieved

::PATHS::
- CHOICE: "Continue action"
  TARGET: lock_click
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Bedroom Door
MOOD: Sound of Entry
CHARACTERS: Narrator
BACKGROUND_IMAGE: lock_click.png
BACKGROUND_EDIT: "Close-up on the door, sound implied"

::SCRIPT::
- CHARACTER: Narrator
  LINE: THE DOOR as the sound of a lock CLICKING is heard.
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue action"
  TARGET: annie_delivers
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Bedroom Doorway
MOOD: Transaction
CHARACTERS: Narrator, Annie
BACKGROUND_IMAGE: annie_delivers.png
BACKGROUND_EDIT: "Annie in the doorway with paper"

::SCRIPT::
- CHARACTER: ANNIE
  LINE: Just the kind you asked for.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: And as the door opens--
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue action"
  TARGET: paul_hiding
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Bedroom Interior
MOOD: Hidden Distress
CHARACTERS: Narrator, Paul
BACKGROUND_IMAGE: paul_hiding.png
BACKGROUND_EDIT: "Paul looking down at his waistband"

::SCRIPT::
- CHARACTER: Narrator
  LINE: PAUL--looking down. Paul's waistband--a half a dozen strips of Novril ominously stick out. As the door swings open, he quickly covers the Novril with his hands.
  EXPRESSION: Panicked

::PATHS::
- CHOICE: "Continue action"
  TARGET: annie_entering
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Bedroom Doorway
MOOD: Concerned Observation
CHARACTERS: Narrator, Annie
BACKGROUND_IMAGE: annie_entering.png
BACKGROUND_EDIT: "Annie in the doorway, looking at Paul"

::SCRIPT::
- CHARACTER: Narrator
  LINE: ANNIE, in the doorway, a strange look on her face.
  EXPRESSION: Curious

::PATHS::
- CHOICE: "Continue action"
  TARGET: annie_asks_paul
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Bedroom Interior
MOOD: Confrontation
CHARACTERS: Narrator, Annie, Paul
BACKGROUND_IMAGE: annie_asks_paul.png
BACKGROUND_EDIT: "Annie looking at Paul's condition"

::SCRIPT::
- CHARACTER: ANNIE
  LINE: Paul, you're dripping with perspiration, your color is very hectic--what have you been doing?
  EXPRESSION: Concerned
- CHARACTER: PAUL
  LINE: You know goddamn well what I've been doing—I'VE BEEN SITTING HERE SUFFERING. I need my pills.
  EXPRESSION: Angry
- CHARACTER: ANNIE
  LINE: Poor dear... Let's get you back in bed and I’ll get them for you.
  EXPRESSION: Tender
- CHARACTER: PAUL
  LINE: I WANT MY PILLS NOW!
  EXPRESSION: Explosive tantrum
- CHARACTER: ANNIE
  LINE: It'll only take a second.
  EXPRESSION: Patient
- CHARACTER: PAUL
  LINE: I want my pain to go 'way, Annie-- make it go 'way, please Annie-- please...
  EXPRESSION: Pleading
- CHARACTER: Narrator
  LINE: (She looks at him— you can't tell if she's buying it or not)
  EXPRESSION: Unreadable

::PATHS::
- CHOICE: "Continue action"
  TARGET: annie_turns_away
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Bedroom Interior
MOOD: Upset Resolve
CHARACTERS: Narrator, Annie
BACKGROUND_IMAGE: annie_turns_away.png
BACKGROUND_EDIT: "Annie looking at Paul, then turning to leave"

::SCRIPT::
- CHARACTER: Narrator
  LINE: CUT TO: ANNIE. She stares a moment more, then turns, starts for the door.
  EXPRESSION: null
- CHARACTER: ANNIE
  LINE: It just breaks my heart to see you like this...
  EXPRESSION: Upset

::PATHS::
- CHOICE: "Continue action"
  TARGET: paul_stuffs_novril
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Bedroom Interior
MOOD: Deceptive Calm
CHARACTERS: Narrator, Paul
BACKGROUND_IMAGE: paul_stuffs_novril.png
BACKGROUND_EDIT: "Paul watching Annie leave, then hiding the pills"

::SCRIPT::
- CHARACTER: Narrator
  LINE: CUT TO: PAUL watching, and the instant she is out the door in the hallway, he stuffs the Novril into his pants.
  EXPRESSION: Cunning

::PATHS::
- CHOICE: "Continue action"
  TARGET: annie_returning_voice
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Hallway/Bedroom
MOOD: Approaching with Contrition
CHARACTERS: Narrator, Annie
BACKGROUND_IMAGE: annie_returning_voice.png
BACKGROUND_EDIT: "Annie's voice from the hallway, closer"

::SCRIPT::
- CHARACTER: ANNIE (O.S.)
  LINE: I've done a lot of thinking on the drive...
  EXPRESSION: Coming closer

::PATHS::
- CHOICE: "Continue action"
  TARGET: annie_enters_with_pills
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Bedroom Interior
MOOD: Contrite and Reconciling
CHARACTERS: Narrator, Annie
BACKGROUND_IMAGE: annie_enters_with_pills.png
BACKGROUND_EDIT: "Annie entering the bedroom with the Novril"

::SCRIPT::
- CHARACTER: Narrator
  LINE: ANNIE, entering the room, the Novril in her hand. She is genuinely contrite.
  EXPRESSION: null
- CHARACTER: ANNIE
  LINE: ...and I'm absolutely convinced that the main reason I've never been more popular is because of my temper. You must be so mad at me. The truth now.
  EXPRESSION: Contrite

::PATHS::
- CHOICE: "Continue action"
  TARGET: annie_hands_pills
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Bedroom Interior
MOOD: Reconciliation
CHARACTERS: Narrator, Annie, Paul
BACKGROUND_IMAGE: annie_hands_pills.png
BACKGROUND_EDIT: "Annie handing Paul the pills, guiding him to bed"

::SCRIPT::
- CHARACTER: Narrator
  LINE: She hands him the pills. And rolls him over to the bed.
  EXPRESSION: null
- CHARACTER: PAUL
  LINE: Well, I don't hold grudges. After all, who doesn't let off a little steam once in a while.
  EXPRESSION: Nonchalant

::PATHS::
- CHOICE: "Continue action"
  TARGET: paul_takes_pills
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Bedroom Interior
MOOD: Giving Aid
CHARACTERS: Narrator, Paul, Annie
BACKGROUND_IMAGE: paul_takes_pills.png
BACKGROUND_EDIT: "Paul taking pills, Annie putting him in bed"

::SCRIPT::
- CHARACTER: Narrator
  LINE: CUT TO: PAUL putting the pills in his mouth, as she picks him up from the chair and puts him gently down in bed.
  EXPRESSION: null
- CHARACTER: ANNIE
  LINE: My genius needs his rest before he writes.
  EXPRESSION: Caring
- CHARACTER: Narrator
  LINE: She hands him a pad and pencil.
  EXPRESSION: null
- CHARACTER: ANNIE
  LINE: Here, in case you think of any ideas.
  EXPRESSION: Encouraging
- CHARACTER: PAUL
  LINE: Yeah, well I wouldn't expect too much.
  EXPRESSION: Understated

::PATHS::
- CHOICE: "Continue action"
  TARGET: annie_inspiration
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Bedroom Interior
MOOD: Encouraging
CHARACTERS: Narrator, Annie, Paul
BACKGROUND_IMAGE: annie_inspiration.png
BACKGROUND_EDIT: "Annie giving Paul a pad and pencil"

::SCRIPT::
- CHARACTER: ANNIE
  LINE: Don't be silly. You'll be brilliant. Think of me as your inspiration.
  EXPRESSION: Confident

::PATHS::
- CHOICE: "Continue action"
  TARGET: annie_leaves_doorway
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Bedroom Doorway
MOOD: Parting Words
CHARACTERS: Narrator, Annie
BACKGROUND_IMAGE: annie_leaves_doorway.png
BACKGROUND_EDIT: "Annie at the bedroom doorway, about to leave"

::SCRIPT::
- CHARACTER: Narrator
  LINE: CUT TO: THE DOORWAY, as ANNIE starts to it.
  EXPRESSION: null
- CHARACTER: ANNIE
  LINE: I have faith in you... my darling...
  EXPRESSION: Loving, then coquettish

::PATHS::
- CHOICE: "Continue action"
  TARGET: annie_kiss
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Bedroom Doorway
MOOD: Grotesque Affection
CHARACTERS: Narrator, Annie
BACKGROUND_IMAGE: annie_kiss.png
BACKGROUND_EDIT: "Annie blowing a kiss to Paul"

::SCRIPT::
- CHARACTER: Narrator
  LINE: On that she turns--for the first time, a coquettish look comes to her face. Catch this—
  EXPRESSION: null
- CHARACTER: ANNIE
  LINE: —ummmm-wahhhh.
  EXPRESSION: Grotesque

::PATHS::
- CHOICE: "Continue action"
  TARGET: paul_mimes_catch
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Bedroom Interior
MOOD: Deception
CHARACTERS: Narrator, Paul
BACKGROUND_IMAGE: paul_mimes_catch.png
BACKGROUND_EDIT: "Paul faking a smile and miming catching the kiss"

::SCRIPT::
- CHARACTER: Narrator
  LINE: CUT TO: PAUL, summoning up all his courage, as he mimes catching it and forces a smile on. She waves, closes the door. HOLD ON PAUL. The smile dies. He reaches in and pulls the two Novril capsules out of his mouth. Now--
  EXPRESSION: Cunning

::PATHS::
- CHOICE: "Continue action"
  TARGET: helicopter_sound
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Soundscape
MOOD: Ominous
CHARACTERS: Narrator
BACKGROUND_IMAGE: helicopter_sound.png
BACKGROUND_EDIT: "Sound implied, visual is black"

::SCRIPT::
- CHARACTER: Narrator
  LINE: CUT TO: THE SOUND OF A HELICOPTER
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue action"
  TARGET: inside_helicopter
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Inside Helicopter
MOOD: Searching
CHARACTERS: Narrator, Buster, Pilot
BACKGROUND_IMAGE: inside_helicopter.png
BACKGROUND_EDIT: "Interior of a helicopter, Buster using binoculars"

::SCRIPT::
- CHARACTER: Narrator
  LINE: INSIDE THE HELICOPTER BUSTER AND PILOT flying along. Buster is all bundled up as he stares out, using the binoculars...
  EXPRESSION:null

::PATHS::
- CHOICE: "Continue action"
  TARGET: shiny_reflection
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Open Area
MOOD: Revealing
CHARACTERS: Narrator
BACKGROUND_IMAGE: shiny_reflection.png
BACKGROUND_EDIT: "Bright reflection from something in the snow"

::SCRIPT::
- CHARACTER: Narrator
  LINE: SOMETHING SHINY reflecting the sun.
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue action"
  TARGET: mustang_revealed
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Open Area
MOOD: Discovery
CHARACTERS: Narrator, Buster
BACKGROUND_IMAGE: mustang_revealed.png
BACKGROUND_EDIT: "Close-up on part of Paul's Mustang, revealed by snow"

::SCRIPT::
- CHARACTER: Narrator
  LINE: HOLD AS IT ALMOST BLINDS US--we're looking at the part of Paul's Mustang that was revealed by the snow when Buster almost found the car.
  EXPRESSION: null
- CHARACTER: BUSTER
  LINE: Walter, we could be skipping lunch today.
  EXPRESSION: Focused

::PATHS::
- CHOICE: "Continue action"
  TARGET: crash_site
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Crash Site
MOOD: Recovery Operation
CHARACTERS: Narrator, Buster, State Policemen, Media
BACKGROUND_IMAGE: crash_site.png
BACKGROUND_EDIT: "Paul's car being hoisted by chains"

::SCRIPT::
- CHARACTER: Narrator
  LINE: CRASH SITE Paul's car being hoisted by chains from the ground and, as it starts to rise up into the afternoon air... PULL BACK TO REVEAL THE AREA BY THE CAR--BUSTER is there and a bunch of STATE POLICEMEN and various MEDIA PEOPLE are there--Buster stands with the STATE POLICE CHIEF watching as the car is hoisted via derrick; the sound of the powerful MOTOR lifting the car is enormous and as the car keeps rising higher and higher and PEOPLE take pictures and stare and
  EXPRESSION: Intense

::PATHS::
- CHOICE: "Continue action"
  TARGET: chief_addressing_reporters
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Crash Site
MOOD: Official Statement
CHARACTERS: Narrator, State Police Chief, Reporters, Buster
BACKGROUND_IMAGE: chief_addressing_reporters.png
BACKGROUND_EDIT: "Chief speaking to reporters, cold weather"

::SCRIPT::
- CHARACTER: Narrator
  LINE: THE STATE POLICE CHIEF is addressing maybe a dozen REPORTERS. It's very cold. BUSTER stands slightly away from the group.
  EXPRESSION: null
- CHARACTER: STATE POLICE CHIEF
  LINE: The presumption must now be that Paul Sheldon is dead. We know he somehow crawled out of his car. But we have been unable to locate his body in the vicinity of the crash. We also know if anyone had found him, they would have taken him to an area hospital. His body is undoubtedly out there buried somewhere in the snow. We'll find him after the first thaw unless the animals have gotten to him first. I'll take questions.
  EXPRESSION: Solemn
- CHARACTER: Narrator
  LINE: After the first sentence, a very cold and very unhappy BUSTER leaves the gathering.
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue action"
  TARGET: buster_studies_car
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Crash Site
MOOD: Suspicion
CHARACTERS: Narrator, Buster, Virginia
BACKGROUND_IMAGE: buster_studies_car.png
BACKGROUND_EDIT: "Buster studying Paul's car, focusing on dents"

::SCRIPT::
- CHARACTER: Narrator
  LINE: PAUL'S CAR as Buster studies it, especially the area by the driver's side where there are still dents visible from Annie's crowbar. VIRGINIA moves to him now. They exchange a glance, start walking together toward their car.
  EXPRESSION: Suspicious

::PATHS::
- CHOICE: "Continue action"
  TARGET: chief_surrounded
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Crash Site
MOOD: Media Frenzy
CHARACTERS: Narrator, Chief, Reporters
BACKGROUND_IMAGE: chief_surrounded.png
BACKGROUND_EDIT: "Chief answering questions from many reporters"

::SCRIPT::
- CHARACTER: Narrator
  LINE: THE CHIEF, surrounded--people are asking questions, raising hands for attention, and as he answers them--
  EXPRESSION: Chaotic

::PATHS::
- CHOICE: "Continue action"
  TARGET: buster_virginia_walking
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Crash Site
MOOD: Doubtful Conversation
CHARACTERS: Narrator, Buster, Virginia
BACKGROUND_IMAGE: buster_virginia_walking.png
BACKGROUND_EDIT: "Buster and Virginia walking towards their car"

::SCRIPT::
- CHARACTER: Narrator
  LINE: BUSTER AND VIRGINIA, close together, walking toward their car.
  EXPRESSION: null
- CHARACTER: VIRGINIA
  LINE: You don't think he’s dead, do you?
  EXPRESSION: Skeptical
- CHARACTER: BUSTER
  LINE: He might well be. But not the way they say. He didn't crawl out of that car by himself. You saw those dents on the door--someone pulled him out.
  EXPRESSION: Convinced
- CHARACTER: VIRGINIA
  LINE: It was an old car--those dents could have been there forever.
  EXPRESSION: Dismissive
- CHARACTER: BUSTER
  LINE: There's two kinds of people that drive around in old cars: the ones that can't afford new ones, and the ones who wouldn't give 'em up for anything in the world. That second bunch don’t drive a
  EXPRESSION: Assertive

::PATHS::
- CHOICE: "End Scene"
  TARGET: end
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Paul's Room
MOOD: Gloomy
CHARACTERS: Narrator, Paul
BACKGROUND_IMAGE: paul_room_night.png
BACKGROUND_EDIT: "Paul's dimly lit room at night, sound of TV"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Paul lies in bed listening to the strains of "The Love Connection," coming from upstairs. As Chuck Woolery drones on, Paul is intently involved in folding a piece of paper from his pad. He is making a container of some sort. He finishes, then reaches down and grabs the Novril capsules that he has been stashing in the mattress.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Carefully, he opens one and pours it into the palm of his hand. First he smells it--no odor--then he takes a tiny bit on a finger and tastes it--no taste. Then, he takes his paper container and empties the contents of all the pills into it, then places it under the mattress.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Now, what to do with the empty capsules. He thinks for a second, then--what the hell--he swallows them. He then places the packet back in the mattress.
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue"
  TARGET: typewriter_day
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: The Typewriter
MOOD: Foreboding
CHARACTERS: Narrator, Paul
BACKGROUND_IMAGE: typewriter_day.png
BACKGROUND_EDIT: "Daytime, typewriter visible with broken 'n', window behind it"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The window is visible behind it. From this angle, it almost seems to be staring at PAUL, broken "n" and all. PAUL tests his wounded arm. He’s able to raise it a few inches, but that’s it.
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue"
  TARGET: outside_window
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Outside the Window
MOOD: Ominous
CHARACTERS: Narrator, Annie, Misery
BACKGROUND_IMAGE: outside_window_day.png
BACKGROUND_EDIT: "Daytime, Annie heading for the barn with Misery the pig"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Annie is visible heading for the barn, followed by Misery, the pig. For a moment, she stops, turns to look back.
  EXPRESSION: null
- CHARACTER: Annie
  LINE: Don’t be nervous--
  EXPRESSION: NULL
- CHARACTER: Annie
  LINE: --just remember, I'll treasure whatever you do.
  EXPRESSION: NULL
- CHARACTER: Narrator
  LINE: Now, as she turns again, moves quickly away--
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue"
  TARGET: typewriter_scene
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: The Typewriter
MOOD: Focus
CHARACTERS: Narrator, Paul
BACKGROUND_IMAGE: typewriter_scene.png
BACKGROUND_EDIT: "Paul at the typewriter, rolling in a new sheet"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Paul. He rolls in a piece of paper, types briefly.
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue"
  TARGET: paul_writing
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: What He's Written
MOOD: Frustration
CHARACTERS: Narrator, Paul
BACKGROUND_IMAGE: paul_writing.png
BACKGROUND_EDIT: "Close up of paper with title and author"

::SCRIPT::
- CHARACTER: Narrator
  LINE: "Misery's Returs." By Paul Sheldon for Annie Wilkes.
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue"
  TARGET: paul_studying
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Paul
MOOD: Contemplation
CHARACTERS: Narrator, Paul
BACKGROUND_IMAGE: paul_contemplating.png
BACKGROUND_EDIT: "Paul studying the paper, then removing it"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Paul, studying the paper. He takes it out, starts to roll in a new sheet.
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue"
  TARGET: machine_new_sheet
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: The Machine
MOOD: Anticipation
CHARACTERS: Narrator, Paul
BACKGROUND_IMAGE: machine_new_sheet.png
BACKGROUND_EDIT: "The typewriter rolling in a new sheet of paper"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The machine as the new sheet is rolled in.
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue"
  TARGET: paul_staring
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Paul
MOOD: Hesitation
CHARACTERS: Narrator, Paul
BACKGROUND_IMAGE: paul_staring.png
BACKGROUND_EDIT: "Paul staring at a blank page, glancing outside"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Paul, staring at the blank page. He takes a deep breath, glances outside, then back to the paper.
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue"
  TARGET: blank_page
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: The Blank Page
MOOD: Blankness
CHARACTERS: Narrator
BACKGROUND_IMAGE: blank_page.png
BACKGROUND_EDIT: "A close-up of a blank page in the typewriter"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The blank page.
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue"
  TARGET: paul_typing_burst
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Paul
MOOD: Urgency
CHARACTERS: Narrator, Paul
BACKGROUND_IMAGE: paul_typing_burst.png
BACKGROUND_EDIT: "Paul typing a burst of words, staring at the result"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Paul, and now there’s a brief light behind his eyes and suddenly he types a burst, stares at what he's written.
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue"
  TARGET: paper_curse_words
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: The Paper
MOOD: Expletive
CHARACTERS: Narrator
BACKGROUND_IMAGE: paper_curse_words.png
BACKGROUND_EDIT: "Close-up of the paper with 'fuckfuckfuckfuckfuck.'"

::SCRIPT::
- CHARACTER: Narrator
  LINE: "fuckfuckfuckfuckfuck."
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue"
  TARGET: paul_muttering
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Paul
MOOD: Resignation
CHARACTERS: Narrator, Paul
BACKGROUND_IMAGE: paul_muttering.png
BACKGROUND_EDIT: "Paul closing his eyes briefly, muttering, then grabbing a new paper"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Paul. He closes his eyes briefly, mutters something, kind of nods, opens his eyes, grabs for another piece of paper, rolls it in and starts mechanically to type.
  EXPRESSION: null

::PATHS::
- CHOICE: "Dissolve"
  TARGET: new_paper_chapter
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: New Piece of Paper
MOOD: Beginning
CHARACTERS: Narrator
BACKGROUND_IMAGE: new_paper_chapter.png
BACKGROUND_EDIT: "A new piece of paper with 'Chapter Two' and a half paragraph"

::SCRIPT::
- CHARACTER: Narrator
  LINE: A new piece of paper with the words "Chapter Two" and a half paragraph of writing as we
  EXPRESSION: null

::PATHS::
- CHOICE: "Pull back"
  TARGET: paul_working_dusk
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Paul Working in his Room
MOOD: Dusk
CHARACTERS: Narrator, Paul, Annie
BACKGROUND_IMAGE: paul_working_dusk.png
BACKGROUND_EDIT: "Paul working at his desk, Annie entering with manuscript pages at dusk"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Paul working in his room. Annie enters, the first pages of manuscript in her hands. It's dusk.
  EXPRESSION: null
- CHARACTER: Annie
  LINE: I'm sorry, Paul. This is all wrong, you’ll have to do it over again.
  EXPRESSION: Disappointed
- CHARACTER: Paul
  LINE: What? What happened to "I’ll treasure whatever you do?"
  EXPRESSION: Stunned
- CHARACTER: Annie
  LINE: Paul, it's not worthy of you. Throw it all out except for the part of naming that gravedigger after me. You can leave that in.
  EXPRESSION: Firm
- CHARACTER: Paul
  LINE: I really value your criticism, but maybe you're being a little hasty here.
  EXPRESSION: Defensive
- CHARACTER: Annie
  LINE: Paul, what you've written just isn't fair.
  EXPRESSION: Accusatory
- CHARACTER: Paul
  LINE: --not fair?
  EXPRESSION: Confused
- CHARACTER: Annie
  LINE: That’s right--when I was growing up in Bakersfield, my favorite thing in all the world was to go to the movies on Saturday afternoons for the chapter plays...
  EXPRESSION: Nostalgic
- CHARACTER: Paul
  LINE: --cliff-hangers--
  EXPRESSION: Realizing
- CHARACTER: Annie
  LINE: I know that, Mister Man--they also call them serials. I'm not stupid, you know.
  EXPRESSION: Annoyed
- CHARACTER: Annie
  LINE: Anyway, my favorite was Rocket Man, and once it was a no-brakes chapter, the bad guys stuck him in a car on a mountain road and knocked him out and welded the doors shut and tore out the brakes and started him to his death and he woke up and tried to steer and tried to get out, but the car went off a cliff before he could escape and it crashed and burned and--I was so upset and excited and the next week you better believe I was first in line and they always start with the end of the last week and there was Rocket Man trying to get out, and here came the cliff and JUST BEFORE the car went off he jumped free and all the kids cheered--
  EXPRESSION: Excited
- CHARACTER: Annie
  LINE: --but I didn't cheer, I stood right up and started shouting, "This isn't what happened last week--have you all got amnesia?--THEY 3UST CHEATED US--THIS WASN'T FAIR--"
  EXPRESSION: Outraged
- CHARACTER: Annie
  LINE: CLOSE UP. Still in her childhood reverie. Shouting: "HE DIDN'T GET OUT OF THE COCKADOODIE CAR!"
  EXPRESSION: Furious
- CHARACTER: Paul
  LINE: They always cheated like that in cliff— --chapter plays.
  EXPRESSION: Self-correcting
- CHARACTER: Annie
  LINE: But not you. Not with my Misery. Remember, Ian did ride for Dr. Cleary at the end of the last book, but his horse fell jumping that fence and Ian broke his shoulder and his ribs and lay there all night in the ditch so he never reached the doctor, so there couldn't have been any "experimental blood transfusion" that saved her life. Misery was buried in the ground at the end, Paul, so you’ll have to start there.
  EXPRESSION: Stern
- CHARACTER: Narrator
  LINE: As she goes--
  EXPRESSION: null
- CHARACTER: Paul
  LINE: Look at this, I've got Lizzie Borden for an editor, here.
  EXPRESSION: Sarcastic
- CHARACTER: Narrator
  LINE: Paul slumps, staring barefully at the typewriter.
  EXPRESSION: Defeated

::PATHS::
- CHOICE: "Dissolve"
  TARGET: outside_farmhouse_night
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Outside the Farmhouse
MOOD: Transition
CHARACTERS: Narrator
BACKGROUND_IMAGE: farmhouse_night.png
BACKGROUND_EDIT: "Nighttime, exterior of the farmhouse"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Dissolve to:
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue"
  TARGET: outside_farmhouse_morning
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Outside the Farmhouse
MOOD: Morning
CHARACTERS: Narrator
BACKGROUND_IMAGE: farmhouse_morning.png
BACKGROUND_EDIT: "Morning, exterior of the farmhouse"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Dissolve to:
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue"
  TARGET: paul_room_day
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Paul's Room
MOOD: Deceptive Calm
CHARACTERS: Narrator, Paul, Annie
BACKGROUND_IMAGE: paul_room_day.png
BACKGROUND_EDIT: "Daytime, Paul at the table, Novril capsules on breakfast tray"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Paul is at the table. He takes the Novril off his breakfast tray, wheels over to the bed, and stuffs them into the mattress. He hears FOOTSTEPS coming down the hall. He smoothly wheels back to the table. A pause.
  EXPRESSION: null
- CHARACTER: Annie
  LINE: What’s the matter, Paul? You haven't written a word.
  EXPRESSION: Concerned
- CHARACTER: Paul
  LINE: I can't write this anymore.
  EXPRESSION: Resigned
- CHARACTER: Annie
  LINE: Don’t be silly. Of course you can.
  EXPRESSION: Encouraging
- CHARACTER: Paul
  LINE: I'm telling you, I can't.
  EXPRESSION: Firm
- CHARACTER: Annie
  LINE: You can--you have the "gotta"--
  EXPRESSION: Assertive
- CHARACTER: Paul
  LINE: The what?
  EXPRESSION: Confused
- CHARACTER: Annie
  LINE: The "gotta." Remember, you talked about it in Playboy magazine. You said there’s a million things you can't do in this world; you can't hit a curve ball, you can’t fix a leaky faucet or make a marriage work— but there’s one thing you always have, and that's the power of the "gotta."
  EXPRESSION: Explaining
- CHARACTER: Paul
  LINE: I said that?
  EXPRESSION: Surprised
- CHARACTER: Annie
  LINE: You said you can make it so they gotta turn the page. You know, "I 'gotta' know will she live," "I 'gotta' know will he catch the killer." "I gotta see how this chapter ends." You said it. I don’t
  EXPRESSION: Emphatic

::PATHS::
- CHOICE: "Continue"
  TARGET: end_scene
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Not Specified
MOOD: Neutral
CHARACTERS: Narrator, Paul, Annie
BACKGROUND_IMAGE: null
BACKGROUND_EDIT: null

::SCRIPT::
- CHARACTER: Narrator
  LINE: usually buy that magazine. I only got it, 'cause they were interviewing you.
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue"
  TARGET: paul_dialogue
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Not Specified
MOOD: Pensive
CHARACTERS: Paul, Annie
BACKGROUND_IMAGE: close_up_paul.png
BACKGROUND_EDIT: "Close up on Paul's face, blinking"

::SCRIPT::
- CHARACTER: Paul
  LINE: What about a bee...?
  EXPRESSION: Pensive
- CHARACTER: Annie
  LINE: What?
  EXPRESSION: Confused
- CHARACTER: Paul
  LINE: Nothing.
  EXPRESSION: Neutral

::PATHS::
- CHOICE: "Continue"
  TARGET: keyboard_scene
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Not Specified
MOOD: Focused
CHARACTERS: Narrator, Annie, Paul
BACKGROUND_IMAGE: keyboard.png
BACKGROUND_EDIT: "A keyboard; a piece of paper slides in and keys move"

::SCRIPT::
- CHARACTER: Narrator
  LINE: THE KEYBOARD as the piece of paper slides in and the keys start to move. Annie stands there for a moment, then quietly backs out of the room.
  EXPRESSION: null

::PATHS::
- CHOICE: "Dissolve to next scene"
  TARGET: window_scene
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Window
MOOD: Anticipation
CHARACTERS: Narrator, Paul, Annie
BACKGROUND_IMAGE: late_afternoon_window.png
BACKGROUND_EDIT: "Late afternoon light through a window"

::SCRIPT::
- CHARACTER: Narrator
  LINE: THE WINDOW. It’s late afternoon. PULL BACK TO REVEAL PAUL in the wheelchair watching as ANNIE finishes reading.
  EXPRESSION: null
- CHARACTER: Paul
  LINE: Well, is it fair? Should I keep going?
  EXPRESSION: Hopeful
- CHARACTER: Annie
  LINE: You better. Oh, Paul, when Ian realized that the reason they’d buried Misery alive was because the bee sting had put her in that temporary coma--
  EXPRESSION: Excited

::PATHS::
- CHOICE: "Continue"
  TARGET: annie_fervor
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Not Specified
MOOD: Fervent
CHARACTERS: Annie, Narrator
BACKGROUND_IMAGE: annie_fervor.png
BACKGROUND_EDIT: "Annie speaking with great passion"

::SCRIPT::
- CHARACTER: Annie
  LINE: --and when Gravedigger Wilkes remembered how thirty years earlier, the same thing had happened to Lady Evelyn-Hyde— --and then old Dr. Cleary deduced that Misery must be Lady Evelyn-Hyde’s long-lost daughter because of the rarity of deadly bee-stings-- my heart just leapt.
  EXPRESSION: Fervent

::PATHS::
- CHOICE: "Cut to Paul"
  TARGET: paul_watching
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Not Specified
MOOD: Detached
CHARACTERS: Paul, Narrator
BACKGROUND_IMAGE: paul_watching_annie.png
BACKGROUND_EDIT: "Paul watching Annie, as if detached from her reading"

::SCRIPT::
- CHARACTER: Narrator
  LINE: PAUL, watching her. It’s as if he had nothing to do with anything she’d read as she goes on.
  EXPRESSION: Neutral
- CHARACTER: Annie
  LINE: I've known from the very first book that Misery had to be born of nobility and I was right!
  EXPRESSION: Triumphant
- CHARACTER: Paul
  LINE: Yeah, yeah...
  EXPRESSION: Mumbling

::PATHS::
- CHOICE: "Cut to both of them"
  TARGET: annie_touches_pages
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Not Specified
MOOD: Reverent
CHARACTERS: Annie, Paul, Narrator
BACKGROUND_IMAGE: annie_touches_pages.png
BACKGROUND_EDIT: "Annie touching pages like gold, Paul watching"

::SCRIPT::
- CHARACTER: Narrator
  LINE: THE TWO OF THEM; she touches the pages as if they were gold, rubbing gently with the tips of her fingers.
  EXPRESSION: null
- CHARACTER: Annie
  LINE: Oh, Paul, can I read each chapter when you finish? I can fill in the "n"s. Will she be her old self, now that Ian has dug her out, or will she have amnesia...?
  EXPRESSION: Eager
- CHARACTER: Paul
  LINE: ...have to wait.
  EXPRESSION: Neutral
- CHARACTER: Annie
  LINE: Will she still love him with that special perfect love?
  EXPRESSION: Pleading
- CHARACTER: Paul
  LINE: Have to wait.
  EXPRESSION: Neutral
- CHARACTER: Annie
  LINE: Not even a hint?
  EXPRESSION: Pleading
- CHARACTER: Paul
  LINE: Paul shakes his head.
  EXPRESSION: Neutral

::PATHS::
- CHOICE: "Cut to Annie spinning"
  TARGET: annie_spinning
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Not Specified
MOOD: Joyful
CHARACTERS: Annie, Narrator
BACKGROUND_IMAGE: annie_spinning.png
BACKGROUND_EDIT: "Annie spinning around the room like a happy child"

::SCRIPT::
- CHARACTER: Narrator
  LINE: ANNIE, spinning around the room like a happy child.
  EXPRESSION: null
- CHARACTER: Annie
  LINE: Misery’s alive! Misery's alive. Oh, it's so romantic--this whole house is going to be filled with romance. I'm going to put on my Liberace records-- you do like Liberace, don’t you?
  EXPRESSION: Ecstatic
- CHARACTER: Paul
  LINE: Whenever he played Radio City, who do you think was right there in the front row?
  EXPRESSION: Enthusiastic
- CHARACTER: Annie
  LINE: I'm going to play my records all day LONG --to inspire you--he's my all-time favorite.
  EXPRESSION: Enthusiastic

::PATHS::
- CHOICE: "Paul calls Annie back"
  TARGET: paul_invitation
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Not Specified
MOOD: Hopeful
CHARACTERS: Paul, Annie
BACKGROUND_IMAGE: annie_at_door.png
BACKGROUND_EDIT: "Annie stops at the door, looking back at Paul"

::SCRIPT::
- CHARACTER: Paul
  LINE: Annie?
  EXPRESSION: Hopeful
- CHARACTER: Annie
  LINE: She can't speak.
  EXPRESSION: Speechless
- CHARACTER: Paul
  LINE: Would you have dinner with me tonight? To celebrate Misery's return. I couldn't have done it without you.
  EXPRESSION: Sincere
- CHARACTER: Annie
  LINE: Oh, Paul. It would be an honor.
  EXPRESSION: Overjoyed

::PATHS::
- CHOICE: "Annie dashes out, Paul's action"
  TARGET: paul_novril
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Not Specified
MOOD: Deceptive
CHARACTERS: Narrator, Paul
BACKGROUND_IMAGE: paul_novril_packet.png
BACKGROUND_EDIT: "Paul wheels to the bed, pulls out Novril packet"

::SCRIPT::
- CHARACTER: Narrator
  LINE: ANNIE dashes excitedly out of the room. PAUL wheels over to the bed, pulls the packet of Novril powder out from the mattress and stuffs it in his pants. The sound of Liberace playing "Tammy" with orchestra and chorus booms in from beyond the door.
  EXPRESSION: null
- CHARACTER: Paul
  LINE: Jesus Christ.
  EXPRESSION: Annoyed

::PATHS::
- CHOICE: "Cut to Buster's office"
  TARGET: buster_office_intro
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Buster's Office
MOOD: Busy
CHARACTERS: Narrator, Virginia, Buster
BACKGROUND_IMAGE: buster_office_dusk.png
BACKGROUND_EDIT: "Dusk light in Buster's office"

::SCRIPT::
- CHARACTER: Narrator
  LINE: INT. BUSTER’S OFFICE - DUSK
  EXPRESSION: null
- CHARACTER: Virginia
  LINE: No, he's not here. I don't know where he went. He never tells me anything anymore. He's probably out having an affair somewhere. Wait a minute. I think I hear him coming.
  EXPRESSION: Agitated
- CHARACTER: Narrator
  LINE: BUSTER enters carrying a bagful of books.
  EXPRESSION: null
- CHARACTER: Virginia
  LINE: It’s Jim Taylor. He wants to know who you've been having an affair with.
  EXPRESSION: Teasing

::PATHS::
- CHOICE: "Cut to Buster on phone"
  TARGET: buster_phone_call
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Buster's Office
MOOD: Casual
CHARACTERS: Buster, Virginia, Narrator
BACKGROUND_IMAGE: buster_phone.png
BACKGROUND_EDIT: "Buster on the phone, Virginia looking through books"

::SCRIPT::
- CHARACTER: Narrator
  LINE: busier. He puts the bag down, shoots Virginia a look and grabs the phone. VIRGINIA looks in the bag.
  EXPRESSION: null
- CHARACTER: Buster
  LINE: Hey, Jim, what's doing? Uh-huh... uh-huh... Jim, we've been over this. If you’re gonna have benches in front of your store, people are gonna sit on them. I don't like him either, but I'm not going to come over there and tell him to move. Give my best to Denise. Bye.
  EXPRESSION: Patient
- CHARACTER: Virginia
  LINE: Well, whoever she is, she sure likes to read a lot.
  EXPRESSION: Amused
- CHARACTER: Buster
  LINE: Virginia, I'm flattered you think I got that much energy. I just figured if I can't find Paul Sheldon, at least I can find out what he wrote about.
  EXPRESSION: Dry
- CHARACTER: Virginia
  LINE: What do you expect to find? A story about a guy who drove his car off a cliff in a snowstorm?
  EXPRESSION: Sarcastic
- CHARACTER: Buster
  LINE: Now, you see, it's that kind of sarcasm that's given our marriage real spice.
  EXPRESSION: Wry

::PATHS::
- CHOICE: "Cut to study at night"
  TARGET: study_night_intro
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Study
MOOD: Romantic
CHARACTERS: Narrator, Paul, Annie
BACKGROUND_IMAGE: study_dinner.png
BACKGROUND_EDIT: "Study table set for a romantic dinner"

::SCRIPT::
- CHARACTER: Narrator
  LINE: STUDY. NIGHT. PAUL is sitting at a table that Annie has set up with her best china and silverware. It is as romantic as Annie Wilkes gets. ANNIE enters, carrying a basket of rolls. She sits and serves Paul.
  EXPRESSION: null
- CHARACTER: Annie
  LINE: I hope you like it.
  EXPRESSION: Hopeful
- CHARACTER: Paul
  LINE: It looks wonderful. And so do you.
  EXPRESSION: Appreciative

::PATHS::
- CHOICE: "They eat"
  TARGET: paul_meatloaf
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Study
MOOD: Awkward
CHARACTERS: Paul, Annie, Narrator
BACKGROUND_IMAGE: dinner_awkward.png
BACKGROUND_EDIT: "Paul and Annie eating in awkward silence"

::SCRIPT::
- CHARACTER: Narrator
  LINE: They eat in awkward silence. Finally:
  EXPRESSION: null
- CHARACTER: Paul
  LINE: I've never had meatloaf this good, what do you do to it?
  EXPRESSION: Curious
- CHARACTER: Annie
  LINE: My secret is I only use fresh tomatoes, never canned. And to give it that little extra zip, I mix in some Spam with the ground beef.
  EXPRESSION: Proud
- CHARACTER: Paul
  LINE: Oh. You can't get this in a restaurant in New York.
  EXPRESSION: Neutral

::PATHS::
- CHOICE: "Paul suggests a toast"
  TARGET: paul_toast
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Study
MOOD: Festive
CHARACTERS: Paul, Annie, Narrator
BACKGROUND_IMAGE: toast_planning.png
BACKGROUND_EDIT: "Paul suggests a toast, Annie agrees"

::SCRIPT::
- CHARACTER: Narrator
  LINE: After another pause:
  EXPRESSION: null
- CHARACTER: Paul
  LINE: Annie, I think we should have a toast.
  EXPRESSION: Suggestive
- CHARACTER: Annie
  LINE: A toast?
  EXPRESSION: Eager
- CHARACTER: Paul
  LINE: Yes, to Misery. Let me pour you some more wine.
  EXPRESSION: Enthusiastic
- CHARACTER: Annie
  LINE: To Misery.
  EXPRESSION: Excited
- CHARACTER: Paul
  LINE: Wait, let's do this right. Do you have any candles?
  EXPRESSION: Thoughtful
- CHARACTER: Annie
  LINE: Oh, I don't know. I think so. I'll go look.
  EXPRESSION: Eager

::PATHS::
- CHOICE: "Annie goes to look, Paul's action"
  TARGET: paul_novril_wine
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Study
MOOD: Deceptive
CHARACTERS: Narrator, Paul, Annie
BACKGROUND_IMAGE: paul_novril_wine.png
BACKGROUND_EDIT: "Paul empties Novril into Annie's wine glass"

::SCRIPT::
- CHARACTER: Narrator
  LINE: She exits into the kitchen. PAUL quickly pulls the packet filled with Novril powder from his pants. He empties it into her glass of wine, stuffs the empty packet back into his pants, talking the whole time:
  EXPRESSION: null
- CHARACTER: Paul
  LINE: Did you study decorating, or do you just have a flair?
  EXPRESSION: Casual
- CHARACTER: Annie
  LINE: Oh, you. I just picked things up over the years.
  EXPRESSION: Flustered
- CHARACTER: Paul
  LINE: Well, it certainly says you.
  EXPRESSION: Appreciative
- CHARACTER: Annie
  LINE: You really think so?
  EXPRESSION: Delighted
- CHARACTER: Paul
  LINE: Absolutely. Listen, if you can't find any, it's okay. I just thought it might be nice.
  EXPRESSION: Insistent
- CHARACTER: Narrator
  LINE: ANNIE re-enters with a candle.
  EXPRESSION: null
- CHARACTER: Annie
  LINE: Are you kidding? If anyone ever told me that one day I’d be having a candlelit dinner with Paul Sheldon in my own house, I woulda checked both legs to see which one was being pulled. Will this do?
  EXPRESSION: Overjoyed
- CHARACTER: Paul
  LINE: It's perfect.
  EXPRESSION: Smooth
- CHARACTER: Narrator
  LINE: She places the candle on the table. With a slight tremor in her hand, she lights the candle. PAUL raises his glass.
  EXPRESSION: null
- CHARACTER: Paul
  LINE: To Misery and Annie Wilkes, who brought her back to life.
  EXPRESSION: Sincere
- CHARACTER: Annie
  LINE: Oh, Paul, every time I think about it, I get goosebumps.
  EXPRESSION: Emotional

::PATHS::
- CHOICE: "End Scene"
  TARGET: end
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Unknown
MOOD: Tension
CHARACTERS: Narrator, Annie, Paul
BACKGROUND_IMAGE: null
BACKGROUND_EDIT: null

::SCRIPT::
- CHARACTER: Narrator
  LINE: y clink glasses.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: And with that, her emotions having gotten the best of her, she knocks over the candle. In trying to right the situation she places her glass back down, and as she reaches for the candle, she knocks over her glass, spilling the wine.
  EXPRESSION: null
- CHARACTER: Annie
  LINE: Oh, God, what have I done? I'm so sorry, Paul. I ruined your beautiful toast. Will you ever forgive me? Here, let me pour another one.
  EXPRESSION: Distressed
- CHARACTER: Narrator
  LINE: (she does)
  EXPRESSION: null
- CHARACTER: Annie
  LINE: Can we pretend this never happened? To Misery?
  EXPRESSION: Hopeful
- CHARACTER: Paul
  LINE: To Misery.
  EXPRESSION: Resigned
- CHARACTER: Narrator
  LINE: So they drink their wine.

::PATHS::
- CHOICE: Continue
  TARGET: outside_farmhouse
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Outside the Farmhouse
MOOD: Progress
CHARACTERS: Narrator
BACKGROUND_IMAGE: outside_farmhouse.png
BACKGROUND_EDIT: "Snow has melted somewhat, daytime"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The snow, although still present, has melted somewhat. And starting now and continuing throughout is this: the sound of typing.

::PATHS::
- CHOICE: Continue
  TARGET: paul_room_typing
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Paul's Room
MOOD: Focus
CHARACTERS: Narrator, Paul
BACKGROUND_IMAGE: paul_room.png
BACKGROUND_EDIT: "Daytime, Paul at typewriter"

::SCRIPT::
- CHARACTER: Narrator
  LINE: PAUL, working at his typewriter.

::PATHS::
- CHOICE: Continue
  TARGET: manuscript_growing
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: The Manuscript
MOOD: Progress
CHARACTERS: Narrator
BACKGROUND_IMAGE: manuscript.png
BACKGROUND_EDIT: "Pages of manuscript growing"

::SCRIPT::
- CHARACTER: Narrator
  LINE: THE MANUSCRIPT. Growing.

::PATHS::
- CHOICE: Continue
  TARGET: annies_bedroom_dusk
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Annie's Bedroom
MOOD: Contentment
CHARACTERS: Narrator, Annie
BACKGROUND_IMAGE: annies_bedroom.png
BACKGROUND_EDIT: "Dusk, Annie reading"

::SCRIPT::
- CHARACTER: Narrator
  LINE: ANNIE, in her room. Reading and loving it.

::PATHS::
- CHOICE: Continue
  TARGET: busters_den_night
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Buster's Den
MOOD: Comfort
CHARACTERS: Narrator, Buster, Virginia
BACKGROUND_IMAGE: busters_den.png
BACKGROUND_EDIT: "Nighttime, Buster by fire with book"

::SCRIPT::
- CHARACTER: Narrator
  LINE: BUSTER sitting in his den reading a Misery novel by the fire. VIRGINIA brings him a cup of tea.

::PATHS::
- CHOICE: Continue
  TARGET: paul_room_day_improved_arm
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Paul's Room
MOOD: Recovery
CHARACTERS: Narrator, Paul
BACKGROUND_IMAGE: paul_room_day.png
BACKGROUND_EDIT: "Daytime, Paul's arm is out of sling, improved mobility"

::SCRIPT::
- CHARACTER: Narrator
  LINE: PAUL, the sling off, moving his injured arm. It’s more mobile than before. Testing his strength, he uses his arm to remove the page and place it on the pile. He puts in another page and continues to type.

::PATHS::
- CHOICE: Continue
  TARGET: annie_enters_paul_room
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Paul's Room
MOOD: Approval
CHARACTERS: Narrator, Annie, Paul
BACKGROUND_IMAGE: paul_room_annie_enters.png
BACKGROUND_EDIT: "Daytime, Annie entering Paul's room with chapter and tea"

::SCRIPT::
- CHARACTER: Narrator
  LINE: ANNIE, entering Paul’s room, carrying a chapter. Handing him a cup of tea.
- CHARACTER: Annie
  LINE: Paul, this is positively the best Misery you’ve ever written.
  EXPRESSION: Enthusiastic
- CHARACTER: Paul
  LINE: I think you're right.
  EXPRESSION: Confident

::PATHS::
- CHOICE: Continue
  TARGET: pile_of_paper_bigger
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: The Pile of Paper
MOOD: Progress
CHARACTERS: Narrator
BACKGROUND_IMAGE: manuscript_pile_bigger.png
BACKGROUND_EDIT: "Pile of paper is larger"

::SCRIPT::
- CHARACTER: Narrator
  LINE: THE PILE OF PAPER. Bigger.

::PATHS::
- CHOICE: Continue
  TARGET: outside_barn
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Outside the Barn
MOOD: Observation
CHARACTERS: Narrator, Annie, Paul
BACKGROUND_IMAGE: outside_barn.png
BACKGROUND_EDIT: "Daytime, Annie looking at the house"

::SCRIPT::
- CHARACTER: Narrator
  LINE: ANNIE, out by the barn. She stares in at the house. Framed in the window is PAUL, working. She smiles, enters the barn.

::PATHS::
- CHOICE: Continue
  TARGET: paul_room_night_stretching
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Paul's Room
MOOD: Diligence
CHARACTERS: Narrator, Paul
BACKGROUND_IMAGE: paul_room_night_stretching.png
BACKGROUND_EDIT: "Nighttime, Paul briefly stretching before typing"

::SCRIPT::
- CHARACTER: Narrator
  LINE: He stretches but only briefly, then back to his typing.

::PATHS::
- CHOICE: Continue
  TARGET: kitchen_cooking
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: The Kitchen
MOOD: Happiness
CHARACTERS: Narrator, Annie
BACKGROUND_IMAGE: kitchen_cooking.png
BACKGROUND_EDIT: "Daytime, Annie cooking and reading"

::SCRIPT::
- CHARACTER: Narrator
  LINE: ANNIE, cooking happily away, reading a chapter.

::PATHS::
- CHOICE: Continue
  TARGET: paul_room_lifting_typewriter
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Paul's Room
MOOD: Effort
CHARACTERS: Narrator, Paul
BACKGROUND_IMAGE: paul_room_lifting_typewriter.png
BACKGROUND_EDIT: "Daytime, Paul attempting to lift typewriter out of sling"

::SCRIPT::
- CHARACTER: Narrator
  LINE: PAUL, arm out of the sling. He manages to lift the typewriter once, sets it back down, puts the sling back on.

::PATHS::
- CHOICE: Continue
  TARGET: paul_room_later_tray
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Paul's Room
MOOD: Appreciation
CHARACTERS: Narrator, Annie, Paul
BACKGROUND_IMAGE: paul_room_later_tray.png
BACKGROUND_EDIT: "Later, Annie bringing a tray of food"

::SCRIPT::
- CHARACTER: Narrator
  LINE: ANNIE, bringing a tray of food.
- CHARACTER: Annie
  LINE: I think it’s so wonderful that Misery would sacrifice her title to take up the cause of her people. That’s true nobility.
  EXPRESSION: Admiring
- CHARACTER: Narrator
  LINE: Paul hands her some new pages. As she exits,

::PATHS::
- CHOICE: Continue
  TARGET: busters_office
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Buster's Office
MOOD: Solitude
CHARACTERS: Narrator, Buster
BACKGROUND_IMAGE: busters_office.png
BACKGROUND_EDIT: "Daytime, Buster alone in his office reading"

::SCRIPT::
- CHARACTER: Narrator
  LINE: BUSTER, in his office reading. He is alone.

::PATHS::
- CHOICE: Continue
  TARGET: annies_living_room_night
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Annie's Living Room
MOOD: Companionship
CHARACTERS: Narrator, Annie
BACKGROUND_IMAGE: annies_living_room_night.png
BACKGROUND_EDIT: "Nighttime, Annie reading by the fire with her pig"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Annie is reading by the fire. Her pig Misery sits beside her, staring at the pages.

::PATHS::
- CHOICE: Continue
  TARGET: paul_room_day_fast_typing
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Paul's Room
MOOD: Intense Focus
CHARACTERS: Narrator, Paul
BACKGROUND_IMAGE: paul_room_day_fast_typing.png
BACKGROUND_EDIT: "Daytime, Paul typing with extreme speed"

::SCRIPT::
- CHARACTER: Narrator
  LINE: His fingers just fly, faster than he’s ever typed and

::PATHS::
- CHOICE: Continue
  TARGET: paul_room_night_staring
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Paul's Room
MOOD: Contemplation
CHARACTERS: Narrator, Paul
BACKGROUND_IMAGE: paul_room_night_staring.png
BACKGROUND_EDIT: "Nighttime, Paul staring"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Paul, staring and

::PATHS::
- CHOICE: Continue
  TARGET: pile_growing
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: The Pile
MOOD: Immense Progress
CHARACTERS: Narrator
BACKGROUND_IMAGE: manuscript_pile_growing.png
BACKGROUND_EDIT: "Pile of manuscript is growing significantly"

::SCRIPT::
- CHARACTER: Narrator
  LINE: THE PILE, growing, growing and

::PATHS::
- CHOICE: Continue
  TARGET: pauls_fingers
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Paul's Fingers
MOOD: Speed
CHARACTERS: Narrator
BACKGROUND_IMAGE: pauls_fingers.png
BACKGROUND_EDIT: "Close up on Paul's fast-moving fingers"

::SCRIPT::
- CHARACTER: Narrator
  LINE: PAUL'S FINGERS

::PATHS::
- CHOICE: Continue
  TARGET: paul_room_new_ream
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Paul's Room
MOOD: Dedication
CHARACTERS: Narrator, Paul
BACKGROUND_IMAGE: paul_room_new_ream.png
BACKGROUND_EDIT: "Daytime, Paul opening a new ream of paper"

::SCRIPT::
- CHARACTER: Narrator
  LINE: PAUL, ripping open a new ream of paper...

::PATHS::
- CHOICE: Continue
  TARGET: paul_room_dusk_silent_nod
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Paul's Room
MOOD: Absorption
CHARACTERS: Narrator, Paul
BACKGROUND_IMAGE: paul_room_dusk_silent_nod.png
BACKGROUND_EDIT: "Dusk, Paul nodding silently, absorbed"

::SCRIPT::
- CHARACTER: Narrator
  LINE: His lips move silently. He's not even aware of it as he nods and...

::PATHS::
- CHOICE: Continue
  TARGET: typewriter_writing
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: The Paper in the Typewriter
MOOD: Creation
CHARACTERS: Narrator
BACKGROUND_IMAGE: typewriter_writing.png
BACKGROUND_EDIT: "Close up of paper being written on by typewriter"

::SCRIPT::
- CHARACTER: Narrator
  LINE: THE PAPER IN THE TYPEWRITER, line after line being written.

::PATHS::
- CHOICE: Continue
  TARGET: intercut_storm
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Storm
MOOD: Ominous
CHARACTERS: Narrator
BACKGROUND_IMAGE: storm.png
BACKGROUND_EDIT: "Lightning and thunder with rain starting"

::SCRIPT::
- CHARACTER: Narrator
  LINE: INTERCUT WITH: Lightning! Giant deep rolls of THUNDER as RAIN begins...

::PATHS::
- CHOICE: Continue
  TARGET: typewriter_lifted
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Typewriter
MOOD: Frantic Activity
CHARACTERS: Narrator
BACKGROUND_IMAGE: typewriter_lifted.png
BACKGROUND_EDIT: "Typewriter being lifted and put down repeatedly"

::SCRIPT::
- CHARACTER: Narrator
  LINE: TYPEWRITER being lifted out of frame, then back in, then out again.

::PATHS::
- CHOICE: Continue
  TARGET: paul_room_night_doubled_pile
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Paul's Room
MOOD: Exhaustion and Effort
CHARACTERS: Narrator, Paul
BACKGROUND_IMAGE: paul_room_night_doubled_pile.png
BACKGROUND_EDIT: "Nighttime, manuscript pile doubled, Paul struggling with typewriter"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The pile of manuscript has doubled. Maybe two hundred pages. PAUL, with some effort, is pumping the typewriter up and down. Finally, he places it back down and puts his arm back in the sling.

::PATHS::
- CHOICE: Continue
  TARGET: paul_looks_outside
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Paul
MOOD: Brief Interruption
CHARACTERS: Narrator, Paul
BACKGROUND_IMAGE: paul_looks_outside.png
BACKGROUND_EDIT: "Paul briefly looking outside"

::SCRIPT::
- CHARACTER: Narrator
  LINE: PAUL, looking outside briefly.

::PATHS::
- CHOICE: Continue
  TARGET: rain_worse
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Rain
MOOD: Intense Storm
CHARACTERS: Narrator
BACKGROUND_IMAGE: rain_worse.png
BACKGROUND_EDIT: "Heavy rain hitting the house"

::SCRIPT::
- CHARACTER: Narrator
  LINE: THE RAIN. Worse. The SOUND hit s the roof of the house, hits the window.

::PATHS::
- CHOICE: Continue
  TARGET: annie_enters_despondent
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Paul's Room
MOOD: Despair
CHARACTERS: Narrator, Annie, Paul
BACKGROUND_IMAGE: annie_enters_despondent.png
BACKGROUND_EDIT: "Nighttime, Annie enters Paul's room looking lifeless and robotic"

::SCRIPT::
- CHARACTER: Narrator
  LINE: ANNIE, lumbering in--she's never looked like this: She’s wearing her slippers and her pink quilted housecoat. Her eyes are without life. Her hair, loose and straggly, hangs around her face. Slowly, like a robot, she goes to PAUL, who looks silently up at her.
- CHARACTER: Annie
  LINE: Here's your pills.
  EXPRESSION: Empty
- CHARACTER: Narrator
  LINE: She drops them on the table.

::PATHS::
- CHOICE: Continue
  TARGET: pills_on_chest
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Paul
MOOD: Concern
CHARACTERS: Narrator, Paul
BACKGROUND_IMAGE: pills_on_chest.png
BACKGROUND_EDIT: "Close up on pills falling on Paul's chest"

::SCRIPT::
- CHARACTER: Narrator
  LINE: PAUL, as the pills hit his chest and bounce into his lap.
- CHARACTER: Paul
  LINE: Annie, what is it?
  EXPRESSION: Concerned

::PATHS::
- CHOICE: Continue
  TARGET: annie_gestures_outside
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Annie
MOOD: Melancholy
CHARACTERS: Narrator, Annie
BACKGROUND_IMAGE: annie_gestures_outside.png
BACKGROUND_EDIT: "Annie half-turns away, then gestures outside"

::SCRIPT::
- CHARACTER: Annie
  LINE: The rain... sometimes it gives me the blues.
  EXPRESSION: Sad

::PATHS::
- CHOICE: Continue
  TARGET: annie_close_up_lifeless
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Annie: Close Up
MOOD: Utter Lifelessness
CHARACTERS: Narrator, Annie
BACKGROUND_IMAGE: annie_close_up_lifeless.png
BACKGROUND_EDIT: "Close up on Annie's face, devoid of expression or light"

::SCRIPT::
- CHARACTER: Narrator
  LINE: ANNIE: CLOSE UP. And suddenly it's as if she's been turned off, gone lifeless.

::PATHS::
- CHOICE: Continue
  TARGET: paul_staring_rain
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Paul
MOOD: Observation
CHARACTERS: Narrator, Paul
BACKGROUND_IMAGE: paul_staring_rain.png
BACKGROUND_EDIT: "Paul staring at Annie, sound of rain"

::SCRIPT::
- CHARACTER: Narrator
  LINE: PAUL, staring at her. No sound but the rain.

::PATHS::
- CHOICE: Continue
  TARGET: annie_straight_on_no_light
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Annie
MOOD: Empty
CHARACTERS: Narrator, Annie
BACKGROUND_IMAGE: annie_straight_on_no_light.png
BACKGROUND_EDIT: "Annie seen straight on, eyes empty"

::SCRIPT::
- CHARACTER: Narrator
  LINE: ANNIE, seen straight on. No light in her eyes.
- CHARACTER: Annie
  LINE: When you first came here, I only loved the writer part of Paul Sheldon. But now I know I love the rest of him too. As much as Misery loves Ian. I know you don't love me--don't say you do--you're a beautiful, brilliant, famous man of the world; and I'm...not a movie star type. You'll never know the fear of losing someone like you if you’re someone like me.
  EXPRESSION: Heartbroken
- CHARACTER: Narrator
  LINE: (beat)
  EXPRESSION: null
- CHARACTER: Paul
  LINE: Why would you lose me?
  EXPRESSION: Confused

::PATHS::
- CHOICE: Continue
  TARGET: annie_explains_fear
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Annie
MOOD: Fearful Revelation
CHARACTERS: Narrator, Annie, Paul
BACKGROUND_IMAGE: annie_explains_fear.png
BACKGROUND_EDIT: "Annie explaining her fear of losing Paul"

::SCRIPT::
- CHARACTER: Annie
  LINE: The book is almost finished. Your legs are getting better. Soon you'll be able to walk. You'll be wanting to leave.
  EXPRESSION: Fearful
- CHARACTER: Paul
  LINE: Why would I want to leave? I like it here.
  EXPRESSION: Reassuring
- CHARACTER: Annie
  LINE: That’s very kind of you, but I'll bet it's not altogether true.
  EXPRESSION: Doubtful
- CHARACTER: Paul
  LINE: It is.
  EXPRESSION: Sincere

::PATHS::
- CHOICE: Continue
  TARGET: annie_shows_gun
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Annie
MOOD: Threatening
CHARACTERS: Narrator, Annie
BACKGROUND_IMAGE: annie_shows_gun.png
BACKGROUND_EDIT: "Annie reaches into her bathrobe and pulls out a .38 Special"

::SCRIPT::
- CHARACTER: Narrator
  LINE: She slowly reaches into the pocket of her bathrobe and pulls out a .38 Special.
- CHARACTER: Annie
  LINE: I have this gun, and sometimes I think about using it.
  EXPRESSION: Menacing
- CHARACTER: Narrator
  LINE: She is absentmindedly clicking the empty gun.
  EXPRESSION: null
- CHARACTER: Annie
  LINE: I better go now. I might put bullets in it.
  EXPRESSION: Unsettling

::PATHS::
- CHOICE: Continue
  TARGET: annie_leaves_locks_door
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Annie
MOOD: Departure
CHARACTERS: Narrator, Annie
BACKGROUND_IMAGE: annie_leaves_locks_door.png
BACKGROUND_EDIT: "Robot-like, Annie crosses to the door and leaves, locking it"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Robot-like, she crosses to the door and leaves. As she closes and locks the door--

::PATHS::
- CHOICE: Continue
  TARGET: paul_stunned
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Paul
MOOD: Shocked Paralysis
CHARACTERS: Narrator, Paul
BACKGROUND_IMAGE: paul_stunned.png
BACKGROUND_EDIT: "Paul is stunned, listening"

::SCRIPT::
- CHARACTER: Narrator
  LINE: PAUL, stunned, listening, waiting--

::PATHS::
- CHOICE: Continue
  TARGET: front_door_closing
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Outside the House
MOOD: Departure Imminent
CHARACTERS: Narrator
BACKGROUND_IMAGE: front_door_closing.png
BACKGROUND_EDIT: "Sound of the front door closing, footsteps, car door opening and slamming"

::SCRIPT::
- CHARACTER: Narrator
  LINE: --here is the sound of the front door closing--
- CHARACTER: Narrator
  LINE: --then footsteps on the outside walk--
- CHARACTER: Narrator
  LINE: --the sound of a car door opening and slamming shut.
- CHARACTER: Narrator
  LINE: Now comes the GUNNING of the motor.

::PATHS::
- CHOICE: Continue
  TARGET: window_annie_drives_by
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: The Window
MOOD: Escape Attempt
CHARACTERS: Narrator, Annie
BACKGROUND_IMAGE: window_annie_drives_by.png
BACKGROUND_EDIT: "Annie drives by, hunched over the wheel, motor sound fading"

::SCRIPT::
- CHARACTER: Narrator
  LINE: THE WINDOW as ANNIE drives by, hunched over the wheel. The MOTOR sound grows fainter, faint...

::PATHS::
- CHOICE: Continue
  TARGET: buster_virginia_bedroom
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Buster and Virginia's Bedroom
MOOD: Routine Reading
CHARACTERS: Narrator, Buster, Virginia
BACKGROUND_IMAGE: buster_virginia_bedroom.png
BACKGROUND_EDIT: "Nighttime, Buster and Virginia in bed reading"

::SCRIPT::
- CHARACTER: Narrator
  LINE: BUSTER AND VIRGINIA are lying in bed. Buster is reading yet another Misery novel, Misery’s Trial. Virginia is also reading.
- CHARACTER: Buster
  LINE: "There is a justice higher than that of man. I will be judged by Him."
  EXPRESSION: Reciting
- CHARACTER: Virginia
  LINE: What?
  EXPRESSION: Confused
- CHARACTER: Buster
  LINE: They’re hauling Misery into court.
  EXPRESSION: Informative
- CHARACTER: Virginia
  LINE: That’s nice.
  EXPRESSION: Neutral
- CHARACTER: Buster
  LINE: "There is a justice higher than that of man--I will be judged by Him."
  EXPRESSION: Muttering

::PATHS::
- CHOICE: End
  TARGET: end
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Annie's Kitchen
MOOD: Tension
CHARACTERS: Narrator, Paul
BACKGROUND_IMAGE: annies_kitchen.png
BACKGROUND_EDIT: "Kitchen counter with knives."

::SCRIPT::
- CHARACTER: Narrator
  LINE: The kitchen KNIVES on the counter.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Paul, now using both arms, forcing his body up toward them. This isn’t easy, it was a bitch the first time he tried it, but nothing’s going to stop him now. He’s leaning against the cupboard, using it for balance--
  EXPRESSION: Determined
- CHARACTER: Narrator
  LINE: --his balance starts to go but he won’t let it as we
  EXPRESSION: Determined

::PATHS::
- CHOICE: "Reach for the knives"
  TARGET: annies_kitchen_knives
  STATE_CHANGE: determination = +1
  CONDITION: null

::SCENE::
LOCATION: Annie's Kitchen - Knives
MOOD: Tension
CHARACTERS: Narrator, Paul
BACKGROUND_IMAGE: annies_kitchen_knives.png
BACKGROUND_EDIT: "Paul's hand grabbing a large knife."

::SCRIPT::
- CHARACTER: Narrator
  LINE: THE KNIVES, AS HIS HAND grabs the largest one, a fat-handled sharp beauty and
  EXPRESSION: Focused
- CHARACTER: Narrator
  LINE: PAUL, and you can sense the relief as he begins to lower himself to the floor.
  EXPRESSION: Relieved

::PATHS::
- CHOICE: "Move to the study"
  TARGET: the_study
  STATE_CHANGE: relief = +1
  CONDITION: null

::SCENE::
LOCATION: The Study
MOOD: Investigation
CHARACTERS: Narrator, Paul
BACKGROUND_IMAGE: the_study.png
BACKGROUND_EDIT: "Paul in wheelchair, searching drawers."

::SCRIPT::
- CHARACTER: Narrator
  LINE: PAUL, back in his wheelchair, knife in his lap, carefully opening drawers of little tables, looking inside. He closes them, moves on, unmindful of the rain. Now--
  EXPRESSION: Focused
- CHARACTER: Narrator
  LINE: THE SHELF OF PAUL SHELDON BOOKS. As before-- except the "My Life" scrapbook is gone.
  EXPRESSION: Observant
- CHARACTER: Narrator
  LINE: PAUL, glancing around-- and there it is, on a coffee table in the living room.
  EXPRESSION: Focused
- CHARACTER: Narrator
  LINE: Also on the table are a roll of scotch tape, a pair of scissors, and a copy of Newsweek. Paul wheels toward the table and the book, which is as big as a folio Shakespeare play and as thick as a family Bible.
  EXPRESSION: Determined

::PATHS::
- CHOICE: "Examine the scrapbook"
  TARGET: the_living_room
  STATE_CHANGE: curiosity = +1
  CONDITION: null

::SCENE::
LOCATION: The Living Room
MOOD: Discovery
CHARACTERS: Narrator, Paul
BACKGROUND_IMAGE: the_living_room.png
BACKGROUND_EDIT: "Paul opening a large scrapbook on a coffee table."

::SCRIPT::
- CHARACTER: Narrator
  LINE: PAUL, opening the book.
  EXPRESSION: Eager
- CHARACTER: Narrator
  LINE: THE FIRST PAGE OF THE BOOK, as Paul opens it. It’s a newspaper clipping as is almost all of what follows. A small article: simply a birth announcement for Anne Marie Wilkes.
  EXPRESSION: Neutral
- CHARACTER: Narrator
  LINE: PAUL turns the page. This headline reads: "Investment Banker Carl Wilkes Dies in Freak Fall."
  EXPRESSION: Shocked
- CHARACTER: Narrator
  LINE: "USC Nursing Student Dies in Freak Fall." That's the headline on the next page.
  EXPRESSION: Shocked
- CHARACTER: Narrator
  LINE: Now: "Miss Wilkes is Nursing School Honors Graduate."
  EXPRESSION: Neutral
- CHARACTER: Narrator
  LINE: Paul turns the page. Manchester, New Hampshire, Union Leader: "Ernest Gonyar, 79, Dies After Long Illness."
  EXPRESSION: Grim
- CHARACTER: Narrator
  LINE: Now that phrase seems to be what catches our eye--"after long illness" is from the next article. "Long illness" from the one after that. Then, on the next page, a variation: "Short Illness."
  EXPRESSION: Suspicious
- CHARACTER: Narrator
  LINE: Nov; we’re in Pennsylvania: "New Hospital Staff Announced."
  EXPRESSION: Neutral
- CHARACTER: Narrator
  LINE: And here come those phrases again on page after page--"After Long Illness." "After Long Illness." "After Long Illness."
  EXPRESSION: Grim
- CHARACTER: Narrator
  LINE: PAUL, transfixed; he keeps on turning the pages--the states keep changing, moving west. Pennsylvania to Minnesota, Minnesota to North Dakota. And always the clippings reporting deaths and deaths and--
  EXPRESSION: Transfixed
- CHARACTER: Narrator
  LINE: --and now we’re in Colorado. "NEW HEAD MATERNITY NURSE NAMED."
  EXPRESSION: Neutral
- CHARACTER: Narrator
  LINE: And now the dead are young and helpless; babies. More and more of them.
  EXPRESSION: Horrified
- CHARACTER: Paul
  LINE: Holy shit.
  EXPRESSION: Stunned
- CHARACTER: Narrator
  LINE: Then a headline which reads: "HEAD MATERNITY NURSE QUESTIONED ON INFANT DEATHS"
  EXPRESSION: Shocked
- CHARACTER: Narrator
  LINE: Next page: "MISS WILKES RELEASED."
  EXPRESSION: Neutral
- CHARACTER: Narrator
  LINE: Next page: "THREE MORE INFANTS DIE."
  EXPRESSION: Horrified
- CHARACTER: Narrator
  LINE: Next page, at last: "DRAGON LADY ARRESTED."
  EXPRESSION: Shocked
- CHARACTER: Narrator
  LINE: Then a photo: the front page of the Rocky Mountain Gazette. Annie on the courthouse steps. "DRAGON LADY CLAIMS INNOCENCE," under which there is a statement by Annie Wilkes.
  EXPRESSION: Observant
- CHARACTER: Narrator
  LINE: Paul turns quickly to the next page and a very large headline: "DRAGON LADY FOUND NOT GUILTY"
  EXPRESSION: Shocked
- CHARACTER: Narrator
  LINE: PAUL just sits there, shaking his head in bewilderment.
  EXPRESSION: Bewildered

::PATHS::
- CHOICE: "Turn to the last page"
  TARGET: the_book_last_page
  STATE_CHANGE: bewilderment = +1
  CONDITION: null

::SCENE::
LOCATION: The Book - Last Page
MOOD: Revelation
CHARACTERS: Narrator, Paul
BACKGROUND_IMAGE: the_book_last_page.png
BACKGROUND_EDIT: "The last page of the scrapbook with a Newsweek article."

::SCRIPT::
- CHARACTER: Narrator
  LINE: THE BOOK, as Paul turns the LAST page.
  EXPRESSION: Eager
- CHARACTER: Narrator
  LINE: PAUL, stunned and now we find out why, as we
  EXPRESSION: Shocked
- CHARACTER: Narrator
  LINE: THE PAGE IN THE BOOK. It's an article from Newsweek magazine, a picture of Paul's car being hauled up out of the snow. Above it this caption: "Presumed Dead--Paul Sheldon."
  EXPRESSION: Shocked

::PATHS::
- CHOICE: "Close the book and leave"
  TARGET: paul_leaves_living_room
  STATE_CHANGE: shock = +2
  CONDITION: null

::SCENE::
LOCATION: Paul Leaves Living Room
MOOD: Urgent Escape
CHARACTERS: Narrator, Paul
BACKGROUND_IMAGE: paul_leaves_living_room.png
BACKGROUND_EDIT: "Paul in wheelchair moving towards the front door."

::SCRIPT::
- CHARACTER: Narrator
  LINE: PAUL. Slamming the book shut, putting it back on the coffee table, then quickly turning his wheelchair as we
  EXPRESSION: Determined
- CHARACTER: Narrator
  LINE: PAUL, steering his wheelchair toward the front door. He tries to position himself for a surprise attack of ANNIE, but he can't find a way to get close enough. The wheelchair is too cumbersome. He looks around and decides to head back to his room. He is faced with the same problem there--so he struggles into bed and, lying on his back, he rests the knife on his chest and stares up at the ceiling.
  EXPRESSION: Frustrated

::PATHS::
- CHOICE: "Prepare to wait"
  TARGET: pauls_window_night
  STATE_CHANGE: frustration = +1
  CONDITION: null

::SCENE::
LOCATION: Paul's Window - Night
MOOD: Anticipation
CHARACTERS: Narrator, Paul
BACKGROUND_IMAGE: pauls_window_night.png
BACKGROUND_EDIT: "Paul's window at night, rain has stopped."

::SCRIPT::
- CHARACTER: Narrator
  LINE: PAUL'S WINDOW, hours later. The rain has stopped.
  EXPRESSION: Patient
- CHARACTER: Narrator
  LINE: PAUL--trying to stay awake. After a few beats, he hears something. It's the sound of a CAR PULLING UP. HEADLIGHTS can be seen flashing through the window. PAUL grips the knife and hides it under the covers. The sound of a CAR DOOR OPENING AND CLOSING, then FOOTSTEPS.
  EXPRESSION: Alert
- CHARACTER: Narrator
  LINE: As the FRONT DOOR OPENS, PAUL girds himself for attack. THE FRONT DOOR CLOSES, then a couple of FOOTSTEPS. Then silence. Then the FOOTSTEPS continue down the hall and up the stairs. After a beat, we hear the TELEVISION. Someone is explaining how you can buy millions of dollars of prime real estate with no money down.
  EXPRESSION: Tense
- CHARACTER: Narrator
  LINE: PAUL, allowing himself to relax, slips the knife under the mattress. As the TV DRONES ON, Paul lies staring up at the ceiling.
  EXPRESSION: Relieved

::PATHS::
- CHOICE: "Wait for dawn"
  TARGET: farmhouse_outside_night
  STATE_CHANGE: relief = +1
  CONDITION: null

::SCENE::
LOCATION: Outside the Farmhouse - Night
MOOD: Stormy
CHARACTERS: Narrator
BACKGROUND_IMAGE: farmhouse_outside_night.png
BACKGROUND_EDIT: "Nighttime, rain, thunder, lightning."

::SCRIPT::
- CHARACTER: Narrator
  LINE: We hear a clap of THUNDER and once again the rain pours down.
  EXPRESSION: Ominous

::PATHS::
- CHOICE: "Return to Paul's room"
  TARGET: paul_bed_thunder
  STATE_CHANGE: ominous = +1
  CONDITION: null

::SCENE::
LOCATION: Paul's Bed - Thunder
MOOD: Terror
CHARACTERS: Narrator, Paul, Annie
BACKGROUND_IMAGE: paul_bed_thunder.png
BACKGROUND_EDIT: "Close up on Paul's eyes, then Annie appearing with a needle."

::SCRIPT::
- CHARACTER: Narrator
  LINE: CLOSE UP: PAUL--eyes closed. There is another loud THUNDERCLAP which causes Paul to stir and open his eyes.
  EXPRESSION: Stirring
- CHARACTER: Narrator
  LINE: He turns his head and another CLAP OF THUNDER is heard, LIGHTNING flashes and reveals ANNIE standing over his bed.
  EXPRESSION: Terrified
- CHARACTER: Narrator
  LINE: Before he can react, she jabs a needle into his arm, pulls it out and starts out of the room. PAUL tries to raise himself, but the power of the drug causes him to collapse, unconscious.
  EXPRESSION: Powerless

::PATHS::
- CHOICE: "Wake up in the morning"
  TARGET: the_room_early_morning
  STATE_CHANGE: unconscious = true, terror = +2
  CONDITION: null

::SCENE::
LOCATION: The Room - Early Morning
MOOD: Disorientation
CHARACTERS: Narrator, Paul, Annie
BACKGROUND_IMAGE: the_room_early_morning.png
BACKGROUND_EDIT: "Paul strapped to the bed, Liberace playing on a record."

::SCRIPT::
- CHARACTER: Narrator
  LINE: It's stopped raining, PAUL lies asleep. Now, surprisingly, we hear a VOICE we've never heard in the movie before--loud--for an instant we don't recognize the voice, then we do: It's LIBERACE talking to his audience on a record going, "Thank you, thank you, what a wonderful thing it is for me to be back with you in Paris..."
  EXPRESSION: Confused
- CHARACTER: Narrator
  LINE: PAUL stirs and awakens to discover that he is strapped to his bed. He can move his arms, but that's it.
  EXPRESSION: Panicked
- CHARACTER: Narrator
  LINE: ANNIE, standing in the room, and she looks very together; her eyes are bright. Too bright. Way too bright. She comes to the foot of his bed.
  EXPRESSION: Menacing
- CHARACTER: Narrator
  LINE: PAUL, groggy from being drugged, tries to clear the cobwebs.
  EXPRESSION: Dazed
- CHARACTER: Annie
  LINE: Paul, I know you’ve been out.
  EXPRESSION: Soft
- CHARACTER: Paul
  LINE: What?
  EXPRESSION: Groggily
- CHARACTER: Annie
  LINE: You've been out of your room.
  EXPRESSION: Soft
- CHARACTER: Paul
  LINE: No, I h
  EXPRESSION: Confused

::PATHS::
- CHOICE: "Question Annie"
  TARGET: annie_question
  STATE_CHANGE: confusion = +1
  CONDITION: null

::SCENE::
LOCATION: INT. STUDY
MOOD: Suspenseful
CHARACTERS: Annie, Paul
BACKGROUND_IMAGE: study.png
BACKGROUND_EDIT: "A study, dimly lit"

::SCRIPT::
- CHARACTER: Annie
  LINE: Paul, my little ceramic penguin in the study always faces due south.
  EXPRESSION: null
- CHARACTER: Paul
  LINE: I don't know what you're talking about.
  EXPRESSION: null

::SCENE::
LOCATION: INT. BEDROOM - CONTINUOUS
MOOD: Threatening
CHARACTERS: Paul, Annie
BACKGROUND_IMAGE: bedroom.png
BACKGROUND_EDIT: "A bedroom, Paul is on the bed"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Paul looks up at her--he is totally honest and sincere. As he talks, his hand surreptitiously begins moving toward the mattress edge.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Annie, as she brings the fat-hand led knife out of her skirt pocket.
  EXPRESSION: null
- CHARACTER: Annie
  LINE: Is this what you're looking for? I know you've been out twice, Paul. At first, I couldn't figure out how you did it, but last night I found your key.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: She holds up the bobby pin
  EXPRESSION: null
- CHARACTER: Annie
  LINE: I know I left my scrapbook out, and I can imagine what you might be thinking of me. But you see, Paul, it's all okay.
  EXPRESSION: null

::SCENE::
LOCATION: INT. BEDROOM - CONTINUOUS
MOOD: Eerie
CHARACTERS: Annie, Paul
BACKGROUND_IMAGE: bedroom.png
BACKGROUND_EDIT: "A bedroom, Paul is on the bed"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Annie, as she walks slowly back to the foot of the bed.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: And now a thump comes from the foot of the bed. Something is out of sight.
  EXPRESSION: null

::SCENE::
LOCATION: INT. BEDROOM - CONTINUOUS
MOOD: Intense
CHARACTERS: Paul, Annie
BACKGROUND_IMAGE: bedroom.png
BACKGROUND_EDIT: "A bedroom, Paul is on the bed"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Paul, staring at her; waiting.
  EXPRESSION: null
- CHARACTER: Annie
  LINE: Last night it came so clear. I realize you just need more time. Eventually, you’ll come to accept the idea of being here. Paul, do you know about the early days at the Kimberly Diamond Mine? Do you know what they did to the native workers who stole diamonds? Don't worry, they didn’t kill them. That would be like junking a Mercedes just because it had a broken spring-- no, if they caught them they had to make sure they could go on working, but they also had to make sure they could never run away. The operation was called hobbling.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: And with that, she reaches down out of sight and comes up holding a 16-inch piece of 4 x 4 wood.
  EXPRESSION: null

::SCENE::
LOCATION: INT. BEDROOM - CONTINUOUS
MOOD: Desperate
CHARACTERS: Paul, Annie
BACKGROUND_IMAGE: bedroom.png
BACKGROUND_EDIT: "A bedroom, Paul is on the bed"

::SCRIPT::
- CHARACTER: Paul
  LINE: Annie, whatever you're thinking about, don't do it.
  EXPRESSION: Pleading

::SCENE::
LOCATION: INT. BEDROOM - CONTINUOUS
MOOD: Cruel
CHARACTERS: Annie, Paul
BACKGROUND_IMAGE: bedroom.png
BACKGROUND_EDIT: "A bedroom, Paul is on the bed"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Annie. She wedges the 4x4 firmly between his legs, just above the ankles, secures it and adjusts his feet.
  EXPRESSION: null
- CHARACTER: Annie
  LINE: Now don't fuss, Paul.
  EXPRESSION: Authoritative
- CHARACTER: Paul
  LINE: Why would I run away? I’m a writer, Annie--it's all I am--and I've never written this well--even you said that this is my best, didn't you?
  EXPRESSION: Pleading
- CHARACTER: Narrator
  LINE: Annie picks up a sledgehammer.
  EXPRESSION: null
- CHARACTER: Paul
  LINE: Didn't you? Why would I leave a place where I'm doing my best work? It doesn't make any sense.
  EXPRESSION: Pleading

::SCENE::
LOCATION: INT. BEDROOM - CONTINUOUS
MOOD: Brutal
CHARACTERS: Annie, Paul
BACKGROUND_IMAGE: bedroom.png
BACKGROUND_EDIT: "A bedroom, Paul is on the bed"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Annie, positioning herself to the side of his right ankle.
  EXPRESSION: null
- CHARACTER: Annie
  LINE: Shh, darling, trust me-- It’s for the best.
  EXPRESSION: Soothing
- CHARACTER: Narrator
  LINE: taking aim at his ankle
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: She takes the sledgehammer back.
  EXPRESSION: null
- CHARACTER: Paul
  LINE: Annie, for God's sake, please.
  EXPRESSION: Pleading
- CHARACTER: Narrator
  LINE: As Annie swings, the sledgehammer makes contact with the ankle. It breaks with a sharp crack.
  EXPRESSION: null

::SCENE::
LOCATION: INT. BEDROOM - CLOSE UP ON PAUL
MOOD: Agonizing
CHARACTERS: Paul
BACKGROUND_IMAGE: paul_face.png
BACKGROUND_EDIT: "Close up on Paul's face, contorted in pain"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Paui : Close up, shrieking.
  EXPRESSION: Shrieking

::SCENE::
LOCATION: INT. BEDROOM - CONTINUOUS
MOOD: Determined
CHARACTERS: Annie, Paul
BACKGROUND_IMAGE: bedroom.png
BACKGROUND_EDIT: "A bedroom, Paul is on the bed"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Annie, moving to the other side of the bed.
  EXPRESSION: null
- CHARACTER: Annie
  LINE: Almost done, just one more.
  EXPRESSION: Relentless

::SCENE::
LOCATION: INT. BEDROOM - CONTINUOUS
MOOD: Extreme Agony
CHARACTERS: Paul, Annie
BACKGROUND_IMAGE: bedroom.png
BACKGROUND_EDIT: "A bedroom, Paul is on the bed"

::SCRIPT::
- CHARACTER: Narrator
  LINE: And as she breaks the other ankle, Paul shrieks even louder.
  EXPRESSION: null

::SCENE::
LOCATION: INT. BEDROOM - CLOSE UP ON ANNIE
MOOD: Obsessed
CHARACTERS: Annie
BACKGROUND_IMAGE: annie_face.png
BACKGROUND_EDIT: "Close up on Annie's face, a disturbing smile"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Annie: Close up.
  EXPRESSION: null
- CHARACTER: Annie
  LINE: God, I love you...
  EXPRESSION: Loving

::SCENE::
LOCATION: INT. BEDROOM - PAUL'S FACE
MOOD: Beyond Pain
CHARACTERS: Paul
BACKGROUND_IMAGE: paul_face.png
BACKGROUND_EDIT: "Close up on Paul's face, showing extreme suffering"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Paul's face. He is beyond agony.
  EXPRESSION: null

::SCENE::
LOCATION: EXT. SILVER CREEK - DAY
MOOD: Disturbing
CHARACTERS: Annie, Misery
BACKGROUND_IMAGE: silver_creek.png
BACKGROUND_EDIT: "Annie driving her Cherokee, honking"

::SCRIPT::
- CHARACTER: Narrator
  LINE: For a long moment, nothing. Then... a faint sound. After a moment, it begins to become more intrusive and we can tell what it is: a car horn honking.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Fade in on: Silver Creek and Annie in her Cherokee, honking for another car to get a move on.
  EXPRESSION: null

::SCENE::
LOCATION: EXT. SILVER CREEK - DAY
MOOD: Frantic
CHARACTERS: Annie, Other Driver
BACKGROUND_IMAGE: silver_creek.png
BACKGROUND_EDIT: "Annie in her Cherokee, honking aggressively"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Annie, honking for another car to get a move on.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The driver of the car yells back. Annie yells louder. The Driver guns off, and Annie pulls into the parking space next to the General Store.
  EXPRESSION: null

::SCENE::
LOCATION: EXT. GENERAL STORE - DAY
MOOD: Aggressive
CHARACTERS: Annie
BACKGROUND_IMAGE: general_store.png
BACKGROUND_EDIT: "Annie getting out of her Cherokee, shaking her fist"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Annie, getting out, shaking a fist at the other car, calling out, "You poop!" She enters the store.
  EXPRESSION: null

::SCENE::
LOCATION: INT. BUSTER'S OFFICE - DAY
MOOD: Preoccupied
CHARACTERS: Buster
BACKGROUND_IMAGE: buster_office.png
BACKGROUND_EDIT: "Buster sitting by the front window, reading"

::SCRIPT::
- CHARACTER: Narrator
  LINE: A hand and a coin moving across it, from finger to finger. Pull back to reveal Buster, sitting by the front window of his office, reading The Rocky Mountain Gazette.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: He watches idly as Annie yells out the window to the car in front of her.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Buster, staring straight ahead. Something is gnawing at him.
  EXPRESSION: Troubled

::SCENE::
LOCATION: INT. VIRGINIA'S OFFICE - DAY
MOOD: Tense
CHARACTERS: Buster, Virginia
BACKGROUND_IMAGE: virginia_office.png
BACKGROUND_EDIT: "Virginia tidying the desk"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Virginia, in his office, tidying the desk. Buster enters, looks angry.
  EXPRESSION: null
- CHARACTER: Buster
  LINE: Just leave it, all right?
  EXPRESSION: Angry
- CHARACTER: Virginia
  LINE: Oh, I like that tone.
  EXPRESSION: Sarcastic
- CHARACTER: Buster
  LINE: How many times do I have to tell you-- I have a system here.
  EXPRESSION: Frustrated
- CHARACTER: Narrator
  LINE: rooting through a pile of papers
  EXPRESSION: null
- CHARACTER: Buster
  LINE: Where the hell is that thing?
  EXPRESSION: Desperate
- CHARACTER: Virginia
  LINE: What thing?
  EXPRESSION: Curious
- CHARACTER: Buster
  LINE: That thing.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: finding what he's looking for, a 3 x 5 card
  EXPRESSION: null
- CHARACTER: Buster
  LINE: Here it is. Right where it's supposed
  EXPRESSION: Relieved
- CHARACTER: Virginia
  LINE: What is it?
  EXPRESSION: Curious
- CHARACTER: Buster
  LINE: I'm not sure. Maybe nothing.
  EXPRESSION: Uncertain
- CHARACTER: Virginia
  LINE: It's good you found it.
  EXPRESSION: Casual
- CHARACTER: Buster
  LINE: There's that spice again.
  EXPRESSION: Uneasy

::SCENE::
LOCATION: EXT. LARGE LIBRARY - DAY
MOOD: Determined
CHARACTERS: Buster
BACKGROUND_IMAGE: library_exterior.png
BACKGROUND_EDIT: "Buster leaving his car, hurrying into the library"

::SCRIPT::
- CHARACTER: Narrator
  LINE: As Buster leaves, Virginia goes back to tidying the desk.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: A large library as Buster leaves his car, hurries inside and
  EXPRESSION: null

::SCENE::
LOCATION: INT. LIBRARY STACKS - DAY
MOOD: Focused
CHARACTERS: Buster
BACKGROUND_IMAGE: library_stacks.png
BACKGROUND_EDIT: "Buster poring over bound volumes, wearing bifocals"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Buster, wearing bifocals, sits poring over bound volumes of The Rocky Mountain Gazette.
  EXPRESSION: null

::SCENE::
LOCATION: INT. LIBRARY STACKS - CONTINUOUS
MOOD: Frustrated
CHARACTERS: Buster
BACKGROUND_IMAGE: library_stacks.png
BACKGROUND_EDIT: "Buster frustrated, switching volumes"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Buster, frustrated, puts one set of volumes down, picks up another, starts through it, as we
  EXPRESSION: null

::SCENE::
LOCATION: INT. LIBRARY - CONTINUOUS
MOOD: Tense
CHARACTERS: Buster
BACKGROUND_IMAGE: gazette_pages.png
BACKGROUND_EDIT: "Pages of The Rocky Mountain Gazette turning"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The Rocky Mountain Gazette, as the pages turn. --only now they stop moving.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Buster, tense, adjusting his bifocals.
  EXPRESSION: null

::SCENE::
LOCATION: INT. LIBRARY - HEADLINES
MOOD: Shocking
CHARACTERS: Narrator
BACKGROUND_IMAGE: headlines.png
BACKGROUND_EDIT: "A series of headlines about Annie Wilkes' murder trial"

::SCRIPT::
- CHARACTER: Narrator
  LINE: A series of headlines pertaining to Annie Wilkes’ murder trial.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: A headline which reads, "Dragon Lady Claims Innocence."
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Under a picture of Annie on the courthouse steps, we see a caption: "Wilkes told reporters on the courthouse steps, ’There is a higher justice than that of man; I will be judged by Him. ’"
  EXPRESSION: null

::SCENE::
LOCATION: INT. LIBRARY - CONTINUOUS
MOOD: Pensive
CHARACTERS: Buster
BACKGROUND_IMAGE: buster_contemplating.png
BACKGROUND_EDIT: "Buster holding a 3x5 card, staring"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Buster. He takes the 3x5 card out of his pocket.
  EXPRESSION: null

::SCENE::
LOCATION: INT. LIBRARY - CLOSE UP ON CARD
MOOD: Revealing
CHARACTERS: Narrator
BACKGROUND_IMAGE: 3x5_card.png
BACKGROUND_EDIT: "Close up of a 3x5 card with a quote"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The card--on it is printed the exact quote we just saw in the paper.
  EXPRESSION: null

::SCENE::
LOCATION: INT. LIBRARY - CONTINUOUS
MOOD: Reflective
CHARACTERS: Buster
BACKGROUND_IMAGE: buster_staring.png
BACKGROUND_EDIT: "Buster sitting, staring at the quote on the card"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Buster, sitting there, staring at the quote.
  EXPRESSION: null
- CHARACTER: Buster
  LINE: Interesting.
  EXPRESSION: Thoughtful

::SCENE::
LOCATION: EXT. FARM - DAY
MOOD: Domestic
CHARACTERS: Annie, Misery, Paul (off-screen)
BACKGROUND_IMAGE: farm.png
BACKGROUND_EDIT: "Annie carrying feed, followed by Misery the sow"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Hold on his face, then—
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Annie, carrying a bag of feed, followed by Misery, the sow, comes into view. She slows, smiles, waves--
  EXPRESSION: null
- CHARACTER: Annie
  LINE: Hi, Punkin.
  EXPRESSION: Affectionate

::SCENE::
LOCATION: EXT. FARM - CONTINUOUS
MOOD: Defiant
CHARACTERS: Paul, Annie
BACKGROUND_IMAGE: farm.png
BACKGROUND_EDIT: "Paul staring out at Annie"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Paul, staring out at her.
  EXPRESSION: null
- CHARACTER: Annie
  LINE: Give us a smile?
  EXPRESSION: Playful
- CHARACTER: Paul
  LINE: (Paul gives her the finger. She laughs)
  EXPRESSION: Defiant
- CHARACTER: Annie
  LINE: Such a kidder.
  EXPRESSION: Amused

::SCENE::
LOCATION: EXT. FARM - CONTINUOUS
MOOD: Enraged
CHARACTERS: Paul
BACKGROUND_IMAGE: farm.png
BACKGROUND_EDIT: "Paul lifting a typewriter"

::SCRIPT::
- CHARACTER: Narrator
  LINE: As she exits our view—
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Paul, lifting the typewriter and repeatedly raising it over his head, this time without any difficulty.
  EXPRESSION: Enraged

::SCENE::
LOCATION: INT. THE GENERAL STORE IN SILVER CREEK - EARLY AFTERNOON
MOOD: Casual
CHARACTERS: Buster, Pete
BACKGROUND_IMAGE: general_store.png
BACKGROUND_EDIT: "Buster entering the empty store, going to the coffee urn"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Buster enters. The place is empty. It's one of those wonderful spots that stocks pretty much everything in what seems like complete disarray. Buster goes to the coffee urn behind the counter, helps himself. He speaks to the guy who sits behind the counter nearby; these two have known each other forever.
  EXPRESSION: null
- CHARACTER: Buster
  LINE: Hey, Pete.
  EXPRESSION: Casual
- CHARACTER: Pete
  LINE: Buster.
  EXPRESSION: Casual
- CHARACTER: Buster
  LINE: Answer me a couple things?
  EXPRESSION: Inquisitive
- CHARACTER: Pete
  LINE: If I can.
  EXPRESSION: Willing
- CHARACTER: Buster
  LINE: Do you have any of those new Paul Sheldon books?
  EXPRESSION: Hopeful
- CHARACTER: Pete
  LINE: We had a batch. Sold 'em all in three day
  EXPRESSION: Casual

::SCENE::
LOCATION: Cash Register Area
MOOD: Curiosity
CHARACTERS: Buster, Pete
BACKGROUND_IMAGE: cash_register.png
BACKGROUND_EDIT: "Interior of a shop, Buster is at the cash register, Pete is nearby"

::SCRIPT::
- CHARACTER: Buster
  LINE: You wouldn’t happen to remember if Miz Wilkes bought one, would you?
  EXPRESSION: Curious
- CHARACTER: Pete
  LINE: Are you kidding? Every time that fella writes a book, she makes me set aside the first copy.
  EXPRESSION: Amused
- CHARACTER: Narrator
  LINE: Buster opens the cash register, drops his coffee money inside, closes the register.
  EXPRESSION: null
- CHARACTER: Buster
  LINE: Has she been buying any odd things lately?
  EXPRESSION: Inquisitive
- CHARACTER: Pete
  LINE: Miz Wilkes? Same old stuff. --Lest you call paper odd.
  EXPRESSION: Neutral
- CHARACTER: Buster
  LINE: Newspapers?
  EXPRESSION: Questioning
- CHARACTER: Pete
  LINE: No, the typing kind.
  EXPRESSION: Explanatory

::PATHS::
- CHOICE: "Continue conversation"
  TARGET: buster_close_up
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Buster - Close Up
MOOD: Realization
CHARACTERS: Buster
BACKGROUND_IMAGE: buster_close_up.png
BACKGROUND_EDIT: "Close up of Buster's face, a look of understanding"

::SCRIPT::
- CHARACTER: Buster
  LINE: Oh. That kind. Nothing odd about that.
  EXPRESSION: Understanding
- CHARACTER: Narrator
  LINE: He cannot hide his excitement now as we--
  EXPRESSION: null

::PATHS::
- CHOICE: "Transition to next scene"
  TARGET: paul_s_room
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Paul's Room
MOOD: Hostility
CHARACTERS: Annie, Paul
BACKGROUND_IMAGE: paul_s_room.png
BACKGROUND_EDIT: "A dimly lit room, Paul is in a wheelchair, Liberace music is playing"

::SCRIPT::
- CHARACTER: Annie
  LINE: Paul, don’t you think it’s time for you to start writing again? It's been over a week.
  EXPRESSION: Concerned
- CHARACTER: Paul
  LINE: I don't know, it's weird, but a couple of broken bones hasn't done a lot for my creative juices. Get the fuck out of here.
  EXPRESSION: Angry
- CHARACTER: Annie
  LINE: Don't talk to me like that.
  EXPRESSION: Hurt
- CHARACTER: Paul
  LINE: Why, what are you going to do? Kill me? Take your best shot.
  EXPRESSION: Provocative
- CHARACTER: Annie
  LINE: Why are you so mean, Mister you'd-be-dead-in-the-snow-if-it-wasn't-for­ me?
  EXPRESSION: Accusatory
- CHARACTER: Paul
  LINE: Oh, no reason, you keep me prisoner, you make me burn my book, you drive a sledgehammer into my ankles...
  EXPRESSION: Bitter
- CHARACTER: Annie
  LINE: I'll drive a sledgehammer into your man-gland if you're not nicer--
  EXPRESSION: Threatening
- CHARACTER: Paul
  LINE: Be my guest.
  EXPRESSION: Defiant
- CHARACTER: Annie
  LINE: That's disgusting.
  EXPRESSION: Disgusted

::PATHS::
- CHOICE: "Annie exits"
  TARGET: empty_road
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: A Road
MOOD: Anticipation
CHARACTERS: Narrator
BACKGROUND_IMAGE: empty_road.png
BACKGROUND_EDIT: "A long, empty road, a car appears around a curve"

::SCRIPT::
- CHARACTER: Narrator
  LINE: A road. Empty. Hold for a moment--now a car appears around a curve.
  EXPRESSION: null

::PATHS::
- CHOICE: "Focus on the car"
  TARGET: the_car
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: The Car
MOOD: Urgency
CHARACTERS: Buster
BACKGROUND_IMAGE: buster_driving.png
BACKGROUND_EDIT: "Interior of a car, Buster is driving fast"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Buster is driving fast.
  EXPRESSION: null

::PATHS::
- CHOICE: "Transition to Paul's room"
  TARGET: paul_in_room
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Paul in his room
MOOD: Lethargy
CHARACTERS: Paul
BACKGROUND_IMAGE: paul_sitting.png
BACKGROUND_EDIT: "Paul sits in his wheelchair by the window, eyes closed"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Paul in his room. He sits as before, by the window. He doesn’t move. Now, he closes his eyes, stretches, sighs as we--
  EXPRESSION: null

::PATHS::
- CHOICE: "Transition to kitchen"
  TARGET: kitchen
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: The Kitchen
MOOD: Domestic
CHARACTERS: Annie
BACKGROUND_IMAGE: annie_kitchen.png
BACKGROUND_EDIT: "A cozy kitchen, Annie is making cocoa"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Annie, busily making cocoa.
  EXPRESSION: null

::PATHS::
- CHOICE: "Transition back to Buster"
  TARGET: buster_in_car_mailbox
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Buster in his car
MOOD: Purposeful
CHARACTERS: Buster
BACKGROUND_IMAGE: buster_mailbox.png
BACKGROUND_EDIT: "Buster's car stops at a mailbox with the name WILKES"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Buster in his car. He stops at a mailbox. The name on the box is WILKES. Buster turns his car slowly into the driveway by the mailbox.
  EXPRESSION: null

::PATHS::
- CHOICE: "Focus on Paul"
  TARGET: paul_stares_window
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Paul stares out window
MOOD: Growing Alarm
CHARACTERS: Paul
BACKGROUND_IMAGE: paul_eyes_wide.png
BACKGROUND_EDIT: "Paul's eyes open wide as he sees Buster's car approaching"

::SCRIPT::
- CHARACTER: Paul
  LINE: He yawns, opens his eyes briefly. Closes them. In the distance now, growing more and more visible is Buster's car-- --and now Paul's eyes go open wide, and he's staring out the window at the car as it keeps on coming, closer, closer and--
  EXPRESSION: Shocked

::PATHS::
- CHOICE: "Focus on Buster"
  TARGET: buster_slow_driving
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Buster slow driving
MOOD: Cautious
CHARACTERS: Buster
BACKGROUND_IMAGE: buster_driving_slow.png
BACKGROUND_EDIT: "Buster is driving very slowly and carefully"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Buster, looking around. He's driving very slowly, carefully.
  EXPRESSION: null

::PATHS::
- CHOICE: "Focus on Paul's realization"
  TARGET: paul_realization
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Paul's Realization
MOOD: A Glimmer of Hope then Abrupt Fear
CHARACTERS: Paul, Annie
BACKGROUND_IMAGE: paul_drug_fight.png
BACKGROUND_EDIT: "Paul fixates on the window, then Annie appears with a needle"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Fixating on the window and now it's all going to be all right, everything’s going to be all right-- --and then Annie is on him, hypodermic needle in hand, jabbing it into his arm. He desperately tries to fight her off, but the drug starts to take hold. He tries to grab her by the neck, but she fights him off as she wheels him out of the room, down the hall and towards the cellar door.
  EXPRESSION: Fearful
- CHARACTER: Annie
  LINE: I don't think I'll ever understand you. I cook your meals, I tend to you practically twenty-four hours a day, and you continue to fight me. When are we going to develop a sense of trust?
  EXPRESSION: Frustrated
- CHARACTER: Narrator
  LINE: Annie opens the cellar door. Paul is all but limp by now. As she picks him up and starts to carry him down the steps--
  EXPRESSION: null

::PATHS::
- CHOICE: "Transition to Buster arriving"
  TARGET: buster_arrives_house
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Buster arrives at house
MOOD: Arrival
CHARACTERS: Buster
BACKGROUND_IMAGE: buster_car_house.png
BACKGROUND_EDIT: "Buster pulls up in front of the house"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Buster pulling up in front of the house. As he gets out of his car--
  EXPRESSION: null

::PATHS::
- CHOICE: "Transition to Annie placing Paul"
  TARGET: annie_cellar_floor
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Annie places Paul on cellar floor
MOOD: Ruthless
CHARACTERS: Annie, Paul
BACKGROUND_IMAGE: annie_cellar.png
BACKGROUND_EDIT: "Annie places Paul on the cellar floor, Paul is unconscious"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Annie placing Paul on the cellar floor and heading up the stairs. Paul is out.
  EXPRESSION: null

::PATHS::
- CHOICE: "Transition to Buster at door"
  TARGET: buster_front_door
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Buster at front door
MOOD: Inquisitive
CHARACTERS: Buster
BACKGROUND_IMAGE: buster_steps_door.png
BACKGROUND_EDIT: "Buster is heading up the steps to the front door"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Buster heading up the steps to the front door.
  EXPRESSION: null

::PATHS::
- CHOICE: "Transition to Annie opening door"
  TARGET: annie_opens_door
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Annie opens door
MOOD: Surprise then Composure
CHARACTERS: Annie, Buster
BACKGROUND_IMAGE: annie_door_buster.png
BACKGROUND_EDIT: "Annie opens the front door to reveal Buster"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Annie stashing the wheelchair in the hall closet. She crosses to the front door, opens it, revealing Buster.
  EXPRESSION: null
- CHARACTER: Annie
  LINE: Oh, my!
  EXPRESSION: Startled
- CHARACTER: Buster
  LINE: Sorry, didn't mean to startle you. You didn't give me a chance to knock.
  EXPRESSION: Apologetic
- CHARACTER: Annie
  LINE: Guess you can tell from my reaction, I'm not all that used to visitors out here. What can I do for you?
  EXPRESSION: Charming
- CHARACTER: Buster
  LINE: I was just wondering if you happen to know anything about Paul Sheldon.
  EXPRESSION: Direct
- CHARACTER: Annie
  LINE: What do you want to know?
  EXPRESSION: Nervous
- CHARACTER: Buster
  LINE: Anything you can tell me might help.
  EXPRESSION: Earnest

::PATHS::
- CHOICE: "Annie starts talking"
  TARGET: annie_talks_birthplace
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Annie talks birthplace
MOOD: Informative
CHARACTERS: Annie
BACKGROUND_IMAGE: annie_talking.png
BACKGROUND_EDIT: "Annie talking, a stream of information"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Annie. The words pour out--
  EXPRESSION: null
- CHARACTER: Annie
  LINE: well, he was born in Worcester, Massachusetts, forty-two years ago, the only child of Franklin and Helene Sheldon, mediocre student, majored in history...
  EXPRESSION: Fluent

::PATHS::
- CHOICE: "Buster interrupts"
  TARGET: buster_interrupts
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Buster interrupts
MOOD: Impatient
CHARACTERS: Buster
BACKGROUND_IMAGE: buster_surprised.png
BACKGROUND_EDIT: "Buster looks at Annie, surprised by the detail"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Buster, watching her, surprised.
  EXPRESSION: null
- CHARACTER: Buster
  LINE: Excuse me, that's not exactly the kind of information I was after. You see, he's been missing for quite some time now, and...
  EXPRESSION: Direct

::PATHS::
- CHOICE: "Annie continues"
  TARGET: annie_proud_fan
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Annie proud fan
MOOD: Enthusiastic then Embarrassed
CHARACTERS: Annie
BACKGROUND_IMAGE: annie_proud.png
BACKGROUND_EDIT: "Annie speaks with pride about her collection, then stops"

::SCRIPT::
- CHARACTER: Annie
  LINE: I know. It's so upsetting. I'm his number-one fan...I've got all his books, every sentence he ever put down. I'm so proud of my Paul Sheldon collection... ...here I am, prattling on and my manners have just flown away. I haven't invited you in. Please.
  EXPRESSION: Enthusiastic

::PATHS::
- CHOICE: "Buster accepts invitation"
  TARGET: buster_enters_house
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Buster enters house
MOOD: Observing
CHARACTERS: Annie, Buster
BACKGROUND_IMAGE: buster_inside.png
BACKGROUND_EDIT: "Annie lets Buster in, they stand in the hallway near Paul's room"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Annie lets Buster in, closes the door. They linger in front of Paul’s door. Buster idly checks out the hallway.
  EXPRESSION: null
- CHARACTER: Annie
  LINE: 'Course you must know about that horrible accident.
  EXPRESSION: Somber
- CHARACTER: Narrator
  LINE: Buster nods and wanders into the living room. Annie follows. He crosses into the study and checks out a bookcase that contains the complete works of Paul Sheldon. One shelf below contains Annie’s infamous scrapbook.
  EXPRESSION: null
- CHARACTER: Annie
  LINE: Almost killed me, too. I prayed when I heard the news. I got down on my knees and begged for it not to be true.
  EXPRESSION: Emotional

::PATHS::
- CHOICE: "Transition to kitchen"
  TARGET: buster_kitchen_study
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Buster in kitchen study
MOOD: Reflective
CHARACTERS: Annie, Buster
BACKGROUND_IMAGE: buster_kitchen_study.png
BACKGROUND_EDIT: "Annie is moved, Buster wanders into the kitchen"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Annie. She's so moved. Buster wanders into the kitchen.
  EXPRESSION: null
- CHARACTER: Annie
  LINE: You’re going to laugh at what I'm about to say, but go ahead, I don't care... ...when I was praying, God told me Lu gel ready.
  EXPRESSION: Earnest

::PATHS::
- CHOICE: "Buster asks for clarification"
  TARGET: buster_get_ready
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Buster asks for clarification
MOOD: Puzzled
CHARACTERS: Buster
BACKGROUND_IMAGE: buster_puzzled.png
BACKGROUND_EDIT: "Buster looks at Annie, confused"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Buster, watching her. This isn't at all what he expected.
  EXPRESSION: null
- CHARACTER: Buster
  LINE: Get ready for what?
  EXPRESSION: Confused

::PATHS::
- CHOICE: "Transition to Paul"
  TARGET: paul_fighting_drug
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Paul fighting drug
MOOD: Struggle
CHARACTERS: Paul
BACKGROUND_IMAGE: paul_eyes_flutter.png
BACKGROUND_EDIT: "Paul tries to fight the drug, his eyes flutter"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Trying to fight the drug; just his eyes flutter.
  EXPRESSION: null

::PATHS::
- CHOICE: "Transition back to hallway"
  TARGET: annie_buster_hallway
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Annie and Buster in hallway
MOOD: Explanatory
CHARACTERS: Annie, Buster
BACKGROUND_IMAGE: annie_buster_hallway.png
BACKGROUND_EDIT: "Annie and Buster walk down the hallway towards Paul's room"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Annie and Buster heading back down the hallway toward Paul's room.
  EXPRESSION: null
- CHARACTER: Annie
  LINE: To try and be his replacement--he gave so much pleasure to so many people and there's a shortage of pleasure on this planet these days, in case you hadn't noticed.
  EXPRESSION: Zealotous

::PATHS::
- CHOICE: "Enter Paul's room"
  TARGET: buster_enters_paul_room
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Buster enters Paul's room
MOOD: Revelation
CHARACTERS: Annie, Buster
BACKGROUND_IMAGE: buster_paul_room.png
BACKGROUND_EDIT: "Buster enters Paul's room, Annie follows"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Buster enters Paul's room. Annie follows.
  EXPRESSION: null
- CHARACTER: Annie
  LINE: God told me, since I was his number-one fan, that I should make up new stories os if I wos Pool Sheldon. So, went to town. And I bought a typewriter. And paper to type on. The same kind Paul Sheldon used. And I turned the guest bedroom into a writing studio. Mould you
  EXPRESSION: Determined

::SCENE::
LOCATION: Bathroom
MOOD: Quiet
CHARACTERS: Buster, Annie
BACKGROUND_IMAGE: bathroom.png
BACKGROUND_EDIT: "Clean, well-maintained bathroom"

::SCRIPT::
- CHARACTER: Annie
  LINE: like to see it?
  EXPRESSION: null
- CHARACTER: Buster
  LINE: Sure.
  EXPRESSION: null
- CHARACTER: Annie
  LINE: It's right this way.
  EXPRESSION: null

::PATHS::
- CHOICE: "Look in the bathroom"
  TARGET: bathroom_interior
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Bathroom Interior
MOOD: Reflective
CHARACTERS: Buster, Annie
BACKGROUND_IMAGE: bathroom_interior.png
BACKGROUND_EDIT: "Buster looking around the bathroom, Annie waiting"

::SCRIPT::
- CHARACTER: Narrator
  LINE: BUSTER takes a look in the bathroom. ANNIE waits for him.
  EXPRESSION: null
- CHARACTER: Annie
  LINE: It's right here. I knew how he wrote, the kinds of words he used, the wonderful stories he told--
  EXPRESSION: Moved
- CHARACTER: Annie
  LINE: --I've spent the last four weeks trying to write like Paul Sheldon.
  EXPRESSION: Moved
- CHARACTER: Annie
  LINE: But I can't do it right. I try and I try and I know all the words--
  EXPRESSION: Despairing
- CHARACTER: Annie
  LINE: --but it's just not the same.
  EXPRESSION: Despairing

::PATHS::
- CHOICE: "Respond to Annie"
  TARGET: bathroom_response
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Bathroom Response
MOOD: Empathetic
CHARACTERS: Buster, Annie
BACKGROUND_IMAGE: bathroom_response.png
BACKGROUND_EDIT: "Buster watches Annie, a moment of quiet reflection"

::SCRIPT::
- CHARACTER: Narrator
  LINE: CUT TO: BUSTER. He just stands there, watches her.
  EXPRESSION: null
- CHARACTER: Buster
  LINE: Well...
  EXPRESSION: Hesitant
- CHARACTER: Buster
  LINE: ...maybe it takes time to get the hang of it.
  EXPRESSION: Encouraging

::PATHS::
- CHOICE: "Offer help"
  TARGET: offer_manuscript
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Offer Manuscript
MOOD: Hopeful
CHARACTERS: Buster, Annie
BACKGROUND_IMAGE: offer_manuscript.png
BACKGROUND_EDIT: "Annie holds up manuscript pages, Buster looks thoughtful"

::SCRIPT::
- CHARACTER: Annie
  LINE: I could give you a couple of hundred pages of mine, and you could tell me what you think.
  EXPRESSION: Hopeful
- CHARACTER: Buster
  LINE: I'm not much of a critic.
  EXPRESSION: Humble
- CHARACTER: Annie
  LINE: Well, I just thought--oh, look at me. You'd think I’d never had a house guest before. Would you like something to drink?
  EXPRESSION: Flustered
- CHARACTER: Buster
  LINE: Sure.
  EXPRESSION: Agreeable
- CHARACTER: Annie
  LINE: How does a nice cup of cocoa sound?
  EXPRESSION: Welcoming
- CHARACTER: Buster
  LINE: Sounds good.
  EXPRESSION: Pleased

::PATHS::
- CHOICE: "Go to kitchen"
  TARGET: kitchen_visit
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Kitchen Visit
MOOD: Domestic
CHARACTERS: Annie, Buster
BACKGROUND_IMAGE: kitchen_visit.png
BACKGROUND_EDIT: "Annie exits to kitchen, Buster remains"

::SCRIPT::
- CHARACTER: Annie
  LINE: There's some already made.
  EXPRESSION: Helpful

::PATHS::
- CHOICE: "Buster lingers"
  TARGET: hallway_conversation
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Hallway Conversation
MOOD: Philosophical
CHARACTERS: Buster, Annie
BACKGROUND_IMAGE: hallway_conversation.png
BACKGROUND_EDIT: "Buster and Annie in the hallway"

::SCRIPT::
- CHARACTER: Narrator
  LINE: As Buster lingers in Paul's room for a beat, then goes into the hallway.
  EXPRESSION: null
- CHARACTER: Buster
  LINE: Must get lonely, living out here all by yourself.
  EXPRESSION: Observant
- CHARACTER: Annie
  LINE: I always say if you can't enjoy your own company, you're not fit company for anyone else.
  EXPRESSION: Wise
- CHARACTER: Buster
  LINE: You got a point there...
  EXPRESSION: Thoughtful

::PATHS::
- CHOICE: "Buster moves upstairs"
  TARGET: paul_struggle
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Paul Struggle
MOOD: Agonizing
CHARACTERS: Paul
BACKGROUND_IMAGE: paul_struggle.png
BACKGROUND_EDIT: "Paul in pain, fighting the drug, arm twitching"

::SCRIPT::
- CHARACTER: Narrator
  LINE: CUT TO: PAUL, still fighting the drug. His arm twitches almost involuntarily, grazing the barbecue.
  EXPRESSION: null

::PATHS::
- CHOICE: "Buster enters Annie's room"
  TARGET: annies_room_enter
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Annie's Room Enter
MOOD: Curious
CHARACTERS: Buster, Annie
BACKGROUND_IMAGE: annies_room_enter.png
BACKGROUND_EDIT: "Buster opens Annie's room door, pauses"

::SCRIPT::
- CHARACTER: Narrator
  LINE: CUT TO: BUSTER opening the door to Annie's room. He looks around and just as he is about to turn to leave--
  EXPRESSION: null

::PATHS::
- CHOICE: "Annie appears"
  TARGET: annie_appears
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Annie Appears
MOOD: Startling
CHARACTERS: Annie, Buster
BACKGROUND_IMAGE: annie_appears.png
BACKGROUND_EDIT: "Annie standing directly in front of Buster"

::SCRIPT::
- CHARACTER: Narrator
  LINE: CUT TO: ANNIE, standing right in front of him.
  EXPRESSION: null
- CHARACTER: Annie
  LINE: Here you are.
  EXPRESSION: Direct

::PATHS::
- CHOICE: "Buster heads downstairs"
  TARGET: descending_stairs
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Descending Stairs
MOOD: Polite Dismissal
CHARACTERS: Buster, Annie
BACKGROUND_IMAGE: descending_stairs.png
BACKGROUND_EDIT: "Buster and Annie on the stairs"

::SCRIPT::
- CHARACTER: Narrator
  LINE: BUSTER heads down the stairs, ANNIE follows.
  EXPRESSION: null
- CHARACTER: Buster
  LINE: Thanks, Miz Wilkes, but I don’t want to take up any more of your time. I best be going.
  EXPRESSION: Polite
- CHARACTER: Annie
  LINE: But you didn’t even taste your cocoa.
  EXPRESSION: Persuasive

::PATHS::
- CHOICE: "Move towards the front door"
  TARGET: front_door_farewell
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Front Door Farewell
MOOD: Finality
CHARACTERS: Buster, Annie
BACKGROUND_IMAGE: front_door_farewell.png
BACKGROUND_EDIT: "Buster and Annie at the front door"

::SCRIPT::
- CHARACTER: Narrator
  LINE: They cross to the front door.
  EXPRESSION: null
- CHARACTER: Buster
  LINE: I'm sure it's wonderful, but really should be getting back.
  EXPRESSION: Firm
- CHARACTER: Narrator
  LINE: BUSTER opens the door.
  EXPRESSION: null

::PATHS::
- CHOICE: "Paul stirs"
  TARGET: paul_stirring
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Paul Stirring
MOOD: Waking
CHARACTERS: Paul
BACKGROUND_IMAGE: paul_stirring.png
BACKGROUND_EDIT: "Paul starting to wake up"

::SCRIPT::
- CHARACTER: Narrator
  LINE: CUT TO: PAUL stirring.
  EXPRESSION: null

::PATHS::
- CHOICE: "Buster and Annie at the door"
  TARGET: door_exchange
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Door Exchange
MOOD: Lingering
CHARACTERS: Buster, Annie
BACKGROUND_IMAGE: door_exchange.png
BACKGROUND_EDIT: "Buster and Annie at the open door"

::SCRIPT::
- CHARACTER: Narrator
  LINE: CUT TO: BUSTER and ANNIE at the door.
  EXPRESSION: null
- CHARACTER: Buster
  LINE: If you don’t mind, perhaps I could pay you another visit sometime.
  EXPRESSION: Hopeful
- CHARACTER: Annie
  LINE: I'd be delighted. Now that you know the way...
  EXPRESSION: Coy

::PATHS::
- CHOICE: "Annie closes door"
  TARGET: buster_leaves
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Buster Leaves
MOOD: Pensive
CHARACTERS: Buster
BACKGROUND_IMAGE: buster_leaves.png
BACKGROUND_EDIT: "Annie closes the door, Buster on the porch"

::SCRIPT::
- CHARACTER: Narrator
  LINE: With that, she closes the door. We stay with BUSTER. He stands on the front porch for a beat, thinking, then starts heading down the porch steps, lust as he reaches about halfway down, we HEAR A LOUD CRASH coming from inside the house.
  EXPRESSION: null

::PATHS::
- CHOICE: "Paul's crash"
  TARGET: paul_crash
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Paul's Crash
MOOD: Violent Awakening
CHARACTERS: Paul
BACKGROUND_IMAGE: paul_crash.png
BACKGROUND_EDIT: "Paul has fallen, knocking over the barbecue"

::SCRIPT::
- CHARACTER: Narrator
  LINE: CUT TO: PAUL--he has managed to partially fight his way through the drug, and in waking has accidentally knocked over the barbecue. He fights to clear the cobwebs.
  EXPRESSION: null

::PATHS::
- CHOICE: "Buster checks on Annie"
  TARGET: buster_checks_annie
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Buster Checks Annie
MOOD: Concerned Inquiry
CHARACTERS: Buster, Annie
BACKGROUND_IMAGE: buster_checks_annie.png
BACKGROUND_EDIT: "Buster looking back at the house"

::SCRIPT::
- CHARACTER: Buster
  LINE: Miz Wilkes, are you all right?
  EXPRESSION: Concerned
- CHARACTER: Narrator
  LINE: There is no answer. He quietly moves into the house.
  EXPRESSION: null
- CHARACTER: Buster
  LINE: Miz Wilkes?
  EXPRESSION: Calling Out

::PATHS::
- CHOICE: "Paul calls out"
  TARGET: paul_calls
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Paul Calls
MOOD: Desperate
CHARACTERS: Paul
BACKGROUND_IMAGE: paul_calls.png
BACKGROUND_EDIT: "Paul on the floor, muffled call"

::SCRIPT::
- CHARACTER: Narrator
  LINE: CUT TO: PAUL, still fighting to gain complete consciousness.
  EXPRESSION: null
- CHARACTER: Paul
  LINE: Here. I'm down here. Down here.
  EXPRESSION: Weak

::PATHS::
- CHOICE: "Buster finds the cellar door"
  TARGET: cellar_door_open
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Cellar Door Open
MOOD: Shocking Revelation
CHARACTERS: Buster, Annie, Paul
BACKGROUND_IMAGE: cellar_door_open.png
BACKGROUND_EDIT: "Buster opens cellar door, light shines on Paul. Annie revealed with shotgun."

::SCRIPT::
- CHARACTER: Narrator
  LINE: CUT TO: BUSTER. Hearing Paul's muffled call for help, he tracks the sound to the cellar door. As PAUL continues to call out, Buster looks around, sees no one, and opens the cellar door. The shaft of light from the open door pours down on Paul, who is still lying on the floor.
  EXPRESSION: null
- CHARACTER: Buster
  LINE: Mr. Sheldon?
  EXPRESSION: Surprised
- CHARACTER: Narrator
  LINE: But before Paul can answer, there’s the sound of a LOUD EXPLOSION. Seemingly from nowhere a hole is ripped through Buster's chest, knocking him out of frame, revealing Annie, smoking shotgun in hand, standing at the top of the cellar steps.
  EXPRESSION: Shocked
- CHARACTER: Annie
  LINE: Don't feel bad, Paul. It had to happen. I've been waiting for this sign.
  EXPRESSION: Delusional
- CHARACTER: Narrator
  LINE: ANNIE walks toward BUSTER’S BODY and very casually takes his gun out of its holster.
  EXPRESSION: null
- CHARACTER: Annie
  LINE: I've known for some time why I was chosen to save you. You and I were meant to be together forever. But now our time in this world must end. But don’t worry, Paul. I've already prepared for what must be done. I put two bullets in my gun, one for you and one for me. Oh, darling, it will be so beautiful.
  EXPRESSION: Fanatical
- CHARACTER: Narrator
  LINE: With that, ANNIE turns and exits the cellar.
  EXPRESSION: null

::PATHS::
- CHOICE: "Paul's mind races"
  TARGET: paul_idea
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Paul Idea
MOOD: Desperate Ingenuity
CHARACTERS: Paul
BACKGROUND_IMAGE: paul_idea.png
BACKGROUND_EDIT: "Paul looks at the barbecue and nearby table with cans"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Paul's mind races desperately. He looks at the barbecue again. Next to it is a messy table with a dozen jars and cans on it.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: CUT TO: THE TABLE. One of the cans is LIGHTER FLUID.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: CUT TO: PAUL. He stares at it for a moment. An idea hits him--
  EXPRESSION: Insightful
- CHARACTER: Narrator
  LINE: --now, PAUL struggles and crawls over to the table. He grabs the lighter fluid in his hands, jams it into the rear of his pants and scrambles back to where ANNIE left him.
  EXPRESSION: Determined

::PATHS::
- CHOICE: "Annie returns"
  TARGET: annie_returns_cellar
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Annie Returns Cellar
MOOD: Deceptive Affection
CHARACTERS: Annie, Paul
BACKGROUND_IMAGE: annie_returns_cellar.png
BACKGROUND_EDIT: "Annie returns with gun and needle, approaching Paul"

::SCRIPT::
- CHARACTER: Narrator
  LINE: CUT TO: ANNIE returning with her .38 Special and a hypodermic needle. She stops at the top of the stairs.
  EXPRESSION: null
- CHARACTER: Annie
  LINE: Now don’t be afraid. I love you.
  EXPRESSION: Deceptive
- CHARACTER: Paul
  LINE: T know ynu do. T love ynu tnn, Annie. And you're right. We are meant to be together. And I know we must die. But it must be so that Misery can live. We have the power to give Misery eternal life. We must finish the book.
  EXPRESSION: Pleading
- CHARACTER: Annie
  LINE: But the time is now. Soon others will come.
  EXPRESSION: Impatient
- CHARACTER: Paul
  LINE: It’s almost done. By dawn we’ll be able to give Misery back to the world.
  EXPRESSION: Urgent

::PATHS::
- CHOICE: "Annie considers"
  TARGET: annie_considers
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Annie Considers
MOOD: Indecisive
CHARACTERS: Annie, Paul
BACKGROUND_IMAGE: annie_considers.png
BACKGROUND_EDIT: "Annie pauses at the top of the stairs, looking at Paul"

::SCRIPT::
- CHARACTER: Narrator
  LINE: ANNIE stares at Paul. She could go either way on this. Then, without a word, she turns and goes back up the stairs.
  EXPRESSION: null
- CHARACTER: Annie
  LINE: Here, Paul. I'll fix you something to eat.
  EXPRESSION: Manipulative
- CHARACTER: Narrator
  LINE: She exits. PAUL hesitates for a moment, then realizes he has no choice. He starts dragging himself over BUSTER and up the stairs.
  EXPRESSION: null

::PATHS::
- CHOICE: "Paul works in his room"
  TARGET: paul_working_night
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Paul's Room - Night
MOOD: Intense Focus
CHARACTERS: Paul, Annie
BACKGROUND_IMAGE: pauls_room_night.png
BACKGROUND_EDIT: "Paul typing furiously in his room, Annie enters with pages"

::SCRIPT::
- CHARACTER: Narrator
  LINE: INT. PAUL’S ROOM - NIGHT
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: 49
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: 49
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: PAUL working. Typing like a madman, totally concentrated on the white paper. His lips move but he's not even aware of it.
  EXPRESSION: Focused
- CHARACTER: Narrator
  LINE: ANNIE enters quietly, holding a few pages.
  EXPRESSION: null
- CHARACTER: Annie
  LINE: Oh, Paul. It's beautiful.
  EXPRESSION: Admiring
- CHARACTER: Paul
  LINE: Three more chapters to go.
  EXPRESSION: Driven
- CHARACTER: Narrator
  LINE: She looks at him now, enthralled.
  EXPRESSION: null
- CHARACTER: Annie
  LINE: The stranger staying at the Inn, is he someone from Misery's past?
  EXPRESSION: Curious
- CHARACTER: Paul
  LINE: Maybe.
  EXPRESSION: Evasive
- CHARACTER: Annie
  LINE: This is so exciting. It's Windthorne, her first love, right?
  EXPRESSION: Enthusiastic
- CHARACTER: Paul
  LINE: Maybe. Are you ready for the next chapter?
  EXPRESSION: Teasing

::PATHS::
- CHOICE: "Annie takes the pages"
  TARGET: annie_takes_pages
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Annie Takes Pages
MOOD: Eager Anticipation
CHARACTERS: Annie
BACKGROUND_IMAGE: annie_takes_pages.png
BACKGROUND_EDIT: "Annie takes the manuscript pages, full of excitement"

::SCRIPT::
- CHARACTER: Annie
  LINE: Oh you!
  EXPRESSION: Playful
- CHARACTER: Narrator
  LINE: She takes the pages and goes.
  EXPRESSION: null

::PATHS::
- CHOICE: "Paul types later"
  TARGET: paul_types_later
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Paul Types Later
MOOD: Frustrated Revision
CHARACTERS: Paul
BACKGROUND_IMAGE: paul_types_later.png
BACKGROUND_EDIT: "Paul ripping out a page and starting over"

::SCRIPT::
- CHARACTER: Narrator
  LINE: CUT TO: INT. PAUL'S ROOM - LATER
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: 50
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: 50
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: PAUL types a moment then rips out the page and starts over.
  EXPRESSION: Frustrated

::PATHS::
- CHOICE: "Annie brings coffee"
  TARGET: annie_brings_coffee
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Annie Brings Coffee
MOOD: Encouraging Support
CHARACTERS: Annie
BACKGROUND_IMAGE: annie_brings_coffee.png
BACKGROUND_EDIT: "Annie places coffee down and pages on the main pile"

::SCRIPT::
- CHARACTER: Narrator
  LINE: CUT TO: ANNIE, putting the coffee down for him, putting the pages back on the main pile.
  EXPRESSION: null
- CHARACTER: Annie
  LINE: (more excited now than the la
  EXPRESSION: Excited

::SCENE::
LOCATION: INT. PAUL’S ROOM - CONTINUOUS
MOOD: Intense / Dramatic
CHARACTERS: Narrator, Annie, Paul
BACKGROUND_IMAGE: paul_room_late.png
BACKGROUND_EDIT: "Late at night, Paul's room, manuscript work in progress"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Paul rubs his eyes. For a moment, he sags, but he fights it. He puts a clean page into the typewriter.
  EXPRESSION: Tired
- CHARACTER: Annie
  LINE: Oh, Paul. I’m dying. Does she wind up with Ian or Windthorne? You have to tell me.
  EXPRESSION: Anxious
- CHARACTER: Paul
  LINE: You’ll know very soon. I’m starting the last chapter. And when I finish, I want everything to be perfect. I'll require three things.
  EXPRESSION: Determined
- CHARACTER: Annie
  LINE: What things?
  EXPRESSION: Curious
- CHARACTER: Paul
  LINE: You don't know?
  EXPRESSION: Playful
- CHARACTER: Annie
  LINE: I was fooling, silly. You need a cigarette, because you used to smoke but you quit except when you finish a book, and you just have one, and the match is to light it. And you need one glass of champagne.
  EXPRESSION: Playful
- CHARACTER: Annie
  LINE: Dome Pear-igg-non.
  EXPRESSION: Thoughtful
- CHARACTER: Paul
  LINE: Dome Pear-igg-non it is.
  EXPRESSION: Agreeable

::PATHS::
- CHOICE: "Exit to get supplies"
  TARGET: window_morning
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: THE WINDOW - MORNING
MOOD: Hopeful / New Beginning
CHARACTERS: Narrator
BACKGROUND_IMAGE: window_morning.png
BACKGROUND_EDIT: "View from a window showing the first light of morning"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The first light of morning is starting to break through.
  EXPRESSION:null

::PATHS::
- CHOICE: "Return to Paul's room"
  TARGET: paul_room_stretching
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: INT. PAUL’S ROOM - CONTINUOUS
MOOD: Focused / Anticipatory
CHARACTERS: Narrator, Paul, Annie
BACKGROUND_IMAGE: paul_room_stretching.png
BACKGROUND_EDIT: "Paul's room, morning light, Paul preparing for the final moments"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Paul, stretching. He makes sure everything is set.
  EXPRESSION: Focused
- CHARACTER: Paul
  LINE: Annie! Annie!
  EXPRESSION: Calling
- CHARACTER: Narrator
  LINE: With that, she enters.
  EXPRESSION: null
- CHARACTER: Annie
  LINE: Yes, Paul.
  EXPRESSION: Eager
- CHARACTER: Paul
  LINE: I'm almost done.
  EXPRESSION: Satisfied
- CHARACTER: Annie
  LINE: Oh, Paul, this is so romantic. Ian and Windthorne dueling for the right to Misery's hand. Does Ian win? Oh, don’t me. It's Windthorne, right?
  EXPRESSION: Excited
- CHARACTER: Paul
  LINE: You’ll know everything in a minute. Get the champagne.
  EXPRESSION: Direct
- CHARACTER: Annie
  LINE: Ahh!!!
  EXPRESSION: Impatient
- CHARACTER: Narrator
  LINE: She exits; Paul adjusts the manuscript on the table and then types the last line.
  EXPRESSION: null

::PATHS::
- CHOICE: "Annie gets champagne"
  TARGET: kitchen_annie
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: KITCHEN - CONTINUOUS
MOOD: Sinister / Preparatory
CHARACTERS: Narrator, Annie
BACKGROUND_IMAGE: kitchen_annie.png
BACKGROUND_EDIT: "Kitchen, Annie preparing supplies, a gun is visible"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Annie in the kitchen. She takes the bottle of Dorn Perignon out of the icebox, places it on a tray with two glasses-- opens a drawer--takes out the gun--places it in her pocket-- then takes out the hypodermic needle and places it on the tray.
  EXPRESSION: Secretive

::PATHS::
- CHOICE: "Return to Paul's room"
  TARGET: paul_room_annie_enters
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: INT. PAUL’S ROOM - CONTINUOUS
MOOD: Climactic / Intense
CHARACTERS: Narrator, Annie, Paul
BACKGROUND_IMAGE: paul_room_annie_enters.png
BACKGROUND_EDIT: "Paul's room, Annie enters with tray, tension is high"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Annie enters with the tray. She sets it down on the table.
  EXPRESSION: null
- CHARACTER: Annie
  LINE: Did I do good?
  EXPRESSION: Eager
- CHARACTER: Paul
  LINE: You did perfect. Except for one thing. This time we need two glasses.
  EXPRESSION: Assertive
- CHARACTER: Narrator
  LINE: He takes the last page out of the typewriter.
  EXPRESSION: null
- CHARACTER: Annie
  LINE: Oh, Paul.
  EXPRESSION: Emotional

::PATHS::
- CHOICE: "Annie exits and Paul prepares to burn the manuscript"
  TARGET: paul_manuscript_prep
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: INT. PAUL’S ROOM - CONTINUOUS
MOOD: Destructive / Manic
CHARACTERS: Narrator, Paul, Annie
BACKGROUND_IMAGE: paul_manuscript_prep.png
BACKGROUND_EDIT: "Paul's room, Paul dousing manuscript with lighter fluid, preparing to ignite"

::SCRIPT::
- CHARACTER: Narrator
  LINE: As soon as she exits, Paul drops the manuscript to the floor, pulls the lighter fluid from his pants, and starts dousing the manuscript with lighter fluid. He grabs the last chapter and twists the last few pages together torch style. He douses it with the fluid and holds the match out of sight. He smiles as we
  EXPRESSION: Manic

::PATHS::
- CHOICE: "Annie enters with second glass"
  TARGET: annie_enters_second_glass
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: INT. PAUL’S ROOM - CONTINUOUS
MOOD: Confrontational / Violent
CHARACTERS: Narrator, Annie, Paul
BACKGROUND_IMAGE: annie_enters_second_glass.png
BACKGROUND_EDIT: "Paul's room, Annie re-enters, Paul reveals his plan"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Annie entering with the second glass...
  EXPRESSION: null
- CHARACTER: Paul
  LINE: It’s all right here, Annie. Remember how for all those years no one ever knew who Misery's real father was, or if they’d ever be reunited? It’s all right here. Will Misery finally lead her countrymen to freedom? Does she finally marry Ian or will it be Windthorne? It's all right here.
  EXPRESSION: Taunting
- CHARACTER: Narrator
  LINE: The match, as he strikes it and
  EXPRESSION: null

::PATHS::
- CHOICE: "Annie screams"
  TARGET: annie_screaming
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: INT. PAUL’S ROOM - CONTINUOUS
MOOD: Desperate / Chaotic
CHARACTERS: Narrator, Annie, Paul
BACKGROUND_IMAGE: annie_screaming.png
BACKGROUND_EDIT: "Paul's room, Annie screams as the manuscript ignites, chaos ensues"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Annie screaming--
  EXPRESSION: Terror
- CHARACTER: Annie
  LINE: Paul, you can't.
  EXPRESSION: Pleading
- CHARACTER: Narrator
  LINE: And as her hands fly out beseechingly--
  EXPRESSION: null

::PATHS::
- CHOICE: "Champagne bottle falls"
  TARGET: champagne_bottle_falls
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: INT. PAUL’S ROOM - CONTINUOUS
MOOD: Violent / Explosive
CHARACTERS: Narrator, Paul
BACKGROUND_IMAGE: champagne_bottle_falls.png
BACKGROUND_EDIT: "Paul's room, champagne bottle explodes on the floor"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The champagne bottle--it falls to the floor, explodes like a torpedo, shards of glass all over, curds of foam everywhere--
  EXPRESSION: Violent
- CHARACTER: Paul
  LINE: Why not? I learned it from you...
  EXPRESSION: Cruel
- CHARACTER: Narrator
  LINE: And on that--
  EXPRESSION: null

::PATHS::
- CHOICE: "Last chapter ignites"
  TARGET: last_chapter_ignites
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: INT. PAUL’S ROOM - CONTINUOUS
MOOD: Incendiary / Vengeful
CHARACTERS: Narrator, Paul, Annie
BACKGROUND_IMAGE: last_chapter_ignites.png
BACKGROUND_EDIT: "Paul's room, the last chapter ignites, Paul holds it like a torch"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The last chapter as Paul brings the match close to it and it bursts into flame. And Paul, holding it like the torch it is. Annie starts moving forward now.
  EXPRESSION: Vengeful
- CHARACTER: Annie
  LINE: No, no, NOT MISERY--NOT MY MISERY...!
  EXPRESSION: Desperate
- CHARACTER: Narrator
  LINE: He drops the last chapter into the soaked manuscript and
  EXPRESSION: null

::PATHS::
- CHOICE: "Manuscript bursts into flame"
  TARGET: manuscript_kaboom
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: INT. PAUL’S ROOM - CONTINUOUS
MOOD: Cataclysmic / Fiery
CHARACTERS: Narrator, Annie
BACKGROUND_IMAGE: manuscript_kaboom.png
BACKGROUND_EDIT: "Paul's room, the entire manuscript explodes into flames"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The manuscript, as KABOOM!, it bursts into flame and--
  EXPRESSION: Cataclysmic

::PATHS::
- CHOICE: "Annie is transfixed"
  TARGET: annie_transfixed
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: INT. PAUL’S ROOM - CONTINUOUS
MOOD: Determined / Charge
CHARACTERS: Narrator, Annie
BACKGROUND_IMAGE: annie_transfixed.png
BACKGROUND_EDIT: "Paul's room, Annie momentarily stunned by the fire, then charges"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Annie, transfixed by the sight for a moment, --and then she charges.
  EXPRESSION: Determined

::PATHS::
- CHOICE: "Annie rushes to the book"
  TARGET: annie_rushes_to_book
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: INT. PAUL’S ROOM - CONTINUOUS
MOOD: Desperate / Self-Sacrificing
CHARACTERS: Narrator, Annie
BACKGROUND_IMAGE: annie_rushes_to_book.png
BACKGROUND_EDIT: "Paul's room, Annie grabs the burning book, trying to smother flames"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The fire as Annie rushes to the book, stoops down, grabs it with both hands, brings the burning mass up to her body, both arms across it, trying to smother the flames--
  EXPRESSION: Desperate

::PATHS::
- CHOICE: "Paul attacks Annie"
  TARGET: paul_attacks_annie
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: INT. PAUL’S ROOM - CONTINUOUS
MOOD: Brutal / Violent
CHARACTERS: Narrator, Paul, Annie
BACKGROUND_IMAGE: paul_attacks_annie.png
BACKGROUND_EDIT: "Paul's room, Paul throws the typewriter at Annie"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Paul, grabbing the typewriter, raising it high above his head, then throwing it down on her with all his power and
  EXPRESSION: Brutal

::PATHS::
- CHOICE: "Typewriter crashes into Annie"
  TARGET: typewriter_crashes
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: INT. PAUL’S ROOM - CONTINUOUS
MOOD: Horrific / Painful
CHARACTERS: Narrator, Annie, Paul
BACKGROUND_IMAGE: typewriter_crashes.png
BACKGROUND_EDIT: "Paul's room, typewriter hits Annie, she screams in pain"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The typewriter, crashing into the back of her head.
  EXPRESSION: Horrific
- CHARACTER: Narrator
  LINE: Annie, screaming, driven to the floor by the blow, the book beneath her, and the flames fly up, her sweater is starting to burn and she's covered with shards of glass from the shattered bottle of champagne and some of the manuscript is hissing from the liquid, but she is able to struggle to her knees--
  EXPRESSION: Painful
- CHARACTER: Annie
  LINE: I'm going to kill you, you lying cocksucker...
  EXPRESSION: Enraged

::PATHS::
- CHOICE: "Annie pulls out gun"
  TARGET: annie_pulls_gun
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: INT. PAUL’S ROOM - CONTINUOUS
MOOD: Violent Confrontation / Struggle
CHARACTERS: Narrator, Annie, Paul
BACKGROUND_IMAGE: annie_pulls_gun.png
BACKGROUND_EDIT: "Paul's room, Annie draws a gun, Paul tackles her"

::SCRIPT::
- CHARACTER: Narrator
  LINE: As she struggles to her feet, she pulls out the gun and shoots at Paul, hitting him in the shoulder. Just as she's about to shoot again, Paul quickly wheels the chair up to her, throws himself out of the chair, and tackles her. The gun flies out of her hand and lands in the hallway, going off as it lands.
  EXPRESSION: Violent
- CHARACTER: Narrator
  LINE: They wrestle on the floor. Flames still around them, Paul gets on top of her, grabs some burning pages, stuffs them into her mouth, shouting --
  EXPRESSION: Brutal
- CHARACTER: Paul
  LINE: Here. Here. You want it? You want it? You can eat it--eat it--eat it till you fucking CHOKE--you sick, twisted fuck.
  EXPRESSION: Maniacal

::PATHS::
- CHOICE: "Paul forces more paper"
  TARGET: annie_hideous
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: INT. PAUL’S ROOM - CONTINUOUS
MOOD: Horrific Transformation / Agony
CHARACTERS: Narrator, Annie
BACKGROUND_IMAGE: annie_hideous.png
BACKGROUND_EDIT: "Paul's room, Annie is horrifically burned, making terrible sounds"

::SCRIPT::
- CHARACTER: Narrator
  LINE: And as he forces more paper into her mouth-- Annie, and she’s hideous--blistered, her hands claw at her throat. She makes horrible sounds, spitting the charred chunks of manuscript out of her mouth. Shards of glass are in her hair. Nov; a shriek and a tremendous jerk of her body and
  EXPRESSION: Agonized

::PATHS::
- CHOICE: "Paul falls away"
  TARGET: paul_falling_away
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: INT. PAUL’S ROOM - CONTINUOUS
MOOD: Eerie Silence / Lingering Agony
CHARACTERS: Narrator, Annie, Paul
BACKGROUND_IMAGE: paul_falling_away.png
BACKGROUND_EDIT: "Paul's room, Paul recoils, Annie slowly gets to her feet"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Paul, falling away --
  EXPRESSION: Detached
- CHARACTER: Narrator
  LINE: Annie, still making the sounds as she gets to her feet, and
  EXPRESSION: Unsettling

::PATHS::
- CHOICE: "Annie heads for the door"
  TARGET: annie_heads_for_door
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: INT. PAUL’S ROOM - CONTINUOUS
MOOD: Futile Escape / Painful End
CHARACTERS: Narrator, Paul, Annie
BACKGROUND_IMAGE: annie_heads_for_door.png
BACKGROUND_EDIT: "Paul's room, Annie stumbles towards the door, Paul kicks her ankle"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Paul, trying to crawl away after her. Annie-- heading for the door, she takes a step away from Paul, then another, then
  EXPRESSION: Desperate

::PATHS::
- CHOICE: "Paul kicks Annie's ankle"
  TARGET: paul_kicks_annie
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: INT. PAUL’S ROOM - CONTINUOUS
MOOD: Tragic Collapse / Impact
CHARACTERS: Narrator, Annie
BACKGROUND_IMAGE: paul_kicks_annie.png
BACKGROUND_EDIT: "Paul's room, Paul kicks Annie's ankle, she loses balance and falls"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Paul, suddenly kicking out with his shattered leg, screaming in pain as it crashes into her ankle and
  EXPRESSION: Painful
- CHARACTER: Narrator
  LINE: Annie, trying to keep her balance, not doing well, her arms windmilling as she fights for balance one last moment, fights and loses, and now, as she topples over--
  EXPRESSION: Tragic

::PATHS::
- CHOICE: "Annie's head slams into typewriter"
  TARGET: typewriter_collision
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: INT. PAUL’S ROOM - CONTINUOUS
MOOD: Final Impact / Catastrophe
CHARACTERS: Narrator
BACKGROUND_IMAGE: typewriter_collision.png
BACKGROUND_EDIT: "Paul's room, Annie's head collides violently with the typewriter"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The typewriter as she falls and her head slams into it, collides with the sharp metal and a
  EXPRESSION: Catastrophic

::SCENE::
LOCATION: Unknown Room
MOOD: Violent Climax
CHARACTERS: Narrator, Annie, Paul
BACKGROUND_IMAGE: unknown_room.png
BACKGROUND_EDIT: "Blood and chaos"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Great wound opens in her head. There is one final cry. Blood pours. It's over. All over. We are looking at a dead body.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Paul, exhausted, panting, lying there, trying to gather his energy. He starts to crawl for the door. Just as he reaches the doorjamb, an arm grabs his leg, and
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue the struggle"
  TARGET: paul_shrieking
  STATE_CHANGE: exhaustion = +1
  CONDITION: null

::SCENE::
LOCATION: Unknown Room
MOOD: Desperate Struggle
CHARACTERS: Narrator, Paul
BACKGROUND_IMAGE: unknown_room_struggle.png
BACKGROUND_EDIT: "Paul's perspective, struggling"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Paul, shrieking, and
  EXPRESSION: Terrified

::PATHS::
- CHOICE: "Continue the struggle"
  TARGET: annie_pulling
  STATE_CHANGE: fear = +1
  CONDITION: null

::SCENE::
LOCATION: Unknown Room
MOOD: Relentless Pursuit
CHARACTERS: Narrator, Annie, Paul
BACKGROUND_IMAGE: annie_pursuit.png
BACKGROUND_EDIT: "Annie's perspective, moving up on Paul"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Annie, pulling herself up his body and
  EXPRESSION: Relentless
- CHARACTER: Narrator
  LINE: Paul, trying to buck her off, but he can't and
  EXPRESSION: Helpless
- CHARACTER: Narrator
  LINE: Annie, the stronger, moving up on him, and
  EXPRESSION: Inevitable
- CHARACTER: Narrator
  LINE: Paul, his grip broken as he turns and
  EXPRESSION: Defeated
- CHARACTER: Narrator
  LINE: Annie, all-powerful, looming over him and
  EXPRESSION: Dominant
- CHARACTER: Narrator
  LINE: Paul, hitting up at her and
  EXPRESSION: Futile
- CHARACTER: Narrator
  LINE: Annie, swelling, and the blood pours down and if she feels his blows she doesn't show it and
  EXPRESSION: Unfeeling
- CHARACTER: Narrator
  LINE: Paul, whatever energy he has left he uses now, trying to twist and strike and as his body moves--
  EXPRESSION: Final Effort

::PATHS::
- CHOICE: "Grasp for a weapon"
  TARGET: metal_lamp
  STATE_CHANGE: desperation = +1
  CONDITION: null

::SCENE::
LOCATION: Unknown Room
MOOD: Glimmer of Hope
CHARACTERS: Narrator, Metal Based Floor Lamp
BACKGROUND_IMAGE: metal_lamp.png
BACKGROUND_EDIT: "Close up on a metal floor lamp"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Metal based floor lamp and
  EXPRESSION: Hopeful

::PATHS::
- CHOICE: "Seize the lamp"
  TARGET: paul_grabbing_lamp
  STATE_CHANGE: hope = +1
  CONDITION: null

::SCENE::
LOCATION: Unknown Room
MOOD: Turning the Tide
CHARACTERS: Narrator, Paul, Annie
BACKGROUND_IMAGE: paul_strikes.png
BACKGROUND_EDIT: "Paul swinging the lamp"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Paul, grabbing the thing, suddenly bringing it across his body, clobbering Annie in the face and
  EXPRESSION: Powerful Strike

::PATHS::
- CHOICE: "Observe Annie's reaction"
  TARGET: annie_startled
  STATE_CHANGE: relief = +1
  CONDITION: null

::SCENE::
LOCATION: Unknown Room
MOOD: Momentary Pause
CHARACTERS: Narrator, Annie
BACKGROUND_IMAGE: annie_startled.png
BACKGROUND_EDIT: "Annie recoiling from the blow"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Annie, startled by the power of the blow and for a moment she is stopped and
  EXPRESSION: Shocked

::PATHS::
- CHOICE: "Follow through with the attack"
  TARGET: paul_crunching_forehead
  STATE_CHANGE: triumph = +1
  CONDITION: null

::SCENE::
LOCATION: Unknown Room
MOOD: Decisive Blow
CHARACTERS: Narrator, Paul, Annie
BACKGROUND_IMAGE: paul_finishing_blow.png
BACKGROUND_EDIT: "Paul striking Annie's forehead"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Paul, as with everything he has left, he crunches her forehead with the sharp heavy metal base, just creams her as the air is forced out of her--
  EXPRESSION: Victorious

::PATHS::
- CHOICE: "Witness Annie's collapse"
  TARGET: annie_collapsing
  STATE_CHANGE: finality = +1
  CONDITION: null

::SCENE::
LOCATION: Unknown Room
MOOD: The End of Annie
CHARACTERS: Narrator, Annie, Paul
BACKGROUND_IMAGE: annie_collapses.png
BACKGROUND_EDIT: "Annie collapsing onto Paul"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Annie. Her eyes roll up into her head. For a moment all we see are the whites--then she collapses on Paul, a motionless mountain of slack flesh.
  EXPRESSION: Deceased

::PATHS::
- CHOICE: "Escape"
  TARGET: paul_scrambling_free
  STATE_CHANGE: survival = +1
  CONDITION: null

::SCENE::
LOCATION: Unknown Room/Corridor
MOOD: Escape and Sanctuary
CHARACTERS: Narrator, Paul
BACKGROUND_IMAGE: paul_escapes.png
BACKGROUND_EDIT: "Paul crawling out of the room and closing the door"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Paul, scrambling free, pushing her off him, crawling for the door--
  EXPRESSION: Relieved
- CHARACTER: Narrator
  LINE: Outside the door, as Paul crawls into view, makes it to the corridor, reaches back, closes the door, locks it. Safe, he collapses, exhausted against the wall opposite the door.
  EXPRESSION: Safe

::PATHS::
- CHOICE: "Rest and recover"
  TARGET: paul_awakened_dawn
  STATE_CHANGE: trauma = -1
  CONDITION: null

::SCENE::
LOCATION: Unknown Room/Corridor
MOOD: Dawn and Intrusion
CHARACTERS: Narrator, Paul
BACKGROUND_IMAGE: paul_awakened_dawn.png
BACKGROUND_EDIT: "Dawn light, Paul still against the wall"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Dissolve to: Paul. Hours later. It is dawn. He is awakened by a loud smashing at the front door. After a couple of heart-stopping pounds,
  EXPRESSION: Startled

::PATHS::
- CHOICE: "Observe the door breaking open"
  TARGET: front_door_smashes
  STATE_CHANGE: anxiety = +1
  CONDITION: null

::SCENE::
LOCATION: Front Door/Room
MOOD: Arrival of Authority
CHARACTERS: Narrator, Police Officers, Paul
BACKGROUND_IMAGE: police_arrival.png
BACKGROUND_EDIT: "Front door smashed open, police with guns"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The front door smashes open, revealing two cops with guns drawn.
  EXPRESSION: Authoritative
- CHARACTER: Narrator
  LINE: The policemen, hurrying to Paul. The Younger Cop kneels beside Paul.
  EXPRESSION: Concerned
- CHARACTER: Younger Cop
  LINE: It's the writer--the dead one--
  EXPRESSION: Informative
- CHARACTER: Paul
  LINE: --right! I’m the dead one--
  EXPRESSION: Weary
- CHARACTER: Older Cop
  LINE: Where's Sheriff McCain?
  EXPRESSION: Inquisitive
- CHARACTER: Paul
  LINE: He's in the cellar. She killed him.
  EXPRESSION: Distraught
- CHARACTER: Older Cop
  LINE: Annie Wilkes?
  EXPRESSION: Disbelieving
- CHARACTER: Paul
  LINE: Yeah. She's in there.
  EXPRESSION: Resigned

::PATHS::
- CHOICE: "Accompany the older cop"
  TARGET: older_cop_enters_room
  STATE_CHANGE: fear = +1
  CONDITION: null

::SCENE::
LOCATION: Inside the Bedroom
MOOD: Investigating the Scene
CHARACTERS: Narrator, Older Cop
BACKGROUND_IMAGE: bedroom_investigation.png
BACKGROUND_EDIT: "Older cop entering the room, gun ready"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The older cop, taking the key to the room, unlocks the door, throws it open, and as he steps inside--
  EXPRESSION: Cautious
- CHARACTER: Narrator
  LINE: The older cop has his gun ready to fire, but even with it tight in his hand, he's edgy as hell. He looks around--
  EXPRESSION: Tense
- CHARACTER: Narrator
  LINE: Glass and bloodstains on the floor. The charred remains of a manuscript. He kneels quickly, glances under the bed--nothing. He looks at the window--wide open.
  EXPRESSION: Observant

::PATHS::
- CHOICE: "Report findings"
  TARGET: paul_and_younger_cop_report
  STATE_CHANGE: confusion = +1
  CONDITION: null

::SCENE::
LOCATION: Bedroom Doorway/Corridor
MOOD: Discrepancy
CHARACTERS: Narrator, Older Cop, Paul, Younger Cop
BACKGROUND_IMAGE: report_discrepancy.png
BACKGROUND_EDIT: "Older cop at the doorway, Paul and younger cop waiting"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Paul and the younger cop. Pause. The older cop is in the doorway now.
  EXPRESSION: Expectant
- CHARACTER: Older Cop
  LINE: Mr. Sheldon? There’s no one in there.
  EXPRESSION: Puzzled

::PATHS::
- CHOICE: "Show Paul's shock"
  TARGET: paul_close_up_shock
  STATE_CHANGE: disbelief = +1
  CONDITION: null

::SCENE::
LOCATION: Unknown Room
MOOD: Shock and Disbelief
CHARACTERS: Narrator, Paul
BACKGROUND_IMAGE: paul_close_up_shock.png
BACKGROUND_EDIT: "Close up on Paul's face in shock"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Paul: Close up. In shock.
  EXPRESSION: Shocked

::PATHS::
- CHOICE: "Transition to the future"
  TARGET: palm_court_plaza_hotel
  STATE_CHANGE: trauma = -2
  CONDITION: null

::SCENE::
LOCATION: Palm Court - Plaza Hotel
MOOD: One Year Later - Serene
CHARACTERS: Narrator, Paul, Marcia Sindell
BACKGROUND_IMAGE: plaza_hotel_happy_paul.png
BACKGROUND_EDIT: "Paul looking healthy and happy"

::SCRIPT::
- CHARACTER: Narrator
  LINE: This legend appear: One year later
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Marcia Sindell is seated at a table. Paul enters, walking briskly, and he's never looked this good before. He's gained his weight back, his color is normal again. He appears to be, for the first time in the movie, a jaunty, happy figure.
  EXPRESSION: Joyful
- CHARACTER: Paul
  LINE: Sorry I'm late. Jenny's basketball game went into overtime. If anybody ever told me I’d have a daughter who’d get a triple double, I'd...
  EXPRESSION: Enthusiastic
- CHARACTER: Sindell
  LINE: Did they win?
  EXPRESSION: Curious
- CHARACTER: Paul
  LINE: Yeah. They’re in the semis.
  EXPRESSION: Proud
- CHARACTER: Sindell
  LINE: Here it is. Very first copy.
  EXPRESSION: Significant
- CHARACTER: Narrator
  LINE: And she hands him a wrapped package. Paul sits, begins unwrapping it. It's a book. A new one by Paul Sheldon. The Higher Education of J. Phillip Stone. Paul turns it over gently in his hands.
  EXPRESSION: Appreciative

::PATHS::
- CHOICE: "Listen to praise for the book"
  TARGET: sindell_book_praise
  STATE_CHANGE: accomplishment = +1
  CONDITION: null

::SCENE::
LOCATION: Palm Court - Plaza Hotel
MOOD: Critical Acclaim
CHARACTERS: Narrator, Sindell, Paul
BACKGROUND_IMAGE: sindell_book_praise.png
BACKGROUND_EDIT: "Sindell talking about the book's reception"

::SCRIPT::
- CHARACTER: Sindell
  LINE: The word I’m getting is the Times review is gonna be a love letter.
  EXPRESSION: Hopeful
- CHARACTER: Paul
  LINE: That'd be a first.
  EXPRESSION: Skeptical
- CHARACTER: Sindell
  LINE: And my contacts at Time and Newsweek tell me they're both raves. And don't laugh--for the first time, I think you’ve got a shot at some prizes.
  EXPRESSION: Excited
- CHARACTER: Paul
  LINE: Great.
  EXPRESSION: Flat
- CHARACTER: Sindell
  LINE: I thought you'd be thrilled. You're being taken seriously.
  EXPRESSION: Encouraging
- CHARACTER: Paul
  LINE: I'm delighted the critics are liking it, and I hope the people like it, too. But it’s not why I wrote the book.
  EXPRESSION: Sincere

::PATHS::
- CHOICE: "Reveal his true motivation"
  TARGET: paul_close_up_peace
  STATE_CHANGE: self_awareness = +1
  CONDITION: null

::SCENE::
LOCATION: Palm Court - Plaza Hotel
MOOD: Inner Peace and Reflection
CHARACTERS: Narrator, Paul
BACKGROUND_IMAGE: paul_close_up_peace.png
BACKGROUND_EDIT: "Close up on Paul, conveying peace"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Paul: Close up. There is a genuine sense of peace about him. He has been through the fire and survived.
  EXPRESSION: Peaceful
- CHARACTER: Paul
  LINE: I like it. Remember how you once said I live my whole life as if I'm in danger of being found out? Well, I believe I've managed to get that guy down on paper. Don't think I'm completely nuts, but in some way, Annie Wilkes, that whole experience, helped me.
  EXPRESSION: Reflective

::PATHS::
- CHOICE: "Consider a non-fiction book"
  TARGET: sindell_non_fiction_suggestion
  STATE_CHANGE: introspection = +1
  CONDITION: null

::SCENE::
LOCATION: Palm Court - Plaza Hotel
MOOD: Agent's Proposition
CHARACTERS: Narrator, Sindell, Paul
BACKGROUND_IMAGE: sindell_non_fiction_suggestion.png
BACKGROUND_EDIT: "Sindell looking business-like"

::SCRIPT::
- CHARACTER: Sindell
  LINE: Paul, since you brought her up, I have to ask you this, or I'd be drummed out of the agents' union--what about a non-fiction book? The truth about what went on in that house.
  EXPRESSION: Business-like
- CHARACTER: Paul
  LINE: Gee, Marcia, if I didn't know you better, I'd think you were suggesting I dredge up the worst horror of my life just so we could make a few bucks.
  EXPRESSION: Sarcastic
- CHARACTER: Sindell
  LINE: Now you've hurt me, Paul.
  EXPRESSION: Playful

::PATHS::
- CHOICE: "Glance around"
  TARGET: paul_glancing_past_marcia
  STATE_CHANGE: unease = +1
  CONDITION: null

::SCENE::
LOCATION: Palm Court - Plaza Hotel
MOOD: Distant Disturbance
CHARACTERS: Narrator, Paul, Marcia
BACKGROUND_IMAGE: paul_glancing_past_marcia.png
BACKGROUND_EDIT: "Paul looking past Marcia"

::SCRIPT::
- CHARACTER: Narrator
  LINE: As Paul glances around...
  EXPRESSION: Distracted

::PATHS::
- CHOICE: "Focus on the disturbance"
  TARGET: dessert_trolley_annie
  STATE_CHANGE: paranoia = +1
  CONDITION: null

::SCENE::
LOCATION: Palm Court - Plaza Hotel
MOOD: Unsettling Recognition
CHARACTERS: Narrator, Paul, Sindell, Annie (as Waitress)
BACKGROUND_IMAGE: dessert_trolley_annie.png
BACKGROUND_EDIT: "Dessert trolley with a waitress resembling Annie"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Paul, looking past Marcia.
  EXPRESSION: Uneasy
- CHARACTER: Narrator
  LINE: Dessert trolley, some distance away, being pushed by a waitress. It is Annie.
  EXPRESSION: Foreboding
- CHARACTER: Narrator
  LINE: Sindell. I thought you were over it.
  EXPRESSION: Concerned
- CHARACTER: Paul
  LINE: I am. Well, maybe not completely--
  EXPRESSION: Hesitant

::PATHS::
- CHOICE: "Observe the trolley approaching"
  TARGET: dessert_trolley_moving_closer
  STATE_CHANGE: fear = +1
  CONDITION: null

::SCENE::
LOCATION: Palm Court - Plaza Hotel
MOOD: Growing Dread
CHARACTERS: Narrator, Annie (as Waitress), Paul, Sindell
BACKGROUND_IMAGE: dessert_trolley_moving_closer.png
BACKGROUND_EDIT: "Dessert trolley moving closer, Annie reaching for a knife"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The dessert trolley, moving inexorably closer to Paul. Annie reaches down and pulls out a very sharp knife.
  EXPRESSION: Menacing

::PATHS::
- CHOICE: "Continue to express Paul's feelings"
  TARGET: paul_annie_knife_dialogue
  STATE_CHANGE: dread = +1
  CONDITION: null

::SCENE::
LOCATION: Palm Court - Plaza Hotel
MOOD: Lingering Trauma
CHARACTERS: Narrator, Paul, Sindell, Annie (as Waitress)
BACKGROUND_IMAGE: paul_annie_knife_dialogue.png
BACKGROUND_EDIT: "Paul talking, Annie with knife in background"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Paul and Sindell
  EXPRESSION: null
- CHARACTER: Paul
  LINE: I don't know if you can ever be totally over something like that--I just don't think about it as much anymore, and when I do, it's not so terrifying.
  EXPRESSION: Reflective
- CHARACTER: Narrator
  LINE: Annie, with the knife raised.
  EXPRESSION: Threatening
- CHARACTER: Narrator
  LINE: Paul, staring up at Annie.
  EXPRESSION: Petrified
- CHARACTER: Paul
  LINE: I mean, once they found her body, my nightmares stopped.
  EXPRESSION: Hopeful

::PATHS::
- CHOICE: "Reveal the waitresses true identity"
  TARGET: paul_and_annie_waitress
  STATE_CHANGE: delusion = +1
  CONDITION: null

::SCENE::
LOCATION: Palm Court - Plaza Hotel
MOOD: False Security
CHARACTERS: Narrator, Paul, Waitress (Annie)
BACKGROUND_IMAGE: paul_and_annie_waitress.png
BACKGROUND_EDIT: "Waitress standing by the trolley, knife in hand"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Paul and Annie--only it isn't Annie, just a Waitress. She stands by the trolley, the knife in her hand, ready to slice whatever anyone wants.
  EXPRESSION: Deceptive
- CHARACTER: Waitress
  LINE: Would you care for anything?
  EXPRESSION: Polite

::PATHS::
- CHOICE: "Order dessert"
  TARGET: paul_order_dessert
  STATE_CHANGE: irony = +1
  CONDITION: null

::SCENE::
LOCATION: Palm Court - Plaza Hotel
MOOD: Final Moment of Peace
CHARACTERS: Narrator, Paul
BACKGROUND_IMAGE: paul_order_dessert.png
BACKGROUND_EDIT: "Paul smiling, soft music in the background"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Paul: The smile holds. In the background now, soft music: someone might be playing "Liberace."
  EXPRESSION: Content
- CHARACTER: Paul
  LINE: Cut me something sinful...
  EXPRESSION: Playful

::PATHS::
- CHOICE: "Fade out"
  TARGET: final_fade_out
  STATE_CHANGE: resolution = +1
  CONDITION: null

::SCENE::
LOCATION: Palm Court - Plaza Hotel
MOOD: End
CHARACTERS: Narrator
BACKGROUND_IMAGE: end_screen.png
BACKGROUND_EDIT: "Fade to black"

::SCRIPT::
- CHARACTER: Narrator
  LINE: HOLD ON PAUL
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: FINAL FADE OUT:
  EXPRESSION: null

::PATHS::
- CHOICE: "End of Movie"
  TARGET: end_movie
  STATE_CHANGE: null
  CONDITION: null

