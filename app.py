import pygame
import PIL
import time
pygame.init()

from PIL import Image


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