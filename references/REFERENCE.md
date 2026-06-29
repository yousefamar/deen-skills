# deen.ai fatwa API — contract

Base URL: `https://api.deen.ai` (no auth; rate-limited). Override with `DEEN_API` env var.

## `POST /search`
Request:
```json
{ "query": "music instruments", "k": 5,
  "filters": { "madhab": "Hanafi Fiqh", "source": "Askimam.org", "lang": "en" } }
```
- `query` (required) — keywords; lexical BM25 (FTS5). Punctuation/operators are sanitized.
- `k` — default 5, hard-capped at 20.
- `filters` — all optional. `madhab` ∈ {Hanafi Fiqh, Shafi'i Fiqh, Maliki Fiqh, Hanbali Fiqh};
  `source` ∈ ~44 sites; `lang` ∈ {ar, en}.

Response:
```json
{ "query": "...", "count": 2,
  "results": [ { "id": 94459, "title": "...", "url": "https://islamqa.org/...",
                 "source": "Askimam.org", "madhab": "Hanafi Fiqh", "lang": "en",
                 "scholars": ["Shaykh Ebrahim Desai"], "score": 14.557,
                 "snippet": "...[match]..." } ] }
```
Higher `score` = more relevant. Empty query → 400; no matches → `count:0, results:[]`.

## `GET /fatwa/{id}`
Returns the full record:
```json
{ "id": 94459, "title": "...", "body": "<full answer text>", "url": "...",
  "site": "islamqa.org", "lang": "en", "madhab": "Hanafi Fiqh",
  "source": "Askimam.org", "source_url": "...", "scholars": ["..."], "answer_no": 19038 }
```

## `GET /health`
`{ "ok": true, "service": "deen-fatwa-search", "count": 142780 }`

## Corpus
142,780 fatwas: 15,038 islamqa.info/en, 29,598 islamqa.info/ar, 98,144 islamqa.org
(aggregator; madhab/source/scholar-tagged). ~33% Arabic. Static snapshot (source data 2024).
