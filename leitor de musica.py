from tkinter import *
#import pygame
import requests

root = Tk()
root.title ("Leitor de Música")
root.geometry("500x300")

def chamar_api():
	url = "https://api.deezer.com/search?q='Foo Fighters'"

	# A GET request to the API
	response = requests.get(url)
	data = response.json()
	dados = data["data"][0]
	dados2 = dados["preview"]

	print(dados2)

	# Print the response
	print(response.json())


chamar_api()


root.mainloop()