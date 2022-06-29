window.addEventListener("load", solve);

function solve() {
    const tableBody = document.getElementById('table-body');
    const publishBtn = document.getElementById('publish');
    const totalProfitSum = document.getElementById('profit');
    const inputFields = {
        'make': document.getElementById('make'),
        'model': document.getElementById('model'),
        'year': document.getElementById('year'),
        'fuel': document.getElementById('fuel'),
        'originalPrice': document.getElementById('original-cost'),
        'sellingPrice': document.getElementById('selling-price')
    };

    document.querySelector('div.form-wrapper form').addEventListener('submit', handleForm);
    publishBtn.addEventListener('click', publish);

    function getInputFieldsValues() {
        return Object.values(inputFields).map(el => el.value);
    }

    function setInputFieldsValues(...values) {
        Object.values(inputFields).map(function (el, ind) {
            el.value = values[ind];
        })
    }

    function isPriceInCriteria() {
        return Number(inputFields['originalPrice'].value) < Number(inputFields['sellingPrice'].value);
    }

    function emptyFields(...args) {
        return args.some(el => el.trim().length === 0);
    }

    function resetFields(...fields) {
        const values = {
            'make': '',
            'model': '',
            'year': '',
            'fuel': '',
            'original-cost': '',
            'selling-price': ''
        };

        fields.forEach(function(field) {
            field.value = values[field.id];
        });
    }

    function handleForm(event) {
        event.preventDefault();
    }

    function publish(event) {
        if (!emptyFields(...getInputFieldsValues()) && isPriceInCriteria()) {
            let [make, model, year, fuel, originalPrice, sellingPrice] = getInputFieldsValues();
            const tr = document.createElement('tr');
            const makeTd = document.createElement('td');
            const modelTd = document.createElement('td');
            const yearTd = document.createElement('td');
            const fuelTd = document.createElement('td');
            const originalPriceTd = document.createElement('td');
            const sellingPriceTd = document.createElement('td');
            const buttonsWrapper = document.createElement('td');
            const editBtn = document.createElement('button');
            const sellBtn = document.createElement('button');


            tr.classList.add('row');
            makeTd.textContent = make;
            modelTd.textContent = model;
            yearTd.textContent = year;
            fuelTd.textContent = fuel;
            originalPriceTd.textContent = originalPrice.toString();
            sellingPriceTd.textContent = sellingPrice.toString();

            editBtn.textContent = 'Edit';
            editBtn.classList.add('action-btn', 'edit');
            editBtn.addEventListener('click', edit);

            sellBtn.textContent = 'Sell';
            sellBtn.classList.add('action-btn', 'sell');
            sellBtn.addEventListener('click', sell);

            buttonsWrapper.appendChild(editBtn);
            buttonsWrapper.appendChild(sellBtn);

            [makeTd, modelTd, yearTd, fuelTd, originalPriceTd, sellingPriceTd].forEach(function (el) {
                tr.appendChild(el);
            });
            tr.appendChild(buttonsWrapper);
            tableBody.appendChild(tr);

            resetFields(...Object.values(inputFields));
        }
    }

    function edit(event) {
        const parent = event.target.parentElement.parentElement;
        const inputFields = Array.from(parent.children);
        inputFields.splice(-1, 1);
        setInputFieldsValues(...inputFields.map(el => el.textContent));
        parent.parentElement.removeChild(parent);
    }

    function sell(event) {
        const parent = event.target.parentElement.parentElement;
        const li = document.createElement('li');
        const model = document.createElement('span');
        const year = document.createElement('span');
        const profitMade = document.createElement('span');

        let inputFields = Array.from(parent.children);
        inputFields.splice(-1, 1);
        inputFields = inputFields.map(el => el.textContent);
        const profit = Number(inputFields[inputFields.length - 1]) - Number(inputFields[inputFields.length - 2]);
        totalProfitSum.textContent = (Number(totalProfitSum.textContent) + profit).toFixed(2)

        model.textContent = `${inputFields[0]} ${inputFields[1]}`;
        year.textContent = inputFields[2];
        profitMade.textContent = profit.toString();

        li.classList.add('each-list');
        [model, year, profitMade].forEach(function (el) {
            li.appendChild(el);
        });

        document.getElementById('cars-list').appendChild(li);
        parent.parentElement.removeChild(parent);
    }
}
