function bill(input) {
    let product, town, quantity;
    [product, town, quantity] = input;
    quantity = Number(quantity);
    if (product == "coffee") {
        if (town == "Sofia") {
            console.log(quantity * 0.50);
        } else if (town == "Plovdiv") {
            console.log(quantity * 0.40);
        } else if (town == "Varna") {
            console.log(quantity * 0.45);
        }
    } else if (product == "water") {
        if (town == "Sofia") {
            console.log(quantity * 0.80);
        } else if (town == "Plovdiv") {
            console.log(quantity * 0.70);
        } else if (town == "Varna") {
            console.log(quantity * 0.70);
        }
    } else if (product == "beer") {
        if (town == "Sofia") {
            console.log(quantity * 1.20);
        } else if (town == "Plovdiv") {
            console.log(quantity * 1.15);
        } else if (town == "Varna") {
            console.log(quantity * 1.10);
        }
    } else if (product == "sweets") {
        if (town == "Sofia") {
            console.log(quantity * 1.45);
        } else if (town == "Plovdiv") {
            console.log(quantity * 1.30);
        } else if (town == "Varna") {
            console.log(quantity * 1.35);
        }
    } else if (product == "peanuts") {
        if (town == "Sofia") {
            console.log(quantity * 1.60);
        } else if (town == "Plovdiv") {
            console.log(quantity * 1.50);
        } else if (town == "Varna") {
            console.log(quantity * 1.55);
        }
    }
}

bill(["coffee", "Varna", "2"])
bill(["peanuts", "Plovdiv", "1"])
bill(["beer", "Sofia", "6"])
bill(["water", "Plovdiv", "3"])
bill(["sweets", "Sofia", "2.23"])