function moving(input) {
    let w = Number(input.shift());
    let l = Number(input.shift());
    let h = Number(input.shift());
    let free_space = w * l * h; let i = 0;
    while (input[i] != "Done") {
        let box = Number(input[i]);
        free_space -= box;
        if (free_space < 0) {
            return `No more free space! You need ${Math.abs(free_space)} Cubic meters more.`
        }
        i++;
    }
    return `${free_space} Cubic meters left.`;
}


console.log(moving(["10",
"10",
"2",
"20",
"20",
"20",
"20",
"122"]));
console.log(moving(["10",
"1",
"2",
"4",
"6",
"Done"]));
