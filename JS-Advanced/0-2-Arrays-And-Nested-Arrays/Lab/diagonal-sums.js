function diagonalSums (matrix) {
    let diagonal1 = [];
    let diagonal2 = [];

    for (let r = 0; r < matrix.length; r++) {
        diagonal1.push(matrix[r][r]);
        diagonal2.push(matrix[r][matrix[r].length - 1 - r]);
    }

    const results = [
        diagonal1.reduce((a, b) => a + b),
        diagonal2.reduce((a, b) => a + b),
    ];

    console.log(results.join(' '));
}


diagonalSums([
    [20, 40],
    [10, 60],
]);
diagonalSums([
    [3, 5, 17],
    [-1, 7, 14],
    [1, -8, 89],
]);
