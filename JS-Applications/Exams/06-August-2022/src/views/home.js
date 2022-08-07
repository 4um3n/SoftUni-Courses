import { homeTemplate, dashboardTemplate } from "../templates/home.js";
import { render } from "../lib.js";
import { getAllOffers } from "../api/offers.js";


export function homeView(ctx) {
    render(homeTemplate(), ctx.main);
}


export async function dashboardView(ctx) {
    const offers = await getAllOffers();
    render(dashboardTemplate(offers), ctx.main);
}