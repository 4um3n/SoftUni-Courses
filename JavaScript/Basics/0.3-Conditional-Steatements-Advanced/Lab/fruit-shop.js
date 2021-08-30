function fruitShop(input) {
    let fruit, day, quantity;
    [fruit, day, quantity] = input;
    quantity = Number(quantity);
    let week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"];
    let workingDays = {
        "banana": 2.50,
        "apple": 1.20,
        "orange": 0.85,
        "grapefruit": 1.45,
        "kiwi": 2.70,
        "pineapple": 5.50,
        "grapes": 3.85
    }
    let weekends = {
        "banana": 2.70,
        "apple": 1.25,
        "orange": 0.90,
        "grapefruit": 1.60,
        "kiwi": 3,
        "pineapple": 5.60,
        "grapes": 4.20
    }

    if (day == "Sunday" || day == "Saturday") {
        if (fruit in weekends) {
            console.log((quantity * weekends[fruit]).toFixed(2));
        } else {
            console.log("error");
        }
    } else if (week.includes(day)) {
        if (fruit in workingDays) {
            console.log((quantity * workingDays[fruit]).toFixed(2));
        } else {
            console.log("error");
        }
    } else {
        console.log("error");
    }
}

fruitShop(["apple", "Tuesday", "2"])
fruitShop(["orange", "Sunday", "3"])
fruitShop(["kiwi", "Monday", "2.5"])
fruitShop(["grapes", "Saturday", "0.5"])
fruitShop(["tomato", "Monday", "0.5"])