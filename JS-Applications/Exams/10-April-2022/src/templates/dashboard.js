import { html } from '../lib.js';


export function dashboardTemplate(HTMLPosts) {
    return html`
        <!-- Dashboard -->
        <section id="dashboard-page">
            <h1 class="title">All Posts</h1>
            ${HTMLPosts}
        </section>
    `
}


export function noPostsTemplate() {
    return html`
        <!-- Display an h1 if there are no posts -->
        <h1 class="title no-posts-title">No posts yet!</h1>        
    `
}


export function allPostsTemplate(posts) {
    return html`
        <!-- Display a div with information about every post (if any)-->
        <div class="all-posts">
            ${posts.map(post => postCardTemplate(post))}
        </div>
    `
}


export function userDashboardTemplate(HTMLPosts) {
    return html`
        <!-- My Posts -->
        <section id="my-posts-page">
            <h1 class="title">My Posts</h1>
            ${HTMLPosts}
        </section>
    `
}


export function userNoPostsTemplate() {
    return html`
        <!-- Display an h1 if there are no posts -->
        <h1 class="title no-posts-title">You have no posts yet!</h1>
    `
}


export function userPostsTemplate(posts) {
    return html`
        <!-- Display a div with information about every post (if any)-->
        <div class="my-posts">
            ${posts.map(p => postCardTemplate(p))}
        </div>
    `
}


function postCardTemplate(post) {
    return html`
        <div class="post">
            <h2 class="post-title">${post.title}</h2>
            <img class="post-image" src=${post.imageUrl} alt="Material Image">
            <div class="btn-wrapper">
                <a href="/details/${post._id}" class="details-btn btn">Details</a>
            </div>
        </div>
    `
}
