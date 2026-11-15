const numbers = [];

for (let i = 0; i < 5; i++) {
    const number = Number(prompt(`Anna luku ${i + 1}:`));
    numbers.push(number);
}

for (let i = numbers.length - 1; i >= 0; i--) {
    console.log(numbers[i]);
}