class LibraryCollection {
    constructor(capacity) {
        this.capacity = capacity;
        this.books = [];
    }

    get _freeSpace() {
        return this.capacity - this.books.length;
    }

    _bookPayed(bookName) {
        return this._getBookByBookName(bookName).payed;
    }

    _payBook(bookName) {
        const book = this._getBookByBookName(bookName);
        if (book) book.payed = true;
    }

    _removeBook(bookName) {
        const bookIndex = this.books.findIndex(book => book.bookName === bookName);
        this.books.slice(bookIndex, 1);
    }

    _getBookByBookName(bookName) {
        return this.books.filter(book => book.bookName === bookName)[0];
    }

    _getBookByAuthor(authorName) {
        return this.books.filter(book => book.bookAuthor === authorName)[0];
    }

    addBook(bookName, bookAuthor) {
        if (!this._freeSpace) {
            throw new Error('Not enough space in the collection.');
        }

        this.books.push({
            bookName,
            bookAuthor,
            'payed': false
        });

        return `The ${bookName}, with an author ${bookAuthor}, collect.`;
    }

    payBook(bookName) {
        if (!this._getBookByBookName(bookName)) {
            throw new Error(`${bookName} is not in the collection.`);
        }

        if (this._bookPayed(bookName)) {
            throw new Error(`${bookName} has already been paid.`);
        }

        this._payBook(bookName);
        return `${bookName} has been successfully paid.`;
    }

    removeBook(bookName) {
        if (!this._getBookByBookName(bookName)) {
            throw new Error('The book, you\'re looking for, is not found.');
        }

        if (!this._bookPayed(bookName)) {
            throw new Error(`${bookName} need to be paid before removing from the collection.`);
        }

        this._removeBook(bookName);
        return `${bookName} remove from the collection.`;
    }

    getStatistics(bookAuthor) {
        function getPaidString(isPaid) {
            return (isPaid) ? 'Has Paid' : 'Not Paid';
        }

        if (bookAuthor) {
            const book = this._getBookByAuthor(bookAuthor);

            if (!book) {
                throw new Error(`${bookAuthor} is not in the collection.`);
            }

            return `${book.bookName} == ${book.bookAuthor} - ${getPaidString(book.payed)}.`;
        }

        const message = [`The book collection has ${this._freeSpace} empty spots left.`];
        this.books.sort((a, b) => a.bookName.localeCompare(b.bookName)).forEach(function (book) {
            message.push(`${book.bookName} == ${book.bookAuthor} - ${getPaidString(book.payed)}.`);
        });
        return message.join('\n');
    }
}


// const library = new LibraryCollection(2)
// console.log(library.addBook('In Search of Lost Time', 'Marcel Proust'));
// console.log(library.addBook('Don Quixote', 'Miguel de Cervantes'));
// console.log(library.addBook('Ulysses', 'James Joyce'));


// const library = new LibraryCollection(2)
// library.addBook('In Search of Lost Time', 'Marcel Proust');
// console.log(library.payBook('In Search of Lost Time'));
// console.log(library.payBook('Don Quixote'));


// const library = new LibraryCollection(2)
// library.addBook('In Search of Lost Time', 'Marcel Proust');
// library.addBook('Don Quixote', 'Miguel de Cervantes');
// library.payBook('Don Quixote');
// console.log(library.removeBook('Don Quixote'));
// console.log(library.removeBook('In Search of Lost Time'));


// const library = new LibraryCollection(2)
// console.log(library.addBook('Don Quixote', 'Miguel de Cervantes'));
// console.log(library.getStatistics('Miguel de Cervantes'));


// const library = new LibraryCollection(5)
// library.addBook('Don Quixote', 'Miguel de Cervantes');
// library.payBook('Don Quixote');
// library.addBook('In Search of Lost Time', 'Marcel Proust');
// library.addBook('Ulysses', 'James Joyce');
// console.log(library.getStatistics());