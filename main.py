import tkinter as tk
import requests

# Replace with your OpenWeatherMap API key
API_KEY = "YOUR_API_KEY"

def get_weather(city):
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
        response = requests.get(url)
        data = response.json()
        weather_description = data["weather"][0]["description"]
        temperature = data["main"]["temp"] - 273.15  # Convert from Kelvin to Celsius
        humidity = data["main"]["humidity"]

        result_label.config(text=f"Weather: {weather_description}\nTemperature: {temperature:.2f}°C\nHumidity: {humidity}%")
    except Exception as e:
        result_label.config(text="An error occurred. Please check the city name or your internet connection.")

def search():
    city = city_entry.get()
    if city:
        get_weather(city)
    else:
        result_label.config(text="Please enter a city name.")

app = tk.Tk()
app.title("Weather App")

city_label = tk.Label(app, text="Enter City:")
city_label.pack()

city_entry = tk.Entry(app)
city_entry.pack()

search_button = tk.Button(app, text="Search", command=search)
search_button.pack()

result_label = tk.Label(app, text="")
result_label.pack()

app.mainloop()

