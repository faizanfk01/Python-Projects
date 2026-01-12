# ================================
# 🔷 OBJECT ORIENTED PROGRAMMING (OOP)
# ================================
# 👉 OOP is a programming paradigm that uses "objects" to structure code logically.
# 👉 It helps model real-world entities using classes and objects.

# ================================
# 🔑 4 PILLARS OF OOP
# ================================
# 1️⃣ Encapsulation – Bundling data & methods inside a class.
# 2️⃣ Abstraction – Hiding complex implementation, exposing only essentials.
# 3️⃣ Inheritance – A class can inherit attributes and methods from another.
# 4️⃣ Polymorphism – Methods behave differently based on the calling object.

# ================================
# 🧬 INHERITANCE (2-line definition)
# ================================
# 👉 Inheritance lets a class reuse code from a parent class.
# 👉 It promotes reusability and logical class hierarchy.


# Class And Objects:

class Person:
    def __init__(self, name, age):  # Constructor
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I'm {self.age} years old.")

# Creating an object
p1 = Person("Alice", 30)
p1.greet()


# __init__ Constructor

class Car:
    def __init__(self, model):
        self.model = model

c = Car("Tesla")
print(c.model)


# Attributes (Instance and Class)

class Dog:
    species = "Canis familiaris"  # Class attribute

    def __init__(self, name):
        self.name = name  # Instance attribute

d = Dog("Rex")
print(d.name, d.species)


# Encapsulation (Private Members)

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private variable

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        self.__balance += amount

acc = BankAccount(1000)
acc.deposit(500)
print(acc.get_balance())


# Inheritance

class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

d = Dog()
d.speak()


# Polymorphism

class Cat:
    def sound(self):
        print("Meow")

class Dog:
    def sound(self):
        print("Bark")

def make_sound(animal):
    animal.sound()

make_sound(Cat())
make_sound(Dog())


# Abstraction (Using ABC)

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

s = Square(4)
print(s.area())


# Method Overriding

class A:
    def show(self):
        print("A class")

class B(A):
    def show(self):
        print("B class")

obj = B()
obj.show()


# Class Methods and Static Methods

class MyClass:
    count = 0

    def __init__(self):
        MyClass.count += 1

    @classmethod
    def get_count(cls):
        return cls.count

    @staticmethod
    def greet():
        print("Hello from static method")

obj1 = MyClass()
obj2 = MyClass()
print(MyClass.get_count())
MyClass.greet()


# Dunder/Magic Methods

class Book:
    def __init__(self, title):
        self.title = title

    def __str__(self):
        return f"Book: {self.title}"

b = Book("1984")
print(b)


# Composition vs Inheritance

class Engine:
    def start(self):
        print("Engine starting...")

class Car:
    def __init__(self):
        self.engine = Engine()  # Composition

    def start(self):
        self.engine.start()

c = Car()
c.start()