function cars(commands) {
    const cars = {};

    function create(car, inherit, parentName) {
        if (inherit) {
            cars[car] = Object.create(cars[parentName]);
        } else {
            cars[car] = {};
        }
    }

    function set(name, key, value) {
        cars[name][key] = value;
    }

    function print(car) {
        const result = [];

        for (const key in cars[car]) {
            result.push(`${key}:${cars[car][key]}`)
        }

        console.log(result.join(','));
    }

    const processor = {
        'create': create,
        'set': set,
        'print': print
    };

    commands.map(el => el.split(' ')).forEach(
        ([command, car, isInherited, parent]) => processor[command](car, isInherited, parent)
    );
}


cars(['create c1',
    'create c2 inherit c1',
    'set c1 color red',
    'set c2 model new',
    'print c1',
    'print c2'])