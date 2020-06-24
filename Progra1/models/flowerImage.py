import numpy as np
from models.flowerConfig import FlowerConfig

class FlowerImage:

    def __init__(self, flower, flowerPathFront, flowerImagePathBack, jsonData ,flowerDirectory, filename):
        self.__size_i = flower.shape[0]
        self.__size_j = flower.shape[1]
        self.__flower = flower
        self.__jsonData = jsonData
        self.__petal = np.full((self.__size_i, self.__size_j, 3), FlowerConfig.BACKGROUND_COLOR)
        self.__center = np.full((self.__size_i, self.__size_j, 3), FlowerConfig.BACKGROUND_COLOR)
        self.__flowerImagePathFront = flowerPathFront
        self.__flowerImagePathBack = flowerImagePathBack
        self.__flowerDirectory = flowerDirectory
        self.__flowerName = filename

    #Setter

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

    #Getter

    def getFlowerImagePathBack(self):
        return self.__flowerImagePathBack

    def getFlowerDirectory(self):
        return self.__flowerDirectory

    def getFlowerName(self):
        return self.__flowerName

    def getJsonData(self):
        return self.__jsonData

    def getSize_I(self):
        return self.__size_i

    def getSize_J(self):
        return self.__size_j

    #Numpy array images

    def getPetal(self):
        return self.__petal

    def getCenter(self):
        return self.__center

    def getFlower(self):
        return self.__flower


