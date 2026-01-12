# Example 1:

try:
    num1 = int(input("Enter a number 1: "))
    num2 = int(input("Enter a number 2: "))
    result = num1 / num2
except ZeroDivisionError:
    print("You cant enter zero")
except ValueError:
    print("Invalid input")
else:
    print(f"The result is: {result}")


# Example 2:

colors = ["red", "green", "blue"]

try:
    pickclr = int(input("Enter an index to pick color: "))
    result = colors[pickclr]
except IndexError:
    print("Out of range")
except ValueError:
    print("Invalid input")
else:
    print(f"The Color is: {result}")