import pygame
from ItemClasses import Weapon


class IronSword(Weapon, pygame.sprite.Sprite):
    def __init__(self, damage, weight, price, imgFile, itemGone):
        super().__init__(damage, weight, price, imgFile, itemGone)
        super(IronSword, self)
        self.surf = pygame.image.load(imgFile).convert()
        self.surf.set_colorkey((0, 0, 0))
        self.rect = self.surf.get_rect().center
        
    