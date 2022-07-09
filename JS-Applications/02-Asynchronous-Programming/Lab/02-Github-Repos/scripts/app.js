async function loadRepos() {
    const username = document.querySelector('#username');
    const reposList = document.querySelector('#repos');
    reposList.innerHTML = '';

    try {
        const response = await fetch(`https://api.github.com/users/${username.value}/repos`);

        if (response.ok === false) {
            throw new Error(`${response.status} ${response.statusText}`);
        }

        const data = await response.json();

        data.forEach(function (repo) {
            reposList.innerHTML += `<li>
                                        <a href="${repo.html_url}" target="_blank">
                                            ${repo.full_name}
                                        </a>
                                    </li>`;
        });
    } catch (error) {
        reposList.innerHTML = `<li>${error.message}</li>`;
    }
}