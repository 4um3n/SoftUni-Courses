import { html, render } from 'https://unpkg.com/lit-html?module'
import { sendRequest, onSubmit, container } from "./helpers.js";


async function onPost(event) {
    const topicId = event.target.getAttribute('data-id');
    const formData = new FormData(event.target.parentElement);
    const comment = {
        'text': formData.get('postText'),
        'username': formData.get('username'),
        'topicId': topicId
    };
    const init = {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(comment)
    };
    await sendRequest('http://localhost:3030/jsonstore/collections/myboard/comments', init);
    await renderComments(topicId);
}


export async function renderComments(id) {
    const post = await sendRequest(`http://localhost:3030/jsonstore/collections/myboard/posts/${id}`);
    const comments = await sendRequest('http://localhost:3030/jsonstore/collections/myboard/comments');
    const HTMLComment = createHTMLComments(post, Object.values(comments).filter(c => c.topicId === id));
    render(HTMLComment, container);
}


function createHTMLComments(topic, comments) {
    return html`
        <div class="theme-content">
            <!-- theme-title  -->
            <div class="theme-title">
                <div class="theme-name-wrapper">
                    <div class="theme-name">
                        <h2>${topic.title}</h2>
                    </div>
                </div>
            </div>
            <!-- comment  -->
            <div class="comment">
                <div class="header">
                    <img src="./static/profile.png" alt="avatar">
                    <p><span>${topic.username}</span> posted on <time>2020-10-10 12:08:28</time></p>
                    <p class="post-content">${topic.text}</p>
                </div>
                ${comments.map(createHTMLComment)}
            </div>
            <div class="answer-comment">
                <p><span>currentUser</span> comment:</p>
                <div class="answer">
                    <form @submit=${onSubmit}>
                        <textarea name="postText" id="comment" cols="30" rows="10"></textarea>
                        <div>
                            <label for="username">Username <span class="red">*</span></label>
                            <input type="text" name="username" id="username">
                        </div>
                        <button @click=${onPost} data-id=${topic._id}>Post</button>
                    </form>
                </div>
            </div>
        </div>
    `
}


function createHTMLComment(comment) {
    return html`
        <div id="user-comment">
            <div class="topic-name-wrapper">
                <div class="topic-name">
                    <p><strong>${comment.username}</strong> commented on <time>3/15/2021, 12:39:02 AM</time></p>
                    <div class="post-content">
                        <p>${comment.text}</p>
                    </div>
                </div>
            </div>
        </div>   
    `
}
