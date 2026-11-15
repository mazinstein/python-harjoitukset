"use strict";

const target = document.querySelector("#target");
const texts = ["First item", "Second item", "Third item"];

for (let i = 0; i < texts.length; i++) {
    const item = document.createElement("li");
    item.textContent = texts[i];

    if (i === 1) {
        item.classList.add("my-item");
    }

    target.appendChild(item);
}