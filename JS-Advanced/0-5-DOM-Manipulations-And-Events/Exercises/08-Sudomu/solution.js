function solve() {
    const buttons = document.querySelectorAll('button');
    const resultDiv = document.querySelector('div[id=check] p');
    const table = document.querySelector('table');
    const inputFieldsBoard = Array.from(document.querySelectorAll('tbody tr')).map(
        row => Array.from(row.children).map(el => el.children[0])
    );

    function checkLine(line) {
        const passingRow = [1, 2, 3].join('');
        return [...line].sort((a, b) => a - b).join('') === passingRow;
    }

    function checkBoard(board) {
        for (let c = 0; c < board[0].length; c++) {
            const currentColumn = [];

            for (let r = 0; r < board.length; r++) {
                if (!checkLine(board[r])) {
                    return false;
                }
                currentColumn.push(board[r][c]);
            }

            if (!checkLine(currentColumn)) {
                return false;
            }
        }

        return true;
    }

    function isSolved(event) {
        const board = inputFieldsBoard.map(arr => arr.map(el => Number(el.value)));

        if (checkBoard(board)) {
            table.style.border = '2px solid green';
            resultDiv.textContent = 'You solve it! Congratulations!';
            resultDiv.style.color = 'green';
        } else {
            table.style.border = '2px solid red';
            resultDiv.textContent = 'NOP! You are not done yet...';
            resultDiv.style.color = 'red';
        }
    }

    function clear(event) {
        table.style.border = 'none';
        resultDiv.textContent = '';
        inputFieldsBoard.flat().forEach(el => el.value = '');
    }

    buttons[0].addEventListener('click', isSolved);
    buttons[1].addEventListener('click', clear);
}
