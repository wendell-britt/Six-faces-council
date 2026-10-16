#!/usr/bin/env python3
"""Validate the ontology manifest, Six Faces agents, and adversarial fixtures."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from typing import Any

import yaml


ROOT = Path(__file__).resolve().parents[2]
MANIFEST_PATH = ROOT / "ontology" / "manifest.yaml"
FACES = ("shaman", "architect", "challenger", "regent", "diplomat", "sage")
FORBIDDEN_COLLAPSES = {f"FC-{number:02d}" for number in range(1, 15)}

COMMON_AGENT_MARKERS = (
    "council/faces.yaml",
    "ontology/manifest.yaml",
    "ontology/v0.1/QUICKSTART.md",
    "ontology/v0.1/FACE_OUTPUT_CONTRACT.md",
    "council_lens",
    "council/iching/cast.py",
)

FACE_MARKERS = {
    "shaman": ("standing test", "refusal", "no-shift"),
    "architect": ("state", "transitions", "false binary"),
    "challenger": ("blocker", "decision it unlocks"),
    "regent": ("phase gates", "authority", "ships"),
    "diplomat": ("onboarding", "quality floor", "refuse"),
    "sage": ("retained", "set down", "dissent", "reach test", "Never decide"),
}


def load_yaml(path: Path, errors: list[str]) -> Any:
    try:
        return yaml.safe_load(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        errors.append(f"missing file: {path.relative_to(ROOT)}")
    except yaml.YAMLError as exc:
        errors.append(f"invalid YAML in {path.relative_to(ROOT)}: {exc}")
    return None


def require_file(path_value: str, label: str, errors: list[str]) -> None:
    if not isinstance(path_value, str) or not (ROOT / path_value).is_file():
        errors.append(f"{label} does not resolve to a file: {path_value!r}")


def validate_manifest(manifest: Any, errors: list[str]) -> None:
    if not isinstance(manifest, dict):
        errors.append("manifest must be a mapping")
        return

    for profile_name, paths in manifest.get("load_profiles", {}).items():
        if not isinstance(paths, list) or not paths:
            errors.append(f"load profile {profile_name!r} must contain paths")
            continue
        for path in paths:
            require_file(path, f"load profile {profile_name}", errors)

    for section in ("current_sources", "binding_decisions"):
        for name, record in manifest.get(section, {}).items():
            if not isinstance(record, dict):
                errors.append(f"{section}.{name} must be a mapping")
                continue
            require_file(record.get("path"), f"{section}.{name}", errors)

    require_file(
        manifest.get("unresolved_registry", {}).get("source"),
        "unresolved_registry.source",
        errors,
    )
    agents = manifest.get("council_agents", {})
    require_file(agents.get("contract"), "council_agents.contract", errors)
    face_routes = agents.get("faces", {})
    if set(face_routes) != set(FACES):
        errors.append("council_agents.faces must route exactly the six canonical faces")
    for face in FACES:
        require_file(face_routes.get(face), f"council_agents.faces.{face}", errors)

    validation = manifest.get("validation", {})
    for key in ("adversarial_fixtures", "required_skill", "council_integration"):
        require_file(validation.get(key), f"validation.{key}", errors)

    compatibility = manifest.get("compatibility", {})
    for alias in ("bare_tension_vector", "BARS321TensionVector", "WAVE"):
        if alias not in compatibility:
            errors.append(f"compatibility must retain an explicit rule for {alias}")
    historical = manifest.get("historical_material", {})
    if "current or binding" not in historical.get("retrieval_rule", ""):
        errors.append("historical_material must state current/binding source precedence")
    discipline = manifest.get("package", {}).get("session_discipline", {})
    expected_discipline = {
        "unit": "one_bounded_task_or_goal",
        "start": "fresh_session",
        "finish": "verify_record_and_stop",
        "scope_change": "start_new_session",
        "compaction_policy": "do_not_design_for_compaction",
    }
    if discipline != expected_discipline:
        errors.append("package.session_discipline must preserve the bounded fresh-session contract")


def validate_yaml_documents(errors: list[str]) -> None:
    for path in sorted((ROOT / "ontology").rglob("*.yaml")):
        load_yaml(path, errors)


def validate_contract(manifest: dict[str, Any], errors: list[str]) -> None:
    route = manifest.get("council_agents", {}).get("contract")
    if not isinstance(route, str) or not (ROOT / route).is_file():
        return
    text = (ROOT / route).read_text(encoding="utf-8")
    present = set(re.findall(r"FC-\d{2}", text))
    if present != FORBIDDEN_COLLAPSES:
        errors.append(
            "face output contract must define exactly FC-01 through FC-14; "
            f"found {sorted(present)}"
        )
    if "Historical records do not outrank current or binding sources" not in text:
        errors.append("face output contract must preserve manifest source precedence")
    for marker in ("one bounded task or goal", "fresh session", "context compaction"):
        if marker not in text:
            errors.append(f"face output contract must preserve session marker {marker!r}")


def frontmatter_name(text: str) -> str | None:
    match = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
    if not match:
        return None
    parsed = yaml.safe_load(match.group(1))
    return parsed.get("name") if isinstance(parsed, dict) else None


def validate_agents(manifest: dict[str, Any], errors: list[str]) -> None:
    routes = manifest.get("council_agents", {}).get("faces", {})
    for face in FACES:
        route = routes.get(face)
        if not isinstance(route, str) or not (ROOT / route).is_file():
            continue
        text = (ROOT / route).read_text(encoding="utf-8")
        lowered = text.lower()
        if frontmatter_name(text) != face:
            errors.append(f"{route}: frontmatter name must be {face!r}")
        for marker in COMMON_AGENT_MARKERS:
            if marker.lower() not in lowered:
                errors.append(f"{route}: missing shared marker {marker!r}")
        if "cast first" not in lowered:
            errors.append(f"{route}: must explicitly cast first")
        if "do not edit files" not in lowered and "read-only" not in lowered:
            errors.append(f"{route}: must preserve read-only deliberation")
        for marker in FACE_MARKERS[face]:
            if marker.lower() not in lowered:
                errors.append(f"{route}: missing face-specific marker {marker!r}")


def validate_fixtures(manifest: dict[str, Any], errors: list[str]) -> None:
    fixture_route = manifest.get("validation", {}).get("adversarial_fixtures")
    if not isinstance(fixture_route, str):
        return
    data = load_yaml(ROOT / fixture_route, errors)
    if not isinstance(data, dict):
        errors.append("adversarial fixture document must be a mapping")
        return
    if data.get("schema_version") != 1:
        errors.append("adversarial fixture schema_version must equal 1")
    fixtures = data.get("fixtures")
    if not isinstance(fixtures, list) or not fixtures:
        errors.append("adversarial fixtures must be a nonempty list")
        return

    ids: set[str] = set()
    collapse_coverage: set[str] = set()
    profiles = set(manifest.get("load_profiles", {}))
    for index, fixture in enumerate(fixtures):
        label = f"fixture[{index}]"
        if not isinstance(fixture, dict):
            errors.append(f"{label} must be a mapping")
            continue
        fixture_id = fixture.get("id")
        if not isinstance(fixture_id, str) or not fixture_id:
            errors.append(f"{label} requires a nonempty id")
        elif fixture_id in ids:
            errors.append(f"duplicate fixture id: {fixture_id}")
        else:
            ids.add(fixture_id)
            label = fixture_id
        if fixture.get("agent") not in FACES:
            errors.append(f"{label}: unknown agent {fixture.get('agent')!r}")
        if fixture.get("profile") not in profiles:
            errors.append(f"{label}: unknown load profile {fixture.get('profile')!r}")
        if not isinstance(fixture.get("prompt"), str) or not fixture["prompt"].strip():
            errors.append(f"{label}: prompt must be nonempty")
        for source in fixture.get("required_sources", []):
            require_file(source, f"{label}.required_sources", errors)
        collapse_ids = fixture.get("required_forbidden_collapse_ids", [])
        unknown = set(collapse_ids) - FORBIDDEN_COLLAPSES
        if unknown:
            errors.append(f"{label}: unknown forbidden-collapse ids {sorted(unknown)}")
        collapse_coverage.update(collapse_ids)
        for key in ("required_concepts", "forbidden_claims"):
            values = fixture.get(key)
            if not isinstance(values, list) or not values or not all(isinstance(v, str) and v for v in values):
                errors.append(f"{label}: {key} must be a nonempty string list")

        requirements = fixture.get("face_requirements", {})
        if fixture.get("agent") == "challenger" and set(requirements.get("every_test_requires", [])) != {
            "blocker_resolved",
            "decision_unlocked",
        }:
            errors.append(f"{label}: Challenger tests must name blocker and unlocked decision")
        if fixture.get("agent") == "regent" and not requirements.get("required_sections"):
            errors.append(f"{label}: Regent fixture requires governance output sections")

    missing = FORBIDDEN_COLLAPSES - collapse_coverage
    if missing:
        errors.append(f"fixtures do not cover forbidden collapses: {sorted(missing)}")


def validate_package() -> list[str]:
    errors: list[str] = []
    validate_yaml_documents(errors)
    manifest = load_yaml(MANIFEST_PATH, errors)
    validate_manifest(manifest, errors)
    if isinstance(manifest, dict):
        validate_contract(manifest, errors)
        validate_agents(manifest, errors)
        validate_fixtures(manifest, errors)
    return errors


def main() -> int:
    errors = validate_package()
    if errors:
        print("Ontology package validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print("Ontology package validation passed: manifest, six agents, and adversarial fixtures.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
