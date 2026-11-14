# 🧠 Cubo AI Pipeline

![JS Tests](https://img.shields.io/github/actions/workflow/status/MassimoDanieli/cubo-ai-pipeline/test.yml?label=JS%20tests&logo=jest)
![AI](https://img.shields.io/github/actions/workflow/status/MassimoDanieli/cubo-ai-pipeline/ai.yml?label=AI%20review&logo=githubactions)

Una web app minuscola (il volume di un cubo) usata come banco di prova per una pipeline CI/CD con l'IA: review delle PR, proposte di test, changelog e un assistente agentico su richiesta.

🌐 Demo: <https://massimodanieli.github.io/cubo-ai-pipeline/> · [Approfondimento tecnico](docs/tech.html)

## La pipeline

| Workflow | Quando | Cosa fa |
|---|---|---|
| [`test.yml`](.github/workflows/test.yml) | push e PR | ESLint + Jest con coverage su Node 22 |
| [`ai.yml`](.github/workflows/ai.yml) → review | ogni PR | review del **diff** con risultati strutturati (file, riga, gravità, fix); un solo commento aggiornato; blocca il merge solo su problemi *critical* |
| [`ai.yml`](.github/workflows/ai.yml) → tests | ogni PR | propone file di test Jest per il codice cambiato, come commento e artifact |
| [`ai.yml`](.github/workflows/ai.yml) → changelog | tag `v*` | voce di changelog dai commit dall'ultimo tag, proposta come PR |
| [`claude.yml`](.github/workflows/claude.yml) | commento con `@claude` | Claude Code gira nel repo, legge i file, lancia i test e risponde o propone una correzione |

I passi IA vengono dai workflow riutilizzabili di [ai-devops-starter-kit v2](https://github.com/MassimoDanieli/ai-devops-starter-kit), quindi il fornitore si cambia con un parametro (`provider: anthropic | openai | local`) senza toccare questo repo.

### Configurazione

Un secret: `ANTHROPIC_API_KEY`. Per `@claude` installa anche la [Claude GitHub App](https://github.com/apps/claude).

Per usare OpenAI aggiungi in `ai.yml`:

```yaml
    with:
      provider: openai
      model: <id del modello>
```

## Locale

```bash
npm ci
npm run lint
npm test            # oppure: npm run coverage
```

Il sito statico è in `docs/` (GitHub Pages).

## Storia

La v1 (maggio 2025) aveva tre script Python che chiamavano `gpt-3.5-turbo`: review file per file, generazione di test, changelog a ogni push su `main`. Il modello è stato spento da OpenAI il 23 ottobre 2026 e la pipeline si è fermata. Anche il workflow dei test era rotto (YAML non valido, ESLint senza ambiente Node/Jest, lockfile non allineato). Dettagli in [CHANGELOG.md](CHANGELOG.md).

MIT © Massimo Danieli
