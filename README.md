# piano

A personal piano learning workspace, following the structure of the physics repo: a curriculum, a practice plan, evidence of progress, reusable templates, and shared AI tutor guidance.

The starting path is beginner friendly. The instrument is a Roland RP750-CH; its serial number and source are recorded in [GOALS.md](GOALS.md). Experience, musical interests, and available practice time still need to be confirmed; the plan adjusts to those answers.

## Start playing

1. Record your starting point with the [baseline check](assessments/baseline.md). Skip unfamiliar tasks rather than preparing for the check.
2. Open the [first lesson](notes/phase-1-foundations/01-keyboard-and-pulse/README.md): find notes, count a steady pulse, and play an original two-bar phrase.
3. Follow the [practice plan](STUDY_PLAN.md). Its provisional example is 20 minutes on five days per week, including logging.
4. Copy the [practice log](templates/practice-log-template.md) into `practice/`, using a date in its filename. Record what actually happened and one next task.
5. Update [progress](PROGRESS.md) when the lesson's playing check, later review, and your own reflection are supported by evidence.

You can say: “Tutor me through the first lesson,” “Help me practice these two bars,” or “Review this recording.” A text description can guide practice; feedback about sound or movement requires accessible audio or video.

## Learning map

- [Goals](GOALS.md): working direction and preferences still to confirm.
- [Curriculum](docs/CURRICULUM.md): five phases, from keyboard basics to independent playing.
- [Study plan](STUDY_PLAN.md): session structure and first four practice blocks.
- [Progress](PROGRESS.md): topic evidence, separate from practice time and book completion.
- [Repertoire](REPERTOIRE.md): pieces, arrangements, difficult passages, and maintenance.
- [Resources](RESOURCES.md): a small set of source links and local-library candidates.
- [Book library](BOOK_LIBRARY.md): Dropbox catalog and file availability.
- [External courses](EXTERNAL_COURSES.md): lesson/provider positions and return points.

## Repository layout

```text
notes/phase-1-foundations/     # first complete lesson and foundation scope
notes/phase-2-reading-and-coordination/
notes/phase-3-keys-and-chords/
notes/phase-4-musical-playing/
notes/phase-5-independent-playing/
assessments/                  # starting diagnostic and later assessments
practice/                     # dated learner logs
repertoire/                   # individual piece records
templates/                    # notes, sessions, pieces, assessments, courses
library/                      # metadata catalog; books stay in Dropbox
external-courses/             # provider records
docs/agents/                  # tutor profile and shared guidance
.agents/skills/               # six reusable local workflows
.cursor/rules/                # thin adapters to shared guidance
.claude/skills/               # relative links to canonical skills
tools/                        # standard-library-only validation and catalog tools
```

Later phases are curriculum outlines. Detailed lessons and assessments are authored as they become relevant. No lessons or playing skills have been completed merely by setting up this repository.

## Tools and tutor setup

No software installation is needed to begin practicing. The optional repository tools require Python 3.10 or newer and no third-party packages:

```sh
python3 tools/agent_config.py check
python3 tools/book_library.py scan
python3 tools/book_library.py search Alfred
python3 tools/agent_config.py export --module notes/phase-1-foundations/01-keyboard-and-pulse > /tmp/piano-study.md
```

See the [agent setup guide](docs/agents/README.md) and [AGENTS.md](AGENTS.md). The handoff packet supports a chat without repository access and omits the separate solution/rubric file.

Books, commercial scores, and large recordings stay outside Git. Link their local paths in records; small original exercises and written learner work belong here.
