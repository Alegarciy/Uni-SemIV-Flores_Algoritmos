class Distribution:
    def __init__(self):
        self.quantity = 0
        self.percentage = 0
        self.range = [0,0]

    def add(self):
        self.quantity += 1

    def setPercentage(self, total):
        self.percentage = (self.quantity / total)*100

    def setRange(self, total, min):
        self.range[0] = min
        self.range[1] = min + total*(self.percentage/100) - 1

    def getRangeMin(self):
        return self.range[0]

    def getRangeMax(self):
        return self.range[1]

    def getQuantity(self):
        return self.quantity

    def getPercentage(self):
        return self.percentage
