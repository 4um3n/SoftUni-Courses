function storeCatalogue(data) {
    const sortedData = {};

    for (let product of data) {
        let [name, price] = product.split(' : ');
        price = Number(price);
        const firstLetter = name[0];

        if (!sortedData[firstLetter]) {
            sortedData[firstLetter] = [];
        }

        sortedData[firstLetter].push(`  ${name}: ${price}`);
        sortedData[firstLetter].sort((a, b) => a.localeCompare(b));
    }

    const result = [];

    for (let [letter, lines] of Object.entries(sortedData)) {
        result.push(`${letter}\n${lines.join('\n')}`);
    }

    result.sort((a, b) => a.localeCompare(b));
    return result.join('\n');
}


console.log(storeCatalogue(
    [
        'Appricot : 20.4',
        'Fridge : 1500',
        'TV : 1499',
        'Deodorant : 10',
        'Boiler : 300',
        'Apple : 1.25',
        'Anti-Bug Spray : 15',
        'T-Shirt : 10'
    ]
))
