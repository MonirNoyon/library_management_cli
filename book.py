class Book:
    def __init__(self, title, authors, isbn, year, price, quantity):
        self.title = title
        self.authors = authors
        self.isbn = isbn
        self.year = year
        self.price = price
        self.quantity = quantity

    def to_dict(self):
        return {
            "title": self.title,
            "authors": self.authors,
            "isbn": self.isbn,
            "year": self.year,
            "price": self.price,
            "quantity": self.quantity
        }

    @staticmethod
    def from_dict(data):
        return Book(
            data["title"],
            data["authors"],
            data["isbn"],
            data["year"],
            data["price"],
            data["quantity"]
        )
