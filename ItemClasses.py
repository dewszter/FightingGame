from Item import Item

class Weapon(Item):
    def __init__(self, damage, weight, price):
        super().__init__(weight, price)
        self.damage = damage
        
class Armor(Item):
    def __init__(self, defense, weight, price):
        super().__init__(weight, price)
        self.defense = defense

class Potion(Item):
    def __init__(self, pStrenght, weight, price):
        super().__init__(weight, price)
        self.pStrenght = pStrenght 
        