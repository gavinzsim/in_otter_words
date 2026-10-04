# Act 1 - Small Changes, Real Impact

# Characters
define t = Character("Trendy")
define p = Character("Spendy")

# Act 1 state
default community_support = 0
default city_budget = 100
default water_quality = 0
default water_solution = ""

# Backgrounds
image bg dirty downtown = "images/dirty_downtown.png"
image bg clean downtown = "images/clean_downtown.png"
image bg dirty cleanup = "images/dirty_garbage_clean_area.png"
image bg clean cleanup = "images/clean_garbage_clean_area.png"
image bg dirty river = "images/dirty_river.png"
image bg clean river = "images/clean_river.png"
image bg trendy room = "images/trendy_bedroom.png"
image bg spendy office = "images/spendy_office.png"
image bg dirty city = "images/dirty_city.png"
image bg clean city = "images/clean_city.png"

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

# Spendy sprites
image spendy normal = "images/Spendy_Normal.png"
image spendy speaking = "images/Spendy_Speaking.png"
image spendy happy speaking = "images/Spendy_Happy_Speaking.png"
image spendy sad = "images/Spendy_Sad.png"
image spendy sad speaking = "images/Spendy_Sad_Speaking.png"
image spendy annoyed = "images/Spendy_Annoyed.png"
image spendy annoyed speaking = "images/Spendy_Annoyed_Speaking.png"
image spendy shocked = "images/Spendy_Shocked.png"

# Character positions
transform trendy_right:
    xalign 1.0
    yalign 1.0
    xoffset -70
    zoom 0.72

transform spendy_right:
    xalign 1.0
    yalign 1.0
    xoffset -70
    zoom 0.72


# Act 1 start
label act1_start:

    $ community_support = 0
    $ city_budget = 100
    $ water_quality = 0
    $ water_solution = ""

    scene bg dirty downtown
    with fade

    show yinny at yinny_left
    show stormy at stormy_right

    s "So... still feeling heroic?"

    y "I said I wanted to help. I never used the word heroic."

    s "Good, because Trendy already claimed that one."

    y "Of course she did."

    s "She's trying to organize a cleanup. Apparently the garbage problem has become a content opportunity."

    y "That sentence somehow made me more worried."

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

    y "I'd prefer not to relive it."

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
            $ community_support += 2

            show trendy happy speaking at trendy_right

            t "Positive, useful, and nobody gets yelled at."

            y "Disappointingly reasonable."

        "Post dramatic photos of the worst garbage piles.":
            $ community_support += 1

            show trendy speaking at trendy_right

            t "A little dramatic, but at least people will see what we're dealing with."

            y "Nothing motivates an otter like being mildly horrified."

        "Tell everyone the city is disgusting and it's their fault.":
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
            $ community_support += 2

            show trendy happy speaking at trendy_right

            t "Perfect."

            t "People know where to go, what to bring, and what we're doing."

            y "Organization. Terrifying."

        "Offer snacks and a group photo afterward.":
            $ community_support += 1

            show trendy speaking at trendy_right

            t "Honestly?"

            t "Snacks have carried entire social movements."

            y "Finally. A cause I understand."

        "\"If you don't come, you personally hate the environment.\"":
            $ community_support -= 2

            show trendy shocked at trendy_right

            t "We cannot guilt-trip the entire city!"

            y "Technically, we can."

            t "We should not."

            y "Important distinction."

    "The post goes live."

    pause 0.5

    t "Oh. Comment."

    t "\"One cleanup isn't going to fix the whole city.\""

    y "Well..."

    menu:

        "How should Yinny respond?"

        "\"You're right. But it can fix this block today.\"":
            $ community_support += 2

            show trendy happy speaking at trendy_right

            t "That."

            y "That?"

            t "That's the whole point."

            t "We don't need to fix everything in one afternoon."

            t "We just need enough people willing to start."

        "\"Fair. We're starting small and seeing where it goes.\"":
            $ community_support += 1

            show trendy speaking at trendy_right

            t "Not flashy."

            y "I thought flashy was your department."

            t "It is."

            t "But that sounds honest. Keep it."

        "\"Then stay home and enjoy the garbage.\"":
            $ community_support -= 3

            show trendy annoyed speaking at trendy_right

            t "Delete it."

            y "But—"

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

        y "They're still here."

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

    jump spendy_intro


# Trendy bad ending
label trendy_bad_ending:

    scene black
    with fade

    centered "ENDING UNLOCKED"

    centered "#Cancelled"

    centered "The cleanup campaign somehow became more controversial than the garbage."

    centered "Nobody remembers what the original post was about."

    centered "One exhausted duck has written a twelve-part response thread."

    pause 3.0

    return


