function sumOfTwoNumbers(input) {
    let start = Number(input.shift());
    let end = Number(input.shift());
    let m = Number(input.shift()); let c = 0;
    for (let x = start; x <= end; x++) {
        for (let y = start; y <= end; y++) {
            c++;
            if (x + y == m) {
                return `Combination N:${c} (${x} + ${y} = ${m})`;
            }
        }
    }
    return `${c} combinations - neither equals ${m}`;
}


console.log(sumOfTwoNumbers(["1",
"10",
"5"]));
console.log(sumOfTwoNumbers(["23",
"24",
"20"]));