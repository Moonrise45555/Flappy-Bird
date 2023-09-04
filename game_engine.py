import random
import sys
import pygame as pg
from pygame.locals import *





    
def draw_pipe(sprites,screen, colour="black"):
    for i in sprites:
        pg.draw.rect(screen,"black",i)
        

