const { rentCar } = require('./rentCar');
const { assert } = require('chai');


describe('Tests rentCar', function () {
    describe('Tests searchCar', function () {
        it('should return string when success', function () {
            const cars = ['Volkswagen', 'BMW', 'Audi', 'BMW'];
            const searched = 'BMW';
            const expected = `There is ${cars.filter(el => el === searched).length} car of model ${searched} in the catalog!`
            const result = rentCar.searchCar(cars, searched);
            assert.equal(result, expected);
        });

        it('should throw an Error when input is invalid', function () {
            const wrapper1 = function() {
                rentCar.searchCar('', 'BMW');
            }
            const wrapper2 = function() {
                rentCar.searchCar([], []);
            }
            assert.throws(wrapper1, `Invalid input!`);
            assert.throws(wrapper2, `Invalid input!`);
        });

        it('should throw an Error when searched car is not met', function () {
            const wrapper = function() {
                rentCar.searchCar([], 'BMW')
            }
            assert.throws(wrapper, 'There are no such models in the catalog!');
        });
    });

    describe('Tests calculatePriceOfCar', function () {
        it('should return string when success', function () {
            const cars = {
                Volkswagen: 20,
                Audi: 36,
                Toyota: 40,
                BMW: 45,
                Mercedes: 50
            };
            const searchedCar = 'BMW';
            const days = 2;
            const expected = `You choose ${searchedCar} and it will cost $${cars[searchedCar] * days}!`;
            const result = rentCar.calculatePriceOfCar(searchedCar, days);
            assert.equal(result, expected);
        });

        it('should throw an Error when input is invalid', function () {
            const wrapper1 = function() {
                rentCar.calculatePriceOfCar(1, 1);
            }
            const wrapper2 = function() {
                rentCar.calculatePriceOfCar('BMW', 'NaN');
            }
            assert.throws(wrapper1, `Invalid input!`);
            assert.throws(wrapper2, `Invalid input!`);
        });

        it('should throw an Error when searched car is not met', function () {
            const wrapper = function() {
                rentCar.calculatePriceOfCar('Not in cars', 2);
            }
            assert.throws(wrapper, 'No such model in the catalog!');
        });
    });

    describe('Tests checkBudget', function () {
        it('should return correct string when budget is enough', function () {
            const [perDay, days, budget] = [5, 2, 10];
            const expected = 'You rent a car!';
            const result = rentCar.checkBudget(perDay, days, budget);
            assert.equal(result, expected);
        });

        it('should return correct string when budget is not enough', function () {
            const [perDay, days, budget] = [5, 2, 9];
            const expected = 'You need a bigger budget!';
            const result = rentCar.checkBudget(perDay, days, budget);
            assert.equal(result, expected);
        });

        it('should throw an Error when input is invalid', function () {
            function wrapper1() {
                const [perDay, days, budget] = [[], 2, 9];
                rentCar.checkBudget(perDay, days, budget);
            }
            function wrapper2() {
                const [perDay, days, budget] = [5, [], 9];
                rentCar.checkBudget(perDay, days, budget);
            }
            function wrapper3() {
                const [perDay, days, budget] = [5, 2, []];
                rentCar.checkBudget(perDay, days, budget);
            }
            [wrapper1, wrapper2, wrapper3].forEach(
                func => assert.throws(func, 'Invalid input!')
            );
        });
    });
});
