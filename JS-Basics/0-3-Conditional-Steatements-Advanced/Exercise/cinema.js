function cinema(input) {
    let projectionType = input[0];
    let rows = Number(input[1]);
    let columns = Number(input[2]);
    let ticketPrice;

    if (projectionType == "Premiere") {
        ticketPrice = 12;
    } else if (projectionType == "Normal") {
        ticketPrice = 7.50;
    } else if (projectionType == "Discount") {
        ticketPrice = 5;
    }

    ticketPrice = ticketPrice * (rows * columns);
    console.log(ticketPrice.toFixed(2))
}

cinema(["Premiere", "10", "12"])
cinema(["Normal", "21", "13"])
cinema(["Discount", "12", "30"])
