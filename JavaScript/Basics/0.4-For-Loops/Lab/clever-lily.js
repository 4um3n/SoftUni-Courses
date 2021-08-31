function cleverLily(input) {
    let years = Number(input[0]);
    let washingMachinePrice = Number(input[1]);
    let toyPrice = Number(input[2]);
    let toysCount = 0;
    let totalMoney = 0;
    let money = 0;
    for (i = 1; i <= years; i++) {
        if (i % 2 == 1) {
            toysCount += 1;
        } else {
            money += 10;
            totalMoney += money;
            totalMoney -= 1;
        }
    }
    totalMoney += toysCount * toyPrice;
    let diff = Math.abs(totalMoney - washingMachinePrice);
    if (totalMoney >= washingMachinePrice) {
        console.log(`Yes! ${diff.toFixed(2)}`)
    } else {
        console.log(`No! ${diff.toFixed(2)}`)
    }
}

cleverLily(["10", "170", "6"])
cleverLily(["21", "1570.98", "3"])