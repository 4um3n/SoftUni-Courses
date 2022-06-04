function solve() {
    const text = document.getElementById('input').value;
    const re = /[A-Za-z\d]+/g
    const sentences = text.split('.').filter(el => re.test(el.toString())).map(el => `${el}.`);
    const output = document.getElementById('output')

    while (sentences.length > 0) {
        const textForParagraph = sentences.splice(0, 3).join(' ');
        const p = document.createElement('p');
        p.textContent = textForParagraph;
        output.appendChild(p);
    }
}
