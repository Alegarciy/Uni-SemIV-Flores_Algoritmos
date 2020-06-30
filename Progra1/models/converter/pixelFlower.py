


class PixelFlower:

    def __init__(self, rgb, idealDiferences, position):
        self.__rgb = rgb
        self.idealDiference = idealDiferences
        self.__position = position
        self.__quantity = 1

    #Functions

    def incrementQuantity(self):
        self.__quantity += 1

    # Setter



    # Getter

    def getRGB(self):
        return self.__rgb 
    
    def getIdealDiference(self):
        return self.idealDiference
   
    def getPosition(self):
        return self.__position

    def getQuantity(self):
        return self.__quantity