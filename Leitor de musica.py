import io
import tkinter as tk
from tkinter import messagebox
import pygame
import requests

# 1. Inicializar o Pygame Mixer
pygame.mixer.init()

# Variável global para controlar se a música está pausada ou não
musica_pausada = False


def chamar_api():
    global musica_pausada

    # Se a música estiver apenas pausada e o utilizador clicar no Play principal,
    # ela continua de onde parou.
    if musica_pausada:
        pygame.mixer.music.unpause()
        musica_pausada = False
        print("Música retomada pelo botão Play!")
        return

    # Caso contrário, para o que estiver a tocar para carregar uma nova pesquisa
    pygame.mixer.music.stop()
    pygame.mixer.music.unload()

    artista = entry_artista.get().strip()
    musica = entry_musica.get().strip()

    termo_pesquisa = f"{musica} {artista}".strip()
    if not termo_pesquisa:
        termo_pesquisa = "Within Temptation"

    url = f"https://api.deezer.com/search?q={termo_pesquisa}"

    try:
        response = requests.get(url)
        data = response.json()

        if not data.get("data"):
            messagebox.showerror("Erro", "Nenhuma música encontrada para esta pesquisa.")
            return

        dados = data["data"][0]
        link_preview = dados["preview"]
        titulo_musica = dados["title"]
        nome_artista = dados["artist"]["name"]

        print(f"A carregar da API: {titulo_musica} - {nome_artista}")

        # Descarregar os bytes do áudio
        resposta_audio = requests.get(link_preview)
        ficheiro_audio_memoria = io.BytesIO(resposta_audio.content)

        # Carregar na memória nativa de música do Pygame
        pygame.mixer.music.load(ficheiro_audio_memoria)
        pygame.mixer.music.play()
        musica_pausada = False
        print("A reproduzir som!")

    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao tocar música: {e}")


def pausar_musica():
    global musica_pausada

    # Se a música NÃO está pausada, vamos pausá-la
    if not musica_pausada:
        pygame.mixer.music.pause()
        musica_pausada = True
        print("Música pausada exatamente aqui!")

    # Se JÁ ESTÁ pausada, o próximo clique vai retomar do mesmo sítio
    else:
        pygame.mixer.music.unpause()
        musica_pausada = False
        print("Música retomada do exato ponto da pausa!")


# --- 2. CRIAÇÃO DA INTERFACE VISUAL ---
root = tk.Tk()
root.title("Leitor de Música")
root.geometry("400x350")
root.config(bg="#2c3e50")

# Título do Programa
lbl_titulo = tk.Label(root, text="Leitor de Música", fg="white", bg="#2c3e50", font=("Arial", 14, "bold"))
lbl_titulo.pack(pady=15)

# Campos de Entrada
tk.Label(root, text="Nome do Artista:", fg="white", bg="#2c3e50", font=("Arial", 10)).pack(pady=2)
entry_artista = tk.Entry(root, width=30, font=("Arial", 11))
entry_artista.pack(pady=5)

# Campo da Música
tk.Label(root, text="Nome da Música:", fg="white", bg="#2c3e50", font=("Arial", 10)).pack(pady=2)
entry_musica = tk.Entry(root, width=30, font=("Arial", 11))
entry_musica.pack(pady=5)

# Campo do Álbum
tk.Label(root, text="Nome do Álbum:", fg="white", bg="#2c3e50", font=("Arial", 10)).pack(pady=2)
entry_album = tk.Entry(root, width=30, font=("Arial", 11))
entry_album.pack(pady=5)

# Carregar imagens do Paint
img_btn_reproduzir = tk.PhotoImage(file="botão_reproduzir.png")
img_btn_pausar = tk.PhotoImage(file="botão pausar.png")

# Botão Reproduzir
btn_reproduzir = tk.Button(root, image=img_btn_reproduzir, command=chamar_api, bd=0, cursor="hand2")
btn_reproduzir.place(x=80, y=260)

# Botão Pausar (Chama a função alternada pausar_musica)
btn_pausar = tk.Button(root, image=img_btn_pausar, command=pausar_musica, bd=0, cursor="hand2")
btn_pausar.place(x=220, y=260)

root.mainloop()
