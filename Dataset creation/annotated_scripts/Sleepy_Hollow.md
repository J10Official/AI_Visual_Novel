::SCENE::
LOCATION: City Streets
MOOD: Mysterious
CHARACTERS: Narrator, Two Constables, Ichabod Crane
BACKGROUND_IMAGE: city_streets_night.png
BACKGROUND_EDIT: "Empty cobblestone streets, stately buildings at night."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Empty cobblestone streets are bordered by stately buildings.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: A rapidly clanging bell breaks the silence from afar.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: INSERT TITLE: New York City
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Two constables clamor around a corner, lanterns held high, listening.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: They disappear down an alleyway.
  EXPRESSION: null

::PATHS::
- CHOICE: "Follow the sound"
  TARGET: city_waterfront
  STATE_CHANGE: curiosity = +1
  CONDITION: null

::SCENE::
LOCATION: City Waterfront
MOOD: Ominous
CHARACTERS: Narrator, Constable One, Constable Two, Man's Voice, Ichabod Crane
BACKGROUND_IMAGE: city_waterfront_night.png
BACKGROUND_EDIT: "Piers bordering the Hudson River at night."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Elsewhere, piers border the Hudson. The bell is louder here.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The two constables arrive, searching, pistols drawn.
  EXPRESSION: null
- CHARACTER: Constable One
  LINE: Where are you?!
  EXPRESSION: Anxious
- CHARACTER: Man's Voice
  LINE: Here...! Over here!
  EXPRESSION: Strained
- CHARACTER: Narrator
  LINE: The constables hurry to the river's edge...
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Down an embankment, the MAN, another constable, has his back to us.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: He's waist deep in dark water, throwing aside his alarm bell, struggling to pull something from the murk...
  EXPRESSION: null
- CHARACTER: Man
  LINE: I need your help with this.
  EXPRESSION: Strained
- CHARACTER: Narrator
  LINE: Constable Two and Constable One move forward, wary.
  EXPRESSION: null
- CHARACTER: Constable One
  LINE: Constable Crane? Ichabod Crane... is that you?
  EXPRESSION: Skeptical
- CHARACTER: Narrator
  LINE: The MAN turns. Meet ICHABOD CRANE, handsome, eyes piercing but nervous and unsettled.
  EXPRESSION: null
- CHARACTER: Ichabod Crane
  LINE: None other, and not only me... I have found something...
  EXPRESSION: Shaken
- CHARACTER: Narrator
  LINE: Ichabod drags a bloated male corpse out from the water. He backs away, shaken, looks to the constables...
  EXPRESSION: null
- CHARACTER: Ichabod Crane
  LINE: ...which was lately a man.
  EXPRESSION: Shaken

::PATHS::
- CHOICE: "Examine the body"
  TARGET: city_watchhouse_jail
  STATE_CHANGE: concern = +1
  CONDITION: null

::SCENE::
LOCATION: City Watchhouse, Jail
MOOD: Grim
CHARACTERS: Narrator, High Constable, Constable One, Ichabod Crane, Constable Two
BACKGROUND_IMAGE: city_watchhouse_jail_night.png
BACKGROUND_EDIT: "Dank, cavernous room in a jail."

::SCRIPT::
- CHARACTER: Narrator
  LINE: In a dank, cavernous room, the distinguished HIGH CONSTABLE lifts a blanket off the corpse in a wheelbarrow manned by Constable Two.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Constable One and Ichabod are near, watching.
  EXPRESSION: null
- CHARACTER: High Constable
  LINE: Burn it.
  EXPRESSION: Dismissive
- CHARACTER: Constable One
  LINE: Yes, sir.
  EXPRESSION: Obedient
- CHARACTER: Narrator
  LINE: Constable Two wheels the corpse down a ramp to another room.
  EXPRESSION: null
- CHARACTER: Ichabod Crane
  LINE: Just a moment, if I may... we do not yet know the cause of death.
  EXPRESSION: Analytical
- CHARACTER: High Constable
  LINE: When you find 'em in the river, cause of death is drowning.
  EXPRESSION: Impatient
- CHARACTER: Ichabod Crane
  LINE: Possibly so if there is water in the lungs, but... by pathology we might determine whether or not he was dead when he went into the river.
  EXPRESSION: Determined
- CHARACTER: High Constable
  LINE: Cut him up? Are we heathens? Let him rest in peace -- in one piece as according to God and the New York Department of Health.
  EXPRESSION: Stern
- CHARACTER: Narrator
  LINE: Ichabod is about to protest, but stops himself, frustrated.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Two thuggish constables -- different ones -- bring in a bleeding semiconscious man.
  EXPRESSION: null
- CHARACTER: High Constable
  LINE: What happened to him?
  EXPRESSION: Inquisitive
- CHARACTER: Thuggish Constable
  LINE: Nothing, sir. Arrested for burglary.
  EXPRESSION: Gruff
- CHARACTER: Narrator
  LINE: The constables throw him against the bars of the slammer while one of them opens the cage door. With their leather truncheons, the cops beat their prisoner into the cage and lock him in.
  EXPRESSION: Brutal
- CHARACTER: High Constable
  LINE: Good work...
  EXPRESSION: Approving
- CHARACTER: Narrator
  LINE: Ichabod hurries to follow his two constables and the corpse.
  EXPRESSION: null

::PATHS::
- CHOICE: "Follow the corpse"
  TARGET: city_watchhouse_exterior
  STATE_CHANGE: persistence = +1
  CONDITION: null

::SCENE::
LOCATION: City Watchhouse
MOOD: Bustling
CHARACTERS: Narrator
BACKGROUND_IMAGE: city_watchhouse_exterior_day.png
BACKGROUND_EDIT: "The metropolis thrives, horsedrawn vehicles, people on the street."

::SCRIPT::
- CHARACTER: Narrator
  LINE: The metropolis thrives; horsedrawn vehicles plodding, men, women and children, merchants and tradesmen everywhere.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Men are held in chains and gibbets in front of the Watchhouse.
  EXPRESSION: Stark

::PATHS::
- CHOICE: "Enter the Watchhouse"
  TARGET: city_watchhouse_jail_audition
  STATE_CHANGE: observation = +1
  CONDITION: null

::SCENE::
LOCATION: City Watchhouse, Jail
MOOD: Absurd
CHARACTERS: Narrator, City Officials, Applicants, Ichabod Crane, Inventor, Burgomaster, High Constable, Magistrates, Aldermen, Spotty Man
BACKGROUND_IMAGE: city_watchhouse_jail_audition.png
BACKGROUND_EDIT: "Audition scene with crime-fighting devices."

::SCRIPT::
- CHARACTER: Narrator
  LINE: We enter midway into a "Audition Scene." A row of city officials are "auditioning" applicants (mostly obvious cranks and eccentrics) with devices for crime fighting and crime solving. The applicants are crowded together to one side, waiting their turn. Ichabod, holding only papers and books, is among them.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: "On Stage" at this moment is an inventor demonstrating his invention, of which more in a moment. Facing the "stage" is the Burgomaster, flanked by the High Constable (who has a list of names) and various magistrates and aldermen.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The Inventor is demonstrating a combination wallet and mousetrap.
  EXPRESSION: null
- CHARACTER: Inventor
  LINE: ...and in a few weeks, the plague of pickpockets will be a thing of the past!
  EXPRESSION: Enthusiastic
- CHARACTER: Narrator
  LINE: He shows how to set the trap-spring.
  EXPRESSION: null
- CHARACTER: Inventor
  LINE: Give me a dozen constables in gentleman's dress... mixing with the crowds where pickpockets are rife!
  EXPRESSION: Confident
- CHARACTER: Narrator
  LINE: He produces a fake hand-on-a-stick and does the business.
  EXPRESSION: null
- CHARACTER: Inventor
  LINE: A stealthy hand dips into the gentleman's pocket... and -- !
  EXPRESSION: Dramatic
- CHARACTER: Narrator
  LINE: There is the sound of the trap snapping shut and the Inventor withdraws the fake hand with its fingers chopped off. The Officials wince, impressed.
  EXPRESSION: Shocking
- CHARACTER: Burgomaster
  LINE: Thank you. We will take your device under consideration, Mr. Vanderbilt... Next!
  EXPRESSION: Appreciative
- CHARACTER: Narrator
  LINE: A spotty man starts dragging a man-sized cage contraption to center stage... while Ichabod tries to get the attention of the Officials.
  EXPRESSION: null
- CHARACTER: Ichabod Crane
  LINE: Gentlemen! -- the Millennium is almost upon us -- In a few months we will be living in the nineteenth century -- !
  EXPRESSION: Urgent
- CHARACTER: High Constable
  LINE: Wait your turn, Constable Crane --
  EXPRESSION: Firm
- CHARACTER: Ichabod Crane
  LINE: These devices are unworthy of a modern civilization...
  EXPRESSION: Disdainful
- CHARACTER: Burgomaster
  LINE: Quiet! -- Next, I say!
  EXPRESSION: Authoritative
- CHARACTER: Spotty Man
  LINE: Thank you, sir!
  EXPRESSION: Proud
- CHARACTER: Narrator
  LINE: He turns proudly to his man-size cage, whose front hinges down for ingress.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The floor of the cage is a steel plate. A "writing board" for signing confessions is attached to the inside of the cage.
  EXPRESSION: null
- CHARACTER: Spotty Man
  LINE: The Tomkins self-locking Confessional is cheap at the price and will last for years with just an occasional wipe with a damp cloth... When the villain steps on the floor plate...
  EXPRESSION: Boastful
- CHARACTER: Narrator
  LINE: Ichabod, dropping books and papers around his feet, is feverishly writing on a blank page (his "traveling inkpot" is hung around his neck).
  EXPRESSION: Frenzied
- CHARACTER: Ichabod Crane
  LINE: Arrest that man!
  EXPRESSION: Accusatory
- CHARACTER: High Constable
  LINE: Arrest... ?
  EXPRESSION: Stunned
- CHARACTER: Ichabod Crane
  LINE: I accuse him of murder!
  EXPRESSION: Bold
- CHARACTER: Spotty Man
  LINE: What the devil are you talking about, you loon?!
  EXPRESSION: Outraged
- CHARACTER: Narrator
  LINE: Ichabod takes two steps toward him and gives him a violent shove in the chest. The Spotty Man staggers back into his cage, which self-locks, and at the same time a head clamp descends from the top, gripping the Spotty Man's head. His arms flail about as he yells.
  EXPRESSION: Chaotic
- CHARACTER: Narrator
  LINE: Ichabod slaps his page on the writing board, offers his pen.
  EXPRESSION: null
- CHARACTER: Ichabod Crane
  LINE: Sign here!
  EXPRESSION: Demanding
- CHARACTER: Spotty Man
  LINE: The release handle...
  EXPRESSION: Pleading
- CHARACTER: Ichabod Crane
  LINE: Not till you confess...!
  EXPRESSION: Unyielding
- CHARACTER: Narrator
  LINE: Uproar around him, Ichabod waits as the prisoner signs the paper, then pulls the "release handle."
  EXPRESSION: null
- CHARACTER: Ichabod Crane
  LINE: I have here a confession to the murder of a man I fished out of the river last night!
  EXPRESSION: Triumphant
- CHARACTER: High Constable
  LINE: Stand down!
  EXPRESSION: Furious
- CHARACTER: Ichabod Crane
  LINE: I stand up, for sense and justice! Our jails overflow with men and women convicted on confessions worth no more than this one!
  EXPRESSION: Righteous
- CHARACTER: Narrator
  LINE: The High Constable bangs a gavel until he gets some silence for the Burgomaster. Meanwhile, the Spotty Man is rescued by his friends.
  EXPRESSION: null
- CHARACTER: Burgomaster
  LINE: Constable, this is a song we have heard from you more than once but never before with this discordant accompaniment. I have two courses open to me. First, I can let you cool your heels in the cells until you learn respect for the dignity of my office...
  EXPRESSION: Measured
- CHARACTER: Ichabod Crane
  LINE: I beg pardon. I only meant well. Why am I the only one who sees that to solve crimes, to detect the guilty, we must use our brains? -- to recognize vital clues, using up-to-date scientific --
  EXPRESSION: Passionate
- CHARACTER: Burgomaster
  LINE: Which brings me to the second course. Constable Crane, there is a town upstate, two days' journey to the north in the Hudson Highlands. It is a place called Sleepy Hollow. Have you heard of it?
  EXPRESSION: Inquisitive
- CHARACTER: Ichabod Crane
  LINE: I have not.
  EXPRESSION: Ignorant
- CHARACTER: Burgomaster
  LINE: An isolated farming community, mostly Dutch. Three persons have been murdered there, all within a fortnight... each found with their head lopped off.
  EXPRESSION: Grave
- CHARACTER: Ichabod Crane
  LINE: Lopped off?
  EXPRESSION: Shocked
- CHARACTER: Burgomaster
  LINE: Clean as dandelion heads, apparently. Now, these ideas of yours, they have never been put to the test...
  EXPRESSION: Challenging
- CHARACTER: Ichabod Crane
  LINE: I have never been allowed to put them to the test!
  EXPRESSION: Frustrated
- CHARACTER: Burgomaster
  LINE: Just so, granted. So you take your experimentations to Sleepy Hollow and deduce, er detect the murderer. Bring him here to face our good justice. Will you do this?
  EXPRESSION: Hopeful
- CHARACTER: Ichabod Crane
  LINE: I shall, gladly.
  EXPRESSION: Determined
- CHARACTER: Burgomaster
  LINE: And remember -- it is you, Ichabod Crane, who is now put to the test.
  EXPRESSION: Encouraging
- CHARACTER: Narrator
  LINE: The Burgomaster smiles encouragingly.
  EXPRESSION: null

::PATHS::
- CHOICE: "Accept the mission"
  TARGET: ichabod_home
  STATE_CHANGE: courage = +1, mission = true
  CONDITION: null

::SCENE::
LOCATION: Ichabod's Home, 2nd Floor
MOOD: Reflective
CHARACTERS: Narrator
BACKGROUND_IMAGE: ichabod_home_2nd_floor.png
BACKGROUND_EDIT: "Interior of Ichabod's home, 2nd floor."

::SCRIPT::
- CHARACTER: Narrator
  LINE: INT/EXT. ICHABOD'S HOME, 2ND FLOOR
  EXPRESSION: null

::PATHS::
- CHOICE: "Prepare for the journey"
  TARGET: travel_to_sleepy_hollow
  STATE_CHANGE: preparation = +1
  CONDITION: null

::SCENE::
LOCATION: Ichabod's Room
MOOD: Melancholy
CHARACTERS: Narrator, Ichabod
BACKGROUND_IMAGE: ichabod_room.png
BACKGROUND_EDIT: "Dimly lit room filled with books, papers, chemicals, and anatomy charts. A small bed is visible. Daytime."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Piles of BOOKS and PAPERS, JARS of CHEMICALS, MAGNIFYING GLASSES, CHALKBOARDS covered with scrawl and ANATOMY CHARTS above a small bed.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: AT THE WINDOW, Ichabod holds a bird cage with a red CARDINAL inside.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: He opens the cage and the bird flies free...
  EXPRESSION: null
- CHARACTER: Ichabod
  LINE: Such a day for such a sad farewell, this is good-bye, my sweet...
  EXPRESSION: Sad
- CHARACTER: Narrator
  LINE: Ichabod watches it go, sad, then looks down. A COACH halts in the street below. The forlorn DRIVER looks up.
  EXPRESSION: null

::PATHS::
- CHOICE: "Depart the city"
  TARGET: nyc_streets
  STATE_CHANGE: melancholy = -1
  CONDITION: null

::SCENE::
LOCATION: New York City Streets
MOOD: Transition
CHARACTERS: Narrator, Ichabod, Coach Driver
BACKGROUND_IMAGE: nyc_streets.png
BACKGROUND_EDIT: "City streets giving way to a dirt road leading to wilderness. Daytime."

::SCRIPT::
- CHARACTER: Narrator
  LINE: ICHABOD'S COACH leaves city limits, forgoing civilization... following a dirt road to forested wilderness.
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue into the forest"
  TARGET: upstate_forests_night
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: New York Forests
MOOD: Foreboding
CHARACTERS: Narrator, Ichabod, Wolf
BACKGROUND_IMAGE: ny_forests_night.png
BACKGROUND_EDIT: "Dark forest at night, coach lanterns providing light. Tight foliage. Nighttime."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Coach lanterns light the way as the coach lumbers along, caressed by tight foliage. A WOLF is HEARD HOWLING.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Ichabod looks out, unnerved, shuts the window's curtain.
  EXPRESSION: Unnerved

::PATHS::
- CHOICE: "Continue the journey"
  TARGET: upstate_forests_day
  STATE_CHANGE: fear = +1
  CONDITION: null

::SCENE::
LOCATION: Upstate Forests
MOOD: Peaceful
CHARACTERS: Narrator, Ichabod
BACKGROUND_IMAGE: upstate_forests_day.png
BACKGROUND_EDIT: "Sun-dappled forest. Daytime."

::SCRIPT::
- CHARACTER: Narrator
  LINE: The coach moves through sun dappled forest...
  EXPRESSION: null

::PATHS::
- CHOICE: "Arrive at destination"
  TARGET: ichabod_coach_interior
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Ichabod's Coach Interior
MOOD: Contemplative
CHARACTERS: Narrator, Ichabod
BACKGROUND_IMAGE: ichabod_coach_interior.png
BACKGROUND_EDIT: "Interior of a coach. Daytime."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Ichabod checks the contents of a LEATHER SATCHEL in his lap. He pauses a moment, studying the palm of his hand.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Ichabod touches the strange SCARS on both his palms: evenly dispersed, tiny dots of tissue. Many scars. After a moment, he returns to looking through his satchel.
  EXPRESSION: null

::PATHS::
- CHOICE: "Proceed to Sleepy Hollow"
  TARGET: sleepy_hollow_road
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Sleepy Hollow, The Long Straight Road
MOOD: Uncertain
CHARACTERS: Narrator, Ichabod
BACKGROUND_IMAGE: sleepy_hollow_road.png
BACKGROUND_EDIT: "A long straight road bordered by massive stone pillars. Late afternoon."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Ichabod stands between two massive STONE PILLARS. He's unsure, turning to watch his coach leave him behind.
  EXPRESSION: Uncertain
- CHARACTER: Narrator
  LINE: Ichabod picks up his bags and heads between the pillars, starting up a LONG STRAIGHT ROAD. He does not notice, in the tree limbs above: THREE DEAD RAVENS, hung by twine.
  EXPRESSION: null

::PATHS::
- CHOICE: "Enter the town"
  TARGET: sleepy_hollow_town_square
  STATE_CHANGE: unease = +1
  CONDITION: null

::SCENE::
LOCATION: Sleepy Hollow, Town Square
MOOD: Ominous
CHARACTERS: Narrator, Ichabod, Elderly Woman, Man
BACKGROUND_IMAGE: sleepy_hollow_town_square.png
BACKGROUND_EDIT: "Dusk. A church and graveyard are visible. Businesses and homes line the road. Dusk."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Ichabod walks on, passing a CHURCH and GRAVEYARD. The road ahead is bordered by rows of businesses and two-story homes.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Ichabod enters the TOWN SQUARE proper. And ELDERLY WOMAN stands in a doorway, watching Ichabod. Ichabod tips his hat. The woman backs away, shuts her door.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Ichabod continues. He looks up... a MAN closes the shutters of a second-story window.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: As Ichabod continues he sees that there are two or three Riflemen placed at vantage points on the roofs and also, when he looks back, a Rifleman up on the Church Tower. The whole village is like a Western town waiting for an attack.
  EXPRESSION: Fearful

::PATHS::
- CHOICE: "Continue to the wooden bunker"
  TARGET: wooden_bunker
  STATE_CHANGE: fear = +2
  CONDITION: null

::SCENE::
LOCATION: Wooden Bunker
MOOD: Tense
CHARACTERS: Narrator, Ichabod, Young Masbath, Jonathan Masbath, Dirt Farmers
BACKGROUND_IMAGE: wooden_bunker.png
BACKGROUND_EDIT: "A strange wooden bunker with a large bell. Several dirt farmers with rifles gathered. Dusk."

::SCRIPT::
- CHARACTER: Narrator
  LINE: A strange WOODEN BUNKER, like a small fortress with a HUGE BELL mounted on top, sits in a field. SEVERAL DIRT FARMERS are gathered, all with rifles.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Ichabod stops as he walks, looking at this...
  EXPRESSION: Puzzled
- CHARACTER: Narrator
  LINE: A boy, YOUNG MASBATH, aged 10, comes to the Designated Rifleman, JONATHAN MASBATH, with food and drink, i.e., a picnic tied up in cloth and a stone bottle of beer. Masbath Senior takes the picnic and gives Young Masbath an affectionate pat. He smiles confidently.
  EXPRESSION: null
- CHARACTER: Jonathan Masbath
  LINE: Don't worry, son.
  EXPRESSION: Confident
- CHARACTER: Narrator
  LINE: One farmer comes to lead Young Masbath away as Jonathan heads into the BUNKER, taking several rifles.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: In front of the BUNKER, across a field, other dirt farmers light TORCH POSTS in a line along the forest edge.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Ichabod ponders this as he trudges along...
  EXPRESSION: Pondering

::PATHS::
- CHOICE: "Head towards the Van Tassel house"
  TARGET: van_tassel_house_exterior
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Van Tassel House
MOOD: Grand
CHARACTERS: Narrator, Ichabod
BACKGROUND_IMAGE: van_tassel_house.png
BACKGROUND_EDIT: "A grand manor house on a hill. Windows are aglow. Dusk."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Ahead on a hill: the grand Van Tassel MANOR HOUSE, windows aglow.
  EXPRESSION: null

::PATHS::
- CHOICE: "Enter the house"
  TARGET: van_tassel_house_door
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Van Tassel House, Front Door
MOOD: Lively
CHARACTERS: Narrator, Ichabod, Sarah, Doctor Lancaster, Kissing Couple
BACKGROUND_IMAGE: van_tassel_house_door.png
BACKGROUND_EDIT: "The front porch of the Van Tassel house at night. Jack-o'-lanterns glow. A harvest party is in progress inside. Night."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Ichabod puts down his bags (a suitcase and a leather box-bag) but keeps his satchel.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: JACK-O'-LANTERNS glow on the porch.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: A KISSING COUPLE are lustfully busy in a dark corner of the porch. The woman is a pretty servant, SARAH. The man we will know as DOCTOR LANCASTER.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Ichabod almost blunders into them, causing a little panic and embarrassment, in which Ichabod shares, and as he mumbles apologies and opens the door, a shaft of light identifies the couple for our further reference.
  EXPRESSION: Embarrassed
- CHARACTER: Narrator
  LINE: The open door reveals the MAIN HALL and FOYER...
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: There's a harvest party in progress. PEOPLE are gathered. QUIET MUSIC is HEARD from elsewhere.
  EXPRESSION: null

::PATHS::
- CHOICE: "Enter the party"
  TARGET: van_tassel_sitting_room
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Van Tassel House, Sitting Room
MOOD: Social
CHARACTERS: Narrator, Ichabod, Men, Women, Girl, Children, Young Men, Ladies, Brom Van Brunt, Doctor Lancaster, Sarah, Blindfolded Woman, Katrina Van Tassel, Baltus Van Tassel, Lady Van Tassel, Rifleman, Magistrate Philipse, Reverend Steenwyck, Notary Hardenbrook, Musicians
BACKGROUND_IMAGE: van_tassel_sitting_room.png
BACKGROUND_EDIT: "A room filled with people at a harvest party. Men and women talking in groups. Music is heard. Night."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Ichabod opens a door. MEN and WOMEN eat and drink, talking quietly in groups. Ichabod looks around, daunted, tentatively makes his way...
  EXPRESSION: Daunted
- CHARACTER: Narrator
  LINE: Ichabod bumps into a few people, excusing himself. He mops his sweaty brow, finds a pretty girl.
  EXPRESSION: Sweaty
- CHARACTER: Ichabod
  LINE: Pardon my intrusion, I seek Baltus Van Tassel but --
  EXPRESSION: Polite
- CHARACTER: Girl
  LINE: In the parlor, sir, further on.
  EXPRESSION: Helpful
- CHARACTER: Narrator
  LINE: Ichabod thanks her, continues...
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Ahead, CHILDREN, YOUNG MEN and LADIES in a circle taunt a BLINDFOLDED YOUNG WOMAN spun around by the handsome, barrel-chested man, BROM VAN BRUNT. Brom releases the woman. Everyone quiets, avoiding her searching hands.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The Blindfolded Woman circles slowly, chanting a REFRAIN that makes the CHILDREN and even some of the younger WOMEN shiver with pleasurable fright. They giggle nervously and hush each other up.
  EXPRESSION: null
- CHARACTER: Blindfolded Woman
  LINE: "The Pickety Witch, the Pickety Witch, who's got a kiss for the pickety witch?"
  EXPRESSION: Playful
- CHARACTER: Narrator
  LINE: She makes a lunge, grabbing empty air, just missing BROM; everyone moans humorously. Doctor Lancaster slips back into the party, and Sarah likewise.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Ichabod is trying to pass through to reach the farther door... and on the NEXT REFRAIN finds himself caught by the Blindfolded Woman.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Everyone stays quiet, that's the game, but of course everyone is also puzzled, not knowing Ichabod. The Woman touches Ichabod's face, which embarrasses Ichabod and displeases Brom.
  EXPRESSION: Embarrassed
- CHARACTER: Child
  LINE: A kiss, a kiss!
  EXPRESSION: Excited
- CHARACTER: Woman
  LINE: She has to guess first.
  EXPRESSION: Playful
- CHARACTER: Narrator
  LINE: The WOMAN is wifely, and as she puts her arm through Doctor Lancaster's arm, we realize she is his wife.
  EXPRESSION: null
- CHARACTER: Blindfolded Woman
  LINE: Is it Theodore?
  EXPRESSION: Questioning
- CHARACTER: Narrator
  LINE: There's a general laugh at that.
  EXPRESSION: Amused
- CHARACTER: Ichabod
  LINE: Pardon, ma'am. I am only a stranger.
  EXPRESSION: Apologetic
- CHARACTER: Blindfolded Woman
  LINE: Then have a kiss on account.
  EXPRESSION: Playful
- CHARACTER: Narrator
  LINE: She kisses him laughingly and takes the blindfold off the reveal a stunning beauty: KATRINA VAN TASSEL. She smiles. Ichabod tries to compose himself, stricken by the sight of her.
  EXPRESSION: Smitten
- CHARACTER: Ichabod
  LINE: I... um, I am looking for Baltus Van Tassel.
  EXPRESSION: Flustered
- CHARACTER: Katrina
  LINE: I am his daughter, Katrina Van Tassel.
  EXPRESSION: Confident
- CHARACTER: Brom
  LINE: And who are you, friend? We have not heard your name yet.
  EXPRESSION: Suspicious
- CHARACTER: Ichabod
  LINE: I have not said it. Excuse me...
  EXPRESSION: Evasive
- CHARACTER: Narrator
  LINE: Brom grabs Ichabod's collar. Ichabod's baffled.
  EXPRESSION: Baffled
- CHARACTER: Brom
  LINE: You need some manners.
  EXPRESSION: Aggressive
- CHARACTER: Katrina
  LINE: Brom!
  EXPRESSION: Concerned
- CHARACTER: Man's Voice (O.S.)
  LINE: (admonishing) Come, come -- we want no raised voices...
  EXPRESSION: Admonishing
- CHARACTER: Narrator
  LINE: We now SEE that the voice belongs to BALTUS VAN TASSEL, a working-class self-made Mr. Big with a sympathetic smile.
  EXPRESSION: null
- CHARACTER: Baltus
  LINE: It is only to raise the spirits during this dark time that I and my good wife are giving this little party...
  EXPRESSION: Welcoming
- CHARACTER: Narrator
  LINE: LADY VAN TASSEL stands behind him, a mix of homespun wife and well-kept lady. Brom releases Ichabod. Children hide behind Katrina.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Ichabod's relieved to have a proper focal point. Others from the party gather.
  EXPRESSION: Relieved
- CHARACTER: Baltus
  LINE: Young sir, you are welcome even if you are selling something!
  EXPRESSION: Joking
- CHARACTER: Narrator
  LINE: The pleasantry relaxes the atmosphere around Ichabod.
  EXPRESSION: Relaxed
- CHARACTER: Ichabod
  LINE: Thank you, sir. I am Constable Ichabod Crane, sent to you from New York with authority to investigate murder in Sleepy Hollow.
  EXPRESSION: Official
- CHARACTER: Narrator
  LINE: This has quite an effect. A man we will know as MAGISTRATE PHILIPSE looks up sharply. A man we will know as REVEREND STEENWYCK grunts skeptically. A man we have already seen, DOCTOR LANCASTER, exchanges a surprised look with another man, NOTARY HARDENBROOK.
  EXPRESSION: null
- CHARACTER: Reverend Steenwyck
  LINE: Well, what use is a Constable?!
  EXPRESSION: Rude
- CHARACTER: Narrator
  LINE: Lady Van Tassel gives the Clergyman a reproachful look.
  EXPRESSION: null
- CHARACTER: Lady Van Tassel
  LINE: Then, Sleepy Hollow is grateful to you, Constable Crane -- I hope you will honor this house by remaining with us until...
  EXPRESSION: Grateful
- CHARACTER: Brom
  LINE: Until you've made the arrest!
  EXPRESSION: Joking
- CHARACTER: Narrator
  LINE: To Ichabod's surprise this gets a nervous laugh. Baltus frowns at Brom.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Katrina looks at Ichabod with renewed interest.
  EXPRESSION: Interested
- CHARACTER: Baltus
  LINE: Well spoke! Come, sir. We'll get you settled. Play on!
  EXPRESSION: Welcoming
- CHARACTER: Narrator
  LINE: Baltus catches the eyes of Philipse, then of Lancaster, nodding as if to say "See you in a minute."
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: As he leads Ichabod out, he murmurs to Steenwyck, who nods and passes
  EXPRESSION: null

::PATHS::
- CHOICE: "Accept the invitation to stay"
  TARGET: van_tassel_guest_room
  STATE_CHANGE: suspicion = +1, Katrina_interest = +1
  CONDITION: null

::SCENE::
LOCATION: Hardenbrook
MOOD: Festive
CHARACTERS: Narrator
BACKGROUND_IMAGE: hardenbrook.png
BACKGROUND_EDIT: "Festive gathering, music playing"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The murmur to Hardenbrook.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The Fiddlers strike up the music. Katrina watches Ichabod's exit. Brom watches Katrina's interest with displeasure.
  EXPRESSION: null

::PATHS::
- CHOICE: "Go to Ichabod's room"
  TARGET: ichabods_room
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Van Tassel House, Ichabod's Room
MOOD: Quiet Study
CHARACTERS: Narrator, Ichabod, Sarah
BACKGROUND_IMAGE: ichabods_room.png
BACKGROUND_EDIT: "Ichabod's room, books and medical instruments laid out"

::SCRIPT::
- CHARACTER: Narrator
  LINE: We hear the music from downstairs. Ichabod is unpacking -- arranging his scientific books. His "medical case," revealing a few mysterious Instruments of Detections, is open on the bed. Sarah is just delivering a pitcher of water to the washstand.
  EXPRESSION: null
- CHARACTER: Ichabod
  LINE: Thank you. Please tell Mr. Van Tassel I will be down in a moment.
  EXPRESSION: Polite
- CHARACTER: Sarah
  LINE: I will, sir.
  EXPRESSION: Obedient
- CHARACTER: Sarah
  LINE: Thank God you are here!
  EXPRESSION: Emotional
- CHARACTER: Narrator
  LINE: Ichabod is a bit surprised by her emotion. Then he pours the water and douses his face.
  EXPRESSION: null

::PATHS::
- CHOICE: "Go to the parlor"
  TARGET: parlor
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Van Tassel House, Parlor
MOOD: Tense Waiting
CHARACTERS: Narrator, Ichabod, Sarah, Baltus, Lady Van Tassel, Lancaster, Philipse, Reverend Steenwyck, Hardenbrook
BACKGROUND_IMAGE: parlor.png
BACKGROUND_EDIT: "Parlor with men waiting, faint party music audible"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Five men wait grimly for Ichabod, silent in the presence of Sarah, who is placing a pipe cradle by Baltus. Lady Van Tassel is pouring the men a drink. The music from the party is faintly audible. Lancaster is 50, dour, always sweaty. Philipse is youngest, a drinker, eyes bloodshot, augmenting his glass with a shot from his private flask. Reverend Steenwyck has a disdainful, sour expression. Hardenbrook is oldest, ancient, nervous, one eye pale and blind.
  EXPRESSION: null
- CHARACTER: Hardenbrook
  LINE: All the way from New York!
  EXPRESSION: Skeptical
- CHARACTER: Doctor Lancaster
  LINE: A waste of time!
  EXPRESSION: Dismissive
- CHARACTER: Steenwyck
  LINE: What can he do?
  EXPRESSION: Disdainful
- CHARACTER: Baltus
  LINE: Gentlemen, gentlemen...
  EXPRESSION: Calming
- CHARACTER: Narrator
  LINE: Sarah, leaving, passes Doctor Lancaster, who secretly trails his hand against Sarah's buttock... not quite secretly enough for the vigilance of Lady Van Tassel, who, by the merest flick of an eye, shows us that she has noticed.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Sarah leaves just as Ichabod appears in the doorway, Sarah closing the door behind him.
  EXPRESSION: null
- CHARACTER: Baltus
  LINE: Excellent! Come in! Leave us, my dear.
  EXPRESSION: Welcoming
- CHARACTER: Ichabod
  LINE: So. Three persons murdered. First, Peter Van Garrett and his son Dirk Van Garrett, both of them strong capable men, found together, decapitated. A week later, the Widow Winship, also decapitated. I will need to ask you many questions, but first let me ask -- is anyone suspected?
  EXPRESSION: Inquisitive
- CHARACTER: Baltus
  LINE: I don't understand you.
  EXPRESSION: Confused
- CHARACTER: Ichabod
  LINE: I say, is there any one person suspect in these acts?
  EXPRESSION: Persistent
- CHARACTER: Narrator
  LINE: The men stir in their seats -- their looks say "I told you so!" -- "Useless!" -- etc.
  EXPRESSION: null
- CHARACTER: Baltus
  LINE: Constable... how much have your superiors explained to you?
  EXPRESSION: Patronizing
- CHARACTER: Ichabod
  LINE: Only that the three were slain in open ground and their heads found severed from their bodies...
  EXPRESSION: Factual
- CHARACTER: Steenwyck
  LINE: The heads were not found severed. The heads were not found at all.
  EXPRESSION: Firm
- CHARACTER: Ichabod
  LINE: The heads are gone?
  EXPRESSION: Surprised
- CHARACTER: Narrator
  LINE: Hardenbrook leans forward, his voice cragged.
  EXPRESSION: null
- CHARACTER: Hardenbrook
  LINE: Taken. Taken by the Headless Horseman. Taken back to hell.
  EXPRESSION: Grave
- CHARACTER: Ichabod
  LINE: Pardon me, I... ?
  EXPRESSION: Confused
- CHARACTER: Baltus
  LINE: Perhaps you had better sit down.
  EXPRESSION: Reassuring
- CHARACTER: Narrator
  LINE: Baltus gestures for Ichabod to sit. Baltus lights his pipe and pours a glass for Ichabod. The men help themselves to food and drink.
  EXPRESSION: null
- CHARACTER: Baltus
  LINE: The Horseman was a Hessian mercenary, sent to our shores by German princes to keep Americans under the yoke of England. But unlike his compatriots who came for money, the Horseman came... for love of carnage... and he was not like the others...
  EXPRESSION: Storytelling

::PATHS::
- CHOICE: "Listen to the story"
  TARGET: flashback_battlefield
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: American Battlefield (Winter)
MOOD: Violent Chaos
CHARACTERS: Narrator, Hessian Horseman, Baltus (V.O.)
BACKGROUND_IMAGE: american_battlefield.png
BACKGROUND_EDIT: "Winter battlefield, close-quarters combat"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The Hessian Horseman rides his black steed into a gory, close-quarters clash, his cloaked uniform adorned with edged weapons. He cuts down Americans left and right.
  EXPRESSION: null
- CHARACTER: Baltus (V.O.)
  LINE: He rode a giant black steed named Daredevil. He was infamous for taking his horse hard into battle... chopping off heads at full gallop.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The Horseman dismounts, hoists a battle axe. With sword and axe, he annihilates. Blood gushes. Bones crack.
  EXPRESSION: null
- CHARACTER: Baltus (V.O.)
  LINE: To look upon him made your blood run cold, for he had filed down his teeth to sharp points... to add to the ferocity of his appearance...
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The Horseman lets out a war cry. Jagged teeth. Grotesque.
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue flashback"
  TARGET: flashback_forest_battle
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Forest Battlefield (Winter)
MOOD: Retreat and Pursuit
CHARACTERS: Narrator, Hessian Horseman, Baltus (V.O.)
BACKGROUND_IMAGE: forest_battlefield.png
BACKGROUND_EDIT: "Winter forest, cannons in distance, pursuit"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Winter. Cannons can be heard booming from afar. Daredevil, galloping is hit and falls. The Horseman is not hurt.
  EXPRESSION: null
- CHARACTER: Baltus (V.O.)
  LINE: This butcher would not finally meet his end till the winter of seventy-nine...
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The Horseman rises, eyes filled with rage, looks to see... Six ragtag Revolutionary Soldiers give chase, firing rifles. The Horseman flees, bullets throwing snow behind.
  EXPRESSION: null
- CHARACTER: Baltus
  LINE: ...not far from here in our Western Woods...
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue flashback"
  TARGET: flashback_deeper_forest
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Deeper in the Forest Battlefield (Winter)
MOOD: Tense Encounter
CHARACTERS: Narrator, Hessian Horseman, Two Young Girls, Soldiers
BACKGROUND_IMAGE: deeper_forest_battlefield.png
BACKGROUND_EDIT: "Deeper forest, soldiers surrounding Horseman"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The Horseman glances back, bounding through, drawing his sword, when suddenly he halts... He's happened upon two young girls gathering firewood. The girls stand frozen at the sight of him for a long, silent moment, till one girl drops the firewood and runs.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The second girl remains, holding the Horseman's gaze. The Horseman and the girl hold each other's gaze for a long beat. The Horseman puts his finger to his lips, warning her to stay quiet.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The girl takes one of her pieces of dry wood and deliberately breaks it, making a noise like a pistol shot. There is a responding shout from a soldier back in the trees. The Horseman turns to the sound.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Soldiers move forward from the forest behind, spreading out. The second girl flees. The Horseman hefts his sword, turning as soldiers surround. One soldier aims his rifle...
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The Horseman reaches over his shoulder, grasps a sheathed knife and throws -- THOCK! The rifleman jerks back, knife in his eye socket.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: A second soldier aims and fires... Blood explodes from the Horseman's arm. His sword drops. The Horseman readies and axe in his good hand. The Revolutionaries move in with swords. They battle, steel against steel. The Horseman fends off blows...
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Soldier Three stabs his blade deep into the Horseman's side. The Horseman roars, bringing his axe down... Breaks the sword at the hilt. An upward stroke sends Soldier Three backward in a fountain of blood.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The Horseman staggers, trying to pull the blade from his ribs. The remaining soldiers close in...
  EXPRESSION: null

