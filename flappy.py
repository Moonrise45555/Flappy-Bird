import pygame as pg
position = pg.Vector2(30,250)
side_length = 30
speed = 0
acceleration = 0.2



def draw_bird(screen):
    global side_length
    global position
    global acceleration
    
    global speed
    
    events = pg.event.get()
    for event in events:
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_UP:

                speed = -4
        if event.type == pg.QUIT:
            pg.quit()
   
    speed += acceleration
    position.y += speed
    if position.y > 499 - side_length or position.y < 0:
        speed = 0
        position.y = 0 if position.y < 0 else 499 - side_length


    pg.draw.rect(screen,"red",pg.Rect(position,pg.Vector2(side_length,side_length)))