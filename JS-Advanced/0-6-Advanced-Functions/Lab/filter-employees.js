function filterEmployees(data, criteria) {
    const employees = JSON.parse(data);

    function filter(criteria) {
        if (criteria === 'all') {
            return true;
        }

        const [key, value] = criteria.split('-');

        if (this.hasOwnProperty(key) && this[key] === value) {
            return true;
        }
    }

    return employees.filter(obj => filter.call(obj, criteria)).map(
        (obj, i) => `${i}. ${obj['first_name']} ${obj['last_name']} - ${obj['email']}`
    ).join('\n');
}
