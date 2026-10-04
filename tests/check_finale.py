"""Run with the Ren'Py SDK Python: python.exe tests/check_finale.py."""
import copy
import json
import os
import pathlib
import pickle
import re
import tempfile
import types

GAME = pathlib.Path(__file__).resolve().parents[1] / "game"


def load_init_python(filename, namespace):
    lines = (GAME / filename).read_text(encoding="utf-8").splitlines()
    inside = False
    body = []
    for line in lines:
        if line == "init python:":
            inside = True
            continue
        if inside and line and not line.startswith("    "):
            break
        if inside:
            body.append(line[4:] if line else "")
    exec(compile("\n".join(body), str(GAME / filename), "exec"), namespace)


def environment(save_dir):
    store = types.SimpleNamespace(
        decision_log=[], total_decision_score=0,
        relationship_scores=dict.fromkeys(("Trendy", "Spendy", "Sparky", "Stormy"), 0),
        trait_scores=dict.fromkeys(("awareness", "practicality", "optimism", "responsibility", "community", "innovation"), 0),
        river_cleanup_score=17, river_cleanup_trash_collected=19,
        river_cleanup_animals_clicked=2, correct_tools=0, wrong_tools=0, safety=0, teamwork=0,
        finale_machine_outcome="prototype_broke_after_unsafe_build",
        openrouter_key=None,
        community_support=0, water_quality=35, city_budget=20, water_solution="cheap",
        sparky_bond=0, cynicism=0,
    )
    logs = []
    namespace = {"store": store, "renpy": types.SimpleNamespace(log=logs.append),
                 "config": types.SimpleNamespace(savedir=save_dir)}
    for filename in ("decision_system.rpy", "openrouter_finale.rpy", "finale.rpy"):
        load_init_python(filename, namespace)
    return namespace, store, logs


def play(namespace, picks):
    for decision_id, option, occurrence in picks:
        namespace["record_decision"](decision_id, option, occurrence)
    return namespace["build_finale_context"]()


def picks(*pairs):
    return [(decision_id, option, 1) for decision_id, option in pairs]


