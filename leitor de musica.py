import io
import tkinter as tk
from tkinter import *
from tkinter import messagebox
import pygame
import requests

root = Tk()
root.title ("Leitor de Música")
root.geometry("500x300")

# Função que será chamada quando o botão for clicado
def enviar_dados():
	# 1. Primeiro cria a variável salvando o Entry
	entry_artista = tk.Entry(root, width=30)

	# 2. Depois coloca ele na tela com o pack
	entry_artista.pack(pady=5)
	
    entry_musica = tk.Entry(root, width=30)
	
    entry_album = tk.Entry(root, width=30)
	
	
	# .get() serve para pegar o texto que foi digitado em cada campo
	artista = entry_artista.get()
	musica = entry_musica.get()
	album = entry_album.get()

	# Exibe um alerta na tela com as informações recebidas
	mensagem = f"Artista: {artista}\nMúsica: {musica}\nÁlbum: {album}"
	messagebox.showinfo("Dados Recebidos", mensagem)


    # 1. Criando a janela principal
        root = tk.Tk()
        root.title("Cadastro de Músicas")
        root.geometry("300x250")  # Define o tamanho da janela

     # 2. Criando os campos para o ARTISTA
        lbl_artista = tk.Label(root, text="Nome do Artista:")
        lbl_artista.pack(pady=2)
        entry_artista = tk.Entry(root, width=30)
        entry_artista.pack(pady=5)

    # 3. Criando os campos para a MÚSICA
        lbl_musica = tk.Label(root, text="Nome da Música:")
        lbl_musica.pack(pady=2)
        entry_musica = tk.Entry(root*, width=30)
        entry_musica.pack(pady=5)

    # 4. Criando os campos para o ÁLBUM
        lbl_album = tk.Label(root, text="Nome do Álbum:")
        lbl_album.pack(pady=2)
        entry_album = tk.Entry(root, width=30)
        entry_album.pack(pady=5)

    # 5. Criando o Botão de Enviar**
        btn_enviar = tk.Button(root, text="Salvar Música", command=enviar_dados)
        btn_enviar.pack(pady=15)

    # Executa o aplicativo
        root.mainloop()



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


enviar_dados()

chamar_api()


root.mainloop()