::PATHS::
- CHOICE: "Return to the parlor"
  TARGET: parlor_after_flashback
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Van Tassel House, Parlor
MOOD: Grim Revelation
CHARACTERS: Narrator, Ichabod, Baltus, Hardenbrook, Doctor Lancaster, Steenwyck
BACKGROUND_IMAGE: parlor_after_flashback.png
BACKGROUND_EDIT: "Parlor, Ichabod visibly spooked, Baltus smoking pipe"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Ichabod is spooked. Pipe smoke wafts from Baltus's mouth.
  EXPRESSION: null
- CHARACTER: Baltus
  LINE: They cut off his head with his own sword. To this day, the Western Woods is a haunted place where brave men will not venture.
  EXPRESSION: Grim
- CHARACTER: Narrator
  LINE: The Horseman's headless corpse lies in a shallow grave.
  EXPRESSION: null
- CHARACTER: Baltus (V.O.)
  LINE: ...for what was planted in the ground that day was a seed of evil.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The Horseman's head is dropped into the grave.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: One of the four surviving soldiers stabs the Horseman's sword deep in the ground as a marker. The grave is done. The soldiers walk away from the grave. They have buried the Horseman in a treeless clearing.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Daredevil appears, limping, from the trees, and puts his nose down to the turned earth. The Second Girl is watching from hiding. She sees: Daredevil collapses on the grave, blood frothing from his mouth. Dying.
  EXPRESSION: null
- CHARACTER: Baltus
  LINE: And so it has been for twenty years. But now the Hessian wakes -- he is on the rampage, cutting off heads where he finds them.
  EXPRESSION: Foreboding
- CHARACTER: Narrator
  LINE: Ichabod sits back, shakes off the reverie of the tale. He takes a gulp from his glass.
  EXPRESSION: null
- CHARACTER: Ichabod
  LINE: Are you... saying... ? Is that what you believe?
  EXPRESSION: Skeptical
- CHARACTER: Hardenbrook
  LINE: Seeing is believing!
  EXPRESSION: Insistent
- CHARACTER: Baltus
  LINE: No one knows why the Hessian has chosen this time to return from the grave.
  EXPRESSION: Puzzled
- CHARACTER: Steenwyck
  LINE: Satan has called forth one of his own.
  EXPRESSION: Zealous
- CHARACTER: Narrator
  LINE: Steenwyck stands and from a side table picks up the hefty Baltus family Bible.
  EXPRESSION: null
- CHARACTER: Steenwyck
  LINE: They tell me you have brought books and trappings of scientific investigation -- this is the only book I recommend you study.
  EXPRESSION: Condescending
- CHARACTER: Narrator
  LINE: He drops the Bible on the table in front of Ichabod, making him jump.
  EXPRESSION: null

::PATHS::
- CHOICE: "Examine the Bible"
  TARGET: examine_bible
  STATE_CHANGE: fear = +1
  CONDITION: null

::SCENE::
LOCATION: Van Tassel House, Study/Parlor
MOOD: Skeptical Inquiry
CHARACTERS: Narrator, Ichabod, Reverend Steenwyck, Hardenbrook, Baltus
BACKGROUND_IMAGE: van_tassel_house_study.png
BACKGROUND_EDIT: "Interior of a dimly lit room, books and papers scattered around."

::SCRIPT::
- CHARACTER: Narrator
  LINE: y lifts the front cover -- revealing a page of ink writing, which he will remember later -- then he snaps out of all this "nonsense."
  EXPRESSION: null
- CHARACTER: Ichabod
  LINE: Reverend Steenwyck... gentlemen... murder needs no ghost come from the grave. Which of you have laid eyes on this Headless Horsemen?
  EXPRESSION: Inquisitive
- CHARACTER: Narrator
  LINE: Pause.
  EXPRESSION: null
- CHARACTER: Hardenbrook
  LINE: Others have. Many others.
  EXPRESSION: Grave
- CHARACTER: Narrator
  LINE: Ichabod allows himself a skeptical smile.
  EXPRESSION: Skeptical
- CHARACTER: Baltus
  LINE: You will see him too if he comes again. The men of the village are posted to watch for him.
  EXPRESSION: Firm
- CHARACTER: Ichabod
  LINE: We have murders in New York without benefit of ghouls and goblins.
  EXPRESSION: Dismissive
- CHARACTER: Baltus
  LINE: You are a long way from New York, sir.
  EXPRESSION: Warning
- CHARACTER: Ichabod
  LINE: A century at least. The assassin is a man of flesh and blood, and I will discover him.
  EXPRESSION: Determined
- CHARACTER: Steenwyck
  LINE: How do you propose to do so?
  EXPRESSION: Questioning
- CHARACTER: Ichabod
  LINE: By discovering his reason. It is what we call "the motive." This mystery will not resist investigation by a Rational Man.
  EXPRESSION: Confident
- CHARACTER: Narrator
  LINE: Ichabod's natural clumsiness, however, causes him to sweep his empty glass off the table, rather ruining the effect of the Rational Man in command of the situation.
  EXPRESSION: Clumsy

::SCENE::
LOCATION: Van Tassel House, Katrina's Room
MOOD: Feminine Chitchat, Anticipation
CHARACTERS: Narrator, Katrina, Lady Van Tassel, Sarah
BACKGROUND_IMAGE: katrinas_room.png
BACKGROUND_EDIT: "A well-appointed bedroom, with a vanity and dressing table."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Katrina is sitting in front of her mirror. Lady Van Tassel is brushing out Katrina's hair, counting the strokes.
  EXPRESSION: null
- CHARACTER: Katrina
  LINE: Well, I'm disappointed... our first visitor from New York... He doesn't know where to put himself and his feet are all over the place.
  EXPRESSION: Disappointed
- CHARACTER: Narrator
  LINE: There is a knock.
  EXPRESSION: null
- CHARACTER: Lady Van Tassel
  LINE: Yes, not like your Brom. Go on brushing, I got to forty-two...
  EXPRESSION: Gossipy
- CHARACTER: Narrator
  LINE: She opens the door to Sarah.
  EXPRESSION: null
- CHARACTER: Sarah
  LINE: That constable, he wants the Bible, Mum...
  EXPRESSION: Dutiful
- CHARACTER: Lady Van Tassel
  LINE: Bible...?
  EXPRESSION: Surprised
- CHARACTER: Katrina
  LINE: I'll bring it to him.
  EXPRESSION: Helpful
- CHARACTER: Narrator
  LINE: Sarah dips a curtsy and goes. Lady Van Tassel gives Katrina a friendly raised eyebrow.
  EXPRESSION: null
- CHARACTER: Katrina
  LINE: We'll see if his city talk fits him better than his clothes.
  EXPRESSION: Teasing

::SCENE::
LOCATION: Van Tassel House, Ichabod's Room
MOOD: Frustration, Expectation
CHARACTERS: Narrator, Ichabod, Katrina
BACKGROUND_IMAGE: ichabods_room.png
BACKGROUND_EDIT: "A simple room cluttered with books and papers, a Bible on a stand."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Ichabod sits surrounded by his books, including his Ledger. Clearly there has been no breakthrough. Ichabod broods. There is a knock at the door, which he seems to have been expecting, for he does not turn around.
  EXPRESSION: Brooding
- CHARACTER: Ichabod
  LINE: Yes -- yes -- come in.
  EXPRESSION: Preoccupied
- CHARACTER: Narrator
  LINE: Katrina enters carrying the Bible.
  EXPRESSION: null
- CHARACTER: Ichabod
  LINE: Thank you, just leave it on the reading stand.
  EXPRESSION: Distracted
- CHARACTER: Narrator
  LINE: Katrina puts down the Bible as directed.
  EXPRESSION: null
- CHARACTER: Ichabod
  LINE: That will be all -- no, tell me, about that big brute who seems to be Miss Katrina's -- He has turned in his chair, too late, and sees Katrina -- Ichabod has a minor convulsion, standing up, knocking papers to the floor, etc.
  EXPRESSION: Startled
- CHARACTER: Ichabod
  LINE: Forgive me, I... I asked Sarah to bring me...
  EXPRESSION: Flustered
- CHARACTER: Katrina
  LINE: So your clever books have failed you and you turn to the Bible after all!
  EXPRESSION: Amused
- CHARACTER: Ichabod
  LINE: I see I am talked about downstairs.
  EXPRESSION: Sharp
- CHARACTER: Katrina
  LINE: In passing only -- we have many things to talk about even in this backward place.
  EXPRESSION: Relaxed
- CHARACTER: Ichabod
  LINE: I am sorry... Please excuse my manner -- I am not used to...
  EXPRESSION: Apologetic
- CHARACTER: Katrina
  LINE: Female company?
  EXPRESSION: Playful
- CHARACTER: Ichabod
  LINE: Society.
  EXPRESSION: Formal
- CHARACTER: Katrina
  LINE: How can you avoid society in New York? How I should love the opera -- and theaters -- to go dancing... Is it wonderful?
  EXPRESSION: Yearning
- CHARACTER: Ichabod
  LINE: I have never been.
  EXPRESSION: Bashful
- CHARACTER: Katrina
  LINE: But there is an art museum? -- a concert hall?
  EXPRESSION: Eager
- CHARACTER: Ichabod
  LINE: I don't know.
  EXPRESSION: Uninformed
- CHARACTER: Katrina
  LINE: Then you have nothing to teach me.
  EXPRESSION: Disappointed
- CHARACTER: Ichabod
  LINE: Perhaps I have. Do you believe the Van Garretts and the Widow Winship were murdered by a headless horseman?
  EXPRESSION: Hopeful
- CHARACTER: Katrina
  LINE: Not everyone here believes it is the Horseman.
  EXPRESSION: Neutral
- CHARACTER: Ichabod
  LINE: Good.
  EXPRESSION: Relieved
- CHARACTER: Katrina
  LINE: Some say it is the witch of the Western Woods who has made a pact with Lucifer.
  EXPRESSION: Mysterious
- CHARACTER: Ichabod
  LINE: There are no witches, or galloping ghosts either! Is everyone in this village in thrall to superstition?
  EXPRESSION: Exasperated
- CHARACTER: Katrina
  LINE: Why are you so frightened of magic? Not all magic is black. There are ancient truths in these woods which have been forgotten in your city parks.
  EXPRESSION: Enchanted
- CHARACTER: Ichabod
  LINE: If they are truths they are not magic -- and if magic, not truth.
  EXPRESSION: Logical
- CHARACTER: Katrina
  LINE: You are foolish. When there is fever in the house, it is well known that willow-herb roots and a crow's foot must be boiled in the milk of a pure white goat with special charms uttered over the fire... and the fever abates.
  EXPRESSION: Knowledgable
- CHARACTER: Ichabod
  LINE: Next time try the herb without the rest -- and now I must ask you -- excuse me --
  EXPRESSION: Impatient
- CHARACTER: Katrina
  LINE: Gladly. I should not have interrupted our town's savior. Good night. And as to your first question, that big brute you were asking about has proposed to me.
  EXPRESSION: Sarcastic
- CHARACTER: Ichabod
  LINE: I... I... I'm happy that...
  EXPRESSION: Stuttering
- CHARACTER: Katrina
  LINE: Proposed to me several times.
  EXPRESSION: Ambiguous
- CHARACTER: Narrator
  LINE: This ambiguous statement, accompanied by a faint smile, confuses Ichabod into silence as she closes the door behind her. He turns with relief to the next business -- the Bible. He opens the front cover. On the endpaper is a Family Tree going back a hundred years, in variously faded inks and handwritings. Ichabod studies it and we see what he learns: that Katrina was born in 1777... to Baltus's first wife, who died in 1797... that Lady Van Tassel is Baltus's second wife (her maiden name is unimportant, because false)... Then he suddenly notices something even more interesting: The family tree has a "Van Garrett" in it -- the husband of Baltus's father's sister.
  EXPRESSION: null
- CHARACTER: Ichabod
  LINE: Van Garrett... !
  EXPRESSION: Muttering
- CHARACTER: Narrator
  LINE: Ichabod looks thoughtful. He starts copying out details into his Ledger. A very faint rumbling disturbs him for a moment. He looks up. Silence now. He continues working.
  EXPRESSION: null

::SCENE::
LOCATION: Sleepy Hollow - Street
MOOD: Ominous Calm
CHARACTERS: Narrator
BACKGROUND_IMAGE: sleepy_hollow_street.png
BACKGROUND_EDIT: "An empty, dark street in Sleepy Hollow."

::SCRIPT::
- CHARACTER: Narrator
  LINE: The empty street. Then the low sinister sound of rumbling is heard again.
  EXPRESSION: null

::SCENE::
LOCATION: Wooden Bunker/Field
MOOD: Fear, Approaching Danger
CHARACTERS: Narrator, Jonathan
BACKGROUND_IMAGE: wooden_bunker_field.png
BACKGROUND_EDIT: "A wooden structure in a field, bordering a dark forest."

::SCRIPT::
- CHARACTER: Narrator
  LINE: The distant SOUND of the GROUND RUMBLING is HEARD. AT THE WOODEN BUNKER, Jonathan looks out, fearful...
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The torches burn bright along the forest line. SEVERAL DEER stampede out... sprinting across the field.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Jonathan watches the forest. A horrible, SILENT stillness has fallen.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Then, Jonathan's eyes widen... A thick FOG creeps from the woods. As fog overtakes each torch, mist snakes up, snuffing each flame... one by one by one, all along the forest edge...
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Jonathan sticks his rifle out from the bunker, sights the gun along the treeline.
  EXPRESSION: null
- CHARACTER: Jonathan
  LINE: Come out, devil... come...
  EXPRESSION: Defiant

::SCENE::
LOCATION: Sleepy Hollow Forests - Overview
MOOD: Unsettling Quiet, Imminent Threat
CHARACTERS: Narrator
BACKGROUND_IMAGE: sleepy_hollow_forest_overview.png
BACKGROUND_EDIT: "Silhouetted treetops against a dark night sky."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Silhouetted treetops. The SOUNDS of JONATHAN'S RIFLE FIRING are HEARD, echoing -- SEVERAL GUNSHOTS, then... SILENCE...
  EXPRESSION: null

::SCENE::
LOCATION: Sleepy Hollow Forest
MOOD: Terror, Pursuit
CHARACTERS: Narrator, Jonathan, Huge Form on Huge Black Horse
BACKGROUND_IMAGE: sleepy_hollow_forest_chase.png
BACKGROUND_EDIT: "Dark, dense forest with thorny bushes."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Jonathan flees through the forest, glances back, terrified. THUNDEROUS HOOFBEATS are HEARD from behind. DEEP IN THE FOREST, we GLIMPSE the source of the HOOFBEATS: a HUGE FORM on a HUGE BLACK HORSE, already gone.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Jonathan pushes through thorny bushes. Jagged branches bloody his hands and cheeks... He bursts from the brier patch and TUMBLES to a TRAIL.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: IN THE FOREST BEHIND: The hooves of the black horse rip underbrush. HOOFBEATS DEAFENING. A spur digs into the snorting steed's already bleeding flank. The pursuer's gloved hand draws a SWORD, blade RINGING.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: ON THE TRAIL, Jonathan runs onward. The shrill WHISTLE of a SWORD SWING is HEARD as the pursuer BLURS PAST... Jonathan is still running when his head lolls back, at an impossible angle... his head tumbles off his shoulders... Jonathan's headless body hits the dirt.
  EXPRESSION: null

::SCENE::
LOCATION: Sleepy Hollow - Day - Early Morning
MOOD: Deceptive Calm
CHARACTERS: Narrator, Woman, People
BACKGROUND_IMAGE: sleepy_hollow_morning.png
BACKGROUND_EDIT: "A street in Sleepy Hollow in the early morning light."

::SCRIPT::
- CHARACTER: Narrator
  LINE: People going about their business calmly. A WOMAN shakes out a blanket from an upper window. The murder has obviously not been discovered yet. No one notices that the WOODEN BUNKER is deserted... and now has a gap of shattered timber.
  EXPRESSION: null

::SCENE::
LOCATION: Livery Stable - Day - Early Morning
MOOD: Rustic Commerce
CHARACTERS: Narrator, Killian, Ichabod
BACKGROUND_IMAGE: livery_stable.png
BACKGROUND_EDIT: "A rustic livery stable, horses and tack visible."

::SCRIPT::
- CHARACTER: Narrator
  LINE: The stables belong to KILLIAN, a dashingly rustic man, father of a young family. Ichabod likes him... though he does not think much of the Horse Killian is offering him, an old nag. Ichabod has a big satchel.
  EXPRESSION: null
- CHARACTER: Killian
  LINE: His name's Gunpowder.
  EXPRESSION: Proud
- CHARACTER: Narrator
  LINE: ICH
  EXPRESSION: null

::SCENE::
LOCATION: Killian's Stable
MOOD: Business Transaction
CHARACTERS: Ichabod, Killian
BACKGROUND_IMAGE: killian_stable.png
BACKGROUND_EDIT: "Daytime, interior of a stable, horses present"

::SCRIPT::
- CHARACTER: Narrator
  LINE: ABOD
  EXPRESSION: null
- CHARACTER: Ichabod
  LINE: A brave name, but... have you got something a little younger?... Taller?
  EXPRESSION: null
- CHARACTER: Killian
  LINE: (apparently getting it) Faster.
  EXPRESSION: Understanding
- CHARACTER: Ichabod
  LINE: Yes.
  EXPRESSION: null
- CHARACTER: Killian
  LINE: A horse cut to dash.
  EXPRESSION: null
- CHARACTER: Ichabod
  LINE: Yes.
  EXPRESSION: null
- CHARACTER: Killian
  LINE: No, I haven't.
  EXPRESSION: null
- CHARACTER: Ichabod
  LINE: Oh.
  EXPRESSION:null
- CHARACTER: Killian
  LINE: Not at the price.
  EXPRESSION: null
- CHARACTER: Ichabod
  LINE: Well... I'm sure he'll do very well. Thank you, Mr. Killian.
  EXPRESSION: Polite
- CHARACTER: Killian
  LINE: Good luck, sir. If you need help, call my name.
  EXPRESSION: Helpful
- CHARACTER: Ichabod
  LINE: Much appreciated.
  EXPRESSION: Grateful

::PATHS::
- CHOICE: "Leave the stable"
  TARGET: killian_house_exterior
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Killian House Exterior
MOOD: Domesticity and Aid
CHARACTERS: Narrator, Killian, Thomas, Mrs. Killian (Beth), Pregnant Woman
BACKGROUND_IMAGE: killian_house_exterior.png
BACKGROUND_EDIT: "Daytime, exterior of Killian House, a notice on the door"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Killian's son Thomas, a small boy, is feeding one of the horses.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: ANGLE ON Mrs. KILLIAN at the door of the Killian House. She is in the act of seeing a woman out of her door, a PREGNANT WOMAN, and handing her a bunch of herbs.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: CLOSER
  EXPRESSION: null
- CHARACTER: Beth
  LINE: (to Pregnant Woman) Mind you rub them well in the breech, Mrs. Sherry -- don't worry, it'll be easy as shelling peas.
  EXPRESSION: Reassuring
- CHARACTER: Narrator
  LINE: As the Pregnant Woman leaves, Beth bawls over her shoulder, turning to go into the house.
  EXPRESSION: null
- CHARACTER: Beth
  LINE: Thomas! -- It's you I want!
  EXPRESSION: Imperative
- CHARACTER: Narrator
  LINE: Beth goes into the house, passing a modest notice on the door: "Knock before entering -- Elizabeth Killian, MIDWIFE"
  EXPRESSION: null
- CHARACTER: Killian
  LINE: (to Thomas) Go off home for your breakfast, Tom -- kiss your mother once for you and twice for me.
  EXPRESSION: Affectionate
- CHARACTER: Narrator
  LINE: As the boy goes, Ichabod has a thought.
  EXPRESSION: null
- CHARACTER: Ichabod
  LINE: Mr. Killian, I was thinking... about the old widow...
  EXPRESSION: Thoughtful
- CHARACTER: Killian
  LINE: Old Widow?
  EXPRESSION: Questioning
- CHARACTER: Ichabod
  LINE: Widow Winship.
  EXPRESSION: null
- CHARACTER: Killian
  LINE: Who told you she was old? She was comely. Widowed young and dead before the bloom was off her.
  EXPRESSION: Informative
- CHARACTER: Narrator
  LINE: Ichabod is surprised. Before he can react further, a distant gunshot is heard -- a signal followed by the distant sight of a man on horseback, hurrying and shouting, waving his rifle. It's clear that Masbath's murder has been discovered. Killian and Ichabod watch the Rider coming, telling the news as he comes.
  EXPRESSION: null
- CHARACTER: Rider
  LINE: (shouting) Murder, murder! The Horseman has killed again!
  EXPRESSION: Panicked

::PATHS::
- CHOICE: "Witness the approaching rider"
  TARGET: farmland_murder_site
  STATE_CHANGE: alarm = +1
  CONDITION: null

::SCENE::
LOCATION: Sleepy Hollow Farmland
MOOD: Urgency and Alarm
CHARACTERS: Narrator, Riders, Baltus, Van Ripper, Brom, Philipse, Doctor Lancaster, Ichabod
BACKGROUND_IMAGE: farmland_murder_site.png
BACKGROUND_EDIT: "Daytime, open fields, multiple riders galloping"

::SCRIPT::
- CHARACTER: Narrator
  LINE: EXT. SLEEPY HOLLOW FARMLAND - DAY
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Riders are galloping across the fields toward the murder site.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Baltus, a Dullardly Man called VAN RIPPER, who was the original Rider who found the body... followed by Brom, and a gig driven fast by Philipse, and Doctor Lancaster and various villagers. Way behind, trying to keep up on Gunpowder, comes Ichabod.
  EXPRESSION: null

::PATHS::
- CHOICE: "Follow the riders to the murder site"
  TARGET: forest_murder_site
  STATE_CHANGE: urgency = +1
  CONDITION: null

::SCENE::
LOCATION: Forest, Masbath Murder Site
MOOD: Grim Discovery and Suspicion
CHARACTERS: Narrator, Baltus, Glen, Doctor Lancaster, Masbath (corpse), Ichabod, Brom, Philipse
BACKGROUND_IMAGE: forest_murder_site.png
BACKGROUND_EDIT: "Morning, wooded area, a body discovered"

::SCRIPT::
- CHARACTER: Narrator
  LINE: EXT. FOREST, MASBATH MURDER SITE - MORNING
  EXPRESSION: null
- CHARACTER: Baltus
  LINE: Mr. Miller -- ride back for the coffin cart -- the rest of you keep a sharp lookout. No -- not at me, Glen, I'm not going to cut my own head off! -- Look out to the woods!
  EXPRESSION: Commanding
- CHARACTER: Narrator
  LINE: Ichabod hasn't quite arrived. The others are watching as Doctor Lancaster turns over the headless corpse of Masbath. He straightens the body reverently. Everyone is shocked and spooked, looking fearfully around. Behind them -- a sound. Everyone reacts but it's Ichabod arriving.
  EXPRESSION: null
- CHARACTER: Brom
  LINE: (laughs) A fine looking animal, Crane.
  EXPRESSION: Mocking
- CHARACTER: Narrator
  LINE: Ichabod dismounts, ignoring Brom. The great Detective is trying to cover up his jitters. New York was never like this.
  EXPRESSION: null
- CHARACTER: Doctor Lancaster
  LINE: The fourth victim, Jonathan Masbath.
  EXPRESSION: Grim
- CHARACTER: Ichabod
  LINE: And... the head...?
  EXPRESSION: Anxious
- CHARACTER: Philipse
  LINE: Taken.
  EXPRESSION: Flat
- CHARACTER: Ichabod
  LINE: Taken!
  EXPRESSION: Shocked
- CHARACTER: Narrator
  LINE: Doctor Lancaster seems unprofessionally jittery. He grasps Philipse by the arm. Philipse shakes him off and pulls out a flask. Ichabod notices this. Their behavior seems to him to be an odd moment. Then he turns his attention back to the matter at hand.
  EXPRESSION: null
- CHARACTER: Ichabod
  LINE: Interesting... very interesting.
  EXPRESSION: Pensive
- CHARACTER: Baltus
  LINE: What is?
  EXPRESSION: Puzzled
- CHARACTER: Ichabod
  LINE: In headless corpse cases of this sort... the head is removed to prevent identification of the body.
  EXPRESSION: Explanatory
- CHARACTER: Baltus
  LINE: But we know this is Jonathan Masbath...
  EXPRESSION: Confused
- CHARACTER: Ichabod
  LINE: Exactly! So, why was the head removed?
  EXPRESSION: Inquisitive
- CHARACTER: Narrator
  LINE: They all wait for enlightenment.
  EXPRESSION: null
- CHARACTER: Baltus
  LINE: Why?
  EXPRESSION: Impatient
- CHARACTER: Ichabod
  LINE: I don't know.
  EXPRESSION: Uncertain
- CHARACTER: Narrator
  LINE: They all watch Ichabod to see what he will do. Philipse takes nips from his flask. But Ichabod isn't sure. He isn't too keen on looking at the corpse. Then he realizes:
  EXPRESSION: null
- CHARACTER: Ichabod
  LINE: You have moved the body?
  EXPRESSION: Accusatory
- CHARACTER: Doctor Lancaster
  LINE: I did.
  EXPRESSION: Defensive
- CHARACTER: Ichabod
  LINE: (furious) You must never move the body!
  EXPRESSION: Outraged
- CHARACTER: Doctor Lancaster
  LINE: Why not?
  EXPRESSION: Bewildered
- CHARACTER: Ichabod
  LINE: Because!
  EXPRESSION: Frustrated
- CHARACTER: Narrator
  LINE: Despite themselves, they are impressed. Ichabod takes heart.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Ichabod finds a huge, deep HOOFPRINT. He kneels, pulls his satchel off his shoulder, takes out a BOWL, BOTTLE of WATER and a BAG of POWDER. The others watch, finding this bizarre, as Ichabod begins mixing the water and powder, making plaster.
  EXPRESSION: null
- CHARACTER: Brom
  LINE: What is that potion?
  EXPRESSION: Skeptical
- CHARACTER: Ichabod
  LINE: You are the blacksmith, Brom. Ever shoe a horse with a hoof this large?
  EXPRESSION: Challenging
- CHARACTER: Narrator
  LINE: Ichabod fills the print with runny plaster.
  EXPRESSION: null
- CHARACTER: Brom
  LINE: (grudging the point) It's big.
  EXPRESSION: Reluctant
- CHARACTER: Narrator
  LINE: Ichabod shoulders his satchel, walks all around, studies the ground, kicks away leaves... and then lopes around puzzlingly. The watchers are astonished by his antics as he leaps from hoofprint to hoofprint.
  EXPRESSION: null
- CHARACTER: Doctor Lancaster
  LINE: (to Philipse) The man's a fool.
  EXPRESSION: Dismissive
- CHARACTER: Philipse
  LINE: (drunk) He's a fool and we're damn fools -- but death will make us all equal.
  EXPRESSION: Cynical
- CHARACTER: Narrator
  LINE: Doctor Lancaster impatiently hushes him and turns away.
  EXPRESSION: null
- CHARACTER: Ichabod
  LINE: The stride is gigantic...
  EXPRESSION: Observant
- CHARACTER: Narrator
  LINE: Ichabod stops, turns, following back to way he came...
  EXPRESSION: null
- CHARACTER: Ichabod
  LINE: The attacker rode Masbath down... turned his horse... came back... Came back to claim the head.
  EXPRESSION: Deductive
- CHARACTER: Narrator
  LINE: He pauses to sum up.
  EXPRESSION: null
- CHARACTER: Ichabod
  LINE: To sum up. Head taken. Big horse. Did this man have any enemies?
  EXPRESSION: Analytical
- CHARACTER: Philipse
  LINE: Well, someone didn't like him.
  EXPRESSION: Noncommittal
- CHARACTER: Narrator
  LINE: But Ichabod has already latched on to something.
  EXPRESSION: null
- CHARACTER: Ichabod
  LINE: Van Ripper, show me where the neck rested.
  EXPRESSION: Authoritative
- CHARACTER: Narrator
  LINE: Van Ripper points. Ichabod opens his satchel, takes out a BOTTLE OF GREEN POWDER. He uncorks the bottle, sprinkles a thin layer of powder on the dirt, waiting. A reaction causes the powder to bubble a little.
  EXPRESSION: null
- CHARACTER: Ichabod
  LINE: A chemical reaction, it shows there was just a smear of blood, no more.
  EXPRESSION: Scientific
- CHARACTER: Van Ripper
  LINE: I didn't see none.
  EXPRESSION: Skeptical
- CHARACTER: Narrator
  LINE: Ichabod's puzzled.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Ichabod swallows, queasy, trying not to let it show.
  EXPRESSION: Nervous
- CHARACTER: Narrator
  LINE: Ichabod takes odd spectacles from his satchel, wire-framed with many lenses: MAGNIFICATION SPECTACLES. He fumbles putting them on, examines the gross neck wound.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Ichabod takes an INSTRUMENT from his satchel, a delicate SCISSOR MECHANISM TOOL that tapes off into tiny jaws. He uses it, hand shaking, to pick at the flesh.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: POV through Ichabod's magnifying spectacles: a CREEPY CRAWLY BUG is feeding on the wound. Ichabod freaks, leaps up.
  EXPRESSION: Horrified
- CHARACTER: Ichabod
  LINE: (recovering, faking) Interesting...
  EXPRESSION: Feigning Calm
- CHARACTER: Baltus
  LINE: What is it? -- What is it?!
  EXPRESSION: Eager
- CHARACTER: Narrator
  LINE: Squinting sidelong at the ground, Ichabod uses his foot to squash and grind the bug, which is too small to be visible.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: He looks at Baltus, his eyes huge in his spectacles.
  EXPRESSION: null
- CHARACTER: Ichabod
  LINE: The wound was cauterized in the very instant... as though the blade itself were red hot... and yet, no blistering, no scorched flesh.
  EXPRESSION: Puzzled and Worried
- CHARACTER: Narrator
  LINE: They all look worried.
  EXPRESSION: null
- CHARACTER: Philipse
  LINE: The Devil's fire!
  EXPRESSION: Fearful
- CHARACTER: Narrator
  LINE: Ichabod looks worried too.
  EXPRESSION: null

::PATHS::
- CHOICE: "Contemplate the implications of the wound"
  TARGET: cemetery_funeral
  STATE_CHANGE: fear = +2
  CONDITION: null

::SCENE::
LOCATION: Cemetery
MOOD: Solemnity and Unease
CHARACTERS: Narrator, Townspeople, Steenwyck, Ichabod, Baltus, Lady Van Tassel, Young Masbath, Brom, Katrina, Theodore, Glenn
BACKGROUND_IMAGE: cemetery_funeral.png
BACKGROUND_EDIT: "Daytime, a funeral service at an open grave"

::SCRIPT::
- CHARACTER: Narrator
  LINE: EXT. CEMETERY -- DAY
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The town is gathered for Jonathan Masbath's funeral. Steenwyck stands at the open grave, reads from the BIBLE.
  EXPRESSION: null
- CHARACTER: Steenwyck
  LINE: (reading) "Be sober, be vigilant... " as it sayeth in the book of Peter, chapter five, verse eight -- "because your adversary the devil, as a roaring lion, walketh about, seeking whom he may devour... "
  EXPRESSION: Reading
- CHARACTER: Narrator
  LINE: People WHISPER and steal glances at Ichabod. Ichabod stands with Baltus and Lady Van Tassel. Ichabod looks around, observing...
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Young Masbath stands with his head bowed. Brom stands beside Katrina, who wipes tears. Brom puts his arm around Katrina, comforting. Theodore and Glenn are nearby with rifles over their shoulders.
  EXPRESSION: null

::PATHS::
- CHOICE: "Observe the mourners and Ichabod's reactions"
  TARGET: cemetery_church_later
  STATE_CHANGE: somber = +1
  CONDITION: null

::SCENE::
LOCATION: Cemetery/Church
MOOD: Transition and Personal Resolve
CHARACTERS: Narrator, Ichabod, Van Tassels, Baltus, Katrina, Young Masbath
BACKGROUND_IMAGE: cemetery_church_later.png
BACKGROUND_EDIT: "Daytime, later, funeral procession leaving the cemetery"

::SCRIPT::
- CHARACTER: Narrator
  LINE: EXT. CEMETERY/CHURCH - (TIME CUT) - LATER - DAY
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The funeral is done. People head out from the cemetery.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Ichabod walks with the Van Tassels. Baltus holds Katrina's hand. Young Masbath runs to catch up with Ichabod.
  EXPRESSION: null
- CHARACTER: Young Masbath
  LINE: Mister Constable, sir...
  EXPRESSION: Respectful
- CHARACTER: Narrator
  LINE: Ichabod stops.
  EXPRESSION: null
- CHARACTER: Ichabod
  LINE: You are Young Masbath...
  EXPRESSION: Recognizing
- CHARACTER: Young Masbath
  LINE: I was Young Masbath, but now the only one. Masbath at your service, in honor bound to avenge my father.
  EXPRESSION: Determined
- CHARACTER: Ichabod
  LINE: Well, one-and-only Masbath, I thank you, but
  EXPRESSION: Grateful

::PATHS::
- CHOICE: "Respond to Young Masbath"
  TARGET: end
  STATE_CHANGE: resolve = +1
  CONDITION: null

::SCENE::
LOCATION: Doctor's Residence - Medical Room
MOOD: Somber
CHARACTERS: Narrator, Young Masbath, Ichabod, Philipse
BACKGROUND_IMAGE: doctor_residence_medical_room.png
BACKGROUND_EDIT: "Medical room with surgical instruments and a coffin"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Ichabod lifts the lid of a large feed bin half full of horse feed.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Young Masbath is curled up inside like a mouse in a nest. Homeless.
  EXPRESSION: null
- CHARACTER: Ichabod
  LINE: Find a place in the Van Tassel's servant quarters. Wake me before dawn. I hope you have a strong stomach.
  EXPRESSION: Disgruntled
- CHARACTER: Young Masbath
  LINE: Thank you, sir.
  EXPRESSION: Grateful

::PATHS::
- CHOICE: "Ichabod dismisses Young Masbath"
  TARGET: cemetery_night_dawn
  STATE_CHANGE: fear = +1
  CONDITION: null

::SCENE::
LOCATION: Cemetery
MOOD: Eerie
CHARACTERS: Narrator, Killian, Ichabod, Young Masbath, Two Men
BACKGROUND_IMAGE: cemetery_night_dawn.png
BACKGROUND_EDIT: "Nighttime cemetery, muddy graves, open coffins"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The lid of a muddy coffin is wrenched open. The coffin contains a headless corpse. Just the one.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: What's happening?
  EXPRESSION: Confused
- CHARACTER: Narrator
  LINE: The coffin is on the ground next to the hole marked by the headstone of Peter Van Garrett.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Killian holds a lantern and a spade. Ichabod, holding a handkerchief to his face, looks into the open coffin. He nods. Ichabod, in shirtsleeves and sweating, has a spade too. Young Masbath is watching uneasily. This is why Young Masbath would need a "strong stomach." He gags, almost pukes.
  EXPRESSION:null
- CHARACTER: Narrator
  LINE: At Ichabod's nod, Killian replaces the lid. Killian has Two Men with him. There are two more coffins and two more piles of dirt, one coffin for Dirk Van Garrett and one for Widow Winship.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Ichabod moves to the second coffin. It contains a headless corpse. Just the one. Ichabod nods, and the lid is replaced.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The third coffin -- the Widow's -- is being opened by one of the Men.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Ichabod takes a lantern and looks expectantly as the lid comes off. The Widow's headless corpse is alone in the coffin.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Ichabod pauses. Nods. As the lid is about to be replaced. He stops it.
  EXPRESSION: null
- CHARACTER: Ichabod
  LINE: Wait.
  EXPRESSION: Urgent
- CHARACTER: Narrator
  LINE: Ichabod takes out a small penknife and cuts through the shroud. He reveals the belly. He stares at it. Was she pregnant? It's impossible to tell. But there is the wound of a sword stab in the stomach.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Suddenly there is a screech, which seems to come from the corpse, giving heart attacks all around -- but now we see a "ghost" holding a lantern. It's Reverend Steenwyck who has discovered them and is shrieking in outrage.
  EXPRESSION: Shocked
- CHARACTER: Steenwyck
  LINE: Sacrilege! Sacrilege!
  EXPRESSION: Outraged
- CHARACTER: Ichabod
  LINE: Science... science, Reverend Steenwyck! Someone in Sleepy Hollow is using the Horseman story for his own murderous purpose, and I intend to... dig it out.
  EXPRESSION: Determined
- CHARACTER: Narrator
  LINE: Steenwyck froths, looks terrified and backs off.
  EXPRESSION: Terrified

::PATHS::
- CHOICE: "Ichabod confronts Steenwyck"
  TARGET: doctor_residence_medical_room_later
  STATE_CHANGE: investigation_progress = +2
  CONDITION: null

::SCENE::
LOCATION: Doctor's Residence - Medical Room
MOOD: Intense
CHARACTERS: Narrator, Ichabod, Killian, Young Masbath, Doctor Lancaster
BACKGROUND_IMAGE: doctor_residence_medical_room_later.png
BACKGROUND_EDIT: "Medical room, coffin now inside, doctor looks horrified"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Ichabod and Killian, helped by Young Masbath, carry the Widow's muddy coffin inside. Doctor Lancaster watches in horror, sweating profusely, freaked out.
  EXPRESSION: Horrified
- CHARACTER: Doctor Lancaster
  LINE: This is... most irregular, Constable.
  EXPRESSION: Uneasy
- CHARACTER: Ichabod
  LINE: I should hope so. But in this case, necessary.
  EXPRESSION: Firm
- CHARACTER: Ichabod
  LINE: I will need to operate.
  EXPRESSION: Resolute
- CHARACTER: Doctor Lancaster
  LINE: Operate? She's dead!
  EXPRESSION: Shocked
- CHARACTER: Ichabod
  LINE: When we say "operate," we mean, of course... er, I'll need the operating table. Lay her out, please. Go on, nothing to be afraid of.
  EXPRESSION: Flustered
- CHARACTER: Narrator
  LINE: When Killian and Young Masbath lay out the corpse, Ichabod gulps water and studies the pages of his Ledger.
  EXPRESSION:null
- CHARACTER: Ichabod
  LINE: There is a common thread between these victims.
  EXPRESSION: Pondering
- CHARACTER: Doctor Lancaster
  LINE: And what's that?
  EXPRESSION: Inquisitive
- CHARACTER: Ichabod
  LINE: I don't know.
  EXPRESSION: Uncertain
- CHARACTER: Narrator
  LINE: He goes to examine the corpse. Young Masbath retreats to a corner, ill at ease.
  EXPRESSION:null
