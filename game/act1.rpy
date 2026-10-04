# Act 1 - Small Changes, Real Impact
# This arc begins from script.rpy's existing ``act1`` placeholder.

# These characters were not previously defined in the project.
define t = Character("Trendy")
define p = Character("Spendy")

# Act 1 state
default community_support = 0
default city_budget = 100
default water_quality = 0
default water_solution = ""

# Existing backgrounds and sprites, given readable Ren'Py image names.
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

image trendy normal = "images/Trendy_Normal.png"
image trendy speaking = "images/Trendy_Speaking.png"
image trendy happy = "images/Trendy_Happy.png"
image trendy happy speaking = "images/Trendy_Happy_Speaking.png"
image trendy sad = "images/Trendy_Sad.png"
image trendy sad speaking = "images/Trendy_Sad_Speaking.png"
image trendy annoyed = "images/Trendy_Annoyed.png"
image trendy annoyed speaking = "images/Trendy_Annoy_Speaking.png"
image trendy shocked = "images/Trendy_Shocked.png"

image spendy normal = "images/Spendy_Normal.png"
image spendy speaking = "images/Spendy_Speaking.png"
image spendy happy speaking = "images/Spendy_Happy_Speaking.png"
image spendy sad = "images/Spendy_Sad.png"
image spendy sad speaking = "images/Spendy_Sad_Speaking.png"
image spendy annoyed = "images/Spendy_Annoyed.png"
image spendy annoyed speaking = "images/Spendy_Annoyed_Speaking.png"
image spendy shocked = "images/Spendy_Shocked.png"

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


# Part 1 - Trendy: Garbage and Community ######################################

label act1_start:

    $ community_support = 0
    $ city_budget = 100
    $ water_quality = 0
    $ water_solution = ""

    scene bg dirty downtown
    with fade

    show yinny at yinny_left
    show stormy at stormy_right

    s "Trendy says she has a plan for the garbage problem."
    y "Is it a plan-plan, or a plan with a logo?"
    s "Both. She sounded very pleased with herself."
    y "That answer did not calm me down."

    jump trendy_intro


label trendy_intro:

    scene bg trendy room
    with dissolve

    show yinny at yinny_left
    show trendy speaking at trendy_right

    t "Yinny! The city is disgusting, the lighting is awful, and I refuse to let either one win."
    y "Your phone has a ring light. The garbage has a smell."
    show trendy normal at trendy_right
    t "Exactly. We make them look at it long enough to care. Then we hand them gloves."
    y "A public-service ambush. Bold."
    show trendy happy speaking at trendy_right
    t "I can get attention. You make sure it turns into actual people doing actual work."
    y "So I am the brakes."
    t "You are the steering wheel. Much cuter branding."

    jump trendy_campaign


label trendy_campaign:

    # Choice 1: a useful slogan gives the campaign a clear, shareable purpose.
    menu:
        "Choose the campaign slogan."

        "#OttersForA CleanerBlock — specific and welcoming.":
            $ community_support += 2
            show trendy happy speaking at trendy_right
            t "Clear, local, and cute without pretending trash is cute. Saved."

        "#TrashIsNotA Personality — sharp but a little vague.":
            $ community_support += 1
            show trendy speaking at trendy_right
            t "A little rude. I respect it."

        "#GarbageForever — commit to the bit.":
            $ community_support -= 2
            show trendy shocked at trendy_right
            t "That sounds like we support garbage."
            y "At least it is honest about being terrible."

    # Choice 2: the campaign's tone determines whether people engage or recoil.
    menu:
        "How dramatic should the launch video be?"

        "Show the litter, then show how neighbors can help.":
            $ community_support += 2
            show trendy happy speaking at trendy_right
            t "Show the problem, show the fix, tell people where to stand. Perfect."

        "Use a sad violin over a floating bottle.":
            $ community_support += 0
            show trendy speaking at trendy_right
            t "Dramatic, but not useless. I can live with that."

        "Have Yinny emerge from a trash can and scream for forty seconds.":
            $ community_support -= 2
            show trendy annoyed speaking at trendy_right
            t "The comments say it was 'aggressively upsetting.'"
            y "Then the art communicated."

    # Choice 3: the post can invite participation, guilt people, or make light of it.
    menu:
        "What kind of post goes out with the video?"

        "A map, a time, gloves, and a simple sign-up link.":
            $ community_support += 2
            show trendy happy speaking at trendy_right
            t "Useful information. My favorite kind of content when it has good typography."

        "A facts post about how litter reaches the river.":
            $ community_support += 1
            show trendy speaking at trendy_right
            t "Facts, but nobody has to do homework to read them. Good."

        "'If you scroll past this, you personally hate ducks.'":
            $ community_support -= 2
            show trendy shocked at trendy_right
            y "I see logic has taken the day off."
            t "The ducks have requested a clarification post."

    # Choice 4: comments shape whether the campaign feels like a conversation.
    menu:
        "A comment says, 'One cleanup won't fix anything.' How does Yinny reply?"

        "'True. It can still fix this block today. Want a pair of gloves?'":
            $ community_support += 2
            show trendy happy speaking at trendy_right
            t "Pinned. Firm, useful, no public meltdown. Beautiful."

        "'Fair. We're starting with what is in front of us.'":
            $ community_support += 1
            show trendy speaking at trendy_right
            t "Not flashy, but it sounds like a person talking to people. Keep it."

        "'Then stay home and become part of the scenery.'":
            $ community_support -= 3
            show trendy annoyed speaking at trendy_right
            t "Yinny. We are trying to recruit them."
            y "I offered them a role in the landscape."

    # Choice 5: promotion needs a concrete reason and a practical plan to show up.
    menu:
        "How does Trendy get people from liking the post to attending?"

        "Ask local clubs to bring a team and assign each one an area.":
            $ community_support += 2
            show trendy happy speaking at trendy_right
            t "Teams, zones, supplies. You really do make my chaos look organized."

        "Offer snacks and a group photo at the end.":
            $ community_support += 1
            show trendy speaking at trendy_right
            t "Never underestimate snacks and a flattering group photo."

        "Post every five minutes until everyone gives in.":
            $ community_support -= 2
            show trendy annoyed speaking at trendy_right
            t "We have been muted by three neighborhoods."
            y "Efficiently, at least."

    if community_support <= -3:
        jump trendy_bad_ending
    else:
        jump trendy_cleanup


