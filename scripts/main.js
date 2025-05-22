export function calcolaVolume(lato) {
  const n = parseFloat(lato);
  if (isNaN(n)) return 'Errore';
  return `Il volume è: ${Math.pow(n, 3)}`;
}

export function calcolaEDisegna() {
  const lato = document.getElementById('lato').value;
  const output = calcolaVolume(lato);
  document.getElementById('risultato').innerText = output;
}

