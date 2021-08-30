function skiTrip(input) {
    let nightsCount = Number(input[0]) - 1;
    let roomType = input[1];
    let appraisal = input[2];
    let price;
    if (roomType == "room for one person") {
        price = 18 * nightsCount;
    } else if (roomType == "apartment") {
        price = 25 * nightsCount;
        if (nightsCount < 10) {
            price -= price * 0.30;
        }else if (nightsCount <= 15){
            price -= price * 0.35; 
        } else if (nightsCount > 15) {
            price -= price * 0.50;
        }
    } else if (roomType == "president apartment") {
        price = 35 * nightsCount;
        if (nightsCount < 10) {
            price -= price * 0.10;
        }else if (nightsCount <= 15){
            price -= price * 0.15; 
        } else if (nightsCount > 15) {
            price -= price * 0.20;
        }
    }

    if (appraisal == "positive") {
        price += price * 0.25;
    } else {
        price -= price * 0.10;
    }

    console.log(price.toFixed(2));
}

skiTrip(["14", "apartment", "positive"])
skiTrip(["30", "president apartment", "negative"])
