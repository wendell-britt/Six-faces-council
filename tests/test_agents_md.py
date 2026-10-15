"""AGENTS.md carries CLAUDE.md's rules for any agent. The board sections are word for word the same, and every
CLAUDE.md section has an AGENTS.md section of the same name, so an agent given only AGENTS.md follows the same
rules (board-off-vendor-quota, 2026-10-16)."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SAME = ("Questions go to the board, never to chat", "The Nonprofit Board's saves")


def sections(text):
    return {m.group(1): m.group(2).strip() for m in re.finditer(r"^## (.+?)\n(.*?)(?=^## |\Z)", text, re.S | re.M)}


CLAUDE, AGENTS = sections((ROOT / "CLAUDE.md").read_text()), sections((ROOT / "AGENTS.md").read_text())


def test_every_claude_section_is_in_agents():
    assert set(CLAUDE) <= set(AGENTS), set(CLAUDE) - set(AGENTS)


def test_board_rules_are_word_for_word():
    for name in SAME:
        assert CLAUDE[name] == AGENTS[name], name


def test_agents_md_names_no_claude_only_tool_as_required():
    body = "\n".join(AGENTS[n] for n in AGENTS if n not in SAME)
    for tool in ("ArtifactData", "start_thread_session", "fire_trigger", "send_message"):
        assert tool not in body, tool


def test_paths_it_names_exist():
    text = (ROOT / "AGENTS.md").read_text()
    for path in set(re.findall(r"`((?:board|council|schema|tests|docs|ontology|\.github|\.claude)/[^`<> ]+)`", text)):
        assert (ROOT / path).exists(), path
