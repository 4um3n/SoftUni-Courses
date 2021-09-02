function traveling(input) {
    while (input[0] != "End") {
        let destination = input.shift();
        let neededMoney = Number(input.shift()); let money = 0;
        while (money < neededMoney) {money += Number(input.shift());}
        console.log(`Going to ${destination}!`);
    }
}


traveling(["Greece",
"1000",
"200",
"200",
"300",
"100",
"150",
"240",
"Spain",
"1200",
"300",
"500",
"193",
"423",
"End"]);
traveling(["France",
"2000",
"300",
"300",
"200",
"400",
"190",
"258",
"360",
"Portugal",
"1450",
"400",
"400",
"200",
"300",
"300",
"Egypt",
"1900",
"1000",
"280",
"300",
"500",
"End"]);

