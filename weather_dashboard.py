import requests
import json
import os

API_KEY = "your_api_key"   
FILE = "history.json"

def load_history():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return []

def save_history(history):
    with open(FILE, "w") as f:
        json.dump(history, f, indent=2)

def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    res = requests.get(url).json()
    if res.get("cod") != 200:
        return f"Error: {res.get('message')}"
    temp = res["main"]["temp"]
    cond = res["weather"][0]["description"]
    return f"{city.title()}: {temp}°C, {cond}"

def main():
    history = load_history()

    while True:
        print("\n--- Weather Dashboard ---")
        print("1. Search weather by city")
        print("2. Show last 5 searches")
        print("3. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            city = input("Enter city: ")
            result = get_weather(city)
            print(result)
            history.append(result)
            save_history(history[-5:])  # keep only last 5

        elif choice == "2":
            print("\nLast 5 Searches:")
            for h in history[-5:]:
                print("-", h)

        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
