import pygame
from Player import Player
from Enemy import Enemy
from Shopkeeper import Shopkeeper
from Weapons import *
from Armors import *
from Potions import *
from random import randint
import os


#Basic pygame setup
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode([800, 800])
timer = 1



mode = "fight"

items = []
itemsInShop = []

dirname = os.path.dirname(__file__)
path = os.path.join(dirname, 'Images\\')

items.append(IronSword(8, 9, 25, path + "ironSword.png"))

items.append(LeatherArmor(21, 8, 25, path + "leatherArmor.png"))
items.append(IronArmor(25, 30, 25, path + "ironArmor" ))

items.append(WeakHealingPotion(5, 4, 30, path + "healingPotion.png"))
items.append(StrenghtPotion(10, 4, 10, path + "strenghtPotion"))

player = Player(192, 0, 0)
shopKeeper = Shopkeeper()
enemyImgFiles = ["donkeykong.png", "mario.png", "pacmanGhost.png", "pacman.png"]
enemies = []

for i in range(20):
   enemyImgFiles.append("mario.png")
   enemies.append(Enemy(142 + i*10, enemyImgFiles[i]))

currEnemy = 4

running = True
while running:
    time = round((pygame.time.get_ticks())/1000)
    

    def DrawPlayerHB():
        
        pygame.draw.rect(screen, (0,0,0), (100,100,(player.maxHp + 8),50), 4)
        pygame.draw.rect(screen, (0,0,255), (104,104,player.hp,42))  
        
        
    def DrawEnemyHB():
        
        pygame.draw.rect(screen, (0,0,0), (500,100,(enemies[currEnemy].maxHp + 8),50), 4)
        pygame.draw.rect(screen, (255,0,0), (504,104,enemies[currEnemy].hp,42))
        
    def DrawInventory():
        for n in range(8):
            pygame.draw.rect(screen, (0,0,0), (50 + n*50,650,48,50), 2)
    
    # Fill the background with white, draw the healthbars and the character sprites
    def DrawFight():
        global timer
        
        screen.fill((255,255,255))
        DrawInventory()
        DrawPlayerHB()
        DrawEnemyHB()
        screen.blit(player.surf, (100,450))
        screen.blit(enemies[currEnemy].surf, (600,400))
        
        #The enemy attacks once every second while the fight is active
        if time - timer >=  0:
            player.TakeDamage()
            timer += 1

    def DrawShop():
        screen.fill((255,255,255))
        DrawInventory()
        DrawPlayerHB()
        screen.blit(player.surf, (100,450))
        screen.blit(shopKeeper.surf, (575, 400))
        
        for i in range(len(itemsInShop)):
            screen.blit(itemsInShop[i].surf, (550 + i*50, 525))
        
        

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            keysPressed = pygame.key.get_pressed()  
            
            if keysPressed[pygame.K_w]:
                enemies[currEnemy].TakeDamage()
           
            
                       
        # Did the user click the window close button?
        if event.type == pygame.QUIT or player.hp <= 0:
            running = False
    
    if currEnemy%4 == 0 and mode != "shop":
            itemsInShop = []
            
            while len(itemsInShop) < 3:
                itemRand = items[randint(0,(len(items)-1))]
                if itemRand not in itemsInShop:#and not in inventory
                    itemsInShop.append(itemRand)
            mode = "shop"
    
    if mode == "fight":
        DrawFight()
    elif mode == "shop":
        DrawShop()
    #elif mode == "dead":
        #DrawDeath()
    #elif mode == "start":
        #DrawStart()
             
        
    #if player.hp <=0: mode = "dead"
    
       
    if enemies[currEnemy].hp <= 0:
        player.AddGold(10 + currEnemy * randint(2, 5))
        player.AddScore()
        currEnemy += 1
        
    
    pygame.display.flip()
    clock.tick(60)
    # Uppdate frame

pygame.quit()