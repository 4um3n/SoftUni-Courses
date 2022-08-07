import {html} from "../lib.js";


export function loginTemplate(onSubmit) {
    return html`
        <!-- Login Page (Only for Guest users) -->
        <section id="login">
            <div class="form">
                <h2>Login</h2>
                <form @submit=${onSubmit} class="login-form">
                    <input type="text" name="email" id="email" placeholder="email" />
                    <input
                            type="password"
                            name="password"
                            id="password"
                            placeholder="password"
                    />
                    <button type="submit">login</button>
                    <p class="message">
                        Not registered? <a href="/register">Create an account</a>
                    </p>
                </form>
            </div>
        </section>
    `
}


export function registerTemplate(onSubmit) {
    return html`
        <!-- Register Page (Only for Guest users) -->
        <section id="register">
            <div class="form">
                <h2>Register</h2>
                <form @submit=${onSubmit} class="login-form">
                    <input
                            type="text"
                            name="email"
                            id="register-email"
                            placeholder="email"
                    />
                    <input
                            type="password"
                            name="password"
                            id="register-password"
                            placeholder="password"
                    />
                    <input
                            type="password"
                            name="re-password"
                            id="repeat-password"
                            placeholder="repeat password"
                    />
                    <button type="submit">register</button>
                    <p class="message">Already registered? <a href="/login">Login</a></p>
                </form>
            </div>
        </section>
    `
}