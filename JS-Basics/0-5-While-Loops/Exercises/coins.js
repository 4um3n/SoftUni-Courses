function minCoins(input) {
    let coins = (Number(input[0]) * 100).toFixed(0); let coinsCount = 0;
    while (coins > 0) {
        if (coins >= 200) {coins -= 200;}
        else if (coins >= 100) {coins -= 100;}
        else if (coins >= 50) {coins -= 50;}
        else if (coins >= 20) {coins -= 20;}
        else if (coins >= 10) {coins -= 10;}
        else if (coins >= 5) {coins -= 5;}
        else if (coins >= 2) {coins -= 2;}
        else if (coins >= 1) {coins -= 1;}
        coinsCount++;
    }
    return coinsCount;
}


console.log(minCoins(["1.23"]));
console.log(minCoins(["2"]));
console.log(minCoins(["0.57"]));
console.log(minCoins(["1.51"]));
console.log(minCoins(["2.73"]));