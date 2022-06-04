function solve() {
    document.querySelector('#searchBtn').addEventListener('click', onClick);

    function onClick() {
        const searchedText = document.getElementById('searchField').value;
        const tableRows = Array.from(document.querySelectorAll('table tbody tr'));

        for (let i = 0; i < tableRows.length; i++) {
            let isMatched = false;

            for (let cell of Array.from(tableRows[i].children)) {
                if (cell.textContent.includes(searchedText)) {
                    if (!tableRows[i].classList.contains('select')) {
                        tableRows[i].classList.add('select');
                    }
                    isMatched = true;
                    break;
                }
            }

            if (!isMatched && tableRows[i].classList.contains('select')) {
                tableRows[i].classList.remove('select');
            }
        }

        document.getElementById('searchField').value = '';
    }
}
