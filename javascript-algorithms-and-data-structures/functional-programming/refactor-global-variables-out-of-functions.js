const bookList = ["The Hound of the Baskervilles", "On The Electrodynamics of Moving Bodies", "Philosophiæ Naturalis Principia Mathematica", "Disquisitiones Arithmeticae"];

function add(arr, bookName) {
    let newBookList = [...arr];
    newBookList.push(bookName);
    return newBookList;

}

function remove(arr, bookName) {
    let newBookList = [...arr];
    if (newBookList.indexOf(bookName) >= 0) {

        newBookList.splice(newBookList.indexOf(bookName), 1);
        return newBookList;

    }
}