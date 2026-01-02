def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def division(a, b):
    return a / b

def calculator():
    operations = ["+", "-", "*", "/"]

    while True:
        operation = input("\nChoose operation (+, -, *, /) or 'X' to exit: ").lower()

        if operation == "x":
            print("\nThanks for using the program. Bye!\n")
            break

        elif operation not in operations:
            print("\nInvalid operation!")
            continue

        else:
            try:
                a = float(input("Enter the first number: "))
                b = float(input("Enter the second number: "))

                if operation == "+":
                    print(f"\nThe answer is: {add(a, b)}")

                elif operation == "-":
                    print(f"\nThe answer is: {subtract(a, b)}")

                elif operation == "*":
                    print(f"\nThe answer is: {multiply(a, b)}")

                elif operation == "/":
                    if b == 0:
                        print("\nYou can't divide by zero!")
                    else:
                        print(f"\nThe answer is: {division(a, b)}")

            except ValueError:
                print("\nPlease enter valid numbers!")

calculator()