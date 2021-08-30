function cinemaTickets(input) {
    let day = input[0];
    let days = {
        12: ["Monday", "Tuesday", "Friday"],
        14: ["Wednesday", "Thursday"],
        16: ["Saturday", "Sunday"]
    };
    if (days[12].includes(day)) {
        console.log("12");
    } else if (days[14].includes(day)) {
        console.log("14");
    } else if (days[16].includes(day)) {
        console.log("16");
    }
}

cinemaTickets(["Monday"])
cinemaTickets(["Wednesday"])
cinemaTickets(["Sunday"])