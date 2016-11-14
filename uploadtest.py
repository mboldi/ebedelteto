import requests
import json

url = 'http://hugo.premontrei.hu/api/v1/cardread'

ID = "0403020100000000"

adat = {"cardreaderId": "1", "cardId": ID}

#adat = json.loads(adatStr)

headers = {"Content-Type": "application/json"}

response = requests.post(url, data = json.dumps(adat), headers=headers)

print response.json()['status']