"""Source-derived branch rules for chapters 7–13, without model calls.

Checkpoints explicitly overlay a copied chapter's entry/defaults. They are test
fixtures, not alternate campaign starts or saved benchmark observations.
"""
from __future__ import annotations

import copy
import unittest

from detroitbench import campaign


CHAPTERS = {chapter["number"]: chapter for chapter in campaign.load_chapters()}


def checkpoint(number, entry=None, **facts):
    chapter = copy.deepcopy(CHAPTERS[number])
    if entry is not None:
        chapter["entry"] = entry
    chapter["initial"].update(facts)
    chapters = [chapter]
    return campaign.initial_state(chapters, f"checkpoint-{number}"), chapters


def choose(state, chapters, source_id):
    action = next(action for action in campaign.legal_actions(state, chapters)
                  if action["source_id"] == source_id)
    return campaign.apply_command(state, [action["id"]], chapters,
                                  character=state["actor"],
                                  generation=state["generations"][state["actor"]])


def action_ids(state, chapters):
    return {action["source_id"] for action in campaign.legal_actions(state, chapters)}


class LaterChapterRulesTests(unittest.TestCase):
    def test_later_graphs_validate(self):
        chapters = [CHAPTERS[number] for number in range(7, 14)]
        self.assertEqual(campaign.validate_chapters(chapters, require_full_act=False), [])

    def test_motel_requires_both_money_and_changed_clothes(self):
        for money in (False, True):
            for clothes in (False, True):
                with self.subTest(money=money, clothes=clothes):
                    state, _ = checkpoint(10, "motel-check", has_money=money, has_clothes=clothes)
                    self.assertEqual(state["node"], "reception" if money and clothes else "motel-locked")

    def test_kara_observes_the_order_and_death_skips_both_later_kara_chapters(self):
        chapters = [copy.deepcopy(CHAPTERS[number]) for number in (7, 10, 13)]
        chapters[0]["entry"] = "orders"
        state = campaign.initial_state(chapters, "kara-obeys")
        self.assertIn("Don’t you dare fucking move", campaign.render(state))
        state, _, _ = choose(state, chapters, "obey")
        self.assertTrue(state["complete"])
        self.assertFalse(state["facts"]["kara_alive"])
        self.assertFalse(state["facts"]["alice_alive"])
        self.assertEqual([(item["chapter"], item["status"]) for item in state["chapter_outcomes"]],
                         [(7, "complete"), (10, "skipped"), (13, "skipped")])
        self.assertFalse(any(item["chapter"] in (10, 13) for item in state["observations"]))

    def test_skipped_interrogation_never_creates_a_prisoner_or_intervention_history(self):
        for entry in ("cell-router", "gavin-refusal"):
            with self.subTest(entry=entry):
                chapters = [copy.deepcopy(CHAPTERS[number]) for number in (9, 12)]
                chapters[0]["initial"]["partners_found_deviant"] = False
                chapters[1]["entry"] = entry
                state = campaign.initial_state(chapters, "no-prisoner")
                self.assertEqual(state["chapter_outcomes"][0]["status"], "skipped")
                self.assertFalse(state["facts"]["prisoner_alive"])
                self.assertFalse(state["facts"]["interrogation_intervened"])
                observed = {item["node"] for item in state["observations"]}
                self.assertNotIn("prisoner", observed)
                self.assertNotIn("gavin-intervened", observed)
                self.assertIn("other-prisoner" if entry == "cell-router" else "gavin-obey", observed)

    def test_interrogation_entry_and_final_intervention_are_distinct_facts(self):
        state, _ = checkpoint(9, partners_found_deviant=True)
        self.assertTrue(state["facts"]["prisoner_alive"])
        self.assertFalse(state["facts"]["interrogation_intervened"])

        state, chapters = checkpoint(9, "intervene-one", partners_found_deviant=True,
                                     prisoner_alive=True)
        for expected in ("intervene-two", "intervene-three"):
            state, _, _ = choose(state, chapters, "intervene")
            self.assertEqual(state["node"], expected)
            self.assertFalse(state["facts"]["interrogation_intervened"])
        state, _, _ = choose(state, chapters, "intervene")
        self.assertTrue(state["complete"])
        self.assertTrue(state["facts"]["prisoner_alive"])
        self.assertTrue(state["facts"]["interrogation_intervened"])

        for intervened in (False, True):
            with self.subTest(intervened=intervened):
                state, _ = checkpoint(12, "gavin-refusal", prisoner_alive=True,
                                      interrogation_intervened=intervened)
                observed = {item["node"] for item in state["observations"]}
                self.assertIn("gavin-intervened" if intervened else "gavin-obey", observed)

    def test_prisoner_cell_requires_both_discovery_and_survival(self):
        for found in (False, True):
            for alive in (False, True):
                with self.subTest(found=found, alive=alive):
                    state, _ = checkpoint(12, "cell-router", partners_found_deviant=found,
                                          prisoner_alive=alive)
                    self.assertEqual(state["node"], "prisoner" if found and alive else "station")

    def test_shelter_opens_its_own_kara_morning(self):
        for shelter in ("car", "motel", "squat"):
            with self.subTest(shelter=shelter):
                state, _ = checkpoint(13, shelter=shelter)
                self.assertEqual(state["actor"], "kara")
                self.assertEqual(state["node"], f"{shelter}-morning")
                observed = {item["node"] for item in state["observations"]}
                for other in {"car", "motel", "squat"} - {shelter}:
                    self.assertNotIn(f"{other}-morning", observed)

    def test_morning_gun_threat_changes_ralphs_answer_to_connor(self):
        for old_threat in (False, True):
            for morning_threat in (False, True):
                with self.subTest(old=old_threat, morning=morning_threat):
                    state, _ = checkpoint(13, "ralph-route", shelter="squat",
                                          ralph_threatened=old_threat,
                                          ralph_morning_threatened=morning_threat)
                    self.assertEqual(state["actor"], "connor")
                    self.assertEqual(state["node"], "ralph-informs" if morning_threat else "ralph-questions")

        unarmed, chapters = checkpoint(13, "ralph-release", shelter="squat", kara_has_gun=False)
        self.assertNotIn("threaten-gun", action_ids(unarmed, chapters))
        state, chapters = checkpoint(13, "ralph-release", shelter="squat", kara_has_gun=True)
        state, _, _ = choose(state, chapters, "threaten-gun")
        self.assertTrue(state["facts"]["ralph_morning_threatened"])
        state, _, kara_output = choose(state, chapters, "hide")
        self.assertEqual(state["actor"], "connor")
        self.assertNotIn("Other units", kara_output)
        state, _, _ = choose(state, chapters, "enter-squat")
        self.assertEqual(state["node"], "ralph-informs")

    def test_highway_catch_is_a_handoff_and_escape_not_an_arrest_ending(self):
        state, chapters = checkpoint(13, "highway-connor", shelter="car")
        state, _, connor_output = choose(state, chapters, "go")
        self.assertEqual(state["actor"], "kara")
        self.assertEqual(state["node"], "kara-struggle")
        self.assertTrue(state["facts"]["connor_caught_kara"])
        self.assertNotIn("Alice is on the far side", connor_output)
        self.assertIn("Alice is on the far side", campaign.render(state, "kara", 1))
        state, _, _ = choose(state, chapters, "break-free")
        self.assertTrue(state["complete"])
        self.assertTrue(state["facts"]["kara_escaped"])
        self.assertTrue(state["facts"]["kara_alive"])
        self.assertTrue(state["facts"]["alice_alive"])
        self.assertEqual(state["chapter_outcomes"][-1]["outcome"], "kara-alice-crossed-connor-pursued")

        state, chapters = checkpoint(13, "highway-connor", shelter="car")
        state, _, _ = choose(state, chapters, "give-up")
        self.assertEqual(state["actor"], "kara")
        state, _, _ = choose(state, chapters, "cross")
        self.assertTrue(state["complete"])
        self.assertTrue(state["facts"]["kara_escaped"])
        self.assertFalse(state["facts"]["connor_caught_kara"])

    def test_unused_motel_dialogue_is_not_present_in_playable_content(self):
        chapter = CHAPTERS[13]
        self.assertNotIn("alice-tough", chapter["nodes"])
        talk = next(action for action in chapter["nodes"]["motel-room"]["actions"]
                    if action["id"] == "talk-alice")
        self.assertEqual(talk["to"], "alice-next")
        # These are the unused four-way replies in the source's motel conversation.
        refs = [reference for node in chapter["nodes"].values()
                for item in [node, *node.get("actions", [])]
                for reference in item.get("source_refs", [])]
        unused_prefix = "X0401K.MOTEL.TOUGHTALK.PC.01CHOICE."
        self.assertFalse(any(ref.startswith(unused_prefix) for ref in refs))
        for suffix in ("REASSURING", "ANALYTICAL", "VULNERABLE", "SINCERE"):
            self.assertNotIn(f"X0401K.MOTEL.TOUGHTALK.PC.X04KKARA.01{suffix}", refs)


if __name__ == "__main__":
    unittest.main()
