function isBudgeEnough(input) {
    let flowerType = input[0];
    let flowersCount = Number(input[1]);
    let budget = Number(input[2]);
    let flowersPrices = {
        "Roses": 5,
        "Dahlias": 3.80,
        "Tulips": 2.80,
        "Narcissus": 3,
        "Gladiolus": 2.50
    }
    let price = flowersCount * flowersPrices[flowerType];
    if (flowerType == "Roses" && flowersCount > 80) {
        price -= price * 0.10;
    } else if (flowerType == "Dahlias" && flowersCount > 90) {
        price -= price * 0.15;
    } else if (flowerType == "Tulips" && flowersCount > 80) {
        price -= price * 0.15;
    } else if (flowerType == "Narcissus" && flowersCount < 120) {
        price += price * 0.15;
    } else if (flowerType == "Gladiolus" && flowersCount < 80) {
        price += price * 0.20;
    }

    let diff = Math.abs(price - budget);
    if (price <= budget) {
        console.log(`Hey, you have a great garden with ${flowersCount} ${flowerType} and ${diff.toFixed(2)} leva left.`)
    } else {
        console.log(`Not enough money, you need ${diff.toFixed(2)} leva more.`)
    }
}
