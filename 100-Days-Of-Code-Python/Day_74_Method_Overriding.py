# Method overriding allows a subclass to provide a specific implementation of a method already defined in its parent class.
# This is used to modify or extend the parent class behavior in the child class.

class Animal:
    def speak(self):
        print("The animal makes a sound.")

class Dog(Animal):
    def speak(self):
        print("The dog barks.")

# Creating objects
generic_animal = Animal()
dog = Dog()

# Method Overriding in action
generic_animal.speak()  # Output: The animal makes a sound.
dog.speak()             # Output: The dog barks. (Overrides Animal's speak method)