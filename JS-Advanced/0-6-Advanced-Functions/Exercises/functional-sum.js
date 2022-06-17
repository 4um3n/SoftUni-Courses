function add(n) {
    function inner(x) {
        n += x;
        return inner;
    }

    inner.toString = function () {return n;}
    return inner;
}

console.log(add(1).toString());
console.log(add(1)(6)(-3).toString());