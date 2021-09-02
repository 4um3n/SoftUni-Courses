function numberPyramid(input) {
    let n = Number(input[0]); let i = 0;
    for (let r = 1; r <= n; r++) {
        let numbers = [];
        for (let c = 1; c <= r; c++) {
            i ++; numbers.push(`${i}`);
            if (i + 1 > n) {break;}
        }
        console.log(numbers.join(' '));
        if (i + 1 > n) {break;}
    }
}


numberPyramid(["7"]);
numberPyramid(["15"]);
numberPyramid(["12"]);