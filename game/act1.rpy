# Act 1 - Trendy: Community Action

# Characters
define t = Character("Trendy")

# Act 1 state
default community_support = 0

# Backgrounds
image bg dirty downtown = "images/dirty_downtown.png"
image bg clean downtown = "images/clean_downtown.png"
image bg dirty cleanup = "images/dirty_garbage_clean_area.png"
image bg clean cleanup = "images/clean_garbage_clean_area.png"
image bg trendy room = "images/trendy_bedroom.png"
image bg dirty city = "images/dirty_city.png"

# Trendy sprites
image trendy normal = "images/Trendy_Normal.png"
image trendy speaking = "images/Trendy_Speaking.png"
image trendy happy = "images/Trendy_Happy.png"
image trendy happy speaking = "images/Trendy_Happy_Speaking.png"
image trendy sad = "images/Trendy_Sad.png"
image trendy sad speaking = "images/Trendy_Sad_Speaking.png"
image trendy annoyed = "images/Trendy_Annoyed.png"
image trendy annoyed speaking = "images/Trendy_Annoy_Speaking.png"
image trendy shocked = "images/Trendy_Shocked.png"

# Character positions
transform trendy_right:
    xalign 1.0
    yalign 1.0
    xoffset -70
    zoom 0.72

# Act 1 start
label act1_start:

    $ community_support = 0
    scene bg dirty downtown
    with fade

    show yinny at yinny_left
    show stormy at stormy_right

    s "So... still feeling heroic?"

    y "I said I wanted to help. I never used the word heroic. I'm just doing what I can."

    s "Good, because Trendy already claimed that one."

    y "Of course she did."

    s "She's trying to organize a cleanup. Apparently the garbage problem has become a content opportunity."

    y "That sentence somehow made me more worried...She's not doing some viral trend right...?"

    s "Just go talk to her."

    y "Fine. If I'm not back by dinner, delete my search history."

    s "Why?"

    y "No reason."

    jump trendy_intro


# Trendy intro
label trendy_intro:

    scene bg trendy room
    with dissolve

    show yinny at yinny_left
    show trendy speaking at trendy_right

    t "Yinny! Perfect timing!"

    y "Those are usually the last words I hear before something becomes my problem."

    t "Have you looked outside?"

    y "Unfortunately."

    show trendy annoyed speaking at trendy_right

    t "Trash on the sidewalks. Trash in the gutters. Trash in the park."

    y "I got buried in it this morning."

    show trendy shocked at trendy_right

    t "Wait. Seriously?"

    y "I'd prefer not to relive it. 0/10 experience rating, would not recommend."

    show trendy speaking at trendy_right

    t "Then you already understand the problem."

    t "People have gotten so used to the garbage that they barely notice it anymore."

    y "So what's your plan?"

    show trendy happy speaking at trendy_right

    t "We make them notice."

    y "Uh oh."

    t "Social media campaign. Photos. Videos. Hashtags."

    y "There it is."

    t "But not just for likes."

    t "We use the attention to organize an actual cleanup."

    y "So the internet does something useful for once?"

    t "Exactly!"

    y "Alright. You handle getting people's attention."

    y "I'll make sure we don't accidentally start a public relations disaster."

    t "Deal."

    jump trendy_campaign


