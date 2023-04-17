import pygame 

class Shopkeeper(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super(Shopkeeper, self).__init__()
        self.surf = pygame.image.load("tem.png").convert()
        self.surf.set_colorkey((255, 255, 255))
        self.rect = self.surf.get_rect()