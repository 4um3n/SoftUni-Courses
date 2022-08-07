import * as request from "./api.js";


const path = {
    "allPets": "/data/pets?sortBy=_createdOn%20desc&distinct=name",
    "pets": "/data/pets",
    "donation": "/data/donation",
    "totalDonations": (petId) => `/data/donation?where=petId%3D%22${petId}%22&distinct=_ownerId&count`,
    "userDonated": (petId, userId) => `/data/donation?where=petId%3D%22${petId}%22%20and%20_ownerId%3D%22${userId}%22&count`
}


export async function getAllPets() {
    return await request.get(path.allPets)
}


export async function getPetById(petId) {
    return await request.get(`${path.pets}/${petId}`)
}


export async function createPet(pet) {
    return await request.post(path.pets, pet)
}


export async function updatePet(pet, petId) {
    return await request.put(`${path.pets}/${petId}`, pet)
}


export async function deletePet(petId) {
    return await request.del(`${path.pets}/${petId}`)
}


export async function donate(petId) {
    return await request.post(path.donation, {petId});
}


export async function getDonations(petId) {
    return await request.get(path.totalDonations(petId));
}


export async function userDonated(petId, userId) {
    return await request.get(path.userDonated(petId, userId));
}