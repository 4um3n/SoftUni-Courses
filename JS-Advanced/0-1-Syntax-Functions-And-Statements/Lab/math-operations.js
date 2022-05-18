function calculate (a, b, operator) {
    const operationsMapper = {
        '+': (a, b) => a + b,
        '-': (a, b) => a - b,
        '*': (a, b) => a * b,
        '/': (a, b) => a / b,
        '%': (a, b) => a % b,
        '**': (a, b) => a ** b,
    };

    console.log(operationsMapper[operator](a, b));
}
