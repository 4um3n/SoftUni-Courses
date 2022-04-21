function histogram(input) {
    let numbers = input.map(Number);
    let n = numbers.shift();
    let p1, p2, p3, p4, p5;
    [p1, p2, p3, p4, p5] = [0, 0, 0, 0 ,0];
    for (let i = 0; i < n; i++) {
        if (numbers[i] < 200) {
            p1 +=1;
        } else if (numbers[i] < 400) {
            p2 += 1;
        } else if (numbers[i] < 600) {
            p3 += 1;
        } else if (numbers[i] < 800) {
            p4 += 1;
        } else if (numbers[i] >= 800) {
            p5 +=1;
        }
    }

    p1 = p1 / n * 100;
    p2 = p2 / n * 100;
    p3 = p3 / n * 100;
    p4 = p4 / n * 100;
    p5 = p5 / n * 100;
    numbers = [p1, p2, p3, p4, p5];
    for (i = 0; i < numbers.length; i++) {
        console.log(`${numbers[i].toFixed(2)}%`);
    }
}


histogram(["3", "1", "2", "999"])
histogram(["7", "800", "801", "250", "199", "399", "599", "799"])
histogram(["9", "367", "99", "200", "799", "999", "333", "555", "111", "9"])
histogram(["14", "53", "7", "56", "180", "450", "920", "12", "7", "150", "250", "680", "2", "600", "200"])