- CHARACTER: Ichabod
  LINE: Once more, the neck wound cauterized. The sword thrust to the stomach, the same, perhaps by chemical means. But to what purpose?
  EXPRESSION: Analytical
- CHARACTER: Narrator
  LINE: Ichabod gingerly feels the corpse's stomach. The Doctor watches. We get the feeling he "knows something."
  EXPRESSION:null
- CHARACTER: Doctor Lancaster
  LINE: To what is your purpose, is the question.
  EXPRESSION: Suspicious

::PATHS::
- CHOICE: "Ichabod continues his examination"
  TARGET: doctor_residence_day_later
  STATE_CHANGE: discovery = +1
  CONDITION: null

::SCENE::
LOCATION: Doctor's Residence - Exterior
MOOD: Tense Confrontation
CHARACTERS: Narrator, Young Masbath, Doctor Lancaster, Philipse, Steenwyck, Hardenbrook, Other People, Ichabod
BACKGROUND_IMAGE: doctor_residence_exterior.png
BACKGROUND_EDIT: "Daytime exterior, crowd gathered, Ichabod emerges bloody"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Young Masbath sits waiting. Doctor Lancaster stands with Philipse (hung over), Steenwyck and Hardenbrook, speaking agitatedly. Other People have gathered in the background.
  EXPRESSION:null
- CHARACTER: Narrator
  LINE: The door to the doctor's residence opens and Ichabod steps out. He is bloodied, shaken, futilely wiping at the mess with a blood-covered cloth, looking up...
  EXPRESSION: Shaken
- CHARACTER: Narrator
  LINE: All attention goes to Ichabod. Everyone's horrified.
  EXPRESSION: Horrified
- CHARACTER: Ichabod
  LINE: I am... finished.
  EXPRESSION: Exhausted
- CHARACTER: Steenwyck
  LINE: What in God's name have you done to her?
  EXPRESSION: Accusatory
- CHARACTER: Philipse
  LINE: And what did you find out, Constable?
  EXPRESSION: Inquisitive
- CHARACTER: Ichabod
  LINE: That there are not four victims but five. The Widow Winship was with child!
  EXPRESSION: Determined
- CHARACTER: Narrator
  LINE: The small crowd murmurs, shocked. Doctor Lancaster recovers, furious.
  EXPRESSION:null
- CHARACTER: Doctor Lancaster
  LINE: What of it? She should have been left to make her peace with God and not cut to bits by the Constabulary!
  EXPRESSION: Furious
- CHARACTER: Narrator
  LINE: Ichabod is shaken for a moment, remembering the similar charge made against him in New York.
  EXPRESSION:null
- CHARACTER: Ichabod
  LINE: The sword was thrust into the womb and no farther. A symbolic murder. We are dealing with a madman.
  EXPRESSION: Analytical

::PATHS::
- CHOICE: "Ichabod addresses the crowd"
  TARGET: covered_bridge_night
  STATE_CHANGE: confrontation = +1
  CONDITION: null

::SCENE::
LOCATION: Long Straight Road, Covered Bridge
MOOD: Ominous
CHARACTERS: Narrator, Ichabod, Gunpowder, Figure on Black Horse
BACKGROUND_IMAGE: covered_bridge_night.png
BACKGROUND_EDIT: "Nighttime, moonlight, a covered bridge"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Pale moonlight. Ichabod rides Gunpowder across the COVERED BRIDGE. They are an ungainly pair.
  EXPRESSION:null
- CHARACTER: Narrator
  LINE: Following the road, Ichabod is lost in thought. The CLOPPING of HOOFBEATS is HEARD on the bridge behind.
  EXPRESSION:null
- CHARACTER: Narrator
  LINE: Ichabod turns to look. HOOFBEATS STOP. No one can be seen in the dark mouth of the bridge. CRICKETS CHIRP.
  EXPRESSION:null
- CHARACTER: Ichabod
  LINE: Who's there?
  EXPRESSION: Cautious
- CHARACTER: Narrator
  LINE: Ichabod faces forward, continuing to the forest. He hums a tune to himself, tone deaf. After a moment, a HORSE is HEARD SNORTING, HOOFBEATS RESUME. Ichabod stops Gunpowder.
  EXPRESSION:null
- CHARACTER: Narrator
  LINE: There is SOMEONE back there, on horseback, coming out from the darkness of the bridge, slowly...
  EXPRESSION:null
- CHARACTER: Ichabod
  LINE: Who are you?
  EXPRESSION: Demanding
- CHARACTER: Narrator
  LINE: The FIGURE comes into moonlight, on a BLACK HORSE, smoke seeming to rise from him; a dark FIGURE, cloaked -- headless.
  EXPRESSION: Terrifying
- CHARACTER: Narrator
  LINE: Ichabod panics, kicking Gunpowder to flee. The figure takes off to follow.
  EXPRESSION: Panicked
- CHARACTER: Narrator
  LINE: Ichabod whips Gunpowder's reins, gasping, moving faster. The figure behind also picks up sp
  EXPRESSION:null

::PATHS::
- CHOICE: "Ichabod flees the Headless Horseman"
  TARGET: chase_sequence
  STATE_CHANGE: fear = +3, pursuit = true
  CONDITION: null

::SCENE::
LOCATION: Sleepy Hollow Forest
MOOD: Terrifying, Chased
CHARACTERS: Narrator, Ichabod, Headless Figure, Glenn, Theodore, Brom
BACKGROUND_IMAGE: sleepy_hollow_forest_night.png
BACKGROUND_EDIT: "Dark forest at night, gunpowder smoke, cloaked figure"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Gunpowder carries Ichabod into the forest. The headless figure is right behind, cloak flowing...
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The HEADLESS FIGURE is HEARD letting out a hellish CRY of rage.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Ichabod glances fearfully over his shoulder...
  EXPRESSION: Afraid
- CHARACTER: Narrator
  LINE: A HORRIBLE FACE with flaming eyes and mouth rushes forward...
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: It SMASHES into Ichabod -- sends him sprawling to the ground in an explosion of red hot ash and cinders...
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Ichabod rolls, shaken... looking behind. The trail is empty. HOOFBEATS are HEARD. SEVERAL HORSES.
  EXPRESSION: Shaken
- CHARACTER: Narrator
  LINE: Ichabod stands. He looks down at the remnants of a BROKEN JACK-O'-LANTERN and smoldering ball of paper on the trail.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The FIGURE rides to a halt, throws off a cloak and "headless" disguise; it's Brom. Glenn and Theodore ride up, laughing.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Brom also laughs, but when he looks back, the smile leaves his face.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: He takes grim satisfaction in what he's done.
  EXPRESSION: Grim
- CHARACTER: Narrator
  LINE: Ichabod's face is haunted, running with the sweat of fear -- he is still trembling from the experience.
  EXPRESSION: Terrified

::PATHS::
- CHOICE: "React to the aftermath"
  TARGET: ichabod_dream_cottage
  STATE_CHANGE: fear = +3, trauma = +1
  CONDITION: null

::SCENE::
LOCATION: Ichabod's Dream - Cottage Exterior
MOOD: Dreamlike, Nostalgic
CHARACTERS: Narrator, Ichabod (dreaming), Female Voice (V.O.), Katrina (vision), Young Boy
BACKGROUND_IMAGE: ichabod_dream_cottage_day.png
BACKGROUND_EDIT: "Daytime, a cottage doorway, bright light"

::SCRIPT::
- CHARACTER: Female Voice (V.O.)
  LINE: Ichabod! Ichabod!
  EXPRESSION: Calling
- CHARACTER: Narrator
  LINE: And suddenly we are pitched into Ichabod's DREAM.
  EXPRESSION: null
- CHARACTER: Female Voice (V.O.)
  LINE: Ichabod! Ichabod... !
  EXPRESSION: Calling
- CHARACTER: Narrator
  LINE: A woman is in the doorway, holding out her arms. She seems to be Katrina as Ichabod first saw her, blindfolded.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: A YOUNG BOY, aged about seven, runs toward her, with a little bunch of wildflowers.
  EXPRESSION: null

::PATHS::
- CHOICE: "Enter the dream sequence"
  TARGET: ichabod_dream_kitchen
  STATE_CHANGE: dream_level = +1
  CONDITION: null

::SCENE::
LOCATION: Ichabod's Dream - Young Ichabod's Kitchen
MOOD: Playful, then eerie
CHARACTERS: Narrator, Blindfolded Woman (Mother), Young Ichabod, Cat, Father (Parson)
BACKGROUND_IMAGE: ichabod_dream_kitchen_night.png
BACKGROUND_EDIT: "Nighttime kitchen, hearth, playing a game"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The Blindfolded Woman is playing the Pickety Witch Game with Ichabod.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: He is laughing -- scared as she grabs the air looking for him. He is holding the wildflowers he picked. She seizes him, kisses him and takes off the blindfold. It's not Katrina, but his Mother, a kind and lovely face. He gives his Mother the flowers. She puts one of the flowers in her hair, laughing. But the others -- she throws on the fire! -- and she crouches at the hearthstone, beckoning him, still "nice." He comes to her, not scared.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: As the flowers burn, they give off smoky fumes, which the Mother inhales like perfume, closing her eyes in a trance. He watches fascinated as she picks up a twig and starts drawing pictures -- strange designs -- in the layer of ash on the hearthstone.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Suddenly Ichabod turns his head to the door, which is opening -- spooky because no one is entering. Then he sees at floor level the family CAT has come through the door. A black cat with a white paw.
  EXPRESSION: Spooky
- CHARACTER: Narrator
  LINE: Ichabod's Mother is "awakened" by this, just in time as Father, a grim Parson all in black, enters.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Ichabod looks up frightened at the face of his Father.
  EXPRESSION: Frightened

::PATHS::
- CHOICE: "Continue dream sequence"
  TARGET: ichabod_dream_bedroom
  STATE_CHANGE: unsettling_dream = +1
  CONDITION: null

::SCENE::
LOCATION: Ichabod's Dream - Young Ichabod's Bedroom
MOOD: Whimsical, then stormy
CHARACTERS: Narrator, Cat, Mother, Young Ichabod
BACKGROUND_IMAGE: ichabod_dream_bedroom_night.png
BACKGROUND_EDIT: "Nighttime bedroom, a toy, lightning outside"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The Cat is on Ichabod's bed... watching Mother who is entertaining Ichabod with the Bird-in-Cage Spinning Disc Toy, which we will get to know.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Ichabod is tucked up in bed, astonished and happy. The Bird and Cage blur together.
  EXPRESSION: Happy
- CHARACTER: Narrator
  LINE: Lightning flashes outside a window, thunder booms, the storm bursts open the window.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The Cat leaps off the bed, caught in lightning flash, the Toy drops, tangled on the bed. Ichabod covers his face, scared; his Mother hugs him.
  EXPRESSION: Scared

::PATHS::
- CHOICE: "Wake up from dream"
  TARGET: van_tassel_ichabod_room
  STATE_CHANGE: dream_level = -1, fear = +1
  CONDITION: null

::SCENE::
LOCATION: Van Tassel House, Ichabod's Room
MOOD: Startled, Anxious
CHARACTERS: Narrator, Ichabod
BACKGROUND_IMAGE: van_tassel_ichabod_room_night.png
BACKGROUND_EDIT: "Nighttime bedroom, Ichabod just woke up"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Ichabod is startled awake, frightened, sweating.
  EXPRESSION: Frightened

::PATHS::
- CHOICE: "Go to the kitchen"
  TARGET: van_tassel_kitchen
  STATE_CHANGE: anxiety = +1
  CONDITION: null

::SCENE::
LOCATION: Van Tassel House, Kitchen
MOOD: Pensive, Curious
CHARACTERS: Narrator, Ichabod
BACKGROUND_IMAGE: van_tassel_kitchen_night.png
BACKGROUND_EDIT: "Nighttime kitchen, Ichabod with lantern and ledger"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Ichabod enters with a lantern and his Ledger. He sits, studies notes, then notices a light down the hall.
  EXPRESSION: null

::PATHS::
- CHOICE: "Investigate the light"
  TARGET: van_tassel_sewing_room
  STATE_CHANGE: curiosity = +1
  CONDITION: null

::SCENE::
LOCATION: Van Tassel House, Sewing Room
MOOD: Intriguing, Uncomfortable
CHARACTERS: Narrator, Ichabod, Katrina
BACKGROUND_IMAGE: van_tassel_sewing_room_night.png
BACKGROUND_EDIT: "Nighttime sewing room, Katrina reading by candlelight"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Ichabod enters. Opposite an elaborate LOOM, Katrina reads by candlelight.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: She looks up, and self-consciously closes her book, which we see is a child's version of THE KNIGHTS OF THE ROUND TABLE. She covers it on her lap.
  EXPRESSION: Shy
- CHARACTER: Ichabod
  LINE: Oh... pardon my intrusion... I saw a light...
  EXPRESSION: Polite
- CHARACTER: Katrina
  LINE: It is no intrusion... I come here to read when I am wakeful.
  EXPRESSION: Calm
- CHARACTER: Ichabod
  LINE: To read books which you must hide... ?
  EXPRESSION: Curious
- CHARACTER: Katrina
  LINE: They were my mother's books... my father frowned at them then, and would frown at me now. He believes tales of romance caused the brain fever that killed my mother. She died two years ago come midwinter.
  EXPRESSION: Sad
- CHARACTER: Narrator
  LINE: Ichabod nods.
  EXPRESSION: Understanding
- CHARACTER: Ichabod
  LINE: I saw it written in the front of the Bible.
  EXPRESSION: Grave
- CHARACTER: Katrina
  LINE: The nurse who cared for her during her sickness is now Lady Van Tassel.
  EXPRESSION: Neutral
- CHARACTER: Ichabod
  LINE: There was something else too. Why did no one think to mention that Van Garretts are kith and kin to the Van Tassels?
  EXPRESSION: Puzzled
- CHARACTER: Katrina
  LINE: Why, because there is hardly a household in Sleepy Hollow that is not connected to every other by blood or marriage. I have more cousins than fingers and toes to count them on.
  EXPRESSION: Matter-of-fact
- CHARACTER: Narrator
  LINE: A cock crows. Ichabod goes to the window to look at the edge of dawn.
  EXPRESSION: null
- CHARACTER: Ichabod
  LINE: I see.
  EXPRESSION: Understanding
- CHARACTER: Katrina
  LINE: This land was Van Garrett Land, given to my father when I was in swaddling clothes.
  EXPRESSION: Proud
- CHARACTER: Ichabod
  LINE: Given by the dead Van Garrett?
  EXPRESSION: Skeptical
- CHARACTER: Katrina
  LINE: (nods) The Van Garretts were the richest family round these parts even then. When my father brought us to Sleepy Hollow, Van Garrett set him up with an acre and a broken-down cottage, and a dozen of Van Garrett hens. My father prospered, and built us a new house. I owe my happiness to him. I remember living poor in the cottage. Should I show you?
  EXPRESSION: Nostalgic
- CHARACTER: Ichabod
  LINE: Yes. I would like to see where you were as poor as I am.
  EXPRESSION: Empathetic

::PATHS::
- CHOICE: "Accept Katrina's offer"
  TARGET: fields_day
  STATE_CHANGE: connection = +1, curiosity = +1
  CONDITION: null

::SCENE::
LOCATION: Fields
MOOD: Romantic, Peaceful
CHARACTERS: Narrator, Ichabod, Katrina
BACKGROUND_IMAGE: fields_day.png
BACKGROUND_EDIT: "Daytime fields, Ichabod and Katrina on horseback"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Ichabod and Katrina make a pretty picture on horseback, riding slowly toward the cottage.
  EXPRESSION: null

::PATHS::
- CHOICE: "Arrive at the cottage ruin"
  TARGET: sleepy_hollow_farmland
  STATE_CHANGE: romance = +1
  CONDITION: null

::SCENE::
LOCATION: Sleepy Hollow Farmland
MOOD: Reflective, Eerie
CHARACTERS: Narrator, Ichabod, Katrina
BACKGROUND_IMAGE: sleepy_hollow_farmland_day.png
BACKGROUND_EDIT: "Daytime farmland, ruin of a cottage"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Ichabod and Katrina, riding, come upon the ruin of a cottage. There is almost nothing left but the hearth and a part of a chimney.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Ichabod dismounts and helps Katrina down from her horse, taking her hand.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Before he lets go, she notices the little scars on his palm. She takes both his hands and looks at them.
  EXPRESSION: Concerned
- CHARACTER: Katrina
  LINE: These are strange... What are they... ?
  EXPRESSION: Puzzled
- CHARACTER: Ichabod
  LINE: I wish I knew. I had them since I can remember.
  EXPRESSION: Unsure
- CHARACTER: Narrator
  LINE: Katrina holds his hands a moment longer, their eyes meet, then she lets go and "enters" the ruin.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Ichabod's attention is caught by a red Cardinal on a branch, like the bird he had in New York.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: He reflects a moment, then turns to watch Katrina crouching by the hearth. She has put a flower in her hair.
  EXPRESSION: null
- CHARACTER: Katrina
  LINE: I used to play by this hearth. It was my first drawing school and my mother was my teacher.
  EXPRESSION: Nostalgic
- CHARACTER: Narrator
  LINE: Unwittingly, Katrina is mimicking Ichabod's dream. She picks up a twig and starts "drawing" on the hearth stone. Like Ichabod's mother in his dream.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Ichabod's blood runs cold but she is unaware of him. Then he notices that a few small wildflowers are growing in the old fireplace. Ichabod feels short of breath, he leans against the stones for support.
  EXPRESSION: Cold, Short of breath
- CHARACTER: Katrina
  LINE: Oh, look! I'd forgotten this! -- see -- carved into the fire-back, the Archer!
  EXPRESSION: Excited
- CHARACTER: Narrator
  LINE: Using her fingers she cleans off the dirt around a simple carving of a man with a Bow and Arrow.
  EXPRESSION: null
- CHARACTER: Katrina
  LINE: This was from long before we lived here.
  EXPRESSION: Informative
- CHARACTER: Narrator
  LINE: She turns to show Ichabod and notices him looking strange.
  EXPRESSION: null
- CHARACTER: Katrina
  LINE: Are you all right?
  EXPRESSION: Concerned
- CHARACTER: Narrator
  LINE: Ichabod nods, recovering, saying nothing.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Katrina is reassured. Suddenly her attention is caught, as Ichabod's was, by the Cardinal bird.
  EXPRESSION: null
- CHARACTER: Katrina
  LINE: (pointing) Oh, look! A Cardinal! My favorite
  EXPRESSION: Delighted

::PATHS::
- CHOICE: "Continue interaction"
  TARGET: end
  STATE_CHANGE: eerie_feeling = +2, connection = +1
  CONDITION: null

::SCENE::
LOCATION: Village House - Interior
MOOD: Curious, Whimsical
CHARACTERS: Narrator, Ichabod, Katrina
BACKGROUND_IMAGE: village_house_interior.png
BACKGROUND_EDIT: "Cozy interior, daylight"

::SCRIPT::
- CHARACTER: Narrator
  LINE: I would love to have a tame one, but I wouldn't have the heart to cage him.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Ichabod unslings his satchel.
  EXPRESSION: null
- CHARACTER: ICHABOD
  LINE: Then I have something for you.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: He has a PAPER DISK with a BIRD on one side and an EMPTY CAGE on the other, pierced by a looped string on which the disk can twist and spin. He demonstrates like a magician. This is the very Toy given to him by his Mother.
  EXPRESSION: null
- CHARACTER: ICHABOD
  LINE: A Cardinal on one side, and an empty cage.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Katrina watches intently. Ichabod spins the Disk.
  EXPRESSION: null
- CHARACTER: ICHABOD
  LINE: And now...
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The bird appears to be inside the cage.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Katrina is astonished and delighted.
  EXPRESSION: null
- CHARACTER: KATRINA
  LINE: You can do magic! Teach me!
  EXPRESSION: null
- CHARACTER: ICHABOD
  LINE: It is no magic. It is optics.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Ichabod gives her the Toy and shows her how to spin it.
  EXPRESSION: null
- CHARACTER: ICHABOD
  LINE: Separate pictures which become one picture in the spinning... Like the truth which I must spin here...
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Katrina spins the disk, the bird appears in the cage.
  EXPRESSION: null

::PATHS::
- CHOICE: "Observe Philipse House"
  TARGET: philipse_house_exterior
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Philipse House - Exterior
MOOD: Suspenseful, Observant
CHARACTERS: Narrator, Steenwyck, Doctor Lancaster, Hardenbrook, Philipse, Ichabod
BACKGROUND_IMAGE: philipse_house_exterior.png
BACKGROUND_EDIT: "Nighttime, village house, lights visible, men arguing inside"

::SCRIPT::
- CHARACTER: Narrator
  LINE: A MOVING POV is checking out the Village House. Through lighted windows, figures of Men are seen pacing, apparently arguing.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Philipse is packing his bags, moving out... while three Men, Steenwyck, Doctor Lancaster and Hardenbrook, are in agitated conference. Their raised voices make an undecipherable hubbub. The POV'S horse makes a horsey snuffling sound. Is it Daredevil?
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Steenwyck comes right to the window as if he has seen something... but he merely closes the shutters.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The REVERSE shows that it is Ichabod who has been spying.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Ichabod backs off and mounts Gunpowder, looking thoughtful, then determined.
  EXPRESSION: null

::PATHS::
- CHOICE: "Intercept Philipse on the road"
  TARGET: road_outside_village
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Road Outside Village - Exterior
MOOD: Confrontational, Mysterious
CHARACTERS: Narrator, Philipse, Ichabod
BACKGROUND_IMAGE: road_outside_village.png
BACKGROUND_EDIT: "Nighttime, rural road, heavily loaded pack horse"

::SCRIPT::
- CHARACTER: Narrator
  LINE: A Mounted Man is approaching on a heavily loaded Pack Horse... Philipse making his getaway from Sleepy Hollow. As he reaches the foreground, Ichabod on Gunpowder intercepts him, grabbing the bridle of the Pack Horse.
  EXPRESSION: null
- CHARACTER: PHILIPSE
  LINE: What are you doing? Let go!
  EXPRESSION: Angry
- CHARACTER: ICHABOD
  LINE: What are you running from, Magistrate Philipse?
  EXPRESSION: null
- CHARACTER: PHILIPSE
  LINE: Damn you, Crane --
  EXPRESSION: Angry
- CHARACTER: ICHABOD
  LINE: You'll raise the village.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Philipse calms down.
  EXPRESSION: null
- CHARACTER: ICHABOD
  LINE: You had a mind to help me.
  EXPRESSION: null
- CHARACTER: PHILIPSE
  LINE: Yes -- and I put myself in mortal dread of...
  EXPRESSION: Fearful
- CHARACTER: ICHABOD
  LINE: Of... what?
  EXPRESSION: null
- CHARACTER: PHILIPSE
  LINE: Powers against which there is no defense.
  EXPRESSION: Fearful
- CHARACTER: ICHABOD
  LINE: How did you know the widow was expecting a child?
  EXPRESSION: null
- CHARACTER: PHILIPSE
  LINE: She told me.
  EXPRESSION: null
- CHARACTER: ICHABOD
  LINE: Then I deduce you are the father.
  EXPRESSION: null
- CHARACTER: PHILIPSE
  LINE: I hope your deductions serve you better in your contest against the Hessian. I am not the father.
  EXPRESSION: Stern
- CHARACTER: ICHABOD
  LINE: Did she tell you the name of the child's father?
  EXPRESSION: null
- CHARACTER: PHILIPSE
  LINE: Yes -- she did. She came to me for advice -- as the town magistrate --
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Ichabod hears sounds... of sheep in agitation at some distance but he holds Philipse to his story.
  EXPRESSION: null
- CHARACTER: PHILIPSE
  LINE: -- to protect the rights of her child. I was bound by my oath of office to keep the secret --
  EXPRESSION: Solemn
- CHARACTER: ICHABOD
  LINE: Do you believe the father killed her?
  EXPRESSION: null
- CHARACTER: PHILIPSE
  LINE: The Horseman killed her! -- You damn fool, do you suppose the Horseman stops to impregnate our women?
  EXPRESSION: Disgusted
- CHARACTER: ICHABOD
  LINE: The Horseman? How often do I have to tell you there is no Horseman! There never was a Horseman! -- and there never will be a Horseman!
  EXPRESSION: Frustrated
- CHARACTER: Narrator
  LINE: Ichabod grabs him fiercely, pulling on the amulet Philipse wears around his neck.
  EXPRESSION: null
- CHARACTER: PHILIPSE
  LINE: Let go! -- it is my talisman that protects me from the Horseman!
  EXPRESSION: Panicked
- CHARACTER: ICHABOD
  LINE: You a magistrate! -- and your head full of such nonsense! Now tell me the name of --
  EXPRESSION: Angry
- CHARACTER: Narrator
  LINE: A flock of sheep comes streaming and bleating across the path. The horses go crazy, BRAYING and rearing. A SOUND is HEARD, distant: THUNDERING HOOFBEATS. Wind kicks up.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Philipse looks to the forest. A FLOCK of BIRDS alights.
  EXPRESSION: null
- CHARACTER: PHILIPSE
  LINE: Oh my... oh my oh my oh my...
  EXPRESSION: Terrified
- CHARACTER: Narrator
  LINE: Philipse runs away. HOOFBEATS LOUDER, CLOSER. Ichabod faces the forest.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The forest explodes open, foliage bending to make way as the HEADLESS HORSEMAN gallops into view atop DAREDEVIL.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Ichabod's stunned. He looks down to draw his flintlock pistol, but the Horseman ROARS by before he can raise it -- a blast of air knocks Ichabod off his horse.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: After this, everything happens very quickly --
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The Horseman chases Philipse.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Philipse looks over his shoulder.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The Horseman draws his sword.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Philipse gathers his courage and stops, turning. He raises his iron key talisman before him. The Horseman is closing...
  EXPRESSION: null
- CHARACTER: ICHABOD
  LINE: Philipse!
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Philipse holds the talisman up, trying to be fearless. The Horseman swings his sword upon the talisman -- CLANK...
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Philipse's severed head spins. His body falls and folds.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The two pieces of Philipse's Talisman, an Iron Key, fly through the air, toward Ichabod, who has only just managed to find his feet and find his fallen pistol.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The Horseman turns Daredevil in a wide circle...
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Daredevil completes the turn, letting out a SCREECHY CRY as the Horseman rides straight toward Ichabod...
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Before Ichabod has time to take aim, the Horseman is upon him and past him! -- heading toward Philipse's corpse... leans effortlessly to skewer Philipse's head with his sword.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: With the head as his prize, the Horseman races away.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Ichabod turns, watches the Horseman head to the forest.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Ichabod stands, stricken. He faints.
  EXPRESSION: null

::PATHS::
- CHOICE: "Wake up in room"
  TARGET: ichabod_bedroom_day
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Van Tassel House, Ichabod's Bedroom - Interior
MOOD: Confused, Disoriented
CHARACTERS: Narrator, Ichabod, Baltus (O.S.)
BACKGROUND_IMAGE: ichabod_bedroom.png
BACKGROUND_EDIT: "Daytime, Ichabod's room, morning"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Ichabod gasps awake. A KNOCKING is HEARD.
  EXPRESSION: null
- CHARACTER: BALTUS'S VOICE
  LINE: Constable Crane... ?
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Ichabod looks at his hand balled into a fist. He opens his hand -- holds BOTH HALVES of PHILIPSE'S IRON KEY TALISMAN.
  EXPRESSION: null

::PATHS::
- CHOICE: "Go to upstairs hall"
  TARGET: upstairs_hall_3rd_floor
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Van Tassel House, Upstairs Hall 3rd Floor - Interior
MOOD: Concerned, Anxious
CHARACTERS: Narrator, Young Masbath, Katrina, Baltus
BACKGROUND_IMAGE: upstairs_hall_3rd_floor.png
BACKGROUND_EDIT: "Daytime, hallway outside Ichabod's room"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Young Masbath is seated by Ichabod's closed door. Katrina is backing up Baltus, who knocks again.
  EXPRESSION: null
- CHARACTER: BALTUS
  LINE: Has he not come out at all?
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Young Masbath shakes his head.
  EXPRESSION: null

::PATHS::
- CHOICE: "Enter Ichabod's room"
  TARGET: ichabod_room_day
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Van Tassel House, Ichabod's Room - Interior
MOOD: Agitated, Confused
CHARACTERS: Narrator, Baltus, Katrina, Young Masbath, Ichabod
BACKGROUND_IMAGE: ichabod_room.png
BACKGROUND_EDIT: "Daytime, Ichabod's room, Ichabod sitting up in bed"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Baltus enters. Katrina and Masbath follow him, cautiously, "visiting the sick." Ichabod sits up in bed, stunned, spaced out.
  EXPRESSION: null
- CHARACTER: ICHABOD
  LINE: It was a Headless Horseman!
  EXPRESSION: Agitated
- CHARACTER: BALTUS
  LINE: You must not excite yourself.
  EXPRESSION: Calm
- CHARACTER: ICHABOD
  LINE: But it was Headless Horseman!
  EXPRESSION: Agitated
- CHARACTER: BALTUS
  LINE: Of course it was.
  EXPRESSION: Calm
- CHARACTER: ICHABOD
  LINE: No, you must believe me, it was Horseman! A dead one! Headless!
  EXPRESSION: Desperate
- CHARACTER: BALTUS
  LINE: I know, I know...
  EXPRESSION: Reassuring
- CHARACTER: ICHABOD
  LINE: You don't know because you weren't there! But it's all true!
  EXPRESSION: Desperate
- CHARACTER: BALTUS
  LINE: Of course it is. I told you! Everyone told you!
  EXPRESSION: Calm
- CHARACTER: ICHABOD
  LINE: I saw him!
  EXPRESSION: Frantic
- CHARACTER: Narrator
  LINE: His eyes roll up and he faints. Katrina and Masbath look helplessly at each other.
  EXPRESSION: null
- CHARACTER: YOUNG MASBATH
  LINE: I suppose it's back to the City, then.
  EXPRESSION: Resigned
- CHARACTER: Narrator
  LINE: Katrina's reaction is mixed -- glad that Ichabod will be safe, sorry if he leaves.
  EXPRESSION: null

::PATHS::
- CHOICE: "Enter Ichabod's dream"
  TARGET: ichabod_dream_forest
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Ichabod's Dream - Forest - Exterior
MOOD: Nostalgic, Ethereal
CHARACTERS: Narrator, Young Ichabod, Mother
BACKGROUND_IMAGE: ichabod_dream_forest.png
BACKGROUND_EDIT: "Daytime, sunlit forest, floating milkweed seedlings"

::SCRIPT::
- CHARACTER: Narrator
  LINE: A MILLION WHITE MILKWEED SEEDLINGS are floating in sunlight. Young Ichabod's laughter is heard.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Now we see that his Mother is blowing the seedlings for his delight.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: She gives him a milkweed pod and shows him how to do it for himself.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Ichabod breaks the pod and releases another million. But when he looks around to share the delight, his Mother has gone... and he sees her disappearing among the trees. He goes to follow her.
  EXPRESSION: null

::PATHS::
- CHOICE: "Follow mother to glade"
  TARGET: ichabod_dream_forest_glade
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Ichabod's Dream - Forest Glade - Exterior
MOOD: Dreamlike, Foreboding
CHARACTERS: Narrator, Ichabod, Mother, Headless Figures, Father
BACKGROUND_IMAGE: ichabod_dream_forest_glade.png
BACKGROUND_EDIT: "Daytime, forest glade, circle of mushrooms"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Ichabod can't see his Mother anywhere... Then he sees her standing in the middle of a CIRCLE OF BEAUTIFUL TOADSTOOLS/MUSHROOMS growing in the Glade.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Ichabod watches as his Mother turns inside the Mushroom Circle, almost dancing. He smiles. Then he sees his Mother stoop to pick a mushroom.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: She eats it. She looks happy. She drops a small piece of the mushroom. Ichabod sees it fall.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: He runs forward and picks it up before she sees him. Ichabod eats it.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: His Mother sees him, takes his hands in hers and dances around in a circle.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: As Ichabod whizzes around laughing, his POV becomes the Enclosing Trees whizzing around, and suddenly he seems to be surrounded by Menacing Headless Figures dressed all in black.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Ichabod falls over dizzy and when he looks up he sees that the Headless Figures have become his Father, watching his Mother heedlessly dancing, his face like thunder. His Mother has loosened her clothes and is virtually bareb
  EXPRESSION: null

::PATHS::
- CHOICE: "Awaken from dream"
  TARGET: end
  STATE_CHANGE: dream_state = true
  CONDITION: null

::SCENE::
LOCATION: Ichabod's House (Dream)
MOOD: Fearful
CHARACTERS: Ichabod, Father, Mother
BACKGROUND_IMAGE: ichabod_house_night.png
BACKGROUND_EDIT: "Nighttime, looking through a crack in the kitchen door."

::SCRIPT::
- CHARACTER: Narrator
  LINE: His Father's eyes begin to glow like live coals as Ichabod cowers away from him.
  EXPRESSION: Fearful
- CHARACTER: Narrator
  LINE: Ichabod's eyes are spying... through a crack in the kitchen door.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: When we see him properly, he is wearing a nightshirt. Then we see his POV, into the kitchen.
  EXPRESSION: null

::SCENE::
LOCATION: Young Ichabod's Kitchen (Dream)
MOOD: Tense, Abusive
CHARACTERS: Mother, Father
BACKGROUND_IMAGE: young_ichabod_kitchen_night.png
BACKGROUND_EDIT: "Nighttime kitchen, Mother seated with head down, Father pacing."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Mother is seated, her head down. Father paces, chastising Mother angrily, his fist balled up in rage.
  EXPRESSION: Angry
- CHARACTER: Narrator
  LINE: Father continues berating Mother. He picks up his Bible off the table, waving it, then grabs Mother by the shoulders, forcing her to the floor...
  EXPRESSION: Violent
- CHARACTER: Narrator
  LINE: Father forces Mother to her knees. Mother is afraid, clasping her hands in front of her as Father forces her to pray.
  EXPRESSION: Afraid
- CHARACTER: Narrator
  LINE: Father starts reading from the Bible. In Ichabod's dream, this is the same Bible from Baltus's house.
  EXPRESSION: null

::SCENE::
LOCATION: Young Ichabod's Stairwell (Dream)
MOOD: Fearful
CHARACTERS: Ichabod
BACKGROUND_IMAGE: young_ichabod_stairwell_night.png
BACKGROUND_EDIT: "Nighttime stairwell, Ichabod backing away."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Ichabod watches, afraid. He backs away, returning upstairs.
  EXPRESSION: Fearful

::SCENE::
LOCATION: Young Ichabod's Bedroom (Dream)
MOOD: Chaotic, Frightening
CHARACTERS: Young Ichabod
BACKGROUND_IMAGE: young_ichabod_bedroom_night.png
BACKGROUND_EDIT: "Nighttime bedroom, window being thrown open by wind and rain."

::SCRIPT::
- CHARACTER: Narrator
  LINE: A window is thrown crashing open, thunder booming... Young Ichabod sits up in his bed. He goes to close the window, rain pouring in. He looks down...
  EXPRESSION: Startled

::SCENE::
LOCATION: EXT. Young Ichabod's House (Dream)
MOOD: Desperate, Tragic
CHARACTERS: Mother, Young Ichabod, Father, Two Men
BACKGROUND_IMAGE: ext_young_ichabod_house_night.png
BACKGROUND_EDIT: "Nighttime, rain, a man dragging Mother toward a coach, two men watching."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Below, in front of the home, a Man drags Mother toward a coach. Two Men stand watching, faces hidden under hat brims. Mother looks back, eyes pleading, struggling...
  EXPRESSION: Pleading
- CHARACTER: Narrator
  LINE: Mother looks up to Young Ichabod.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The Two Men looks up to Young Ichabod: one is Father, and the third man is a Cotton Matherish man with a villainous face.
  EXPRESSION: Sinister
- CHARACTER: Narrator
  LINE: Young Ichabod reaches helplessly toward Mother.
  EXPRESSION: Helpless
- CHARACTER: Narrator
  LINE: Mother is forced into the coach.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The Third Man speaks to Father, then walks to the coach. He gets onto the coach as the coach starts away.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Father watches, rain flowing down his stony features.
  EXPRESSION: Stoic
- CHARACTER: Narrator
  LINE: Lighting flashes... And we see the family Cat watching with glowing eyes.
  EXPRESSION: Eerie

::SCENE::
LOCATION: Van Tassel House
MOOD: Determined
CHARACTERS: Ichabod
BACKGROUND_IMAGE: van_tassel_house_day.png
BACKGROUND_EDIT: "Daytime, Ichabod waking up with renewed determination."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Ichabod's eyes as he opens them. He wakes, breathing heavily. After a beat, he flings back the bedclothes and springs out of bed, energized by a new determination.
  EXPRESSION: Determined

::SCENE::
LOCATION: Van Tassel House, Downstairs
MOOD: Formal, Urgent
CHARACTERS: Baltus, Steenwyck, Doctor Lancaster, Notary Hardenbrook, Lady Van Tassel, Katrina, Ichabod, Young Masbath
BACKGROUND_IMAGE: van_tassel_house_downstairs_day.png
BACKGROUND_EDIT: "Daytime, a meeting in progress with drinks being served."

::SCRIPT::
- CHARACTER: Baltus
  LINE: Right -- this time I'll go to New York myself and I won't be fobbled off with an amateur deductor.
  EXPRESSION: Authoritative
- CHARACTER: Hardenbrook
  LINE: Detector.
  EXPRESSION: Correcting
- CHARACTER: Steenwyck
  LINE: Deductive.
  EXPRESSION: Correcting
- CHARACTER: Doctor Lancaster
  LINE: No... no...
  EXPRESSION: Doubtful
- CHARACTER: Baltus
  LINE: An amateur sleuth! This time it's a magistrate that's dead, and --
  EXPRESSION: Impatient
- CHARACTER: Narrator
  LINE: The door is flung open without ceremony.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: It's Ichabod ready for action, transformed, raring to go -- with Young Masbath round-eyed just behind him.
  EXPRESSION: Eager
- CHARACTER: Ichabod
  LINE: Gentlemen! -- I need able men, to go with me to the Western Woods. Who will be the first to volunteer?
  EXPRESSION: Bold
- CHARACTER: Baltus
  LINE: You... ? We thought you'd shot your bolt...
  EXPRESSION: Skeptical
- CHARACTER: Ichabod
  LINE: A setback, merely. And yet, a step forward too -- we now know who has done these terrible --
  EXPRESSION: Confident
- CHARACTER: Steenwyck
  LINE: You now know, we already knew --
  EXPRESSION: Dismissive
- CHARACTER: Ichabod
  LINE: Quite so -- and now it seems fate has chosen me to make my name in a case without parallel in the annals of crime -- in short, to pit myself against a murdering ghost.
  EXPRESSION: Exalted
- CHARACTER: Katrina
  LINE: No, Ichabod -- Constable --
  EXPRESSION: Fearful
- CHARACTER: Lady Van Tassel
  LINE: Do you intend to arrest him? Or impound his horse... ?
  EXPRESSION: Amused
- CHARACTER: Narrator
  LINE: The Men chuckle indulgently.
  EXPRESSION: Amused
