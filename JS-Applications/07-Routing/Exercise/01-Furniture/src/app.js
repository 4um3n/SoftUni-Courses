import { page } from "../node_modules/page/page.js"
import { loginView } from "./views/loginView.js"

page('/', '/login')
page('/login', loginView)

page.start()