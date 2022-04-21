function isNumInRange(input) {
    let n = Number(input[0]);
    let theRange = [];
    for (let i = -100; i < 101; i++) {
        theRange.push(i);
    }

    if (theRange.includes(n) && n != 0) {
        console.log("Yes");
    } else {
        console.log("No");
    }
}



isNumInRange(["-25"])
isNumInRange(["0"])
isNumInRange(["25"])