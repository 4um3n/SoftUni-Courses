function biggestElement (matrix) {
    let rowsBiggestElements = [];

    for (let row of matrix) {
        rowsBiggestElements.push(Math.max(...row));
    }

    return Math.max(...rowsBiggestElements);
}


console.log(biggestElement(
    [
        [20, 50, 10],
        [8, 33, 145],
    ]
));
console.log(biggestElement(
    [
        [3, 5, 7, 12],
        [-1, 4, 33, 2],
        [8, 3, 0, 4],
    ]
));