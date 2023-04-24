import pygame
from ItemClasses import Armor

class IronArmor(Armor, pygame.sprite.Sprite):
    def __init__(self, defense, weight, price, imgFile):
        super().__init__(defense, weight, price, imgFile)
        super(IronArmor, self)
        self.surf = pygame.image.load(imgFile).convert()
        self.surf.set_colorkey((246, 246, 246))
        self.rect = self.surf.get_rect().center
        

class LeatherArmor(Armor, pygame.sprite.Sprite):
    def __init__(self, defense, weight, price, imgFile):
        super().__init__(defense, weight, price, imgFile)
        super(LeatherArmor, self)
        self.surf = pygame.image.load(imgFile).convert()
        self.surf.set_colorkey((242, 242, 242))
        self.rect = self.surf.get_rect().center
        