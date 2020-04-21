axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = 'X-CSRFTOKEN';

const bookData = JSON.parse(document.getElementById('book-data').value)
    .reduce((result, item) => {
        const property = `book-${item.id}`;
        result[property] = item;
        return result;
    }, {});

function getBook(bookId) {
    return bookData[`book-${bookId}`];
}

function getElementById(id) {
    return document.getElementById(id);
}

function rating(bookId, score) {
    axios.post('books/rating', {
        bookId: bookId,
        score: score,
    })
    .then(res => {
        for (let i = 1; i <= 5; i++) {
            const classList = getElementById(`${bookId}-star-${i}`).classList;
            if (i <= score) {
                classList.add('fa-star');
                classList.add('text-warning');
                classList.remove('fa-star-o');
            } else {
                classList.remove('fa-star');
                classList.remove('text-warning');
                classList.add('fa-star-o');
            }
        }
    })
}

function reading(bookId) {
    const book = getBook(bookId);
    book.userbook__is_reading = !book.userbook__is_reading;
    axios.post('books/reading', {
        bookId: bookId,
        isReading: book.userbook__is_reading,
    })
    .then(res => {
        const classList = getElementById(`reading-${bookId}`).classList;
        if (book.userbook__is_reading) {
            classList.add('text-warning');
            classList.remove('text-white');
        } else {
            classList.remove('text-warning');
            classList.add('text-white');
        }
    })
}

function favorite(bookId) {
    const book = getBook(bookId);
    book.userbook__is_favorite = !book.userbook__is_favorite;
    axios.post('books/favorite', {
        bookId: bookId,
        isFavorite: book.userbook__is_favorite,
    })
    .then(res => {
        const classList = getElementById(`favorite-${bookId}`).classList;
        if (book.userbook__is_favorite) {
            classList.add('text-danger');
            classList.remove('text-white');
        } else {
            classList.remove('text-danger');
            classList.add('text-white');
        }
    })
}

function read(bookId, isRead) {
    const book = getBook(bookId);
    book.userbook__is_read = !book.userbook__is_read;
    axios.post('books/read', {
        bookId: bookId,
        isRead: book.userbook__is_read,
    })
    .then(res => {
        const classList = getElementById(`read-${bookId}`).classList;
        if (book.userbook__is_read) {
            classList.add('text-success');
        } else {
            classList.remove('text-success');
        }
    })
}
