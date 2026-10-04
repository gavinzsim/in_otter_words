
# CHARACTERS

# Characters
define y = Character("Yinny")
define s = Character("Stormy")

# Backgrounds
image bg city = "images/city.png"
image bg bathroom = "images/bathroom.png"
image bg campus = "images/campus.png"
image bg bedroom = "images/bedroom.png"

# Characters
image yinny = "images/yinny.webp"
image stormy = "images/stormy.webp"

# VARIABLES

default snooze_count = 0


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

    "BEEP. BEEP. BEEP."

    y "..."

    y "No."

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

            y "How is five minutes already over?"

            jump wake_up


# SNOOZE ENDING

label snooze_ending:

    scene black
    with fade

    "Several hours later..."

    y "..."

    y "WAIT."

    y "WHAT TIME IS IT?!"

    centered "ENDING UNLOCKED"

    centered "\"You Snooze, You Lose\""

    centered "Yinny successfully avoided both responsibility and the plot."

    pause 3.0

    return


# GETTING READY

label get_up:

    scene bg bedroom
    with dissolve

    y "Fine. I'm awake."

    y "Technically."

    scene bg bathroom
    with fade

    "Yinny turns on the sink."

    "The water comes out slightly brown."

    y "..."

    y "Huh."

    y "A little browner than yesterday."

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

    y "Alright. New day."

    y "Fresh air."

    pause 0.5

    y "Mostly fresh."

    "Plastic bags tumble across the sidewalk."

    "A bottle rolls past Yinny."

    y "Morning."

    "The bottle continues rolling."

    y "Rude."

    "Yinny takes another step."

    scene black
    with hpunch

    "FWOOOOSH!"

    y "HUH?!"

    "A mountain of garbage collapses on top of Yinny."

    y "MMMPH!"

    y "WHY IS THERE A WHOLE CHAIR IN HERE?!"

    s "Yinny?"

    s "Is that you?"

    y "NO."

    y "I'M THE GARBAGE."

    s "Hang on."

    "Stormy starts pulling bags away."

    scene bg city
    with dissolve

    show stormy

    s "There."

    s "You alive?"

    y "Physically?"

    y "Probably."

    s "Good enough."


# STORMY CONVERSATION

label stormy_intro:

    s "This is getting ridiculous."

    y "The garbage?"

    s "The garbage."

    s "The water."

    s "The air."

    s "Yesterday I saw a fish swimming around a shopping cart."

    y "Maybe it was moving."

    s "Yinny."

    y "Right. Environmental disaster."

    s "Everyone just keeps acting like this is normal."

    "Yinny looks around."

    "Trash covers the street."

    "The water flowing into a nearby drain has a suspicious green tint."

    "Nobody else seems particularly concerned."

    y "..."

    y "I guess I never really thought about it."

    s "Well?"

    s "Are you going to?"

    menu:
        "Try to do something about it":
            jump choose_help

        "It's probably not my problem":
            jump trash_ending


# IGNORE EVERYTHING ENDING

label trash_ending:

    y "Honestly..."

    y "Someone else will probably deal with it."

    s "Seriously?"

    y "I'm just one otter."

    y "What am I supposed to do?"

    s "..."

    y "Anyway, see you later!"

    hide stormy

    "Yinny continues walking."

    "They carefully step around several garbage bags."

    "Then around a broken television."

    "Then around another pile of garbage."

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

    y "..."

    y "Okay."

    y "Maybe you're right."

    s "I usually am."

    y "Let's not get carried away."

    s "So you'll help?"

    y "Yeah."

    y "I don't exactly know how..."

    y "But this can't just keep being normal."

    s "That's a start."

    y "So where do we even begin?"

    s "I might know some people."

    y "That sounds suspicious."

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

    y "Alright."

    y "Let's go save the world."

    s "Maybe start with the neighborhood."

    y "Less dramatic."

    s "Much more achievable."

    y "Fine."

    y "Let's go mildly improve the world."

    # Later:
    # jump trendy_arc

    centered "End of Opening Demo"

    return

    return
