# 🎲 Number Guessing Game

An interactive, logic-based command-line game built in Python.

This program challenges the user to guess a randomly generated number between 1 and 100. It features a limited number of attempts, real-time feedback (Too High/Too Low), and input validation to ensure a smooth gaming experience.

## 🚀 Features

- **🎰 Random Number Generation:** Utilizes Python's `random` module to ensure a unique target number every game.
- **⏳ Difficulty Limit:** The player has a strict limit of **7 attempts** to guess the correct number.
- **📉 Dynamic Feedback:** Provides "Too High" or "Too Low" hints after every incorrect guess.
- **🛡️ Input Validation:** Handles non-numeric inputs and out-of-range numbers gracefully without crashing.
- **🔄 Replayability:** Includes a "Play Again" loop, allowing continuous gameplay without restarting the script.

## 💻 Getting Started

### Prerequisites

- **Python 3.x** installed on your system.
- No external libraries required (uses standard `random` module).

### ⚙️ Installation

1.  **Clone the repository**:

    ```bash
    git clone [https://github.com/faizanfk01/Python-Projects.git](https://github.com/faizanfk01/Python-Projects.git)
    cd Python-Projects/Number-Guessing-Game
    ```

2.  **Run the game:**
    ```bash
    python main.py
    ```

## 🧑‍💻 How to Play

1.  Run the script in your terminal.
2.  The game will select a secret number between **1 and 100**.
3.  Enter your guess when prompted.
4.  Read the hint ("Too High" or "Too Low") and adjust your next guess.
5.  Try to find the number before your **7 tries** run out!

## 📂 File Structure

```text
Number-Guessing-Game/
├── main.py              # Main game script
├── README.md            # Project documentation

```

## 📊 Example Output

```text
Welcome to number Guessing Game!
You will have to guess the number between 1-100.
Let's Begin.

Enter your guess here (7) guesses: 50
Too Low! Guess again.

Enter your guess here (6) guesses: 75
Too High! Guess again.

Enter your guess here (5) guesses: 63

You got it! The number was 63
You guessed the number in 3 guesses

Do you want to play again? (Y/N): n

Thanks for playing the Game!

```

## ⚡ Technologies Used

- **Python 3.x**
- **Random Module:** For generating the secret number.
- **Control Flow:** `while` loops for game rounds and input validation.
- **Exception Handling:** `try-except` blocks to prevent crashes on invalid input.

## 💡 Future Improvements

- 🎚️ **Difficulty Levels:** Add Easy (unlimited tries), Medium (10 tries), and Hard (5 tries) modes.
- 🏆 **High Score System:** Save the fewest number of guesses to a file.
- 🤖 **AI Solver:** Create a mode where the computer tries to guess your number.

## 🌟 Show Some Love

If you enjoyed playing or analyzing this logic, please **⭐ the repository**! 🚀
