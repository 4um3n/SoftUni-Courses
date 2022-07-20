import { render } from 'https://unpkg.com/lit-html?module'
import { createHomeView, createMovieView } from "./html-services.js";
import {getAllMovies, getMovieLikes} from "./rest-services.js";
import { getUser } from "../auth/rest-services.js";
const container = document.querySelector('#container');



export async function renderHomeView() {
    let user;

    if (sessionStorage.hasOwnProperty('accessToken')) {
        user = await getUser();
    }
    
    const movies = await getAllMovies();
    const HTMLMovies = [];

    for (const movie of movies) {
        const likes = await getMovieLikes(movie._id);
        HTMLMovies.push(createMovieView(movie, likes, user));
    }

    const homeView = createHomeView(HTMLMovies, user);
    render(homeView, container);
}
