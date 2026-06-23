---
name: deen-fatwa-search
description: Search 142,780 Islamic rulings (fatwas) from islamqa.info and islamqa.org — Hanafi/Shafi'i/Maliki/Hanbali, English & Arabic — by keyword, with optional filters by madhab, source, and language. Use when the user asks about an Islamic ruling, fiqh, or wants sourced scholarly opinions on a religious matter. Returns ranked excerpts with citations (source site, madhab, scholars, URL); full text fetchable by id. Retrieval-only: ground every answer in the returned fatwas, cite them, and state which madhab/source each comes from.
license: MIT
metadata:
  author: deen.ai
  version: "1.0"
compatibility: Requires python3 and outbound HTTPS to api.deen.ai
---

# deen.ai fatwa search

A retrieval tool over a corpus of **142,780 fatwas** (islamqa.info + the islamqa.org
aggregator of ~44 fatwa sites). It does **lexical keyword search** — it does not answer;
**you** answer, grounded in what it returns.

## When to use
Any question about an Islamic ruling, practice, or fiqh where citing real fatwas matters.

## Workflow
1. **Search** with concise keywords (not a full sentence):
   ```
   scripts/deen.py search "music instruments wedding" -k 5
   ```
2. **Read the snippets/scores.** If results look weak (low scores, off-topic), **reformulate** —
   try synonyms, Islamic terms (e.g. `wudu`/`ablution`, `salah`/`prayer`), or for an Arabic
   question search Arabic terms (or translate to English) since the corpus is bilingual.
3. **Fetch full text** for the best hit(s) before quoting a ruling:
   ```
   scripts/deen.py get 94459
   ```
4. **Answer grounded + cited.** Quote/paraphrase only what the fatwas say, link the `url`, and
   **name the source and madhab** of each ruling.

## Filters (optional)
- `--madhab "Hanafi Fiqh"` (also `Shafi'i Fiqh`, `Maliki Fiqh`, `Hanbali Fiqh`)
- `--source "Askimam.org"` (one of ~44 sites; e.g. Muftionline.co.za, Seekersguidance.org)
- `--lang ar` | `--lang en`

Use `--madhab` when the user follows a specific school. `-k` caps results (default 5, max 20).

## Critical: transparency about tradition
The corpus mixes scholarly traditions — **islamqa.info is Salafi-leaning; the islamqa.org docs
are overwhelmingly Deobandi/Hanafi**. Rulings can differ by madhab. So:
- **Always state which source/madhab/scholar a ruling comes from.** Never present one school's
  position as "the" Islamic ruling.
- If schools differ, say so and show the range.
- You are surfacing scholarship, not issuing a fatwa — encourage the user to consult a qualified
  scholar for binding rulings.

See [REFERENCE.md](references/REFERENCE.md) for the raw API contract.
