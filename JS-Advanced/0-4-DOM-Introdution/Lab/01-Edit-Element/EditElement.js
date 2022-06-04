function editElement(elem, match, replacer) {
    const re = new RegExp(match, 'g');
    elem.innerHTML = elem.innerHTML.replace(re, replacer);
}