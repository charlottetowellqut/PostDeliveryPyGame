import pygame
import os

# Sprite Class
class Sprite(pygame.sprite.Sprite): 
    def __init__(self, imagefile, x, y, vel, backGroundSize): 
        super().__init__()
        self.x = x #x position
        self.y = y #y position
        self.backGroundSize = backGroundSize
        self.vel = vel
        self.shape = pygame.image.load(os.path.join("./Media/", imagefile))
        
    def Show(self, surface):
        surface.blit(self.shape, (self.x, self.y))
        
    def handleInput(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.walkHorizontal(-1*self.vel)
        if keys[pygame.K_RIGHT]:
            self.walkHorizontal(self.vel)
        if keys[pygame.K_UP]:
            self.walkVertical(-1*self.vel)
        if keys[pygame.K_DOWN]:
            self.walkVertical(self.vel)
            
    def walkHorizontal(self, vel):
        newX = self.x + vel
        if not (newX < 0 or newX > (self.backGroundSize[0] - self.shape.get_width())): #cant walk of edge
            self.x += vel
            if vel > 0:
                #walk right
                pass
            else:
                #walk left:
                pass
            #set sprite back to looking straight
    
    def walkVertical(self, vel):
        newY = self.y + vel
        if not (newY < 0 or newY > self.backGroundSize[1]-self.shape.get_height()):
            self.y += vel
            if vel > 0:
                #walk down
                pass
            else:
                #walk up
                pass
            #set sprite back to looking straight