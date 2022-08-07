import { page } from "./lib.js";
import { decorateContext, setUpNavigation } from "./middlewares.js";
import { loginView, logoutView, registerView } from "./views/auth.js";
import { dashboardView, homeView } from "./views/home.js";
import {
    createPetView,
    deletePetView,
    donateView,
    editPetView,
    petDetailsView
} from "./views/pets.js";


page(decorateContext);
page(setUpNavigation);
page("/register", registerView);
page("/login", loginView);
page("/logout", logoutView);
page("index.html", "/");
page("/", homeView);
page("/dashboard", dashboardView);
page("/create-pet", createPetView);
page("/edit-pet/:id", editPetView)
page("/delete-pet/:id", deletePetView)
page("/pet-details/:id", petDetailsView)
page("/donate/:id", donateView)


page.start();