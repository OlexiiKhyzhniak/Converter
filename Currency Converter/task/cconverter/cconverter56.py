import json
import requests


val_uta = input()
val_uta = val_uta.lower()
# url2 = 'http://www.floatrates.com/json-feeds.html'
req = requests.get(f"http://www.floatrates.com/daily/{val_uta}.json")
req2 = req.json()
print(req2['usd'])
print(req2['eur'])
