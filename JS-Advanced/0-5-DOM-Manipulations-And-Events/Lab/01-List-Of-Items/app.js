function addItem() {
    const newListItem = document.createElement('li');
    newListItem.textContent = document.getElementById('newItemText').value;
    document.getElementById('items').appendChild(newListItem);
}