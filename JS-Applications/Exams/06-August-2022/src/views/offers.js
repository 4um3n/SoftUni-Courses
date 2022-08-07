import { page, render } from "../lib.js";
import { createOfferTemplate, editOfferTemplate , offerDetailsTemplate } from "../templates/offers.js";
import { onCreateOffer, onEditOffer } from "../listeners/offers.js";
import { getOfferById, getApplications, deleteOffer, apply } from "../api/offers.js";


export function createOfferView(ctx) {
    const template = createOfferTemplate(onCreateOffer);
    render(template, ctx.main);
}


export async function editOfferView(ctx) {
    const offerId = ctx.params.id;
    const offer = await getOfferById(offerId);
    const template = editOfferTemplate(offer, onEditOffer);
    render(template, ctx.main);
}


export async function deleteOfferView(ctx) {
    const offerId = ctx.params.id;
    const sure = confirm("Are you sure?");

    if (sure) {
        await deleteOffer(offerId);
        page.redirect("/");
    }

}


export async function offerDetailsView(ctx) {
    const offerId = ctx.params.id;
    const offer = await getOfferById(offerId);
    const applications = await getApplications(offerId);
    const template = await offerDetailsTemplate(offer, applications);
    render(template, ctx.main);
}


export async function applyView(ctx) {
    const offerId = ctx.params.id;
    await apply(offerId);
    page.redirect(`/offer-details/${offerId}`);
}

