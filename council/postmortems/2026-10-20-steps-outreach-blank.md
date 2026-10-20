# Your steps and Outreach loaded blank, 19–20 October 2026

Wendell, 2026-10-20: "council board has lost the outreach notes, and the steps that I'm supposed to take- we need to
recover those and get a postmortem on why they were removed".

## What happened

Nothing was removed. The board's store still held every row when this was checked on 2026-10-20 at 00:35 UTC: 43 step
lists, 163 steps (his notes on them included, such as the Pragya, Nora, Mattias and Vince note on
podcast-outreach-chase-01), 115 contacts and 5 shows. The page stopped reading them.

#312 (merged 2026-10-19 23:50 UTC, commit 00aa2d1, "Tap the Vein is bars-engine's own page, framed in the Morning tab")
deleted the board's own Tap the Vein runner, `ttvRender` among it. One call to it stayed in the page's start-up block:

```js
db = window.claude && window.claude.use ? await window.claude.use('db') : null;
...
renderMorning(); ttvRender();          // ReferenceError: ttvRender is not defined
db.doc('morning/menu').onSnapshot(...)  // never reached, nor anything below
...
db.collection('lists').onSnapshot(...)
db.collection('contacts').onSnapshot(...)
db.collection('steps').onSnapshot(...)
```

The call threw on every load, after the store connected and before any subscription. Your steps (lists and steps),
Outreach (contacts and shows), blockers, picks, the pickup bar and the live answers on the Open tab never loaded.
The Open tab still drew its rows from the data baked into the page, so the page looked as if it worked. Both copies
were blank: the claude.ai board, republished from main by the board reads after #312, and bars-engine's
/board/council, which serves `board/council-board.html` straight from main.

#313, #314, #315, the compost pass and the menu-key-match rewrite (#305) were checked and are not the cause. The
compost pass writes `steps` docs, and they are all still in the store. #315 changed only the Morning merge in
`sync_board.py`.

## Why the checks missed it

- Every board check reads Python data or matches strings in the page: `build_board.py` checks question options,
  `sync_board.py` compares rows, bars-engine's `council-page.test.ts` checks which collections the page names. None of
  them runs the page's script, so a call to a deleted function passed all of them.
- The only place the error showed was the browser console. The page has no visible sign that a load failed, and an
  empty Your steps tab looks the same as a board with nothing waiting on him ("Nothing waiting on you").
- #312 was checked in the Morning tab, which it changed. The tabs it broke are drawn by the code after the throw.

## Recovery

- `board/template.html`: the stale `ttvRender();` call is gone and `council-board.html` is rebuilt. Loaded in Chromium
  against a copy of the live store, the old page throws `ttvRender is not defined` and shows 0 steps and 0 contacts.
  The fixed page throws nothing and shows 161 step rows (21 open) and 115 contacts.
- No store data was written or deleted.
- bars-engine's /board/council is fixed once this merges to main. The claude.ai board is fixed once
  `board/council-board.html` from main is republished to https://claude.ai/artifact/DxyShVS8tmvJym4HAsgnho.

## The guard

`board/page_calls.py` reads the page's scripts with comments, strings and template text blanked out, and lists any
bare call to a name the page never declares (functions, const/let/var, parameters) and that is not a browser global.
`build_board.py` now refuses to write `council-board.html` when that list is not empty, so a board read or a sync
cannot publish a page like the 19 October one. `tests/test_page_calls.py` runs it over the template, the built page and
the Nonprofit Board, and has a case with the 19 October line in it. The steward runs the tests on every pull request.

What it does not catch: a function that exists but throws, a name defined only on `window` by another script, and
calls built by name at run time. A browser load of the built page against a stub store would catch those. It needs
Chromium in CI, so it is left as the next step and was not built here.
