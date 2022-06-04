function subtract() {
    const n1 = Number(document.getElementById('firstNumber').value);
    const n2 = Number(document.getElementById('secondNumber').value);
    document.getElementById('result').textContent = (!isNaN(n1) && !isNaN(n2)) ? n1 - n2 : 'error';
}