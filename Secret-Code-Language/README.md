# 🕵️ Secret Code Generator

A fun and interactive Python script that encrypts and decrypts messages using a custom **cipher algorithm**.

This tool transforms standard text into a scrambled format using random characters and position shifting, making the message unreadable to anyone who doesn't have the decoder logic. It demonstrates string manipulation, list processing, and randomization in Python.

## 🚀 Features

- **🔐 Custom Encryption Logic:**
  - **Short Words (< 3 chars):** Simply reversed (e.g., "no" → "on").
  - **Long Words (≥ 3 chars):** The first letter is moved to the end, and 3 random "garbage" characters are attached to both the start and end (e.g., "code" → `x7@` + `odec` + `!9a`).
- **🔓 Reliable Decryption:** accurately strips away the random characters and reverses the shifting logic to restore the original message.
- **🎲 Random Salt:** Uses a mix of letters, numbers, and symbols to create unique encrypted strings every time.
- **🛡️ Input Handling:** Processes entire sentences, handling each word individually.

## 💻 Getting Started

### Prerequisites

- **Python 3.x** installed on your system.
- No external libraries required (uses standard `random` module).

### ⚙️ Installation

1.  **Clone the repository** (or download the file):

    ```bash
    git clone [https://github.com/faizanfk01/Python-Projects.git](https://github.com/faizanfk01/Python-Projects.git)
    cd Python-Projects/Secret-Code-Generator
    ```

2.  **Run the program:**
    ```bash
    python main.py
    ```

## 🧑‍💻 How to Use

1.  Run the script in your terminal.
2.  **Choose a Mode:**
    - Type **`code`** to encrypt a message.
    - Type **`decode`** to decrypt a message.
3.  **Enter your Text:** Type the word or sentence you want to process.
4.  **Copy the Output:** The result will be displayed instantly.

## 📂 File Structure

```text
Secret-Code-Generator/
├── main.py           # Main encryption/decryption script
├── README.md         # Project documentation

```

## 📊 Example Output

### Encoding a Message

```text
Do you want to code or decode?: code
Enter a sentence or word to code: hello python

Coded: a1@elloh99! x#2ythonp00)

```

_(Note: The random characters at the start/end will change every time you run it!)_

### Decoding a Message

```text
Do you want to code or decode?: decode
Enter the coded sentence or word to decode: a1@elloh99! x#2ythonp00)

Decoded: hello python

```

## ⚡ Technologies Used

- **Python 3.x**
- **String Manipulation:** Slicing (`[1:]`, `[:-1]`) and Reversing (`[::-1]`).
- **Random Module:** To generate the 3-character prefix and suffix.
- **Control Flow:** `if-else` logic to handle word lengths.

## 💡 Future Improvements

- 🗝️ **Custom Keys:** Allow the user to define their own specific "random" characters for personal security.
- 📄 **File Processing:** Read a `.txt` file and encrypt the whole document.
- 🖥️ **GUI:** Create a windowed app to paste text easily.

## 🌟 Show Some Love

If you enjoyed this encryption tool, please **⭐ the repository** to support! 🚀
