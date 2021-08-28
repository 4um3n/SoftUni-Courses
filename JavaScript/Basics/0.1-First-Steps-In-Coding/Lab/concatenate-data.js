function concatenateData(input) {
    let firstName, lastName, age, town;
    [firstName, lastName, age, town] = input;
    console.log(`You are ${firstName} ${lastName}, a ${age}-years old person from ${town}.`);
}

concatenateData(['Maria', 'Ivanova', 20, 'Sofia']);
