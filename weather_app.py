import requests

api_key = "your api here"

city = input("Enter the city name: ").capitalize().strip()

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

get_data = requests.get(url)

data = get_data.json()


get_weather = data["weather"][0]["description"].capitalize()
get_temperature = data["main"]["temp"]

temperature_in_celsius = get_temperature - 273.15 # Converts temperature to Celsius

print(f"The Weather in {city} is {get_weather}")
print(f"The Temperature in {city} is {temperature_in_celsius:.2f}°C")