import {html} from "../lib.js";


export function guestNavigationTemplate() {
    return html`
        <!--Users and Guest-->
        <li><a href="/">Home</a></li>
        <li><a href="/dashboard">Dashboard</a></li>
        <!--Only Guest-->
        <li><a href="/login">Login</a></li>
        <li><a href="/register">Register</a></li>
    `
}


export function userNavigationTemplate() {
    return html`
        <!--Users and Guest-->
        <li><a href="/">Home</a></li>
        <li><a href="/dashboard">Dashboard</a></li>
        <!--Only Users-->
        <li><a href="/create-pet">Create Postcard</a></li>
        <li><a href="/logout">Logout</a></li>
    `
}