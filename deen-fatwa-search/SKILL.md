---
name: deen-fatwa-search
description: Search 142,780 Islamic rulings (fatwas) from islamqa.info and islamqa.org — Hanafi/Shafi'i/Maliki/Hanbali, English & Arabic — by keyword, with optional filters by madhab, source, and language. Use when the user asks about an Islamic ruling, fiqh, or wants sourced scholarly opinions on a religious matter. Returns ranked excerpts with citations (source site, madhab, scholars, URL); full text fetchable by id. Retrieval-only: ground every answer in the returned fatwas, cite them, and state which madhab/source each comes from.
license: MIT
metadata:
  author: deen.ai
  version: "2.0"
compatibility: Requires the ability to make HTTPS requests (curl, or your environment's HTTP/fetch tool) to api.deen.ai
---

# deen.ai fatwa search

A retrieval tool over **142,780 fatwas** (islamqa.info + the islamqa.org aggregator of ~44
fatwa sites). It does **lexical keyword search** — it does not answer; **you** answer,
grounded in what it returns.

It's a plain HTTPS/JSON API at **`https://api.deen.ai`** (no key, no auth). Call it with
`curl`, or whatever HTTP/fetch capability you have — there is nothing to install.

## When to use
Any question about an Islamic ruling, practice, or fiqh where citing real fatwas matters.

## Endpoints

**Search** — `POST /search`, JSON body `{ "query", "k"?, "filters"? }`:
```bash
curl -s https://api.deen.ai/search -H 'content-type: application/json' \
  -d '{"query":"music instruments wedding","k":5}'
```
`k` = number of results (default 5, max 20). `filters` (all optional):
`{"madhab":"Hanafi Fiqh","source":"Askimam.org","lang":"ar"}`.
Returns ranked `results[]`, each: `id, title, url, source, madhab, scholars[], lang, score, snippet`
(higher `score` = more relevant).

**Get full text** — `GET /fatwa/{id}` (use an `id` from a search result):
```bash
curl -s https://api.deen.ai/fatwa/94459
```
Returns the full record incl. `body` (the complete answer).

## Workflow
1. **Search** with concise keywords (not a full sentence).
2. **Read the snippets and scores.** If results look weak (low/flat scores, off-topic),
   **reformulate** — try synonyms or Islamic terms (`wudu`/`ablution`, `salah`/`prayer`); for an
   Arabic question, search Arabic terms or translate to English (the corpus is bilingual).
3. **Fetch the full text** (`GET /fatwa/{id}`) for the best hit(s) before quoting a ruling.
4. **Answer grounded + cited** — quote/paraphrase only what the fatwas say, link the `url`, and
   **name the source and madhab** of each ruling.

## Filters
- `madhab`: `Hanafi Fiqh` · `Shafi'i Fiqh` · `Maliki Fiqh` · `Hanbali Fiqh`
- `source`: one of ~44 sites (e.g. `Askimam.org`, `Muftionline.co.za`, `Seekersguidance.org`)
- `lang`: `ar` · `en`

Use `madhab` when the user follows a specific school.

## Critical: transparency about tradition
The corpus mixes scholarly traditions — **islamqa.info is Salafi-leaning; the islamqa.org docs
are overwhelmingly Deobandi/Hanafi**. Rulings can differ by madhab. So:
- **Always state which source/madhab/scholar a ruling comes from.** Never present one school's
  position as "the" Islamic ruling.
- If schools differ, say so and show the range.
- You are surfacing scholarship, not issuing a fatwa — encourage the user to consult a qualified
  scholar for binding rulings.

See [REFERENCE.md](references/REFERENCE.md) for the full API contract.
