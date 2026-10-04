# Engine-level smoke test for the local finale presentation.
init python:
    def test_generated_response(context):
        scene = {"background": "untrusted/path", "characters": ["Yinny", "Stormy", "Sparky"],
                 "speaker": "Unknown", "text": "The next safe step belongs to all of us."}
        return validate_finale({"ending_title": "A Shared Start", "tone": "hopeful",
                                "reflection": "Yinny thinks about the team's work.",
                                "scenes": [dict(scene) for _ in range(8)],
                                "closing_message": "Keep making small changes together."})

testcase finale_fallback_render:
    $ os.environ.pop("OPENROUTER_API_KEY", None)
    $ store.openrouter_key = None
    run Jump("finale")
    advance until "The End" timeout 30.0
    assert eval finale_result is not None
    assert eval len(finale_result["scenes"]) == 8
    exit

testcase finale_generated_render:
    $ request_openrouter_finale = test_generated_response
    run Jump("finale")
    advance until "The End" timeout 30.0
    assert eval finale_result["ending_title"] == "A Shared Start"
    assert eval finale_result["scenes"][0]["background"] == "park"
    assert eval finale_result["scenes"][0]["speaker"] == "Narrator"
    exit
