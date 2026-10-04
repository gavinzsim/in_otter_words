# ACT 2 - SPARKY

label act2_sparky:

    scene black
    with fade

    centered "Two weeks later..."

    scene bg park
    with fade

    show yinny at yinny_left

    "The city is cleaner."

    "Not clean. Cleaner."

    "Yinny stares at a trash can that is, for once, not overflowing."

    y "..."

    y "There's still so much left."

    y "The water's still noticeably discolored. The air still has a stink."

    y "We fixed one street. It took us so long to clean one, what of the hundreds that still need cleaning?"

    "Yinny sinks onto a park bench."

    show sparky at sparky_right
    sp "Wow... That is a very heavy sigh."

    y "AH!"

    y "Where did you come from?"

    sp "The bench behind you."

    sp "I've been here for ten minutes."

    y "...Why?"

    sp "Sunshine. It's nice."

    sp "I'm Sparky! You're the otter who got buried in garbage, right?"

    y "Does everyone know about that?"

    sp "There's a video. It was pretty viral."

    y "Of course there is."

    show SparkyWorried at sparky_right
    sp "You look like you're carrying the whole city on your back."

    y "Because it feels like I am."

    y "We cleaned up, and people noticed. But it's not enough."

    y "It's going to take forever at this rate."

    sp "Mm."

    sp "Can I ask you something?"

    menu:
        "Sure, go ahead.":
            $ sparky_bond += 1
            sp "Thanks!"

        "Not really in the mood.":
            $ cynicism += 1
            sp "That's okay."
            sp "I'll ask anyway, but gently."

    sp "When was the last time you looked at what's gotten better?"

    y "..."

    y "Better?"

    y "I mean... there's still garbage."

    sp "That's what's wrong. It's what you're looking at."

    sp "I asked about 'what's better', about what has changed since you started this."

    jump sparky_walk


# THE WALK
label sparky_walk:

    scene bg city
    with fade

    show yinny at yinny_left
    show SparkyHappy at sparky_right

    sp "Come on. Walk with me."

    y "Where?"

    sp "Nowhere fancy. Just to look around, consider it as sightseeing."

    "They walk down the same street where Yinny was buried."

    "The sidewalk is visible."

    "A few otters are sorting recycling into bins."

    "A kid proudly shows her friend a bottle going into the right bin."

    sp "Remember this street?"

    y "I remember being under it."

    sp "Exactly. Look at it now."

    y "...It's a sidewalk."

    sp "A sidewalk!"

    sp "With nobody going around it or playing a 'game' of dodgeball with garbage!"

    menu:
        "It's a start, I guess.":
            $ sparky_bond += 1
            y "Okay. It is kind of nice."
            sp "See? Progress!"

        "That's the bare minimum.":
            $ cynicism += 1
            y "A sidewalk shouldn't count as an achievement."
            show SparkyWorried at sparky_right
            sp "Oh."
            sp "Well. It counts a little."

    "A group of otters waves at Yinny from across the street."

    "Yinny waves back, confused."

    sp "You know them?"

    y "No."

    sp "But they know you."

    sp "Your campaign got them out here. You got them to do something for the city."

    y "It was Trendy's campaign, not me."

    sp "Trendy's campaign, with YOU in it."

    y "..."

    y "I guess I never thought about people actually listening."

    jump sparky_river


