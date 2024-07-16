from book import Book


def get_user_input(title, options="String"):
    while True:
        get_input = input(title)

        if options == "Integer" and get_input.isdigit():
            return int(get_input)
        elif options == "Float":
            try:
                get_input = int(get_input)
                return get_input
            except ValueError:
                pass
            try:
                get_input = float(get_input)
                return get_input
            except ValueError:
                pass

        elif options == "String" and not get_input.isdigit():
            return get_input
        else:
            print(f"Please Enter {options} input")


def display_menu():
    print("Library Management System")
    print("-------------------------")
    print("1. Add a book")
    print("2. View all books")
    print("3. Search books by title or ISBN")
    print("4. Search books by author")
    print("5. Remove a book")
    print("6. Lend a book")
    print("7. View lent books")
    print("8. Return a book")
    print("0. Exit")


def get_book_details():
    title = get_user_input("Enter book title: ")
    authors = get_user_input("Enter authors (comma-separated): ").split(',')
    isbn = get_user_input("Enter ISBN: ")
    year = get_user_input("Enter publishing year: ", options="Integer")
    price = get_user_input("Enter price: ", options="Float")
    quantity = get_user_input("Enter quantity: ", options="Integer")
    return Book(title, authors, isbn, year, price, quantity)
