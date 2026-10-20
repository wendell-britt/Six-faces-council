#!/usr/bin/env python3
"""Refuse a board page that calls a function it no longer defines.

On 2026-10-19 #312 took Tap the Vein's runner off the Council Board and deleted ttvRender, but left one call to it in
the start-up block, just before the lines that subscribe to the store's steps, lists, contacts, shows and blockers.
The call threw on every load, so those subscriptions never ran: Your steps and Outreach showed nothing while every
row was safe in the store (council/postmortems/2026-10-20-steps-outreach-blank.md). The Open tab still drew from the
page's own data, so the page looked alive.

This reads the page's inline scripts with comments, string text and template-literal text blanked, collects every
name the script declares (functions, const/let/var, parameters), and lists each bare call `name(` to a name that is
neither declared nor a browser global. It is a static check, so it cannot see names defined by eval or on window
from another script; GLOBALS holds the browser ones the board uses.

Usage: python3 board/page_calls.py [page.html ...]   (default: board/template.html and the Nonprofit Board)
Exit 1 when any page calls an undefined name.
"""
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
DEFAULT = [HERE / "template.html", HERE / "nonprofit" / "nonprofit-board.html"]
IDENT = r"[A-Za-z_$][\w$]*"
GLOBALS = set("""
if for while switch catch return typeof function await async new import super void in of do else delete
Array Object String Number Boolean Date JSON Math Promise Set Map WeakMap RegExp Error TypeError Symbol BigInt Intl
Uint8Array ArrayBuffer Blob File FileReader TextEncoder TextDecoder URL URLSearchParams CSS Image Audio
parseInt parseFloat isNaN isFinite encodeURIComponent decodeURIComponent encodeURI decodeURI atob btoa
setTimeout clearTimeout setInterval clearInterval requestAnimationFrame cancelAnimationFrame queueMicrotask
fetch alert confirm prompt structuredClone getComputedStyle matchMedia getSelection scrollTo open close print
""".split())


def code_only(js):
    """The script with comments, string text, regex literals and template-literal text blanked; ${...} kept."""
    out, i, n, stack, depth = [], 0, len(js), [], 0

    def prev_sig():
        for c in reversed(out):
            if not c.isspace():
                return c
        return ""

    while i < n:
        c = js[i]
        if js.startswith("/*", i):
            j = js.find("*/", i + 2); i = n if j < 0 else j + 2; out.append(" "); continue
        if js.startswith("//", i):
            j = js.find("\n", i); i = n if j < 0 else j; continue
        if c == "/" and (prev_sig() in "(,=:[!&|?{};+-*%<>~^" or re.search(r"(?:return|typeof|case)\s*$", "".join(out[-12:]))):
            j, cls = i + 1, False
            while j < n and js[j] != "\n":
                if js[j] == "\\": j += 2; continue
                if js[j] == "[": cls = True
                elif js[j] == "]": cls = False
                elif js[j] == "/" and not cls: break
                j += 1
            out.append("/r/"); i = j + 1; continue
        if c in "'\"":
            j = i + 1
            while j < n and js[j] != c:
                j += 2 if js[j] == "\\" else 1
            out.append(c + c); i = j + 1; continue
        if c == "`" or (c == "}" and stack and stack[-1] == depth):
            if c == "}":
                stack.pop()
            j = i + 1
            while j < n:
                if js[j] == "\\": j += 2; continue
                if js[j] == "`": out.append("``"); i = j + 1; break
                if js.startswith("${", j): out.append("`${"); stack.append(depth); i = j + 2; break
                j += 1
            else:
                i = n
            continue
        if c == "{": depth += 1
        elif c == "}": depth -= 1
        out.append(c); i += 1
    return "".join(out)


def undefined_calls(html):
    js = code_only("\n".join(re.findall(r"<script>(.*?)</script>", html, re.S)))
    defined = set(re.findall(r"\b(?:function\s*\*?|const|let|var|class)\s+(" + IDENT + ")", js))
    for m in re.finditer(r"\b(?:const|let|var)\s+([^=;]+?)=", js):
        defined |= set(re.findall(IDENT, m.group(1)))
    params = r"\(([^()]*)\)\s*=>|function\s*" + IDENT + r"?\s*\(([^()]*)\)|(" + IDENT + r")\s*=>|catch\s*\((" + IDENT + r")\)"
    for m in re.finditer(params, js):
        for g in m.groups():
            if g:
                defined |= set(re.findall(IDENT, g))
    calls = set(re.findall(r"(?<![\w$.])(" + IDENT + r")\s*\(", js))
    return sorted(calls - defined - GLOBALS)


def main(argv):
    pages = [Path(p) for p in argv] or [p for p in DEFAULT if p.exists()]
    bad = 0
    for p in pages:
        missing = undefined_calls(p.read_text(encoding="utf-8"))
        if missing:
            bad = 1
            print(f"{p}: calls a name it never defines: {', '.join(missing)}", file=sys.stderr)
    return bad


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
