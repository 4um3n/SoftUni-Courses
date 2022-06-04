function toggle() {
    const button = document.getElementsByClassName('button')[0];
    const textWrapper = document.getElementById('extra');

    if (textWrapper.style.display === 'none') {
        textWrapper.style.display = 'block';
        button.textContent = 'Less';
    } else {
        textWrapper.style.display = 'none';
        button.textContent = 'More';
    }
}
