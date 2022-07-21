import { towns } from "./towns.js";
import { html, render } from "https://unpkg.com/lit-html?module";


const container = document.querySelector('#towns');
const result = document.querySelector('#result');
const input = document.querySelector('#searchText');
attachEvents();


function attachEvents() {
    window.addEventListener('load', () => renderTowns(towns.map(t => createHTMLTown(t, ''))));
    document.querySelector('button').addEventListener('click', onSearch);
}

function onSearch() {
    const filteredTowns = search(towns, input.value);
    const HTMLTowns = towns.map(
        town => createHTMLTown(
            town, filteredTowns.includes(town) ? 'active' : ''
    ));
    renderTowns(HTMLTowns, container);
    result.textContent = `${filteredTowns.length} matches found`;
}


function search(towns, value) {
    value = value.toLowerCase();

    return towns.filter(
        town => town.toLowerCase().includes(value) || value.includes(town.toLowerCase())
    );
}


function createHTMLTown(town, active) {
    return html`
        <li class="${active}" >${town}</li>
    `;
}

function renderTowns(towns) {
    const ul = html`
        <ul>
            ${towns}
        </ul>
    `;
    render(ul, container);
}


