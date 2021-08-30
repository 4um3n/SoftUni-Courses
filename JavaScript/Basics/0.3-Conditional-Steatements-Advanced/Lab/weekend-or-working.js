function workOrHome(input) {
    let workingDays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"];
    let weekendDays = ["Saturday", "Sunday"];
    let day = input[0];
    if (workingDays.includes(day)) {
        console.log("Working day");
    } else if (weekendDays.includes(day)) {
        console.log("Weekend");
    } else {
        console.log("Error");
    }
}
