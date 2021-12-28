import os
import pygame
from pygame.locals import *




screenzize = (640, 640)
print(os.getcwd())
picture_root_dir = os.path.join(os.getcwd(), 'resources/pictures')
fontpath = os.path.join(os.getcwd(), 'resources/font/FZSTK.TTF')
marshallah_song = os.path.join(os.getcwd(), 'resources/music/Mashallah Brother!.mp3')
victory_nasheed = os.path.join(os.getcwd(), 'resources/music/Victory_nasheed.mp3')






background_colour = (255, 255, 255)
red_colour = (255, 0, 0)
blue_colour = (0, 0, 255)
black_colour = (0, 0, 0)

FPS = 40

random = 100