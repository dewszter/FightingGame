import pygame

#Class for the player with attributes healthpoints, score, gold and image file name
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
        
    #Function for taking damage, happens everytime the enemy attacks, and when the player heals itself it inputs a
    #reduced-damage-value that is larger than 8 so that the player takes negative damage.    
    def TakeDamage(self, reducedDamage):
        self.hp -= (8 - reducedDamage)
    
    #Is able to add or remove gold to the player, happens when the player kills an enemy or buys an item.  
    def ChangeGold(self, changedGold):
        self.gold += changedGold
    
    #Adds 100 score to the player
    def AddScore(self):
        self.score += 100
    
    #Get hp
    def GetHp(self):
        return self.hp
    #Get MaxHp
    def GetMaxHp(self):
        return self.maxHp
    #Get score
    def GetScore(self):
        return self.score
    #Get gold
    def GetGold(self):
        return self.gold
    
    