- CHARACTER: Ichabod
  LINE: Neither. To put an end to the killing. To discover the cause and remove it. Who's with me?
  EXPRESSION: Determined
- CHARACTER: Narrator
  LINE: No one.
  EXPRESSION: null

::SCENE::
LOCATION: EXT. Western Woods
MOOD: Adventurous, Mysterious
CHARACTERS: Ichabod, Young Masbath
BACKGROUND_IMAGE: ext_western_woods_day.png
BACKGROUND_EDIT: "Daytime, dark, gnarled and creepy woods, Ichabod and Young Masbath riding."

::SCRIPT::
- CHARACTER: Narrator
  LINE: No one, indeed... Ichabod and Young Masbath ride alone... their horses loaded up for the expedition.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Dark, gnarled and creepy woods. Ichabod and Young Masbath move through. Sound of birds etc.
  EXPRESSION: null
- CHARACTER: Ichabod
  LINE: The Van Garretts, the Widow Winship ... your father, Jonathan Masbath... and now Philipse... Something must connect them. Can you think?
  EXPRESSION: Inquisitive
- CHARACTER: Young Masbath
  LINE: We had no dealings with the magistrate that I know of...
  EXPRESSION: Puzzled
- CHARACTER: Ichabod
  LINE: And the widow? Your father knew her?
  EXPRESSION: Inquisitive
- CHARACTER: Young Masbath
  LINE: Everyone knew Widow Winship.
  EXPRESSION: Casual
- CHARACTER: Ichabod
  LINE: In a manner of speaking, I trust.
  EXPRESSION: Sarcastic
- CHARACTER: Young Masbath
  LINE: She would bring old Mr. Van Garrett a basket of eggs many a day.
  EXPRESSION: Informative
- CHARACTER: Ichabod
  LINE: Did your father have dealings with the Van Garretts?
  EXPRESSION: Inquisitive
- CHARACTER: Young Masbath
  LINE: He worked for them, we lived in the coach house.
  EXPRESSION: Surprised
- CHARACTER: Narrator
  LINE: Ichabod halts his horse, surprised.
  EXPRESSION: Surprised
- CHARACTER: Young Masbath
  LINE: It's nothing -- there were many servants... all dismissed now, of course.
  EXPRESSION: Dismissive
- CHARACTER: Narrator
  LINE: (beat -- they ride on)
  EXPRESSION: null
- CHARACTER: Young Masbath
  LINE: But there was something happened one night, a week before the murder. An argument upstairs between father and son, and my father was later sent for by Mr. Van Garrett.
  EXPRESSION: Reflective
- CHARACTER: Ichabod
  LINE: An argument between father and son?
  EXPRESSION: Thoughtful
- CHARACTER: Narrator
  LINE: (to himself, thoughtfully)
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: After which, the elder Van Garrett summoned his servant, Masbath...
  EXPRESSION: null
- CHARACTER: Young Masbath
  LINE: Listen.
  EXPRESSION: Urgent
- CHARACTER: Ichabod
  LINE: I hear nothing.
  EXPRESSION: Perplexed
- CHARACTER: Young Masbath
  LINE: Nor I -- no birds -- no crickets -- Everything has gone quiet.
  EXPRESSION: Uneasy
- CHARACTER: Narrator
  LINE: -- it's all gone so quiet...
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Ichabod notes this nervously.
  EXPRESSION: Nervous
- CHARACTER: Ichabod
  LINE: You're right!
  EXPRESSION: Alarmed
- CHARACTER: Narrator
  LINE: He gees up the horses. They break into a gallop. A moving POV watches them gallop by.
  EXPRESSION: null

::SCENE::
LOCATION: EXT. Western Woods and Cave Entrance
MOOD: Foreboding, Cautious
CHARACTERS: Ichabod, Young Masbath
BACKGROUND_IMAGE: ext_western_woods_cave_entrance_day.png
BACKGROUND_EDIT: "Daytime, Ichabod and Masbath reaching a hill crest, looking down at a cave with a rock archway."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Ichabod and Masbath reach a hill crest. They stop, uneasy.
  EXPRESSION: Uneasy
- CHARACTER: Narrator
  LINE: Below, there is a cave with a rock archway. An ill-fitting door covers the mouth. The chimney spews smoke.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Ichabod and Masbath share a fearful look.
  EXPRESSION: Fearful
- CHARACTER: Narrator
  LINE: Elsewhere, someone watches... A moving POV watches Ichabod and Masbath as they ride to the cave, following...
  EXPRESSION: Suspicious
- CHARACTER: Narrator
  LINE: Ichabod and Young Masbath dismount, tying their horses, then heading to the cave. They arrive at the cave door. Ichabod hesitantly knocks.
  EXPRESSION: Hesitant

::SCENE::
LOCATION: INT. Cave Home
MOOD: Creepy, Disturbing
CHARACTERS: Ichabod, Young Masbath, Crone
BACKGROUND_IMAGE: int_cave_home_day.png
BACKGROUND_EDIT: "Daytime, interior of a cave, walls hung with skins and skeletons."

::SCRIPT::
- CHARACTER: Narrator
  LINE: The door is ajar... Ichabod and Young Masbath step in... Walls are hung with skins and skeletons. Across the cave, a crone sits facing away, motionless.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Ichabod and Young Masbath look to each other, fearful.
  EXPRESSION: Fearful
- CHARACTER: Ichabod
  LINE: Pardon my intrusion...
  EXPRESSION: Apologetic
- CHARACTER: Narrator
  LINE: The Crone, with gray hair and gray features, sits disinterested. Behind, Ichabod edges slowly forward...
  EXPRESSION: Disinterested
- CHARACTER: Crone
  LINE: You are from the Hollow?
  EXPRESSION: Neutral
- CHARACTER: Ichabod
  LINE: In a way, yes. I, um...
  EXPRESSION: Distracted
- CHARACTER: Narrator
  LINE: Ichabod is distracted by gourd bowls of dead insects, leaves and acorns... knives, scissors and yellowed bones.
  EXPRESSION: Disturbed
- CHARACTER: Ichabod
  LINE: I should like to say... um... I make no assumptions about your occupation, no, your ways, witch -- which -- which are nothing to me... um... whatever you are, each to his own -- um --
  EXPRESSION: Flustered
- CHARACTER: Narrator
  LINE: The Crone places something on a table beside her... a dead bird, a bright red cardinal.
  EXPRESSION: Ominous
- CHARACTER: Narrator
  LINE: Ichabod backs away, but Masbath comes to stand beside him.
  EXPRESSION: Supportive
- CHARACTER: Young Masbath
  LINE: Do you know of the Horseman, ma'am... ? The Hessian.
  EXPRESSION: Inquisitive
- CHARACTER: Crone
  LINE: (draws her finger across her neck)
  EXPRESSION: Menacing
- CHARACTER: Young Masbath
  LINE: That'll be him, miss.
  EXPRESSION: Resigned
- CHARACTER: Narrator
  LINE: Around her neck is a cord on which is threaded a carved stone, a mystic bauble. Ichabod notices it. The Crone stands, faces them, tall ... points to Ichabod.
  EXPRESSION: Noticing
- CHARACTER: Crone
  LINE: You, follow with me. Go out, child. Keep away. No matter what you hear, keep away.
  EXPRESSION: Commanding
- CHARACTER: Narrator
  LINE: She takes a candle and heads deeper into the cave...
  EXPRESSION: null

::SCENE::
LOCATION: INT. Cave Home, Lower Cave
MOOD: Terrifying, Mysterious
CHARACTERS: Crone, Ichabod
BACKGROUND_IMAGE: int_cave_home_lower_cave_day.png
BACKGROUND_EDIT: "Daytime, lower cave passage, Ichabod following the Crone."

::SCRIPT::
- CHARACTER: Narrator
  LINE: The Crone enters through a passage, Ichabod follows, terrified, bent under the low ceiling.
  EXPRESSION: Terrified
- CHARACTER: Ichabod
  LINE: Um... what might he hear that he must keep away from... ?
  EXPRESSION: Nervous
- CHARACTER: Crone
  LINE: Sit there.
  EXPRESSION: Directing
- CHARACTER: Narrator
  LINE: Ichabod sits on a crooked stool. The Crone kneels with her back to him, grasps two metal cuffs with chains attached, slides these onto her wrists, testing them...
  EXPRESSION: null
- CHARACTER: Crone
  LINE: He rides, to the Hollow and back. I hear him. I smell the blood on him.
  EXPRESSION: Foreboding
- CHARACTER: Ichabod
  LINE: Do... do you? Well... I'm here to find him and... er... make him stop...
  EXPRESSION: Hesitant
- CHARACTER: Crone
  LINE: You want to see into the netherworld ... I can show you...
  EXPRESSION: Inviting
- CHARACTER: Narrator
  LINE: The Crone gathers straw in a pile on the floor, then gathers bowls, putting grass and powder on the pi
  EXPRESSION: null

::SCENE::
LOCATION: Cave Home - Lower Cave
MOOD: Dark
CHARACTERS: Narrator, Crone, Ichabod
BACKGROUND_IMAGE: cave_home_lower_cave_day.png
BACKGROUND_EDIT: "Dimly lit cave interior, cluttered with strange items"

::SCRIPT::
- CHARACTER: Narrator
  LINE: le, WITHERING over it. She takes a JAR from a table.
  EXPRESSION: null
- CHARACTER: Ichabod
  LINE: What... what are you doing?
  EXPRESSION: Confused
- CHARACTER: Narrator
  LINE: The Crone shakes one jar, pulls the lid off and upends it. A BABY BAT squirms, dazed. The Crone grips the bat, uses a knife to cut off its head, soaks the straw with blood.
  EXPRESSION: null
- CHARACTER: Crone
  LINE: Do not move or speak. When the other comes, I will hold him.
  EXPRESSION: Stern
- CHARACTER: Narrator
  LINE: Using her candle, the Crone lights the straw pile.
  EXPRESSION: null
- CHARACTER: Ichabod
  LINE: The other... ?
  EXPRESSION: Curious
- CHARACTER: Crone
  LINE: Silence. He comes now.
  EXPRESSION: Grim
- CHARACTER: Narrator
  LINE: Ichabod would like to leave now.
  EXPRESSION: Fearful

::PATHS::
- CHOICE: "Wait for the 'other'"
  TARGET: ext_cave_home_day
  STATE_CHANGE: fear = +1
  CONDITION: null

::SCENE::
LOCATION: Cave Home - Exterior
MOOD: Eerie
CHARACTERS: Narrator, Young Masbath
BACKGROUND_IMAGE: cave_home_exterior_day.png
BACKGROUND_EDIT: "Exterior of a cave dwelling, windy day"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Young Masbath waits. WIND picks up, kicking leaves, sending them in swirls. Masbath holds himself against the chill.
  EXPRESSION: Cold

::PATHS::
- CHOICE: "Continue waiting"
  TARGET: int_cave_home_lower_cave_day_2
  STATE_CHANGE: none
  CONDITION: null

::SCENE::
LOCATION: Cave Home - Lower Cave
MOOD: Foreboding
CHARACTERS: Narrator, Crone, Ichabod
BACKGROUND_IMAGE: cave_home_lower_cave_day_2.png
BACKGROUND_EDIT: "Dimly lit cave interior, wind howling"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The Crone slumps forward to the floor, suddenly immobile, still with her back to Ichabod. WIND HOWLS through a hole/window.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Ichabod looks around, uncertain, stands.
  EXPRESSION: Uncertain
- CHARACTER: Ichabod
  LINE: Excuse me... ma'am... ?
  EXPRESSION: Hesitant
- CHARACTER: Narrator
  LINE: The Crone remains motionless. The WIND intensifies. Candles blow out.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Ichabod inches closer...
  EXPRESSION: Cautious
- CHARACTER: Ichabod
  LINE: Do you hear me... ?
  EXPRESSION: Anxious

::PATHS::
- CHOICE: "Approach the Crone"
  TARGET: int_cave_home_lower_cave_day_3
  STATE_CHANGE: fear = +2
  CONDITION: null

::SCENE::
LOCATION: Cave Home - Lower Cave
MOOD: Terrifying
CHARACTERS: Narrator, Creature/Crone, Ichabod
BACKGROUND_IMAGE: cave_home_lower_cave_day_3.png
BACKGROUND_EDIT: "Cave interior, chaotic with sudden monstrous transformation"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The Crone suddenly jumps erect, spinning -- a half-human, half-demon CREATURE, black clawed hands reaching...
  EXPRESSION: Shocked
- CHARACTER: Ichabod
  LINE: Ichabod cries out, leaping backward...
  EXPRESSION: Terrified
- CHARACTER: Narrator
  LINE: CHAINS on the restraining CUFFS around the creature's hands go taut, yanking the creature back.
  EXPRESSION: null
- CHARACTER: Ichabod
  LINE: Ichabod KNOCKS over a table of bones, hits the floor. The creature is chained, but still wants Ichabod. It SHRIEKS.
  EXPRESSION: Panicked
- CHARACTER: Narrator
  LINE: The creature's face still seethes from transformation.
  EXPRESSION: Monstrous
- CHARACTER: Creature/Crone
  LINE: You seek the warrior bathed in blood ... the Headless Horseman...
  EXPRESSION: Menacing
- CHARACTER: Ichabod
  LINE: Ichabod scrambles back as far as possible. The creature claws the rock floor, yearning.
  EXPRESSION: Desperate
- CHARACTER: Creature/Crone
  LINE: Follow the Indian trail to where the sun dies. Follow to the Tree of the Dead...
  EXPRESSION: Cryptic
- CHARACTER: Narrator
  LINE: The creature yanks, testing the chains. Behind, the BOLT holding the chains slips... the WALL CRACKS a little.
  EXPRESSION: Ominous
- CHARACTER: Creature/Crone
  LINE: Climb down to the Horseman's resting place. Do you hear... ?
  EXPRESSION: Demanding
- CHARACTER: Narrator
  LINE: Ichabod nods, quaking, aghast. He glances to the exit.
  EXPRESSION: Trembling
- CHARACTER: Narrator
  LINE: The chain bolt gives more... coming loose...
  EXPRESSION: Critical
- CHARACTER: Ichabod
  LINE: Ichabod flees toward the door. The creature HOWLS, leaping... the chain bolt BREAKS...
  EXPRESSION: Frantic
- CHARACTER: Ichabod
  LINE: Ichabod cries out as he is TACKLED to the floor...
  EXPRESSION: Overwhelmed

::PATHS::
- CHOICE: "Escape the cave"
  TARGET: int_cave_home_lower_cave_day_4
  STATE_CHANGE: fear = +3, adrenaline = +2
  CONDITION: null

::SCENE::
LOCATION: Cave Home - Lower Cave
MOOD: Relief then Urgency
CHARACTERS: Narrator, Crone, Ichabod
BACKGROUND_IMAGE: cave_home_lower_cave_day_4.png
BACKGROUND_EDIT: "Cave interior, after a struggle"

::SCRIPT::
- CHARACTER: Narrator
  LINE: It is only the CRONE lying on him; she has returned to human form, semiconscious. Ichabod desperately shoves her off...
  EXPRESSION: Recovering

::PATHS::
- CHOICE: "Flee the cave"
  TARGET: ext_cave_home_exterior_day_2
  STATE_CHANGE: fear = -1
  CONDITION: null

::SCENE::
LOCATION: Cave Home - Exterior
MOOD: Hasty Departure
CHARACTERS: Narrator, Ichabod, Young Masbath
BACKGROUND_IMAGE: cave_home_exterior_day_2.png
BACKGROUND_EDIT: "Exterior of the cave, Ichabod rushing out"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Ichabod sprints out from the cave, past Young Masbath.
  EXPRESSION: Rushed
- CHARACTER: Ichabod
  LINE: We are leaving.
  EXPRESSION: Urgent
- CHARACTER: Young Masbath
  LINE: What happened?
  EXPRESSION: Concerned
- CHARACTER: Ichabod
  LINE: We are leaving now.
  EXPRESSION: Determined
- CHARACTER: Narrator
  LINE: Ichabod scrambles onto Gunpowder, riding, glancing back. Young Masbath follows.
  EXPRESSION: Fleeing

::PATHS::
- CHOICE: "Ride away quickly"
  TARGET: western_woods_area_two_farther_on_later_day
  STATE_CHANGE: fear = -2
  CONDITION: null

::SCENE::
LOCATION: Western Woods Area Two, Farther On
MOOD: Focused Determination
CHARACTERS: Narrator, Ichabod, Young Masbath
BACKGROUND_IMAGE: western_woods_area_two_farther_on_later_day.png
BACKGROUND_EDIT: "Riding through woods, afternoon"

::SCRIPT::
- CHARACTER: Ichabod
  LINE: "Take the Indian trail... To the Tree of the Dead... "
  EXPRESSION: Recalling
- CHARACTER: Young Masbath
  LINE: How will we recognize it?
  EXPRESSION: Questioning
- CHARACTER: Ichabod
  LINE: Without difficulty I rather fear. And "Climb down to the Horseman's resting place... " she said.
  EXPRESSION: Resigned
- CHARACTER: Young Masbath
  LINE: His... camp?
  EXPRESSION: Inquiring
- CHARACTER: Ichabod
  LINE: His grave.
  EXPRESSION: Grave
- CHARACTER: Narrator
  LINE: A SNAPPING BRANCH is HEARD. Ichabod turns to look back...
  EXPRESSION: Alert
- CHARACTER: Ichabod
  LINE: Quicken pace.
  EXPRESSION: Urgent
  LINE: Ichabod rides faster. Young Masbath keeps up...
  EXPRESSION: Pursued
- CHARACTER: Narrator
  LINE: FARTHER ON, they charge over a hill. Ichabod halts Gunpowder, climbs clumsily off, handing the reins to Masbath.
  EXPRESSION: Strategic
- CHARACTER: Ichabod
  LINE: Ride on.
  EXPRESSION: Command
- CHARACTER: Narrator
  LINE: Young Masbath obeys. Ichabod takes out his pistol and wades into forest growth, backtracking...
  EXPRESSION: Stealthy

::PATHS::
- CHOICE: "Investigate the sound"
  TARGET: western_woods_area_three_day
  STATE_CHANGE: caution = +1
  CONDITION: null

::SCENE::
LOCATION: Western Woods Area Three
MOOD: Tense Confrontation
CHARACTERS: Narrator, Ichabod, Figure in Gray Cloak
BACKGROUND_IMAGE: western_woods_area_three_day.png
BACKGROUND_EDIT: "Deep woods, Ichabod moving stealthily"

::SCRIPT::
- CHARACTER: Narrator
  LINE: INSIDE THE FOREST, Ichabod moves through UNDERBRUSH, keeping low. A HORSE is HEARD SNORTING.
  EXPRESSION: Vigilant
- CHARACTER: Narrator
  LINE: Ichabod forges on, pushes through branches, fearful...
  EXPRESSION: Apprehensive
- CHARACTER: Narrator
  LINE: He comes up behind a FIGURE IN A GRAY CLOAK on horseback, raising his pistol, cocking the hammer...
  EXPRESSION: Confrontational
- CHARACTER: Ichabod
  LINE: Halt and turn! I have a pistol aimed.
  EXPRESSION: Authoritative

::PATHS::
- CHOICE: "Reveal identity"
  TARGET: western_woods_area_three_day_2
  STATE_CHANGE: tension = +1
  CONDITION: null

::SCENE::
LOCATION: Western Woods Area Three
MOOD: Shock and Relief
CHARACTERS: Narrator, Ichabod, Katrina
BACKGROUND_IMAGE: western_woods_area_three_day_2.png
BACKGROUND_EDIT: "Woods clearing, Ichabod lowers his pistol"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The FIGURE stops, pushes off the cloak hood. It is Katrina.
  EXPRESSION: Surprised
- CHARACTER: Katrina
  LINE: It is me.
  EXPRESSION: Calm
- CHARACTER: Ichabod
  LINE: Katrina... I might have killed you. Why have you come?
  EXPRESSION: Shaken
- CHARACTER: Katrina
  LINE: Because no one else would go with you.
  EXPRESSION: Steadfast
- CHARACTER: Narrator
  LINE: She smiles a little. Ichabod is heartened.
  EXPRESSION: Hopeful
- CHARACTER: Ichabod
  LINE: I am now twice the man.
  EXPRESSION: Confident
- CHARACTER: Narrator
  LINE: Ichabod takes her hand.
  EXPRESSION: Affectionate
- CHARACTER: Ichabod
  LINE: It is your white magic.
  EXPRESSION: Grateful
- CHARACTER: Narrator
  LINE: She is about to turn this moment into a kiss -- but...
  EXPRESSION: Interrupted
- CHARACTER: Young Masbath (O.S.)
  LINE: Pardon my intrusion...
  EXPRESSION: Apologetic
- CHARACTER: Narrator
  LINE: Ichabod and Katrina look to see Masbath has backtracked.
  EXPRESSION: Curious
- CHARACTER: Young Masbath
  LINE: I think you'd better come and look at this...
  EXPRESSION: Concerned

::PATHS::
- CHOICE: "Follow Young Masbath"
  TARGET: western_woods_tree_of_the_dead_dusk
  STATE_CHANGE: curiosity = +1
  CONDITION: null

::SCENE::
LOCATION: Western Woods, Tree of the Dead
MOOD: Awe and Horror
CHARACTERS: Narrator, Ichabod, Masbath, Katrina
BACKGROUND_IMAGE: western_woods_tree_of_the_dead_dusk.png
BACKGROUND_EDIT: "Clearing with a massive, gnarled tree at dusk"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Ichabod, Masbath and Katrina come into a clearing, slowing their horses... looking up in wonder at...
  EXPRESSION: Awestruck
- CHARACTER: Narrator
  LINE: The monstrously huge TREE OF THE DEAD, at the clearing's center. Its branches reach far and wide, knotted and gross, like agony captured in wood sculpture.
  EXPRESSION: Horrified
- CHARACTER: Young Masbath
  LINE: The Tree of the Dead.
  EXPRESSION: Amazed
- CHARACTER: Katrina
  LINE: It does announce itself.
  EXPRESSION: Understated
- CHARACTER: Narrator
  LINE: Ichabod dismounts, crossing a line beyond which grass and weeds will not grow. Young Masbath and Katrina dismount behind. They all walk toward the tree...
  EXPRESSION: Solemn
- CHARACTER: Narrator
  LINE: Ichabod stares up into the endless, dead canopy of branches.
  EXPRESSION: Contemplative
- CHARACTER: Narrator
  LINE: There's a VERTICAL WOUND in the bark, like a terrible suture, now healed and scarred. Ichabod approaches...
  EXPRESSION: Intrigued
- CHARACTER: Narrator
  LINE: He feels the mushy scar, picking at its scabs till sap begins to run.
  EXPRESSION: Determined
- CHARACTER: Narrator
  LINE: Red Sap. Ichabod fingers it, sniffs it.
  EXPRESSION: Suspicious
- CHARACTER: Ichabod
  LINE: Blood.
  EXPRESSION: Horrified
- CHARACTER: Katrina
  LINE: The tree bleeds? How can it be?
  EXPRESSION: Disbelieving
- CHARACTER: Narrator
  LINE: Ichabod goes to where Katrina and Masbath wait with the horses, digs in a saddle bag for a hand AXE.
  EXPRESSION: Purposeful
- CHARACTER: Young Masbath
  LINE: What is it?
  EXPRESSION: Inquisitive
- CHARACTER: Ichabod
  LINE: Stay here.
  EXPRESSION: Firm
- CHARACTER: Narrator
  LINE: At the trunk, Ichabod thumps the flat end of the axe against the suture. It sounds hollow. He begins to CHOP...
  EXPRESSION: Resolute
- CHARACTER: Narrator
  LINE: He CHOPS into the suture... pulls away loose bark. The tree drips more blood and a goo. Ichabod uses both hands on the axe to hack at the festering suture.
  EXPRESSION: Frenzied
- CHARACTER: Katrina
  LINE: What are you doing?
  EXPRESSION: Alarmed
- CHARACTER: Ichabod
  LINE: Just... keep where you are.
  EXPRESSION: Distracted
- CHARACTER: Narrator
  LINE: Young Masbath moves closer. Ichabod keeps CHOPPING, then grips a large, loose flap, trying to pull it away. It's not easy. Ichabod struggles.
  EXPRESSION: Straining
- CHARACTER: Narrator
  LINE: Katrina follows Young Masbath's slow advance.
  EXPRESSION: Concerned
- CHARACTER: Narrator
  LINE: Ichabod's pulling -- the flap suddenly gives, revealing a blood-soaked, wide-eyed, gap-mouthed HUMAN HEAD.
  EXPRESSION: Shocked
- CHARACTER: Ichabod
  LINE: Ichabod recoils. Behind him, Katrina stifles a scream.
  EXPRESSION: Horrified
- CHARACTER: Narrator
  LINE: Ichabod backs off, back of his hand to his mouth.
  EXPRESSION: Nauseated
- CHARACTER: Narrator
  LINE: It is PHILIPSE'S HEAD, hanging off the trunk flap, held by roots grown around and into the flesh.
  EXPRESSION: Gruesome
- CHARACTER: Narrator
  LINE: FOUR other SEVERED, DECAYING HEADS are held by ingrown roots within the dewy innards. One of the heads is Jonathan Masbath's. Before Young Masbath sees it, Katrina hides his face in her bosom and comforts him.
  EXPRESSION: Horrific
- CHARACTER: Katrina
  LINE: My God...
  EXPRESSION: Aghast
- CHARACTER: Ichabod
  LINE: He... he tries to take the heads back with him. They will not pass...
  EXPRESSION: Disturbed
- CHARACTER: Katrina
  LINE: We must leave this place.
  EXPRESSION: Urgent
- CHARACTER: Narrator
  LINE: Ichabod looks to the branches towering above.
  EXPRESSION: Contemplative
- CHARACTER: Ichabod
  LINE: This is... a gateway, between two worlds...
  EXPRESSION: Mystified
- CHARACTER: Narrator
  LINE: Ichabod studies the ground, circling the trunk... Around the other side, Ichabod gets to his knees...
  EXPRESSION: Searching
- CHARACTER: Narrator
  LINE: He's found the HORSEMAN'S SWORD: the grave marker, jutting out from the ground, rusted twenty years' worth, gripped by the tree trunk and vines.
  EXPRESSION: Determined
- CHARACTER: Ichabod
  LINE: Climb down to the Horseman's resting place...
  EXPRESSION: Directing
- CHARACTER: Ichabod
  LINE: Bring the shovel.
  EXPRESSION: Demanding
- CHARACTER: Narrator
  LINE: Now he sees Katrina hugging the boy.
  EXPRESSION: Observant
- CHARACTER: Ichabod
  LINE: Forgive me... I...
  EXPRESSION: Apologetic
- CHARACTER: Young Masbath
  LINE: Yes, sir -- the shovel... Two shovels and the rifle, I suggest.
  EXPRESSION: Brave

::PATHS::
- CHOICE: "Dig for the sword"
  TARGET: western_woods_tree_of_the_dead_dusk_2
  STATE_CHANGE: discovery = +1, fear = +2
  CONDITION: null

::SCENE::
LOCATION: Western Woods, Tree of the Dead
MOOD: Grave Discovery
CHARACTERS: Narrator, Young Masbath, Ichabod, Katrina
BACKGROUND_IMAGE: western_woods_tree_of_the_dead_dusk_2.png
BACKGROUND_EDIT: "Dusk in the clearing, lantern light, digging begins"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Lantern light.
  EXPRESSION: null
- CHARACTER: Young Masbath
  LINE: Young Masbath's crouched, rifle across his knees. He watches the tree, looking up...
  EXPRESSION: Vigilant
- CHARACTER: Narrator
  LINE: High branches swarm with BATS.
  EXPRESSION: Ominous
- CHARACTER: Narrator
  LINE: Behind Masbath, Ichabod and Katrina dig up the SHALLOW GRAVE.
  EXPRESSION: Laborious
- CHARACTER: Katrina
  LINE: This ground has been disturbed, the soil is loose.
  EXPRESSION: Observant
- CHARACTER: Narrator
  LINE: Ichabod throws down his Shovel.
  EXPRESSION: Frustrated
- CHARACTER: Narrator
  LINE: Young Masbath comes to the grave. Ichabod pulls at thick BURLAP CLOTH heavy with dirt... straining as it comes away...
  EXPRESSION: Straining
- CHARACTER: Narrator
  LINE: Ichabod drops the burlap, looking down, disbelieving...
  EXPRESSION: Shocked
- CHARACTER: Ichabod
  LINE: Look... !
  EXPRESSION: Astonished
- CHARACTER: Narrator
  LINE: WE SEE: Roots have gripped th
  EXPRESSION: null

::PATHS::
- CHOICE: "Examine the burlap"
  TARGET: end
  STATE_CHANGE: horror = +3
  CONDITION: null

::SCENE::
LOCATION: Graveyard
MOOD: Mystery
CHARACTERS: Narrator, Katrina, Ichabod
BACKGROUND_IMAGE: graveyard.png
BACKGROUND_EDIT: "Night, a disturbed grave, skeletal remains"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The HORSEMAN'S BONES and tattered uniform. The skeleton is all there -- except the skull.
  EXPRESSION: null
- CHARACTER: Katrina
  LINE: The skull is gone. What does it mean?
  EXPRESSION: Confused
- CHARACTER: Ichabod
  LINE: It means, my dear Miss Van Tassel, it means -- yes! What exactly does it mean? -- It means, unless I am mistaken... it definitely means something -- what that something is, only time will tell! But I sense that we are very close to the answer here, if only we had one more clue...
  EXPRESSION: Energized
- CHARACTER: Narrator
  LINE: Ichabod is unaware that the ground is writhing around him.
  EXPRESSION: null
- CHARACTER: Katrina
  LINE: Ichabod... !
  EXPRESSION: Afraid
- CHARACTER: Narrator
  LINE: Ichabod turns, looks... Katrina and Young Masbath back away, because... the ROOTS in the grave are ALIVE, entwining around remains.
  EXPRESSION: null
- CHARACTER: Ichabod
  LINE: Ichabod spins to the twisted tree...
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The vertical SUTURE SEETHES, pulling inward... sucking Philipse's head back in and closing, bubbling. Ichabod bounds over the grave dirt pile, hastening Katrina and Young Masbath along as he flees across the field.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: At the tree, the suture swells. Ichabod, Katrina and Young Masbath pass where their freaking horses are tied to a fallen trunk, heading for cover.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: A RUMBLING is HEARD from the tree. It's wound suddenly BURSTS wide, spitting smoldering cinders.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: At the tree line, Ichabod, Katrina and Young Masbath take cover, looking back.
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue fleeing"
  TARGET: western_woods_tree_effect
  STATE_CHANGE: fear = +2
  CONDITION: null

::SCENE::
LOCATION: Western Woods Tree of the Dead (Effect)
MOOD: Ominous
CHARACTERS: Narrator
BACKGROUND_IMAGE: tree_of_the_dead_effect.png
BACKGROUND_EDIT: "Dusk, a glowing tree wound"

::SCRIPT::
- CHARACTER: Narrator
  LINE: From the tree wound, a glow BRIGHTENS... till suddenly the Headless Horseman and Daredevil EXPLODE into existence... They hit the ground running.
  EXPRESSION: null

::PATHS::
- CHOICE: "Observe the Horseman"
  TARGET: western_woods_tree
  STATE_CHANGE: fear = +3
  CONDITION: null

::SCENE::
LOCATION: Western Woods Tree of the Dead
MOOD: Menacing
CHARACTERS: Narrator, Ichabod, Young Masbath, Headless Horseman
BACKGROUND_IMAGE: western_woods_tree.png
BACKGROUND_EDIT: "Dusk, trees silhouetted, lightning striking"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Ichabod watches the Horseman ride away, bolts of LIGHTING STRIKING the GROUND BEHIND. The Horseman disappears into the forest.
  EXPRESSION: null
- CHARACTER: Ichabod
  LINE: Did you see that?! Take Katrina home!
  EXPRESSION: Astonished
- CHARACTER: Narrator
  LINE: Ichabod runs toward the horses.
  EXPRESSION: null
- CHARACTER: Young Masbath
  LINE: Constable!
  EXPRESSION: Concerned

::PATHS::
- CHOICE: "Chase the Horseman"
  TARGET: western_woods_area_two
  STATE_CHANGE: determination = +1, fear = +2
  CONDITION: null

::SCENE::
LOCATION: Western Woods Area Two
MOOD: Urgent
CHARACTERS: Narrator, Headless Horseman
BACKGROUND_IMAGE: western_woods_area_two.png
BACKGROUND_EDIT: "Night, forest, horse galloping"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The Horseman rips past on Daredevil...
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue pursuit"
  TARGET: western_woods_area_three
  STATE_CHANGE: urgency = +1
  CONDITION: null

::SCENE::
LOCATION: Western Woods Area Three
MOOD: Desperate
CHARACTERS: Narrator, Ichabod
BACKGROUND_IMAGE: western_woods_area_three.png
BACKGROUND_EDIT: "Night, forest, Ichabod on horseback"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Ichabod rides as fast as Gunpowder is able...
  EXPRESSION: null

::PATHS::
- CHOICE: "Keep up the chase"
  TARGET: western_woods_area_two_farther
  STATE_CHANGE: stamina = -1
  CONDITION: null

::SCENE::
LOCATION: Western Woods Area Two, Farther On
MOOD: Tense
CHARACTERS: Narrator, Ichabod
BACKGROUND_IMAGE: western_woods_area_two_farther.png
BACKGROUND_EDIT: "Night, forest, trees bending"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Trees are silhouetted against the sky. As Daredevil's HOOFBEATS get LOUDER, branches bend like arms and fingers yearning to touch. As HOOFBEATS ROAR PAST, the trees relax.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Ichabod ducks under foliage as he pursues. He sees... Through the forest ahead: the SKY'S LIT UP. Distant fire.
  EXPRESSION: null

::PATHS::
- CHOICE: "Investigate the light"
  TARGET: western_woods_cave_home
  STATE_CHANGE: curiosity = +1
  CONDITION: null

::SCENE::
LOCATION: Western Woods, Cave Home
MOOD: Horrifying
CHARACTERS: Narrator, Ichabod, Gunpowder, Crone
BACKGROUND_IMAGE: western_woods_cave_home.png
BACKGROUND_EDIT: "Night, cave entrance spewing flame, smoke"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The Crone's CAVE vomits FLAME. Ichabod arrives on Gunpowder, horrified, struggling for control as Gunpowder rears, trying to see through BLACK SMOKE...
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Embers swirl everywhere. Ichabod dismounts, moving closer to the cave ... suddenly he SLIPS... Ichabod falls down a bloody rock, landing very close to the CRONE'S HEADLESS BODY. Ichabod recoils, crawling away, looking to the carnage in terror...
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The corpse lies near the cave entrance. The jagged skin of the neck wound still bleeds. The ground and dead leaves around the corpse are thick with BLOOD. Ichabod crawls back to the Crone, terrified... because he has seen a CLUE. The cord around the Crone's neck has been cut and the Carved Bauble is missing (along with the Crone's head).
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Ichabod hears a Horse neighing in the trees... and the sound of the horse crashing through the undergrowth, departing... but he can see nothing.
  EXPRESSION: null

::PATHS::
- CHOICE: "Search for clues"
  TARGET: forest_patrol
  STATE_CHANGE: discovery = +1, fear = +3
  CONDITION: null

::SCENE::
LOCATION: Forest
MOOD: Anxious
CHARACTERS: Narrator, Brom, Theodore, Glen
BACKGROUND_IMAGE: forest_patrol.png
BACKGROUND_EDIT: "Night, trees, sounds of a horse"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Brom, Theodore and Glen are on patrol -- Brom with his new rifle. They can hear the same horse crashing invisibly through branches, the sound of hooves. They can't tell where the sound is coming from. They look around nervously.
  EXPRESSION: null
- CHARACTER: Brom
  LINE: Split up! He won't get away.
  EXPRESSION: Determined
- CHARACTER: Narrator
  LINE: The three of them gallop off in three directions. When they clear the frame there is a sound of deep rumbling, the sound we heard before Jonathan Masbath was murdered.
  EXPRESSION: null

::PATHS::
- CHOICE: "Follow the sound"
  TARGET: killians_home_kitchen_night_1
  STATE_CHANGE: suspense = +2
  CONDITION: null

::SCENE::
LOCATION: Killian's Home, Kitchen
MOOD: Uneasy
CHARACTERS: Narrator, Killian, Thomas, Beth
BACKGROUND_IMAGE: killians_home_kitchen.png
BACKGROUND_EDIT: "Night, small home, remnants of supper"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Small home. Killian, Thomas and BETH, Killian's wife, have finished supper. Beth clears plates as Killian picks his teeth with a knife.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The same rumbling sound is faintly heard. The glasses on the table shiver audibly. Killian notices. Then the phenomenon stops. Killian continues picking his teeth.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Thomas gets down from his chair. He goes to the fireplace to light a tallow wick, which he takes to the next room.
  EXPRESSION: null

::PATHS::
- CHOICE: "Follow Thomas"
  TARGET: killians_home_white_room_night_1
  STATE_CHANGE: curiosity = +1
  CONDITION: null

::SCENE::
LOCATION: Killian's Home, White Room
MOOD: Playful then Tense
CHARACTERS: Narrator, Thomas
BACKGROUND_IMAGE: killians_home_white_room.png
BACKGROUND_EDIT: "Night, room with a fireplace, magic lantern"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Thomas plops on the floor and lights his MAGIC LANTERN: a lantern with an outer sleeve of glass painted with SILHOUETTES of LIONS and MONSTERS. Thomas turns the lantern and looks to the walls where the creatures' SHADOWS are cast. He roars for them, imagining them real and having a grand time.
  EXPRESSION: null

::PATHS::
- CHOICE: "Return to the kitchen"
  TARGET: killians_home_kitchen_night_2
  STATE_CHANGE: playfulness = +1
  CONDITION: null

::SCENE::
LOCATION: Killian's Home, Kitchen
MOOD: Domestic then Ominous
CHARACTERS: Narrator, Beth, Killian
BACKGROUND_IMAGE: killians_home_kitchen.png
BACKGROUND_EDIT: "Night, kitchen"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Beth comes for dishes.
  EXPRESSION: null
- CHARACTER: Beth
  LINE: Don't pick teeth. You teach Thomas bad habits.
  EXPRESSION: Playful
- CHARACTER: Killian
  LINE: I am a bad habit. There's nothing for it.
  EXPRESSION: Playful
- CHARACTER: Beth
  LINE: Oh, isn't there.
  EXPRESSION: Affectionate

::PATHS::
- CHOICE: "Continue domesticity"
  TARGET: forest_night_brom
  STATE_CHANGE: intimacy = +1
  CONDITION: null

::SCENE::
LOCATION: Forest
MOOD: Foreboding
CHARACTERS: Narrator, Brom
BACKGROUND_IMAGE: forest_night_brom.png
BACKGROUND_EDIT: "Night, forest, horse, thunder"

