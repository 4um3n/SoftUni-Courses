class Stringer {
    constructor(text, size) {
        this.innerString = text;
        this.innerLength = size;
    }

    get innerLength() {
        return this._innerLenght
    }

    set innerLength(value) {
        if (value < 0) {
            value = 0;
        }
        this._innerLenght = value;
    }

    decrease(n) {
        this.innerLength -= n;
    }

    increase(n) {
        this.innerLength += n;
    }

    toString() {
        const text = [this.innerString.slice(0, this.innerLength)];

        if (this.innerString.length > this.innerLength) {
            text.push('...');
        }

        return text.join('');
    }
}


let test = new Stringer("Test", 5);
console.log(test.toString()); // Test

test.decrease(3);
console.log(test.toString()); // Te...

test.decrease(5);
console.log(test.toString()); // ...

test.increase(4);
console.log(test.toString()); // Test
