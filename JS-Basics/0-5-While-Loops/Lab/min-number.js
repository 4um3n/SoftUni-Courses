function minNumber(input) {
    let i = 0; let min = 9999999999;
    while (input[i] != "Stop") {
        n = Number(input[i]); 
        if (n < min) {
            min = n;
        }
        i++
    }
    return min;
}
