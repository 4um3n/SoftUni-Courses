import { register, login, logout } from "./rest-services.js";
import { renderHomeView } from '../movies/render-services.js';
import { renderLoginView } from "./render-services.js";


export async function onRegister(event) {
    event.preventDefault();
    const formData = new FormData(event.target);
    const email = formData.get('email');
    const pass = formData.get('password');
    const rePass = formData.get('repeatPassword');

    try {
        if (!email) {
            throw new Error('Email must be filled!');
        }

        if (pass.length < 6) {
            throw new Error('Password must be at least 6 characters!')
        }

        if (pass !== rePass) {
            throw new Error('The two passwords are not equal!')
        }
    } catch (error) {
        alert(error.message);
        return
    }

    const data = await register({
        'email': email,
        'password': pass
    });

    sessionStorage.setItem('accessToken', data.accessToken);
    sessionStorage.setItem('userId', data.userId);
    await renderHomeView()
}


export async function onLogin(event) {
    event.preventDefault();
    const formData = new FormData(event.target);
    const data = await login({
        'email': formData.get('email'),
        'password': formData.get('password')
    });

    sessionStorage.setItem('accessToken', data.accessToken);
    sessionStorage.setItem('userId', data.userId);
    await renderHomeView()
}


export async function onLogout(event) {
    event.preventDefault();
    await logout();
    sessionStorage.removeItem('accessToken');
    sessionStorage.removeItem('userId');
    renderLoginView();
}