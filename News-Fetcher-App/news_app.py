import requests
import json

api_key = "your api here"

query = input("What type of news do you want?: ")

url = f"https://newsapi.org/v2/everything?q={query}&apiKey={api_key}"

r = requests.get(url)
news = json.loads(r.text)

for article in news["articles"]:
    print(f"Title: {article["title"]}")
    print(f"Description: {article["description"]}")
    print()
    print("-----------------------------------------")
