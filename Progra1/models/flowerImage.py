#import numpy as np

class FlowerImage:

    def __init__(self, flower, flowerPathFront, flowerImagePathBack, jsonData ,flowerDirectory, filename):
        self.__flower = flower
        self.__jsonData = jsonData
        self.__petal = None
        self.__center = None
        self.__flowerImagePathFront = flowerPathFront
        self.__flowerImagePathBack = flowerImagePathBack
        self.__flowerDirectory = flowerDirectory
        self.__flowerName = filename
        
    def setPetalImage(self, petalImage):
        self.__petalImage = petalImage
    
    def setCenterImage(self, centerImage):
        self.__centerImage = centerImage

    def setFlowerImage(self, flowerImage):
        self.__flowerImage = flowerImage

    def setJsonData(self, jsonData):
        self.__jsonData = jsonData

    def getFlowerImagePathFront(self):
        return self.__flowerImagePathFront

    def getFlowerImagePathBack(self):
        return self.__flowerImagePathBack

    #Getter

    def getFlowerDirectory(self):
        return self.__flowerDirectory

    def getFlowerName(self):
        return self.__flowerName


