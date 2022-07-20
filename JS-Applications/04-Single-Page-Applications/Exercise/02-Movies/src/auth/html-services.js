import { html } from 'https://unpkg.com/lit-html?module'
import { createNavigation, createFooter } from "../html-services.js";
import { onLogin, onRegister } from "./listeners.js";


export function createLoginView() {
    return html`
        ${createNavigation()}
        <section id="form-login" class="view-section">
            <form
                    id="login-form"
                    class="text-center border border-light p-5"
                    action=""
                    method=""
                    @submit=${onLogin}
            >
                <div class="form-group">
                    <label for="email">Email</label>
                    <input
                            id="email"
                            type="email"
                            class="form-control"
                            placeholder="Email"
                            name="email"
                            value=""
                    />
                </div>
                <div class="form-group">
                    <label for="password">Password</label>
                    <input
                            id="password"
                            type="password"
                            class="form-control"
                            placeholder="Password"
                            name="password"
                            value=""
                    />
                </div>

                <button type="submit" class="btn btn-primary">Login</button>
            </form>
        </section>
        ${createFooter()}
    `
}


export function createRegisterView() {
    return html`
        ${createNavigation()}

        <section id="form-sign-up" class="view-section">
            <form
                    id="register-form"
                    class="text-center border border-light p-5"
                    action=""
                    method=""
                    @submit=${onRegister}
            >
                <div class="form-group">
                    <label for="email">Email</label>
                    <input
                            id="email"
                            type="email"
                            class="form-control"
                            placeholder="Email"
                            name="email"
                            value=""
                    />
                </div>
                <div class="form-group">
                    <label for="password">Password</label>
                    <input
                            id="password"
                            type="password"
                            class="form-control"
                            placeholder="Password"
                            name="password"
                            value=""
                    />
                </div>

                <div class="form-group">
                    <label for="repeatPassword">Repeat Password</label>
                    <input
                            id="repeatPassword"
                            type="password"
                            class="form-control"
                            placeholder="Repeat-Password"
                            name="repeatPassword"
                            value=""
                    />
                </div>

                <button type="submit" class="btn btn-primary">Register</button>
            </form>
        </section>
        ${createFooter()}
    `
}