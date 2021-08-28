function budgetCalculator(input) {
    let hallPrice = Number(input[0]);
    let cakePrice = hallPrice * 0.20;
    let drinksPrice = cakePrice - cakePrice * 0.45;
    let animatorPrice = hallPrice / 3;
    hallPrice += cakePrice + drinksPrice + animatorPrice;
    console.log(hallPrice);   
}

budgetCalculator(["2250"]);
budgetCalculator(["3720"]);
