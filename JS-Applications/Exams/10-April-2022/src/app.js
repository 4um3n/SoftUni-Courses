import { page }  from './lib.js';
import {
    dashboardView,
    userDashboardView,
    createPostView,
    editPostView,
    deletePostView,
    postDetailsView,
    donate
} from "./views/posts.js";
import { loginView, logoutView, registerView } from "./views/auth.js";
import { decorateContext, setUpNavigation } from "./middlewares.js";


page(decorateContext);
page(setUpNavigation);
page('/register', registerView);
page('/login', loginView);
page('/logout', logoutView);
page('/index.html', '/');
page('/', dashboardView);
page('/my-posts', userDashboardView);
page('/details/:id', postDetailsView);
page('/create-post', createPostView);
page('/edit-post/:id', editPostView);
page('/delete-post/:id', deletePostView);
page('/donate/:id', donate);

page.start();
