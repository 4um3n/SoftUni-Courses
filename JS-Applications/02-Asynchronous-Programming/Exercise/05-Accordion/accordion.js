async function getTitles() {
    const url = 'http://localhost:3030/jsonstore/advanced/articles/list';
    return await (await fetch(url)).json();
}

async function getContent(id) {
    const baseUrl = 'http://localhost:3030/jsonstore/advanced/articles/details';
    return await (await fetch(`${baseUrl}/${id}`)).json();
}

function createPreview(content) {
    return e('div', {className: 'accordion'},
        e('div', { className: 'head'},
            e('span', {}, content.title),
            e('button', {className: 'button', id: content._id, onClick: toggleCard}, 'More')
        ),
        e('div', {className: 'extra', id: `extra-content-${content._id}`},
            e('p', {}, '')
        )
    );

    // <div class="accordion">
    //    <div class="head">
    //        <span>Scalable Vector Graphics</span>
    //        <button class="button" id="ee9823ab-c3e8-4a14-b998-8c22ec246bd3">More</button>
    //    </div>
    //    <div class="extra">
    //        <p>Scalable Vector Graphics .....</p>
    //    </div>
    // </div>
}

async function toggleCard(event) {
    const contentWrapper = document.querySelector(`#extra-content-${event.target.id}`)

    if (contentWrapper.style.display === '') {
        event.target.textContent = 'LESS';
        contentWrapper.style.display = 'block';
        const content = await getContent(event.target.id);
        contentWrapper.querySelector('p').textContent = content.content;
    } else {
        contentWrapper.style.display = ''
        event.target.textContent = 'MORE';
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

window.addEventListener('load', async () => {
    const data = await getTitles();
    const cards = data.map(createPreview);
    const main = document.querySelector('#main');
    cards.forEach(c => main.appendChild(c));
});