# Trendy campaign
label trendy_campaign:

    show trendy normal at trendy_right

    "Trendy opens a new post."

    t "First things first."

    t "We need something people will actually want to join."

    menu:

        "What should the campaign focus on?"

        "Show the problem, then invite everyone to help fix it.":
            $ record_decision("trendy_campaign_focus", "invite")
            $ community_support += 2

            show trendy happy speaking at trendy_right

            t "Positive, useful, and nobody gets yelled at."

            y "Disappointingly reasonable."

        "Post dramatic photos of the worst garbage piles.":
            $ record_decision("trendy_campaign_focus", "dramatic")
            $ community_support += 1

            show trendy speaking at trendy_right

            t "A little dramatic, but at least people will see what we're dealing with."

            y "Nothing motivates an otter like being mildly horrified."

        "Tell everyone the city is disgusting and it's their fault.":
            $ record_decision("trendy_campaign_focus", "blame")
            $ community_support -= 2

            show trendy annoyed speaking at trendy_right

            t "Yinny."

            y "Too aggressive?"

            t "You insulted the entire city in the first sentence."

            y "So... strong opening?"

            t "No."

    show trendy normal at trendy_right

    t "Okay. People are looking."

    t "Now we need them to actually show up."

    menu:

        "What should the cleanup post include?"

        "A meeting place, time, supplies, and a simple sign-up link.":
            $ record_decision("trendy_cleanup_post", "details")
            $ community_support += 2

            show trendy happy speaking at trendy_right

            t "Perfect."

            t "People know where to go, what to bring, and what we're doing."

            y "Organization... Terrifying."

        "Offer snacks and a group photo afterward.":
            $ record_decision("trendy_cleanup_post", "snacks")
            $ community_support += 1

            show trendy speaking at trendy_right

            t "Honestly?"

            t "Snacks have carried entire social movements."

            y "Finally. A cause I understand."

        "\"If you don't come, you personally hate the environment.\"":
            $ record_decision("trendy_cleanup_post", "guilt")
            $ community_support -= 2

            show trendy shocked at trendy_right

            t "We cannot guilt-trip the entire city!"

            y "Technically, we can."
            hide trendy shocked
            show trendy annoyed speaking at trendy_right
            t "We should not."

            y "Important distinction, we still can."

    "The post goes live."

    pause 0.5

    t "Oh. Comment."

    t "\"One cleanup isn't going to fix the whole city.\""

    y "Well..."

    menu:

        "How should Yinny respond?"

        "\"You're right. But it can fix this block today. One step at a time.\"":
            $ record_decision("trendy_criticism_reply", "one_block")
            $ community_support += 2

            show trendy happy speaking at trendy_right

            t "That."

            y "That?"

            t "That's the whole point."

            t "We don't need to fix everything in one afternoon."

            t "We just need enough people willing to start."

        "\"Fair. We're starting small and seeing where it goes.\"":
            $ record_decision("trendy_criticism_reply", "start_small")
            $ community_support += 1

            show trendy speaking at trendy_right

            t "Not flashy."

            y "I thought flashy was your department."

            t "It is."

            t "But that sounds honest. Keep it."

        "\"Then stay home and enjoy the garbage.\"":
            $ record_decision("trendy_criticism_reply", "dismiss")
            $ community_support -= 3

            show trendy annoyed speaking at trendy_right

            t "Delete it."

            y "But..."

            t "Delete."

            y "Freedom of speech is dead."

            t "Yinny."

    if community_support <= -3:
        jump trendy_bad_ending
    else:
        jump trendy_cleanup


# Cleanup day
label trendy_cleanup:

    scene bg dirty cleanup
    with fade

    show yinny at yinny_left
    show trendy normal at trendy_right

    "The day of the cleanup arrives."

    if community_support >= 4:

        "By the time Yinny arrives, the street is already full of volunteers."

        "Neighbors pass out gloves and garbage bags while local clubs divide into teams."

        show trendy happy speaking at trendy_right

        t "Look!"

        t "They actually came!"

        y "That's way more people than I expected."

        t "How many were you expecting?"

        y "Six."

        y "Seven if we counted the guy selling hot dogs."

        t "Have a little faith."

        y "I have faith."

        y "I just also have expectations."

    else:

        "The crowd is smaller than Trendy hoped."

        "A few neighbors, a local club, and several very determined volunteers wait with garbage bags."

        show trendy speaking at trendy_right

        t "Okay."

        t "Not exactly viral."

        y "They're still here. Better than just the two of us."

        t "Yeah."

        show trendy happy speaking at trendy_right

        t "They're still here."

        y "Turns out ten people picking up garbage is more useful than ten thousand people liking a photo."

        t "Do not say that too loudly around my career."

    "The group gets to work."

    "Bottles disappear from the sidewalk."

    "Garbage bags fill one after another."

    "Slowly, the pavement begins to reappear."

    scene bg clean cleanup
    with dissolve

    show yinny at yinny_left
    show trendy happy at trendy_right

    y "Huh."

    t "What?"

    y "The ground has a color."

    t "Very observant."

    y "Thank you."

    "Yinny drags one final bag toward the collection pile."

    "Something near the curb catches their eye."

    y "Trendy."

    show trendy speaking at trendy_right

    t "What?"

    y "Come look at this."

    "Garbage is packed around a storm drain."

    "Dirty water slips through the gaps and disappears underground."

    t "That's... not great."

    y "Where does this drain go?"

    t "Toward the river, I think."

    y "So even after we pick all this up..."

    t "Anything that washes into the drains can still end up downstream."

    "For a moment, both of them look at the newly cleaned street."

    y "We fixed the part we could see."

    t "Yeah."

    t "But apparently the city has problems underneath the problems."

    y "Fantastic."

    show trendy happy speaking at trendy_right

    t "I know someone who loves problems underneath problems."

    y "That is a concerning description of a friend."

    t "Spendy."

    y "Oh."

    y "That actually makes sense."

    scene black
    with fade

    centered "END OF ACT 1"

    centered "Community Action"

    pause 2.0

    jump act2_spendy


# Trendy bad ending
label trendy_bad_ending:

    scene black
    with fade

    centered "ENDING UNLOCKED"

    centered "#Cancelled"

    centered "The cleanup campaign somehow became more controversial than the garbage."

    centered "Nobody remembers what the original post was about."

    centered "One exhausted otter has written a twelve-part response thread."

    pause 3.0

    return
