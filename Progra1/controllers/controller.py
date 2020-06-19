from models.imageConverter import ImageConverter
from models.flowerImage import FlowerImage
class Controller:

        imageConverter = ImageConverter()

        @staticmethod
        def loadImage(image, jsonData):
            Controller.imageConverter.addImage(image, jsonData)

        @staticmethod
        def getListLoadedImages():
            return Controller.imageConverter.userImages