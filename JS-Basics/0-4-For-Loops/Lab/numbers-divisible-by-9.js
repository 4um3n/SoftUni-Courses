function divisibleByNine(input) {
    let a = Number(input[0]);
    let b = Number(input[1]);
    let result = [];
    for (i = a; i <= b; i++) {
        if (i % 9 == 0) {
            result.push(i)
        }
    }
    let newResult = 0;
    result.forEach(number => {newResult += number});
    console.log(`The sum: ${newResult}`);
    result.forEach(number => {console.log(number)})
}

divisibleByNine(["100", "200"])