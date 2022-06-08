function focused() {
    function onFocus(event) {
        event.target.parentNode.classList.add('focused')
    }

    function onBlur(event) {
        event.target.parentNode.classList.remove('focused')
    }

    const inputFields = document.querySelectorAll('input[type=text]');

    for (let inputField of inputFields) {
        inputField.addEventListener('focus', onFocus);
        inputField.addEventListener('blur', onBlur);
    }
}
