import { page, render } from "../lib.js";
import { createGamesTemplate, editGameTemplate , gameDetailsTemplate } from "../templates/games.js";
import { onCreateGame, onUpdateGame } from "../listeners/games.js";
import { getGameById, getDonations, deleteGame, donate } from "../api/games.js";


export function createGamesView(ctx) {
    const template = createGamesTemplate(onCreateGame);
    render(template, ctx.main);
}


export async function editGameView(ctx) {
    const gameId = ctx.params.id;
    const game = await getGameById(gameId);
    const template = editGameTemplate(game, onUpdateGame);
    render(template, ctx.main);
}


export async function deleteGameView(ctx) {
    const gameId = ctx.params.id;
    const sure = confirm("Are you sure?");

    if (sure) {
        await deleteGame(gameId);
        page.redirect("/");
    }

}


export async function gameDetailsView(ctx) {
    const gameId = ctx.params.id;
    const game = await getGameById(gameId);
    const template = await gameDetailsTemplate(game);
    render(template, ctx.main);
}


export async function donateView(ctx) {
    const gameId = ctx.params.id;
    await donate(gameId);
    page.redirect(`/pet-details/${gameId}`);
}
