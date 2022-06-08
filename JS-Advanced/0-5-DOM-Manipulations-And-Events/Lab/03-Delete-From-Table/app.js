function addItem() {
    const newListItem = document.createElement('li');
    const deleteLink = document.createElement('a');

    deleteLink.textContent = '[Delete]';
    deleteLink.href = '#';
    deleteLink.addEventListener('click', function () {
        this.parentNode.remove();
    });

    newListItem.textContent = document.getElementById('newItemText').value;
    newListItem.appendChild(deleteLink);

    document.getElementById('items').appendChild(newListItem);
}
