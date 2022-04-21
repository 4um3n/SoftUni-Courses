function isPasswordValid(input) {
    let user = input.shift(); let password = input.shift();
    i = 0;
    while (input[i] != password) {
        i++;
    
    }
    console.log(`Welcome ${user}!`)
}


isPasswordValid(["Nakov",
"1234",
"Pass",
"1324",
"1234"]);
isPasswordValid((["Gosho",
"secret",
"secret"]));