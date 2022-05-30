function fromJSONToHTML(data) {
    const table = {};
    const result = ['<table>'];

    if (data.length > 0) {
        for (const key of data[0].keys()) {
            table[key] = [];
        }
    }

    for (const obj of data) {
        for (let [k, v] of Object.entries(obj)) {
            table[k].push(v);
        }
    }

    const heading = table.keys();
    const th = ['    <tr>'];
    for (const head of heading) {
        th.push(['<th>', `${head}`, '</th>'].join(''));
    }
    th.push('</tr>');
}

