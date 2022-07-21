import {html} from "https://unpkg.com/lit-html?module";
import {renderAllBooks} from "./views.js";
import {onCreateBook, onDeleteBook, onSaveBook, onUpdateBook} from "./listeners.js";


export function getHTMLPage(rows) {
    return html`
        <button @click="${renderAllBooks}" id="loadBooks">LOAD ALL BOOKS</button>
        <table>
            <thead>
            <tr>
                <th>Title</th>
                <th>Author</th>
                <th>Action</th>
            </tr>
            </thead>
            <tbody id="container">
            ${rows}
            </tbody>
        </table> 
        <div id="form-wrapper">
            
        </div>
    `
}


export function getHTMLTableRow(row, id) {
    return html`
        <tr data-id="${id}">
            <td class="row-data">${row.title}</td>
            <td class="row-data">${row.author}</td>
            <td>
                <button @click="${onUpdateBook}">Edit</button>
                <button @click="${onDeleteBook}">Delete</button>
            </td>
        </tr>
    `
}


export function getHTMLAddForm() {
    return html`
        <form @submit="${onCreateBook}" id="add-form">
            <h3>Add book</h3>
            <label>TITLE</label>
            <input type="text" name="title" placeholder="Title...">
            <label>AUTHOR</label>
            <input type="text" name="author" placeholder="Author...">
            <input type="submit" value="Submit">
        </form>
    `
}


export function getHTMLUpdateForm(title, author, book_id) {
    return html`
        <form @submit="${onSaveBook}" id="edit-form" data-id="${book_id}">
            <input type="hidden" name="id">
            <h3>Edit book</h3>
            <label>TITLE</label>
            <input value="${title}" type="text" name="title" placeholder="Title...">
            <label>AUTHOR</label>
            <input value="${author}" type="text" name="author" placeholder="Author...">
            <input type="submit" value="Save">
        </form>
    `
}