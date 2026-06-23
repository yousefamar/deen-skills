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

**No install/dependencies.** The skill is pure documentation; the agent calls the public API
directly with `curl` or its own HTTP/fetch tool.

## Call the API directly
```bash
curl -s https://api.deen.ai/search -H 'content-type: application/json' \
  -d '{"query":"is music haram","filters":{"madhab":"Hanafi Fiqh"}}'

curl -s https://api.deen.ai/fatwa/94459
```
See [`deen-fatwa-search/references/REFERENCE.md`](deen-fatwa-search/references/REFERENCE.md)
for the full HTTP contract.

## License
MIT — see [LICENSE](LICENSE).
