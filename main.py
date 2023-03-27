import pygame
from PlayerBlue import PlayerBlue
from PlayerRed import PlayerRed


pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode([800, 800])

running = True

playerBlue = PlayerBlue(192)
playerRed = PlayerRed(192)

while running:

    def DrawBlueHB():
        
        pygame.draw.rect(screen, (0,0,0), (100,100,200,50), 4)
        pygame.draw.rect(screen, (0,0,255), (104,104,playerBlue.hp,42))
        
        
        
    def DrawRedHB():
        
        pygame.draw.rect(screen, (0,0,0), (500,100,200,50), 4)
        pygame.draw.rect(screen, (255,0,0), (504,104,playerRed.hp,42))
    




    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            keysPressed = pygame.key.get_pressed()  
            
            if  keysPressed[pygame.K_UP]:
                playerBlue.TakeDamage()
            if keysPressed[pygame.K_w]:
                playerRed.TakeDamage()
           
            
                       
        # Did the user click the window close button?
        if event.type == pygame.QUIT:
            running = False
    
   
    
    # Fill the background with white, draw the healthbars and the sprites
    screen.fill((255,255,255))
    DrawBlueHB()
    DrawRedHB()
    screen.blit(playerBlue.surf, (100,450))
    screen.blit(playerRed.surf, (600,400))
    
    
   
    
    pygame.display.flip()
    clock.tick(60)
    # Uppdate frame

pygame.quit()