function vowelsSum(input) {
    let text = input[0];
    let mapper = {
        "a": 1,
        "e": 2,
        "i": 3,
        "o": 4,
        "u": 5 
    }
    let result = 0;
    for (i = 0; i < text.length; i ++) {
        if (text[i].toLowerCase() in mapper) {
            result += mapper[text[i].toLowerCase()]
        }
    }
    console.log(result)
}

vowelsSum(["hello"])
vowelsSum(["hi"])
vowelsSum(["bamboo"])
vowelsSum(["beer"])