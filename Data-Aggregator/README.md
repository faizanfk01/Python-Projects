# 📊 Data Aggregator & Analyzer

A streamlined **Number Aggregation Tool** built in pure Python.

This utility allows users to input a dynamic list of numbers and automatically generates a comprehensive statistical summary, including sums, averages, and boundary values. It is designed to handle user input robustly with built-in error checking.

## 🚀 Features

- **🔢 Dynamic Input:** Accepts an unlimited count of numerical inputs from the user.
- **🛡️ Error Handling:** Gracefully catches non-numeric inputs (preventing crashes).
- **📊 Statistical Analysis:** Instantly calculates:
  - Total Count (Length)
  - Summation
  - Average (Mean)
  - Maximum Value
  - Minimum Value
- **🛑 Controlled Exit:** Uses the simple `done` keyword to finalize data entry.

## 💻 Getting Started

### Prerequisites

- **Python 3.x** installed on your system.
- No external libraries are required — this project runs on **pure Python logic**.

### ⚙️ Installation

1.  **Clone the repository** (or download the file):

    ```bash
    git clone [https://github.com/faizanfk01/Python-Projects.git](https://github.com/faizanfk01/Python-Projects.git)
    cd Python-Projects/Data-Aggregator
    ```

2.  **Run the program:**
    ```bash
    python main.py
    ```

## 🧑‍💻 How to Use

1.  Run the script in your terminal.
2.  **Enter numbers** one by one when prompted.
3.  Type **`done`** (case-insensitive) when you are finished entering data.
4.  The program will instantly display a statistical breakdown of your data.

## 📂 File Structure

```text
Data-Aggregator/
├── main.py            # Main Python script
├── README.md          # Project documentation

```

## 📊 Example Output

```text
Enter numbers or type 'done' to stop: 10
Enter numbers or type 'done' to stop: 25
Enter numbers or type 'done' to stop: 5
Enter numbers or type 'done' to stop: hello
Invalid input. Please enter a number or 'done'.

Enter numbers or type 'done' to stop: done
All numbers are entered

The length of the list is: 3
The sum of all numbers is: 40
The average of numbers is: 13.333333333333334
The maximum value in numbers is: 25
The minimum value in numbers is: 5

```

## ⚡ Technologies Used

- **Python 3.x**
- **Input/Output Handling**
- **Math Functions** (`min`, `max`, `sum`)
- **Exception Handling** (`try`, `except`)

## 💡 Future Improvements

- 📈 Add calculation for **Median** and **Mode**.
- 💾 Export the results to a **TXT or CSV file**.
- 📉 Add a feature to visualize data using `matplotlib`.
- 🖥️ Create a simple GUI for data entry.

## 🌟 Show Some Love

If you found this logic useful or interesting, please **⭐ the repository** to support! 🚀
