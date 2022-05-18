function circleArea (r) {
    let result;

    if (typeof r === 'number') {
        result = (Math.PI * r ** 2).toFixed(2);
    } else {
        result = `We can not calculate the circle area, because we receive a ${typeof r}.`;
    }

    console.log(result);
}

circleArea(5);
circleArea('name');
