# 🛠️ Multi-Function Python Utility

A comprehensive, menu-driven Python application that consolidates **9 different functional modules** into a single executable interface.

This project serves as a "Swiss Army Knife" of Python basics, demonstrating how to integrate multiple logic streams (like banking, calculation, and data management) into one cohesive system using functions and a central control loop.

## 🚀 Features & Modules

This program includes the following tools, accessible via a main menu:

1.  **🔢 Secure Integer System:** Robust input handling that ensures only valid integers are processed.
2.  **🎓 Eligibility Checker:** Logic to determine university admission based on age and marks.
3.  **🏧 ATM System:** A banking simulation supporting balance checks, deposits, and withdrawals.
4.  **🔐 Login System:** A security simulation with username/password verification and account locking after 3 failed attempts.
5.  **📊 List Analyzer:** Separates and counts even/odd numbers from a user-generated list.
6.  **🧮 Calculator:** A functional calculator supporting basic arithmetic (+, -, \*, /) and multiple-number addition.
7.  **🛡️ Data Validation:** A nested function demonstration for strict type checking.
8.  **🛒 Shopping Cart:** A billing system that calculates totals, applies discounts for high-value orders (>10k), and generates a bill summary.
9.  **📝 Student Report:** Generates a performance report (Total, Percentage, Grade) based on marks from 5 subjects.

## 💻 Getting Started

### Prerequisites

- **Python 3.x** installed on your system.
- No external libraries required.

### ⚙️ Installation

1.  **Clone the repository**:

    ```bash
    git clone [https://github.com/faizanfk01/Python-Projects.git](https://github.com/faizanfk01/Python-Projects.git)
    cd Python-Projects/Multi-Function-Tool
    ```

2.  **Run the program:**
    ```bash
    python main.py
    ```

## 🧑‍💻 How to Use

1.  Run the program in your terminal.
2.  You will be presented with a **Master Menu** listing all 9 tools.
3.  Enter the number (1-9) corresponding to the tool you want to use.
4.  Follow the prompts for that specific tool.
5.  When finished, you will return to the main menu.
6.  Select **Option 10** to exit the application completely.

## 📂 File Structure

```text
Multi-Function-Tool/
├── main.py                  # Main script containing all 9 modules
├── README.md                # Project documentation

```

## 📊 Example Output

```text
1. Integer System
2. Check Student Eligibility
3. ATM System
4. Login System
5. List Analyzer
6. Calculator
7. Data Validation
8. Shopping cart system
9. Student Report Generator
10. Exit

Choose(1-10): 3

1. Check Balance
2. Deposit Cash
3. Withdraw Cash
4. Exit
Enter your choice: 1
Your balance is Rs. 0

```

## ⚡ Technologies Used

- **Python 3.x**
- **Modular Programming:** Extensive use of functions to segregate logic.
- **Control Flow:** `while` loops, `if-elif-else` conditions.
- **Error Handling:** `try-except` blocks for robust user experience.
- **Data Structures:** Lists for managing shopping items and numbers.

## 💡 Future Improvements

- 💾 **File Persistence:** Save ATM balances or Shopping Cart data to a text file so it remains after closing the program.
- 🖥️ **GUI Interface:** Convert the menu-driven text system into a windowed application using Tkinter.
- 🧩 **Module Separation:** Split the 9 functions into separate `.py` files and import them into `main.py` for cleaner code organization.

## 🌟 Show Some Love

If you found this multi-tool useful for learning Python structure, please **⭐ the repository**! 🚀
