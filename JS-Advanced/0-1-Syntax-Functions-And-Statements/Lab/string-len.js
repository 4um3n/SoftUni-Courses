function lenOfStrings(str1, str2, str3) {
    const stringsLen = Array.from(arguments).map((elem) => elem.length).reduce((a, b) => a + b);
    const averageStringsLen = Math.floor(stringsLen / arguments.length);
    console.log(`${stringsLen}\n${averageStringsLen}`);
}

lenOfStrings('chocolate', 'ice cream', 'cake');
lenOfStrings('pasta', '5', '22.3');