::SCRIPT::
- CHARACTER: Narrator
  LINE: A black horse runs, hooves pounding the ground. THUNDER is HEARD. The horse stops... it is Brom's horse, with Brom riding. Brom looks skyward.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: All around, the WIND HALTS. A DEAD SILENCE falls. Distant HOOFBEATS can be HEARD. Brom takes his long rifle from his shoulder, rides...
  EXPRESSION: null

::PATHS::
- CHOICE: "Confront the threat"
  TARGET: killians_home_kitchen_night_3
  STATE_CHANGE: tension = +3
  CONDITION: null

::SCENE::
LOCATION: Killian's Home, Kitchen
MOOD: Supernatural
CHARACTERS: Narrator, Killian
BACKGROUND_IMAGE: killians_home_kitchen.png
BACKGROUND_EDIT: "Night, kitchen, fireplace pulsing"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Behind Killian, MANTELPIECE STONES pulse, breathing. Demonic faces form, then disappear. WIND HOWLS.
  EXPRESSION: null

::PATHS::
- CHOICE: "Observe the phenomenon"
  TARGET: killians_home_white_room_night_2
  STATE_CHANGE: supernatural_fear = +2
  CONDITION: null

::SCENE::
LOCATION: Killian's Home, White Room
MOOD: Unsettling
CHARACTERS: Narrator, Thomas, Beth
BACKGROUND_IMAGE: killians_home_white_room.png
BACKGROUND_EDIT: "Night, magic lantern casting shadows, wind ferocity"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Thomas continues his fun, shadow animals circling him. Beth enters, looking at Thomas, smiling. The magic lantern suddenly stops spinning. Shadow creatures freeze.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Beth looks up, noticing the FEROCITY of the WIND. The smile leaves her face.
  EXPRESSION: null

::PATHS::
- CHOICE: "Investigate the wind"
  TARGET: killians_home_kitchen_night_4
  STATE_CHANGE: fear = +2
  CONDITION: null

::SCENE::
LOCATION: Killian's Home, Kitchen
MOOD: Escalating Danger
CHARACTERS: Narrator, Killian, Beth
BACKGROUND_IMAGE: killians_home_kitchen.png
BACKGROUND_EDIT: "Night, house creaking, wind ceasing"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The ENTIRE HOUSE CREAKS. Killian stands, looking up. The HOUSE CREAKS again, then suddenly the WIND CEASES. Silence.
  EXPRESSION: null
- CHARACTER: Killian
  LINE: Beth...
  EXPRESSION: Concerned

::PATHS::
- CHOICE: "Call for Beth"
  TARGET: killians_home_white_room_night_3
  STATE_CHANGE: suspense = +2
  CONDITION: null

::SCENE::
LOCATION: Killian's Home, White Room
MOOD: Fearful
CHARACTERS: Narrator, Beth, Thomas
BACKGROUND_IMAGE: killians_home_white_room.png
BACKGROUND_EDIT: "Night, Beth holding Thomas, magic lantern spinning"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Beth picks up Thomas. The magic lantern shadow creatures begin spinning anew, quickly, around and around.
  EXPRESSION: null

::PATHS::
- CHOICE: "Wait for Killian"
  TARGET: killians_home_kitchen_night_5
  STATE_CHANGE: anticipation = +1
  CONDITION: null

::SCENE::
LOCATION: Killian's Home, Kitchen
MOOD: Violent Attack
CHARACTERS: Narrator, Killian, Beth, Headless Horseman
BACKGROUND_IMAGE: killians_home_kitchen.png
BACKGROUND_EDIT: "Night, kitchen, fire flaring, door splintering"

::SCRIPT::
- CHARACTER: Narrator
  LINE: With a ROAR, the fire flares. Killian looks... In the leaping flames he seems to see -- as we also seem to see -- the ILLUSION OF DEMONIC FACES molded out of flames. Behind Killian, the DOOR SPLINTERS INWARD. The Horseman steps in, a battle axe in each hand. WIND BLASTS...
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The DOOR to the other room SLAMS. Killian grabs a chair and HURLS it... The Horseman swings, SMASHING it aside.
  EXPRESSION: null
- CHARACTER: Killian
  LINE: Beth... run!
  EXPRESSION: Terrified
- CHARACTER: Narrator
  LINE: Get out!
  EXPRESSION: null

::PATHS::
- CHOICE: "Defend Beth"
  TARGET: killians_home_white_room_night_4
  STATE_CHANGE: bravery = +1, sacrifice = +1
  CONDITION: null

::SCENE::
LOCATION: Killian's Home, White Room
MOOD: Desperate Escape
CHARACTERS: Narrator, Beth, Thomas, Killian (O.S.)
BACKGROUND_IMAGE: killians_home_white_room.png
BACKGROUND_EDIT: "Night, Beth and Thomas by a closed door"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Beth holds Thomas as she back away from the closed door.
  EXPRESSION: null
- CHARACTER: Killian
  LINE: (from kitchen) Get out!
  EXPRESSION: Shouting

::PATHS::
- CHOICE: "Hide"
  TARGET: killians_home_kitchen_night_6
  STATE_CHANGE: desperation = +2
  CONDITION: null

::SCENE::
LOCATION: Killian's Home, Kitchen
MOOD: Brutal Combat
CHARACTERS: Narrator, Killian, Headless Horseman
BACKGROUND_IMAGE: killians_home_kitchen.png
BACKGROUND_EDIT: "Night, kitchen, combat, sparks flying"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Killian grabs an IRON SKEWER from the fireplace, SWINGS it to fend off a blow from the Horseman. The Horseman SWINGS the other axe. Killian ducks. The axe CRACKS fireplace stone, throwing sparks.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Killian lunges, JAMMING the skewer into the Horseman... The skewer comes through the Horseman's back. The Horseman SWIPES with the flat of one axe -- POUNDS Killian aside... Killian hits the wall, BASHING his head. Hits the floor.
  EXPRESSION: null

::PATHS::
- CHOICE: "Seek an escape route"
  TARGET: killians_home_white_room_night_5
  STATE_CHANGE: injury = +2
  CONDITION: null

::SCENE::
LOCATION: Killian's Home, White Room
MOOD: Discovery
CHARACTERS: Narrator, Beth
BACKGROUND_IMAGE: killians_home_white_room.png
BACKGROUND_EDIT: "Night, Beth revealing a trap door"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Beth kicks a carpet to reveal a TRAP DOOR.
  EXPRESSION: null

::PATHS::
- CHOICE: "Use the trap door"
  TARGET: killians_home_kitchen_night_7
  STATE_CHANGE: hope = +1
  CONDITION: null

::SCENE::
LOCATION: Killian's Home, Kitchen
MOOD: Ruthless
CHARACTERS: Narrator, Headless Horseman, Killian
BACKGROUND_IMAGE: killians_home_kitchen.png
BACKGROUND_EDIT: "Night, Horseman pulling skewer, lifting Killian's head"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The Horseman pulls the skewer out of his body, throws it. He goes to lift Killian by the hair with one hand, brings back the axe in the other hand...
  EXPRESSION: null

::PATHS::
- CHOICE: "Escape through the trap door"
  TARGET: killians_home_white_room_night_6
  STATE_CHANGE: terror = +3
  CONDITION: null

::SCENE::
LOCATION: Killian's Home, White Room
MOOD: Desperate Hiding
CHARACTERS: Narrator, Beth, Thomas
BACKGROUND_IMAGE: killians_home_white_room.png
BACKGROUND_EDIT: "Night, Beth lowering Thomas into a crawl space"

::SCRIPT::
- CHARACTER: Narrator
  LINE: At the trap door, Beth lowers Thomas to stairs leading to a CRAWL SPACE under the GAPPED floorboards. Thomas is crying.
  EXPRESSION: null
- CHARACTER: Beth
  LINE: Hush -- hush -- quiet as a mouse, now. You must hide...
  EXPRESSION: Frantic
- CHARACTER: Thomas
  LINE: Mother...
  EXPRESSION: Crying
- CHARACTER: Narrator
  LINE: Beth closes the trap door, frantically replacing the carpet. The room's door FLIES OPEN... the Horseman strides in, carrying Killian's severed head. Beth shrieks.
  EXPRESSION: null

::PATHS::
- CHOICE: "Face the Horseman"
  TARGET: forest_near_killian_house
  STATE_CHANGE: despair = +3
  CONDITION: null

::SCENE::
LOCATION: EXT. FOREST NEAR KILLIAN HOUSE
MOOD: Desperate
CHARACTERS: Narrator
BACKGROUND_IMAGE: forest_near_killian_house.png
BACKGROUND_EDIT: "Night, forest, sound of horse"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Br
  EXPRESSION: null

::SCENE::
LOCATION: Killian's Home, Cellar
MOOD: Terror
CHARACTERS: Narrator, Thomas, Beth
BACKGROUND_IMAGE: killian_cellar.png
BACKGROUND_EDIT: "Night, dark, dusty cellar"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Thomas, on his horse, hears Beth's shriek.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Beth's SCREAMS are abruptly CUT OFF. Her BODY is HEARD HITTING the floor above. Thomas sees the shadow of Beth's head rolling across the gaps in the floorboards above him, coming to rest with her hair showing, hanging down in the gap. FOOTSTEPS are HEARD...
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue hiding"
  TARGET: killian_white_room
  STATE_CHANGE: fear = +2
  CONDITION: null

::SCENE::
LOCATION: Killian's Home, White Room
MOOD: Gruesome
CHARACTERS: Narrator, Horseman, Killian, Beth
BACKGROUND_IMAGE: killian_white_room.png
BACKGROUND_EDIT: "Night, a room with white walls, slightly disheveled"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The Horseman's hands place Killian's and Beth's heads in a sack, cinching the sack shut.
  EXPRESSION: null

::PATHS::
- CHOICE: "Observe"
  TARGET: killian_kitchen
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Killian's Home, Kitchen
MOOD: Ominous
CHARACTERS: Narrator, Horseman
BACKGROUND_IMAGE: killian_kitchen.png
BACKGROUND_EDIT: "Night, a rustic kitchen, a battle axe on the floor"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The Headless Horseman enters, bends to retrieve the battle axe he left. He stands. Long, silent pause.
  EXPRESSION: null

::PATHS::
- CHOICE: "Wait"
  TARGET: killian_crawl_space
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Killian's Home, Crawl Space
MOOD: Desperate
CHARACTERS: Narrator, Thomas
BACKGROUND_IMAGE: killian_crawl_space.png
BACKGROUND_EDIT: "Night, dark, cramped crawl space"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Thomas cowers, trembling. QUIET.
  EXPRESSION: null

::PATHS::
- CHOICE: "Stay hidden"
  TARGET: killian_kitchen_chopping
  STATE_CHANGE: fear = +3
  CONDITION: null

::SCENE::
LOCATION: Killian's Home, Kitchen
MOOD: Violent
CHARACTERS: Narrator, Horseman
BACKGROUND_IMAGE: killian_kitchen_chopping.png
BACKGROUND_EDIT: "Night, kitchen floor being chopped"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The Horseman falls to his knees. He starts to CHOP at the floor with both axes. CHOPPING, CHOPPING, CHOPPING... making quick work of it...
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue hiding"
  TARGET: killian_crawl_space_hole
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Killian's Home, Crawl Space
MOOD: Imminent Danger
CHARACTERS: Narrator, Thomas, Horseman
BACKGROUND_IMAGE: killian_crawl_space_hole.png
BACKGROUND_EDIT: "Night, debris falling from above"

::SCRIPT::
- CHARACTER: Narrator
  LINE: A hole appears as debris falls... Thomas looks up. He tries to crawl away. The Horseman's arm SHOVES through from above -- grabbing Thomas and YANKING him up through the hole.
  EXPRESSION: null

::PATHS::
- CHOICE: "Attempt escape"
  TARGET: killian_farm_outskirts
  STATE_CHANGE: fear = +5
  CONDITION: null

::SCENE::
LOCATION: Killian's Farm, Town Outskirts
MOOD: Confrontation
CHARACTERS: Narrator, Brom, Horseman, Daredevil, Ichabod, Gunpowder
BACKGROUND_IMAGE: killian_farm_outskirts.png
BACKGROUND_EDIT: "Night, outskirts of a farm, scattered houses"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Brom rides from the forest. Ahead, at Killian's house, among scattered homes on the outskirts of town, Daredevil rides up as the Headless Horseman walks out with his sack of heads. The Horseman ties the sack to his saddle and leaps up. The Horseman ignores Brom. But Brom refuses to be ignored. Brom puts his reins in his mouth, aims his rifle... FIRING... BOOM -- the slug blows the Horseman off Daredevil, EXPLODING. Daredevil keeps going. The Horseman's smoldering body is left "face down."
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Brom halts his horse. He climbs down, pleased. The Horseman moves. Brom backs away, satisfaction diminishing. The Horseman rises to his knees. Brom falls to one knee, begins reloading. He fills the gun from his powder horn. The Horseman stands, unsheathes his sword and turns. The blast has exposed rotten flesh and maggot-infested muscle. Brom readies his ramrod, but there's no time. He rises, hefting his rifle, straight at the Horseman with a yell... The Horseman is on him. Brom swings the rifle, blocking. The battle is on, with Brom fending off the Horseman's sword with the rifle -- CLANK... CLANK... CLANK...
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: ACROSS THE FIELD, Ichabod and Gunpowder arrive... UP THE FIELD, the Horseman makes a backhanded swing, knocks Brom's rifle away, sends Brom to the ground...
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The Horseman walks away from Brom. Ichabod sees this, registers it. Brom pulls a knife and throws it. The knife blade goes through the Horseman from back to front, like a spear thrust through a smoldering sack of rotten flesh. The Horseman pulls Brom's knife, blade first, from his chest and turns upon Brom. Brom scrambles up, flees, running toward Killian's. The Horseman THROWS the knife... THWAP -- the knife imbeds in Brom's thigh. The Horseman strides to Brom. Ichabod closes in, pulling an unlit lantern off his saddle. The Horseman changes his sword grip, blade open... plants one foot on Brom's back, raising his sword to skewer... Ichabod arrives at full gallop -- SMASHES the lantern into the Horseman -- KNOCKING the Horseman off Brom.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: IN THE DISTANCE, Theodore and Glen arrive on horseback. They halt where they are, watching. Brom runs, limping to Killian's house, a goal in sight: FARM IMPLEMENTS propped there. Brom grabs SCYTHES with long curved blades, one in each hand. The Horseman rises. Ichabod leaps off Gunpowder, runs to Brom's side. Once more, the Horseman turns away.
  EXPRESSION: null
- CHARACTER: Brom
  LINE: I'll get him!
  EXPRESSION: Determined
- CHARACTER: Narrator
  LINE: Brom grabs Ichabod's pistol. Ichabod grabs Brom's pistol arm.
  EXPRESSION: null
- CHARACTER: Ichabod
  LINE: Wait! Don't you see? -- he's not after us!
  EXPRESSION: Urgent
- CHARACTER: Narrator
  LINE: Brom shakes himself free and -- FIRES -- the bullet rips through the Horseman's stomach to reveal putrid innards. The Horseman turns and strides back -- no more nice guy!
  EXPRESSION: null
- CHARACTER: Ichabod
  LINE: He is now!
  EXPRESSION: Scared
- CHARACTER: Narrator
  LINE: Brom throws the pistol at the Horseman. Across the way, Theodore looks to Glenn, turns his horse and flees. Glenn follows Theodore away. Brom steps up, scythes ready. He and the Horseman go at it -- Brom blocks axe and sword, deflecting blows...
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Ichabod grabs a long-handled SICKLE, circles them... SWINGS the sickle. The Horseman blocks. The Horseman battles both men at once, catching blows... counting every strike, METAL RINGING. Ichabod's sickle is knocked out of his hand. Brom catches the Horseman's sword in one scythe, catches the axe handle in the other scythe... The Horseman flatfoot KICKS Brom, sending him down. Brom picks up Ichabod's sickle and SWINGS it... The blade embeds in the Horseman down to the hilt.
  EXPRESSION: null
- CHARACTER: Ichabod
  LINE: Now you've annoyed him.
  EXPRESSION: Wry
- CHARACTER: Narrator
  LINE: The Horseman drops his axe, grasps the sickle handle... The handle SLAMS Ichabod away... Ichabod crawls, shaking off the blow. The Horseman staggers, trying to pull the blade from his body.
  EXPRESSION: null
- CHARACTER: Ichabod
  LINE: We cannot win this.
  EXPRESSION: Defeated
- CHARACTER: Narrator
  LINE: Brom yanks Ichabod to his feet and grabs his scythes. As they flee, Ichabod grabs a wood-splitting AXE from the stump where it's imbedded. Behind, the Horseman manages to extract the sickle, drops it. Brom and Ichabod head toward the COVERED BRIDGE that leads across to the town square.
  EXPRESSION: null

::PATHS::
- CHOICE: "Flee across the bridge"
  TARGET: covered_bridge_town_square
  STATE_CHANGE: fear = +5, weapons_obtained = true
  CONDITION: null

::SCENE::
LOCATION: Town Square and Covered Bridge
MOOD: Desperate Escape
CHARACTERS: Narrator, Brom, Ichabod, Horseman, Theodore, Glenn
BACKGROUND_IMAGE: covered_bridge_town_square.png
BACKGROUND_EDIT: "Night, a town square with a covered bridge"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Brom and Ichabod start across. Ichabod must help support Brom as Brom limps. Behind, the Horseman picks up the pace, closing fast... Inside the bridge, Ichabod and Brom are halfway across. FOOTSTEPS are HEARD POUNDING. Ichabod glances back... The Horseman is not behind them. Ichabod and Brom looks up. The POUNDING FOOTSTEPS are on the roof, passing over... ! Ahead, at the mouth of the covered bridge, the Horseman leaps down, spinning in midair, lands, crouched. Ichabod and Brom halt. The Horseman rises.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Ichabod releases Brom and moves forward, gripping his wood axe in both hands, SWINGING the axe downward... The Horseman swings his axe -- SPLINTERS Ichabod's axe handle. The Horseman, axe in one hand, sword in the other, turns upon Brom, and in pulling Brom aside out of the path of the sword, Ichabod receives a sword-thrust in the shoulder, which makes him scream out. The Horseman lifts his sword arm, THROWING Ichabod and withdrawing the sword in one motion... Ichabod tumbles.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Brom moves forward with scythes. The Horseman sets upon him with incredible ferocity -- battling Brom back, striking so hard and fast it's hard for Brom to keep blocking. Ichabod tries to get up, but falls, looking up...
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: ICHABOD'S POV: The Horseman KNOCKS one of Brom's scythes away, takes another SWING -- sends Brom spinning in a spray of blood... The Horseman stands over Brom's body, CHOPPING with his sword. Our POINT OF VIEW grows BLURRY... A BLURRY HORSEMAN approaches the POV. Ichabod is at the Horseman's mercy.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Then, another ANGLE -- the Horseman ignores Ichabod, strides past him. Ichabod takes a step back and collapses.
  EXPRESSION: null

::PATHS::
- CHOICE: "Fade to black"
  TARGET: van_tassel_ichabod_room
  STATE_CHANGE: brom_defeated = true, ichabod_injured = true
  CONDITION: null

::SCENE::
LOCATION: Van Tassel House, Ichabod's Room
MOOD: Recovery
CHARACTERS: Narrator, Ichabod, Doctor Lancaster, Baltus Van Tassel
BACKGROUND_IMAGE: van_tassel_ichabod_room.png
BACKGROUND_EDIT: "Night, Ichabod's bedroom, candlelight"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Candlelight. Ichabod, shirtless, feverish, opens his eyes. The wound at the top of his chest is raw but with the edges sealed shut. Ichabod in on his bed. Doctor Lancaster bends over him. Baltus Van Tassel observes.
  EXPRESSION: null
- CHARACTER: Doctor Lancaster
  LINE: Remarkable. A wound like this should have killed him... but it needs no stitch and there's hardly loss of blood.
  EXPRESSION: Amazed
- CHARACTER: Narrator
  LINE: Baltus sees Ichabod's eyes open.
  EXPRESSION: null
- CHARACTER: Baltus Van Tassel
  LINE: He stirs.
  EXPRESSION: Hopeful
- CHARACTER: Narrator
  LINE: Ichabod tries to rise, looking around, collapses in pain.
  EXPRESSION: null
- CHARACTER: Doctor Lancaster
  LINE: You must be still... the fever is on you.
  EXPRESSION: Concerned
- CHARACTER: Ichabod
  LINE: Katrina...
  EXPRESSION: Weak

::PATHS::
- CHOICE: "Rest"
  TARGET: van_tassel_kitchen
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Van Tassel House, Kitchen
MOOD: Mystical
CHARACTERS: Narrator, Katrina
BACKGROUND_IMAGE: van_tassel_kitchen.png
BACKGROUND_EDIT: "Night, a kitchen hearth, bubbling beaker"

::SCRIPT::
- CHARACTER: Narrator
  LINE: A Woman is bent over the hearth, mumbling. Then we see it is Katrina, mumbling over a boiling beaker of milk and green leaves. There is a dead crow on the hea
  EXPRESSION: null

::SCENE::
LOCATION: Van Tassel House - Ichabod's Room
MOOD: Recuperation
CHARACTERS: Narrator, Katrina, Baltus, Doctor Lancaster, Ichabod
BACKGROUND_IMAGE: ichabod_room_night.png
BACKGROUND_EDIT: "Nighttime, Ichabod's bedroom, dim light"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Katrina enters with the beaker of medicine. Baltus and Doctor Lancaster are bending over Ichabod, the Doctor trying to make Ichabod drink a livid green liquid from a shot glass.
  EXPRESSION: null
- CHARACTER: Doctor Lancaster
  LINE: It will restore you.
  EXPRESSION: Solemn
- CHARACTER: Narrator
  LINE: Ichabod closes his lips tight and refuses the drink -- he doesn't trust Lancaster. Katrina comes to the bedside with her beaker. Ichabod sees her. He is in pain, feverish.
  EXPRESSION: null
- CHARACTER: Ichabod
  LINE: I... I... tried to stop Brom but...
  EXPRESSION: Weak
- CHARACTER: Katrina
  LINE: Sssh... no one could have done more. Drink this down, it will make you sleep.
  EXPRESSION: Soothing
- CHARACTER: Ichabod
  LINE: The Horseman was not set to kill Brom... or me... If Brom had not attacked him...
  EXPRESSION: Pained
- CHARACTER: Baltus
  LINE: Later. Rest now.
  EXPRESSION: Authoritative
- CHARACTER: Ichabod
  LINE: I have discovered something.
  EXPRESSION: Urgent
- CHARACTER: Narrator
  LINE: Baltus and Doctor Lancaster glance at each other.
  EXPRESSION: null
- CHARACTER: Baltus
  LINE: These are ravings...
  EXPRESSION: Skeptical
- CHARACTER: Ichabod
  LINE: The Horseman does not kill for the sake of killing... he choses his victims.
  EXPRESSION: Determined
- CHARACTER: Katrina
  LINE: Drink...
  EXPRESSION: Gentle
- CHARACTER: Narrator
  LINE: She holds the beaker to Ichabod's lips. He drains it and falls back on the pillow, closing his eyes.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Baltus turns at a sound from the door. Lady Van Tassel has entered quietly. She comes to him anxiously and grips his hand.
  EXPRESSION: null
- CHARACTER: Lady Van Tassel
  LINE: What is it, Baltus?
  EXPRESSION: Anxious
- CHARACTER: Baltus
  LINE: Nothing... nothing... Don't be troubled, my love...
  EXPRESSION: Reassuring
- CHARACTER: Narrator
  LINE: They hold hands lovingly, staring at Ichabod, who has fallen asleep.
  EXPRESSION: null

::SCENE::
LOCATION: Ichabod's Dream - Church
MOOD: Eerie
CHARACTERS: Narrator, Young Ichabod, Father, Third Man
BACKGROUND_IMAGE: church_dream_night.png
BACKGROUND_EDIT: "Nighttime, empty church, dimly lit by lantern"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Empty church. Young Ichabod enters, carries a lantern past pews. He HEARS a SOUND, moving behind a pew to hide.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Ahead, across the church, a RED DOOR opens... Father and the villainous Third Man come out, shutting the door, speaking quietly.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The Third man holds a piece of parchment paper. Father is ever emotionless.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Ichabod watches them, ducking down to keep hidden...
  EXPRESSION: Fearful
- CHARACTER: Narrator
  LINE: Father and the Third Man walk to leave down the aisle, passing close to Ichabod without seeing him. They exit, leaving Young Ichabod alone in the silent church.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Young Ichabod rises, begins moving fearfully forward... FOLLOW as he crosses through the church... going to the RED DOOR... opening it...
  EXPRESSION: Fearful

::SCENE::
LOCATION: Ichabod's Dream - Church - Beyond the Red Door
MOOD: Horrifying
CHARACTERS: Narrator, Young Ichabod
BACKGROUND_IMAGE: torture_chamber_dream.png
BACKGROUND_EDIT: "Morning, room filled with torture devices, a shaft of light on an Iron Maiden"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Young Ichabod enters. The room contains TORTURE DEVICES: IRON CUFFS, THUMB SCREWS, KNIFES and NEEDLES. There is a SPIKED CHAIR, fitted with sharp spikes, adorned with straps for holding down the "accused."
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Young Ichabod backs away, terrified, then sees... A shaft of light cuts across a large, sarcophagus-like IRON MAIDEN -- where MOTHER'S EYES can be seen through the slit in the Iron Maiden's face. Open eyes. Dead eyes.
  EXPRESSION: Terrified
- CHARACTER: Narrator
  LINE: Young Ichabod lets out a strangled cry, runs to the Iron Maiden, trying to pull it open, clawing at the lock...
  EXPRESSION: Desperate
- CHARACTER: Narrator
  LINE: Finally, Young Ichabod backs away, choking on misery. He looks around in despair. He falls to his knees at the spiked chair, places his hands on the spikes, pressing...
  EXPRESSION: Devastated
- CHARACTER: Narrator
  LINE: As he sobs, blood runs down from his hands. He looks down and sees the CAT is there, looking up at him. The cat reaches up to rub its head against his face.
  EXPRESSION: Sorrowful

::SCENE::
LOCATION: Van Tassel House - Ichabod's Room
MOOD: Comforting
CHARACTERS: Narrator, Ichabod, Katrina
BACKGROUND_IMAGE: ichabod_room_night_comfort.png
BACKGROUND_EDIT: "Nighttime, Ichabod's bedroom, Ichabod is held by Katrina"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Ichabod, sobbing, has jerked up out of the dream straight into Katrina's embrace. She is sitting on the bed, holding him, calming him. She notices blood on his palms.
  EXPRESSION: null
- CHARACTER: Katrina
  LINE: Hush... hush... you were dreaming.
  EXPRESSION: Gentle
- CHARACTER: Narrator
  LINE: She takes a plain linen handkerchief from her cuff and dabs at the blood.
  EXPRESSION: null
- CHARACTER: Ichabod
  LINE: Yes... thing I had forgotten and would like not to remember.
  EXPRESSION: Troubled
- CHARACTER: Katrina
  LINE: Perhaps the remembering is the hard road to peace of mind... What ails you, Ichabod?
  EXPRESSION: Caring
- CHARACTER: Ichabod
  LINE: I was well, it was the world that was ill... But since I came here...
  EXPRESSION: Melancholy
- CHARACTER: Katrina
  LINE: You were not a happy man when you came. I think your wound was deeper than the wound you received from the Horseman... But your fever is broken, and though I cannot cure the world I would make you live happy in it... Tell me what you dreamed.
  EXPRESSION: Empathetic
- CHARACTER: Ichabod
  LINE: How I found my mother dead... how good and evil sometimes wear each other's clothes. She was an innocent, a child of nature, condemned... murdered... by my father...
  EXPRESSION: Anguished
- CHARACTER: Katrina
  LINE: Murdered by...?
  EXPRESSION: Shocked
- CHARACTER: Ichabod
  LINE: Yes -- murdered to save her soul! By a Bible-Black tyrant behind a mask of righteousness. I was seven when I lost my faith.
  EXPRESSION: Bitter
- CHARACTER: Katrina
  LINE: What do you believe in, Ichabod?
  EXPRESSION: Curious
- CHARACTER: Ichabod
  LINE: Sense and reason, cause and consequence, an ordered universe... Oh lord, I should not have come to this place where my rational mind has been so controverted by the spirit world...
  EXPRESSION: Desperate
- CHARACTER: Katrina
  LINE: Is there nothing you will take from Sleepy Hollow that was worth the coming here?
  EXPRESSION: Hopeful
- CHARACTER: Narrator
  LINE: Their eyes meet.
  EXPRESSION: null
- CHARACTER: Ichabod
  LINE: No... not nothing. A kiss... and how rare a thing... a kiss from a lovely woman before she saw my face or knew my name.
  EXPRESSION: Tender
- CHARACTER: Katrina
  LINE: Yes, without sense or reason...
  EXPRESSION: Playful
- CHARACTER: Narrator
  LINE: They hold still, perhaps about to kiss.
  EXPRESSION: null
- CHARACTER: Katrina
  LINE: It was a kiss on account.
  EXPRESSION: Teasing
- CHARACTER: Narrator
  LINE: But Ichabod breaks the moment.
  EXPRESSION: null
- CHARACTER: Ichabod
  LINE: Oh -- God forgive me -- I talk of kisses and you have lost your brave man Brom --
  EXPRESSION: Remorseful
- CHARACTER: Katrina
  LINE: I have shed my tears for Brom... and yet my heart is not broken. Do you think me wicked?
  EXPRESSION: Vulnerable
- CHARACTER: Ichabod
  LINE: No... but perhaps there is a little bit of the witch in you, Katrina.
  EXPRESSION: Admiring
- CHARACTER: Katrina
  LINE: Why do you say that?
  EXPRESSION: Curious
- CHARACTER: Ichabod
  LINE: Because you have bewitched me.
  EXPRESSION: Captivated
- CHARACTER: Narrator
  LINE: This time their held look turns into a passionate embrace...
  EXPRESSION: null

::SCENE::
LOCATION: Van Tassel House - Porch
MOOD: Suspenseful
CHARACTERS: Narrator, Young Masbath
BACKGROUND_IMAGE: porch_night.png
BACKGROUND_EDIT: "Nighttime, exterior of the house, porch"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Young Masbath slowly opens the door to peer out. He walks out onto the porch, watching as...
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: ACROSS THE LAWN, a CLOAKED FIGURE walks, carrying a LANTERN. The figure heads onto the long straight road, into the forest, lantern light dissipating.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Young Masbath steps off the porch, in cautious pursuit.
  EXPRESSION: Cautious

::SCENE::
LOCATION: The Hollow
MOOD: Eerie Awakening
CHARACTERS: Narrator
BACKGROUND_IMAGE: hollow_early_morning.png
BACKGROUND_EDIT: "Early morning, fog-shrouded forests"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Dawn light is visible over fog-shrouded forests.
  EXPRESSION: null

::SCENE::
LOCATION: Van Tassel House - Ichabod's Room
MOOD: Recovery and Revelation
CHARACTERS: Narrator, Ichabod, Lady Van Tassel, Young Masbath
BACKGROUND_IMAGE: ichabod_room_morning.png
BACKGROUND_EDIT: "Morning, Ichabod's bedroom, Lady Van Tassel attends him"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Ichabod awakes, rolls... finds Lady Van Tassel at his bedside with food and drink. Ichabod covers himself with his sheets.
  EXPRESSION: null
- CHARACTER: Lady Van Tassel
  LINE: You slept like the dead.
  EXPRESSION: Neutral
- CHARACTER: Ichabod
  LINE: You are too kind to me... I do not look to be served by the lady of the house.
  EXPRESSION: Polite
- CHARACTER: Lady Van Tassel
  LINE: Nor would you be but that the servant girl has vanished.
  EXPRESSION: Informative
- CHARACTER: Ichabod
  LINE: Sarah?
  EXPRESSION: Surprised
- CHARACTER: Lady Van Tassel
  LINE: Run away, like many more -- people are leaving in fear without ceremony.
  EXPRESSION: Concerned
- CHARACTER: Ichabod
  LINE: Where is... ?
  EXPRESSION: Inquisitive
- CHARACTER: Lady Van Tassel
  LINE: She watched over you till dawn. Now it is her turn to sleep.
  EXPRESSION: Matter-of-fact
- CHARACTER: Narrator
  LINE: Young Masbath enters as Lady Van Tassel goes out.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Ichabod looks at his palms, which are stained with dried blood.
  EXPRESSION: null
- CHARACTER: Ichabod
  LINE: Help me. I am fit for another day, I think.
  EXPRESSION: Resolute
- CHARACTER: Narrator
  LINE: The scene incorporates Young Masbath pouring water for Ichabod to wash himself, and helping him into his clothes.
  EXPRESSION: null
- CHARACTER: Young Masbath
  LINE: Where are we going?
  EXPRESSION: Curious
- CHARACTER: Ichabod
  LINE: To the Notary's office.
  EXPRESSION: Determined
- CHARACTER: Young Masbath
  LINE: Why?
  EXPRESSION: Inquisitive
- CHARACTER: Ichabod
  LINE: Because that is where I expect to find deposited... the last will and testament of the elder Van Garrett...
  EXPRESSION: Insightful
- CHARACTER: Young Masbath
  LINE: You have thought of something...
  EXPRESSION: Hopeful
- CHARACTER: Ichabod
  LINE: ...of something you said, Young Masbath... The Widow Winship came many a day with a basket of eggs to Van Garrett... who I understand had hens to spare... I begin to see. It was Van Garrett's child that the widow was carrying. And what news have you?
  EXPRESSION: Realizing
- CHARACTER: Young Masbath
  LINE: I heard someone leaving last night. Looked like they headed to town, but I lost them in the woods.
  EXPRESSION: Informative
- CHARACTER: Ichabod
  LINE: You didn't see who?
  EXPRESSION: Eager
- CHARACTER: Young Masbath
  LINE: All I saw was their lantern.
  EXPRESSION: Vague
- CHARACTER: Narrator
  LINE: Ichabod ponders, troubled, as Masbath brings him a shirt.
  EXPRESSION: null
- CHARACTER: Ichabod
  LINE: The Horseman does the killing but, I believe, at the bidding of a mortal, someone of flesh and blood.
  EXPRESSION: Convinced
- CHARACTER: Young Masbath
  LINE: What... ? What makes you say that?
  EXPRESSION: Surprised
- CHARACTER: Ichabod
  LINE: The witch... the crone, when I happened upon...
  EXPRESSION: Fragmented

::SCENE::
LOCATION: Not Specified
MOOD: Macabre
CHARACTERS: Narrator, Young Masbath, Ichabod
BACKGROUND_IMAGE: not_specified.png
BACKGROUND_EDIT: "Close-up on a corpse in a pool of blood"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Her corpse, she lay in a pool of blood. Blood poured hard from her neck. The wound was not cauterized.
  EXPRESSION: null
- CHARACTER: Young Masbath
  LINE: Then, she was not killed by the Hessian. Someone only tried to make it seem so.
  EXPRESSION: Thoughtful
- CHARACTER: Ichabod
  LINE: It was the settling of a private score. But the Horseman cuts heads to a different drum. The crone pointed us to what drives the Hessian -- his skull has been stolen from his grave. The person who stole it has power over the Hessian. Here is why the Headless One has returned through the gate of the Tree of the Dead. He chops heads until his own is restored to him.
  EXPRESSION: Serious
- CHARACTER: Young Masbath
  LINE: But what person... ?
  EXPRESSION: Curious
- CHARACTER: Ichabod
  LINE: A person who stands to gain by these murders.
  EXPRESSION: Certain

::SCENE::
LOCATION: Town Square - Church
MOOD: Chaotic, Tense
CHARACTERS: Narrator, Ichabod, Young Masbath, Reverend Steenwyck, Townsfolk
BACKGROUND_IMAGE: town_square_church.png
BACKGROUND_EDIT: "Daytime, bustling town square with a church, people boarding up windows"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Wagons, horses and townsfolk swarm. A crowd empties the town's general store. Provisions are passed along, man to man, and loaded onto wheelbarrows.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Ichabod and Young Masbath ride, passing many angry faces. All up and down the long straight road, home owners board up windows with lumber.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Ichabod and Young Masbath stop, tying their horses in front of the "NOTARY." Ichabod looks off... Down the road, people head to the church. Much activity...
  EXPRESSION: null
- CHARACTER: Ichabod
  LINE: Sanctuary. Or, so they hope.
  EXPRESSION: Cynical
- CHARACTER: Narrator
  LINE: People carry supplies into the church, within the bordering wrought-iron fence. Others work to build and erect massive wooden crosses. In the crowd here, Reverend Steenwyck spots Ichabod and Young Masbath, pushes past people, shouting...
  EXPRESSION: null
- CHARACTER: Reverend Steenwyck
  LINE: There he is! There...!
  EXPRESSION: Accusatory
- CHARACTER: Narrator
  LINE: People begin to pay attention to Steenwyck as he climbs atop a crate, pointing toward Ichabod...
  EXPRESSION: null
- CHARACTER: Reverend Steenwyck
  LINE: The desecrater of Christian burial! Twice he met the Horseman, and kept his head! How is it so... ?
  EXPRESSION: Outraged
- CHARACTER: Narrator
  LINE: At the Notary, Ichabod tries to ignore, heads inside, as a clod of earth hits him on the shoulder. In the churchyard, Steenwyck continues his rant.
  EXPRESSION: null
- CHARACTER: Reverend Steenwyck
  LINE: The Devil protects his own!
  EXPRESSION: Fanatical

::SCENE::
LOCATION: Notary Public - Hardenbrook's Offices
MOOD: Tense, Suspicious
CHARACTERS: Narrator, Ichabod, Young Masbath, Hardenbrook
BACKGROUND_IMAGE: notary_office.png
BACKGROUND_EDIT: "Daytime, small, untidy room with dusty documents"

::SCRIPT::
- CHARACTER: Narrator
  LINE: A small, untidy room with piles of dusty documents in great disorder.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The Notary Hardenbrook looks at Ichabod with his one good eye. Young Masbath stands near.
  EXPRESSION: null
- CHARACTER: Ichabod
  LINE: I take it, Mr. Hardenbrook, that wills and testaments are held here on public record?
  EXPRESSION: Inquisitive
- CHARACTER: Narrator
  LINE: Hardenbrook is in a funk, trying to act calm. He passes a document across the desk.
  EXPRESSION: Anxious
- CHARACTER: Hardenbrook
  LINE: I believe this is what you wish to see. Take it and go!
  EXPRESSION: Nervous
- CHARACTER: Narrator
  LINE: Ichabod scans the will of Peter Van Garrett.
  EXPRESSION: null
- CHARACTER: Hardenbrook
  LINE: Van Garrett Senior left his estate to his next of kin, that is to say, to his only son. However, the son being murdered in the same instant...
  EXPRESSION: Resigned
- CHARACTER: Ichabod
  LINE: The next of kin after the son would be the eldest of the line from Van Garrett's father's sister... none other than the Baltus Van Tassel: something else no one thought to mention!
  EXPRESSION: Realized
- CHARACTER: Hardenbrook
  LINE: Well, you have found your way to it, and I hope you will leave now before my windows are boken.
  EXPRESSION: Fearful
