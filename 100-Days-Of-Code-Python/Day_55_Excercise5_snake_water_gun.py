import random

options = ["snake", "water", "gun"]

computerscore = 0
playerscore = 0
draw = 0

while True:
    player = input("Enter your Choice: ").lower()
    print()
    if player not in options:
        print("Invalid input!")
        continue

    else:
        computer = random.choice(options)

        print(f"Player Choose: {player.capitalize()}")
        print(f"Computer Choose: {computer.capitalize()}")

        if player == computer:
            print("It's a Draw!")
            draw += 1
        elif computer == "snake" and player == "water":
            print("Computer Wins!")
            computerscore += 1
        elif computer == "water" and player == "gun":
            print("Computer Wins!")
            computerscore += 1
        elif computer == "gun" and player == "snake":
            print("Computer Wins!")
            computerscore += 1
        else:
            print("You Win!")
            playerscore += 1
        print()
        playagain = input("Want to play again(Yes/No)?: ").lower()
        print()
        if playagain != "yes":
            print("Thanks For Playing!")
            break

print()
print("The Scores Are:")
print()
print(f"Computer Score: {computerscore}")
print(f"Player Score: {playerscore}")
print(f"Draws: {draw}")
print()