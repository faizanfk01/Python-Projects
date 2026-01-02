# # Exercise 1: Secure Integer Input System

def integer_system():
    while True:
        try:
            num = int(input("Enter a number: "))
            return f"The number is {num}"
        
        except ValueError:
            print("Please enter a valid number")


# # Exercise 2: Student Eligibility Checker

def eligibility(age, marks):
    if age >= 18 and marks >= 50:
        print("You are Eligible")
    else:
        print("You are not eligible for university!")

def check_eligibility():
    while True:
        try:
            age = int(input("Enter your age: "))
            marks = int(input("Enter your marks: "))
            eligibility(age, marks)
            break

        except ValueError:
            print("Please enter a valid number for age and marks")


# Exercise 3: ATM Withdrawal System

def check_balance(balance):
    return balance


def deposit(balance, amount):
    if amount <= 0:
        print("Deposit amount must be greater than zero.")
        return balance

    balance += amount
    print(f"Rs. {amount} deposited successfully.")
    return balance


def withdraw(balance, amount):
    if amount <= 0:
        print("Withdrawal amount must be greater than zero.")
        return balance

    if amount > balance:
        print("Insufficient balance!")
        return balance

    balance -= amount
    print(f"Rs. {amount} withdrawn successfully.")
    return balance


def atm():
    balance = 0

    while True:
        try:
            print("\n1. Check Balance")
            print("2. Deposit Cash")
            print("3. Withdraw Cash")
            print("4. Exit")

            choice = int(input("Enter your choice: "))

            if choice == 1:
                print(f"Your balance is Rs. {check_balance(balance)}")

            elif choice == 2:
                amount = int(input("Enter amount to deposit: "))
                balance = deposit(balance, amount)

            elif choice == 3:
                amount = int(input("Enter amount to withdraw: "))
                balance = withdraw(balance, amount)

            elif choice == 4:
                print("Thanks for using our ATM. Goodbye!")
                break

            else:
                print("Invalid choice! Please try again.")

        except ValueError:
            print("Please enter valid numeric values.")

# Exercise 4: Login System with Limited Attempts

def input_username_pass():

    username = input("Enter your username here: ")
    password = input("Enter your password here: ")

    return username, password

def verify_userpassword(username, password):

    correct_username = "admin123"
    correct_password = "FAIZANkhan123"

    if username == correct_username and password == correct_password:
        return True
    else:
        return False
    

def login_system():
    attempts = 0
    max_attempts = 3

    while attempts < max_attempts:
        username, password = input_username_pass()

        if verify_userpassword(username, password):
            print("Login successful!")
            break
        else:
            attempts += 1
            remaining = max_attempts - attempts
            print(f"Invalid username or password. Attempts left: {remaining}")

    print("System locked due to too many failed attempts.")


# Exercise 5: List Analyzer

def collect_numbers(num, numbers):
    numbers.append(num)

def count_even(numbers):

    even = [i for i in numbers if i % 2 == 0]
    return len(even), even

def count_odd(numbers):
    odd = [i for i in numbers if i % 2 != 0]
    return len(odd), odd

def list_analyzer():
    numbers = []
    while True:
        user_input = input("Enter numbers or press E to exit: ")

        if user_input.lower() == "e":
            break

        try:
            num = int(user_input)
            collect_numbers(num, numbers)

        except ValueError:
            print("Please enter a valid integer.")

    even_count, even_numbers = count_even(numbers)
    odd_count, odd_numbers = count_odd(numbers)

    print("\nAll numbers are added.")
    print(f"Total even numbers: {even_count}")
    print(f"Total odd numbers: {odd_count}")
    print(f"Even numbers: {even_numbers}")
    print(f"Odd numbers: {odd_numbers}\n")

