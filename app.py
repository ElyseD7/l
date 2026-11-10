import pygame
import PIL

from PIL import Image
img = Image.open("mike.jpeg")
img.show()

pygame.mixer.music.load()
pygame.mixer.music.unload()
