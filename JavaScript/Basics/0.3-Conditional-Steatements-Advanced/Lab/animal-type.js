function animalType(input) {
    let animal = input[0].toLowerCase();
    let mammals = ["dog"];
    let reptiles = ["crocodile", "tortoise", "snake"];
    if (mammals.includes(animal)) {
        console.log("mammal");
    } else if (reptiles.includes(animal)) {
        console.log("reptile");
    } else {
        console.log("unknown");
    }
}
