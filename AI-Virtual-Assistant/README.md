# 🤖 AI Virtual Assistant  

An **all-in-one AI-powered desktop assistant** 🖥️  
This assistant can listen to your voice, answer questions with OpenAI, read the news, manage your credentials, handle employee data, open websites, and even control your computer!  

-----------------------------------------------------------------------

## ✨ Features  

### 🎤 Voice Assistant  
- Uses **speech recognition** to listen for commands  
- Wake word detection → Say **"Hey"** to activate the assistant  
- Responds with **speech (text-to-speech)** using Windows voice  

### 🧠 AI Chat (Powered by OpenAI)  
- Answers your questions politely and concisely  
- Can chat with you naturally like a human  

### 📰 News Reader  
- Fetches the latest news using the **NewsAPI**  
- Reads out loud the **title** and **description**  
- Asks if you want to continue or issue another command  

### 🔐 Credentials Manager  
- Save your **emails & passwords** securely in `credentials.txt`  
- Retrieve credentials by saying the website/app name  
- Simple voice-controlled password manager  

### 🧑‍💼 Employee Management System  
- Add new employees (with validation for names & IDs)  
- View employees by name, role, or ID  
- Update employee details  
- Delete employees  
- Stores all employee info in `employees_details.txt` 
- Export all employee info to CSV in `employees_details_sheet.csv`

### 🌐 Website Opener  
- Opens websites directly by voice command  
- Uses a `websites.py` file to store your favorite websites  

### 💻 System Controls  
- Shutdown PC 📴  
- Restart PC 🔄  
- Logout current user 🔑  

------------------------------------------------------------------------

## 🛠️ Requirements  

This project requires **Python 3.x** and the following libraries:  

### ✅ Built-in (no install needed)  
- `os`  
- `time`  
- `json`  
- `webbrowser`  

------------------------------------------------------------------------

### 📦 External Libraries (install via pip)  

        pip install requests openai SpeechRecognition pywin32 pyaudio

# ⚠️ Note:

- pyaudio is required for microphone input.

- On some systems, install it using

        pip install pipwin
        pipwin install pyaudio

------------------------------------------------------------------------

## 📂 Project Structure

        AI-Virtual-Assistant/
        │-- virtual_assistant.py        # Main program
        │-- websites.py                 # Your favorite websites dictionary
        │-- credentials.txt             # Stores saved credentials
        │-- employees_details.txt       # Stores employee info
        |-- employees_details_sheet.csv # Exports to CSV File

------------------------------------------------------------------------

## 🔑 Setup

1. Clone the repository

        https://github.com/faizanfk01/AI-Virtual-Assistant.git

2. Navigate to the project folder:

        cd AI-Virtual-Assistant

3. Install dependencies

        pip install requests openai SpeechRecognition pywin32 pyaudio

4. Set up your API keys

- In virtual_ assistant.py, replace with your keys:

        client = OpenAI(api_key="YOUR_OPENAI_API_KEY")
        api_key = "YOUR_NEWSAPI_KEY"

5. Create websites.py file

- Example:

        websites = {
            "youtube": "https://www.youtube.com",
            "google": "https://www.google.com",
            "github": "https://github.com"
        }

6. Run the assistant

        python virtual_assistant.py

------------------------------------------------------------------------

## 🎮 Usage


- Say "Hey" to wake up the assistant

- Commands you can try:

  - "Open YouTube"

  - "Read news about technology"

  - "Save password for Gmail"

  - "View credentials for GitHub"

  - "Add employee"

  - "View employee with ID 101"

  - "Shutdown computer"

  - Or just ask any question → it will answer using OpenAI

------------------------------------------------------------------------

## 🔮 Future Improvements

- Encrypt credentials for better security

- Add task scheduler (set reminders, alarms, etc.)

- Improve wake word detection with offline models

- GUI dashboard to monitor assistant activity

------------------------------------------------------------------------

## 📜 License

This project is licensed under the MIT License – free to use and modify.

------------------------------------------------------------------------

## 🌟 Show Some Love

If you liked this project, please ⭐ the repository to support development 🚀

