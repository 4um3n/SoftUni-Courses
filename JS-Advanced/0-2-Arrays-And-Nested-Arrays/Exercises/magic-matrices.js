function isMatrixMagic(matrix) {
    let rowsSums = [];
    let columnsSums = [];

    for (let r = 0; r < matrix.length; r++) {
        rowsSums.push(matrix[r].reduce((a, b) => a + b));
    }

    for (let c = 0; c < matrix[0].length; c++) {
        let currentColumn = [];

        for (let r = 0; r < matrix.length; r++) {
            currentColumn.push(matrix[r][c]);
        }

        columnsSums.push(currentColumn.reduce((a, b) => a + b));
    }

    const requiredSum = rowsSums[0];
    const isMagic = rowsSums.every(x => x === requiredSum) && columnsSums.every(x => x === requiredSum);
    console.log(isMagic);
}


isMatrixMagic([
    [4, 5, 6],
    [6, 5, 4],
    [5, 5, 5]
]);
isMatrixMagic([
    [11, 32, 45],
    [21, 0, 1],
    [21, 1, 1]
]);
isMatrixMagic([
    [1, 0, 0],
    [0, 0, 1],
    [0, 1, 0]
]);