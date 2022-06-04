function solve() {
    const conversionMapper = {
        'Camel Case': text => {
            let words = text.split(' ').map(el => el.toLowerCase());
            words = words.map((el, ind) => (ind > 0) ? el.charAt(0).toUpperCase() + el.slice(1) : el);
            return words.join('')
        },

        'Pascal Case': text => {
            let words = text.split(' ').map(el => el.toLowerCase());
            words = words.map(el => el.charAt(0).toUpperCase() + el.slice(1));
            return words.join('')
        }
    };

    const text = document.getElementById('text').value;
    const textCase = document.getElementById('naming-convention').value;
    document.getElementById('result').textContent = (textCase in conversionMapper) ? conversionMapper[textCase](text) : 'Error!'
}
