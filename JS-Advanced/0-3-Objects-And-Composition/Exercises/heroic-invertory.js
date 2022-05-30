function heroicInventory(data) {
    const inventory = [];

    for (const line of data) {
        let [name, level, items] = line.split('/');
        items = items ? items.split(',').map(x => x.trim()) : [];

        inventory.push({
            'name': name.trim(),
            'level': Number(level.trim()),
            'items': items,
        });
    }

    return JSON.stringify(inventory);
}


console.log(heroicInventory(
    [
        'Isacc / 25 / Apple, GravityGun',
        'Derek / 12 / BarrelVest, DestructionSword',
        'Hes / 1 / Desolator, Sentinel, Antara'
    ]
));
console.log(heroicInventory(['Jake / 1000 / Gauss, HolidayGrenade']));