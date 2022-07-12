function attachEvents() {
    document.querySelector('#submit').addEventListener('click', onSubmit)
    window.addEventListener('load', refreshTable);
}

function areEmpty(...fields) {
    return !fields.every(field => field.value);
}

async function onSubmit(event) {
    const firstName = document.querySelector('input[name=firstName]');
    const lastName = document.querySelector('input[name=lastName]');
    const facultyNumber = document.querySelector('input[name=facultyNumber]');
    const grade = document.querySelector('input[name=grade]');

    if (areEmpty(firstName, lastName, facultyNumber, grade)) {
        return
    }

    try {
        await createStudent(firstName.value, lastName.value, facultyNumber.value, grade.value)
        firstName.value = ''
        lastName.value = ''
        facultyNumber.value = ''
        grade.value = ''
    } catch (error) {
        alert(error.message);
    }

}

async function createStudent(firstName, lastName, facultyNumber, grade) {
    const body = JSON.stringify({
        firstName,
        lastName,
        facultyNumber,
        grade
    });
    const response = await fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body
    });
    const data = await response.json();

    if (response.status !== 200) {
        throw new Error(data.message);
    }
}

async function refreshTable() {
    const table = document.querySelector('#results tbody');
    table.innerHTML = '';
    const data = await (await fetch(url)).json();

    for (const student of Object.values(data)) {
        table.appendChild(
            e('tr', {},
                e('th', {}, student.firstName),
                e('th', {}, student.lastName),
                e('th', {}, student.facultyNumber),
                e('th', {}, student.grade),
            )
        );
    }

}

function e(type, attributes, ...content) {
    const result = document.createElement(type);

    for (let [attr, value] of Object.entries(attributes || {})) {
        if (attr.substring(0, 2) == 'on') {
            result.addEventListener(attr.substring(2).toLocaleLowerCase(), value);
        } else {
            result[attr] = value;
        }
    }

    content = content.reduce((a, c) => a.concat(Array.isArray(c) ? c : [c]), []);

    content.forEach(e => {
        if (typeof e == 'string' || typeof e == 'number') {
            const node = document.createTextNode(e);
            result.appendChild(node);
        } else {
            result.appendChild(e);
        }
    });

    return result;
}

const url = 'http://localhost:3030/jsonstore/collections/students';
attachEvents();