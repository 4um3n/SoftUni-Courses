function attachEvents() {
    document.querySelector('#btnLoadPosts').addEventListener('click', loadPosts);
    document.querySelector('#btnViewPost').addEventListener('click', loadPost)
}

async function getPosts() {
    const url = 'http://localhost:3030/jsonstore/blog/posts';
    return await (await fetch(url)).json();
}

async function getCommentsById(id) {
    const url = 'http://localhost:3030/jsonstore/blog/comments';
    const comments =  Object.values(await (await fetch(url)).json());
    return comments.filter(c => c.postId === id)
}

async function loadPosts(event) {
    selectedPost.innerHTML = '';
    postTitle.textContent = 'Post Details';
    postBody.textContent = '';
    postComments.innerHTML = ''
    const posts = await getPosts();

    for (const post of Object.values(posts)) {
        selectedPost.appendChild(e('option', {value: post.id, }, post.title));
        postsTitles[post.id] = post.title;
        postsBodies[post.id] = post.body;
    }
}

async function loadPost(event) {
    postComments.innerHTML = ''
    postTitle.textContent = postsTitles[selectedPost.value];
    postBody.textContent = postsBodies[selectedPost.value];
    const comments = await getCommentsById(selectedPost.value);

    for (const comment of Object.values(comments)) {
        postComments.appendChild(e('li', {id: comment.id}, comment.text));
    }

}

function e(type, attributes, ...content) {
    const result = document.createElement(type);

    for (let [attr, value] of Object.entries(attributes || {})) {
        if (attr.substring(0, 2) == 'on') {
            result.addEventListener(attr.substring(2).toLocaleLowerCase(), value);
        } else {
            result[attr] = value;
        }
    }

    content = content.reduce((a, c) => a.concat(Array.isArray(c) ? c : [c]), []);

    content.forEach(e => {
        if (typeof e == 'string' || typeof e == 'number') {
            const node = document.createTextNode(e);
            result.appendChild(node);
        } else {
            result.appendChild(e);
        }
    });

    return result;
}

const postsTitles = {}
const postsBodies = {}
const postTitle = document.querySelector('#post-title');
const postBody = document.querySelector('#post-body');
const postComments = document.querySelector('#post-comments');
const selectedPost = document.querySelector('#posts');
attachEvents();
