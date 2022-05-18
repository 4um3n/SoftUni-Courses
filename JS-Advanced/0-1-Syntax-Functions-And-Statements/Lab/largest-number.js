function largestNumber (num1, num2, num3) {
    const result = Math.max.apply(Math, arguments);
    console.log(`The largest number is ${result}.`);
}

largestNumber(-2, -5, -10);
