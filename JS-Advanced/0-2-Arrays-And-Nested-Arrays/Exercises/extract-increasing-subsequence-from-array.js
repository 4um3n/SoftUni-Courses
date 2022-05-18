function extractIncreasingSubsecuence(numbers) {
    let max = (numbers.length > 0) ? numbers[0] : 0;

    numbers = numbers.filter(function (x) {
        if (x >= max) {
            max = x;
            return true;
        }
        return false;
    });

    return numbers;
}


console.log(extractIncreasingSubsecuence([1, 3, 8, 4, 10, 12, 3, 2, 24]));
console.log(extractIncreasingSubsecuence([1, 2, 3, 4]));
console.log(extractIncreasingSubsecuence([20, 3, 2, 15, 6, 1]));
