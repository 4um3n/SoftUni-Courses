class CarDealership {
    constructor(name) {
        this.name = name;
        this.availableCars = [];
        this.soldCars = [];
        this.totalIncome = 0;
    }

    _negativeValues() {
        return Array.from(arguments).some(el => isNaN(el) || el < 0);
    }

    _getCarIndex(model) {
        for (let i = 0; i < this.availableCars.length; i++) {
            if (this.availableCars[i].model === model) {
                return i;
            }
        }

        return -1;
    }

    _makeBargain(carIndex, desiredMileage) {
        const car = this.availableCars[carIndex];

        if (car.mileage > desiredMileage) {
            if (Math.abs(car.mileage - desiredMileage) <= 40000) {
                car.price -= car.price * 0.05;
            } else {
                car.price -= car.price * 0.1;
            }
        }
    }

    addCar(model, horsepower, price, mileage) {
        horsepower = Number(horsepower);
        price = Number(price);
        mileage = Number(mileage);

        if (!model.trim() || this._negativeValues(horsepower, price, mileage)) {
            throw new Error('Invalid input!');
        }

        this.availableCars.push({
            model,
            horsepower: Number(horsepower),
            price: Number(price),
            mileage: Number(mileage)
        });

        return `New car added: ${model} - ${horsepower} HP - ${mileage.toFixed(2)} km - ${price.toFixed(2)}$`
    }

    sellCar(model, desiredMileage) {
        const searchedCarIndex = this._getCarIndex(model);

        if (searchedCarIndex < 0) {
            throw new Error(`${model} was not found!`);
        }

        this._makeBargain(searchedCarIndex, desiredMileage);
        const price = this.availableCars[searchedCarIndex].price
        this.totalIncome += price;
        this.soldCars.push(this.availableCars[searchedCarIndex]);
        this.availableCars.splice(searchedCarIndex, 1);
        return `${model} was sold for ${price.toFixed(2)}$`
    }

    currentCar() {
        if (this.availableCars.length === 0) {
            return 'There are no available cars';
        }

        const message = ['-Available cars:'];
        this.availableCars.forEach(function (car) {
            message.push(`---${car.model} - ${car.horsepower} HP - ${car.mileage.toFixed(2)} km - ${car.price.toFixed(2)}$`);
        });
        return message.join('\n');
    }

    salesReport(criteria) {
        const criteriaMapper = {
            'horsepower': (a, b) => b.horsepower - a.horsepower,
            'model': (a, b) => a.model.localeCompare(b.model)
        };

        if (!Object.keys(criteriaMapper).includes(criteria)) {
            throw new Error('Invalid criteria!');
        }

        this.soldCars.sort(criteriaMapper[criteria]);

        const message = [
            `-${this.name} has a total income of ${this.totalIncome.toFixed(2)}$`,
            `-${this.soldCars.length} cars sold:`
        ];

        this.soldCars.forEach(function (car) {
            message.push(`---${car.model} - ${car.horsepower} HP - ${car.price.toFixed(2)}$`);
        });

        return message.join('\n');
    }
}


// let dealership = new CarDealership('SoftAuto');
// console.log(dealership.addCar('Toyota Corolla', 100, 3500, 190000));
// console.log(dealership.addCar('Mercedes C63', 300, 29000, 187000));
// console.log(dealership.addCar('', 120, 4900, 240000));

// let dealership = new CarDealership('SoftAuto');
// dealership.addCar('Toyota Corolla', 100, 3500, 190000);
// dealership.addCar('Mercedes C63', 300, 29000, 187000);
// dealership.addCar('Audi A3', 120, 4900, 240000);
// console.log(dealership.sellCar('Toyota Corolla', 230000));
// console.log(dealership.sellCar('Mercedes C63', 110000));

// let dealership = new CarDealership('SoftAuto');
// dealership.addCar('Toyota Corolla', 100, 3500, 190000);
// dealership.addCar('Mercedes C63', 300, 29000, 187000);
// dealership.addCar('Audi A3', 120, 4900, 240000);
// console.log(dealership.currentCar());

// let dealership = new CarDealership('SoftAuto');
// dealership.addCar('Toyota Corolla', 100, 3500, 190000);
// dealership.addCar('Mercedes C63', 300, 29000, 187000);
// dealership.addCar('Audi A3', 120, 4900, 240000);
// dealership.sellCar('Toyota Corolla', 230000);
// dealership.sellCar('Mercedes C63', 110000);
// console.log(dealership.salesReport('horsepower'));
