# deen skills

[Agent Skills](https://agentskills.io) for [deen.ai](https://deen.ai) that give any
skill-compatible AI agent (Claude Code, VS Code + Copilot, OpenAI Codex, …) the ability to
search Islamic rulings.

## [`deen-fatwa-search`](SKILL.md)

Search **142,780 fatwas** (islamqa.info + the islamqa.org aggregator of ~44 fatwa sites;
Hanafi/Shafi'i/Maliki/Hanbali; English & Arabic) by keyword, with optional filters by madhab,
source, and language. Returns ranked, cited excerpts; fetches full text by id. Backed by the
public API at **https://api.deen.ai** (no key required).

It is **retrieval-only**: the agent grounds and cites its answer in real fatwas, and states
which source/madhab each ruling comes from. It does not issue rulings.

## Install

```bash
npx skills add yousefamar/deen-skills
```

Then ask your agent an Islamic-ruling question, it discovers the skill by its description and
activates it automatically. No dependencies: the skill is pure documentation and the agent
calls the public API directly.

(By hand instead: copy `SKILL.md` and `references/` into your agent's skills directory, e.g.
`~/.claude/skills/deen-fatwa-search/`.)

## Call the API directly

```bash
curl -s https://api.deen.ai/search -H 'content-type: application/json' \
  -d '{"query":"is music haram","filters":{"madhab":"Hanafi Fiqh"}}'

curl -s https://api.deen.ai/fatwa/94459
```

See [`references/REFERENCE.md`](references/REFERENCE.md) for the full HTTP contract.

## License

MIT, see [LICENSE](LICENSE).
