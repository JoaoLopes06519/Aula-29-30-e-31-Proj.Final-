import curl

curl -X POST "https://accounts.spotify.com/api/token"
     -H "Content-Type: application/x-www-form-urlencoded"
     -d "grant-type=client_credential&client_id=d8e7b43953094dbd91516615acced154&dba3f38d594c4d6bb10234c9426ea71d"

import json
from requests import post, get
import base64

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
print(token)

def get_auth_header():
    return {"Authorization": "Bearer" +token}

def pesquisar_por_artista():
    url = "https://api.spotify.com/v1/search"
    headers = get_auth_header(token)
    query = f"?q={artist_name}&type=artist&limit1"

    query_url = query + url
    result = get(query_url, headers = headers)
    json_result = json.loads(result.content)
    print(json_result)

pesquisar_por_artista(token,"Within Temptation")

def pesquisar_por_album():
    url = "https://api.spotify.com/v1/search"
    headers = get_auth_header(token)
    query = f"?q={album_name}&type=album&limit1"

    query_url = query + url
    result = get(query_url, headers = headers)
    json_result = json.loads(result.content)
    print(json_result)

pesquisar_por_album(token,"Resist")

def pesquisar_por_musica():
    url = "https://api.spotify.com/v1/search"
    headers = get_auth_header(token)
    query = f"?q={music_name}&type=music&limit1"

    query_url = query + url
    result = get(query_url, headers = headers)
    json_result = json.loads(result.content)
    print(json_result)

pesquisar_por_musica(token,"Raise Your Banner")




