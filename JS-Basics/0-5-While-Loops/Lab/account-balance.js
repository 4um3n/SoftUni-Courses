function accountBalance(input) {
    let i = 0; let balance = 0;
    while (input[i] != "NoMoreMoney") {
        n = Number(input[i]);
        if (n < 0) {
            console.log("Invalid operation!")
            return `Total: ${balance.toFixed(2)}`;
        }
        console.log(`Increase: ${n.toFixed(2)}`)
        balance += n; i++;
    }
    return `Total: ${balance.toFixed(2)}`;
}


console.log(accountBalance(["5.51",
"69.42",
"100",
"NoMoreMoney"]));
console.log(accountBalance(["120",
"45.55",
"-150"]));