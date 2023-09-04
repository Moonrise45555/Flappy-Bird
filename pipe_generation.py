import random
import game_engine
import pygame as pg
def generate_pipe():
    pos = pg.Vector2(400,0)
    bottom_pipe_height = random.randint(10,489)
    top_pipe_height = 499 - bottom_pipe_height - 25
    pipe_width = 10
    color = "black"
    
    top_rectangle = pg.Rect(pg.Vector2(0,0),pg.Vector2(10,top_pipe_height))
    bottom_rectangle = pg.Rect(pg.Vector2(0,top_pipe_height + 25),pg.Vector2(10,499))
    return game_engine.game_object(pos,[top_rectangle,bottom_rectangle])
