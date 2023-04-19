import pygame
from ItemClasses import Potion

class HealingPotion(Potion, pygame.sprite.Sprite):
    def __init__(self, pStrenght, weight, price):
        super().__init__(pStrenght, weight, price)
        super(HealingPotion, self)
        self.surf = pygame.image.load(".png").convert()
        self.surf.set_colorkey((0, 0, 0))
        self.rect = self.surf.get_rect()
        