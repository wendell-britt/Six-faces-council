# The blocker panel

Wendell, 2026-10-12, on the overdue card: "This eventually needs to send someone to a blocker panel. Either the WAVE
game or Ontology game or a lightweight one for the council board, but it needs to be more than a reminder to go
through the blockage. It needs to actually run a player through the blockage and save the data about the specific
task that was blocked and what came up for the player and how it was resolved."

The board's own light version came first, shaped as the WAVE room's steps so the room or the Ontology game can write
the same record later. It lives in `board/template.html` (the `bk-` block).

## Where it opens

An overdue step on Your steps shows "Work through what's in the way" under the slipped note. Any other open step has
the same button inside "Stuck, or something looks different?". A step that has been worked through says how many
times and how the last run ended.

## The run

1. **Charge.** How much charge the step carries, 0 to 10.
2. **Welcome.** What the body notices when he pictures starting the step: quick picks (tight, heavy, buzzing, and so
   on) and a line of his own.
3. **Acknowledge.** A name for it (required), the element it is closest to (Metal, Water, Fire, Wood, Earth), and
   what kind of block it is: a feeling about it, something missing, no time or energy, or the step is unclear.
4. **Validate.** What it has been trying to do for him.
5. **Exhale.** Is it in alignment with what he wants right now? Yes: it stays and shapes the ending. No: it leaves on
   a breath, then "is any part still here, saying it should stay?" A part gets a staged 3-2-1 (face it, talk to it,
   be it, as `cave-321-form` staged) and is then welcomed as its own charge. At most three rounds.
6. **Ending.** Do it now (the smallest first move), move the date (a day and why), the step needs changing (what
   would make it doable), drop the step (why), or still stuck. Then the charge again, 0 to 10.

The stage words come from the Ontology game's `WAVE_STEPS` (bars-engine `content/ontology-game/game.jsx`) where it
has them. The four Allow rungs are folded into Validate here to keep the run short on a phone.

## The record

Every stage saves the whole run to `blockers/<step id>--<base36 time>` in the board's store, so a run left half way
still says what came up. Send to Claude counts it. `board/pull.py` copies each run to `council/blockers/<id>.json` on
main (a later save of the same run replaces the file), lists it in the ledger record, and prints one `needs work`
line per run: the task, the names, the ending and the charge. A session acts on "the step needs changing", "drop the
step" and "still stuck"; "move the date" has already moved the step's due date, with the why in its `moved` list.

```json
{
 "engine": "board-wave", "version": 1,
 "step": "vercel-3", "list": "vercel", "task": "Add the env var in Vercel", "due": "2026-10-11", "overdueDays": 1,
 "startedAt": "…", "savedAt": "…", "finishedAt": "…",
 "status": "open | resolved | stuck", "stage": "the stage it was saved at",
 "charge": {"before": 7, "after": 3},
 "rounds": [
  {"from": "the step", "body": ["Tight"], "felt": "…", "name": "dread", "element": "metal", "kind": "unclear",
   "validated": true, "purpose": "…", "aligned": false, "partStayed": true,
   "part321": {"face": "…", "talk": "…", "be": "…"}},
  {"from": "a part of dread", "name": "guard", "aligned": true}
 ],
 "resolution": {"kind": "now | moved | change | drop | stuck", "text": "…", "date": "only for moved", "at": "…"}
}
```

The step itself gets `blocker` (the run's id) and `blockerAt`.

## Plugging in the WAVE room or the Ontology game

Another engine takes over by writing the same record with its own `engine` value (`wave-room`, `ontology-game`) to the
same collection, and the button opens it instead of the board's panel. Fields it does not have stay out; pull.py reads
only `savedAt`, `status`, `stage`, `task`, `rounds[].name`, `resolution` and `charge`.

The WAVE room is the first (bars-engine #324, 2026-10-14). The board's Tap the Vein skip opens it with
`#wave=board&charge=...&ref=tap-the-vein--<time>` (docs/morning.md). The room saves the run to bars-engine, not to the
board's store, because the cave page cannot reach the store. `board/pull.py` fetches those runs first with
`council/wave_runs.py` (`GET /api/council/wave-runs`, `COUNCIL_MENU_TOKEN`) and writes them into `<dir>/blockers/`, so
they land like a panel run. `--no-room` skips the fetch. A room run adds `ref`, `skipStreak`, `due`, `finishedAt` and,
on each round, `texture`, `goal`, `push`, `aligned`, `move`, `line`, `light` and `layers`.

## Reading the store

A board read lists `blockers` with the other collections (`board/read.py`). It is optional, because the pickup
routine's prompt predates it: a read that leaves it out still runs, and the runs reach main on the next read that
lists it.
