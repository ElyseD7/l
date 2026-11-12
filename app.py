import pygame
import PIL

from PIL import Image
img = Image.open("mike.jpeg")
img.show()

songs = ["thriller", "off_the_wall"]

pygame.mixer.music.load()
pygame.mixer.music.unload()
