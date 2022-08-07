import { homeTemplate } from "../templates/home.js";
import { render } from "../lib.js";
import { getAllGames } from "../api/games.js";


export async function homeView(ctx) {
    const games = await getAllGames();
    render(homeTemplate(games), ctx.main);
}
