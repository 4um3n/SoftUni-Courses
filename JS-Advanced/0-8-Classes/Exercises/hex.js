class Hex {
    constructor(value) {
        this.value = value;
    }

    valueOf() {
        return this.value;
    }

    toString() {
        return `0x${this.value.toString(16).toUpperCase()}`;
    }

    plus(hexObj) {
        return new Hex(this.valueOf() + hexObj.valueOf());
    }

    minus(hexObj) {
        return new Hex(this.valueOf() - hexObj.valueOf());
    }

    parse(hexString) {
        return parseInt(hexString, 16);
    }
}
