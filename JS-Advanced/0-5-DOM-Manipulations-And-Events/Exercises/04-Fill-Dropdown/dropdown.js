function addItem() {
    const newItemTextInputField = document.getElementById('newItemText');
    const newItemValueInputField = document.getElementById('newItemValue');
    const option = document.createElement('option');
    option.textContent = newItemTextInputField.value;
    option.value = newItemValueInputField.value;
    newItemTextInputField.value = '';
    newItemValueInputField.value = '';
    document.querySelector('select[id=menu]').appendChild(option);
}
