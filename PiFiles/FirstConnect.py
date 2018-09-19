input("Pause.")

import json
import requests

print("Getting Data...\n")
r = requests.get('http://172.16.0.1:8001/FieldData/GetData')
print(r.text)
print('\n')
print("Got Data.\n")

parsed = json.loads(r.text)
ball = parsed['Ball']
print(ball['Object Center'])

input("Function Complete. Press 'Enter' to exit.")