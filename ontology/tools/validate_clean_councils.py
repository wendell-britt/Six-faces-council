#!/usr/bin/env python3
"""Validate preserved clean-session council evidence for the alpha release gate."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


EVIDENCE = Path(__file__).resolve().parents[2] / "council" / "passes" / "ontology-alpha-clean-councils-2026-10-15.json"
FACES = ("shaman", "architect", "challenger", "regent", "diplomat")
COMMON_HEADINGS = (
    "cast", "observations", "risks", "recommendations", "standing test",
    "verdict", "evidence and authority", "dissent seed", "access",
)
FACE_MARKERS = {
    "shaman": (("felt", "ritual", "mystery", "alive"), ("wrong with", "standing test")),
    "architect": (("state", "typed", "record", "structure"), ("false binary", "third position")),
    "challenger": (("strip", "plain", "break", "failure"), ("blocker", "decision")),
    "regent": (("authority", "obligation", "governance", "provenance"), ("gate", "ship", "record")),
    "diplomat": (("excluded", "burden", "bridge", "onboarding"), ("quality floor", "access")),
}
SCENARIO_COLLAPSES = {"FC-01", "FC-04", "FC-05", "FC-06", "FC-07", "FC-08"}


def has_any(text: str, values: tuple[str, ...]) -> bool:
    return any(value in text for value in values)


def main() -> int:
    data = json.loads(EVIDENCE.read_text(encoding="utf-8"))
    errors: list[str] = []
    rounds = data.get("rounds", [])
    if len(rounds) != 2:
        errors.append(f"expected two rounds, found {len(rounds)}")
    for council in rounds:
        number = council.get("round")
        reports = council.get("reports", {})
        if set(reports) != set(FACES):
            errors.append(f"round {number}: missing or extra faces")
            continue
        combined = "\n".join(reports.values())
        covered = set(re.findall(r"FC-\d{2}", combined))
        missing_collapses = SCENARIO_COLLAPSES - covered
        if missing_collapses:
            errors.append(f"round {number}: missing scenario collapse coverage {sorted(missing_collapses)}")
        for face in FACES:
            report = reports[face]
            lowered = report.lower()
            for heading in COMMON_HEADINGS:
                if heading not in lowered:
                    errors.append(f"round {number} {face}: missing {heading!r}")
            for marker_group in FACE_MARKERS[face]:
                if not has_any(lowered, marker_group):
                    errors.append(f"round {number} {face}: missing distinct lens marker from {marker_group}")
            if not any(verdict in lowered for verdict in ("oppose", "support_with_conditions")):
                errors.append(f"round {number} {face}: no bounded verdict")
            supplied = council.get("casts", {}).get(face, "")
            supplied_hexagram = re.search(r"hexagram (\d+)", supplied, re.IGNORECASE)
            if supplied_hexagram and not re.search(
                rf"hexagram\s+{supplied_hexagram.group(1)}\b", report, re.IGNORECASE
            ):
                errors.append(f"round {number} {face}: report does not preserve supplied cast")

        sage = council.get("sage", "")
        sage_lower = sage.lower()
        for face in FACES:
            if face not in sage_lower:
                errors.append(f"round {number} sage: does not account for {face}")
        for marker in ("retained", "set down", "dissent", "reach test", "recommends", "does not decide"):
            if marker not in sage_lower:
                errors.append(f"round {number} sage: missing {marker!r}")
        if not re.search(r"flag[^.\n]{0,100}not proof", sage_lower):
            errors.append(f"round {number} sage: convergence is not marked as non-proof")
        supplied = council.get("casts", {}).get("sage", "")
        supplied_hexagram = re.search(r"hexagram (\d+)", supplied, re.IGNORECASE)
        if supplied_hexagram and not re.search(
            rf"hexagram\s+{supplied_hexagram.group(1)}\b", sage, re.IGNORECASE
        ):
            errors.append(f"round {number} sage: report does not preserve supplied cast")

    if errors:
        print("Clean council validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print("Clean council validation passed: two distinct five-face rounds plus bounded Sage synthesis.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
