"""council/spirit-care/sim.py: four players come back to mortal spirits (spirit care pass 1, the Challenger's test).

Rerun after any change to the ladder, the tracks or the return copy. His answered pair (A on sc-undying, A on
sc-after-death) must pass every check; under the other options only the stake check may miss.
"""
import importlib.util
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("spirit_care_sim", ROOT / "council" / "spirit-care" / "sim.py")
sim = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sim)


class SpiritCareSimTest(unittest.TestCase):
    def test_recommended_pair_passes_every_check(self):
        for name, ok in sim.checks(sim.run(*sim.RECOMMENDED), sim.RECOMMENDED[0]):
            self.assertTrue(ok, name)

    def test_every_option_pair_passes_all_but_the_stake(self):
        for u in sim.UNDYING:
            for d in sim.AFTER_DEATH:
                for name, ok in sim.checks(sim.run(u, d), u):
                    if name not in sim.STAKE_CHECKS:
                        self.assertTrue(ok, f"{u}{d}: {name}")

    def test_vanished_player_welcomed_first(self):
        for r in sim.run("A", "A"):
            if r["who"] == "vanished":
                self.assertEqual(r["screen"][0][0], "welcome")

    def test_a_spirit_can_die(self):
        self.assertTrue(any(r["spirit"].stage == "gone" for r in sim.run("A", "A")))

    def test_undying_never_dies(self):
        for r in sim.run("C", "A"):
            if not r["spirit"].shared:
                self.assertNotEqual(r["spirit"].stage, "gone", r["spirit"].name)
        pip = next(r["spirit"] for r in sim.run("B", "A") if r["spirit"].name == "Pip")
        self.assertNotIn("gone", pip.history)

    def test_rest_pauses_everything(self):
        tide = next(r["spirit"] for r in sim.run("A", "A") if r["who"] == "rest")
        self.assertEqual(set(tide.history[7:17]), {tide.history[6]})

    def test_no_skip_catches_a_skip(self):
        self.assertFalse(sim.no_skip(["thriving", "stale"]))
        self.assertFalse(sim.no_skip(["thriving", "dimming", "stale"]))   # dimming not held for its dwell
        self.assertTrue(sim.no_skip(["thriving", "dimming", "dimming", "dimming", "stale"]))

    def test_shadow_line_names_the_source_not_the_player(self):
        lines = [t for r in sim.run("A", "A") for k, t in r["screen"] if k == "shadow"]
        self.assertTrue(lines)
        for t in lines:
            self.assertNotIn("you", t.lower().split(), t)

    def test_quest_offer_rules(self):
        self.assertTrue(sim.offer_rules_hold())

    def test_cli_exits_clean(self):
        self.assertEqual(sim.main([]), 0)
        self.assertEqual(sim.main(["--all"]), 0)


if __name__ == "__main__":
    unittest.main()
