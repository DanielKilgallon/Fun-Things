import json
import random

with open("./CoolNames.json", mode="r", encoding="utf-8") as json_data:
    data = json.load(json_data)
    print(random.choice(data))