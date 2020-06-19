#import numpy as np

class FlowerImage:

    def __init__(self, flower, jsonData):
        self.__flower = flower
        self.__jsonData = jsonData
        self.__petal = None
        self.__center = None
        
    def setPetalImage(self, petalImage):
        self.__petalImage = petalImage
    
    def setCenterImage(self, centerImage):
        self.__centerImage = centerImage

    def setFlowerImage(self, flowerImage):
        self.__flowerImage = flowerImage

    def setJsonData(self, jsonData):
        self.__jsonData = jsonData


