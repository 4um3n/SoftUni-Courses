function solve() {
    const baseUrl = 'http://localhost:3030/jsonstore/bus/schedule';
    const departBtn = document.querySelector('#depart');
    const arriveBtn = document.querySelector('#arrive');
    const info = document.querySelector('#info span.info');
    let data = {
        name: 'depot',
        next: 'depot'
    };

    async function depart() {
        try {
            const response = await fetch(`${baseUrl}/${data.next}`);
            data = await response.json();
            departBtn.disabled = true;
            arriveBtn.disabled = false;
            info.textContent = `Next stop ${data.name}`;
        } catch (error) {
            info.textContent = error.message;
        }
    }

    function arrive() {
        departBtn.disabled = false;
        arriveBtn.disabled = true;
        info.textContent = `Arriving at ${data.name}`;
    }

    return {
        depart,
        arrive
    };
}

let result = solve();