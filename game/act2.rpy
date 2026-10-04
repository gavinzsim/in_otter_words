# Act 2 - Spendy: Sustainable Solutions

define p = Character("Spendy")

default city_budget = 100
default water_quality = 0
default water_solution = ""

image bg dirty river = "images/dirty_river.png"
image bg clean river = "images/clean_river.png"
image bg spendy office = "images/spendy_office.png"
image bg clean city = "images/clean_city.png"

image spendy normal = "images/Spendy_Normal.png"
image spendy speaking = "images/Spendy_Speaking.png"
image spendy happy speaking = "images/Spendy_Happy_Speaking.png"
image spendy sad = "images/Spendy_Sad.png"
image spendy sad speaking = "images/Spendy_Sad_Speaking.png"
image spendy annoyed = "images/Spendy_Annoyed.png"
image spendy annoyed speaking = "images/Spendy_Annoyed_Speaking.png"
image spendy shocked = "images/Spendy_Shocked.png"

transform spendy_right:
    xalign 1.0
    yalign 1.0
    xoffset -70
    zoom 0.72

label act2_spendy:

    $ city_budget = 100
    $ water_quality = 0
    $ water_solution = ""

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

    p "Yinny!"

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

    p "You'll be fine."

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

            p "It has a decorative laser engraving of a koi fish on it..."

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

        "Build a fountain to show for 'water awareness' — Cost: 60 | Improvement: +5":
            $ city_budget -= 60
            $ water_quality += 5

            show spendy annoyed speaking at spendy_right

            p "We have purchased synchronized water jets."

            y "'Educational' synchronized water jets."

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

            p "It is a valve, Yinny. Not a disco rave."

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

        "There is less debris along the bank, and the cloudy sheen has began to disappear."

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

    jump act2_end


# Spendy bad ending
label spendy_bad_ending:

    scene black
    with fade

    centered "ENDING UNLOCKED"

    centered "Bankruptcy"

    centered "Your Wallet Was Sacrificed for the Greater Cause"

    pause 1.0

    centered "The environmental upgrades are excellent."

    centered "Unfortunately, the city no longer has a budget for long term maintenance. Even in debt in some aspects."

    show spendy sad at spendy_right

    p "We spent money we did not have."

    y "But the river looks nice."

    p "Yinny."

    y "I'm trying to find the positive."

    p "The positive is currently our debt."

    y "Ah."

    pause 3.0

    return


# Act 2 ending
label act2_end:

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

    "For once, it does not carry the smell of garbage."

    y "Huge improvement."

    "Then a low rumble echoes somewhere beneath the street."

    y "..."

    "The ground vibrates slightly."

    y "That doesn't sound environmentally friendly."

    "Another distant rumble follows."

    y "Right."

    y "Of course we're not done."

    scene black
    with fade

    centered "END OF ACT 2"

    pause 0.7

    centered "Sustainable Solutions"

    pause 2.0

    jump act3_sparky
