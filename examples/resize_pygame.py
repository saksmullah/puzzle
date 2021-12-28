import pygame
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((500, 500), HWSURFACE|DOUBLEBUF|RESIZABLE)
pic = pygame.image.load('../resources/pictures/surah Nas.jpg')
screen.blit(pygame.transform.scale(pic, (500, 500)), (0,0))
pygame.display.flip()

while True:
    pygame.event.pump()
    event = pygame.event.wait()
    if event.type == QUIT: pygame.display.quit()
    elif event.type == VIDEORESIZE:
        screen = pygame.display.set_mode(event.__dict__['size'], HWSURFACE|DOUBLEBUF|RESIZABLE)
        screen.blit(pygame.transform.scale(pic,event.__dict__['size']), (0,0)) #pic is the variable
        pygame.display.flip()