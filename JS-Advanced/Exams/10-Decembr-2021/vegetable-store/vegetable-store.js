class VegetableStore {
    constructor(owner, location) {
        this.owner = owner;
        this.location = location;
        this.avalableProducts = [];
    }

    _getVegetableByType(vegetableType) {
        for (const vegetable of this.avalableProducts) {
            if (vegetable.type === vegetableType) {
                return vegetable;
            }
        }
    }

    _updateVegetable(vegetable, quantity, price) {
        vegetable.quantity += quantity;
        if (vegetable.price < price) vegetable.price = price;
    }

    _addNewVegetable(type, quantity, price) {
        this.avalableProducts.push({
            type,
            quantity,
            price
        });
    }

    loadingVegetables(vegetables) {
        const addedVegetablesTypes = [];

        for (let product of vegetables) {
            let [type, quantity, price] = product.split(' ');
            quantity = Number(quantity);
            price = Number(price);
            const vegetable = this._getVegetableByType(type);

            if (vegetable) {
                this._updateVegetable(vegetable, quantity, price);
            } else {
                this._addNewVegetable(type, quantity, price);
            }

            if (!addedVegetablesTypes.includes(type)) addedVegetablesTypes.push(type);
        }

        return `Successfully added ${addedVegetablesTypes.join(', ')}`;
    }

    buyingVegetables(selectedProducts) {
        let totalPrice = 0;

        for (const product of selectedProducts) {
            let [type, quantity] = product.split(' ');
            const vegetable = this._getVegetableByType(type);

            if (!vegetable) {
                throw new Error(
                    `${type} is not available in the store, your current bill is $${totalPrice.toFixed(2)}.`
                );
            }

            if (quantity > vegetable.quantity) {
                throw new Error(
                    `The quantity ${quantity} for the vegetable ${type} is not available in the store, your current bill is $${totalPrice.toFixed(2)}.`
                );
            }

            totalPrice += vegetable.price * quantity;
            vegetable.quantity -= quantity;
        }

        return `Great choice! You must pay the following amount $${totalPrice.toFixed(2)}.`
    }

    rottingVegetable(type, quantity) {
        const vegetable = this._getVegetableByType(type);

        if (!vegetable) {
            throw new Error(`${type} is not available in the store.`);
        }

        if (quantity > vegetable.quantity) {
            vegetable.quantity = 0;
            return `The entire quantity of the ${type} has been removed.`;
        }

        vegetable.quantity -= quantity;
        return `Some quantity of the ${type} has been removed.`;
    }

    revision() {
        const message = [`Available vegetables:`]

        message.push.apply(message, this.avalableProducts.sort((a, b) => a['price'] - b['price']).map(
            el => `${el.type}-${el.quantity}-$${el.price}`
        ));

        message.push(`The owner of the store is ${this.owner}, and the location is ${this.location}.`);
        return message.join('\n');
    }
}



// let vegStore = new VegetableStore("Jerrie Munro", "1463 Pette Kyosheta, Sofia");
// console.log(vegStore.loadingVegetables(["Okra 2.5 3.5", "Beans 10 2.8", "Celery 5.5 2.2", "Celery 0.5 2.5"]));


// let vegStore = new VegetableStore("Jerrie Munro", "1463 Pette Kyosheta, Sofia");
// console.log(vegStore.loadingVegetables(["Okra 2.5 3.5", "Beans 10 2.8", "Celery 5.5 2.2", "Celery 0.5 2.5"]));
// console.log(vegStore.buyingVegetables(["Okra 1"]));
// console.log(vegStore.buyingVegetables(["Beans 8", "Okra 1.5"]));
// console.log(vegStore.buyingVegetables(["Banana 1", "Beans 2"]));


// let vegStore = new VegetableStore("Jerrie Munro", "1463 Pette Kyosheta, Sofia");
// console.log(vegStore.loadingVegetables(["Okra 2.5 3.5", "Beans 10 2.8", "Celery 5.5 2.2", "Celery 0.5 2.5"]));
// console.log(vegStore.rottingVegetable("Okra", 1));
// console.log(vegStore.rottingVegetable("Okra", 2.5));
// console.log(vegStore.buyingVegetables(["Beans 8", "Okra 1.5"]));


// let vegStore = new VegetableStore("Jerrie Munro", "1463 Pette Kyosheta, Sofia");
// console.log(vegStore.loadingVegetables(["Okra 2.5 3.5", "Beans 10 2.8", "Celery 5.5 2.2", "Celery 0.5 2.5"]));
// console.log(vegStore.rottingVegetable("Okra", 1));
// console.log(vegStore.rottingVegetable("Okra", 2.5));
// console.log(vegStore.buyingVegetables(["Beans 8", "Celery 1.5"]));
// console.log(vegStore.revision());
