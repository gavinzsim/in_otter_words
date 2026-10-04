
# CHARACTERS

# Characters
define y = Character("Yinny")
define s = Character("Stormy")
define sp = Character("Sparky")

# Backgrounds
image bg city = "images/dirty_city.png"
image bg bathroom = "images/bathroom.png"
image bg campus = "images/campus.png"
image bg bedroom = "images/yinny_bedroom.png"
image bg livingroom = "images/act4_living.jpg"
image bg park = "images/park.png"
image bg river = "images/dirty_river.png"


# Characters
image yinny = "images/yinny_otter.png"
image stormy = "images/Stormy_Normal.png"
image StormyAnnoyedSpeaking = "images/Stormy_Annoyed_Speaking.png"
image StormyAnnoyed = "images/Stormy_Annoyed.png"
image StormyHappy = "images/Stormy_Happy.png"
image StormyHappySpeaking = "images/Stormy_Happy_Speaking.png"
image StormyNormal = "images/Stormy_Normal.png"
image StormySpeaking = "images/Stormy_Speaking.png"
image StormyShocked = "images/Stormy_Shocked.png"
image garbage_pile = "images/garbage_pile.png"
image sparky = "images/Sparky_Normal.png"
image SparkyHappy = "images/Sparky_Happy.png"
image SparkyWorried = "images/Sparky_Annoyed.png"
image SparkySad = "images/Sparky_Sad.png"


# Yinny's canvas includes visual space beneath her feet; offset it downward so
# the visible sprite baseline matches Stormy's.
transform yinny_left:
    xalign 0.0
    yalign 1.0
    xoffset -75
    yoffset 200
    zoom 0.7

# Place Stormy slightly inward from the right edge and align the characters
# lower in the scene.
transform stormy_right:
    xalign 1.0
    yalign 1.0
    zoom 0.7

transform sparky_right:
    xalign 1.0
    yalign 1.0
    zoom 0.7



# VARIABLES

default snooze_count = 0
default cynicism = 0
default sparky_bond = 0



# GAME START

label start:

    scene black
    with fade

    centered "In Otter Words"

    pause 2.0

    centered "A perfectly normal day in a perfectly normal city."

    pause 1.5

    jump wake_up


# OPENING - ALARM

label wake_up:

    scene bg bedroom
    show yinny at yinny_left

    "BEEP. BEEP. BEEP."

    y "..."

    y "No, it's too early..."

    menu:
        "Get up":
            jump get_up

        "Snooze":
            $ snooze_count += 1

            if snooze_count >= 3:
                jump snooze_ending

            "Yinny smacks the alarm clock."

            scene black
            with fade

            pause 1.0

            scene bg bedroom
            with fade

            "BEEP. BEEP. BEEP."

            y "How is five minutes already over?!"

            jump wake_up


# SNOOZE ENDING

label snooze_ending:

    scene black
    with fade

    show yinny at yinny_left

    "Several hours later..."

    y "..."

    y "WAIT."

    y "WHAT TIME IS IT?!"

    centered "ENDING UNLOCKED"

    centered "\"You Snooze, You Lose\""

    centered "Yinny successfully avoided both responsibility and the plot."

    centered "Congrats, aren't you proud of yourself?"

    pause 3.0

    return


# GETTING READY

label get_up:

    scene bg bedroom
    with dissolve

    show yinny at yinny_left

    y "Fine. I'm awake... at least enough to function."

    scene bg bathroom
    with fade

    show yinny at yinny_left

    "Yinny turns on the sink."

    "The water comes out slightly brown."

    y "..."

    y "Huh... A little browner than yesterday."

    y "Probably fine."

    "Yinny brushes their teeth anyway."

    scene black
    with fade

    "After getting ready..."

    jump outside


# OUTSIDE

