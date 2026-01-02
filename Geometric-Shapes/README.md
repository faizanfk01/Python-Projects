# 📐 Geometric Shapes Calculator (OOP)

A Python program demonstrating **Object-Oriented Programming (OOP)** concepts, specifically **Inheritance** and **Polymorphism**.

This script defines a base class `Shape` and derived classes for specific geometric figures (`Circle`, `Rectangle`, `Triangle`). It calculates the area of each shape using overridden methods and demonstrates polymorphic behavior by iterating through a mixed list of shapes.

## 🚀 Features

- **🧩 Inheritance Structure:** Uses a parent class `Shape` that serves as a template for child classes.
- **🔄 Polymorphism:** Each specific shape overrides the `area()` method to implement its own calculation logic.
- **📝 String Representation:** customized `__str__` methods to provide human-readable output when printing objects.
- **📐 Supported Shapes:**
  - **Circle:** Calculates area using radius ($A = \pi r^2$).
  - **Rectangle:** Calculates area using width and height ($A = w \times h$).
  - **Triangle:** Calculates area using base and height ($A = 0.5 \times b \times h$).

## 💻 Getting Started

### Prerequisites

- **Python 3.x** installed on your system.
- No external libraries required.

### ⚙️ Installation

1.  **Clone the repository**:

    ```bash
    git clone [https://github.com/faizanfk01/Python-Projects.git](https://github.com/faizanfk01/Python-Projects.git)
    cd Python-Projects/Geometric-Shapes
    ```

2.  **Run the program:**
    ```bash
    python class_shape.py
    ```

## 🧑‍💻 How to Use

1.  Run the script in your terminal.
2.  The program may prompt for a dummy input (e.g., "Enter a number") to start execution.
3.  It will then automatically process a pre-defined list of shapes (`Circle`, `Rectangle`, `Triangle`) and print their calculated areas.

## 📂 File Structure

```text
Geometric-Shapes/
├── main.py     # Main script with Shape classes
├── README.md          # Documentation

```

## 📊 Example Output

```text
Enter a number: 10

Area of circle is: 1962.5
Area of rectangle is: 40
Area of Triangle is: 48.0

```

## ⚡ Technologies Used

- **Python 3.x**
- **OOP Concepts:**
- Abstract Base Logic (Simulated)
- Method Overriding
- Class Inheritance

## 💡 Future Improvements

- 🏗️ **Input Validation:** Allow users to input dimensions for each shape dynamically.
- ➕ **More Shapes:** Add support for Square, Trapezoid, or Polygon.
- 📏 **Perimeter Calculation:** Add a `perimeter()` method to the base class.

## 🌟 Show Some Love

If this code helped you understand Python OOP better, please **⭐ the repository**! 🚀
