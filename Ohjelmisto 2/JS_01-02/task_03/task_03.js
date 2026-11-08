const a = Number(prompt("Anna ensimmäinen kokonaisluku:"));
const b = Number(prompt("Anna toinen kokonaisluku:"));
const c = Number(prompt("Anna kolmas kokonaisluku:"));

const summa = a + b + c;
const tulo = a * b * c;
const keskiarvo = summa / 3;

document.querySelector("#tulos").textContent =
    `Summa: ${summa}, tulo: ${tulo}, keskiarvo: ${keskiarvo}`;