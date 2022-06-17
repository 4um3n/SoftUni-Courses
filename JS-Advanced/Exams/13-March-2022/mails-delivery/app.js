function solve() {
    const recipientNameInput = document.getElementById('recipientName');
    const titleInput = document.getElementById('title');
    const messageInput = document.getElementById('message');
    const listOfMails = document.getElementById('list');
    const addMailButton = document.getElementById('add');
    const resetInputFieldsButton = document.getElementById('reset');

    addMailButton.type = 'button';
    addMailButton.addEventListener('click', addMail);

    resetInputFieldsButton.type = 'button';
    resetInputFieldsButton.addEventListener('click', resetInputFields)

    function emptyFields(...args) {
        return args.some(el => el.trim().length === 0);
    }

    function resetInputFields() {
        [titleInput, recipientNameInput, messageInput].forEach(el => el.value = '');
    }

    function addMail() {
        if (!emptyFields(recipientNameInput.value, titleInput.value, messageInput.value)) {
            const title = document.createElement('h4');
            const name = document.createElement('h4');
            const message = document.createElement('span');
            const sendButton = document.createElement('button');
            const deleteButton = document.createElement('button');
            const buttonsWrapper = document.createElement('div');
            const mailListItem = document.createElement('li');

            title.textContent = `Title: ${titleInput.value}`
            title.classList.add('email-headers');
            name.textContent = `Recipient Name: ${recipientNameInput.value}`
            name.classList.add('email-headers');
            message.textContent = messageInput.value;

            sendButton.textContent = 'Send';
            sendButton.id = 'send';
            sendButton.type = 'submit';
            sendButton.addEventListener('click', sendEmail);

            deleteButton.textContent = 'Delete';
            deleteButton.id = 'delete';
            deleteButton.type = 'submit';
            deleteButton.addEventListener('click', deleteEmail);

            buttonsWrapper.id = 'list-action';
            [sendButton, deleteButton].forEach(el => buttonsWrapper.appendChild(el));

            [title, name, message, buttonsWrapper].forEach(el => mailListItem.appendChild(el));
            listOfMails.appendChild(mailListItem);
            resetInputFields();
        }
    }

    function parseEmail(dataWrapper) {
        const [titleH4, nameH4] = Array.from(dataWrapper.getElementsByClassName('email-headers')).slice(0, 2);
        const buttonsWrapper = dataWrapper.querySelector('div');
        const titleSpan = document.createElement('span');
        const nameSpan = document.createElement('span');

        titleSpan.textContent = titleH4.textContent;
        titleSpan.classList.add('email-headers');
        nameSpan.textContent = `To: ${nameH4.textContent.split(': ')[1]}`;
        nameSpan.classList.add('email-headers');

        dataWrapper.appendChild(titleSpan);
        dataWrapper.appendChild(nameSpan);
        dataWrapper.replaceChild(titleSpan, titleH4);
        dataWrapper.replaceChild(nameSpan, nameH4);
        dataWrapper.removeChild(buttonsWrapper);
        return dataWrapper;
    }

    function sendEmail(event) {
        const dataWrapper = event.target.parentElement.parentElement;
        const buttonsWrapper = dataWrapper.querySelector('div[id=list-action]')
        const deleteEmailButton = buttonsWrapper.querySelector('button[id=delete]');
        const sendEmailButton = buttonsWrapper.querySelector('button[id=send]');
        const parsedDataWrapper = parseEmail(dataWrapper);

        buttonsWrapper.removeChild(sendEmailButton);
        buttonsWrapper.id = '';
        buttonsWrapper.classList.add('btn');
        deleteEmailButton.classList.add('delete');

        parsedDataWrapper.appendChild(buttonsWrapper);
        parsedDataWrapper.parentElement.removeChild(parsedDataWrapper);
        document.querySelector('div[class=sent-mails] > ul[class=sent-list]').appendChild(parsedDataWrapper);
    }

    function deleteEmail(event) {
        const parsedDataWrapper = parseEmail(event.target.parentElement.parentElement);
        parsedDataWrapper.parentElement.removeChild(parsedDataWrapper);
        document.querySelector('div[class=trash] > ul[class=delete-list]').appendChild(parsedDataWrapper);
    }
}

solve()