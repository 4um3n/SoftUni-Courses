function birthdayCake(input) {
    let cakeArea = Number(input.shift()) * Number(input.shift());
    let i = 0; let eatenPieces = 0;
    while (input[i] != "STOP") {
        let n = Number(input[i]);
        cakeArea -= n; i++;
        if (cakeArea < 0) {
            return `No more cake left! You need ${Math.abs(cakeArea)} pieces more.`;
        }    
    }
    return `${cakeArea} pieces are left.`;
}


console.log(birthdayCake(["10",
"10",
"20",
"20",
"20",
"20",
"21"]));
console.log(birthdayCake(["10",
"2",
"2",
"4",
"6",
"STOP"]));