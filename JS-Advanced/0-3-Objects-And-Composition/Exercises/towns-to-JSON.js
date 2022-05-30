function townsToJSON(data) {
    const resultData = [];
    data.shift();

    for (let line of data) {
        let [town, lat, long] = line.split('|').filter(x => x).map(x => x.trim());

        lat = +(Number(lat).toFixed(2));
        long = +(Number(long).toFixed(2));

        resultData.push({
            'Town': town,
            'Latitude': lat,
            'Longitude': long
        });
    }

    return JSON.stringify(resultData);
}


console.log(townsToJSON(
    [
        '| Town | Latitude | Longitude |',
        '| Sofia | 42.696552 | 23.32601 |',
        '| Beijing | 39.913818 | 116.363625 |'
    ]
));
