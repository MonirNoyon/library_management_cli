from library import Library
from book import Book
from menu import display_menu, get_book_details


def main():
    library = Library()

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            book = get_book_details()
            library.add_book(book)
        elif choice == '2':
            books = library.view_books()
            if len(books) == 0:
                print("Not available books")
            else:
                for book in books:
                    print(book)

        elif choice == '3':
            search_term = input("Enter title or ISBN to search: ")
            books = library.search_books(search_term)
            for book in books:
                print(book)
        elif choice == '4':
            author_name = input("Enter author name to search: ")
            books = library.search_books_by_author(author_name)
            for book in books:
                print(book)
        elif choice == '5':
            search_term = input("Enter title or ISBN to remove: ")
            try:
                library.remove_book(search_term)
            except ValueError as e:
                print(e)
        elif choice == '6':
            search_term = input("Enter title or ISBN to lend: ")
            borrower = input("Enter borrower's name: ")
            try:
                library.lend_book(search_term, borrower)
            except ValueError as e:
                print(e)
        elif choice == '7':
            lent_books = library.view_lent_books()
            for lent_book in lent_books:
                print(lent_book)
        elif choice == '8':
            search_term = input("Enter title or ISBN to return: ")
            borrower = input("Enter borrower's name: ")
            try:
                library.return_book(search_term, borrower)
            except ValueError as e:
                print(e)
        elif choice == '0':
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
