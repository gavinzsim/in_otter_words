# Act 4 - Stormy's Machine

# These backgrounds and expressions use the assets already included with the game.
image bg lab = "images/normal_stormy_lab.png"
image bg bad lab = "images/destroyed_stormy_lab.png"
image StormySad = "images/Stormy_Sad.png"
image StormySadSpeaking = "images/Stormy_Sad_Speaking.png"

# State for Act 4's component-building choices.
default correct_tools = 0
default wrong_tools = 0
default machine_progress = 0
default safety = 0
default teamwork = 0
transform flip:
    xalign 0.25
    yalign 1.0
    xzoom -1

label act4:
    scene bg livingroom
    with fade

    "Stormy sobs loudly as he runs away from his completed experiment."

    show StormySad
    s "As always, I'm all alone."
    s "I just wanted to show everyone my talent, to show them my creations..."

    "He hops on the couch and cuddles with a strange new plushie."

    s "But of course no one actually cares."
    "Stormy continues to cry himself to sleep."

    "Ding dong, ding dong."
    hide StormySad
    show StormySadSpeaking at flip
    s "Wait, who's there?"
    s "I'm coming!"
    "Stormy wipes his tears and rushes to the door."

    s "Sniff sniff, who's here?"
    "Stormy opens the door and sees a familiar face."

    y "Hey, I hope it's okay if I barge in here randomly."
    hide StormySadSpeaking
    show StormyShocked at right
    s "Yinny! You came!"

    show yinny at left
    y "Yeah, I came over. What are you working on?"

    hide StormyShocked                    
    show StormyHappySpeaking
    s "Something incredible."

    y "That doesn't answer my question..."
    s "I'm building a new energy machine!"

    y "..."
    y "That sounds dangerous."

    s "Dangerous?"
    s "No, no, no."
    s "It's only incredibly powerful and efficient."

    y "That's not exactly reassuring."
    s "Don't worry, I have it all under control. Come with me, I'll show you!!"

    menu:
        "Not Really":
            $ record_decision("stormy_visit", "reluctant")
            y "Sorry dude, I'm not really a science guy."
            s "Oh... guess I'll just go back to my room and cry myself to sleep."
            y "Uh, wait, I meant of course I will!"
            s "REALLY?? Let's go!"
            jump act4_part2

        "Of course!":
            $ record_decision("stormy_visit", "enthusiastic")
            y "Yeah, let's do it!"
            s "Yay! Finally, someone to show it to. Let's go!"
            y "Wait, you couldn't show it to anyone else? What about Sparky or the others?"
            s "Um... let's not talk about that right now. I just want to show you my machine!"
            jump act4_part2


label act4_part2:
    scene bg lab
    show StormyNormal

    "Stormy grabs Yinny and rushes to the machine."
    s "I've been working on this for days."
    y "Days?"
    s "Yes!"
    s "I barely slept. I was on a strict deadline. It had to be done by the end of today-"
    y "Stormy..."
    s "I know! I know!"
    s "But look! The prototype is almost complete."
    y "What are you making?"

    s "Okay. Remember when I found you under a pile of garbage a while ago? I thought I would make a machine to help get rid of garbage more easily."
    s "This machine should clean any garbage in the area and transport it to a different dimension within a certain radius!"
    s "Only problem, though, is that I'm missing a few components..."

    y "And you were going to build this thing by yourself?"
    s "Of course."
    y "Why?"
    s "Because I know what I'm doing."

    "..."
    y "Do you?"
    s "..."
    s "Mostly."

    y "Why haven't you asked for help? I feel like this isn't something you should do alone."
    s "I don't need help."
    y "Stormy."
    s "..."
    s "Okay, fine. I need a lot of help, but no one wants to help me."
    s "Trendy is busy with her social media stuff, Spendy is dealing with finances, and Sparky hates me."

    y "Don't say that. I'm sure if we asked them, they would help you immediately!"
    s "You're lying. They would never help me. They all are..."

    "The door suddenly opens wide."
    jump act4_part3


label act4_part3:
    scene bg lab

    show SparkyHappy at center
    sp "I never said anything about hating you, Stormy. Don't put words in my mouth."

    show trendy happy at left
    t "I always have time for you, silly!"

    show spendy normal at right
    p "Dirt is like money. They both come and go easily and quickly."
    p "But our time together is important."

    hide SparkyHappy
    hide trendy happy
    hide spendy normal
    show StormyShocked
    s "What the... you guys were listening this whole time..."

    y "Ohh, so that's why I heard muttering outside. I thought it was the neighbors."
    y "So what do you think now, Stormy?"

    show StormySadSpeaking
    s "I still don't know how to feel. I can't believe you guys are my friends. I'm so glad you all came to help me save the environment with my machine!"

    show trendy happy
    t "Well, of course! We're a team, aren't we?"

    show StormyHappySpeaking
    s "You're right! We are!"

    jump building_minigame


