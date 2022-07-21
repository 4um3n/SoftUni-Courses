export async function getAllBooks() {
    return sendRequest('http://localhost:3030/jsonstore/collections/books');
}


export async function createBook(book) {
    const init = {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(book)
    }
    return sendRequest(`http://localhost:3030/jsonstore/collections/books`, init);
}


export async function updateBook(book, id) {
    const url = `http://localhost:3030/jsonstore/collections/books/${id}`;
    const init = {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(book)
    }
    await sendRequest(url, init);
}


export async function deleteBook(id) {
    return await sendRequest(`http://localhost:3030/jsonstore/collections/books/${id}`, {
        method: 'DELETE'
    });
}


async function sendRequest(url, init) {
    const response = await fetch(url, init);
    const data = await response.json();

    if (response.status !== 200) {
        throw new Error(data.message);
    }

    return data;
}
