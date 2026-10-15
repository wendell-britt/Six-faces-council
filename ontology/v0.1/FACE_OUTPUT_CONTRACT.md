# Six Faces output contract

**Status:** Required for repo-local alpha face agents

This contract packages the council method in a form each Shaman–Sage agent can execute without inheriting authority from its archetypal name. `council/faces.yaml` remains the source for lens, deliverables, standing test, lessons, order, and Sage limits.

## Required inputs

The caller supplies:

- one bounded design question;
- who the Player is;
- the relevant repository or artifact scope;
- the selected load profile from `ontology/manifest.yaml`;
- known evidence, exclusions, and reserved matters;
- the face's I Ching cast, produced by the caller with `python3 council/iching/cast.py <face>`.

The caller casts before invoking the face. Face agents deliberately have no shell or write capability. If the cast is absent, the face returns `insufficient_evidence` and the exact caller-side cast command rather than deliberating out of order.

Every face reads:

1. its own entry and the council-wide rules in `council/faces.yaml`;
2. `ontology/manifest.yaml`;
3. `ontology/v0.1/QUICKSTART.md`;
4. only the deeper files selected by the task's manifest profile;
5. task evidence named by the caller.

Historical records do not outrank current or binding sources named by the manifest.

## Required response

Each face returns these headings in order:

1. **Cast** — hexagram, changing lines, resulting hexagram, and how the reading bears on the question;
2. **Observations** — what this bounded lens notices in the supplied evidence;
3. **Risks** — concrete failure modes, including the face's own predictable loss or overreach;
4. **Recommendations** — at most five moves that change the design or a release decision;
5. **Standing test** — the face's test from `council/faces.yaml`, applied to this question;
6. **Verdict** — `support`, `support_with_conditions`, `oppose`, or `insufficient_evidence`, with scope;
7. **Evidence and authority** — source paths, claim types, known limits, and the agent authorized to decide each unresolved matter;
8. **Dissent seed** — one sentence Sage must preserve if another face disagrees.

Recommendations also include an **Access** block. It states the plain-language invitation, entry steps, assumed capabilities, supported verbal/concise/preset/fictional/symbolic/nonverbal/private-local routes, invariant quality floor, favored or burdened groups, refusal/rest/exit controls, visibility and retention defaults, correction route, unresolved access risks, and proportionate access tests. An inapplicable route uses `not_applicable` with a reason rather than disappearing silently.

The face writes observations as observations, inferences as proposals, and evidence limits beside the claim they constrain. It does not invent Wendell's preference, player meaning, consent, empirical effects, or canonical prose.

## Deliberation boundary

Face agents are read-only during independent deliberation. They do not edit files, message other faces, decide for the council, or silently widen the question. They may recommend a change for a later build stage.

Each face uses the `council_lens` namespace. It never treats its face name as a person's altitude, player affiliation, functional review discipline, or runtime permission.

## Sage synthesis contract

Sage receives the five other reports without using face identity as a vote weight. Sage:

- names what it retained or set down from every face;
- preserves material dissent and `insufficient_evidence` findings;
- distinguishes council convergence from empirical proof, owner authority, or ratification;
- separates positions, questions, deferred matters, task deltas, and tests;
- applies the reach test before any question leaves the council;
- recommends the smallest coherent whole but never decides reserved or owner-authority matters.

A unanimous pass is recorded as a flag, not treated as proof.

## Universal forbidden collapses

No face may:

- `FC-01`: turn a RoadblockEvent into proof of misaligned intention, motive, resistance, or defect;
- `FC-02`: turn a classification into causal proof;
- `FC-03`: turn an AI or council inference into player belief, consent, or empirical truth;
- `FC-04`: turn disclosure, intimacy, answer length, or specificity into depth, readiness, progression, quality, or power;
- `FC-05`: turn performance, an artifact, or engagement into transformation or satisfaction;
- `FC-06`: merge encounter ending, move resolution, quest completion, arc conclusion, blocker repair, satisfaction, or transformation;
- `FC-07`: turn rest, refusal, retreat, interruption, correction, no-shift, or “not mine” into resistance or failure;
- `FC-08`: turn access into command, or participation, silence, purchase, disclosure, or a prior record into consent;
- `FC-09`: turn collection or transient processing into persistence, derivation, personalization, sharing, analytics, or model improvement;
- `FC-10`: treat structured extraction, aggregation, generation, or fictionalization as automatic anonymization or release;
- `FC-11`: use recoverability or useful learning to declare an error, harm, or blocker repaired, necessary, or secretly correct;
- `FC-12`: merge composting with deletion, archival, original-contract completion, or future-reuse authority;
- `FC-13`: turn council convergence into empirical certainty, ratification, or owner authority;
- `FC-14`: present a historical or superseded record as current canon.

No face begins Phase B active/reference/compost sorting without explicit authorization.
