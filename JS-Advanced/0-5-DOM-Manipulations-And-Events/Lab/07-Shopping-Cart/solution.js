function solve() {
    Array.from(document.querySelectorAll('button.add-product')).forEach(
        el => el.addEventListener('click', addProduct));
    document.querySelector('button.checkout').addEventListener('click', checkout);

    const boughtProducts = [];
    let totalPrice = 0;

    function addProduct(event) {
        const parent = event.target.parentElement.parentElement;
        const productName = parent.querySelector('div.product-title').textContent;
        let productPrice = Number(parent.querySelector('div.product-line-price').textContent);
        productPrice = +(productPrice.toFixed(2))

        if (!boughtProducts.includes(productName)) {
            boughtProducts.push(productName);
        }

        totalPrice += productPrice;
        document.querySelector('textarea').textContent +=
            `Added ${productName} for ${productPrice.toFixed(2)} to the cart.\n`
    }

    function checkout(event) {
        const boughtProductsText = boughtProducts.map(
            el => el.charAt(0).toUpperCase() + el.slice(1).toLowerCase()).join(', ');

        document.querySelector('textarea').textContent +=
            `You bought ${boughtProductsText} for ${totalPrice.toFixed(2)}.`

        Array.from(document.querySelectorAll('button.add-product')).forEach(
            el => el.removeEventListener('click', addProduct));

        document.querySelector('button.checkout').removeEventListener('click', checkout);
    }
}
