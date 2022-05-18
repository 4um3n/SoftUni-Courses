function beautifyNames(names) {
    names = names.sort((a, b) => a.localeCompare(b));
    names = names.map((name, i) => `${i + 1}.${name}`);
    console.log(names.join('\n'));
}

beautifyNames(["John", "Bob", "Christina", "Ema"]);
