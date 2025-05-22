const { calcolaVolume } = require('../scripts/main');

test('volume corretto per 3', () => {
  expect(calcolaVolume('3')).toBe('Il volume è: 27');
});

test('gestisce input non numerico', () => {
  expect(calcolaVolume('abc')).toBe('Errore');
});

