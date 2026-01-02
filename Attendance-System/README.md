# 📝 Attendance Management System  

A simple and interactive **Attendance Management System** built in Python.  
This program allows you to mark attendance for a list of students, display a summary, and optionally save the records in a **CSV file** for future reference.  

---

## 🚀 Features  

- 👨‍🎓 **Mark Attendance**: Mark each student as Present (P) or Absent (A).
- 📊 **Summary Report**: Get a quick summary of present and absent students.  
- 💾 **Save to CSV**: Optionally save attendance records with date, name, roll number, and status.  
- 📅 **Date Tracking**: Automatically records today’s date (or lets you enter a custom date).  
- ✅ **Error Handling**: Ensures only valid input (P/A) is accepted.  

------------------------------------------------------------------------

## 💻 Getting Started  

### Prerequisites  

- Python 3.x installed on your system.
- No external libraries are required — this project uses only **built-in modules** (`csv`, `datetime`).  

------------------------------------------------------------------------

## ⚙️ Installation  

1. Clone the repository (or download the file):
   ```bash
   git clone https://github.com/faizanfk01/Attendance-System.git
   cd attendance-system
2. Run the program:
   ```bash
   python Attendance_System.py
   ```
------------------------------------------------------------------------

## 🧑‍💻 How to Use

1. Run the program in your terminal.
2. Enter the date when prompted (or press **Enter** for today’s date).
3. For each student, type:
   * `P` → if Present
   * `A` → if Absent
4. At the end, view a **summary report** of attendance.
5. Choose whether to save the data in a `attendance.csv` file.

------------------------------------------------------------------------

## 📂 File Structure

```
attendance-system/
├── attendance_manager.py  # Main Python program
├── attendance.csv         # Attendance records (created after saving)
```

------------------------------------------------------------------------

## 📊 Example Output

```
Enter date (YYYY-MM-DD) or press Enter for today: 
Faizan : 25108191 (P/A): p
Abdullah : 25108200 (P/A): a
...

✅ Attendance Marked Successfully!

Present Students:
Faizan : 25108191
Hamza : 25108202

Absent Students:
Abdullah : 25108200
Subhan : 25108203

📊 Summary for 2025-09-18: 2 Present, 2 Absent
✅ Attendance saved to attendance.csv
```
------------------------------------------------------------------------

## ⚡ Technologies Used

- Python 3.x
- CSV module (built-in)
- Datetime module (built-in)

------------------------------------------------------------------------

## 💡 Future Improvements

- ⌨️ Add user input for **dynamic student list**.
- 📱 Export attendance in **Excel format (XLSX)**.
- 🖥️ Add a **GUI version** using Tkinter or PyQt.
- 🌐 Connect with an online **database** for centralized attendance management.

------------------------------------------------------------------------

## 🌟 Show Some Love
If you found this project helpful, please ⭐ the repository to support! 🚀
