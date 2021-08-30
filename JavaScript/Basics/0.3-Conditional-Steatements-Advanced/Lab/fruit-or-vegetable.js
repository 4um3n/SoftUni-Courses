function fruitOrVegetable(input) {
    let food = input[0];
    let fruits = ["banana", "apple", "kiwi", "cherry", "lemon", "grapes"];
    let vegetables = ["tomato", "cucumber", "pepper", "carrot"];
    if (fruits.includes(food)) {
        console.log("fruit");
    } else if (vegetables.includes(food)) {
        console.log("vegetable");
    } else {
        console.log("unknown");
    }
}