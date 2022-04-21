function sumNumbers(input) {
    let x = Number(input.shift()); let i = 0; let result = 0;
    while (result < x) {
        result += Number(input[i]); i++;
    }
    console.log(result)
}


sumNumbers(["100",
"10",
"20",
"30",
"40"]);
sumNumbers(["20",
"1",
"2",
"3",
"4",
"5",
"6"]);