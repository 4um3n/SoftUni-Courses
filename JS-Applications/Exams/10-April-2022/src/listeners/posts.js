import { emptyFields } from "../utils.js";
import { post, put } from "../api/api.js";
import { page } from "../lib.js";

export async function onCreatePost(event) {
    event.preventDefault();
    const formData = new FormData(event.target);

    if (emptyFields(...formData.values())) {
        return
    }

    await post(`/data/posts`, {
        title: formData.get('title'),
        description: formData.get('description'),
        imageUrl: formData.get('imageUrl'),
        address: formData.get('address'),
        phone: formData.get('phone')
    });

    page.redirect('/');
}


export async function onEditPost(event) {
    event.preventDefault();
    const formData = new FormData(event.target);

    if (emptyFields(...formData.values())) {
        return
    }

    const postId = formData.get('id');

    await put(`/data/posts/${postId}`, {
        title: formData.get('title'),
        description: formData.get('description'),
        imageUrl: formData.get('imageUrl'),
        address: formData.get('address'),
        phone: formData.get('phone')
    });

    page.redirect(`/details/${postId}`);
}