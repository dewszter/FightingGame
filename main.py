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
screen = pygame.display.set_mode([800, 800])
clock = pygame.time.Clock()
timer = 1





mode = "fight"

items = []
itemsInShop = []
#itemsInInventory = []

dirname = os.path.dirname(__file__)
path = os.path.join(dirname, 'Images\\')

items.append(IronSword(8, 9, 25, path + "ironSword.png"))

items.append(LeatherArmor(21, 8, 25, path + "leatherArmor.png"))
items.append(IronArmor(25, 30, 25, path + "ironArmor.png" ))

items.append(WeakHealingPotion(5, 4, 30, path + "healingPotion.png"))
items.append(StrenghtPotion(10, 4, 10, path + "strenghtPotion.png"))



player = Player(200, 0, 0, path + "megaman.png")
shopKeeper = Shopkeeper(path + "tem.png")
enemyImgFiles = ["donkeykong.png", "mario.png", "pacmanGhost.png", "pacman.png"]
enemies = []

for i in range(20):
   enemyImgFiles.append(("mario.png"))
   enemies.append(Enemy(150 + i*10, path + enemyImgFiles[i]))

currEnemy = 4


running = True
while running:
    time = round((pygame.time.get_ticks())/1000)
    
    def DrawText(content, color, pos, size):
        font = pygame.font.Font('freesansbold.ttf', size)
        text = font.render(content, True, color, (255,255,255))
        textRect = text.get_rect()
        textRect = pos
        
        screen.blit(text,textRect)
    

    def DrawPlayerHB():
        
        pygame.draw.rect(screen, (0,0,0), (100,100,player.maxHp,50), 4)
        pygame.draw.rect(screen, (0,0,255), (104,104,(player.hp -8),42))  
        
        
    def DrawEnemyHB():
        
        pygame.draw.rect(screen, (0,0,0), (500,100,enemies[currEnemy].maxHp,50), 4)
        pygame.draw.rect(screen, (255,0,0), (504,104,(enemies[currEnemy].hp - 8),42))
        
    def DrawInventory():
        for n in range(8):
            pygame.draw.rect(screen, (0,0,0), (50 + n*50,650,48,50), 2)
        
        #add items in inventory
    
    # Fill the background with white, draw the healthbars and the character sprites
    def DrawFight():
        global timer
        
        screen.fill((255,255,255))
        DrawText("SCORE: " + str(player.score), (0,0,0), (100,50), 32)
        DrawText("GOLD: " + str(player.gold), (255,211,0), (100,200), 32)
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
        DrawText("SCORE: " + str(player.score), (0,0,0), (100,50), 32)
        DrawText("GOLD: " + str(player.gold), (255,211,0), (100,200), 32)
        DrawInventory()
        DrawPlayerHB()
        screen.blit(player.surf, (100,450))
        screen.blit(shopKeeper.surf, (550, 400))
        
        for i in range(len(itemsInShop)):
            screen.blit(itemsInShop[i].surf, (500 + i*75, 525))
            
            DrawText("Price: " + str(itemsInShop[i].price), (0,0,0),  (500 + i*75, 600), 12)
            if isinstance(itemsInShop[i], Weapon) == True:
                DrawText("Damage: " + str(itemsInShop[i].damage), (0,0,0),  (500 + i*75, 625), 12)
            elif isinstance(itemsInShop[i], Armor) == True:
                DrawText("Defense: " + str(itemsInShop[i].defense), (0,0,0),  (500 + i*75, 625), 12)
            elif isinstance(itemsInShop[i], Potion) == True:
                DrawText("Potion-", (0,0,0),  (500 + i*75, 625), 12)
                DrawText("Strenght: " + str(itemsInShop[i].pStrenght), (0,0,0),  (500 + i*75, 650), 12)
            DrawText("Weight: " + str(itemsInShop[i].weight), (0,0,0),  (500 + i*75, 675), 12)
        
        

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            keysPressed = pygame.key.get_pressed()  
            
            #When the player presses W, deal damage to the enemy.
            if keysPressed[pygame.K_w]:
                enemies[currEnemy].TakeDamage()
           
            
                       
        # Did the user click the window close button or die?
        if event.type == pygame.QUIT or player.hp <= 0:
            running = False
    
    #After every fourth enemy, select three random items to show in the shop and enter shop mode
    if  currEnemy %4 == 0 and currEnemy > 0 and mode != "shop":
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
    
    #If an enemy dies, give the player gold and score, and swap to the next enemy.
    if enemies[currEnemy].hp <= 0:
        player.AddGold(10 + currEnemy * randint(2, 5))
        player.AddScore()
        currEnemy += 1
        
    
    pygame.display.flip()
    clock.tick(60)
    # Uppdate frame with 60 frames per second.

pygame.quit()