function isSpeedInLimit (speed, area) {
    function getStatus (diffSpeed) {
        if (diffSpeed <= 20) {
            return 'speeding';
        } else if (diffSpeed <= 40) {
            return 'excessive speeding'
        }
        return 'reckless driving'
    }

    let result;
    const areasSpeedLimit = {
        'motorway': 130,
        'interstate': 90,
        'city': 50,
        'residential': 20,
    };
    const speedLimit = areasSpeedLimit[area];

    if (speed <= speedLimit) {
        result = `Driving ${speed} km/h in a ${speedLimit} zone`;
    } else {
        const diff = Math.abs(speedLimit - speed);
        result = `The speed is ${diff} km/h faster than the allowed speed of ${speedLimit} - ${getStatus(diff)}`;
    }

    console.log(result);
}

isSpeedInLimit(40, 'city');
isSpeedInLimit(21, 'residential');
isSpeedInLimit(120, 'interstate');
isSpeedInLimit(200, 'motorway');
