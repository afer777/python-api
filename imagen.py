
from webexteamssdk import WebexTeamsAPI

api = WebexTeamsAPI()
room_id = "Y2lzY29zcGFyazovL3VzL1JPT00vYzg2ZjljMDAtNTY5Yi0xMWVjLThjNmUtYjE2MmM5MjUxYmVl"
files= ["https://upload.wikimedia.org/wikipedia/commons/f/f3/Deadpool%2C_Georgia_Viaduct%2C_Vancouver%2C_April_6_2015_-_3.jpg"]

api.messages.create(roomId = room_id, text = "Deadpool enviando imagenes desde Python",files=files)