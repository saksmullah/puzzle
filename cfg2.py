import os
import pygame

screenzize = (640, 640)
picture_root_dir = os.path.join(os.getcwd(), 'Game5_Puzzle/resources/pictures')#to acsses the folder and the picture in that folder
fontpath = os.path.join(os.getcwd(), 'Game5_Puzzle/resources/font/FZSTK.TTF')
song = os.path.join(os.getcwd(), 'Game5_Puzzle/resources/music/Ezio.mp3' )

background_colour = (255, 255, 255)
red_colour = (255, 0, 0)
blue_colour = (0, 0, 255)
black_colour = (0, 0, 0)

FPS = 40

random = 100 # to reffer to the pictures so the user dont expect what picture he is goin to see