function attachEvents() {
    document.querySelector('#btnLoad').addEventListener('click', onLoad);
    document.querySelector('#btnCreate').addEventListener('click', onCreate);
}

async function onLoad(event) {
    const data = await (await fetch(url)).json();
    const phonebook = document.querySelector('#phonebook');
    phonebook.innerHTML = '';

    for (const [id, obj] of Object.entries(data)) {
        const deleteBtn = e('button', {id: id, onClick: onDelete}, 'Delete')
        phonebook.appendChild(
            e('li', {}, `${obj.person}: ${obj.phone}`, deleteBtn)
        );
    }
}

async function onCreate(event) {
    const person = document.querySelector('#person');
    const phone = document.querySelector('#phone');
    const body = JSON.stringify({
        'person': person.value,
        'phone': phone.value
    });

    try {
        const response = await fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body
        });

        const data = await response.json();

        if (response.status === 200) {
            person.value = '';
            phone.value = '';
        } else {
            throw new Error(data.message);
        }

    } catch (error) {
        alert(error.message);
    }
}

async function onDelete(event) {
    const id = event.target.id;
    event.target.parentElement.remove();
    await fetch(`${url}/${id}`, {
        method: 'DELETE',
        headers: {
            'Content-Type': 'application/json'
        }
    });
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

const url = 'http://localhost:3030/jsonstore/phonebook';
attachEvents();