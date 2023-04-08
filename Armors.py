import pygame
from ItemClasses import *

class IronArmor(Armor, pygame.sprite.Sprite):
    def __init__(self, defense, weight, price):
        super().__init__(defense, weight, price)
        super(IronArmor, self)
        self.surf = pygame.image.load("ironArmor.png").convert()
        self.surf.set_colorkey((255, 255, 255))
        self.rect = self.surf.get_rect()
        

class BadArmor(Armor, pygame.sprite.Sprite):
    def __init__(self, defense, weight, price):
        super().__init__(defense, weight, price)
        super(BadArmor, self)
        self.surf = pygame.image.load("badArmor.png").convert()
        self.surf.set_colorkey((255, 255, 255))
        self.rect = self.surf.get_rect()
        