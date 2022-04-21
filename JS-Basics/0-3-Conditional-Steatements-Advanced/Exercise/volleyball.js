function volleyball(input) {
    let yearType = input[0];
    let holidaysCount = Number(input[1]);
    let weekendsCount = Number(input[2]);
    let gamesCount = (48 - weekendsCount) * (3 / 4);
    gamesCount += weekendsCount + (holidaysCount * (2 / 3));
    if (yearType == "leap") {
        gamesCount += gamesCount * 0.15;
    }
    gamesCount = Math.floor(gamesCount);
    console.log(gamesCount)
}

volleyball(["leap", "5", "2"])
volleyball(["normal", "3", "2"])
volleyball(["leap", "2", "3"])
volleyball(["normal", "11", "6"])
volleyball(["leap", "0", "1"])
volleyball(["normal", "6", "13"])