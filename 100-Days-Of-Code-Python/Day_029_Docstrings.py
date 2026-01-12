# A docstring (documentation string) is a special type of comment in Python,
# used to describe the purpose and behavior of a function, class, or module.
# It is written as the first statement in a block using triple quotes (''' or """).


# Example 1: Function with a docstring

def greet(name):
    """
    This function takes a name as input
    and returns a greeting message.
    """
    return f"Hello, {name}!"

print(greet("Alice"))  # Output: Hello, Alice!
print(greet.__doc__)


# Example 2: Class with a docstring

class Dog:
    """
    A simple Dog class
    Attributes:
        name (str): The name of the dog
    """

    def __init__(self, name):
        """
        Constructor for Dog class.
        """
        self.name = name

    def bark(self):
        """
        Makes the dog bark.
        """
        return f"{self.name} says woof!"

my_dog = Dog("Buddy")
print(my_dog.bark())          # Output: Buddy says woof!
print(Dog.__doc__)            # Prints the class docstring
print(my_dog.bark.__doc__)    # Prints the method docstring