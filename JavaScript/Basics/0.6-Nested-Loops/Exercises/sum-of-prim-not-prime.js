function primesAndNonPrimes(input) {
    let primes = 0; let nonPrimes = 0;
    while (input[0] != "stop") {
        n = Number(input.shift());
        if (n < 0) {
            console.log("Number is negative."); continue;
        }
        let isPrime = false;
        if (n >= 2) {isPrime = true;}
        for (let x = 2; x < n; x++) {
            if (n % x == 0) {
                isPrime = false; break;
            }
        }
        if (isPrime) {primes += n;}
        else {nonPrimes += n;}
    }
    console.log(`Sum of all prime numbers is: ${primes}`);
    console.log(`Sum of all non prime numbers is: ${nonPrimes}`);
}

primesAndNonPrimes(["3",
"9",
"0",
"7",
"19",
"4",
"stop"]);
primesAndNonPrimes(["30",
"83",
"33",
"-1",
"20",
"stop"]);