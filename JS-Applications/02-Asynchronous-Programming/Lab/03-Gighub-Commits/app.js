async function loadCommits() {
    const username = document.querySelector('#username');
    const repo = document.querySelector('#repo');
    const commitsList = document.querySelector('#commits');
    commitsList.innerHTML = '';

    try {
        const response = await fetch(`https://api.github.com/repos/${username.value}/${repo.value}/commits`);

        if (response.ok === false) {
            throw new Error(`Error: ${response.status} (Not Found)`);
        }

        const data = await response.json();

        data.forEach(function (commit) {
            commitsList.innerHTML += `<li>
                                            ${commit.commit.author.name}: ${commit.commit.message}
                                      </li>`;
        });
    } catch (error) {
        commitsList.innerHTML = `<li>${error.message}</li>`;
    }
}