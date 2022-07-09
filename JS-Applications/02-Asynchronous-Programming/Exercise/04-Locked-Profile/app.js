async function lockedProfile() {
    const baseUrl = 'http://localhost:3030/jsonstore/advanced/profiles';
    const response = await fetch(baseUrl);
    const data = await response.json();
    const main = document.querySelector('#main');

    for (const profile of Object.values(data)) {
        const div = document.createElement('div');
        div.classList.add('profile');
        div.innerHTML = `
            <img src="./iconProfile2.png" class="userIcon" />
            <label>Lock</label>
            <input type="radio" name="${profile.username}Locked" value="lock" checked>
            <label>Unlock</label>
            <input type="radio" name="${profile.username}Locked" value="unlock">
            <br>
            <hr>
            <label>Username</label>
            <input type="text" name="user1Username" value="${profile.username}" disabled readonly />
            <div class="user1Username" style="display: none">
                <hr>
                <label>Email:</label>
                <input type="email" name="user1Email" value="${profile.email}" disabled readonly />
                <label>Age:</label>
                <input type="text" name="user1Age" value="${profile.age}" disabled readonly />
            </div>
            <button>Show more</button>
        `;
        div.querySelector('button').addEventListener('click', toggleInfo);
        main.appendChild(div);
    }
}


function toggleInfo(event) {
    const parent = event.target.parentElement;
    const is_locked = parent.querySelector('input[value=lock]').checked;

    if (!is_locked) {
        const button = parent.querySelector('button');
        const content = parent.querySelector('div.user1Username');
        button.textContent = (button.textContent === 'Show more') ? 'Hide it' : 'Show more';
        content.style.display = (content.style.display === 'none') ? 'block' : 'none';
    }
}
