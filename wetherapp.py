import requests

def get_weather(city):
    try:
        # OpenWeatherMap API (Free signup required to get API key)
        API_KEY = "yo20cbe1a97ee6428f627e472c27141a85"
        BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

        # Send request
        params = {"q": city, "appid": API_KEY, "units": "metric"}
        response = requests.get(BASE_URL, params=params)

        # Check response
        if response.status_code == 200:
            data = response.json()
            main = data["main"]
            weather = data["weather"][0]

            print(f"\n🌍 Weather in {city.title()}:")
            print(f"Temperature: {main['temp']}°C")
            print(f"Feels Like: {main['feels_like']}°C")
            print(f"Condition: {weather['description'].title()}")
            print(f"Humidity: {main['humidity']}%")
        else:
            print("⚠️ City not found. Try again.")

    except Exception as e:
        print("❌ Error:", e)


def main():
    print("=== Weather Forecast CLI App ===")
    while True:
        city = input("\nEnter city name (or type 'exit' to quit): ")
        if city.lower() == "exit":
            print("Goodbye 👋")
            break
        get_weather(city)


if __name__ == "__main__":
    main()



