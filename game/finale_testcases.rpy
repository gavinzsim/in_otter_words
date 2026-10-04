# Engine-level smoke test for the local finale presentation.
init python:
    def test_generated_response(context):
        scene = {"background": "untrusted/path", "characters": ["Yinny", "Stormy", "Sparky"],
                 "speaker": "Unknown", "expression": "happy",
                 "text": "The next safe step belongs to all of us.", "outcome_for": []}
        scenes = []
        for name in FINALE_MAIN_OTTERS:
            beat = dict(scene)
            beat["text"] = "%s found a new direction after the city's changes." % name
            beat["outcome_for"] = [name]
            scenes.append(beat)
        return validate_finale({"ending_title": "A Shared Start", "summary": "The team imagines a shared future.",
                                "scenes": scenes,
                                "final_line": "Keep making small changes together."})

testcase finale_fallback_render:
    $ os.environ.pop("OPENROUTER_API_KEY", None)
    $ store.openrouter_key = None
    run Jump("finale")
    advance until "The End" timeout 30.0
    assert eval finale_result is not None
    assert eval len(finale_result["scenes"]) == 5
    exit

testcase finale_generated_render:
    $ store.openrouter_key = "test-local-key"
    assert eval load_openrouter_key() == "test-local-key"
    $ request_openrouter_finale = test_generated_response
    run Jump("finale")
    advance until "The End" timeout 30.0
    assert eval finale_result["ending_title"] == "A Shared Start"
    assert eval finale_result["scenes"][0]["background"] == "park"
    assert eval finale_result["scenes"][0]["speaker"] == "Narrator"
    exit
