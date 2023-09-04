import random
import sys
import pygame as pg
import pipe as pipe
import game_engine
from pygame.locals import *
from time import sleep
import flappy
window_width = 600
window_height = 499
pipes = []
window = pg.display.set_mode((window_width, window_height))
FRAMELENGTH = 1/60
pg.init()
timer = 0
Spawndelay = 180
while True:
    sleep(FRAMELENGTH)
    
    timer += 1

    
    window.fill("white")
    flappy.draw_bird(window)
    if timer == Spawndelay:
        pipes.append(pipe.generate_pipe())
        timer = 0
    pg.draw.circle(window,"black",pg.Vector2(10,10),10)
    pipe.draw_and_move_pipes(pipes,window)
    pg.display.flip()





