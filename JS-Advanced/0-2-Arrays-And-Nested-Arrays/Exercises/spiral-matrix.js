function spiralMatrix(maxR, maxC) {
    function setUpField() {
        let field = [];

        for (let r = 0; r < maxR; r++) {
            let line = [];
            for (let c = 0; c < maxC; c++) {
                line.push(false);
            }
            field.push(line);
        }

        return field;
    }

    function matrixToString(matrix) {
        return matrix.map(row => row.join(' ')).join('\n');
    }

    function getMoves() {
        return {
            'right': (r, c) => [r, c + 1],
            'down': (r, c) => [r + 1, c],
            'left': (r, c) => [r, c - 1],
            'up': (r, c) => [r - 1, c],
        };
    }

    function possibleMoves(totalMoves) {
        return totalMoves < maxR * maxC
    }

    function validPoint(r, c, matrix) {
        return 0 <= r && r < matrix.length && 0 <= c && c < matrix[r].length && !matrix[r][c]
    }

    function getMatrix(matrix) {
        const moves = getMoves();
        const movesQueue = Array.from(Object.keys(moves));
        let move = movesQueue.shift();
        let n = 1;
        let totalMoves = 0;
        let r = 0; let c = 0;
        let lastR = r; let lastC = c;

        while (possibleMoves(totalMoves)) {
            if (!validPoint(r, c, matrix)) {
                movesQueue.push(move);
                move = movesQueue.shift();
                [r, c] = [lastR, lastC];
                totalMoves--; n--;
            }

            matrix[r][c] = n; n++;
            [lastR, lastC] = [r, c];
            [r, c] = moves[move](r, c);
            totalMoves++;
        }

        return matrixToString(matrix);
    }

    console.log(getMatrix(setUpField()))
}


spiralMatrix(9, 9);
