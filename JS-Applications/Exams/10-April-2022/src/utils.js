export function clearUserData() {
    localStorage.removeItem('user');
}


export function setUserData(user) {
    localStorage.setItem('user', JSON.stringify(user));
}


export function getUserData() {
    return JSON.parse(localStorage.getItem('user'));
}


export function emptyFields(...fields) {
    return fields.some(field => !field);
}