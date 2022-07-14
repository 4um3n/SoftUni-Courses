function attachEvents() {
    document.querySelector('#logout').addEventListener('click', onLogout);
    document.querySelector('#home-view button.load').addEventListener('click', loadCatches)
}

async function loadCatches(event) {
    clearCatches();
    const currentCatches = await getCatches();
    const userId = localStorage.getItem('userId');

    currentCatches.forEach(currentCatch => {
        const htmlCatch = createCatch(currentCatch);
        const updateBtn = htmlCatch.querySelector('#update-btn');
        const deleteBtn = htmlCatch.querySelector('#delete-btn');

        if (htmlCatch['owner-id'] !== userId) {
            updateBtn.disabled = true;
            deleteBtn.disabled = true;
        }

        catches.appendChild(htmlCatch);
    });
}

async function uploadCatch(event) {
    event.preventDefault();
    const data = new FormData(event.target);
    const body = {
        "angler": data.get('angler'),
        "weight": data.get('weight'),
        "species": data.get('species'),
        "location": data.get('location'),
        "bait": data.get('bait'),
        "captureTime": data.get('captureTime'),
    };

    try {
        const response = await fetch('http://localhost:3030/data/catches', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-Authorization': localStorage.getItem('accessToken')
            },
            body: JSON.stringify(body)
        });

        const responseData = await response.json();

        if (response.status !== 200) {
            throw new Error(responseData.message);
        }

        await loadCatches();
        clearForm();
    } catch (error) {
        alert(error.message);
    }
}

async function updateCatch(event) {
    const data = {};
    Array.from(event.target.parentElement.querySelectorAll('input')).forEach(el => {
        data[el.className] = el.value;
    });

    try {
        const response = await fetch(`http://localhost:3030/data/catches/${event.target['data-id']}`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
                'X-Authorization': localStorage.getItem('accessToken')
            },
            body: JSON.stringify(data)
        });
        const responseData = await response.json();

        if (response.status !== 200) {
            throw new Error(responseData.message);
        }

        await loadCatches();
        clearForm();
    } catch (error) {
        alert(error.message);
    }
}

async function deleteCatch(event) {
    try {
        const response = await fetch(`http://localhost:3030/data/catches/${event.target['data-id']}`, {
            method: 'DELETE',
            headers: {
                'X-Authorization': localStorage.getItem('accessToken')
            },
        });
        const responseData = await response.json();

        if (response.status !== 200) {
            throw new Error(responseData.message);
        }

        await loadCatches();
        clearForm();
    } catch (error) {
        alert(error.message);
    }
}

async function getCatches() {
    try {
        const response = await fetch('http://localhost:3030/data/catches');
        const catches = await response.json();

        if (response.status !== 200) {
            throw new Error(catches.message);
        }

        return catches;
    } catch (error) {
        alert(error.message);
    }
}

function createCatch(currentCatch) {
    return e('div', {className: 'catch', 'owner-id': currentCatch._ownerId},
        e('label', {}, 'Angler'),
        e('input', {type: 'text', className: 'angler', value: currentCatch.angler}),
        e('label', {}, 'Weight'),
        e('input', {type: 'number', className: 'weight', value: currentCatch.weight}),
        e('label', {}, 'Species'),
        e('input', {type: 'text', className: 'species', value: currentCatch.species}),
        e('label', {}, 'Location'),
        e('input', {type: 'text', className: 'location', value: currentCatch.location}),
        e('label', {}, 'Bait'),
        e('input', {type: 'text', className: 'bait', value: currentCatch.bait}),
        e('label', {}, 'Capture Time'),
        e('input', {type: 'number', className: 'captureTime', value: currentCatch.captureTime}),
        e('button', {className: 'update', id: 'update-btn', 'data-id': currentCatch._id, onClick: updateCatch}, 'Update'),
        e('button', {className: 'delete', id: 'delete-btn', 'data-id': currentCatch._id, onClick: deleteCatch}, 'Delete'),
    );
}

function clearCatches() {
    catches.innerHTML = '';
}

function clearForm() {
    addCatchForm.querySelectorAll('input').forEach(el => el.value = '');
}


async function onLogout(event) {
    try {
        location.assign('./login.html');
        await logout();
        localStorage.setItem('userId', '');
        localStorage.setItem('accessToken', '');
    } catch (error) {
        alert(error.message);
    }
}

async function logout() {
    const response = await fetch('http://localhost:3030/users/logout', {
        method: "GET",
        headers: {
            'X-Authorization': localStorage.getItem('accessToken')
        }
    });

    if (response.status !== 204) {
        throw new Error(`${response.status} ${response.statusText}`);
    }
}



async function getUser() {
    const response = await fetch('http://localhost:3030/users/me', {
        method: 'GET',
        headers: {
            'X-Authorization': localStorage.getItem('accessToken')
        }
    });

    const data = await response.json();

    if (response.status !== 200) {
        throw new Error(data.message);
    }

    return data;
}

async function renderUsername() {
    try {
        const user = await getUser();
        document.querySelector('nav p.email').textContent = `Welcome ${user.email}`;
    } catch (error) {
        alert(error.message);
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

function route() {
    if (!localStorage.getItem('accessToken')) {
        location.assign('./login.html')
    }
}

async function main() {
    route();
    await renderUsername();
    attachEvents();
    clearCatches();
    addCatchForm.querySelector('button.add').disabled = false;
    addCatchForm.addEventListener('submit', uploadCatch);
}

document.querySelector('#login').style.display = 'none';
document.querySelector('#register').style.display = 'none';
const catches = document.querySelector('#catches');
const addCatchForm = document.querySelector('#addForm');
await main();