label trendy_cleanup:

    scene bg dirty cleanup
    with fade

    show yinny at yinny_left
    show trendy normal at trendy_right

    if community_support >= 6:
        "Cleanup day arrives with club teams, neighbors, gloves, and an alarming amount of labeled snacks."
        show trendy happy speaking at trendy_right
        t "Look at them! They actually came!"
        y "I was prepared for twelve people and one pigeon pretending not to watch."
        "Otters sort bottles, collect litter, and work their way along the riverbank."
        "By lunch, the bins are full and the pavement has reappeared."

        scene bg clean cleanup
        with dissolve
        show yinny at yinny_left
        show trendy happy at trendy_right

        y "The pavement had a color this whole time."
        t "And people are already asking when we do this again."
        y "We made caring contagious. That feels medically suspicious."

    else:
        "A smaller group arrives: a few neighbors, one club, and a determined otter with six spare bags."
        show trendy speaking at trendy_right
        t "Not viral. Still real. I will take real."
        y "Nothing does not carry a full trash bag uphill."
        "They clear the worst of the litter and sort what they can before the afternoon ends."

        scene bg clean cleanup
        with dissolve
        show yinny at yinny_left
        show trendy happy at trendy_right

        t "It is noticeably better."
        y "Official Yinny review: noticeably better is, in fact, better."

    jump spendy_intro


label trendy_bad_ending:

    scene black
    with fade

    centered "ENDING UNLOCKED"
    centered "#Cancelled"
    centered "Yinny and Trendy made picking up garbage controversial."
    centered "The cleanup page is now a fight between twelve otters and one exhausted duck."

    pause 3.0
    return


# Part 2 - Spendy: Water and Practical Solutions ##############################

label spendy_intro:

    scene bg dirty river
    with fade

    show yinny at yinny_left
    show spendy speaking at spendy_right

    p "The cleanup is a good start. Now we deal with the part of the city people drink."
    y "You mean the water that came out of my tap brown this morning?"
    show spendy normal at spendy_right
    p "Tea brown, or call-someone brown?"
    y "No tea bag. Definitely call-someone brown."
    "A bottle bumps against the riverbank. The water beside it has a cloudy sheen."
    show spendy speaking at spendy_right
    p "We can improve it. We just need improvements we can afford to maintain after everyone stops clapping."
    y "So no money river. Just this one, which is trying its best to become soup."

    jump spendy_water_investigation


label spendy_water_investigation:

    scene bg spendy office
    with dissolve

    show yinny at yinny_left
    show spendy normal at spendy_right

    p "The runoff pipe is leaking, the river needs filtering, and our whole budget is [city_budget]."
    y "That number has the emotional weight of a tiny sandwich."
    show spendy speaking at spendy_right
    p "Pick the first move. I will make the numbers behave."

    jump spendy_solutions


