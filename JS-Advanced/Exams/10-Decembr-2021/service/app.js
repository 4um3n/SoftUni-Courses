window.addEventListener('load', solve);

function solve() {
    const productTypeInputField = document.getElementById('type-product');
    const requiredFields = {
        'descriptionInputField': document.getElementById('description'),
        'clientNameInputField': document.getElementById('client-name'),
        'clientPhoneInputField': document.getElementById('client-phone')
    };

    document.querySelector('#right form').addEventListener('submit', handleForm);
    document.querySelector('#right button').addEventListener('click', sendForm);
    document.querySelector('button.clear-btn').addEventListener('click', clearCompletedRepairs);

    function handleForm(event) {
        event.preventDefault();
    }

    function emptyFields(...args) {
        return args.some(el => el.trim().length === 0);
    }

    function resetFields(...fields) {
        fields.forEach(function (field) {
            field.value = '';
        });
    }

    function getProblemContainer() {
        const container = document.createElement('div');
        const h2 = document.createElement('h2');
        const h3 = document.createElement('h3');
        const h4 = document.createElement('h4');
        const startBtn = document.createElement('button');
        const endBtn = document.createElement('button');

        h2.textContent = `Product type for repair: ${productTypeInputField.value}`;
        h3.textContent = `Client information: ${requiredFields.clientNameInputField.value}, ${requiredFields.clientPhoneInputField.value}`;
        h4.textContent = `Description of the problem: ${requiredFields.descriptionInputField.value}`;

        startBtn.textContent = 'Start repair';
        startBtn.classList.add('start-btn');
        startBtn.addEventListener('click', startRepair);

        endBtn.textContent = 'Finish repair';
        endBtn.classList.add('finish-btn');
        endBtn.disabled = true;
        endBtn.addEventListener('click', finishRepair);

        container.classList.add('container');
        [h2, h3, h4, startBtn, endBtn].forEach(
            el => container.appendChild(el)
        );

        resetFields(...Object.values(requiredFields));
        return container;
    }

    function sendForm(event) {
        if (!emptyFields(...Object.values(requiredFields).map(el => el.value))) {
            const container = getProblemContainer();
            document.getElementById('received-orders').appendChild(container);
        }
    }

    function startRepair(event) {
        event.target.parentElement.querySelector('button.finish-btn').disabled = false;
        event.target.disabled = true;
    }

    function finishRepair(event) {
        const container = event.target.parentElement;
        Array.from(container.querySelectorAll('button')).forEach(function (el) {
            el.parentElement.removeChild(el);
        });
        container.parentElement.removeChild(container);
        document.getElementById('completed-orders').appendChild(container);
    }

    function clearCompletedRepairs(event) {
        Array.from(event.target.parentElement.getElementsByClassName('container')).forEach(function (el) {
            el.parentElement.removeChild(el);
        });
    }
}
