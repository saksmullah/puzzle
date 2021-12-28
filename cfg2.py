'''
Created on Mar 30, 2021

@author: martinyanev
'''
import os

SCREENSIZE = (640, 640)

song = os.path.join(os.getcwd(), 'resources/music/Ezio.mp3' ) #adding music to the game
PICTURE_ROOT_DIR = os.path.join(os.getcwd(), 'resources/pictures')

FONTPATH = os.path.join(os.getcwd(), 'resources/font/FZSTK.TTF')

BACKGROUNDCOLOR = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

FPS = 40

RANDNUM = 100