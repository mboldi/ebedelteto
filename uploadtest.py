import requests
import json

url = 'http://hugo.premontrei.hu/api/v1/cardread'

adatStr = '{"cardreaderId": "1", "cardId": "0102030400000000"}'

adat = json.loads(adatStr)

headers = {"Content-Type": "application/json"}

response = requests.post(url, data = json.dumps(adat), headers=headers)

print response.json()['output'][1]