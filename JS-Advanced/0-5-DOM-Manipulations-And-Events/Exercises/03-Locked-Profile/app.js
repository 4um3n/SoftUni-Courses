function lockedProfile() {
    Array.from(document.querySelectorAll('button')).forEach(
        el => el.addEventListener('click', showMore)
    );

    function showMore(event) {
        const displayStyleMapper = {
            'block': '',
            '': 'block'
        };
        const buttonTextMapper = {
            'Show more': 'Hide it',
            'Hide it': 'Show more'
        };
        const hiddenDiv = event.target.parentElement.querySelector('div');
        if (event.target.parentElement.querySelector('input[value=unlock]').checked) {
            hiddenDiv.style.display = displayStyleMapper[hiddenDiv.style.display];
            event.target.textContent = buttonTextMapper[event.target.textContent];
        }
    }
}
