import * as request from "./api.js";


const path = {
    "recentGames": `/data/games?sortBy=_createdOn%20desc&distinct=category`,
    "allGames": "/data/games?sortBy=_createdOn%20desc",
    "games": "/data/games",
    "donation": "/data/donation",
    "totalDonations": (gameId) => `/data/donation?where=gameId%3D%22${gameId}%22&distinct=_ownerId&count`,
    "commentsByGame": (gameId, userId) => `/data/donation?where=gameId%3D%22${gameId}%22%20and%20_ownerId%3D%22${userId}%22&count`
}


export async function getAllGames() {
    return await request.get(path.recentGames)
}


export async function getGameById(petId) {
    return await request.get(`${path.games}/${petId}`)
}


export async function createGame(game) {
    return await request.post(path.games, game)
}


export async function updateGame(game, gameId) {
    return await request.put(`${path.games}/${gameId}`, game)
}


export async function deleteGame(gameId) {
    return await request.del(`${path.games}/${gameId}`)
}


export async function donate(gameId) {
    return await request.post(path.donation, {petId: gameId});
}


export async function getDonations(gameId) {
    return await request.get(path.totalDonations(gameId));
}


export async function userDonated(gameId, userId) {
    return await request.get(path.userDonated(gameId, userId));
}