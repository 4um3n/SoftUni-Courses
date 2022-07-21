import {render} from "https://unpkg.com/lit-html?module";
import {getAllBooks} from "./rest-services.js";
import {getHTMLAddForm, getHTMLPage, getHTMLTableRow, getHTMLUpdateForm} from "./templates.js";


export function renderPage() {
    const page = getHTMLPage([]);
    render(page, document.querySelector('body'));
}


export async function renderAllBooks() {
    try {
        const rows = Object.entries(await getAllBooks());
        const HTMLRows = rows.map(([id, row]) => getHTMLTableRow(row, id));
        render(HTMLRows, document.querySelector('#container'));
    } catch (error) {
        alert(error.message);
    }
}


export function renderAddForm() {
    const addForm = getHTMLAddForm();
    render(addForm, document.querySelector('#form-wrapper'))
}


export function renderUpdateForm(title, author, book_id) {
    const addForm = getHTMLUpdateForm(title, author, book_id);
    render(addForm, document.querySelector('#form-wrapper'))
}