label spendy_solutions:

    # Decision 1: each option has a different cost-to-benefit tradeoff.
    menu:
        "Choose the first water improvement."

        "Install litter screens at the runoff drains (cost 20; modest improvement).":
            $ city_budget -= 20
            $ water_quality += 15
            $ water_solution = "cheap"
            show spendy happy speaking at spendy_right
            p "Cheap, quick, and effective. I could frame this invoice."

        "Install modular filtration at the main outflow (cost 50; strong improvement).":
            $ city_budget -= 50
            $ water_quality += 45
            $ water_solution = "balanced"
            show spendy happy speaking at spendy_right
            p "It costs more now, but it solves more for longer. That is an investment, not a panic purchase."

        "Buy the Aqua-Sovereign 9000 with decorative laser koi (cost 100; huge improvement).":
            $ city_budget -= 100
            $ water_quality += 70
            $ water_solution = "extreme"
            show spendy shocked at spendy_right
            p "It filters everything, including our ability to buy pencils."
            y "The koi have lasers. That is clearly public safety."

    # Decision 2: a complementary improvement makes the first choice matter.
    menu:
        "Choose a follow-up improvement. Budget remaining: [city_budget]."

        "Repair a leaky street runoff pipe (cost 20; quality +20).":
            $ city_budget -= 20
            $ water_quality += 20
            show spendy speaking at spendy_right
            p "Less dirty runoff enters the river. Extremely boring. Extremely correct."

        "Add refill stations and public water testing (cost 10; quality +10).":
            $ city_budget -= 10
            $ water_quality += 10
            show spendy speaking at spendy_right
            p "Public test results, fewer disposable bottles, and a bill I can look in the eye."

        "Add a synchronized fountain show to 'raise water awareness' (cost 60; quality +5).":
            $ city_budget -= 60
            $ water_quality += 5
            show spendy annoyed speaking at spendy_right
            p "That is not water treatment. That is wet choreography."
            y "Morale is a fluid metric."

    # Decision 3: an unexpected cost tests whether the plan remains realistic.
    show spendy shocked at spendy_right
    p "Update: the pressure valve is corroded. It needs attention before winter, not after a flood."

    menu:
        "How do Yinny and Spendy handle the surprise valve cost?"

        "Use a standard replacement valve (cost 20; quality +15).":
            $ city_budget -= 20
            $ water_quality += 15
            show spendy happy speaking at spendy_right
            p "Reliable, repairable, and gloriously unglamorous."

        "Delay the valve and monitor it closely (no cost; quality -5).":
            $ water_quality -= 5
            show spendy sad speaking at spendy_right
            p "I hate deferring it, but monitoring buys us time. Barely."

        "Commission a diamond-studded smart valve (cost 65; quality +15).":
            $ city_budget -= 65
            $ water_quality += 15
            show spendy annoyed speaking at spendy_right
            p "It sends push notifications in three languages. It is still a valve."
            y "A very well-dressed valve."

    if city_budget < 0:
        jump spendy_bad_ending
    else:
        jump spendy_resolution


label spendy_resolution:

    scene bg clean river
    with fade

    show yinny at yinny_left
    show spendy normal at spendy_right

    if water_solution == "balanced" and water_quality >= 65 and city_budget >= 20:
        show spendy happy speaking at spendy_right
        p "Water quality is up, the budget is stable, and we can maintain the system next month. That is the whole point."
        y "A plan that works without eating the city. Suspiciously excellent."
        "The river runs clearer, and the testing kit shows a real improvement."
        "Spendy reserves the remaining budget for maintenance and refuses to discuss a ribbon cannon."

    else:
        show spendy speaking at spendy_right
        p "It is not perfect. It is cleaner, it is safer, and it gives us a foundation instead of another emergency."
        y "Progress: less glamorous than lasers, much more useful than lasers."
        "The river is visibly clearer. The next upgrades will have to wait for the next budget."

    jump act1_end


label spendy_bad_ending:

    scene black
    with fade

    centered "ENDING UNLOCKED"
    centered "Bankruptcy — Your Wallet Was Sacrificed for the Greater Cause"
    centered "The river is thriving. City Hall now accepts payment in decorative laser koi."

    show spendy sad at spendy_right
    p "We have achieved negative money. Do you understand how hard that is to say calmly?"
    y "But the valve is dressed for success."

    pause 3.0
    return


# Act 1 ending ###############################################################

label act1_end:

    scene bg clean city
    with fade

    show yinny at yinny_left

    if community_support >= 6:
        "The streets look calmer. Cleanup teams are already arguing over which block gets next weekend."
    else:
        "The streets are not spotless, but the worst piles are gone. A few new volunteers pass by with bags."

    if water_solution == "balanced" and water_quality >= 65 and city_budget >= 20:
        "Down by the river, cleaner water catches the afternoon light."
    else:
        "Down by the river, the water is clearer than it was yesterday. For once, that feels like enough."

    y "Less garbage. Better water. And nobody had to be chased with a ring light."
    y "There is still a lot left to fix. Naturally."
    "A low, unfamiliar rumble travels through the pipes beneath the city."
    y "That does not sound like a small problem."
    y "Great. The city has a sequel."

    # Keep the Act 1 title card readable and separate from the final city scene.
    scene black
    with fade

    centered "End of Act 1"
    centered "Small changes. Real impact."

    pause 2.0
    return
