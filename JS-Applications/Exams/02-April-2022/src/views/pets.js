import { page, render } from "../lib.js";
import { createPetTemplate, editPetTemplate , petDetailsTemplate } from "../templates/pets.js";
import { onCreatePet, onUpdatePet } from "../listeners/pets.js";
import { getPetById, getDonations, deletePet, donate } from "../api/pets.js";


export function createPetView(ctx) {
    const template = createPetTemplate(onCreatePet);
    render(template, ctx.main);
}


export async function editPetView(ctx) {
    const petId = ctx.params.id;
    const pet = await getPetById(petId);
    const template = editPetTemplate(pet, onUpdatePet);
    render(template, ctx.main);
}


export async function deletePetView(ctx) {
    const petId = ctx.params.id;
    const sure = confirm("Are you sure?");

    if (sure) {
        await deletePet(petId);
        page.redirect("/");
    }

}


export async function petDetailsView(ctx) {
    const petId = ctx.params.id;
    const pet = await getPetById(petId);
    const donations = await getDonations(petId) * 100;
    const template = await petDetailsTemplate(pet, donations);
    render(template, ctx.main);
}


export async function donateView(ctx) {
    const petId = ctx.params.id;
    await donate(petId);
    page.redirect(`/pet-details/${petId}`);
}

