import pygame


class Enemy(pygame.sprite.Sprite):
    def __init__(self, hp, imgFile):
        super(Enemy, self).__init__()
        self.maxHp = hp
        self.hp = hp
        self.surf = pygame.image.load(imgFile).convert()
        self.surf.set_colorkey((255, 255, 255))
        self.rect = self.surf.get_rect()
        
        
    def TakeDamage(self):
        self.hp -= 5 #playerdamagemultiplier