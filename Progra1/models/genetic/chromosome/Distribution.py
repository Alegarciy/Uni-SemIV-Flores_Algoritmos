import math

class Distribution:
    def __init__(self):
        self.quantity = 0
        self.percentage = 0
        self.range = [0,0]
        self.totalBits = 0

    def add(self):
        self.quantity += 1

    def setQuantity(self, total):
        self.quantity = total

    def setPercentage(self, total):
        self.percentage = (self.quantity / total)*100

    def setRange(self, min):
        self.range[0] = min
        self.range[1] = math.floor(min + self.totalBits*(self.percentage/100) - 1)

    def setMaxRange(self, max):
        self.range[1] = max
        
    def setTotal(self, total):
        self.totalBits = total

    def getRangeMin(self):
        return self.range[0]

    def getRangeMax(self):
        return self.range[1]

    def getQuantity(self):
        return self.quantity

    def getPercentage(self):
        return self.percentage


    def print(self):
        print("[", self.getQuantity(), " ", "%",  self.getPercentage(), " (" , self.getRangeMin(), self.getRangeMax(), ")", "]")
