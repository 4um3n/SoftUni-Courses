function fishTank(input) {
    let length = Number(input[0]);
    let width = Number(input[1]);
    let height = Number(input[2]);
    let takenPercent = Number(input[3]);
    takenPercent *= 0.01;
    let fishTankCapacity = (width * length * height) * 0.001;
    let neededWaterLiters = fishTankCapacity * (1 - takenPercent);
    console.log(neededWaterLiters)
}

fishTank(["85", "75", "47", "17"])
fishTank(["105", "77", "89", "18.5"])
