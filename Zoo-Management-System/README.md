# 🦁 Zoo Management System (Advanced OOP)

A comprehensive Python simulation demonstrating advanced **Object-Oriented Programming (OOP)** concepts, including **Abstraction**, **Encapsulation**, and **Polymorphism**.

This project models a zoo environment where different animal species share common traits but exhibit unique behaviors. It also includes a `ZooKeeper` class that demonstrates secure data handling using access modifiers (public, protected, and private attributes).

## 🚀 Features

- **🧩 Abstraction:** Uses the `ABC` (Abstract Base Class) module to define a strict template for all animals, ensuring they all implement `make_sound` and `eat` methods.
- **🔒 Encapsulation:** Demonstrates data security in the `ZooKeeper` class:
  - **Protected Members (`_employee_id`):** Internal use suggestion.
  - **Private Members (`__salary`):** Strictly inaccessible from outside directly.
  - **Getters & Setters:** Uses `@property` decorators to safely modify private data with validation logic.
- **🔄 Polymorphism:** Iterates through a mixed list of animals (`Lion`, `Monkey`), calling the same methods but triggering different behaviors.
- **🌍 Class Attributes:** Utilizes shared variables (`zoo_name`) common to all instances.

## 💻 Getting Started

### Prerequisites

- **Python 3.x** installed on your system.
- No external libraries required (uses standard `abc` and `random` modules).

### ⚙️ Installation

1.  **Clone the repository** (or download the file):

    ```bash
    git clone [https://github.com/faizanfk01/Python-Projects.git](https://github.com/faizanfk01/Python-Projects.git)
    cd Python-Projects/Zoo-Management-System
    ```

2.  **Run the program:**
    ```bash
    python main.py
    ```

## 🧑‍💻 How to Use

1.  Run the script in your terminal.
2.  The program will automatically:
    - Initialize the Zoo environment.
    - Create a Zookeeper and demonstrate secure salary updates.
    - Create a list of animals.
    - Iterate through the animals to display their unique sounds and eating habits.

## 📂 File Structure

```text
Zoo-Management-System/
├── main.py            # Main script with Animal and ZooKeeper classes
├── README.md          # Project documentation

```

## 📊 Example Output

```text
Welcome to The Python Zoo!

Employee ID of zoo keeper Hamza is: 5823
Salary of Hamza was: 45000
Updated Salary of Hamza is: 55000

Lio says: Roar!
Lio eats a large piece of meat!
Lio lives at The Python Zoo

Momo says: Ooh ooh aah aah!
Momo peels and eats a banana
Momo lives at The Python Zoo

```

## ⚡ Technologies Used

- **Python 3.x**
- **Advanced OOP:**
- Abstract Base Classes (`ABC`, `@abstractmethod`)
- Property Decorators (`@property`, `@setter`)
- Name Mangling (Double underscore `__`)
- Inheritance & `super()`

## 💡 Future Improvements

- 🏥 **Vet Check System:** Add a `Vet` class to check animal health status.
- 🎫 **Ticket System:** Implement a visitor class to track ticket sales and revenue.
- 🏗️ **Enclosures:** Create specific enclosure objects (e.g., "Savannah", "Jungle") to group animals.

## 🌟 Show Some Love

If this code helped you understand Python Encapsulation and Abstraction, please **⭐ the repository**! 🚀
