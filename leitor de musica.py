import io
from tkinter import *
import pygame
import requests

root = Tk()
root.title ("Leitor de Música")
root.geometry("500x300")

def chamar_api():
	url = "https://api.deezer.com/search?q='Within Temptation'"

	# A GET request to the API
	response = requests.get(url)
	data = response.json()
	dados = data["data"][0]
	dados2 = dados["preview"]
	musica = dados["title"]
	artista = dados["artist"]["name"]
	album = dados["album"]["title"]

	print(dados2)

	# Print the response
	print(response.json())


	# 2. Descarregar o ficheiro de áudio em formato de bytes
	resposta_audio = requests.get(dados2)

	# Transformar os bytes num "objeto semelhante a um ficheiro" na memória
	ficheiro_audio_memoria = io.BytesIO(resposta_audio.content)

	# 3. Inicializar o Pygame e reproduzir
	pygame.mixer.init()

	# O pygame.mixer.music consegue ler objetos do tipo BytesIO diretamente!
	pygame.mixer.music.load(ficheiro_audio_memoria)

	print("\nA reproduzir a amostra! Prime Ctrl+C para parar.")
	pygame.mixer.music.play()

	# Manter o programa aberto enquanto a música toca
	import time

	while pygame.mixer.music.get_busy():
		time.sleep(1)





chamar_api()


root.mainloop()
