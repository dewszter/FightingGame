import pygame
from ItemClasses import Armor
#Class for the Iron armor sprite, which is a subclass to armor
class IronArmor(Armor, pygame.sprite.Sprite):
    def __init__(self, defense, weight, price, imgFile, itemGone):
        super().__init__(defense, weight, price, imgFile, itemGone)
        super(IronArmor, self)
        self.surf = pygame.image.load(imgFile).convert()
        self.surf.set_colorkey((246, 246, 246))
        self.rect = self.surf.get_rect().center
        
#Class for the Leather armor sprite, which is a subclass to armor
class LeatherArmor(Armor, pygame.sprite.Sprite):
    def __init__(self, defense, weight, price, imgFile, itemGone):
        super().__init__(defense, weight, price, imgFile, itemGone)
        super(LeatherArmor, self)
        self.surf = pygame.image.load(imgFile).convert()
        self.surf.set_colorkey((242, 242, 242))
        self.rect = self.surf.get_rect().center
        