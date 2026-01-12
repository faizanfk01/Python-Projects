# Operators
"""
Addition = +
Subtraction = -
Multiplication = *
Exponential = **
Divide = /
Floor Division = //
Modulus = %

"""

while True:

    num1 = float(input("Enter Number 1: "))
    num2 = float(input("Enter Number 2: "))

    operator = input("Enter (+, -, *, **, /, //, %): ")

    if operator in ["/", "//", "%"] and num2 == 0:
        print("Error: Cannot divide by zero.")
    elif operator == "+":
        print(f"The answer is: {num1 + num2}")
    elif operator == "-":
        print(f"The answer is: {num1 - num2}")
    elif operator == "*":
        print(f"The answer is: {num1 * num2}")
    elif operator == "**":
        print(f"The answer is: {num1 ** num2}")
    elif operator == "/":
        print(f"The answer is: {num1 / num2:.2f}")
    elif operator == "//":
        print(f"The answer is: {num1 // num2:.2f}")
    elif operator == "%":
        print(f"The answer is: {num1 % num2:.2f}")
    else:
        print(f"Invalid operator '{operator}'. Please choose from +, -, *, /, //, %, **.")

    cont = input("Do you want to calculate again? (yes/no): ").lower()
    if cont != "yes":
        break