# Exercise 6: Menu-Driven Calculator (Strictly Functions)

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

        if operation not in operations:
            print("\nInvalid operation!")
            continue

        multiple = input("Do you want to calculate multiple numbers? (Y/N): ").lower()

        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))

            if multiple != "y":
                if operation == "+":
                    print(f"\nAnswer: {add(a, b)}")
                elif operation == "-":
                    print(f"\nAnswer: {subtract(a, b)}")
                elif operation == "*":
                    print(f"\nAnswer: {multiply(a, b)}")
                elif operation == "/":
                    if b == 0:
                        print("\nYou can't divide by zero!")
                    else:
                        print(f"\nAnswer: {division(a, b)}")

            else:
                if operation != "+":
                    print("\nMultiple calculation is only supported for addition.")
                    continue

                numbers = [a, b]

                while True:
                    user_input = input("Enter number (or E to finish): ").lower()

                    if user_input == "e":
                        break

                    try:
                        numbers.append(float(user_input))
                    except ValueError:
                        print("Please enter a valid number.")

                print(f"\nAnswer: {sum(numbers)}")

        except ValueError:
            print("\nPlease enter valid numbers!")


# Exercise 7: Nested Function for Data Validation

def data_validation():
    def validate():
        while True:
            num = input("Enter a number: ")
            
            if num.isdigit():
                print(f"Valid integer entered: {num}")
                break
            else:
                print("That's not an integer. Try again.")

    validate()


# Exercise 8: Shopping Cart Billing System

def add_item_price(items, prices, item, price):
    items.append(item)
    prices.append(price)

def calculate_total(prices):
    return sum(prices)

def apply_discount(total):
    if total > 10000:
        discount = 30
        return (discount * total) / 100
    else:
        return 0

def shopping_cart():
    items = []
    prices = []

    while True:
        item = input("Enter your items or press S to stop: ").lower()

        if item == "s":
            break

        try:
            price = int(input("Enter price for each item here: "))
            add_item_price(items, prices, item, price)

        except ValueError:
            print("Please enter a valid price.")
            
    total = calculate_total(prices)
    discount = apply_discount(total)
    final_amount = total - discount

    print("\n--- BILL SUMMARY ---")
    print(f"Items: {items}")
    print(f"Prices: {prices}")
    print(f"Total Amount: {total}")
    print(f"Discount: {discount}")
    print(f"Final Payable Amount: {final_amount}")

# Exercise 9: Student Report Generator

def input_marks(marks, enter_marks):
    marks.append(enter_marks)

def calculate_total_marks(marks):
    return sum(marks)

def calculate_percentage(marks):
    total = calculate_total_marks(marks)
    max_marks = len(marks) * 100
    percentage = (total / max_marks) * 100

    return percentage

def assign_grades(percentage):
    if percentage >= 80:
        return "A"

    elif percentage >= 60:
        return "B"

    elif percentage >= 40:
        return "C"

    else:
        return "F"


def student_report():
    marks = []

    for i in range(1, 6):
        while True:
            try:
                entered_marks = int(input(f"Enter marks of subject {i}: "))
                if 0 <= entered_marks <= 100:
                    input_marks(marks, entered_marks)
                    break
                else:
                    print("Marks must be between 0 and 100.")
            except ValueError:
                print("Please enter a valid integer.")

    total = calculate_total_marks(marks)
    percentage = calculate_percentage(marks)
    grade = assign_grades(percentage)

    print("\n--- STUDENT REPORT ---")
    print(f"Total Marks: {total}")
    print(f"Percentage: {percentage:.2f}%")
    print(f"Grade: {grade}")


def main():
    while True:
        print("\n1. Integer System\n2. Check Student Eligibility\n3. ATM System\n4. Login System\n5. List Analyzer\n6. Calculator\n7. Data Validation\n8. Shopping cart system\n9. Student Report Generator\n10. Exit")
        try:
            choice = int(input("Choose(1-10): "))

            if choice == 1:
                print(integer_system())

            elif choice == 2:
                check_eligibility()

            elif choice == 3:
                atm()

            elif choice == 4:
                login_system()

            elif choice == 5:
                list_analyzer()

            elif choice == 6:
                calculator()

            elif choice == 7:
                data_validation()

            elif choice == 8:
                shopping_cart()
            
            elif choice == 9:
                student_report()

            elif choice == 10:
                print("\nThanks for using the program Bubyeee!")
                break

            else:
                print("\nPlease enter a number between 1-10")

        except ValueError:
            print("Please enter valid numbers!")

main()