# Spendy intro
label spendy_intro:

    scene bg dirty river
    with fade

    show yinny at yinny_left
    show spendy speaking at spendy_right

    p "So Trendy found the storm drain."

    y "She described you as someone who likes problems underneath problems."

    show spendy normal at spendy_right

    p "I'll choose to take that as a compliment."

    "Yinny looks across the river."

    "The water is cloudy, and bits of litter have collected along the bank."

    y "This is worse than I thought."

    p "The garbage is only part of it."

    show spendy speaking at spendy_right

    p "Runoff from the streets enters here."

    p "There's also a damaged pipe upstream, and the city's filtration system is overdue for an upgrade."

    y "That would explain the brown water from my tap this morning."

    show spendy shocked at spendy_right

    p "Your water was brown?"

    y "Very."

    p "And you still drank it?"

    y "I considered it."

    p "Yinny."

    y "I didn't!"

    show spendy normal at spendy_right

    p "The good news is that we can improve this."

    y "And the bad news?"

    p "Everything costs money."

    y "There it is."

    jump river_cleanup_start


# Water investigation
label spendy_water_investigation:

    scene bg spendy office
    with dissolve

    show yinny at yinny_left
    show spendy normal at spendy_right

    "Spendy spreads several reports across the desk."

    p "Here's what we're working with."

    show spendy speaking at spendy_right

    p "The city has 100 budget points available."

    p "We need to reduce pollution now..."

    p "...but whatever we install also needs to be maintained later."

    y "So we can't just buy the biggest machine."

    p "We can."

    y "Oh."

    p "It would just be a terrible idea."

    y "Important clarification."

    p "Environmental planning isn't about finding the most impressive solution."

    p "It's about finding something effective that we can actually afford to keep working."

    y "Effective, affordable, maintainable."

    p "Exactly."

    y "Very responsible."

    y "I hate it."

    p "You'll survive."

    jump spendy_solutions


# Water solutions
label spendy_solutions:

    show spendy speaking at spendy_right

    p "First decision."

    p "What do we do about the polluted runoff entering the river?"

    menu:

        "Choose the main water improvement."

        "Install runoff screens — Cost: 20 | Improvement: +15":
            $ city_budget -= 20
            $ water_quality += 15
            $ water_solution = "cheap"

            show spendy happy speaking at spendy_right

            p "Simple and inexpensive."

            p "It won't solve everything, but it'll stop a lot of solid waste before it reaches the river."

            y "Small fix. Real improvement."

            p "Exactly."

        "Install modular filtration — Cost: 50 | Improvement: +45":
            $ city_budget -= 50
            $ water_quality += 45
            $ water_solution = "balanced"

            show spendy happy speaking at spendy_right

            p "More expensive, but much stronger."

            p "And because it's modular, we can repair or expand it later."

            y "So this is the boring sensible choice."

            p "My favorite kind."

        "Install the Aqua-Sovereign 9000 — Cost: 100 | Improvement: +70":
            $ city_budget -= 100
            $ water_quality += 70
            $ water_solution = "extreme"

            show spendy shocked at spendy_right

            p "You spent the entire budget."

            y "But look at those specifications."

            p "It has decorative laser koi."

            y "Exactly."

            p "Those do not improve the water."

            y "They improve my water."

    show spendy normal at spendy_right

    p "Budget remaining: [city_budget]."

    y "That number feels more threatening when you say it out loud."

    show spendy speaking at spendy_right

    p "Next problem."

    p "The damaged runoff pipe is still sending dirty water downstream."

    y "So cleaning the river without fixing the pipe would be..."

    p "Cleaning the floor while the sink is overflowing."

    y "Got it."

    menu:

        "What should they do about the damaged runoff pipe?"

        "Repair the pipe — Cost: 20 | Improvement: +20":
            $ city_budget -= 20
            $ water_quality += 20

            show spendy happy speaking at spendy_right

            p "Good."

            p "Stopping pollution at the source is usually cheaper than cleaning it up forever."

            y "Very annoyingly logical."

        "Add public testing and refill stations — Cost: 10 | Improvement: +10":
            $ city_budget -= 10
            $ water_quality += 10

            show spendy speaking at spendy_right

            p "Useful, especially for keeping residents informed."

            y "But the pipe?"

            p "Still leaking."

            y "Right."

            p "Helping people see a problem isn't the same as fixing its source."

        "Build a fountain show for 'water awareness' — Cost: 60 | Improvement: +5":
            $ city_budget -= 60
            $ water_quality += 5

            show spendy annoyed speaking at spendy_right

            p "We have purchased synchronized water jets."

            y "Educational synchronized water jets."

            p "The polluted pipe is twenty metres away."

            y "But can the polluted pipe play music?"

            p "I regret inviting you."

    if city_budget < 0:
        jump spendy_bad_ending

    show spendy shocked at spendy_right

    p "Wait."

    y "That's not your good 'wait,' is it?"

    p "There is no good 'wait.'"

    "Spendy points at the latest inspection report."

    p "The pressure valve is corroded."

    p "If it fails, part of the system could shut down."

    y "How much?"

    p "A normal replacement costs 20."

    y "Budget remaining?"

    p "[city_budget]."

    y "Ah."

    p "This is why leaving room in the budget matters."

    menu:

        "How should they handle the valve?"

        "Install a standard replacement — Cost: 20 | Improvement: +15":
            $ city_budget -= 20
            $ water_quality += 15

            show spendy happy speaking at spendy_right

            p "Reliable."

            p "Repairable."

            p "Not remotely exciting."

            y "You've never looked happier."

        "Monitor it for now — Cost: 0 | Improvement: -5":
            $ water_quality -= 5

            show spendy sad speaking at spendy_right

            p "Not ideal."

            p "We'll have to inspect it constantly until we can afford the replacement."

            y "So we're buying time."

            p "Exactly."

            p "Sometimes that's the realistic option."

        "Install a premium smart valve — Cost: 65 | Improvement: +15":
            $ city_budget -= 65
            $ water_quality += 15

            show spendy annoyed speaking at spendy_right

            p "It sends notifications."

            y "Useful."

            p "It tracks pressure from your phone."

            y "Very useful."

            p "It has customizable RGB lighting."

            y "Essential."

            p "It is a valve, Yinny."

    if city_budget < 0:
        jump spendy_bad_ending
    else:
        jump spendy_resolution


