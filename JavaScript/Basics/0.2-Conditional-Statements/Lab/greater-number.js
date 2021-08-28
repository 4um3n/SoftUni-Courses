function graterNumber(input) {
    let a, b;
    a = Number(input[0]);
    b = Number(input[1]);
    if (a > b) {
        console.log(a);
    
    }
    else {
        console.log(b);
    }
}

graterNumber(["5", "3"]);
graterNumber(["3", "5"]);
graterNumber(["10", "10"]);
graterNumber(["-5", "5"]);