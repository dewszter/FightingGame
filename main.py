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

weight = 0
currEnemy = 4



mode = "fight"

items = []
itemsInShop = []
itemsOwned= []


dirname = os.path.dirname(__file__)
path = os.path.join(dirname, 'Images\\')

items.append(IronSword(8, 10, 25, path + "ironSword.png", False))

items.append(LeatherArmor(20, 8, 25, path + "leatherArmor.png", False))
items.append(IronArmor(28, 30, 35, path + "ironArmor.png", False))

items.append(WeakHealingPotion(2, 4, 30, path + "healingPotion.png", False))
items.append(StrenghtPotion(4, 4, 10, path + "strenghtPotion.png", False))



player = Player(200, 0, 50, path + "megaman.png")
shopKeeper = Shopkeeper(path + "tem.png")
enemyImgFiles = ["donkeykong.png", "mario.png", "pacmanGhost.png", "pacman.png"]
enemies = []

#Create 100 enemies
for i in range(100):
   enemyImgFiles.append(("mario.png"))
   enemies.append(Enemy(150 + i*10, path + enemyImgFiles[i]))



running = True
while running:
    
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
        for i in range(5):
            pygame.draw.rect(screen, (0,0,0), (50 + i*75,650,73,75), 2)
            if len(itemsOwned) > i:
                screen.blit(itemsOwned[i].surf, (50 + i*75, 650))
            
    def Click(mouseX, mouseY):
        global weight
        global currEnemy
        global mode
            #This runs when the player clicks an item in the shop, if they have enough gold, and if they don't own the item
        for i in range(3):            
            if mouseX > 500 + i*75 and mouseX < 500 + (i+1)*75 and mouseY > 525 and mouseY < 600 and player.gold >= itemsInShop[i].price and itemsInShop[i].itemGone == False and mode == "shop":
                itemsOwned.append(itemsInShop[i])
                player.ChangeGold(-itemsInShop[i].price)
                itemsInShop[i].itemGone = True
                
                #Updates the weight once everytime a new item is bought
                weight += itemsInShop[i].weight
                    
        #If the user clicks the continue button, exit the shop and move on to the next enemy
        if mouseX > 525 and mouseX < 675 and mouseY > 725 and mouseY < 775:
            currEnemy += 1
            mode = "fight"
    
        
                
                
    
    # Fill the background with white, draw the healthbars and the character sprites
    def DrawFight():
        global timer
        
        screen.fill((255,255,255))
        DrawText("SCORE: " + str(player.score), (0,0,0), (100,50), 32)
        DrawText("GOLD: " + str(player.gold), (255,211,0), (100,200), 32)
        DrawText("WEIGHT: " + str(weight), (0,0,0), (50,750), 24)
        DrawInventory()
        DrawPlayerHB()
        DrawEnemyHB()
        screen.blit(player.surf, (100,450))
        screen.blit(enemies[currEnemy].surf, (600,400))
        
        

    def DrawShop():
        screen.fill((255,255,255))
        DrawText("SCORE: " + str(player.score), (0,0,0), (100,50), 32)
        DrawText("GOLD: " + str(player.gold), (255,211,0), (100,200), 32)
        DrawText("WEIGHT: " + str(weight) + "/50", (0,0,0), (50,750), 24)
        DrawText("CONTINUE", (0,0,0), (537.5, 737.5), 24)
        pygame.draw.rect(screen, (0,0,0), (525,725,150,50), 4)
        DrawInventory()
        DrawPlayerHB()
        screen.blit(player.surf, (100,450))
        screen.blit(shopKeeper.surf, (550, 400))
        
        for i in range(3):
            if itemsInShop[i].itemGone == False:
                screen.blit(itemsInShop[i].surf, (500 + i*75, 525))
            else:
                pygame.draw.rect(screen, (255,255,255), (500 + i*75, 525, 75,75))
            
            DrawText("Price: " + str(itemsInShop[i].price), (0,0,0),  (500 + i*75, 600), 12)
            if isinstance(itemsInShop[i], Weapon) == True:
                DrawText("Damage: " + str(itemsInShop[i].damage), (0,0,0),  (500 + i*75, 625), 12)
            elif isinstance(itemsInShop[i], Armor) == True:
                DrawText("Defense: " + str(itemsInShop[i].defense), (0,0,0),  (500 + i*75, 625), 12)
            elif isinstance(itemsInShop[i], Potion) == True:
                DrawText("Potion-", (0,0,0),  (500 + i*75, 625), 12)
                DrawText("Strenght: " + str(itemsInShop[i].pStrenght), (0,0,0),  (500 + i*75, 650), 12)
            DrawText("Weight: " + str(itemsInShop[i].weight), (0,0,0),  (500 + i*75, 675), 12)
        
    def CalcDamage():
        extraDamage = 0
        for i in itemsOwned:
            if isinstance(i, Weapon) == True:
                extraDamage += i.damage
            elif isinstance(i, StrenghtPotion) == True:
                extraDamage += i.pStrenght
        return extraDamage
    
    def CalcDefense():
        reducedDamage = 0
        for i in itemsOwned:
            if isinstance(i, Armor) == True:
                reducedDamage += i.defense
            reducedDamage = reducedDamage//5
        return reducedDamage
            
    #Check for events
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            keysPressed = pygame.key.get_pressed()  
            
            #When the player presses W, deal damage to the enemy.
            if keysPressed[pygame.K_w]:
                extraDamage = CalcDamage()
                enemies[currEnemy].TakeDamage(extraDamage)
           
        if event.type == pygame.MOUSEBUTTONUP:
            mouseX = pygame.mouse.get_pos()[0]
            mouseY = pygame.mouse.get_pos()[1]
            
            Click(mouseX, mouseY)
            
                       
        # Did the user click the window close button or die?
        if event.type == pygame.QUIT or player.hp <= 0:
            running = False
    
    #The enemy attacks once every second while the fight is active
    time = round((pygame.time.get_ticks())/1000)
    reducedDamage = CalcDefense()
    if time - timer >=  0:
        if mode == "fight":
            player.TakeDamage(reducedDamage)
        timer += 1

    #If an enemy dies, give the player gold and score, and swap to the next enemy.
    if enemies[currEnemy].hp <= 0:
        player.ChangeGold(10 + currEnemy * randint(2, 5))
        player.AddScore()
        currEnemy += 1
        for i in itemsOwned:
            if isinstance(i, WeakHealingPotion):
                player.TakeDamage(25)
    
    #After every fourth enemy, select three different random items, that are not in inventory to show in the shop and enter shop mode
    if  currEnemy %4 == 0 and currEnemy > 0 and mode == "fight":
            itemsInShop = []
            
            while len(itemsInShop) < 3:
                itemRand = items[randint(0,(len(items)-1))]
                if itemRand not in itemsInShop and itemRand not in itemsOwned:
                    itemsInShop.append(itemRand)
            mode = "shop"
    
        
    #if player.hp <=0: mode = "dead"
    
    
    if mode == "fight":
        DrawFight()
    elif mode == "shop":
        DrawShop()
    #elif mode == "dead":
        #DrawDeath()
    #elif mode == "start":
        #DrawStart()
             
        
    
    
    pygame.display.flip()
    clock.tick(60)
    # Uppdate frame with 60 frames per second.

pygame.quit()