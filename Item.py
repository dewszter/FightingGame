class Item():
    def __init__(self, weight, price, imgFile, itemGone):
        self.weight = weight
        self.price = price  
        self.imgFile = imgFile
        self.itemGone = itemGone
        
    def GetWeight(self):
        return self.weight
    def GetPrice(self):
        return self.price
    def GetItemGone(self):
        return self.itemGone
    def SetItemGone(self, set):
        self.itemGone = set
        
    