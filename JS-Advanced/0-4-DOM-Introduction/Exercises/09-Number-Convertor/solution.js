function solve() {
    const option1 = document.createElement('option');
    option1.value = 'hexadecimal';
    option1.textContent = 'Hexadecimal';

    const option2 = document.createElement('option');
    option2.value = 'binary';
    option2.textContent = 'Binary';

    const convertToOptions = document.getElementById('selectMenuTo');
    convertToOptions.appendChild(option1);
    convertToOptions.appendChild(option2);

    document.getElementsByTagName('button')[0].addEventListener('click', onClick)

    function onClick() {
        function decimalToHexadecimal(num) {
            return num.toString(16).toLocaleUpperCase();
        }

        function decimalToBinary(num) {
            return num.toString(2);
        }

        const convertMapper = {
            'hexadecimal': decimalToHexadecimal,
            'binary': decimalToBinary
        };

        const n = Number(document.getElementById('input').value);
        const convertTo = document.getElementById('selectMenuTo').value;

        document.getElementById('result').value = convertMapper[convertTo](n);
    }
}
