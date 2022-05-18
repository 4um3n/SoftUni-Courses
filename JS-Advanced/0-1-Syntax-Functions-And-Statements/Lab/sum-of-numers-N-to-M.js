function sumOfNumbersInRange(start, end) {
    const startNum = Number(start);
    const endNum = Number(end);

    let result = 0;
    for (let n = startNum; n <= endNum; n++) {
        result += n;
    }

    console.log(result);
}

sumOfNumbersInRange('-8', '20');
