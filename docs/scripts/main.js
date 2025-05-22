window.calcolaEDisegna = function () {
  const lato = parseFloat(document.getElementById("lato").value);
  const risultato = isNaN(lato) || lato < 0
    ? "Errore"
    : `Il volume è: ${Math.pow(lato, 3)}`;
  document.getElementById("risultato").innerText = risultato;
};
