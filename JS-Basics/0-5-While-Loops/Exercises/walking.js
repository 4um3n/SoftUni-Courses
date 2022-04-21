function walking(input) {
    let i = 0; let goal = 10000; let steps = 0;
    while (steps < goal || i < input.length) {
        let x = input[i];
        if (x == 'Going home') {
            steps += Number(input[i + 1]);
            if (steps < goal) {
                return `${Math.abs(steps - goal)} more steps to reach goal.`;
            }
            break;
        }
        steps += Number(x); i++;
    }
    return `Goal reached! Good job!\n${Math.abs(steps - goal)} steps over the goal!`;
}


console.log(walking(["1000",
"1500",
"2000",
"6500"]));
console.log(walking(["1500",
"3000",
"250",
"1548",
"2000",
"Going home",
"2000"]));
console.log(walking(["1500",
"300",
"2500",
"3000",
"Going home",
"200"]));
console.log(walking(["125",
"250",
"4000",
"30",
"2678",
"4682"]));