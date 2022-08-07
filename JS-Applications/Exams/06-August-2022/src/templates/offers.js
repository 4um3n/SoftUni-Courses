import {html} from "../lib.js";
import {getUserData} from "../utils.js";
import {userApplied} from "../api/offers.js";


export function createOfferTemplate(onSubmit) {
    return html`
        <!-- Create Page (Only for logged-in users) -->
        <section id="create">
            <div class="form">
                <h2>Create Offer</h2>
                <form @submit=${onSubmit} class="create-form">
                    <input
                            type="text"
                            name="title"
                            id="job-title"
                            placeholder="Title"
                    />
                    <input
                            type="text"
                            name="imageUrl"
                            id="job-logo"
                            placeholder="Company logo url"
                    />
                    <input
                            type="text"
                            name="category"
                            id="job-category"
                            placeholder="Category"
                    />
                    <textarea
                            id="job-description"
                            name="description"
                            placeholder="Description"
                            rows="4"
                            cols="50"
                    ></textarea>
                    <textarea
                            id="job-requirements"
                            name="requirements"
                            placeholder="Requirements"
                            rows="4"
                            cols="50"
                    ></textarea>
                    <input
                            type="text"
                            name="salary"
                            id="job-salary"
                            placeholder="Salary"
                    />

                    <button type="submit">post</button>
                </form>
            </div>
        </section>
    `
}


export function editOfferTemplate(offer, onSubmit) {
    return html`
        <!-- Edit Page (Only for logged-in users) -->
        <section id="edit">
          <div class="form">
            <h2>Edit Offer</h2>
            <form @submit="${onSubmit}" id=${offer._id} class="edit-form">
              <input
                type="text"
                name="title"
                id="job-title"
                placeholder="Title"
                value=${offer.title}
              />
              <input
                type="text"
                name="imageUrl"
                id="job-logo"
                placeholder="Company logo url"
                value=${offer.imageUrl}
              />
              <input
                type="text"
                name="category"
                id="job-category"
                placeholder="Category"
                value=${offer.category}
              />
              <textarea
                id="job-description"
                name="description"
                placeholder="Description"
                rows="4"
                cols="50"
              >${offer.description}</textarea>
              <textarea
                id="job-requirements"
                name="requirements"
                placeholder="Requirements"
                rows="4"
                cols="50"
              >${offer.requirements}</textarea>
              <input
                type="text"
                name="salary"
                id="job-salary"
                placeholder="Salary"
                value=${offer.salary}
              />

              <button type="submit">post</button>
            </form>
          </div>
        </section>
    `
}


export async function offerDetailsTemplate(offer, applications) {
    let HTMLButtons;
    const user = getUserData();

    if (user) {
        if (offer._ownerId === user.id) {
            HTMLButtons = creatorButtonsTemplate(offer._id)
        } else if (! await userApplied(offer._id, user.id)) {
            HTMLButtons = nonCreatorButtonsTemplate(offer._id)
        }
    }

    return html`
        <!-- Details page -->
        <section id="details">
            <div id="details-wrapper">
                <img id="details-img" src=${offer.imageUrl} alt="example1"/>
                <p id="details-title">${offer.title}</p>
                <p id="details-category">
                    Category: <span id="categories">${offer.category}</span>
                </p>
                <p id="details-salary">
                    Salary: <span id="salary-number">${offer.salary}</span>
                </p>
                <div id="info-wrapper">
                    <div id="details-description">
                        <h4>Description</h4>
                        <span>${offer.description}</span>
                    </div>
                    <div id="details-requirements">
                        <h4>Requirements</h4>
                        <span>${offer.requirements}</span>
                    </div>
                </div>
                <p>Applications: <strong id="applications">${applications}</strong></p>
                <!--Edit and Delete are only for creator-->
                <div id="action-buttons">
                    ${HTMLButtons}
                </div>
            </div>
        </section>
    `
}


function creatorButtonsTemplate(offerId) {
    return html`
        <a href="/edit-offer/${offerId}" id="edit-btn">Edit</a>
        <a href="/delete-offer/${offerId}" id="delete-btn">Delete</a>
    `
}


function nonCreatorButtonsTemplate(offerId) {
    return html`
        <!--Bonus - Only for logged-in users ( not authors )-->
        <a href="/apply/${offerId}" id="apply-btn">Apply</a>
    `
}


