function pieceOfPie(flavors, startFlavor, endFlavor) {
    const startIndex = flavors.indexOf(startFlavor);
    const endIndex = flavors.indexOf(endFlavor);
    return flavors.slice(startIndex, endIndex + 1);
}


console.log(pieceOfPie(
    [
        'Pumpkin Pie',
        'Key Lime Pie',
        'Cherry Pie',
        'Lemon Meringue Pie',
        'Sugar Cream Pie'
    ],
    'Key Lime Pie',
    'Lemon Meringue Pie'
));
console.log(pieceOfPie(
    [
        'Apple Crisp',
        'Mississippi Mud Pie',
        'Pot Pie',
        'Steak and Cheese Pie',
        'Butter Chicken Pie',
        'Smoked Fish Pie'
    ],
    'Pot Pie',
    'Smoked Fish Pie'
));