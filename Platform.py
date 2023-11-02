import pygame
import os

class Platform(pygame.sprite.Sprite): 
    
    def __init__(self, imagefile, x, y): 
        super().__init__()
        self.image = pygame.image.load(os.path.join("./Media/", imagefile))
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x