function argumentInfo(...args) {
    const argsTypes = [];
    const argsAppearances = {};

    args.forEach(
        function (arg) {
            const argType = typeof arg;
            argsTypes.push(`${argType}: ${arg}`);

            if (!(argType in argsAppearances)) {
                argsAppearances[argType] = 0;
            }

            argsAppearances[argType]++;
        }
    );

    console.log(argsTypes.join('\n'));
    console.log(Array.from(Object.keys(argsAppearances).map(
        arg => `${arg} = ${argsAppearances[arg]}`
    )).join('\n'));
}


argumentInfo('cat', 'bla', 42, function () {console.log('Hello world!');})
// argumentInfo({ name: 'bob'}, 3.333, 9.999);