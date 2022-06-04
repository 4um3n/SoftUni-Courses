function solve() {
    document.querySelector('#btnSend').addEventListener('click', onClick);

    function onClick() {
        const restaurants = {};
        let bestRestaurantName = '';
        let bestAverageSalary = 0;
        const data = JSON.parse(document.querySelector('textarea').value);

        for (let line of data) {
            const data = line.split(' - ');
            const restaurantName = data.shift();
            const workersData = data[0].split(', ');
            let tmpAverageSalary = 0;

            if (!(restaurants.hasOwnProperty(restaurantName))) {
                restaurants[restaurantName] = {};
            }

            for (let workerData of workersData) {
                let [worker, salary] = workerData.split(' ');
                restaurants[restaurantName][worker] = Number(salary);
                tmpAverageSalary += Number(salary);
            }

            tmpAverageSalary /= Object.keys(restaurants[restaurantName]).length;

            if (tmpAverageSalary > bestAverageSalary) {
                bestAverageSalary = tmpAverageSalary;
                bestRestaurantName = restaurantName;
            }
        }

        const bestRestaurantSalary = Math.max(...Object.values(restaurants[bestRestaurantName]));
        const bestRestaurantResult = `Name: ${bestRestaurantName} Average Salary: ${bestAverageSalary.toFixed(2)} Best Salary: ${bestRestaurantSalary.toFixed(2)}`
        const bestRestaurantWorkers = Object.entries(restaurants[bestRestaurantName]).sort(
            (a, b) => b[1] - a[1]
        ).map(
            el => `Name: ${el[0]} With Salary: ${el[1]}`
        ).join(' ');

        document.querySelector('#bestRestaurant p').textContent = bestRestaurantResult;
        document.querySelector('#workers p').textContent = bestRestaurantWorkers;
    }
}
