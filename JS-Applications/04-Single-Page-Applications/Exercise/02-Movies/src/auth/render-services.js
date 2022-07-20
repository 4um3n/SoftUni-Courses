import { render } from 'https://unpkg.com/lit-html?module'
import { createRegisterView, createLoginView } from "./html-services.js";
const container = document.querySelector('#container');


export function renderRegisterView() {
    const registerView = createRegisterView();
    render(registerView, container);
}


export function renderLoginView() {
    const loginView = createLoginView();
    render(loginView, container);
}
