import requests
import json
import base64
import os

url = "https://dev111297.service-now.com/api/now/table/incident"
username = os.environ["SERVICENOW_USERNAME"]
password = os.environ["SERVICENOW_PASSWORD"]
room_id = "Y2lzY29zcGFyazovL3VzL1JPT00vYmFkYjcyZTAtNTg5OC0xMWVjLThkMjYtYTk1ZWQ3ZDZhYTJl"

payload = {
    "description": "Al intentar llamar a una extensión recibo tono de ocupado.",
    "short_description": "Tiquete abierto desde Python",
    "category": "Network",
    "caller_id": "abraham.lincoln@example.com"
}

data = json.dumps(payload)

headers = {
  "Content-Type": "application/json"
}

response = requests.post(url, auth=(username, password), headers=headers, data=data)

print(response.text)