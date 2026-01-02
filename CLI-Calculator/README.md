# 🧮 CLI Calculator

A robust and interactive **Command-Line Calculator** built using pure Python.

This program serves as a demonstration of **functional programming** and **control flow**. It breaks down arithmetic operations into reusable functions and implements a continuous user loop with strict error handling for seamless calculation.

## 🚀 Features

- **➕ Full Arithmetic Support:** Handles Addition, Subtraction, Multiplication, and Division.
- **🛡️ Smart Error Handling:**
  - Catches non-numeric inputs gracefully.
  - Prevents crashes caused by **Division by Zero**.
- **🔄 Continuous Operation:** The calculator keeps running until you explicitly choose to exit ('X').
- **🧩 Modular Design:** Logic is separated into distinct functions (`add`, `subtract`, etc.) for better code readability.

## 💻 Getting Started

### Prerequisites

- **Python 3.x** installed on your system.
- No external libraries are required.

### ⚙️ Installation

1.  **Clone the repository** (or download the file):

    ```bash
    git clone [https://github.com/faizanfk01/Python-Projects.git](https://github.com/faizanfk01/Python-Projects.git)
    cd Python-Projects/CLI-Calculator
    ```

2.  **Run the program:**
    ```bash
    python main.py
    ```

## 🧑‍💻 How to Use

1.  Run the script in your terminal.
2.  Choose an operation symbol: **`+`**, **`-`**, **`*`**, or **`/`**.
3.  Enter the **two numbers** you wish to calculate.
4.  The result will be displayed instantly.
5.  To quit the program, simply type **`X`** or **`x`** when asked for an operation.

## 📂 File Structure

```text
CLI-Calculator/
├── main.py                # Main script with arithmetic functions
├── README.md              # Project documentation

```

## 📊 Example Output

```text
Choose operation (+, -, *, /) or 'X' to exit: +
Enter the first number: 10
Enter the second number: 50

The answer is: 60.0

Choose operation (+, -, *, /) or 'X' to exit: /
Enter the first number: 10
Enter the second number: 0

You can't divide by zero!

```

## ⚡ Technologies Used

- **Python 3.x**
- **Functions:** To encapsulate logic (`def add()`, etc.).
- **Control Flow:** `while True` for the main loop.
- **Exception Handling:** `try-except` blocks for input validation.

## 💡 Future Improvements

- 🧪 **Scientific Mode:** Add support for power (`^`), square root (`sqrt`), and modulus (`%`).
- 📜 **History Log:** Save the last 5 calculations to view later.
- 🧮 **GUI Version:** Create a visual interface using **Tkinter** or **PyQt**.

## 🌟 Show Some Love

If this project helped you practice Python functions, please **⭐ the repository**! 🚀
