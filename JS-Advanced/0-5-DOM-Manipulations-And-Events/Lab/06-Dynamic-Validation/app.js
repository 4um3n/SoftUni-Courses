function validate() {
    function onChange(event) {
        const re = /^[a-z]+@[a-z]+(\.[a-z]+)+/g

        if (re.test(event.target.value)) {
            event.target.classList.remove('error');
        } else {
            event.target.classList.add('error');
        }
    }

    document.getElementById('email').addEventListener('change', onChange);
}
