function even(numbers) {
    const result = [];

    for (const number of numbers) {
        if (number % 2 === 0) {
            result.push(number);
        }
    }

    return result;
}

const numbers = [2, 7, 4, 9, 12, 3];
const evenNumbers = even(numbers);

console.log("Alkuperäinen taulukko:", numbers);
console.log("Parilliset luvut:", evenNumbers);