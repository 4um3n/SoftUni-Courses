function diagonalAttack(initialField) {
    function fieldToString(field) {
        return field.map(row => row.join(' ')).join('\n');
    }

    function haveEqualSums(field, sum, leftDiagonal, rightDiagonal) {
        for (let r = 0; r < field.length; r++) {
            for (let c = 0; c < field[r].length; c++) {
                const point = [r, c].toString();
                if (!leftDiagonal.includes(point) && !rightDiagonal.includes(point)) {
                    field[r][c] = sum;
                }
            }
        }

        return field;
    }

    function getField(field) {
        const fieldOfNumbers = field.map(row => row.split(' ').map(x => Number(x)));

        const leftDiagonal = [];
        const rightDiagonal = [];
        let leftDiagonalSum = 0;
        let rightDiagonalSum = 0;
        let leftPoint;
        let rightPoint;

        const pointInDiagonal = {
            'left': r => fieldOfNumbers[r][r],
            'right': r => fieldOfNumbers[r][fieldOfNumbers[r].length - 1 - r],
        }

        for (let r = 0; r < fieldOfNumbers.length; r++) {
            leftPoint = [r, r].toString();
            rightPoint = [r, fieldOfNumbers[r].length - 1 - r].toString();
            leftDiagonal.push(leftPoint);
            rightDiagonal.push(rightPoint);
            leftDiagonalSum += pointInDiagonal['left'](r);
            rightDiagonalSum += pointInDiagonal['right'](r);
        }

        if (leftDiagonalSum === rightDiagonalSum) {
            return fieldToString(haveEqualSums(
                fieldOfNumbers,
                leftDiagonalSum,
                leftDiagonal,
                rightDiagonal
            ));
        }

        return fieldToString(fieldOfNumbers);
    }

    console.log(getField(initialField));
}


diagonalAttack([
    '5 3 12 3 1',
    '11 4 23 2 5',
    '101 12 3 21 10',
    '1 4 5 2 2',
    '5 22 33 11 1'
]);

diagonalAttack([
    '1 1 1',
    '1 1 1',
    '1 1 0'
]);
