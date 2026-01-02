# 🎓 Student Record Manager

A lightweight **Database Simulation** built using Python dictionaries.

This script acts as a digital ledger for student information. It allows users to quickly retrieve specific student details using a unique identifier (Roll Number) or generate a complete roster of all enrolled students. It demonstrates efficient data retrieval using **Hash Maps (Dictionaries)**.

## 🚀 Features

- **⚡ Instant Search:** Uses dictionary key lookup (`O(1)` time complexity) to find student records instantly by Roll Number.
- **📋 Complete Roster View:** A dedicated option (Press 7) to iterate through and display every student in the database.
- **📂 Structured Data:** Stores multiple attributes (Name, Age, Grade) for each student using lists mapped to keys.
- **🛡️ Input Validation:** Handles cases where a requested Roll Number does not exist in the system.

## 💻 Getting Started

### Prerequisites

- **Python 3.x** installed on your system.
- No external libraries are required.

### ⚙️ Installation

1.  **Clone the repository** (or download the file):

    ```bash
    git clone [https://github.com/faizanfk01/Python-Projects.git](https://github.com/faizanfk01/Python-Projects.git)
    cd Python-Projects/Student-Record-Manager
    ```

2.  **Run the program:**
    ```bash
    python main.py
    ```

## 🧑‍💻 How to Use

1.  Run the script in your terminal.
2.  **To Search:** Enter a specific Roll Number (e.g., `1`, `4`, `6`).
3.  **To View All:** Enter the number **`7`**.
4.  The system will print the requested details nicely formatted.

## 📂 File Structure

```text
Student-Record-Manager/
├── main.py               # Main script with dictionary database
├── README.md             # Project documentation

```

## 📊 Example Output

```text
Enter the student roll no (or press 7 to show all students): 1

Roll No: 1
Name : Faizan
Age : 20
Grade : A

```

```text
Enter the student roll no (or press 7 to show all students): 7

Roll No. 1
Name : Faizan
...
Roll No. 2
Name : Abbas
...

```

## ⚡ Technologies Used

- **Python 3.x**
- **Data Structures:**
- **Dictionaries (`dict`):** For the primary database.
- **Lists (`list`):** For storing individual student attributes.

- **Control Flow:** `if-elif-else` for menu logic.

## 💡 Future Improvements

- ➕ **Add Students:** Allow the user to input new students and save them to the dictionary.
- 💾 **Save to File:** Export the data to a `students.json` or `students.csv` file so records aren't lost when the program closes.
- 🗑️ **Delete Records:** Add functionality to remove a student by Roll Number.
- 🔍 **Search by Name:** Allow searching by "Faizan" instead of just ID.

## 🌟 Show Some Love

If this project helped you understand Python Dictionaries better, please **⭐ the repository**! 🚀
