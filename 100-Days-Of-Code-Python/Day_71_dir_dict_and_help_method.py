# dir(): Returns a list of valid attributes and methods of an object.
# It helps you inspect the structure of objects (like variables, functions, classes).

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def drive(self):
        print(f"{self.brand} {self.model} is driving.")

my_car = Car("Toyota", "Corolla")
print("Using dir():")
print(dir(my_car))  # Lists all available attributes and methods

# __dict__: Returns the instance namespace as a dictionary containing all instance variables.
# It is used to introspect or access object state.

print("\nUsing __dict__:")
print(my_car.__dict__)  # {'brand': 'Toyota', 'model': 'Corolla'}

# help(): Displays the documentation of objects, classes, functions, or modules.
# It is used to explore built-in help or docstrings.

print("\nUsing help():")
help(Car)  # Displays info about the Car class