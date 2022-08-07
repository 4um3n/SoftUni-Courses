import { html } from "../lib.js";
import { getUserData } from "../utils.js";
import { userDonated } from "../api/games.js";


export function createGamesTemplate(onSubmit) {
    return html`
        <!-- Create Page ( Only for logged-in users ) -->
        <section id="create-page" class="auth">
            <form @submit="${onSubmit}" id="create">
                <div class="container">

                    <h1>Create Game</h1>
                    <label for="leg-title">Legendary title:</label>
                    <input type="text" id="title" name="title" placeholder="Enter game title...">

                    <label for="category">Category:</label>
                    <input type="text" id="category" name="category" placeholder="Enter game category...">

                    <label for="levels">MaxLevel:</label>
                    <input type="number" id="maxLevel" name="maxLevel" min="1" placeholder="1">

                    <label for="game-img">Image:</label>
                    <input type="text" id="imageUrl" name="imageUrl" placeholder="Upload a photo...">

                    <label for="summary">Summary:</label>
                    <textarea name="summary" id="summary"></textarea>
                    <input class="btn submit" type="submit" value="Create Game">
                </div>
            </form>
        </section>
    `
}


export function editGameTemplate(game, onSubmit) {
    return html`
        <!-- Edit Page ( Only for the creator )-->
        <section id="edit-page" class="auth">
            <form @submit="${onSubmit}" dataId=${game._id} id="edit">
                <div class="container">

                    <h1>Edit Game</h1>
                    <label for="leg-title">Legendary title:</label>
                    <input type="text" id="title" name="title" value=${game.title}>

                    <label for="category">Category:</label>
                    <input type="text" id="category" name="category" value=${game.category}>

                    <label for="levels">MaxLevel:</label>
                    <input type="number" id="maxLevel" name="maxLevel" min="1" value=${game.maxLevel}>

                    <label for="game-img">Image:</label>
                    <input type="text" id="imageUrl" name="imageUrl" value=${game.imageUrl}>

                    <label for="summary">Summary:</label>
                    <textarea name="summary" id="summary">${game.summary}</textarea>
                    <input class="btn submit" type="submit" value="Edit Game">

                </div>
            </form>
        </section>
    `
}


export async function gameDetailsTemplate(game, comments) {
    const HTMLComments = (comments.length <= 0) ? noCommentsTemplate() : commentsTemplate(comments);
    const user = getUserData();
    let buttons;
    let bonus;

    if (user) {
        if (game._ownerId === user.id) {
            buttons = creatorButtonsTemplate(game._id);
        } else {
            bonus = addCommentsTemplate(game._id);
        }
    }

    return html`
        <!--Details Page-->
        <section id="game-details">
            <h1>Game Details</h1>
            <div class="info-section">

                <div class="game-header">
                    <img class="game-img" src=${game.imageUrl}/>
                    <h1>${game.title}</h1>
                    <span class="levels">MaxLevel: ${game.maxLevel}</span>
                    <p class="type">${game.category}</p>
                </div>

                <p class="text">${game.summary}</p>

                <!-- Bonus ( for Guests and Users ) -->
                <div class="details-comments">
                    <h2>Comments:</h2>
                    ${HTMLComments}                    
                </div>
                
                ${buttons}

            </div>

            ${bonus}

        </section>
    `
}


function creatorButtonsTemplate(gameId) {
    return html`
        <!-- Edit/Delete buttons ( Only for creator of this game )  -->
        <div class="buttons">
            <a href="/edit-game/${gameId}" class="button">Edit</a>
            <a href="/delete-game/${gameId}" class="button">Delete</a>
        </div>
    `
}


function addCommentsTemplate(gameId) {
    return html`
        <!-- Bonus -->
        <!-- Add Comment ( Only for logged-in users, which is not creators of the current game ) -->
        <article class="create-comment">
            <label>Add new comment:</label>
            <form class="form">
                <textarea name="comment" placeholder="Comment......"></textarea>
                <input class="btn submit" type="submit" value="Add Comment">
            </form>
        </article>
    `
}


function commentsTemplate(comments) {
    return html`
        <ul>
            <!-- list all comments for current game (If any) -->
            ${comments.map(c => commentTemplate(c))}            
        </ul>
    `
}


function commentTemplate() {
    return html`
        <li class="comment">
            <p>Content: The best game.</p>
        </li>
    `
}


function noCommentsTemplate() {
    return html`
        <!-- Display paragraph: If there are no games in the database -->
        <p class="no-comment">No comments.</p>
    `
}

