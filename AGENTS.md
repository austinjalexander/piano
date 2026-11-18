# Piano learning repository instructions

These instructions apply throughout this repository. Follow the current user request; use tutoring workflows when teaching and ordinary repository workflows for maintenance.

## Start here

1. Read [the piano profile](docs/agents/PROFILE.md) for goals, source documents, budget assumptions, and the reference lesson.
2. Before teaching, read `PROGRESS.md`, the target lesson/phase README, and the latest relevant actual practice or piece record. Consult `STUDY_PLAN.md`, `docs/CURRICULUM.md`, and `REPERTOIRE.md` for scope.
3. Use [tutoring guidance](docs/agents/tutoring.md), [module structure](docs/agents/module-structure.md), and [music notation conventions](docs/agents/music-style.md) when relevant.
4. Choose the workflow in `.agents/skills/`: `tutor-session`, `grade-performance`, `diagnose-prereqs`, `author-module`, `external-course`, or `book-library`. Read the selected skill rather than relying on its name. [Agent setup](docs/agents/README.md) explains the adapters and handoff tool.

## Evidence and scope

- Generated lessons, cataloged books, and visited resource pages are preparation, not learner progress.
- Mark a topic complete only after corrected required practice, its independent check, a successful review on another day, and the learner's own dated 2–4 sentence reflection. Link evidence and retain earlier attempts.
- Never invent practice, times, tempos, scores, reflections, teacher feedback, course completion, instrument ownership, or account access. Label self-reported, audio-reviewed, video-reviewed, and teacher-reported evidence explicitly.
- Describe sound only when accessible audio supports it, and movement/fingering only when visible evidence supports it. Text descriptions support discussion and self-reported results, not claims of observation. State unassessed criteria.
- Keep independent checks free of hints or demonstrations until the attempt ends. Offer staged hints during practice; honor a request for a demonstration and record assistance.
- Set tasks within the confirmed piano budget. The 100-minute weekly example remains provisional. Do not copy the physics budget or credential goals.
- Use comfortable, controlled practice before speed. Stop tasks that cause pain; do not prescribe forced stretches or claim a text tutor can diagnose physical technique.
- Preserve learner work, external books, and recordings. Verify readable editions before assigning pages. Do not move or rename Dropbox files as part of ordinary lesson setup.

## Maintaining the configuration

Shared behavior lives here, in `docs/agents/`, and in `.agents/skills/`. Cursor rules and `CLAUDE.md` are thin adapters; `.claude/skills/` links to the local canonical skills. There are no links to the physics repo. Run `python3 tools/agent_config.py check` after changes. Do not modify global assistant configuration for this project.
