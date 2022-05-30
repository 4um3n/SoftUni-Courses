function carFactory(requirement) {
    function getEngine(power) {
        const possibleEngines = [
            {'power': 90, 'volume': 1800},
            {'power': 120, 'volume': 2400},
            {'power': 200, 'volume': 3500},
        ].filter(x => x.power >= power);
        return possibleEngines[0];
    }

    const carriageMapper = {
        'hatchback': function (color) {
            return {'type': 'hatchback', 'color': color};
        },
        'coupe': function (color) {
            return {'type': 'coupe', 'color': color};
        }
    };

    function getWheels(size) {
        const wheels = [0, 0, 0, 0];
        size = Math.floor(Number(size));

        if (size % 2 === 0) {
            size--;
        }

        wheels.fill(size);
        return wheels;
    }

    return {
        'model': requirement.model,
        'engine': getEngine(requirement.power),
        'carriage': carriageMapper[requirement.carriage](requirement.color),
        'wheels': getWheels(requirement.wheelsize)
    };

}


console.log(carFactory(
    {
        model: 'VW Golf II',
        power: 90,
        color: 'blue',
        carriage: 'hatchback',
        wheelsize: 14
    }
));

console.log(carFactory(
    {
        model: 'Opel Vectra',
        power: 110,
        color: 'grey',
        carriage: 'coupe',
        wheelsize: 17
    }
));
