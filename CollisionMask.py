import pygame
import os

class CollisionMask(pygame.sprite.Sprite): 
    def __init__(self, Sprite, direction): 
        super().__init__()
        self.direction = direction
        if self.direction == "bottom":
            self.image = pygame.Surface((Sprite.rect.width, 1))
            self.rect = self.image.get_rect()
            self.rect.y = Sprite.rect.y + Sprite.rect.height - 1
            self.rect.x = Sprite.rect.x
        elif self.direction == "top":
            self.image = pygame.Surface((Sprite.rect.width, 1))
            self.rect = self.image.get_rect()
            self.rect.y = Sprite.rect.y + 1
            self.rect.x = Sprite.rect.x
        elif self.direction == "left":
            self.image = pygame.Surface((1, Sprite.rect.height))
            self.rect = self.image.get_rect()
            self.rect.y = Sprite.rect.y
            self.rect.x = Sprite.rect.x - 1
        elif self.direction == "right":
            self.image = pygame.Surface((1, Sprite.rect.height))
            self.rect = self.image.get_rect()
            self.rect.y = Sprite.rect.y
            self.rect.x = Sprite.rect.x + Sprite.rect.width - 1
        
    def update(self, Sprite):
        if self.direction == "bottom":
            self.rect.y = Sprite.rect.y + Sprite.rect.height - 1
            self.rect.x = Sprite.rect.x
        elif self.direction == "top":
            self.rect.y = Sprite.rect.y + 1
            self.rect.x = Sprite.rect.x
        elif self.direction == "left":
            self.rect.y = Sprite.rect.y
            self.rect.x = Sprite.rect.x - 1
        elif self.direction == "right":
            self.rect.y = Sprite.rect.y
            self.rect.x = Sprite.rect.x + Sprite.rect.width - 1