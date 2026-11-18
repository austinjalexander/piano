# Piano repository profile

The user wants a piano learning repository following the physics repo's organization. The confirmed goal is learning piano. The instrument is a Roland RP750-CH, verified from a learner-provided label photo on October 20, 2026; the serial number is recorded in [GOALS.md](../../GOALS.md). Previous ability, genres, teacher arrangements, target pieces, and practice capacity are unconfirmed. Do not infer any of these from another learning repository or a manual filename.

## Sources

- `GOALS.md`: confirmed intent and adjustable learning proposals.
- `docs/CURRICULUM.md`: topic IDs, scope, and prerequisites.
- `STUDY_PLAN.md`: practice structure and provisional weekly capacity.
- `PROGRESS.md`: topic evidence and pending starting information.
- `REPERTOIRE.md` and `repertoire/`: actual piece/arrangement records.
- `practice/`: dated learner logs. It starts empty; templates are not attempts.
- `RESOURCES.md`: selected primary-source links and local-book candidates.
- `BOOK_LIBRARY.md`, `library/config.json`, and `library/catalog.json`: external library metadata and access limits.
- `EXTERNAL_COURSES.md` and `external-courses/`: provider/teacher/method positions and return queue.

Paths above are relative to the repository root. Canonical complete lesson: `notes/phase-1-foundations/01-keyboard-and-pulse/`. Other phase READMEs are outlines; detailed lessons and checks are pending.

## Pacing and evidence

The example budget is **20 minutes × 5 days = 100 minutes/week including logging**, pending confirmation. It is separate from physics. Do not assume extra time for an online course or teacher assignment; replace overlapping tasks within the budget.

The entry lesson intentionally uses letter names rather than staff notation, a comfortable self-chosen pulse, and separate hands. Its success does not complete staff reading, hands-together playing, or a repertoire piece. A baseline can route an experienced player to useful work without automatically completing earlier topics.

Local library root: `/Users/nwprt/Dropbox/1_Studies/Piano`. At setup, one PDF reports nonzero size and ten report zero bytes. The cover of `RP750_eng01_W.pdf` was inspected on October 20, 2026 and identifies the Roland RP750 Digital Piano owner's manual. The instrument model was separately verified from the learner's label photo; keyboard and pedal condition/setup remain unassessed. Keep books outside Git and verify actual editions/pages before mapping lessons. Do not import the physics repo's library organization preferences as authorization here.

## Repository maintenance

Tools use Python 3.10+ standard library only. No scientific package, notebook environment, notation software, or MIDI dependency is needed to begin. Run the configuration check and exercise any changed CLI workflow. Documentation changes need link/config validation; avoid adding a test suite that merely matches prose.

Do not copy configuration via symlinks to another repository. Local Claude skill links point only to `.agents/skills/` in this checkout. No exam grade, certificate route, or completion schedule is established.
