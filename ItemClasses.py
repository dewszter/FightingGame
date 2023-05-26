from Item import Item

#Class for weapon which is a subclass to item, with the unique attribute damage
class Weapon(Item):
    def __init__(self, damage, weight, price, imgFile, itemGone):
        super().__init__(weight, price, imgFile, itemGone)
        self.damage = damage
     
    #Get damage    
    def GetDamage(self):
        return self.damage
    
#Class for armor which is a subclass to item, with the unique attribute defense       
class Armor(Item):
    def __init__(self, defense, weight, price, imgFile, itemGone):
        super().__init__(weight, price, imgFile, itemGone)
        self.defense = defense
    
    #Get defense
    def GetDefense(self):
        return self.defense

#Class for potion which is a subclass to item, with the unique attribute potion strenght
class Potion(Item):
    def __init__(self, pStrenght, weight, price, imgFile, itemGone):
        super().__init__(weight, price, imgFile, itemGone)
        self.pStrenght = pStrenght
        
    #Get potion strenght 
    def GetPStrenght(self):
        return self.pStrenght    