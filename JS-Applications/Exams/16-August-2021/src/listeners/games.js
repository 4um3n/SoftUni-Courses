import {emptyFields} from "../utils.js";
import {createGame, updateGame} from "../api/games.js";
import {page} from "../lib.js";


export async function onCreateGame(event) {
    event.preventDefault();
    const formData = new FormData(event.target);

    if (emptyFields(...formData.values())) {
        return
    }

    const game = {
        "title": formData.get("title"),
        "category": formData.get("category"),
        "maxLevel": formData.get("maxLevel"),
        "imageUrl": formData.get("imageUrl"),
        "summary": formData.get("summary"),
    };

    await createGame(game);
    page.redirect("/");
}


export async function onUpdateGame(event) {
    event.preventDefault();
    const formData = new FormData(event.target);

    if (emptyFields(...formData.values())) {
        return
    }

    const game = {
        "title": formData.get("title"),
        "category": formData.get("category"),
        "maxLevel": formData.get("maxLevel"),
        "imageUrl": formData.get("imageUrl"),
        "summary": formData.get("summary"),
    };

    const gameId = event.target.dataId;
    await updateGame(game, gameId);
    page.redirect("/");
}
