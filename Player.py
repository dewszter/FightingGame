import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, hp, score, gold, imgFile):
        super(Player, self).__init__()
        self.maxHp = hp
        self.hp = hp
        self.score = score
        self.gold = gold
        
        #Sprite setup is similar for all sprites, select an image file, and choose a color that will become transparent
        self.surf = pygame.image.load(imgFile).convert()
        self.surf.set_colorkey((255, 255, 255))
        self.rect = self.surf.get_rect()
        
        
    def TakeDamage(self, reducedDamage):
        self.hp -= (8 - reducedDamage)
        
    def ChangeGold(self, changedGold):
        self.gold += changedGold
    
    def AddScore(self):
        self.score += 100
    
    def GetHp(self):
        return self.hp
    def GetMaxHp(self):
        return self.maxHp
    def GetScore(self):
        return self.score
    def GetGold(self):
        return self.gold
    
    