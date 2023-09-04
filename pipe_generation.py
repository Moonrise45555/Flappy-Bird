import random
import game_engine
import pygame as pg
def generate_pipe():
    color = "black"
    hole_height = 50
    pos = pg.Vector2(400,0)
    top_pipe_height = random.randint(25,499-hole_height -25)
    bottom_pipe_height = 499 - top_pipe_height - hole_height
    pipe_width = 50
    bottom_rectangle = pg.Rect(pg.Vector2(pos.x + 0,0),pg.Vector2(pipe_width,bottom_pipe_height))
    top_rectangle = pg.Rect(pg.Vector2(pos.x + 0,bottom_pipe_height + hole_height),pg.Vector2( pipe_width,top_pipe_height))
    return [top_rectangle,bottom_rectangle]
