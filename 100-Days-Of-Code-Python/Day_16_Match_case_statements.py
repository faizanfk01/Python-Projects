# Example 1:

day = input("Enter your Day: ").lower()

match day:
    case "monday":
        print("Today is Weekday, Monday")
    case "tuesday":
        print("Today is Weekday, Tuesday")
    case "wednesday":
        print("Today is Weekday, Wednesday")
    case "thursday":
        print("Today is Weekday, Thursday")
    case "friday":
        print("Today is Weekday, Friday")
    case "saturday":
        print("It's Weekend, Saturday")
    case "sunday":
        print("It's Weekend, Sunday")
    case _:
        print("Invalid day. Please enter a valid day of the week.")



# Example 2:

game = input("Start, Pause Or Quit: ").lower()

match game:
    case "start":
        print("You started the game")
    case "pause":
        print("You paused the game")
    case "quit":
        print("You quit the game")
    case _:
        print("Invalid Input")


# Excercise 3:

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

operator = input("Enter operator (+, -, *, /): ")

match operator:
    case "+":
        print(f"The Answer is: {num1 + num2}")
    case "-":
        print(f"The Answer is: {num1 - num2}")
    case "*":
        print(f"The Answer is: {num1 * num2}")
    case "/":
        if num2 == 0:
            print("cannot divide by zero")
        else:
            print(f"The Answer is: {num1 / num2}")
    case _:
        print("Invalid Operater or number!")