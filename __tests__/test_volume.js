const { JSDOM } = require('jsdom');
const fs = require('fs');
const path = require('path');

const html = fs.readFileSync(path.resolve(__dirname, '../index.html'), 'utf8');

describe('Calcolo del Volume di un Cubo', () => {
  let dom;
  let latoInput;
  let calcolaButton;
  let risultatoElement;

  beforeEach(() => {
    dom = new JSDOM(html, { runScripts: 'dangerously' });
    latoInput = dom.window.document.getElementById('lato');
    calcolaButton = dom.window.document.querySelector('button');
    risultatoElement = dom.window.document.getElementById('risultato');
  });

  it('Calcola il volume correttamente', () => {
    latoInput.value = '5';
    calcolaButton.click();
    expect(risultatoElement.innerHTML).toBe('Il volume è: 125');
  });
});

