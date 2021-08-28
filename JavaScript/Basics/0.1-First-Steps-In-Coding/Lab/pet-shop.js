function petShop(input) {
    let dogsCount = Number(input[0]);
    let othersCount = Number(input[1]);
    let result = dogsCount * 2.50 + othersCount * 4;
    console.log(`${result} lv.`);
}

petShop(["13", "9"]);