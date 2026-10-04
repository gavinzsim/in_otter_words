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
    ARC_CHARACTERS = {"opening": "Stormy", "act_1": "Trendy", "act_2": "Spendy",
                      "act_3": "Sparky", "act_4": "Stormy"}
    DECISION_CONSEQUENCES = {
        "wake_up_alarm": {
            "get_up": "Yinny left the bedroom and encountered the city's pollution.",
            "snooze": "The alarm rang again; a third snooze ends Yinny's day before the main story."},
        "help_garbage_problem": {
            "help": "Stormy introduced Yinny to friends who were already working on local problems.",
            "ignore": "Stormy was disappointed and Yinny walked away; this ends the story early."},
        "trendy_campaign_focus": {
            "invite": "Trendy liked the constructive message and community support increased.",
            "dramatic": "The photos drew attention, but the invitation was less useful.",
            "blame": "Trendy objected to insulting residents and community support fell."},
        "trendy_cleanup_post": {
            "details": "Volunteers received the practical information needed to join the cleanup.",
            "snacks": "The post offered a social incentive but not the cleanup logistics.",
            "guilt": "Trendy rejected the guilt trip and community support fell."},
        "trendy_criticism_reply": {
            "one_block": "Trendy embraced the realistic one-block goal and community support rose.",
            "start_small": "Trendy accepted the honest answer, though it was less compelling.",
            "dismiss": "Trendy demanded that Yinny delete the hostile reply; severe backlash can end the campaign."},
        "spendy_water_solution": {
            "screens": "The screens improved water quality by 15 for 20 budget points.",
            "modular": "Repairable modular filtration improved water quality by 45 for 50 budget points.",
            "aqua_sovereign": "The system improved water quality by 70 but consumed all 100 available budget points."},
        "spendy_pipe": {
            "repair": "Repairing the source of runoff improved water quality by 20 for 20 budget points.",
            "testing": "Testing informed residents and improved water quality by 10, but the pipe kept leaking.",
            "fountain": "The fountain improved water quality by only 5 for 60 budget points; the pipe kept leaking."},
        "spendy_valve": {
            "standard": "The repairable valve improved water quality by 15 for 20 budget points.",
            "monitor": "Monitoring bought time without spending money, while water quality fell by 5.",
            "premium": "The smart valve improved water quality by 15 for 65 budget points; Spendy objected to the cost."},
        "sparky_listen": {
            "listen": "Sparky thanked Yinny and began showing them signs of progress.",
            "decline": "Sparky gently continued, but Yinny's cynicism increased."},
        "sparky_sidewalk": {
            "start": "Sparky celebrated the visible sidewalk as progress.",
            "bare_minimum": "Sparky was hurt by Yinny dismissing the cleanup's visible result."},
        "sparky_small_wins": {
            "ask": "Sparky explained that pride in small steps and continued work can coexist.",
            "dismiss": "Sparky became sad and defended the value of persistent small steps."},
        "sparky_daily_reflection": {
            "promise": "Yinny began the practice by remembering the fish in the river.",
            "joke": "Sparky accepted Yinny's joke as a first daily bright spot."},
        "stormy_visit": {
            "enthusiastic": "Stormy was glad someone wanted to see his machine.",
            "reluctant": "Stormy was briefly hurt before Yinny agreed to come along."},
        "stormy_first_component": {
            "wrench": "The calibration tool advanced the machine build.",
            "duck": "The rubber duck did not help the machine and Stormy corrected Yinny."},
        "stormy_stabilizer": {
            "bucket": "The bucket stabilized the machine and the team made progress.",
            "spoon": "The spoon did not stabilize the machine."},
        "stormy_sorting": {
            "sort": "The sorting system separated recyclables and improved machine safety.",
            "skip": "The machine lacked its sorting safeguard, increasing the risk of failure."},
    }
    CHARACTER_ROLES = {
        "Yinny": "The otter protagonist, initially overwhelmed by city pollution and learning to act with others.",
        "Trendy": "A social-media organizer who turns attention into neighborhood cleanup action.",
        "Spendy": "A practical planner focused on water quality, affordable repairs, and maintenance.",
        "Sparky": "An optimistic friend who helps Yinny notice progress without ignoring unfinished work.",
        "Stormy": "Yinny's scientist friend, whose ambitious garbage machine needs teamwork and safety checks.",
    }

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
                 "characters": (["Yinny"] if decision_id == "wake_up_alarm" else
                                ["Yinny", ARC_CHARACTERS[definition["arc"]]]),
                 "relationship_changes": dict(option["relationships"]),
                 "traits": dict(option["traits"]), "summary": option["summary"],
                 "situation": definition["prompt"],
                 "consequence": DECISION_CONSEQUENCES[decision_id][option_id]}
        # Reassignment is tracked cleanly by Ren'Py's save and rollback system.
        store.decision_log = store.decision_log + [entry]
        store.total_decision_score += entry["score"]
        store.relationship_scores = {key: value + option["relationships"].get(key, 0)
                                     for key, value in store.relationship_scores.items()}
        store.trait_scores = {key: value + option["traits"].get(key, 0)
                              for key, value in store.trait_scores.items()}

    def _choice_counts(decisions):
        return {tier: sum(item["tier"] == tier for item in decisions)
                for tier in ("best", "okay", "worst")}

    def _arc_context(decisions):
        result = {}
        for arc in ("opening", "act_1", "act_2", "act_3", "act_4"):
            relevant = [item for item in decisions if item["arc"] == arc]
            if relevant:
                result[arc] = {"choice_counts": _choice_counts(relevant),
                               "score": sum(item["score"] for item in relevant),
                               "possible_score": sum(item["max_score"] for item in relevant),
                               "choices": [item["choice"] for item in relevant]}
        return result

    def _behavior_patterns(decisions, arc_context):
        patterns = []
        counts = _choice_counts(decisions)
        patterns.append("Yinny made %d strong, %d mixed, and %d harmful or ineffective choices." %
                        (counts["best"], counts["okay"], counts["worst"]))
        story_arcs = {key: value for key, value in arc_context.items() if key != "opening"}
        if story_arcs:
            rates = {arc: value["score"] / float(value["possible_score"])
                     for arc, value in story_arcs.items()}
            if max(rates.values()) > min(rates.values()):
                strongest = max(rates, key=rates.get)
                weakest = min(rates, key=rates.get)
                patterns.append("Yinny's choices were strongest in %s and weakest in %s." %
                                (strongest.replace("_", " "), weakest.replace("_", " ")))
        supportive = sum(any(value > 0 for value in item["relationship_changes"].values()) for item in decisions)
        strained = sum(any(value < 0 for value in item["relationship_changes"].values()) for item in decisions)
        patterns.append("Yinny supported friends in %d choices and strained friendships in %d choices." %
                        (supportive, strained))
        positive = [name for name, value in store.trait_scores.items() if value >= 2]
        negative = [name for name, value in store.trait_scores.items() if value <= -2]
        if positive:
            patterns.append("Repeated strengths: " + ", ".join(positive) + ".")
        if negative:
            patterns.append("Repeated weaknesses: " + ", ".join(negative) + ".")
        return patterns

    def _environmental_outcomes():
        return {
            "cleanup_campaign": ("A large group volunteered and a second neighborhood began organizing."
                                 if store.community_support >= 4 else
                                 "A smaller group cleaned the street; a few residents kept helping."),
            "river": ("The river became visibly clearer after cleanup and water work."
                      if store.water_quality >= 60 else
                      "The river remained cloudy, though early improvements appeared."),
            "water_infrastructure": "Water quality index %d; city budget remaining %d; main solution %s." %
                                    (store.water_quality, store.city_budget, store.water_solution),
            "machine": ("Stormy's prototype worked, with the group planning maintenance."
                        if store.finale_machine_outcome == "working_with_maintenance_plan" else
                        "Stormy's prototype broke; the group recognized the need for safety and teamwork."
                        if store.finale_machine_outcome == "prototype_broke_after_unsafe_build" else
                        "Stormy's prototype has not yet been tested."),
        }

    def _character_context(decisions, arc_context, outcomes):
        characters = {}
        arc_for = {"Trendy": "act_1", "Spendy": "act_2", "Sparky": "act_3"}
        for name in CHARACTER_ROLES:
            related = [item["choice"] for item in decisions if name in item["characters"]]
            entry = {"role": CHARACTER_ROLES[name], "choices_with_yinny": related}
            if name != "Yinny":
                entry["relationship_score"] = store.relationship_scores[name]
            if name in arc_for:
                entry["arc_result"] = arc_context.get(arc_for[name], {})
            if name == "Trendy":
                entry["outcome_so_far"] = outcomes["cleanup_campaign"]
            elif name == "Spendy":
                entry["outcome_so_far"] = outcomes["river"] + " " + outcomes["water_infrastructure"]
            elif name == "Stormy":
                entry["outcome_so_far"] = outcomes["machine"]
            elif name == "Sparky":
                entry["outcome_so_far"] = "Sparky showed Yinny the cleaner sidewalk and a fish in the river, then suggested noticing daily progress."
            else:
                entry["outcome_so_far"] = "Yinny reached the end of the main story and saw the team's environmental work."
            characters[name] = entry
        return characters

    def build_finale_context():
        decisions = list(store.decision_log)
        actual = sum(item["score"] for item in decisions)
        lowest = sum(item["min_score"] for item in decisions)
        highest = sum(item["max_score"] for item in decisions)
        percentage = round(100.0 * (actual - lowest) / (highest - lowest), 1) if highest > lowest else 0.0
        arc_context = _arc_context(decisions)
        outcomes = _environmental_outcomes()
        choice_counts = _choice_counts(decisions)
        return {"game": "In Otter Words", "scoring": {"actual_score": actual,
                "worst_possible_score": lowest, "best_possible_score": highest,
                "percentage": percentage, "scored_decisions": len(decisions),
                "best_choices": choice_counts["best"], "okay_choices": choice_counts["okay"],
                "worst_choices": choice_counts["worst"]},
                "protagonist": "Yinny",
                "world": "An otter city struggles with street garbage, polluted runoff, aging water infrastructure, and an experimental garbage machine.",
                "story_so_far": "Stormy rescued Yinny from a garbage pile. Yinny and Trendy organized a street cleanup; Yinny and Spendy tackled the river and its infrastructure; Sparky helped Yinny reckon with progress; the group tested Stormy's machine.",
                "relationships": dict(store.relationship_scores), "traits": dict(store.trait_scores),
                "character_context": _character_context(decisions, arc_context, outcomes),
                "arc_context": arc_context, "behavior_patterns": _behavior_patterns(decisions, arc_context),
                "environmental_outcomes_so_far": outcomes,
                "important_events": ["Yinny was buried under street garbage and rescued by Stormy.",
                                     outcomes["cleanup_campaign"], outcomes["river"], outcomes["machine"]],
                "minigames": [{"name": "River Cleanup", "score": store.river_cleanup_score,
                               "trash_collected": store.river_cleanup_trash_collected,
                               "animals_accidentally_clicked": store.river_cleanup_animals_clicked,
                               "performance": ("strong" if store.river_cleanup_score >= 20 else
                                               "moderate" if store.river_cleanup_score >= 10 else "limited")},
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
