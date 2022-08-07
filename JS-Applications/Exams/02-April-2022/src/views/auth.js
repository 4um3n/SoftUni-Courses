import { render, page } from "../lib.js";
import { logout } from "../api/auth.js";
import { loginTemplate, registerTemplate } from "../templates/auth.js";
import { onRegister, onLogin } from "../listeners/auth.js";


export function loginView(ctx) {
    render(loginTemplate(onLogin), ctx.main);
}


export function registerView(ctx) {
    render(registerTemplate(onRegister), ctx.main);
}


export async function logoutView() {
    await logout();
    page.redirect('/');
}
