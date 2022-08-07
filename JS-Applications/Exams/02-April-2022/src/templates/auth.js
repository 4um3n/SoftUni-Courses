import {html} from "../lib.js";


export function loginTemplate(onSubmit) {
    return html`
        <!--Login Page-->
        <section id="loginPage">
            <form @submit=${onSubmit} class="loginForm">
                <img src="../../images/logo.png" alt="logo" />
                <h2>Login</h2>

                <div>
                    <label for="email">Email:</label>
                    <input id="email" name="email" type="text" placeholder="steven@abv.bg" value="">
                </div>

                <div>
                    <label for="password">Password:</label>
                    <input id="password" name="password" type="password" placeholder="********" value="">
                </div>

                <button class="btn" type="submit">Login</button>

                <p class="field">
                    <span>If you don't have profile click <a href="/register">here</a></span>
                </p>
            </form>
        </section>
    `
}


export function registerTemplate(onSubmit) {
    return html`
        <!--Register Page-->
        <section id="registerPage">
            <form @submit=${onSubmit} class="registerForm">
                <img src="../../images/logo.png" alt="logo" />
                <h2>Register</h2>
                <div class="on-dark">
                    <label for="email">Email:</label>
                    <input id="email" name="email" type="text" placeholder="steven@abv.bg" value="">
                </div>

                <div class="on-dark">
                    <label for="password">Password:</label>
                    <input id="password" name="password" type="password" placeholder="********" value="">
                </div>

                <div class="on-dark">
                    <label for="repeatPassword">Repeat Password:</label>
                    <input id="repeatPassword" name="repeatPassword" type="password" placeholder="********" value="">
                </div>

                <button class="btn" type="submit">Register</button>

                <p class="field">
                    <span>If you have profile click <a href="/login">here</a></span>
                </p>
            </form>
        </section>
    `
}