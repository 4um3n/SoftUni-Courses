import {emptyFields} from "../utils.js";
import {createOffer, updateOffer} from "../api/offers.js";
import {page} from "../lib.js";


export async function onCreateOffer(event) {
    event.preventDefault();
    const formData = new FormData(event.target);

    if (emptyFields(...formData.values())) {
        return
    }

    const offer = {
        "title": formData.get("title"),
        "imageUrl": formData.get("imageUrl"),
        "category": formData.get("category"),
        "description": formData.get("description"),
        "requirements": formData.get("requirements"),
        "salary": formData.get("salary"),
    };

    await createOffer(offer);
    page.redirect("/");
}


export async function onEditOffer(event) {
    event.preventDefault();
    const formData = new FormData(event.target);

    if (emptyFields(...formData.values())) {
        return
    }

    const offer = {
        "title": formData.get("title"),
        "imageUrl": formData.get("imageUrl"),
        "category": formData.get("category"),
        "description": formData.get("description"),
        "requirements": formData.get("requirements"),
        "salary": formData.get("salary"),
    };

    const offerId = event.target.id;
    await updateOffer(offer, offerId);
    page.redirect("/");
}
