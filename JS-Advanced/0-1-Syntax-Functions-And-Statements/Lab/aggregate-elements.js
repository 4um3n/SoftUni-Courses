function aggregateElements (numbers) {
    function sumNumbers (numbers) {
        return numbers.reduce((a, b) => a + b);
    }

    function sumInverseNumbers (numbers) {
        const inverseNumbers = numbers.map(x => 1 / x);
        return sumNumbers(inverseNumbers);
    }

    function concatenateNumbers (numbers) {
        const numbersToString = numbers.map(x => x.toString());
        return numbersToString.join('');
    }

    console.log(sumNumbers(numbers));
    console.log(sumInverseNumbers(numbers));
    console.log(concatenateNumbers(numbers));
}

aggregateElements([2, 4, 8, 16]);
