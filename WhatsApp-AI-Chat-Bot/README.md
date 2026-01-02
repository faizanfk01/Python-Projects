# 🤖 WhatsApp AI Chat Bot

A Python-based **AI WhatsApp bot** that automatically replies to messages in WhatsApp Web using **OpenAI's GPT model**.  
The bot mimics human conversation, replies in the same language and tone, and can respond with emojis, humor, and casual chat style.

------------------------------------------------------------------------

## 🚀 Features

- ✅ Automatically detects and replies to new WhatsApp messages  
- ✅ Mimics human-like conversation: playful, casual, or supportive  
- ✅ Responds in the **same language** as the user  
- ✅ Recognizes media messages (stickers, photos, voice notes, documents) and responds appropriately  
- ✅ Continuous monitoring of WhatsApp Web for new messages  

------------------------------------------------------------------------

## 🛠️ Tech Stack & Requirements

- **Python 3.x**  
- **Selenium** (for WhatsApp Web automation)  
- **PyAutoGUI** (for keyboard/mouse automation)  
- **Pyperclip** (for clipboard operations)  
- **OpenAI SDK** (for AI replies)  
- **Chrome browser** with WhatsApp Web logged in  
- **ChromeDriver** compatible with your Chrome version  

------------------------------------------------------------------------

### 📦 Installing Required Libraries

1. Install the dependencies using pip:

        pip install selenium pyautogui pyperclip openai

2. Ensure you have ChromeDriver installed and added to your system PATH.
        Download from: https://sites.google.com/chromium.org/driver/

3. Log into WhatsApp Web on your Chrome profile for the bot to work.

------------------------------------------------------------------------

## 📂 Project Structure

        WhatsApp-AI-Bot/
        │-- WhatsApp-Ai-ChatBot.py    # Main bot script

------------------------------------------------------------------------

## 🎮 How to Run

1. Clone this repository:

        https://github.com/faizanfk01/WhatsApp-AI-Chat-Bot.git

3. Navigate to the project folder:

        cd WhatsApp-AI-Chat-Bot

4. Install dependencies (if not already installed):

        pip install selenium pyautogui pyperclip openai

5. Set up your OpenAI API Key:

    Replace "your-api-here" in the script with your own OpenAI API key:

        client = OpenAI(api_key="YOUR_OPENAI_KEY_HERE")

6. Create a Chrome user data directory:

- Choose a location on your computer for a separate Chrome profile for the bot.

- Example: C:/WhatsAppBotProfile (create this folder manually).

- Update the script:

        user_data_dir = r"C:/WhatsAppBotProfile"

6. Run the bot:

        python WhatsApp_Ai_ChatBot.py

7. The bot will start monitoring messages:

- Replies automatically in a human-like manner

- Acknowledges media messages like stickers, photos, and voice notes

------------------------------------------------------------------------

## 🔮 Future Enhancements

- 🖥️ Add a GUI dashboard to monitor messages and bot activity

- 📊 Track conversation history and generate analytics

- 🌐 Deploy as a web app for remote monitoring

- 🔔 Add customizable responses and templates for quick replies

------------------------------------------------------------------------

## 🤝 Contributing

Pull requests are welcome! You can contribute by improving AI behavior, adding new features, or making it more robust.

------------------------------------------------------------------------

## 📜 License

This project is licensed under the MIT License — free to use and modify.

------------------------------------------------------------------------

## 🌟 Show Some Love

If you find this bot useful, please ⭐ the repository to support it! 🚀
