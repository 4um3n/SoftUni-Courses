function graduation(input) {
    let i = 0; let grades = 0; let classN = 0; let excluded = 0;
    let name = input.shift(); input = input.map(n => Number(n));
    while (excluded < 2) {
        if (input[i] < 4) {excluded++; i++; continue;}
        classN++; grades += input[i];
        if (i == input.length - 1) {
            let average = grades / classN;
            return `${name} graduated. Average grade: ${average.toFixed(2)}`
        }
        i++;
    }
    classN++;
    return `${name} has been excluded at ${classN} grade`;  
}


console.log(graduation(["Gosho",
"5",
"5.5",
"6",
"5.43",
"5.5",
"6",
"5.55",
"5",
"6",
"6",
"5.43",
"5"]));
console.log(graduation(["Mimi",
"5",
"6",
"5",
"6",
"5",
"6",
"6",
"2",
"3"]));