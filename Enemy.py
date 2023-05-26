import pygame

#A class for the enemies, with attributes hp and image file name.
class Enemy(pygame.sprite.Sprite):
    def __init__(self, hp, imgFile):
        super(Enemy, self).__init__()
        self.maxHp = hp
        self.hp = hp
        self.surf = pygame.image.load(imgFile).convert()
        self.surf.set_colorkey((255, 255, 255))
        self.rect = self.surf.get_rect()
        
    #Reduce the hp of the enemy, happens everytime the player attacks, with increased damage from the players items.    
    def TakeDamage(self, extraDamage):
        self.hp -= (5 + extraDamage)
    
    #Get hp
    def GetHp(self):
        return self.hp
    #Get maxHp
    def GetMaxHp(self):
        return self.maxHp
    