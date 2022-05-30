function lowestPriceInTown(data) {
    const products = {};

    for (const line of data) {
        let [town, product, price] = line.split(' | ');
        price = Number(price);

        if (!(product in products)) {
            products[product] = {
                'price': price,
                'town': town
            };
        }

        if (products[product]['price'] > price) {
            products[product]['price'] = price;
            products[product]['town'] = town;
        }
    }

    const result = [];
    for (const prod in products) {
        const line = `${prod} -> ${products[prod].price} (${products[prod].town})`;
        result.push(line);
    }
    return result.join('\n');
}


console.log(lowestPriceInTown(
    [
        'Sample Town | Sample Product | 1000',
        'Sample Town | Orange | 2',
        'Sample Town | Peach | 1',
        'Sofia | Orange | 3',
        'Sofia | Peach | 2',
        'New York | Sample Product | 1000.1',
        'New York | Burger | 10'
    ]
));

