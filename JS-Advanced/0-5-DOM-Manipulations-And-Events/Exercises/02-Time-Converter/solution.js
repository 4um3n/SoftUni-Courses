function attachEventsListeners() {
    Array.from(document.querySelectorAll('input[value=Convert]')).forEach(
        el => el.addEventListener('click', convert)
    );

    function convert(event) {
        const convertMapper = {
            'days': n => [
                n,
                n*24,
                n*1440,
                n*86400
            ],
            'hours': n => [
                n / 24,
                n,
                n * 60,
                n * 3600
            ],
            'minutes': n => [
                n / 1400,
                n / 60,
                n,
                n * 60,
            ],
            'seconds': n => [
                n / 86400,
                n / 3600,
                n / 60,
                n
            ]
        };

        const numberInputField = event.target.parentElement.querySelector('input[type=text]');
        const convertedValues = convertMapper[numberInputField.id](Number(numberInputField.value));

        Array.from(document.querySelectorAll('input[type=text]')).forEach(
            el => el.value = convertedValues.shift()
        );

    }
}
