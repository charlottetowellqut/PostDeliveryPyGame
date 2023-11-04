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
        
        
        self.bottom_collision_mask = CollisionMask(self, "bottom")
        self.top_collision_mask = CollisionMask(self, "top")
        self.left_collision_mask = CollisionMask(self, "left")
        self.right_collision_mask = CollisionMask(self, "right")

        
    def Show(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))
        
        
    def update_collision_masks(self):
        self.bottom_collision_mask.update(self)
        self.top_collision_mask.update(self)
        self.left_collision_mask.update(self)
        self.right_collision_mask.update(self)
        
        
    def move(self):
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
        self.update_collision_masks()
            
    def walkHorizontal(self, vel):
        newX = self.rect.x + vel
        if not (newX < 0 or newX > (self.backGroundSize[0] - self.rect.width)): #cant walk off edge
            self.rect.x += vel
            if vel > 0: #walk right
                pass
            else: walk left
                #walk left animation
                pass
            #set sprite back to looking straight
    
    def walkVertical(self, vel):
        #check bottom collision
        bottomPlatformCollision = len(pygame.sprite.spritecollide(self.bottom_collision_mask, self.floortiles, False)) > 0        
        #move if valid
        if (bottomPlatformCollision and vel > 0) or (not bottomPlatformCollision and vel < 0):
            self.rect.y -= vel
            
    def Gravity(self, gravity):
        self.walkVertical(gravity)