import requests

API_KEY = "c5f777f9dad606dc9b9181b7d26ea8f6"
city = input("Enter city name: ")

url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
response = requests.get(url).json()

if response.get("main"):
    temp = response["main"]["temp"]
    desc = response["weather"][0]["description"]
    print(f"Temperature in {city}: {temp}°C")
    print(f"Weather: {desc}")
else:
    print("City not found!")
