function biggerHalf (numbers) {
    numbers = numbers.sort((a, b) => a - b);
    let middle = (numbers.length / 2).toFixed(0);

    if (numbers.length % 2 === 1) {
        middle--;
    }

    return numbers.slice(middle);
}

console.log(biggerHalf([4, 7, 2, 5]));
console.log(biggerHalf([3, 19, 14, 7, 2, 19, 6]));
