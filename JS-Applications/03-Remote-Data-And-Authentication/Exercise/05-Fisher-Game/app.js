function attachEvents() {
    document.querySelector('#login').addEventListener('click', loadLogin);
    document.querySelector('#register').addEventListener('click', loadRegister);
}

function loadLogin() {
    window.location = 'src/login.html';
}

function loadRegister() {
    window.location = 'src/register.html';
}

attachEvents();