label outside:

    scene bg city
    with fade

    show yinny at yinny_left

    y "Alright. New day."

    y "Fresh air... *Inhales*..."

    pause 0.5

    y "Mostly fresh."

    "Plastic bags tumble across the sidewalk."

    "A bottle rolls past Yinny."

    y "Morning."

    "The bottle continues rolling."

    y "Rude."

    "Yinny starts to take another step forward."

    scene black
    with hpunch

    "Clitter. Clatter... CRASH!"
    with hpunch

    y "AAAAAHHHHHHH!?!"
    with hpunch

    "A mountain of garbage collapses on top of Yinny."

    y "MMMPH!"

    scene bg city
    with dissolve

    show garbage_pile at yinny_left

    y "WHY IS THERE A WHOLE CHAIR IN HERE?!"

    s "Yinny...?"

    s "Is that you?"

    y "No... *embarrassed*"

    y "...I'M THE GARBAGE, FEAR ME D:<"

    s "*Sighs* Hold on, Yinny."

    "Stormy starts pulling bags away."

    hide garbage_pile
    show yinny at yinny_left
    show stormy at stormy_right

    s "There."

    s "You alive?"

    y "Physically?"

    y "Probably. Mentally? Let's not talk about that."

    s "Good enough."


# STORMY CONVERSATION

label stormy_intro:

    s "This is getting ridiculous."

    y "The garbage?"

    s "The garbage."

    s "The water."

    s "The air."

    s "Yesterday I saw a fish swimming around a shopping cart."

    y "Maybe it was trying to get in on the seafood sales, it ain't cheap."

    s "... Yinny."

    y "Right. Environmental disaster."

    s "Everyone just keeps acting like this is normal. We all know it's not."

    "Yinny looks around."

    "Trash covers the street."

    "The water flowing into a nearby drain has a suspicious green tint."

    "Nobody else seems particularly concerned."

    y "..."

    y "I guess I never really thought about it."

    s "Well...?"

    s "Are you going to do anything?"

    menu:
        "Try to do something.":
            jump choose_help

        "It's not my problem":
            jump trash_ending


# IGNORE EVERYTHING ENDING

label trash_ending:

    y "Honestly..."

    y "Someone else will probably deal with it."

    s "Seriously?"

    y "I'm just one otter. What am I supposed to do?"

    s "..."

    y "Anyways, see you later!"

    hide stormy

    "Yinny continues walking."

    "They carefully step around several piles of litter..."

    "... ducking past a broken television..."

    "... then hopped over a pile of garbage."

    y "See?"

    y "Totally normal."

    scene black
    with fade

    centered "ENDING UNLOCKED"

    centered "\"One Man's Trash Is Another's Normal\""

    centered "Nothing changed."

    centered "Which, unfortunately, was the problem."

    pause 3.0

    return


# MAIN STORY BEGINS

label choose_help:

    y "... ... ... okay."

    y "Maybe you're right."

    s "I usually am."

    y "Let's not get carried away with that. You were only right on this."

    s "So you'll help?"

    y "Yeah... but I don't exactly know how."

    y "However, this can't just keep being the norm."

    s "That's a start."

    y "So where do we even begin?"

    s "I might know some people."

    y "That sounds suspicious. I hope you're not planning to take me out of my lack of sleep misery."

    s "You'll survive."

    y "You said that after digging me out of garbage."

    s "And I was right."

    scene black
    with fade

    centered "MAIN STORY"

    centered "Maybe one otter can't fix everything."

    centered "But one otter can start."

    pause 2.0

    jump main_story


# PLACEHOLDER FOR ARC 1

label main_story:

    scene bg city
    with fade

    show yinny at yinny_left
    show stormy at stormy_right

    y "Alright. Let's go save the world."

    s "Maybe start with the neighborhood."

    y "It's less dramatic, there's no flair."

    s "Much more achievable."

    y "Fine. Let's go about mildly improving the world."

    # Later:
    # jump trendy_arc

    centered "End of Opening Demo"

    jump act1

label act1:

    jump act1_start
















