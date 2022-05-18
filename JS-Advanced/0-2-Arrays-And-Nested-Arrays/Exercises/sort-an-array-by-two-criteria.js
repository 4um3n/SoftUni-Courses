function sortArray(arrayOfStrings) {
    arrayOfStrings = arrayOfStrings.sort(function (a, b) {
        if (a.length > b.length) {
            return 1;
        } else if (a.length < b.length) {
            return -1;
        }
        return a.localeCompare(b);
    });

    console.log(arrayOfStrings.join('\n'));
}


sortArray(['alpha', 'beta', 'gamma']);
sortArray(['Isacc', 'Theodor', 'Jack', 'Harrison', 'George']);
sortArray(['test', 'Deny', 'omen', 'Default']);
