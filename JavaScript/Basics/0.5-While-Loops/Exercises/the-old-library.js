function findBook(input) {
    let searchedBook = input.shift(); let i = 0;
    while (i < input.length) {
        if (input[i] == searchedBook) {return `You checked ${i} books and found it.`}
        if (input[i] == "No More Books") {break;}
        i++
    }
    return `The book you search is not here!\nYou checked ${i} books.`;
}


console.log(findBook(["Troy",
"Stronger",
"Life Style",
"Troy"]));console.log(findBook(["Bourne",
"True Story",
"Forever",
"More Space",
"The Girl",
"Spaceship",
"Strongest",
"Profit",
"Tripple",
"Stella",
"The Matrix",
"Bourne"]));
console.log(findBook(["The Spot",
"Hunger Games",
"Harry Potter",
"Torronto",
"Spotify",
"No More Books"]));
console.log(findBook(["Bourne",
"True Story",
"Forever",
"More Space",
"The Girl",
"Spaceship",
"Strongest",
"Profit",
"Tripple",
"Stella",
"The Matrix",
"Bourne"]));