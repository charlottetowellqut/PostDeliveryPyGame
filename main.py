import pygame
import os
from Player import Player
from Platform import Platform

#init game
pygame.init()

#game clock
clock = pygame.time.Clock()

#game screen - full screen
screen_info = pygame.display.Info()
#screenwidth,screenheight = screen_info.current_w,screen_info.current_h-50 #-50 for top window bar

#multiple of 50 - all tiles in this game are 50x50 squares
screenwidth = 1250
screenheight = 650
backGroundSize = (screenwidth, screenheight)
screen = pygame.display.set_mode(backGroundSize)


bg = pygame.image.load(os.path.join("./Media/", "clouds.png"))

allSprites = pygame.sprite.Group()

#set grass tile floor across length of bg
floortiles = pygame.sprite.Group()
tilewidth = 50
y = screenheight - tilewidth
for i in range( int(screenwidth / tilewidth) + 1 ):
    x = (i-1)*tilewidth
    grassTile = Platform("grasstile.png", x, y)
    floortiles.add(grassTile)
    allSprites.add(grassTile)


pygame.mouse.set_visible(0)
pygame.display.set_caption('Little Game')

vel = 2 #velocity
gravity = -10 #gravity strength

Postie = Player("sprite1.png", 50, y-100, vel, backGroundSize, floortiles)
allSprites.add(Postie)

run = True
while run:
    screen.blit(bg, (0, 0)) #draws bg image at initial coordinates
    floortiles.draw(screen)
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    Postie.handleInput()  
    Postie.Gravity(gravity)
    Postie.Show(screen)

    pygame.display.update()
    
pygame.quit()