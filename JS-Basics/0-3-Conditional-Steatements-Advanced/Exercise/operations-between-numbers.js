function calculator(input) {
    let n1 = Number(input[0]);
    let n2 = Number(input[1]);
    let operator = input[2];
    let result;
    if (operator == "+") {
        result = n1 + n2;
    } else if (operator == "-") {
        result = n1 - n2;
    } else if (operator == "*") {
        result = n1 * n2;
    } else if (operator == "/") {
        if (n2 == 0) {
            console.log(`Cannot divide ${n1} by zero`);
            return;
        } else {
            result = n1 / n2;
            console.log(`${n1} / ${n2} = ${result.toFixed(2)}`);
            return;
        }
    } else if (operator == "%") {
        if (n2 == 0) {
            console.log(`Cannot divide ${n1} by zero`);
            return;
        } else {
            result = n1 % n2;
            console.log(`${n1} % ${n2} = ${result}`);
            return;
        }
    }

    let numType;
    if (result % 2 == 0) {
        numType = "even";
    } else {
        numType = "odd";
    }
    console.log(`${n1} ${operator} ${n2} = ${result} - ${numType}`)
}