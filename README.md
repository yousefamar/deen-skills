# deen skills

[Agent Skills](https://agentskills.io) for [deen.ai](https://deen.ai) — give any
skill-compatible AI agent (Claude Code, VS Code + Copilot, OpenAI Codex, …) the ability
to search Islamic rulings.

## Skills

### [`deen-fatwa-search`](deen-fatwa-search/)
Search **142,780 fatwas** (islamqa.info + the islamqa.org aggregator of ~44 fatwa sites;
Hanafi/Shafi'i/Maliki/Hanbali; English & Arabic) by keyword, with optional filters by
madhab, source, and language. Returns ranked, cited excerpts; fetches full text by id.
Backed by the public API at **https://api.deen.ai** (no key required).

It is **retrieval-only** — the agent grounds and cites its answer in real fatwas, and
states which source/madhab each ruling comes from. It does not issue rulings.

## Install

A skill is just a folder. Copy the skill into your agent's skills directory:

```bash
git clone https://github.com/yousefamar/deen-skills.git

# Claude Code (user-level):
cp -r deen-skills/deen-fatwa-search ~/.claude/skills/

# VS Code (Copilot) / OpenAI Codex (project-level):
mkdir -p .agents/skills && cp -r deen-skills/deen-fatwa-search .agents/skills/
```

Then ask your agent an Islamic-ruling question — it discovers the skill by its description
and activates it automatically.

**Requirements:** `python3` (standard library only — no pip installs) and outbound HTTPS to
`api.deen.ai`. Point elsewhere with `DEEN_API=<url>`.

## Try the script directly
```bash
deen-fatwa-search/scripts/deen.py search "is music haram" --madhab "Hanafi Fiqh"
deen-fatwa-search/scripts/deen.py get 94459
deen-fatwa-search/scripts/deen.py --help
```

## API
See [`deen-fatwa-search/references/REFERENCE.md`](deen-fatwa-search/references/REFERENCE.md)
for the raw HTTP contract.

## License
MIT — see [LICENSE](LICENSE).
