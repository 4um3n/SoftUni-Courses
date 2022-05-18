function evenPositionElement (data) {
    let filteredData = [];

    while (data.length > 0) {
        filteredData.push(data.shift());
        data.shift();
    }

    console.log(filteredData.join(' '));
}


evenPositionElement(['20', '30', '40', '50', '60']);
evenPositionElement(['5', '10']);
