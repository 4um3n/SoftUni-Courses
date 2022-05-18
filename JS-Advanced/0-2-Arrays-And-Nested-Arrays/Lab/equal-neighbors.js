function equalNeighbors(matrix) {
    let matched = [];

    function pointInRange(r, c) {
        return 0 <= r && r < matrix.length && 0 <= c && c < matrix[0].length;
    }

    function isMatched(points) {
        for (let match of matched) {
            if (match.toString() === points.toString()) {
                return true;
            }
        }
        return false;
    }

    function comparePoints(r, c, r1, c1) {
        if (pointInRange(r, c) && pointInRange(r1, c1) && !isMatched([r, c, r1, c1]) && !isMatched([r1, c1, r, c])) {
            return matrix[r][c] === matrix[r1][c1];
        }
        return false;
    }

    function getTotalMatches() {
        let totalMathces = 0;
        const movesMapper = [
            (r, c) => [r, c - 1],
            (r, c) => [r, c + 1],
            (r, c) => [r - 1, c],
            (r, c) => [r + 1, c],
        ];

        for (let row = 0; row < matrix.length; row++) {
            for (let col = 0; col < matrix[row].length; col++) {
                for (let move of movesMapper) {
                    let [row1, col1] = move(row, col);
                    if (comparePoints(row, col, row1, col1)) {
                        totalMathces++;
                        matched.push([row, col, row1, col1]);
                    }
                }
            }
        }
        return totalMathces;
    }

    return getTotalMatches();
}


console.log(equalNeighbors([
    ['2', '3', '4', '7', '0'],
    ['4', '0', '5', '3', '4'],
    ['2', '3', '5', '4', '2'],
    ['9', '8', '7', '5', '4']
]));

console.log(equalNeighbors([
    ['test', 'yes', 'yo', 'ho'],
    ['well', 'done', 'yo', '6'],
    ['not', 'done', 'yet', '5']
]));
