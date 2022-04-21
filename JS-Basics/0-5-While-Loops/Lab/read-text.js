function wordsReading(input) {
    i = 0;
    while (input[i] != "Stop") {
        console.log(input[i]);
        i += 1;
    }
}


wordsReading(["Nakov",
"SoftUni",
"Sofia",
"Bulgaria",
"SomeText",
"Stop",
"AfterStop",
"Europe",
"HelloWorld"]);
wordsReading(["Sofia",
"Berlin",
"Moscow",
"Athens",
"Madrid",
"London",
"Paris",
"Stop",
"AfterStop"]);