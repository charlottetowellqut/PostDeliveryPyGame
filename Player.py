import pygame
import os
from CollisionMask import CollisionMask

# Player Class
class Player(pygame.sprite.Sprite): 
    def __init__(self, imagefile, x, y, vel, backGroundSize, floortiles): 
        super().__init__()
        self.image = pygame.image.load(os.path.join("./Media/", imagefile))
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
        
        self.backGroundSize = backGroundSize
        self.vel = vel #velocity
        self.floortiles = floortiles
        
        
        self.bottom_collision_mask = CollisionMask(self)

        
    def Show(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))
        
        
    def update_bottom_mask(self):
        self.bottom_collision_mask.move(self.rect.x, self.rect.y + self.rect.height - 1)
        
        
    def handleInput(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.walkHorizontal(-1*self.vel)
        if keys[pygame.K_RIGHT]:
            self.walkHorizontal(self.vel)
        if keys[pygame.K_UP]:
            print("walk vertical")
            self.walkVertical(100)
        #if keys[pygame.K_DOWN]:
        #    self.walkVertical(self.vel)
            
    def walkHorizontal(self, vel):
        newX = self.rect.x + vel
        if not (newX < 0 or newX > (self.backGroundSize[0] - self.rect.width)): #cant walk off edge
            self.rect.x += vel
            self.update_bottom_mask()
            if vel > 0:
                #walk right animation
                pass
            else:
                #walk left animation
                pass
            #set sprite back to looking straight
    
    def walkVertical(self, vel):
        bottomPlatformCollision = len(pygame.sprite.spritecollide(self.bottom_collision_mask, self.floortiles, False)) > 0
        print(f"bottom platform collision: {bottomPlatformCollision}")
        
        if (bottomPlatformCollision and vel > 0) or (not bottomPlatformCollision and vel < 0):
            self.rect.y -= vel
            self.update_bottom_mask()
            
    def Gravity(self, gravity):
        self.walkVertical(gravity)