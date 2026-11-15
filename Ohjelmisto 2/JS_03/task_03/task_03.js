const dogs = [];

for (let i = 0; i < 6; i++) {
    const name = prompt(`Anna koiran ${i + 1} nimi:`);
    dogs.push(name);
}

dogs.sort();
dogs.reverse();

const target = document.querySelector("#target");

for (const dog of dogs) {
    const item = document.createElement("li");
    item.textContent = dog;
    target.appendChild(item);
}