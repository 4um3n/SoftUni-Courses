class Contact {
    constructor(firstName, lastName, phone, email) {
        this.firstName = firstName;
        this.lastName = lastName;
        this.phone = phone;
        this.email = email;
        this.wrapper = this._getHTMLStructure();
        this.online = false;
    }

    get online() {
        return this._online;
    }

    set online(value) {
        this._online = value;
        const titleWrapper = this.wrapper.querySelector('div.title');

        if (value) {
            titleWrapper.classList.add('online');
        } else {
            titleWrapper.classList.remove('online');
        }
     }


    _getHTMLStructure() {
        const wrapper = document.createElement('article');
        const titleWrapper = document.createElement('div');
        const infoWrapper = document.createElement('div');
        const infoButton = document.createElement('button');
        const phoneSpan = document.createElement('span');
        const emailSpan = document.createElement('span');

        infoButton.textContent = 'ℹ';
        infoButton.addEventListener('click', this.toggleInfo);
        titleWrapper.classList.add('title');
        titleWrapper.textContent = `${this.firstName} ${this.lastName}`;
        titleWrapper.appendChild(infoButton);

        phoneSpan.textContent = `☎ ${this.phone}`;
        emailSpan.textContent = `✉ ${this.email}`;
        infoWrapper.classList.add('info');
        infoWrapper.style.display = 'none';
        infoWrapper.appendChild(phoneSpan);
        infoWrapper.appendChild(emailSpan);

        wrapper.appendChild(titleWrapper);
        wrapper.appendChild(infoWrapper);
        return wrapper;
    }

    render(id) {
        document.getElementById(id).appendChild(this.wrapper);
    }

    toggleInfo(event) {
        event.target.parentElement.parentElement.querySelector('div.info').style.display = 'block';
    }
}

function main() {
    let contacts = [
        new Contact("Ivan", "Ivanov", "0888 123 456", "i.ivanov@gmail.com"),
        new Contact("Maria", "Petrova", "0899 987 654", "mar4eto@abv.bg"),
        new Contact("Jordan", "Kirov", "0988 456 789", "jordk@gmail.com")
    ];
    contacts.forEach(c => c.render('main'));

    // After 1 second, change the online status to true
    setTimeout(() => contacts[1].online = true, 2000);
}
