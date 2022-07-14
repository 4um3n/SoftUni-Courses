function attachEvents() {
    loginForm.addEventListener('submit', onLogin);
}

async function onLogin(event) {
    event.preventDefault();
    const form = new FormData(event.target);

    try {
        await login({
            "email": form.get('email'),
            "password": form.get('password')
        });

        location.assign('./index.html')
    } catch (error) {
        alert(error.message);
    }

}

async function login(user) {
    const response = await fetch('http://localhost:3030/users/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(user)
    });
    const data = await response.json();

    if (response.status !== 200) {
        throw new Error(data.message);
    }

    localStorage.setItem('accessToken', data.accessToken);
    localStorage.setItem('userId', data._id);
}


const loginForm = document.querySelector('#login-form');
document.querySelector('#home').style.display = 'none';
document.querySelector('#logout').style.display = 'none';
document.querySelector('nav p.email').style.display = 'none';
attachEvents();
