
# CHARACTERS

# Characters
define y = Character("Yinny")
define s = Character("Stormy")
define sp = Character("Sparky")
define t = Character("Trendy")
define spe = Character("Spendy")

# Backgrounds
image bg city = "images/dirty_city.png"
image bg bathroom = "images/bathroom.png"
image bg campus = "images/campus.png"
image bg bedroom = "images/yinny_bedroom.png"
image bg livingroom = "images/act4_living.jpg"
image lab = "images/normal_stormy_lab.png"
image badLab = "images/destroyed_stormy_lab.png"
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
image StormySadSpeaking = "images/Stormy_Sad_Speaking.png"
image StormySad = "images/Stormy_Sad.png"
image StormyShocked = "images/Stormy_Shocked.png"
image TrendyHappy = "images/Trendy_Happy.png"
image SpendyHappy = "images/Spending_Happy.png"
image SparkyHappy = "images/Sparky_Happy.png"
image garbage_pile = "images/garbage_pile.png"

default machine_progress = 0
default correct_tools = 0
default wrong_tools = 0
default teamwork = 0
default safety = 0

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


#Placeholder for Act 4
# The game starts here.

label act4:
    scene bg livingroom
    with fade

    "Stormy sobs loudly as he runs away from his completed experiment."

    show StormyNormal
    s "As always, I'm all alone." 
    
    s "I just wanted to show everyone my talent."

    "He hops on the couch and cuddles with a strange new plushie"

    s "But of course no one actually cares."
    "Stormy continues to cry himself to sleep"
    
    "ding dong, ding dong"

    s "wait who's here?"

    s "I'm coming!"
    "Stormy wipes his tears and rushes to the door."

    s "Sniff sniff who's here"

    "Stormy opens the door and sees a familiar face."

    y "Hey I hope it's okay if I barge in here randomly."

    show StormyShocked
    s "Yinny!"

    s "You came!"

    y "What are you working on?"

    show StormyHappySpeaking
    s "Something incredible."

    y "That doesn't answer my question..."

    s "I'm building a new energy machine!"

    y "..."

    y "That sounds dangerous."

    s "Dangerous?"

    s "No, no, no."

    s "It's only incredibly powerful."

    y "That's not exactly reassuring."

    s "Don't worry, I have it all under control. Come with me I'll show you!!"

    menu:
        "Not Really":
            y "Sorry dude, I'm not really a science guy"

            s "oh...guess I'll just go back to my room and cry myself to sleep"

            y "Uh wait I mean of course I will!"

            s "REALLY?? YAY!!! Let's Go!"

            jump Act4_Part2
        "Of course!":
            y "Yeah let's do it!"

            s "Yippie!! Finally, someone to show it to! Let's go!"

            y "Wait you couldn't show it to anyone else? What about Sparky?"

            s "Um...let's not talk about that right now. I just want to show you my machine!"

            jump Act4_Part2
    
    #Act4 Part 2
label Act4_Part2:

    scene lab
    show StormyNormal
    "Stormy grabs Yinny and rushes to the machine"
    
    s "I've been working on this for days."
    
    y "Days?"
    
    s "Yes!"
    
    s "I barely slept. I was on a strict deadline. It had to be done by the end of today."
    
    y "Stormy..."
    
    s "I know! I know!"
    
    s "But look!"
    
    s "The prototype is almost complete."
    
    y "What are you making?"

    s "Okay. Remember when I found you under a pile of garbage a while ago? I thought I would make a machine to help rid of garbage easier"
    s "This machine should clean any garbage in the area and transport them to a different dimension within a certain radius!"

    s "Only problem though is that I'm missing a few components..."
    
    y "And you were going to build this thing by yourself?"

    s "Of course."

    y "Why?"

    s "Because I know what I'm doing."
    
    "..."
    
    y "Do you?"
    
    s "..."
    
    s "Mostly"

    y "Why haven't you asked for help? I feel like this isn't something you should do alone"

    s "I don't need help."

    y "Stormy."

    s "..."

    s "Okay fine I need a lot of help but no one wants to help me."

    s "Trendy is busy with her social media stuff, Spendy is dealing with finances and Sparky hates me."

    y "Don't say that I'm sure if we asked them, they would help you immediately!"

    s "You're lying they would never help me. They all are..."

    "The door suddenly opens wide"

    jump Act4_Part3

label Act4_Part3:
    scene lab
    show SparkyHappy at center
    sp "I never said anything about hating you Sparky. Don't put words in my mouth."

    show TrendyHappy at left
    t "I always have time for you silly!"

    show SpendyHappy at right
    spe "Dirt is like money. They both come and go easily and quickly."
    spe "But our time together is important."

    hide SparkyHappy
    hide TrendyHappy
    hide SpendyHappy
    show StormyShocked
    s "What the...you guys were listening this whole time..."


    y "Ohh so that's why I heard muttering outside. Thought it was the neighbors"
    y "So what do you think now Stormy?"

    show StormySadSpeaking
    s "I still don't know how to feel. I can't believe you guys are my friends. I'm so glad you all came to help me save the enviroment with my machine!"

    show TrendyHappy
    t "Well of course! We're a team aren't we?"
    
    show StormyHappySpeaking
    s "You're right! We are!"

    jump buildingMinigame

