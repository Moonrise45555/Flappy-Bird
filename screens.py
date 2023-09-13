import pygame as pg

def draw_start_menu(screen,screen_height,screen_width):
    screen.fill("white")
    title_font = pg.font.SysFont('monospace', 40)
    start_font = pg.font.SysFont('arial', 30)
    text_font = pg.font.SysFont('calibri', 20)
    title = title_font.render('Flappy Bird', True, "red")
    start_button = start_font.render('Press Space to Start', True, "black")
    screen.blit(title, (screen_width/2 - title.get_width()/2, screen_height/2 - title.get_height()/2))
    screen.blit(start_button, (screen_width/2 - start_button.get_width()/2, screen_height/2 + start_button.get_height()/2))
    pg.display.update()

def draw_game_over_screen(screen,screen_height,screen_width):
   screen.fill("white")
   title_font = pg.font.SysFont('monospace', 40)
   instruction_font = pg.font.SysFont('arial',30)
   title = title_font.render('Game Over', True, "red")
   restart_button = instruction_font.render('R - Restart', True, "black")
   quit_button = instruction_font.render('Q - Quit', True, "black")
   screen.blit(title, (screen_width/2 - title.get_width()/2, screen_height/2 - title.get_height()/3))
   screen.blit(restart_button, (screen_width/2 - restart_button.get_width()/2, screen_height/1.9 + restart_button.get_height()))
   screen.blit(quit_button, (screen_width/2 - quit_button.get_width()/2, screen_height/2 + quit_button.get_height()/2))
   pg.display.update()