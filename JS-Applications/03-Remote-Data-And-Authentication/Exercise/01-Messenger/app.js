function attachEvents() {
    document.querySelector('#refresh').addEventListener('click', onRefresh);
    document.querySelector('#submit').addEventListener('click', onSubmit);
}

async function onRefresh(event) {
    const textArea = document.querySelector('#messages');
    const data = await (await fetch(url)).json();
    const messages = [];

    for (const message of Object.values(data || {})) {
        messages.push(`${message.author}: ${message.content}`);
    }

    textArea.textContent = '';
    textArea.textContent = messages.join('\n');

}

async function onSubmit(event) {
    const name = document.querySelector('input[name=author]');
    const content = document.querySelector('input[name=content]');

    const body = JSON.stringify({
        'author': name.value,
        'content': content.value,
    });

    try {
        const response = await fetch(url, {
            method: "POST",
            headers: {
                'Content-Type': 'application/json'
            },
            body
        });

        const data = await response.json();

        if (response.status !== 200) {
            throw new Error(data.message);
        }

    } catch (error) {
        console.log(error.message);
    }

    name.value = '';
    content.value = '';
}

const url = 'http://localhost:3030/jsonstore/messenger';
attachEvents();