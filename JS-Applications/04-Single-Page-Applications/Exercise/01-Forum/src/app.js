import { renderTopics } from "./topics.js";
import { container } from "./helpers.js";


function attachEvents() {
    window.addEventListener('load', onLoad);
    document.querySelector('nav a').addEventListener('click', home);
}


async function onLoad(event) {
    container.innerHTML = '';
    await renderTopics()
}


async function home() {
    await renderTopics();
}


attachEvents();
