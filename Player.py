import pygame
import os

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
        
        self.create_bottom_mask()

        
    def Show(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))
        
    def create_bottom_mask(self):
        # Get the bottom row of pixels from the sprite's rect
        bottom_row = self.image.subsurface(pygame.Rect(0, self.rect.height - 1, self.rect.width, 1))
        bottom_mask = pygame.mask.from_surface(bottom_row)

        self.bottom_collision_mask = bottom_mask
        
        
    def handleInput(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.walkHorizontal(-1*self.vel)
        if keys[pygame.K_RIGHT]:
            self.walkHorizontal(self.vel)
        if keys[pygame.K_UP]:
            self.walkVertical(-1*self.vel)
        #if keys[pygame.K_DOWN]:
        #    self.walkVertical(self.vel)
            
            #to-do next
            # set a floor
            # set gravity
            # set jumping
            
    def walkHorizontal(self, vel):
        newX = self.rect.x + vel
        if not (newX < 0 or newX > (self.backGroundSize[0] - self.rect.width)): #cant walk off edge
            self.rect.x += vel
            if vel > 0:
                #walk right animation
                pass
            else:
                #walk left animation
                pass
            #set sprite back to looking straight
    
    def walkVertical(self, vel):
        #if vel > 0:
        #    bottomPlatformCollision = pygame.sprite.spritecollide(self.bottom_collision_mask, self.floortiles, False)
        #    if bottomPlatformCollision and vel > 0:
        #        vel = 0
        self.rect.y += vel
        self.create_bottom_mask()