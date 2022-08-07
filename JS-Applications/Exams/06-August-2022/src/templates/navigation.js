import {html} from "../lib.js";


export function guestNavigationTemplate() {
    return html`
        <div>
            <a href="/dashboard">Dashboard</a>
        </div>
        
        <!-- Guest users -->
        <div class="guest">
            <a href="/login">Login</a>
            <a href="/register">Register</a>
        </div>
    `
}


export function userNavigationTemplate() {
    return html`
        <div>
            <a href="/dashboard">Dashboard</a>
        </div>

        <!-- Logged-in users -->
        <div class="user">
            <a href="/create-offer">Create Offer</a>
            <a href="/logout">Logout</a>
        </div>
    `
}