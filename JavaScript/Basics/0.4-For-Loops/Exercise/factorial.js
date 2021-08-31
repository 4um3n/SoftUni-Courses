function factorial(input) {
    let n = Number(input[0]);
    if (n < 2) {
        return 1;
    }

    n_factorial = n * factorial([`${n - 1}`]);
    return n_factorial;
}


console.log(factorial(["8"]));