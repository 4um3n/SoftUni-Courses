function sameNumbers (number) {
    function areSame (arrayFromElements) {
        // Put all array elements in a HashSet
        const set = new Set(arrayFromElements);
        // If all elements are same, size of
        // HashSet should be 1. As HashSet contains only distinct values.
        return (set.size === 1);
    }

    let result;
    const digitsArray = Array.from(number.toString()).map((x) => Number(x));

    if (areSame(digitsArray)) {
        result = 'true\n';
    } else {
        result = 'false\n';
    }

    result += `${digitsArray.reduce((a, b) => a + b)}`;
    console.log(result);
}

sameNumbers(2222222);
sameNumbers(1234);
