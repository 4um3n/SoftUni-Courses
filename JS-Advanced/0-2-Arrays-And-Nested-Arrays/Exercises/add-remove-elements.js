function addRemove(commands) {
    let numbers = [];
    let n = 1;

    const commandsMapper = {
        'add': (arr, el) => arr.push(el),
        'remove': arr => arr.pop(),
    };


    for (let command of commands) {
        commandsMapper[command](numbers, n);
        n++;
    }

    console.log((numbers.length > 0) ? numbers.join('\n') : 'Empty');
}


addRemove(['add', 'add', 'add', 'add']);
addRemove(['add', 'add', 'remove', 'add', 'add']);
addRemove(['remove', 'remove', 'remove']);

