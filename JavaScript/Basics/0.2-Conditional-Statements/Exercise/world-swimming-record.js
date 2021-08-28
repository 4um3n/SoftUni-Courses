function isRecordBeaten(input) {
    let recordSeconds = Number(input[0]);
    let distance = Number(input[1]);
    let secondsPerMeter = Number(input[2]);
    let distanceSeconds = distance * secondsPerMeter;
    distanceSeconds += Math.floor(distance / 15) * 12.5;
    if (distanceSeconds < recordSeconds) {
        console.log(`Yes, he succeeded! The new world record is ${distanceSeconds.toFixed(2)} seconds.`);
    } else {
        diff = Math.abs(recordSeconds - distanceSeconds);
        console.log(`No, he failed! He was ${diff.toFixed(2)} seconds slower.`);
    }
}

isRecordBeaten(["10464", "1500", "20"]);
isRecordBeaten(["55555.67", "3017", "5.03"]);