label buildingMinigame:
    scene lab
    show StormyHappySpeaking
    s "Okay so here's the plan! I need you all to focus and help me finish this project!"
    s "we need three components so I need you guys to grab the right ones for me okay?"

    menu:
        "Calibration wrench":
            $ correct_tools += 1
            $ machine_progress += 1

            y "This one?"

            s "Perfect!"

            s "That's exactly what we need."

            t "Yay you're so smart Yinny!"

            jump second_component

        "Rubber duck":
            $ wrong_tools += 1

            y "This?"

            s "..."

            s "Yinny."

            y "Yeah?"

            s "That's a rubber duck."

            sp "I think it looks important."

            s "It is not important."

            sp "I'm sure it's fine let's use it!"

            jump second_component

label second_component:
    scene lab
    s "Now we need something to stabilize the machine. Allows us to make sure no garbage can fall out either!"

    y "Got it."

    menu:

        "A giant bucket":
            $ correct_tools += 1
            $ machine_progress += 1

            s "Excellent!"

            sp "We're actually getting somewhere!"

            $ teamwork += 1

            jump third_component

        "A giant spoon":
            $ wrong_tools += 1

            sp "I vote for the spoon."

            s "Why?"

            sp "Because it's giant."

            s "That isn't a reason."

            t "So is the bucket but I think a spoon is good for scooping out garbage!"

            jump third_component

label third_component:
    scene lab
    s "One final component."

    s "This one is important."

    y "What does it do?"

    s "It's a sorting system for the garbage. We want to make sure that we sort recycables away from regular garbage."

    s "Try to be extra careful with this one. Make sure you input it into the system."

    menu:

        "Input a sorting system that sorts everything and puts them in different bins within machine":
            $ correct_tools += 1
            $ safety += 2
            $ machine_progress += 1

            s "Perfect."

            spe "Good. That makes sense."

            spe "Now we'll know what kind of garbage we collected!"

            s "Exactly."

            jump machine_ready

        "Ignore it and finish project":
            $ safety -= 2
            $ wrong_tools += 1

            y "We don't really need that."

            s "What?"

            y "I mean why don't we just finish the project and see what happens?"

            spe "It's that the important point of the machine? Also it stops it from overflowing and other errors?"

            s "..."

            st "Fine."

            jump machine_ready

label machine_ready:

    scene scene lab
    with dissolve

    show StormyHappySpeaking

    s "Alright everyone!"

    s "It's ready!"

    sp "LET'S GO!"

    spe "Wait."

    t "What?"

    spe "Shouldn't we test it first?"

    s "It's fine. We did all the right moves...I think"

    y "Stormy."

    s "What?"

    y "You just spent the entire day telling us that this machine is important."

    y "Maybe we should make sure it's safe."

    pause

    s "..."

    s "You're right. Better safe than sorry."

    $ safety += 1

    s "We'll run a controlled test."

    jump finaleDecision

label finaleDecision:
    if safety >= 2 and correct_tools >= 2:
        jump stormy_good_ending
    else:
        jump otter_disaster

label stormy_good_ending:

    scene lab
    with fade

    show StormyHappySpeaking

    s "It's working!"

    sp "WE DID IT!"

    t "Woah! I should document this on social media!!"

    spe "Not yet we should try to wait till the deadline passes."

    t "but we should document everything..."

    s "We will and schedule regular maintenance."

    y "You sound different."

    s "Do I?"

    y "You were going to do everything yourself this morning."

    s "I thought the machine was the important part."

    s "But I think I was wrong."

    s "The people taking care of the machine are just as important."

    y "Now you're thinking like a scientist."

    s "I am a scientist."

    y "You know what I mean."

    s "..."

    s "Thank you, Yinny. And thank you all for helping."
    return

label otter_disaster:

    scene lab
    with vpunch

    s "Uh..."

    y "Stormy?"

    s "That's sounds really bad..."

    sp "Is it supposed to make that noise?"

    "BEEP."

    "BEEP."

    "BEEP."

    t "Stormy."

    s "Yes?"

    t "Why is it doing that?"

    s "I..."

    s "feel like that we did something wrong..."

    y "What?"

    s "Several things."

    "BEEP BEEP BEEP!"

    sp "EVERYONE OUT!"

    scene black
    with vpunch

    "WHOOM!"

    "..."

    scene badLab

    show StormySad

    s "..."

    y "..."

    s "..."

    t "..."

    spe "..."

    s "The machine is..."

    s "Definitely broken."

    y "You think?"

    s "On the bright side..."

    y "There is no bright side."

    s "..."

    s "sigh..."

    s "I wanted to prove that we could create something incredible."

    s "But I forgot something important."

    y "What's that?"

    s "Just because we can build something..."

    s "...doesn't mean we should rush to use it."

    s "Technology needs responsibility."

    s "And people need to work together to keep it safe."

    y "So..."

    y "What did we learn?"

    spe "Don't let Sparky touch the tools?"

    sp "HEY!"

    t "That's one lesson."

    s "But the bigger lesson is that powerful technology requires care."

    s "And maintenance."

    y "And teamwork."

    s "And maybe..."

    s "A checklist."

    y "Definitely a checklist..."

    return
