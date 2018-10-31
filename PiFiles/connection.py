import json
import requests


r = requests.get("http://172.16.0.1:8001/FieldData/GetData")
parsed = dict()
parsed = json.loads(r.text)

