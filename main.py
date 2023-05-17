#------------------Import Classes---------------------------

import pygame
from Player import Player
from Enemy import Enemy
from Shopkeeper import Shopkeeper
from Weapons import *
from Armors import *
from Potions import *
from random import randint
import os


#------------------Basic pygame setup------------------------------------
pygame.init()
screen = pygame.display.set_mode([800, 800])
clock = pygame.time.Clock()


#------------------Other variable and list declarations---------------------------
timer = 1
weight = 0
currEnemy = 0
mode = "fight"
items = []
itemsInShop = []
itemsOwned= []
enemies = []

#------------------Create Instances---------------------------

#Create a constant, IMGS_PATH that contains the IMGS_PATH to the image folder
dirname = os.path.dirname(__file__)
IMGS_PATH = os.path.join(dirname, 'Images\\')

#Create instances of the Item superclass, with different subclasses.
items.append(IronSword(8, 10, 25, IMGS_PATH + "ironSword.png", False))

items.append(LeatherArmor(2, 8, 25, IMGS_PATH + "leatherArmor.png", False))
items.append(IronArmor(5, 30, 35, IMGS_PATH + "ironArmor.png", False))

items.append(WeakHealingPotion(2, 4, 30, IMGS_PATH + "healingPotion.png", False))
items.append(StrenghtPotion(4, 4, 10, IMGS_PATH + "strenghtPotion.png", False))


#Create instances of the Player class and Shopkeeper class
player = Player(200, 0, 0, IMGS_PATH + "megaman.png")
shopKeeper = Shopkeeper(IMGS_PATH + "tem.png")



#Create 100 instances of the Enemy class
enemyImgFiles = ["donkeykong.png", "mario.png", "pacmanGhost.png", "pacman.png"]
for i in range(100):
    #Fill the rest of enemy images with mario to make sure all enemys can be created.
   enemyImgFiles.append(("mario.png"))
   enemies.append(Enemy(150 + i*10, IMGS_PATH + enemyImgFiles[i]))



