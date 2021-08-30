function personTitles(input) {
    let age = Number(input[0]);
    let gender = input[1].toLowerCase();
    if (age < 16) {
        if (gender == "f") {
            console.log("Miss");
        } else if (gender == "m") {
            console.log("Master");
        }
    } else {
       if (gender == "f") {
            console.log("Ms.");
        } else if (gender == "m") {
            console.log("Mr.");
        }
    }
}
