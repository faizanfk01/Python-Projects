# Exanple 1:

import time

running = True

num = int(input("Enter a Time for countdown: "))

if num <= 0:
    print("Enter a number greater than zero")
    

else:
    while running:
        num -= 1
        time.sleep(1)
        print(f"Count down: {num}")

        if num == 0:
            print("count down finished")
            running = False


# Example 2:

is_running = True
total = 0
while is_running:
    num2 = int(input("Enter a number: "))
    total += num2
    if num2 == 0:
        print(f"Total sum: {total} ")
        is_running = False


# Example 3:

password = "faizankhan123"

while True:

    passw = input("Enter you password: ")
    if passw != password:
        print("Wrong password!, try again.")
    else:
        print("You have logined!")
        break


# Example 4:

import random

num1 = 1
num2 = 20
answer = random.randint(num1, num2)

running2 = True

while running2:
    guess = int(input("Enter you guess: "))

    if guess < num1 or guess > num2:
        print(f"Out of range enter between: {num1} and {num2}")
    elif guess < answer:
        print("Too low!")
    elif guess > answer:
        print("Too high!")
    else:
        print(f"Correct, your answer is: {answer}")

    if answer == guess:
        play_again = input("Do you wanna play again? (yes or no): ").lower()
        if play_again != "yes":
            print("Thanks for playing!")
            running2 = False
        else:
            answer = random.randint(num1, num2)


# Example 5:



while True:
    multtable = int(input("Enter a number for Table: "))
    
    for i in range(1, 11):
        print(f"{multtable} X {i} = {multtable * i}")

    choice = input("want to generate another table (yes/no): ").lower()
    if choice != "yes":
        print("Thanks for using")
        break


# Example 6:


running3 = True

balance = 0
yourpin = 5445

while True:

    pin = int(input("Enter your PIN: "))

    if pin != yourpin:
        print("You have entered a wrong password")

    else:
        print("Correct PIN!")

        while running3:
            bank = int(input("check balance = 1, Deposit = 2, withdraw = 3, Exit = 4: "))

            if bank == 1:
                print(f"Your Balance is: {balance}$")

            elif bank == 2:
                deposit = int(input("How much do you want deposit: "))
                balance += deposit
                print(f"You have deposited {deposit}$, Your balance is {balance}$")

            elif bank == 3:
                withdraw = int(input("How much do you want to withdraw: "))
                if withdraw > balance:
                    print("Insufficient balance")
                else:
                    balance -= withdraw
                    print(f"You have withdrawn: {withdraw}$, your balance is: {balance}$")
            elif bank == 4:
                print("Thanks for using")
                running3 = False
            else:
                print("Invalid selection in options")
        break