# Spendy resolution
label spendy_resolution:

    if water_quality >= 60:

        scene bg clean river
        with fade

        show yinny at yinny_left
        show spendy normal at spendy_right

        "A few days later, Yinny and Spendy return to the river."

        "The difference is visible."

        "There is less debris along the bank, and the cloudy sheen has begun to disappear."

    else:

        scene bg dirty river
        with fade

        show yinny at yinny_left
        show spendy normal at spendy_right

        "A few days later, Yinny and Spendy return to the river."

        "The water is not clean yet."

        "But there is less garbage collecting near the outflow, and the first improvements are starting to show."

    if water_solution == "balanced" and water_quality >= 65 and city_budget >= 10:

        show spendy happy speaking at spendy_right

        p "Good water improvement."

        p "Infrastructure repaired."

        p "And we still have [city_budget] budget points left."

        y "So we didn't choose the biggest solution..."

        p "We chose one that solved the problem without creating a new one."

        y "And we can actually afford to maintain it."

        p "Now you're getting it."

        y "I don't like how financially responsible I'm becoming."

    elif water_solution == "extreme" and city_budget == 0:

        show spendy speaking at spendy_right

        p "The filtration system works."

        y "That sounds good."

        p "It is."

        p "But we have no money left for maintenance."

        y "Less good."

        p "The most powerful solution isn't automatically the best solution."

        y "But the laser koi—"

        p "No."

    else:

        show spendy speaking at spendy_right

        p "It's not perfect."

        p "But the water is better than it was before."

        y "And we didn't need to fix everything at once."

        p "Exactly."

        p "You make the best improvement you realistically can..."

        p "...then you keep building from there."

        y "Small changes."

        p "Real impact."

        y "Hey."

        y "That's pretty good."

    jump act1_end


# Spendy bad ending
label spendy_bad_ending:

    scene black
    with fade

    centered "ENDING UNLOCKED"

    centered "Bankruptcy"

    centered "Your Wallet Was Sacrificed for the Greater Cause"

    pause 1.0

    centered "The environmental upgrades are excellent."

    centered "Unfortunately, the city now has negative money."

    show spendy sad at spendy_right

    p "We spent money we did not have."

    y "But the river looks nice."

    p "Yinny."

    y "I'm trying to find the positive."

    p "The positive is currently our debt."

    y "Ah."

    pause 3.0

    return


# Act 1 ending
label act1_end:

    scene bg clean city
    with fade

    show yinny at yinny_left

    "By the end of the week, the city feels a little different."

    if community_support >= 4:

        "The cleaned streets have stayed mostly clear."

        "A second neighborhood has already started organizing its own cleanup."

    else:

        "The streets are not spotless."

        "But the worst piles are gone, and a few residents have started carrying garbage bags of their own."

    if water_quality >= 60:

        "Down by the river, the water is visibly clearer."

    else:

        "Down by the river, the cleanup is still a work in progress."

    y "Huh."

    y "We actually did something."

    y "The whole city isn't magically fixed..."

    y "...but it's better than it was."

    "Yinny watches a pair of volunteers carry another bag of garbage down the street."

    y "I guess Trendy was right."

    y "People will help if you give them somewhere to start."

    "A breeze moves through the city."

    "For once, it does not carry the smell of a nearby garbage pile."

    y "Huge improvement."

    "Then a low rumble echoes somewhere beneath the street."

    y "..."

    "The ground vibrates slightly."

    y "That didn't sound environmentally friendly."

    "Another distant rumble follows."

    y "Right."

    y "Of course we're not done."

    scene black
    with fade

    centered "END OF ACT 1"

    pause 0.7

    centered "Small Changes, Real Impact"

    pause 2.0

    return


