function tournament(input) {
    let daysCount = Number(input.shift());
    let totalWins = 0; let totalLoses = 0; 
    let money = 0; let currentMoney = 0; 
    for (let _ = 0; _ < daysCount; _++) {
        let wins = 0; let loses = 0; currentMoney = 0;
        while (input[0] != "Finish") {
            input.shift(); let result = input.shift();
            if (result == "win") {wins++; currentMoney += 20;}
            else if (result == "lose") {loses++;}
        }
        if (wins > loses) {
            totalWins++;
            money +=  currentMoney + currentMoney * 0.10;
        } else {totalLoses++; money += currentMoney}
        input.shift();
    }
    if (totalWins > totalLoses) {
        money += money * 0.20;
        return `You won the tournament! Total raised money: ${money.toFixed(2)}`;
    }
    return `You lost the tournament! Total raised money: ${money.toFixed(2)}`;
}


console.log(tournament(["2",
"volleyball",
"win",
"football",
"lose",
"basketball",
"win",
"Finish",
"golf",
"win",
"tennis",
"win",
"badminton",
"win",
"Finish"]));
console.log(tournament([
    "3",
    "darts",
    "lose",
    "handball",
    "lose",
    "judo",
    "win",
    "Finish",
    "snooker",
    "lose",
    "swimming",
    "lose",
    "squash",
    "lose",
    "table tennis",
    "win",
    "Finish",
    "volleyball",
    "win",
    "basketball",
    "win",
    "Finish"]));