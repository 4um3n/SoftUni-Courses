const {flowerShop} = require('./flowerShop');
const {assert} = require('chai');

describe('Test flowerShop', function () {
    const price = 5;
    const quantity = 10;
    const flower = 'Lily';
    const flowers = ["Rose", "Lily", "Orchid"];

    describe('Test calcPriceOfFlowers', function () {
        it('should return the correct string when success', function () {
            const expected = `You need $${(price * quantity).toFixed(2)} to buy ${flower}!`
            const result = flowerShop.calcPriceOfFlowers(flower, price, quantity);
            assert.equal(result, expected);
        });

        it('should raise Error when any of the arguments is invalid type', function () {
            [
                function () {
                    flowerShop.calcPriceOfFlowers(1, price, quantity);
                },
                function () {
                    flowerShop.calcPriceOfFlowers(flower, '1', quantity)
                },
                function () {
                    flowerShop.calcPriceOfFlowers(flower, price, '1')
                }
            ].forEach(func => assert.throws(func, 'Invalid input!'));
        });
    });

    describe('Test checkFlowersAvailable', function () {
        it('should return the correct string when flower in flowers', function () {
            const expected = `The ${flower} are available!`
            const result = flowerShop.checkFlowersAvailable(flower, flowers);
            assert.equal(result, expected);
        });

        it('should return the correct string when flower not in flowers', function () {
            const expected = `The ${flower} are sold! You need to purchase more!`
            const result = flowerShop.checkFlowersAvailable(flower, ['Test', 'test']);
            assert.equal(result, expected);
        });
    });

    describe('Test sellFlowers', function () {
        it('should return correct string when flower removed successfully', function () {
            const tmpFlowers = [...flowers];
            const result = flowerShop.sellFlowers(tmpFlowers, 1);
            tmpFlowers.splice(1, 1);
            const expected = tmpFlowers.join(' / ');
            assert.equal(result, expected);
        });

        it('should throw an Error when any of the arguments is invalid type', function () {
            [
                function () {
                    flowerShop.sellFlowers('test', 1);
                },
                function () {
                    flowerShop.sellFlowers(flowers, 'test');
                }
            ].forEach(func => assert.throws(func, 'Invalid input!'));
        });
    });
});
