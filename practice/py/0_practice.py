'''
Write a Library class with no_of_books and books as two instance variables. Write a program to create a library from this Library class and
 show how you can print all books, add a book and get the number of books using different methods. Show that your program doesnt persist the 
 books after the program is stopped!
'''


class library:
    def __init__(self):
        self.noofbook = 0
        self.books = []
    def addBook(self,book):
        if book is None:
            print("Give the name of book")
            return
        self.books.append(book)
        self.noofbook += 1
    def listallbooks(self):
        for book in self.books:
            print(book)
    def howmanybook(self):
        return self.noofbook
    
b = library()

b.addBook("GOT")
b.addBook("Spiderman")
b.addBook("Spiderman")
b.addBook("Spiderman")
b.addBook("Spiderman")

print(b.howmanybook())
b.listallbooks()