import pygame 

#Class for the shopkeeper sprite, with the attribute image file name.
class Shopkeeper(pygame.sprite.Sprite):
    def __init__(self, imgFile) -> None:
        super(Shopkeeper, self).__init__()
        self.surf = pygame.image.load(imgFile).convert()
        self.surf.set_colorkey((255, 255, 255))
        self.rect = self.surf.get_rect()