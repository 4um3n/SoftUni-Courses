function extractWords (text) {
    const wordsPattern = /[A-Za-z\d]+/g;
    let matches = [];

    if (wordsPattern.test(text)) {
        matches = text.match(wordsPattern);
    }

    matches = matches.map((elem) => elem.toUpperCase());
    console.log(matches.join(', '));
}


extractWords('Hi, how are you?');
extractWords('hello');
