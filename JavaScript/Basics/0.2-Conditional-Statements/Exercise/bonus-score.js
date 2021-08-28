function bonus(input) {
    let n = Number(input[0]);
    let bonus;
    if (n <= 100) {
        bonus = 5;
    }
    else if (n <= 1000) {
        bonus = n * 0.20;
    }
    else {
        bonus = n * 0.10;
    }

    if (n % 2 == 0) {
        bonus += 1;
    }

    if (n % 10 == 5) {
        bonus += 2;
    }

    n += bonus;
    console.log(`${bonus}\n${n}`);
}

bonus(["20"]);
bonus(["175"]);
bonus(["2703"]);
bonus(["15875"]);
