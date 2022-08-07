import {loginTemplate, registerTemplate} from "../templates/auth.js";
import {render} from "../lib.js";
import {get} from "../api/api.js";
import {clearUserData} from "../utils.js"
import { page } from '../lib.js';


export function registerView(ctx) {
    const template = registerTemplate();
    render(template, ctx.main);
}


export function loginView(ctx) {
    const template = loginTemplate();
    render(template, ctx.main);
}


export async function logoutView() {
    await get('/users/logout');
    clearUserData();
    page.redirect('/')
}