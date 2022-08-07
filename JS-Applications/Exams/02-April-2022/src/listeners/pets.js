import {emptyFields} from "../utils.js";
import {createPet, updatePet} from "../api/pets.js";
import {page} from "../lib.js";


export async function onCreatePet(event) {
    event.preventDefault();
    const formData = new FormData(event.target);

    if (emptyFields(...formData.values())) {
        return
    }

    const pet = {
        "name": formData.get("name"),
        "breed": formData.get("breed"),
        "age": formData.get("age"),
        "weight": formData.get("weight"),
        "image": formData.get("image"),
    };

    await createPet(pet);
    page.redirect("/");
}


export async function onUpdatePet(event) {
    event.preventDefault();
    const formData = new FormData(event.target);

    if (emptyFields(...formData.values())) {
        return
    }

    const pet = {
        "name": formData.get("name"),
        "breed": formData.get("breed"),
        "age": formData.get("age"),
        "weight": formData.get("weight"),
        "image": formData.get("image"),
    };

    const petId = event.target.id;
    await updatePet(pet, petId);
    page.redirect("/");
}
