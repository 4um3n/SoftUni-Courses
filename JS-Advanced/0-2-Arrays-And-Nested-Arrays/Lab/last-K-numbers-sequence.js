function weirdFibonacci (sequenceLength, k) {
    let sequence = (sequenceLength > 0) ? [1] : [];
    let i = 0;

    while (sequence.length < sequenceLength) {
        const tmpSequence = sequence.slice(i, i + k);
        sequence.push(tmpSequence.reduce((a, b) => a + b));
        if (sequence.length > k) {i++;}
    }

    return sequence;
}


console.log(weirdFibonacci(6, 3));
console.log(weirdFibonacci(8, 2));
