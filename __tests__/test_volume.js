Ecco un test automatico Jest che simula l'inserimento di un valore, clicca sul bottone e verifica che il contenuto del tag con ID "risultato" sia corretto:

```javascript
// index.test.js

// Importa Jest e il modulo da testare
const { JSDOM } = require('jsdom');
const fs = require('fs');
const path = require('path');

// Carica il contenuto dell'HTML
const html = fs.readFileSync(path.resolve(__dirname, 'index.html'), 'utf8');

// Definisci il test
describe('Calcolo del Volume di un Cubo', () => {
  let dom;
  let latoInput;
  let calcolaButton;
  let risultatoElement;

  beforeEach(() => {
    // Crea un nuovo DOM prima di ogni test
    dom = new JSDOM(html, { runScripts: 'dangerously' });

    // Ottieni i riferimenti agli elementi HTML
    latoInput = dom.window.document.getElementById('lato');
    calcolaButton = dom.window.document.querySelector('button');
    risultatoElement = dom.window.document.getElementById('risultato');
  });

  it('Calcola il volume correttamente', () => {
    // Simula l'inserimento di un valore
    latoInput.value = '5';

    // Simula il click sul bottone
    calcolaButton.click();

    // Verifica che il risultato sia corretto
    expect(risultatoElement.innerText).toBe('Il volume è: 125');
  });
});
```

Assicurati di avere Jest installato nel tuo progetto e di aver configurato correttamente i file di test. Esegui il test con Jest per verificare che funzioni correttamente.