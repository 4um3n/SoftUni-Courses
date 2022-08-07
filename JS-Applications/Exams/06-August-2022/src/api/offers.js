import * as request from "./api.js";


const path = {
    "offers": "/data/offers",
    "allOffers": "/data/offers?sortBy=_createdOn%20desc",
    "applications": "/data/applications",
    "totalApplications": (offerId) => `/data/applications?where=offerId%3D%22${offerId}%22&distinct=_ownerId&count`,
    "userApplied": (offerId, userId) => `/data/applications?where=offerId%3D%22${offerId}%22%20and%20_ownerId%3D%22${userId}%22&count`
}


export async function getAllOffers() {
    return await request.get(path.allOffers)
}


export async function getOfferById(offerId) {
    return await request.get(`${path.offers}/${offerId}`)
}


export async function createOffer(offer) {
    return await request.post(path.offers, offer)
}


export async function updateOffer(pet, petId) {
    return await request.put(`${path.offers}/${petId}`, pet)
}


export async function deleteOffer(offerId) {
    return await request.del(`${path.offers}/${offerId}`)
}


export async function apply(offerId) {
    return await request.post(path.applications, {offerId: offerId});
}


export async function getApplications(offerId) {
    return await request.get(path.totalApplications(offerId));
}


export async function userApplied(offerId, userId) {
    return await request.get(path.userApplied(offerId, userId));
}