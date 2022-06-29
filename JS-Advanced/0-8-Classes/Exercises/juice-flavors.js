function juiceFlavours(data) {
    const juices = new Map();
    const bottles = new Map();

    for (const juiceData of data) {
        let [juice, amount] = juiceData.split(' => ');
        amount = Number(amount);

        if (!juices.has(juice)) {
            juices.set(juice, 0);
        }

        const totalJuiceAmount = juices.get(juice) + amount;
        juices.set(juice, totalJuiceAmount);

        if (totalJuiceAmount >= 1000) {
            if (!bottles.has(juice)) {
                bottles.set(juice, 0)
            }

            const currentBottles = Math.trunc(totalJuiceAmount / 1000);
            const totalBottlesAmount = bottles.get(juice) + currentBottles;
            const leftJuice = totalJuiceAmount % 1000;
            bottles.set(juice, totalBottlesAmount);
            juices.set(juice, leftJuice);
        }
    }

    return Array.from(bottles.keys()).map(
        j => `${j} => ${bottles.get(j)}`
    ).join('\n');
}

console.log(juiceFlavours([
    'Kiwi => 234',
    'Pear => 2345',
    'Watermelon => 3456',
    'Kiwi => 4567',
    'Pear => 5678',
    'Watermelon => 6789'
]));
