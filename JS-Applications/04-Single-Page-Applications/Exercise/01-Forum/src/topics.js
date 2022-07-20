import { html, render } from 'https://unpkg.com/lit-html?module'
import { sendRequest, onSubmit, container } from "./helpers.js";
import { renderComments } from "./comments.js";


export async function renderTopics() {
    const topics = await getTopics();
    const HTMLTopics = createHTMLTopics(Object.values(topics))
    render(HTMLTopics, container);
}


async function getTopics() {
    return await sendRequest('http://localhost:3030/jsonstore/collections/myboard/posts');
}

async function onPost(event) {
    const formData = new FormData(event.target.parentElement.parentElement);
    const topic = {
        'title': formData.get('topicName'),
        'username': formData.get('username'),
        'text': formData.get('postText'),
    }
    const init = {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(topic)
    };
    const url = 'http://localhost:3030/jsonstore/collections/myboard/posts';
    await sendRequest(url, init);
    await renderTopics();
}


function createHTMLTopics(topics) {
    return html`
        <main>
            <div class="new-topic-border">
                <div class="header-background">
                    <span>New Topic</span>
                </div>
                <form @submit=${onSubmit}>
                    <div class="new-topic-title">
                        <label for="topicName">Title <span class="red">*</span></label>
                        <input type="text" name="topicName" id="topicName">
                    </div>
                    <div class="new-topic-title">
                        <label for="username">Username <span class="red">*</span></label>
                        <input type="text" name="username" id="username">
                    </div>
                    <div class="new-topic-content">
                        <label for="postText">Post <span class="red">*</span></label>
                        <textarea type="text" name="postText" id="postText" rows="8" class="height"></textarea>
                    </div>
                    <div class="new-topic-buttons">
                        <button class="cancel">Cancel</button>
                        <button @click=${onPost} class="public">Post</button>
                    </div>

                </form>
            </div>

            <div class="topic-title">

                <!-- topic component  -->
                <div class="topic-container">
                    ${topics.map(createHTMLTopic)}
                </div>

            </div>

        </main>
    `
}


function createHTMLTopic(topic) {
    return html`
        <div class="topic-name-wrapper">
            <div class="topic-name">
                <a @click=${onComment} href="#" class="normal">
                    <h2 data-id=${topic._id} >${topic.title}</h2>
                </a>
                <div class="columns">
                    <div>
                        <p>Date:
                            <time>2020-10-10T12:08:28.451Z</time>
                        </p>
                        <div class="nick-name">
                            <p>Username: <span>${topic.username}</span></p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    `
}


async function onComment(event) {
    const id = event.target.getAttribute('data-id');
    await renderComments(id);
}