def main():
    with tempfile.TemporaryDirectory() as save_dir:
        ns, store, logs = environment(save_dir)
        best_picks = [(key, next(option for option, data in item["options"].items()
                                 if data["tier"] == "best"), 1)
                      for key, item in ns["DECISION_CATALOG"].items()]
        best = play(ns, best_picks)
        assert (best["scoring"]["actual_score"], best["scoring"]["best_possible_score"]) == (32, 32)
        assert best["scoring"]["scored_decisions"] == 16
        assert best["scoring"]["best_choices"] == 16
        assert best["scoring"]["okay_choices"] == 0
        assert best["scoring"]["worst_choices"] == 0
        assert best["relationships"]["Stormy"] > 0
        assert best["minigames"][0]["score"] == 17
        assert best["minigames"][0]["trash_collected"] == 19
        assert best["minigames"][0]["animals_accidentally_clicked"] == 2
        assert best["character_context"]["Trendy"]["choices_with_yinny"]
        assert best["environmental_outcomes_so_far"]["machine"]
        assert best["behavior_patterns"]
        assert not any("strongest in" in pattern for pattern in best["behavior_patterns"])
        assert all(item["consequence"] and item["situation"] for item in best["decisions"])
        assert len(ns["build_fallback_finale"](best)["scenes"]) == 5
        assert ns["write_finale_context"](best) == str(pathlib.Path(save_dir) / "finale_context.json")
        assert json.loads((pathlib.Path(save_dir) / "finale_context.json").read_text(encoding="utf-8")) == best
        restored_store = pickle.loads(pickle.dumps(store))
        ns["store"] = restored_store
        assert ns["build_finale_context"]()["decisions"] == best["decisions"]

        # Every story menu option is catalogued and every mapped image is real.
        story_files = [GAME / name for name in ("script.rpy", "act1.rpy", "act2.rpy", "act3.rpy", "act4.rpy")]
        story_text = "\n".join(path.read_text(encoding="utf-8") for path in story_files)
        assert story_text.count("menu:") == len(ns["DECISION_CATALOG"]) == 16
        assert story_text.count("$ record_decision(") == sum(len(item["options"]) for item in ns["DECISION_CATALOG"].values()) == 38
        assert all(set(item["options"]) == set(ns["DECISION_CONSEQUENCES"][key])
                   for key, item in ns["DECISION_CATALOG"].items())
        declared = {}
        for match in re.finditer(r'^image (.+?) = "(images/[^"]+)"', story_text, re.MULTILINE):
            declared[match.group(1)] = match.group(2)
        images = list(ns["FINALE_BACKGROUNDS"].values())
        images += [pose for variants in ns["FINALE_EXPRESSIONS"].values() for pose in variants.values()]
        for image_name in images:
            assert image_name in declared, image_name
            assert (GAME / declared[image_name]).is_file(), image_name

        ns, store, logs = environment(save_dir)
        mixed = play(ns, picks(("wake_up_alarm", "get_up"), ("trendy_campaign_focus", "dramatic"),
                               ("spendy_water_solution", "screens"), ("sparky_listen", "decline"),
                               ("stormy_sorting", "sort")))
        assert mixed["scoring"]["actual_score"] == 6
        assert (mixed["scoring"]["best_choices"], mixed["scoring"]["okay_choices"],
                mixed["scoring"]["worst_choices"]) == (2, 2, 1)
        assert ns["build_fallback_finale"](mixed) == ns["build_fallback_finale"](best)

        # This low route can pass the existing Act 1 and Act 3 ending gates.
        ns, store, logs = environment(save_dir)
        low_route = [("wake_up_alarm", "snooze", 1), ("wake_up_alarm", "snooze", 2),
                     ("wake_up_alarm", "get_up", 3)] + picks(
            ("help_garbage_problem", "help"), ("trendy_campaign_focus", "blame"),
            ("trendy_cleanup_post", "guilt"), ("trendy_criticism_reply", "one_block"),
            ("spendy_water_solution", "screens"), ("spendy_pipe", "testing"),
            ("spendy_valve", "premium"), ("sparky_listen", "decline"),
            ("sparky_sidewalk", "bare_minimum"), ("sparky_small_wins", "ask"),
            ("sparky_daily_reflection", "joke"), ("stormy_visit", "reluctant"),
            ("stormy_first_component", "duck"), ("stormy_stabilizer", "spoon"),
            ("stormy_sorting", "skip"))
        low = play(ns, low_route)
        assert low["scoring"]["actual_score"] == 11
        assert low["scoring"]["best_possible_score"] == 36
        assert low["scoring"]["percentage"] < 33.3
        assert ns["build_fallback_finale"](low) == ns["build_fallback_finale"](best)
        ns["record_decision"]("wake_up_alarm", "snooze", 1)
        assert len(store.decision_log) == 18  # Revisiting a label never double counts.
        assert json.loads(json.dumps(low))["decisions"] == low["decisions"]

        # Equal overall scores still yield distinct character and behavior context.
        other_ns, _, _ = environment(save_dir)
        route_a = play(other_ns, picks(("trendy_campaign_focus", "invite"),
                                       ("spendy_water_solution", "aqua_sovereign")))
        another_ns, _, _ = environment(save_dir)
        route_b = play(another_ns, picks(("trendy_campaign_focus", "blame"),
                                         ("spendy_water_solution", "modular")))
        assert route_a["scoring"]["actual_score"] == route_b["scoring"]["actual_score"] == 2
        assert route_a["character_context"] != route_b["character_context"]
        assert route_a["behavior_patterns"] != route_b["behavior_patterns"]

        # Missing key and malformed API JSON both choose the local finale.
        prior_key = os.environ.get("OPENROUTER_API_KEY")
        prior_urlopen = ns["urllib"].request.urlopen
        try:
            os.environ.pop("OPENROUTER_API_KEY", None)
            assert ns["generate_finale"](low)["ending_title"] == "The Story Continues"
            store.openrouter_key = "local-test-secret"
            assert ns["load_openrouter_key"]() == "local-test-secret"
            os.environ["OPENROUTER_API_KEY"] = "test-secret"
            assert ns["load_openrouter_key"]() == "local-test-secret"
            store.openrouter_key = None
            assert ns["load_openrouter_key"]() == "test-secret"

            class InvalidResponse:
                status = 200
                def __enter__(self):
                    return self
                def __exit__(self, *args):
                    pass
                def read(self, amount):
                    return b'{"choices":[{"message":{"content":"{broken"}}]}'

            def fake_urlopen(request, timeout):
                assert timeout == 90
                assert request.full_url == ns["OPENROUTER_FINALE_URL"]
                payload = json.loads(request.data)
                assert payload["model"] == "z-ai/glm-5.3-flash"
                assert payload["provider"]["require_parameters"]
                assert json.loads(payload["messages"][1]["content"].split("\n")[1]) == low
                return InvalidResponse()

            ns["urllib"].request.urlopen = fake_urlopen
            assert ns["generate_finale"](low)["ending_title"] == "The Story Continues"
            assert not any("test-secret" in line for line in logs)

            valid = {"ending_title": "A Different Future", "summary": "The city changes in unexpected ways.",
                     "scenes": [{"background": "park", "characters": ["Yinny", "Trendy"],
                                 "speaker": "Trendy", "expression": "happy",
                                 "text": "Remember our cleanup?"} for _ in range(8)],
                     "final_line": "There was still another day to shape."}
            class ValidResponse(InvalidResponse):
                def read(self, amount):
                    return json.dumps({"choices": [{"message": {"content": json.dumps(valid)}}]}).encode("utf-8")
            ns["urllib"].request.urlopen = lambda request, timeout: ValidResponse()
            assert ns["generate_finale"](low)["ending_title"] == "A Different Future"
        finally:
            ns["urllib"].request.urlopen = prior_urlopen
            if prior_key is None:
                os.environ.pop("OPENROUTER_API_KEY", None)
            else:
                os.environ["OPENROUTER_API_KEY"] = prior_key

        scene = {"background": "../../private", "characters": ["Yinny", "Alien"],
                 "speaker": "Alien", "expression": "shocked", "text": "Look [secret] {tag}!"}
        data = {"ending_title": "Ripples", "summary": "A complicated future.",
                "scenes": [copy.deepcopy(scene) for _ in range(8)], "final_line": "Keep going."}
        validated = ns["validate_finale"](data)
        assert validated["scenes"][0]["background"] == "park"
        assert validated["scenes"][0]["characters"] == ["Yinny"]
        assert validated["scenes"][0]["speaker"] == "Narrator"
        assert "[" not in validated["scenes"][0]["text"]
        assert ns["resolve_finale_background"]("clean_city_sunset") == "clean_city"
        assert ns["resolve_finale_background"]("broken_lab") == "damaged_lab"
        # A valid model response is returned unchanged in direction and title.
        ns["request_openrouter_finale"] = lambda context: validated
        assert ns["generate_finale"](low)["ending_title"] == "Ripples"
    print("Finale checks passed: context depth, choice counts, menu coverage, assets, varied scores, one fallback, save state, JSON, request, invalid visuals, dedup.")


if __name__ == "__main__":
    main()
