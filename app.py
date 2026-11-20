import pygame
import PIL
import time
import tkinter as tk
pygame.init()

from PIL import Image

import tkinter as tk

window = tk.Tk()
window.geometry("300x200")

tk.Label(window, text="MP3 Player", bg="lightblue").pack(fill="x")


window.mainloop()

button_row = tk.Frame(window)
button_row.pack(pady=10)

def play(x):
    pygame.mixer.music.load(x)
    pygame.mixer.music.play()


songs = ["bad.mp3", "offthewall.mp3", "rockmyworld.mp3"]
for i in range(len(songs)):
    print(f'{songs[i]} {i+1}')
x = int(input('Select a song '))
if x == 1:
    img = Image.open("bad.jpg")
    img.show()
    play("bad.mp3")
elif x == 2:
    img = Image.open("offthewall.jpg")
    play("offthewall.mp3")
    img.show()
elif x == 3:
    img = Image.open("j.jpeg")
    play("rockmyworld.mp3")
    img.show()



time.sleep(300)
#pygame.mixer.music.unload()
#Tkinter