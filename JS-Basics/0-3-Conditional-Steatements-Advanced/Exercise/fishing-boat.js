function isBudgetEnough(input) {
    let budget = Number(input[0]);
    let season = input[1];
    let fishermanCount = Number(input[2]);
    let price = 0;
    if (season == "Spring") {
        price = 3000;
        if (fishermanCount <= 6) {
            price -= price * 0.10;
        } else if (fishermanCount <= 11) {
            price -= price * 0.15;
        } else if (fishermanCount > 11) {
            price -= price * 0.25;
        }
    } else if (season == "Summer" || season == "Autumn") {
        price = 4200;
        if (fishermanCount <= 6) {
            price -= price * 0.10;
        } else if (fishermanCount <= 11) {
            price -= price * 0.15;
        } else if (fishermanCount > 11) {
            price -= price * 0.25;
        }
    } else if (season == "Winter") {
        price = 2600;
        if (fishermanCount <= 6) {
            price -= price * 0.10;
        } else if (fishermanCount <= 11) {
            price -= price * 0.15;
        } else if (fishermanCount > 11) {
            price -= price * 0.25;
        }
    }

    if (season != "Autumn" && fishermanCount % 2 == 0) {
        price -= price * 0.05;
    }
    
    let diff = Math.abs(price - budget);
    if (price <= budget) {
        console.log(`Yes! You have ${diff.toFixed(2)} leva left.`);
    } else {
        console.log(`Not enough money! You need ${diff.toFixed(2)} leva.`);
    }
}

isBudgetEnough(["2000", "Winter", "13"])
