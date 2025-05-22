# 🧠 Cubo AI Pipeline

![GPT Review](https://img.shields.io/github/actions/workflow/status/MassimoDanieli/cubo-ai-pipeline/review.yml?label=GPT%20Review&logo=openai)
![JS Tests](https://img.shields.io/github/actions/workflow/status/MassimoDanieli/cubo-ai-pipeline/test.yml?label=JS%20Tests&logo=jest)
![Changelog](https://img.shields.io/badge/Changelog-GPT%20Generated-blueviolet?style=flat)
![100% AI Pipeline](https://img.shields.io/badge/AI--Driven-DevOps%20Pipeline-brightgreen?logo=github)

---

## 📋 Descrizione

**Cubo AI Pipeline** è una demo completa di CI/CD guidata dall'intelligenza artificiale.
Include:

- ✅ **Web UI HTML** per calcolare il volume di un cubo
- ✅ **Code review automatica** con ChatGPT
- ✅ **Generazione test JS** con GPT su `index.html`
- ✅ **Esecuzione test Jest in CI**
- ✅ **Generazione automatica di `CHANGELOG.md`** via GPT
- ✅ **File `.gpt-review/*.md` salvati e versionabili**

---

## ⚙️ Funzionalità DevOps AI

### 🔍 Code Review GPT
Ogni PR analizza i file modificati (`.js`, `.html`, `.py`) con GPT-3.5.  
Risultato salvato in `.gpt-review/review-*.md`.

### 🧪 Test JS generati da GPT
GPT genera automaticamente test Jest per la UI HTML.  
I test sono salvati in `__tests__/test_volume.js`.

### 🧪 Esecuzione test automatica
Ogni PR esegue `npx jest`. Se il test fallisce, la pipeline blocca il merge.

### 🧠 Changelog GPT
Ogni push su `main` genera un file `CHANGELOG.md` con gli ultimi commit descritti da GPT.

---

## 🚀 Come eseguire localmente

```bash
# Setup ambiente virtuale Python
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Setup npm
npm install

# Genera test JS via GPT
python3 scripts/generate_js_test.py

# Esegui test Jest
npm test