running = True
while running:
    
    #------------------------------------Functions------------------------------------------------------
    
    #Draw text at the given position with the given color and fontsize
    def DrawText(content, color, pos, size):
        font = pygame.font.Font('freesansbold.ttf', size)
        text = font.render(content, True, color, (255,255,255))
        textRect = text.get_rect()
        textRect = pos
        
        screen.blit(text,textRect)
    
    #Draw the players healthbar, the first rect is the box and the second is the fill color which changes size based on hp
    def DrawPlayerHB():
        
        pygame.draw.rect(screen, (0,0,0), (100,100,player.GetMaxHp(),50), 4)
        pygame.draw.rect(screen, (0,0,255), (104,104,(player.GetHp() -8),42))  
    
    #Draw the enemy healthbar, the first rect is the box and the second is the fill color which changes size based on hp          
    def DrawEnemyHB():
        
        pygame.draw.rect(screen, (0,0,0), (500,100,enemies[currEnemy].GetMaxHp(),50), 4)
        pygame.draw.rect(screen, (255,0,0), (504,104,(enemies[currEnemy].GetHp() - 8),42))
    
    #Draw 5 empty boxes with the same size on a horizontal line     
    def DrawInventory():
        for i in range(5):
            pygame.draw.rect(screen, (0,0,0), (50 + i*75,650,73,75), 2)
            if len(itemsOwned) > i:
                screen.blit(itemsOwned[i].surf, (50 + i*75, 650))
    
    #This runs when the mousebutton is released, with the x and y position as parameters         
    def Click(mouseX, mouseY):
        global weight
        global currEnemy
        global mode
            #This runs when the player clicks an item in the shop, if they have enough gold, and if they don't own the item
        for i in range(3):            
            if mouseX > 500 + i*75 and mouseX < 500 + (i+1)*75 and mouseY > 525 and mouseY < 600 and player.GetGold() >= itemsInShop[i].GetPrice() and itemsInShop[i].GetItemGone() == False and mode == "shop":
                itemsOwned.append(itemsInShop[i])
                player.ChangeGold(-itemsInShop[i].GetPrice())
                itemsInShop[i].SetItemGone(True)
                
                #Updates the weight once everytime a new item is bought
                weight += itemsInShop[i].GetWeight()
                
                #If the player bought a healingpotion, heal the player 50 hp
                if isinstance(itemsInShop[i], WeakHealingPotion):
                    player.TakeDamage(58)
                    
        #If the user clicks the continue button, exit the shop and move on to the next enemy
        if mouseX > 525 and mouseX < 675 and mouseY > 725 and mouseY < 775:
            currEnemy += 1
            mode = "fight"
    
        
                
                
    
    #Draw the necessary sprites and forms for the fight screen
    def DrawFight():
        global timer
        
        screen.fill((255,255,255))
        DrawText("SCORE: " + str(player.GetScore()), (0,0,0), (100,50), 32)
        DrawText("GOLD: " + str(player.GetGold()), (255,211,0), (100,200), 32)
        DrawText("WEIGHT: " + str(weight), (0,0,0), (50,750), 24)
        DrawInventory()
        DrawPlayerHB()
        DrawEnemyHB()
        screen.blit(player.surf, (100,450))
        screen.blit(enemies[currEnemy].surf, (600,400))
        
        
    #Draw the necessary sprites and forms for the shopscreen
    def DrawShop():
        screen.fill((255,255,255))
        DrawText("SCORE: " + str(player.GetScore()), (0,0,0), (100,50), 32)
        DrawText("GOLD: " + str(player.GetGold()), (255,211,0), (100,200), 32)
        DrawText("WEIGHT: " + str(weight) + "/50", (0,0,0), (50,750), 24)
        DrawText("CONTINUE", (0,0,0), (537.5, 737.5), 24)
        pygame.draw.rect(screen, (0,0,0), (525,725,150,50), 4) #Continue button
        DrawInventory()
        DrawPlayerHB()
        screen.blit(player.surf, (100,450))
        screen.blit(shopKeeper.surf, (550, 400))
        
        
        #Draw the 3 random selected items...
        for i in range(3):
            if itemsInShop[i].GetItemGone() == False:
                screen.blit(itemsInShop[i].surf, (500 + i*75, 525))
            #And if an item is bought, draw a white rectangle
            else:
                pygame.draw.rect(screen, (255,255,255), (500 + i*75, 525, 75,75))
                
            #Write the price, quality and weight under each item
            DrawText("Price: " + str(itemsInShop[i].GetPrice()), (0,0,0),  (500 + i*75, 600), 12)
            if isinstance(itemsInShop[i], Weapon) == True:
                DrawText("Damage: " + str(itemsInShop[i].GetDamage()), (0,0,0),  (500 + i*75, 625), 12)
            elif isinstance(itemsInShop[i], Armor) == True:
                DrawText("Defense: " + str(itemsInShop[i].GetDefense()), (0,0,0),  (500 + i*75, 625), 12)
            elif isinstance(itemsInShop[i], Potion) == True:
                DrawText("Potion-", (0,0,0),  (500 + i*75, 625), 12)
                DrawText("Strenght: " + str(itemsInShop[i].GetPStrenght()), (0,0,0),  (500 + i*75, 650), 12)
            DrawText("Weight: " + str(itemsInShop[i].GetWeight()), (0,0,0),  (500 + i*75, 675), 12)
    
    #def DrawDeath()
    
    #def DrawStart()
    
        
    #Check how much extra damage the player should do
    def CalcDamage():
        extraDamage = 0
        for i in itemsOwned:
            if isinstance(i, Weapon) == True:
                extraDamage += i.GetDamage()
            elif isinstance(i, StrenghtPotion) == True:
                extraDamage += i.GetPStrenght()
        return extraDamage
    
    #Check how much defense the player has
    def CalcDefense():
        reducedDamage = 0
        for i in itemsOwned:
            if isinstance(i, Armor) == True:
                reducedDamage += i.GetDefense()
        return reducedDamage
            
            
            
            
            
    #------------------------------------Check for events---------------------------------------------------------------
    
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
            
                       
        # Did the user click the window close button or die, temporary solution for death. <=4 because of rect-borders
        if event.type == pygame.QUIT or player.hp <= 4:
            running = False
    
    
    #---------------------------------General Logic------------------------------------------------------------------------
    
    #The enemy attacks once every second while the fight is active
    time = round((pygame.time.get_ticks())/1000)
    reducedDamage = CalcDefense()
    if time - timer >=  0:
        if mode == "fight":
            player.TakeDamage(reducedDamage)
        timer += 1

    #If an enemy dies, give the player gold and score, and swap to the next enemy.
    if enemies[currEnemy].GetHp() <= 0:
        player.ChangeGold(10 + currEnemy * randint(2, 5))
        player.AddScore()
        currEnemy += 1
    
    #After every fourth enemy, select three different random items, that are not in inventory to show in the shop and enter shop mode
    if  currEnemy %4 == 0 and currEnemy > 0 and mode == "fight":
            itemsInShop = []
            
            while len(itemsInShop) < 3:
                itemRand = items[randint(0,(len(items)-1))]
                if itemRand not in itemsInShop and itemRand not in itemsOwned:
                    itemsInShop.append(itemRand)
            mode = "shop"
    
        
    #if player.hp <=0: mode = "dead"
    
    #Draw the current mode
    if mode == "fight":
        DrawFight()
    elif mode == "shop":
        DrawShop()
    #elif mode == "dead":
        #DrawDeath()
    #elif mode == "start":
        #DrawStart()
             
        
    
    
    # Uppdate frame with 60 frames per second.
    pygame.display.flip()
    clock.tick(60)

pygame.quit()