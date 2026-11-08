const vuosi = Number(prompt("Anna vuosiluku:"));
const tulos = document.querySelector("#tulos");

if (vuosi % 400 === 0 || (vuosi % 4 === 0 && vuosi % 100 !== 0)) {
    tulos.textContent = `${vuosi} on karkausvuosi.`;
} else {
    tulos.textContent = `${vuosi} ei ole karkausvuosi.`;
}