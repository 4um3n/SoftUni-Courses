import {html} from 'https://unpkg.com/lit-html?module'
import { createNavigation, createFooter } from "../html-services.js";
import { onLike } from "./listeners.js";

export function createHomeView(movies, user) {
    return html`
        ${createNavigation(user)}

        <section id="home-page" class="view-section">
            <div
                    class="jumbotron jumbotron-fluid text-light"
                    style="background-color: #343a40"
            >
                <img
                        src="https://slicksmovieblog.files.wordpress.com/2014/08/cropped-movie-banner-e1408372575210.jpg"
                        class="img-fluid"
                        alt="Responsive image"
                        style="width: 150%; height: 200px"
                />
                <h1 class="display-4">Movies</h1>
                <p class="lead">
                    Unlimited movies, TV shows, and more. Watch anywhere. Cancel
                    anytime.
                </p>
            </div>

            <h1 class="text-center">Movies</h1>

            <section id="add-movie-button" class="user">
                <a href="#" class="btn btn-warning">Add Movie</a>
            </section>

            <section id="movie">
                <div class="mt-3">
                    <div class="row d-flex d-wrap">
                        <ul
                                id="movies-list"
                                class="card-deck d-flex justify-content-center"
                        >
                            <!-- movie list -->
                            ${movies}
                        </ul>
                    </div>
                </div>
            </section>
        </section>

        ${createFooter()}
    `
}


export function createMovieView(movie, likes, user) {
    let buttons = html``;
    let details = html``;

    if (user) {
        if (user._id === movie._ownerId) {
            buttons = html`
                <a class="btn btn-danger" href="#">Delete</a>
                <a class="btn btn-warning" href="#">Edit</a>
            `
        } else {
            buttons = html`
                <a @click=${onLike} class="btn btn-primary" href="#">Like</a>
            `
        }

        details = html`
            <div owner-id=${movie._ownerId} data-id=${movie._id} class="col-md-4 text-center">
                <h3 class="my-3">Movie Description</h3>
                <p>${movie.description}</p>
                ${buttons}
                <span class="enrolled-span">Liked ${likes}</span>
            </div>
        `
    }

    return html`
        <section id="movie-example" class="view-section">
            <div class="container">
                <div class="row bg-light text-dark">
                    <h1>Movie title: ${movie.title}</h1>

                    <div class="col-md-8">
                        <img
                                class="img-thumbnail"
                                src=${movie.img}
                                alt="Movie"
                        />
                    </div>
                    ${details}
                </div>
            </div>
        </section>
    `
}


export function createAddMovieView() {
    return html`
        <section id="add-movie" class="view-section">
            <form
                    id="add-movie-form"
                    class="text-center border border-light p-5"
                    action="#"
                    method=""
            >
                <h1>Add Movie</h1>
                <div class="form-group">
                    <label for="title">Movie Title</label>
                    <input
                            id="title"
                            type="text"
                            class="form-control"
                            placeholder="Title"
                            name="title"
                            value=""
                    />
                </div>
                <div class="form-group">
                    <label for="description">Movie Description</label>
                    <textarea
                            class="form-control"
                            placeholder="Description"
                            name="description"
                    ></textarea>
                </div>
                <div class="form-group">
                    <label for="imageUrl">Image url</label>
                    <input
                            id="imageUrl"
                            type="text"
                            class="form-control"
                            placeholder="Image Url"
                            name="img"
                            value=""
                    />
                </div>
                <button type="submit" class="btn btn-primary">Submit</button>
            </form>
        </section>
        ${createFooter()}
    `
}


export function createEditMovieView() {
    return html`
        <section id="edit-movie" class="view-section">
            <form class="text-center border border-light p-5" action="#" method="">
                <h1>Edit Movie</h1>
                <div class="form-group">
                    <label for="title">Movie Title</label>
                    <input
                            id="title"
                            type="text"
                            class="form-control"
                            placeholder="Movie Title"
                            value=""
                            name="title"
                    />
                </div>
                <div class="form-group">
                    <label for="description">Movie Description</label>
                    <textarea
                            class="form-control"
                            placeholder="Movie Description..."
                            name="description"
                    ></textarea>
                </div>
                <div class="form-group">
                    <label for="imageUrl">Image url</label>
                    <input
                            id="imageUrl"
                            type="text"
                            class="form-control"
                            placeholder="Image Url"
                            value=""
                            name="img"
                    />
                </div>
                <button type="submit" class="btn btn-primary">Submit</button>
            </form>
        </section>
        ${createFooter()}
    `
}
