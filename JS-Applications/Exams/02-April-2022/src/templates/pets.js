import { html } from "../lib.js";
import { getUserData } from "../utils.js";
import { userDonated } from "../api/pets.js";


export function createPetTemplate(onSubmit) {
    return html`
        <!--Create Page-->
        <section id="createPage">
            <form @submit=${onSubmit} class="createForm">
                <img src="../../images/cat-create.jpg">
                <div>
                    <h2>Create PetPal</h2>
                    <div class="name">
                        <label for="name">Name:</label>
                        <input name="name" id="name" type="text" placeholder="Max">
                    </div>
                    <div class="breed">
                        <label for="breed">Breed:</label>
                        <input name="breed" id="breed" type="text" placeholder="Shiba Inu">
                    </div>
                    <div class="Age">
                        <label for="age">Age:</label>
                        <input name="age" id="age" type="text" placeholder="2 years">
                    </div>
                    <div class="weight">createPetCardView
                        <label for="weight">Weight:</label>
                        <input name="weight" id="weight" type="text" placeholder="5kg">
                    </div>
                    <div class="image">
                        <label for="image">Image:</label>
                        <input name="image" id="image" type="text" placeholder="./image/dog.jpeg">
                    </div>
                    <button class="btn" type="submit">Create Pet</button>
                </div>
            </form>
        </section>
    `
}


export function editPetTemplate(pet, onSubmit) {
    return html`
        <!--Edit Page-->
        <section id="editPage">
            <form @submit=${onSubmit} id=${pet._id} class="editForm">
                <img src=${pet.image}>
                <div>
                    <h2>Edit PetPal</h2>
                    <div class="name">
                        <label for="name">Name:</label>
                        <input name="name" id="name" type="text" value=${pet.name}>
                    </div>
                    <div class="breed">
                        <label for="breed">Breed:</label>
                        <input name="breed" id="breed" type="text" value=${pet.breed}>
                    </div>
                    <div class="Age">
                        <label for="age">Age:</label>
                        <input name="age" id="age" type="text" value=${pet.age}>
                    </div>
                    <div class="weight">
                        <label for="weight">Weight:</label>
                        <input name="weight" id="weight" type="text" value=${pet.weight}>
                    </div>
                    <div class="image">
                        <label for="image">Image:</label>
                        <input name="image" id="image" type="text" value=${pet.image}>
                    </div>
                    <button class="btn" type="submit">Edit Pet</button>
                </div>
            </form>
        </section>
    `
}


export async function petDetailsTemplate(pet, donations) {
    let HTMLActions;
    const user = getUserData();

    if (user) {
        const creator = pet._ownerId === user.id;
        const donated = await userDonated(pet._id, user.id);
        HTMLActions = await actionsTemplate(creator, donated, pet._id);
    }

    return html`
        <!--Details Page-->
        <section id="detailsPage">
            <div class="details">
                <div class="animalPic">
                    <img src=${pet.image} ">
                </div>
                <div>
                    <div class="animalInfo">
                        <h1>Name: ${pet.name}</h1>
                        <h3>Breed: ${pet.breed}</h3>
                        <h4>Age: ${pet.age}</h4>
                        <h4>Weight: ${pet.weight}</h4>
                        <h4 class="donation">Donation: ${donations}$</h4>
                    </div>
                    ${HTMLActions}
                </div>
            </div>
        </section>
    `
}


function actionsTemplate(creator, donated, petId) {
    let HTMLButtons;

    if (creator) {
        HTMLButtons = creatorButtons(petId)
    } else if (!donated) {
        HTMLButtons = nonCreatorButtons(petId);
    }

    return html`
        <!-- if there is no registered user, do not display div-->
        <div class="actionBtn">
            ${HTMLButtons}
        </div>
    `
}


function creatorButtons(petId) {
    return html`
        <!-- Only for registered user and creator of the pets-->
        <a href="/edit-pet/${petId}" class="edit">Edit</a>
        <a href="/delete-pet/${petId}" class="remove">Delete</a>
    `
}


function nonCreatorButtons(petId) {
    return html`
        <!--(Bonus Part) Only for no creator and user-->
        <a href="/donate/${petId}" class="donate">Donate</a>
    `
}


