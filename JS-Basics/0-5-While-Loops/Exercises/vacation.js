function isVacationPossible(input) {
    let neededMoney = Number(input.shift());
    let currentMoney = Number(input.shift())
    let totalDays = 0; let spendDays = 0; let i = 0;
    while (currentMoney < neededMoney) {
        let command = input[i]; let money = Number(input[i + 1]);
        if (command == "spend") {
            if (money > currentMoney) {money = currentMoney;}
            currentMoney -= money;
            spendDays++; totalDays++; i += 2;
            if (spendDays == 5 || i == input.length) {
                return `You can't save the money.\n${totalDays}`;
            }
            continue;
        }
        spendDays = 0;
        currentMoney += money; i += 2; totalDays++;
    }
    return `You saved the money for ${totalDays} days.`;
}


console.log(isVacationPossible(["2000",
"1000",
"spend",
"1200",
"save",
"2000"]));
console.log(isVacationPossible(["110",
"60",
"spend",
"10",
"spend",
"10",
"spend",
"10",
"spend",
"10",
"spend",
"10"]));