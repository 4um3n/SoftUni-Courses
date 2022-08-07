import {html} from "../lib.js";

export function userNavigationTemplate() {
    return html`
        <a href="/">Dashboard</a>
        <!-- Logged-in users -->
        <div id="user">
            <a href="/my-posts">My Posts</a>
            <a href="/create-post">Create Post</a>
            <a href="/logout">Logout</a>
        </div>
    `
}


export function guestNavigationTemplate() {
    return html`
        <a href="/">Dashboard</a>
        <!-- Guest users -->
        <div id="guest">
            <a href="/login">Login</a>
            <a href="/register">Register</a>
        </div>
    `
}

