function yardGardening(input) {
    let area = Number(input[0]);
    let price = area * 7.61;
    let discount = price * 0.18;
    price -= discount;
    console.log(`The final price is: ${price} lv.\nThe discount is: ${discount} lv.`);
}

yardGardening(["550"]);
