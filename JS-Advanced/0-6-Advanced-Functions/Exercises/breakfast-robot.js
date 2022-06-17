function solution() {
    const ingredients = {
        'protein': 0,
        'carbohydrate': 0,
        'fat': 0,
        'flavour': 0,
    };

    const products = {
        'apple': {
            'carbohydrate': 1,
            'flavour': 2
        },
        'lemonade': {
            'carbohydrate': 10,
            'flavour': 20
        },
        'burger': {
            'carbohydrate': 5,
            'fat': 7,
            'flavour': 3
        },
        'eggs': {
            'protein': 5,
            'fat': 1,
            'flavour': 1
        },
        'turkey': {
            'protein': 10,
            'carbohydrate': 10,
            'fat': 10,
            'flavour': 10
        }
    };


    function IngredientException(message) {
        this.message = message;
        this.name = 'ProductException'
    }

    function checkIngredients(product, quantity) {
        Object.keys(products[product]).forEach((ingredient) => {
            if (ingredients[ingredient] < products[product][ingredient] * quantity) throw new IngredientException(
                `Error: not enough ${ingredient} in stock`
            );
        });
    }

    function useIngredients(product, quantity) {
        Object.keys(products[product]).forEach((ingredient) => {
            ingredients[ingredient] -= products[product][ingredient] * quantity;
        });
    }

    function prepareProduct(product, quantity) {
        try {
            checkIngredients(product, quantity);
            useIngredients(product, quantity);
            return 'Success';
        } catch (exception) {
            return exception.message;
        }
    }

    const commandsMapper = {
        restock(ingredient, quantity) {
            ingredients[ingredient] += quantity;
            return 'Success'
        },
        prepare(product, quantity) {
            return prepareProduct(product, quantity);
        },
        report() {
            return Object.keys(ingredients).map(ingr => `${ingr}=${ingredients[ingr]}`).join(' ');
        }
    };

    function manager(commands) {
        let [command, more, quantity] = commands.split(' ');
        return commandsMapper[command](more, Number(quantity));
    }

    return manager;
}

let manager = solution();
const input = [
    'prepare turkey 1',
    'restock protein 10',
    'prepare turkey 1',
    'restock carbohydrate 10',
    'prepare turkey 1',
    'restock fat 10',
    'prepare turkey 1',
    'restock flavour 10',
    'prepare turkey 1',
    'report'
];

for (let c of input) {
    console.log(manager((c)));
}
