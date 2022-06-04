function solve() {
    const option1 = document.createElement('option');
    option1.value = 'hexdecimal';
    option1.textContent = 'Hexdecimal';

    const option2 = document.createElement('option');
    option2.value = 'binary';
    option2.textContent = 'Binary';

    const convertToOptions = document.getElementById('selectMenuTo');
    convertToOptions.appendChild(option1);
    convertToOptions.appendChild(option2);

    document.getElementsByTagName('button')[0].addEventListener('click', onClick)

    function onClick() {
        function decimalToHexdecimal(num) {
            return num.toString(16);
        }

        function decimalToBinary(num) {
            let bin = 0;
            let rem, i = 1;

            while (num !== 0) {
                rem = num % 2;
                num = parseInt(num / 2);
                bin = bin + rem * i;
                i *= 10;
            }

            return bin;
        }

        const convertionMapper = {
            'hexdecimal': decimalToHexdecimal,
            'binary': decimalToBinary
        };

        const n = Number(document.getElementById('input').value);
        const convertTo = document.getElementById('selectMenuTo').value;

        document.getElementById('result').value = convertionMapper[convertTo](n);
    }
}
