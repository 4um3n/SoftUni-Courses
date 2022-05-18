function moneyNeeded (fruitName, fruitGrams, fruitPricePerKilogram) {
    const fruitKilograms = (fruitGrams / 1000)
    const fruitPrice = (fruitKilograms * fruitPricePerKilogram)
    const result = `I need $${fruitPrice.toFixed(2)} to buy ${fruitKilograms.toFixed(2)} kilograms ${fruitName}.`
    console.log(result)
}

moneyNeeded('orange', 2500, 1.80)
