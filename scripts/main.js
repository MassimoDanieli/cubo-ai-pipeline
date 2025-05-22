// scripts/main.js
function calcola() {
  const lato = parseFloat(document.getElementById('lato').value);
  if (isNaN(lato)) {
    document.getElementById('risultato').innerHTML = 'Inserisci un numero valido';
    return;
  }
  const volume = Math.pow(lato, 3);
  document.getElementById('risultato').innerHTML = 'Il volume è: ' + volume;
}

