# 🚗 Car Simulation System (OOP)

A text-based vehicle simulation built using **Object-Oriented Programming (OOP)** principles in Python.

This program models a real-world car's behavior using classes and objects. It allows users to interact with a specific vehicle instance (a Toyota Hilux Revo), controlling its engine state, driving capability, and retrieving vehicle attributes through a menu-driven interface.

## 🚀 Features

- **🏎️ OOP Implementation:** Uses a `Car` class to encapsulate attributes (`brand`, `color`, `model`, `year`) and behaviors (`start`, `stop`, `drive`).
- **🔛 State Management:** logically tracks the engine status (`is_running`). You cannot drive if the engine is off, and you cannot start an engine that is already running.
- **🛣️ Drive Simulation:** Simulates driving a specific distance, dependent on the engine state.
- **📄 Object Representation:** Utilizes the `__str__` magic method to provide a human-readable description of the car object.
- **🎮 Interactive Menu:** A continuous loop allowing full control until the user decides to exit.

## 💻 Getting Started

### Prerequisites

- **Python 3.x** installed on your system.
- No external libraries are required — this project utilizes **Standard Python**.

### ⚙️ Installation

1.  **Clone the repository** (or download the files):

    ```bash
    git clone [https://github.com/faizanfk01/Python-Projects.git](https://github.com/faizanfk01/Python-Projects.git)
    cd Python-Projects/Car-Simulation-OOP
    ```

2.  **Run the program:**
    ```bash
    python main.py
    ```

## 🧑‍💻 How to Use

1.  Run the program in your terminal.
2.  You will see a menu with 5 options.
3.  **Start the Car (Option 1):** Turns the engine on.
4.  **Drive (Option 3):** Simulates driving 600km (requires engine to be on).
5.  **Check Details (Option 4):** Displays the car's full specs.
6.  **Stop (Option 2):** Turns the engine off.
7.  **Exit (Option 5):** Quits the simulation.

## 📂 File Structure

```text
Car-Simulation-OOP/
├── main.py            # Main Python script containing the Car class
├── README.md          # Project documentation

```

## 📊 Example Output

```text
1. Start
2. Stop
3. Check Distance
4. Check your car model
5. Exit
Choose 1-5: 4

Your car is a 2022 Toyota Corolla in Blue color.

1. Start
...
Choose 1-5: 3

Start your Toyota Corolla first

1. Start
...
Choose 1-5: 1

Your Toyota Corolla starts. Vroom Vroom!

1. Start
...
Choose 1-5: 3

Your Toyota Corolla is driving 600 km

```

## ⚡ Technologies Used

- **Python 3.x**
- **Object-Oriented Programming (OOP)**
- Classes & Objects
- Constructors (`__init__`)
- Magic Methods (`__str__`)
- Instance Methods

## 💡 Future Improvements

- ⛽ **Fuel System:** Add a fuel attribute that decreases when driving.
- 🏎️ **Custom Input:** Allow the user to input their own car brand/model at the start.
- ⚙️ **Gear Logic:** Add functionality to change gears while driving.
- 🎨 **GUI:** Create a visual dashboard using Tkinter.

## 🌟 Show Some Love

If you found this OOP example helpful, please **⭐ the repository** to support! 🚀
