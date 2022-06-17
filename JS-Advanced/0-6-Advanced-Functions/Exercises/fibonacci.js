function getFibonator() {
    let n = 0;
    let n1 = 1;

    function fib() {
        const temp = n1;
        n1 += n;
        n = temp;
        return temp;
    }

    return fib;
}


let fib = getFibonator();
console.log(fib()); // 1
console.log(fib()); // 1
console.log(fib()); // 2
console.log(fib()); // 3
console.log(fib()); // 5
console.log(fib()); // 8
console.log(fib()); // 13