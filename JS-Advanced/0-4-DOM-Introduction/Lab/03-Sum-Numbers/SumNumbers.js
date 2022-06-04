function calc() {
    const n1 = Number(document.getElementById('num1').value);
    const n2 = Number(document.getElementById('num2').value);
    document.getElementById('sum').value = (!isNaN(n1) && !isNaN(n2)) ? n1 + n2 : 'error';
}
