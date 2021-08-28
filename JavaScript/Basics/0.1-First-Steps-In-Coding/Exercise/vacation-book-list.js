function vacationBooks(input) {
    let pagesCount = Number(input[0]);
    let pagesPerHour = Number(input[1]);
    let daysCount = Number(input[2]);
    let timeForOneBook = pagesCount / pagesPerHour;
    let readingHoursPerDay = timeForOneBook / daysCount;
    console.log(readingHoursPerDay);
}

vacationBooks(["212", "20", "2"]);
vacationBooks(["432", "15", "4"]);