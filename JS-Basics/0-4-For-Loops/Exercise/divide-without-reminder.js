function divideWithoutReminder(input) {
    let numbers = input.map(Number);
    let n = numbers.shift();
    let p1, p2, p3;
    [p1, p2, p3] = [0, 0, 0];
    for (let i = 0; i < n; i++) {
        if (numbers[i] % 2 == 0) {
            p1 += 1;
        } 
        
        if (numbers[i] % 3 == 0) {
            p2 += 1;
        }

        if (numbers[i] % 4 == 0) {
            p3 += 1;
        }
    }
    p1 = p1 / n * 100;
    p2 = p2 / n * 100;
    p3 = p3 / n * 100;
    numbers = [p1, p2, p3];
    for (i = 0; i < 3; i++) {
        console.log(`${numbers[i].toFixed(2)}%`)
    }
}


divideWithoutReminder((["10", "680", "2", "600", "200", "800", "799", "199", "46", "128", "65"]));
