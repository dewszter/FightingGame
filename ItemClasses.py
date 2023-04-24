from Item import Item

class Weapon(Item):
    def __init__(self, damage, weight, price, imgFile):
        super().__init__(weight, price, imgFile)
        self.damage = damage
        
class Armor(Item):
    def __init__(self, defense, weight, price, imgFile):
        super().__init__(weight, price, imgFile)
        self.defense = defense

class Potion(Item):
    def __init__(self, pStrenght, weight, price, imgFile):
        super().__init__(weight, price, imgFile)
        self.pStrenght = pStrenght 
        