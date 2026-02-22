# 🌤️ Weather App (with Smart Advice)

A sleek, dark-themed desktop weather application built using Python and **PyQt5**. 

This app fetches real-time meteorological data from the OpenWeatherMap API and displays it in a clean, user-friendly interface. Uniquely, it includes a **"Smart Advice"** feature that generates practical, day-to-day recommendations (like checking tire pressure or securing outdoor items) based on the current temperature and weather conditions.

## 🚀 Features

* **🌍 Real-Time Data:** Displays accurate temperature, feels-like temperature, humidity, wind speed, and atmospheric pressure.
* **🎨 Modern UI:** Built with PyQt5 featuring a custom stylesheet (QSS) for a polished, dark-mode aesthetic.
* **💡 Smart Advice Engine:** Analyzes the weather data to provide practical lifestyle and maintenance tips.
* **🛡️ Robust Error Handling:** Gracefully catches and displays HTTP errors, connection timeouts, and invalid city names.

## 📋 Prerequisites & Requirements

To run this application, you need Python 3.x installed along with the following libraries:

```bash
pip install PyQt5 requests

```

### 🔑 API Key Required

This application requires a free API key from **OpenWeatherMap** to fetch real-time data.

1. Go to [openweathermap.org](https://openweathermap.org/) and create a free account.
2. Navigate to your profile and generate a new API Key.
3. Open `main.py` and replace the placeholder on line 156 with your actual key:
```python
api_key = "YOUR_API_KEY_HERE"

```



## 💻 How to Run

1. **Clone the repository:**
```bash
git clone [https://github.com/faizanfk01/Python-Projects.git](https://github.com/faizanfk01/Python-Projects.git)
cd Python-Projects/Weather-App-GUI

```


2. **Install the required libraries** (see Prerequisites).
3. **Run the script:**
```bash
python main.py

```


4. Enter any city name (e.g., "Islamabad", "London", "Tokyo") and click **Check Weather**.

## 📂 File Structure

```text
Weather-App-GUI/
├── main.py         # Main PyQt5 application script
├── README.md       # Project documentation

```

## ⚡ Technologies Used

* **Python 3.x**
* **PyQt5:** For building the graphical user interface.
* **Requests Module:** For handling REST API GET requests.
* **JSON:** For parsing the API response data.

## 🌟 Show Some Love

If you like this UI or the practical advice feature, please **⭐ the repository**! 🚀