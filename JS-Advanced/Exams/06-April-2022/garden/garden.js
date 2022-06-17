class Garden {
    constructor(spaceAvailable) {
        this.spaceAvailable = spaceAvailable;
        this.plants = [];
        this.storage = [];
    }

    getPlantsNames() {
        return this.plants.map(el => el.plantName);
    }

    getPlant(plantName) {
        return this.plants.filter(el => el.plantName === plantName)[0];
    }

    removePlant(plantName) {
        const ind = this.plants.findIndex(el => el.plantName === plantName);
        this.plants.splice(ind, 1);
    }

    addPlant(plantName, spaceRequired) {
        if (this.spaceAvailable < spaceRequired) {
            throw new Error('Not enough space in the garden.');
        }

        this.plants.push({
            plantName,
            spaceRequired,
            'ripe': false,
            'quantity': 0
        });

        this.spaceAvailable -= spaceRequired;
        return `The ${plantName} has been successfully planted in the garden.`
    }

    ripenPlant(plantName, quantity) {
        if (!this.getPlantsNames().includes(plantName)) {
            throw new Error(`There is no ${plantName} in the garden.`);
        }

        if (this.getPlant(plantName).ripe) {
            throw new Error(`The ${plantName} is already ripe.`);
        }

        if (quantity <= 0) {
            throw new Error('The quantity cannot be zero or negative.');
        }

        const plant = this.getPlant(plantName);
        plant.quantity += quantity;
        plant.ripe = true;

        if (quantity > 1) {
            return `${quantity} ${plantName}s have successfully ripened.`
        }

        return `${quantity} ${plantName} has successfully ripened.`
    }


    harvestPlant(plantName) {
        if (!this.getPlantsNames().includes(plantName)) {
            throw new Error(`There is no ${plantName} in the garden.`);
        }

        if (!this.getPlant(plantName).ripe) {
            throw new Error(`The ${plantName} cannot be harvested before it is ripe.`);
        }

        const plant = this.getPlant(plantName);

        this.storage.push({
            plantName,
            'quantity': plant.quantity
        });

        this.spaceAvailable += plant.spaceRequired;
        this.removePlant(plantName);
        return `The ${plantName} has been successfully harvested.`
    }


    generateReport() {
        const plants = this.plants.map(plant => plant.plantName).sort((a, b) => a.localeCompare(b)).join(', ');
        let storage = this.storage.map(plant => `${plant.plantName} (${plant.quantity})`).join(', ');
        if (!storage) storage = 'The storage is empty.';

        return [
            `The garden has ${this.spaceAvailable} free space left.`,
            `Plants in the garden: ${plants}`,
            `Plants in storage: ${storage}`
        ].join('\n');
    }
}



// const myGarden = new Garden(250)
// console.log(myGarden.addPlant('apple', 20));
// console.log(myGarden.addPlant('orange', 200));
// console.log(myGarden.addPlant('olive', 50));


// const myGarden = new Garden(250)
// console.log(myGarden.addPlant('apple', 20));
// console.log(myGarden.addPlant('orange', 100));
// console.log(myGarden.addPlant('cucumber', 30));
// console.log(myGarden.ripenPlant('apple', 10));
// console.log(myGarden.ripenPlant('orange', 1));
// console.log(myGarden.ripenPlant('orange', 4));


// const myGarden = new Garden(250)
// console.log(myGarden.addPlant('apple', 20));
// console.log(myGarden.addPlant('orange', 100));
// console.log(myGarden.addPlant('cucumber', 30));
// console.log(myGarden.ripenPlant('apple', 10));
// console.log(myGarden.ripenPlant('orange', 1));
// console.log(myGarden.ripenPlant('olive', 30));


// const myGarden = new Garden(250)
// console.log(myGarden.addPlant('apple', 20));
// console.log(myGarden.addPlant('orange', 100));
// console.log(myGarden.addPlant('cucumber', 30));
// console.log(myGarden.ripenPlant('apple', 10));
// console.log(myGarden.ripenPlant('orange', 1));
// console.log(myGarden.ripenPlant('cucumber', -5));


// const myGarden = new Garden(250)
// console.log(myGarden.addPlant('apple', 20));
// console.log(myGarden.addPlant('orange', 200));
// console.log(myGarden.addPlant('raspberry', 10));
// console.log(myGarden.ripenPlant('apple', 10));
// console.log(myGarden.ripenPlant('orange', 1));
// console.log(myGarden.harvestPlant('apple'));
// console.log(myGarden.harvestPlant('olive'));


// const myGarden = new Garden(250)
// console.log(myGarden.addPlant('apple', 20));
// console.log(myGarden.addPlant('orange', 200));
// console.log(myGarden.addPlant('raspberry', 10));
// console.log(myGarden.ripenPlant('apple', 10));
// console.log(myGarden.ripenPlant('orange', 1));
// console.log(myGarden.harvestPlant('apple'));
// console.log(myGarden.harvestPlant('raspberry'));


// const myGarden = new Garden(250)
// console.log(myGarden.addPlant('apple', 20));
// console.log(myGarden.addPlant('orange', 200));
// console.log(myGarden.addPlant('raspberry', 10));
// console.log(myGarden.ripenPlant('apple', 10));
// console.log(myGarden.ripenPlant('orange', 1));
// console.log(myGarden.harvestPlant('orange'));
// console.log(myGarden.generateReport());
