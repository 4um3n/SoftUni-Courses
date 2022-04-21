function isBudgetEnough(input) {
    let budget = Number(input[0]);
    let statistsCount = Number(input[1]);
    let clothesPrice = Number(input[2]);
    let decorPrice = budget * 0.10;
    clothesPrice *= statistsCount;
    if (statistsCount > 150) {
        clothesPrice -= clothesPrice * 0.10;
    }

    diff = Math.abs(budget - (clothesPrice + decorPrice));
    if (clothesPrice + decorPrice > budget) {
        console.log(`Not enough money!\nWingard needs ${diff.toFixed(2)} leva more.`);
    } else {
        console.log(`Action!\nWingard starts filming with ${diff.toFixed(2)} leva left.`);
    }
}

isBudgetEnough(["20000", "120", "55.5"]);
isBudgetEnough(["15437.62", "186", "57.99"]);
isBudgetEnough(["9587.88", "222", "55.68"]);
