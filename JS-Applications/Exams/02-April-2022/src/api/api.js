import {clearUserData, getUserData} from "../utils.js";

const host = 'http://localhost:3030';


function getInit(method, data) {
    const init = {
        'method': method,
        'headers': {}
    }

    if (data) {
        init.headers['Content-Type'] = 'application/json';
        init.body = JSON.stringify(data)
    }

    const user = getUserData();

    if (user) {
        init.headers['X-Authorization'] = user.accessToken;
    }

    return init;
}


async function request(path, init) {
    const url = `${host}${path}`;

    try {
        const response = await fetch(url, init);

        if (!response.ok) {
            if (response.status === 403) {
                clearUserData();
            }

            const data = await response.json();
            throw new Error(data.message);
        }

        if (response.status === 204) {
            return response
        } else {
            return response.json();
        }

    } catch (error) {
        alert(error.message);
        console.log(error.message);
        throw error;
    }
}


export async function get(path) {
    return await request(path, getInit('GET'));
}

export async function post(path, data) {
    const init = getInit('POST', data);
    return await request(path, init);
}

export async function put(path, data) {
    const init = getInit('PUT', data);
    return await request(path, init);
}

export async function del(path, data) {
    const init = getInit('DELETE', data);
    return await request(path, init);
}
