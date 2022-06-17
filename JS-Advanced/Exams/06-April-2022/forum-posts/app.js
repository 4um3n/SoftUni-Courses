window.addEventListener("load", solve);

function solve() {
    document.getElementById('publish-btn').addEventListener('click', publish);
    const titleField = document.getElementById('post-title');
    const categoryField = document.getElementById('post-category');
    const contentField = document.getElementById('post-content');
    const reviewList = document.getElementById('review-list');
    const publishedList = document.getElementById('published-list');
    document.getElementById('clear-btn').addEventListener('click', clear);

    function edit(event) {
        const li = event.target.parentElement;
        titleField.value = li.querySelector('article h4').textContent;
        categoryField.value = li.querySelectorAll('article p')[0].textContent.split(':')[1].trim();
        contentField.value = li.querySelectorAll('article p')[1].textContent.split(':')[1].trim();
        li.parentElement.removeChild(li);
    }


    function approve(event) {
        const li = event.target.parentElement;
        Array.from(li.querySelectorAll('button')).forEach(el => li.removeChild(el));
        li.parentElement.removeChild(li);
        publishedList.appendChild(li);
    }


    function clear(event) {
        Array.from(publishedList.children).forEach(
            el => el.parentElement.removeChild(el)
        );
    }


    function emptyFields(...args) {
        return args.some(el => el.trim().length === 0);
    }


    function publish(event) {
        if (!emptyFields(titleField.value, categoryField.value, contentField.value)) {
            const dataWrapper = document.createElement('article');
            const title = document.createElement('h4');
            const category = document.createElement('p');
            const content = document.createElement('p');
            const editButton = document.createElement('button');
            const approveButton = document.createElement('button');
            const li = document.createElement('li');

            title.textContent = titleField.value;
            category.textContent = `Category: ${categoryField.value}`;
            content.textContent = `Content: ${contentField.value}`;
            [title, category, content].forEach(el => dataWrapper.appendChild(el));

            editButton.classList.add('action-btn', 'edit');
            editButton.textContent = 'Edit';
            editButton.addEventListener('click', edit);

            approveButton.classList.add('action-btn', 'approve');
            approveButton.textContent = 'Approve';
            approveButton.addEventListener('click', approve);

            li.classList.add('rpost');
            [dataWrapper, editButton, approveButton].forEach(el => li.appendChild(el));
            reviewList.appendChild(li);

            titleField.value = '';
            categoryField.value = '';
            contentField.value = '';
        }
    }
}
