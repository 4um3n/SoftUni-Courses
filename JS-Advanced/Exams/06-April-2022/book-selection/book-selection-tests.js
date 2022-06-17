const {assert, expect} = require('chai');
const {bookSelection} = require('./bookSelection');


describe('Tests bookSelection', function () {
    describe('Tests isGenreSuitable', function () {
        it('should return "Books with ${genre} genre are not suitable for kids at ${age} age"', function () {
            const age = 12;
            const genres = ['Thriller', 'Horror'];

            for (const genre of genres) {
                const result = bookSelection.isGenreSuitable(genre, age);
                const expected = `Books with ${genre} genre are not suitable for kids at ${age} age`;
                assert.equal(result, expected);
            }
        });

        it('should return "Those books are suitable" when is not a kid', function () {
            const genres = ['Thriller', 'Horror'];

            for (const genre of genres) {
                const result = bookSelection.isGenreSuitable(genre, 13);
                const expected = `Those books are suitable`;
                assert.equal(result, expected);
            }
        });
    });

    describe('Tests isItAffordable', function () {
        it('test when budget is enough expect success', function () {
            const price = 9;
            const budget = 10;
            const expected = `Book bought. You have ${budget - price}$ left`;
            const result = bookSelection.isItAffordable(price, budget);
            assert.equal(expected, result);
        });

        it('test when budget is not enough', function () {
            const price = 10;
            const budget = 9;
            const expected = `You don't have enough money`;
            const result = bookSelection.isItAffordable(price, budget);
            assert.equal(expected, result);
        });

        it('test when price and budget are not numbers expect to raise', function () {
            expect(bookSelection.isItAffordable).to.throw('Invalid input');
        });
    });

    describe('Tests suitableTitles', function () {
        it('should return an array with objects', function () {
            const expected = ['test1', 'test2'];
            const arr = [
                {
                    title: 'test1',
                    genre: 'test genre'
                },
                {
                    title: 'test2',
                    genre: 'test genre'
                },
                {
                    title: 'test3',
                    genre: 'test'
                },
            ];

            const result = bookSelection.suitableTitles(arr, 'test genre');
            assert.equal(JSON.stringify(expected), JSON.stringify(result));
        });

        it('should raise Error("Invalid input")', function () {
            expect(bookSelection.suitableTitles).to.throw('Invalid input');
        });
    });
});