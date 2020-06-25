from models.imageConverter import ImageConverter
from models.flowerImage import FlowerImage
class Controller:

        imageConverter = ImageConverter()

        @staticmethod
        def loadImage(image, jsonData, filename, ext):
            Controller.imageConverter.addImage(image, jsonData, filename, ext)

        @staticmethod
        def deleteImage(position):
            Controller.imageConverter.deleteImage(position)

        @staticmethod
        def getListLoadedImages():
            return Controller.imageConverter.userImages

        @staticmethod
        def startProcess():
            Controller.imageConverter.convert()

        @staticmethod
        def getConvertProcess():
            return Controller.imageConverter.getConvertProcess()

        @staticmethod
        def isReadyToConvert():
            return Controller.imageConverter.isReadyToConvert()

        @staticmethod
        def getConvertProgress():
            return Controller.imageConverter.getProgress()