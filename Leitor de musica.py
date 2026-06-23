import io
import tkinter as tk
from tkinter import messagebox
import pygame
import requests

# Inicializa o mixer do pygame logo no início
pygame.mixer.init()


def enviar_dados():
    # 1. Usamos o .get() para extrair o texto de cada campo que criámos lá em baixo
    nome_artista = entry_artista.get()
    nome_musica = entry_musica.get()
    nome_album = entry_album.get()

    # Se o utilizador não escrever nada, usamos uma pesquisa padrão
    termo_pesquisa = ""
    if nome_musica:
        termo_pesquisa += nome_musica
    if nome_artista:
        termo_pesquisa += f" {nome_artista}"

    if not termo_pesquisa:
        termo_pesquisa = "Within Temptation"  # Padrão caso esteja vazio

    # Exibe um alerta na tela com as informações recebidas
    mensagem = f"A pesquisar...\nArtista: {nome_artista}\nMúsica: {nome_musica}"
    messagebox.showinfo("Dados Recebidos", mensagem)

    # Chamar a API dinamicamente com o que o utilizador digitou
    chamar_api(termo_pesquisa)


def chamar_api(termo):
    # Parar qualquer música que esteja a tocar antes de iniciar outra
    pygame.mixer.music.stop()
    pygame.mixer.music.unload()

    # Inserir o termo de pesquisa diretamente no URL da API
    url = f"https://api.deezer.com/search?q={termo}"

    try:
        response = requests.get(url)
        data = response.json()

        if not data.get("data"):
            messagebox.showerror("Erro", "Nenhuma música encontrada!")
            return

        dados = data["data"][0]
        link_preview = dados["preview"]
        titulo = dados["title"]
        artista = dados["artist"]["name"]

        print(f"A tocar: {titulo} - {artista}")
        print(f"URL do Preview: {link_preview}")

        # 2. Descarregar o ficheiro de áudio em formato de bytes
        resposta_audio = requests.get(link_preview)
        ficheiro_audio_memoria = io.BytesIO(resposta_audio.content)

        # 3. Carregar e reproduzir no Pygame
        pygame.mixer.music.load(ficheiro_audio_memoria)
        pygame.mixer.music.play()

        # NOTA: Removeu-se o "while" com "time.sleep" para a janela do Tkinter não congelar!

    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro ao carregar a música: {e}")


# --- CONFIGURAÇÃO DA INTERFACE (Fora das funções) ---
root = tk.Tk()
root.title("Leitor de Música")
root.geometry("350x300")
img_btn_play = tk.PhotoImage(file="botão_reproduzir.png")
img_btn_stop = tk.PhotoImage(file="botão pausar.png")

# Criar e posicionar as Labels e Entries na janela principal
tk.Label(root, text="Artista:", font=("Arial", 10)).pack(pady=2)
entry_artista = tk.Entry(root, width=30)
entry_artista.pack(pady=5)

tk.Label(root, text="Música:", font=("Arial", 10)).pack(pady=2)
entry_musica = tk.Entry(root, width=30)
entry_musica.pack(pady=5)

tk.Label(root, text="Álbum:", font=("Arial", 10)).pack(pady=2)
entry_album = tk.Entry(root, width=30)
entry_album.pack(pady=5)

img_btn_reproduzir = tk.PhotoImage(file="botão_reproduzir.png.")
img_btn_pausar = tk.PhotoImage(file="botão pausar.png")

btn_reproduzir = tk.Button(root, image=img_btn_play, command=chamar_api, bd=0, cursor="hand2")
btn_reproduzir.place(x=100, y=250)

btn_pausar = tk.Button(root, image=img_btn_pausar, command=chamar_api, bd=0, cursor="hand2")
btn_pausar.place(x=100, y=250)


# Executa o aplicativo (Apenas uma vez, no final do ficheiro!)
root.mainloop()