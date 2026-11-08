const kerrat = Number(prompt("Montako kertaa noppaa heitetään?"));
let summa = 0;

for (let i = 0; i < kerrat; i++) {
    const heitto = Math.floor(Math.random() * 6) + 1;
    summa += heitto;
}

document.querySelector("#tulos").textContent = `Silmälukujen summa: ${summa}`;