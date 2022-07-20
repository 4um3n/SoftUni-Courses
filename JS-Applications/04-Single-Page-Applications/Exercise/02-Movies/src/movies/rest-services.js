import { sendRequest } from "../rest-services.js";


export async function getAllMovies() {
    return await sendRequest('http://localhost:3030/data/movies')
}


export async function getMovieLikes(id) {
    const url = `http://localhost:3030/data/likes?where=movieId%3D%22${id}%22&distinct=_ownerId&count`;
    return await sendRequest(url);
}


export async function likeMovie(id) {
    const url = 'http://localhost:3030/data/likes';
    const init = {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-Authorization': sessionStorage.getItem('accessToken')
        },
        body: JSON.stringify({
            "movieId": id
        })
    }
    await sendRequest(url, init);
}


export async function dislikeMovie(id) {
    const url = `http://localhost:3030/data/likes/${id}`;
    const init = {
        method: 'DELETE',
        headers: {
            'X-Authorization': sessionStorage.getItem('accessToken')
        },
    }
    await sendRequest(url, init);
}


export async function getLikeFromUser(movieId, userId) {
    const url =`http://localhost:3030/data/likes?where=movieId%3D%22${movieId}%22%20and%20_ownerId%3D%22${userId}%22`;
    return await sendRequest(url)
}


export async function createMovie(movie) {
    const init = {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-Authorization': sessionStorage.getItem('accessToken')
        },
        body: JSON.stringify(movie)
    };
    return await sendRequest('http://localhost:3030/data/movies', init);
}


export async function updateMovie(movie, id) {
    const init = {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
            'X-Authorization': sessionStorage.getItem('accessToken')
        },
        body: JSON.stringify(movie)
    };
    return await sendRequest(`http://localhost:3030/data/movies/${id}`, init);
}


export async function deleteMovie(id) {
    const init = {
        method: 'DELETE',
        headers: {
            'Content-Type': 'application/json',
            'X-Authorization': sessionStorage.getItem('accessToken')
        },
    };
    return await sendRequest(`http://localhost:3030/data/movies/${id}`, init);
}
