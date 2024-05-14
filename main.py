from tkinter import *
import tkinter as tk
from tkinter import filedialog
import os
from os import environ, listdir
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame, sys, time

root = tk.Tk()
root.title("Music Player")
root.geometry("400x300")  # Define o tamanho da janela
root.configure(bg="lavender")  # Altera a cor de fundo da janela
root.iconbitmap('icons/icone.ico')

pygame.mixer.init()
dir_path = filedialog.askdirectory()

if dir_path:
    files = os.listdir(dir_path)
    mp3_files = [file for file in files if file.endswith('.mp3')]

    if not mp3_files:
        print("Nenhum arquivo .mp3 encontrado no diretório selecionado.")
    else:
        # Mostra os arquivos encontrados
        print("Arquivos .mp3 encontrados:")
        for mp3_file in mp3_files:
            print(os.path.join(dir_path, mp3_file))

current_index = 0  # Definir a variável current_index fora da função
pygame.mixer.music.load(os.path.join(dir_path, mp3_files[current_index]))
pygame.mixer.music.play()

def despausar():
    pygame.mixer.music.unpause()

def pausar():
    pygame.mixer.music.pause()        

def proxima_musica():
    global current_index
    if mp3_files:
        current_index = (current_index + 1) % len(mp3_files)
        pygame.mixer.music.load(os.path.join(dir_path, mp3_files[current_index]))
        pygame.mixer.music.play()


def musica_anterior():
    global current_index
    if mp3_files:
        pygame.mixer.music.load(os.path.join(dir_path, mp3_files[current_index - 1]))
        pygame.mixer.music.play()
        current_index = (current_index - 1) % len(mp3_files)

button_style = {
    "font": ("Helvetica", 8, "bold"),
    "bg": "white",
    "fg": "black",
    "activebackground": "gainsboro",
    "activeforeground": "black",
    "width": 15,
    "bd": 5
}

botao_proxima_musica = tk.Button(root, text="Próxima música", command=proxima_musica, **button_style)
botao_proxima_musica.pack(pady=10)

botao_musica_anterior = tk.Button(root, text="Música anterior", command=musica_anterior, **button_style)
botao_musica_anterior.pack(pady=10)

botao_de_pause = tk.Button(root, text="Pausar música", command=pausar, **button_style)
botao_de_pause.pack(pady=10)


botao_de_despause = tk.Button(root, text="Despausar música", command=despausar, **button_style)
botao_de_despause.pack(pady=10)

root.mainloop()