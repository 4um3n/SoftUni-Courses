function tradeCommission(input) {
    let town = input[0];
    let volume = Number(input[1]);
    let commission = "error";

    if (town == "Sofia") {
        if (volume < 0) {
            commission = "error";
        }else if (volume <= 500) {
            commission = volume * 0.05;
        } else if (volume <= 1000) {
            commission = volume * 0.07;
        } else if (volume <= 10000) {
            commission = volume * 0.08;
        } else if (volume > 10000) {
            commission = volume * 0.12;
        }
    } else if (town == "Varna") {
        if (volume < 0) {
            commission = "error";
        } else if (volume <= 500) {
            commission = volume * 0.045;
        } else if (volume <= 1000) {
            commission = volume * 0.075;
        } else if (volume <= 10000) {
            commission = volume * 0.1;
        } else if (volume > 10000) {
            commission = volume * 0.13;
        }
    } else if (town == "Plovdiv") {
        if (volume < 0) {
            commission = "error";
        } else if (volume <= 500) {
            commission = volume * 0.055;
        } else if (volume <= 1000) {
            commission = volume * 0.08;
        } else if (volume <= 10000) {
            commission = volume * 0.12;
        } else if (volume > 10000) {
            commission = volume * 0.145;
        }
    }

    if (typeof commission == "string") {
        console.log(commission);
    } else {
        console.log(commission.toFixed(2))
    }
}

tradeCommission(["Sofia", "1500"])
tradeCommission(["Plovdiv", "499.99"])
tradeCommission(["Varna", "3874.50"])
tradeCommission(["Plovdiv", "-20"])