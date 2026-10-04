default finale_context = None

init python:
    def _fallback_beat(background, characters, speaker, text):
        return {"background": background, "characters": characters,
                "speaker": speaker, "expression": "normal", "text": text}

    def build_fallback_finale(context):
        # One neutral emergency ending. No score, relationship, or story-state
        # branch may select or alter it; normal play always requests the LLM.
        return {"ending_title": "The Story Continues", "summary": "Technical fallback only.",
                "scenes": [
                    _fallback_beat("park", ["Yinny"], "Narrator", "The city continued to change."),
                    _fallback_beat("park", ["Yinny"], "Narrator", "Some things improved. Others still needed work."),
                    _fallback_beat("park", ["Yinny", "Stormy"], "Narrator", "Yinny knew every choice had left its mark."),
                    _fallback_beat("park", ["Yinny", "Stormy"], "Stormy", "You're thinking way too hard again."),
                    _fallback_beat("park", ["Yinny", "Stormy"], "Yinny", "Probably."),
                ],
                "final_line": "Whatever came next, they would face it one day at a time."}

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
            if name == scene.get("speaker"):
                sprite = FINALE_EXPRESSIONS[name].get(scene.get("expression"), sprite)
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
    $ renpy.say(centered, "Finale: What Kind of Change Did Yinny Make?")
    $ renpy.say(centered, finale_result["ending_title"])

    while finale_scene_index < len(finale_result["scenes"]):
        $ render_finale_scene(finale_result["scenes"][finale_scene_index])
        $ finale_scene_index += 1

    $ renpy.say(None, finale_result["final_line"])
    scene black
    with fade
    centered "The End"
    return
