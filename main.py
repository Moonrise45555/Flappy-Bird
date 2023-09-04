import random
import sys
import pygame as pg
import pipe_generation as pipe
import game_engine
from pygame.locals import *
from time import sleep
window_width = 600
window_height = 499

window = pg.display.set_mode((window_width, window_height))

pg.init()
while True:
    sleep(0.5)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
    window.fill("white")
    pg.draw.circle(window,"black",pg.Vector2(10,10),10)
    game_engine.draw_pipe(pipe.generate_pipe(),window)
    pg.display.flip()





