function specialNumber(input) {
    let n = Number(input[0]);
    let specialNumbers = [];
    for (let num = 1111; num <= 9999; num++) {
        num = `${num}`; isSpecial = true;
        for (i = 0; i < num.length; i++) {
            let x = Number(num[i]);
            if (!(n % x == 0)) {isSpecial = false; break;}
        }
        if (isSpecial) {specialNumbers.push(num);}
    }
    return specialNumbers.join(' ');
}


console.log(specialNumber(["3"]));
console.log(specialNumber(["11"]));
console.log(specialNumber(["16"]));