label building_minigame:
    scene bg lab
    show StormyHappySpeaking
    s "Okay, so here's the plan! I need you all to focus and help me finish this project!"
    s "We need three components, so I need you guys to grab the right ones for me, okay?"

    menu:
        "Calibration wrench":
            $ record_decision("stormy_first_component", "wrench")
            $ correct_tools += 1
            $ machine_progress += 1
            y "This one?"
            s "Perfect!"
            s "That's exactly what we need."
            t "Yay, you're so smart, Yinny!"
            jump second_component

        "Rubber duck":
            $ record_decision("stormy_first_component", "duck")
            $ wrong_tools += 1
            y "This?"
            s "..."
            s "Yinny."
            y "Yeah?"
            s "That's a rubber duck."
            sp "I think it looks important."
            s "It is not important. It's a rubber duck."
            sp "I'm sure it's fine, let's use it!"
            jump second_component


label second_component:
    scene bg lab
    s "Now we need something to stabilize the machine. This lets us make sure no garbage can fall out either!"
    y "Got it."

    menu:
        "A giant bucket":
            $ record_decision("stormy_stabilizer", "bucket")
            $ correct_tools += 1
            $ machine_progress += 1
            s "Excellent!"
            sp "We're actually getting somewhere!"
            $ teamwork += 1
            jump third_component

        "A giant spoon":
            $ record_decision("stormy_stabilizer", "spoon")
            $ wrong_tools += 1
            sp "I vote for the spoon."
            s "Why?"
            sp "Because it's giant."
            s "That isn't a reason."
            t "So is the bucket, but I think a spoon is good for scooping out garbage!"
            jump third_component


label third_component:
    scene bg lab
    s "One final component."
    s "This one is important."
    y "What does it do?"
    s "It's a sorting system for the garbage. We want to make sure that we sort recyclables away from regular garbage."
    s "Try to be extra careful with this one. Make sure you input it into the system."

    menu:
        "Input a sorting system that puts everything in different bins within the machine":
            $ record_decision("stormy_sorting", "sort")
            $ correct_tools += 1
            $ safety += 2
            $ machine_progress += 1
            s "Perfect."
            p "Good. That makes sense."
            p "Now we'll know what kind of garbage we collected!"
            s "Exactly."
            jump machine_ready

        "Ignore it and finish the project":
            $ record_decision("stormy_sorting", "skip")
            $ safety -= 2
            $ wrong_tools += 1
            y "We don't really need that."
            s "What? Why?"
            y "I mean, why don't we just finish the project and see what happens?"
            p "That is the important point of the machine??? It also stops it from overflowing and causing other errors???"
            s "..."
            s "Fine."
            jump machine_ready


label machine_ready:
    scene bg lab
    with dissolve

    show StormyHappySpeaking
    s "Alright, everyone!"
    s "It's ready!"
    sp "LET'S GO!"
    p "Wait."
    t "What?"
    p "Shouldn't we test it first?"
    s "It's fine. We did all the right moves... I think..."
    y "Stormy."
    s "What?"
    y "You just spent the entire day telling us that this machine is important."
    y "Maybe we should make sure it's safe."
    pause
    s "..."
    s "You're right. Better safe than sorry."
    $ safety += 1
    s "We'll run a controlled test."
    jump finale_decision


label finale_decision:
    if safety >= 2 and correct_tools >= 2:
        jump stormy_good_ending
    else:
        jump otter_disaster


label stormy_good_ending:
    $ finale_machine_outcome = "working_with_maintenance_plan"
    scene bg lab
    with fade

    show StormyHappySpeaking
    s "It's working!"
    sp "WE DID IT!"
    t "Woah! I should document this on social media!!"
    p "Not yet. We should wait until the deadline passes."
    t "But we should document everything..."
    s "We will, and we'll schedule regular maintenance."
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
    jump finale


label otter_disaster:
    $ finale_machine_outcome = "prototype_broke_after_unsafe_build"
    scene bg lab
    with vpunch

    s "Uh..."
    y "Stormy?"
    s "That sounds really bad..."
    sp "Is it supposed to make that noise? It sounds like an alarm of some sort..."
    "BEEP."
    "BEEP."
    "BEEP."
    t "Stormy."
    s "Yes?"
    t "Why is it doing that?"
    s "I..."
    "BEEP."
    s "...feel like we did something wrong..."
    "BEEP."
    y "What?"
    "BEEP. BEEP."
    s "Scratch that, several things wrong."
    "BEEP BEEP BEEP!"
    sp "EVERYONE OUT!"

    scene black
    with vpunch
    "BOOM!"
    "..."

    scene bg bad lab
    show StormySad
    s "..."
    y "..."
    s "..."
    t "..."
    p "..."
    s "The machine is..."
    s "Definitely broken."
    y "You think?"
    s "On the bright side..."
    y "There is no bright side."
    s "..."
    s "Sigh..."
    s "I wanted to prove that we could create something incredible."
    s "But I forgot something important."
    y "What's that?"
    s "Just because we can build something..."
    s "...doesn't mean we should rush to use it."
    s "Technology needs responsibility, and people need to work together to keep it safe."
    y "So..."
    y "What did we learn?"
    p "Don't let Sparky touch the tools?"
    sp "HEY!"
    t "That's one lesson."
    s "But the bigger lesson is that powerful technology requires care."
    s "And maintenance."
    y "And teamwork."
    s "And maybe..."
    s "A checklist?"
    y "Definitely a checklist..."
    jump finale
