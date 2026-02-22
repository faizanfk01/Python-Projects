import sys
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QGridLayout, QFrame
from PyQt5.QtCore import Qt

class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Weather App by Faizan")
        self.setFixedSize(650, 980) 
        self.initUI()

    def initUI(self):
        self.main_layout = QVBoxLayout()
        self.main_layout.setContentsMargins(35, 35, 35, 35)
        self.main_layout.setSpacing(20)

        self.city_input = QLineEdit(self)
        self.city_input.setPlaceholderText("Enter city (e.g. Islamabad)...")
        self.city_input.setObjectName("city_input")
        
        self.get_weather_button = QPushButton("🔍 Check Weather")
        self.get_weather_button.setObjectName("get_weather_button")
        
        self.main_layout.addWidget(self.city_input)
        self.main_layout.addWidget(self.get_weather_button)

        self.hero_frame = QFrame()
        self.hero_frame.setObjectName("hero_frame")
        self.hero_layout = QVBoxLayout()
        
        self.emoji_label = QLabel("🌍")
        self.emoji_label.setObjectName("emoji_label")
        self.emoji_label.setAlignment(Qt.AlignCenter)
        
        self.temperature_label = QLabel("--°C")
        self.temperature_label.setObjectName("temperature_label")
        self.temperature_label.setAlignment(Qt.AlignCenter)
        
        self.description_label = QLabel("Waiting for input...")
        self.description_label.setObjectName("description_label")
        self.description_label.setAlignment(Qt.AlignCenter)

        self.hero_layout.addWidget(self.emoji_label)
        self.hero_layout.addWidget(self.temperature_label)
        self.hero_layout.addWidget(self.description_label)
        self.hero_frame.setLayout(self.hero_layout)
        self.main_layout.addWidget(self.hero_frame)

        self.details_frame = QFrame()
        self.details_frame.setObjectName("details_frame")
        self.details_grid = QGridLayout()
        self.details_grid.setSpacing(15)

        self.feels_like_label = QLabel("Feels Like: --")
        self.feels_like_label.setObjectName("grid_label")
        self.feels_like_label.setAlignment(Qt.AlignCenter) 

        self.humidity_label = QLabel("Humidity: --")
        self.humidity_label.setObjectName("grid_label")
        self.humidity_label.setAlignment(Qt.AlignCenter) 

        self.wind_label = QLabel("Wind: --")
        self.wind_label.setObjectName("grid_label")
        self.wind_label.setAlignment(Qt.AlignCenter) 

        self.pressure_label = QLabel("Pressure: --") 
        self.pressure_label.setObjectName("grid_label")
        self.pressure_label.setAlignment(Qt.AlignCenter) 

        self.details_grid.addWidget(self.feels_like_label, 0, 0)
        self.details_grid.addWidget(self.humidity_label, 0, 1)
        self.details_grid.addWidget(self.wind_label, 1, 0)
        self.details_grid.addWidget(self.pressure_label, 1, 1)

        self.details_frame.setLayout(self.details_grid)
        self.main_layout.addWidget(self.details_frame)

        self.advice_frame = QFrame()
        self.advice_frame.setObjectName("advice_frame")
        self.advice_layout = QVBoxLayout()
        
        self.advice_title = QLabel("💡 Weather Advice:")
        self.advice_title.setObjectName("advice_title")
        
        self.advice_text = QLabel("Enter a city to generate practical advice.")
        self.advice_text.setObjectName("advice_text")
        self.advice_text.setWordWrap(True) 
        
        self.advice_layout.addWidget(self.advice_title)
        self.advice_layout.addWidget(self.advice_text)
        self.advice_frame.setLayout(self.advice_layout)
        self.main_layout.addWidget(self.advice_frame)

        self.setLayout(self.main_layout)

        self.setStyleSheet("""
            QWidget {
                background-color: #0f172a;
                color: #f8fafc;
                font-family: 'Segoe UI', Arial;
            }
            QLineEdit#city_input {
                font-size: 24px; padding: 15px;
                background-color: #1e293b; border: 2px solid #475569;
                border-radius: 15px; color: white;
            }
            QPushButton#get_weather_button {
                font-size: 22px; font-weight: bold;
                background-color: #0ea5e9; color: white;
                border-radius: 15px; padding: 15px;
            }
            QPushButton#get_weather_button:hover { background-color: #0284c7; }
            
            QFrame#hero_frame, QFrame#details_frame {
                background-color: #1e293b; border-radius: 15px; padding: 15px;
            }
            QFrame#advice_frame {
                background-color: #064e3b; 
                border: 2px solid #10b981; border-radius: 15px; padding: 15px;
            }
            
            QLabel#emoji_label { font-size: 110px; background-color: #0f172a; border-radius: 10px; padding: 5px; }
            QLabel#temperature_label { font-size: 85px; font-weight: bold; background-color: #0f172a; border-radius: 10px; padding: 5px; }
            QLabel#description_label { font-size: 28px; text-transform: capitalize; color: #94a3b8; background-color: #0f172a; border-radius: 10px; padding: 5px; }
            
            QLabel#grid_label { 
                background-color: #0f172a; 
                border-radius: 10px; 
                padding: 12px; 
                font-size: 20px; 
                color: #cbd5e1; 
            }
            
            QLabel#advice_title { font-size: 24px; font-weight: bold; color: #34d399; background-color: #022c22; border-radius: 10px; padding: 10px; }
            QLabel#advice_text { font-size: 22px; color: #ecfdf5; margin-top: 5px; background-color: #022c22; border-radius: 10px; padding: 15px; }
            
            QLabel { font-size: 20px; color: #cbd5e1; }
        """)

        self.get_weather_button.clicked.connect(self.get_weather)

    def get_weather(self):
        self.advice_text.setText("Analyzing new data...")
        self.description_label.setText("Fetching...")
        self.emoji_label.setText("🌍")
        
        self.temperature_label.setStyleSheet("font-size: 85px; font-weight: bold; background-color: #0f172a; border-radius: 10px; padding: 5px; color: #ffffff;")
        self.temperature_label.setText("--°C")
        
        self.feels_like_label.setText("Feels Like: --")
        self.humidity_label.setText("Humidity: --")
        self.wind_label.setText("Wind: --")
        self.pressure_label.setText("Pressure: --")
        
        api_key = "YOUR_API_KEY_HERE"
        city = self.city_input.text()
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()

            if data["cod"] == 200:
                self.display_weather(data)

        except requests.exceptions.HTTPError as http_error:
            match response.status_code:
                case 400: self.display_error("Bad request:\nPlease check your input")
                case 401: self.display_error("Unauthorized:\nInvalid API key")
                case 403: self.display_error("Forbidden:\nAccess is denied")
                case 404: self.display_error("Not found:\nCity not found")
                case 500: self.display_error("Internal server Error:\nPlease try again later")
                case 502: self.display_error("Bad Gateway:\nInvalid response from the server")
                case 503: self.display_error("Service Unavailable:\nService is down")
                case 504: self.display_error("Gateway Timeout:\nNo response from the server")
                case _: self.display_error(f"HTTP error occured:\n{http_error}")

        except requests.exceptions.ConnectionError:
            self.display_error("Connection Error:\nCheck your internet connection")
        except requests.exceptions.Timeout:
            self.display_error("Timeout Error:\nThe request timed out")
        except requests.exceptions.RequestException as req_error:
            self.display_error(f"Request Error:\n{req_error}")

    def display_error(self, message):
        self.temperature_label.setText(message)
        self.temperature_label.setStyleSheet("font-size: 24px; color: #ef4444; background-color: #0f172a; border-radius: 10px; padding: 5px;")
        self.emoji_label.setText("⚠️")
        self.description_label.setText("Error")
        self.advice_text.setText("Could not retrieve data to analyze.")
        
        self.feels_like_label.setText("Feels Like: --")
        self.humidity_label.setText("Humidity: --")
        self.wind_label.setText("Wind: --")
        self.pressure_label.setText("Pressure: --")

    def display_weather(self, data):
        self.temperature_label.setStyleSheet("font-size: 85px; font-weight: bold; color: #ffffff; background-color: #0f172a; border-radius: 10px; padding: 5px;")
        
        temperature_k = data["main"]["temp"]
        temperature_c = temperature_k - 273.15
        
        feels_like_c = data["main"]["feels_like"] - 273.15
        weather_id = data["weather"][0]["id"]
        weather_description = data["weather"][0]["description"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]
        pressure = data["main"]["pressure"]

        self.temperature_label.setText(f"{temperature_c:.0f}°C")
        self.emoji_label.setText(self.get_weather_emoji(weather_id))
        self.description_label.setText(weather_description)
        
        self.feels_like_label.setText(f"🌡️ Feels Like: {feels_like_c:.0f}°C")
        self.humidity_label.setText(f"💧 Humidity: {humidity}%")
        self.wind_label.setText(f"🌬️ Wind: {wind_speed} m/s")
        self.pressure_label.setText(f"⏲️ Pressure: {pressure} hPa")

        self.generate_dad_advice(temperature_c, weather_id, wind_speed)

    def generate_dad_advice(self, temp, weather_id, wind):
        advice = ""
        
        if 200 <= weather_id <= 622:
            advice += "Precipitation expected. Bad day for a car wash. Drive carefully on wet roads.\n"
        elif weather_id == 800:
            advice += "Clear skies. Great day to wash the car or do outdoor maintenance.\n"
            
        if temp > 35:
            advice += "High heat warning. AC electricity load will be heavy today. Check car coolant levels.\n"
        elif temp < 10:
            advice += "Cold temperatures. Geyser gas usage will be high. Check tire pressure as it drops in cold weather.\n"
            
        if wind > 10:
            advice += "High winds detected. Secure loose outdoor items."
            
        if advice == "":
            advice = "Conditions are stable. Normal daily routines recommended."
            
        self.advice_text.setText(advice)

    @staticmethod
    def get_weather_emoji(weather_id):
        if 200 <= weather_id <= 232: return "⛈️"
        elif 300 <= weather_id <= 321: return "🌦️"
        elif 500 <= weather_id <= 531: return "🌧️"
        elif 600 <= weather_id <= 622: return "❄️"
        elif 701 <= weather_id <= 741: return "༄"
        elif weather_id == 762: return "🌋"
        elif weather_id == 771: return "💨"
        elif weather_id == 781: return "🌪️"
        elif weather_id == 800: return "☀️"
        elif 801 <= weather_id <= 804: return "☁️"
        else: return "🌍"

if __name__ == "__main__":
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())