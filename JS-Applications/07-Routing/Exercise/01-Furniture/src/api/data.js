import { createApi } from './api.js';

const api = createApi(null, null, (msg) => alert(msg));

const endpoints = {
    FURNITURE: 'data/catalog'
};

export const login = api.login.bind(api);
export const register = api.register.bind(api);
export const logout = api.logout.bind(api);

export async function getFurniture(page = 1, search) {
    let url = endpoints.FURNITURE + `&offset=${(page - 1) * 5}&pageSize=5`;
    return await api.get(url);
}

export async function getRecipeCount(search) {
    let url = endpoints.RECIPE_COUNT;
    if (search) {
        url += '&where=' + encodeURIComponent(`name like "${search}"`);
    }
    return await api.get(endpoints.RECIPE_COUNT);
}

export async function getRecent() {
    return await api.get(endpoints.RECENT_RECIPES);
}

export async function getRecipeById(id) {
    return await api.get(endpoints.RECIPE_BY_ID + id);
}

export async function createRecipe(recipe) {
    return await api.post(endpoints.RECIPES, recipe);
}

export async function editRecipe(id, recipe) {
    return await api.put(endpoints.RECIPE_BY_ID + id, recipe);
}

export async function deleteRecipeById(id) {
    return await api.delete(endpoints.RECIPE_BY_ID + id);
}

export async function getCommentsByRecipeId(recipeId) {
    return await api.get(endpoints.COMMENTS_BY_RECIPE_ID + encodeURIComponent(`"${recipeId}"`) + '&load=' + encodeURIComponent('author=_ownerId:users'));
}

export async function createComment(comment) {
    const result = await api.post(endpoints.COMMENTS, comment);
    return await api.get(endpoints.COMMENT_BY_ID + result._id + '?load=' + encodeURIComponent('author=_ownerId:users'));
}