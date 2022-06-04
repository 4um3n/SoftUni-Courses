function extractText() {
    const list = Array.from(document.getElementById('items').children);
    document.getElementById('result').value = list.map(el => el.textContent).join('\n');
}