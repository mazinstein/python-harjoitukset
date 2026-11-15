function concat(strings) {
    let result = "";

    for (const text of strings) {
        result += text;
    }

    return result;
}

const names = ["Johnny", "DeeDee", "Joey", "Marky"];
const result = concat(names);

document.querySelector("#target").textContent = result;