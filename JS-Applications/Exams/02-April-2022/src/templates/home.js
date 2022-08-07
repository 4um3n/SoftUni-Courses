import {html} from "../lib.js";


export function homeTemplate() {
    return html`
        <!--Welcome Page-->
        <section class="welcome-content">
            <article class="welcome-content-text">
                <h1>We Care</h1>
                <h1 class="bold-welcome">Your Pets</h1>
                <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod.</p>
            </article>
            <article class="welcome-content-image">
                <img src="../../images/header-dog.png" alt="dog">
            </article>
        </section>
    `
}


export function dashboardTemplate(pets) {
    const HTMLPets = (pets.length <= 0) ? noPetsTemplate() : pets.map(p => petCardTemplate(p))
    return html`
        <!--Dashboard-->
        <section id="dashboard">
            <h2 class="dashboard-title">Services for every animal</h2>
            <div class="animals-dashboard">
                ${HTMLPets}
            </div>
        </section>
    `
}


function petCardTemplate(pet) {
    return html`
        <div class="animals-board">
            <article class="service-img">
                <img class="animal-image-cover" src=${pet.image}>
            </article>
            <h2 class="name">${pet.name}</h2>
            <h3 class="breed">${pet.breed}</h3>
            <div class="action">
                <a class="btn" href="/pet-details/${pet._id}">Details</a>
            </div>
        </div>
    `
}


function noPetsTemplate() {
    return html`
        <!--If there is no pets in dashboard-->
        <div>
            <p class="no-pets">No pets in dashboard</p>
        </div>           
    `
}