function minNumber(input) {
    let numbers = input.map(Number);
    let n = numbers.shift();
    let minN = 999999999;
    for (let i = 0; i < n; i++) {
        if (numbers[i] < minN) {
            minN = numbers[i];
        }
    }
    console.log(minN);
}


minNumber(["3", "-10", "20", "-30"])