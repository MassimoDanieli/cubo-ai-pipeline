import { calcolaVolume } from '../scripts/main.js';

describe('calcolaVolume()', () => {
  test('ritorna il volume corretto per input valido', () => {
    expect(calcolaVolume('4')).toBe('Il volume è: 64');
  });

  test('gestisce input non numerico', () => {
    expect(calcolaVolume('ciao')).toBe('Errore');
  });

  test('gestisce input vuoto', () => {
    expect(calcolaVolume('')).toBe('Errore');
  });
});

