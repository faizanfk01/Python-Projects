import random

print("\nWelcome to number Guessing Game!\nYou will have to guess the number between 1-100.\nLet's Begin.")

while True:
    secret_number = random.randint(1, 100)
    tries = 7
    guess_count = 0

    while tries > 0:
        try:
            user_guess = int(input(f"\nEnter your guess here ({tries}) guesses: "))

            if user_guess > 100 or user_guess < 1:
                print("Please choose a number between 1-100")
                tries -= 1
                guess_count += 1
                continue

            guess_count += 1
                
            if user_guess > secret_number:
                print("Too High! Guess again.")
                tries -= 1

            elif user_guess < secret_number:
                print("Too Low! Guess again.")
                tries -= 1

            else:
                print(f"\nYou got it! The number was {secret_number}")
                print(f"You guessed the number in {guess_count} guesses")
                break

        except ValueError:
            print("That's not a valid number! Please try again.")
            tries -= 1
            guess_count += 1

    else:
        print(f"Out of guesses! The number was {secret_number}")

    play_again = input("\nDo you want to play again? (Y/N): ").lower()
    if play_again != "y":
        print("\nThanks for playing the Game!\n")
        break