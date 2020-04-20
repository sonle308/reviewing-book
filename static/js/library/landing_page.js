axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = 'X-CSRFTOKEN';

function rating(bookId, score) {
    axios.post('books/rating', {
        bookId: bookId,
        score: score,
    })
    .then(res => {
        console.log(res)
    })
}

function reading(bookId, isReading) {
    axios.post('books/reading', {
        bookId: bookId,
        isReading: isReading,
    })
    .then(res => {
        console.log(res)
    })
}

function favorite(bookId, isFavorite) {
    axios.post('books/favorite', {
        bookId: bookId,
        isFavorite: isFavorite,
    })
    .then(res => {
        console.log(res)
    })
}
