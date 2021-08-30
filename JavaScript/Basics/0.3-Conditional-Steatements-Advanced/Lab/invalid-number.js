function isNumberInvalid(input) {
    let n = Number(input[0]);
    let theRange = [];
    for (let i = 100; i <= 200; i++) {
        theRange.push(i);
    }
    
    if (!theRange.includes(n) && n != 0) {
        console.log("invalid");
    } 
}

isNumberInvalid(["75"])
isNumberInvalid(["150"])
isNumberInvalid(["220"])
isNumberInvalid(["199"])
isNumberInvalid(["-1"])
isNumberInvalid(["100"])
isNumberInvalid(["200"])
isNumberInvalid(["0"])