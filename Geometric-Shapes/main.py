class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2
    
    def __str__(self):
        return f"Area of circle is: {self.area()}"
    
class Rectangle(Shape):
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def area(self):
        return self.height * self.width
    
    def __str__(self):
        return f"Area of rectangle is: {self.area()}"
    
class Triangle(Shape):
    def __init__(self, height, base):
        self.height = height
        self.base = base

    def area(self):
        return 0.5 * self.base * self.height
    
    def __str__(self):
        return f"Area of Triangle is: {self.area()}"
    
user_input = int(input("Enter a number: "))

shapes = [Circle(25), Rectangle(5, 8), Triangle(8, 12)]

for shape in shapes:
    print(shape)