import requests

def get_weather(city_name):
    api_key = "528bc1904001340e332f47391785bd3d"  # Replace with your actual key
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    
    # Parameters for the API call
    params = {
        "q": city_name,
        "appid": api_key,
        "units": "metric"  # Use 'imperial' for Fahrenheit
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if data["cod"] == 200:
            temp = data["main"]["temp"]
            desc = data["weather"][0]["description"]
            print(f"\n--- Weather in {city_name.capitalize()} ---")
            print(f"Temperature: {temp}°C")
            print(f"Condition: {desc.title()}")
        else:
            print(f"City not found. (Error: {data['message']})")
            
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    city = input("Enter city name: ")
    get_weather(city)