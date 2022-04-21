function billCalculator(input) {
    let strawberriesPrice = Number(input[0]);
    let bananasCount = Number(input[1]);
    let orangesCount = Number(input[2]);
    let raspberriesCount = Number(input[3]);
    let strawberriesCount = Number(input[4]);
    let raspberriesPrice = strawberriesPrice / 2;
    let orangesPrice = orangesCount * (raspberriesPrice - raspberriesPrice * 0.40);
    let bananasPrice = bananasCount * (raspberriesPrice - raspberriesPrice * 0.80);
    raspberriesPrice *= raspberriesCount;
    strawberriesPrice *= strawberriesCount;
    let result = raspberriesPrice + strawberriesPrice + orangesPrice + bananasPrice;
    console.log(result);
}

billCalculator(["48", "10", "3.3", "6.5", "1.7"])
billCalculator(["63.5", "3.57", "6.35", "8.15", "2.5"])