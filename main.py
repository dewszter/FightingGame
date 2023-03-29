import pygame
from Player import Player
from Enemy import Enemy


pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode([800, 800])


running = True

player = Player(192)
enemy = Enemy(192)

while running:

    def DrawBlueHB():
        
        pygame.draw.rect(screen, (0,0,0), (100,100,200,50), 4)
        pygame.draw.rect(screen, (0,0,255), (104,104,player.hp,42))
        
        
        
    def DrawRedHB():
        
        pygame.draw.rect(screen, (0,0,0), (500,100,200,50), 4)
        pygame.draw.rect(screen, (255,0,0), (504,104,enemy.hp,42))
    




    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            keysPressed = pygame.key.get_pressed()  
            
            if keysPressed[pygame.K_w]:
                enemy.TakeDamage()
           
            
                       
        # Did the user click the window close button?
        if event.type == pygame.QUIT:
            running = False
    
    time = (pygame.time.get_ticks())/1000
    
    # Fill the background with white, draw the healthbars and the sprites
    screen.fill((255,255,255))
    DrawBlueHB()
    DrawRedHB()
    screen.blit(player.surf, (100,450))
    screen.blit(enemy.surf, (600,400))
    
    print(time)
    if abs(time - round(time)) < 0.01:
       player.TakeDamage()
    
    pygame.display.flip()
    clock.tick(60)
    # Uppdate frame

pygame.quit()