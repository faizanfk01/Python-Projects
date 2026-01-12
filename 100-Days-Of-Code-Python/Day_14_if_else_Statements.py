# Example 1:

age = int(input("Enter your age: "))

if age < 0:
    print("You are not born yet")
elif age  <= 2:
    print("You are a Baby")
elif age <= 12:
    print("You are a Child")
elif age <= 19:
    print("You are a Teenager")
elif age <= 64:
    print("You are Adult")
else:
    print("You are a senior")

# # Example 2:

num = int(input("Enter the Number: "))

if num == 0:
    print("The number is zero")
elif num > 0:
    print("The number is positive")
else:
    print("The number is negative")

if num % 2 == 0:
    print("The number is Even")
else:
    print("The number is odd")

# Example 3:

score = int(input("Enter Your Score: "))

if score > 100:
    print("Invalid score, please enter a score between 0 and 100.")
elif score >= 90:
    print("You have got Grade A")
elif score >= 80:
    print("You have got Grade B")
elif score >= 70:
    print("You have got Grade C")
elif score >= 60:
    print("You have got Grade D")
else:
    print("You have got Grade F")

# Example 3:

import random

running = True

while running:

    playerchoice = None
    computer_choice = random.choice(['rock', 'paper', 'scissors'])

    
    while playerchoice not in ['rock', 'paper', 'scissors']:
        playerchoice = input("Enter Your Choice (Rock, Paper, Scissors): ").lower()
        if playerchoice not in ['rock', 'paper', 'scissors']:
            print("Invalid input! Please enter rock, paper, or scissors.")

    print(f"Player: {playerchoice}")
    print(f"Computer: {computer_choice}")

    if computer_choice == playerchoice:
        print("it's a draw!")
    elif computer_choice == "rock" and playerchoice == "scissors":
        print("computer wins!")
    elif computer_choice == "scissors" and playerchoice == "paper":
        print("computer wins!")
    elif computer_choice == "paper" and playerchoice == "rock":
        print("computer wins!")
    else:
        print("You win!")

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        running = False

# Example 4:

num1 = 1
num2 = 100

while True:
    answer = random.randint(num1, num2)
    print(f"Guess the number between {num1} and {num2}")

    while True:
        guess = int(input("Enter your guess: "))

        if guess < num1 or guess > num2:
            print(f"Please enter a number between {num1} and {num2}.")
        elif guess < answer:
            print("Too low!")
        elif guess > answer:
            print("Too High!")
        else:
            print(f"Correct! The answer was {answer}.")
            break

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        break

# Example 5:

running = True
balance = random.randint(1000, 5000)

print("*** Welcome to Bank of FK ***")
while running:
    

    atm = int(input("Press for, Balance = 1, Deposit = 2, Withdraw = 3, Exit = 4: "))

    if atm == 1:
        print(f"Your Balance is: {balance}$")


    elif atm == 2:
        deposit = int(input("How much to deposit: "))
        balance += deposit
        print(f"You have deposited {deposit}$, your balance is {balance}$")


    elif atm == 3:
        withdraw = int(input("How much do you want to withdraw: "))
        if withdraw > balance:
            print("Insufficient funds!")
        else:
            balance -= withdraw 
            print(f"You have withdrawn {withdraw}$, Your Balance is {balance}$")

    elif atm == 4:
        print("Thanks for using!")
        running = False
    

    else:
        print("Invalid option! Please choose 1, 2, 3 or 4.")