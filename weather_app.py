import requests

class WeatherApp:
    def __init__(self, api_key):
        self._api_key = api_key
        self._city = None
        self._weather_data = None

    def set_city(self, city):
        self._city = city

    def get_city(self):
        return self._city

    def _fetch_weather(self):
        if not self._city:
            raise ValueError("City is not set. Use set_city() to set the city.")
        
        url = f"http://api.openweathermap.org/data/2.5/weather?q={self._city}&appid={self._api_key}&units=metric"
        response = requests.get(url)

        if response.status_code == 200:
            self._weather_data = response.json()
        else:
            self._weather_data = None

    def get_weather(self):
        if not self._weather_data:
            self._fetch_weather()
        return self._weather_data

    def display_weather(self):
        self._fetch_weather()
        if self._weather_data:
            weather = self._weather_data

            city_name = weather['name']
            temperature = weather['main']['temp']
            weather_description = weather['weather'][0]['description']
            humidity = weather['main']['humidity']
            wind_speed = weather['wind']['speed']

            print(f"Weather in {city_name}:")
            print("=" * 30)
            print(f"🌍 City: {city_name}")
            print(f"🌡️  Temperature: {temperature} °C")
            print(f"🌦️  Description: {weather_description.capitalize()}")
            print(f"💧 Humidity: {humidity}%")
            print(f"🍃 Wind Speed: {wind_speed} km/h")
        else:
            print("Error: Unable to fetch weather data. Please check the city name or your API key.")

def main():
    api_key = "8c2b98e9957d1baa97a9aecb15f14af9"
    weather_app = WeatherApp(api_key)

    city = input("Enter the city name: ")
    weather_app.set_city(city)

    weather_app.display_weather()

if __name__ == "__main__":
    main()
