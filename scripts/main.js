function calcolaVolume(input) {
  const lato = parseFloat(input);
  if (isNaN(lato) || lato < 0) return 'Errore';
  return `Il volume è: ${Math.pow(lato, 3)}`;
}

module.exports = { calcolaVolume };

