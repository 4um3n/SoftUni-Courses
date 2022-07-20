import { sendRequest } from '../rest-services.js'


export async function register(user) {
    const init = {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(user)
    }
    return await sendRequest('http://localhost:3030/users/register', init);
}


export async function login(user) {
    const init = {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(user)
    }
    return await sendRequest('http://localhost:3030/users/login', init);
}


export async function logout() {
    try {
        const response = await fetch('http://localhost:3030/users/logout', {
            method: 'GET',
            headers: {
                'X-Authorization': sessionStorage.getItem('accessToken')
            }
        });

        if (response.status !== 204) {
            throw new Error(`${response.status} ${response.statusText}`);
        }
    } catch (error) {
        alert(error.message);
    }
}


export async function getUser() {
    const init = {
        method: 'GET',
        headers: {
            'X-Authorization': sessionStorage.getItem('accessToken')
        }
    }
    return await sendRequest('http://localhost:3030/users/me', init);
}

