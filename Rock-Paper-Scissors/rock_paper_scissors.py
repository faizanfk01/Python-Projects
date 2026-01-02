import random

def rock_paper_scissors():
    choices = ["rock", "paper", "scissors"]
    while True:
        computer_choice = random.choice(choices)
        player_choice = input("Enter rock, paper, or scissors: ").lower()
        if player_choice not in choices:
            print("Invalid choice. Please try again.")
            continue
        else:
            print(f"Computer Choose: {computer_choice}")
            print(f"Player Choose: {player_choice}")
            if computer_choice == player_choice:
                print("It's a tie")
            
            elif (player_choice == "rock" and computer_choice == "paper") or (player_choice == "paper" and computer_choice == "scissors") or (player_choice == "scissors" and computer_choice == "rock"):
                print("You Lose!")
            
            else:
                print("You Win")

        play_again = input("Do you want to play again?(Yes/No): ").lower()
        if play_again != "yes":
            print("Thank You so much for playing!")
            break

rock_paper_scissors()