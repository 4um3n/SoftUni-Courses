import {renderAddForm, renderPage} from "./views.js";


attachEvents();

function attachEvents() {
    window.addEventListener('load', onLoad);
}


async function onLoad() {
    renderPage();
    renderAddForm();
}