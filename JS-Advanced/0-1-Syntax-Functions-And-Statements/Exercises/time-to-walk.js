function walkToShoolTotalTime (stepsToSchool, foodprintMeters, speedKmH) {
    function secondsToHours (seconds) {
        const hours = Math.floor(seconds / 3600);
        seconds %= 3600; // leftover seconds after hours calculation
        const minutes = Math.floor(seconds / 60);
        seconds %= 60; // leftover seconds after minutes calculation

        // Turn all of the three values (hours, minutes, seconds) into strings
        // and if any of them is lower than 10, put a zero ('0') before it
        const hour = (hours < 10) ? `0${hours}` : hours.toString();
        const minute = (minutes < 10) ? `0${minutes}` : minutes.toString();
        const second = (seconds < 10) ? `0${seconds.toFixed(0)}` : seconds.toFixed(0).toString();
        return `${hour}:${minute}:${second}`;
    }

    const speedKmS = speedKmH / 3600;
    const totalWalkedMeters = (stepsToSchool * foodprintMeters);
    const totalWalkedKilometers = totalWalkedMeters / 1000;
    const totalBreaksCount = Math.floor(totalWalkedMeters / 500);

    let totalWalkedSeconds = totalWalkedKilometers / speedKmS;
    totalWalkedSeconds += 60 * totalBreaksCount;
    console.log(secondsToHours(totalWalkedSeconds));
}

walkToShoolTotalTime(4000, 0.60, 5);
walkToShoolTotalTime(2564, 0.70, 5.5);
