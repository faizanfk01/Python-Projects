# Getters and setters are methods used to access and modify private attributes in a controlled way.
# In Python, they are implemented using the @property decorator for clean, readable syntax.

class Person:
    def __init__(self, name, age):
        self._name = name        # conventionally private attribute
        self._age = age

    @property
    def name(self):
        """Getter for name"""
        return self._name

    @name.setter
    def name(self, value):
        """Setter for name"""
        if isinstance(value, str) and value.strip():
            self._name = value
        else:
            raise ValueError("Name must be a non-empty string.")

    @property
    def age(self):
        """Getter for age"""
        return self._age

    @age.setter
    def age(self, value):
        """Setter for age"""
        if isinstance(value, int) and value >= 0:
            self._age = value
        else:
            raise ValueError("Age must be a non-negative integer.")

# Testing the class
p = Person("Alice", 30)
print("Name:", p.name)   # uses getter
print("Age:", p.age)     # uses getter

p.name = "Bob"           # uses setter
p.age = 25               # uses setter

print("Updated Name:", p.name)
print("Updated Age:", p.age)

# Uncommenting the following lines would raise ValueError due to invalid data
# p.age = -5
# p.name = ""