function colorize() {
    Array.from(document.querySelectorAll('tr:nth-child(even)')).forEach(
        el => el.style.background = 'Teal'
    );
}
