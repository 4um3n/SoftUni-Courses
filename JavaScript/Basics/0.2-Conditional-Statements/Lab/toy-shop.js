function isHolidayPossible(input) {
    let holidayPrice = Number(input[0]);
    let puzzlesCount = Number(input[1]);
    let dollsCount = Number(input[2]);
    let bearsCount = Number(input[3]);
    let minionsCount = Number(input[4]);
    let trucksCount = Number(input[5]);
    let result = puzzlesCount * 2.60 + dollsCount * 3 +
     bearsCount * 4.10 + minionsCount * 8.20 + trucksCount * 2;
    if (bearsCount + dollsCount + puzzlesCount + minionsCount + trucksCount >= 50) {
        result -= result * 0.25;
    }

    result -= result * 0.10;
    let diff = Math.abs(result - holidayPrice);
    if (result >= holidayPrice) {
        console.log(`Yes! ${diff.toFixed(2)} lv left.`);
    }
    else {
        console.log(`Not enough money! ${diff.toFixed(2)} lv needed.`);
    }   
}

isHolidayPossible(["40.8", "20", "25", "30", "50", "10"]);
isHolidayPossible(["320", "8", "2", "5", "5", "1"]);
