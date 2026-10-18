import unittest
import importlib.util
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = ROOT / "ontology" / "manifest.yaml"
VALIDATOR_PATH = ROOT / "ontology" / "tools" / "validate_package.py"
CLEAN_COUNCIL_VALIDATOR_PATH = ROOT / "ontology" / "tools" / "validate_clean_councils.py"


def load_validator():
    spec = importlib.util.spec_from_file_location("validate_ontology_package", VALIDATOR_PATH)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


class DesignOntologyPackageTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.manifest = yaml.safe_load(MANIFEST_PATH.read_text())
        cls.quickstart = (ROOT / "ontology" / "v0.1" / "QUICKSTART.md").read_text()
        machine_path = ROOT / cls.manifest["current_sources"]["machine_vocabulary"]["path"]
        cls.ontology = yaml.safe_load(machine_path.read_text())

    def test_manifest_declares_provisional_alpha(self):
        package = self.manifest["package"]
        self.assertEqual(package["version"], "0.1.0-alpha.2")
        self.assertEqual(package["status"], "provisional")
        self.assertEqual(package["owner"], "Wendell Britt")
        self.assertEqual(package["session_discipline"]["unit"], "one_bounded_task_or_goal")
        self.assertEqual(package["session_discipline"]["scope_change"], "start_new_session")
        self.assertEqual(package["session_discipline"]["compaction_policy"], "do_not_design_for_compaction")

    def test_skill_and_face_contract_enforce_bounded_sessions(self):
        skill = (ROOT / ".claude" / "skills" / "design-ontology" / "SKILL.md").read_text()
        contract = (ROOT / self.manifest["council_agents"]["contract"]).read_text()
        for text in (skill, contract):
            self.assertIn("one bounded task or goal", text)
            self.assertIn("fresh session", text)
            self.assertIn("context compaction", text)

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
        paths.add(self.manifest["validation"]["adversarial_fixtures"])
        paths.add(self.manifest["validation"]["clean_council_evidence"])
        paths.add(self.manifest["council_agents"]["contract"])
        paths.update(self.manifest["council_agents"]["faces"].values())

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
            "Intimate disclosure is not progression currency",
            "Every BAR has provenance; not every provenance-bearing object is a BAR",
            "it does not owe the garden a harvest",
            "it may not name the player's experience for them",
            "Consent is situated authorization for an operation now",
            "PermissionEnvelope",
            "Deletion disposes of named content and descendants",
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
            "long answers prove depth",
            "every artifact is automatically a BAR",
            "composting requires a new artifact",
            "a derived voice is the source person",
        ]
        lowered = self.quickstart.lower()
        for phrase in forbidden:
            with self.subTest(phrase=phrase):
                self.assertNotIn(phrase.lower(), lowered)

    def test_six_faces_skill_routes_game_design_to_ontology(self):
        skill = (ROOT / ".claude" / "skills" / "six-faces" / "SKILL.md").read_text()
        self.assertIn("design-ontology", skill)
        self.assertIn("ontology/manifest.yaml", skill)

    def test_privacy_permission_grammar_is_purpose_specific_and_propagating(self):
        privacy = self.ontology["privacy_consent_authority"]
        purposes = set(privacy["distinct_operations"])
        self.assertTrue(
            {
                "collection",
                "transient_processing",
                "persistence",
                "derivation",
                "personalization",
                "explanation",
                "visibility",
                "reuse",
                "sharing_publication",
                "export",
                "analytics_evaluation",
                "model_improvement",
                "retention",
                "correction",
                "deletion",
                "revocation",
            }.issubset(purposes)
        )
        self.assertEqual(
            privacy["derivative_rule"],
            "descendants_inherit_the_effective_permission_envelope",
        )
        self.assertEqual(privacy["data_class_defaults"]["model_improvement"], "explicit_opt_in_only")
        self.assertIn("composting", privacy["deletion_is_not"])

    def test_privacy_decision_resolves_consent_record_scope(self):
        path = ROOT / self.manifest["binding_decisions"]["privacy_consent_authority"]["path"]
        decision = path.read_text()
        self.assertIn("ConsentRecord is evidence of a past decision", decision)
        self.assertIn("Every derivative inherits a permission envelope", decision)
        self.assertIn("BARS reconciliation test", decision)

    def test_packaged_face_agents_and_adversarial_contract_validate(self):
        validator = load_validator()
        self.assertEqual(validator.validate_package(), [])

    def test_clean_council_release_evidence_validates(self):
        spec = importlib.util.spec_from_file_location(
            "validate_clean_councils", CLEAN_COUNCIL_VALIDATOR_PATH
        )
        module = importlib.util.module_from_spec(spec)
        assert spec.loader is not None
        spec.loader.exec_module(module)
        self.assertEqual(module.main(), 0)


if __name__ == "__main__":
    unittest.main()
