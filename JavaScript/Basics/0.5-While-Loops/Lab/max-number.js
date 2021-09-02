function maxNumber(input) {
    let i = 0; let max = -9999999999;
    while (input[i] != "Stop") {
        n = Number(input[i]); 
        if (n > max) {
            max = n;
        }
        i++
    }
    return max;
}
