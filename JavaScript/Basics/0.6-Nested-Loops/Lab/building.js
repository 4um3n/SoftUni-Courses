function building(input) {
    let floors = Number(input[0]);
    let rooms = Number(input[1]);
    for (let f = floors; f >= 1; f--) {
        let currentFloor = [];
        for (let r = 0; r < rooms; r++) {
            if (f == floors) {
                currentFloor.push(`L${f}${r}`);
            } else if (f % 2 == 0) {
                currentFloor.push(`O${f}${r}`);
            } else if (f % 2 == 1) {
                currentFloor.push(`A${f}${r}`);
            }
        }
        console.log(currentFloor.join(' '));
    }
}


building((["6", "4"]));
building((["9", "5"]));