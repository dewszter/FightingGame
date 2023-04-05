import pygame
from Player import Player
from Enemy import Enemy


pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode([800, 800])
timer = 1
shop = False




player = Player(192)
enemyImgFiles = ["donkeykong.png", "mario.png", "pacmanGhost.png", "pacman.png"]
enemies = []

for i in range(10):
    enemyImgFiles.append("mario.png")
    enemies.append(Enemy(192 + i*20, enemyImgFiles[i]))

currEnemy = 0

running = True
while running:

    def DrawBlueHB():
        
        pygame.draw.rect(screen, (0,0,0), (100,100,(player.maxHp + 8),50), 4)
        pygame.draw.rect(screen, (0,0,255), (104,104,player.hp,42))
        
        
        
    def DrawRedHB():
        
        pygame.draw.rect(screen, (0,0,0), (500,100,(enemies[currEnemy].maxHp + 8),50), 4)
        pygame.draw.rect(screen, (255,0,0), (504,104,enemies[currEnemy].hp,42))
    
    # Fill the background with white, draw the healthbars and the sprites
    def DrawFight():
        
        screen.fill((255,255,255))
        DrawBlueHB()
        DrawRedHB()
        screen.blit(player.surf, (100,450))
        screen.blit(enemies[currEnemy].surf, (600,400))
        
        if time - timer >=  0:
            player.TakeDamage()
            timer += 1

    def DrawShop():
        screen.fill((255,255,255))
        DrawBlueHB()
        screen.blit(player.surf, (100,450))
        

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            keysPressed = pygame.key.get_pressed()  
            
            if keysPressed[pygame.K_w]:
                enemies[currEnemy].TakeDamage()
           
            
                       
        # Did the user click the window close button?
        if event.type == pygame.QUIT or player.hp <= 0:
            running = False
    
    time = round((pygame.time.get_ticks())/1000)
    
    if shop == False:
        DrawFight()
    else:
        DrawShop()

    #The enemy attacks once every second
    
       
    if enemies[currEnemy].hp <= 0:
        
        #if currEnemy%4 == 0:
            #shop
        currEnemy += 1
    
    pygame.display.flip()
    clock.tick(60)
    # Uppdate frame

pygame.quit()