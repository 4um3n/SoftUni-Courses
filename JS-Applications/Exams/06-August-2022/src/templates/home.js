import {html} from "../lib.js";


export function homeTemplate() {
    return html`
        <!-- Home page -->
        <section id="home">
            <img
                    src="../../images/pngkey.com-hunting-png-6697165-removebg-preview.png"
                    alt="home"
            />
            <h2>Searching for a job?</h2>
            <h3>The right place for a new career start!</h3>
        </section>
    `
}


export function dashboardTemplate(offers) {
    const HTMLOffers = (offers.length <= 0) ? noOffersTemplate() : offers.map(o => offerCardTemplate(o))
    return html`
        <!-- Dashboard page -->
        <section id="dashboard">
            <h2>Job Offers</h2>

            ${HTMLOffers}
            
        </section>
    `
}


function offerCardTemplate(offer) {
    return html`
        <!-- Display a div with information about every post (if any)-->
        <div class="offer">
            <img src=${offer.imageUrl} alt="example1" />
            <p>
                <strong>Title: </strong><span class="title">${offer.title}</span>
            </p>
            <p><strong>Salary:</strong><span class="salary">${offer.salary}</span></p>
            <a class="details-btn" href="/offer-details/${offer._id}">Details</a>
        </div>
    `
}


function noOffersTemplate() {
    return html`
        <!-- Display an h2 if there are no posts -->
        <h2>No offers yet.</h2>         
    `
}