function attachEvents() {
    document.querySelector('#loadBooks').addEventListener('click', reloadBooks);
    formBtn.addEventListener('click', createBook);
}

async function reloadBooks() {
    formBtn.removeEventListener('click', editBook);
    formBtn.addEventListener('click', createBook);
    formBtn.textContent = 'Submit';
    formTitle.textContent = 'FORM';
    formBtn.id = '';
    title.value = '';
    author.value = '';

    const data = await (await fetch(url)).json();
    const tableBody = document.querySelector('table tbody');
    tableBody.innerHTML = '';

    Object.entries(data).forEach(([id, book]) => {
        tableBody.appendChild(createRow(book.author, book.title, id));
    });
}

async function getBookById(id) {
    return await (await fetch(`${url}/${id}`)).json();
}

async function createBook(event) {
    event.preventDefault();
    await setBook('POST', url)
}

async function editBook(event) {
    event.preventDefault();
    await setBook('PUT', `${url}/${event.target.id}`)
}

async function deleteBook(event) {
    try {
        await makeRequest('DELETE', `${url}/${event.target.id}`)
        await reloadBooks();
    } catch (error) {
        alert(error.message);
    }
}

async function setBook(method, url) {
    if (areEmpty(title, author)) {
        return
    }

    const body = JSON.stringify({
        'author': author.value,
        'title': title.value
    });

    try {
        await makeRequest(method, url, body);
        await reloadBooks();
    } catch (error) {
        alert(error.message);
    }
}

async function onEditBook(event) {
    const book = await getBookById(event.target.id);
    formTitle.textContent = 'Edit FORM';
    title.value = book.title;
    author.value = book.author;
    formBtn.removeEventListener('click', createBook);
    formBtn.addEventListener('click', editBook);
    formBtn.textContent = 'Save';
    formBtn.id = event.target.id;
}

async function makeRequest(method, url, body) {
    const response = await fetch(url, {
        method: method,
        headers: {
            'Content-Type': 'application/json'
        },
        body
    });
    const data = await response.json();

    if (response.status !== 200) {
        throw new Error(data.message);
    }

    return data;
}

function areEmpty(...fields) {
    return !fields.every(field => field.value);
}

function createRow(author, book, id) {
    return e('tr', {},
        e('td', {}, book),
        e('td', {}, author),
        e('td', {},
            e('button', {id: id, onClick: onEditBook}, 'Edit'),
            e('button', {id: id, onClick: deleteBook}, 'Delete')
        )
    );
    // <tr>
    //     <td>Harry Poter</td>
    //     <td>J. K. Rowling</td>
    //     <td>
    //         <button>Edit</button>
    //         <button>Delete</button>
    //     </td>
    // </tr>
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

const url = 'http://localhost:3030/jsonstore/collections/books';
const title = document.querySelector('input[name=title]');
const author = document.querySelector('input[name=author]');
const formTitle = document.querySelector('form h3');
const formBtn = document.querySelector('form button');
attachEvents()
