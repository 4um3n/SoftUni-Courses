function encodeAndDecodeMessages() {
    function encode(event) {
        const textArea = event.target.parentElement.querySelector('textarea');
        const characters = Array.from(textArea.value).map(
            el => String.fromCharCode(el.charCodeAt(0) + 1)
        );
        document.querySelectorAll('textarea')[1].value = characters.join('');
        textArea.value = '';
    }

    function decode(event) {
        const textArea = event.target.parentElement.querySelector('textarea');
        const characters = Array.from(textArea.value).map(
            el => String.fromCharCode(el.charCodeAt(0) - 1)
        );
        textArea.value = characters.join('');
    }

    const buttons = document.querySelectorAll('button');
    buttons[0].addEventListener('click', encode);
    buttons[1].addEventListener('click', decode);
}
