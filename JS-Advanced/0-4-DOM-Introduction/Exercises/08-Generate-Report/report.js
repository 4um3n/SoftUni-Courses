function generateReport() {
    const report = [];
    const tableHeaders = Array.from(document.querySelectorAll('table th'));
    const tableRows = Array.from(document.querySelectorAll('table tbody tr'));

    const columnsIndexes = tableHeaders.map(
        (el, ind) => [el, ind]
    ).filter(
        el => el[0].children[0].checked
    ).map(el => el[1]);

    for (let row of tableRows) {
        const tmpObj = {};

        for (let i of columnsIndexes) {
            const columnName = `${tableHeaders[i].textContent}`;
            tmpObj[columnName] = row.children[i].textContent;
        }

        if (Object.keys(tmpObj).length > 0) {
            report.push(tmpObj);
        }
    }

    document.getElementById('output').value = JSON.stringify(report);
}
