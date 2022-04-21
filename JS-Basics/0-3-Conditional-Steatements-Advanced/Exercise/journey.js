function journey(input) {
    let budget = Number(input[0]);
    let season = input[1];
    let destination, shelterType, spendMoney;

    if (budget <= 100) {
        destination = "Bulgaria";
        if (season == "summer") {
            shelterType = "Camp";
            spendMoney = budget * 0.30;
        } else if (season == "winter") {
            shelterType = "Hotel";
            spendMoney = budget * 0.70;
        }
    } else if (budget <= 1000) {
        destination = "Balkans";
        if (season == "summer") {
            shelterType = "Camp";
            spendMoney = budget * 0.40;
        } else if (season == "winter") {
            shelterType = "Hotel";
            spendMoney = budget * 0.80;
        }
    } else if (budget > 1000) {
        destination = "Europe";
        shelterType = "Hotel";
        spendMoney = budget * 0.90;
    }

    console.log(`Somewhere in ${destination}\n${shelterType} - ${spendMoney.toFixed(2)}`);

}
