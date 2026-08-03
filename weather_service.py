import requests

class WeatherService:
    def get_weather(self, latitude: float, longitude: float) -> dict | None:
        url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            return {
                "temperature": data["current_weather"]["temperature"],
                "windspeed": data["current_weather"]["windspeed"],
            }
        except requests.RequestException:
            print("Ошибка подключения")
            return None

if __name__ == "__main__":
    ws = WeatherService()
    result = ws.get_weather(55.75, 37.62)
    print(result)