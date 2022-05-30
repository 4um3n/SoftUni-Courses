function townPopulation(data) {
    const result = {};

    for (let d of data) {
        [town, population] = d.split(' <-> ');
        (town in result) ? result[town] += Number(population) : result[town] = Number(population);
    }

    Object.entries(result).forEach(([k, v]) => {
        console.log(`${k} : ${v}`);
    });
}


townPopulation([
    'Sofia <-> 1200000',
    'Montana <-> 20000',
    'New York <-> 10000000',
    'Washington <-> 2345000',
    'Las Vegas <-> 1000000'
]);
townPopulation([
    'Istanbul <-> 100000',
    'Honk Kong <-> 2100004',
    'Jerusalem <-> 2352344',
    'Mexico City <-> 23401925',
    'Istanbul <-> 1000'
]);