- CHARACTER: Narrator
  LINE: The crowd murmurs outside like angry bees. Ichabod flourishes the will.
  EXPRESSION: null
- CHARACTER: Ichabod
  LINE: I am not ready to leave.
  EXPRESSION: Determined
- CHARACTER: Narrator
  LINE: Hardenbrook starts moaning and wringing his hands.
  EXPRESSION: Distraught
- CHARACTER: Ichabod
  LINE: A brick through your window is not what puts you in terror, Hardenbrook ... there is something else... I saw your fear, and Steenwyck's and the doctor's, when you met at Philipse's house... Philipse paid with his head, and you fear for your own.
  EXPRESSION: Accusatory
- CHARACTER: Hardenbrook
  LINE: Yes, it's true! -- but we did not know it was a murdering plot when we were drawn in!
  EXPRESSION: Conflicted
- CHARACTER: Ichabod
  LINE: Drawn in by whom?!
  EXPRESSION: Demanding
- CHARACTER: Hardenbrook
  LINE: Mercy upon me! -- We meant no harm to come to her!
  EXPRESSION: Pleading
- CHARACTER: Ichabod
  LINE: No harm to come to whom?
  EXPRESSION: Persistent
- CHARACTER: Hardenbrook
  LINE: But the marriage made her next of kin...
  EXPRESSION: Babbling
- CHARACTER: Ichabod
  LINE: Made who next of kin to whom?! -- I'm confused!
  EXPRESSION: Frustrated
- CHARACTER: Young Masbath
  LINE: He means old Van Garrett secretly married the Widow Winship.
  EXPRESSION: Insightful
- CHARACTER: Ichabod
  LINE: Of course! And Van Garrett made a new will, leaving everything to her and his unborn child... So she stood between Baltus and the legacy! Where is the will?
  EXPRESSION: Eureka
- CHARACTER: Hardenbrook
  LINE: I cannot be seen to help you -- the Horseman will come for me -- !
  EXPRESSION: Terrified
- CHARACTER: Ichabod
  LINE: I will not leave without the very last will and testament of --
  EXPRESSION: Unyielding
- CHARACTER: Narrator
  LINE: Hardenbrook digs into a mountain of documents, hurling handfuls into the air... and flings the second will at Ichabod. Young Masbath nervously checks the door.
  EXPRESSION: null
- CHARACTER: Hardenbrook
  LINE: Go, then! I am a dead man!
  EXPRESSION: Despairing
- CHARACTER: Narrator
  LINE: He starts to sob.
  EXPRESSION: null
- CHARACTER: Young Masbath
  LINE: Sir...
  EXPRESSION: Concerned
- CHARACTER: Ichabod
  LINE: Young Masbath... I know why your father died. That night when Van Garrett quarreled with his son, Jonathan Masbath was summoned upstairs to witness the new Will. Here is your father's signature. It was his death warrant.
  EXPRESSION: Grave
- CHARACTER: Narrator
  LINE: Young Masbath takes the document and looks at it tearfully.
  EXPRESSION: null
- CHARACTER: Ichabod
  LINE: But the secret was not safe. Mrs. Killian the midwife was forewarned the baby was coming -- and so she, too, had to die.
  EXPRESSION: Grim
- CHARACTER: Narrator
  LINE: One of the other hurled documents has fluttered down fortuitously in front of Ichabod. He picks it up.
  EXPRESSION: null
- CHARACTER: Ichabod
  LINE: The marriage certificate. Parson Steenwyck married them. Doctor Lancaster confirmed the widow was pregnant. She told the secret to Magistrate Philipse. Notary Hardenbrook concealed the documents...
  EXPRESSION: Revealing
- CHARACTER: Narrator
  LINE: Hardenbrook snivels and moans and wrings his hands.
  EXPRESSION: null
- CHARACTER: Ichabod
  LINE: And you all kept silence! Why?... For some nameless dread of the man who stood to gain by it -- Baltus Van Tassel!
  EXPRESSION: Realized

::SCENE::
LOCATION: Van Tassel House - Stairs
MOOD: Transition
CHARACTERS: Narrator, Ichabod, Young Masbath
BACKGROUND_IMAGE: van_tassel_stairs.png
BACKGROUND_EDIT: "Daytime, interior stairs of a house"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Ichabod and Young Masbath start up the stairs, noticing:
  EXPRESSION: null

::SCENE::
LOCATION: Van Tassel House - Parlor
MOOD: Brooding, Greedy
CHARACTERS: Narrator, Baltus
BACKGROUND_IMAGE: van_tassel_parlor.png
BACKGROUND_EDIT: "Daytime, parlor with an oak coffer of silver coins"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Baltus, alone, with a glass of liquor, is brooding over an oak coffer of silver coins, running coins through his fingers.
  EXPRESSION: null

::SCENE::
LOCATION: Van Tassel House - Stairs
MOOD: Conversational, Skeptical
CHARACTERS: Narrator, Ichabod, Young Masbath
BACKGROUND_IMAGE: van_tassel_stairs.png
BACKGROUND_EDIT: "Daytime, interior stairs of a house"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Ichabod continues with Young Masbath, speaking quietly.
  EXPRESSION: null
- CHARACTER: Young Masbath
  LINE: I think there is some error in your reasoning...
  EXPRESSION: Doubtful
- CHARACTER: Ichabod
  LINE: Really? Do give me the benefit of your...
  EXPRESSION: Polite
- CHARACTER: Young Masbath
  LINE: All these murders... just so that Baltus Van Tassel should inherit yet more land and property?
  EXPRESSION: Disbelieving
- CHARACTER: Ichabod
  LINE: Precisely. Men murder for profit. Possibly you don't know New York... ?
  EXPRESSION: Assertive
- CHARACTER: Narrator
  LINE: Suddenly he sees his bedroom door is ajar.
  EXPRESSION: null

::SCENE::
LOCATION: Van Tassel House - Ichabod's Bedroom
MOOD: Surprising, Revealing
CHARACTERS: Narrator, Ichabod, Katrina, Young Masbath
BACKGROUND_IMAGE: ichabod_bedroom.png
BACKGROUND_EDIT: "Daytime, Ichabod's bedroom, door ajar"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Ichabod's entry surprises... Katrina, sitting at Ichabod's desk, reading his Ledger.
  EXPRESSION: null
- CHARACTER: Ichabod
  LINE: Katrina... why are you in my room?
  EXPRESSION: Surprised
- CHARACTER: Katrina
  LINE: Because it is yours. Is it wicked of me?
  EXPRESSION: Playful
- CHARACTER: Ichabod
  LINE: No... no...
  EXPRESSION: Flustered
- CHARACTER: Katrina
  LINE: I missed you. Where did you go?
  EXPRESSION: Affectionate
- CHARACTER: Ichabod
  LINE: To the Notary... I had questions to ask Hardenbrook.
  EXPRESSION: Evasive
- CHARACTER: Katrina
  LINE: And did you learn anything of interest?
  EXPRESSION: Curious
- CHARACTER: Narrator
  LINE: Ichabod and Young Masbath exchange a glance.
  EXPRESSION: null
- CHARACTER: Ichabod
  LINE: Well... perhaps.
  EXPRESSION: Guarded
- CHARACTER: Katrina
  LINE: My father...
  EXPRESSION: Neutral
- CHARACTER: Ichabod
  LINE: Your father... ?
  EXPRESSION: Startled
- CHARACTER: Katrina
  LINE: Yes. My father thinks you should return to New York.
  EXPRESSION: Informative
- CHARACTER: Ichabod
  LINE: Really? Why is that?
  EXPRESSION: Inquisitive
- CHARACTER: Katrina
  LINE: I don't know. Perhaps he looked in your ledger and did not like what he saw...
  EXPRESSION: Smug
- CHARACTER: Narrator
  LINE: She leaves the Ledger open on the desk. Ichabod steps over to look. Young Masbath cranes his neck to look. It is a page of doodles with the name "Katrina" written several times, and a sketch of Katrina. Embarrassed Ichabod closes the Ledger.
  EXPRESSION: null
- CHARACTER: Katrina
  LINE: He believes townfolk and country do not mix.
  EXPRESSION: Explanatory
- CHARACTER: Narrator
  LINE: Ichabod opens the drawer in the desk and puts away the document he took from the Notary. He is nervous because he knows they point to complicity by Katrina's father. Young Masbath, watching, understands this.
  EXPRESSION: null
- CHARACTER: Ichabod
  LINE: Locks the drawer and pockets the key.
  EXPRESSION: Cautious
- CHARACTER: Katrina
  LINE: What have you there?
  EXPRESSION: Probing
- CHARACTER: Ichabod
  LINE: Evidence. I'm sorry, I must ask your...
  EXPRESSION: Apologetic
- CHARACTER: Katrina
  LINE: Then I will leave you to your thoughts. Sleep well.
  EXPRESSION: Graceful
- CHARACTER: Narrator
  LINE: Katrina leaves. Ichabod is troubled.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Then -- to add to his troubles -- he suddenly sees a huge spider scuttling under his bed. He doesn't like spiders, even small ones. He gives a yelp.
  EXPRESSION: Fearful
- CHARACTER: Young Masbath
  LINE: It's only a spider.
  EXPRESSION: Calm
- CHARACTER: Ichabod
  LINE: Where's it gone? -- Where's it gone? Can you see it?
  EXPRESSION: Panicked
- CHARACTER: Narrator
  LINE: Young Masbath crouches to look under the bed. He frowns,
  EXPRESSION: null

::SCENE::
LOCATION: Van Tassel House - Ichabod's Room
MOOD: Suspense
CHARACTERS: Narrator, Young Masbath, Ichabod
BACKGROUND_IMAGE: ichabod_room_pentagram.png
BACKGROUND_EDIT: "Nighttime, Ichabod's room, bed moved"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Puzzled.
  EXPRESSION: null
- CHARACTER: Young Masbath
  LINE: There's something under there...
  EXPRESSION: Puzzled
- CHARACTER: Ichabod
  LINE: Kill it! Kill it! No -- no... er... stun it...
  EXPRESSION: Panicked
- CHARACTER: Young Masbath
  LINE: Help me move the bed.
  EXPRESSION: Determined
- CHARACTER: Narrator
  LINE: Young Masbath and Ichabod move the bed.
  EXPRESSION: null
- CHARACTER: Young Masbath
  LINE: Look...
  EXPRESSION: Astonished
- CHARACTER: Narrator
  LINE: UNDER THE BED is revealed a strange PENTAGRAM drawn in chalk.
  EXPRESSION: null
- CHARACTER: Young Masbath
  LINE: The Evil Eye!
  EXPRESSION: Terrified
- CHARACTER: Ichabod
  LINE: What... ? What is... ?
  EXPRESSION: Confused
- CHARACTER: Young Masbath
  LINE: It is someone casting spells against you.
  EXPRESSION: Grave
- CHARACTER: Ichabod
  LINE: The Evil Eye.
  EXPRESSION: Fearful
- CHARACTER: Narrator
  LINE: The spider is sitting on the Pentagram.
  EXPRESSION: null

::PATHS::
- CHOICE: "Investigate further"
  TARGET: ichabod_room_later
  STATE_CHANGE: fear = +2
  CONDITION: null

::SCENE::
LOCATION: Van Tassel House - Ichabod's Room - Later - Night
MOOD: Vigilant
CHARACTERS: Narrator, Young Masbath, Ichabod
BACKGROUND_IMAGE: ichabod_room_waiting.png
BACKGROUND_EDIT: "Nighttime, Ichabod's room, Young Masbath sleeping"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Young Masbath, fully dressed, sleeps on the bed. Ichabod sits waiting.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: He takes the cover off the lantern, looks at a CLOCK. Midnight.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Ichabod hears A DOOR OPEN AND CLOSE, then a CREAK on the stairs. He lights a candle. Then he goes to wake Young Masbath.
  EXPRESSION: Alert

::PATHS::
- CHOICE: "Wake Young Masbath and investigate"
  TARGET: ichabod_door
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Van Tassel House - Ichabod's Door - Night
MOOD: Tense
CHARACTERS: Narrator, Ichabod, Young Masbath
BACKGROUND_IMAGE: ichabod_door.png
BACKGROUND_EDIT: "Nighttime, hallway outside Ichabod's room"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Ichabod and Young Masbath come out of the room.
  EXPRESSION: null

::PATHS::
- CHOICE: "Proceed down the stairs"
  TARGET: second_floor_hallway
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Van Tassel House - Second Floor Hallway - Night
MOOD: Cautious
CHARACTERS: Narrator, Ichabod, Young Masbath
BACKGROUND_IMAGE: second_floor_hallway.png
BACKGROUND_EDIT: "Nighttime, dimly lit hallway"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Ichabod and Young Masbath come down STAIRS with a lantern, cautious.
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue to the sitting room"
  TARGET: sitting_room
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Van Tassel House - Sitting Room - Night
MOOD: Eerie
CHARACTERS: Narrator, Ichabod, Young Masbath
BACKGROUND_IMAGE: sitting_room.png
BACKGROUND_EDIT: "Nighttime, sitting room, dim lantern light"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Ichabod and Young Masbath cross, A CREAKING FLOORBOARD is HEARD from ANOTHER ROOM. Ichabod quickly covers his lantern.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Across the room, LIGHT comes under a DOOR, stops... continues.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: FOOTSTEPS are HEARD, then a DOOR OPENING and CLOSING.
  EXPRESSION: null

::PATHS::
- CHOICE: "Follow the sounds"
  TARGET: forest_by_house
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Forest by Van Tassel House - Night
MOOD: Fearful
CHARACTERS: Narrator, Ichabod, Young Masbath
BACKGROUND_IMAGE: forest_night.png
BACKGROUND_EDIT: "Nighttime forest, distant lantern light"

::SCRIPT::
- CHARACTER: Narrator
  LINE: LANTERN LIGHT moves, far ahead. Ichabod and Young Masbath follow, fearful, keeping hidden.
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue following"
  TARGET: forest_hillside
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Forest by Van Tassel House - Farther On (Hillside) - Night
MOOD: Anticipation
CHARACTERS: Narrator, Ichabod, Young Masbath
BACKGROUND_IMAGE: forest_hillside.png
BACKGROUND_EDIT: "Nighttime hillside overlooking a clearing"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Ichabod and Young Masbath stop on a hillside.
  EXPRESSION: null
- CHARACTER: Ichabod
  LINE: Wait here.
  EXPRESSION: Determined
- CHARACTER: Narrator
  LINE: Ichabod advances, up the hill... peers forward to see...
  EXPRESSION: null

::PATHS::
- CHOICE: "Observe from the hillside"
  TARGET: forest_clearing
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Forest Clearing by Van Tassel House - Night
MOOD: Shocking
CHARACTERS: Narrator, Ichabod, Lady Van Tassel, Reverend Steenwyck
BACKGROUND_IMAGE: forest_clearing_sex.png
BACKGROUND_EDIT: "Nighttime clearing, lantern on rock, couple having sex"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The lantern sits on a rock. On a blanket, a semi-naked MAN and semi-naked WOMAN are in the midst of rough SEX.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Ichabod crawls to peer from underbrush.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The couple keeps coupling, the MAN on top. His grunts and gasps are particularly desperate. He's all over the WOMAN, who lays back... it is LADY VAN TASSEL.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Ichabod swallows.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Lady Van Tassel pulls down the man's shirt, exposes his flesh. She raises a small, sharp KNIFE behind his back.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Ichabod's eyes widen. He's about to shout a warning, but...
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Lady Van Tassel brings the blade to her own hand, slicing deep into her palm. Blood flows. She rubs her cut hand over her partner's arching back, smearing blood.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Lady Van Tassel caresses the man's chest, neck, face... trailing blood.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The man lifts his head, in ecstasy, sucking the woman's bloody fingers ... it's REVEREND STEENWYCK.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Ichabod backs away, having seen more than enough.
  EXPRESSION: Horrified

::PATHS::
- CHOICE: "Return to Young Masbath"
  TARGET: forest_estate_hillside
  STATE_CHANGE: trauma = +5
  CONDITION: null

::SCENE::
LOCATION: Forest by Van Tassel Estate (Hillside) - Night
MOOD: Disturbed
CHARACTERS: Narrator, Ichabod, Young Masbath
BACKGROUND_IMAGE: forest_hillside_return.png
BACKGROUND_EDIT: "Nighttime hillside, Ichabod returning to Young Masbath"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Ichabod returns to Young Masbath's side.
  EXPRESSION: null
- CHARACTER: Young Masbath
  LINE: What was there?
  EXPRESSION: Curious
- CHARACTER: Ichabod
  LINE: Something I wish I had not seen. A beast with two backs.
  EXPRESSION: Troubled
- CHARACTER: Young Masbath
  LINE: A beast with... ? What next in these bewitched woods?!
  EXPRESSION: Amazed

::PATHS::
- CHOICE: "Return to Ichabod's room"
  TARGET: ichabod_room_aftermath
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Van Tassel House - Ichabod's Room - Night
MOOD: Desperate
CHARACTERS: Narrator, Ichabod, Young Masbath
BACKGROUND_IMAGE: ichabod_room_desk_drawer.png
BACKGROUND_EDIT: "Nighttime, Ichabod's room, desk drawer slightly open"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Ichabod and Young Masbath enter.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Ichabod sees that his desk drawer is slightly open.
  EXPRESSION: Foreboding
- CHARACTER: Narrator
  LINE: He opens the drawer knowing the worst. The documents have been taken.
  EXPRESSION: Devastated
- CHARACTER: Young Masbath
  LINE: Masbath suddenly sniffs the air. He signals to Ichabod, alert. He sniffs again... and in the grate is the source of the smell: the documents burned to ashes.
  EXPRESSION: Alert
- CHARACTER: Narrator
  LINE: Ichabod, in despondency, brings his finger to his head, rubbing his temples.
  EXPRESSION: Despairing

::PATHS::
- CHOICE: "Confront Lady Van Tassel"
  TARGET: kitchen_confrontation
  STATE_CHANGE: despair = +3
  CONDITION: null

::SCENE::
LOCATION: Van Tassel House - Kitchen - Day
MOOD: Confrontational
CHARACTERS: Narrator, Lady Van Tassel, Ichabod
BACKGROUND_IMAGE: kitchen_confrontation.png
BACKGROUND_EDIT: "Daytime, kitchen, Lady Van Tassel with bandaged hand"

::SCRIPT::
- CHARACTER: Lady Van Tassel
  LINE: She will not see you.
  EXPRESSION: Dismissive
- CHARACTER: Narrator
  LINE: She is talking to Ichabod. Her hand is loosely bandaged.
  EXPRESSION: null
- CHARACTER: Ichabod
  LINE: Did she say... anything?
  EXPRESSION: Concerned
- CHARACTER: Lady Van Tassel
  LINE: Only that she will not come down.
  EXPRESSION: Cold
- CHARACTER: Ichabod
  LINE: I see. Thank you.
  EXPRESSION: Resigned
- CHARACTER: Narrator
  LINE: Ichabod turns to go.
  EXPRESSION: null
- CHARACTER: Lady Van Tassel
  LINE: Constable, you have not asked me how I hurt my hand since yesterday... which would have been polite. In fact you have been as careful not to look at it as not to mention it.
  EXPRESSION: Accusatory
- CHARACTER: Narrator
  LINE: She strips off the bandage to show a roughly sewn cut.
  EXPRESSION: null
- CHARACTER: Ichabod
  LINE: Yes -- I'm sorry... How did you... ?
  EXPRESSION: Flustered
- CHARACTER: Lady Van Tassel
  LINE: I know you saw me.
  EXPRESSION: Menacing
  DIALOGUE_EFFECT: whispering close
- CHARACTER: Ichabod
  LINE: What... ?
  EXPRESSION: Startled
- CHARACTER: Lady Van Tassel
  LINE: I know you followed last night. You must promise not to tell my husband what you saw... promise me...
  EXPRESSION: Threatening
- CHARACTER: Narrator
  LINE: Ichabod tries to pull away, but she grips tighter. The FRONT DOOR is HEARD SLAMMING. Ichabod is panicky.
  EXPRESSION: null
- CHARACTER: Lady Van Tassel
  LINE: Reverend Steenwyck has power over me.
  EXPRESSION: Fearful
- CHARACTER: Ichabod
  LINE: P-p-power...?
  EXPRESSION: Incredulous
- CHARACTER: Lady Van Tassel
  LINE: He knows something terrible against my dear husband -- what you witnessed was the price of Steenwyck's silence.
  EXPRESSION: Desperate
- CHARACTER: Ichabod
  LINE: What does Steenwyck know?
  EXPRESSION: Anxious
- CHARACTER: Narrator
  LINE: Footsteps approach the door, the handle turns.
  EXPRESSION: null
- CHARACTER: Lady Van Tassel
  LINE: Later -- later...
  EXPRESSION: Evasive
- CHARACTER: Narrator
  LINE: She pulls away just as Baltus enters.
  EXPRESSION: null
- CHARACTER: Baltus
  LINE: The town is in a ferment. Horror piled on tragedy -- Hardenbrook is dead -- strangled.
  EXPRESSION: Grim
- CHARACTER: Narrator
  LINE: Baltus goes straight to a flagon on the side table and lifts it to his lips. Ichabod stares at Baltus's strong hands gripping the neck of the flagon.
  EXPRESSION: null
- CHARACTER: Lady Van Tassel
  LINE: Oh... ! That harmless old man?
  EXPRESSION: Feigning Shock
- CHARACTER: Baltus
  LINE: Hanged himself in the night!
  EXPRESSION: Blunt
- CHARACTER: Ichabod
  LINE: Hanged himself?
  EXPRESSION: Disbelieving
- CHARACTER: Baltus
  LINE: Reverend Steenwyck has called a meeting at the church -- tonight. Every man, woman and child. He will speak against you -- if you are wise you will be gone from here. Steenwyck's congregation is already halfway to being a mob.
  EXPRESSION: Warning
- CHARACTER: Ichabod
  LINE: I will go when I have done what I came to do.
  EXPRESSION: Determined
- CHARACTER: Narrator
  LINE: Lady Van Tassel comes to calm her husband. Baltus notices her wound.
  EXPRESSION: null
- CHARACTER: Baltus
  LINE: What is this?
  EXPRESSION: Concerned
- CHARACTER: Lady Van Tassel
  LINE: I was careless with the kitchen knife --
  EXPRESSION: Casual
- CHARACTER: Baltus
  LINE: The wound looks angry --
  EXPRESSION: Worried
- CHARACTER: Lady Van Tassel
  LINE: I'll bind it later with wild arrowroot flowers -- I know where I'll find some. Will you ride with me?
  EXPRESSION: Suggestive
- CHARACTER: Narrator
  LINE: Ichabod slips silently out of the room.
  EXPRESSION: null

::PATHS::
- CHOICE: "Go upstairs to Katrina's room"
  TARGET: stairs_up
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Van Tassel House - Stairs - Day
MOOD: Urgent
CHARACTERS: Narrator, Ichabod
BACKGROUND_IMAGE: stairs_day.png
BACKGROUND_EDIT: "Daytime, interior stairs"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Ichabod goes up the stairs.
  EXPRESSION: null

::PATHS::
- CHOICE: "Go to second floor"
  TARGET: second_floor_day
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Van Tassel House - Second Floor - Day
MOOD: Anxious
CHARACTERS: Narrator, Ichabod
BACKGROUND_IMAGE: second_floor_day.png
BACKGROUND_EDIT: "Daytime, second floor hallway"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Ichabod knocks quietly at Katrina's door. No answer. He quietly opens the door.
  EXPRESSION: null

::PATHS::
- CHOICE: "Enter Katrina's room"
  TARGET: katrinas_room
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Van Tassel House - Katrina's Room - Day
MOOD: Betrayed
CHARACTERS: Narrator, Ichabod, Young Masbath
BACKGROUND_IMAGE: katrinas_room_empty.png
BACKGROUND_EDIT: "Daytime, Katrina's room, bed unslept in, ashes in grate"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Katrina's bed has been slept in but it's empty and she is not there.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: But in the grate there is the telltale heap of charred paper and ash, recognizable as Ichabod's documents.
  EXPRESSION: Devastated
- CHARACTER: Narrator
  LINE: A sound at the door makes him whip around. It is Young Masbath.
  EXPRESSION: Startled
- CHARACTER: Young Masbath
  LINE: I saw her riding away towards the old pasture.
  EXPRESSION: Informative

::PATHS::
- CHOICE: "Follow Katrina to the old pasture"
  TARGET: windmill_day
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Windmill - Day
MOOD: Sinister
CHARACTERS: Narrator, Cloaked Figure
BACKGROUND_IMAGE: windmill_burning_straw.png
BACKGROUND_EDIT: "Daytime, inside a windmill, burning straw and skull"

::SCRIPT::
- CHARACTER: Narrator
  LINE: A small PILE of STRAW burns. GLOVED HANDS unfold a paper filled with HAIR CLIPPINGS, which are sprinkled on the fire.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: A cloaked FIGURE kneels at the pile. This person removes a HUMAN SKULL from a cloth bag.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The skull is placed at center in the flames. It's teeth are sharp, cut to points -- the HORSEMAN'S SKULL.
  EXPRESSION: null

::PATHS::
- CHOICE: "Head to the Ruined Cottage"
  TARGET: estate_fields
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Van Tassel Estate - Fields - Day
MOOD: Heartbroken
CHARACTERS: Narrator, Ichabod, Katrina
BACKGROUND_IMAGE: ruined_cottage_hearth.png
BACKGROUND_EDIT: "Daytime, fields, Ichabod approaching ruined cottage"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Ichabod rides Gunpowder, approaching the Ruined Cottage. He finds Katrina crouched over the hearthstone. Her horse grazes. She hears his horse and turns.
  EXPRESSION: null
- CHARACTER: Ichabod
  LINE: Katrina...
  EXPRESSION: Pained
- CHARACTER: Narrator
  LINE: Ichabod dismounts. Katrina had made a small fire. She is "doing magic." Mumbling. She turns to look at Ichabod in anger and tears.
  EXPRESSION: null
- CHARACTER: Ichabod
  LINE: You took the papers and burned them...?
  EXPRESSION: Sympathetic
- CHARACTER: Katrina
  LINE: So that you would not have them to accuse my father...!
  EXPRESSION: Defiant
- CHARACTER: Ichabod
  LINE: I... I accuse no one... but if there is guilt I cannot alter it no matter how much it grieves me... and no spells of yours can alter it either...
  EXPRESSION: Pained
- CHARACTER: Katrina
  LINE: If you knew my father you would not have such harsh thoughts about him -- no, nor if you felt anything for me!
  EXPRESSION: Accusatory
- CHARACTER: Ichabod
  LINE: I am pinioned by a chain of reasoning! Why else did his four friends conspire to conceal...?
  EXPRESSION: Tormented
- CHARACTER: Katrina
  LINE: You are the Constable, not I -- so find another chain of reasoning and let me be.
  EXPRESSION: Dismissive
- CHARACTER: Ichabod
  LINE: I cannot -- not the one or the other. I am heartsick with it.
  EXPRESSION: Desperate
- CHARACTER: Katrina
  LINE: I think you have no heart -- and I had a mind once to give you mine.
  EXPRESSION: Bitter
- CHARACTER: Narrator
  LINE: Katrina mounts her horse, which rears up. She is momentarily like a female warrior, her
  EXPRESSION: null

::PATHS::
- CHOICE: "Confront the truth of the matter"
  TARGET: end
  STATE_CHANGE: heartbreak = +5, understanding = -2
  CONDITION: null

::SCENE::
LOCATION: Field and Copse
MOOD: Anguished, Foreboding
CHARACTERS: Narrator, Ichabod, Katrina, Baltus, The Headless Horseman
BACKGROUND_IMAGE: field_copse_evening.png
BACKGROUND_EDIT: "Evening light, distant bell tolling, distant trees"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Eyes ablaze with anger and tears.
  EXPRESSION: Angry, Tearful
- CHARACTER: Ichabod
  LINE: Yes -- I think you loved me that day when you followed me into the Western Woods! -- to have braved such peril!
  EXPRESSION: Pleading
- CHARACTER: Katrina
  LINE: What peril was there for me if it was my own father who controlled the Headless Horseman?! Good-bye, Ichabod Crane! I curse the day you came to Sleepy Hollow!
  EXPRESSION: Scornful, Bitter
- CHARACTER: Narrator
  LINE: Ichabod watches her gallop away and hides his anguished face for comfort in Gunpowder's neck.
  EXPRESSION: Devastated
- CHARACTER: Narrator
  LINE: A distant bell is tolling as Baltus waits on his horse... watching where Lady Van Tassel can be glimpsed among the spaced trees gathering "arrowroot flowers."
  EXPRESSION: Anxious
- CHARACTER: Baltus
  LINE: Come. Hurry up! The meeting bell has started toning.
  EXPRESSION: Impatient
- CHARACTER: Narrator
  LINE: He looks anxiously toward the vintage, then back to the trees... where to his horror he sees... the Headless Horseman moves slowly toward Lady Van Tassel, calmly unsheathing his sword.
  EXPRESSION: Horrified

::PATHS::
- CHOICE: "Continue to the church"
  TARGET: church_exterior_night
  STATE_CHANGE: fear = +3
  CONDITION: null

::SCENE::
LOCATION: Sleepy Hollow - Church
MOOD: Grim, Urgent
CHARACTERS: Narrator, Steenwyck, Churchgoers
BACKGROUND_IMAGE: church_exterior_night.png
BACKGROUND_EDIT: "Nighttime, church entrance, bell tolling"

::SCRIPT::
- CHARACTER: Narrator
  LINE: People are entering the Church while the bell tolls them in... watched grimly by Steenwyck.
  EXPRESSION: null

::PATHS::
- CHOICE: "Observe from the shadows"
  TARGET: town_square_church_night
  STATE_CHANGE: caution = +1
  CONDITION: null

::SCENE::
LOCATION: Sleepy Hollow Town Square - Church
MOOD: Chaotic, Panicked
CHARACTERS: Narrator, Ichabod, Katrina, Baltus, The Headless Horseman
BACKGROUND_IMAGE: town_square_church_night.png
BACKGROUND_EDIT: "Nighttime, town square, church entrance visible"

::SCRIPT::
- CHARACTER: Narrator
  LINE: More people are heading toward the Church. In the shadows, Ichabod, hatted and cloaked to make himself look anonymous, also watches the people going by... and sees Katrina among them.
  EXPRESSION: Cautious, Observant
- CHARACTER: Baltus
  LINE: The Horseman... !
  EXPRESSION: Terrified
- CHARACTER: Narrator
  LINE: Baltus is barely hanging on. He stops, falling off his horse, scrambling toward Katrina, who is not far from Ichabod.
  EXPRESSION: Desperate
- CHARACTER: Baltus
  LINE: Save me...
  EXPRESSION: Pleading
- CHARACTER: Katrina
  LINE: Father...?
  EXPRESSION: Worried
- CHARACTER: Baltus
  LINE: He killed her...
  EXPRESSION: Devastated
- CHARACTER: Narrator
  LINE: Baltus grasps Katrina, deathly afraid.
  EXPRESSION: Terrified
- CHARACTER: Baltus
  LINE: The Horseman has killed your stepmother!
  EXPRESSION: Grieving, Terrified
- CHARACTER: Narrator
  LINE: HOOFBEATS are HEARD... the SCREECHY CRY of Daredevil. Baltus looks...
  EXPRESSION: Alerted
- CHARACTER: Narrator
  LINE: The Horseman rides into view, giving chase...
  EXPRESSION: Threatening
- CHARACTER: Narrator
  LINE: Instant mayhem -- the few people in the churchyard flee, heading for the Church...
  EXPRESSION: Chaotic
- CHARACTER: Narrator
  LINE: Baltus runs toward the Church...
  EXPRESSION: Fleeing
- CHARACTER: Katrina
  LINE: Father!
  EXPRESSION: Distressed
- CHARACTER: Narrator
  LINE: Katrina chases after Baltus. Ichabod now sees that his "case" is falling apart. He and Young Masbath start running to the Church.
  EXPRESSION: Realizing, Determined

::PATHS::
- CHOICE: "Enter the church"
  TARGET: church_interior_night
  STATE_CHANGE: panic = +2
  CONDITION: null

::SCENE::
LOCATION: Church
MOOD: Chaotic, Panicked
CHARACTERS: Narrator, Gatherers, Baltus, Katrina, Ichabod, Young Masbath, The Headless Horseman
BACKGROUND_IMAGE: church_interior_night.png
BACKGROUND_EDIT: "Nighttime interior, pews, windows, cellar entrance"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The GATHERERS in the pews react to the commotion, shouting, some running to the windows... to the doors...
  EXPRESSION: Panicked
- CHARACTER: Narrator
  LINE: Baltus pushes through the IRON GATE, across the churchyard, bounding up the stairs... Katrina following him.
  EXPRESSION: Hurried
- CHARACTER: Narrator
  LINE: The Horseman rides behind...
  EXPRESSION: Pursuing
- CHARACTER: Narrator
  LINE: Ichabod, with Masbath, follow into the churchyard. Ichabod glances back...
  EXPRESSION: Observant
- CHARACTER: Ichabod
  LINE: I know what you are thinking.
  EXPRESSION: Knowing
- CHARACTER: Young Masbath
  LINE: It seems Baltus Van Tassel is not the one who controls the Horseman.
  EXPRESSION: Realizing
- CHARACTER: Narrator
  LINE: As the Horseman reaches the open gate, Daredevil rears up violently, snorting, unwilling to enter.
  EXPRESSION: Unwilling

::SCENE::
LOCATION: Church
MOOD: Chaotic, Fearful
CHARACTERS: Narrator, Baltus, Katrina, Ichabod, Gatherers, Steenwyck, Riflemen
BACKGROUND_IMAGE: church_interior_night.png
BACKGROUND_EDIT: "Nighttime interior, chaos, barricading"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Baltus makes his way into the church, shoving people aside.
  EXPRESSION: Determined
- CHARACTER: Narrator
  LINE: Men pass RIFLES from stockpiles and climb onto pews at the boarded windows. Women herd children into a cellar.
  EXPRESSION: Preparing, Frightened
- CHARACTER: Narrator
  LINE: Baltus searches for a hiding place, moves toward the back...
  EXPRESSION: Searching
- CHARACTER: Narrator
  LINE: Katrina moves through, following Baltus...
  EXPRESSION: Concerned
- CHARACTER: Narrator
  LINE: At the front of the Church, Ichabod squeezes in just as the front doors are forced shut. Ichabod surveys the madness...
  EXPRESSION: Overwhelmed
- CHARACTER: Narrator
  LINE: Ichabod runs to a window, looking out between boards...
  EXPRESSION: Observant

::SCENE::
LOCATION: Church
MOOD: Tense, Defiant
CHARACTERS: Narrator, The Headless Horseman, Daredevil
BACKGROUND_IMAGE: church_exterior_night.png
BACKGROUND_EDIT: "Nighttime, churchyard gate, Horseman's attempt"

::SCRIPT::
- CHARACTER: Narrator
  LINE: At the church yard gates, the Horseman grabs Daredevil's reins, tries to move forward again. Same result -- Daredevil freaks.
  EXPRESSION: Frustrated
- CHARACTER: Narrator
  LINE: The Horseman gives his AXE an underhand toss... to the ground inside the gate...
  EXPRESSION: Determined
- CHARACTER: Narrator
  LINE: The axe instantly BEGINS TO DEGRADE -- like dust in the rain.
  EXPRESSION: Mystical
- CHARACTER: Narrator
  LINE: The Horseman steers away, keeping outside the fence.
  EXPRESSION: Strategic

::SCENE::
LOCATION: Church
MOOD: Desperate, Accusatory
CHARACTERS: Narrator, Ichabod, Katrina, Baltus, Steenwyck, Riflemen
BACKGROUND_IMAGE: church_interior_night.png
BACKGROUND_EDIT: "Nighttime interior, pews, windows, altar"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Ichabod comes away from the window, looking to the mass of panicked citizens. He sees Katrina pushing up the aisle... she's heading toward Baltus.
  EXPRESSION: Concerned
- CHARACTER: Narrator
  LINE: Katrina turns to Ichabod, her face aflame with accusation.
  EXPRESSION: Accusatory
- CHARACTER: Narrator
  LINE: Ichabod is humbled, desperate to make it up -- but Katrina runs toward ... the Altar, where she prostrates herself, evidently in a paroxysm of despair.
  EXPRESSION: Humbled, Desperate
- CHARACTER: Narrator
  LINE: RIFLES BOOM LOUDLY as men at the windows begin FIRING...
  EXPRESSION: Violent

::SCENE::
LOCATION: Church
MOOD: Under Attack, Desperate
CHARACTERS: Narrator, The Headless Horseman, Daredevil, Riflemen
BACKGROUND_IMAGE: church_exterior_night.png
BACKGROUND_EDIT: "Nighttime, church exterior, under fire"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The Horseman circles, under fire.
  EXPRESSION: Unaffected
- CHARACTER: Narrator
  LINE: Great clouds of gun smoke shoot from the Church.
  EXPRESSION: Chaotic
- CHARACTER: Narrator
  LINE: Men fire down from the belfry.
  EXPRESSION: Defiant
- CHARACTER: Narrator
  LINE: Parts of the Horseman and Daredevil splatter red as slugs hit, without effect.
  EXPRESSION: Invulnerable
- CHARACTER: Narrator
  LINE: At the other side of the Church... The Horseman circles, heading to the town square...
  EXPRESSION: Relentless

::SCENE::
LOCATION: Church
MOOD: Frantic, Confrontational
CHARACTERS: Narrator, Riflemen, Young Masbath, Baltus, Steenwyck, Ichabod
BACKGROUND_IMAGE: church_interior_night.png
BACKGROUND_EDIT: "Nighttime interior, riflemen repositioning, confrontation"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Riflemen shout to each other, running to the opposite windows to follow the Horseman.
  EXPRESSION: Urgent
- CHARACTER: Narrator
  LINE: Young Masbath grabs a rifle, leaps to join the brigade.
  EXPRESSION: Brave
- CHARACTER: Narrator
  LINE: Baltus is trying to force his way to one of the cellar doors, when Steenwyck grips him angrily, SHOVES him...
  EXPRESSION: Aggressive
- CHARACTER: Steenwyck
  LINE: You'll kill us all... !
  EXPRESSION: Fearful
- CHARACTER: Narrator
  LINE: Baltus stumbles back, topples pews.
  EXPRESSION: Unsteady
- CHARACTER: Steenwyck
  LINE: You're the one the Horseman wants.
  EXPRESSION: Accusatory
- CHARACTER: Narrator
  LINE: Steenwyck grabs Baltus, dragging him to the front.
  EXPRESSION: Forceful
- CHARACTER: Narrator
  LINE: Ichabod's pushing past people, trying to get to them.
  EXPRESSION: Determined

::SCENE::
LOCATION: Town Square - Church
MOOD: Menacing, Preparatory
CHARACTERS: Narrator, The Headless Horseman, Daredevil
BACKGROUND_IMAGE: town_square_church_night.png
BACKGROUND_EDIT: "Nighttime, town square, horseman preparing rope"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The Horseman brings Daredevil to a halt, yanks a large coil of ROPE off a hitching post, turns to ride back...
  EXPRESSION: Purposeful

