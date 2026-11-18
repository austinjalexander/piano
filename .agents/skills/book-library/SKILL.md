---
name: book-library
description: Find and verify piano books, scores, or manuals in the configured external library and map selected sections to study.
---

# Use the piano library

Read `BOOK_LIBRARY.md` and `library/config.json`. Search the saved catalog first with `python3 tools/book_library.py search <words>`; refresh metadata with `scan` when useful. The tool does not hydrate or read PDF contents.

Check chosen files' availability before using them. Zero bytes means no readable content in the current local state; do not infer why. Verify title, edition, contents, and printed/PDF page conventions from the readable source before pinning a section. A nonempty manual filename does not confirm instrument ownership or verified contents.

Keep canonical books/scores in the external library. Store only metadata, source references, and actual learner evidence here. Ordinary discovery does not authorize renaming, moving, or deleting files. For separately requested organization, make a concrete reversible manifest and avoid overwrites, preserving editions and annotations.
