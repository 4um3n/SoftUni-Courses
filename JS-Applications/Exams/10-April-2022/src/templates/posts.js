import {html} from "../lib.js";
import {onCreatePost, onEditPost} from "../listeners/posts.js";


export function createPostTemplate() {
    return html`
        <!-- Create Page (Only for logged-in users) -->
        <section id="create-page" class="auth">
            <form @submit=${onCreatePost} id="create">
                <h1 class="title">Create Post</h1>

                <article class="input-group">
                    <label for="title">Post Title</label>
                    <input type="title" name="title" id="title">
                </article>

                <article class="input-group">
                    <label for="description">Description of the needs </label>
                    <input type="text" name="description" id="description">
                </article>

                <article class="input-group">
                    <label for="imageUrl"> Needed materials image </label>
                    <input type="text" name="imageUrl" id="imageUrl">
                </article>

                <article class="input-group">
                    <label for="address">Address of the orphanage</label>
                    <input type="text" name="address" id="address">
                </article>

                <article class="input-group">
                    <label for="phone">Phone number of orphanage employee</label>
                    <input type="text" name="phone" id="phone">
                </article>

                <input type="submit" class="btn submit" value="Create Post">
            </form>
        </section>
    `
}


export function editPostTemplate(post) {
    return html`
        <!-- Edit Page (Only for logged-in users) -->
        <section id="edit-page" class="auth">
            <form @submit=${onEditPost} id="edit">
                <h1 class="title">Edit Post</h1>

                <input hidden="hidden" type="text" name="id" value=${post._id}>
                
                <article class="input-group">
                    <label for="title">Post Title</label>
                    <input type="text" name="title" id="title" value=${post.title}>
                </article>

                <article class="input-group">
                    <label for="description">Description of the needs </label>
                    <input type="text" name="description" id="description" value=${post.description}>
                </article>

                <article class="input-group">
                    <label for="imageUrl"> Needed materials image </label>
                    <input type="text" name="imageUrl" id="imageUrl" value=${post.imageUrl}>
                </article>

                <article class="input-group">
                    <label for="address">Address of the orphanage</label>
                    <input type="text" name="address" id="address" value=${post.address}>
                </article>

                <article class="input-group">
                    <label for="phone">Phone number of orphanage employee</label>
                    <input type="text" name="phone" id="phone" value=${post.phone}>
                </article>

                <input type="submit" class="btn submit" value="Edit Post">
            </form>
        </section>
    `
}


export function postDetailsTemplate(post, donations, HTMLButtons) {
    return html`
        <!-- Details Page -->
        <section id="details-page">
            <h1 class="title">Post Details</h1>

            <div id="container">
                <div id="details">
                    <div class="image-wrapper">
                        <img src=${post.imageUrl} alt="Material Image" class="post-image">
                    </div>
                    <div class="info">
                        <h2 class="title post-title">${post.title}</h2>
                        <p class="post-description">Description: ${post.description}<p>
                        <p class="post-address">Address: ${post.address}</p>
                        <p class="post-number">Phone number: ${post.phone}</p>
                        <p class="donate-Item">Donate Materials: ${donations}</p>

                        <!--Edit and Delete are only for creator-->
                        <div class="btns">
                            ${HTMLButtons}
                        </div>

                    </div>
                </div>
            </div>
        </section>
    `
}


export function userButtons(postId) {
    return html`
        <a href="/edit-post/${postId}" class="edit-btn btn">Edit</a>
        <a href="/delete-post/${postId}" class="delete-btn btn">Delete</a>
    `
}


export function guestButtons(postId) {
    return html`
        <!--Bonus - Only for logged-in users ( not authors )-->
        <a href="/donate/${postId}" class="donate-btn btn">Donate</a>
    `
}