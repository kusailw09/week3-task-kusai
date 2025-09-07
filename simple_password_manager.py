import json, base64, os

FILE = "passwords.json"

def load_data():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return []

def save_data(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=2)

def encode(pwd):
    return base64.b64encode(pwd.encode()).decode()

def decode(pwd):
    return base64.b64decode(pwd.encode()).decode()

def add_entry(site, user, pwd):
    data = load_data()
    data.append({"website": site, "username": user, "password": encode(pwd)})
    save_data(data)
    print("Saved successfully!")

def view_entries():
    data = load_data()
    if not data:
        print("No entries found.")
    for e in data:
        print(f"{e['website']} | {e['username']} | {decode(e['password'])}")

# --- Menu ---
while True:
    print("\n1. Add Entry\n2. View Entries\n3. Exit")
    ch = input("Enter choice: ")

    if ch == "1":
        s = input("Website: ")
        u = input("Username: ")
        p = input("Password: ")
        add_entry(s, u, p)

    elif ch == "2":
        view_entries()

    elif ch == "3":
        break
    else:
        print("Invalid choice!")
