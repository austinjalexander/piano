# Piano tutor setup

This checkout owns its configuration. Its organization follows the physics repo, while its curriculum and evidence rules are adapted for musical practice.

## Shared entry points

[AGENTS.md](../../AGENTS.md), [the profile](PROFILE.md), [tutoring guidance](tutoring.md), [module structure](module-structure.md), and [music conventions](music-style.md) hold the canonical behavior. Six workflows live in [.agents/skills/](../../.agents/skills/): tutoring, performance feedback, prerequisite diagnosis, lesson authoring, external courses, and book-library use.

Cursor rule files refer to shared guidance; `CLAUDE.md` imports `AGENTS.md`; `.claude/skills/` contains relative links to local canonical skill folders. No link points into the physics checkout.

Open the repository root in the assistant you use. Request a workflow naturally, for example “Tutor me through the keyboard and pulse lesson,” or name the skill in a tool that supports local skills. Reload project guidance after setup if necessary. Local validation checks files and links; it does not prove a running client has loaded them.

## Validate and hand off

```sh
python3 tools/agent_config.py check
python3 tools/agent_config.py export --skill tutor-session --module notes/phase-1-foundations/01-keyboard-and-pulse > /tmp/piano-study.md
```

The tools require Python 3.10+ and no third-party packages. The checker validates skills, relative Claude links, adapters, topic IDs, and local Markdown link targets. It never edits another repo or global settings.

The export command includes shared guidance, current planning/progress, the selected workflow, and the learner-facing lesson files. It omits the separate solutions file. For a lesson that is only an outline, author its complete files first.

See [the handoff guide](CHATGPT-START.md) for a conversation without repository tools.
