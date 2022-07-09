async function getInfo() {
    const baseUrl = 'http://localhost:3030/jsonstore/bus/businfo'
    const stopId = document.querySelector('#stopId');
    const stopName = document.querySelector('#stopName');
    const busesList = document.querySelector('#buses');

    try {
        const response = await fetch(`${baseUrl}/${stopId.value}`);

        if (response.ok === false) {
            throw new Error(`${response.status} ${response.statusText}`);
        }

        const data = await response.json();
        stopName.textContent = data.name;

        Object.entries(data.buses).forEach(function ([busId, time]) {
             busesList.innerHTML += `<li>Bus ${busId} arrives in ${time} minutes</li>`;
        });
    } catch (error) {
        stopName.textContent = 'Error';
    }
}
