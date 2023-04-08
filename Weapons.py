import pygame
from ItemClasses import *


class IronSword(Weapon, pygame.sprite.Sprite):
    def __init__(self, damage, weight, price):
        super().__init__(damage, weight, price)
        super(IronSword, self)
        self.surf = pygame.image.load("ironSword.png").convert()
        self.surf.set_colorkey((0, 0, 0))
        self.rect = self.surf.get_rect()
        
    