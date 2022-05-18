function greatestCommonDivisor(a, b) {
    // let result;
    // for (let n = 1; n <= a && n <= b; n++) {
    //     if (a % n === 0 && b % n === 0) {
    //         result = n;
    //     }
    // }

    function getGCD(x, y) {
        if (x === 0) {
            return y;
        } else if (y === 0) {
            return x;
        }
        return getGCD(y, x % y);
    }

    const result = getGCD(a, b);
    console.log(result);
}

greatestCommonDivisor(2154, 458);
