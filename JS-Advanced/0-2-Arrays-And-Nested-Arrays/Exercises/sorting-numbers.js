function sortingNumbers(numbers) {
    const sortedNumbers = [];
    const minMax = [
        nums => Math.min(...nums),
        nums => Math.max(...nums),
    ];

    while (numbers.length > 0) {
        const n = minMax[0](numbers);
        sortedNumbers.push(n);
        minMax.push(minMax.shift());
        numbers.splice(numbers.indexOf(n), 1);
    }

    return sortedNumbers;
}


console.log(sortingNumbers([1, 65, 3, 52, 48, 63, 31, -3, 18, 56]));
console.log(sortingNumbers([-3, 65, 1, 63, 3, 56, 18, 52, 31, 48]));