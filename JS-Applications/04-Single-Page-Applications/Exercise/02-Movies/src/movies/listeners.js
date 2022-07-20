import {dislikeMovie, getLikeFromUser, likeMovie} from "./rest-services.js";

export async function onLike(event) {
    event.preventDefault();
    const movieId = event.target.parentElement.getAttribute('data-id');
    const userId = sessionStorage.getItem('userId');
    const liked = await getLikeFromUser(movieId, userId);

    if (liked.length === 0) {
        await likeMovie(movieId);
    } else {
        await dislikeMovie(movieId);
    }
}
