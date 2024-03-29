import { guestNavigationTemplate, userNavigationTemplate } from "./templates/navigation.js";
import { render } from "./lib.js";
import { getUserData } from "./utils.js";


const main = document.querySelector('#content');
const nav = document.querySelector('header nav ul');


export function decorateContext(ctx, next) {
    ctx.main = main;
    next();
}


export function setUpNavigation(ctx, next) {
    const buttons = (getUserData()) ? userNavigationTemplate() : guestNavigationTemplate();
    render(buttons, nav);
    next();
}
