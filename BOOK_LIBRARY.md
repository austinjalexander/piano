# Piano book library

External root: `/Users/nwprt/Dropbox/1_Studies/Piano`. Books, scores, and the instrument manual stay there; this repo stores metadata and study references.

## Initial inventory

The October 18, 2026 metadata scan found 11 PDFs: `RP750_eng01_W.pdf` reports 6,863,371 bytes, and the other ten report zero bytes. A nonempty file still needs a readability/content check before assigning pages. Zero-byte files have no readable PDF content in the current local state; the cause is unconfirmed. Preserve them and check their availability in Dropbox before using them.

Filename candidates include Alfred's adult lesson books Levels One and Two, several general piano introductions/exercise books, and a popular-solos collection. Titles are inferred from filenames, not verified bibliographic metadata. The machine-readable inventory is [catalog.json](library/catalog.json); the root and destination are set in [config.json](library/config.json).

## Refresh and search

```sh
python3 tools/book_library.py scan
python3 tools/book_library.py search Alfred
```

The scan reads directory metadata only and writes the repo catalog. It does not read PDF contents, request cloud downloads, rename files, or change Dropbox settings. It refuses to replace the catalog if the library root is unavailable. Search uses the saved catalog, so an unavailable cloud file can still be discovered.

## Selecting a source

1. Find candidates by filename, then inspect the chosen readable file's title page, edition, and contents.
2. Map the specific section to a curriculum topic. Record printed page versus PDF page if they differ.
3. Put reading/page/bar positions in the relevant course or piece record. Record actual reading and playing separately.
4. Preserve external files. Renaming, moving, or deleting library files is a separate task; use an exact reversible manifest and avoid overwrites when that work is requested.

Pending: verify the ten zero-byte files' availability and selected books' editions. No external files were moved or changed during setup.
