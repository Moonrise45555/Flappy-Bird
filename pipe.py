import random
import game_engine
import pygame as pg
def generate_pipe():
    color = "black"
    hole_height = 100
    pos = pg.Vector2(550,0)
    top_pipe_height = random.randint(25,499-hole_height -25)
    bottom_pipe_height = 499 - top_pipe_height - hole_height
    pipe_width = 50
    bottom_rectangle = pg.Rect(pg.Vector2(pos.x + 0,0),pg.Vector2(pipe_width,bottom_pipe_height))
    top_rectangle = pg.Rect(pg.Vector2(pos.x + 0,bottom_pipe_height + hole_height),pg.Vector2( pipe_width,top_pipe_height))
    
    return [top_rectangle,bottom_rectangle]
    
score = 0
def draw_and_move_pipes(pipes,screen):
    global score
    pg.font.init()
    for i in pipes:
        for pipe in i:
            pg.draw.rect(screen,"black",pipe)
            pipe.topleft = (pipe.topleft[0] - 1,pipe.topleft[1])
            pipe.bottomright = (pipe.bottomright[0] - 1,pipe.bottomright[1])
            

        if pipe.bottomright[0] < 0:
                score += 1
                my_font = pg.font.SysFont('Monospace', 30)
                text_surface = my_font.render(str(score), False, (220, 0, 0))
                screen.blit(text_surface, (300,0))

                del pipes[0]
                
            