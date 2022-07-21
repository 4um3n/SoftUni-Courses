import { html, render } from "https://unpkg.com/lit-html?module";

const form = document.querySelector('form');
const container = document.querySelector('#root');
attachEvents();

function attachEvents() {
    form.addEventListener('submit', onSubmit);
}


function onSubmit(event) {
    event.preventDefault();
    const formData = new FormData(form);
    const towns = formData.get('towns').split(', ')
    const HTMLTowns = getHTMLTowns(towns);
    render(HTMLTowns, container)
}


function getHTMLTowns(towns) {
    return html`
        <ul>
            ${towns.map(getHTMLTown)}
        </ul>
    `;
}


function getHTMLTown(town) {
    return html`
        <li>${town}</li>
    `
}