::SCENE::
LOCATION: Church
MOOD: Tumultuous, Confrontational
CHARACTERS: Narrator, Baltus, Steenwyck, Ichabod, Crowd, One Rifleman
BACKGROUND_IMAGE: church_interior_night.png
BACKGROUND_EDIT: "Nighttime interior, escalating conflict, pistol drawn"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Baltus pulls free from Steenwyck, falls to the floor again.
  EXPRESSION: Weakened
- CHARACTER: Steenwyck
  LINE: Why should we die for you? Get out!
  EXPRESSION: Angry
- CHARACTER: Narrator
  LINE: Others join the rage, pulling Baltus toward the front of the Church, shouting. Ichabod joins in, struggling to push people off of Baltus...
  EXPRESSION: Uprising, Struggling
- CHARACTER: Ichabod
  LINE: Stop this... !
  EXPRESSION: Pleading
- CHARACTER: Narrator
  LINE: Ichabod gets to Baltus's side, trying to protect.
  EXPRESSION: Protective
- CHARACTER: Ichabod
  LINE: The Horseman cannot enter! It does not matter who he wants, he cannot cross the gate... !
  EXPRESSION: Reassuring, Desperate
- CHARACTER: Narrator
  LINE: At the windows, ONE RIFLEMAN cries out.
  EXPRESSION: Alarmed
- CHARACTER: One Rifleman
  LINE: He's coming back!
  EXPRESSION: Panicked
- CHARACTER: Narrator
  LINE: More panic. Steenwyck points toward Baltus.
  EXPRESSION: Accusatory
- CHARACTER: Steenwyck
  LINE: We have to save ourselves... !
  EXPRESSION: Self-preserving
- CHARACTER: Narrator
  LINE: Baltus pulls the PISTOL from Ichabod's holster...
  EXPRESSION: Bold
- CHARACTER: Baltus
  LINE: No! Unhand me! Stand off... !
  EXPRESSION: Defiant
- CHARACTER: Narrator
  LINE: Baltus brandishes the gun. Everyone backs off.
  EXPRESSION: Intimidating

::SCENE::
LOCATION: Church
MOOD: Violently Breached, Destructive
CHARACTERS: Narrator, The Headless Horseman
BACKGROUND_IMAGE: church_exterior_night.png
BACKGROUND_EDIT: "Nighttime, church facade, gate breached"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The Horseman rides past the front, fired upon...
  EXPRESSION: Undeterred
- CHARACTER: Narrator
  LINE: The Horseman halts along a length of the wrought gate, reaches... yanks off one IRON POST, which is pointed on top, like an arrow head.
  EXPRESSION: Powerful

::SCENE::
LOCATION: Church
MOOD: Violent Revelation, Chaos
CHARACTERS: Narrator, Baltus, Doctor Lancaster, Steenwyck, Katrina, Ichabod
BACKGROUND_IMAGE: church_interior_night.png
BACKGROUND_EDIT: "Nighttime interior, near altar, dramatic confrontation"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Baltus holds everyone away with the pistol, enraged...
  EXPRESSION: Enraged
- CHARACTER: Baltus
  LINE: The next person to lay hands on me will have a bullet.
  EXPRESSION: Threatening
- CHARACTER: Narrator
  LINE: Doctor Lancaster, who so far has just been one of the crowd, now pushes his way between Steenwyck and Baltus.
  EXPRESSION: Intervening
- CHARACTER: Doctor Lancaster
  LINE: Enough have died already! It is time to confess our sins and ask God to forgive our trespasses!
  EXPRESSION: Urgent, Repentant
- CHARACTER: Steenwyck
  LINE: Don't be a fool! I warn you, Doctor Lancaster -- !
  EXPRESSION: Warning
- CHARACTER: Baltus
  LINE: What is it that you know?
  EXPRESSION: Curious
- CHARACTER: Doctor Lancaster
  LINE: Your four friends played you false. We were devilishly possessed by one who --
  EXPRESSION: Revealing, Interrupted
- CHARACTER: Narrator
  LINE: That's as far as he gets before Steenwyck wrenches a heavy ornate CROSS from the wall and smashes his skull with a blow of tremendous force, with the Cross.
  EXPRESSION: Brutal
- CHARACTER: Narrator
  LINE: Baltus FIRES -- blasts a bloody hole in Steenwyck's stomach... !
  EXPRESSION: Vengeful
- CHARACTER: Narrator
  LINE: Everyone backs farther away as Steenwyck falls. Steenwyck lays gasping, eyes huge. He tries crawl...
  EXPRESSION: Dying, Horrified
- CHARACTER: Narrator
  LINE: Katrina rises to her feet and stands; staring wide-eyed at the horror.
  EXPRESSION: Shocked
- CHARACTER: Narrator
  LINE: Ichabod moves toward her.
  EXPRESSION: Concerned
- CHARACTER: Narrator
  LINE: Steenwyck lays still with a bloody gurgle, face down. Baltus looks to all the horrified people around him.
  EXPRESSION: Dead, Appalled
- CHARACTER: Baltus
  LINE: There is conspiracy here! And I will seek it out!
  EXPRESSION: Determined, Accusatory
- CHARACTER: Narrator
  LINE: CRASH! -- the IRON POST comes SPEARING through a window, trailing rope...
  EXPRESSION: Violent
- CHARACTER: Narrator
  LINE: CRACK -- SKEWERS Baltus from behind: its bloodied point bursting out through his breastbone...
  EXPRESSION: Fatal
- CHARACTER: Narrator
  LINE: Baltus gasps, stunned... he drops the gun, looks down to clutch the post. Blood streams out of his mouth.
  EXPRESSION: Dying, Shocked
- CHARACTER: Narrator
  LINE: Ichabod catches Katrina as she swoons. Horrorstruck, he hugs her... and thus notices that hanging on a ribbon around her neck is the little carved bauble taken from the neck of the dead Crone. Almost at the same time, Ichabod sees that on the flagstones where Katrina was lying there is now a "Drawing" done in chalk, identical to the "Evil Eye" drawing he found under his bed.
  EXPRESSION: Horrorstruck, Realizing

::PATHS::
- CHOICE: "Confront the truth"
  TARGET: ending
  STATE_CHANGE: revelation = true, horror = +3
  CONDITION: null

::SCENE::
LOCATION: Church - Interior
MOOD: Shocked, Horrified
CHARACTERS: Ichabod, Katrina, Baltus, Narrator
BACKGROUND_IMAGE: church_interior_night.png
BACKGROUND_EDIT: "Dimly lit church interior at night, tension high"

::SCRIPT::
- CHARACTER: Ichabod
  LINE: (gasps) The Evil Eye again!
  EXPRESSION: Shocked
- CHARACTER: Narrator
  LINE: At that moment, a piece of White Chalk falls from Katrina's senseless hand.
  EXPRESSION: null
- CHARACTER: Ichabod
  LINE: Oh God... .it was you!
  EXPRESSION: Horrified
- CHARACTER: Narrator
  LINE: The full horrible implication of this hits Ichabod just as: The rope tied to the post suddenly YANKS Baltus backward with incredible force -- SLAMS him into the WINDOW...
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue"
  TARGET: church_exterior_night_154
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Church - Exterior
MOOD: Violent, Tragic
CHARACTERS: Baltus, Horseman, Narrator
BACKGROUND_IMAGE: church_exterior_night.png
BACKGROUND_EDIT: "Nighttime church exterior, a window shatters, a horse and rider are present"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Baltus CRASHES backward through the window, hits the ground, DRAGGED...
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: OUTSIDE THE FENCE, the Horseman rides Daredevil away from the church, with the rope tied around Daredevil's saddle pommel...
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Baltus SLAMS the fence. The rope SNAPS. Baltus is held there awkwardly, gurgling blood.
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue"
  TARGET: church_interior_night_155
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Church - Interior
MOOD: Grief-stricken, Pleading
CHARACTERS: Ichabod, Katrina, Narrator
BACKGROUND_IMAGE: church_interior_night.png
BACKGROUND_EDIT: "Dimly lit church interior at night, Ichabod holding Katrina"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Ichabod, holding Katrina, cries out --
  EXPRESSION: null
- CHARACTER: Ichabod
  LINE: Oh... Katrlna... Oh God, forgive her...
  EXPRESSION: Pleading

::PATHS::
- CHOICE: "Continue"
  TARGET: church_exterior_night_156
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Church - Exterior
MOOD: Grim, Final
CHARACTERS: Horseman, Baltus, Narrator
BACKGROUND_IMAGE: church_exterior_night.png
BACKGROUND_EDIT: "Nighttime church exterior, the Horseman is about to strike"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The Horseman turns Daredevil, riding back... his sword raised high...
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: ... he chops off Baltus's head.
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue"
  TARGET: vantassel_house_night_157
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Van Tassel House - Katrina's Room - Night
MOOD: Somber, Grieving
CHARACTERS: Katrina, Ichabod, Narrator
BACKGROUND_IMAGE: vantassel_house_katrinas_room_night.png
BACKGROUND_EDIT: "Dimly lit bedroom at night, Katrina lies in bed"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Katrina lies insensible in her bed... the ribbon with the bauble around her neck.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Ichabod stands watching her, alone with his grief and his appalling "secret."
  EXPRESSION: null
- CHARACTER: Ichabod
  LINE: It was an evil spirit possessed you. I pray God it is satisfied now, and that you find peace. Goodbye, Katrina. The Evil Eye has done its work. My life is over -- spared for a lifetime of horrors in my sleep, waking each day to grief.
  EXPRESSION: Resigned, Grief-stricken
- CHARACTER: Narrator
  LINE: Ichabod leaves the room, closing the door.
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue"
  TARGET: vantassel_house_dawn_158
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Van Tassel House - Kitchen, Porch, and Lawn - Dawn
MOOD: Finality, Departure
CHARACTERS: Ichabod, Young Masbath, Narrator
BACKGROUND_IMAGE: vantassel_house_lawn_dawn.png
BACKGROUND_EDIT: "Dawn at the Van Tassel house, a fire burns in a circle of rocks"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Ichabod, watch only by Young Masbath, stands by a FIRE burning in a CIRCLE of ROCKS nearby. He has his Ledger. After a moment, he throws the LEDGER onto the fire. The pages catch quickly.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: He opens his satchel and digs out a BOOK. His luggage is packed on the porch.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: He walks back to the fire, looks at the book in his hand, the book Katrina gave him. He stands staring down.
  EXPRESSION: Pensive
- CHARACTER: Narrator
  LINE: A DECREPIT COACH is arriving.
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue"
  TARGET: vantassel_house_day_159
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Van Tassel House - Kitchen, Porch, and Lawn - Day
MOOD: Farewell, Resignation
CHARACTERS: Ichabod, Young Masbath, Van Ripper, Narrator
BACKGROUND_IMAGE: vantassel_house_lawn_day.png
BACKGROUND_EDIT: "Daytime at the Van Tassel house, a decrepit coach is present"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The decrepit COACH, with Gunpowder as one of its team, waits, loaded with Ichabod's baggage.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Van Ripper, the driver, helps Ichabod with strapping the load. Young Masbath watches, not helping.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Ichabod turns to Young Masbath. Angry tears come to Young Masbath's eyes. The farewell is like an argument.
  EXPRESSION: null
- CHARACTER: Young Masbath
  LINE: But who will look for the truth when you have gone?
  EXPRESSION: Pleading
- CHARACTER: Ichabod
  LINE: There is no more truth to be found. That is why I can go and leave this wretched place behind me.
  EXPRESSION: Resigned
- CHARACTER: Young Masbath
  LINE: You think it was Katrina, don't you?
  EXPRESSION: Accusatory
- CHARACTER: Ichabod
  LINE: That can never be uttered. Never.
  EXPRESSION: Stern
- CHARACTER: Narrator
  LINE: Ichabod takes his hand away.
  EXPRESSION: null
- CHARACTER: Young Masbath
  LINE: A strange sort of witch! -- with a kind and loving heart! How can you think so?
  EXPRESSION: Bewildered
- CHARACTER: Ichabod
  LINE: I have a good reason.
  EXPRESSION: Firm
- CHARACTER: Young Masbath
  LINE: Then you are bewitched by reason.
  EXPRESSION: Cynical
- CHARACTER: Ichabod
  LINE: I am beaten down by it! It's a hard lesson for a hard world, and you had better learn it, Young Masbath -- villainy wears many masks, none so dangerous as the mask of virtue. Farewell!
  EXPRESSION: Bitter
- CHARACTER: Narrator
  LINE: Van Ripper climbs onto the coach. Ichabod looks to the Manor House. Only one light shines, in a SECOND FLOOR WINDOW.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Ichabod climbs into the coach.
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue"
  TARGET: van_ripper_coach_day_160
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Van Ripper's Coach - Interior
MOOD: Reflective, Troubled
CHARACTERS: Ichabod, Narrator
BACKGROUND_IMAGE: van_ripper_coach_interior_day.png
BACKGROUND_EDIT: "Interior of a coach, Ichabod slumps down"

::SCRIPT::
- CHARACTER: Narrator
  LINE: INSIDE THE COACH, Ichabod slumps. He pounds twice on the coach wall.
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue"
  TARGET: vantassel_house_front_lawn_day_161
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Van Tassel House - Front Lawn - Day
MOOD: Sad Departure
CHARACTERS: Van Ripper, Young Masbath, Narrator
BACKGROUND_IMAGE: vantassel_house_lawn_day.png
BACKGROUND_EDIT: "Daytime front lawn of Van Tassel house, coach is leaving"

::SCRIPT::
- CHARACTER: Narrator
  LINE: OUTSIDE, Van Ripper whips the reins. The coach starts. Young Masbath watches, wiping tears.
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue"
  TARGET: vantassel_house_katrinas_room_day_162
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Van Tassel House - Katrina's Room - Day
MOOD: Heartbroken
CHARACTERS: Katrina, Narrator
BACKGROUND_IMAGE: vantassel_house_katrinas_room_day.png
BACKGROUND_EDIT: "Katrina's room, she wakes up and looks out the window"

::SCRIPT::
- CHARACTER: Katrina
  LINE: (Wakes up)
  EXPRESSION: Disoriented
- CHARACTER: Narrator
  LINE: Katrina wakes. She hears the Coach Wheels. She gets up from the bed and goes to the window. Her POV shows the Coach leaving... Katrina's face shows that her world has collapsed around her.
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue"
  TARGET: town_square_church_day_163
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Town Square - Church - Day
MOOD: Grim Discovery
CHARACTERS: Van Ripper, Ichabod, Cart Man, Katrina, Narrator
BACKGROUND_IMAGE: town_square_church_day.png
BACKGROUND_EDIT: "Daytime town square, coach passes a cart with a headless body"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Van Ripper's coach crosses the covered bridge... past the town square ... past the church. Near Doctor Lancaster's house, the coach passes a flat cart... on which lies the headless corpse of Lady Van Tassel. Ichabod looks at the corpse and he notes the gashed palm of one dead hand.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The cart is being pulled at a walking pace by a single horse. The CART MAN walking, holding the bridle.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The cart man pauses, seeing a RIDER approaching, traveling in the same direction as Ichabod's coach.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Ichabod realizes that the rider is Katrina. He looks from the coach window and sees Katrina get down from the horse and go to the cart.
  EXPRESSION: null
- CHARACTER: Ichabod
  LINE: (Pulls back from window and closes his eyes)
  EXPRESSION: Troubled

::PATHS::
- CHOICE: "Continue"
  TARGET: vantassel_house_ichabods_room_day_164
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Van Tassel House - Ichabod's Room - Day
MOOD: Empty, Lost
CHARACTERS: Young Masbath, Narrator
BACKGROUND_IMAGE: vantassel_house_ichabods_room_day.png
BACKGROUND_EDIT: "Ichabod's room, now empty, Young Masbath enters"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Young Masbath enters, looks around the empty room. He goes to sit, crosses his arms on the desk and lays down his head.
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue"
  TARGET: vantassel_house_parlor_day_165
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Van Tassel House - Parlor - Day
MOOD: Despair, Contemplation
CHARACTERS: Katrina, Narrator
BACKGROUND_IMAGE: vantassel_house_parlor_day.png
BACKGROUND_EDIT: "Parlor of Van Tassel house, Katrina stares into the fireplace"

::SCRIPT::
- CHARACTER: Katrina
  LINE: (Enters and slumps in a chair, staring into the burning fireplace)
  EXPRESSION: Desperate
- CHARACTER: Narrator
  LINE: Katrina enters. She crosses, slumps in a chair, staring into the burning fireplace
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue"
  TARGET: vantassel_house_various_rooms_pov_day_166
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Van Tassel House - Various Rooms - POV - Day
MOOD: Mysterious, Searching
CHARACTERS: Narrator
BACKGROUND_IMAGE: vantassel_house_various_rooms_pov_day.png
BACKGROUND_EDIT: "POV shot moving through the house, searching rooms"

::SCRIPT::
- CHARACTER: Narrator
  LINE: A POV MOVES SLOWLY THROUGH THE HOUSE; SOMEONE'S searching various rooms...
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue"
  TARGET: van_ripper_coach_day_167
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Van Ripper's Coach - Interior
MOOD: Realization, Urgency
CHARACTERS: Ichabod, Van Ripper, Narrator
BACKGROUND_IMAGE: van_ripper_coach_interior_day.png
BACKGROUND_EDIT: "Interior of a coach, Ichabod finds a book"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Ichabod opens his satchel, takes out a bottle of water and gulps from it. In replacing the bottle, he finds... the Book given him by Katrina.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: He opens the book. There is a DIAGRAM DRAWING on a whole page. Ichabod recognizes... the "Drawing" of the supposed "Evil Eye," identical to the two we have seen before. But what gets Ichabod's real attention is the bold "headline." The Headline over the Picture is "For The Protection of A Loved One Against Evil Spirits."
  EXPRESSION: null
- CHARACTER: Ichabod
  LINE: (Gasps, and mutters the words aloud) What a fool he's been!
  EXPRESSION: Astonished
- CHARACTER: Ichabod
  LINE: (to himself) But then, who... ?
  EXPRESSION: Puzzled
- CHARACTER: Narrator
  LINE: He is puzzled. He stares at his open palms. The scars on his palms trigger a thought... Then he understands: something we will soon understand.
  EXPRESSION: null
- CHARACTER: Ichabod
  LINE: He slides the front window panel to shout through it. Van Ripper, turn the coach... !
  EXPRESSION: Urgent
- CHARACTER: Van Ripper
  LINE: What?
  EXPRESSION: Confused
- CHARACTER: Ichabod
  LINE: Turn around, now!
  EXPRESSION: Demanding

::PATHS::
- CHOICE: "Continue"
  TARGET: vantassel_house_various_rooms_parlor_pov_evening_168
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Van Tassel House - Various Rooms - Parlor - POV - Evening
MOOD: Ominous, Watching
CHARACTERS: Narrator, Katrina
BACKGROUND_IMAGE: vantassel_house_parlor_pov_evening.png
BACKGROUND_EDIT: "POV shot moving through the house, stopping at the parlor doorway"

::SCRIPT::
- CHARACTER: Narrator
  LINE: SOMEONE still moves through the house, a TRAVELING POV -- moving through ROOMS on the ground floor... Stopping at the doorway of the PARLOR, looking to where Katrina is seated across the room.
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue"
  TARGET: doctors_residence_medical_room_evening_169
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Doctor's Residence - Medical Room - Evening
MOOD: Shocking Discovery, Urgency
CHARACTERS: Mrs. Lancaster, Ichabod, Narrator
BACKGROUND_IMAGE: doctors_residence_medical_room_evening.png
BACKGROUND_EDIT: "Medical room with two coffins, Ichabod bursts in"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Mrs. Lancaster comes to answer BANGING on the door. She opens the door and Ichabod pushes past, satchel in hand, taking Mrs. Lancaster's lantern.
  EXPRESSION: null
- CHARACTER: Ichabod
  LINE: Pardon my intrusion...
  EXPRESSION: Apologetic but urgent
- CHARACTER: Narrator
  LINE: There are TWO COFFINS on the floor. Ichabod throws off the lids from the coffins, looking to the headless BODIES of BALTUS and LADY VAN TASSEL.
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue"
  TARGET: vantassel_house_parlor_intercut_evening_170
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Van Tassel House - Parlor - Intercut - Evening
MOOD: Ominous, Peaceful
CHARACTERS: Katrina, Figure in Black, Narrator
BACKGROUND_IMAGE: vantassel_house_parlor_intercut_evening.png
BACKGROUND_EDIT: "Parlor, Katrina's eyes closed, a dark figure approaches"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Katrina still sits, her eyes closed. A FIGURE in BLACK moves forward in the darkness behind...
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue"
  TARGET: doctors_residence_medical_room_intercut_evening_171
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Doctor's Residence - Medical Room - Intercut - Evening
MOOD: Revelation, Disbelief
CHARACTERS: Ichabod, Mrs. Lancaster, Lady Van Tassel (corpse), Narrator
BACKGROUND_IMAGE: doctors_residence_medical_room_intercut_evening.png
BACKGROUND_EDIT: "Medical room, Ichabod examines Lady Van Tassel's hand"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Ichabod goes to lift Lady Van Tassel's hand with the GASH on its palm, bends to study... pulling at the sewn wound -- pulling the stitches apart between his thumbs...
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Mrs. Lancaster watches.
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue"
  TARGET: vantassel_house_parlor_intercut_evening_172
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Van Tassel House - Parlor - Intercut - Evening
MOOD: Startled, Fearful
CHARACTERS: Katrina, Narrator
BACKGROUND_IMAGE: vantassel_house_parlor_intercut_evening.png
BACKGROUND_EDIT: "Parlor, Katrina sits up and hears a noise"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Katrina hears a BOARD CREAK. She sits up, turning...
  EXPRESSION: null
- CHARACTER: Katrina
  LINE: Who is it?
  EXPRESSION: Fearful

::PATHS::
- CHOICE: "Continue"
  TARGET: doctors_residence_medical_room_intercut_evening_173
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Doctor's Residence - Medical Room - Intercut - Evening
MOOD: Shocked Realization
CHARACTERS: Ichabod, Narrator
BACKGROUND_IMAGE: doctors_residence_medical_room_intercut_evening.png
BACKGROUND_EDIT: "Medical room, Ichabod rips off his spectacles"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Ichabod releases the corpse's hand, tears off his spectacles, shaken by the realization...
  EXPRESSION: null
- CHARACTER: Ichabod
  LINE: No bloodflow, no clotting, no healing... When this cut was made... this woman was already dead.
  EXPRESSION: Devastated
- CHARACTER: Narrator
  LINE: Ichabod grabs his satchel, bolts out the door...
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue"
  TARGET: vantassel_house_parlor_intercut_evening_174
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Van Tassel House - Parlor - Intercut - Evening
MOOD: Terrified, Supernatural
CHARACTERS: Katrina, Lady Van Tassel, Narrator
BACKGROUND_IMAGE: vantassel_house_parlor_intercut_evening.png
BACKGROUND_EDIT: "Parlor, Lady Van Tassel appears, Katrina faints"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The FIGURE moves closer in darkness...
  EXPRESSION: null
- CHARACTER: Katrina
  LINE: Who is there... ?
  EXPRESSION: Trembling
- CHARACTER: Narrator
  LINE: The FIGURE comes into the dim, flickering fire light... Lady Van Tassel.
  EXPRESSION: null
- CHARACTER: Lady Van Tassel
  LINE: Dear step daughter...
  EXPRESSION: Sinister
- CHARACTER: Narrator
  LINE: Katrina stands, terrified, trying to form words... Lady Van Tassel cackles like a witch.
  EXPRESSION: null
- CHARACTER: Lady Van Tassel
  LINE: You look as if you've seen a ghost.
  EXPRESSION: Mocking
- CHARACTER: Narrator
  LINE: Katrina's eyes roll up as she FAINTS dead away to the floor.
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue"
  TARGET: town_square_doctors_residence_night_175
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Town Square - Doctor's Residence - Night
MOOD: Frantic Escape
CHARACTERS: Ichabod, Narrator
BACKGROUND_IMAGE: town_square_doctors_residence_night.png
BACKGROUND_EDIT: "Nighttime town square, Ichabod runs from the doctor's residence"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Ichabod runs out from the DOCTOR'S RESIDENCE
  EXPRESSION: null

::PATHS::
- CHOICE: "End Scene"
  TARGET: end
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Road near building
MOOD: Action
CHARACTERS: Ichabod, Van Ripper
BACKGROUND_IMAGE: road_near_building.png
BACKGROUND_EDIT: "Nighttime, a building with a side, empty coach"

::SCRIPT::
- CHARACTER: Narrator
  LINE: E, leaps up onto the empty coach, pushing Van Ripper's rifle aside.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Van Ripper's urinating against the side of the building.
  EXPRESSION: null
- CHARACTER: Van Ripper
  LINE: Be with you in a minute, Constable.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Ichabod whips the horses, driving the coach away.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Van Ripper frowns in confusion.
  EXPRESSION: Confused

::PATHS::
- CHOICE: "Continue driving away"
  TARGET: windmill_interior
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: The Windmill (Interior)
MOOD: Spooky
CHARACTERS: Narrator, Katrina, Lady Van Tassel
BACKGROUND_IMAGE: windmill_interior.png
BACKGROUND_EDIT: "Nighttime, interior of a windmill, filled with junk, machinery, and boxes. Katrina lies unconscious."

::SCRIPT::
- CHARACTER: Narrator
  LINE: The interior of the windmill is large and shadowy, with lots of old junk, clutter, machinery, boxes, etc.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Katrina lies unconscious.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Lady Van Tassel comes to cut off a clump of Katrina's hair with SCISSORS, grinning as she does it.
  EXPRESSION: Sinister
- CHARACTER: Narrator
  LINE: A CONJURING PILE has been prepared, containing a small ANIMAL'S HEART with an iron NAIL through it. Lady Van Tassel adds Katrina's hair, lights the pile off a lantern.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Lady Van Tassel WHISPERS over the fire.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: She looks to Katrina, who stirs.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Lady Van Tassel takes the HORSEMAN'S SKULL from a bag over her shoulder, places it in the flames.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: THUNDER is HEARD.
  EXPRESSION: null
- CHARACTER: Lady Van Tassel
  LINE: Rise up once more, my Dark Avenger! -- Rise up! -- One more night of Beheading! -- Rise up with your sword, and your Mistress of the night will make you whole -- a head for a head, my unholy Horseman -- rise -- rise -- rise from the earth, come forth again through the Tree of the Dead... come now for... Katrina!
  EXPRESSION: Chanting, Evil

::PATHS::
- CHOICE: "Continue the ritual"
  TARGET: western_woods_tree_of_dead
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Western Woods - Tree of the Dead
MOOD: Supernatural
CHARACTERS: Narrator
BACKGROUND_IMAGE: western_woods_tree_of_dead.png
BACKGROUND_EDIT: "Nighttime, wind scattering dead leaves, a twisted tree opening wide with shafts of light"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The WIND scatters dead leaves.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The TWISTED TREE OPENS WIDE with a RUMBLE -- SHAFTS of LIGHT shooting out.
  EXPRESSION: null

::PATHS::
- CHOICE: "Return to the road"
  TARGET: road_to_van_tassel_estate
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: The Road to Van Tassel Estate
MOOD: Urgent
CHARACTERS: Narrator, Ichabod
BACKGROUND_IMAGE: road_to_van_tassel_estate.png
BACKGROUND_EDIT: "Nighttime, Ichabod driving the coach hard ahead"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Ichabod drives the coach hard ahead.
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue driving"
  TARGET: windmill_interior_katrina_awake
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: The Windmill (Interior)
MOOD: Deceptive Calm
CHARACTERS: Narrator, Katrina, Lady Van Tassel
BACKGROUND_IMAGE: windmill_interior_katrina_awake.png
BACKGROUND_EDIT: "Nighttime, interior of a windmill, dying fire, Lady Van Tassel watching Katrina."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Katrina sits up, groggy, looking around... sees the dying fire, and Lady Van Tassel watching her.
  EXPRESSION: null
- CHARACTER: Lady Van Tassel
  LINE: Awake at last. Did you think it was all a nasty dream? Alas, no.
  EXPRESSION: Mocking
- CHARACTER: Katrina
  LINE: My father saw the Horseman kill you...
  EXPRESSION: Confused, Fearful
- CHARACTER: Lady Van Tassel
  LINE: He saw the Horseman coming to me with his sword unsheathed! But it is I who govern the Horseman, my dear, and Baltus did not stay to see.
  EXPRESSION: Arrogant, Cruel
- CHARACTER: Katrina
  LINE: But there was your body!
  EXPRESSION: Disbelieving
- CHARACTER: Lady Van Tassel
  LINE: The servant girl, Sarah, I always thought her useless, but she turned, out useful. Tomorrow I'll totter out of the woods and spin a tale how I found Baltus and Sarah in the act of lust... as I watched, the Horseman was upon them, and off went Sarah's head! I fainted and remember nothing more...
  EXPRESSION: Crafty, Vicious
- CHARACTER: Katrina
  LINE: Who are you?
  EXPRESSION: Fearful
- CHARACTER: Lady Van Tassel
  LINE: My family name was... Archer.
  EXPRESSION: Cold
- CHARACTER: Katrina
  LINE: The Archer...
  EXPRESSION: Recalling, Fearful
- CHARACTER: Lady Van Tassel
  LINE: I lived with my father and mother and my sister in a gamekeeper's cottage not far from here...
  EXPRESSION: Nostalgic, Deceptive
- CHARACTER: Narrator
  LINE: The conversation is being heard by a MOVING POV among the shadows.
  EXPRESSION: null
- CHARACTER: Lady Van Tassel
  LINE: Until one day, my father died, and the landlord who received many years of loyal service from my parents... evicted us. No one in this God-fearing town would take us in...
  EXPRESSION: Bitter, Resentful
- CHARACTER: Narrator
  LINE: The MOVING POV stops, spying from behind the clutter.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The REVERSE SHOT reveals YOUNG MASBATH, holding his breath.
  EXPRESSION: null
- CHARACTER: Lady Van Tassel
  LINE: ... because my mother was suspected of witchcraft...
  EXPRESSION: Cynical
- CHARACTER: Narrator
  LINE: Young Masbath looks about for a weapon. His eyes alight on a large Wooden Mallet.
  EXPRESSION: null
- CHARACTER: Lady Van Tassel
  LINE: She was no witch, but I believe she knew much that lies under the surface of life... and she schooled her daughters well while we lived as outcasts in the Western Woods. She died within a year... and my sister and I remained in our refuge, seeing not a soul... until, gathering firewood one day, we crossed the path of the Hessian...
  EXPRESSION: Resentful, Vengeful

::PATHS::
- CHOICE: "Continue listening"
  TARGET: flashback_forest_battlefield
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Forest Battlefield (Western Woods) - Flashback
MOOD: Violent
CHARACTERS: Narrator, Hessian Horseman, Two Young Girls
BACKGROUND_IMAGE: forest_battlefield_flashback.png
BACKGROUND_EDIT: "Daytime, a battlefield in the western woods, Hessian Horseman with a head"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The Hessian Horseman (avec head) has happened upon TWO YOUNG GIRLS gathering firewood.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The girls stand frozen at the sight of him, till one girl drops her firewood and runs...
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: The second girl remains, holding the Horseman's gaze.
  EXPRESSION: null

::PATHS::
- CHOICE: "Return to the windmill"
  TARGET: windmill_interior_lady_van_tassel_narrative
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: The Windmill (Interior)
MOOD: Vengeful Narrative
CHARACTERS: Narrator, Lady Van Tassel
BACKGROUND_IMAGE: windmill_interior_lady_van_tassel_narrative.png
BACKGROUND_EDIT: "Nighttime, interior of a windmill, Lady Van Tassel speaking"

::SCRIPT::
- CHARACTER: Narrator
  LINE: I saw his death, and from that moment...
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue to flashback"
  TARGET: flashback_forest_battlefield_burial
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Forest Battlefield (Western Woods) - Flashback
MOOD: Somber
CHARACTERS: Narrator, Girl, Horseman
BACKGROUND_IMAGE: forest_battlefield_burial_flashback.png
BACKGROUND_EDIT: "Daytime, a burial in the western woods, a girl watching"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The Girl watches the burial of the Horseman... and his Head dropped into the grave.
  EXPRESSION: null

::PATHS::
- CHOICE: "Return to the windmill"
  TARGET: windmill_interior_lady_van_tassel_offer
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: The Windmill (Interior)
MOOD: Dark Bargain
CHARACTERS: Narrator, Young Masbath, Lady Van Tassel, Katrina
BACKGROUND_IMAGE: windmill_interior_lady_van_tassel_offer.png
BACKGROUND_EDIT: "Nighttime, interior of a windmill, Young Masbath moving quietly behind Lady Van Tassel"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Young Masbath, unseen, works his way quietly around behind Lady Van Tassel.
  EXPRESSION: null
- CHARACTER: Lady Van Tassel
  LINE: ... I offered my soul to Satan if he would raise the Hessian from the grave to avenge me.
  EXPRESSION: Wicked
- CHARACTER: Katrina
  LINE: Avenge you?
  EXPRESSION: Shocked
- CHARACTER: Lady Van Tassel
  LINE: Against Van Garrett, who evicted my family, against Baltus Van Tassel who, with wife and simpering girlchild, stole our home. I swore I would make myself mistress of all they had... The easiest part was the first -- to enter your house as your mother's sick nurse and put her body into the grave, and my own into the marriage bed.
  EXPRESSION: Cackling, Vengeful
- CHARACTER: Narrator
  LINE: Katrina cries out in horror.
  EXPRESSION: null
- CHARACTER: Lady Van Tassel
  LINE: Not quite so easy was to secure my legacy... but lust delivered Reverend Steenwyck into my power. Fear did the same for the Notary Hardenbrook. The drunken Philipse succumbed for a share of the proceeds, and the Doctor's silence I exchanged for my complicity in his fornications...
  EXPRESSION: Smug, Manipulative
- CHARACTER: Narrator
  LINE: Masbath moves into the open, weapon raised. Katrina sees him and stifles a gasp.
  EXPRESSION: null
- CHARACTER: Katrina
  LINE: Yes! -- you have everything now.
  EXPRESSION: Distracted, Fearful
- CHARACTER: Lady Van Tassel
  LINE: No, my dear -- you do, by your father's will. But I get everything in the event of your death.
  EXPRESSION: Cackling, Greedy
- CHARACTER: Narrator
  LINE: Lady Van Tassel's hand reaches for the Mystic Bauble on Katrina's neck. She rips it free.
  EXPRESSION: null
- CHARACTER: Lady Van Tassel
  LINE: This pretty bauble, which I so kindly gave you to wear, has done it's work. My sister, by the way, sadly passed away...
  EXPRESSION: Mocking, Cruel

::PATHS::
- CHOICE: "Continue narration and flashback"
  TARGET: flashback_crone_cave_home
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Outside Crone's Cave Home - Flashback
MOOD: Brutal
CHARACTERS: Narrator, Lady Van Tassel, Crone
BACKGROUND_IMAGE: outside_crone_cave_home_flashback.png
BACKGROUND_EDIT: "Daytime, outside a cave home, the Crone is beaten and bloodied. Lady Van Tassel's hand hauls her up."

::SCRIPT::
- CHARACTER: Narrator
  LINE: The Crone falls to the ground outside her cave, unconscious, beaten and bloodied.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: A hand -- Lady Van Tassel's hand -- enters FRAME to haul the Crone up by the hair, and WE SEE the Crone's bloodied features face to face with the wicked smile of Lady Van Tassel.
  EXPRESSION: null

::PATHS::
- CHOICE: "Return to the windmill"
  TARGET: windmill_interior_lady_van_tassel_sister_death
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: The Windmill (Interior)
MOOD: Brutal Revelation
CHARACTERS: Narrator, Lady Van Tassel
BACKGROUND_IMAGE: windmill_interior_lady_van_tassel_sister_death.png
BACKGROUND_EDIT: "Nighttime, interior of a windmill, Lady Van Tassel speaking"

::SCRIPT::
- CHARACTER: Lady Van Tassel
  LINE: ... quite recently.
  EXPRESSION: Cold

::PATHS::
- CHOICE: "Continue to flashback"
  TARGET: flashback_crone_cave_home_sword
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Outside Crone's Cave Home - Flashback
MOOD: Violent Conclusion
CHARACTERS: Narrator, Lady Van Tassel, Crone
BACKGROUND_IMAGE: outside_crone_cave_home_sword_flashback.png
BACKGROUND_EDIT: "Daytime, outside a cave home, Lady Van Tassel holds a sword high, then swings down. Severed head and torso are seen."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Lady Van Tassel holds a SWORD high, SWINGS DOWN...
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Then we see the separated Head and Torso... and the severed CORD, which had been around the Crone's neck... and Lady Van Tassel's Hand reaching for the Mystic Bauble, which had fallen free.
  EXPRESSION: null

::PATHS::
- CHOICE: "Return to the windmill"
  TARGET: windmill_interior_masbath_confrontation
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: The Windmill (Interior)
MOOD: Confrontation
CHARACTERS: Narrator, Young Masbath, Lady Van Tassel, Katrina
BACKGROUND_IMAGE: windmill_interior_masbath_confrontation.png
BACKGROUND_EDIT: "Nighttime, interior of a windmill, Young Masbath about to strike Lady Van Tassel with a mallet"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Young Masbath is about ready to bring the mallet down upon Lady Van Tassel's head.
  EXPRESSION: null
- CHARACTER: Katrina
  LINE: It was the Crone you killed... your own sister...
  EXPRESSION: Accusatory, Horrified
- CHARACTER: Lady Van Tassel
  LINE: She brought it upon herself...
  EXPRESSION: Cold, Unrepentant
- CHARACTER: Narrator
  LINE: Like a whiplash, Lady Van Tassel turns cackling at Young Masbath -- she sensed him by witchery!
  EXPRESSION: null
- CHARACTER: Lady Van Tassel
  LINE: -- by helping you and your master!
  EXPRESSION: Threatening
- CHARACTER: Narrator
  LINE: Young Masbath shrieks and drops the mallet.
  EXPRESSION: null
- CHARACTER: Lady Van Tassel
  LINE: You are just in time to have your head sliced off!
  EXPRESSION: Menacing
- CHARACTER: Narrator
  LINE: Katrina and Young Masbath run to each other for mutual comfort.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: LIGHTNING BRIGHTENS the forest. Lady Van Tassel looks up.
  EXPRESSION: null
- CHARACTER: Lady Van Tassel
  LINE: The Horseman comes. And tonight he comes for you!
  EXPRESSION: Triumphant, Sinister

::PATHS::
- CHOICE: "Flee the windmill"
  TARGET: western_woods_horseman
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Western Woods
MOOD: Foreboding
CHARACTERS: Narrator, Horseman
BACKGROUND_IMAGE: western_woods_horseman.png
BACKGROUND_EDIT: "Nighttime, the Horseman rides Daredevil, described as a freight train of moldering flesh."

