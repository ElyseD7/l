import pygame
import PIL
import time
pygame.init()

from PIL import Image
img = Image.open("mike.jpeg")
img.show()

def play(x):
    pygame.mixer.music.load(x)
    pygame.mixer.music.play()


songs = ["bad.mp3", "offthewall.mp3", "rockmyworld.mp3"]
for i in range(len(songs)):
    print(songs[i])
x = input('Select a song ')


play(x)
time.sleep(10)
#pygame.mixer.music.unload()
#Tkinter