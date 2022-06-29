const { carService } = require('./car-service');
const { assert } = require('chai');


describe('Tests carService', function () {
    describe('Tests isItExpensive', function () {
        const expensiveIssues = ['Engine', 'Transmission'];

        it('should return the correct string when issue is expensive', function () {
            const expected = 'The issue with the car is more severe and it will cost more money';
            expensiveIssues.forEach(function (issue) {
                assert.equal(carService.isItExpensive(issue), expected);
            });
        });

        it('should return the correct string when issue is not expensive', function () {
            const expected = 'The overall price will be a bit cheaper';
            assert.equal(carService.isItExpensive('Not Expensive'), expected);
        });
    });

    describe('Tests discount', function () {
        const withoutDiscountParts = 2;
        const percent15DiscountParts = 7;
        const percent30DiscountParts = 8;
        const totalPrice = 100;

        it('should return the correct string when discount is not possible', function () {
            const expected = 'You cannot apply a discount';
            const result = carService.discount(withoutDiscountParts, totalPrice);
            assert.equal(result, expected);
        });

        it('should return the correct string when discount is 15%', function () {
            const expected = `Discount applied! You saved ${totalPrice * 0.15}$`;
            const result = carService.discount(percent15DiscountParts, totalPrice);
            assert.equal(result, expected);
        });

        it('should return the correct string when discount is 30%', function () {
            const expected = `Discount applied! You saved ${totalPrice * 0.30}$`;
            const result = carService.discount(percent30DiscountParts, totalPrice);
            assert.equal(result, expected);
        });

        it('should throw an Error when "numberOfParts" is not a Number', function () {
            function wrapper() {
                carService.discount('1', totalPrice);
            }
            assert.throws(wrapper, 'Invalid input');
        });

        it('should throw an Error when "totalPrice" is not a Number', function () {
            function wrapper() {
                carService.discount(withoutDiscountParts, '1');
            }
            assert.throws(wrapper, 'Invalid input');
        });
    });

    describe('Tests partsToBuy', function () {
        const partsCatalogue = [
            {
                part: "blowoff valve",
                price: 145
            },
            {
                part: "coil springs",
                price: 230
            }
        ];

        const neededParts = [
            "blowoff valve",
            "injectors"
        ];

        it('should return 0 when "partsCatalogue" is empty', function () {
            const expected = 0;
            const result = carService.partsToBuy([], neededParts);
            assert.equal(result, expected);
        });

        it('should return correct price when arguments are valid', function () {
            const expected = 145;
            const result = carService.partsToBuy(partsCatalogue, neededParts);
            assert.equal(result, expected);
        });

        it('should throw an Error when "partsCatalogue" is not an Array', function () {
            function wrapper() {
                carService.partsToBuy('1', neededParts);
            }
            assert.throws(wrapper, 'Invalid input')
        });

        it('should throw an Error when "neededParts" is not an Array', function () {
            function wrapper() {
                carService.partsToBuy(partsCatalogue, '1');
            }
            assert.throws(wrapper, 'Invalid input')
        });
    });
});
