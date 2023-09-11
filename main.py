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

game_over = False
def Game_over():
    print("game over")
    pg.quit()
from copy import deepcopy

def pipes_to_holes(pipes):
    holes = []
    for pair in pipes:
        #top left of hole is defined by x1 and y1
        x1 = pair[0].topleft[0]
        y1 = pair[0].bottomright[1]
        #bottom right of the hole is defined bz x2 and y2
        x2 = pair[1].bottomright[0]
        y2 = pair[1].topleft[1]
        holes.append([[x1,y1],[x2,y2]])
    return deepcopy(holes)
    
def inside(candidate,topleft,bottomright):
    
    if candidate.x > topleft[0] and candidate.x < bottomright[0]:
        
        if candidate.y > topleft[1] and candidate.y < bottomright[1]:
            
            return True
    return False
     

        
        
while game_over == False:
    
    sleep(FRAMELENGTH)
    
    timer += 1
    #collision ocde
    for pair in pipes:
        for pipea in pair:
            if inside(flappy.position,pipea.topleft,pipea.bottomright):
                game_over = True
    for pair in pipes:
        for pipea in pair:
            if inside(pg.Vector2(flappy.position.x + flappy.side_length,flappy.position.y + flappy.side_length),pipea.topleft,pipea.bottomright):
                game_over = True
    for pair in pipes:
        for pipea in pair:
            if inside(pg.Vector2(flappy.position.x + flappy.side_length,flappy.position.y),pipea.topleft,pipea.bottomright):
                game_over = True
    for pair in pipes:
        for pipea in pair:
            if inside(pg.Vector2(flappy.position.x,flappy.position.y + flappy.side_length),pipea.topleft,pipea.bottomright):
                game_over = True





    #collision code
    
    window.fill("white")
    flappy.draw_bird(window)
   
    if timer == Spawndelay:
        pipes.append(pipe.generate_pipe())
        timer = 0
    
    pipe.draw_and_move_pipes(pipes,window)
    pg.display.flip()





