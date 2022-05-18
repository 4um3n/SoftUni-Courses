function numbersCooking (number, ...operations) {
    let result = [];
    const operationsMapper = {
        'chop': (x) => x / 2,
        'dice': (x) => Math.sqrt(x),
        'spice': (x) => x + 1,
        'bake': (x) => x * 3,
        'fillet': (x) => x - x * 0.20,
    };

    for (const operation of operations) {
        number = operationsMapper[operation](number);
        result.push(number);
    }

    console.log(result.join('\n'));
}


numbersCooking('32', 'chop', 'chop', 'chop', 'chop', 'chop')
numbersCooking('9', 'dice', 'spice', 'chop', 'bake', 'fillet')