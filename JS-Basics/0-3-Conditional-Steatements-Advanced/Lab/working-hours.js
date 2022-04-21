function isOfficeWorking(input) {
    let hour = Number(input[0]);
    let day = input[1];
    let workingDays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];
    let workingHours = [10, 11, 12, 13, 14, 15, 16, 17, 18];
    if (workingDays.includes(day) && workingHours.includes(hour)) {
        console.log("open");
    } else {
        console.log("closed");
    }
}
