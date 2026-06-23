#!/usr/bin/env python3
"""deen.ai fatwa search — CLI over the public api.deen.ai (stdlib only).

Usage:
  deen.py search "<keywords>" [--madhab M] [--source S] [--lang ar|en] [-k N] [--json]
  deen.py get <id> [--json]
  deen.py --help

Search lexically (BM25) over 142,780 Islamic rulings (islamqa.info + islamqa.org),
then fetch full text by id. Retrieval only — it returns sourced fatwas, it does not
issue rulings.

Options:
  -k N            Number of results (default 5, capped at 20).
  --madhab M      Filter: "Hanafi Fiqh" | "Shafi'i Fiqh" | "Maliki Fiqh" | "Hanbali Fiqh".
  --source S      Filter by source site, e.g. "Askimam.org".
  --lang ar|en    Filter by language.
  --json          Emit raw JSON (default: human-readable, citation-formatted).

Environment:
  DEEN_API        API base URL (default https://api.deen.ai).

Exit codes: 0 ok · 2 usage error · 3 request/network error.
"""
import sys, os, json, urllib.request, urllib.error

API = os.environ.get("DEEN_API", "https://api.deen.ai").rstrip("/")


def die(code, msg):
    print(msg, file=sys.stderr)
    sys.exit(code)


def _req(path, payload=None):
    data = json.dumps(payload).encode() if payload is not None else None
    req = urllib.request.Request(
        API + path, data=data,
        headers={"content-type": "application/json"},
        method="POST" if payload is not None else "GET")
    try:
        with urllib.request.urlopen(req, timeout=35) as r:   # headroom for cold starts
            return json.load(r)
    except urllib.error.HTTPError as e:
        die(3, f"request failed: HTTP {e.code} — {e.read().decode()[:200]}")
    except Exception as e:
        die(3, f"request failed: {type(e).__name__}: {e}")


def _parse(argv):
    """Return (positional, opts) for the shared flag set."""
    pos, opts = [], {"k": 5, "json": False, "filters": {}}
    i = 0
    while i < len(argv):
        a = argv[i]
        if a in ("-h", "--help"):
            print(__doc__); sys.exit(0)
        elif a == "--json": opts["json"] = True; i += 1
        elif a == "-k": opts["k"] = int(argv[i + 1]); i += 2
        elif a in ("--madhab", "--source", "--lang"):
            opts["filters"][a[2:]] = argv[i + 1]; i += 2
        else:
            pos.append(a); i += 1
    return pos, opts


def cmd_search(argv):
    pos, opts = _parse(argv)
    if not pos:
        die(2, "usage: deen.py search \"<keywords>\" [--madhab M] [--source S] [--lang ar|en] [-k N]")
    out = _req("/search", {"query": pos[0], "k": opts["k"], "filters": opts["filters"]})
    if opts["json"]:
        print(json.dumps(out, ensure_ascii=False, indent=2)); return
    print(f"{out['count']} result(s) for: {out['query']}\n")
    for r in out["results"]:
        sch = (" — " + ", ".join(r["scholars"])) if r.get("scholars") else ""
        print(f"[{r['id']}] score={r['score']}  ({r['lang']}, {r.get('madhab') or '—'}, {r['source']}{sch})")
        print(f"  {r['title']}")
        print(f"  {r['snippet']}")
        print(f"  {r['url']}\n")


def cmd_get(argv):
    pos, opts = _parse(argv)
    if not pos:
        die(2, "usage: deen.py get <id>")
    d = _req("/fatwa/" + str(pos[0]))
    if opts["json"]:
        print(json.dumps(d, ensure_ascii=False, indent=2)); return
    print(f"[{d['id']}] {d['title']}")
    print(f"source={d['source']}  madhab={d.get('madhab') or '—'}  lang={d['lang']}  "
          f"scholars={', '.join(d.get('scholars') or []) or '—'}")
    print(f"url={d['url']}\n")
    print(d["body"])


def main():
    if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help"):
        print(__doc__); sys.exit(0)
    cmd, argv = sys.argv[1], sys.argv[2:]
    if cmd == "search": cmd_search(argv)
    elif cmd == "get": cmd_get(argv)
    else: die(2, f"unknown command: {cmd}\n{__doc__}")


if __name__ == "__main__":
    main()
