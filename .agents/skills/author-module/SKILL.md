---
name: author-module
description: Author or revise a complete piano lesson with playable examples, required practice, and a separate assessment rubric.
---

# Author a piano lesson

Read `docs/agents/PROFILE.md`, `docs/agents/module-structure.md`, `docs/agents/music-style.md`, the reference lesson, and the target curriculum topic/dependencies.

Create `README.md`, `notes.md`, `exercises.md`, and `solutions.md` for a complete lesson. Use one canonical independent check in the README and link it from the other files. Specify observable criteria, allowed aids/preparation, hand/register, duration/meter, beat unit where relevant, and a later review. Set a workload that fits short sessions.

Use original exercises or exact references to inspected readable books/scores. Do not invent edition-specific page/bar assignments. Letter-name patterns cannot test staff reading; fresh-reading checks need unfamiliar material. Keep correction keys separate from prompts and do not prefill learner work.

Link the module from its phase README, preserve topic IDs, and run `python3 tools/agent_config.py check`. Creating the lesson leaves its progress box unchecked.
