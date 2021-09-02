function cinemaTickets(input) {
    let standardTickets, kidTickets, studentTickets, occupiedChairs;
    [standardTickets, kidTickets, studentTickets, occupiedChairs] = [0, 0, 0, 0];
    while (input[0] != "Finish") {
        occupiedChairs = 0;
        let movie = input.shift(); 
        let freeChairs = Number(input.shift());
        while (occupiedChairs < freeChairs && input[0] != "End" && input[0] != "Finish") {
            let ticket = input.shift(); 
            if (ticket == "standard") {standardTickets++;}
            else if (ticket == "kid") {kidTickets++;}
            else if (ticket == "student") {studentTickets++;}
            occupiedChairs++;
        }
        occupiedChairs = occupiedChairs / freeChairs * 100;
        console.log(`${movie} - ${occupiedChairs.toFixed(2)}% full.`);
        if (input[0] == "End") {input.shift()}
    }
    
    totalTickets = standardTickets + studentTickets + kidTickets;
    standardTickets = standardTickets / totalTickets * 100;
    studentTickets = studentTickets / totalTickets * 100;
    kidTickets = kidTickets / totalTickets * 100;
    console.log(`Total tickets: ${totalTickets}`);
    console.log(`${studentTickets.toFixed(2)}% student tickets.`);
    console.log(`${standardTickets.toFixed(2)}% standard tickets.`);
    console.log(`${kidTickets.toFixed(2)}% kids tickets.`);
}


cinemaTickets(["Taxi",
"10",
"standard",
"kid",
"student",
"student",
"standard",
"standard",
"End",
"Scary Movie",
"6",
"student",
"student",
"student",
"student",
"student",
"student",
"Finish"]);
cinemaTickets(["The Matrix",
"20",
"student",
"standard",
"kid",
"kid",
"student",
"student",
"standard",
"student",
"End",
"The Green Mile",
"17",
"student",
"standard",
"standard",
"student",
"standard",
"student",
"End",
"Amadeus",
"3",
"standard",
"standard",
"standard",
"Finish"]);