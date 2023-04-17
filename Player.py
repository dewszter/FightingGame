import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, hp, score, gold):
        super(Player, self).__init__()
        self.maxHp = hp
        self.hp = hp
        self.score = score
        self.gold = gold
        self.surf = pygame.image.load("megaman.png").convert()
        self.surf.set_colorkey((255, 255, 255))
        self.rect = self.surf.get_rect()
        
        
    def TakeDamage(self):
        self.hp -= 5 #enemydamagemultiplier
        
    def AddGold(self, addedGold):
        self.gold += addedGold
    
    def AddScore(self):
        self.score += 100
    