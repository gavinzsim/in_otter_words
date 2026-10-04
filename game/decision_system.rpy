# All story choice values live here. Existing act variables still control their
# original branches; these values only describe the completed playthrough.
default decision_log = []
default total_decision_score = 0
default relationship_scores = {"Trendy": 0, "Spendy": 0, "Sparky": 0, "Stormy": 0}
default trait_scores = {"awareness": 0, "practicality": 0, "optimism": 0, "responsibility": 0, "community": 0, "innovation": 0}
default finale_machine_outcome = "not_reached"
default finale_result = None
default finale_scene_index = 0

init python:
    import json
    import os

    def decision_option(tier, summary, relationships=None, traits=None):
        return {"tier": tier, "summary": summary,
                "relationships": relationships or {}, "traits": traits or {}}

    # Option keys are implementation IDs, never displayed to players.
    DECISION_CATALOG = {
        "wake_up_alarm": {"arc": "opening", "prompt": "Will Yinny get out of bed?", "options": {
            "get_up": decision_option("best", "Yinny got up to face the day.", traits={"responsibility": 1}),
            "snooze": decision_option("worst", "Yinny snoozed the alarm and delayed facing the day.", traits={"responsibility": -1})}},
        "help_garbage_problem": {"arc": "opening", "prompt": "Will Yinny help Stormy address the city's pollution?", "options": {
            "help": decision_option("best", "Yinny agreed to help Stormy tackle the neighborhood's pollution.", {"Stormy": 1}, {"awareness": 1, "community": 1}),
            "ignore": decision_option("worst", "Yinny left the garbage problem to someone else.", {"Stormy": -1}, {"responsibility": -1, "community": -1})}},
        "trendy_campaign_focus": {"arc": "act_1", "prompt": "What should Trendy's campaign focus on?", "options": {
            "invite": decision_option("best", "Yinny showed the garbage problem and invited neighbors to help fix it.", {"Trendy": 1}, {"awareness": 1, "community": 1}),
            "dramatic": decision_option("okay", "Yinny used dramatic garbage photos to draw attention, without a direct invitation.", traits={"awareness": 1}),
            "blame": decision_option("worst", "Yinny blamed residents for the city's garbage and alienated volunteers.", {"Trendy": -1}, {"community": -1, "responsibility": -1})}},
        "trendy_cleanup_post": {"arc": "act_1", "prompt": "What should the cleanup post include?", "options": {
            "details": decision_option("best", "Yinny provided a meeting place, time, supplies, and signup link for the cleanup.", {"Trendy": 1}, {"practicality": 1, "community": 1}),
            "snacks": decision_option("okay", "Yinny offered snacks and a group photo, but left out practical cleanup details.", traits={"community": 1}),
            "guilt": decision_option("worst", "Yinny guilted residents into attending the cleanup.", {"Trendy": -1}, {"community": -1, "responsibility": -1})}},
        "trendy_criticism_reply": {"arc": "act_1", "prompt": "How should Yinny answer criticism that one cleanup cannot fix the city?", "options": {
            "one_block": decision_option("best", "Yinny acknowledged the limits of one cleanup and invited progress on one block.", {"Trendy": 1}, {"practicality": 1, "optimism": 1, "community": 1}),
            "start_small": decision_option("okay", "Yinny honestly proposed starting small and seeing where it leads.", traits={"practicality": 1, "optimism": 1}),
            "dismiss": decision_option("worst", "Yinny told a critic to stay home and enjoy the garbage.", {"Trendy": -1}, {"community": -1, "optimism": -1})}},
        "spendy_water_solution": {"arc": "act_2", "prompt": "Which water improvement should the city install?", "options": {
            "screens": decision_option("okay", "Yinny chose inexpensive runoff screens, a limited but affordable improvement.", {"Spendy": 1}, {"practicality": 1}),
            "modular": decision_option("best", "Yinny chose effective modular filtration that the city can repair and expand.", {"Spendy": 1}, {"practicality": 1, "responsibility": 1}),
            "aqua_sovereign": decision_option("worst", "Yinny spent the whole budget on the impressive Aqua-Sovereign 9000, leaving no maintenance funds.", {"Spendy": -1}, {"practicality": -1, "responsibility": -1})}},
        "spendy_pipe": {"arc": "act_2", "prompt": "What should the city do about the damaged runoff pipe?", "options": {
            "repair": decision_option("best", "Yinny repaired the leaking pipe and stopped pollution at its source.", {"Spendy": 1}, {"practicality": 1, "responsibility": 1}),
            "testing": decision_option("okay", "Yinny funded public testing and refill stations, informing residents while the pipe kept leaking.", traits={"awareness": 1, "community": 1}),
            "fountain": decision_option("worst", "Yinny bought an expensive awareness fountain while the polluted pipe kept leaking.", {"Spendy": -1}, {"practicality": -1, "responsibility": -1})}},
        "spendy_valve": {"arc": "act_2", "prompt": "How should the city handle the corroded pressure valve?", "options": {
            "standard": decision_option("best", "Yinny installed a reliable, repairable standard valve.", {"Spendy": 1}, {"practicality": 1, "responsibility": 1}),
            "monitor": decision_option("okay", "Yinny monitored the failing valve until a replacement could be funded.", traits={"practicality": 1, "awareness": 1}),
            "premium": decision_option("worst", "Yinny bought an overpriced smart valve with decorative features.", {"Spendy": -1}, {"practicality": -1, "responsibility": -1})}},
        "sparky_listen": {"arc": "act_3", "prompt": "Will Yinny listen to Sparky in the park?", "options": {
            "listen": decision_option("best", "Yinny made room to listen to Sparky's perspective.", {"Sparky": 1}, {"awareness": 1, "optimism": 1}),
            "decline": decision_option("worst", "Yinny brushed off Sparky's offer to talk.", {"Sparky": -1}, {"optimism": -1})}},
        "sparky_sidewalk": {"arc": "act_3", "prompt": "How does Yinny see the cleaner sidewalk?", "options": {
            "start": decision_option("best", "Yinny recognized the cleared sidewalk as a useful start.", {"Sparky": 1}, {"awareness": 1, "optimism": 1}),
            "bare_minimum": decision_option("worst", "Yinny dismissed the cleaner sidewalk as the bare minimum.", {"Sparky": -1}, {"optimism": -1})}},
        "sparky_small_wins": {"arc": "act_3", "prompt": "How does Yinny react to small wins at the river?", "options": {
            "ask": decision_option("best", "Yinny asked whether small wins are enough, giving Sparky room to explain persistence.", {"Sparky": 1}, {"awareness": 1, "optimism": 1}),
            "dismiss": decision_option("worst", "Yinny dismissed small wins as unable to help with bigger problems.", {"Sparky": -1}, {"optimism": -1})}},
        "sparky_daily_reflection": {"arc": "act_3", "prompt": "Will Yinny try Sparky's daily reflection?", "options": {
            "promise": decision_option("best", "Yinny promised to notice one improvement each day, beginning with the fish.", {"Sparky": 1}, {"optimism": 1, "responsibility": 1}),
            "joke": decision_option("okay", "Yinny joked about a day without falling garbage, but accepted Sparky's hopeful practice.", {"Sparky": 1}, {"optimism": 1})}},
        "stormy_visit": {"arc": "act_4", "prompt": "Will Yinny see Stormy's new machine?", "options": {
            "enthusiastic": decision_option("best", "Yinny eagerly agreed to see Stormy's new machine.", {"Stormy": 1}, {"community": 1}),
            "reluctant": decision_option("worst", "Yinny initially rejected Stormy's invitation, then agreed after seeing him hurt.", {"Stormy": -1}, {"community": -1})}},
        "stormy_first_component": {"arc": "act_4", "prompt": "Which first component should Yinny bring?", "options": {
            "wrench": decision_option("best", "Yinny brought the calibration wrench needed for Stormy's machine.", {"Stormy": 1}, {"practicality": 1, "innovation": 1}),
            "duck": decision_option("worst", "Yinny brought a rubber duck instead of the needed calibration wrench.", {"Stormy": -1}, {"practicality": -1, "innovation": -1})}},
        "stormy_stabilizer": {"arc": "act_4", "prompt": "Which component should stabilize the machine?", "options": {
            "bucket": decision_option("best", "Yinny selected the giant bucket that stabilizes the machine.", {"Stormy": 1}, {"practicality": 1, "innovation": 1}),
            "spoon": decision_option("worst", "Yinny selected a giant spoon instead of a stabilizing bucket.", {"Stormy": -1}, {"practicality": -1, "innovation": -1})}},
        "stormy_sorting": {"arc": "act_4", "prompt": "Should the machine sort collected garbage?", "options": {
            "sort": decision_option("best", "Yinny installed a sorting system for recyclables and other garbage, protecting the machine.", {"Stormy": 1}, {"responsibility": 1, "innovation": 1}),
            "skip": decision_option("worst", "Yinny skipped the machine's sorting and safety system to finish faster.", {"Stormy": -1}, {"responsibility": -1, "innovation": -1})}},
    }
    TIER_POINTS = {"best": 2, "okay": 1, "worst": 0}

    def record_decision(decision_id, option_id, occurrence=1):
        definition = DECISION_CATALOG[decision_id]
        option = definition["options"][option_id]
        unique_id = decision_id if decision_id != "wake_up_alarm" else "wake_up_alarm_%d" % occurrence
        if any(item["id"] == unique_id for item in store.decision_log):
            return
        scores = [TIER_POINTS[item["tier"]] for item in definition["options"].values()]
        entry = {"id": unique_id, "decision_id": decision_id, "arc": definition["arc"],
                 "prompt": definition["prompt"], "choice": option["summary"],
                 "tier": option["tier"], "score": TIER_POINTS[option["tier"]],
                 "min_score": min(scores), "max_score": max(scores),
                 "characters": list(option["relationships"].keys()),
                 "relationship_changes": dict(option["relationships"]),
                 "traits": dict(option["traits"]), "summary": option["summary"]}
        # Reassignment is tracked cleanly by Ren'Py's save and rollback system.
        store.decision_log = store.decision_log + [entry]
        store.total_decision_score += entry["score"]
        store.relationship_scores = {key: value + option["relationships"].get(key, 0)
                                     for key, value in store.relationship_scores.items()}
        store.trait_scores = {key: value + option["traits"].get(key, 0)
                              for key, value in store.trait_scores.items()}

    def build_finale_context():
        decisions = list(store.decision_log)
        actual = sum(item["score"] for item in decisions)
        lowest = sum(item["min_score"] for item in decisions)
        highest = sum(item["max_score"] for item in decisions)
        percentage = round(100.0 * (actual - lowest) / (highest - lowest), 1) if highest > lowest else 0.0
        assessment = "high" if percentage >= 66.7 else "mixed" if percentage >= 33.3 else "low"
        return {"game": "In Otter Words", "scoring": {"actual_score": actual,
                "worst_possible_score": lowest, "best_possible_score": highest,
                "percentage": percentage, "scored_decisions": len(decisions), "assessment": assessment},
                "relationships": dict(store.relationship_scores), "traits": dict(store.trait_scores),
                "minigames": [{"name": "River Cleanup", "score": store.river_cleanup_score},
                              {"name": "Stormy's Machine", "correct_components": store.correct_tools,
                               "wrong_components": store.wrong_tools, "safety": store.safety,
                               "teamwork": store.teamwork, "outcome": store.finale_machine_outcome}],
                "story_state": {"community_support": store.community_support,
                                "water_quality": store.water_quality, "city_budget": store.city_budget,
                                "water_solution": store.water_solution,
                                "sparky_bond": store.sparky_bond, "cynicism": store.cynicism},
                "decisions": decisions}

    def write_finale_context(context):
        # config.savedir is the user-writable Ren'Py save location in builds.
        try:
            os.makedirs(config.savedir, exist_ok=True)
            path = os.path.join(config.savedir, "finale_context.json")
            with open(path, "w", encoding="utf-8") as output:
                json.dump(context, output, ensure_ascii=False, indent=2)
            return path
        except (OSError, TypeError, ValueError) as error:
            renpy.log("[Finale] Could not write context file: %s" % type(error).__name__)
            return None

    def debug_finale_state():
        context = build_finale_context()
        renpy.log("[Finale] Debug state: %s" % json.dumps(context, ensure_ascii=False))
        return context
