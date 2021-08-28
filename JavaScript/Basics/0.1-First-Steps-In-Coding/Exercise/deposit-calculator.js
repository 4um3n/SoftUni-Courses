function depositCalculator(input) {
    let depositedSum = Number(input[0]);
    let depositTerm = Number(input[1]);
    let interestRate = Number(input[2]);
    let result = depositedSum + (depositTerm * ((depositedSum * interestRate / 100) / 12));
    console.log(result.toFixed(2));
}

depositCalculator(["200", "3", "5.7"]);
depositCalculator(["2350", "6", "7"]);
