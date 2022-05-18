function smallestTwoNumbers(numbers) {
    let firstMinNum = Math.min(...numbers);

    if (numbers.length === 1) {
        console.log(firstMinNum);
    } else {
        numbers = numbers.filter(n => n !== firstMinNum);
        const secondMinNum = (numbers.length > 0) ? Math.min(...numbers) : firstMinNum;
        console.log(`${firstMinNum} ${secondMinNum}`);
    }
}


smallestTwoNumbers([30, 15, 50, 5]);
smallestTwoNumbers([3, 0, 10, 4, 7, 3]);
smallestTwoNumbers([3]);
smallestTwoNumbers([3, 3]);
