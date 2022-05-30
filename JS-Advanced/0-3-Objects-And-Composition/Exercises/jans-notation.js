function solveJansNotation(data) {
    const operandsStack = [];
    const operatorsMapper = {
        '+': (x, y) => x + y,
        '-': (x, y) => x - y,
        '*': (x, y) => x * y,
        '/': (x, y) => x / y,
    };

    while (0 < data.length) {
        const operator = data.shift();

        if (!isNaN(Number(operator))) {
            operandsStack.push(Number(operator));
            continue;
        }

        if (operandsStack.length < 2) {
            return 'Error: not enough operands!'
        }

        const n = operatorsMapper[operator](
            operandsStack[operandsStack.length - 2],
            operandsStack[operandsStack.length - 1]
        );
        operandsStack.splice(-2, 2, n);
    }

    if (operandsStack.length === 1) {
        return operandsStack[0];
    }

    return 'Error: too many operands!'
}