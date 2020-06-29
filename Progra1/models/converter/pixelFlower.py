


class PixelFlower:

    def __init__(self, rgb, idealDiferences, position):
        self.__rgb = rgb
        self.idealDiference = idealDiferences
        self.__position = position


    # Getter

    def getRGB(self):
        return self.__rgb 
    
    def getIdealDiference(self):
        return self.idealDiference
   
    def getPosition(self):
        return self.__position