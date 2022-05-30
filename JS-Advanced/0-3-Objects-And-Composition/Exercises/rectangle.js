function rectangle(w, h, color) {
    w = Number(w);
    h = Number(h);
    color = [
        color.charAt(0).toUpperCase(),
        color.slice(1)
    ].join('');

    function calcArea() {
        return this.width * this.height;
    }

    return {
        'width': w,
        'height': h,
        'color': color,
        'calcArea': calcArea
    };
}

let rect = rectangle(4, 5, 'red');
console.log(rect.width);
console.log(rect.height);
console.log(rect.color);
console.log(rect.calcArea());
