from weather_service import WeatherService
from database import Database

if __name__ == "__main__":
    ws = WeatherService()
    db = Database()
    CITIES = {
        "Москва": (55.75, 37.62),
        "Санкт-Петербург": (59.93, 30.31),
        "Казань": (55.79, 49.12),
        "Новосибирск": (55.03, 82.92)
    }

    while True:
        option = input("1. Узнать погоду\n2. История запросов\n3. Выход\n")
        if option == "1":
            city = input("Введите город: ")
            if city not in CITIES:
                print(f"Доступны: {', '.join(CITIES)}")
                continue
            result = ws.get_weather(*CITIES.get(city))
            if result is None:
                continue
            print(f"В {city} {result["temperature"]}°C, ветер {result["windspeed"]} км/ч")
            db.save_request(city, result["temperature"], result["windspeed"])
        elif option == "2":
            history = db.get_history()
            if not history:
                print("История пуста")
            else:
                print(f"{'ID':<3} | {'Город':<10} | {'Температура':<12} | {'Ветер':<5} | {'Дата':<10}")
                for row in history:
                    print(f"{row[0]:<3} | {row[1]:<10} | {row[2]:<12} | {row[3]:<5} | {row[4]:<10}")
        elif option == "3":
            db.close()
            print("До свидания")
            break
        else:
            print("Неверный выбор, возвращаемся в меню")
            continue
