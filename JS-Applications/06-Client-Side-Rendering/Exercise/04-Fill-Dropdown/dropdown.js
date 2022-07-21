import {html, render} from './node_modules/lit-html/lit-html.js';


const selectContainer = document.querySelector('#menu');
const form = document.querySelector('form');
attachEvents();


function attachEvents() {
    window.addEventListener('load', onLoad);
    form.addEventListener('submit', onSubmit);
}


async function onLoad() {
    await renderOptions();
}


async function onSubmit(event) {
    event.preventDefault();
    const formData = new FormData(form);
    const init = {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            'text': formData.get('text')
        })
    }

    try {
        await sendRequest('http://localhost:3030/jsonstore/advanced/dropdown', init);
        await renderOptions();
        form.reset();
    } catch (error) {
        alert(error.message);
    }

}


async function renderOptions() {
    try {
        const data = await sendRequest('http://localhost:3030/jsonstore/advanced/dropdown');
        const HTMLOptions = Object.values(data).map(createHTMLOption);
        render(HTMLOptions, selectContainer);
    } catch (error) {
        alert(error.message);
    }
}


function createHTMLOption(option) {
    return html`
        <option value="${option._id}">${option.text}</option>
    `
}

async function sendRequest(url, init) {
    const response = await fetch(url, init);
    const data = await response.json();

    if (response.status !== 200) {
        throw new Error(data.message);
    }

    return data;
}