function solve() {
    function fighter(name) {
        function fight() {
            this.stamina--;
            console.log(`${this.name} slashes at the foe!`)
        }

        return {
            'name': name,
            'health': 100,
            'stamina': 100,
            'fight': fight
        };
    }

    function mage(name) {
        function cast() {
            this.mana--;
            console.log(`${this.name} slashes at the foe!`)
        }

        return {
            'name': name,
            'health': 100,
            'mana': 100,
            'cast': cast,
        };
    }

    return {
        'fighter': fighter,
        'mage': mage
    };
}