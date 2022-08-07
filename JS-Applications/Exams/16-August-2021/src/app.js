import { page } from "./lib.js";
import { decorateContext, setUpNavigation } from "./middlewares.js";
import { loginView, logoutView, registerView } from "./views/auth.js";
import { homeView } from "./views/home.js";
import {
    createGamesView,
    deleteGameView,
    donateView,
    editGameView,
    gameDetailsView
} from "./views/games.js";


page(decorateContext);
page(setUpNavigation);
page("/register", registerView);
page("/login", loginView);
page("/logout", logoutView);
page("index.html", "/");
page("/", homeView);
page("/create-game", createGamesView);
page("/edit-game/:id", editGameView)
page("/delete-game/:id", deleteGameView)
page("/game-details/:id", gameDetailsView)
page("/donate/:id", donateView)


page.start();