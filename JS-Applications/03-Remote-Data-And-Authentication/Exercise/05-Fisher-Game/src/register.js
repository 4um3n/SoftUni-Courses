function attachEvents() {
    registerForm.addEventListener('submit', onRegister);
}

async function onRegister(event) {
    event.preventDefault();
    const form = new FormData(event.target);
    const email = form.get('email');
    const password = form.get('password');
    const rePass = form.get('rePass');

    try {
        if (password !== rePass) {
            throw new Error('The two passwords don\'t match!')
        }

        await register({
            'email': email,
            'password': password
        });

        location.assign('./login.html')
    } catch (error) {
        alert(error.message);
    }


}

async function register(user) {
    const response = await fetch('http://localhost:3030/users/register', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(user)
    });

    const data = await response.json();

    if (response.status !== 200) {
        throw new Error(data.message);
    }
}


const registerForm = document.querySelector('#register-form');
document.querySelector('#home').style.display = 'none';
document.querySelector('#logout').style.display = 'none';
document.querySelector('nav p.email').style.display = 'none';
attachEvents();
