class Company {
    constructor() {
        this.departments = {};
    }

    _checkArguments(...args) {
        return args.every(el => el);
    }

    _getBestDepartment() {
        let bestDepartment;
        let bestAverageSalary = 0;

        for (const [department, employees] of Object.entries(this.departments)) {
            const averageSalary = employees.map(emp => emp.salary).reduce((a, c) => a + c) / employees.length;

            if (bestAverageSalary < averageSalary) {
                bestAverageSalary = averageSalary;
                bestDepartment = department;
            }
        }

        return [bestDepartment, bestAverageSalary];


    }

    addEmployee(username, salary, position, department) {
        if (!this._checkArguments(username, salary, position, department)) {
            throw new Error('Invalid input!');
        }

        if (salary < 0) {
            throw new Error('Invalid input!');
        }

        if (!Object.keys(this.departments).includes(department)) {
            this.departments[department] = [];
        }

        this.departments[department].push({
            username,
            salary,
            position,
        });

        return `New employee is hired. Name: ${username}. Position: ${position}`;
    }

    bestDepartment() {
        const [bestDepartment, bestAveragesalary] = this._getBestDepartment();
        const message = [
            `Best Department is: ${bestDepartment}`,
            `Average salary: ${bestAveragesalary.toFixed(2)}`
        ];

        this.departments[bestDepartment].sort(function (a, b) {
            if (a.salary > b.salary) {
                return -1
            } else if (a.salary < b.salary) {
                return 1
            }
            return a.username.localeCompare(b.username);
        }).forEach(function (employee) {
            message.push(`${employee.username} ${employee.salary} ${employee.position}`);
        });

        return message.join('\n');
    }
}
