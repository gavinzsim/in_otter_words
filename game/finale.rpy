default finale_context = None

init python:
    def _fallback_beat(background, characters, speaker, text):
        return {"background": background, "characters": characters,
                "speaker": speaker, "text": text}

    def build_fallback_finale(context):
        score = context["scoring"]["assessment"]
        relationships = context["relationships"]
        traits = context["traits"]
        story = context["story_state"]
        machine = context["minigames"][1]["outcome"]
        city = "clean_city" if story["community_support"] >= 4 else "dirty_city"
        river = "clean_river" if story["water_quality"] >= 60 else "dirty_river"
        lab = "stormy_lab" if machine == "working_with_maintenance_plan" else "damaged_lab"
        title = {"high": "Small Ripples, Wider Circles", "mixed": "A Work in Progress",
                 "low": "The Next Small Step"}[score]
        reflection = {
            "high": "Yinny sees how much changed when neighbors kept showing up for one another.",
            "mixed": "Some plans worked, and some left a mess. Yinny takes another look at what can be repaired.",
            "low": "The city still carries the weight of rushed choices. Yinny cannot pretend otherwise.",
        }[score]
        trendy = ("You helped people find a place to start. They're still showing up." if relationships["Trendy"] > 0
                  else "The turnout wasn't what I hoped. Next time, let's make the invitation clearer.")
        spendy = ("The water work can keep improving because we left room to maintain it." if relationships["Spendy"] > 0
                  else "We learned the hard way that a repair plan needs a budget too.")
        sparky = ("See? You can notice what got better and still care about what's left." if relationships["Sparky"] > 0
                  else "You don't have to feel cheerful about it. Just don't miss the next chance to help.")
        stormy = ("The test worked. Now the team needs to keep checking it together." if machine == "working_with_maintenance_plan"
                  else "The prototype broke. We need to rebuild it safely, with everyone checking the plan.")
        if story["community_support"] >= 4:
            city_line = "Neighbors are already organizing another cleanup down the street."
        else:
            city_line = "A few neighbors are still collecting litter, even though the street needs more hands."
        if story["water_quality"] >= 60:
            river_line = "The river is clearer near the bank, though the upstream work continues."
        else:
            river_line = "The river is still cloudy. The first repairs helped, but there is more to do."
        if traits["innovation"] < 0 or machine != "working_with_maintenance_plan":
            innovation_line = "A clever invention still needs a checklist and people willing to question it."
        else:
            innovation_line = "A good invention works best when people take care of it after the test."
        scenes = [
            _fallback_beat(city, ["Yinny", "Trendy"], "Narrator", city_line),
            _fallback_beat(city, ["Yinny", "Trendy"], "Trendy", trendy),
            _fallback_beat(river, ["Yinny", "Spendy"], "Narrator", river_line),
            _fallback_beat(river, ["Yinny", "Spendy"], "Spendy", spendy),
            _fallback_beat("park", ["Yinny", "Sparky"], "Sparky", sparky),
            _fallback_beat(lab, ["Yinny", "Stormy"], "Stormy", stormy),
            _fallback_beat(lab, ["Yinny", "Stormy"], "Yinny", innovation_line),
            _fallback_beat(city, ["Yinny"], "Yinny", "I can't do all of this alone. But I can take the next step with them."),
        ]
        return {"ending_title": title, "tone": "hopeful" if score == "high" else "reflective",
                "reflection": reflection, "scenes": scenes,
                "closing_message": "Small, steady changes grow when a community keeps making them together."}

    def render_finale_scene(scene):
        background = FINALE_BACKGROUNDS.get(scene.get("background"), FINALE_BACKGROUNDS[FINALE_DEFAULT_BACKGROUND])
        renpy.scene()
        renpy.show(background)
        names = [name for name in scene.get("characters", []) if name in FINALE_SPRITES]
        if "Yinny" in names:
            names.remove("Yinny")
            names.insert(0, "Yinny")
        for index, name in enumerate(names[:3]):
            sprite, usual_transform = FINALE_SPRITES[name]
            if name == "Yinny":
                placement = store.yinny_left
            elif len(names) == 1:
                placement = store.center
            elif index == 1 and len(names) == 3:
                placement = store.center
            elif index == 2:
                placement = store.right
            else:
                placement = getattr(store, usual_transform)
            renpy.show(sprite, at_list=[placement])
        renpy.with_statement(store.dissolve)
        speaker = {"Yinny": store.y, "Trendy": store.t, "Spendy": store.p,
                   "Sparky": store.sp, "Stormy": store.s}.get(scene.get("speaker"))
        renpy.say(speaker, scene["text"])

screen finale_loading():
    zorder 100
    frame:
        xalign 0.5
        yalign 0.08
        background Solid("#09253fe6")
        padding (30, 18)
        text "Yinny looks back at everything that's happened..." color "#f4fbff" size 30

label finale:
    $ finale_context = build_finale_context()
    $ finale_scene_index = 0
    $ renpy.log("[Finale] Score: %d / %d" % (finale_context["scoring"]["actual_score"], finale_context["scoring"]["best_possible_score"]))
    $ renpy.log("[Finale] Decisions recorded: %d" % finale_context["scoring"]["scored_decisions"])
    $ renpy.log("[Finale] Building finale context...")
    $ write_finale_context(finale_context)

    scene bg park
    with dissolve
    show yinny at yinny_left
    "Yinny looks back at everything that's happened..."
    show screen finale_loading
    $ renpy.pause(0.1, hard=True)
    $ finale_result = generate_finale(finale_context)
    hide screen finale_loading

    scene bg park
    with fade
    $ renpy.say(centered, "Finale — What Kind of Change Did Yinny Make?")
    $ renpy.say(centered, finale_result["ending_title"])
    $ renpy.say(None, finale_result["reflection"])

    while finale_scene_index < len(finale_result["scenes"]):
        $ render_finale_scene(finale_result["scenes"][finale_scene_index])
        $ finale_scene_index += 1

    scene bg park
    with fade
    show yinny at yinny_left
    $ renpy.say(None, finale_result["closing_message"])
    scene black
    with fade
    centered "The End"
    return
