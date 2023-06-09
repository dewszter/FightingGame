import pygame
from ItemClasses import Potion
#Class for the Weak healing potion sprite, which is a subclass to potion
class WeakHealingPotion(Potion, pygame.sprite.Sprite):
    def __init__(self, pStrenght, weight, price, imgFile, itemGone):
        super().__init__(pStrenght, weight, price, imgFile, itemGone)
        super(WeakHealingPotion, self)
        self.surf = pygame.image.load(imgFile).convert()
        self.surf.set_colorkey((255, 255, 255))
        self.rect = self.surf.get_rect().center
        
        
#Class for the Strenght potion sprite, which is a subclass to potion
class StrenghtPotion(Potion, pygame.sprite.Sprite):
    def __init__(self, pStrenght, weight, price, imgFile, itemGone):
        super().__init__(pStrenght, weight, price, imgFile, itemGone)
        super(StrenghtPotion, self)
        self.surf = pygame.image.load(imgFile).convert()
        self.surf.set_colorkey((248, 248, 248))
        self.rect = self.surf.get_rect().center
        