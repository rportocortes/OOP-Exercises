class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def __str__(self):
        return f"{self.title} - {self.author}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def borrow(self, title):
        for book in self.books:
            if book.title == title:
                book.available = False

    def return_book(self, title):
        for book in self.books:
            if book.title == title:
                book.available = True

    def list_available(self):
        for book in self.books:
            if book.available == True:
                print(book)


b1 = Book("Harry Potter", "J.K. Rowling")
b2 = Book("The Hobbit", "J.R.R. Tolkien")
b3 = Book("1984", "George Orwell")

lib = Library()
lib.add_book(b1)
lib.add_book(b2)
lib.add_book(b3)

lib.borrow("Harry Potter")
lib.list_available()