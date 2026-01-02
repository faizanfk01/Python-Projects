# 💳 Payment Processing System (OOP)

A scalable and modular payment simulation built using **Object-Oriented Programming (OOP)** principles in Python.

This project demonstrates the **Strategy Pattern** and **Abstraction** using Python's `abc` (Abstract Base Classes) module. It defines a common interface for payments and implements concrete strategies for Credit Card and PayPal transactions, allowing for easy extensibility.

## 🚀 Features

- **🧩 Abstraction:** Uses the `ABC` (Abstract Base Class) module to enforce a strict contract for all payment methods.
- **🔄 Polymorphism:** Treats different payment types (`CreditCard`, `PayPal`) uniformly through a shared interface.
- **🔌 Extensible Design:** New payment methods (e.g., Bitcoin, Apple Pay) can be added without modifying existing code.
- **🛠️ Clean Architecture:** strict separation of concerns between the payment definition and implementation.

## 💻 Getting Started

### Prerequisites

- **Python 3.x** installed on your system.
- No external libraries are required (uses standard `abc` module).

### ⚙️ Installation

1.  **Clone the repository** (or download the file):

    ```bash
    git clone [https://github.com/faizanfk01/Python-Projects.git](https://github.com/faizanfk01/Python-Projects.git)
    cd Python-Projects/Payment-Processing-System
    ```

2.  **Run the program:**
    ```bash
    python main.py
    ```

## 🧑‍💻 How to Use

1.  Run the script in your terminal.
2.  The program automatically initializes a list of different payment processors.
3.  It iterates through the list and processes a test transaction of **$100** using each method.
4.  The output demonstrates how different classes handle the same `pay()` method call differently.

## 📂 File Structure

```text
Payment-Processing-System/
├── main.py              # Main script with Abstract Base Class and implementations
├── README.md            # Project documentation

```

## 📊 Example Output

```text
Paid $100 using credit card.
Paid $100 using PayPal.

```

## ⚡ Technologies Used

- **Python 3.x**
- **Abstract Base Classes (`abc`)**
- **OOP Principles:**
- Inheritance
- Polymorphism
- Interface Segregation

## 💡 Future Improvements

- 🏦 **Bank API Integration:** Connect to real Stripe or PayPal APIs for actual processing.
- 🧾 **Transaction Logging:** Save transaction history to a CSV or JSON file.
- 🔒 **Security:** Add validation for card numbers or email formats.
- 📱 **Add Crypto:** Implement a `CryptoPayment` class to demonstrate scalability.

## 🌟 Show Some Love

If this project helped you understand Python Abstraction and OOP, please **⭐ the repository**! 🚀
