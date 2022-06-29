function deckOfCards(cards) {
    function getCard(f, s) {
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

    const message = [];

    for (const card of cards) {
        try {
            const f = card.slice(0, card.length - 1);
            const s = card[card.length - 1];
            const tmpCardObj = getCard(f, s);
            message.push(tmpCardObj.toString());
        } catch (error) {
            return `Invalid card: ${card}`;
        }
    }

    return message.join(' ');
}


console.log(deckOfCards(['AS', '10D', 'KH', '2C']));
console.log(deckOfCards(['5S', '3D', 'QD', '1C']));