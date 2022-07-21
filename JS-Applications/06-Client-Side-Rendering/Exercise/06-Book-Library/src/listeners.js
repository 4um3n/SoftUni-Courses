import {createBook, deleteBook, updateBook} from "./rest-services.js";
import {renderAddForm, renderAllBooks, renderUpdateForm} from "./views.js";

export async function onCreateBook(event) {
    event.preventDefault();
    const formData = new FormData(event.target);
    const book = {
        'title': formData.get('title'),
        'author': formData.get('author')
    }

    try {
        if (!book.title || !book.author) {
            throw new Error('Title and author must be filled!');
        }

        await createBook(book);
        event.target.reset();
        await renderAllBooks();
    } catch (error) {
        alert(error.message);
    }
}


export function onUpdateBook(event) {
    const tr = event.target.parentElement.parentElement;
    const [title, author] = Array.from(tr.querySelectorAll('.row-data')).map(el => el.textContent);
    renderUpdateForm(title, author, tr.getAttribute('data-id'));
}


export async function onSaveBook(event) {
    event.preventDefault();
    const id = event.target.getAttribute('data-id');
    const formData = new FormData(event.target);
    const book = {
        'title': formData.get('title'),
        'author': formData.get('author')
    }

    try {
        if (!book.title || !book.author) {
            throw new Error('Title and author must be filled!');
        }

        await updateBook(book, id);
        await renderAllBooks();
        renderAddForm();
    } catch (error) {
        alert(error.message);
    }
}


export async function onDeleteBook(event) {
    const tr = event.target.parentElement.parentElement;
    const id = tr.getAttribute('data-id');

    try {
        await deleteBook(id);
        await renderAllBooks();
        renderAddForm();
    } catch (error) {
        alert(error.message);
    }
}
