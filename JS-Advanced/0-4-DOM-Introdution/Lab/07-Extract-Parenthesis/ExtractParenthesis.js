function extract(content) {
    const text = document.getElementById(content).textContent;
    const re = /\(([^)]+)\)/g;
    return text.match(re).join('; ');
}
