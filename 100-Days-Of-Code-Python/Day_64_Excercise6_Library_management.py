class Library:
    def __init__(self, no_of_books, books):
        self.no_of_books = no_of_books
        self.books = books

    def print_books(self):
        print("Books in the Library: ")
        for book in self.books:
            print(f"{book}")

    def add_book(self, book_name):
        self.books.append(book_name)
        self.no_of_books += 1
        print(f"Book '{book_name}' added successfully!")

    def get_no_of_books(self):
        return self.no_of_books
    

my_library = Library(5, [
    "Rich Dad & Poor Dad",
    "Think & Grow Rich",
    "Money Management",
    "Business Mind",
    "Python"
])

my_library.print_books()
my_library.add_book("Atomic Habits")

print(f"Total books now: {my_library.get_no_of_books()}")