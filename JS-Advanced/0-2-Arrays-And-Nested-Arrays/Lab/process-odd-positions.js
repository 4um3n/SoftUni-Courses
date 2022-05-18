function processOddPositions (numbers) {
    let oddPositionNumbers = [];

    while (numbers.length > 0) {
        numbers.shift();
        oddPositionNumbers.push(numbers.shift());
    }

    oddPositionNumbers = oddPositionNumbers.map(x => x * 2);
    return oddPositionNumbers.reverse();
}


console.log(processOddPositions([10, 15, 20, 25]));
console.log(processOddPositions([3, 0, 10, 4, 7, 3]));
