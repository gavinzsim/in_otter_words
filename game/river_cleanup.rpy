# River Cleanup Minigame
#
# This file intentionally keeps the temporary minigame state separate from
# river_cleanup_score, so the final score remains available to later story
# labels after the screen closes.

define RIVER_CLEANUP_DURATION = 60.0
define RIVER_CLEANUP_SPAWN_INTERVAL = 1.25
define RIVER_CLEANUP_TARGET_LIFETIME = 3.0
define RIVER_CLEANUP_TARGET_SIZE = 180
define RIVER_CLEANUP_TRASH_POINTS = 1
define RIVER_CLEANUP_ANIMAL_POINTS = -1

default river_cleanup_score = 0
default river_cleanup_trash_collected = 0
default river_cleanup_animals_clicked = 0
default river_cleanup_active = False
default river_cleanup_remaining = 60
default river_cleanup_started_at = 0.0
default river_cleanup_next_id = 0
default river_cleanup_targets = []
default river_cleanup_popups = []

init python:
    # All entries deliberately use the same point values. The filenames are
    # mapped directly from the existing images folder; plastic rings are used
    # as the closest available visual for discarded netting.
    RIVER_CLEANUP_TRASH = (
        ("Plastic bottle", "images/trash_plastic_bottle.png"),
        ("Cigarette butts", "images/trash_cig_butts.png"),
        ("Discarded netting", "images/trash_plastic_rings.png"),
        ("Empty chip wrapper", "images/trash_chip_bag.png"),
        ("Balled-up paper", "images/trash_paper_ball.png"),
    )

    RIVER_CLEANUP_ANIMALS = (
        ("Salmon", "images/fish_salmon.png"),
        ("Pufferfish", "images/fish_pufferfish.png"),
        ("Tiny orca", "images/fish_tinyorca.png"),
        ("Crow", "images/bird_crow.png"),
        ("Seagull", "images/bird_seagull.png"),
    )

    def river_cleanup_now():
        return renpy.get_game_runtime()

    def river_cleanup_reset():
        """Starts a fresh round without touching any other story variables."""
        store.river_cleanup_score = 0
        store.river_cleanup_trash_collected = 0
        store.river_cleanup_animals_clicked = 0
        store.river_cleanup_active = True
        store.river_cleanup_remaining = int(RIVER_CLEANUP_DURATION)
        store.river_cleanup_started_at = river_cleanup_now()
        store.river_cleanup_next_id = 0
        store.river_cleanup_targets = []
        store.river_cleanup_popups = []

    def river_cleanup_spawn():
        if not store.river_cleanup_active:
            return

        elapsed = river_cleanup_now() - store.river_cleanup_started_at
        if elapsed >= RIVER_CLEANUP_DURATION:
            return

        # A 65/35 trash-to-animal mix and 1.25-second cadence normally gives
        # players roughly 10-20 points, while careful runs can exceed 20.
        is_trash = renpy.random.random() < 0.65
        name, image = renpy.random.choice(
            RIVER_CLEANUP_TRASH if is_trash else RIVER_CLEANUP_ANIMALS
        )

        store.river_cleanup_next_id += 1
        store.river_cleanup_targets.append({
            "id": store.river_cleanup_next_id,
            "name": name,
            "image": image,
            "points": RIVER_CLEANUP_TRASH_POINTS if is_trash else RIVER_CLEANUP_ANIMAL_POINTS,
            # The HUD occupies the top 150 pixels. The remaining bounds leave
            # a full target-size margin so no object can leave the screen.
            "x": renpy.random.randint(35, 1920 - RIVER_CLEANUP_TARGET_SIZE - 35),
            "y": renpy.random.randint(170, 1080 - RIVER_CLEANUP_TARGET_SIZE - 45),
            "drift": renpy.random.randint(-14, 14),
            "expires_at": river_cleanup_now() + RIVER_CLEANUP_TARGET_LIFETIME,
        })
        renpy.restart_interaction()

    def river_cleanup_remove_target(target_id):
        store.river_cleanup_targets = [
            target for target in store.river_cleanup_targets
            if target["id"] != target_id
        ]
        renpy.restart_interaction()

    def river_cleanup_expire(target_id):
        if store.river_cleanup_active:
            river_cleanup_remove_target(target_id)

    def river_cleanup_click(target_id):
        """Scores one target and removes it before another click can register."""
        if not store.river_cleanup_active:
            return

        for target in store.river_cleanup_targets:
            if target["id"] == target_id:
                river_cleanup_remove_target(target_id)
                store.river_cleanup_score += target["points"]
                if target["points"] > 0:
                    store.river_cleanup_trash_collected += 1
                else:
                    store.river_cleanup_animals_clicked += 1
                store.river_cleanup_popups.append({
                    "text": "+1" if target["points"] > 0 else "-1",
                    "color": "#b9f6ca" if target["points"] > 0 else "#ff9e9e",
                    "x": target["x"] + (RIVER_CLEANUP_TARGET_SIZE // 2),
                    "y": target["y"],
                    "expires_at": river_cleanup_now() + 0.8,
                })
                renpy.restart_interaction()
                return

    def river_cleanup_tick():
        if not store.river_cleanup_active:
            return

        elapsed = river_cleanup_now() - store.river_cleanup_started_at
        store.river_cleanup_remaining = max(
            0, int(__import__("math").ceil(RIVER_CLEANUP_DURATION - elapsed))
        )
        now = river_cleanup_now()
        store.river_cleanup_popups = [
            popup for popup in store.river_cleanup_popups
            if popup["expires_at"] > now
        ]
        renpy.restart_interaction()

    def river_cleanup_finish():
        """Stops every timer-driven action and clears only temporary objects."""
        store.river_cleanup_active = False
        store.river_cleanup_remaining = 0
        store.river_cleanup_targets = []
        store.river_cleanup_popups = []

    def river_cleanup_result_message():
        if store.river_cleanup_score >= 20:
            return "Great cleanup! The riverbank is looking much better."
        elif store.river_cleanup_score >= 10:
            return "Decent cleanup! Every piece of trash helped."
        return "The river still needs some help, but you made a start."


transform river_cleanup_float(drift=0):
    subpixel True
    alpha 0.0
    linear 0.12 alpha 1.0
    ease 0.9 xoffset drift
    ease 0.9 xoffset 0
    repeat

transform river_cleanup_popup:
    alpha 1.0
    yoffset 0
    parallel:
        linear 0.75 yoffset -45
    parallel:
        linear 0.75 alpha 0.0


screen river_cleanup():
    tag river_cleanup
    modal True

    # The gameplay background is explicitly drawn here, keeping the river in
    # view even if a future story label calls this screen from another scene.
    add "images/dirty_river.png"

    frame:
        xalign 0.5
        yalign 0.0
        xsize 1920
        ysize 145
        background Solid("#09253fe6")
        padding (55, 20)

        hbox:
            xfill True
            yalign 0.5
            spacing 40

            vbox:
                text "RIVER CLEANUP" size 34 color "#f4fbff" bold True
                text "Click trash  +1    Avoid animals  -1" size 22 color "#b7d9eb"

            null width 800

            vbox:
                xalign 1.0
                text "TIME  [river_cleanup_remaining]" xalign 1.0 size 35 color "#fff3b0" bold True
                text "SCORE  [river_cleanup_score]" xalign 1.0 size 30 color "#f4fbff" bold True

    for target in river_cleanup_targets:
        # Each target owns an expiration timer. The click action removes the
        # target immediately, so this timer can never score it a second time.
        timer max(0.01, target["expires_at"] - river_cleanup_now()) action Function(river_cleanup_expire, target["id"])

        imagebutton:
            xpos target["x"]
            ypos target["y"]
            idle Transform(target["image"], size=(RIVER_CLEANUP_TARGET_SIZE, RIVER_CLEANUP_TARGET_SIZE))
            hover Transform(target["image"], size=(RIVER_CLEANUP_TARGET_SIZE + 12, RIVER_CLEANUP_TARGET_SIZE + 12))
            at river_cleanup_float(target["drift"])
            action Function(river_cleanup_click, target["id"])
            tooltip target["name"]

    for popup in river_cleanup_popups:
        text popup["text"]:
            xpos popup["x"]
            ypos popup["y"]
            xanchor 0.5
            color popup["color"]
            size 48
            bold True
            outlines [(3, "#102030", 0, 0)]
            at river_cleanup_popup

    # Timers drive the game without a blocking Python loop.
    timer 0.10 repeat True action Function(river_cleanup_tick)
    timer RIVER_CLEANUP_SPAWN_INTERVAL repeat True action Function(river_cleanup_spawn)
    timer RIVER_CLEANUP_DURATION action [Function(river_cleanup_finish), Return()]


screen river_cleanup_instructions():
    tag river_cleanup_instructions
    modal True

    add "images/dirty_river.png"

    frame:
        xalign 0.5
        yalign 0.5
        xsize 1540
        ysize 880
        padding (55, 42)
        background Solid("#09253ff0")

        vbox:
            xfill True
            spacing 22

            text "RIVER CLEANUP" xalign 0.5 size 48 color "#f4fbff" bold True
            text "Clean up the litter before it drifts away!" xalign 0.5 size 27 color "#c8e6f5"

            hbox:
                xalign 0.5
                spacing 42

                frame:
                    xsize 670
                    ysize 505
                    padding (28, 24)
                    background Solid("#1c5b43e8")

                    vbox:
                        xfill True
                        spacing 14

                        text "CLICK TRASH" xalign 0.5 size 34 color "#b9f6ca" bold True
                        text "+1 point for every piece" xalign 0.5 size 23 color "#e5fff0"

                        hbox:
                            xalign 0.5
                            spacing 34

                            for image in ("images/trash_plastic_bottle.png", "images/trash_chip_bag.png", "images/trash_paper_ball.png"):
                                add Transform(image, size=(165, 165))

                frame:
                    xsize 670
                    ysize 505
                    padding (28, 24)
                    background Solid("#73333be8")

                    vbox:
                        xfill True
                        spacing 14

                        text "AVOID ANIMALS" xalign 0.5 size 34 color "#ffb8b8" bold True
                        text "-1 point if you click one" xalign 0.5 size 23 color "#ffe6e6"

                        hbox:
                            xalign 0.5
                            spacing 34

                            for image in ("images/fish_salmon.png", "images/fish_tinyorca.png", "images/bird_seagull.png"):
                                add Transform(image, size=(165, 165))

            text "You have 60 seconds. Click quickly, but watch what you click!" xalign 0.5 size 27 color "#fff3b0" bold True
            textbutton "Continue" xalign 0.5 action Return() text_size 30


screen river_cleanup_result():
    tag river_cleanup_result
    modal True

    add "images/dirty_river.png"

    frame:
        xalign 0.5
        yalign 0.5
        xsize 760
        ysize 415
        padding (48, 38)
        background Solid("#09253fed")

        vbox:
            xalign 0.5
            yalign 0.5
            spacing 24

            text "RIVER CLEANUP COMPLETE" xalign 0.5 size 42 color "#f4fbff" bold True
            text "Final score: [river_cleanup_score]" xalign 0.5 size 36 color "#fff3b0" bold True
            text "[river_cleanup_result_message()]" xalign 0.5 text_align 0.5 size 25 color "#c8e6f5"
            textbutton "Continue" xalign 0.5 action Return() text_size 28


label river_cleanup_start:

    # This label can also be called directly from a later story arc.
    show yinny at yinny_left
    show spendy normal at spendy_right

    p "Before we start planning upgrades, let's clear the litter we can reach."
    y "A river cleanup? I can do that."
    y "Trash gets picked up. Fish and birds get left alone. Got it."

    hide yinny
    hide spendy
    window hide

    call screen river_cleanup_instructions
    $ river_cleanup_reset()
    call screen river_cleanup
    call screen river_cleanup_result

    window auto
    show yinny at yinny_left
    show spendy normal at spendy_right

    # The final score stays in river_cleanup_score for the rest of the story.
    if river_cleanup_score >= 20:
        y "Okay... the river actually looks way better."
    elif river_cleanup_score >= 10:
        y "Not perfect, but definitely better than before."
    else:
        y "Uh... maybe cleanup isn't my strongest skill."

    jump spendy_water_investigation
