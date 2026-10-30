"""Behavioral contracts for the source-grounded opening chapters.

These exercise information boundaries and consequences across real chapter data,
rather than snapshotting prose or mirroring every JSON transition.
"""
from __future__ import annotations

import unittest

from detroitbench import campaign


def chapters(*numbers):
    wanted = set(numbers)
    result = [chapter for chapter in campaign.load_chapters() if chapter["number"] in wanted]
    if {chapter["number"] for chapter in result} != wanted:
        raise AssertionError(f"Missing chapter fixtures: {wanted}")
    return result


def choose(state, corpus, action_id):
    actions = {action["source_id"]: action for action in campaign.legal_actions(state, corpus)}
    if action_id not in actions:
        raise AssertionError(f"{action_id} unavailable at {state['node']}: {list(actions)}")
    return campaign.apply_command(state, [actions[action_id]["id"]], corpus)[0]


def play(state, corpus, *actions):
    for action in actions:
        state = choose(state, corpus, action)
    return state


def visible(state):
    return "\n".join(item["text"] for item in state["observations"])


class EarlyChapterContracts(unittest.TestCase):
    def test_opening_is_observed_without_a_fabricated_choice(self):
        corpus = chapters(2, 3)
        state = campaign.initial_state(corpus, "opening")
        self.assertEqual(state["decision_count"], 0)
        self.assertEqual(state["chapter"], 3)
        self.assertEqual(state["actor"], "markus")
        self.assertEqual(state["chapter_outcomes"][0]["outcome"], "kara_named")
        kara_text = "\n".join(item["text"] for item in state["observations"] if item["actor"] == "kara")
        self.assertIn("My name is Kara.", kara_text)
        self.assertNotIn("My name is Kara.", campaign.render(state, "markus", 1))
        self.assertFalse(any(node.get("actions") for node in corpus[0]["nodes"].values()))

    def test_optional_observations_remain_available_in_either_order(self):
        corpus = chapters(3)
        first = campaign.initial_state(corpus, "first")
        first = play(first, corpus, "look-around", "bench")
        ids = {action["source_id"] for action in campaign.legal_actions(first, corpus)}
        self.assertIn("workers", ids)
        self.assertIn("go-to-paints", ids)
        self.assertNotIn("bench", ids)  # No repeated-observation score farming.
        first = choose(first, corpus, "workers")
        second = campaign.initial_state(corpus, "second")
        second = play(second, corpus, "look-around", "workers", "bench")
        for key in ("c3_bench_seen", "c3_workers_seen"):
            self.assertTrue(first["facts"][key])
            self.assertEqual(first["facts"][key], second["facts"][key])

    def test_gun_discovery_transfers_knowledge_without_giving_kara_a_gun(self):
        corpus = chapters(4)
        state = campaign.initial_state(corpus, "home")
        self.assertNotIn("handgun", visible(state))
        state = play(state, corpus, "look-around", "kitchen", "wash-dishes", "take-beer",
                     "garden", "collect-laundry", "take-detergent", "ignore", "collect-trash",
                     "report-todd", "todd-room", "tidy-pills", "ignore")
        self.assertTrue(state["facts"]["kara_knows_gun"])
        self.assertFalse(state["facts"].get("kara_has_gun", False))
        self.assertIn("handgun", visible(state))
        self.assertFalse(state["facts"]["kara_knows_window"])
        self.assertNotIn("Alice’s drawings", visible(state))

    def test_painter_chess_lie_is_branch_local_and_explicit(self):
        corpus = chapters(5)
        state = campaign.initial_state(corpus, "painter")
        state = play(state, corpus, "drop-package", "wake-carl", "serve-breakfast", "chess", "lose")
        self.assertNotIn("You just played better!", visible(state))
        state = choose(state, corpus, "lie")
        self.assertIn("You just played better!", visible(state))
        self.assertEqual(state["facts"]["c5_chess_result"], "lose")
        self.assertEqual(state["facts"]["c5_chess_answer"], "lie")
        self.assertNotIn("What happened to your clothes?", visible(state))
        self.assertNotIn("forgotten where the living room is", visible(state))

    def _partners_investigation(self, corpus):
        state = campaign.initial_state(corpus, "partners")
        return play(state, corpus, "look-around", "scan-hank", "talk-hank", "reason",
                    "diplomacy", "patient", "follow-hank")

    def test_reconstruction_requires_discovered_evidence(self):
        corpus = chapters(6)
        state = self._partners_investigation(corpus)
        self.assertNotIn("report-hank", {a["source_id"] for a in campaign.legal_actions(state, corpus)})
        state = play(state, corpus, "living-room", "body", "information", "knife", "reconstruct-body",
                     "return", "kitchen", "chair", "bat", "missing-knife", "reconstruct-assault", "return")
        self.assertIn("report-hank", {a["source_id"] for a in campaign.legal_actions(state, corpus)})
        state = play(state, corpus, "report-hank", "kitchen", "beat", "knife", "livingroom", "kill",
                     "follow-blue-blood", "take-chair", "search")
        self.assertTrue(state["complete"])
        self.assertTrue(state["facts"]["partners_found_deviant"])
        self.assertFalse(state["facts"]["partners_found_ra9"])
        self.assertFalse(state["facts"]["partners_found_statuette"])

    def test_failed_investigation_skips_interrogation(self):
        corpus = chapters(6, 9)
        state = self._partners_investigation(corpus)
        state = play(state, corpus, "wait", "leave")
        self.assertTrue(state["complete"])
        self.assertFalse(state["facts"]["partners_found_deviant"])
        self.assertEqual(state["chapter_outcomes"][-1]["chapter"], 9)
        self.assertEqual(state["chapter_outcomes"][-1]["status"], "skipped")


if __name__ == "__main__":
    unittest.main()
