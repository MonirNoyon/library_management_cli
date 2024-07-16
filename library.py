import json
from book import Book
from utils import save_data, load_data, load_raw_data


class Library:
    def __init__(self):
        self.books = [Book.from_dict(data) for data in load_raw_data('/data/books.json')]
        print(f"current Book List {self.books}")
        self.lent_books = load_data('/data/lent_books.json')

    def add_book(self, book):
        self.books.append(book)
        self.save_books()

    def view_books(self):
        return [book.to_dict() for book in self.books]

    def search_books(self, search_term):
        result = [book.to_dict() for book in self.books if
                  search_term.lower() in book.title.lower() or search_term in book.isbn]
        if len(result) == 0:
            print("Don't have found any Items")
            return result
        else:
            return result

    def search_books_by_author(self, author_name):
        result = [book.to_dict() for book in self.books if
                  author_name.lower() in [author.lower() for author in book.authors]]
        return result

    def remove_book(self, search_term):
        book_to_remove = None
        for book in self.books:
            if search_term.lower() in book.title.lower() or search_term in book.isbn:
                book_to_remove = book
                break
        if book_to_remove:
            self.books.remove(book_to_remove)
            self.save_books()
            print("Successfully Remove book")
        else:
            raise ValueError("This book isn’t available to remove.")

    def lend_book(self, search_term, borrower):
        book_to_lend = None
        for book in self.books:
            if search_term.lower() in book.title.lower() or search_term in book.isbn:
                book_to_lend = book
                break
        if book_to_lend and book_to_lend.quantity > 0:
            book_to_lend.quantity -= 1
            self.lent_books.append({"book": book.to_dict(), "borrower": borrower})
            self.save_books()
            self.save_lent_books()
        else:
            raise ValueError("Not enough books available to lend.")

    def return_book(self, search_term, borrower):
        lent_book_to_return = None
        for lent_book in self.lent_books:
            if search_term.lower() in lent_book["book"]["title"].lower() or search_term in lent_book["book"]["isbn"]:
                if lent_book["borrower"] == borrower:
                    lent_book_to_return = lent_book
                    break
        if lent_book_to_return:
            for book in self.books:
                if book.isbn == lent_book_to_return["book"]["isbn"]:
                    book.quantity += 1
                    self.lent_books.remove(lent_book_to_return)
                    self.save_books()
                    self.save_lent_books()
                    break
        else:
            raise ValueError("This book wasn’t lent out to this borrower.")

    def view_lent_books(self):
        return self.lent_books

    def save_books(self):
        save_data('data/books.json', [book.to_dict() for book in self.books])

    def save_lent_books(self):
        save_data('data/lent_books.json', self.lent_books)
