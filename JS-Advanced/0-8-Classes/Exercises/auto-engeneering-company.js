function producedCars(data) {
    const brands = new Map();

    for (const line of data) {
        let [brand, model, amount] = line.split(' | ');
        amount = Number(amount);

        if (!brands.has(brand)) {
            brands.set(brand, new Map());
        }

        if (!brands.get(brand).has(model)) {
            brands.get(brand).set(model, 0);
        }

        const totalModelAmount = brands.get(brand).get(model) + amount;
        brands.get(brand).set(model, totalModelAmount);
    }

    const message = [];

    for (const b of brands.keys()) {
        message.push(b);
        const models = brands.get(b);

        for (const m of models.keys()) {
            message.push((`###${m} -> ${models.get(m)}`));
        }
    }

    return message.join('\n');
}


console.log(producedCars([
    'Audi | Q7 | 1000',
    'Audi | Q6 | 100',
    'BMW | X5 | 1000',
    'BMW | X6 | 100',
    'Citroen | C4 | 123',
    'Volga | GAZ-24 | 1000000',
    'Lada | Niva | 1000000',
    'Lada | Jigula | 1000000',
    'Citroen | C4 | 22',
    'Citroen | C5 | 10'
]));
