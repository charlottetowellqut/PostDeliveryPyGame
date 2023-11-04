import pygame
import os

class CollisionMask(pygame.sprite.Sprite): 
    def __init__(self, Sprite): 
        super().__init__()
        self.image = pygame.Surface((Sprite.rect.width, 1))
        self.rect = self.image.get_rect()
        self.rect.y = Sprite.rect.y + Sprite.rect.height - 1
        self.rect.x = Sprite.rect.x
        
    def move(self, x, y):
        self.rect.x = x
        self.rect.y = y