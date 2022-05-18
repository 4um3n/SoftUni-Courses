function validityChecker(x, y, x1, y1) {
    const firstPointDistance = Math.sqrt(x ** 2 + y ** 2);
    const secondPointDistance = Math.sqrt(x1 ** 2 + y1 ** 2);
    const distanceBetweenPoints = Math.sqrt((x1 - x) ** 2 + (y1 - y) ** 2);

    const firstPointResult = (firstPointDistance % 1 === 0) ? 'valid' : 'invalid';
    const secondPointResult = (secondPointDistance % 1 === 0) ? 'valid' : 'invalid';
    const distanceBetweenPointsResult = (distanceBetweenPoints % 1 === 0) ? 'valid' : 'invalid';

    const result = [
        `{${x}, ${y}} to {0, 0} is ${firstPointResult}`,
        `{${x1}, ${y1}} to {0, 0} is ${secondPointResult}`,
        `{${x}, ${y}} to {${x1}, ${y1}} is ${distanceBetweenPointsResult}`,
    ];

    console.log(result.join('\n'));
}


validityChecker(3, 0, 0, 4);
validityChecker(2, 1, 1, 1);