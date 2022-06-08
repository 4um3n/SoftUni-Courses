function solve() {
    const buttons = document.querySelectorAll('button');
    const textAreas = document.querySelectorAll('textarea')
    buttons[0].addEventListener('click', generate);
    buttons[1].addEventListener('click', buy);

    function generate(event) {
        const data = JSON.parse(textAreas[0].value);

        for (const rowData of data) {
            const row = document.createElement('tr');

            const imageTd = document.createElement('td');
            const image = document.createElement('img');
            image.src = rowData['img'];
            imageTd.appendChild(image);

            const nameTd = document.createElement('td');
            nameTd.textContent = rowData['name'];

            const priceTd = document.createElement('td');
            priceTd.textContent = rowData['price'];

            const decorationFactorTd = document.createElement('td');
            decorationFactorTd.textContent = rowData['decFactor'];

            const markTd = document.createElement('td');
            const mark = document.createElement('input');
            mark.type = 'checkbox';
            markTd.appendChild(mark);

            row.appendChild(imageTd);
            row.appendChild(nameTd);
            row.appendChild(priceTd);
            row.appendChild(decorationFactorTd);
            row.appendChild(markTd);

            document.querySelector('tbody').appendChild(row);
        }
    }

    function buy(event) {
        const bought = Array.from(document.querySelectorAll('input[type=checkbox]')).filter(el => el.checked);
        const names = [];
        let totalPrice = 0;
        let totalDecFactor = 0;

        for (const product of bought) {
            const columns = product.parentElement.parentElement.children;
            names.push(columns[1].textContent);
            totalPrice += Number(columns[2].textContent);
            totalDecFactor += Number(columns[3].textContent);
        }

        totalDecFactor /= names.length;
        textAreas[1].value = [
            `Bought furniture: ${names.join(', ')}`,
            `Total price: ${totalPrice.toFixed(2)}`,
            `Average decoration factor: ${totalDecFactor}`
        ].join('\n');

    }
}
