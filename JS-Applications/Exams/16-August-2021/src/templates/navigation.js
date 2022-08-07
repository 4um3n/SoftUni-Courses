import {html} from "../lib.js";


export function guestNavigationTemplate() {
    return html`
        <a href="/dashboard">All games</a>
        <!-- Guest users -->
        <div id="guest">
            <a href="/login">Login</a>
            <a href="/register">Register</a>
        </div>
    `
}


export function userNavigationTemplate() {
    return html`
        <a href="/dashboard">All games</a>
        <!-- Logged-in users -->
        <div id="user">
            <a href="/create-game">Create Game</a>
            <a href="/logout">Logout</a>
        </div>
    `
}