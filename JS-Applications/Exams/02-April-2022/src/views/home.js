import { homeTemplate, dashboardTemplate } from "../templates/home.js";
import { render } from "../lib.js";
import { getAllPets } from "../api/pets.js";


export function homeView(ctx) {
    render(homeTemplate(), ctx.main);
}


export async function dashboardView(ctx) {
    const pets = await getAllPets();
    render(dashboardTemplate(pets), ctx.main);
}