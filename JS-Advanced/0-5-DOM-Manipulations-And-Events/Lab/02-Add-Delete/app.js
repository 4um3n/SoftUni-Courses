function deleteByEmail() {
    const searchedEmail = document.querySelector('input[name="email"]').value;
    const rows = document.querySelectorAll('table[id="customers"] tbody tr');
    let result = 'Not found.';

    for (let row of rows) {
        const column = row.children[row.children.length - 1];
        if (column.textContent === searchedEmail) {
            row.parentNode.removeChild(row);
            result = 'Deleted';
            break;
        }
    }

    document.getElementById('result').textContent = result;
}