# THE RIVER
label sparky_river:

    scene bg river
    with fade

    show yinny at yinny_left
    show sparky at sparky_right

    "The river is not clear."

    "But it is no longer a shopping cart graveyard."

    "Something silver flickers beneath the surface."

    y "Is that..."

    sp "A fish!"

    sp "A fish that's actually swimming!"

    y "On purpose?"

    sp "On purpose!"

    "Yinny watches the fish circle lazily."

    y "Stormy saw one last week. It was stuck in a cart."

    sp "Different fish. Or maybe he's moved up in the world."

    "Yinny laughs. It surprises them."

    y "Okay."

    y "Okay, that's actually pretty great."

    show SparkyHappy at sparky_right
    sp "There it is!"

    sp "That's the feeling I wanted you to find."

    y "But Sparky, it's not like the problem's solved."

    sp "Nope."

    sp "And it might not be for a long time."

    sp "But if you only count the finish line, you'll never notice you've been moving. The goal is important, but so are the steps you take to reach it."

    menu:
        "So I should just be happy with small wins?":
            $ sparky_bond += 1
            sp "Not 'just.' You should be proud of them AND keep going."
            sp "You get to do both. No one said you can only do one of them."

        "Small wins don't fix big problems.":
            $ cynicism += 1
            sp "..."
            show SparkySad at sparky_right
            sp "Maybe not individually..."
            sp "But they add up. Like drops into a bucket, with enough persistence, we will fill it."

    jump sparky_check


# CHECK FOR ENDING
label sparky_check:

    if cynicism >= 3:
        jump depression_ending
    else:
        jump sparky_resolution


# BAD ENDING: DEPRESSION
label depression_ending:

    scene bg river
    with fade

    show yinny at yinny_left
    show SparkySad at sparky_right

    y "You know what?"

    y "Even the fish is going to end up in a plastic bag."

    sp "Yinny..."

    y "The river will be polluted again in a year."

    y "And the city will have forgotten about us."

    y "And the sun will burn out eventually."

    sp "That's... a very long timeline."

    y "Nothing matters. We're a speck on a rock."

    sp "..."

    sp "I came to cheer you up."

    sp "But now I'm thinking about the sun."

    y "Yeah."

    sp "..."

    sp "Do you think the fish is okay?"

    y "No."

    sp "..."

    "Sparky slowly lowers their head."

    "The two otters sit in silence."

    "A single piece of trash floats by."

    "Neither of them has the energy to grab it."

    scene black
    with fade

    centered "ENDING UNLOCKED"

    centered "\"Depression\""

    centered "Yinny was so determined to be realistic that they made the sunshine otter give up."

    centered "That takes talent."

    pause 3.0

    return


# GOOD PATH: RESOLUTION
label sparky_resolution:

    scene bg river
    with dissolve

    show yinny at yinny_left
    show sparky at sparky_right

    y "I think I've been doing this wrong."

    sp "Oh?"

    y "I keep measuring everything against the perfect version."

    y "A clean city. Zero waste. Everything fixed."

    y "Anything less feels like failing."

    sp "That sounds exhausting."

    y "It is."

    sp "Want a trick?"

    y "Please."

    show SparkyHappy at sparky_right
    sp "Every night, think of one thing that got better today."

    sp "Doesn't matter how small."

    sp "A full recycling bin. A new volunteer. A fish."

    y "That's it?"

    sp "That's it."

    sp "Hope isn't pretending things are fine."

    sp "It's noticing that things can improve, and that you helped."

    menu:
        "Promise to try it":
            $ sparky_bond += 2
            y "Okay. I'll try."
            y "Today's thing is... the fish."
            sp "A great start!"

        "Joke about it":
            $ sparky_bond += 1
            y "Today's good thing is that nobody has dropped garbage on me."
            sp "A high bar, and you cleared it!"

    "Yinny watches the fish disappear under the water."

    y "Thanks, Sparky."

    y "I think I needed this."

    sp "Anytime!"

    sp "Also, I heard Stormy is building something."

    y "Building what?"

    sp "No idea."

    sp "But the last time Stormy said 'don't worry,' a wall caught fire."

    y "That's not reassuring."

    sp "I know!"

    sp "Let's go check on him!"

    y "..."

    y "Hopefully nothing's exploded yet."

    scene black
    with fade

    centered "Hope doesn't fix everything."

    centered "But it keeps you going long enough to fix something."

    pause 2.0

    jump act2_stormy


# STORMY PART OF ACT 2
label act2_stormy:

    jump act4
