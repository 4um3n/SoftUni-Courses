import { post } from "../api/api.js";
import { page } from "../lib.js";
import {emptyFields, setUserData} from "../utils.js";


export async function onRegister(event) {
    event.preventDefault();
    const formData = new FormData(event.target);
    const email = formData.get('email');
    const password = formData.get('password');
    const rePass = formData.get('repeatPassword');

    if (emptyFields(email, password, rePass)) {
        return
    }

    if (password !== rePass) {
        return
    }

    const user = await post('/users/register', {
        email,
        password
    });
    const userData = {
        id: user._id,
        accessToken: user.accessToken,
        email: user.email
    }

    setUserData(userData);
    page.redirect('/');
}


export async function onLogin(event) {
    event.preventDefault();

    const formData = new FormData(event.target);

    if (emptyFields(...formData.values())) {
        return
    }

    const user = await post('/users/login', {
        email: formData.get('email'),
        password: formData.get('password')
    });
    const userData = {
        id: user._id,
        accessToken: user.accessToken,
        email: user.email
    }

    setUserData(userData);
    page.redirect('/');
}
