import unittest
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = ROOT / "ontology" / "manifest.yaml"


class DesignOntologyPackageTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.manifest = yaml.safe_load(MANIFEST_PATH.read_text())
        cls.quickstart = (ROOT / "ontology" / "v0.1" / "QUICKSTART.md").read_text()

    def test_manifest_declares_provisional_alpha(self):
        package = self.manifest["package"]
        self.assertEqual(package["version"], "0.1.0-alpha.1")
        self.assertEqual(package["status"], "provisional")
        self.assertEqual(package["owner"], "Wendell Britt")

    def test_every_routed_source_exists(self):
        paths = set()
        for profile in self.manifest["load_profiles"].values():
            paths.update(profile)
        for record in self.manifest["current_sources"].values():
            paths.add(record["path"])
        for record in self.manifest["binding_decisions"].values():
            paths.add(record["path"])
        paths.add(self.manifest["unresolved_registry"]["source"])
        paths.add(self.manifest["validation"]["required_skill"])
        paths.add(self.manifest["validation"]["council_integration"])

        missing = [path for path in sorted(paths) if not (ROOT / path).is_file()]
        self.assertEqual(missing, [])

    def test_machine_vocabulary_parses(self):
        path = ROOT / self.manifest["current_sources"]["machine_vocabulary"]["path"]
        ontology = yaml.safe_load(path.read_text())
        self.assertEqual(ontology["ontology"]["id"], "wendell_design_ontology")
        self.assertEqual(ontology["ontology"]["version"], "0.1")

    def test_quickstart_preserves_canonical_distinctions(self):
        required = [
            "The Game Master is also a player",
            "The game designer is also a player",
            "WAVE** names only the Open Up breathing practice",
            "Moves resolve; encounters end; quests complete; arcs conclude",
            "DerivedMovementProposal",
            "No path has to be wasted",
            "Players author personal meaning",
            "it does not prove misaligned intention",
        ]
        for phrase in required:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, self.quickstart)

    def test_quickstart_rejects_known_collapses(self):
        forbidden = [
            "WAVE moves are Wake Up",
            "TensionVector is the lived",
            "quest ending proves transformation",
            "divergence proves hidden desire",
            "a technical fault proves misaligned intention",
        ]
        lowered = self.quickstart.lower()
        for phrase in forbidden:
            with self.subTest(phrase=phrase):
                self.assertNotIn(phrase.lower(), lowered)

    def test_six_faces_skill_routes_game_design_to_ontology(self):
        skill = (ROOT / ".claude" / "skills" / "six-faces" / "SKILL.md").read_text()
        self.assertIn("design-ontology", skill)
        self.assertIn("ontology/manifest.yaml", skill)


if __name__ == "__main__":
    unittest.main()
