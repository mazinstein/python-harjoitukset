const count = Number(prompt("Kuinka monta osallistujaa?"));
const names = [];

for (let i = 0; i < count; i++) {
    const name = prompt(`Anna osallistujan ${i + 1} nimi:`);
    names.push(name);
}

names.sort();

const target = document.querySelector("#target");

for (const name of names) {
    const item = document.createElement("li");
    item.textContent = name;
    target.appendChild(item);
}