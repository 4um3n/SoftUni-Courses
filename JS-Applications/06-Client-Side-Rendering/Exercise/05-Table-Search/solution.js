import {html, render} from "https://unpkg.com/lit-html?module";


attachEvents();
const container = document.querySelector('table.container > tbody');
const searchField = document.querySelector('#searchField');


function attachEvents() {
    window.addEventListener('load', () => onSearch());
    document.querySelector('#searchBtn').addEventListener('click', onSearch);
}


function getClass(row, searched) {
    if (!searched) {
        return '';
    }

    const rowIn = [
        row.firstName.toLowerCase().includes(searched),
        row.lastName.toLowerCase().includes(searched),
        row.email.toLowerCase().includes(searched),
        row.course.toLowerCase().includes(searched),
        searched.includes(row.firstName.toLowerCase()),
        searched.includes(row.lastName.toLowerCase()),
        searched.includes(row.email.toLowerCase()),
        searched.includes(row.course.toLowerCase())
    ];

    if (rowIn.some(el => el)) {
        return 'select';
    }

    return '';
}


async function onSearch() {
    try {
        const searched = searchField.value.toLowerCase();
        const data = await sendRequest('http://localhost:3030/jsonstore/advanced/table');
        const rows = Object.values(data);
        renderRows(rows, searched);
        searchField.value = '';
    } catch (error) {
        alert(error.message);
    }
}


function renderRows(rows, searched) {
    const HTMLRows = rows.map(row => createHTMLRow(row, getClass(row, searched)));
    render(HTMLRows, container);
}


function createHTMLRow(row, className) {
    return html`
        <tr class="${className}">
            <td>${row.firstName} ${row.lastName}</td>
            <td>${row.email}</td>
            <td>${row.course}</td>
        </tr>
    `
}


async function sendRequest(url, init) {
    const response = await fetch(url, init);
    const data = await response.json();

    if (response.status !== 200) {
        throw new Error(data.message);
    }

    return data;
}