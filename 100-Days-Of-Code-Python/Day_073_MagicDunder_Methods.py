# Magic methods (also called dunder methods) are special methods in Python with double underscores.
# They allow classes to implement and customize built-in behavior like printing, adding, or length checking.

class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __str__(self):
        # Called when print() or str() is used
        return f"Book: {self.title}, Pages: {self.pages}"

    def __len__(self):
        # Called when len() is used
        return self.pages

    def __add__(self, other):
        # Called when + is used between two Book objects
        return self.pages + other.pages

# Creating Book objects
book1 = Book("Atomic Habits", 250)
book2 = Book("Deep Work", 300)

# __str__ example
print(book1)  # Book: Atomic Habits, Pages: 250

# __len__ example
print(len(book2))  # 300

# __add__ example
total_pages = book1 + book2
print("Total Pages:", total_pages)  # 550