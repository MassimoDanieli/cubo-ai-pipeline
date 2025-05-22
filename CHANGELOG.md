# Changelog

## [Unreleased]

### Aggiunto
- Funzione `calcolaVolume(input)` isolata e testabile
- Test Jest per `calcolaVolume()` in `__tests__/main.test.js`
- Badge "JS Tests Passing" nel `README.md`
- Pipeline CI GitHub Actions per Jest (`test.yml`)

### Rimosso
- File `__tests__/test_volume.js` basato su jsdom non più necessario

### Modificato
- Refactor del codice da ES Module (`import/export`) a CommonJS (`require/module.exports`) per compatibilità con Jest
- Aggiornamento `package.json` rimuovendo `"type": "module"`
