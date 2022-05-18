function negativePositiveNumbers (numbers) {
    let sortedNumbers = [];

    while (numbers.length > 0) {
        const n = numbers.shift();
        (n < 0) ? sortedNumbers.unshift(n) : sortedNumbers.push(n);
    }

    console.log(sortedNumbers.join('\n'));
}


negativePositiveNumbers([7, -2, 8, 9]);
negativePositiveNumbers([3, -2, 0, -1]);
