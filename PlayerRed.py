import pygame
from random import randint

class PlayerRed(pygame.sprite.Sprite):
    def __init__(self, hp):
        super(PlayerRed, self).__init__()
        self.hp = hp
        self.surf = pygame.image.load("PlayerRed.png").convert()
        self.surf.set_colorkey((255, 255, 255))
        self.rect = self.surf.get_rect()
        
        
    def TakeDamage(self):
        self.hp -= randint(5, 20)