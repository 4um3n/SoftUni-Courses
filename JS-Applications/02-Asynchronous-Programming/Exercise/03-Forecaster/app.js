function attachEvents() {
    const allLocationsUrl = 'http://localhost:3030/jsonstore/forecaster/locations';
    const currentWhetherUrl = 'http://localhost:3030/jsonstore/forecaster/today';
    const upcomingWhetherUrl = 'http://localhost:3030/jsonstore/forecaster/upcoming';
    const whetherWrapper = document.querySelector('#forecast');
    const current = document.querySelector('#current');
    const upcoming = document.querySelector('#upcoming');
    const whetherLocation = document.querySelector('#location');
    const symbolsMapper = {
        'Sunny': '&#x2600;',
        'Partly sunny': '&#x26C5;',
        'Overcast': '&#x2601;',
        'Rain': '&#x2614; ',
        'Degrees': '&#176;'
    };

    const currentWhether = document.createElement('div');
    currentWhether.classList.add('forecasts');

    const upcomingWhether = document.createElement('div');
    upcomingWhether.classList.add('forecast-info')

    document.querySelector('#submit').addEventListener('click', getLocation);

    async function getLocation(event) {
        try {
            const response = await fetch(allLocationsUrl);

            if (response.ok === false) {
                throw new Error(`Error`);
            }

            const data = await response.json();
            const code = data.filter(el => el.name === whetherLocation.value)[0].code;

            whetherWrapper.style.display = 'block';
            currentWhether.innerHTML = '';
            upcomingWhether.innerHTML = '';
            whetherLocation.value = '';

            await setCurrentWhether(code)
            await setUpcomingWhether(code)

        } catch (error) {
            whetherWrapper.style.display = 'block';
            currentWhether.textContent = 'Error';
            upcomingWhether.textContent = 'Error';
            current.appendChild(currentWhether);
            upcoming.appendChild(upcomingWhether);
            whetherLocation.value = '';
        }
    }

    async function setCurrentWhether(code) {
        const response = await fetch(`${currentWhetherUrl}/${code}`);
        const data = await response.json();
        currentWhether.innerHTML = `
            <span class="condition symbol">${symbolsMapper[data.forecast.condition]}</span>
            <span class="condition">
                <span class="forecast-data">${data.name}</span>
                <span class="forecast-data">${data.forecast.low}${symbolsMapper.Degrees}/${data.forecast.high}${symbolsMapper.Degrees}</span>
                <span class="forecast-data">${data.forecast.condition}</span>
            </span>
        `;
        current.appendChild(currentWhether);
    }

    async function setUpcomingWhether(code) {
        const response = await fetch(`${upcomingWhetherUrl}/${code}`);
        const data = await response.json();

        for (const day of data.forecast) {
            const span = document.createElement('span');
            span.classList.add('upcoming');
            span.innerHTML = `
                <span class="symbol">${symbolsMapper[day.condition]}</span>
                <span class="forecast-data">${day.low}${symbolsMapper.Degrees}/${day.high}${symbolsMapper.Degrees}</span>
                <span class="forecast-data">${day.condition}</span>
            `;
            upcomingWhether.appendChild(span);
        }

        upcoming.appendChild(upcomingWhether);
    }
}

attachEvents();
