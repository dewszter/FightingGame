
#Class for the items, with the attributes wight, price, image file name and the boolean itemGone
class Item():
    def __init__(self, weight, price, imgFile, itemGone):
        self.weight = weight
        self.price = price  
        self.imgFile = imgFile
        self.itemGone = itemGone
    
    #Get weight    
    def GetWeight(self):
        return self.weight
    
    #Get price
    def GetPrice(self):
        return self.price
    
    #Get Itemgone
    def GetItemGone(self):
        return self.itemGone
    
    #Set itemgone
    def SetItemGone(self, set):
        self.itemGone = set
        
    