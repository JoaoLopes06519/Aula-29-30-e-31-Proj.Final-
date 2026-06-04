import json
from requests import post, get
import base64
from tkinter import *

root = Tk()
root.title = ("Leitor de Música")
root.geometry = ("400x300")

def get_token():
    client_id = "d8e7b43953094dbd91516615acced154"
    client_secret = "dba3f38d594c4d6bb10234c9426ea71d"

    auth_string = f"{client_id}:{client_secret}"
    auth_bytes = auth_string.encode("utf-8")

    auth_base64 = str(base64.b64encode(auth_bytes))

    url = ("https://accounts.spotify.com/api/token")
    cabecalho = {"Authorization": "Basic" + auth_base64
             "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {"grant_type":"client_credentials"}
    result = post(url, cabecalho = cabecalho, data = data)
    json_result = json.loads(result.content)
    token = json_result ["acess_token"]
    return token

token = get_token()






