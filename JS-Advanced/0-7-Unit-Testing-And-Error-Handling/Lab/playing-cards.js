function solve(f, s) {
    class Card {
        validFaces = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'];
        validSuits = {
            'S': '♠',
            'H': '♥',
            'D': '♦',
            'C': '♣',
        };

        constructor(face, suite) {
            this.face = face;
            this.suite = suite;
        }

        get face() {
            return this._face;
        }

        set face(value) {
            if (!this.validFaces.includes(value)) {
                throw new Error('Error');
            }

            this._face = value;
        }

        get suite() {
            return this._suite;
        }

        set suite(value) {
            if (!Object.keys(this.validSuits).includes(value)) {
                throw new Error('Error');
            }

            this._suite = this.validSuits[value];
        }

        toString() {
            return `${this.face}${this.suite}`
        }
    }

    return new Card(f, s);
}


console.log(solve('A', 'S').toSting());
console.log(solve('10', 'H').toSting());
console.log(solve('1', 'C').toSting());
