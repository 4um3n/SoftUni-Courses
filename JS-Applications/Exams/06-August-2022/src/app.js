import { page } from "./lib.js";
import { decorateContext, setUpNavigation } from "./middlewares.js";
import { loginView, logoutView, registerView } from "./views/auth.js";
import { dashboardView, homeView } from "./views/home.js";
import {
    createOfferView,
    deleteOfferView,
    applyView,
    editOfferView,
    offerDetailsView
} from "./views/offers.js";


page(decorateContext);
page(setUpNavigation);
page("/register", registerView);
page("/login", loginView);
page("/logout", logoutView);
page("index.html", "/");
page("/", homeView);
page("/dashboard", dashboardView);
page("/create-offer", createOfferView);
page("/edit-offer/:id", editOfferView)
page("/delete-offer/:id", deleteOfferView)
page("/offer-details/:id", offerDetailsView)
page("/apply/:id", applyView)


page.start();