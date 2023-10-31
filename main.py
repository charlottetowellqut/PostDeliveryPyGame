import pygame
import sys
import os
from Sprite import Sprite

#init game
pygame.init()

#game clock
clock = pygame.time.Clock()

#game screen
screenheight = 640
screenwidth = 576
backGroundSize = (screenheight, screenwidth)
screen = pygame.display.set_mode(backGroundSize)# Load the background image here. Make sure the file exists!
bg = pygame.image.load(os.path.join("./Media/", "Background2.png"))

pygame.mouse.set_visible(0)
pygame.display.set_caption('Little Game')
vel = 2 #velocity
Postie = Sprite("sprite1.png", 311, 261, vel, backGroundSize)

run = True
while run:
    screen.blit(bg, (0, 0)) #draws bg image at initial coordinates
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    Postie.handleInput()    
    Postie.Show(screen)

    pygame.display.update()
    
pygame.quit()