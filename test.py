import requests
import json

url = 'https://portal.unn.ru/ruzapi/schedule/group/47181?start=2024.09.10&finish=2024.09.10&lng=1'
r = requests.get(url)
print(len(r.json()))
print(json.dumps(r.json(), indent=4))