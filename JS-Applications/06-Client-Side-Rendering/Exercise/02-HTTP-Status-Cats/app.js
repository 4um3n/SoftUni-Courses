import { cats } from "./catSeeder.js";
import { html, render } from "https://unpkg.com/lit-html?module";
const container = document.querySelector('#allCats');
render(createHTMLCats(cats), container);


function toggleCard(event) {
    const button = event.target;
    const card = button.parentElement.querySelector('div.status');

    if (card.style.display === 'none') {
        button.textContent = 'Hide status code';
        card.style.display = 'block';
    } else {
        button.textContent = 'Show status code';
        card.style.display = 'none';
    }
}


function createHTMLCatCard(cat) {
    return html`
        <li>
            <img src="./images/${cat.imageLocation}.jpg" width="250" height="250" alt="Card image cap">
            <div class="info">
                <button @click=${toggleCard} class="showBtn">Show status code</button>
                <div class="status" style="display: none" id="${cat.statusCode}">
                    <h4>Status Code: ${cat.statusCode}</h4>
                    <p>${cat.statusMessage}</p>
                </div>
            </div>
        </li>
    `
}

function createHTMLCats(cats) {
    return html`
        <ul>
            ${cats.map(createHTMLCatCard)}
        </ul>
    `
}
