function sumOfDigits(input) {
    let number = input[0];
    let result = 0;
    for (i = 0; i < number.length; i++) {
        let digit = Number(number[i]);
        result += digit;
    }
    console.log(`The sum of the digits is:${result}`)
}

sumOfDigits(["1234"])
sumOfDigits(["564891"])