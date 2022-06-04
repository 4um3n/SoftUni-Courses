function search() {
    const serachedText = document.getElementById('searchText').value;
    const towns = Array.from(document.getElementById('towns').children);
    let totalMatches = 0;

    for (let town of towns) {
        if (town.textContent.includes(serachedText)) {
            totalMatches++;
            town.style.fontWeight = 'bold';
            town.style.textDecoration = 'underline';
        }
    }

    document.getElementById('result').textContent = `${totalMatches.toString()} matches found`;
}
