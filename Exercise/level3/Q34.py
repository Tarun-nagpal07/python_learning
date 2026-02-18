'''Build a small library system with Book, Member, and Library classes. Library supports
add_book(), borrow_book(member), return_book(member), and list_available().
Demonstrate all operations.'''

class Book:
    def __init__(self, title, quantity):
        self.title = title
        self.quantity = quantity

    def __str__(self):
        return f"{self.title} (Available: {self.quantity})"


class Member:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class Library:
    def __init__(self):
        self.books = {}          
        self.borrowed = {}       

    def add_book(self, title, quantity):
        if title in self.books:
            print("Book already exists!")
        else:
            self.books[title] = Book(title, quantity)
            print(f"{title} added successfully!")

    def list_available(self):
        print("\nAvailable Books:")
        for book in self.books.values():
            if book.quantity > 0:
                print(book)

    def borrow_book(self, member, title):
        if title in self.books and self.books[title].quantity > 0:
            self.books[title].quantity -= 1

            self.borrowed.setdefault(member.name, []).append(title)
            print("Borrowed!")
        else:
            print("Book not available!")

    def return_book(self, member, title):
        if member.name in self.borrowed and title in self.borrowed[member.name]:
            self.books[title].quantity += 1
            self.borrowed[member.name].remove(title)
            print("Returned!")
        else:
            print("This member did not borrow this book.")


lib = Library()

lib.add_book("Python 101", 3)
lib.add_book("Data Science", 2)

arya = Member("arya")
bob = Member("Bob")

lib.borrow_book(arya, "Python 101")
lib.borrow_book(bob, "Data Science")

lib.list_available()

lib.return_book(arya, "Python 101")

lib.list_available()
