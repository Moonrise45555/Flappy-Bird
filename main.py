import random
import sys
import pygame as pg
import pipe_generation
from pygame.locals import *
from time import sleep
window_width = 600
window_height = 499

window = pg.display.set_mode((window_width, window_height))

pg.init()
while True:
    sleep(1)
    window.fill("white")
    pg.draw.circle(window,"black",pg.Vector2(10,10),10)
    pg.display.flip()





