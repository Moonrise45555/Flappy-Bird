import random
import sys
import pygame as pg
from pygame.locals import *


class rectangle():
    colour = "black"
    topleft = pg.Vector2(0,0)
    bottomright = pg.Vector2(1,1)
    def __init__(self,bottomright,topleft,col="black"):
        self.bottomright = bottomright
        self.topleft = topleft
        self.colour = col


class game_object():
    position = pg.Vector2(0,0)
    sprites = []
    def __init__(self,pos,rectangles):
        self.sprites = rectangles
        self.position = pos
