import requests
import json

url = "https://webexapis.com/v1/messages"
token = "ZGM5NmFjNWMtNmNiMy00OGMxLTljMWUtYmFiNzE1MWM3NjNlM2I5YWZkY2QtMjM0_PF84_2a001399-4e85-4adc-b568-32f8032f2ae7"
room_id = "Y2lzY29zcGFyazovL3VzL1JPT00vYzg2ZjljMDAtNTY5Yi0xMWVjLThjNmUtYjE2MmM5MjUxYmVl"

payload = {
  "roomId": room_id,
  "text": "hi from Postman"
}

data = json.dumps(payload)

headers = {
  "Authorization": "Bearer " + token,
  "Content-Type": "application/json"
}

response = requests.post(url, headers=headers, data=data)

print(response.text)