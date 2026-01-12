# Instance variables are specific to each object and defined using self.var inside __init__().
# Class variables are shared across all instances and defined directly inside the class.

class Car:
    # Class variable (shared by all instances)
    wheels = 4

    def __init__(self, brand, color):
        # Instance variables (unique for each object)
        self.brand = brand
        self.color = color

# Creating objects
car1 = Car("Toyota", "Red")
car2 = Car("Honda", "Blue")

# Accessing variables
print(f"Car1 -> Brand: {car1.brand}, Color: {car1.color}, Wheels: {car1.wheels}")
print(f"Car2 -> Brand: {car2.brand}, Color: {car2.color}, Wheels: {car2.wheels}")

# Changing class variable affects all instances
Car.wheels = 6
print(f"After changing class variable:")
print(f"Car1 -> Wheels: {car1.wheels}")
print(f"Car2 -> Wheels: {car2.wheels}")

# Changing instance variable affects only that instance
car1.color = "Black"
print(f"Car1 New Color: {car1.color}")
print(f"Car2 Color remains: {car2.color}")