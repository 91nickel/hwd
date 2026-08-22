import requests

data = requests.get("http://api.open-notify.org/iss-now.json").json()
lat  = data["iss_position"]["latitude"]
lon  = data["iss_position"]["longitude"]
print(f"МКС сейчас над координатами: {lat}, {lon}")

people = requests.get("http://api.open-notify.org/astros.json").json()
print("Сейчас в космосе:", people["number"], "человек")
for p in people["people"]:
    print("-", p["name"])
