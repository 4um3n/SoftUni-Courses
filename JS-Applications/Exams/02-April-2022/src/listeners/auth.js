import { page } from "../lib.js";
import { emptyFields } from "../utils.js";
import { register, login } from "../api/auth.js";


export async function onLogin(event) {
    event.preventDefault();
    const formData = new FormData(event.target);

    if (emptyFields(...formData.values())) {
        return
    }

    await login(formData.get('email'), formData.get('password'))
    page.redirect('/')
}


export async function onRegister(event) {
    event.preventDefault();
    const formData = new FormData(event.target);

    if (emptyFields(...formData.values())) {
        return
    }

    if (formData.get('password') !== formData.get('repeatPassword')) {
        return
    }

    await register(formData.get('email'), formData.get('password'))
    page.redirect('/')
}
