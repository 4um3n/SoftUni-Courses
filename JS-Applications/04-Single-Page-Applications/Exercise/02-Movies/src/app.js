import { renderHomeView } from "./movies/render-services.js";

attachEvents();


function attachEvents() {
    window.addEventListener('load', onLoad);
}


async function onLoad() {
    await renderHomeView();
}
