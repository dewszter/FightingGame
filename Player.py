import pygame
from random import randint

class Player(pygame.sprite.Sprite):
    def __init__(self, hp):
        super(Player, self).__init__()
        self.maxHp = hp
        self.hp = hp
        self.surf = pygame.image.load("megaman.png").convert()
        self.surf.set_colorkey((255, 255, 255))
        self.rect = self.surf.get_rect()
        
        
    def TakeDamage(self):
        self.hp -= 5 #enemydamagemultiplier
    