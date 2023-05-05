from Item import Item

class Weapon(Item):
    def __init__(self, damage, weight, price, imgFile, itemGone):
        super().__init__(weight, price, imgFile, itemGone)
        self.damage = damage
        
    def GetDamage(self):
        return self.damage
        
class Armor(Item):
    def __init__(self, defense, weight, price, imgFile, itemGone):
        super().__init__(weight, price, imgFile, itemGone)
        self.defense = defense

class Potion(Item):
    def __init__(self, pStrenght, weight, price, imgFile, itemGone):
        super().__init__(weight, price, imgFile, itemGone)
        self.pStrenght = pStrenght 
        