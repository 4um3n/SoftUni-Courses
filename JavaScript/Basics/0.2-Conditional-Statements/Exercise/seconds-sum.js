function secondsSum(input) {
    let a = Number(input[0]);
    let b = Number(input[1]);
    let c = Number(input[2]);
    let seconds = a + b + c;
    let minutes = Math.floor(seconds / 60);
    seconds = seconds % 60;
    if (seconds < 10) {
        seconds = `0${seconds}`
    }

    console.log(`${minutes}:${seconds}`);
}

secondsSum(["35", "45", "44"]);
secondsSum(["22", "7", "34"]);
secondsSum(["50", "50", "49"]);
secondsSum(["14", "12", "10"]);
