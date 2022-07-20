import { html } from 'https://unpkg.com/lit-html?module'
import { renderHomeView } from './movies/render-services.js';
import { renderLoginView, renderRegisterView } from "./auth/render-services.js";
import { onLogout } from "./auth/listeners.js";

export function createNavigation(user) {
    let buttons = html``;

    if (user) {
        buttons = html`
            <li class="nav-item user">
                <a class="nav-link" id="welcome-msg">Welcome, ${user.email}</a>
            </li>
            <li class="nav-item user">
                <a @click=${onLogout} id="logout-link" class="nav-link" href="#">Logout</a>
            </li>
        `
    } else {
        buttons = html`
            <li class="nav-item guest">
                <a @click=${renderLoginView} id="login-link"class="nav-link" href="#">Login</a>
            </li>
            <li class="nav-item guest">
                <a @click=${renderRegisterView} id="register-link" class="nav-link" href="#">Register</a>
            </li>
        `
    }

    return html`
        <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
            <a @click=${ renderHomeView } class="navbar-brand text-light" href="#">Movies</a>
            <ul class="navbar-nav ml-auto">
                ${buttons}
            </ul>
        </nav>
    `
}


export function createFooter() {
    return html`
        <footer class="page-footer font-small">
            <div class="footer-copyright text-center py-3">
                &copy; 2020
                <a href="#" class="text-dark">JS Applications</a>
            </div>
        </footer>
    `
}
