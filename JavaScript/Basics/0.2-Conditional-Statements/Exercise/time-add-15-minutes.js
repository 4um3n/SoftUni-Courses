function addMinutes(input) {
    let hours = Number(input[0]);
    let minutes = Number(input[1]);
    minutes += 15;
    while (minutes > 60) {
        minutes -= 60;
        hours += 1;
        if (hours > 23) {
            hours = 0;
        }
    }

    if (minutes < 10) {
        minutes = `0${minutes}`;
    }

    console.log(`${hours}:${minutes}`);
}

addMinutes(["1", "46"])
addMinutes(["0", "01"])
addMinutes(["23", "59"])
addMinutes(["11", "08"])
addMinutes(["12", "49"])
