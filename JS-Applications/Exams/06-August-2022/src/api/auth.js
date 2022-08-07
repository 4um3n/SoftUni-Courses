import * as request from "./api.js"
import { setUserData, clearUserData } from "../utils.js";


const path = {
    "register": "/users/register",
    "login": "/users/login",
    "logout": "/users/logout"
}


export async function register(email, password) {
    const user =  await request.post(path.register, {email, password});
    setUserData({
        id: user._id,
        email: user.email,
        accessToken: user.accessToken
    });
    return user;
}


export async function login(email, password) {
    const user =  await request.post(path.login, {email, password});
    setUserData({
        id: user._id,
        email: user.email,
        accessToken: user.accessToken
    });
    return user;
}


export async function logout() {
    await request.get(path.logout);
    clearUserData();
}
