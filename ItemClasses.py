from Item import Item

class Weapon(Item):
    super(Item)
    def __init__(self, damage):
        self.damage = damage
        