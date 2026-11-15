# Changelog

All notable changes to this project are documented here. From v2 the entries
are drafted by the AI changelog workflow on each `v*` tag and arrive as a PR.

## [2.0.0] - 2026-11-14

### Changed
- AI review, test proposals and changelog now come from the reusable workflows of
  [ai-devops-starter-kit v2](https://github.com/MassimoDanieli/ai-devops-starter-kit):
  diff-based review with structured findings, one PR comment updated in place,
  any provider (Anthropic, OpenAI, local model).
- Changelog is written on `v*` tags and proposed as a PR instead of being pushed to `main`.
- JS test workflow repaired (the YAML was broken) and moved to Node 22; ESLint config
  fixed for Node and Jest files; `package-lock.json` resynced.

### Added
- `@claude` assistant on PRs and issues via `anthropics/claude-code-action`.

### Removed
- Python GPT scripts (`chatgpt_review.py`, `generate_js_test.py`, `generate_changelog.py`)
  and their copies in `docs/scripts/`: they called `gpt-3.5-turbo`, shut down by
  OpenAI on 23 October 2026.

## [1.0.0] - 2025-05-31

### Added
- Cube volume web UI, Jest tests, GPT-3.5 code review, GPT-generated JS tests and
  GPT changelog on every push to `main`.
