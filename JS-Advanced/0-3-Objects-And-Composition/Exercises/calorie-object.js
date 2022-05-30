function calorieObject(data) {
    const tmpObject = {};

    while (data.length > 0) {
        tmpObject[data.shift()] = Number(data.shift());
    }

    return tmpObject;
}

console.log(calorieObject(['Yoghurt', '48', 'Rise', '138', 'Apple', '52']));
console.log(calorieObject(['Potato', '93', 'Skyr', '63', 'Cucumber', '18', 'Milk', '42']));