::SCRIPT::
- CHARACTER: Narrator
  LINE: The Horseman rides Daredevil, a freight train of moldering flesh...
  EXPRESSION: Horrifying

::PATHS::
- CHOICE: "Return to the windmill"
  TARGET: windmill_interior_final_confrontation
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: The Windmill (Interior)
MOOD: Desperate Escape
CHARACTERS: Narrator, Katrina, Young Masbath, Lady Van Tassel
BACKGROUND_IMAGE: windmill_interior_final_confrontation.png
BACKGROUND_EDIT: "Nighttime, interior of a windmill, Katrina and Young Masbath holding hands, scared. Lady Van Tassel has the Horseman's skull."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Katrina and Young Masbath are holding hands, scared.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Lady Van Tassel picks up the Horseman's skull in her gloved hand and puts up her face and gives out a long animal howl.
  EXPRESSION: Animalistic
- CHARACTER: Narrator
  LINE: Distantly, Daredevil is heard answering with a scream.
  EXPRESSION: Terrifying
- CHARACTER: Narrator
  LINE: Katrina and Young Masbath run.
  EXPRESSION: Fearful
- CHARACTER: Narrator
  LINE: Lady Van Tassel has need to stop them.
  EXPRESSION: null
- CHARACTER: Lady Van Tassel
  LINE: Run! There is no escape!
  EXPRESSION: Mocking, Inevitable

::PATHS::
- CHOICE: "Try to escape"
  TARGET: van_tassel_house_porch
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Van Tassel House - Porch and Lawn
MOOD: Urgent
CHARACTERS: Narrator, Ichabod
BACKGROUND_IMAGE: van_tassel_house_porch.png
BACKGROUND_EDIT: "Nighttime, Ichabod leaping from the coach onto the porch, seeing firelight."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Ichabod leaps from the coach, bounds up porch stairs...
  EXPRESSION: null
- CHARACTER: Ichabod
  LINE: Katrina!
  EXPRESSION: Desperate
- CHARACTER: Narrator
  LINE: Ichabod stops, sees FIRELIGHT at the Windmill. He runs... leaps back up to the coach and takes off...
  EXPRESSION: null

::PATHS::
- CHOICE: "Race to the windmill"
  TARGET: windmill_exterior_wind
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: The Windmill (Exterior)
MOOD: Chaotic Climax
CHARACTERS: Narrator, Lady Van Tassel
BACKGROUND_IMAGE: windmill_exterior_wind.png
BACKGROUND_EDIT: "Nighttime, thunder booms, wind howls. Lady Van Tassel stands in the doorway with the skull, laughing."

::SCRIPT::
- CHARACTER: Narrator
  LINE: THUNDER BOOMS. WIND HOWLS.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Lady Van Tassel stands in the doorway with the skull in one hand, laughing.
  EXPRESSION: Maniacal

::PATHS::
- CHOICE: "Observe the scene"
  TARGET: windmill_exterior_other_side
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Around the Other Side of the Windmill
MOOD: Unseen Action
CHARACTERS: Narrator
BACKGROUND_IMAGE: windmill_exterior_other_side.png
BACKGROUND_EDIT: "Nighttime, around the other side of the windmill."

::SCRIPT::
- CHARACTER: Narrator
  LINE: Katr
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue observing"
  TARGET: end
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Open area near a windmill
MOOD: Urgent
CHARACTERS: Narrator, Katrina, Young Masbath, Ichabod, Lady Van Tassel, Horseman
BACKGROUND_IMAGE: open_area_windmill.png
BACKGROUND_EDIT: "Open field with a windmill in the background, dusk"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Katrina and Young Masbath break out into the open. Ichabod drives toward them...
  EXPRESSION: null
- CHARACTER: Katrina
  LINE: Ichabod!
  EXPRESSION: Alarmed
- CHARACTER: Narrator
  LINE: Ichabod meets them, halts the coach and jumps down (as the coach horses trot away), running to put his arms around Katrina and Young Masbath...
  EXPRESSION: null
- CHARACTER: Ichabod
  LINE: Thank God...
  EXPRESSION: Relieved
- CHARACTER: Narrator
  LINE: Lady Van Tassel's mad laughter is heard. Ichabod and Katrina turn as... Lady Van Tassel rides from around the windmill on her white horse. She shrieks with laughter.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Along the treeline, the Horseman breaks into the open... Hell on horseback -- full speed ahead...
  EXPRESSION: Terrified
- CHARACTER: Lady Van Tassel
  LINE: Have you come back to arrest him after all?!
  EXPRESSION: Mocking
- CHARACTER: Narrator
  LINE: Ichabod thinks fast, moving to the windmill, leading Katrina and Young Masbath along with him.
  EXPRESSION: null
- CHARACTER: Ichabod
  LINE: Quickly...!
  EXPRESSION: Urgent
- CHARACTER: Narrator
  LINE: Behind, wind tosses Lady Van Tassel's dress and hair. She holds the Horseman's skull high.
  EXPRESSION: null
- CHARACTER: Lady Van Tassel
  LINE: Mind your hat, Constable!
  EXPRESSION: Taunting
- CHARACTER: Narrator
  LINE: Young Masbath scurries up the ladder and in. Katrina's next. Ichabod looks behind... The Horseman is almost upon them. Ichabod follows Katrina, pulling himself up. The Horseman arrives, dismounting, moving forward...
  EXPRESSION: null

::PATHS::
- CHOICE: "Enter the windmill"
  TARGET: windmill_interior_night
  STATE_CHANGE: fear = +2
  CONDITION: null

::SCENE::
LOCATION: Windmill Interior
MOOD: Desperate
CHARACTERS: Narrator, Ichabod, Young Masbath, Katrina, Horseman
BACKGROUND_IMAGE: windmill_interior_night.png
BACKGROUND_EDIT: "Interior of a dimly lit windmill, dusty with milling equipment"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Ichabod leaps up, lifts the heavy trap door on its hinges, slams it. The door is POUNDED from outside, buckling.
  EXPRESSION: null
- CHARACTER: Young Masbath
  LINE: It won't hold.
  EXPRESSION: Fearful
- CHARACTER: Narrator
  LINE: Ichabod goes to a large GRINDSTONE against a wall. He struggles to roll it... Young Masbath helps him roll it to the trapdoor. It falls on top with a THUD. Masbath jumps back as the Horseman's sword jabs up through the grindstone's center hole. The sword withdraws. POUNDING begins anew.
  EXPRESSION: null

::PATHS::
- CHOICE: "Continue to defend the door"
  TARGET: windmill_exterior_night
  STATE_CHANGE: fear = +1
  CONDITION: null

::SCENE::
LOCATION: Windmill Exterior
MOOD: Relentless Attack
CHARACTERS: Narrator, Horseman
BACKGROUND_IMAGE: windmill_exterior_night.png
BACKGROUND_EDIT: "Exterior of the windmill at night, under attack"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The Horseman chops at the door with his axe.
  EXPRESSION: null

::PATHS::
- CHOICE: "Return to interior"
  TARGET: windmill_interior_night_2
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Windmill Interior
MOOD: Panicked Ingenuity
CHARACTERS: Narrator, Katrina, Young Masbath, Ichabod
BACKGROUND_IMAGE: windmill_interior_night_2.png
BACKGROUND_EDIT: "Interior of the windmill, interior attack from below"

::SCRIPT::
- CHARACTER: Narrator
  LINE: POUNDING CONTINUES, Katrina and Young Masbath back away. Ichabod holds his lantern up, desperate for ideas, searching. Above, to the right, is the high MILLING PLATFORM, where grain is ground and bagged, and a ladder leading to it. To the left is the crooked, open STAIRCASE.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Ichabod picks up a BAILING HOOK, a plan forming. He gives his lantern to Katrina and points.
  EXPRESSION: null
- CHARACTER: Ichabod
  LINE: Get up these stairs. Open the door to the roof and wait.
  EXPRESSION: Urgent
- CHARACTER: Narrator
  LINE: Katrina and Young Masbath obey, heading left. Ichabod crosses to the right, starts climbing the ladder to the milling platform... On the platform, Ichabod grasps a wooden lever, pulling it. The entire windmill CREAKS and GROANS as massive GEARS and COUNTERWHEELS above begin to turn.
  EXPRESSION: null

::PATHS::
- CHOICE: "Activate the windmill"
  TARGET: windmill_exterior_night_2
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Windmill Exterior
MOOD: Machinery in Motion
CHARACTERS: Narrator, Horseman
BACKGROUND_IMAGE: windmill_exterior_night_2.png
BACKGROUND_EDIT: "Exterior of the windmill at night, rotors beginning to spin"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The windmill's rotors slowly begin spinning. Under the windmill, the Horseman keeps chopping... His axe exposes grindstone, throwing sparks.
  EXPRESSION: null

::PATHS::
- CHOICE: "Observe from inside"
  TARGET: windmill_interior_night_3
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Windmill Interior
MOOD: Heightened Danger
CHARACTERS: Narrator, Katrina, Ichabod
BACKGROUND_IMAGE: windmill_interior_night_3.png
BACKGROUND_EDIT: "Interior of the windmill, grindstone shaking"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Katrina looks down from the stairway. The POUNDING on the trap door causes the grindstone to jump.
  EXPRESSION: null
- CHARACTER: Katrina
  LINE: Ichabod...
  EXPRESSION: Alarmed
- CHARACTER: Ichabod
  LINE: Keep climbing. I will follow... Hopefully.
  EXPRESSION: Determined, but uncertain
- CHARACTER: Narrator
  LINE: Ichabod drags large BAGS of GRAIN, lining them up at the edge of the milling platform. Above, Young Masbath throws open the door to the roof. Below, Ichabod uses the bailing hook to cut holes into the grain bags, so that MILLED GRAIN SPILLS out and falls to the floor, creating clouds of grain dust. Ichabod grabs one open bag, dumps it. He slices into a sack hanging from a pulley system, pushes it so it swings in circles, grain flooding out... More and more DUST RISES, filling the air...
  EXPRESSION: null

::PATHS::
- CHOICE: "Go to the roof"
  TARGET: windmill_roof_night
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Windmill Roof
MOOD: Precarious Escape
CHARACTERS: Narrator, Katrina, Young Masbath, Ichabod
BACKGROUND_IMAGE: windmill_roof_night.png
BACKGROUND_EDIT: "Rooftop of the windmill at night, with spinning rotors"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Masbath and Katrina come out. Rotors spin behind them.
  EXPRESSION: null

::PATHS::
- CHOICE: "Return to interior"
  TARGET: windmill_interior_night_4
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Windmill Interior
MOOD: Violent Incursion
CHARACTERS: Narrator, Katrina, Ichabod, Horseman
BACKGROUND_IMAGE: windmill_interior_night_4.png
BACKGROUND_EDIT: "Interior of the windmill, trapdoor broken open"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The GRINDSTONE blocking the trap door FALLS THROUGH as wood splinters and gives. A moment, then the Horseman climbs in.
  EXPRESSION: null
- CHARACTER: Katrina
  LINE: Behind you!
  EXPRESSION: Warning
- CHARACTER: Narrator
  LINE: Ichabod looks down, sees the Horseman, then looks to the staircase adjacent from the high platform. He runs... He LEAPS across the space between the platform and stairs... Ichabod grasps the outer rail of the staircase, hanging on, pulls himself up onto the stairs... Below, the Horseman moves through clouds of billowing dust, runs and LEAPS, incredibly high... The Horseman grasps a hanging chain, swinging, his momentum carrying him in a wide arc... Above, Ichabod runs upstairs, to the roof door. The Horseman's weight swings him toward the stairwell... He releases the chain... airborne momentarily... The Horseman lands high up on the stairwell.
  EXPRESSION: null

::PATHS::
- CHOICE: "Escape to the roof"
  TARGET: windmill_roof_night_2
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Windmill Roof
MOOD: Desperate Measures
CHARACTERS: Narrator, Katrina, Young Masbath, Ichabod
BACKGROUND_IMAGE: windmill_roof_night_2.png
BACKGROUND_EDIT: "Rooftop of the windmill at night, rotors spinning rapidly"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Katrina and Young Masbath help Ichabod onto the roof.
  EXPRESSION: null
- CHARACTER: Katrina
  LINE: Quickly, close it!
  EXPRESSION: Panicked
- CHARACTER: Ichabod
  LINE: No...
  EXPRESSION: Resolute
- CHARACTER: Narrator
  LINE: Ichabod takes the lantern from Katrina.
  EXPRESSION: null
- CHARACTER: Ichabod
  LINE: Get to the crest of the roof and be ready to jump.
  EXPRESSION: Urgent
- CHARACTER: Young Masbath
  LINE: Jump? From up here?!
  EXPRESSION: Shocked
- CHARACTER: Narrator
  LINE: Ichabod shepherds Katrina and Young Masbath to the edge, where the rotors spin close.
  EXPRESSION: null
- CHARACTER: Ichabod
  LINE: Jump for the sails! Wait till I give the word!
  EXPRESSION: Commanding
- CHARACTER: Katrina
  LINE: Ichabod!... I can't...
  EXPRESSION: Terrified
- CHARACTER: Ichabod
  LINE: Yes, you can, my love -- hand in hand...
  EXPRESSION: Reassuring
- CHARACTER: Narrator
  LINE: Ichabod moves back to the trap door. Katrina and Young Masbath look at the rotors, and down at the long distance between them and the ground.
  EXPRESSION: null
- CHARACTER: Ichabod
  LINE: Be ready...
  EXPRESSION: Tense
- CHARACTER: Narrator
  LINE: Ichabod DROPS the LANTERN into the windmill and runs...
  EXPRESSION: null
- CHARACTER: Ichabod
  LINE: Now!
  EXPRESSION: Urgent

::PATHS::
- CHOICE: "Jump from the roof"
  TARGET: windmill_interior_night_5
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Windmill Interior
MOOD: Inferno
CHARACTERS: Narrator, Horseman
BACKGROUND_IMAGE: windmill_interior_night_5.png
BACKGROUND_EDIT: "Interior of the windmill consumed by fire"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The Horseman continues up. The lantern falls past...
  EXPRESSION: null

::PATHS::
- CHOICE: "Watch the exterior"
  TARGET: windmill_roof_night_3
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Windmill Roof
MOOD: Chaotic Escape
CHARACTERS: Narrator, Young Masbath, Ichabod, Katrina
BACKGROUND_IMAGE: windmill_roof_night_3.png
BACKGROUND_EDIT: "Rooftop of the windmill, raining debris and flames"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Young Masbath jumps. Ichabod grips Katrina, jumps... They hit one rotor, gripping the frame and cloth as the rotor begins its DOWNWARD TURN...
  EXPRESSION: null

::PATHS::
- CHOICE: "Descend with the rotor"
  TARGET: windmill_interior_night_6
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Windmill Interior
MOOD: Cataclysmic Blaze
CHARACTERS: Narrator, Horseman
BACKGROUND_IMAGE: windmill_interior_night_6.png
BACKGROUND_EDIT: "Interior of the windmill, engulfed in flames"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The lantern hits the ground and shatters -- FLAMES EXPLODE! Throughout the windmill's interior, grain dust is consumed instantaneously -- FLAMES ROAR upward... FLAMES engulf the Horseman...
  EXPRESSION: null

::PATHS::
- CHOICE: "Observe the aftermath"
  TARGET: windmill_exterior_night_3
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Windmill Exterior
MOOD: Devastation
CHARACTERS: Narrator, Ichabod, Katrina, Young Masbath
BACKGROUND_IMAGE: windmill_exterior_night_3.png
BACKGROUND_EDIT: "Exterior of the burning windmill, collapsing structure"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The rotor is halfway to its lowest point. Masbath, Katrina and Ichabod hang on as the ENTIRE STRUCTURE TREMBLES... Flames shoot out windows, doors and seams! On the rotor, Ichabod struggles to keep a grip on Katrina. Masbath drops. Ichabod and Katrina fall... They all hit the ground. Ichabod rolls over, gasping, holding his shoulders, getting to his feet... Ichabod, Katrina and Young Masbath run away as smoldering debris rains down.
  EXPRESSION: null

::PATHS::
- CHOICE: "Flee the scene"
  TARGET: across_field_night
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Across the Field
MOOD: Temporary Respite
CHARACTERS: Narrator, Ichabod, Katrina, Young Masbath
BACKGROUND_IMAGE: across_field_night.png
BACKGROUND_EDIT: "Open field at night, with lightning and thunder"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Ichabod ushers them along as they run, heading uphill. Lightning flashes across the sky. Thunder rumbles.
  EXPRESSION: null

::PATHS::
- CHOICE: "Look back at the windmill"
  TARGET: windmill_night_2
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Windmill
MOOD: Destruction
CHARACTERS: Narrator
BACKGROUND_IMAGE: windmill_night_2.png
BACKGROUND_EDIT: "The windmill collapsing in flames"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Behind, the WINDMILL begins to CRUMBLE, huge burning sections crashing to the ground.
  EXPRESSION: null

::PATHS::
- CHOICE: "Observe the destruction"
  TARGET: across_field_night_2
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Across the Field
MOOD: Awe and Uncertainty
CHARACTERS: Narrator, Ichabod, Katrina, Young Masbath
BACKGROUND_IMAGE: across_field_night_2.png
BACKGROUND_EDIT: "Open field at night, looking back at the burning windmill rubble"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Ichabod, Katrina and Young Masbath slow, looking back at the incredible conflagration.
  EXPRESSION: null
- CHARACTER: Young Masbath
  LINE: Is he dead?
  EXPRESSION: Hopeful, but fearful
- CHARACTER: Ichabod
  LINE: He was dead to start with -- that's the problem.
  EXPRESSION: Grim
- CHARACTER: Katrina
  LINE: Look...
  EXPRESSION: Astonished

::PATHS::
- CHOICE: "Witness the Horseman's return"
  TARGET: windmill_night_3
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Windmill
MOOD: Unkillable
CHARACTERS: Narrator, Horseman
BACKGROUND_IMAGE: windmill_night_3.png
BACKGROUND_EDIT: "Windmill rubble, the Horseman rising from the ashes"

::SCRIPT::
- CHARACTER: Narrator
  LINE: IN THE WINDMILL RUBBLE, the Horseman RISES, shoving off burning debris. His flame-ravaged uniform smolders.
  EXPRESSION: Terrified

::PATHS::
- CHOICE: "Flee towards the coach"
  TARGET: across_field_night_3
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Across the Field
MOOD: Renewed Flight
CHARACTERS: Narrator, Ichabod, Katrina, Young Masbath
BACKGROUND_IMAGE: across_field_night_3.png
BACKGROUND_EDIT: "Open field at night, spotting the coach"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Ichabod spins, searching for possibilities... He spots the COACH and HORSES not too far away...
  EXPRESSION: Hopeful
- CHARACTER: Ichabod
  LINE: Come on!
  EXPRESSION: Urgent
- CHARACTER: Narrator
  LINE: They flee toward the coach. Behind... Daredevil rides to rejoin the Horseman.
  EXPRESSION: null

::PATHS::
- CHOICE: "Escape in the coach"
  TARGET: road_van_tassel_estate_night
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: The Road from Van Tassel Estate
MOOD: Desperate Chase
CHARACTERS: Narrator, Katrina, Young Masbath, Ichabod, Horseman
BACKGROUND_IMAGE: road_van_tassel_estate_night.png
BACKGROUND_EDIT: "A dark road at night, coach fleeing"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The coach hits the long straight road, rumbling at top speed away from the Van Tassel Estate, into the forest... Katrina and Masbath hold on as the coach shakes violently.
  EXPRESSION: null
- CHARACTER: Katrina
  LINE: Where are we going?
  EXPRESSION: Anxious
- CHARACTER: Ichabod
  LINE: Anywhere!
  EXPRESSION: Desperate
- CHARACTER: Young Masbath
  LINE: He's right behind!
  EXPRESSION: Terrified
- CHARACTER: Narrator
  LINE: Behind on the trail, the Horseman chases, closing fast.
  EXPRESSION: null
- CHARACTER: Katrina
  LINE: Make for the church!
  EXPRESSION: Hopeful
- CHARACTER: Ichabod
  LINE: We'll never reach it!
  EXPRESSION: Resigned
- CHARACTER: Narrator
  LINE: Young Masbath grabs Ichabod's satchel, offers it...
  EXPRESSION: null
- CHARACTER: Young Masbath
  LINE: Here, sir... you must have something in your bag of tricks.
  EXPRESSION: Hopeful
- CHARACTER: Ichabod
  LINE: Nothing that will help us, I am afraid. Take the reins...
  EXPRESSION: Grim
- CHARACTER: Narrator
  LINE: Young Masbath takes them. Ichabod gives Van Ripper's rifle to Katrina, then crawls back across the coach roof. Ichabod gets to a baggage area at the rear, struggling to open a storage box. Behind, the Horseman draws his sword, closer. Ichabod opens the box a
  EXPRESSION: null

::PATHS::
- CHOICE: "See what's in the box"
  TARGET: coach_interior_night
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Behind the Trail
MOOD: Action
CHARACTERS: Narrator, Katrina, Ichabod, Horseman
BACKGROUND_IMAGE: trail_background.png
BACKGROUND_EDIT: "Jagged hand saw, coach, Horseman with sword"

::SCRIPT::
- CHARACTER: Narrator
  LINE: and pulls out a jagged HAND SAW.
  EXPRESSION: null
- CHARACTER: Katrina
  LINE: Look out...!
  EXPRESSION: Fear
- CHARACTER: Narrator
  LINE: Ichabod looks. The Horseman rides up, SWINGS his sword...
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Ichabod recoils -- THWACK -- just missed.
  EXPRESSION: Surprise
- CHARACTER: Narrator
  LINE: The Horseman lets the coach get ahead, shifting to the other side of the trail... coming along side again...
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Ichabod backpedals, looking to Masbath.
  EXPRESSION: Fear
- CHARACTER: Ichabod
  LINE: Keep him off! Block him!
  EXPRESSION: Desperate
- CHARACTER: Narrator
  LINE: Masbath guides the horses over. The Horseman must fall behind to avoid the wheels.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: One wheel hits a large rock...
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Ichabod bounces, falling, drops the saw...
  EXPRESSION: Shock
- CHARACTER: Narrator
  LINE: He hangs off the side of the coach.
  EXPRESSION: Danger
- CHARACTER: Narrator
  LINE: The saw clatters away on the trail.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Ichabod tries for better purchase. He grips the coach door.
  EXPRESSION: Desperate
- CHARACTER: Narrator
  LINE: Katrina climbs to offer her hand.
  EXPRESSION: Hope
- CHARACTER: Katrina
  LINE: Take my hand!
  EXPRESSION: Urgent
- CHARACTER: Narrator
  LINE: Ichabod reaches to her, but the coach door falls open...
  EXPRESSION: Despair
- CHARACTER: Narrator
  LINE: Ichabod's PISTOL falls from the holster and is lost on the trail.
  EXPRESSION: null
- CHARACTER: Narrator
  LINE: Ichabod clings helplessly to the door as branches slam him.
  EXPRESSION: Pain

::PATHS::
- CHOICE: "Continue clinging to the door"
  TARGET: ahead_on_trail
  STATE_CHANGE: HP = -10, fear = +5
  CONDITION: null

::SCENE::
LOCATION: Behind the Trail
MOOD: Ominous
CHARACTERS: Narrator, Horseman, Daredevil
BACKGROUND_IMAGE: behind_trail.png
BACKGROUND_EDIT: "Horseman getting up, Daredevil screeching"

::SCRIPT::
- CHARACTER: Narrator
  LINE: The Horseman gets to his feet. Ahead, Daredevil stands waiting, giving a SCREECH.
  EXPRESSION: null

::PATHS::
- CHOICE: "Move towards the sound"
  TARGET: ahead_on_trail
  STATE_CHANGE: null
  CONDITION: null

::SCENE::
LOCATION: Ahead on the Trail Near the Tree of the Dead
MOOD: Panicked
CHARACTERS: Narrator, Katrina, Ichabod, Young Masbath
BACKGROUND_IMAGE: near_tree_of_dead.png
BACKGROUND_EDIT: "Ruined coach wheel, characters examining it"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Katrina and Ichabod rejoin Mashath, climb off the coach to examine the ruined wheel, panicked.
  EXPRESSION: null
- CHARACTER: Ichabod
  LINE: This is not good.
  EXPRESSION: Worried
- CHARACTER: Young Masbath
  LINE: We're doomed.
  EXPRESSION: Hopeless
- CHARACTER: Ichabod
  LINE: We have to get out of the open somehow. Quick, follow me...
  EXPRESSION: Determined
- CHARACTER: Narrator
  LINE: They turn to run, but suddenly falter, seeing... Riding over the crest of the hill, comes Lady Van Tassel, on her white horse, with Ichahod's lost pistol in her hand...
  EXPRESSION: Shocked

::PATHS::
- CHOICE: "Confront Lady Van Tassel"
  TARGET: near_forest
  STATE_CHANGE: fear = +10, danger = +10
  CONDITION: null

::SCENE::
LOCATION: Near Forest
MOOD: Confrontational
CHARACTERS: Narrator, Lady Van Tassel, Horseman, Katrina, Ichabod
BACKGROUND_IMAGE: near_forest.png
BACKGROUND_EDIT: "Lady Van Tassel on white horse with pistol, Horseman approaching"

::SCRIPT::
- CHARACTER: Lady Van Tassel
  LINE: What? Still alive?!
  EXPRESSION: Malicious
- CHARACTER: Narrator
  LINE: Across the distance, the Horseman strides in this direction.
  EXPRESSION: Ominous
- CHARACTER: Ichabod
  LINE: Run, Katrina...
  EXPRESSION: Urgent
- CHARACTER: Lady Van Tassel
  LINE: Yes, do run. And jump. And skip. And now let's see a somersault!
  EXPRESSION: Mocking
- CHARACTER: Narrator
  LINE: Lady Van Tassel points her gun at Katrina.
  EXPRESSION: Threatening
- CHARACTER: Ichabod
  LINE: Run!
  EXPRESSION: Desperate
- CHARACTER: Narrator
  LINE: Ichahod makes a move toward Lady Van Tassel, but Lady Van Tassel aims and FIRES -- shoots Ichahod in the chest! Ichahod goes down...
  EXPRESSION: Violence
- CHARACTER: Katrina
  LINE: No!
  EXPRESSION: Grief
- CHARACTER: Narrator
  LINE: Young Masbath cries out, falls to his knees beside Ichabod. Katrina moves toward Ichahod... Lady Van Tassel rides forward -- GRABS Katrina by the hair, PULLING HER, riding off toward the Horseman... Ichabod lays clutching the smoldering wound in his chest, gasping. Young Masbath holds him...
  EXPRESSION: Cruelty
- CHARACTER: Young Masbath
  LINE: Oh, God... no... no...
  EXPRESSION: Devastated
- CHARACTER: Narrator
  LINE: Lady Van Tassel drags Katrina by the hair as Katrina screams and struggles and kicks.
  EXPRESSION: Brutal
- CHARACTER: Narrator
  LINE: The Horseman keeps coming...
  EXPRESSION: Inevitable
- CHARACTER: Narrator
  LINE: Lady Van Tassel stops her horse, halfway to the Horseman, drops Katrina and starts riding back, shouting...
  EXPRESSION: Manipulative
- CHARACTER: Lady Van Tassel
  LINE: There she is. Take her, she's yours!
  EXPRESSION: Cruel
- CHARACTER: Narrator
  LINE: Katrina gets up to run, stumbles, falls...
  EXPRESSION: Vulnerable
- CHARACTER: Narrator
  LINE: The Horseman strides after...
  EXPRESSION: Relentless
- CHARACTER: Narrator
  LINE: Up the field, Ichabod gets to his knees, feeling his chest with both hands, not quite understanding, struggling to shake off delirium...
  EXPRESSION: Pain
- CHARACTER: Young Masbath
  LINE: Sir, you're... you're not dead...
  EXPRESSION: Amazed
- CHARACTER: Ichabod
  LINE: Not... yet...
  EXPRESSION: Determined
- CHARACTER: Narrator
  LINE: Ichabod looks up, trying to comprehend... Lady Van Tassel had turned her horse, her back to us, keeping her distance from the Horseman. Beyond her, Katrina flees this direction with the Horseman at her heels.
  EXPRESSION:null
- CHARACTER: Narrator
  LINE: Ichabod's focused on something... The black SADDLEBAG slung over Lady Van Tassel's horse.
  EXPRESSION: Realization
- CHARACTER: Narrator
  LINE: Ichabod rises out of pure determination, runs...
  EXPRESSION: Determined
- CHARACTER: Narrator
  LINE: Katrina runs... the Horseman is closing on her.
  EXPRESSION: Danger
- CHARACTER: Narrator
  LINE: Lady Van Tassel watches, grinning, but at the last second something catches her eye and she turns, just as...
  EXPRESSION: Shocked
- CHARACTER: Narrator
  LINE: Ichabod LEAPS... TACKLES Lady Van Tassel off of her horse, taking her down to the ground HARD... her bag falling open...
  EXPRESSION: Violent
- CHARACTER: Narrator
  LINE: The Horseman's skull rolling out...
  EXPRESSION: Horrifying
- CHARACTER: Narrator
  LINE: Ichabod scrambles toward the skull -- but falls, halted. Lady Van Tassel grips his leg, holding him.
  EXPRESSION: Trapped
- CHARACTER: Narrator
  LINE: Young Masbath grabs a heavy, broken TREE LIMB off the ground.
  EXPRESSION: Hopeful
- CHARACTER: Narrator
  LINE: The Horseman is mere yards behind Katrina...
  EXPRESSION: Imminent
- CHARACTER: Narrator
  LINE: Ichabod struggles to get free from Lady Van Tassel, can't break her grip when, BANG -- Young Masbath SMASHES Lady Van Tassel over the head with the tree limb. She's out.
  EXPRESSION: Violence
- CHARACTER: Narrator
  LINE: The Horseman catches Katrina...
  EXPRESSION: Devastating
- CHARACTER: Narrator
  LINE: Ichabod scrambles free, running, reaching for the skull... grasping it...
  EXPRESSION: Determined
- CHARACTER: Narrator
  LINE: The Horseman holds Katrina ready by her hair as she falls to her knees, screaming and struggling. The Horseman raises his sword...
  EXPRESSION: Cruel
- CHARACTER: Narrator
  LINE: Ichabod rises, THROWS the skull with all his might...
  EXPRESSION: Desperate
- CHARACTER: Ichabod
  LINE: Horseman!
  EXPRESSION: Defiant
- CHARACTER: Narrator
  LINE: The skull spins through the air...
  EXPRESSION:null
- CHARACTER: Narrator
  LINE: The Horseman suddenly drops Katrina, reaches up with one hand... catches the skull.
  EXPRESSION: Surprise
- CHARACTER: Narrator
  LINE: Katrina runs. Ichabod runs to meet her, grabs her as she falls.
  EXPRESSION: Relief
- CHARACTER: Narrator
  LINE: Together, they back away from the Horseman...
  EXPRESSION: Fearful
- CHARACTER: Narrator
  LINE: The Horseman holds the skull out... brings it to his shoulders, to its rightful place. THUNDER POUNDS.
  EXPRESSION: Transformative
- CHARACTER: Narrator
  LINE: TRANSFORMATION begins -- blood and flesh rise up from the Horseman's throat and grip the skull...
  EXPRESSION: Gruesome
- CHARACTER: Narrator
  LINE: The Horseman's reformation continues. Muscle forms. Liquids become solids. He is made whole once more, the same evil, human face we saw in Baltus's stories.
  EXPRESSION: Horrifying
- CHARACTER: Narrator
  LINE: The Horseman looks to Ichabod and Katrina, touches his restored face.
  EXPRESSION: Vengeful
- CHARACTER: Narrator
  LINE: Daredevil rides up, SCREECHING. The Horseman replaces his sword, climbs into the saddle.
  EXPRESSION:null
- CHARACTER: Narrator
  LINE: He rides toward Katrina and Ichabod, but he does not want them. They are so exhausted they fall down. Young Masbath comes to stand with them.
  EXPRESSION:null
- CHARACTER: Narrator
  LINE: The Horseman leans to grab Lady Van Tassel's unconscious form, pulls her up across Daredevil's back.
  EXPRESSION:null
- CHARACTER: Narrator
  LINE: The Horseman rides away with her.
  EXPRESSION:null
- CHARACTER: Narrator
  LINE: Ichabod and Katrina watch him go. They look at each other, then kiss gratefully. Ichabod looks to Young Masbath...
  EXPRESSION: Relief
- CHARACTER: Ichabod
  LINE: How are you, Young Masbath?
  EXPRESSION: Concerned
- CHARACTER: Young Masbath
  LINE: Weary, sir.
  EXPRESSION: Tired
- CHARACTER: Narrator
  LINE: Ichabod holds out his arm. Masbath comes over. They embrace. Katrina touches the burned bullet hole in Ichabod's clothing.
  EXPRESSION: Emotional
- CHARACTER: Katrina
  LINE: I thought I had lost you.
  EXPRESSION: Relieved
- CHARACTER: Narrator
  LINE: Ichabod reaches into his clothing, takes out a BOOK he kept in an inner pocket close to his heart... The BOOK OF SPELLS with a bullet lodged in it.
  EXPRESSION: Miraculous
- CHARACTER: Narrator
  LINE: Katrina wraps her arms around Ichabod.
  EXPRESSION: Affectionate

::PATHS::
- CHOICE: "Reflect on survival"
  TARGET: western_woods_tree_of_dead_night
  STATE_CHANGE: fear = -10, relief = +10
  CONDITION: null

::SCENE::
LOCATION: Western Woods - Tree of the Dead
MOOD: Eerie
CHARACTERS: Narrator, Horseman, Lady Van Tassel, Daredevil
BACKGROUND_IMAGE: western_woods_tree_of_dead.png
BACKGROUND_EDIT: "Horseman entering clearing with Lady Van Tassel, Tree of the Dead"

::SCRIPT::
- CHARACTER: Narrator
  LINE: HOOFBEATS.
  EXPRESSION:null
- CHARACTER: Narrator
  LINE: The Horseman enters the clearing, holding on to Lady Van Tassel.
  EXPRESSION:null
- CHARACTER: Narrator
  LINE: Ahead, the Tree of the dead awaits.
  EXPRESSION:null
- CHARACTER: Narrator
  LINE: Lady Van Tassel is awakening...
  EXPRESSION: Fear
- CHARACTER: Narrator
  LINE: The Horseman grips Lady Van Tassel's hair, pulling her face up closer to his, just as she opens her eyes...
  EXPRESSION: Threatening
- CHARACTER: Lady Van Tassel
  LINE: Lady Van Tassel screams...
  EXPRESSION: Terror
- CHARACTER: Narrator
  LINE: As the Horseman brings his face to meet hers, about to engage in a KISS, his jagged teeth open wide.
  EXPRESSION: Gruesome
- CHARACTER: Narrator
  LINE: Ahead, the twisted tree's wound opens, deep and glowing, as Daredevil picks up speed.
  EXPRESSION: Ominous

::PATHS::
- CHOICE: "Witness the end"
  TARGET: western_woods_tree_of_dead_night_2
  STATE_CHANGE: dread = +10
  CONDITION: null

::SCENE::
LOCATION: Western Woods - Tree of the Dead
MOOD: Supernatural
CHARACTERS: Narrator, Daredevil, Horseman, Lady Van Tassel
BACKGROUND_IMAGE: western_woods_tree_of_dead_2.png
BACKGROUND_EDIT: "Daredevil jumping, lightning striking, Horseman entering tree"

::SCRIPT::
- CHARACTER: Narrator
  LINE: Daredevil JUMPS in the air just as a LIGHTNING BOLT blasts down from the sky, striking the Horseman...
  EXPRESSION: Dramatic
- CHARACTER: Narrator
  LINE: For an instant, Horseman and horse are transformed, SKELETONS OF LIGHT, entering the tree!
  EXPRESSION: Supernatural
- CHARACTER: Narrator
  LINE: Silence and smoke.
  EXPRESSION: Still
- CHARACTER: Narrator
  LINE: At the tree, Lady Van Tassel's hand sticks out from the tight-shut suture.
  EXPRESSION: Horrifying
- CHARACTER: Narrator
  LINE: The sewn wound on her palm seeps blood as her fingers curl.
  EXPRESSION: Gruesome

::PATHS::
- CHOICE: "Observe the aftermath"
  TARGET: new_york_city_street_ichabods_home
  STATE_CHANGE: shock = +10
  CONDITION: null

::SCENE::
LOCATION: New York City Street - Ichabod's Home
MOOD: Peaceful
CHARACTERS: Narrator, Ichabod, Katrina, Young Masbath, Cat
BACKGROUND_IMAGE: nyc_street.png
BACKGROUND_EDIT: "Coach arriving at Ichabod's home, snow falling"

::SCRIPT::
- CHARACTER: Narrator
  LINE: A coach pulls up to Ichabod's home. Ichabod is the driver.
  EXPRESSION:null
- CHARACTER: Narrator
  LINE: He gets off, goes and opens the coach door. He helps Katrina down.
  EXPRESSION:null
- CHARACTER: Narrator
  LINE: Next, Young Masbath sticks his head out.
  EXPRESSION:null
- CHARACTER: Narrator
  LINE: Katrina holds Young Masbath's hand. Ichabod comes to hold Katrina's hand.
  EXPRESSION:null
- CHARACTER: Narrator
  LINE: A STRAY CAT watches them --
  EXPRESSION:null
- CHARACTER: Narrator
  LINE: Young Masbath looks entranced at the BUSTLING METROPOLIS.
  EXPRESSION: Amazed
- CHARACTER: Young Masbath
  LINE: Oh, my!
  EXPRESSION: Awestruck
- CHARACTER: Katrina
  LINE: And cobbled streets!
  EXPRESSION: Impressed
- CHARACTER: Ichabod
  LINE: Yes... New York, New York! Just in time for the new century! It's the modern age, Katrina!
  EXPRESSION: Proud
- CHARACTER: Katrina
  LINE: It's always the modern age, Ichabod ... but the ancient ones endure.
  EXPRESSION: Wise
- CHARACTER: Narrator
  LINE: Large snowflakes begin to fall upon the scene.
  EXPRESSION:null
- CHARACTER: Narrator
  LINE: Ichabod puts an arm around Katrina and the other arm around Masbath.
  EXPRESSION: Affectionate
- CHARACTER: Narrator
  LINE: The CAT is black with one white paw... the Cat from Ichabod's dreams... The CAT turns to look at the trio.
  EXPRESSION: Mysterious
- CHARACTER: Narrator
  LINE: ECU -- The CAT'S EYES ARE HUMAN, INTELLIGENT, KINDLY... They are Ichabod's Mother's eyes.
  EXPRESSION: Profound
- CHARACTER: Narrator
  LINE: Ichabod, Katrina and Young Masbath enter Ichabod's house, as the SNOW continues to fall.
  EXPRESSION: Peaceful

::PATHS::
- CHOICE: "End the story"
  TARGET: end
  STATE_CHANGE: null
  CONDITION: null

