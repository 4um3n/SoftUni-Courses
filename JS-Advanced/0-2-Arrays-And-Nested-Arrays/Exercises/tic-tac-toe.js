function ticTacToe(moves) {
    function getField() {
        let field = [];
        for (let _ = 0; _ < 3; _++) {
            field.push([false, false, false]);
        }
        return field;
    }

    function checkLine(line, player) {
        return line.every(x => x === player);
    }

    function checkRowsAndColumns(field, player) {
        for (let c = 0; c < field[0].length; c++) {
            const currentColumn = [];

            for (let r = 0; r < field.length; r++) {
                if (checkLine(field[r], player)) {
                    return true;
                }
                currentColumn.push(field[r][c]);
            }

            if (checkLine(currentColumn, player)) {
                return true;
            }
        }

        return false;
    }

    function checkDiagonals(field, player) {
        const diagonal1 = [];
        const diagonal2 = [];

        for (let r = 0; r < field.length; r++) {
            diagonal1.push(field[r][r]);
            diagonal2.push(field[r][field.length - 1 - r]);
        }

        return !!(checkLine(diagonal1, player) || checkLine(diagonal2, player));
    }

    function winner(field, player) {
        return !!(checkRowsAndColumns(field, player) || checkDiagonals(field, player));
    }

    function emptySpaces(field) {
        for (let r = 0; r < field.length; r++) {
            for (let c = 0; c < field[r].length; c++) {
                if (!field[r][c]) {
                    return true;
                }
            }
        }
        return false;
    }

    function getResult(text, field) {
        const fieldToString = field.map(row => row.join('\t')).join('\n')
        return `${text}\n${fieldToString}`
    }

    function play(field, moves, player = 'X') {
        for (const move of moves) {
            const [r, c] = move.split(' ').map(x => Number(x));

            if (field[r][c]) {
                console.log('This place is already taken. Please choose another!');
                continue;
            }

            field[r][c] = player;

            if (winner(field, player)) {
                console.log(getResult(
                    `Player ${player} wins!`,
                    field
                ));
                return;
            }

            if (!emptySpaces(field)) {
                break;
            }

            player = (player === 'O') ? 'X' : 'O';
        }

        console.log(getResult(
            'The game ended! Nobody wins :(',
            field
        ));
    }

    play(getField(), moves);
}


ticTacToe([
    "0 1",
    "0 0",
    "0 2",
    "2 0",
    "1 0",
    "1 1",
    "1 2",
    "2 2",
    "2 1",
    "0 0"
]);
ticTacToe([
    "0 0",
    "0 0",
    "1 1",
    "0 1",
    "1 2",
    "0 2",
    "2 2",
    "1 2",
    "2 2",
    "2 1"
]);
ticTacToe([
    "0 1",
    "0 0",
    "0 2",
    "2 0",
    "1 0",
    "1 2",
    "1 1",
    "2 1",
    "2 2",
    "0 0"
]);
