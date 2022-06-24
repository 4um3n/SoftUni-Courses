function solve() {
    const inputFields = {
         firstNameInputField: document.getElementById('fname'),
         lastNameInputField: document.getElementById('lname'),
         emailInputField: document.getElementById('email'),
         birthInputField: document.getElementById('birth'),
         positionInputField: document.getElementById('position'),
         salaryInputField: document.getElementById('salary')
    }
    const hireButton = document.getElementById('add-worker');
    const salaryBudgetSum = document.getElementById('sum');

    hireButton.type = 'button';
    hireButton.addEventListener('click', addWorker)

    function emptyFields(...args) {
        return args.some(el => el.trim().length === 0);
    }

    function getTableRow(...values) {
        const tableRow = document.createElement('tr');
        const fireButton = document.createElement('button');
        const editButton = document.createElement('button');

        values.forEach(function(value) {
            const tableColumn = document.createElement('td');
            tableColumn.textContent = value;
            tableRow.appendChild(tableColumn);
        });

        fireButton.textContent = 'Fired';
        fireButton.classList.add('fired');
        fireButton.addEventListener('click', fireWorker);

        editButton.textContent = 'Edit';
        editButton.classList.add('edit');
        editButton.addEventListener('click', editWorker);

        const tableColumn = document.createElement('td');
        tableColumn.appendChild(fireButton);
        tableColumn.appendChild(editButton);
        tableRow.appendChild(tableColumn);
        return tableRow;
    }

    function resetFields(...fields) {
        fields.forEach(function(field) {
            field.value = '';
        });
    }

    function changeBudget(value, operation) {
        const operations = {
            '+': function () {
                salaryBudgetSum.textContent = (Number(salaryBudgetSum.textContent) + Number(value)).toFixed(2);
            },
            '-': function () {
                salaryBudgetSum.textContent = (Number(salaryBudgetSum.textContent) - Number(value)).toFixed(2);
            }
        };
        operations[operation]();
    }

    function addWorker(event) {
        const fieldsValues = Object.values(inputFields).map(el => el.value);
        if (!emptyFields(...fieldsValues)) {
             document.getElementById('tbody').appendChild(getTableRow(...fieldsValues));
             changeBudget(inputFields["salaryInputField"].value, '+');
             resetFields(...Object.values(inputFields));
        }
    }

    function editWorker(event) {
        const tableRow = event.target.parentElement.parentElement;
        const workerData = Array.from(tableRow.children).slice(0, -1).map(el => el.textContent);

        Object.keys(inputFields).forEach(function (key, index) {
            inputFields[key].value = workerData[index];
        });

        changeBudget(workerData[workerData.length - 1], '-');
        tableRow.parentElement.removeChild(tableRow);
    }

    function fireWorker(event) {
        const tableRow = event.target.parentElement.parentElement;
        const salary = Array.from(tableRow.children).slice(-2, -1)[0].textContent;
        changeBudget(salary, '-');
        tableRow.parentElement.removeChild(tableRow);
    }
}

solve()
