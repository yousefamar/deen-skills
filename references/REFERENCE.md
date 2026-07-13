# deen.ai fatwa API — contract

Base URL: `https://api.deen.ai` (no auth; rate-limited). Override with `DEEN_API` env var.

## `POST /search`
Request:
```json
{ "query": "music instruments", "k": 5,
  "filters": { "madhab": "Hanafi", "source": "askimam", "lang": "en" } }
```
- `query` (required) — keywords; lexical BM25 (FTS5). Punctuation/operators are sanitized.
- `k` — default 5, hard-capped at 20. Near-duplicate syndication copies are collapsed
  server-side, so the k results you get are distinct fatwas.
- `filters` — all optional. `madhab` ∈ {Hanafi, Shafi'i, Maliki, Hanbali, multi};
  `source` ∈ ~45 site keys (e.g. `islamqa.info`, `askimam`, `muftionline`,
  `daruliftabirmingham`, `Seekersguidance.org`, `aliftaajo`); `lang` ∈ {en, ar, ur}.

Response:
```json
{ "query": "...", "count": 2,
  "results": [ { "id": 94459, "title": "...", "url": "https://askimam.org/fatwa/19038",
                 "source": "askimam", "madhab": "Hanafi", "lang": "en",
                 "scholars": ["Shaykh Ebrahim Desai"], "score": 14.557,
                 "snippet": "...[match]..." } ] }
```
Higher `score` = more relevant. Empty query → 400; no matches → `count:0, results:[]`.

## `GET /fatwa/{id}`
Returns the full record:
```json
{ "id": 94459, "title": "...", "body": "<full answer text>", "url": "...",
  "site": "askimam", "lang": "en", "madhab": "Hanafi",
  "source": "askimam", "source_url": "...", "scholars": ["..."], "answer_no": 19038 }
```

## `GET /health`
`{ "ok": true, "service": "deen-fatwa-search", "count": 166628 }`

## Corpus
166,628 fatwas scraped directly from 45+ fatwa institutions' own sites, each linking back to
its original URL. Languages: en 122,539 / ar 35,403 / ur 7,358. Madhab-tagged where the source
states it (Hanafi 113,911, Shafi'i 6,049, Hanbali 376, Maliki 277; islamqa.info is untagged).
Largest sources: islamqa.info 44,633 · muftionline 25,331 · askimam 24,696 ·
Darulifta-Deoband.com 8,966 · Seekersguidance.org 8,848 · daruliftabirmingham 8,729 ·
daruliftadeobandwaqf 6,768 · hadithanswers 6,628 · plus ~37 more darul-iftas. Exact
question+answer duplicates are merged at ingest; residual near-duplicate pairs are tracked
in-DB (`dup_meta`, with confidence) and collapsed at search time.
