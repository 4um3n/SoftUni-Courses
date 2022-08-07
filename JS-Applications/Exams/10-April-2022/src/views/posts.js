import { render, page } from '../lib.js';
import { get, post, del } from '../api/api.js';
import { getUserData } from "../utils.js";
import {
    noPostsTemplate,
    allPostsTemplate,
    userNoPostsTemplate,
    userPostsTemplate,
    dashboardTemplate,
    userDashboardTemplate
} from "../templates/dashboard.js";
import {
    createPostTemplate,
    editPostTemplate,
    postDetailsTemplate,
    userButtons,
    guestButtons
} from "../templates/posts.js";


export async function dashboardView(ctx) {
    const posts = await get('/data/posts?sortBy=_createdOn%20desc');
    let template;

    if (posts.length <= 0) {
        template = noPostsTemplate();
    } else {
        template = allPostsTemplate(posts);
    }

    render(dashboardTemplate(template), ctx.main);
}


export async function userDashboardView(ctx) {
    const user = getUserData();
    const posts = await get(`/data/posts?where=_ownerId%3D%22${user.id}%22&sortBy=_createdOn%20desc`);
    let HTMLPosts;

    if (posts.length <= 0) {
        HTMLPosts = userNoPostsTemplate();
    } else {
        HTMLPosts = userPostsTemplate(posts);
    }

    render(userDashboardTemplate(HTMLPosts), ctx.main);
}


export async function postDetailsView(ctx) {
    const postId = ctx.params.id;
    const post = await get(`/data/posts/${postId}`);
    const donations = await get(`/data/donations?where=postId%3D%22${postId}%22&distinct=_ownerId&count`)
    let buttons;

    const user = getUserData();
    if (user) {
        const userPosts = await get(`/data/posts?where=_ownerId%3D%22${user.id}%22&sortBy=_createdOn%20desc`);

        if (userPosts.map(p => p._id).includes(postId)) {
            buttons = userButtons(postId);
        } else {
            const userDonated = await get(`/data/donations?where=postId%3D%22${postId}%22%20and%20_ownerId%3D%22${user.id}%22&count`);
            if (!userDonated) {
                buttons = guestButtons(postId);
            }
        }
    }

    const template = postDetailsTemplate(post, donations, buttons);
    render(template, ctx.main);
}


export function createPostView(ctx) {
    const template = createPostTemplate();
    render(template, ctx.main)
}


export async function editPostView(ctx) {
    const postId = ctx.params.id;
    const post = await get(`/data/posts/${postId}`);
    const template = editPostTemplate(post);
    render(template, ctx.main);
}


export async function deletePostView(ctx) {
    const postId = ctx.params.id;
    const sure = confirm('Are you sure?');

    if (sure) {
        await del(`/data/posts/${postId}`);
        page.redirect('/');
    }
}


export async function donate(ctx) {
    const postId = ctx.params.id;
    await post(`/data/donations`, {postId});
    page.redirect(`/details/${postId}`);
}
