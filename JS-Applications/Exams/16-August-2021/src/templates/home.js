import {html} from "../lib.js";


export function homeTemplate(games) {
    const HTMLGames = (games.length <= 0) ? noGamesTemplate() : games.map(g => gameCardTemplate(g))
    return html`
        <!--Home Page-->
        <section id="welcome-world">

            <div class="welcome-message">
                <h2>ALL new games are</h2>
                <h3>Only in GamesPlay</h3>
            </div>
            <img src="../../images/four_slider_img01.png" alt="hero">

            <div id="home-page">
                <h1>Latest Games</h1>
                ${HTMLGames}
            </div>
        </section>
    `
}


function gameCardTemplate(game) {
    return html`
        <!-- Display div: with information about every game (if any) -->
        <div class="game">
            <div class="image-wrap">
                <img src=${game.imageUrl}>
            </div>
            <h3>${game.title}</h3>
            <div class="rating">
                <span>☆</span><span>☆</span><span>☆</span><span>☆</span><span>☆</span>
            </div>
            <div class="data-buttons">
                <a href="/game-details/${game._id}" class="btn details-btn">Details</a>
            </div>
        </div>
    `
}


function noGamesTemplate() {
    return html`
        <!-- Display paragraph: If there is no games  -->
        <p class="no-articles">No games yet</p>          
    `
}