import random
import sys
import pygame as pg
import pipe as pipe
import game_engine
from pygame.locals import *
from time import sleep
import flappy
import screens as screens

window_width = 600
window_height = 499
pipes = []

window = pg.display.set_mode((window_width, window_height))
FRAMELENGTH = 1/60
pg.init()


pg.mixer.music.load('sound.mp3')
pg.mixer.music.play(-1,0.0)


timer = 0
Spawndelay = 180

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
     
game_state = "start_menu"

game_over = False
        
        
while True:
    for event in pg.event.get():
       if event.type == pg.QUIT:
           pg.quit()
           quit()
    if game_state == "start_menu":
       screens.draw_start_menu(window,window_height,window_width)
       keys = pg.key.get_pressed()
       if keys[pg.K_SPACE]:
           pipes = []
           timer = 0
           game_state = "game"
           game_over = False
    elif game_state == "game_over":
       pipe.score = 0
       screens.draw_game_over_screen(window,window_height,window_width)
       keys = pg.key.get_pressed()
       if keys[pg.K_r]:
           game_state = "start_menu"
       if keys[pg.K_q]:
           pg.quit()
           quit()
  
    elif game_state == "game":
        sleep(FRAMELENGTH)
        
        window.fill("white")
        flappy.draw_bird(window)
    
        if timer == Spawndelay:
            pipes.append(pipe.generate_pipe())
            timer = 0
        pipe.draw_and_move_pipes(pipes,window)
        my_font = pg.font.SysFont('Monospace', 30)
        text_surface = my_font.render(str(pipe.score), False, (220, 0, 0))
        window.blit(text_surface, (300,0))
        
        pg.display.flip()
        timer += 1

        #collision code
        for pair in pipes:
            for pipea in pair:
                if inside(flappy.position,pipea.topleft,pipea.bottomright):
                    game_over = True
                    game_state = "game_over"
        for pair in pipes:
            for pipea in pair:
                if inside(pg.Vector2(flappy.position.x + flappy.side_length,flappy.position.y + flappy.side_length),pipea.topleft,pipea.bottomright):
                    game_over = True
                    game_state = "game_over"
        for pair in pipes:
            for pipea in pair:
                if inside(pg.Vector2(flappy.position.x + flappy.side_length,flappy.position.y),pipea.topleft,pipea.bottomright):
                    game_over = True
                    game_state = "game_over"
        for pair in pipes:
            for pipea in pair:
                if inside(pg.Vector2(flappy.position.x,flappy.position.y + flappy.side_length),pipea.topleft,pipea.bottomright):
                    game_over = True
                    game_state = "game_over"
        #collision code
        
        """window.fill("white")
        flappy.draw_bird(window)
    
        if timer == Spawndelay:
            pipes.append(pipe.generate_pipe())
            timer = 0
        
        pipe.draw_and_move_pipes(pipes,window)
        pg.display.flip()"""





