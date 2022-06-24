const { companyAdministration } = require('./companyAdministration');
const { assert } = require('chai');


describe('Tests companyAdministration', function () {
    describe('Tests hiringEmployee', function () {
        const validYearsOfExperience = 3;
        const validName = 'Name';
        const validPosition = 'Programmer';

        it('should throw an Error when position is not a "Programmer"', function () {
            function wrapper() {
                companyAdministration.hiringEmployee(validName, 'notAProgrammer', validYearsOfExperience);
            }

            assert.throws(wrapper, `We are not looking for workers for this position.`)
        });

        it('should return correct string when the hire is successful', function () {
            const expected = `${validName} was successfully hired for the position ${validPosition}.`;
            const result = companyAdministration.hiringEmployee(validName, validPosition, validYearsOfExperience);
            assert.equal(result, expected);
        });

        it('should return correct string when the hire is not successful', function () {
            const expected = `${validName} is not approved for this position.`;
            const result = companyAdministration.hiringEmployee(validName, validPosition, 2);
            assert.equal(result, expected);
        });
    });

    describe('Tests calculateSalary', function () {
        const payPerHour = 15;
        const bonusMoney = 1000;
        const validHours = 160;
        const validBonusHours = 161;

        it('should return correctly calculated salary when hours <= 160', function () {
            const expected = validHours * payPerHour;
            const result = companyAdministration.calculateSalary(validHours);
            assert.equal(result, expected);
        });

        it('should return correctly calculated hours when hours > 160', function () {
            const expected = validBonusHours * payPerHour + bonusMoney;
            const result = companyAdministration.calculateSalary(validBonusHours);
            assert.equal(result, expected);
        });

        it('should throw an Error when "hours" is not a Number', function () {
            function wrapper() {
                companyAdministration.calculateSalary(validHours.toString());
            }

            assert.throws(wrapper, 'Invalid hours');
        });

        it('should throw an Error when "hours" is a negative number', function () {
            function wrapper() {
                companyAdministration.calculateSalary(-validHours);
            }

            assert.throws(wrapper, 'Invalid hours');
        });
    });

    describe('Test firedEmployee', function () {
        const validEmployees = ['Peter', 'Ivan', 'Georgi'];
        const validIndex = 2;

        it('should return correct string when removing the employee was successful', function () {
            const validEmployeesCopy = [...validEmployees]
            validEmployeesCopy.splice(validIndex, 1)
            const expected = validEmployeesCopy.join(', ');
            const result = companyAdministration.firedEmployee(validEmployees, validIndex);
            assert.equal(result, expected);
        });

        it('should throw an Error when passed array is not an Array', function () {
            function wrapper() {
                companyAdministration.firedEmployee('notAnArray', validIndex);
            }

            assert.throws(wrapper, 'Invalid input');
        });

        it('should throw an Error when passed index is not a Number', function () {
            function wrapper() {
                companyAdministration.firedEmployee(validEmployees, '1');
            }

            assert.throws(wrapper, 'Invalid input');
        });

        it('should throw an Error when passed index is outside the limits of the passed array', function () {
            function wrapper1() {
                companyAdministration.firedEmployee(validEmployees, validIndex - validEmployees.length);
            }

            function wrapper2() {
                companyAdministration.firedEmployee(validEmployees, validIndex + 1);
            }

            [wrapper1, wrapper2].forEach(func => assert.throws(func, 'Invalid input'));
        });
    });
});
