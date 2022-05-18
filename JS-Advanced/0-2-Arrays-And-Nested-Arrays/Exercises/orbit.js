function orbit(data) {
    function setUpField(maxR, maxC) {
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

    function fieldToString(field) {
        return field.map(row => row.join(' ')).join('\n');
    }

    function getOrbit(field, initialR, initialC, n = 1) {
        for (let r = 0; r < field.length; r++) {
            for (let c = 0; c < field[r].length; c++) {
                const distance = Math.max(...[
                    Math.abs(r - initialR),
                    Math.abs(c - initialC),
                ]);

                field[r][c] = distance + n;
            }
        }

        return fieldToString(field);
    }

    console.log(getOrbit(setUpField(...data), data[2], data[3]));
}


orbit([4, 4, 0, 0]);
orbit([5, 5, 2, 2]);
orbit([3, 3, 2, 2]);
orbit([9, 9, 4, 8]);
