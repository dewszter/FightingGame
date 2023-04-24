import pygame
from ItemClasses import Potion

class WeakHealingPotion(Potion, pygame.sprite.Sprite):
    def __init__(self, pStrenght, weight, price, imgFile):
        super().__init__(pStrenght, weight, price, imgFile)
        super(WeakHealingPotion, self)
        self.surf = pygame.image.load(imgFile).convert()
        self.surf.set_colorkey((255, 255, 255))
        self.rect = self.surf.get_rect().center
        
class StrenghtPotion(Potion, pygame.sprite.Sprite):
    def __init__(self, pStrenght, weight, price, imgFile):
        super().__init__(pStrenght, weight, price, imgFile)
        super(StrenghtPotion, self)
        self.surf = pygame.image.load(imgFile).convert()
        self.surf.set_colorkey((248, 248, 248))
        self.rect = self.surf.get_rect().center
        