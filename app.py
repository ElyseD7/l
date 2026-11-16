import pygame
import PIL
import time
pygame.init()

from PIL import Image
img = Image.open("mike.jpeg")
img.show()

songs = ["thriller", "off_the_wall"]



def play(x):
    pygame.mixer.music.load(x)
    pygame.mixer.music.play()


play("offthewall.mp3")
time.sleep(10)
#pygame.mixer.music.unload()